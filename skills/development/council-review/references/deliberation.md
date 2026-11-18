# Deliberation

The council deliberates in at most three rounds: propose, vote, final vote. Votes
are **blind within a round** and **open between rounds**: no member sees a peer's
vote from the current round, and every member sees every vote and reason from the
round before.

A finding is accepted only when every member votes `agree` in the same round. You,
the chair, relay and count. You merge duplicates and fold amendments, and you never
add, drop, or overrule a finding.

## Dispatching members

Keep each member for every round. In round 1, dispatch one subagent per member, all
eight in one batch so they run in parallel. In rounds 2 and 3, send the round's
task to the same eight subagents, again in one batch. A member that carries over
keeps the code it already read, so each vote costs a fraction of a fresh review.

When your agent cannot send a message to a finished subagent, dispatch a new one
for that member. Give it the full round 1 brief below, plus its own earlier
proposals and votes, then the current round's task.

Members are read-only: they read files and run read-only `git` and `gh` commands,
and they never post, push, or edit.

The round 1 brief has these parts, in this order:

1. "You are the <member> member of an eight-member code review council for PR
   <url> at commit <headRefOid>."
2. The member's own section of `council.md`, pasted in full, plus the three shared
   questions (real, in scope, worth a comment) from the top of that file.
3. The context pack from Step 2 of the skill, pasted in full or as paths the member
   can read.
4. The round's task and return format, from the round sections below.
5. "Read the code you cite. A finding or vote that rests on the diff alone, when the
   answer lives in a caller or a file outside the diff, is a guess."

Without subagents, play each member in turn. Before each member's turn, re-read its
section of `council.md`. Write the member's full output before you start the next
member, and do not revise an earlier member's output after a later member speaks.

## Round 1: propose

Task: "Review the PR through your remit only. Return at most five proposals, most
severe first. Return an empty list when you find nothing that passes the three
questions."

Return format, one block per proposal:

```
- title: <one line>
  file: <path>
  lines: <RIGHT-side start>-<end>
  severity: must-fix | recommendation
  claim: <what is wrong, in one or two sentences>
  evidence: <the code, caller, or input that proves it>
  fix: <the change to make; a code snippet when it is five lines or fewer>
```

Severity:

- **must-fix**: the PR breaks the build, produces a wrong result, loses or corrupts
  data, opens a security hole, breaks a caller or a downstream consumer, or ships a
  failure nobody can see.
- **recommendation**: a real problem a senior reviewer would raise, which the PR can
  merge without.

## Ballot

Merge proposals that make the same claim about the same code into one finding,
even when they come from different members. Number the findings `F1..Fn`. Each
finding keeps:

- `raised_by`: every member that proposed it.
- The strongest evidence and the most concrete fix from the merged proposals.
- `severity`: the highest severity any raiser proposed. The vote decides the final
  severity.

Two proposals about the same lines that make different claims stay two findings.

## Round 2: vote

Task: "Vote on every finding on the ballot, including the ones you raised. Read the
cited code before each vote."

Return format, one block per finding:

```
- finding: F<n>
  vote: agree | object | amend
  severity: must-fix | recommendation
  reason: <one or two sentences; required for object and amend>
  amendment: <the corrected claim, lines, or fix; amend only>
```

- `agree`: the finding passes all three questions as written. `severity` is the
  highest severity the member accepts for it.
- `object`: the finding fails a question. The reason names the question and the
  proof: a false positive with the code that disproves it, pre-existing code the PR
  did not touch, a point already in the PR comments, or a cost too small to comment
  on.
- `amend`: the finding is real, but its claim, lines, or fix is wrong. The
  amendment gives the corrected version.

### Tally round 2

- Every member votes `agree` → **accepted**.
- Any `object` or `amend` → **unsettled**. Fold every `amend` into a revised
  finding. When two amendments contradict, carry both as variants (`F3a`, `F3b`)
  into round 3.

## Round 3: final vote

Send each member only the unsettled findings, each one with its revised text and
every vote and reason from round 2, attributed by member.

Task: "This is the final vote. Read your peers' reasons. Answer each objection or
amendment that bears on your vote. Vote `agree` or `object`; there is no `amend`
in this round."

Return the round 2 format without `amendment`. The reason is now required for
every vote that differs from the member's round 2 vote.

### Tally round 3

- Every member votes `agree` → **accepted**.
- Any `object` → **not agreed**. Record each objector and its reason for the report.
- When more than one variant of a finding is accepted, keep the variant with the
  lower severity and record the other as not agreed.

## Severity of an accepted finding

An accepted finding takes the lowest severity any member voted for. If one member
votes `agree` at `recommendation` and seven vote `agree` at `must-fix`, the finding
is accepted as a recommendation. This keeps the severity unanimous too.

## Record for the report

For each finding, keep the final text, the accepted severity or "not agreed",
`raised_by`, the members whose amendments were folded in (`amended_by`), and each
member's last vote and reason. The report reads from this record.
