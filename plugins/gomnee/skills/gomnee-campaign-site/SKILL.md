---
name: gomnee-campaign-site
description: Create or improve a customer-owned campaign-page repository, then use available Gomnee site capabilities to preview and explicitly publish an exact committed version with optional network measurement.
---

# Gomnee campaign sites

Use when the person wants a focused offer/service page, a supporting website on
its own domain, or an improvement to an existing campaign site. Keep one
canonical company website with its existing Article, GSC and accepted Strategy
authority. Supporting sites share that strategic core.

## Check access and intent

Discover the actual available tools before promising hosting actions. The Sites
MCP feature must be enabled and its Clerk permissions configured. Follow the
server-advertised site read, management and separate publication/restoration
permissions; measurement has its own read permission. Tool visibility,
assigned application permissions and
the current token's granted permissions are distinct. If a capability is absent
or consent fails, explain the missing step and use the existing authorized UI
where appropriate. Do not loop reauthorization or silently widen authority.

Call `gomnee_list_workspaces` if the workspace is unknown, then
`gomnee_list_sites` and `gomnee_get_site` to identify the exact existing main or
supporting site. Do not guess slugs, source-site IDs, deployment IDs or domains.
Confirm the requested result and existing main-site action. A coding/editing
request permits the requested source changes; publication remains an explicit
request affecting an exact candidate and hostname.

## Reuse company and Strategy context

Read relevant accepted Company Context and Strategy using the tools available
for that workspace. Existing task/context parts and accepted Demand evidence
are the business basis. Explain the customer situation this page addresses and
how the offer contributes. Do not invent a new audience, offer, proof claim or
accepted Demand merely because a keyword/domain is available.

The first optional starter is a focused offer/service page: hero, reader
problem, benefits, steps, optional supported proof, FAQ and an action on the
main website. It has no lead form or lead-capture endpoint. Keep proof absent
when credible supporting material is unavailable.

## Edit customer Git

Use `gomnee_get_campaign_starter` for the versioned manifest, file index, local
content schema and reconstruction instructions. Request each advertised
`filePath` to receive its exact contents; preserve hidden files and nested paths
and verify the file's `sha256`. Require the same `sourceRevision` digest on each
read, restarting from a fresh index if it changes. This digest identifies the
starter contents, not a Git commit. No access to Gomnee's private GitHub
repository is needed. Copy the starter once into the
customer-owned repository using your existing authorized GitHub or local coding
tools. Gomnee's GitHub App reads committed source; it does not write repositories.
For an existing custom site, work with its actual code instead of overwriting it
with a starter.

Read the repository's instructions and current diff first. `content.json`, its
schema, CSS and renderer belong to that repository. Fill required content from
accepted company facts, replace placeholders, choose the correct canonical and
main-site action, and customize the brand. `contentStatus: configured` is a
technical marker, not approval. Keep valid draft content previewable.

Run the repository's nearest meaningful validation and inspect the rendered
page on mobile/desktop with relevant keyboard behavior. Review claims, proof,
page links and indexing settings. Commit through the user's normal Git review
path. Never store provider credentials, tokens, sessions or `.env` files in
source. Template upgrades are optional reviewed diffs; preserve custom edits.

## Preview, domain and explicit publication

1. Use `gomnee_register_campaign_site` to register a new supporting origin when
   needed. Registration is not proof of ownership, hosting or traffic.
2. Complete the first read-only GitHub authorization in Sites. For a new campaign,
   use `gomnee_connect_campaign_hosting` with its registered `networkSiteId`, a new
   hosting `siteId`, and `sourceSiteId` from an already connected hosted site in
   this workspace. Keep those identifiers on retries. Use
   `gomnee_list_site_repositories` to select only a repository authorized by that
   GitHub App installation; newly added repositories need selected-repository access.
3. Use `gomnee_review_site_source`, then `gomnee_configure_site_source` with the
   exact returned source/profile/version fields. Inspect the actual repository;
   the starter manifest does not bypass source or build-profile validation.
4. Use `gomnee_deploy_site_preview` to request a durable build of that exact
   committed source, with the `configurationDigest` that
   `gomnee_configure_site_source` returned. A merge to the selected branch does
   not move a hosted site by itself. Read current state through `gomnee_get_site`. Pending,
   failed, ready and live are different states; retry only through returned
   recovery guidance and preserve command IDs for identical retries.
