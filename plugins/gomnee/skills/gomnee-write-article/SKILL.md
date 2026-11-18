---
name: gomnee-write-article
description: Write, edit or continue an Article in Gomnee. Use for a planned article, brief, complete draft, a small change to an existing blog post, or a saved proposal waiting for review. Route from the saved Article state, preserve accepted work, and follow saved owner approval controls for each exact decision.
---

# Write a Gomnee Article

## Edit an imported old CMS article

First distinguish imported CMS content from a Gomnee-managed Article. Imported
old posts use `gomnee_list_cms_articles` and `gomnee_get_cms_article`, then the
separate CMS proposal/review/update journey in
[imported-cms-articles.md](references/imported-cms-articles.md). Do not pass an
imported item ID to Article authoring tools. The owner-approved CMS path reuses
existing Article read/propose/approve/publish permissions. Missing tools require
operator activation; missing permissions require reconnecting with that consent.

## Archive or restore existing work

An explicit lifecycle request uses `gomnee_get_article_lifecycle` and
`gomnee_manage_article_lifecycle` when available. Copy exact guards and retain
one command UUID and a truthful reason. Archive preserves saved content and
history, removes the planned item and withdraws pending requests. A `stopping`
result is incomplete; recover that same command and follow its current context.
Restore returns the item unscheduled. Read fresh Article context before
continuing writing. A request to stop only the current drafting or brief
preparation uses the existing native Stop control through the Article's Gomnee
link; generation cancellation is not exposed by these lifecycle tools. Archive
requires the person's explicit instruction to archive the Article. See
[lifecycle-controls.md](../../references/lifecycle-controls.md). These tools
never approve content, publish or change a live page.

## What you are doing

You author proposals. Gomnee holds the authority: the accepted Company
Context, Strategy, Demand and Asset decide what this Article is for. An owner configures which named decisions require direct review and which
product code may execute under workspace settings. Use only advertised policy
capabilities and their separate consents. Describe a proposal as applied or an
Article as approved only when its saved receipt says so. Publication remains a
separate explicit request; writing never implies permission to publish.

A good result is a complete Article a reviewer can approve with few edits,
because every claim is supported, the promise is kept, and the reader's task
is done.

Use the tools exposed by the connected host, their current definitions and
returned guidance. A tool named here may be missing from this connection;
discover it or use the exact returned Gomnee recovery/review link. See the
[MCP workflow](../../references/mcp-workflow.md) for connection, retry and review
boundaries. You write the proposal with the person's chosen intelligence;
do not assume an external call can run Gomnee's native writer.

## The journey

First find the saved work and choose the entry point. Use the shortest path
that completes the person's request:

| Request and saved state                                    | Entry point                                                                                                                                               |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Write a planned Article; the accepted Asset has no Article | Prepare the Article, read its context, then propose the first brief.                                                                                      |
| Continue an Article with an applied brief and no draft     | Read fresh context and write the complete draft from that brief.                                                                                          |
| Edit an existing draft or published Article                | Read its context and propose the requested change. Preserve the rest; preparation and a new brief are unnecessary unless Gomnee reports a prerequisite.   |
| Return to a saved review                                   | Read the proposal's compact status first. Follow its decision, feedback and next action. A pending review stays pending.                                  |
| Repair or refine a saved Article proposal                  | Read its decision and bounded proposal context, then inspect the affected parts and propose the supported amendments. Use the full read when unavailable. |
| Add or replace only an existing Article's cover            | Host the selected image explicitly, then use the advertised cover-only proposal form against the current revision. Return its exact Owner review link.    |
| A new draft needs an older brief upgraded                  | Explain that prerequisite and propose the brief update using Gomnee's current guidance. Continue drafting after recorded application.                     |

The stages below are the new-Article journey. Enter at the relevant stage;
do not repeat completed stages. Each proposal ends with its exact saved receipt.
A pending proposal needs human review at its exact link; an applied policy
decision allows the already requested next stage. A complete drafting request already authorizes continuing
after an applied brief; the decision receipt supplies the next step.

A bounded edit to an existing revision can preserve its older document format
when Gomnee permits that edit. State that readiness blockers remain. Do not turn
a requested summary edit into a full brief upgrade or rewrite; follow the
current operation's guidance, and keep publication separate.

The proposal envelope and the Article document have independent versions.
Read both from the current tool schema and context guidance; do not infer the
Article's format from the envelope's version. Use the server's current document
requirements and exact base identifiers when preparing a proposal.

For a cover-only request, follow
[article-covers.md](references/article-covers.md). A cover is listing/card
artwork, separate from body hero or inline media. Hosting makes the selected
image public; a separate exact Owner review adopts it into a new unapproved
revision. Ordinary automatic draft-application settings do not apply a cover
proposal. Do not resend the full Article just to change its cover.

1. **Find the work.** If the workspace is unknown, list workspaces and let the
   person choose by name when the choice is ambiguous; never guess a slug.
   Use a single returned workspace when it matches their request. List Articles and accepted
   Assets. If the person pasted a Gomnee link, use the Article or Asset it
   names.
