# Working in agent-stack

This repository holds personal agent skills and related customizations. Keep each skill portable and self-contained under `skills/<category>/<skill-name>/`. Development skills belong in `skills/development`; everyday-life skills belong in `skills/life`.

- Use lowercase `rob/` for new branches; do not rename existing branches just to apply it.
- Use conventional commit messages and PR titles.
- Link related Jira tickets in PR descriptions as `/task <full Jira ticket URL>`.
- For code changes, write a failing test first and then implement the behavior. Run the appropriate linter before committing: RuboCop for Ruby, Prettier and ESLint for JavaScript/TypeScript, or the configured project linter for other languages.
- For skill changes, run a realistic scenario before and after the change. Keep facts about tests run separate from proposed checks. Re-run relevant scenarios when the instructions change.
- Keep public examples synthetic. Do not copy private PR bodies, internal links, or personal records into this repository.
- Preserve explicit user instructions and existing authorization. A skill does not authorize unrelated actions or sending messages.

For distribution changes or new skills, run `bash tests/distribution.sh` and `shellcheck tests/distribution.sh`. The check installs into temporary project directories, never user skill directories. Keep the tested skills-CLI version aligned between the test and installation docs. Validate skill metadata and relative links, run relevant behavioral scenarios, and check `git diff --check` for documentation changes.
