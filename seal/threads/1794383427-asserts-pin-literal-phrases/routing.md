# Routing: 1794383427-asserts-pin-literal-phrases

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | test/1488-asserts-pin-literal-phrases |

Answered 2026-11-11 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-11, for the work items of 0.37.4 (#1481–#1489, #1498), and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*. The milestone's *Model* paragraph puts this item's framer on Fable.

- **Planning, framer.** Each of several hundred asserts is weighed against #1233's criterion, a fact a reader acts on, and that weighing is the design; `docs/running/what-a-script-gates.md` states the criterion the frame applies.
- **Implementation, crafter.** A framer stands, and the build is a phase of its plan.
- **Review, through the review chain.** An assert removed that held a fact a reader acts on would show only when a later change breaks that fact, so a reader independent of the build is worth its rounds.
- **Automation, yes.** The issue fixes the criterion and its *Done when*, and every remaining choice has a default the tree or the framer can give.
- **Destination, open the pull request**, as under `complete`.
