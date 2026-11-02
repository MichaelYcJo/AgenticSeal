# Routing: 1793588973-pr-body-reads-a-details-tag-as-github-does

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | fix/1218-pr-body-refuses-only-an-exact-details-line |

Answered 2026-11-02 by the owner, before the first edit.

## Why this way

The owner pressed automation once for the whole of 0.28.0 and answered that the session squash-merges each pull request into release/v0.28.0 once its CI is green. #1218 shares no file with #1139 and #1217, in flight beside it, and goes before #1204, which also edits skills/code-review/scripts/pr_body.py.
