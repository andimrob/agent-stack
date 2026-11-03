# agent-stack

My personal agent skills, harness customizations, and experiments, for development and everyday life. Previously named `agent-dev-stack`.

## Skills

- [`skills/development/create-pr`](skills/development/create-pr/SKILL.md): prepare, create, or update a pull request in my writing style, with consistent formatting and accurate validation notes.
- [`skills/life`](skills/life/README.md): space for everyday-life skills as they are added.

Each skill lives in `skills/<category>/<skill-name>/` and has its own `SKILL.md`. Category directories are organizational; they are not skills themselves.

## Install in multiple coding agents

With Node.js 22.20.0+ and Git installed:

```bash
npx --yes skills@1.7.6 add andimrob/agent-stack --global \
  --skill '*' --agent claude-code codex --full-depth
```

Add `cursor gemini-cli` after `codex` to target those agents too. This installs the same skills into each selected harness; no separate skill versions are needed. Inspect destinations and any same-name replacements before installing. The CLI can run non-interactively when it detects a coding agent.

Merge skill changes to `main` to publish them, then rerun the command on each machine to refresh existing skills and discover new ones. Updates are explicit, not pushed automatically into running harnesses.

See [distribution](docs/distribution.md) for project installs, updates, removal, fixed revisions, supported paths, and the distinction between Agent Skills and native plugins.

Keep skill names unique across categories. Bundle references and helpers with the skill that needs them, using relative paths so a skill can be used on its own. Add further categories only when actual skills need them.

This is a public repository. Examples are synthetic; private work artifacts, personal records, and credentials belong outside it.

## Contributing

See [AGENTS.md](AGENTS.md) for conventions and [the create-pr scenarios](tests/create-pr.md) for behavioral checks. Run `bash tests/distribution.sh` to verify multi-agent installation and `shellcheck tests/distribution.sh` to lint the test. There is no application build step.
