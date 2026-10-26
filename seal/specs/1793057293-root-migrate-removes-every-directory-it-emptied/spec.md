# Feature Specification: root-migrate removes every directory it emptied (#1016, #1018)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | The run asks nobody. What the tree does not decide is a written default in `questions.md`, and the owner reviews the pull request |
| executed: `git grep -n -i "root-migrate\|empty director\|emptied" -- docs/` in this worktree | No hit. The policy root (`docs/`, since `seal/config.md` has no `Policy root` row) states nothing about what the root migration removes, so this work changes no rule and its `## Rule changes` is the no-change block |
| `hooks/root-migrate.py#move`, its docstring sentence "The empty directories left behind are removed." | The behaviour the hook already promises. This work makes the sentence hold and rewrites it in place to say exactly what is removed |
| `hooks/root-migrate.py#move`, the bottom-up walk after the file-by-file loop (`os.walk(under(root, src), topdown=False)` and the test `if not dirs and not files`) | The defect. `os.walk` lists a directory's entries before it yields that directory's subdirectories, so when the walk reaches a directory, its `dirs` list still names the subdirectories the walk has just removed. Every directory that held a subdirectory stays, at every depth: the item's own directory, and any subdirectory that held another one. Only directories with no subdirectory are removed |
| executed: `python3 -c "import inspect, os; print(inspect.getsource(os.walk))"` on the local Python 3.15.0 | The listing order the row above states: with `topdown=False`, the directory is scanned into `dirs` and `nondirs`, the tuple is pushed, and its subdirectories are walked and yielded first. CI runs Python 3.12 (`.github/workflows/test.yml`, the matrix rows); its order is not read here, and phase 1's dispatched run measures it (`questions.md` Q1) |
| `tests/test_root_migrate.py#Test_move::test_accepts_a_directory_whole_or_file_by_file_into_one_that_exists`, the comment "the item's own directory, listed before its `rounds/` went, stays on disk empty" and `assert list((proj / "specs" / ITEM).iterdir()) == []` | The case that pins the defect as it stands (#942 changed no shipped code). It is rewritten to refuse it |
| `tests/test_root_migrate.py#Test_main::test_accepts_either_mark_alone_and_resumes_its_item_once_settled` | The resumed shape #1016 names. Its `rounds/round-1.md` row leaves `specs/<ONE_MARK>/` on disk, empty, and the case asserts only that `rounds/` is gone, so nothing pins the item's directory either way |
| `README.md` *Coming up from 0.3.x*, the by-hand line `rmdir .specseal specs  # git mv leaves them empty on disk` | `git mv` of a file leaves its emptied source directories on disk. The hook's own cleanup is therefore the only thing that removes them |
| `hooks/root-migrate.py`'s module docstring, the boundary "only what git tracks", which ends "`.specseal/` may remain on disk holding nothing else" | An ignored file is not a unit and stays where it is. A directory holding one is not empty and is not removed, at any depth |
| `hooks/root-migrate.py`'s module docstring, the boundary "a stopped move resumes" | A run stopped at a file leaves the files it already moved moved. Their source directories stay on disk until the run that finishes the item, so the removal at the end of that run has to see directories an earlier run emptied (*Scope*, item 2) |
| `hooks/root-migrate.py#run_moves`, the loop over `OLD_HOME` and `OLD_ITEMS` after every unit moved | `specs/` and `.specseal/` are removed with one `os.rmdir` each, only once every unit moved, never through a link (contract rule 13, PR #700). The single `rmdir` is kept: `specs/` holds nothing of the plugin's once every item's own directory is gone, and it may still hold a team's directory, which stays |
| `hooks/root-migrate.py#main`, the printed line built from `old_items` and `unmarked` | Read, not run: after a full run, `old_items` lists everything still on disk under `specs/`. The empty directory the defect leaves is id-shaped and carries no tracked mark, so the line names the plugin's own moved work item as "left specs/<id> where it is" with the reason that it is not a SpecSeal work item. The fix removes that clause from the line, which is a change a person reads (contract rule 14) |
| executed: `git show ca66eca5:seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md`, section *`hooks/root-migrate.py`, at df5136f1 and 95db3498*, paragraph *What building it found* | #942's finding, as #1018 cites it: the walk lists the directory's children before it removes them, and `run_moves` then leaves `specs/` too |
| executed: `git grep -n "topdown=False\|os.rmdir\|removedirs\|\.rmdir()" -- '*.py' ':!tests/'` and the same for `shutil.move`, `os.rename`, `os.replace` and `"mv"` | The class (contract rule 12): one bottom-up walk in shipped code, `move`'s. `seal.py`'s mode switch renames the root whole (`os.rename`), and `settle.py` removes a directory with `shutil.rmtree`; neither leaves an emptied directory. `move` takes no unit kind, so a directory under `.specseal/` merged into an existing `seal/<name>/` is the same instance as a work item, and the same fix covers it |
| contract rules 13 and 15 | A case is seen red before it is planted. The fix's emptiness test is the code's own, so the case that pins it still holds with `os.rmdir` given a semantics that removes a directory with something in it (*Scope*, item 3) |
| The owner's direction in the spawn prompt (not a tree document) | The fix is seen red first on Linux, macOS and Windows, which CI runs. Edge cases the one-issue automation flow cannot produce get a limit sentence and no guard |

## Scope

**The design in one paragraph.** `move`'s bottom-up walk stays, and it
decides whether a directory is empty when it reaches that directory, from a
fresh listing, rather than from the listing `os.walk` took before the
directory's subdirectories were removed. Every directory under `src` that
holds nothing at that moment is removed, the deepest first, and `src` with
them. So a work item's directory, and every subdirectory of it, goes when
the move leaves nothing in it, whichever run emptied it. `run_moves` then
finds `specs/` empty where it held only work items, and removes it as it
does today.

### In

1. **The emptiness test reads the directory when the walk reaches it.**
   `hooks/root-migrate.py#move` keeps `os.walk(under(root, src),
   topdown=False)` and replaces `if not dirs and not files:` with a test
   that lists `here` again at that moment (`os.listdir`) and removes it with
   `os.rmdir` only when the listing is empty. An `OSError` from either call
   is passed over, as the `rmdir` is today.
2. **Both shapes, one fix.** The merge of a directory holding subdirectories
   into one that exists (#1018), at any depth. The resumed move (#1016),
   including a directory an earlier, stopped run emptied: that run moved
   its files and stopped before the walk, and the run that finishes the item
   removes it.
3. **An ignored file keeps its directory.** A directory under `src` that
   holds an ignored file, such as `.DS_Store`, is not empty, so it stays,
   with every directory above it up to `src`. The test is the code's own
   listing, so this holds with `os.rmdir` given a semantics that removes a
   non-empty directory (contract rule 13).
4. **The docstring states it.** `move`'s sentence "The empty directories
   left behind are removed." is rewritten in place to say that every
   directory under `src` holding nothing when the walk reaches it is
   removed, deepest first, `src` included, and that one an ignored file
   holds stays. One limit sentence follows it: a directory link or a Windows
   junction placed under `src` by hand is not something git checks out,
   and the walk is not guarded against one (the direction above).
5. **The cases.** The two cases that pin the defect are rewritten to refuse
   it, and two are added (*User scenarios & acceptance*). Every case is
   seen red before the fix lands, locally and on CI's three legs
   (`plan.md` *Phases*).

### Out

- **`run_moves`'s cleanup of `.specseal/` and `specs/`.** It stays one
  `os.rmdir` each. A recursive removal there would reach a team's directory
  under `specs/`, which the module docstring says stays.
- **A repository the hook already migrated.** Its marker is stamped and
  `moves()` lists nothing, so the hook returns before any walk, and an empty
  `specs/<id>/` an earlier release left stays until a person removes it.
  Sweeping it would make the hook read the old tree after the migration,
  against the boundary "silent when there is nothing to do" and against the
  `# RIDER:` that says the file is deletable once no repository is left to
  migrate.
- **The cleanup on a stopped run.** A run that stops at a file does not walk
  before it raises, as today. The run that finishes the item removes what
  every earlier run emptied (*In* item 2), so the stopped state a person
  settles by hand keeps its layout.
- **The printed line for an item's directory an ignored file keeps.** Such a
  directory stays on disk, so `main`'s line still names it as left and not a
  SpecSeal work item. `questions.md` Q2 holds it.
- **`README.md`'s by-hand block.** It moves each work item whole with
  `git mv specs/<id> seal/specs/<id>`, which leaves no directory behind, so
  it does not change.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a merge into an existing directory, at depth two (#1018) | Given the old layout's work item `specs/<ITEM>/` with `routing.md`, `rounds/round-1.md` and a committed file two directories down, such as `phases/deep/p.md`, and `seal/specs/<ITEM>/spec.md` already present. When `move` moves `specs/<ITEM>` to `seal/specs/<ITEM>`, then every file is at its destination and `specs/<ITEM>` does not exist | `Test_move::test_accepts_a_directory_whole_or_file_by_file_into_one_that_exists`, rewritten: the comment and the `iterdir() == []` assertion go, and the case asserts the directory is gone. The nested file is planted in the case, not in the module's fixture. Seen red against the current walk |
| S2 a resumed move, with a directory an earlier run emptied (#1016) | Given a work item `specs/<ONE_MARK>/` holding one mark (each row of the case's parameter), `phases/phase-1.md` and `spec.md`, and `seal/specs/<ONE_MARK>/spec.md` already present. When the first start moves `phases/phase-1.md` and stops at `spec.md`, the person runs `git rm specs/<ONE_MARK>/spec.md`, and the next start runs, then `specs/<ONE_MARK>` does not exist, and the printed line does not name `specs/<ONE_MARK>` | `Test_main::test_accepts_either_mark_alone_and_resumes_its_item_once_settled`, extended: `phases/phase-1.md` planted, and the assertion that `rounds/` is gone replaced by one that the item's directory is gone, plus one that the line does not name it. Seen red against the current walk on both rows: the first start leaves `phases/` empty, and the second start's walk removes it after it has already listed the item's directory as holding `phases/` |
| S3 `specs/` goes once its work items have (#1018) | Given `specs/` holding only the work item (`specs/notes` removed and committed) and S1's destination file present. When `run_moves` moves every unit, then it returns every unit moved with no error, and neither `specs/<ITEM>` nor `specs/` exists | a new case in `Test_run_moves`, seen red against the current walk |
| S4 an ignored file keeps its directories | Given S1's item with an ignored `rounds/.DS_Store` on disk beside its tracked round file. When `move` runs with `os.rmdir` replaced by one that removes a directory whatever it holds, then `specs/<ITEM>/rounds/.DS_Store` is still there | a new case in `Test_move`. It passes against the current walk, which reads the stale listing, so it is seen red against the fix with its fresh listing taken out (contract rule 15, the sentence it pins deleted) |
| S5 the rest of the module | Given the fix. When `tests/test_root_migrate.py` and `tests/test_the_root_migrates_itself.py` run, then both pass | the smith runs both modules (contract rule 2: the module and the one it touches) |

## Data & interfaces

- `hooks/root-migrate.py#move(root, src, dst)`: signature, return and
  `MoveError` unchanged. What changes is which directories under `src` are
  gone when it returns without raising.
- `hooks/root-migrate.py#main`'s printed line: a work item the run moved is
  no longer named in its "left ... where it is" clause, because its
  directory is gone. The line's wording is unchanged.
- No file format, no config row, no environment variable.

## Rule changes

- nothing
  why: The policy root states nothing about which directories the root migration removes (executed `git grep`, *Grounding*). The behaviour is stated once, in `hooks/root-migrate.py#move`'s docstring, which the build rewrites in place.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The stale emptiness test | `hooks/root-migrate.py#move`, `if not dirs and not files:` inside the bottom-up walk | replaced by a fresh listing of the directory when the walk reaches it (*Scope*, *In* item 1) |
| The docstring sentence the code did not hold | `hooks/root-migrate.py#move`, "The empty directories left behind are removed." | rewritten in place to the sentence and limit of *In* item 4 |
| The pin on the empty directory | `tests/test_root_migrate.py#Test_move::test_accepts_a_directory_whole_or_file_by_file_into_one_that_exists`, the comment beginning "The walk removes each emptied directory below the item" and `assert list((proj / "specs" / ITEM).iterdir()) == []` | S1 asserts the directory is gone |
| The resumed case's narrower assertion | `tests/test_root_migrate.py#Test_main::test_accepts_either_mark_alone_and_resumes_its_item_once_settled`, `assert not (proj / "specs" / ONE_MARK / "rounds").exists()` | S2's assertion that `specs/<ONE_MARK>` is gone, which covers `rounds/` |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-27 by framer, before the build.
