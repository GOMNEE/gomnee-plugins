# Gomnee plugins

The Gomnee plugin for Claude and ChatGPT: journey skills plus the connection to the Gomnee MCP server at `https://app.gomnee.com/mcp`.

This repository holds exactly what ships. The Gomnee product and its MCP server live elsewhere, and skills are drafted elsewhere before they are promoted here.

## Install in Claude Code

```bash
claude plugin marketplace add GOMNEE/gomnee-plugins
claude plugin install gomnee@gomnee
```

The first Gomnee request opens the Gomnee sign-in and consent page. What the plugin does, sends and fetches is described in the [plugin README](plugins/gomnee/README.md).

## Layout

| Path | What it is |
| --- | --- |
| `plugins/gomnee/` | The plugin: skills, shared references, the Claude manifest (`.claude-plugin/plugin.json`, `.mcp.json`) and the portable manifest used for ChatGPT (`plugin.json`, `mcp.json`) |
| `plugins/gomnee/assets/icon.png` | The listing icon for both hosts |
| `.claude-plugin/marketplace.json` | The Claude marketplace entry that points at the plugin |
| `scripts/package.py` | Builds the ChatGPT archive from `plugins/gomnee/` |
| `listing/` | Drafted directory listing data and the reviewer account checklist. Nothing here is submitted |
| `contract/gomnee-server.json` | A copy of the server's contract: the tool names it can register and the Article house targets |
| `scripts/test_*.py` | Checks for the archive, this repository's layout and the skill text against the server contract |

The skills and references are one source for both hosts. Only the manifests differ.

## Build and check

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/package.py --output dist/gomnee.zip --receipt dist/gomnee.receipt.json
claude plugin validate ./plugins/gomnee --profile directory
```

The archive is reproducible: the same source gives the same bytes. It contains the portable manifests, the license, the third-party notices, the icon and the skill and reference Markdown. The build checks the ChatGPT listing fields against the directory's limits, and its receipt lists under `missingForReview` any listing URL a review still needs. It leaves out the Claude-only connection settings. The build makes no network request and submits nothing.

## Staying in step with the server

Skills may only name tools the Gomnee server provides, and the house targets they quote must equal the server's. `contract/gomnee-server.json` is a copy of `apps/web/tests/unit/plugin-contract.json` from the Gomnee product repository. When that file changes there, replace the copy here and fix any skill the tests report.

## Releasing a change

1. Change the plugin under `plugins/gomnee/`.
2. Raise `version` in both `plugins/gomnee/.claude-plugin/plugin.json` and `plugins/gomnee/plugin.json`. The build fails if they differ.
3. Run the three commands above.
4. Tag the commit. The ChatGPT archive is built from that tag.

Installing or updating the plugin never grants a permission. Each person connects Gomnee and approves its permissions in their own host.

## License

[Apache License 2.0](LICENSE). Material adapted from other projects is listed in [`plugins/gomnee/THIRD_PARTY_NOTICES.md`](plugins/gomnee/THIRD_PARTY_NOTICES.md).
