# Questions for the planner: the next round is a fix's first reader (#1615)

The ticket left these open, and the tree answered each:

- Whether the sealer reading a records-only fix is new work: `frame/design.md` G1 and G2.
- Whether a regression's records-only fix still owes a round: `frame/design.md` G3 and G18, and `frame/plan.md` *Alternatives considered*, the row opening "Keep the round after a regression's records-only fix".
- How the orchestrator tells a pass the sealer reads from one a round reads: `frame/design.md` G20.
- What the sealer reads of a records-only fix: `frame/plan.md` *Alternatives considered*, the row opening "Keep the sealer's read of a records-only fix as it is".
- What "each with a check" asks of a record row: `frame/plan.md` *Alternatives considered*, the rows opening "A `check:` line for each record row" and "A seeded proofer case".
- Which axes are added, and whether one is left out with a reason: `frame/design.md` Scope item 1 adds every axis the issue proposes, so the issue's "or the issue says why one is not added" has nothing to name.
- What "a drawn screen" is: `frame/design.md` G21.
- Which mechanism beside text reads a fix's records before the next round: `frame/plan.md` *Alternatives considered*, the hook, agent and workflow rows.
- Where the issue's second *Done when* line goes: `frame/design.md` G25 and Scope item 7.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Why did `seal gate --preflight --base 8dea1ca7b` at `e902ea9a3` pass, with no chain line for `round-1.md`'s two `fixed` findings whose commit `a43ab8261` changed `skills/verify/scripts/broad_gate.py`, where `chain_check.py --worktree` at the same commit named each with "a verifying round is owed" (`frame/design.md` G20)? The framer's probe ran in a `git clone --no-local` with no GitHub remote, so `gh pr view` failed there for a reason it does not fail for in the orchestrator's clone, and the framer did not trace which work items the non-`--worktree` run judged at that commit. Scope item 4 does not rest on the preflight, so the answer does not change this build | a measurement: the orchestrator, running both commands at a commit of a branch in its own clone where the last record holds a `fixed` finding whose commit changed code, before the pull request opens | (a) The preflight's chain arm judges the records arm before a pull request exists, and the probe's result came from the clone: nothing follows. (b) It does not: `skills/code-review/gate-to-pull-request.md` *The preflight is yours, and it is not the broad gate* says "a refusal on a record arm, which the broad run would return after that suite, arrives before it", which then does not hold before the pull request, and that is an issue of its own | (a), and nothing in this build reads the preflight for it | open |
