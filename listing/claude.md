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
| Privacy policy | | `https://gomnee.com/privacy` (needs the update below) |
| Terms | | `https://gomnee.com/terms` |
| Documentation | public by publish date | pending: no page yet |
| Support contact | | pending: no page yet |
| Icon | | `plugins/gomnee/assets/icon.png` |

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

Requires a Gomnee account with a workspace connected to Google Search Console. You choose the permissions Claude may use when you sign in, and you can revoke them at any time.

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
| No collection of the conversation | Gomnee receives tool requests and the proposals written, not the chat | Matches the privacy policy update |
| Public documentation | Pending | The documentation page exists |

### Screenshots of the review card

Three to five PNG images, at least 1,000 pixels wide, cropped to the card, each with the request that produced it. They can only be taken in a real Claude install with a pending proposal. Not taken yet.

## Plugin listing

| Field | Value |
| --- | --- |
| Name | `gomnee` (permanent once listed) |
| Repository | `fedewedreamlabsio/gomnee-plugins`: private during review, public before the listing goes live |
| Paired connector | The connector listing above, same server address |
| Validator | `claude plugin validate ./plugins/gomnee --profile directory` reports nothing at 0.2.0 |

## Open before submitting

| Item | Owner |
| --- | --- |
| Documentation page and support contact on gomnee.com | Marketing site |
| Privacy policy update for the connection | Marketing site, approved by the owner |
| Reviewer account and demo workspace (see [reviewer.md](reviewer.md)) | Owner |
| One full run of the skills in a real Claude install | Owner |
| Screenshots of the review card | After the install |
| Check whether the portal accepts the client ID in `plugins/gomnee/.mcp.json`, or wants the address only | Plugin |
| Every permission the server lists is assigned to Claude's clients | Owner, in the sign-in provider |
| The server's tool set has settled (old tools removed, inspiration tools renamed) | Server |
| Decision to list while Gomnee is invite-only | Owner |
