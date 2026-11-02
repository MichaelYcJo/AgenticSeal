# Routing: 1793582903-each-entry-links-its-pull-request

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Answer pressed | automation |
| Branch | feat/1139-a-released-entry-reaches-its-work-only-through-a-hidden-id |

Answered 2026-11-02 by the owner, before the first edit.

## Why this way

The owner pressed automation once for the whole of 0.28.0 and answered that the session squash-merges each pull request into release/v0.28.0 once its CI is green. #1139 follows #1054 and #1045, merged as #1284 and #1285, which also edit the settle; #1153 edits the same release-note renderer and follows it.
