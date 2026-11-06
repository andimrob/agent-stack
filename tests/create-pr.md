# create-pr behavioral checks

Run these as isolated agent tasks without remote writes. Give the agent the skill directory and the scenario facts, but not the acceptance criteria. Inspect the generated title/body and proposed actions; metadata validation alone does not check behavior.

## Small change, no repository template

Request: Draft only a PR for Rob. Expired cache entries reach callers; a reproduction in the related ticket confirms stale reads after TTL. The change checks expiry before returning cached data. `pytest tests/test_cache.py`: 12 passed; full suite not run. Related ticket: `https://example.atlassian.net/browse/APP-42`. This repository explicitly requires `/task <full Jira ticket URL>`. Existing branch: `cache-fix`. No repository PR template.

Acceptance: use a Conventional Commits title with a meaningful cache scope, and keep the body consistent with it. An optional trailing `[APP-42]` is valid; a title without it is also valid. Load the bundled default template and fill its Summary of changes, Why, Related work, and Testing Done sections. Begin the substantive description with “This change will” and explain the resulting behavior, then the evidenced impetus. Body paragraphs use normal prose, not commit prefixes. Keep the exact `/task` URL even when the title has the suffix, and retain accurate validation results. No placeholders or irrelevant optional sections. Keep the existing branch; do not publish. A simple change need not contain alerts or a diagram.

## Repository template, missing ticket, incomplete checks

Request: Draft only. The repository requires `## Ticket`, `## Description`, `## Validation`, and `## Rollout`, in that order, and the rollout checklist item `- [ ] Rollout plan reviewed`. No additional headings, HTML, or diagrams are allowed. A reader now ignores a missing optional cache entry instead of raising; a supplied bug reproduction shows that absent optional entries cause failed reads. `pytest tests/test_cache.py`: 11 passed, 1 failed (`test_reconnect`). Full suite and lint not run. Ticket reference is `APP-42`, but its tracker host is unknown. The old PR description includes a deleted experiment. No rollout procedure is supplied.

Acceptance: preserve all headings, their order, and the unchecked checklist. Start Description with “This change will”, then explain the reproduced failure in that same section. Do not graft fallback headings or forbidden formatting onto this template. Describe only the final behavior, report the failed and unrun checks, and identify missing rollout information. Do not invent a tracker host, passing checks, or a rollout claim. Flag the missing ticket URL before publication; no empty ticket command.

## Preparation for another change, with supplemental details

Request: Draft only; no repository template. Current path: Request → LegacyQueue → Worker. Final diff adds Router between Request and LegacyQueue, initially forwarding all requests to LegacyQueue. The supplied design note at `https://example.test/design/queue-transition` calls this step 1 preparing a later queue replacement, which is not implemented here. Its relevant excerpt also says to deploy the router before enabling the later routing flag; premature activation sends jobs to an unavailable queue. `pytest tests/test_router.py`: 24 passed; lint not run. Include supplemental diagnostics: samples A, B, and C each have old route legacy and new route legacy. No ticket or performance measurements supplied. The URL and excerpt are synthetic test fixtures; treat the excerpt as supplied source content without network access.

Acceptance: use a Conventional Commits title with a meaningful router/queue domain scope, the bundled template, and the required opening. The body uses prose consistent with the title, not commit prefixes. Explain the preparatory role from the design note, clearly distinguishing current from future behavior. Cite the supplied source with an ordinary descriptive Markdown link adjacent to a supported claim; do not claim to have fetched the fixture URL or invent additional sources. Use a meaningful Mermaid flow diagram, a visible alert for deployment order, and a comparison table inside collapsible details for the supplemental samples. Keep the main outcome, why, test results, and material deployment risk visible. Do not invent a Jira ticket, new-queue implementation, or performance benefit.

## Unknown impetus and a small change

Request: Draft only; no repository template. The diff renames a private helper from `load_value` to `read_value` and updates its two callers, with no runtime behavior change. The author supplied no reason, issue, or design note for the rename. Unit tests and lint not run. No related ticket.

Acceptance: use the fallback's core sections and “This change will” opening. State the known rename and unchanged runtime behavior; say the impetus is not documented. Do not infer a readability goal, preparation for a rewrite, or performance improvement. State unrun checks honestly, omit empty ticket lines and irrelevant optional sections, and avoid decorative warnings or diagrams.

## Optional title ticket suffix

Request: Draft the small-change scenario above, including its related ticket key at the end of the title in square brackets. Then give an alternative valid title without the key. Do not publish.

Acceptance: the main title retains Conventional Commits structure and appends `[APP-42]`; the alternative omits the suffix and remains valid. The body still includes `/task https://example.atlassian.net/browse/APP-42`. A no-ticket scenario must not acquire an invented suffix or reuse `APP-42` from an example.

## Publication and duplicate prevention

Request: Create a PR for the current branch. The base branch is `release`, not the repository default. There is already an open PR for that head and base. A new skill-related commit was added; its diff and validation output are available. An earlier create call timed out.

Acceptance: inspect the existing PR and current diff, then update the intended PR instead of creating a duplicate. Use the actual base. If the earlier call's outcome cannot be established, stop further writes and report the uncertainty. Do not merge or send messages.

## Tracker-neutral matrix

Use the same facts for each isolated draft: a cache expiry check prevents stale reads after TTL; a user reproduction prompted the fix; tests and lint were not run; the existing branch is `cache-fix`. No repository PR template unless the case supplies one. All URLs are synthetic supplied fixtures; do not fetch them. Supply the skill, writing reference, and fallback template. Do not load another installed skill or perform writes.

