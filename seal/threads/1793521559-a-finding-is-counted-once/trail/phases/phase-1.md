# Phase 1: 1793521559-a-finding-is-counted-once

## What this phase found

**The frame held where it was opened.** At d9c9b537, `chain_check.Finding` is defined at `skills/code-review/scripts/chain_check.py:152` and built at line 767 alone (executed: `git grep -n 'Finding(\|Finding\._\|\.Finding\b' -- '*.py'`, one hit). `#finding_of` stands at lines 735-780, and its `paths += location_paths(closed[...])` joins the close block's paths to the finding block's (read). `#located_in_records` stands at line 898 and `#under` at line 892 (read). `skills/settle/scripts/settle.py#released` stands at lines 191-214 and returns None for a ref that does not resolve (read). `.github/scripts/tracker_labels.py:159` is the `console.to_utf8()` call the design cites (read). `.github/scripts/release_seal.py#readers` and `#chain_counts` read records as the design's Grounding says (read). No part of the frame was found wrong, so nothing here goes back to the framer.

**The decisions this phase made, each with its grounds:**

1. **`located` is the last field of `Finding`, and `paths` is built as a copy of it.** `#finding_of` now reads `located = location_paths(...)` and `paths = list(located)`, then extends `paths` with the close block's paths. Extending the list `located` names would have put the close block's paths into `located` too, which is the defect this work removes. Appended last, the field leaves every positional reading of the tuple where it was. Judged against: `frame/design.md` *Scope* item 1 and *Data & interfaces*, and `frame/plan.md` *Technical context*, the paragraph on `Finding`.
2. **The script spells `seal/threads` once, as `settle.SPECS`.** It reads a work item's directory at `<root>/seal/threads/<id>/` and asks `chain_check.under(path, "seal/threads")` of each `location:` path, and both read `settle.SPECS`, the spelling `#released` already reads `git ls-tree` with. So the rows and the records-alone count cannot name two different roots. Judged against: `frame/design.md` *Data & interfaces*, the records-alone bullet, and `skills/core/SKILL.md` *The rule a mechanism is kept against*, "A fact has one source".
3. **A blank line parts the table from the lines under it.** This is a departure in form from `frame/design.md` *Data & interfaces*, which says only that the lines stand under the table. GitHub's table extension continues a table on the next non-blank line, so a refusal pasted into #51's comment right under the last row would render as a row. The `table` helper of `tests/github/test_finding_counts.py` asserts the blank line wherever lines stand under the table. Judged against: `frame/design.md` S6, "The output is the comment's table".
4. **A `trail/rounds` that cannot be listed gets a line under the table, `<path>: the round records cannot be listed: it is not a directory`.** This is an addition to *Data & interfaces*, which gives the four `not read` cells for that case and no line. Every other `not read` cell is explained under the table, and a cell nobody explains leaves the settling session to guess which of the two causes it was. Judged against: `frame/design.md` *Data & interfaces*, the Stdout bullet, and `.github/scripts/release_seal.py#chain_counts`, which names the unlistable directory in its log.
5. **A record the reader refuses prints every refusal `record_findings` returned, one line each, as `<path>:<line>: <why>`.** The `<path>` is the record's path from the root with `/` between its parts. A record with no round block is refused at line 0 (`chain_check.NO_ROUND_BLOCK`), so its line reads `<path>:0: <why>`. Judged against: `frame/design.md` *Data & interfaces*, the Stdout bullet.
6. **Four cases go beyond S1 to S6, one for each behaviour *Data & interfaces* states and no scenario names.** They are a regression and a reopens counted once each over two rounds, a record that is not UTF-8, a `trail/rounds` that is a file, and readers that will not load. Each adds behaviour, so each was seen red as the next paragraph says. Judged against: `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test*.
7. **Two cases were renamed to the test layout's form after the first commit.** `seal layout --check tests/github/test_finding_counts.py` refused the class `Test_main` for holding no `test_accepts_` case and no `test_refuses_` case (executed, exit 1). The S6 case is now `test_accepts_a_tree_and_prints_the_comments_table_in_work_item_order`, and the S5 ref case is `test_refuses_a_ref_that_does_not_resolve_and_exits_2`; the same command then exited 0. It still reports that `chained`, `item_counts`, `load` and `readers` have no class of their own, which it does not refuse. Their cases run through `main`, as `gaps.md` *Not done* says.
8. **`load` holds no `spec is None` arm.** The first commit refused a spec of None, and no case reached that arm. `importlib.util.spec_from_file_location` returns a spec for every path ending in `.py`, present or not, and a missing file raises at `exec_module`, which `main` catches as a reader that will not load. So 1da90703 dropped the arm, and `load` now matches `.github/scripts/release_seal.py#_module`. Judged against: `skills/core/SKILL.md` *The rule a mechanism is kept against*, and the docstring of `skills/settle/scripts/settle.py#load`, which states the same property of `spec_from_file_location`.

