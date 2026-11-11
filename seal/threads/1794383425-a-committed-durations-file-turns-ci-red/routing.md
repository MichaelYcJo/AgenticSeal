# Routing: 1794383425-a-committed-durations-file-turns-ci-red

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/1486-a-committed-durations-file-turns-ci-red |

Answered 2026-11-11 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-11, for the work items of 0.37.4 (#1481–#1489, #1498), and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*. The owner chose, on 2026-11-11 in the batch asked before the first edit, a durations union kept in `actions/cache` and a pinned YAML parser, as the issue's *Decisions* records.

- **Planning, framer.** The decisions fix the direction and leave the design open: how the cache is keyed, written on `main` and restored by pull requests, how the timeouts and shard count are recomputed, and which documents (`CONTRIBUTING.md`, the release checklist) state the refresh.
- **Implementation, crafter.** A framer stands, and the build is a phase of its plan.
- **Review, through the review chain.** The change rewrites CI workflow steps and the test runner's environment, which every pull request runs through; a defect there shows on every later pull request.
- **Automation, yes.** The owner's decisions are given, and every remaining choice has a default the tree or the framer can give.
- **Destination, open the pull request**, as under `complete`.
