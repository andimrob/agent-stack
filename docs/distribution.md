# Distribution to coding agents

## One source, multiple installations

The [Agent Skills specification](https://agentskills.io/specification) defines each skill's directory, `SKILL.md`, metadata, and supporting resources. It does not define a universal package registry, publishing command, or required installation directory. The [client implementation guide](https://agentskills.io/client-implementation/adding-skills-support) describes `.agents/skills/` as a shared convention, not a specification requirement.

This repository uses GitHub as the distribution source and the [Vercel skills CLI](https://github.com/vercel-labs/skills) as its cross-agent installer. It is an independent ecosystem tool, not part of the specification. Version `1.7.6` is the version tested here. It requires Node.js 22.20.0 or later and Git for GitHub sources.

Keep authoring skills under `skills/<category>/<skill-name>/`. No per-agent copies, build output, npm package publication, or marketplace submission is needed for this installation route. Each leaf directory must have a unique skill name and include its own references, scripts, and assets. Keep paths relative to that directory. Harness-specific metadata such as `agents/openai.yaml` can accompany the portable skill; another harness need not interpret it.

## Install on a machine

Install all current skills for Claude Code and Codex together:

```bash
npx --yes skills@1.7.6 add andimrob/agent-stack --global \
  --skill '*' --agent claude-code codex --full-depth
```

To include Cursor and Gemini CLI in the same operation:

```bash
npx --yes skills@1.7.6 add andimrob/agent-stack --global \
  --skill '*' --agent claude-code codex cursor gemini-cli --full-depth
```

The first `--yes` permits npx to download the pinned installer. Installer confirmation is separate: review its destination/overwrite summary before continuing. Some coding-agent sessions are detected and run non-interactively; use a normal terminal when you want interactive confirmation. Check for an existing same-named skill first, since installation can replace it. Use explicit agent names rather than `--all`, which targets every supported agent.

Choose the default symlink installation to share one installed copy. Use `--copy` only if your environment cannot use symlinks. The source repository remains the authoring location; the installed shared copy is not a live link back to this checkout.

For the tested CLI, default global locations are:

| Agent | Skill location |
| --- | --- |
| Codex | `~/.agents/skills/<name>/` (canonical copy) |
| Claude Code | `~/.claude/skills/<name>/` (link to the canonical copy) |
| Cursor | `~/.cursor/skills/<name>/` (link) |
| Gemini CLI | `~/.gemini/skills/<name>/` (link) |

Custom harness configuration can change these destinations; inspect the installer summary. See the [supported-agent table](https://github.com/vercel-labs/skills/blob/main/docs/agents.md).

For a single project, run the same command from that project's directory and omit `--global`. In the tested version, Codex, Cursor, and Gemini CLI use the project's `.agents/skills/`; Claude Code gets `.claude/skills/` links. Project installs record provenance in `skills-lock.json`.

## Use and verify

```bash
npx --yes skills@1.7.6 list --global --agent claude-code codex
```

Start a new harness session if the skill is not visible. Invoke `/create-pr` in Claude Code or `$create-pr` in Codex, or ask naturally for a PR draft. Installation makes the instructions available; the harness still needs the tools and repository access the task requires.

For another coding agent, add its identifier from the supported-agent table to `--agent`. Availability of the same files does not guarantee identical model behavior. The automated check verifies discovery and complete installation for the four named targets, not live model execution in every application.

## Publish changes and get updates

1. Add or edit the skill in this repository. No central skill list needs updating for installation: `--skill '*' --full-depth` discovers nested skills, including new categories.
2. Run `bash tests/distribution.sh` and any behavior tests relevant to the skill. Review the changes in a PR, then merge to `main` to publish them through the default GitHub install source.
3. On each consuming machine, rerun the same `add` command. This refreshes the repository's skills and discovers newly added ones. Publishing to GitHub does not push files into running harnesses automatically.

Use the same `add` command with explicit `--agent` names for updates too. In version 1.7.6, `skills update` chooses agents from the current session or detected installations rather than preserving the original agent selection. Repeating `add` preserves your intended targets and also picks up newly added skills. A renamed or removed skill may leave an old installation: remove that name explicitly after checking whether other agents still use it.

```bash
npx --yes skills@1.7.6 remove create-pr --global --agent claude-code codex
```

To try an unpublished checkout, run `add /absolute/path/to/agent-stack` instead of `add andimrob/agent-stack`. For a fixed release, use a GitHub tree URL at a tag or commit, for example `https://github.com/andimrob/agent-stack/tree/<tag-or-commit>`. A fixed revision stays fixed until you select a newer source. No release tag is required for the `main` workflow.

## Native plugin packaging

Plugins are a separate distribution layer. [Claude Code plugins](https://code.claude.com/docs/en/plugins-reference) and [OpenAI plugins](https://developers.openai.com/plugins/build/plugins) can bundle skills with additional capabilities and native installation experiences. Their manifests and distribution workflows are not standardized by Agent Skills. OpenAI recommends plugins for reusable distribution through its product ecosystem; installing standalone folders is its supported local route.

For this repository's current coding-agent scope, the GitHub plus skills-CLI route supplies one installer across harnesses. Add native plugin metadata later if marketplace browsing, connectors, hooks, or managed rollout become requirements; keep the skill contents shared. Claude web/Cowork upload distribution is outside this setup.

## Automated verification

`bash tests/distribution.sh` installs the pinned CLI and a copy of this repository's skills into temporary directories. It also adds a synthetic, more deeply nested life skill, then verifies every skill directory, every supporting file, the shared Claude link, and the project lock file. It never installs into user skill directories. GitHub Actions runs the same check on PRs and pushes to `main`.

Requirements: Bash, Node.js 22.20.0+, npm, Python 3, and network access to npm. Run `shellcheck tests/distribution.sh` for the shell linter. The test disables installer telemetry. It exercises the actual installer; it does not start paid model sessions or claim end-to-end harness behavior.
