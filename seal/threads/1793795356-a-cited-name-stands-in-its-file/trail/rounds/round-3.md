# Review round 3: 1793795356-a-cited-name-stands-in-its-file

```seal
target: fb21d56a9, fixes d010d6d4e..fb21d56a9
```

This is a verifying round. Its target is `git diff d010d6d4e..fb21d56a9`: the fix commit `f9a92629c`, which adds two entries to S9's tables, rewrites one sentence of the changelog fragment and closes one `gaps.md` row, and round 2's close blocks at `fb21d56a9`. It was read in a `git clone --no-local` of the branch worktree, checked out at `fb21d56a9`, under the round's scratch directory. `seal/parity.md` is not declared, so no `original:` line is owed. `seal/config.md` has no `Record language` row, so the record is in English. The round stays inside the fix diff. Its new units are the two S9 entries at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:862-867` and `:940-944`, the changelog sentence at `seal/threads/1793795356-a-cited-name-stands-in-its-file/changelog.md:3`, and the closed row at `seal/threads/1793795356-a-cited-name-stands-in-its-file/gaps.md:10`. No unit in the diff came from a build phase.

Carried from earlier rounds as coordinates, not re-established: `holds` and `excuser` at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:184-207`, which round 2 read and the fix diff does not touch; the S9 fixture `POLICY_CITING`, `NAME_OLD`, `NAME_NEW` and `pending` at lines 785-822, which the new entries reuse; `NAME_TOKEN` and its look-behind at line 257, which round 1 compared on six strings; round 1's list of every file naming the module, at `trail/rounds/round-1.md:94`, which the closed `gaps.md` row cites; the history of each of the five names, from `frame/design.md:15` (the framer's `git log` runs); and the `closed` form `skills/verify/scripts/unverified_check.py` reads, which round 2 read at line 136. This round re-derived each verdict below against the code at `fb21d56a9`.

The axes walked were Test quality (whether each new entry holds a direction of `holds` that no other entry of its table holds, and fails against the code it was written against), Exclusions and boundaries (a cited token under a longer path, in a `from` and in a `to`), and one axis of this change's own: whether the release note's new sentence and the closed memo row say what the tree and the earlier records show.

## Findings

None. Both closes of round 2 hold, and the new units hold, as *Confirmations* states.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the path side of `holds` is now pinned, at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:862-867` in `EXCUSING` and `:940-944` in `REFUSING`. The fix pass claimed the two entries were added as round 2 gave them. They are its paste-ready snippet byte for byte, under the names it proposed (read: the diff). The fix pass claimed that an end-only bound fails exactly the two new entries and that the substring test fails all four name entries that bound a name. This round replaced line 193 through the `Edit` tool and ran S9's two tests each time (executed). With `re.search(re.escape(cited) + r"(?!\w)", flat)`, exactly "a change that moves the name's file under a longer path" and "a from that holds the name under a longer path" failed, 2 failed and 18 passed. With `cited in flat`, those two and the two round 1 added failed, 4 failed and 16 passed. So each new entry holds a direction no other entry of its table holds, which answers the group reading the proofer definition asks of a new test: an end-only `holds` keeps every older entry green. The line was restored and `git diff --quiet` exited 0. The module passed whole, 55 cases, with no warning (executed). That matches the fix pass's count.

