import json
import shutil
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from package import build_archive, collect_source, validate_official_schemas


class PortablePluginPackageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "plugin"
        shutil.copytree(Path(__file__).resolve().parents[1] / "plugins" / "gomnee", self.source)

    def mutate_json(self, relative, update):
        path = self.source / relative
        value = json.loads(path.read_text())
        update(value)
        path.write_text(json.dumps(value))

    def test_archive_is_deterministic_preserves_shared_bytes_and_excludes_other_source(self):
        (self.source / ".beads").mkdir()
        (self.source / ".beads/issues.jsonl").write_text("private tracker")
        (self.source / ".env.production").write_text("private configuration")
        (self.source / "product.ts").write_text("private product source")
        first = build_archive(self.source, self.root / "first.zip")
        second = build_archive(self.source, self.root / "second.zip")
        self.assertEqual(first["sha256"], second["sha256"])
        with ZipFile(first["archive"]) as archive:
            paths = archive.namelist()
            self.assertIn("skills/gomnee-start/SKILL.md", paths)
            self.assertIn("references/mcp-workflow.md", paths)
            self.assertIn("LICENSE", paths)
            self.assertIn("assets/icon.png", paths)
            self.assertNotIn("README.md", paths)
            self.assertNotIn(".mcp.json", paths)
            self.assertNotIn(".claude-plugin/plugin.json", paths)
            self.assertNotIn(".beads/issues.jsonl", paths)
            self.assertNotIn(".env.production", paths)
            self.assertNotIn("product.ts", paths)
            for name in paths:
                self.assertEqual(archive.read(name), (self.source / name).read_bytes())
        self.assertEqual(first["schemas"], [])
        self.assertEqual(first["missingForReview"], ["supportURL"])
        self.assertFalse(first["hostQualified"])
        self.assertFalse(first["published"])

    def test_rejects_hosted_package_with_loopback_oauth_configuration(self):
        self.mutate_json("mcp.json", lambda value: value["mcpServers"]["gomnee"].update(
            {"oauth": {"clientId": "loopback-client", "callbackPort": 5556}}
        ))
        with self.assertRaisesRegex(ValueError, "only the public HTTPS endpoint"):
            collect_source(self.source)

    def interface(self, update):
        self.mutate_json("plugin.json",
                         lambda value: update(value["extensions"]["com.openai"]["interface"]))

    def test_rejects_listing_text_over_the_directory_limit(self):
        self.interface(lambda value: value.update({"shortDescription": "x" * 31}))
        with self.assertRaisesRegex(ValueError, "over 30 characters: shortDescription"):
            collect_source(self.source)

    def test_rejects_listing_url_that_is_not_plain_https(self):
        self.interface(lambda value: value.update({"supportURL": "http://gomnee.com/support"}))
        with self.assertRaisesRegex(ValueError, "plain HTTPS: supportURL"):
            collect_source(self.source)

    def test_rejects_listing_icon_that_is_missing_or_not_square(self):
        self.interface(lambda value: value.update({"logo": "./assets/missing.png"}))
        with self.assertRaisesRegex(ValueError, "icon is not packaged: logo"):
            collect_source(self.source)
        self.interface(lambda value: value.update({"logo": "./assets/icon.png"}))
        icon = self.source / "assets/icon.png"
        data = bytearray(icon.read_bytes())
        data[16:20] = (512).to_bytes(4, "big")
        icon.write_bytes(bytes(data))
        with self.assertRaisesRegex(ValueError, "square PNG"):
            collect_source(self.source)

    def test_rejects_client_credentials_in_the_hosted_connection(self):
        self.mutate_json("mcp.json", lambda value: value["mcpServers"]["gomnee"]["extensions"][
            "com.openai"]["auth"]["client"].update({"clientId": "static-client"}))
        with self.assertRaisesRegex(ValueError, "only the public HTTPS endpoint"):
            collect_source(self.source)

    def test_rejects_claude_portable_version_drift(self):
        self.mutate_json(
            "plugin.json",
            lambda value: value.update({"version": value["version"] + "-drift"}),
        )
        with self.assertRaisesRegex(ValueError, "metadata differs: version"):
            collect_source(self.source)

    def test_rejects_reference_to_source_excluded_from_archive(self):
        path = self.source / "references/mcp-workflow.md"
        path.write_text(path.read_text() + "\n[Installation](../README.md)\n")
        with self.assertRaisesRegex(ValueError, "Reference is not packaged"):
            collect_source(self.source)

    def test_rejects_reference_escaping_plugin(self):
        path = self.source / "references/mcp-workflow.md"
        path.write_text(path.read_text() + "\n[Internal](../../AGENTS.md)\n")
        with self.assertRaisesRegex(ValueError, "Reference escapes plugin"):
            collect_source(self.source)

    def test_rejects_secret_shapes_in_an_allowed_markdown_path(self):
        path = self.source / "references/credentials.md"
        path.write_text("-----BEGIN PRIVATE KEY-----\nprivate key bytes\n")
        with self.assertRaisesRegex(ValueError, "Credential-shaped content excluded"):
            collect_source(self.source)

    def test_rejects_symlink_even_when_it_points_inside_plugin(self):
        (self.source / "references/linked.md").symlink_to("mcp-workflow.md")
        with self.assertRaisesRegex(ValueError, "Symlink excluded"):
            collect_source(self.source)

    def test_rejects_hidden_and_unreviewed_file_types_inside_shared_resources(self):
        for filename in (".env", "worker.ts"):
            with self.subTest(filename=filename):
                path = self.source / "references" / filename
                path.write_text("unreviewed source")
                with self.assertRaises(ValueError):
                    collect_source(self.source)
                path.unlink()

    def test_rejects_archive_written_inside_canonical_plugin_source(self):
        with self.assertRaisesRegex(ValueError, "outside the canonical plugin source"):
            build_archive(self.source, self.source / "archive.zip")

    def test_rejects_tampered_official_schema_before_optional_validator(self):
        (self.root / "plugin.schema.json").write_text('{"$id":"https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"}')
        files, _, _ = collect_source(self.source)
        with self.assertRaisesRegex(ValueError, "Official schema bytes differ"):
            validate_official_schemas(files, self.root)


if __name__ == "__main__":
    unittest.main()