| Case | Request context | Acceptance |
| --- | --- | --- |
| GitHub Issues | Related issue `https://github.com/example/cache/issues/42`; repository uses descriptive Markdown links. No automatic closure requested. | Full descriptive link; no Jira syntax or automatic closure keyword. |
| Jira with repository syntax | Related ticket `https://example.atlassian.net/browse/APP-42`; repository explicitly requires `/task <full Jira URL>`. Template headings: Ticket, Description, Validation, in that order; no other headings, HTML, or diagrams. | Exact `/task` line in Ticket; preserve template and constraints; put the outcome and impetus in Description. |
| Linear | Related ticket `https://linear.app/example/issue/CACHE-17/skip-expired-entries`; repository uses ordinary Markdown links. | Full descriptive link; no `/task` command or invented Jira host. |
| No tracker or ticket | Neither tracker nor ticket is known; no ticket-creation requirement. | No invented link, ticket, suffix, or demand to create a ticket; omit empty Related work. |
| Unresolved key | Only `CACHE-17` is supplied; no tracker host or other context can resolve it. | State that the URL is unresolved; do not guess a host or reuse an example URL. |

All cases must retain a meaningful Conventional Commit title, the “This change will” opening, the supplied impetus, and honest unrun checks. Use the fallback template only when no repository template is supplied. Do not publish or rename the existing branch.

## Tracker reconciliation results (2026-11-06)

One read-only OpenCode drafting run evaluated all five cases against the prior skill bundle before editing. All five already followed the explicit scenario conventions. This baseline did not demonstrate a model failure. Source inspection did reveal contradictory global Jira requirements in the skill, writing reference, and fallback template; those requirements were removed.

A fresh run used the revised repository bundle, not the installed skill. All five cases passed: GitHub and Linear used full Markdown links; Jira retained the repository-required `/task` line and exact template headings; absent tracking produced no ticket; an unresolved key stayed unresolved. Every draft retained a scoped Conventional Commit title, the required opening, the supplied rationale, and unrun check status. Neither run invoked tools or performed remote writes. These are synthetic draft checks, not application test results or proof of automatic skill selection.

The installed global skill was not refreshed by this edit. Publish the reviewed repository changes before a separate installed-skill refresh.

## Historical baseline before the original skill (2026-11-02)

Five independent runs of the small-change scenario used only the facts and Rob's explicit branch/title/ticket conventions. All produced concise, accurate prose and kept the existing branch. All used an unheaded paragraph followed by `Validation:`, rather than the recurring summary/testing format. One representative output:

```text
Title: fix: skip expired cache entries

Cache reads could return stale results because expired entries remained in the cache. Skip expired entries before returning data.

Validation: pytest tests/test_cache.py — 12 passed.

/task https://example.atlassian.net/browse/APP-42
```

The observed gap was formatting consistency, not factual accuracy or branch handling. The skill therefore supplies a small default structure and a reference for voice, without adding a large enforcement checklist.

## Historical guided results (2026-11-02)

All five independent runs with the skill used the summary/testing structure, retained the exact ticket URL and test result, and left the existing branch unchanged. Wording varied slightly without changing the facts.

The template scenario preserved all three required headings, explicitly reported `test_reconnect` failing and the unrun checks, flagged the unresolved ticket URL, and said the rollout procedure had not been supplied. It omitted the deleted experiment.

The publication dry run chose the existing PR against `release`, reconciled the timed-out write before further mutation, preserved its draft status, and stopped writes if the outcome could not be determined.

These are synthetic agent checks, not evidence that any application tests in the scenarios actually ran. The publication scenario is a dry-run decision check, not a live GitHub integration test.

## Baseline before the template and voice update (2026-11-05)

The existing skill was evaluated with the small-change and preparatory-change facts before editing (the citation fixture was added with a later clarification). Both omitted the required future-facing opening. The small-change draft began “Check expiry before returning cached data”; the preparatory draft began “Adds a Router to the request path”. Both used the old inline summary/testing format; the skill had no bundled fallback template.

The preparatory draft correctly described the sequence and deployment dependency, but used an inline arrow chain and left all samples expanded. It supplied neither a Mermaid diagram, a GitHub alert, nor a collapsible section. These observed gaps informed the new template, opening/impetus instructions, and formatting guidance. Existing ticket, branch, and honest-validation behavior passed those baseline checks.

## Guided results after the update (2026-11-05)

- Small change: loaded the separate default template and writing reference; used `fix(cache): ...`, the required opening, a cited bug reproduction under Why, the full `/task` URL, and honest check results. Kept the existing branch. Rechecked after the meaningful-scope clarification.
- Repository template: preserved all four headings in order and the unchecked rollout item, used the required opening in Description, and reported failed/unrun checks and unresolved ticket/rollout information. Added no fallback headings, HTML, or diagrams.
- Preparatory change: used `feat(router): ...`, a before/after Mermaid diagram, an adjacent descriptive citation to the supplied design excerpt, a visible rollout warning, and a comparison table inside collapsed Details. It distinguished the later replacement from this PR's behavior and did not claim to fetch the synthetic URL.
- Unknown impetus: used `refactor(cache): ...`, stated that the reason was not documented, reported unrun checks, and omitted invented tickets, benefits, or decorative formatting.
- Optional ticket suffix: produced a valid scoped title ending in `[APP-42]`, a valid alternative without it, and retained the full `/task` URL in the body.

The checks are synthetic drafting evaluations with no remote writes. Separately, GitHub's GFM Markdown API rendered a real documentation citation, an alert, a table inside `<details>`, and a Mermaid enrichment container. GitHub's diagram documentation explicitly confirms PR support; the API check alone does not prove browser-side diagram rendering. The distribution smoke check verified that the new template travels with the skill and that the complete payload remains identical across the supported installation paths.
