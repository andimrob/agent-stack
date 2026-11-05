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

Every PR title uses Conventional Commits: `type(scope): summary`, for example `feat(router): add legacy queue routing` or `fix(cache): skip expired entries`. Use a standard type such as `feat`, `fix`, or `docs`; prefer a meaningful scope naming the affected domain or component, following repository conventions. Omit the scope only when no useful one is evident. A PR title may optionally end with a related ticket key in square brackets, such as `fix(cache): skip expired entries [APP-42]`. Use only an evidenced related key; the suffix is optional and supplements the body's full `/task` URL. Commit messages use Conventional Commits too. Keep the body's outcome and rationale consistent with the title; commit syntax belongs in the title, not before every body paragraph. New branches use lowercase `rob/`; keep existing branch names.

Always use the target repository's applicable PR template when one exists. Preserve its section order, headings, required fields, checklists, and constraints. Inspect template locations and repository instructions before deciding there is none. If several templates exist, choose the one applicable to this change using those instructions; resolve any material ambiguity before publication.

When the repository has no PR template, read and fill [the bundled default PR template](assets/default-pr-template.md). Keep its Summary of changes, Why, and Testing Done sections; include its conditional sections when relevant. Replace all drafting instructions and placeholders before publication. Do not apply this fallback's headings to an existing repository template.

Start the substantive description with **“This change will…”**, completing the sentence with what applying or merging the change will do. Then explain **why**: the evidenced bug or request that prompted it, the preparation it enables, or its place in a larger sequence. Ground that impetus in the request, issue, design, or inspected code; do not invent motivation or claim a future step is delivered here. If the impetus is unknown, say so. In a repository template, put these paragraphs in its description field and use its existing rationale field if present; preserve any required material that precedes the description.

Omit ticket lines when there is no related ticket. If only a ticket key is known, resolve its full URL from supplied or connected context; flag it as unresolved if that fails. Do not guess the tracker host or leave an empty `/task` line. Place ticket lines in the template's ticket field when it has one.

Use GitHub-flavored Markdown generously to give the description structure and make it glanceable and comprehensible: tables for comparisons, notes/alerts for consequential notices, Mermaid diagrams for flows, citations supporting claims, collapsible details for supplemental material, and the usual headings, lists, emphasis, and code formatting. Follow [the formatting and citation guidance](references/writing-style.md#github-markdown). Use real, traceable sources and syntax supported in PR bodies. Keep the outcome, impetus, test results, and material risks visible when details are collapsed. Honor the repository template's structure and formatting restrictions.

Scale detail to the change. Small changes can use short sections; complex changes may need bullets, comparisons, and diagrams. If scope changed, rewrite the title and description around the final diff. Preserve required repository fields and separately managed bot sections when updating an existing PR.

## Create or update

A request to draft ends with the title and body. A request to create or update authorizes that action within the specified repository and branch; complete preparation before asking about any genuinely unresolved target. This skill does not authorize merging, unrelated edits, or messages to other people.

Use a structured GitHub tool when available. With `gh`, write the exact body to a temporary UTF-8 file and pass `--body-file` to preserve Markdown and avoid shell interpolation. Verify repository, head, base, title, body, and draft status before writing. Honor a requested draft status; for an unspecified new PR, create a draft and say so.

After writing, read the PR back and report its URL. If a write times out, check whether it succeeded before retrying; if the outcome stays unknown, report that and stop further writes.
