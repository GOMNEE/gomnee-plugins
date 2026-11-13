---
name: gomnee-start
description: Help a founder or marketer get oriented in their Gomnee workspace and choose a useful next action. Use for "help me grow my website", "what should I publish next", "where do I start", "what needs my attention", a general Gomnee question or pasted workspace link, or an explicit request to reschedule, unschedule, cancel, archive or restore saved content. Route specific Article writing, campaign website hosting and site audits to their focused skills.
---

# Choose the next Gomnee action

Help the person move from their goal to one useful action grounded in their
saved workspace. Keep the conversation in their language. Explain Gomnee's
terms only when needed: a Demand is a reader's need; an Asset is an accepted
content item intended to meet it.

Discover the Gomnee tools exposed by this connection. Their current definitions
and returned guidance control inputs, effects and next actions; this skill does
not make a missing tool available. Use the
[MCP workflow](../../references/mcp-workflow.md) for connection limits, review,
retries or interrupted work. You supply the analysis and proposals; do not assume
an external request can run Gomnee's native writer. Named decisions may be
requested only through advertised policy capabilities with their separate consents.

## Find the right entry point

For campaign creation, hosting, preview, website updates or restore, use the
`gomnee-campaign-site` skill and its currently advertised hosting tools. Website
publication is an explicit exact-deployment Owner command with separate consent;
Article approval settings do not grant this authority. If hosting tools are
absent, report that the external hosting surface is not activated.

For supporting-site traffic, use advertised `gomnee_get_website_network` and
`gomnee_get_website_network_activity` reads when available. They need
the server-advertised measurement permission, independent of Article/Strategy consent. The network
read supplies public verification files, current pixel setup and immutable
tagged links; installation uses the person's existing authorized coding and
deployment tools. Registration, verification and collection remain explicit Owner commands in
Sites or the separately consented hosting tools. Deletion remains in Sites. Distinguish declared sources, enabled collection and
actually received events. Tagged arrivals and source clicks are independent
observations; a copied link is not proof of its original source. Never infer
matched people, visitors, conversions, revenue or causal impact.

1. Use a known workspace or discover it with `gomnee_list_workspaces`. Match
   the returned customer-visible name or exact Gomnee link. When one workspace
   matches, proceed and name it; ask the person to choose when ambiguous.
   Never guess IDs, borrow another workspace or invent accepted state.
2. Route a specific writing/editing request to the Article skill and a site
   audit to the audit skill. A pasted Article link identifies work to inspect,
   not authority to apply or publish it. For a saved proposal link, read
   `gomnee_get_proposal_status` first and follow its durable decision.
   For a status or attention question, use the advertised workspace Overview
   read when available. It supplies saved reviews, running work and recovery
   links; it does not itself approve work or start a job.
3. For a general growth or next-content question, read
   the advertised compact task context when available, or
   `gomnee_get_strategy_context`, and relevant `gomnee_list_strategy_demands` to understand
   the accepted company, current Strategy and reader needs. Read the selected
   Demand with `gomnee_get_strategy_demand_context` only when it helps choose
   the next step. Respect returned readiness, blockers and exact links.
4. Choose further evidence for the question. For site performance, use
   `gomnee_query_search_console`; keep coverage, date range and snapshot visible.
   For market estimates, use `gomnee_list_saved_research` and
   `gomnee_read_saved_research` with `includeProvenance: true` when the
   advertised input supports it; preserve market, provider, collection date,
   missing metrics and limits. Read existing evidence before recommending a new
   collection. Empty search data is not proof that nobody wants the topic.
5. To continue accepted work, use `gomnee_list_articles` and its returned
   Articles and Assets. Resume an existing Article directly. If planning is the
   next step, read `gomnee_get_planner_context` and honor eligibility and saved
   evidence. A published target should not become a duplicate new allocation.
   `pendingProposals` lists the topics of Plan proposals awaiting review: do
   not propose those again, and read one with `gomnee_get_proposal_status`
   when you need its decision. Accepted Assets alone do not describe the
   pending review queue. Follow the saved review or decision.
   For a Planner proposal, copy its exact allocation and supplied references.
   Cite publication performance only when its recommendation is `follow_up_asset`
   and the proposed Asset belongs to that snapshot's Demand. A snapshot awaiting
   data is not that signal; omit its citation while considering existing work.

For deeper research interpretation, Strategy changes or a content-plan proposal,
load [research-and-planning.md](references/research-and-planning.md). Use only
the operations exposed in the connected catalog. If a needed operation is absent,
give the exact returned Gomnee action and explain what the connection cannot do.

Read only what the next decision needs. Do not fetch every workspace surface
or present a generic SEO checklist before understanding the person's goal.

## Manage an existing item

For an explicit archive, restore, reschedule, unschedule or cancel request,
use the compact lifecycle tools described in
[lifecycle-controls.md](../../references/lifecycle-controls.md). Discover the
exact item through the current catalog; `gomnee_list_articles` with
`includeArchived: true`, when advertised, includes retained archived work.
Read its lifecycle context, use the action matching the person's instruction,
and report the saved result. Management consent does not authorize content
approval or publication. If a control or scope is missing, follow the returned
reconnect or Gomnee action; never request credentials in chat.

## Make progress easy to recognize

Lead with the current state, its implication and one recommended next step.
For an open-ended request, offer two to four concrete choices grounded in the
returned state. For an explicit task, proceed within its authorized scope
without asking the person to choose it again.

Name the reason: the accepted reader need, useful company contribution, saved
search evidence or unfinished review. Separate observed data from your judgment.
Do not promise rankings, traffic or publication based on a proposal.
Empty or pre-publication Search Console data cannot establish that further
content or research would be useless. Explain why this next action is a good
use of effort given the accepted needs and current coverage, and keep uncertain
alternatives open.
Interpret numeric conventions only when supplied provider definitions or
primary documentation states them; do not invent a rounding floor. Judge
duplicate work by distinct reader tasks and current coverage. Existing topics
alone do not establish ranking competition or cannibalization.

If Gomnee names a prerequisite, explain it plainly and provide the exact
recovery link or discoverable reference. Pending business or Strategy decisions
stay in their existing human review path. Do not work around validation or
invent a parallel plan or onboarding shortcut.

## Finish and return

Read-only advice ends with the useful action, its reason and the exact returned
link to the selected work or recovery action. For existing Articles, the tool
description also supplies a browser-link template: fill it only with the
returned workspace slug and Article ID. Do not invent an origin or ID, or
prepare an Article merely to obtain a link. Do not make the person hunt through
navigation for an Article you already found. Changed Strategy,
Plan, brief or draft ends with its exact saved receipt. If it remains pending,
give the human review link; if applied under workspace settings, read fresh state
and continue only the already requested work. Follow
Gomnee's current tool guidance for the required form; skill prose does not
decide schema versions or grant authority.

On return, read the compact saved decision before loading the complete proposal
again. Request-changes feedback guides a fresh proposal. An applied brief allows
the already requested drafting work to continue after reading fresh context.
Application, Article approval and explicitly requested publication remain
separate decisions governed by saved owner settings and separate consents.
Read the MCP workflow reference for policy controls; never change them yourself.
