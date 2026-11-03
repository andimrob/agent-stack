# Writing in Rob's voice

## Explicit conventions

Rob requires conventional PR titles and commit messages, lowercase `rob/` for new branches, and `/task <full Jira ticket URL>` for related tickets. Existing branches keep their names. These current instructions take precedence over older examples.

## Observed tendencies

A sample of PRs authored by Rob in 2024 used short, practical explanations. Small changes commonly began with “This change…” or “This adjusts…”, then named the behavior and its reason. More involved changes explained the cause and a meaningful implementation choice in a few paragraphs. First person appeared when explaining a decision.

Use those tendencies as defaults, not verbal tics: state the change directly, connect it to the problem, and use concrete names only when they help the reviewer. “This change” is a natural opening, not a required phrase.

The recurring summary and testing labels inform this skill's fallback format. They may partly reflect repository templates, so the target repository's current template wins. The format is a consistent default chosen for this skill, not a claim that Rob always uses it.

## Limits of the evidence

GitHub authorship does not prove who composed every sentence. Recent examples included explicit automation attribution and bot summaries; those were not treated as evidence of Rob's personal voice. Older empty ticket placeholders and repository-specific commands are not portable conventions.

Private source text and internal links are intentionally absent. Use the observed level of detail, not proprietary content. Testing notes should include actual outcomes even when older examples named only a test framework.

## Synthetic small-change example

Title: `fix: skip expired cache entries`

```markdown
**Summary of changes**:
This change skips expired cache entries so readers no longer receive stale results.

/task https://example.atlassian.net/browse/APP-42

**Testing Done**:
`pytest tests/test_cache.py` — 12 passed.
```

The ticket, behavior, and test result above are illustrative, not reusable facts.
