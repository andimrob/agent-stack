# Personal guidance delivery

## Approved decisions — 2026-11-06

Keep personal guidance, workflow skills, lifecycle hooks, and supporting scripts in this repository. [Personal guidance](../guidance/personal.md) is the portable baseline. Harness-specific adapters stay separate; project rules stay in the project's `AGENTS.md`. Future adapters, hooks, and scripts need no placeholder implementation now.

New branches use `rob/<descriptive-change-slug>`. Add a meaningful qualifier or small collision suffix only when the exact name belongs to different work. Do not routinely add randomness, use an agent-specific prefix, or rename existing branches to impose the convention.

All approved personal preferences apply across harnesses: TDD, language-appropriate linting before commits, Conventional Commit messages and PR titles, code-comment restrictions and their exceptions, project-root `.scratch/` files, and the complete ASD-STE100 chat rules. The chat style does not replace the separate standards for code, commits, PR bodies, or repository documents.

PR tracking is repository-specific. Use full links to known related work in the repository's documented format, whether it uses GitHub Issues, Jira, Asana, or Linear. Do not invent links, assume a host, demand ticket creation for every PR, or impose `/task` globally. A repository can still require `/task <full Jira ticket URL>`. The `create-pr` skill must follow this same rule while preserving repository templates and its outcome-first description format.

## Current route: direct native files

Use one copy of the baseline in each harness's native global guidance file. No new import mechanism, service, plugin, hook, or automatic update is introduced. Native filenames come from the [Claude Code memory documentation](https://code.claude.com/docs/en/memory), [Codex guidance documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md), and [OpenCode rules documentation](https://opencode.ai/docs/rules/).

| Harness | Native destination | Local ownership and adapter |
| --- | --- | --- |
| Claude Code | `~/.claude/CLAUDE.md` | Managed by chezmoi; retains its existing Claude-only `@RTK.md` import after the baseline. |
| Codex | `~/.codex/AGENTS.md` | Managed by chezmoi; direct baseline. Remove the dangling `@RTK.md` import because its local target is absent. |
| OpenCode | `~/.config/opencode/AGENTS.md` | Unmanaged native file; replace the existing link to Claude's guidance with a direct baseline so Claude hook assumptions do not cross harnesses. |

For this machine, the two chezmoi sources are `~/.local/share/chezmoi/home/dot_claude/CLAUDE.md` and `~/.local/share/chezmoi/home/dot_codex/AGENTS.md`. Reconcile both source and native files. Do not apply the entire dotfile repository. OpenCode's configuration has no explicit instruction imports or agent prompt overrides; leave its provider, plugin, permission, and other settings unchanged.

For later manual updates:

1. Review changes to `guidance/personal.md` and inspect each destination for local edits, symlinks, management ownership, and overrides.
2. Preserve unrelated local content. Copy the baseline under the native title, once per destination. Keep harness-only additions outside it. Update any managed source at the same time.
3. Verify every baseline section against the canonical document, resolve symlinks, check management source/native equality, and confirm unrelated settings stayed unchanged.
4. Start fresh harness sessions and check actual context. File equality proves delivery to disk, not live loading or model compliance.

Do not also import the baseline through OpenCode's `instructions` list or a second global file. Its native `AGENTS.md` takes precedence over the Claude global fallback. Codex global overrides can supersede its regular `AGENTS.md`; inspect them before claiming successful loading. Claude's existing RTK hook description remains in its adapter only. No corresponding Codex or OpenCode hook is assumed.

The project-root `.scratch/` convention is already globally ignored on this machine. Keep backups and validation artifacts there. On another machine, verify the ignore configuration before using it. Do not commit private backup files or internal tracker examples.

## Remaining one-day plan

