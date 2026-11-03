---
name: create-pr
description: Use when Rob asks to prepare, draft, create, or update a GitHub pull request or its title and description. Does not apply to reviewing someone else's PR or merging a PR.
---

# Create PR

Write for a reviewer who has not read the conversation. Read [writing-style.md](references/writing-style.md) when drafting; it separates observed voice from explicit conventions.

## Establish the actual change

Read applicable repository instructions and PR templates. Inspect the working tree, branch, remotes, intended base, commits, and full diff against that base. Check for an existing PR for the head/base before creating one. Use the intended base for stacked or release work; do not assume the default branch.

Describe the final change: the concrete problem, resulting behavior, and any tradeoff the reviewer needs to assess. Use current validation output. Report failures, skipped checks, and checks not run accurately. Run relevant checks when authorized and feasible; never turn a proposed test into a completed test.

## Write the title and body

Use a conventional title: `fix: ...`, `feat: ...`, `docs: ...`, or another appropriate type; add a scope when it clarifies the change. Commit messages use the same convention. New branches use lowercase `rob/`; keep existing branch names.

Follow the repository's PR template, preserving required fields. When there is no template, use this order:

1. `**Summary of changes**:` followed by a short paragraph explaining what changed and why. Add details only when they help review.
2. Each related Jira ticket on its own line as `/task <full Jira ticket URL>`.
3. `**Testing Done**:` followed by the checks actually run and their results, including material limitations.

Omit ticket lines when there is no related ticket. If only a ticket key is known, resolve its full URL from supplied or connected context; flag it as unresolved if that fails. Do not guess the tracker host or leave an empty `/task` line. Place ticket lines in the template's ticket field when it has one.

Scale detail to the change. Small changes usually need one paragraph plus testing; complex changes may need bullets or further sections. If scope changed, rewrite the title and description around the final diff. Preserve required repository fields and separately managed bot sections when updating an existing PR.

## Create or update

A request to draft ends with the title and body. A request to create or update authorizes that action within the specified repository and branch; complete preparation before asking about any genuinely unresolved target. This skill does not authorize merging, unrelated edits, or messages to other people.

Use a structured GitHub tool when available. With `gh`, write the exact body to a temporary UTF-8 file and pass `--body-file` to preserve Markdown and avoid shell interpolation. Verify repository, head, base, title, body, and draft status before writing. Honor a requested draft status; for an unspecified new PR, create a draft and say so.

After writing, read the PR back and report its URL. If a write times out, check whether it succeeded before retrying; if the outcome stays unknown, report that and stop further writes.
