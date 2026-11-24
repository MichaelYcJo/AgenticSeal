# Routing: 1795439973-six-test-modules-cost-past-the-rewrite-bound

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | perf/1581-six-test-modules-cost-past-the-60-s-rewrite-bound |

Answered 2026-11-23 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-23, for the twelve issues of the milestone `release: 0.38.6` (#1571 to #1582), in the one batch asked before the first edit. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The issue asks six test modules to be rewritten by `CONTRIBUTING.md` *The test layout*, among them `tests/skills/test_chain_check.py` and `tests/skills/test_broad_gate.py`, which hold the cases of the checks that refuse a ready pull request and of the broad gate. A rewrite that drops a case's fact lets a defect in those gates through unseen.
- **Planning, framer.** The issue leaves open how each module's world is built, which cases become unit calls, and the order across six modules of some 1,200 cases; the measurement it is judged by comes from CI after the release.
- **Implementation, crafter.** The diff rewrites six large modules.
- **Review, through the review chain.** Whether each rewritten case still holds what the old one held is a judgment a round reads.
- **Automation, yes.** The work reaches nothing outside the repository. The `test-durations` artifact that answers *Done when* is read from CI, and the frame reads the Windows leg of a `workflow_dispatch` run of `tests` on the branch in its stead until the first push run on `main` after the release (`frame/design.md` S1).
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.38.6` at `ef776317b`, after every other item of the release landed, #1580 (PR #1599, the shared `tests/conftest.py#section`, `test_broad_gate.py#unquoted_flat`, `test_chain_check.py`'s reading over `section`) and #1596 (PR #1597, a case in `test_chain_check.py` *Test_broad_gate*) among them. No other item of the release runs beside it.
