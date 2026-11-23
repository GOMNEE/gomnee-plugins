# On-page elements

Gomnee carries the approved Article through a separately reviewed publication
mapping. The customer's template renders its public fields and selected modules.
Write each element truthfully and follow the declared destination projection;
never assume that publication preserves a field the destination cannot carry.

## How the body is rendered

- The site's template shows the **title** as the page's main heading. Do not
  repeat it inside the body.
- Gomnee renders each planned section as a second-level heading followed by
  its Markdown. Prefer third-level headings for subsections and never repeat
  the page's main heading. When the current contract permits a useful additional
  H2 in draft Markdown, it can satisfy a commissioned H2 secondary term without
  changing the accepted section headings. Keep the reading order clear.
- Keep heading levels in order. Headings help a reader scan the argument;
  they are not a keyword list.

## Title

- Accurate, specific, and in the Article's language. It must be fulfilled by
  the body.
- Include the reviewed primary phrase naturally, ideally near the start. The
  applied brief determines the title and intended H1; change it through a brief
  proposal when necessary.
- Keep it accurate and readable. The separate search-title house limit is at
  most 60 Unicode characters; use the exact server guidance and reviewed
  exceptions. Search engines may still rewrite it.
- Distinct from other pages on the same site.

## Summary

- One or two sentences that say what the reader gets. Preserve the applied
  brief's summary.
- Fill the explicit search description separately: the house default is
  140–160 Unicode characters with the reviewed primary phrase. Accuracy and
  natural writing matter alongside that commitment; a useful deviation needs
  the human's reasoned exception. Do not assume the site derives it from summary.

## Slug

- Lowercase words joined by hyphens, in the Article's language, with the core
  phrase and nothing else.
- **The slug cannot change after the first publication.** Choose it carefully
  in the reviewed brief and preserve it in the draft.

## Images and media

- Only images that explain or prove something. Describe what an informative
  image shows in its alternative text; decorative images need none.
- Do not reference an image the site does not have. Media rights must be
  clear before publication.
- Meet commissioned useful visual requirements; a missing or unhelpful image
  is an editorial task, not permission to invent a URL. A format exception
  needs the human's exact review.

### Host an image with Gomnee

When the person explicitly wants Gomnee to host an existing image publicly,
use `gomnee_host_image` if the connection advertises it. This uses the existing
`gomnee:article:work` consent, requires an Owner and completed Search Console
setup, and returns a stable public HTTPS URL. Hosting makes the image public
immediately; it does not edit, approve or publish an Article.

Use one fresh command UUID and the discovered workspace slug. Direct transfer
requires `name`, rights with `basis: "owned" | "licensed"`, `credit` (text or
`null`) and `publicUseConfirmed: true`, plus exactly one source:

- A host-supplied `file` object with `download_url` and `file_id`; `mime_type`
  and `file_name` are optional. PNG, JPEG and WebP files may be up to 8 MiB.
- `data: {base64, mediaType}` for a supported image up to 2 MiB decoded, when
  the client can transfer the bytes without copying large binary data through
  model text.

ChatGPT can supply the file object when its file-transfer integration is
available. When ChatGPT, Claude or another client cannot transfer the file,
call with only `workspaceSlug` and `commandId`. An `awaiting_upload` response
contains an authenticated Gomnee upload link: give it to the person, let them
upload and confirm public-use rights there, then read the same command UUID
again to obtain the saved `publicUrl`. A local file path is not a download URL;
never invent a file reference or ask the person to paste base64.

Gomnee verifies the bytes and normalizes the image to PNG without resizing.
Use the returned verified dimensions, rights/credit and public URL in the
existing Article `presentation.media` proposal fields, with useful alternative
text and the appropriate hero or inline placement. SVG is unsupported here.
Existing private Creative assets cannot be made public by passing their IDs.
Keep the same UUID for status and identical retries; a different image or
hosting request needs a new UUID. Refresh Article context and follow the
ordinary proposal, approval and publication flow after hosting.

For listing/card artwork, use the separately advertised cover-only form in
[article-covers.md](article-covers.md). It takes the exact hosting receipt,
not a URL in `presentation.media`, and always requires the Owner's cover
review before creating a new unapproved Article revision.

## Structured data

Use the reviewed mapping's declared owner for generated markup. Applicable
Article/BlogPosting and selected FAQ/HowTo entities come from the same visible
content and real destination facts, with consistent author, dates and headline.
Do not add a second competing generator or promise rich results. Commission
useful FAQ or procedure content for the reader task, then check faithful public
rendering separately.

## Search features worth writing for

- A short definition, ordered steps or a comparison table can be quoted
  directly by search and AI answers when the reader asked that question. Use
  them when they are the best answer, not as decoration.

Adapted in part from the SearchFit SEO toolkit (MIT). See
`THIRD_PARTY_NOTICES.md`.