2. **Prepare, if needed.** An accepted Asset without an Article needs
   `gomnee_prepare_article`. It creates the Article workspace only, with no
   model or provider cost. Explain it briefly and proceed when the person's
   request already authorizes preparing the planned Article.
3. **Read the current context.** Prefer the advertised compact task-context
   read, or use `gomnee_get_article_context` as the full-context fallback.
   Start with current state, proposal guidance and brief findings. Load the
   task-specific saved documents and evidence it references; follow cursors
   or pages when more relevant content remains. Note the
   reader, the task, the accepted angle, the Demand, keywords, saved evidence,
   attached sources, any saved brief or draft, and the exact digest.
4. **Check the angle before the brief.** Verify every factual premise the
   planned angle depends on — especially claims about third-party products,
   integrations, prices, versions or regulations — against primary sources.
   If the premise is wrong, say so plainly. Reframe within the accepted Asset
   when the Asset still holds; otherwise recommend changing the Asset in
   Gomnee rather than writing around it.
5. **Research the actual questions.** Use accepted company expertise, relevant
   saved search research and retained primary-source passages. Discover the
   company's configured source map when the connected tools support it; its
   purposes guide what to read. Follow
   [research-and-sources.md](references/research-and-sources.md) for exact source
   reads, privacy, truncation and public attachment. Read fresh context after
   attaching or selecting evidence. Record gaps rather than inventing proof.
6. **Propose the brief.** Use the current brief form returned by Gomnee. Before prose, connect company
   expertise, the desired association and relevant SEO research to a specific
   contribution. Record the company rationale and a concrete writing approach;
   use a provisional basis when no approved voice examples
   exist. Call `gomnee_find_internal_links` for real inventory and select only
   useful pages. Build the brief from the brief card in
   [editorial-standard.md](references/editorial-standard.md). Check the brief's
   title, slug, planned headings, FAQ origins and required modules before
   submitting; use the returned brief preflight findings. For a tutorial,
   establish the actual first-hand evidence and useful public verification
   excerpt, or record the docs-only limitation for human review before prose.
   A retained source alone is not proof of a tested procedure. For an older brief,
   preserve its accepted reader task and evidence while proposing necessary
   current-standard repairs with the upgrade in one reviewed proposal. An
   absent report is not a pass. Show the person
   a short summary, submit it with `gomnee_submit_article_proposal`, open the
   saved decision receipt first. If still pending, open the exact review with
   `gomnee_read_article_proposal` and give its review link. If applied under
   workspace settings, read fresh context and continue the requested draft.
   Supported MCP Apps hosts show human decision buttons for pending work. The human connects
   the review card once and decides there; you never activate their connection
   or ask for its private verifier. Do not draft until the brief has been applied.
   For a current proposal awaiting human review, use `gomnee_wait_for_decision`
   for a bounded wait within their request to continue. An outdated pending
   proposal needs fresh context and revision; waiting cannot make it applicable.
   Read the compact saved receipt and follow its next action; a pending timeout
   is not approval.
7. **Propose the complete draft.** After the brief is applied, read the context
   again and use Gomnee's current draft form from that brief: preserve its title,
   slug, section keys/headings, claims and source basis. Structural corrections
   go through a new brief proposal before drafting. Follow the editorial,
   on-page, localization and linking
   references, and submit. The receipt's server-owned quality report names
   mechanical failures and unassessed editorial checks. Fix actionable findings
   through a fresh proposal, preserving the reviewed brief; use
   `gomnee_get_quality_report` for the saved revision. Its `scorecard` says how
   many checks are left before approval and which need a change, which need the
   reviewer's call and which are already fine. Do not declare a model or
   human review completed yourself. First-hand evidence must be actual output
   with date/environment; an untested tutorial needs public docs-only disclosure
   and an authorized exact reasoned exception. Check the saved application status and hand
   over the review link when review is still required.
8. **Revise.** Reviewer feedback or a requested edit becomes a new proposal
   against fresh context. For an existing proposal, prefer
   `gomnee_get_article_proposal_context` and `gomnee_read_article_proposal_part`
   when available to inspect the exact saved work without loading the entire
   payload. Use `gomnee_amend_article_proposal` only for its advertised typed
   amendments; it saves a new ordinary proposal and leaves the source unchanged.
   Use the full proposal read and normal submission when these tools are absent
   or the change exceeds their form. Never resend an old base. Follow
   [proposal-iteration.md](references/proposal-iteration.md) for precise FAQ
   repairs and evidence-only brief changes that can retain a complete draft.
   For a small edit, change only the requested content and explain what changed.
   Preserve other fields and keep Article approval and publication separate.
9. **Resume.** Use `gomnee_get_proposal_status` to check the durable decision.
   Request-changes feedback guides a new proposal against fresh context. Withdraw
   your obsolete pending submissions with `gomnee_withdraw_proposal`, naming a
   saved replacement when appropriate. Keep accepted decisions and history.

The tool descriptions and results state the exact proposal form for each
stage, the base identifiers to use and what is blocked. Follow them. When a
result names a next action or a recovery link, prefer it over your own plan.

