# Technical SEO craft

General site health, beyond the Article pages. Report what you observe with
evidence and a concrete fix. Prioritize by effect on crawling, indexing and
readers, not by the length of the list.

## Crawlability

- `robots.txt` exists, references the sitemap, and does not block pages,
  scripts, styles or images that pages need. Watch for an accidental
  `Disallow: /`.
- The XML sitemap lists only canonical, indexable URLs that return 200 — no
  redirects, errors or `noindex` pages. Very large sites split it with a
  sitemap index.
- Meta robots and `X-Robots-Tag` agree with the intent of each page; no page
  is both canonicalized elsewhere and `noindex`.

## Indexation

- Important pages return 200. Removed pages return 404 or 410, not a soft 404
  that renders an error with status 200.
- Permanent moves use 301 or 308, with no chains or loops.
- One preferred host and protocol: `http` and the non-preferred `www` variant
  redirect in one step.
- Canonical tags resolve duplicates from trailing slashes, parameters and
  pagination. Search engines no longer use `rel="next"`/`rel="prev"`; each
  paginated page is canonical to itself.

## URL structure

- Readable, lowercase, hyphen-separated paths without session or tracking
  parameters.
- Consistent patterns for each content type.

## Performance

- Field data first; see the public SEO standard for targets.
- Common causes to look for in the source: unoptimized or unsized images,
  render-blocking scripts or styles, heavy third-party scripts loaded eagerly,
  web fonts without a display strategy, large client-side bundles.
- For Next.js: use the framework's image component, keep static content on
  the server rather than in client components, and load heavy components on
  demand.

## Mobile

- A viewport meta tag, no horizontal scrolling, readable text without zoom,
  adequately sized touch targets, no intrusive interstitials.

## Security

- HTTPS everywhere with no mixed content, and an HSTS header.
- No exposed files such as `.env`, `.git` or backups.

## Internal links

- **Orphans:** pages no internal link points to. Link them from related
  content or navigation.
- **Dead ends:** pages with no onward links. Add the natural next step.
- **Buried pages:** important pages many clicks from the home page. Link them
  from hub pages.
- **Vague anchors:** "click here", "read more". Replace with descriptive
  text.
- Broken internal and external links: list the URL, the page it is on and
  the status.

## Several languages

- Each language version has its own canonical URL, correct `lang`, and
  reciprocal `hreflang` alternates including `x-default`.
- Keywords are researched per market, not translated.

## Not findings

Scores out of 100 and invented search-engine quotas are not findings. General
site health is distinct from an Article's reviewed house commitments: inspect
the accepted brief and current findings before assessing commissioned length,
links or keyword repetition.

Adapted in part from the SearchFit SEO toolkit (MIT). See
`THIRD_PARTY_NOTICES.md`.
