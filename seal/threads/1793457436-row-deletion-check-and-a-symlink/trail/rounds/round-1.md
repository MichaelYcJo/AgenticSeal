# Review round 1: 1793457436-row-deletion-check-and-a-symlink

```seal
target: b2e4ca18 against origin/release/v0.27.1
```

This is the first round, so no earlier round's coordinates were carried. Every fact below was established this round, in a worktree of the branch at b2e4ca18 and in a `git clone --no-local` of it under the round's scratch directory.

## Findings

### 1. A closing memo that was a real file at the base and is a link in the branch loses its rows with exit 0

```seal
severity: must
location: `skills/verify/scripts/unverified_check.py:1103-1116`, `skills/verify/scripts/unverified_check.py:1587-1652`, `tests/skills/test_unverified_check.py:2204`
evidence: executed `sh <scratch>/test_tmp_real_to_link.sh`
```

Why it matters: the check exists to refuse a row that leaves a `## Not verified` table without being closed. `docs/the-record-layout.md` *The fold, and what tells it from a deletion* says that a pull request removing "a `gaps.md` from a directory that stays, or a row from a table is still a deletion". After this change, one such deletion passes in every order. Before it, the same deletion was refused in one order.

The cause is the change's own design. `unique_by_target` now keeps only the real path (`unverified_check.py:1116`), and the loop at `unverified_check.py:1587` reads the base side only at that kept path (`unverified_check.py:1604`). A scanned path that is a link in the tree is therefore never read at the base, whatever it held there. The presence arm does not catch the case either. It builds `here` from the unresolved paths (`unverified_check.py:1655`), so the link counts as the memo still standing.

The probe built a repository with `specs/a/gaps.md` holding three rows and `specs/b/gaps.md` holding one. It committed that, then replaced `specs/a/gaps.md` with a tracked link to `../b/gaps.md` and committed again. It ran `unverified_check.py specs --baseline HEAD~1` against b2e4ca18 and against a92c358b:

- At b2e4ca18 the run printed `1 closing memos · 1 open · 0 closed · 0 unreadable` and exited 0, with the link at `specs/a` and with the link at `specs/z`.
- At a92c358b, with the link at `specs/a`, the run printed `specs/a/gaps.md:1  3 rows at HEAD~1, 1 here` and exited 1. With the link at `specs/z`, it exited 0, because the old rule kept `specs/b/gaps.md`, which sorts first.

So in the order where the link sorts first, the change turns a refusal into a pass. It is a regression against the merge base. It is not a case that was already missed and stays missed.

The class (contract rule 12, built from what produces the defect) is every scanned path whose tree entry is a link and whose base entry was a regular file. Two cases make up that class. A link to another memo inside the repository passes in silence: the probe above, in both orders. A link to a file outside the repository is named by the Scope item 2 notice, but the base rows at the link's own path are still never compared. The frame looked only at the reverse transition, a link at the base replaced by a real file, in `frame/design.md` *Scope*, *Out*, the first bullet. It ruled out reading git's mode for that case because no deletion passes there. Here a deletion passes, so the frame's reason for not reading the mode does not apply.

The fix keeps the chosen rule for the real file and adds a second read for each link path that was a regular file at the base. The memo's base rows are compared at the link's own path, and the rows the link reads now are its target's. Name not in tree: `mode_at`, and the shared comparison `compare`. The comparison body is the one at `unverified_check.py:1618-1652`, moved into `compare` so both reads use it. Precondition: each `path` in `files` comes from `overviews`, under `real(arg)`, and `os.walk` does not follow linked directories. `os.path.islink` is therefore true only where the `gaps.md` itself is a link. `at` is `/`-joined, as `repo_relative` returns it.

```python
def mode_at(root, ref, rel):  # NAME NOT IN TREE
    """The mode REF records for REL, `120000` for a link, or None where REF
    holds no such path."""
    r = subprocess.run(
        ["git", "-C", root, "ls-tree", ref, "--", rel],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    head = r.stdout.split(" ", 1)[0] if r.returncode == 0 else ""
    return head or None


# In main, inside `if args.baseline:` and after the per-file loop:
        # The loop above reads the base at each real path. A path that is a
        # link now and was a file at the base held its own rows there, and
        # nothing else reads them.
        for path in files:
            if not os.path.islink(path):
                continue
            at = repo_relative(path, root)
            if at is None or mode_at(root, base, at) in (None, "120000"):
                continue
            open_rows, closed_rows, errors = check_file(path)
            if not errors:
                compare(display_path(path, cwd), at, open_rows, closed_rows)  # NAME NOT IN TREE
```

The case belongs in `Test_main` of `tests/skills/test_unverified_check.py`, beside `test_refuses_a_row_deleted_through_a_tracked_link_naming_the_real_file` (line 2204). The base holds two real memos, the larger one is replaced by a link to the smaller one, and the case runs in both link orders. It expects exit 1, with the deletion line naming the link's path. It is seen red against b2e4ca18 in both orders, and against a92c358b in the order where the link sorts after its target.

## Confirmations

