# Routing: 1795849898-body-decision-with-its-question

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1593-body-decision-with-its-question |

Answered 2026-11-28 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 of the routing question with `agentic` on 2026-11-28, for a request naming #1648, #1593, #1631, #1583 and #1671, and chose to cut the three releases side by side. Each row below is judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer:** the issue leaves the design open: where a decision's question is carried, in `pr.md` or by `agentic pr-body`, and what becomes of an empty questions table.
- **Implementation, crafter:** this session orchestrates four work items side by side, so the build goes to a crafter to keep what the orchestrator holds small.
- **Review, through the review chain:** the change rewrites text the orchestrator acts on at every pull request, and a defect in it shows as a body a later owner misreads, not as a failing suite.
- **Automation, yes:** every question the orchestrator foresees has a default the tree or the framer can give.
- **Destination, open the pull request:** nothing in the issue or the batch asks for the branch back.

The work item was routed into the release branch for the patch, with #1648. On 2026-11-28 its build showed it is a feat, and the owner moved it to a minor of its own after #1671's (`frame/plan.md` *Judgments of the run*). Its base is that minor's branch once it is cut, which the orchestrator merges before the pull request opens.
