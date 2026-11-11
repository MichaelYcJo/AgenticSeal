# Routing: 1794376287-check-lines-ride-in-every-preload

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/1475-check-lines-ride-in-every-preload |

Answered 2026-11-11 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-11, for the work items of 0.37.3 (#1471–#1475, #1480, #1503), and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*. The owner chose deletion for #1475 on 2026-11-11, in the batch asked before the first edit, as the issue's *Decision* records.

- **Planning, framer.** The decision fixes the direction and leaves to the frame what `.github/scripts/rules.py` and its cases read once the six preloaded files carry no line, whether a line added back to one of them is refused, and where `skills/settle/rule-changes.md` says so; #1471, #1472, #1473, #1474, #1480 and #1503 moved and removed lines in every one of those files since the issue's counts were taken.
- **Implementation, crafter.** A framer stands, and the build is a phase of its plan.
- **Review, through the review chain.** The change deletes lines a script reads from every file an agent preloads, so a line left, or a test the deleted lines named that stops running, would show in a later release rather than in this suite.
- **Automation, yes.** The issue fixes the direction and its *Done when*, and every remaining choice has a default the tree or the framer can give.
- **Destination, open the pull request**, as under `complete`.
