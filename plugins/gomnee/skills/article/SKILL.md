---
name: article
description: Write, edit or continue an Article in Gomnee, from a planned item through brief, draft, images and review. Use for "write the next article", "write the brief", "draft it", "add an image", "change the title of this post", "fix the review findings", "is it ready to approve", "publish it", or a saved Article proposal waiting for review. Also covers edits to old articles imported from a CMS.
---

# Article

An Article runs through five stages. Each ends with something the person decides.

| Stage | You produce | The person decides |
| --- | --- | --- |
| Brief | What the Article is for, its sections and its evidence | Whether the brief is right |
| Draft | The complete Article, written from the applied brief | Whether the draft is right |
| Images | Real images with rights, alt text and placement | Rights, and whether each image may be public |
| Review | Fixes for what the checks found | Approval of the exact revision |
| Publish | Nothing, unless asked | Publication, always on explicit request |

A good result is a complete Article a reviewer can approve with few edits, because every claim is supported, the promise is kept and the reader's task is done.

Read [Working with Gomnee](../../references/working-with-gomnee.md) first.

## Find the entry point

| Request and saved state | Start at |
| --- | --- |
| A planned item with no Article | Prepare (step 2), then Brief |
| An applied brief and no draft | Draft |
| A draft without images | Images |
| A change to an existing draft or published Article | Edit (step 12). No new brief unless Gomnee asks for one |
| A saved proposal or review to return to | Read `gomnee_get_proposal_status` first and follow its decision |
| Only the cover | [article-covers.md](references/article-covers.md) |
| An old article imported from a CMS | [imported-cms-articles.md](references/imported-cms-articles.md). Do not pass an imported item to the Article tools |
| Archive or restore | [lifecycle-controls.md](../../references/lifecycle-controls.md), only on the person's explicit instruction |

Enter at the stage that fits. Do not repeat a finished stage.

## Steps

### Find and read

1. **Find the work** with `gomnee_list_articles`, or use the Article or planned item a pasted link names.
2. **Prepare, if needed.** A planned item without an Article needs `gomnee_prepare_article`. It opens the Article and costs nothing.
3. **Read the Article.** `gomnee_read_article` returns the state, the `contextDigest` a proposal needs, how to propose, and the current brief and draft whole. Read its other parts (evidence, sources, internal links, quality checks) by name with `gomnee_read_context_parts`, several in one call.

### Brief

4. **Check the angle before writing.** Verify every factual premise the planned angle rests on against primary sources, above all claims about other companies' products, prices, versions or rules. If a premise is wrong, say so. Reframe within the planned item when it still holds; otherwise recommend changing the planned item.
5. **Research the actual questions.** Use the company's accepted expertise, saved search research and passages from primary sources. Follow [research-and-sources.md](references/research-and-sources.md). Record gaps instead of inventing proof.
6. **Build the brief** from the brief card in [editorial-standard.md](references/editorial-standard.md) and the targets in [house-defaults.md](references/house-defaults.md). Connect the company's expertise to a specific contribution. Choose real pages to link with `gomnee_find_internal_links`. For a tutorial, establish the first-hand evidence, or record that it is written from documentation only.
7. **Submit the brief** with `gomnee_submit_article_proposal` and read the receipt. Do not draft until the brief has been applied.

### Draft

8. **Read the Article again** after the brief is applied.
9. **Write the complete draft from that brief.** A draft keeps the sections its brief gave it, with the same keys in the same order. A change to the structure needs a brief change first, then a new draft. Follow [on-page.md](references/on-page.md), [internal-links.md](references/internal-links.md) and, when the market's language differs from the conversation, [localization.md](references/localization.md).
10. **Submit the draft** with `gomnee_submit_article_proposal`. The receipt lists the checks that did not pass.

### Images

11. **Add real images before review.** Follow [images.md](references/images.md): choose what to show, confirm rights with the person for each image, host it, and place it with alt text. Hosting makes a file public at once, so it needs the person's agreement every time.

### Edit and revise

12. **Change part of a draft with `gomnee_propose_article_edit`.** Give only what changes: fields, the search title or description, the opening, whole sections by key, claims. Everything left out stays as it is. Use `gomnee_submit_article_proposal` for the first draft and for changes to authors, media or citations.
13. **Fix what review found.** `gomnee_get_quality_report` shows the saved revision's findings and how many checks are left. Fix each one you can in a new proposal against a fresh read. For a saved proposal that needs correction, follow [proposal-iteration.md](references/proposal-iteration.md).
14. **Reviewer feedback becomes a new proposal.** Never resend an old base. Withdraw your outdated pending proposals with `gomnee_withdraw_proposal`.

### Approve and publish, only when asked

15. **Approval.** When the person asks for final approval, `gomnee_approve_article` requests it for the exact current revision under the owner's settings. Checks that gate approval must be fixed in a new revision or waived by the person, with their reason, when they sign. Never sign, waive or write a waiver reason for them. An editor's scorecard is guidance and does not gate approval. "Queued for review" is not "approved".
16. **Publication.** Only when the person asked to publish, use `gomnee_publish_article` for the exact approved revision. Read the recorded publication state before saying it is live.

## Writing rules that matter most

- **Nothing invented.** No product capability, customer result, statistic, quote, test, byline or first-person experience that the evidence does not support. If the Article needs proof you do not have, narrow the promise or record the gap in the brief.
- **Answer early.** The opening gives the answer, recommendation or thesis before background.
- **Caveats go to the reviewer, not the reader.** Evidence limits and verification notes belong in the brief's gaps and the draft's cautions. A caveat that changes what a reader should do belongs in the text.
- **Write for the market.** Use its language and conventions, not translated English.
- **Meet the brief.** Never pad, stuff keywords, invent questions or add decorative images to clear a check.

## What the person decides

- Each brief and draft, at its review link, unless the owner's settings apply it.
- Rights for every image, and whether it may be public.
- Approval of the exact revision, and any waiver.
- Publication.

## Do not

- Do not draft before the brief is applied.
- Do not add, remove or reorder a draft's sections.
- Do not turn a requested small edit into a rewrite.
- Do not host an image before the person confirms its rights.
- Do not describe an Article as approved or live unless the saved state says so.
- Do not publish because a draft, an approval or a date exists.

## When something fails

Read the refusal. It names the failing check and what would be accepted. Fix that one thing, read the Article again and resubmit. If the missing step belongs to the owner in Gomnee, explain it and give the link.

## References

- [editorial-standard.md](references/editorial-standard.md): brief card, formats, quality bar. Before the brief and the draft.
- [house-defaults.md](references/house-defaults.md): current house targets and permitted exceptions. Before the brief.
- [research-and-sources.md](references/research-and-sources.md): company knowledge, primary sources, limits. For research or a missing-evidence finding.
- [on-page.md](references/on-page.md): title, summary, headings, metadata. For the draft.
- [internal-links.md](references/internal-links.md): linking to the site's own pages. For the draft.
- [localization.md](references/localization.md): writing for the market. When languages differ.
- [images.md](references/images.md): rights, hosting, placement, alt text. For the images stage.
- [article-covers.md](references/article-covers.md): the listing cover. For a cover.
- [proposal-iteration.md](references/proposal-iteration.md): inspect and correct a saved proposal. For reviewer feedback.
- [imported-cms-articles.md](references/imported-cms-articles.md): old CMS articles. For imported content.
