# Routing: 1795405728-lib-routing-splits-a-row-on-an-escaped-pipe

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1574-lib-routing-splits-a-row-on-an-escaped-pipe |

Answered 2026-11-23 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-23, for the twelve issues of the milestone `release: 0.38.6` (#1571 to #1582), in the one batch asked before the first edit. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** `lib/routing.py`'s table reader is read by `chain_check.py` on every commit and pull request, and `lib/lines.py`'s splitter by `lib/gaps.py`, a gate for `settle --apply` and `seal unverified`; changing what a row is changes what those gates decide.
- **Planning, framer.** The issue names the direction, one row splitter and one line split, and leaves open which readers move in which order and what each reader's callers then see.
- **Implementation, crafter.** The readers span `lib/` and the scripts that call them, while the orchestrator holds two other work items of the release.
- **Review, through the review chain.** A reader that a gate runs on is the case `skills/core/SKILL.md` *The rule a mechanism is kept against* names: it reads a parser's result exactly or it is not a gate.
- **Automation, yes.** The work reaches nothing outside the repository, and every question has a default the issue or the tree gives.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.38.6` at `da7bd3968`, after #1571, #1578, #1577 and #1579 landed. The owner's lanes put this issue after #1575 and #1576 in the code lane; it starts beside them because the prose lane finished and it shares the fewest files with #1573, which holds the code lane. #1573 (the git runners, `lib/routing.py#current_branch` among them) and #1582 (the stamp's sprite) run beside it, and #1575 (`lib/blocks.py`, `lib/lines.py` and `lib/fields.py` delimiters) follows. Whichever lands later merges the base before its broad run (`skills/implement/merge-order.md`).
