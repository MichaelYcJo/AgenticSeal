# Phase 1: 1794465690-a-passing-release-note-reads-like-a-failure

## What this phase found

**The frame holds, with one coordinate that states no old shape.** Each coordinate `frame/design.md` *Grounding* and `frame/plan.md` *Technical context* give was opened at `c368121de`, and each matched: `table` at `publish_release_note.py:643`, `header` at `:652`, `sealed_header` at `:712`, and the count and replace at `release_seal.py:557-576`. `frame/design.md` *Scope* item 5 and its *Removes* row also name `publish_release_note.py:86-92` as a docstring that states the old shape. Those lines state only that `header` and `sealed_header` build the two forms, at `3a75cc23d` and at HEAD alike. They hold under the new shape, so this phase left them as they are. Judged against `frame/design.md` *Scope* item 5, whose aim is to rewrite what states a table, a cell or the two reds.

**One builder takes the float and its clear from its caller.** `paragraph(lines, before="", after="")` writes `<p>`, `before`, the lines parted by `<br>`, `after` and `</p>` on one line. `header` passes neither argument. `sealed_header` passes the floated `<img … align="left">` as `before` and `<br clear="left">` as `after`, so the float and the break that clears it are written by one function. Judged against `frame/design.md` *Scope* item 2 (one builder replaces `table`) and *Data & interfaces*, whose two shapes the builder writes byte for byte. The docstring of `paragraph` states why the header is one line and why it is no table. The docstring of `header` states that the `<p>` and `</p>` bound the text the seal counts. Those reasons used to live in `table`'s docstring.

**S6 is two parameters of the existing refusal case, not a new function.** The two cases are `the note's header holds one more count line` and `the note's header holds one more digit`, in `tests/github/test_release_seal.py#test_refuses_on_any_failure_and_leaves_the_note_as_published`, and each has a row in `REASONS`. That case already holds every refusal of the seal, the two existing header refusals among them, and it asserts that nothing is uploaded and nothing is edited. In the first case the seal's pull request list loses its outside author, so the seal computes a header without the contributors line, while the note keeps that line. In the second case the note reads `12 pull requests merged` where the seal counts 2. `seal layout --pairs` over the two test files named no pairs before any case was written. Judged against the crafter's rule *A new test starts from its group*.

**Two test names changed, because no cell is left.** The constant `RESULTS_CELL` is now `BADGE_LINES` in both test files. The case `test_the_sealed_header_given_no_image_is_its_results_cell_alone` is now `test_the_sealed_header_given_no_image_is_its_badges_alone`, which is the rename `frame/design.md` S3 asks for. `git grep` for both old names finds them only in this work item's `frame/design.md`: the *Verifiable how* cells of S3, S4 and S5, and the *Removes* row, which states the tree at `3a75cc23d`. Judged against contract rule 19.

**Two assertions grew.** `test_the_note_opens_with_a_header_of_its_counts` now also asserts that the note holds no `<table>`, which is S1's last sentence. The escaped case in `test_the_header_is_built_by_one_function_and_its_sealed_twin_by_another` used to check for a substring and now compares the whole string. The header is one line, so the whole string also pins the float and the clear on escaped input.

**Seen red before the code.** With the new cases in place and the code still writing the table, the command below failed 11 cases and passed 23. The failures were the S1 case, `test_the_theme_follows_the_notes_header` (which reads `HEADER`), the S2 case, the S3 case, the S5 case with the image, and the six parameters of the S5 case without it.

`bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py -q -p no:xdist -k "header or opens_with or replaces_its_header or other_than_yes or refuses_on_any_failure or hand_edited or second_run"`

The two S6 parameters passed against the table, because the table's own tags bounded the header. Their red came from the mutation run below, as `frame/plan.md` row 1 asks.

**Mutation, after commit `aec18b104`.** Every run's verdict was `red`, and no mutant survived.

| Break | Cases run | Verdict |
|---|---|---|
| `header` returns its lines joined by `<br>` with no `<p>` and `</p>` | the two S6 parameters (`-k holds`) | red. Both failed at `assert len(warnings) == 1`: the seal no longer refused, which is the guard S6 names |
| the seal's `<img>` loses `align="left"` | S1, S2, S3, S5 (`-k 'opens_with or sealed_twin or given_no_image or replaces_its_header or other_than_yes'`) | red, at the whole-string assertion of the S2 case (run alone to read the line) |
| `sealed_header` passes no `<br clear="left">` | the same | red |
| `paragraph` writes no `<p>` and `</p>` | the same | red |
| `paragraph` parts the lines with a newline in place of `<br>` | the same | red |
| `sealed_header` with no image passes `<br clear="left">` | the same | red |

The local `table` in `release_seal.py#seal_release` is now `header` with no other change. It adds no behaviour, so it needed no mutation run. Its proof is the existing S5 and S7 cases passing at the new name, and `git grep -n 'table' .github/scripts/release_seal.py` lists one line, `:302`, which is about a round record's shape, not the header.

**Phase boundary.** The set is the two test files, `tests/text` and `tests/behaviour`. No other test file reads either script: `tests/skills/test_settle.py` names `publish_release_note.py` only in a docstring. The set ran as one command: `bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py tests/text tests/behaviour -q`. Before this record existed, it failed one case, `tests/behaviour/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`, which asks for the `gaps.md` this phase writes, and passed 1,208. Over the tree that holds this record and `gaps.md`, the same command exited 0, with 1,209 passed and 8 skipped.

**A docstring commit after the run.** Reading the range against HEAD found two docstring faults. `header`'s docstring named the longer header line in words that read two ways, and `results`' docstring broke a line in the middle of a paragraph. Commit `d5d029827` corrects both and changes no code. The two test files ran again at that commit, with 113 passed. The mutation runs and the boundary run above measured `aec18b104`, whose code is the same.

**For phase 2.** The badges still carry the two reds, so both test files' `badge` helpers still pin `d42420` on `8e0c12`. The docstring of `badge` and the comment above `BADGE_LABEL_COLOUR` are phase 2's to rewrite. No other line of `release_seal.py` or `publish_release_note.py` states the header as a table or a cell. The other uses of `table` in `publish_release_note.py` are about the `### Process changes` table.
