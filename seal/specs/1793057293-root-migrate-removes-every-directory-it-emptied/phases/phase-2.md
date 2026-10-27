# Phase 2: 1793057293-root-migrate-removes-every-directory-it-emptied

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | d2dd3584 |

## What this phase was asked

Build the fix `plan.md` names: `move`'s walk lists each directory again when
it reaches it and removes it only when that listing is empty. Rewrite the
`move` docstring in place, with the junction limit sentence. Add S4 and see
it red under the mutant that drops the re-read. Then write `phases/phase-2.md`,
the work item's `overview.md` and `changelog.md` in the shape of earlier work
items, and `plan.md`'s Status cell. Record Q1's answer in `questions.md` and
here: the `tests` run 40421812732 at `07638965` failed exactly the four
`tests/test_root_migrate.py` cases on ubuntu, macOS and Windows. The only
other failure in that run was
`tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which this phase's `overview.md` answers. Run `tests/test_root_migrate.py`,
`tests/test_the_root_migrates_itself.py` and
`tests/test_chain_hooks_hardening.py`, `bin/test-layout --check` and
`--pairs`, and `uvx ruff check` and `uvx ruff format --check` over the
changed Python files, and not the whole suite. Build on `questions.md`'s
defaults.

## What this phase found

**Q1 is answered (a)** (`executed`: `gh run view 40421812732 --log-failed`,
read). The run's head is `07638965`. Its failing jobs were the ubuntu leg,
macOS groups 1 and 2, and Windows groups 2 and 3. Across them, each of S1,
S3 and the two S2 rows failed once per system, and
`test_every_spec_directory_that_reached_the_ladder_has_an_overview` failed
once per system. No other case failed. So Python 3.12 lists a directory
before it yields its subdirectories on all three systems, and every case
pins something on each of them. `questions.md` Q1's Status carries the
answer.

**The frame holds, except for one sentence about links** (`read`). The walk
is where phase 1 found it, and `git grep` for `topdown=False`, `os.rmdir`,
`removedirs` and `.rmdir()` in shipped Python still finds one bottom-up walk,
`move`'s (`executed` at `d2dd3584`). The exception is *In* item 4's limit
sentence, "a directory link or a Windows junction placed under `src` by hand
is not something git checks out". Git does track a symbolic link, and a
tracked one is listed by `git ls-files` and moved by `git mv` before the
walk starts. An untracked link is not entered: `os.walk`'s bottom-up branch
excludes "symlinks to directories if followlinks is False" (read in
`os.walk`'s source on the local Python 3.15.0). Its parent's fresh listing
names the link, so the parent is not empty and stays. A Windows junction is
the case left. `DirEntry.is_symlink()` is false for one, so the walk enters
it and removes the empty directories behind it. The docstring states that
limit alone. `overview.md` records it as a divergence, and nothing ran on
Windows to show it (`unverified`).

**The fix.** `move`'s walk keeps `os.walk(under(root, src), topdown=False)`.
At each directory it calls `os.listdir(here)` and calls `os.rmdir(here)`
only where that listing is empty. One `try` covers both calls and passes
over an `OSError`. A comment above the loop says why the walk's own lists
are not used. The docstring sentence "The empty directories left behind are
removed." is rewritten in place. It now says that every directory under
`src` holding nothing when the walk reaches it is removed, deepest first and
`src` last, whichever run emptied it. It says that a directory an ignored
file holds stays, with every directory above it. The junction limit follows.

**A second limit sentence, from round 1's Not judged row** (`read`). The
round's row is a directory another process holds open on Windows, where
`os.rmdir` raises. Its probe simulated that on macOS: the directory and every
one above it stayed, and nothing raised. The owner's standing direction is
that an edge the one-issue flow cannot produce gets a limit sentence and no
guard. So round 1's fix pass added one beside the junction's: where the
removal of a directory fails, that directory and every one above it stay,
and nothing is removed by mistake. The "is removed" sentence now names that
exception with "unless its removal fails". The changelog fragment's
`Limits` line carries the same sentence. Nothing ran it on Windows
(`unverified`).

**S4, as built**, is
`Test_move::test_refuses_to_remove_a_directory_an_ignored_file_holds_under_any_rmdir`.
It commits a `.gitignore` naming `.DS_Store`, writes
`specs/<ITEM>/rounds/.DS_Store` and `seal/specs/<ITEM>/spec.md`, and gives
`os.rmdir` a semantics that empties a directory and then removes it. The
replacement keeps the real `os.rmdir` for the removal itself. `shutil.rmtree`
would call the patched `os.rmdir` and recurse. The case then runs `move` and
asserts that `rounds/round-1.md` is at its destination and that the
`.DS_Store` is still in `specs/<ITEM>/rounds/`. It uses S1's merge shape
without S1's nested file, which pins nothing here.

**S4 was green before the fix, and red under the mutant that drops the
re-read** (`executed`). Before the fix,
`bin/test tests/test_root_migrate.py -q -p no:xdist -rf` exited 1 with 4
failed and 70 passed. The four were S1, S3 and both S2 rows, and S4 passed,
as `spec.md`'s S4 row says it would. Replacing the fresh listing with the
stale one is the code before the fix, so it cannot show S4 red. The mutant
for "drops the re-read" is therefore the plan's six-month failure scenario:
`if not os.listdir(here):` replaced with `if True:`, a bare `os.rmdir`
attempt at every directory. `bin/mutation-check` with that one mutant and
`-k an_ignored_file_holds_under_any_rmdir` exited 0 and printed
`red: the cases failed against the mutation (exit 1)`. The failure was S4's
`.DS_Store` assertion.

**Every added unit was mutated, in one batch** (`executed`, exit 0).
`bin/mutation-check hooks/root-migrate.py` was run over `Test_move`,
`Test_run_moves` and the resumed `Test_main` case, with three mutants: the
listing test replaced with `if True:`, `os.rmdir(here)` replaced with
`pass`, and `topdown=False` turned to `topdown=True`. It printed
`3 mutants, 3 red, 0 SURVIVED, 0 with no verdict`. The working tree was
clean after both runs.

**The cases after the fix** (`executed`, exit 0 each).
`bin/test tests/test_root_migrate.py tests/test_the_root_migrates_itself.py
-q -p no:xdist` passed 79. `uvx ruff check` and `uvx ruff format --check`
over `hooks/root-migrate.py` and `tests/test_root_migrate.py` were clean.
`bin/test-layout --check` refused nothing, and its reports on
`hooks/root-migrate.py` are the three phase 1 saw (`git`, `say` and `under`
have no class). `--pairs` named no pair in either file.

**The records' checks** (`executed`, exit 0 each, with `overview.md`
written). `bin/test tests/test_chain_hooks_hardening.py -q` passed 26,
`test_every_spec_directory_that_reached_the_ladder_has_an_overview` among
them, which was the one other failure in run 40421812732.
`bin/test tests/test_a_question_says_who_can_answer_it.py
tests/test_the_changelog_is_gathered_at_release.py -q` passed 15.
`bin/unverified-check` over the work item read `overview.md` with 3 open
rows and none unreadable.
