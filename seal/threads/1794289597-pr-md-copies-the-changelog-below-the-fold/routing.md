# Routing: 1794289597-pr-md-copies-the-changelog-below-the-fold

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/1478-pr-md-copies-the-changelog-below-the-fold |

Answered 2026-11-10 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-10, for the four process items of 0.37.2 (#1476–#1479), and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer.** The change moves the changelog fragment from `pr.md` into what `seal pr-body` composes, and touches a script, the chain check's body arm and four documents that state the `pr.md` rule; which file owns that rule, what `pr.<lang>.md` translates in the new shape, and how a body composed before this change is read are design choices the issue leaves to the frame.
- **Implementation, crafter.** A framer stands, and the build is a phase of its plan.
- **Review, through the review chain.** The body arm gates every ready pull request, so a wrong composition fails every later work item's pull request, not only this one.
- **Automation, yes.** The issue fixes the direction and its *Done when*, and every remaining choice has a default the tree or the framer can give.
- **Destination, open the pull request**, as under `complete`.
