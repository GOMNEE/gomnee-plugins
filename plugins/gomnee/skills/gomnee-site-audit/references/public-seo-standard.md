# Gomnee public SEO standard

This is the standard Gomnee holds a published Article page to. It favours
truthful, consistent pages over checklists. Nothing here guarantees rankings,
rich results or AI citations.

## Page identity

- One canonical URL per Article, self-referencing, on the site's preferred
  host and protocol, without query strings.
- The page is indexable: status 200, no `noindex` in meta robots or
  `X-Robots-Tag`, not blocked by `robots.txt`. Preview and staging hosts are
  the opposite: they must not be indexable.
- `<html lang>` matches the Article's language.

## Title and description

- A unique title element that matches or closely reflects the visible title.
- A meta description from the approved search field and reviewed destination
  mapping; it need not be identical to the Article summary.
- The house defaults are search title at most 60 Unicode characters and
  description 140–160, each with the reviewed primary phrase. Check current
  commitments and recorded exceptions when available. Search engines may
  rewrite both; these are Gomnee editorial limits, not ranking guarantees.

## Structured data

- Emit one Article or BlogPosting entity per Article page, generated from the
  real published facts. BlogPosting fits an ordinary blog post.
- Google recommends — it does not require — `headline`, `author`, `image`,
  `datePublished` and `dateModified`. `mainEntityOfPage`, `publisher`,
  `inLanguage` and `description` are useful vocabulary.
- Only real values. Omit an optional field rather than inventing it. The
  publisher is the site's organization, not Gomnee. A model is not an author.
- Structured data must agree with what the page shows: headline, byline and
  dates.
- No duplicates: when a CMS, theme and custom code each emit Article markup,
  keep one.
- Generate selected FAQPage/HowTo only from the same actual visible modules
  and the reviewed mapping's declared owner. They are not a reason to invent
  FAQ or procedure content and do not promise rich results.
- BreadcrumbList only for a real navigational hierarchy.

## Readability and media

- One visible main heading, ordered subheadings, readable body text on a
  phone.
- Informative images carry alternative text describing what they show;
  decorative images carry empty alternative text.
- Images are sized for their display and served in modern formats where the
  stack supports it.

## Performance

Measure with field data, not a single lab run. Google's targets at the 75th
percentile: Largest Contentful Paint within 2.5 s, Interaction to Next Paint
below 200 ms, Cumulative Layout Shift below 0.1. A good result does not
guarantee rankings; a poor one is worth fixing for readers.

## Discovery

- Articles appear in the XML sitemap with accurate last-modified dates.
- `robots.txt` references the sitemap.
- Each Article is reachable through the site's own links, not only the
  sitemap.

## Article commitments and unsupported rules

Inspect the accepted brief, current findings and human exceptions when available.
Commissioned depth, useful heading spacing, keyword placement/repetition,
FAQ and visuals are Article house commitments. A missing required module is a
finding; a justified exception is distinct from an ordinary pass. Public-page
inspection alone cannot establish the exact accepted brief or claim entailment.

Do not invent a universal search-engine word count, require the exact keyword
in every heading, add decorative images or FAQs to every page, require
`llms.txt`, or substitute a third-party SEO score for evidence. If the accepted
Article basis is inaccessible, mark house-standard compliance unknown.
