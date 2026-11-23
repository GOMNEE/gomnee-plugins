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
ONBOARDING_SKILL = "./skills/start/SKILL.md"
MCP_AUTH = {"type": "oauth", "client": {"mode": "cimd"}}
# Listing limits from OpenAI's submission reference (manifest fields, listing metadata).
CATEGORIES = ("Productivity", "Creativity", "Developer Tools", "Business & Operations",
              "Data & Analytics", "Communication", "Education & Research", "Security",
              "Finance", "Healthcare", "Travel", "Entertainment", "Other")
TEXT_LIMITS = {"displayName": 30, "shortDescription": 30, "longDescription": 4000,
               "developerName": 80}
URL_FIELDS = ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL")
ICON_FIELDS = ("composerIcon", "logo")
INTERFACE_FIELDS = {*TEXT_LIMITS, "category", *URL_FIELDS, "defaultPrompt", "brandColor",
                    *ICON_FIELDS}
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


def png_size(data, relative):
    require(data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR",
            f"Icon is not a PNG: {relative}")
    return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")


def check_listing(extension, files):
    require(set(extension) == {"interface", "onboardingSkill"},
            "Unreviewed host extension")
    require(extension["onboardingSkill"] == ONBOARDING_SKILL, "Unreviewed onboarding skill")
    require(ONBOARDING_SKILL[2:] in files, "Onboarding skill is not packaged")
    interface = extension["interface"]
    require(set(interface) <= INTERFACE_FIELDS, "Unreviewed listing field")
    for field, limit in TEXT_LIMITS.items():
        value = interface.get(field)
        require(isinstance(value, str) and 0 < len(value) <= limit,
                f"Listing text missing or over {limit} characters: {field}")
    require(interface.get("category") in CATEGORIES, "Unknown listing category")
    for field in URL_FIELDS:
        if field in interface:
            url = urlsplit(interface[field])
            require(url.scheme == "https" and url.netloc and "@" not in url.netloc,
                    f"Listing URL must be plain HTTPS: {field}")
    prompts = interface.get("defaultPrompt", [])
    require(isinstance(prompts, list) and len(prompts) <= 3 and len(set(prompts)) == len(prompts)
            and all(isinstance(prompt, str) and 0 < len(prompt) <= 128 and "@" not in prompt
                    for prompt in prompts),
            "Starter prompts must be at most three unique strings of 128 characters")
    if "brandColor" in interface:
        require(re.fullmatch(r"#[0-9A-Fa-f]{6}", interface["brandColor"]) is not None,
                "Brand color must be #RRGGBB")
    for field in ICON_FIELDS:
        path = interface.get(field)
        require(isinstance(path, str) and path.startswith("./assets/") and path[2:] in files,
                f"Listing icon is not packaged: {field}")
        width, height = png_size(files[path[2:]], path)
        require(width == height and 48 <= width <= 4096 and len(files[path[2:]]) <= 5 * 1024 * 1024,
                f"Listing icon must be a square PNG of 48 to 4096 pixels: {field}")
    # Each of these is required before an MCP review; a missing one is reported, not refused,
    # so the archive can be built while the page it points to is being prepared.
    return [field for field in URL_FIELDS if field not in interface]


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
    assets = root / "assets"
    if assets.exists():
        require(assets.is_dir() and not assets.is_symlink(), "Unexpected assets entry")
        for source in sorted(assets.iterdir()):
            relative = source.relative_to(root).as_posix()
            require(source.is_file() and not source.is_symlink() and source.suffix == ".png"
                    and not source.name.startswith("."), f"Unreviewed asset: {relative}")
            files[relative] = source.read_bytes()

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
    require(set(manifest["extensions"]) == {"com.openai"}, "Unreviewed host extension")
    missing_listing = check_listing(manifest["extensions"]["com.openai"], files)
    connector = json.loads(files["mcp.json"])
    require(connector == {"$schema": MCP_SCHEMA, "mcpServers": {"gomnee": {
        "type": "streamable-http", "url": MCP_URL,
        "extensions": {"com.openai": {"auth": MCP_AUTH}}}}},
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
    return dict(sorted(files.items())), manifest, missing_listing


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
    files, manifest, missing_listing = collect_source(plugin_root)
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
        "missingForReview": missing_listing,
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
