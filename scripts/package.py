"""Build the portable Gomnee plugin archive from plugins/gomnee.

This command performs no network access, host installation or publication.
Use --schema-directory to additionally validate against downloaded official
Agent Plugins schemas with the optional jsonschema Python package.
"""

import argparse
import hashlib
import json
import re
import stat
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZIP_STORED, ZipFile, ZipInfo


PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
MCP_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
MCP_URL = "https://app.gomnee.com/mcp"
SCHEMA_DIGESTS = {
    "plugin.schema.json": "0a4aad95ce337878ad38802ebf0daa3fde76abe3f65400c86bcbb1ec0b3ab883",
    "mcp.schema.json": "6539175bfcdf43085855183e86da40ea94b166547a72b47ae9a0a390516d3acb",
}
ROOT_FILES = ("plugin.json", "mcp.json", "LICENSE", "THIRD_PARTY_NOTICES.md")
SHARED_DIRECTORIES = ("skills", "references")
IDENTITY_FIELDS = ("name", "version", "description", "author", "homepage", "repository",
                   "license", "keywords")
SECRET_PATTERNS = (
    rb"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
    rb"\b(?:ghp_|github_pat_|xox[baprs]-|sk-proj-)[A-Za-z0-9_-]{20,}",
    rb"\bAKIA[A-Z0-9]{16}\b",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_source(root, relative):
    path = root / relative
    require(not path.is_symlink(), f"Symlink excluded: {relative}")
    require(path.resolve().is_relative_to(root), f"Escaping source: {relative}")
    require(path.is_file(), f"Missing source file: {relative}")
    data = path.read_bytes()
    require(
        not any(re.search(pattern, data) for pattern in SECRET_PATTERNS),
        f"Credential-shaped content excluded: {relative}",
    )
    return data


def collect_source(plugin_root):
    root = Path(plugin_root).resolve()
    files = {name: read_source(root, name) for name in ROOT_FILES}
    for directory in SHARED_DIRECTORIES:
        base = root / directory
        require(base.is_dir() and not base.is_symlink(), f"Missing shared directory: {directory}")
        for source in sorted(base.rglob("*")):
            relative = source.relative_to(root).as_posix()
            require(not source.is_symlink(), f"Symlink excluded: {relative}")
            require(not any(part.startswith(".") for part in source.relative_to(base).parts),
                    f"Hidden shared source excluded: {relative}")
            if source.is_dir():
                continue
            require(source.suffix == ".md", f"Unreviewed shared file type: {relative}")
            files[relative] = read_source(root, relative)

    manifest = json.loads(files["plugin.json"])
    claude = json.loads(read_source(root, ".claude-plugin/plugin.json"))
    require(set(manifest) == {"$schema", *IDENTITY_FIELDS, "extensions"},
            "Portable manifest must keep the reviewed minimal field set")
    require(manifest["$schema"] == PLUGIN_SCHEMA, "Unexpected portable manifest schema")
    for field in IDENTITY_FIELDS:
        require(manifest[field] == claude[field], f"Claude/portable metadata differs: {field}")
    require(manifest["name"] == "gomnee", "Unexpected plugin identity")
    require(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]) is not None,
            "Plugin version must be explicit semantic version")
    onboarding = "./skills/gomnee-start/SKILL.md"
    require(manifest["extensions"] == {"com.openai": {"onboardingSkill": onboarding}},
            "Unreviewed host extension or onboarding skill")
    require(onboarding[2:] in files, "Onboarding skill is not packaged")
    connector = json.loads(files["mcp.json"])
    require(connector == {"$schema": MCP_SCHEMA,
                          "mcpServers": {"gomnee": {"type": "streamable-http", "url": MCP_URL}}},
            "Portable MCP must contain only the public HTTPS endpoint and transport")

    skills = sorted((root / "skills").iterdir())
    require(bool(skills), "No skills packaged")
    for skill in skills:
        require(skill.is_dir(), f"Unexpected skill entry: {skill.name}")
        skill_file = f"skills/{skill.name}/SKILL.md"
        require(skill_file in files, f"Missing skill instructions: {skill.name}")
        content = files[skill_file].decode("utf-8")
        frontmatter = re.match(r"\A---\n([\s\S]*?)\n---\n", content)
        require(frontmatter is not None, f"Missing skill frontmatter: {skill.name}")
        require(re.search(rf"^name: {re.escape(skill.name)}$", frontmatter[1], re.M) is not None,
                f"Skill name differs from folder: {skill.name}")
        require(re.search(r"^description: \S.+$", frontmatter[1], re.M) is not None,
                f"Missing skill description: {skill.name}")

    for relative, data in files.items():
        if not relative.endswith(".md"):
            continue
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", data.decode("utf-8")):
            target_path = urlsplit(target).path
            if urlsplit(target).scheme or not target_path:
                continue
            require(not target.startswith("//"), f"Unreviewed network reference in {relative}")
            resolved = (root / relative).parent / unquote(target_path)
            require(resolved.resolve().is_relative_to(root),
                    f"Reference escapes plugin: {relative}")
            target_relative = resolved.resolve().relative_to(root).as_posix()
            require(target_relative in files, f"Reference is not packaged: {relative}: {target}")
    return dict(sorted(files.items())), manifest


