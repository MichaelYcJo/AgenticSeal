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
| What the limit sentence in `move`'s docstring names | *In* item 4: "a directory link or a Windows junction placed under `src` by hand is not something git checks out, and the walk is not guarded against one" / the docstring names only "a Windows junction placed under `src` by hand, which git does not track", which "is walked into, and the empty directories behind it are removed too" | the code | Git tracks a symbolic link, so "git checks out neither" is false for one, and a tracked link is moved by `git mv` with the other files before the walk. An untracked directory link is not entered: `os.walk`'s bottom-up branch says "exclude symlinks to directories if followlinks is False". Its parent's fresh listing names it, so the parent stays. A junction is not a symbolic link to `DirEntry.is_symlink()`, so the walk enters it, which is the limit `plan.md` *Technical context* describes (`phases/phase-2.md`) |
| Whether S3 stands as a case of its own | `spec.md` S3: "a new case in `Test_run_moves`, seen red against the current walk" / round 1's fix pass deleted `Test_run_moves::test_accepts_an_item_merged_into_one_that_exists_and_takes_away_specs` | the code | S3's two assertions are each held by another case. S1, `Test_move::test_accepts_a_directory_whole_or_file_by_file_into_one_that_exists`, asserts that the merged item's directory is gone. `Test_run_moves::test_accepts_every_unit_and_takes_away_the_emptied_roots` asserts that `run_moves` removes an emptied `specs/`, and that removal is one `os.rmdir` that does not depend on how the item left. Round 1 ran five mutants with S3 left out: the walk's removal, the test that keeps `src`, the `specs/` cleanup, the walk's direction and the fresh listing. All five went red, so no defect was found that only S3 catches (`rounds/round-1.md` finding 1) |

## Not verified

| Item | Who must answer |
|---|---|
| The fix and S4 on the Linux and Windows legs. Locally only macOS ran them | the orchestrator, by the branch's `tests` workflow run after the push |
| The junction limit in `move`'s docstring: that the walk enters a Windows junction under `src` and removes the empty directories behind it. It was read from `os.walk`'s source and never run on Windows | the repository owner, who directed that the limit gets a sentence and no guard |
| The full suite, the repository-wide lint and format check, and the typecheck at the branch head | the orchestrator, by `broad-gate --record` once the review rounds settle |

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
