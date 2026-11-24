# Claude directory listing: preparation

Status: **not submitted.** This file holds the drafted listing data so that submission is a matter of copying it into Anthropic's portal (`claude.ai/directory/manage`). Requirements are as read from Anthropic's documentation on 2026-11-12; check them again before submitting.

A plugin that brings a sign-in connection is listed as two paired entries with the same server address and the same organisation: the **connector** (the Gomnee server) and the **plugin** (the skills).

## Connector listing

| Field | Limit | Draft |
| --- | --- | --- |
| Name | 100 characters | Gomnee |
| One-line description | 200 characters | Plan and write search content from your own strategy: review your business map, research keywords, plan articles and take them from brief to review, with every decision left to you. |
| Server address | | `https://app.gomnee.com/mcp` |
| Categories | 1 to 5 | Marketing; Content; SEO (choose from the portal's list) |
| Privacy policy | | `https://gomnee.com/privacy`, with the section "AI assistants connected to Gomnee" at `#ai-assistants`. Live, effective 2026-11-23 |
| Terms | | `https://gomnee.com/terms`, with the section "Using Gomnee through an AI assistant". Live, effective 2026-11-23 |
| Documentation | public by publish date | `https://gomnee.com/docs/assistants`. Live and open without sign-in, but unlisted for now (see below) |
| Support contact | | `support@gomnee.com`, page `https://gomnee.com/support`; security reports to `security@gomnee.com` and `https://gomnee.com/.well-known/security.txt`. Live, unlisted for now |
| Icon | | `plugins/gomnee/assets/icon.png` |

The site pages were checked from outside on 2026-11-24: each address answers, the documentation and support pages carry "noindex", and neither is in the sitemap or linked from the homepage. They become listed when the marketing site's `ASSISTANT_PAGES_LISTED` switch is turned on.

### Description (2,000 characters at most)

Gomnee is an organic-growth workspace for founders and marketing teams. It keeps your business map, your content strategy, your Google Search Console data and your saved research in one place, and turns them into planned, reviewed articles.

With Gomnee connected, Claude can read your strategy, plan, articles and saved research, and write proposals: a new strategy direction, keywords linked to a reader question, a content plan, an article brief or a draft. You review each proposal in Gomnee or in a review card inside Claude. Nothing changes until you decide, unless you have set that kind of decision to apply automatically in your own Gomnee settings.

What you can ask for:

- Where your workspace stands and what to do next.
- A review of your business map against your live site.
- Keyword research for the questions your readers ask, and a check of what actually ranks.
- A content plan with titles, angles and target dates.
- A brief, a complete draft, images and fixes for review findings on an article.
- An audit of your site for publishing readiness and SEO health.

Approving an article and publishing it are separate steps that Claude takes only when you ask, each under its own permission. New research uses your plan's research allowance and is always quoted first.

Requires a Gomnee account with a workspace connected to Google Search Console. You choose the permissions Claude may use when you sign in, and you can disconnect at any time.

### Example requests (at least three working ones are required)

| Request | What happens | Tools it uses |
| --- | --- | --- |
| "Where do I begin with Gomnee?" | Finds the workspace, reads its state and names one next step. On a new workspace it reviews the business map first. | `gomnee_list_workspaces`, `gomnee_get_workspace_visibility`, `gomnee_read_strategy` |
| "What does Search Console say about my site this month?" | Reads saved search data by query and page and summarises what Google associates the site with. | `gomnee_query_search_console` |
| "What should we publish next?" | Reads the plan and the articles and recommends the next item with its reason. | `gomnee_read_plan`, `gomnee_list_articles` |
| "Tighten the opening of this article." | Reads the article and proposes a change to the opening only, for review. | `gomnee_read_article`, `gomnee_propose_article_edit` |
| "Research keywords for my strategy." | Reads saved research, quotes a collection and starts it only after agreement. | `gomnee_list_saved_research`, `gomnee_quote_research_collection` |

### Compliance statements the portal asks for

Each line is Gomnee's position as understood today. The owner confirms each before submitting.

| Statement | Position | To confirm |
| --- | --- | --- |
| Follows the directory policy | Intended | Read the current policy once more before submitting |
| Uses only our own API | The server is Gomnee's own. Research tools reach public pages and search results through Gomnee's research providers | Whether the policy's wording on third-party domains covers this |
| No money transfers | None. Research uses the plan's allowance; nothing is bought or transferred in Claude | |
| No AI image, video or audio generation | Cover rendering fills a saved template; it does not generate images | That no listed tool generates media |
| Protection against injected instructions | Tool results mark source text as evidence, never instructions, and writes are proposals a person decides | |
| No collection of the conversation | Gomnee receives tool requests and the proposals written, not the chat | The live privacy policy says the same: "Gomnee does not receive or collect your conversation with the assistant." |
| Public documentation | Live at `https://gomnee.com/docs/assistants` since 2026-11-24 | Whether reviewers need the page listed and indexed, or only reachable |

### Screenshots of the review card

Three to five PNG images, at least 1,000 pixels wide, cropped to the card, each with the request that produced it. They can only be taken in a real Claude install with a pending proposal. Not taken yet.

## Plugin listing

| Field | Value |
| --- | --- |
| Name | `gomnee` (permanent once listed) |
| Repository | `fedewedreamlabsio/gomnee-plugins`: private during review, public before the listing goes live |
| Paired connector | The connector listing above, same server address |
| Validator | `claude plugin validate ./plugins/gomnee --profile directory` passes at 0.2.7. It notes that it takes the privacy policy address from the README: the Claude app rejects that key in the manifest, so it is left out |

## Done

| Item | When |
| --- | --- |
| Documentation, support, privacy and terms pages are live on gomnee.com. Checked from outside | 2026-11-24 |
| Privacy and terms wording approved, and both mailboxes confirmed as live, by the owner. Recorded in the marketing site's pull request 23, not checked from here | 2026-11-23 |
| The support page is in the ChatGPT listing data (`supportURL` in `plugins/gomnee/plugin.json`); the build reports no missing listing link | 2026-11-24 |
| The server's tool set is settled for now: 131 tools on production, none with a version number in its name. The server session has paused further tool-list changes | 2026-11-23 |

## Open before submitting

| Item | Owner |
| --- | --- |
| Turn on the marketing site's listing switch for the documentation and support pages | Owner, at go-live |
| Reviewer account and demo workspace (see [reviewer.md](reviewer.md)) | Owner |
| One full run of the skills in a real Claude install | Owner |
| Screenshots of the review card | After the install |
| Check whether the portal accepts the client ID in `plugins/gomnee/.mcp.json`, or wants the address only. It did not stop a privately added plugin from connecting in the Claude app on 2026-11-23 | Plugin |
| Every permission the server lists is assigned to Claude's clients. A fresh plugin install signed in and listed workspaces on 2026-11-23, which points that way for the Claude app; not checked permission by permission, and not for Claude Code | Owner, in the sign-in provider |
| Confirm each compliance statement above | Owner |
| Decision to list while Gomnee is invite-only | Owner |

## Known later changes

The server session plans two more tool changes after its pause, each announced first: removing the version input the connected-source tools still accept, and moving the remaining tools onto shared definitions. After any change, copy the server's contract into `contract/gomnee-server.json`; the checks then report any tool a skill or this folder still names. Once listed, a changed tool name also needs a reviewed listing edit.
