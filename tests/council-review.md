# council-review scenarios

Behavioral checks for [`council-review`](../skills/development/council-review/SKILL.md). Run each scenario against a real PR you may read, and post nothing.

## Small library change with an existing comment

Request: Review a PR of about 100 changed lines in a library, with one existing review comment.

Acceptance:

- All eight members propose in round 1. An empty list from a member is a valid answer.
- No member repeats the point in the existing comment.
- The chair merges duplicate proposals into one ballot finding and keeps every raiser's name.
- Every member votes on every finding in round 2. Only findings with an `object` or `amend` vote go to round 3.
- The report has 🔴 findings before 🟡 findings, a ⚖️ Not agreed list with each objector's reason, and the summary table last.
- Nothing is posted without the user's confirmation.

## Clean PR

Request: Review a PR with no real issues, for example a documentation typo fix.

Acceptance: the report says "The council found no issues it agreed on." and does not invent findings.

## Recorded dry run (2026-10-30)

A live run on a real library PR of about 100 changed lines, with the skill before members carried over between rounds:

- Round 1: four members returned no proposals. Four members returned 7 proposals, which the chair merged into 4 findings.
- Round 2: two findings were accepted 8/8. One finding had one amendment, which corrected its fix. One finding had 3 agree and 5 object.
- Round 3: the amended finding was accepted 8/8. Both members that raised the split finding changed their votes to object, so it was not agreed 0–8.
- Result: 3 accepted recommendations, 1 not agreed, nothing posted.
- Cost: each member used about 100–130k tokens. The slowest round 1 member took about 21 minutes.

The run continued the same member agents into rounds 2 and 3, and each vote took 10–40 seconds. The skill now says to keep each member for every round.

These results come from one PR. They show that the protocol runs end to end, not that its findings are always right.