```seal
confirms: none
```
What matched: Scope items 1 and 4. `unique_by_target` returns the sorted real paths (`skills/verify/scripts/unverified_check.py:1116`), and each new case pins it. The crafter claimed the cases were seen red against the old rule. This round put a92c358b's first-path body of `unique_by_target` into the scratch clone at b2e4ca18 and ran the link cases. 8 failed and 4 passed. The failures were both parameters of `test_accepts_the_real_files_own_path_wherever_the_link_sorts`, three parameters of `test_refuses_a_row_deleted_through_a_tracked_link_naming_the_real_file`, the before order of `test_accepts_a_tracked_link_counted_once_and_not_deleted`, and both parameters of `test_accepts_a_link_to_a_file_beyond_the_repository_as_not_compared`. The parameter that passed against the old rule is the after order scanned whole, which the phase record says passed at a92c358b. Executed.

```seal
confirms: none
```
What matched: the departure the phase record names. `unverified_check.py:1604-1615` names a kept path as outside the repository where `repo_relative` returns None or its first component is `..`. Without the None arm, `show(root, base, None)` would ask git for `<base>:None`, get None back, and leave the file out of the report in silence. The `another volume` parameter (`tests/skills/test_unverified_check.py:2237-2245`) makes `os.path.relpath` raise only for the target's directory. That reaches the None arm, and it also reaches `display_path`'s absolute-path fallback for the report line. The departure applies the frame's own Scope item 2 reason to a path the frame's *Data & interfaces* did not foresee, and it is grounded in `skills/core/SKILL.md` *The rule a mechanism is kept against*, as the record says. Read.

```seal
confirms: none
```
What matched: the `show()` box of the issue. `show` (`unverified_check.py:1438-1445`) and `check_file` (`unverified_check.py:838-849`) both decode with `encoding="utf-8", errors="replace"`, so the two sides decode by one rule, as `frame/design.md` *Grounding* says. The new `Test_show` case (`tests/skills/test_unverified_check.py:1754`) covers what its two siblings do not: one is a readable path, the other a missing one. It passed at the base, as the design says. The phase record says it was seen red with `show()` reverted to `text=True`. This round did not run that revert. Read.

```seal
confirms: none
```
What matched: the presence arm is unchanged and still builds `here` from the unresolved paths (`unverified_check.py:1655`), as *Data & interfaces* requires. The `linked` fixture's link stands under its own path in `ls-tree`. With the fixture now built in both orders, `test_accepts_a_tracked_link_counted_once_and_not_deleted` asserts that neither path is named `not compared` or `left the record`. The module ran green through the runner: `bin/test tests/skills/test_unverified_check.py -q`, 354 passed, exit 0, with no skips on macOS. Executed.

```seal
confirms: none
```
What matched: no other place states the old rule. `git grep` for `first in sort order` and `first path in sort` finds only the work item's own frame and the two new test docstrings, which state the old rule as history (`tests/skills/test_unverified_check.py:1618`, `tests/skills/test_unverified_check.py:2207`). This is a search on wordings, so it is a sample, as the phase record also says. `seal layout --pairs` exited 0. Executed.

```seal
confirms: none
```
What matched: `## Rule changes` is `nothing`, and that holds. The rule that a removed row or a removed `gaps.md` is a deletion is stated in `docs/the-record-layout.md` *The fold, and what tells it from a deletion* and in `skills/verify/SKILL.md` *And something has to read the row afterwards*, and this work changes neither. The design's *Grounding* cites *The unverified record, and the baseline it is read against* for that rule. That section states the merge-base and nothing-declared rules, not the row rule. The citation names the wrong section, and nothing in the build rests on it. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the link cases run or skip on the Windows legs (`frame/questions.md` Q1) | `tests/skills/test_unverified_check.py` | a measurement: the Windows legs of `.github/workflows/test.yml` on this pull request; naming a skip there is #1221's |
| What Windows `os.path.realpath` answers for a tracked link whose target is on another drive, run end to end; the `another volume` case induces the raise rather than running it | `skills/verify/scripts/unverified_check.py:1604` | a maintainer with a Windows machine holding two drives |
| The crafter's three `seal mutate` runs, not re-run this round | `trail/phases/phase-1.md` | the sealer, at its sample of the crafter's claims |
| The full suite, the repository-wide `ruff check` and `ruff format --check`; the crafter's `unverified` label for them is honest, since `gaps.md` names the orchestrator as their answerer | `gaps.md` | the orchestrator, through `seal gate`, once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `sh <scratch>/test_tmp_real_to_link.sh` | Two repositories, each with a three-row memo replaced by a tracked link to a one-row memo, at `specs/a` and at `specs/z` beside `specs/b`. At b2e4ca18 both runs exited 0. At a92c358b the `specs/a` run exited 1 with `3 rows at HEAD~1, 1 here` and the `specs/z` run exited 0. |
| `python -m pytest -q tests/skills/test_unverified_check.py -k "unique_by_target or tracked_link or beyond_the_repository"`, in the scratch clone at b2e4ca18 with a92c358b's body of `unique_by_target` | 8 failed, 4 passed |
| `bin/test tests/skills/test_unverified_check.py -q`, in the worktree at b2e4ca18 | 354 passed, exit 0 |
| `bin/seal layout --pairs`, in the worktree | exit 0 |
