---
name: plan
description: Plan what to publish in Gomnee by turning Demands with keywords into planned content items (Assets) with a title, an angle and a target date. Use for "plan the articles", "what should we publish", "fill the calendar", "add an item to the plan", "change this planned item", or when planning is waiting on something. Proposes the plan for the owner's review.
---

# Plan

The plan turns Demands with keywords into **Assets**: planned pieces with a title, an angle, an intent, a primary keyword and a target date. Each accepted Asset later becomes one article.

Gomnee's own suggestion (the **allocation**) is a list of eligible rows, not a plan. This skill groups it into a plan worth accepting.

Read [Working with Gomnee](../../references/working-with-gomnee.md) first.

## Before you start

From `research`, per Demand: the primary keyword, the secondaries, the format that ranks, the angle, and any Demand merged into another article.

## Steps

### Get planning ready

1. **Read what planning is waiting on.** `gomnee_get_planning_evidence_preparation` names each missing input, why it is unmet, who resolves it and the next step. It also shows the planning preferences as they stand and any keyword request already running.

   | Missing | Resolved by |
   | --- | --- |
   | An active Demand | `strategy` |
   | Strategy alignment after a business-map change | The owner, in Gomnee |
   | Planning preferences | The owner, in Gomnee. Suggest values that follow from the Strategy |
   | Keyword data | Step 2 |

2. **Prepare keyword data only if nobody has.** If a request is already running, wait. Otherwise, with the person's agreement, call `gomnee_prepare_planning_evidence` as its description says. It is paid, with a small stated maximum. Read its status with the same command ID until planning is ready. On a failed or unclear state, stop and tell the person; never retry with a new ID.
3. **Read the preferences back to the person.** Preferences marked as defaults were never chosen by anyone. Ask the owner to choose them in Gomnee before you plan against them.

### Read the plan

4. **Read `gomnee_read_plan`.** It returns the current plan, the `contextDigest` a proposal needs and the parts available. Read the allocation and the planning brief with `gomnee_read_context_parts`. When the plan lists a part for the goal that orders the allocation, read it too: it says what the plan is ordered by and why.
5. **Skip what is already there.** Do not propose a topic that is already planned, awaiting review, or answered by an existing page.

### Group the allocation

6. **Plan one Asset per Demand**, not one per keyword.

   ```text
   Is the Demand answered by an existing page, or merged into another article?
   ├── Yes → no Asset. Say so in the rationale.
   └── No  → find the allocation row whose primary keyword is the one chosen in
             research.
             ├── Found     → that row is the Asset. Other rows of the same Demand
             │               supply the secondary keywords.
             └── Not found → choose the nearest row of the same Demand and note
                             the intended keyword in the angle.
   ```

7. **Build each Asset from its row.** Copy the row's references unchanged. Write the title, the angle (the gap found in research), why this and why now, the intent and the target date yourself.
8. **Take secondary keywords only from rows of the same Demand.** A refusal names any keyword that is not eligible and why.
9. **Order by what the Strategy needs first**, not by score. The first Asset should be the question the site exists to answer.

### Submit

10. **Submit one proposal** with `gomnee_submit_planner_proposal`, following the tool's description for the form. In the rationale, say why the plan has fewer items than the allocation.
11. **Read the receipt** and hand over the review link when it is pending.
12. **Confirm** with `gomnee_list_articles`: the planned items appear there.

### Change an accepted item

- **Title, angle or intent:** propose the edit with `gomnee_submit_planner_proposal`. First read the plan's pending-edits part, when it is listed: it holds rewordings already waiting for review, and those should not be proposed again. Do not cancel and re-add an item to change its words. If the item already has an Article, propose the change on the Article.
- **Date, cancel or restore:** follow [lifecycle-controls.md](../../references/lifecycle-controls.md). These apply at once.

## Checks

- One Asset per Demand at most. No two Assets face the same results page.
- No Asset targets a keyword an existing page owns.
- Every date is inside the planning window.
- The person has chosen or confirmed the preferences.

## What the person decides

- The planning preferences.
- The order and the dates. A date is an editorial target. It never schedules publication.
- Whether a merged Demand should get its own article later.

## Do not

- Do not accept the allocation as it stands.
- Do not start a second keyword request while one is running.
- Do not invent the references a row supplies.
- Do not fill the calendar to match a rhythm nobody chose.
- Do not plan from the allocation's score alone.

## Hand-off

Give `article`, for the first Asset: its title, angle, format, primary and secondary keywords, the People Also Ask questions and saved results from research, and the nearest existing page with the direction of the link between them.
