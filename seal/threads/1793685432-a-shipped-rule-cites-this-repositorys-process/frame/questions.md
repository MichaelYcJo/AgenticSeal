# Questions for the planner: a shipped rule cites this repository's process

The tree answered these judgments the ticket left open. Each line points at the row that holds its grounds.

- The work item's subject, and so whether `docs/` is edited directly or through `## Rule changes`: `frame/design.md` *Grounding*, first row, and `frame/plan.md` *Alternatives considered*, the `## Rule changes` row.
- Whether any unsettled design's rule changes need re-pointing: `frame/design.md` *Grounding*, second row.
- Where each rule's home is, a skill or a `docs/running/` document: `frame/plan.md` *Alternatives considered*, the first two rows.
- Whether the never-rebase box stays in *0. Before starting*: `frame/plan.md` *Alternatives considered*, the row that drops the box.
- Which of the `.github/` lines follow a moved rule: `frame/design.md` *Grounding*, the `.github/` row.
- Whether a moved sentence gains a pin or a check line: `frame/plan.md` *Alternatives considered*, the pin row, and `frame/design.md` *Grounding*, the #1277 row.
- Whether this work conflicts with #1320: `frame/design.md` *Grounding*, the PR #1320 row.

No row needs a person. Under `Automation` `yes` the build goes on each row's default.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the merge of `release/v0.30.1` into this branch, after #1320 lands, resolve a conflict in a file outside this work item's records? #1320 is open and its head can still move, so no merge can be run at framing time. The two diffs read on 2026-11-03 touch different paragraphs of `skills/implement/orchestration.md` and no other shared file | the work | A clean merge owes nothing more. A conflict resolved in `skills/implement/orchestration.md` owes a verifying round on the resolution, as `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* states | The merge is clean, and no verifying round is owed. The orchestrator records the merge's outcome where that section says | answered 2026-11-03 by the orchestrator: #1320 merged as `62a15c50e`, and the merge of `origin/release/v0.30.1` at `5e9ab6658` resolved no conflict (executed: `git merge --no-edit`, `git status --short` empty), so no verifying round is owed |