```seal
confirms: round-2#2
```
What holds: the sentence at `seal/threads/1793795356-a-cited-name-stands-in-its-file/changelog.md:3` now reads "Five places in the tree cited a name their cited file does not bind: three files had lost the name, one cited file had been deleted, and one planted key named a file that never existed." The fix pass claimed `broad_gate.py`, `test_unverified_rows_close.py` and `mode-gate.py` are tracked and `round_record.py` and `tests/test_tmp_seventh.py` are not. `git ls-files --error-unmatch` agrees on all five (executed). None of the three tracked files binds its cited name: an `ast` walk over each that took every `def`, `class`, stored name and import at any depth found none of `PANEL_VALUE_WIDTH`, `unreadable` and `test_the_fence_rule_agrees_with_the_config_reader` (executed). That walk is looser than the module's reader, so the reader resolves none of them either. `skills/code-review/scripts/round_record.py` was deleted at `8350c5788` (executed: `git log --diff-filter=D`). `tests/test_tmp_seventh.py` appears in no commit of any ref in the clone (executed: `git log --all`), so "never existed" holds for the history the clone holds. The sentence matches the "Why it does not resolve" column at `frame/design.md:91-95`. A search of the work item and the module for the old wordings found the fragment as the one present-tense statement of the five's reasons (executed: `git grep -n -i -E "tracked file binds|no longer binds|does not bind|never existed"`). `trail/rounds/round-1.md:79` and `:100` state the fragment at the commits those records name, so they stand.

What matched: the closed row at `seal/threads/1793795356-a-cited-name-stands-in-its-file/gaps.md:10`. It opens with `closed`. `seal unverified` read the memo as 2 open and 2 closed with nothing unreadable (executed). Its answer cell cites round 1's module docstring entry, and that entry at `trail/rounds/round-1.md:94` says what the cell says: every file naming the module was listed by `git grep` and read, and a sentence describing the reach without the path falls outside that list (read). The cell calls that remainder a class over wordings that no method lists whole. That is a sample left a sample over an open class, as contract rule 12 allows when the account names it, and the cell names it. Round 2 left this row open as a remark and named the fix pass as one who may close it.

What matched: the fix pass left a `to` that rewrites a citation as `<commit>:<path>#<name>` unpinned. `frame/design.md:61` puts every `<commit>:<path>` in shipped text under *Out* and says "This work adds none". So no case is owed here, and the fix diff adds no such token to shipped text (read: the diff).

What matched: the record readers of the files the fix diff changes still pass. The citation module, `tests/text/test_a_cited_commit_outlives_the_squash.py`, `tests/behaviour/test_unverified_rows_close.py` and `tests/behaviour/test_the_set_a_work_item_always_has.py` passed, 109 cases (executed). The fix pass's account of the plan row's six modules "with two record readers" was not re-run whole. The citation module is the one of those six that the fix diff changes.

Nothing is left open by this round. What comes due is the orchestrator's broad run, and the sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. `gaps.md:7` labels them for the orchestrator, and the label is honest: the fix pass names scoped runs and not the broad gate | `gaps.md:7` | the orchestrator, at the broad gate |
| The `path#name` tokens #1254's and #1255's branches write, which this case reads once they merge beside this one | `gaps.md:8` | the orchestrator, at the broad gate on the release branch after the merges |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -rw -p no:xdist` at `fb21d56a9` | 55 passed, no warning |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist -k "pending_correction or no_pending_correction"`, with line 193 replaced through the `Edit` tool by `return re.search(re.escape(cited) + r"(?!\w)", flat) is not None` | 2 failed, 18 passed: the two entries `f9a92629c` added, and no other |
| The same run with line 193 replaced by `return cited in flat` | 4 failed, 16 passed: the two entries round 1's fix added and the two `f9a92629c` added. Line 193 was restored through the `Edit` tool, and `git diff --quiet` in the clone exited 0 after |
| `python3 -I -c` with an `ast` walk over `skills/verify/scripts/broad_gate.py`, `hooks/mode-gate.py` and `tests/behaviour/test_unverified_rows_close.py`, collecting every `def`, `class`, stored name and import alias at any depth | each printed `False` for its cited name |
| `bin/seal unverified seal/threads/1793795356-a-cited-name-stands-in-its-file --baseline base/release`, where `base/release` is `release/v0.32.0` fetched into the clone | exit 0; 2 open, 2 closed, 0 unreadable |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_a_cited_commit_outlives_the_squash.py tests/behaviour/test_unverified_rows_close.py tests/behaviour/test_the_set_a_work_item_always_has.py -q -p no:xdist` | 109 passed |
