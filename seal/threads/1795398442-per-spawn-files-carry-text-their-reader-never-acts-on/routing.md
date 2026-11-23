# Routing: 1795398442-per-spawn-files-carry-text-their-reader-never-acts-on

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | refactor/1579-per-spawn-files-carry-text-their-reader-never-acts-on |

Answered 2026-11-23 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-23, for the twelve issues of the milestone `release: 0.38.6` (#1571 to #1582), in the one batch asked before the first edit. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The change moves text between files the crafter, the proofer, every agent and the orchestrator open at their steps, and a passage moved to a file its reader no longer opens is a rule that reader stops following.
- **Planning, framer.** The issue fixes the direction and leaves open where each passage lands, which agent-definition copies become one contract rule, and how the supporting file for the pull-request material is named and cited.
- **Implementation, crafter.** The edits span about fifteen files and the cases that cite them while the orchestrator holds two other work items of the release at the same time.
- **Review, through the review chain.** Finding every reader of a moved passage, and every citation and `check:` line that named it, is a reader's work (contract rule 12).
- **Automation, yes.** The work reaches nothing outside the repository, and every question has a default the issue or the tree gives.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.38.6` at `3c89a70d5`, after #1571 and #1578 landed; #1578 rewrote several of the files this issue names, so the issue's coordinates, written at v0.38.5, have moved. #1577 (`templates/setup/config.md` *Broad gate*, `skills/config/SKILL.md`) and #1573 (the git runners) run beside it. Whichever lands later merges the base before its broad run (`skills/implement/merge-order.md`).
