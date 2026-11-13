# Gomnee plugins

The Gomnee plugin for Claude and ChatGPT: journey skills plus the connection to the Gomnee MCP server at `https://app.gomnee.com/mcp`.

This repository holds exactly what ships. The Gomnee product and its MCP server live elsewhere, and skills are drafted elsewhere before they are promoted here.

## Install in Claude Code

```bash
claude plugin marketplace add fedewedreamlabsio/gomnee-plugins
claude plugin install gomnee@gomnee
```

The first Gomnee request opens the Gomnee sign-in and consent page. What the plugin does, sends and fetches is described in the [plugin README](plugins/gomnee/README.md).

## Layout

| Path | What it is |
| --- | --- |
| `plugins/gomnee/` | The plugin: skills, shared references, the Claude manifest (`.claude-plugin/plugin.json`, `.mcp.json`) and the portable manifest used for ChatGPT (`plugin.json`, `mcp.json`) |
| `.claude-plugin/marketplace.json` | The Claude marketplace entry that points at the plugin |
| `scripts/package.py` | Builds the ChatGPT archive from `plugins/gomnee/` |
| `scripts/test_*.py` | Checks for the archive and for this repository's layout |

The skills and references are one source for both hosts. Only the manifests differ.

## Build and check

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/package.py --output dist/gomnee.zip --receipt dist/gomnee.receipt.json
claude plugin validate ./plugins/gomnee --profile directory
```

The archive is reproducible: the same source gives the same bytes. It contains the portable manifests, the license, the third-party notices and the skill and reference Markdown. It leaves out the Claude-only connection settings. The build makes no network request and submits nothing.

## Releasing a change

1. Change the plugin under `plugins/gomnee/`.
2. Raise `version` in both `plugins/gomnee/.claude-plugin/plugin.json` and `plugins/gomnee/plugin.json`. The build fails if they differ.
3. Run the three commands above.
4. Tag the commit. The ChatGPT archive is built from that tag.

Installing or updating the plugin never grants a permission. Each person connects Gomnee and approves its permissions in their own host.

## License

[Apache License 2.0](LICENSE). Material adapted from other projects is listed in [`plugins/gomnee/THIRD_PARTY_NOTICES.md`](plugins/gomnee/THIRD_PARTY_NOTICES.md).
