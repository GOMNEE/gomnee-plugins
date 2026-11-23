# Report template

Keep the report scannable. Put the decision first.

```markdown
# Site audit: <site>

**Date:** <YYYY-MM-DD> · **Intent:** <Gomnee hosting + publishing | publishing only>
**Market:** <country, language> · **Evidence:** <live site | repository @ <commit> | both>

## Summary

- **Gomnee readiness:** <N> fail · <N> unknown · <N> pass — <one line on what blocks onboarding>
- **SEO health:** <one line on the most important issue>
- **Do first:** <1–3 actions, blocking readiness items before SEO>

## Gomnee readiness

| ID  | Requirement | Result                      | Evidence                            | Change needed                |
| --- | ----------- | --------------------------- | ----------------------------------- | ---------------------------- |
| H1  | …           | Pass / Fail / Unknown / N/A | <URL + status, quote, or path:line> | <what to change in the site> |

Gomnee qualifies hosting with its own candidate deployment and publishing with
its own probe and read-back. This audit does not qualify the site.

## SEO health

### High — affects crawling, indexing or readers now

- **<finding>** — <evidence>. Fix: <specific change>.

### Medium

- …

### Low

- …

## Not assessed

- <requirement> — <why the evidence was out of reach and how to obtain it>

## Observations versus inferences

- <any conclusion drawn indirectly, and what would confirm it>
```

Use `Unknown` rather than guessing. Omit empty priority groups.