def validate_official_schemas(files, schema_directory):
    receipts = []
    schemas = []
    for filename, expected_id in (("plugin.schema.json", PLUGIN_SCHEMA), ("mcp.schema.json", MCP_SCHEMA)):
        schema_data = (Path(schema_directory) / filename).read_bytes()
        digest = hashlib.sha256(schema_data).hexdigest()
        require(digest == SCHEMA_DIGESTS[filename], f"Official schema bytes differ: {filename}")
        schema = json.loads(schema_data)
        require(schema.get("$id") == expected_id, f"Unexpected official schema identity: {filename}")
        schemas.append((filename, schema))
        receipts.append({"url": expected_id, "sha256": digest})
    try:
        from jsonschema import Draft202012Validator
    except ImportError as error:
        raise ValueError("Official schema validation requires the jsonschema Python package") from error
    for filename, schema in schemas:
        Draft202012Validator.check_schema(schema)
        source_filename = filename.replace(".schema", "")
        Draft202012Validator(schema).validate(json.loads(files[source_filename]))
    return receipts


def build_archive(plugin_root, output, schema_directory=None):
    files, manifest = collect_source(plugin_root)
    schemas = validate_official_schemas(files, schema_directory) if schema_directory else []
    output = Path(output).resolve()
    require(not output.is_relative_to(Path(plugin_root).resolve()),
            "Archive must be written outside the canonical plugin source")
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_STORED) as archive:
        for relative, data in files.items():
            info = ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.compress_type = ZIP_STORED
            archive.writestr(info, data)
    with ZipFile(output) as archive:
        require(archive.namelist() == list(files), "Archive manifest changed")
        require(all(archive.read(name) == data for name, data in files.items()),
                "Archive source bytes changed")
    return {
        "name": manifest["name"],
        "version": manifest["version"],
        "archive": str(output),
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "bytes": output.stat().st_size,
        "schemas": schemas,
        "files": [{"path": name, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
                  for name, data in files.items()],
        "hostQualified": False,
        "submitted": False,
        "published": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin-root", type=Path,
                        default=Path(__file__).resolve().parents[1] / "plugins" / "gomnee")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--schema-directory", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    receipt = build_archive(args.plugin_root, args.output, args.schema_directory)
    serialized = json.dumps(receipt, indent=2) + "\n"
    if args.receipt:
        require(args.receipt.resolve() != args.output.resolve(), "Receipt cannot overwrite archive")
        require(not args.receipt.resolve().is_relative_to(args.plugin_root.resolve()),
                "Receipt must be written outside the canonical plugin source")
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
