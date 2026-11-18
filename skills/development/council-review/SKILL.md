---
name: council-review
description: >
  Review a GitHub pull request with a council of eight expert reviewers who
  deliberate and vote; only findings every member agrees on reach the PR.
  Use when the user says "council review", "review this PR", "review PR 123",
  pastes a pull request URL and asks for a review, or wants feedback on a
  branch that has an open PR before it merges.
compatibility: >
  Needs an authenticated gh CLI and read access to the PR's repository. Runs
  best where the agent can dispatch parallel subagents; without them, play each
  council member in turn in the same context.
---

# Council review

You chair a council of eight reviewers. Each member brings one expertise to the PR.
The council deliberates in rounds, and a finding is accepted only when every member
votes `agree`. You relay between members, merge duplicates, and count votes. You
never add, drop, or overrule a finding on your own.

The council members are Security, Correctness, Testing, Architecture, Design,
Performance, Observability, and Analytics. [council.md](references/council.md) holds each
member's remit.

## Step 1: Resolve the PR

1. Take the PR from the user's message: a number, a URL, or nothing. With nothing,
   use the current branch's PR (`gh pr view --json number`). If there is none, ask.
2. A URL names its own repository. Pass `--repo <owner>/<repo>` to every `gh`
   command, taken from the URL and never from the working directory.
3. Capture the PR metadata:

   ```bash
   gh pr view <N> --repo <owner>/<repo> --json number,url,title,body,state,isDraft,headRefOid,baseRefName,author
   ```

4. Stop on a closed, merged, or draft PR. Say which, and offer to review it anyway.

Done when you hold the PR number, `<owner>/<repo>`, and `headRefOid`.

## Step 2: Build the context pack

Gather this once. Every member gets the same pack, so no member reviews a narrower
picture than another.

- The diff: `gh pr diff <N> --repo <owner>/<repo>`.
- The title and description: author intent decides "wrong or on purpose?".
- The existing comments: `gh pr view <N> --repo <owner>/<repo> --comments`. The
  council does not repeat a point already raised.
- Every `AGENTS.md` and `CLAUDE.md` at the repository root and in each directory
  that holds a changed file.
- A **call-site map**: for every changed function, class, method, or exported
  symbol, search the repository for its callers. Record
  `symbol → caller path:line` with a few lines of context. The diff shows the
  change; the callers show the damage.

When the PR's repository is not checked out locally, read files through
`gh api repos/<owner>/<repo>/contents/<path>?ref=<headRefOid>`.

Done when every changed symbol has an entry in the call-site map, even an entry
that says "no callers".

## Step 3: Deliberate

Read [deliberation.md](references/deliberation.md) now. It holds the round protocol, the proposal,
ballot, and vote formats, and the briefing each member gets. Run its rounds in
order:

1. **Round 1, propose.** Dispatch all eight members in parallel, one subagent each,
   read-only. Each returns its proposals.
2. **Ballot.** Merge duplicate proposals into findings `F1..Fn`.
3. **Round 2, vote.** Every member votes on every finding. Send the task to the
   same eight subagents from round 1.
4. **Round 3, final vote.** Every member votes again on each finding that round 2
   did not settle.

A finding is accepted when every member votes `agree`. A finding that has any
`object` after the last round is **not agreed**.

Done when every finding on the ballot is accepted or not agreed, and you hold each
member's vote and reason for each finding.

## Step 4: Report in chat

Read [report-format.md](references/report-format.md) and write the report in that format. Report
findings with RIGHT-side (new file) line numbers from the diff.

Keep the report to the council's verdict. An empty accepted list is a valid result.

## Step 5: Offer to post

Ask the user what to post:

1. **Nothing**: the review stays in chat.
2. **Inline review** (recommended): one PR review with an inline comment for each
   accepted finding, plus a summary body.
3. **Summary comment**: one PR comment with the overview and the summary table.

Post only after the user confirms the exact content. When the user picks an
option, read [posting.md](references/posting.md) and follow it.
