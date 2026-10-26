# Questions for the planner: root-migrate removes every directory it emptied (#1016, #1018)

## Answered by the tree

The two issues left these open, and the tree answers them. Each names where
the answer was read, so a reviewer can overturn it by opening the same place.

1. **A1 Whether #1016 and #1018 need two fixes.** No. Both are the one walk
   in `hooks/root-migrate.py#move` deciding emptiness from a listing taken
   before the subdirectories were removed (`spec.md` *Grounding*). The merge
   shape and the resumed shape differ only in which run emptied a directory,
   and S1 and S2 pin one each.
2. **A2 Whether the removal tracks what the move emptied, or walks
   afterwards.** It walks, and reads each directory again when it reaches
   it. Tracking misses the resumed shape: a directory an earlier, stopped
   run emptied is the parent of no file the finishing run moves
   (`plan.md` *Alternatives considered*, rows A and B).
3. **A3 Whether an empty directory under `src` that this move did not empty
   goes too.** Yes. Git tracks no empty directory, so it never held anything
   git knew of, and `move`'s docstring already promises "The empty
   directories left behind are removed." A directory holding an ignored file
   is not empty and stays (module docstring, boundary "only what git
   tracks"; S4).
4. **A4 Whether `run_moves`'s removal of `specs/` and `.specseal/` changes.**
   No. One `os.rmdir` each stays, because `specs/` may hold a team's
   directory (`plan.md` *Alternatives considered*, row F).
5. **A5 Whether a run that stops removes what it emptied before stopping.**
   No. The run that finishes the item removes it (`spec.md` *Out*).
6. **A6 Whether a repository the hook already migrated is swept for the
   empty directories an earlier release left.** No. The hook returns before
   any walk there, and a sweep would read the old tree after the migration,
   against the boundary "silent when there is nothing to do" and the
   `# RIDER:` at the top of `hooks/root-migrate.py` (`spec.md` *Out*).
7. **A7 How the red is seen on Linux, macOS and Windows.** Phase 1 commits
   the cases with no fix, and the orchestrator pushes the branch and
   dispatches the `tests` workflow on it. `.github/workflows/test.yml`
   declares `workflow_dispatch` for a pushed branch measured without a pull
   request (its comment cites #841), and its matrix runs all three systems.
   No agent pushes (contract rule 6), so the push and the dispatch are the
   orchestrator's.
8. **A8 What guards a directory link or a Windows junction placed under a
   work item's directory.** Nothing. Git checks out neither, the one-issue
   flow cannot produce one, and `move`'s docstring states it as a limit
   (the owner's direction in the spawn prompt).
9. **A9 Whether a rule changes.** No. `docs/` states nothing about what the
   root migration removes (executed `git grep`, `spec.md` *Grounding*).

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does Python 3.12's `os.walk`, which CI runs, list a directory before it yields its subdirectories as 3.15's does, so that S1, S2 and S3 fail on the Linux, macOS and Windows legs against the current walk? The tree could not answer it: the source read was the local 3.15.0, and the current `Test_move` case passing on CI shows the item directory left, which is the same fact read the other way | a measurement | (a) yes: phase 1's dispatched run shows those cases red on all three systems, and phase 2 proceeds. (b) no on some leg: a case that is green there pins nothing on that system, and the phase that meets it records the leg and rewrites the case until it is red there | (a), measured by phase 1's dispatched `tests` run | answered 2026-10-27 by the orchestrator: (a). The `tests` run 40421812732 at `07638965` failed S1, both rows of S2 and S3 on the ubuntu, macOS and Windows legs alike, and no other `tests/test_root_migrate.py` case |
| Q2 | After the fix, a moved work item's directory that holds only an ignored file, such as `specs/<id>/rounds/.DS_Store`, stays on disk, and `main`'s printed line names it as left with the reason "no routing.md or rounds/ that git tracks", calling it not a SpecSeal work item. Should the line give such a directory its own reason? The tree could not answer it: the module docstring says what stays (an ignored file) and says nothing about how the line names a work item's directory it kept | a person | (a) leave the line as it is: this work changes no message wording, and the line stays false about that one directory. (b) a third clause in the line for an id-shaped directory that this run moved and an ignored file kept, pinned by a case: a change a person reads, outside both issues' scope | (a): this work builds no new line wording, and the owner can open an issue for (b) | open |
