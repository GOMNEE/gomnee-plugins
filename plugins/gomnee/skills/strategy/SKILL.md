---
name: strategy
description: Write or change the Gomnee Strategy, which is the Territories a brand wants to be known for and the Demands (reader questions) under them. Use when the Strategy is empty or thin, or for "set up my strategy", "add a territory", "add a demand", "what should we be known for", "which page already answers this question". Proposes changes for the owner's review and spends nothing.
---

# Strategy

A Gomnee Strategy has two levels. A **Territory** is what the brand wants to be known for. A **Demand** is one question, asked by one audience with one problem. Keywords come later and are evidence, not structure.

This skill drafts Territories and Demands with the person and submits them as proposals. It spends nothing.

Read [Working with Gomnee](../../references/working-with-gomnee.md) first.

## Before you start

- The business map is current. If it is not, run `start` first.
- The person has agreed what the site is expert in and what it must not appear to sell.

## What good looks like

| | Territory | Demand |
| --- | --- | --- |
| Is | A positioning statement: what the brand should be known for | One question a person would ask |
| Is not | A keyword cluster, a blog category, a product line | A keyword, a title, a topic with several questions |
| Comes from | One identity, the audience it serves, the expertise it shows | One audience and one problem from the business map |
| How many | Two or three to start. Few and long-lived | As many as there are distinct questions |
| Test | Would it still be true in two years? | Can one page answer it completely? |

```text
Is it something the brand wants to be known for, not just rank for?
├── No  → it is a keyword group. Make it keywords under an existing Demand.
└── Yes → Can you name the audience and the expertise from the business map?
          ├── No  → the map is missing an entity. Propose it first (step 6).
          └── Yes → Is there evidence people ask about it?
                    ├── No  → hold it back. Record why.
                    └── Yes → propose it with one first Demand.
```

## Steps

### Draft

1. **Read the Strategy.** `gomnee_read_strategy` returns the outline, the Strategy map and the `contextDigest` a proposal needs. Read the Company Context part with `gomnee_read_context_parts` for the audiences and problems you will name.
2. **Draft two or three Territories.** For each: the name, what the brand should be known for in one sentence, and one first Demand.
3. **Say what each Territory leaves out.** Name the queries that belong to other kinds of page, such as lists, products or tools.
4. **Map the questions.** For each audience, list what they ask from first noticing the problem to choosing a provider, as search queries and as prompts to an AI assistant. This list is the source of further Demands and the seed list for `research`.
5. **Show the draft to the person** before submitting. Under an automatic approval setting a proposal applies at once.

### Fix the map first when it is missing something

6. If a Territory needs an audience, problem or expertise the business map lacks, propose it with `gomnee_submit_company_context_proposal`. It waits for the owner in the Business Map and never applies by itself. Hold the Territory until the entity exists. A problem may be helped by an expertise alone: never invent an offer to link one.

### Submit

7. **Submit with `gomnee_submit_strategy_proposal`**, using the `contextDigest` from your latest read. One proposal can carry several Territory and Demand changes, reviewed as a whole. Follow the tool's description for the form.
8. **Cite only what Gomnee returned:** entities from the business map, Search Console queries by their exact text, pages by their full address. A refusal says which citation was not accepted and what would be.
9. **Read the receipt** and hand over the review link when it is pending.
10. **Confirm** with `gomnee_read_strategy`: the outline shows the new Territories and Demands.

### Add Demands over time

11. After `research` has sized the questions, propose a Demand for each one worth answering. Write the question the way the person would ask it. A low-volume question still belongs if it is the question the site exists to answer.

### A Demand an existing page already answers

Many Demands are answered by a page the company already has. A directory answers "find an agency in Milan" with its Milan page, not with an article.

12. Read `gomnee_list_website_pages` for the site's pages and `gomnee_list_demand_answers` for what already answers each Demand.
13. Propose the answer with `gomnee_submit_demand_answer_proposal`: one page, or a family of pages that share an address pattern, as the Demand's primary or a supporting answer. Give the strongest evidence first: Search Console rows showing the query landing on the page, then what kind of page ranks, then the page's stated purpose.
14. The owner decides it in Strategy. Read the outcome with `gomnee_read_demand_answer_proposal`. Once a primary answer is approved, do not plan an article for that Demand.

## After the business map changes

If a Strategy proposal is refused because the Strategy must first be aligned with a changed business map, do not retry. The owner approves that alignment in Gomnee. Then read the Strategy again and revise it to follow the map: a new problem may call for a new Demand, and an existing Demand may belong to a different problem.

## Checks

- Each Territory reads as positioning and names an identity.
- Each Demand has one audience and one problem that exist in the business map.
- Each rationale says what is left to other pages.
- Every proposal has a receipt you have read.

## What the person decides

- The Territories. They are positioning: you draft, the person owns.
- Which candidates to hold back for lack of evidence.
- Every pending proposal, at its review link.
- Corrections to the business map.

## Do not

- Do not name a Territory after a keyword.
- Do not put two questions in one Demand.
- Do not invent entities, queries or addresses for citations.
- Do not retry a refused proposal unchanged.
- Do not describe a pending proposal as accepted.

## Hand-off

Give `research`: the Demands with their questions, the question list from step 4, and the queries each Territory leaves to other pages.
