# Implementation Plan: 1795405728-lib-routing-splits-a-row-on-an-escaped-pipe

## Technical context

The tree as read at `351a28c71`.

**The row splitters.** `lib/tables.py` holds the cell grammar: `CELL` (`:58`), `unescaped` (`:64-78`), `TABLE_ROW` and `CELL_PIPE` (`:297-298`), `EVEN_ESCAPED_PIPE` (`:303`) and `table_cells` (`:306-319`). `tests/lib/test_tables.py`'s `Test_gfm_table` holds the walker built on them to cmark-gfm through `tests/gfm_table_oracle.py`. `TABLE_ROW` requires the closing pipe, so a row without it is None. `lib/lines.py#split_row` (`:83-93`) splits at every unescaped pipe and accepts an open end. `lib/routing.py#table_rows` (`:122-151`) splits at every pipe. Scope item 1 widens `TABLE_ROW`'s grammar to the open end and leaves `CELL`, `unescaped` and `EVEN_ESCAPED_PIPE` as they are. Which callers read the result is `frame/design.md` G7.

**The line splits.** `lib/blocks.py#gfm_lines` (`:383-389`) is the GFM split, and `lib/lines.py#readable`, `lib/fields.py#read` and `skills/settle/scripts/rules.py#shown_lines` already read through it. `lib/tables.py#gfm_table` (`:492-494`), `lib/routing.py#table_rows` (`:142-143`) and `skills/verify/scripts/pact_check.py#near_headers` and `#first_table` (`:338-339`, `:358-359`) split with `str.splitlines` and pass the text beside the lines, so that `lib/blocks.py#walk_text` (`:400-454`) can answer each piece by the GFM line it starts in. Once every caller passes `gfm_lines`, `walk_text`'s answer equals `walk`'s, line for line.

**Imports.** `lib/routing.py` imports `optin` and `blocks` by plain name after putting its own directory on `sys.path` (`:38-55`), and `lib/sibling.py#load` registers a module under its stem, so a plain `import tables` there and `sibling.load("lib/tables.py")` in a script are one module. `lib/gaps.py` imports from `lines` the same way (`:36-45`).

**The separator.** `lib/routing.py#table_rows` skips a line whose first cell is dashes and colons alone. Scope item 2 asks `tables.DELIMITER_ROW` instead, the delimiter rule measured against cmark-gfm. `lib/lines.py#is_separator` would answer the same on every routing row, and asking it would make `routing` import a third module for one test.

