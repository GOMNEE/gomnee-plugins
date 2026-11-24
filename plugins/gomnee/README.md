# Gomnee

Gomnee turns a company's business context, strategy, website evidence and Google Search Console data into planned, reviewed content. This plugin connects your assistant to your Gomnee workspaces and adds eight skills that guide the work from a first strategy to a reviewed article.

Your assistant does the thinking and writes proposals. Gomnee keeps the accepted state and records every decision. Nothing is approved or published unless you decide it, or your own approval settings do.

## What you need

- A Gomnee account with a workspace. Gomnee is invite-only at the moment.
- The workspace owner signs in when the plugin first connects.

## Skills

| Skill | What it does |
| --- | --- |
| `start` | Finds where your workspace stands and names the next step. On a new workspace it reviews your business map with you first. |
| `strategy` | Drafts what your brand wants to be known for (Territories) and the reader questions under them (Demands). |
| `research` | Researches keywords for those questions and checks what actually ranks for them. |
| `plan` | Turns the researched questions into planned content with titles, angles and target dates. |
| `article` | Takes a planned item through brief, draft, images and review, and edits existing articles. |
| `audit` | Audits a website for Gomnee readiness and SEO health, with evidence for every finding. |
| `campaign` | Builds a campaign page in your own repository and previews and publishes it through Gomnee hosting, where hosting is switched on. |
| `feedback` | Writes up a problem or a missing capability in Gomnee for you to email to `support@gomnee.com`. |

The usual order is start, strategy, research, plan, article. Ask in your own words, for example "Where do I begin with Gomnee?", "Research keywords for these questions" or "Write the next planned article".

## Install in Claude

In the Claude app: Customize, Plugins, Add marketplace, then enter `GOMNEE/gomnee-plugins` and install Gomnee.

In Claude Code:

```bash
claude plugin marketplace add GOMNEE/gomnee-plugins
claude plugin install gomnee@gomnee
```

The first Gomnee request opens the Gomnee sign-in page, where you choose the permissions the assistant may use. Installing or updating the plugin never grants a permission by itself.

To update, refresh the marketplace and the plugin in your plugin manager, then start a new conversation.

## Use another assistant

The Gomnee connection works without this plugin. In ChatGPT or another assistant that supports MCP, connect `https://app.gomnee.com/mcp` and sign in with your Gomnee account. The skills in this plugin install in Claude.

## What the plugin sends and fetches

- Every request to Gomnee is made with your own Gomnee account and limited to the workspaces and permissions you approve.
- **Reading saved work costs nothing.** Strategy, plans, articles, saved research and Search Console data are read from what Gomnee has stored.
- **New research uses your plan's research allowance.** It contacts a research provider, is always quoted first and is started only with your agreement.
- **Reading a public source** asks Gomnee to fetch that public page and keep the passages used as evidence.
- **Connected company sources** (GitHub or Notion, where you connected them) are read only for sources you selected. Private material stays private.
- **Hosting an image** makes that file public at once. The assistant asks you about rights and public use for each image first.
- **The site audit** reads public pages of the site you name and, in Claude Code, files in a repository you open. It changes nothing unless you ask for a specific change in your own repository.
- The plugin contains no scripts, hooks or tracking.

## Decisions stay with you

- Changes to your strategy, plan, briefs and drafts are saved as proposals. You review each one in Gomnee, or your approval settings apply it.
- Approving an article and publishing it are separate steps. The assistant does either only when you ask.
- Only the workspace owner changes approval settings, in Gomnee.

## Support

Documentation and contact: https://gomnee.com

- [Privacy policy](https://gomnee.com/privacy)
- [Terms of service](https://gomnee.com/terms)

## License

The plugin is released under the [Apache License 2.0](LICENSE). Third-party material is acknowledged in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
