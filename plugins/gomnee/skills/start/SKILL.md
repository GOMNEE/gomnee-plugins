---
name: start
description: Get oriented in a Gomnee workspace and choose the next step. Use at the start of any Gomnee session and for "where do I begin", "what can you do with Gomnee", "set up my workspace", "review my business map", "what needs my attention", "what should I publish next", a pasted Gomnee link, or a request to reschedule, cancel, archive or restore saved content. On a new workspace it reviews the business map with the person first.
---

# Start

Find out where the workspace stands and name one useful next step. On a workspace with no Strategy yet, review the business map with the person first: everything Gomnee produces rests on it.

This skill reads and reports. It spends nothing. The only thing it may propose is a correction to the business map, and only once the person has agreed the wording.

Read [Working with Gomnee](../../references/working-with-gomnee.md) first.

## Steps

### 1. Find the workspace and its state

1. Find the workspace with `gomnee_list_workspaces`.
2. Read `gomnee_get_workspace_visibility` for waiting decisions, running work and connection health.
3. Read `gomnee_read_strategy`. Its `outline` lists every Territory with its active Demands.
4. Choose the path:

   | State | Path |
   | --- | --- |
   | No Territories, or the person says this is their first session | First session (section 2) |
   | A Strategy exists | Every later session (section 3) |
   | The person asked to reschedule, cancel, archive or restore something | Manage an item (section 4) |
   | The person pasted a link to a proposal | Read `gomnee_get_proposal_status` and follow its decision |

### 2. First session: review the business map

The person must be present. This is a conversation.

1. **Read the map.** `gomnee_read_strategy` lists the Company Context among its parts; read it with `gomnee_read_context_parts`.

   | Entity | What to check |
   | --- | --- |
   | Identity | Is there one clear identity? If another company makes the site, is that stated? |
   | Offer | Is every offer real and described on the site? Is anything real missing, such as a free tool? |
   | Audience | Are the groups distinct? Is one missing? |
   | Problem | Is it written as the audience would say it? |
   | Expertise | Does its scope say what the business does not do? |
   | Proof | Is each figure true today? |

2. **Read every entity to the person, in their language.** Ask of each: is this true, is it current, would you say it this way?
3. **Compare the map with the live site.** Open the home page, the main product pages and the about page. `gomnee_list_website_pages` lists the pages Gomnee has saved. Note what the site says that the map lacks, and what the map claims that the site does not show.
4. **Check every figure** in a proof against the site today.
5. **Trace each chain:** which audience has which problem, addressed by which offer, helped by which expertise, supported by which proof.

   ```text
   Is a link missing?
   ├── Problem with expertise but no offer → content can build reputation with
   │                                          nothing to sell. Legitimate. Say so.
   ├── Offer that addresses no problem      → mis-described, or not worth content.
   ├── Audience with no problem             → it will produce no Demands.
   └── Chain complete                       → a candidate Territory.
   ```

   Never invent an offer to complete a chain.
6. **Write down the boundaries:** what the business will not sell, claim or publish. Ask the person directly. Carry them into every later brief as cautions.
7. **Note the other foundations:** the research market (`gomnee_list_research_markets`), Search Console (`gomnee_query_search_console`), the Brand Kit (`gomnee_get_brand_kit`), the approval settings (`gomnee_get_approval_policy`) and whether the site has pages that are not articles.
8. **Give the readout** (template below). Tell the person what Google already associates the site with, from Search Console by query and by page. On a new site this is the first useful fact.
9. **Propose the corrections the person agreed.** `gomnee_submit_company_context_proposal` saves them for the owner's review in the Business Map. It never applies by itself. If the person prefers, give them the exact wording to enter in Gomnee.
10. **Agree the rules** before any Strategy is proposed:
    - what the site is expert in, and what it must not appear to sell;
    - whether paid research may be started, and up to what amount;
    - the approval settings. Manual review suits most. Recommend that Article approval and publication stay manual.

### 3. Every later session: orient and route

1. From the Strategy outline, the plan (`gomnee_read_plan`) and the Articles (`gomnee_list_articles`), work out what exists and what is waiting.
2. Answer the person's actual question with evidence chosen for it:
   - site performance: `gomnee_query_search_console`;
   - market estimates: `gomnee_list_saved_research` and `gomnee_read_saved_research`, before suggesting any new collection.
3. Lead with the state, what it means and one recommended next step. For an open question offer two to four concrete choices. For an explicit task, proceed.

   | State | Next skill |
   | --- | --- |
   | The map needs corrections | This skill, section 2 |
   | No Territories, or a new Territory or Demand is wanted | `strategy` |
   | Demands without keywords, or a question about demand size or what ranks | `research` |
   | Demands with keywords and nothing planned | `plan` |
   | A planned item, a brief, a draft or a review is waiting | `article` |
   | A question about the site itself | `audit` |
   | A campaign page | `campaign` |
   | Gomnee behaved wrongly | `feedback` |

Give the reason for the step: the reader's need, the saved evidence or the unfinished review. Empty Search Console data does not show that nobody wants a topic. Similar topics alone do not show that two pages compete.

### 4. Manage an existing item

For an explicit request to reschedule, remove a date, cancel, archive or restore, follow [lifecycle-controls.md](../../references/lifecycle-controls.md). Read the item's lifecycle first, use the action that matches the instruction and report the saved result. These changes apply at once. They never approve or publish, and a date never schedules publication.

## Readout template

```markdown
# Gomnee foundations review: <workspace>, <date>

## What the site is, in one sentence

## What Google associates it with today
<range>: <impressions> impressions, <clicks> clicks, average position <n>.
Top topics: <…>. Pages that collect them: <…>.

## The business map
Right as it is: <entities that are true and current>

| Finding | Effect later | Proposed wording |
| --- | --- | --- |

Boundaries: <what will not be sold, claimed or published>

## Ready / missing
| Foundation | State | Blocks |
| --- | --- | --- |
| Business map | sound / needs corrections | strategy |
| Strategy | <t> Territories, <d> Demands / empty | research, planning |
| Research market | <country, language> / missing | research |
| Search Console | connected, fresh to <date> / missing | evidence, measurement |
| Brand Kit | saved / missing | images, covers |
| Approval settings | <summary> | |

## Three first moves
```

## What the person decides

- Every change to the business map.
- The boundaries, the spend and the approval settings.
- Which next step comes first.

## Do not

- Do not propose a Territory before the map is confirmed.
- Do not invent an offer, an audience or a figure to make the map look complete.
- Do not correct the person's wording of their own business. Suggest; they decide.
- Do not start paid research.
- Do not skip the readout because little is ready. On a first session the review is the value.
- Do not present a generic SEO checklist before understanding the person's goal.

## Hand-off

Give the next skill: the workspace, the readout with corrections still open, the boundaries, the agreed rules and any candidate Territories from the chain tracing.
