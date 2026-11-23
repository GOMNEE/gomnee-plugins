# Keywords

Keywords in Gomnee are evidence attached to a Demand. This part collects the evidence and links to each Demand only the keywords an article should rank for.

## The linking rule

```text
What does the searcher want?
├── A list of providers, products or places → a list page owns it. Do not link.
├── A tool or calculator                    → a tool page owns it. Do not link.
├── An explanation, method or comparison    → link it to the Demand that asks
│                                             that question.
└── Unclear                                 → link it for now and check the
                                              search results.
```

Volume does not change the answer. The largest commercial terms usually belong to list or product pages.

## Collect

1. **Choose what to measure.** A keyword collection is one of five jobs:

   | Job | Use |
   | --- | --- |
   | Exact-list metrics (`keyword_metrics`) | Size the questions you wrote by hand |
   | Phrase suggestions (`phrase_expansion`) | See what people add to the main term: city, sector, price, "best" |
   | Category ideas (`category_ideas`) | Broad discovery only. It explores the seeds' wider category, not their phrases |
   | Related searches (`related_searches`) | Searches related to one seed |
   | Site terms (`website_terms`) | Terms a named site is associated with |

   For question-level research use exact-list metrics and phrase suggestions.
2. **Quote, agree, start and read** as [collecting.md](collecting.md) describes.
3. **Reduce the result to one table** and keep it in your notes:

   ```markdown
   | keyword | volume | CPC | difficulty | intent |
   ```

   Results are long. Read them with a sub-agent when the host has one, and ask it to return only this table and the phrases that came back with no data.
4. **Use one run per keyword.** When a keyword appears in two collections, nominate it from one of them only.

## Nominate and link

5. **Add any Demand still missing** with the `strategy` skill, for each sized question worth its own Demand.
6. **Nominate** the chosen rows with `gomnee_nominate_research_keywords`. Nomination only creates candidates. It selects and links nothing.
7. **Read the candidates** with `gomnee_list_demand_keyword_candidates`. Take each keyword's candidate details from this read; do not pair lists by position.
8. **Assign each keyword to one Demand** with the linking rule. Write the assignment down: per Demand, the linked keywords with volume, and separately the keywords left unlinked with the kind of page that owns each.
9. **Submit the keyword review** with `gomnee_submit_strategy_proposal`, following the tool's description for the form. A phrase the provider had no data for can be linked as a custom keyword; its volume stays unknown.
10. **Read the receipt.** Confirm one Demand with `gomnee_find_strategy_demand_evidence`.

## AI visibility baseline

Quote an AI visibility collection for the site's domain. If the quote says the market or platform is unsupported, record that no baseline exists and move on. Quoting is free.

## Checks

- Every started collection had a quote and the person's agreement.
- Each keyword is linked to at most one Demand.
- No list, product or tool query is linked to a Demand.
- The total spend is recorded.

## Say what the numbers mean

When the questions people decide by have small measured volume and the volume sits on terms other pages own, say so before planning. The articles then earn their place by depth, by links to those pages and by being the page an AI answer cites. Nobody should expect traffic from the articles alone.