**Failure scenario, six months on.** A caller added later treats `table_cells` returning a tuple as proof that the line ends with a pipe, and reads prose after a last pipe as a value. `gfm_table` refuses such a row by its width, and `routing` reads the first two cells, as cmark-gfm does with a two-cell header (`frame/design.md` G8). A reader that asks neither the width nor the first two cells meets the open end unguarded. The docstring of `table_cells` is where that reader learns it, so Scope item 1 states the open end there.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep `table_cells` closed at the end, and move every caller onto it unchanged | A `Planning` or `Automation` row written without its closing pipe stops reading, and `parse` reads either as unanswered without a word, so `chain_check.py` stops holding a `framer` answer against the frame's mark. `lib/gaps.py` refuses a row GitHub shows. Both readers read the row today, and cmark-gfm renders it (`frame/design.md` G8, G11) | Rejected |
| Widen `table_cells` to the open end cmark-gfm reads, and move every caller onto it (Scope item 1) | The scenario under *Technical context* | Chosen |
| Fix the routing reader alone, by calling `lib/lines.py#split_row` | Two splitters stay. Where a pipe follows an even run of backslashes, `split_row` keeps a backslash in the cell that cmark-gfm drops, and it reads a row indented four spaces, which cmark-gfm renders as code (`frame/design.md` G8). The issue's first *Done when* line stays unmet | Rejected |
| Keep `split_row` in `lib/lines.py` as the one splitter, and have `lib/tables.py` import it (replacing the structure that holds the grammar in `tables.py`) | The cell grammar and the walker held to cmark-gfm stand in two files, and `Test_gfm_table` holds a splitter its module does not define. The premise that keeps the grammar in `tables.py`, checked: `CELL`, `unescaped` and `EVEN_ESCAPED_PIPE` are `tables.py`'s and only `tables.py` reads them (executed: `git grep -nw -E 'TABLE_ROW\|CELL_PIPE\|EVEN_ESCAPED_PIPE\|ESCAPED_PIPE' -- '*.py'` prints lines of `lib/tables.py` alone) | Rejected |
| Read `routing.md` through `lib/tables.py#gfm_table` with an `Axis` and `Answer` header (replacing the routing reader's own row loop) | `gfm_table` refuses a table with a line directly above its header and a row of another width, so a declaration with a sentence above its table or a third column turns into no declaration. `docs/checks/the-fold.md` *Whether a line is live is asked by what the line does* gives `lib/routing.py#shown` a base reading that hides nothing, and `gfm_table` reads through `hidden_lines`, whose base reading hides a fence nobody closed. The premise that keeps the routing loop, checked: that section names `shown` apart (G4) | Rejected |
| Keep the bridge (`walk_text` and the `text` parameters) and only fix the row split | Two line splits stay, which `lib/tables.py:229-235` calls a silent drift. A row holding a U+2028 keeps being refused by `gfm_table` and cut by `routing`, where cmark-gfm renders it whole (G8) | Rejected |
| Narrow `passages.py#FENCE` to three spaces and keep its walk | A fence rule outside both of `lib/lines.py`'s lists stays, and it still opens a fence on a backtick line whose info string holds a backtick, which `lib/blocks.py#fence_opener` refuses | Rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2 and 3 | `bin/test -q tests/lib/test_tables.py tests/lib/test_routing.py tests/lib/test_lines.py tests/lib/test_gaps.py tests/test_gfm_table_oracle.py tests/skills/test_chain_check.py tests/skills/test_fold_check.py tests/skills/test_pact_check.py tests/skills/test_rule_changes.py` passes. The cases of S1 and of S2's `gfm_table` row are each seen red against `351a28c71`. Searches 3, 6 and 7 of `frame/design.md` print nothing. S7's probe prints equal answers for every committed `routing.md` | |
| 2 | `frame/design.md` *Scope* items 4, 5 and 6 | `bin/test -q tests/lib/test_blocks.py tests/lib/test_tables.py tests/lib/test_routing.py tests/lib/test_lines.py tests/lib/test_fields.py tests/test_commonmark_oracle.py tests/test_censuses.py tests/skills/test_pact_check.py tests/skills/test_settle.py tests/skills/test_rules.py tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py tests/behaviour/test_one_heading_rule_holds_to_commonmark.py` passes. S3's case is seen red against `351a28c71`. Searches 1, 2 and 4 of `frame/design.md` print nothing | |
| 3 | `frame/design.md` *Scope* item 7 | `bin/test -q tests/skills/test_passages.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/skills/test_chain_check.py` passes. S5's case is seen red against `351a28c71`. Search 5 of `frame/design.md` prints nothing | |

The broad gate is the orchestrator's, after the rounds settle (contract rule 2); every phase hands over the suite as `unverified`.

## Overlap with the release

The spawn names #1573, #1582 and #1575. #1573's frame was read at its checkout's HEAD, `94e6a6772`, with its diff against the merge base `f2a664eb8`. #1582's diff was read at its checkout's HEAD, `b5961a287`; it has since landed on `origin/release/v0.38.6` as `c3f568c6a` (#1589). #1575 has no branch, and its issue was read. #1576 is not named by the spawn: its branch carries `routing.md` alone at `89fefd100`, and its issue was read (executed: `gh issue view 1576`), because it removes a function this work removes.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1573, every git and `gh` call runs through `lib/gitcmd.py` | `lib/routing.py`: #1573 replaces `import subprocess` with `import gitcmd` at `:33-41` and rewrites `current_branch`; this work adds the `tables` import after `:42-55` and rewrites `shown` and `table_rows` (`:99-151`). `tests/lib/test_routing.py`: both change `Test_module`'s copy without the walk (`:527-539`), which #1573 makes take `gitcmd.py` and this work makes take `tables.py`. `skills/code-review/scripts/chain_check.py`: #1573's last hunk above `table_rows` ends in `pull_request_body`, near `:640`; this work removes `table_rows` at `:657-664`. `skills/verify/scripts/pact_check.py`: #1573 changes `check` at `:637` and `:678`; this work changes `:330-365` | #1573 | Five of #1573's six phases carry a closing commit at `94e6a6772`, so it is likelier to be sealed first. The one textual conflict is the copy case's list of siblings, which this work's rounds resolve by listing both files after merging the base |
| #1582, the broad gate's verdict depends on the stamp's sprite | No file: #1582 changes `skills/verify/scripts/broad_gate.py`, `seal_stamp.py` and their cases. Both scripts load `lib/routing.py`, and this work makes that load import `lib/tables.py` too | #1582, landed | It is on the release branch at `c3f568c6a`. This work merges the base before its broad run, and a load of one more `lib/` module changes nothing #1582's cases read |
| #1575, the comment and fence delimiters each keep one definition | `lib/lines.py`: #1575 moves `OPENER` and `CLOSER` at `:77-78`; this work removes `split_row` at `:83-93` and rewrites the comment at `:47-53`. `lib/blocks.py`: #1575 moves `OPENER` and `CLOSER` at `:99-100`; this work rewrites `:66-71` and removes `walk_text` at `:400-454`. `skills/settle/scripts/fold_check.py`: #1575's issue cites `:85`, `:90`, `:138-143`, `:249` and `:297-311` at v0.38.5; this work changes `:37-39` and `index_rows` at `:152-163` | #1574 | #1575 has neither a branch nor a frame, and `routing.md` places it after this work. Its framer then reads `lib/lines.py` with `split_row` gone, and the adjacent lines at `:77-93` cost no merge at all |
| #1576, code, comments and tests stand on facts that no longer hold | `skills/code-review/scripts/chain_check.py#table_rows` and its case at `tests/skills/test_chain_check.py:4934`, which both remove. `lib/gaps.py`: #1576's issue cites the old mark at `:53-56` and `:171-180`; this work changes the imports at `:36-45`. `lib/routing.py`: #1576's issue cites the old `rounds` reading at `:381-393` and `:422`; this work changes `:42-151` | #1574 | This frame is committed and #1576's is not. Whichever lands second drops one row of its removals, and the hunks in `lib/gaps.py` and `lib/routing.py` are apart. #1576's framer reads the release branch, so it finds `table_rows` gone where this work lands first |

## Operational impact

No migration, environment variable or dependency. `lib/routing.py` loads `lib/tables.py` at import, so every script that loads `routing` loads one more `lib/` module, the `Stop` hook's `seal_stamp.py` among them. A row written without its closing pipe reads in every reader, where `lib/tables.py#gfm_table` refused it before. A text holding a character only Python ends a line at is read by GFM lines, so `gfm_table`'s two sentences about such a character are no longer printed. No committed record reads differently (`frame/design.md` G9). This pull request does not move the version.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
