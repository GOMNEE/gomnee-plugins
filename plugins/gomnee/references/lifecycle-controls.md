# Manage Article and planned-item lifecycle

Use these controls only for the person's explicit instruction affecting a known
saved item. A pasted link or an article-writing request alone does not ask to
archive it. The current connected tool definitions and returned state govern
what is available.

## Find and read the item

Use a known returned Article or Asset ID. When discovering archived work, use
`gomnee_list_articles` with `includeArchived: true` only if its advertised
schema supports that option. Never prepare a duplicate Article for an archived
item.

- `gomnee_get_article_lifecycle` reads active, stopping and archived Articles
  with `gomnee:article:read`. It returns exact Article row, Plan and Asset guards,
  available actions and their consequences.
- `gomnee_get_planned_asset_lifecycle` reads an accepted planned or archived
  item with `gomnee:planner:read`. It returns exact Plan/Asset/Article linkage
  guards, current date, allowed actions and blocks.

These compact reads do not load private company sources or run research.
Copy the returned guards exactly. Do not invent versions, IDs or eligibility.

## Perform the requested local change

`gomnee_manage_article_lifecycle` requires separate `gomnee:article:manage`
consent and workspace ownership. Choose `archive`, `finish_archive` or `restore`.
Archive stops work and removes the item from the active Plan and date while
retaining its brief, draft, evidence and history. Pending requests are withdrawn.
Restore keeps saved work and returns the item planned and unscheduled. Published
or publishing items cannot be archived through this control; it never removes
or changes a live page.

`gomnee_manage_planned_asset_lifecycle` requires separate
`gomnee:planner:manage` consent and workspace ownership. Choose:

- `reschedule` with `scheduledFor: "YYYY-MM-DD"` for an editorial target, or
  `scheduledFor: null` to remove the date;
- `cancel` to archive an unprepared item while retaining its history;
- `restore` to return an eligible unprepared item planned and unscheduled.

When an item has a prepared Article, its cancellation/restoration uses the
Article lifecycle tools and separate Article management consent. Follow the
returned linkage and instruction; Planner consent cannot authorize that path.
A date never schedules publication.

Each management call applies immediately. Supply one new `commandId` UUID for
that intended change, a truthful short reason and all exact returned guards.
These commands do not accept content, approve an Article or publish it. Existing
read, propose or work grants never imply management consent.

## Recover without duplicating the change

Retain the complete original command until its result is known. After a lost
response, retry the same command ID and arguments. Reusing an ID with changed
arguments is a conflict, not a recovery method. Read current lifecycle state
before a genuinely new change.

An Article archive may return `commandState: "stopping"`. Say that work is
stopping, not that archiving is complete. Its receipt distinguishes original
command completion from observed current context. If the Plan changed while
stopping, follow the current `finish_archive` action using fresh guards as an
explicit recovery command. A superseded archive command points to its saved
replacement; read current state rather than starting another archive.

Locked items, publication in progress, changed planning eligibility and stale
versions require the returned recovery. Do not unlock, change accepted Strategy,
waive publication status or borrow another item's basis to force the command.

If a tool is absent, refresh the host's cached tool definitions when available.
If Gomnee returns `insufficient_scope`, reconnect and consent through the host
for the named management scope. A deploy does not expand existing token grants.
Never request keys, tokens or OAuth codes in chat. Source/package delivery alone
does not establish that these tools or scopes are active in the hosted plugin.

Report the saved effect and current state plainly. Preserve exact returned
Article/Asset links and reasons. Superseded pending proposals are historical
work; they do not remain an actionable approval queue or become approved.