The next phase covers [#5: portable preference delivery](https://github.com/andimrob/agent-stack/issues/5) and [#6: delivery canary](https://github.com/andimrob/agent-stack/issues/6). This reconciliation does not complete either issue.

| Time box | Work | Acceptance |
| --- | --- | --- |
| 1 hour | Define the baseline/adapters boundary, precedence, destination ownership, and rollback contract from this manual route. | One canonical source; no duplicate baseline; private local additions stay private. |
| 3 hours | Implement explicit delivery with tests written first. Cover Claude Code, Codex, and OpenCode native files, managed sources, drift, and existing links. | Preview before writes; idempotent repeat; preserve unrelated content; detect conflicts; restore prior files on failure. No broad dotfile apply or unrequested background update. |
| 2 hours | Add provenance and a harmless delivery canary. Record source revision, content hash, adapter version, destination, and time. | Separate on-disk delivery evidence from observed session context. Exercise stale content, missing files, duplicate loads, and overrides. Do not treat a model's unsupported self-report as proof. |
| 2 hours | Run local acceptance in fresh Claude, Codex, and OpenCode sessions, then test the selected cloud environment. Document results and limits. | Local sessions expose the expected revision/canary once and follow branch, tracker, comment, scratch, and chat-scope fixtures. Cloud receives the same approved baseline through a supported route and passes the same checks without relying on local home files. An unavailable cloud environment remains pending, not passed. |

Cloud destination and supported injection route must be established during that phase. Lifecycle event coverage, plugin packaging, and automatic updates remain later design work unless required by the agreed delivery acceptance. Do not claim cloud support from local tests.

## Verification boundaries

For this reconciliation, check the exact baseline text in all three native files and both managed sources, branch conflict removal, preserved comment exceptions and chat-only scope, and unchanged Claude RTK and OpenCode configuration. Keep the repository's existing project instructions intact.

The tracker change is a repository skill edit. Validate the GitHub, repository-specific Jira `/task`, another-tracker, and unknown-ticket scenarios in [the skill checks](../tests/create-pr.md). Publishing and refreshing the installed skill are separate follow-up actions; local global guidance changes do not update an installed skill automatically.

No claim of fresh-session guidance delivery or cloud acceptance follows from file checks alone. Existing sessions can retain earlier instructions; use fresh sessions for acceptance.

Reconciliation checks on 2026-11-06 passed: all three native files and both chezmoi sources contain the exact portable baseline once; `chezmoi diff` for the two managed targets is empty; no Codex global override exists; the Claude RTK files and OpenCode configuration are unchanged. The comment exceptions, scratch convention, TDD, lint rules, and complete chat-only style section match the original approved text. The public baseline contains generalized examples. OpenCode now has a regular native file rather than a link to Claude's file.

The Codex app supplied the updated global instructions to the active chat after the native file changed. That is observed context evidence for this chat, not proof for every session. Rob's subsequent manual Claude check could not find the expected user/root `CLAUDE.md` in the visible instructions. Claude visibility is unresolved; do not claim successful loading. Fresh OpenCode guidance provenance and cloud acceptance remain unverified. The skill's five tracker draft checks, metadata validation, relative-link checks, distribution smoke check, ShellCheck, and whitespace checks passed. The installed skill still matches the previously published `main`; the revised skill requires publication and a separate refresh.

## Resume handoff — 2026-11-06

Stop after preparing the draft review PR from `rob/shared-personal-guidance` into `main`. Do not continue Claude debugging, change native files, implement hooks/canaries, or refresh the skill in this session.

| Boundary | Preserved state | Next action after review |
| --- | --- | --- |
| `agent-stack` | This PR contains the portable baseline, manual delivery plan, README links, and tracker-neutral PR skill/reference/template/scenarios. | Review and merge separately. The draft branch is reviewable, but default-branch distribution changes only after merge. This is groundwork for #5 and #6, not completion of either issue. |
| chezmoi | The Claude source is modified. The Codex source existed before this task and remains untracked. Other modified config/test files and an untracked branch-prefix test are unrelated. | Keep these local edits. No chezmoi commit, push, or PR is authorized by this publication request. Review that repository separately before any future publication. |
| Native home files | Claude, Codex, and OpenCode guidance files are already updated. Managed Claude/Codex sources match their native files. OpenCode has a direct file instead of a Claude symlink. | Do not repeat the reconciliation merely because the PR is unmerged. First inspect current state and preserve any newer user edits. |
| Installed skill | The prior published `create-pr` payload remains installed; this PR's tracker changes have not been installed. | After merge, explicitly refresh `create-pr` for Claude Code, Codex, and OpenCode, then verify the full payload. |
| Session evidence | This Codex chat received the new guidance. Rob's Claude visibility check failed to show the expected user/root file. OpenCode guidance provenance and cloud acceptance are unverified. | Resume with Claude's actual instruction-source evidence and configuration; do not infer loading from file existence. Then continue the separate delivery/provenance plan. |

The local `.scratch/guidance-reconciliation/` directory retains pre-task file snapshots, a manifest, synthetic draft outputs, and `local-review.md` with task-only cross-repository diffs. These artifacts are ignored and must remain uncommitted: they contain machine-local context. The saved source baselines separate this task from earlier chezmoi edits, including the old agent-specific branch rule and the already-untracked Codex file.

The refresh command for the later post-merge step is:

```bash
npx --yes skills@1.7.6 add andimrob/agent-stack --global \
  --skill create-pr --agent claude-code codex opencode --full-depth
```

Local synchronization, repository publication, installed skill refresh, and live-session proof are separate states. Neither a PR nor matching files proves that Claude loaded the instructions. No cloud delivery, lifecycle hook, or canary implementation is complete.
