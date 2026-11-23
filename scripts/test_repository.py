import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "gomnee"


class RepositoryLayoutTests(unittest.TestCase):
    def test_marketplace_lists_the_plugin_at_its_folder(self):
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
        (entry,) = marketplace["plugins"]
        self.assertEqual(entry["name"], manifest["name"])
        self.assertEqual((ROOT / entry["source"]).resolve(), PLUGIN)

    def test_plugin_carries_the_repository_license(self):
        self.assertEqual((PLUGIN / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())
        manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
        self.assertEqual(manifest["license"], "Apache-2.0")

    def test_claude_manifest_has_only_keys_the_app_recognises(self):
        # The Claude app strips other top-level keys on sync and warns about each.
        # The directory finds the icon at assets/icon.png and the privacy policy
        # through the README's link, so neither needs a manifest key.
        manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
        self.assertLessEqual(set(manifest), {"name", "displayName", "version", "description",
                                             "author", "homepage", "repository", "license",
                                             "keywords"})
        self.assertTrue((PLUGIN / "assets/icon.png").is_file())
        self.assertIn("(https://gomnee.com/privacy)", (PLUGIN / "README.md").read_text())

    def test_plugin_readme_links_stay_inside_the_plugin(self):
        readme = (PLUGIN / "README.md").read_text()
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", readme):
            parts = urlsplit(target)
            if parts.scheme or not parts.path:
                self.assertEqual(parts.scheme, "https", target)
                continue
            resolved = (PLUGIN / unquote(parts.path)).resolve()
            self.assertTrue(resolved.is_relative_to(PLUGIN), target)
            self.assertTrue(resolved.exists(), target)


if __name__ == "__main__":
    unittest.main()
