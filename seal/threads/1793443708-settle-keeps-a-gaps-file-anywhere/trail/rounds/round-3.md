# Review round 3: 1793443708-settle-keeps-a-gaps-file-anywhere

```seal
target: df5cba11, fixes e60e8df3..df5cba11
```

## Findings

## Confirmations

```seal
confirms: round-2#1
```
The close holds. d79bed62 replaces the inline `try` around `os.symlink` at `tests/skills/test_settle.py:1161` with `symlink_or_skip(held, trail / "rounds", directory=True)`, as round 2 proposed (read). `symlink_or_skip` is already imported at `:47`, and `os` and `pytest` stay in use in the module (read). Removing `trail.mkdir()` was the mutation round 2 saw survive as a skip. This round re-ran it at df5cba11, and the `link` shape failed on "the link's parent does not exist" (executed, `## Probes`). The old `except` also caught `NotImplementedError`, and the helper does not. Python raises that only on Windows before 6.0, and the repository needs Python 3.12, so no supported platform loses a skip. The old skip message is pinned nowhere (read, round 2's `git grep`).

Claimed: the class is every link a case makes in the seven files this work item touches. Those files come from `git diff --name-only` without the records. The search in them found only the helper's own `os.symlink` at `tests/conftest.py:647` and `shutil.copytree(..., symlinks=True)` at `:1412`. Found: `git diff --name-only 5560c742..df5cba11` gives the same seven non-record files (executed). The crafter's `git grep` over them, re-run, lists the helper's docstring and its call at `tests/conftest.py:627-655`, the helper's own call at `:647`, the copy at `:1412` and the import at `tests/skills/test_settle.py:47`. No other case makes a link outside the helper (executed). `:1412` is `World.__init__` copying a template tree, and it keeps the template's links as they are. It makes no link of a case's own, so it is outside the class (read). The answer says the search reads spellings and is a sample beyond the spellings listed (contract rule 12). That is the right label for it.

```seal
confirms: none
```
The records commit df5cba11 changes only round 2's `verdict:` line and `answer:` line (executed, `git diff -U0 e60e8df3..df5cba11 -- seal`). d79bed62 touches `tests/skills/test_settle.py`, the path round 2's `location:` names (executed, `git diff --stat`). The fix diff adds no unit beyond the one call. So round 2's confirmations of the new units and of round 1's first finding were carried as coordinates and not re-derived this round. `bin/test tests/skills/test_settle.py -q -rs` at df5cba11 gave 101 passed and none skipped (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the repository-wide lint and the format check (the `Broad gate` row). `tests/conftest.py` changed in the work item, so every module reads it | `seal/config.md` | the orchestrator, by `seal gate --base origin/release/v0.27.0 --record 1793443708-settle-keeps-a-gaps-file-anywhere` |
| Whether Windows needs `target_is_directory` for a link to a directory that already exists, carried from round 2 | `tests/conftest.py:627-629`, `tests/skills/test_seal.py:637`, `tests/skills/test_seal.py:1164` | the `windows-latest` legs of `.github/workflows/test.yml` on the pull request |
| Both `Test_misplaced` cases and the `link` shape run, none skipped, on Windows | `gaps.md` *Not verified* | the `windows-latest` legs of `.github/workflows/test.yml` on the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_settle.py -q -rs`, in a `git clone --no-local` of the worktree at df5cba11 | exit 0, 101 passed, none skipped |
| `bin/seal mutate tests/skills/test_settle.py --tests "bin/test tests/skills/test_settle.py -q -p no:xdist -rs -k link"`, removing `trail.mkdir()` in `test_a_work_item_whose_rounds_cannot_be_listed_is_not_counted_as_none` | red: `AssertionError: the link's parent does not exist`; file restored |
| `git grep -n -E "symlink\|symlink_to\|hardlink\|os\.link\(\|\.link_to\(\|mklink\|ln -s\|CreateSymbolicLink\|junction"` over the seven non-record files, setting aside `symlink_or_skip(` calls | `tests/conftest.py:627-655` (the helper), `:1412` (the template copy), `tests/skills/test_settle.py:47` (the import); nothing else |
