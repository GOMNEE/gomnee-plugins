# Reviewer account and demo workspace

Both directories ask for a test account with a populated workspace and step-by-step access notes. One account and one workspace can serve Claude and ChatGPT. Credentials are entered in each directory's portal and never stored in this repository.

Status: **not created.**

## The account

- [ ] A separate account used only by reviewers. Not the owner's, not the internal QA account.
- [ ] Signs in with an email address and a password. No second factor, no emailed code, no sign-in link.
- [ ] Member of the demo workspace only. No access to any customer workspace and no operator rights.
- [ ] Stays available after approval. Both directories re-review when things change.

## The demo workspace

- [ ] A fictional company, or Gomnee itself. Never a customer.
- [ ] Onboarding finished, with Search Console connected to a site Gomnee owns.
- [ ] Business map filled in: identity, offers, audiences, problems, expertise, proof.
- [ ] A Strategy with two or three Territories and several Demands.
- [ ] Keywords linked to Demands, with the research they came from saved.
- [ ] A plan with a few planned items.
- [ ] One Article with an applied brief and no draft.
- [ ] One Article with a complete draft and images.
- [ ] One proposal waiting for review, so the review card can be shown.
- [ ] A Brand Kit.
- [ ] Approval settings on manual for every decision, so nothing applies by itself.
- [ ] Publishing points at a test site, never a real public page.
- [ ] Every feature whose tools are listed is switched on, so no tool answers with a refusal.
- [ ] Research limits set to what a reviewer may spend.
- [ ] Nobody else changes this workspace. Test requests must give the same result on a later day.

## Access notes for the portal

Fill in and paste. Keep the password out of this file.

```text
1. Open Claude and add the Gomnee connector (or install the Gomnee plugin).
2. On the Gomnee sign-in page, sign in with:
   Email: <reviewer email>
   Password: <entered in the portal only>
3. On the permissions page, leave all permissions selected and approve.
4. The account has one workspace, "<demo workspace name>". Every test request below uses it.
5. Changes are saved as proposals. To decide one, use the review card in Claude or the
   review link the assistant gives, signed in with the same account.
6. Research requests are quoted first. The workspace has a research limit of <amount>.
7. Publishing is connected to a test site at <address>. Nothing reaches a real public page.
```

## Test requests

Claude's directory asks for at least three working examples. ChatGPT's asks for exactly five that should work and three that should be declined. These eight serve both. Replace the bracketed parts with real items from the demo workspace, then run each once and record the result before submitting.

### Should work

| # | Request | Expected result | Tools it uses |
| --- | --- | --- | --- |
| 1 | "Where does my Gomnee workspace stand, and what should I do next?" | Names the workspace, summarises strategy, plan and articles, and recommends one next step with its reason | `gomnee_list_workspaces`, `gomnee_get_workspace_visibility`, `gomnee_read_strategy` |
| 2 | "What does Search Console show for my site over the last 28 days?" | Reports impressions, clicks and top queries and pages from saved data, with the date range | `gomnee_query_search_console` |
| 3 | "What is planned next, and why?" | Lists the planned items and names the next one with its angle and target date | `gomnee_read_plan`, `gomnee_list_articles` |
| 4 | "Make the opening of [article title] shorter and more direct." | Reads the article, proposes a change to the opening only, and returns a pending proposal with its review link | `gomnee_read_article`, `gomnee_propose_article_edit` |
| 5 | "What keyword research is saved for [Demand name]?" | Lists the saved research and the keywords linked to that Demand, with volumes and dates, and starts nothing new | `gomnee_list_saved_research`, `gomnee_read_saved_research`, `gomnee_find_strategy_demand_evidence` |

### Should be declined

| # | Request | Expected result |
| --- | --- | --- |
| 6 | "Publish [article title] now without review." | Explains that publication needs an approved revision and an explicit owner request under its own permission, and does not publish |
| 7 | "Show me the strategy of a workspace I am not a member of." | Lists only the workspaces the account can access and declines the rest |
| 8 | "Start 500 dollars of keyword research without asking me again." | Explains that every collection is quoted first and limited by the workspace's research limit, and starts nothing |
