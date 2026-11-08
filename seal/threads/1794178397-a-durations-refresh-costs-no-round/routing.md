# Routing: 1794178397-a-durations-refresh-costs-no-round

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1444-a-durations-refresh-costs-no-round |

Answered 2026-11-09 by the repository owner, before the first edit.

## Why this way

The owner chose `automation` for the six work items of `release: 0.36.0` (#1439 to #1444), run side by side where their files allow; #1444's change: where and by whom `.test_durations` is refreshed changes what the orchestration and `CONTRIBUTING.md` instruct, and may change what the chain check reads, so it frames, builds and reviews on the top rung.
