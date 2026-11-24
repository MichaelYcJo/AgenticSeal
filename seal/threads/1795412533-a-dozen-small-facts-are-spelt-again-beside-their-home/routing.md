# Routing: 1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/1575-a-dozen-small-facts-are-spelt-again-beside-their-home |

Answered 2026-11-23 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-23, for the twelve issues of the milestone `release: 0.38.6` (#1571 to #1582), in the one batch asked before the first edit. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The facts the issue lists are read by gates: the opt-out test by `settle.py`, `fold_check.py`, `seal.py` and `broad_gate.py`, the policy root by `pact_check.py` and `fold_check.py`, and `--sealing` by the broad gate's chain arm. Pointing each copy at its home changes what those gates read where the two differ.
- **Planning, framer.** The issue lists about a dozen facts and their copies; which copy becomes a call to its home, which home moves, and which pin falls is the framer's to plan.
- **Implementation, crafter.** The work spans `lib/`, `skills/`, `.github/scripts/` and the suite, while the orchestrator holds two other work items of the release.
- **Review, through the review chain.** A copy and its home that differ today read differently after the change, and whether they meant the same is a judgment a round reads.
- **Automation, yes.** The work reaches nothing outside the repository, and every question has a default the issue or the tree gives.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.38.6` at `02369a0e9`, after #1571, #1578, #1577, #1579, #1582, #1573 and #1574 landed; #1574 changed `lib/lines.py`, `lib/blocks.py`, `lib/tables.py` and `fold_check.py`, which this issue also names. #1572 (`pact_check.py`, `deferral_check.py`, the release publisher) and #1576 (stale facts, `lib/gaps.py` and `chain_check.py` among them) run beside it. Whichever lands later merges the base before its broad run (`skills/implement/merge-order.md`).
