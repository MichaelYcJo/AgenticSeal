# Routing: 1795849901-number-read-at-cut

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | feat/1671-number-read-at-cut |

Answered 2026-11-28 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 of the routing question with `agentic` on 2026-11-28, for a request naming #1648, #1593, #1631, #1583 and #1671, and chose to cut the three releases side by side. Each row below is judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer:** the issue leaves open what the `merged:` label says before a release is cut, what the unnumbered branch is called, and where it is cut again after a release. The rule is stated across `docs/releasing/` and several workflow scripts.
- **Implementation, crafter:** the change spans the release workflows, their scripts, the contribution guide and the tests, a diff too large for the orchestrator to hold beside three other work items.
- **Review, through the review chain:** the change rewrites the release gates every later release passes through, and a defect there stops a release.
- **Automation, yes:** the owner set the direction in #1671 on 2026-11-28, and the open points have defaults the tree or the framer can give.
- **Destination, open the pull request:** nothing in the issue or the batch asks for the branch back.

The base is the release branch for the minor that carries #1671's feat, cut after the minor of #1583. This is the release's only work item, so it carries the version move.
