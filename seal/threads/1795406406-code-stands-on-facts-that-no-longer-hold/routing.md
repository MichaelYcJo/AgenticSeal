# Routing: 1795406406-code-stands-on-facts-that-no-longer-hold

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/1576-code-stands-on-facts-that-no-longer-hold |

Answered 2026-11-23 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-23, for the twelve issues of the milestone `release: 0.38.6` (#1571 to #1582), in the one batch asked before the first edit, and decided three of this issue's questions in that batch: `tracker_labels.py` is removed, the six readings of old record forms are removed, and `seal layout --moved` is kept with its keep-or-drop question sent to `seal/follow-up.md`. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The removals reach `unverified_check.py`'s exit-0 branches and `chain_check.py`'s readers, which gate a commit and a pull request, and a workflow step on every push to `main`.
- **Planning, framer.** The issue lists many sites across `skills/`, `lib/`, `.github/` and `tests/`; which fall together and in what order is the framer's to plan.
- **Implementation, crafter.** The work spans scripts, a workflow and the suite, while the orchestrator holds two other work items of the release.
- **Review, through the review chain.** Removing a reading a gate makes changes what that gate decides on a record an old release wrote, which is a judgment a round reads.
- **Automation, yes.** The owner's decisions above answer what needs a person; the rest has a default the issue or the tree gives.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.38.6` at `c3f568c6a`, after #1571, #1578, #1577, #1579 and #1582 landed. #1573 (every git and `gh` call onto `lib/gitcmd.py`, `skills/verify/scripts/unverified_check.py` and `skills/implement/scripts/seal.py` among them) and #1574 (`lib/routing.py` and `lib/lines.py` row readers) run beside it. Whichever lands later merges the base before its broad run (`skills/implement/merge-order.md`).
