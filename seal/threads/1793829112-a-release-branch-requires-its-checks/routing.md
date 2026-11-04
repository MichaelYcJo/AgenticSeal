# Routing: 1793829112-a-release-branch-requires-its-checks

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | chore/457-a-red-check-merges-into-a-release-branch |

Answered 2026-11-05 by the owner, before the first edit.

## Why this way

#457 decides which checks the `release/**` ruleset requires and states it where the policy documents claim the merge rule, text a person reads and acts on, so the ladder calls for a frame. The owner pressed automation for this work item, and answered in the same batch that the orchestrator applies the ruleset change with `gh api` after the work item is sealed.
