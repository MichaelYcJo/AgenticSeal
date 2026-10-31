# Routing: 1793443708-settle-keeps-a-gaps-file-anywhere

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | fix/1126-settle-keeps-a-gaps-file-anywhere |

Answered 2026-10-31 by the owner, before the first edit.

## Why this way

The owner pressed automation for 0.27.0's first work item (#1198) in this session and said whatever can run in parallel may run in parallel; #1126 edits the settle's reader, which #1198 does not touch, so it runs beside #1198 under the same answer, and the pull request goes into release/v0.27.0.
