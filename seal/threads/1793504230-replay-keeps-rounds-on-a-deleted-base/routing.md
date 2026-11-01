# Routing: 1793504230-replay-keeps-rounds-on-a-deleted-base

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | fix/1224-replay-keeps-rounds-on-a-deleted-base |

Answered 2026-11-01 by the owner, before the first edit.

## Why this way

The owner pressed automation for the three 0.27.1 reader fixes the reviews of #19 and #1150 deferred (#1225, #1224, #1228). #1225 and #1224 run beside one another, each in its own worktree because two crafters in one working tree are not safe; #1228 edits the file #1224 edits, so it follows #1224.
