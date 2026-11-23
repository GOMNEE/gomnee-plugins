# Propose an Article cover

A cover is listing/card artwork. It is separate from the optional body hero
and inline images. Use this flow only when the connected tool advertises the
cover-only form; never place a local path or arbitrary image URL in its source.
It uses existing Article propose and work consent. If the connection lacks a
required permission, follow the host's reconnect/consent path; do not ask for
credentials in chat.

1. **Read the exact Article basis.** Read fresh context and retain the current
   revision ID/digest and owning context digest. An existing revision is
   required. Do not create a new brief or rewrite Article text to add a cover.
2. **Host the selected image explicitly.** When the person's request authorizes
   public hosting and its rights are confirmed, use `gomnee_host_image` with
   one command UUID. Follow the direct-transfer or signed-in upload fallback
   in [on-page.md](on-page.md#images-and-media). Hosting makes this image
   public immediately; it does not change the Article. Read that same command
   until it returns its committed receipt. Do not invent upload links, file
   references or secret values, or ask the person to paste base64.
3. **Submit only the cover change.** Use the cover form that
   `gomnee_submit_article_proposal` describes, with the current context digest
   and one submission UUID. It names the exact base revision, the cover change
   with the hosted image as its source, alternative text and an explanation.
   Copy the source identifiers from that exact hosted receipt; the digest
   identifies the normalized PNG, not the local source design. Write useful
   alternative text. Do not supply a replacement Article body, infer image rights or use
   private Creative/Chat IDs as a hosting receipt.
4. **Return the exact Owner review.** Read the saved receipt and give its
   authenticated review link. The person sees the exact cover and alternative
   text and chooses whether to save it. A pending cover stays pending even
   when the workspace automatically applies ordinary draft proposals. You do
   not operate the human review on their behalf.
5. **Confirm the saved result.** After the recorded Owner decision, read fresh
   Article context. Applying the cover creates a new unapproved revision and
   preserves the other Article content. Earlier editorial approval does not
   transfer. Approval and publication each require their own explicit action.

If the base or hosted image is unavailable or changed, follow the returned
blocker and read fresh state. Keep exact retries on the same command/submission
UUID; a different image or changed proposal needs a new UUID. Do not use a
full-document proposal or another ID to evade manual cover review.

This flow does not expose template generation, rendering or private asset
release through MCP. Generating or editing source artwork happens in the
person's chosen design tool; only a qualified existing hosted PNG can be
proposed here. The older brief/draft proposal forms and ordinary hero/inline
media workflow keep their existing contracts.
