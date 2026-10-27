# Overview: root-migrate removes every directory it emptied (#1016, #1018)

## Why this work exists

The root migration left a work item's directory on disk, empty, and
`specs/` with it, where it merged the item into a `seal/specs/<id>/` that
already existed or finished a move an earlier session stopped. The notice
then named the plugin's own moved item as "not a SpecSeal work item". Now
the move lists each directory again when it reaches it and removes every
one that holds nothing, so `specs/` goes too once only work items were in
it.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Whether S3 stands as a case of its own | `spec.md` S3: "a new case in `Test_run_moves`, seen red against the current walk" / round 1's fix pass deleted `Test_run_moves::test_accepts_an_item_merged_into_one_that_exists_and_takes_away_specs` | the code | S3's two assertions are each held by another case. S1, `Test_move::test_accepts_a_directory_whole_or_file_by_file_into_one_that_exists`, asserts that the merged item's directory is gone. `Test_run_moves::test_accepts_every_unit_and_takes_away_the_emptied_roots` asserts that `run_moves` removes an emptied `specs/`, and that removal is one `os.rmdir` that does not depend on how the item left. Round 1 ran five mutants with S3 left out: the walk's removal, the test that keeps `src`, the `specs/` cleanup, the walk's direction and the fresh listing. All five went red, so no defect was found that only S3 catches (`rounds/round-1.md` finding 1) |
| What `move`'s docstring says where the removal of a directory fails | *In* item 4: every directory under `src` "holding nothing when the walk reaches it is removed", and "One limit sentence follows it", the junction's / 3fd067a8 adds "unless its removal fails" to that sentence and a second limit: "Where the removal of a directory fails, as on Windows when another process holds it open, that directory and every one above it stay, and nothing is removed by mistake." | the code | Round 1's Not judged row named the edge. Its probe simulated a failing `os.rmdir` on macOS: the directory and every one above it stayed, and nothing raised. The owner's direction (`spec.md` *Grounding*, last row) gives an edge the one-issue flow cannot produce a limit sentence and no guard (`phases/phase-2.md`) |

## Not verified

| Item | Who must answer |
|---|---|
| closed the fix and S4 on the Linux and Windows legs. Locally only macOS ran them | the branch's `tests` workflow run 40425810821 at `087d676e` passed every leg, the four Windows groups included; the commit after it adds only round 3's record |
| The junction limit in `move`'s docstring: that the walk enters a Windows junction under `src` and removes the empty directories behind it. It was read from `os.walk`'s source and never run on Windows | the repository owner, who directed that the limit gets a sentence and no guard |
| The held-open limit in `move`'s docstring: that on Windows, where another process holds a directory open and its removal fails, that directory and every one above it stay. Round 1's probe simulated the failing `os.rmdir` on macOS, and nothing ran it on Windows | the repository owner, who directed that the limit gets a sentence and no guard |
| closed the full suite, the repository-wide lint and format check, and the typecheck at the branch head | `broad-gate.md` records the run at `f416c213` against `fa7d1374`; its printed report read BROAD GATE PASSED, ruff check and format clean, the suite 6,551 passed and 14 skipped, chain-check exit 0. The repository has no typecheck to run (#951 adds one) |

## Not done

`main`'s printed line for a moved item's directory that an ignored file
keeps on disk. It still names that directory as left and as not a SpecSeal
work item. `questions.md` Q2 holds it, and its default, (a), builds no new
wording.

A sweep of a repository the hook already migrated. An empty `specs/<id>/`
that an earlier release left there stays until a person removes it, because
the hook returns before any walk once its marker is stamped (`spec.md`
*Out*).

The price of S4 in `.test_durations`. The new case stays unpriced until the
next refresh from a `tests` run's artifact.

## Fed back into the spec

none
