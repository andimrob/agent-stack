# Personal guidance

## Pull Requests

- Follow the repository's documented tracker and PR link format. GitHub Issues, Jira, Asana, and Linear are possible trackers.
- Include full links to related tickets or issues when available; these are normally expected for tracked work.
- Do not invent a ticket or tracker host, or require a new ticket for every PR. If only a key is known and its URL cannot be resolved, state that limitation.
- Use `/task <full Jira ticket URL>` only when the repository's instructions require it. There is no global `/task` requirement.
- Always use Conventional Commits for PR titles (for example, `fix(cache): skip expired entries`).

## Commits

Always use conventional commit style for commit messages (e.g., `fix(cache): skip expired entries`, `feat(queue): retry failed jobs`).

## Branches

- Name new Git branches `rob/<descriptive-change-slug>`, with the lowercase `rob/` prefix.
- Do not add a routine random suffix or use a separate agent prefix.
- Only when that exact name belongs to different work, add a meaningful qualifier or a small collision suffix.
- Keep existing branch names. Do not rename them just to enforce this convention.

## Development Methodology

Always write code using Test-Driven Development (TDD): write failing tests first, then implement the code to make them pass.

## Code Quality

Before committing changes to code, always run the appropriate linter for the language:
- Ruby (`.rb`): rubocop
- JavaScript/TypeScript: prettier and eslint
- Other languages: use the project's configured linter if available

## Code Comments

Do NOT write comments. Write self-documenting code instead — extract well-named
variables, methods, and tests to carry the meaning a comment would. This ban covers
narrative/explanatory comments (restating what a line does, why a change was made, or
where code came from) AND "constraint"/"gotcha" comments: encode the constraint in a
test or a well-named symbol, not prose. The ONLY exceptions are functional pragmas that
tooling requires (e.g. `# rubocop:disable`, `// eslint-disable-next-line`,
`# frozen_string_literal: true`) and a comment the user has explicitly asked for in this
task. When editing existing code, also delete any stray narrative comments you touch.

## Temporary Files

Put temporary files (scratch scripts, screenshots, notes, intermediate outputs) in a `.scratch/` directory at the project root instead of `/tmp`, the session scratchpad, or other system temp directories. Create the directory if it doesn't exist — it is globally gitignored.

## How to Write to Me

Always write your replies to me in ASD-STE100 Simplified Technical English. Apply these
rules:

- Use one meaning for each word, and one part of speech for each word.
- Use approved words. Keep technical names and technical verbs that the domain needs
  (for example `rebase`, `worktree`, `gauge`).
- Write no more than 20 words in an instruction sentence, and no more than 25 words in a
  descriptive sentence.
- Use the active voice. Use the passive voice only when the actor does not matter.
- Use the simple present, past, or future tense. Do not use `-ing` forms, except in a
  technical name.
- Give one instruction in each sentence.
- Include the articles `a`, `an`, and `the`.
- Use no more than three words in a noun cluster.
- Write one topic in each paragraph. Write no more than six sentences in a paragraph.
- Put complex material in a vertical list.
- Do not use idioms, slang, metaphor, or humor.
- Put a warning or a caution before the step that it applies to. Write it as a command.

This rule applies to my chat replies. Code, commit messages, PR bodies, and repository
documents keep the standards in the other sections of this file.
