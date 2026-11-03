# agent-stack

My personal agent skills, harness customizations, and experiments, for development and everyday life. Previously named `agent-dev-stack`.

## Skills

- [`skills/development/create-pr`](skills/development/create-pr/SKILL.md): prepare, create, or update a pull request in my writing style, with consistent formatting and accurate validation notes.
- [`skills/life`](skills/life/README.md): space for everyday-life skills as they are added.

Each skill lives in `skills/<category>/<skill-name>/` and has its own `SKILL.md`. Read the leaf skill directly, or install that leaf directory through your agent's supported skill mechanism. Category directories are organizational; they are not skills themselves. Runtime discovery depends on the agent, so cloning this repository alone does not install the skills.

Keep skill names unique across categories. Bundle references and helpers with the skill that needs them, using relative paths so a skill can be used on its own. Add further categories only when actual skills need them.

This is a public repository. Examples are synthetic; private work artifacts, personal records, and credentials belong outside it.

## Contributing

See [AGENTS.md](AGENTS.md) for conventions and [the create-pr scenarios](tests/create-pr.md) for behavioral checks. There is currently no application code, build step, or configured linter.
