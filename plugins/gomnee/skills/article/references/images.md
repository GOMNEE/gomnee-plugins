# Images

Gomnee can host an image you already have and return a stable public address for the Article. It does not generate images here.

Two facts shape this stage: **hosting is public at once**, and **rights are declared on the person's behalf**. Neither is undone by editing the Article.

## What to show

```text
Does the Article state something the site itself can show?
├── Yes → a real screenshot of the site's own page, or a chart of the site's own
│         figures. This is also first-hand evidence. Best choice.
├── No, but a diagram would explain a method or comparison
│       → draw it with the Brand Kit's palette and fonts (gomnee_get_brand_kit).
└── Neither → ask the person for an image. Do not add a decorative stock image
              to pass a check.
```

Never use an image whose source you cannot name.

## Hero, inline and cover

| | Hero | Inline | Cover |
| --- | --- | --- | --- |
| Where it shows | At the top of the Article | Inside one section | On the Article's card in the blog index |
| How it is set | In the draft's media | In the draft's media, tied to a section | A separate proposal: [article-covers.md](article-covers.md) |
| Alt text | What the image shows | What the image shows | Leads with the topic |

## Steps

1. **Decide the role of each image:** one hero, and inline images tied to their sections.
2. **Confirm rights with the person, for each image.** Ask: is it owned or licensed, and what credit line, if any? Do not decide this yourself.
3. **Prepare the file** as PNG, JPEG or WebP. Convert large images to WebP to keep them small.
4. **Host it** with `gomnee_host_image`, following its description for sending the file. If you cannot send the file, the tool returns a signed-in upload link for the person; call again with the same command ID to get the saved address.
5. **Tell the person the image is now public.** Hosting does not change, approve or publish the Article, but anyone can read the address from this moment.
6. **Place the image in the draft's media** with the address exactly as returned, the verified dimensions from the hosting result, alt text, an optional caption and the credit. A screenshot used as evidence is also referenced from the draft's verification excerpts.
7. **Submit the change** with `gomnee_submit_article_proposal`. Changes to media go through the whole-draft proposal.
8. **Prepare the cover before the first approval.** Saving a cover creates a new unapproved revision, so doing it early means the person approves once.
9. **Read the quality report again** and confirm the image finding has cleared.

## Alt text and captions

- Alt text says what is in the image, in the Article's language, in one sentence. No "image of".
- For a chart, state the finding, not the chart type.
- A caption adds what the alt text does not: the date, the source, what to notice.
- A screenshot of the site's own page gets the date it was taken.
- Mark an image decorative only when it carries no information.

## Where the site puts images

Placement and required size belong to the site's template, not to Gomnee. Check on the person's own site how the hero and inline images appear and what width looks right before relying on it.

## Checks

- The person confirmed rights for every image before it was hosted.
- Every address is exactly the one returned.
- Every image has real alt text or is truly decorative.
- A screenshot shows the page as it is today, with nothing private in it.
- The Article is still unapproved and unpublished.

## Do not

- Do not host an image before the person confirms rights.
- Do not use a stock or generated image as if it were first-hand evidence.
- Do not host a screenshot that shows private data, another person's account or an unpublished page.
- Do not shorten or rewrite the returned address.
- Do not add a decorative image only to clear a finding.
- Do not pass image data or tokens through chat text.
