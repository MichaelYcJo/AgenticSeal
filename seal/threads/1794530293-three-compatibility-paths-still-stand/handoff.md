# Handoff: 1794530293-three-compatibility-paths-still-stand

Written 2026-11-13 by the orchestrator, at the owner's request to stop the
session after round 1's fix pass. The orchestrator that takes this work over
deletes this file once it has read it, in a commit of its own.

## Where the work stands

- Branch `refactor/1500-three-compatibility-paths-still-stand`, pushed, based
  on `release/v0.38.1` at `8f6acbb0e`. The routing is in `routing.md`
  (owner's answer `agentic`, 2026-11-13).
- Both phases are built and closed (`frame/plan.md` *Phases*, Status column).
- Round 1 (`trail/rounds/round-1.md`, target `c97122644`) opened two `should`
  findings. The framer folded finding 1 into the frame (`567f4d78e`); the
  phase 2 crafter's fix pass fixed both (`874b25a46`, `305a9b838`,
  `acecc2e12`), and the record with its close blocks is committed
  (`aab7a8a5c`).
- `pr.md` is written and quotes the frame as round 1's fold left it
  (`69ed2e983`).

## What comes next, in order

1. A verifying round, round 2, over the diff of the fixes,
   `69ed2e983..acecc2e12`, answering findings 1 and 2.
   `chain_check.py` at `acecc2e12` reports that round as owed (the fix
   pass crafter's run, executed).
2. Before spawning it, weigh one possible fold the fix pass crafter named:
   `frame/design.md` G3 says the *Updating* line says "what a person still
   on 0.36.x or earlier does instead", which restates the issue's *Done
   when* in version terms while the folded *Scope* item 12 and S7 name the
   files. G3 stands in the section dated to `dda87704c`, so it may stand as
   the issue's words; the round reads it either way.
3. Drain the rows (`skills/implement/orchestration.md` *Orchestrator: drain
   the rows before the broad run, and keep the records*), then
   `seal gate --preflight` and `seal gate --record`.
4. `seal pr-body` into the scratch directory, then the sealer.
5. Open the pull request into `release/v0.38.1` with the title
   `refactor:` gives (`frame/plan.md` *Judgments of the run*).

## The release's other items

- #1543 was built under the route `direct` and is pull request #1547 into
  `release/v0.38.1`, every check passed at `2c6e2d63c`. It stays unmerged
  until this work item merges, because this item carries the version move
  and the first pull request into the branch carries it
  (`frame/plan.md` *Overlap with the release*). Its worktree is
  `/Users/michael/Documents/GitHub/SpecSeal-worktrees/agenticseal-1543`.
- #1422 waits on the owner's paid runs; nothing was built for it.
- #1548, opened in this run, is the prevention home for the frame census
  defect both phases met (`frame/plan.md` *Judgments of the run*); it is in
  the backlog, not this release.