## Approval and explicitly requested publication

Read `gomnee_get_approval_policy` when available. Only owners save controls in
Gomnee; a writing request never authorizes changing them. Existing connections
need separate consent before proposals can apply under policy. A settings
change never sweeps pending work; do not resubmit with new IDs to evade review.

If the person's request includes final editorial approval, an advertised
`gomnee_approve_article` can request it for the exact current revision under
`article_approval` policy and separate approval consent. A missing assessment
queues one bounded product review. Queued is not approved; inspect current
quality and saved state. Use the exact current editorial review packet and the
explicit optional `editorialReview` input only when the advertised schema, owner
automatic policy and requested task permit it; follow
[editorial-standard.md](references/editorial-standard.md). Missing evidence stays
unassessed even after a named permitted exception.

When the review packet carries `reviewLayers`, the workspace reviews in three
layers. Lint is the gate: fix each error you can in a new revision, using its
`locations`; the person may instead waive an error marked `waivable` when they
sign. Warnings never block. The `editorialScorecard` is an independent editor's
guidance and never gates approval. Policy approval then takes no
`editorialReview` and never waives an error. Never sign, waive or write a waiver
reason for the person.

Only when publication was requested, use an advertised `gomnee_publish_article`
with separate publication consent, the exact approved revision/current row
version and matching create/update operation. Keep one command ID for identical
retries. A replayed `queued` receipt repeats the original start, rather than the
attempt's current state. Inspect recorded publication state for completion,
failure or recovery before saying it is live. Return the Article's authenticated
review/publishing link when policy requires a human.
Follow [the MCP workflow](../../references/mcp-workflow.md) for source adoption,
revocation, scope upgrades and recovery. Native generation is not exposed by
these commands.

## Writing rules that matter most

The references carry the detail. These rules override convenience:

- **Nothing invented.** No product capability, integration, customer result,
  statistic, quote, test, byline or first-person experience that the evidence
  does not support. If the Article needs proof you do not have, narrow the
  promise or record the gap in the brief.
- **Answer early.** The opening gives the answer, recommendation or thesis
  before background.
- **Caveats go to the reviewer, not the reader.** Evidence limits, missing
  sources and verification notes belong in the brief's gaps and the draft's
  review-only cautions. Required public verification disclosure and caveats
  that change what a reader should do belong in the Article text. Never expose
  private provenance or evidence-management chatter.
- **Write for the accepted market.** Use the market language and local
  conventions from the context, not translated English boilerplate.
- **Meet the reviewed commission.** Follow current house defaults and accepted
  brief commitments with natural prose. A format, locale or evidence exception
  needs exact reasoned review through the currently authorized decision path. Never pad, stuff keywords, invent
  questions or use decorative media to clear a check. Quality and effort are
  separate: fewer steps do not excuse weaker evidence or an incomplete answer.

## Talking with the person

- Lead with the one next step. Keep updates short.
- Explain routine preparation and source attachment briefly. Proceed within
  the person's existing request or agreed plan; ask only for a missing choice,
  unclear scope or a new cost-bearing action. When policy requires human review, the decision still requires their exact
  review in Gomnee.
- Show what you are about to submit in a few lines, not the whole payload.
- After submitting, give the review link and say what happens next: the
  person reviews a pending proposal in Gomnee, or product code has applied it
  under workspace settings. Continue only after the recorded decision.
- When the person asks whether it is live, answer from Gomnee's recorded
  state. Approval and publication are separate decisions governed by their settings.

## When something fails

Read the error. Gomnee names the failing check, the blocker and usually a
recovery link. Fix that one thing, read fresh context, and try again. Do not
retry blindly or change several things at once. Reuse a submission ID only to
repeat an identical request. If a prerequisite lives in the app — a pending
Company Context review, planning evidence approval or a stale Strategy —
explain it and give the link instead of working around it.

## References

Load a reference when the stage needs it:

- [editorial-standard.md](references/editorial-standard.md) — brief card,
  article formats and their required parts, quality bar, what never to do.
  Load before the brief and before the draft.
- [on-page.md](references/on-page.md) — title, summary, slug, headings,
  images, metadata. Load for the draft.
- [localization.md](references/localization.md) — writing for the market
  rather than translating. Load when the market language differs from the
  conversation or the sources.
- [internal-links.md](references/internal-links.md) — linking to the site's
  own pages. Load for the draft.
- [research-and-sources.md](references/research-and-sources.md) — connected
  company knowledge, primary evidence, source limits and privacy. Load for
  research or a missing-evidence finding.
- [house-defaults.md](references/house-defaults.md) — current house targets and
  permitted review exceptions. Load before commissioning or repairing a brief.
- [proposal-iteration.md](references/proposal-iteration.md) — inspect and amend
  a saved proposal, repair exact findings and retain eligible draft work. Load
  for reviewer feedback or an existing proposal that needs correction.
- [article-covers.md](references/article-covers.md) — host an existing image,
  propose only the exact cover replacement and return the Owner review.
