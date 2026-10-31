# Design: 1793457436-row-deletion-check-and-a-symlink

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-record-layout.md` *The fold, and what tells it from a deletion* | Under `--baseline`, a `## Not verified` table that holds fewer rows than at the merge base fails the run. This work changes no part of that rule. It makes the code meet it where a tracked link stands beside its target. |
| `docs/the-record-layout.md` *The fold, and what tells it from a deletion*, the bullet *A line a record's rows are COUNTED on is blanked the same way on both sides of a comparison* | The two sides of a row comparison are read by one rule. This work applies the same principle one level up: both sides read the same file. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | A script names what it did not read and decides nothing on it. A kept path that no commit of the repository can hold is therefore named as not compared, never skipped in silence (Scope item 2). |
| `docs/what-a-script-gates.md` *The checks*, row `seal unverified` | The row says what the check reads and refuses. Nothing in it changes, so no rule change is owed (`## Rule changes`). |
| executed: `sh <scratch>/probe.sh`, run against a `git clone --no-local` of this branch at 3d9828ce, five repositories each holding one `## Not verified` table of 3 rows | (1) `specs/a/gaps.md -> ../b/gaps.md`, two rows deleted from `specs/b/gaps.md`: `1 closing memos · 1 open · 0 closed · 0 unreadable · 1 not compared`, the notice reading `(no ## Not verified section)`, EXIT=0. (2) The same with the link at `specs/z`: `3 rows at HEAD, 1 here`, EXIT=1. (3) The link alone under the scanned `specs/`, its target at `other/b/gaps.md`: EXIT=0 with the same notice. (4) The link's target outside the repository: EXIT=0 with the same notice. (5) A link at the base replaced by a real file of 1 row, the target still holding 3: EXIT=0 with the same notice. The defect the issue reported stands at this base, and (3) is a second instance of it. |
| executed: `git -C <r1> show HEAD:specs/a/gaps.md` | Prints `../b/gaps.md`, the link's blob. That text is what `check_text` was handed for the base side in (1). |
| executed: the same probe after replacing the body of `unique_by_target` with `sorted(dict.fromkeys(os.path.realpath(p) for p in paths))` in the scratch clone | (1), (2) and (3) exit 1 with `3 rows at HEAD, 1 here`, each naming the real file. (4) exits 0 with no notice at all, because `git show <ref>:../outside/gaps.md` exits 128 and `show()` returns None. (5) is unchanged. So the chosen change needs Scope item 2, or it turns a notice into silence. |
| read: `skills/verify/scripts/unverified_check.py#show` | `show()` already passes `encoding="utf-8", errors="replace"`, as `check_file` does. The issue's second box holds at this base. `tests/skills/test_unverified_check.py#Test_show` has two cases, and neither feeds it a byte that is not UTF-8, so nothing pins the box. |
| read: `skills/verify/scripts/unverified_check.py#overviews` and `#main` | `overviews` resolves each argument once with `real()`. `os.walk` is called without `followlinks`, so it does not enter a linked directory. A link therefore reaches `unique_by_target` only as a file named `gaps.md`. The presence arm builds `here` from the unresolved `files` list, and `overviews_at` lists a tracked link under its own path. That arm keeps every path, and this work leaves it alone. |
| read: `tests/skills/test_unverified_check.py#linked` | The fixture's link is `specs/1780000001-other/gaps.md -> ../1780000000-work/gaps.md`. The link sorts after its target, which is the order in which the defect cannot show. |
| read: `tests/conftest.py#symlink_or_skip` | A case makes its links through this helper, which skips where the platform refuses `os.symlink`. #1221 (open) records that no Windows run names its skipped cases, and the new cases meet that limit (`frame/questions.md` Q1). |
| read: the orchestrator's line on the issue's one comment, and `gh issue view 19 --json body,comments` (executed) | The comment moved the issue to 0.27.0. It says `unique_by_target` kept the first path in sort order there and the `show()` encoding half was already fixed. Both hold at a92c358b, after #1198 (7a8899d5). |

## Scope

In:

1. `unique_by_target` keeps one path per real file, and the path it keeps is the real file's own path (`os.path.realpath`), whichever path the scan reached it by. The tree side and the base side of the row comparison then read the same file. This holds wherever the link sorts, and whether or not the target lies under the scanned path.
2. A kept path that lies outside the repository is not read at the base. It is named under `not compared`, and the reason says the file is outside the repository, which no commit of it holds. Today such a link reaches the same list with a reason that is false (`no ## Not verified section`). After item 1 it would leave the report in silence (Grounding, the second probe).
3. `unique_by_target`'s docstring is rewritten in place to say which path is kept and why.
4. Cases in `tests/skills/test_unverified_check.py`:
   - a link whose directory sorts **before** its target's, with rows deleted from the target: exit 1, the line naming the target;
   - the link alone under the scanned path: exit 1;
   - a target outside the repository: exit 0 with the item 2 notice, its text pinned;
   - `show()` decoding a byte that is not UTF-8 the way `check_file` does;
   - `Test_unique_by_target` stating that the real path is kept.

