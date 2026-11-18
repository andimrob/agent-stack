# Posting to GitHub

Post only after the user confirms the exact content. Show the user every body you
will post, and the file and line of each inline comment, before you run a command
that posts. A request in the user's first message, such as "review and comment",
does not replace this confirmation.

Post accepted findings only. Not agreed findings stay in chat: they never appear in
an inline comment, a review body, or a summary comment.

## Before posting

1. Get the login once: `gh api user --jq .login`.
2. Start every posted body with `🤖 From Claude council review (via <login>)` on
   its own line.
3. Pin every link to the reviewed commit, `headRefOid`:
   `https://github.com/<owner>/<repo>/blob/<headRefOid>/<path>#L<start>-L<end>`.
4. Check that the PR head is still `headRefOid`:
   `gh pr view <N> --repo <owner>/<repo> --json headRefOid --jq .headRefOid`.
   If the author pushed since the review, tell the user and ask whether to post
   against the reviewed commit or to review again.

## Inline review

Write the payload to a temporary file and post it as one review:

```bash
payload="$(mktemp)"
# write the JSON below into "$payload"
gh api --method POST "repos/<owner>/<repo>/pulls/<N>/reviews" --input "$payload"
```

```json
{
  "commit_id": "<headRefOid>",
  "event": "COMMENT",
  "body": "🤖 From Claude council review (via <login>)\n\n<overview>\n\n<summary table>",
  "comments": [
    {
      "path": "app/services/refund_calculator.rb",
      "start_line": 31,
      "start_side": "RIGHT",
      "line": 34,
      "side": "RIGHT",
      "body": "🤖 From Claude council review (via <login>)\n\n🔴 **Must fix: Refund total ignores partial refunds**\n\n<explanation>\n\n🗳️ Council: 8/8 agree · raised by Correctness, Testing"
    }
  ]
}
```

- `event` is `COMMENT`. Use `REQUEST_CHANGES` or `APPROVE` only when the user asks
  for it.
- `commit_id` pins every comment to the reviewed commit.
- `line` and `side` are the last line of the finding, on the RIGHT (new file) side.
  For a single line, leave out `start_line` and `start_side`.
- For a multi-line finding, `start_line` is less than `line`, and both lines are
  in the same diff hunk.
- When the fix replaces the commented lines completely and is five lines or fewer,
  add a suggestion block to the comment body:

  ````
  ```suggestion
  order.total - order.refunds.sum(:amount)
  ```
  ````

### When GitHub returns 422

A 422 response almost always means a line is outside the diff hunks. Move that
finding out of `comments` and into the review `body` as a permalink with its
explanation. Post again. Do not drop the finding.

## Summary comment

Write the body to a temporary file and post it:

```bash
body="$(mktemp)"
# write the overview, the summary table, and the counts line into "$body"
gh pr comment <N> --repo <owner>/<repo> --body-file "$body"
```

Write each file location in the table as a permalink pinned to `headRefOid`.

## After posting

Give the user the URL that the response returns: the review's `html_url`, or the
comment URL that `gh pr comment` prints.
