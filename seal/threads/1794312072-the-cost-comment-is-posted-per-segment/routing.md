# Routing: 1794312072-the-cost-comment-is-posted-per-segment

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/1479-the-cost-comment-is-posted-per-segment |

Answered 2026-11-10 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-10, for the four process items of 0.37.2 (#1476–#1479), and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer.** The issue leaves two choices to the frame: where the meter's internals go, the `session_cost.py` docstring or `docs/running/measuring-a-run.md`, and where the observation a session wrote after a segment goes once the per-segment post ends. The posting rule is also stated beyond its section, at `skills/implement/orchestration.md` and in the two citations #1478 kept in `skills/code-review/orchestration.md` and `skills/commit-pr-convention/SKILL.md`.
- **Implementation, crafter.** A framer stands, and the build is a phase of its plan.
- **Review, through the review chain.** Every orchestrating session reads the measuring section, so a dropped command or exit-code meaning would show as an orchestrator that measures wrongly in a later run, not as a failing suite.
- **Automation, yes.** The issue fixes the direction, its *Done when* and its out-of-scope line, and every remaining choice has a default the tree or the framer can give.
- **Destination, open the pull request**, as under `complete`.
