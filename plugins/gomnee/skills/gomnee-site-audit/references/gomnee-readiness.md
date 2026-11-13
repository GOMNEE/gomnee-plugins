# Gomnee readiness requirements

Gomnee keeps hosting and Article publishing independent. A site can be hosted
by Gomnee or stay where it is; either way Gomnee publishes approved Articles
through a qualified publishing destination, and the site keeps its own
routes, templates and design. Gomnee never adds a blog to a site or edits
its code.

Check each requirement. Record `Pass`, `Fail`, `Unknown` or
`Not applicable`, with evidence.

## A. Hosting by Gomnee

Applies only when the site will be hosted by Gomnee.

| ID  | Requirement                                                                                                                                                                                                                                                 | How to check                                                  |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| H1  | Source is a GitHub repository the owner can connect to Gomnee's GitHub App, selecting only this repository                                                                                                                                                  | Repository host and ownership                                 |
| H2  | A supported build profile: Next.js, as a static export or full-stack (pages, API routes, server functions, middleware)                                                                                                                                      | `package.json`, framework config                              |
| H3  | The profile is explicit: root directory, package manager with a lockfile, Node version, install and build commands                                                                                                                                          | Lockfile, `engines`, config files, scripts                    |
| H4  | Every required environment variable is known by name, so the owner can enter the values in Gomnee; the site does not rely on committed secrets or `.env` files                                                                                              | Code references to environment variables; repository contents |
| H5  | The site needs nothing the host would have to provide beyond serving it: no host-provided database, background worker, scheduled job, private network or persistent disk. External services reached over the internet through configured variables are fine | Dependencies, config, deployment files                        |
| H6  | The build succeeds from a clean checkout with the declared commands                                                                                                                                                                                         | Run the build only if the person asks; otherwise `Unknown`    |
| H7  | The owner controls the public domain and can change its DNS at cutover                                                                                                                                                                                      | Ask; registrar or DNS provider                                |

## B. Publishing Articles

Applies to every site that will receive Gomnee Articles.

| ID  | Requirement                                                                                                                                                                             | How to check                                                         |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| P1  | The site has a public Article route and template, such as `/blog/{slug}`, that faithfully renders its reviewed mapped Article fields and required public modules with the site's design | Routes, templates, a live Article page and exact reviewed projection |
| P2  | The template renders Markdown safely: headings, lists, links, tables, code, images; no raw HTML injection from content                                                                  | Markdown renderer and its configuration                              |
| P3  | The template emits accurate page metadata from the Article: title, description, self-referencing canonical URL                                                                          | Rendered `<head>` of a live Article                                  |
| P4  | Article structured data (Article or BlogPosting) is generated once, from real publication facts — see the public SEO standard                                                           | JSON-LD in rendered pages; its source                                |
| P5  | Slugs are stable: an Article's URL never changes after publication, and the route does not rewrite it                                                                                   | Routing and slug handling                                            |
| P6  | New Articles become discoverable: they appear in the sitemap and in an index or navigation path                                                                                         | Sitemap generation; index page                                       |
| P7  | A publishing destination Gomnee can deliver to exists (see below)                                                                                                                       | Source, or ask the owner                                             |

### What a publishing destination must offer

Gomnee delivers one exact approved revision and verifies the result. A
destination — a site-owned API or a CMS that Gomnee supports — must provide:

- **Identity check:** confirms the site, the contract version and the
  capabilities it supports, using a key the site issues to Gomnee.
- **Read one Article** by Gomnee's stable Article identifier, returning its
  current remote version, status, canonical URL, template version, publication/update timestamps and complete public payload matching the content digest.
- **Create or update one Article** from a single request that carries a unique
  command key, the exact approved mapped revision, public fields and modules,
  public presentation (authors, media, citations and search metadata), and
  the remote version Gomnee last saw. Repeating the same command returns the
  original result; an update against a changed remote version is refused
  without changing the page.
- **A receipt** with a stable remote identity, a version that only increases,
  the canonical public URL and the content digest.

The neutral Custom Website protocol uses the Project's canonical HTTPS origin
and `/api/integrations/gomnee/publishing/v1` (GET capabilities), with
`/articles/{articleKey}` for GET/PUT. Inspect the actual capability document for
its adapter identity, contract/content versions, exact site origin, pinned
template and supported destination fields. Do not assume an arbitrary CMS
endpoint is supported or impose a guessed contract version.

Canonical Article quality and destination compatibility are separate. Preview
the reviewed mapping's preserved fields and approved rendering conversions,
then verify the actual page. A legacy Markdown destination cannot silently drop
authors, media, citations or required rich modules. A newly declared destination
schema requires refreshed capabilities and a new reviewed mapping before an
explicit selected-page update; it is not automatic republication.

A destination does not need remote drafts, remote deletion or listing.
Gomnee qualifies every destination with its own probe and read-back before it
publishes to it. The audit reports
whether the site appears to provide these capabilities; it cannot qualify
the destination. When the site has no destination yet, record `Fail` for P7
and state that Gomnee must agree the destination before onboarding completes.

## C. First-party measurement

Applies when Gomnee hosts the site and the owner enables measurement.

| ID  | Requirement                                                                                                 | How to check                                                                |
| --- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| M1  | Calls to action the owner wants counted carry a `data-gomnee-cta` attribute with a short, stable identifier | Markup of primary CTAs                                                      |
| M2  | The privacy notice can take a short entry describing Gomnee's page-view and link-click counting             | Privacy page exists and is editable                                         |
| M3  | The site's routing or middleware does not block same-origin paths Gomnee adds at deployment                 | Catch-all routes, middleware matchers — inference; mark `Unknown` if unsure |

Gomnee's measurement uses no cookies, persistent identifiers or cross-site
tracking, and ships without a consent banner of its own. The owner remains
responsible for the site's privacy notice.

## D. Search Console

| ID  | Requirement                                                                               | How to check                                                                                                                                                                                                                         |
| --- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| S1  | A verified Search Console property covers the exact public site                           | Use the connected exact-property state or owner-provided Search Console evidence. A verification tag or file alone does not prove the property is currently verified.                                                                |
| S2  | The owner can grant Gomnee read-only access; Gomnee cannot complete onboarding without it | Ask                                                                                                                                                                                                                                  |
| S3  | The sitemap is submitted in that property                                                 | Use its Search Console Sitemaps report or explicit owner evidence. A sitemap reference in `robots.txt` supports discovery but does not prove submission in that property; otherwise mark `Unknown`.                                  |
| S4  | Report crawl, indexing and snippet controls relevant to Google's Search AI features       | Inspect Googlebot access, `noindex`, `nosnippet`, `max-snippet` and `data-nosnippet` on representative pages. Record observed restrictions and uninspected pages; never assume a generic AI inclusion switch or guarantee inclusion. |

Google documents [sitemap discovery and Search Console submission](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
as separate methods. Its [Search AI feature guidance](https://developers.google.com/search/docs/appearance/ai-features)
describes existing crawl, indexing and snippet controls. Keep these public-page
observations separate from account-only Search Console evidence.
