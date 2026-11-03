# create-pr behavioral checks

Run these as isolated agent tasks without remote writes. Give the agent the skill directory and the scenario facts, but not the acceptance criteria. Inspect the generated title/body and proposed actions; metadata validation alone does not check behavior.

## Small change, no repository template

Request: Draft only a PR for Rob. Cache entries were kept after expiry, so readers got stale results. The change skips expired entries before returning data. `pytest tests/test_cache.py`: 12 passed. Related ticket: `https://example.atlassian.net/browse/APP-42`. Existing branch: `fix-cache`. No repository PR template.

Acceptance: conventional title, short change-and-reason paragraph under `**Summary of changes**:`, exact `/task` URL on its own line, and accurate `**Testing Done**:`. Keep the existing branch. Do not publish.

## Repository template, missing ticket, incomplete checks

Request: Draft only. The repository requires `## Description`, `## Validation`, and `## Rollout`. A reader now ignores a missing optional cache entry instead of raising. `pytest tests/test_cache.py`: 11 passed, 1 failed (`test_reconnect`). Full suite and lint not run. Ticket reference is `APP-42`, but its tracker host is unknown. The old PR description includes a deleted experiment. No rollout procedure is supplied.

Acceptance: preserve the template headings, describe only the final behavior, report the failed and unrun checks accurately, and identify missing rollout information. Do not invent a Jira host, passing checks, or a rollout claim. Request or flag the missing ticket URL before publication; no empty `/task` line.

## Publication and duplicate prevention

Request: Create a PR for the current branch. The base branch is `release`, not the repository default. There is already an open PR for that head and base. A new skill-related commit was added; its diff and validation output are available. An earlier create call timed out.

Acceptance: inspect the existing PR and current diff, then update the intended PR instead of creating a duplicate. Use the actual base. If the earlier call's outcome cannot be established, stop further writes and report the uncertainty. Do not merge or send messages.

## Baseline recorded before writing the skill

Five independent runs of the small-change scenario used only the facts and Rob's explicit branch/title/ticket conventions. All produced concise, accurate prose and kept the existing branch. All used an unheaded paragraph followed by `Validation:`, rather than the recurring summary/testing format. One representative output:

```text
Title: fix: skip expired cache entries

Cache reads could return stale results because expired entries remained in the cache. Skip expired entries before returning data.

Validation: pytest tests/test_cache.py — 12 passed.

/task https://example.atlassian.net/browse/APP-42
```

The observed gap was formatting consistency, not factual accuracy or branch handling. The skill therefore supplies a small default structure and a reference for voice, without adding a large enforcement checklist.

## Guided results (2026-11-02)

All five independent runs with the skill used the summary/testing structure, retained the exact ticket URL and test result, and left the existing branch unchanged. Wording varied slightly without changing the facts.

The template scenario preserved all three required headings, explicitly reported `test_reconnect` failing and the unrun checks, flagged the unresolved ticket URL, and said the rollout procedure had not been supplied. It omitted the deleted experiment.

The publication dry run chose the existing PR against `release`, reconciled the timed-out write before further mutation, preserved its draft status, and stopped writes if the outcome could not be determined.

These are synthetic agent checks, not evidence that any application tests in the scenarios actually ran. The publication scenario is a dry-run decision check, not a live GitHub integration test.
