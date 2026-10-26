# Implementation Plan: root-migrate removes every directory it emptied (#1016, #1018)

Approved 2026-10-27 by the orchestrator, when `smith` was spawned.

## Summary

`hooks/root-migrate.py#move` keeps its bottom-up walk and decides whether a
directory is empty when the walk reaches it, from a fresh `os.listdir`, in
place of the listing `os.walk` took before the directory's subdirectories
were removed. A work item's directory and every subdirectory of it then go
when the move leaves nothing in them, in a merge into an existing
destination (#1018) and in a resumed move (#1016), whichever run emptied
them. `run_moves` then removes an emptied `specs/` as it does today. The
cases that pin the empty directory are rewritten to refuse it, and they are
seen red on CI's three operating systems before the fix lands.

## Technical context

- `hooks/root-migrate.py` lines 352 to 394, `move`. Line 362 sends a file
  through one `git mv`, and line 367 a directory whose destination is absent.
  Lines 370 to 388 move a directory into an existing destination file by
  file, the marks last. Lines 389 to 394 are the walk this work changes:
  `os.walk(under(root, src), topdown=False)` and `if not dirs and not
  files:` before `os.rmdir(here)`, with `OSError` passed over.
- Why the walk misses (read: `os.walk`'s source, printed by `inspect` on
  Python 3.15.0, `spec.md` *Grounding*). With `topdown=False`, `os.walk`
  scans a directory into `dirs` and `nondirs`, then walks and yields its
  subdirectories, then yields the directory with the lists it scanned first.
  The walk removes an emptied `rounds/`, and the item's directory then
  arrives with `dirs == ["rounds"]` and stays. The same holds at every
  depth: a directory is removed only where it never held a subdirectory.
- `git mv` of a file leaves its emptied source directories on disk
  (`README.md` *Coming up from 0.3.x*, the `rmdir` line; the current
  `Test_move` case asserts the empty item directory exists). So the walk is
  the only thing that removes them.
- `hooks/root-migrate.py` lines 414 to 438, `run_moves`. After every unit
  moved, `.specseal/` and `specs/` each get one `os.rmdir`, skipped for a
  link (PR #700, contract rule 13). Unchanged by this work: once the item
  directories are gone, `specs/` is empty unless it holds something not
  the plugin's.
- `hooks/root-migrate.py` lines 549 to 565, `main`'s printed line. It names
  everything `old_items` finds on disk under `specs/` after the run. The
  directory the defect leaves is id-shaped with no tracked mark, so the
  line calls the plugin's own moved item "not a SpecSeal work item". The fix
  removes that clause, and S2 pins its absence.
- `tests/test_root_migrate.py` lines 412 to 426 (`Test_move`, the case S1
  rewrites), lines 629 to 649 (`Test_main`, the resumed case S2 extends),
  lines 464 to 469 (`Test_run_moves`, beside which S3 goes) and lines 486 to
  507 (the Windows `rmdir` case, the shape S4 copies to replace `os.rmdir`).
  The module fixture `_templates` is copied by every case, and it stays
  unchanged: S1's nested file and S2's `phases/phase-1.md` are planted in
  their own cases, so no other case's count of units or calls moves.
- **The failure scenario of the chosen approach, six months on.** A later
  edit shortens the fresh listing to a bare `os.rmdir` attempt, which every
  real platform refuses on a non-empty directory, so every behaviour case
  stays green. S4 is the case that goes red then, because it gives
  `os.rmdir` a semantics that removes a non-empty directory. A second
  scenario: a person places a directory link or a Windows junction under a
  work item's directory by hand. Python's `os.walk` does not walk into a
  symbolic link, and on Windows it walks into a junction, so the walk could
  remove empty directories inside the junction's target. Git checks out
  neither, and the one-issue flow cannot produce one, so `move`'s docstring
  states it as a limit and nothing guards it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Keep the walk; read each directory again when the walk reaches it, and remove it when that listing is empty | It also removes an empty directory under `src` that this move did not empty, such as one an earlier, stopped run emptied, or one that was empty before. Nothing is lost by that: git tracks no empty directory, so such a directory never held anything git knew of, and the whole-directory branch already carries it away with `src`. A junction placed under `src` by hand is the limit above | **chosen.** The premise that keeps the walk, checked: every directory under `src` that holds nothing when the walk reaches it is something the old layout left, never work. `README.md`'s by-hand line and the current `Test_move` pin say `git mv` leaves such directories; an ignored file keeps its directory non-empty, so it stays (S4); an untracked file stops the run before any move (`dirty`, `Test_dirty`) |
| B. Replace the walk: track what this call emptied. Collect each moved file's parent directories up to `src`, and after the loop remove them deepest first where empty | The resumed shape (#1016). A run stopped at a taken file has already moved the files before it, and their directories stay on disk, because the stopped run raises before any removal. The run that finishes the item moves none of those files, so it never tracks their directories, and `src` stays holding them. S2's `phases/` is that state. Adding a removal on the stopped path does not close it: a run stopped under 0.22.3, which removes nothing on a stop, or a process killed mid-run, leaves the same state for the tracking run to miss | rejected. It is exact about what one call emptied, and the hook's resume is several calls |
| C. Remove `src` whole with `shutil.rmtree` after the loop | It deletes an ignored file under `src`, a `.DS_Store` or a person's ignored notes, against the module docstring's boundary "only what git tracks", which says an ignored file stays where it is | rejected |
| D. Walk from each moved file's directory upwards with `os.removedirs` | `os.removedirs` climbs past `src` into `specs/` and above, removing every parent that becomes empty. That takes `run_moves`'s decision about `specs/` and `.specseal/` away from it, and it climbs through a directory link where `run_moves` refuses one | rejected |
| E. Keep the walk as it is and walk again until a pass removes nothing | It reaches A's result with one pass per level of depth, and keeps the stale listing that caused the defect | rejected |
| F. Keep `run_moves`'s single `os.rmdir` of `specs/` and `.specseal/`, against replacing it with a recursive removal | A recursive removal would reach a team's directory under `specs/`, which stays (module docstring, `Test_main::test_accepts_only_work_items_under_specs_and_names_the_rest`) | kept. The premise, checked: with A, every work item's directory is gone before this loop runs, so `specs/` is empty exactly when nothing but work items was in it |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The cases, red, with no change to `hooks/root-migrate.py`: S1 rewrites `Test_move::test_accepts_a_directory_whole_or_file_by_file_into_one_that_exists` (its comment and its `iterdir() == []` assertion go), S2 extends `Test_main::test_accepts_either_mark_alone_and_resumes_its_item_once_settled`, and S3 is a new `Test_run_moves` case, each as `spec.md` *User scenarios & acceptance* states it. One commit | The smith runs `bin/test tests/test_root_migrate.py -q -p no:xdist` and reads its exit code directly: 1, with S1, both rows of S2 and S3 the only failures. After the commit, the orchestrator pushes the branch and dispatches `tests` on it (`gh workflow run tests --ref fix/1016-root-migrate-removes-every-directory-it-emptied`); on the Linux leg and on the macOS and Windows legs that hold `tests/test_root_migrate.py`, those cases are the failures (`questions.md` Q1) | db3670d2 |
| 2 | The fix: `move`'s walk reads each directory again when it reaches it (`spec.md` *In* items 1 to 3), its docstring sentence rewritten in place with the limit sentence (*In* item 4), and S4 added | S4 seen red with the fresh listing taken out of the fix, then green; S1 to S3 green; `bin/test tests/test_root_migrate.py tests/test_the_root_migrates_itself.py -q` exits 0 (S5). The broad gate is the orchestrator's, once, after the review rounds (contract rule 2) | d2dd3584 |

## Operational impact

None a deployer has to act on: no migration, no environment variable, no
dependency, no config row. A repository whose root migration stopped under
an earlier release and resumes under this one gets the directories that
migration emptied removed at the run that finishes it. A repository the hook
already migrated is not revisited, and an empty `specs/<id>/` an earlier
release left there stays until a person removes it (`spec.md` *Out*).
