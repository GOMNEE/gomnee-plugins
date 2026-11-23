# Collecting research

Rules for any research that contacts a provider. Reading saved research never does.

## Quote, agree, start, read

1. **Quote.** `gomnee_quote_research_collection` shows the source, the market and the maximum that would be reserved. A quote starts nothing and grants nothing. `gomnee_list_research_markets` lists the saved markets (country, language, device).
2. **Agree.** Tell the person the total across all quotes. Start only with their agreement, or inside a budget they already set.
3. **Start.** `gomnee_start_research_collection` with the identical request, the quote and one new operation ID. Keyword and search research run **one collection at a time** per workspace: start the next when the previous has finished.
4. **Follow.** `gomnee_status_research_collection` until it has succeeded. A job waiting on its provider reads as running: do not start it again.
5. **Read.** `gomnee_result_research_collection` returns the saved result in pages. Follow them to the end before concluding.

## When something is unclear

- **A lost or uncertain start:** repeat the identical call with the same operation ID. Never use a new ID: that can pay twice.
- **A failed job:** read its status for the reason. A read the provider refused is final; a retry will not change it.
- **An unknown charge:** stop new paid work and tell the person.
- **Cancelling** asks a running job to stop. It does not undo a charge already made.
- **Refreshing** collects a new result under a new quote. The earlier result stays.

## One search or one source

- `gomnee_search_research_web` runs one plain query on the workspace's market and returns the results page. It answers `pending` at first: repeat the identical call to read the result, which never pays again.
- `gomnee_run_research_collection` reads one external source in one call, within the maximum the request itself states. `not_started` means nothing was started, and the answer says why.

## What a result is worth

- A keyword estimate comes from a provider, for one market and one date.
- A results page shows what ranked for that query, market and device at that time.
- An empty result is not proof that nobody searches. A provider can return no data and still charge for the lookup.
- Keep the market, the date and the limits with every number you pass on.
