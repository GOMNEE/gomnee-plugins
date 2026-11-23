---
name: feedback
description: Report a problem or a missing capability in Gomnee in a form the Gomnee team can act on. Use the moment a Gomnee tool returns an error that does not name its real cause, a step needs trial and error, a result cannot be read or cited, or you had to work outside Gomnee, and for "report this to Gomnee", "log this bug", "tell Gomnee about this", "Gomnee got this wrong".
---

# Feedback

Agents meet Gomnee's rough edges before people do. Each one written down once, with the exact call and answer, saves everyone else the same detour.

This skill writes a report for the person to send to Gomnee at `support@gomnee.com`. It changes nothing in Gomnee and sends nothing by itself.

## When to report

Write a report as soon as one of these happens. Do not wait for the end of the task.

| Signal | Example |
| --- | --- |
| A refusal names a cause you can check is false | "The Article changed", but a fresh read shows it did not |
| A refusal gives no next step | A failed read with no detail |
| A state reads as failure but is only waiting | A job shown as failed that later succeeds |
| Two tools disagree | Two different states for the same item |
| The right input had to be found by trial | A form no description explains |
| A result is too large to read or cannot be cited | Results you cannot refer to |
| You left Gomnee to finish the step | A manual check or an outside search |
| Something was stored as if a person chose it | Settings nobody entered |

Do not report your own mistakes, a correct refusal with a clear message, or anything about the person's site instead of about Gomnee.

## Steps

1. **Check once, cheaply.** Repeat the call only if it is free and changes nothing. Never repeat a paid start, a proposal, an approval or a publication to confirm a problem.
2. **Decide the kind.** A defect or unclear behaviour is a **problem**. A capability that does not exist is a **wish**.
3. **Rate a problem:**

   | Level | Meaning |
   | --- | --- |
   | Blocks | The task cannot be finished |
   | Costs time | A wrong first attempt or a detour |
   | Unclear | Wording or documentation |

4. **Write the report** in the format below. Facts only: the call, the answer, the date.
5. **Say what you did instead,** and whether it worked.
6. **Show the report to the person** and ask them to email it to `support@gomnee.com`. Give it as one block they can copy, with a subject line: "Gomnee feedback: <the one line>". When you have a working folder, also append it to `gomnee-feedback.md` there, so reports from one session stay together.
7. **Carry on** with the task when a way around exists. Tell the person at once when the problem blocks the work.

## Report format

```markdown
### <Problem | Wish> · <Blocks | Costs time | Unclear> · <one line>

Found <YYYY-MM-DD>. <Reproducible | Seen once>. Request reference: <if the answer gave one>.

Before the call: <what was true: what existed, the approval settings>.

1. `<tool>` with <the inputs that matter> answered <the exact code>: "<the exact message>".
2. <the check that shows the stated cause is wrong, if any>.

What an agent concludes from this, and why that is wrong or costly: <one paragraph>.

What I did instead: <the way around, and whether it worked | nothing>.

Smallest fix that would have prevented it: <one suggestion>.
```

For a wish, replace the numbered calls with what you had to do without the capability. That cost is the important part.

Rules for the text:

- Quote codes and messages exactly.
- One problem per report.
- No blame and no adjectives. "Answers `service_unavailable` for an out-of-range page" is enough.
- Label a guess as "probable cause".

## Checks

- Someone who has never seen the workspace can reproduce it.
- It names the exact tool, the exact answer and the date.
- It contains no secret, token, personal data or Article text. Item references are fine.

## What the person decides

- Whether to send the report.
- Whether a blocking problem stops the work.

## Do not

- Do not spend money or submit anything to reproduce a problem.
- Do not retry a failed paid job with a new operation ID to see what happens.
- Do not send the report anywhere yourself, even when you have an email tool. The person sends it.
- Do not mix tasks about the person's site into the report.
