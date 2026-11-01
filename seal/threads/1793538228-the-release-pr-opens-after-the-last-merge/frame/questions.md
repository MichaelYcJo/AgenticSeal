# Questions for the planner: the release pull request opens after the last work item merges (#1258)

The ticket left these judgments open, and the tree answered each. Nobody reopens them:

- Whether `docs/branch-and-release.md` and the two orchestration skills carry the early moment: they do not. Design `## Grounding` G2 and G3, `plan.md` A7.
- How the orchestrator reads that the last work item has merged: design G9 and G10, `plan.md` A1 and A8.
- Whether the step's `check:` line stays: design G11, `plan.md` A9.
- Whether the early runs caught anything that justifies keeping the pull request open: design G7, `plan.md` A2.

Assumed, because a different answer builds the same text: an orchestrating session works the release down `docs/release-checklist.md` after the last merge, as 0.27.3's milestone session does. Where none is running, the release waits in a state `gh pr list --base main` shows (`plan.md` *Technical context*).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does 0.27.3's release pull request run `tests` once for the tree it ships, with no `pull_request` run before its last merge? No probe can answer it before the release, because the pull request does not exist until the last merge | a measurement | Once: the rule holds. More than once: read which push started each extra run, a settle's pull request or a fix after a red run, against the failure scenarios in `plan.md` *Technical context* | Built as designed. The reader is the orchestrator of 0.27.3's release, running `gh run list --branch release/v0.27.3` after the merge into `main` | open |
