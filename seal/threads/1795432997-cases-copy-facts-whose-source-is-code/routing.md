# Routing: 1795432997-cases-copy-facts-whose-source-is-code

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | test/1580-cases-copy-facts-whose-source-is-code |

Answered 2026-11-23 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-23, for the twelve issues of the milestone `release: 0.38.6` (#1571 to #1582), in the one batch asked before the first edit. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The issue names about thirty cases across `tests/text/`, `tests/behaviour/`, `tests/evals/` and `tests/skills/`, a shared `section()` helper for `tests/conftest.py`, and the removal of `evals/scripts/behaviour.py` functions only tests call. A case rewritten to read its value from code can stop guarding the fact it guarded, and whether the new case holds the same fact is a reader's work.
- **Planning, framer.** The issue leaves open, per case, whether it reads its value from the code, from a parser, or is removed because another case holds the fact, and which stop rule the one `section()` keeps among the ten that differ.
- **Implementation, crafter.** The diff spans some twenty test modules and the evals scripts, while the orchestrator holds #1596 beside it.
- **Review, through the review chain.** Whether a removed case's fact is held by another case is a judgment a round reads.
- **Automation, yes.** The work reaches nothing outside the repository, and every question has a default the issue or the tree gives.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.38.6` at `2025561ae`, after ten of the release's items landed, #1575 and #1576 among them, which changed `tests/run_tests.py`, `tests/conftest.py`'s neighbours and `tests/skills/test_broad_gate.py`. #1581 rewrites `tests/skills/test_test_layout.py` and `tests/skills/test_broad_gate.py`, which this issue also names, so #1581 starts after this item merges. #1596 runs beside this item in `chain_check.py` and the review-chain documents, and neither names the other's files.
