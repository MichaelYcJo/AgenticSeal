# Routing: 1794401941-payload-calibration-reached-by-tests-alone

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/1484-payload-calibration-reached-by-tests-alone |

Answered 2026-11-11 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-11, for the work items of 0.37.4 (#1481–#1489, #1498), and decided this issue's question the same day: remove the calibration and baseline paths of `seal payload` and keep the byte composition `release_report.py` reads. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, framer.** Which code behind the three flags goes and which the byte composition still needs, and where each of the five symbols' callers and citations stand after #1482 moved `unverified_check.py`'s readers, is read from the tree before the cut.
- **Implementation, crafter.** A framer stands, and the build is the phases of its plan.
- **Review, through the review chain.** A removal that takes a path `release_report.py` still reads shows only on the release pull request, so a reader independent of the build is worth its rounds.
- **Automation, yes.** The owner's decision and the issue's *Done when* leave no question that needs a person.
- **Destination, open the pull request**, as under `complete`.