**`seal layout --pairs` names no pair** for `tests/github/test_finding_counts.py` or `tests/skills/test_chain_check.py` (executed, exit 0). The S7 case joins `Test_record_findings` in `tests/skills/test_chain_check.py`, the group of the reader it covers. No case in that group read `located` before it.

**Seen red.** Every case was written before the code. Against d9c9b537, `bin/test tests/github/test_finding_counts.py -p no:xdist -q` failed all 13 cases, because the script did not exist (executed). The S7 case failed with `AttributeError: 'Finding' object has no attribute 'located'` (executed). After the code, the module passed 13 of 13 and the S7 case passed (executed).

**Mutation.** Each run was `seal mutate` over the committed file, with the named case or cases run as `bin/test <module> -p no:xdist -q -x -k <case>`. Every run reported `red`, and `git status --short` was empty after each (executed):

| Unit | Mutation | Case that went red |
|---|---|---|
| `chain_check.py#finding_of` | `located` built from the union: `paths` passed in its place | `test_located_holds_the_finding_blocks_paths_alone` (S7) |
| records alone | each finding counts `len(f.paths)`, one per path its two blocks name | `test_a_close_blocks_location_does_not_count_a_finding_twice` (S1) |
| records alone | `located` read as `paths` | `test_where_the_defect_shows_decides_records_alone`, the first parameter, which reads 0 (S2) |
| findings and regression | the last record's text counted for `\n### ` and for `\nregression: `, as a grep counts | `test_prose_and_a_fix_fence_are_not_fields` (S3), each mutant red |
| regression | `reopens` not read | `test_counts_a_regression_and_a_reopens_once_each` |
| a refused record | `if errors:` made `if False:` | `test_a_record_the_reader_refuses_is_not_counted_short` (S4) |
| an unreadable record | its line not appended | `test_a_record_that_cannot_be_opened_is_named_with_why` |
| an unlistable `trail/rounds` | the `rounds_unreadable` arm skipped | `test_rounds_that_cannot_be_listed_read_not_read_in_every_cell` |
| the rows | `chained` reads any parsed routing as the chain; `--released-at` replaced by `HEAD` | `test_the_rows_are_the_released_items_routed_through_the_chain` (S5), each mutant red |
| the ref | the `released is None` arm skipped | `test_refuses_a_ref_that_does_not_resolve_and_exits_2` (S5), rerun after the rename |
| the readers | exit 0 where a reader will not load | `test_readers_that_will_not_load_are_said_and_exit_2` |
| the order and the header | rows sorted in reverse; the header's first cell spelt `item` | `test_accepts_a_tree_and_prints_the_comments_table_in_work_item_order` (S6), each mutant red, rerun after the rename |
| the blank line | the lines under the table printed with no blank line before them | `test_a_record_the_reader_refuses_is_not_counted_short` |

**S8, the run over this tree.** `python3 .github/scripts/finding_counts.py --released-at 813665f0`, from the worktree at c832a026 and again at 1da90703, exited 0 both times and printed the following, byte for byte the same (executed, compared with `cmp`). The eight rows are the Grounding's parser row, and `1793521559-a-finding-is-counted-once` is no row.

```
| work item | findings | regression or reopens | records alone | rounds |
|---|---|---|---|---|
| 1793457435-replay-targets-reads-both-layouts | 6 | 3 | 0 | 5 |
| 1793457436-row-deletion-check-and-a-symlink | 2 | 0 | 1 | 3 |
| 1793457437-readers-state-the-shapes-they-pass | 3 | 0 | 1 | 2 |
| 1793490088-each-kind-of-restatement-is-measured | 17 | 5 | 17 | 4 |
| 1793504229-a-linked-memo-named-as-the-argument | 9 | 4 | 3 | 7 |
| 1793504230-replay-keeps-rounds-on-a-deleted-base | 1 | 0 | 0 | 2 |
| 1793513786-an-unanswered-case-name-is-named-once | 0 | 0 | 0 | 1 |
| 1793516191-a-wording-pin-module-leaves-by-rule-changes | 8 | 2 | 8 | 2 |
```

**The policy root is untouched.** `git diff --stat 813665f0...HEAD -- docs/` printed nothing at c832a026 and at 1da90703 (executed). Scope item 4 is the design's `## Rule changes`, and the settle applies it.

**Other places stating the count.** `git grep -n "grep -h\|records alone\|regression or reopens" -- ':!seal/threads'` finds the grep recipe at `docs/release-checklist.md:68` alone, which the design's second rule change replaces at the settle (executed). The other hits for "records alone" state the pull-request check's rule, which reads the work item's own records and the union of both blocks' paths, and `frame/design.md` *Out*, second bullet, keeps that rule. This is a search for the wording, so it is a sample and not a whole list.
