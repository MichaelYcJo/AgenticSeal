# Routing: 1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/1582-the-broad-gates-verdict-depends-on-the-stamps-sprite |

Answered 2026-11-23 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-23, for the twelve issues of the milestone `release: 0.38.6` (#1571 to #1582), in the one batch asked before the first edit. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The change decides whether `seal gate`'s verdict can depend on a decorative file, and moves helpers between two gate scripts whose cases pin the wrapper that exists for that case.
- **Planning, framer.** The issue leaves the framer to choose between moving the text-panel helpers to a module both scripts import and reading the sprite inside `build()`, and to settle the one rule for whether two refs name the same commit.
- **Implementation, crafter.** The edits span `broad_gate.py`, `seal_stamp.py` and their cases while the orchestrator holds two other work items of the release.
- **Review, through the review chain.** `broad_gate.py` is a gate script, and a helper that moves takes its callers' readings with it.
- **Automation, yes.** The work reaches nothing outside the repository, and every question has a default the issue or the tree gives.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.38.6` at `f2a664eb8`, after #1571, #1578 and #1577 landed; #1577 rewrote `broad_gate.py`'s command reading, so the issue's coordinates, written at v0.38.5, have moved. #1573 (the git runners, which reach `broad_gate.py`) and #1579 (documents) run beside it. Whichever lands later merges the base before its broad run (`skills/implement/merge-order.md`).