5. Review the immutable candidate URL and the selected hostname. Use
   `gomnee_prepare_site_domain` for non-routing preparation. Domain purchase and
   DNS mutations require their own authority; preparation does not publish.
   Supporting domains require the returned workspace-specific TXT record before
   domain assignment. Keep that public record for later updates/recovery; a source
   reconnection renews it. Shared provider ownership and optional tracking proof
   do not replace hosting authority.
   For a public root domain such as `example.com`, the person may explicitly
   select `includeWwwRedirect: true` to prepare `www.example.com` as a permanent
   308 redirect to the root, preserving page paths and query parameters. This
   remains one hosted website. Read `domainConfiguration.redirectHostname` and
   the DNS instructions for both addresses. Existing single-address sites do
   not gain a redirect through reads, previews or ordinary publication; an
   already paired site must retain `includeWwwRedirect: true` on preparation.
   Arbitrary subdomains and private platform hostnames cannot gain an inferred
   www alias. Preparation keeps existing traffic in place, including a legacy
   www redirect on another project; it is not migration completion.
6. On the person's explicit publication request, use `gomnee_publish_site` with
   the exact candidate and current versions. Read back the resulting site state
   and live URL. A tool dispatch, successful build or preview is not a live pass.
   A paired publication requires both the root deployment and the exact www
   redirect to pass HTTPS verification. An existing live website still needs a
   reviewed, marker-bearing candidate before publishing a newly prepared pair;
   build a new preview when no eligible candidate exists. Keep the old serving
   targets until both addresses are confirmed. Partial or unknown effects must
   use the original operation's recovery rather than a new publication.

For an explicitly requested rollback, use `gomnee_restore_site` with a retained
deployment belonging to that same site. Restoration changes the live website.
For paired addresses, choose only a retained deployment with
`identityVerified: true`. Older deployments without that exact routing proof
remain in history but cannot restore a pair; build and publish a fresh verified
preview to establish a verified revision. It becomes a restore point only after
a later explicitly approved publication replaces it.
`gomnee_disconnect_site_source` detaches this site's future source reads while
retaining the shared GitHub grant and sibling bindings. Its existing live
website remains served. Hosting
operations never approve or publish a Gomnee Article through its CMS destination.

If a dispatched operation remains uncertain after its job stops, new hosting
commands stay blocked. Read the exact operation ID, prior job ID and current site
version. Only on the person's explicit instruction, use
`gomnee_reconcile_site_operation` with confirmation
`resume_original_hosting_operation`. This resumes the same intent and may finish
its original build, publication or restoration; it is not a read-only status
check. Read back the outcome and never start a different command to bypass the
unresolved operation. Missing provider/source authority needs its stated recovery,
not repeated blind resumes.

## Optional network measurement

Read `gomnee_get_website_network` for the exact source, immutable links and public
installation instructions. `gomnee_manage_site_tracking` exposes only the
bounded available tracking operations such as creating a link, verifying control
and setting collection. Respect each operation's Owner/version requirements.

Commit the returned public proof file at the fixed verification path, deploy it
to the exact origin, explicitly verify it, and enable collection separately.
Use the current public network-v2 script and notice for this installation. In
the starter, `gomnee.public.json` remains null until that information exists.
Do not duplicate the loader or treat existing hosted-v1 counts as v2 arrivals.

Create the registered supporting-root-to-main-action link and copy its complete
returned URL into the primary action. Do not fabricate a link ID. The main
destination needs its own collection enabled to observe tagged arrivals.
Stopping collection and deleting retained observations are distinct actions;
do not substitute a source edit for an immediate stop.

## Improve one reviewed version at a time

Read the current live commit and relevant
`gomnee_get_website_network_activity` window before proposing changes. Combine
source-labelled observations with the accepted company/Strategy basis. Views,
clicks and main-site arrivals are independent counts, not unique people, funnel
conversion, revenue or proof of causation.

Agree on a concrete revision, make an ordinary Git diff, validate it, stage the
new commit and review its candidate. Explicitly publish only when requested.
Do not run an autonomous optimizer, declare experiment winners from these
counts or publish on a model's authority. Report source changes, deployment
state and actual acceptance separately.