Out:

- **A link at the base replaced by a real file** (probe 5). The run names the file as not compared and exits 0. No row left the record, because the link's target still holds every row. The notice's reason (`no ## Not verified section`) is imprecise. Making it precise means asking `#mode_at` for every scanned real file as well as for each link, one more `git ls-tree` per closing memo, for a case that passes no deletion. It is left as it stands.
- **The other readers that take a file from `git show` or `git cat-file blob`** (`skills/verify/scripts/test_layout.py#_moved_main`, `skills/code-review/scripts/chain_check.py#read_record`, `skills/implement/scripts/seal.py#staged_text`, and the history readers in `seal_stamp.py`, `pact_check.py`, `publish_release_note.py` and `tag_release.py`). The list comes from `git grep -n -E '"show",|cat-file' -- '*.py' ':!tests' ':!evals'` (executed). Each one would read a link's blob for a link. None of them reads a path that this repository or the plugin's own layout makes a link. The two that compare against a working-tree read (`_moved_main` and `staged_text`) fail loudly on a mismatch: an unparsable module, or a file that differs. Neither passes in silence. The issue names only the row-deletion check.
- **Naming the skipped link cases on Windows.** That is #1221's.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A link sorts before its target | Given a tracked `gaps.md` link whose directory sorts before the target's, and two rows deleted from the target without being closed. When `seal unverified --baseline <ref> <dir>` runs, then it exits 1 and the deletion line names the target's path with `3 rows at <ref>, 1 here`. | the case of Scope item 4, seen red against the current `unique_by_target` |
| A link sorts after its target | Given the same with the link sorting after its target, then the same exit and line. | the existing order, kept by the fixture beside the new one |
| Only the link is under the scanned path | Given a link under the scanned directory whose target lies elsewhere in the repository, and rows deleted from the target. When the check runs on the link's directory alone, then it exits 1 naming the target. | a case of Scope item 4 |
| The target is outside the repository | Given a tracked link to a file outside the repository. When the check runs with `--baseline`, then it exits 0, prints the file's open rows, and lists it under `not compared` with a reason saying it is outside the repository. | a case pinning the notice's text (contract rule 14) |
| A link and its target are counted once | Given both paths under the scanned directory, then the tally counts one closing memo and its open rows once, and the presence arm reports neither path as deleted. | `test_accepts_a_tracked_link_counted_once_and_not_deleted`, run against the fixture with both link orders |
| The base side decodes as the tree side | Given a closing memo whose committed text holds a byte that is not UTF-8. When `show()` reads it at a ref, then it returns the text with U+FFFD where `check_file` puts it, and raises nothing. | a `Test_show` case, seen red with `show()` reverted to `text=True` |

## Data & interfaces

- `skills/verify/scripts/unverified_check.py#unique_by_target(paths)` returns the sorted, de-duplicated real paths of `paths`. Its two callers in `#main` (the per-file loop and the tally) take them as they are.
- `skills/verify/scripts/unverified_check.py#main`, in the `--baseline` arm of the per-file loop: a kept path whose `repo_relative` form leaves the repository root (`..` as its first component) is appended to `uncompared` with the Scope item 2 reason. It is not handed to `show()`. A path with no relative form at all is refused before the loop, as it is today.
- `skills/verify/scripts/unverified_check.py#mode_at` asks `git ls-tree` whether a path was a link (`120000`) at the base, and `#compare_at` holds the one comparison of a path's rows at the base with the rows read here. After the per-file loop, each scanned path that is a link here and was not one at the base is compared again at its own path, against the rows its target holds now (round 1's finding 1).
- What a person sees changes in three places. A deletion found through a link is reported under the target's path, where the link's path stood. A link to a file outside the repository is listed under `not compared` with a new reason. A closing memo that became a link on the branch, to a file holding fewer rows, is reported under the link's own path.

## Rule changes

- nothing
  why: The policy already says a `## Not verified` table that lost rows against the merge base fails the run (`docs/the-record-layout.md` *The fold, and what tells it from a deletion*). This work makes the code meet that rule where a tracked link sorts before its target. Which path the check keeps is a property of the script, stated in its docstring.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The rule that the first path in sort order is kept for a real file | `skills/verify/scripts/unverified_check.py#unique_by_target` | The same docstring, rewritten in place: the real file's own path is kept. |
| The `not compared … (no ## Not verified section)` notice a kept link produced, which compared a link's blob with its target's text | `skills/verify/scripts/unverified_check.py#main` | Gone for a link inside the repository, whose target is now compared. A link to a file outside the repository is named with a reason that is true (Scope item 2). |

Framed 2026-10-31 by framer, before the build.
