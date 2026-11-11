# Questions for the planner: 88 of 141 test files declare no TARGET, so the layout and its duplicate finder never read them (#1489)

The judgments the issue left open that the tree answered, so nobody reopens them:

- What "cleaned once" means for the pairs of `tests/github/test_run_tests.py`: `frame/design.md` G4 and *The pair reader*, and `plan.md` A7 to A9.
- Where a file that keeps no `TARGET` says why, and whether a script reads it: `frame/design.md` *The reason line*, and `plan.md` A6.
- Which cases move, which declare a document, and which stay: `frame/design.md` *The kinds* and *The files*, and `plan.md` A3 to A5, A11, A14 and A15.
- Which of the cases #1488's criterion still has to rule: `frame/design.md` G5, G6 and *The cases #1488 read*.
- How a check line comes to name a moved case at its new home: `frame/design.md` G9, G10, *Scope* item 9 and `## Rule changes`, and `plan.md` A2.
- Whether `--all` stays: `frame/design.md` G11 and `## Removes`, and `plan.md` A6.
- How the remaining pairs carry their reason: `frame/design.md` *Scope* item 11, and `plan.md` A10.
- Which merges first among the release's open items: `plan.md` *Overlap with the release*.

No row below needs a person.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which kind each case of the 86 files is, and where each M case lands. The reason the tree does not answer it here: G7's probe follows names to a loader or an import, not what an assert holds, and the framer read the files' docstrings and the probe's rows, not each case. A case's subject is settled by reading it whole, which is the build. | the work | The phase rules each case by `frame/design.md` *The kinds*. Where a file's kind or a case's destination differs from *The files*, the phase records the file, the kind it found and why in its `trail/phases/phase-N.md`, and builds to what it found. | `frame/design.md` *The files* | open |
| Q2 | Whether each move passes `bin/seal layout --moved`. The reason no probe answers it here: the check collects both sides with pytest from a worktree of its base, and the base is a phase's ruling commit, which does not exist yet. | the work | Exit 0: the record carries the command and its last line, and no mutation table. Exit 1: the record names the failing cases, and the module carries the mutation table `CONTRIBUTING.md` *The test layout* asks for. | `frame/design.md` *Scope* item 5 | open |
| Q3 | Which test modules outside a phase's narrow run turn red once its cases move or go. The reason no probe answers it here: it is the suite's behaviour, and the framer runs none of the repository's test modules (contract rule 2). | a measurement | A module in the narrow run turns red: the phase fixes the place it reads and records it. One outside it turns red: the orchestrator's broad gate finds it, and the fix goes through a round. None turns red: the row closes on the phase runs and the gate's record. | `frame/design.md` *The narrow run* at each phase boundary, and the rest of the suite `unverified`, answered by the orchestrator's broad gate | open |
| Q4 | Which check line or sentence a phase must re-point is held by an unsettled design's operation when the phase reaches it. The reason the tree does not answer it here: it follows from Q1's rulings and from the designs merged by then. At the frame, #1488's operations hold four `docs/` lines that name files this work keeps in place (`frame/design.md` G10). | the work | None: nothing more. One or more: the phase names each in its record, and the orchestrator sends them to the framer as one fold, which adds a `change` for each, with the edition's operation, to `frame/design.md` `## Rule changes`. | `frame/design.md` *Scope* item 9 | open |
| Q5 | Which pairs `bin/seal layout --pairs` prints once the cases have moved, and the input each pair's cases differ by. The reason no probe answers it here: a pair a move makes exists only after the move, and the input that differs is read in the two cases. | the work | The phase that makes a pair writes its reason in the class docstring, and phase 8 writes it for each pair that stood before the build. A pair whose two cases hold one fact is named in the phase record and kept, since a cut needs the mutation table (`plan.md` A10). | `frame/design.md` *Scope* item 11 | open |
