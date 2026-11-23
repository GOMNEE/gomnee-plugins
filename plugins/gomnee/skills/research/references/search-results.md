# Search results

Keyword tools estimate intent. The live results show it. This check can move a keyword to another Demand, hand it to an existing page, merge two planned articles, or give an article its angle. Run it before planning.

It is cheap but paid. Quote or state the maximum first.

## Choose the queries

One or two per Demand, not every keyword:

- the keyword you expect to be primary;
- every keyword whose owner is unclear;
- one keyword from each pair of Demands that might share a results page.

## Collect

- **For a few queries,** `gomnee_search_research_web` runs one plain query and returns its results page.
- **For many keywords from a saved keyword run,** quote and start a results collection as [collecting.md](collecting.md) describes. Ask for the top 20: that is enough to see the kinds of page, and deeper costs more.

Read saved results with `gomnee_read_saved_research`. They are long; use a sub-agent when the host has one.

## Record, per query

- the kind of page of each top-10 result: ranked list, provider or product page, guide, definition, tool, forum or social post;
- who ranks in the top five, and what they sell;
- whether the site itself appears in the top 20, and with which page;
- the AI Overview, as far as it is shown: whether one appears, its opening sentence and its sources;
- the People Also Ask questions, **word for word**. A brief can cite them later only by exact wording.

Take a result's address from what the row shows as its destination. A search engine's own redirect link is not the result's address.

## Decide

| Decision | Rule |
| --- | --- |
| **Format** | Write the format that ranks. If tools rank, an article will not. If definitions rank, write a definition. |
| **Ownership** | If lists or product pages rank, the site's list or product page owns the query. Unlink it from the Demand, and propose that page as the Demand's answer with the `strategy` skill. |
| **Overlap** | If two planned articles would face the same results page, merge them: one becomes a section of the other. |
| **Gap** | What no ranking page offers. This becomes the article's angle. |

Then write, per Demand: the primary keyword, the secondary keywords, the format, the angle, and any Demand that becomes a section of another article.

## Save

Save the findings as an investigation with `gomnee_save_research_investigation`, one per question. Cite the saved results pages through `gomnee_inspect_research_citations`, which returns the references an investigation accepts. Mark each finding as an observation (what the page shows) or an inference (what you conclude), say how sure you are, and list what you did not check.

## Checks

- Every query has all four decisions written down.
- Every People Also Ask question is copied exactly.
- No finding names a source the results did not show.
- The spend is recorded.

## Do not

- Do not restart a job that is waiting on its provider.
- Do not plan an article for a query where only tools or lists rank.
- Do not treat a results page as proof of a factual claim.
- Do not report an AI Overview's sources when the view shortened them.
- Do not run the check on every keyword.
