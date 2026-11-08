# Routing: 1794178394-each-run-reaches-the-tree-wide-guards

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1441-each-run-reaches-the-tree-wide-guards |

Answered 2026-11-09 by the repository owner, before the first edit.

## Why this way

The owner chose `automation` for the six work items of `release: 0.36.0` (#1439 to #1444), run side by side where their files allow; #1441's change: which tests run at a review round and at a phase boundary is what `skills/verify/SKILL.md` instructs every crafter and the runner prints, so it frames, builds and reviews on the top rung.
