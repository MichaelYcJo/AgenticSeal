# Phase 1: 1795405728-lib-routing-splits-a-row-on-an-escaped-pipe

## What this phase found

**The frame holds against the tree at `7892a5812`.** `CELL`,
`TABLE_ROW`, `CELL_PIPE`, `EVEN_ESCAPED_PIPE` and `table_cells` stood at
the coordinates `frame/plan.md` *Technical context* gives. The three
`split_row` callers, `chain_check.py#table_rows` with its one case, and
`lib/routing.py#table_rows` with its split and separator test stood where
`frame/design.md` G7 and `## Removes` put them (read). Searches 3, 6 and 7
printed the lines the design lists before the build (executed).

**`CELL` takes one more alternative, a backslash that ends the line.** This
departs from `frame/plan.md` *Technical context*, which leaves `CELL` as it
is. cmark-gfm 2025.10.22 renders `| Branch | fix/a \` under a two-cell
header as the cell `fix/a \`. `lib/lines.py#split_row` read the same cell
(executed: `test_tmp_cmark.py` in this phase's scratch directory,
`uv run --no-project --with cmarkgfm==2025.10.22`). Without the
alternative, `table_cells` refuses that row, so `lib/gaps.py` and
`fold_check.py#index_rows` would stop reading a row they read before. That
runs against *Scope* item 1's rule that the text after the last unescaped
pipe is one more cell. `Test_table_cells`'s `a backslash last` case pins
it, held to cmark-gfm (judged against `frame/design.md` *Scope* item 1 and
`skills/core/SKILL.md` *Judgment is spent where meaning is the question*).

**`TABLE_ROW` now matches only a row's start, at most three spaces and a
pipe.** With the open end, `(?:CELL|\|)*` matches every rest of a line, so
the whole-line pattern decided nothing beyond the start. `table_cells`
runs `CELL_PIPE` from the end of that match (read, judged against
`frame/plan.md` *Technical context*, "widens `TABLE_ROW`'s grammar to the
open end").

**One case outside *Scope* item 6's list is re-pinned.** It is
`tests/lib/test_tables.py`'s case on a backslash against a pipe, renamed
`test_a_backslash_against_a_pipe_is_an_escaped_pipe`. It asserted that
`| Broad gate | C:\Users\x\tools\|` is no row. Under *Scope* item 1 the
line is a row whose last cell is `C:\Users\x\tools|`, and cmark-gfm
renders that cell (executed, asserted in the case through
`tests/gfm_table_oracle.py`). The same shape against an inner pipe still
reads as no two-cell row. The docstring pointed to #415's frame section
*What this repair cannot see*, and that pointer went with the old reading
(judged against contract rule 14 and `frame/design.md` S4's rule that a
new reading equals cmark-gfm's or is a refusal).

**One moved case changed its text.** `split_row`'s escaped-pipe case wrote
its cell as a code span. cmark-gfm renders a code span's text without the
backticks, so a cell holding one cannot be compared with the renderer.
In `Test_table_cells` the cell is plain text with the same escaped pipe,
`whether a \| b parses`. All six accepted shapes are now held to
cmark-gfm as well as to their cells (judged against
`frame/design.md` *Scope* item 3).

**The routing reader changes on three shapes no committed declaration
holds.** First, a row indented four spaces or a tab is code now, where
`line.strip()` read it. Second, a row whose first cell is empty is read as
the label `''`. The old separator test `set(cells[0]) <= set(":- ")`
skipped such a row, and `tables.DELIMITER_ROW` skips only a delimiter row.
Third, the three shapes S1 and S2 name read as cmark-gfm renders them. No
label `parse` reads is empty, so `''` answers nothing. The S7 probe below
compares `parse` and `table_rows` over every committed declaration, and no
answer moved. `lib/gaps.py` and `fold_check.py#index_rows` meet the first
change too, and G9 found no committed record or index row indented four
spaces (read, judged against `frame/design.md` G9).

**S7's probe.** `git archive 351a28c71 lib` was unpacked into this phase's
scratch directory. `test_tmp_s7_dump.py` ran once under each `lib/`, with
`python3 -I`, over the 40 files `git ls-files 'seal/threads/*/routing.md'`
lists. Each run dumped `routing.parse(text)` and `routing.table_rows(text)`
per file, and `test_tmp_s7_compare.py` printed `40 files; 0 differ`
(executed).

**Seen red against `7892a5812`, with the code as the frame found it**
(executed, one command,
`bin/test -q -p no:xdist tests/lib/test_tables.py tests/lib/test_routing.py -k "table_cells or escaped_pipe or closing_pipe or cmark_gfm or copied_without"`).
Nine cases failed:

- S1: `Test_parse::test_reads_an_escaped_pipe_and_an_open_row_as_cmark_gfm_does`,
  whose failing line read `('fix/a\\', 'framer') == ('fix/a|b', 'framer')`.
  `Test_table_rows::test_reads_each_row_as_cmark_gfm_renders_it`, for the
  shapes `an escaped pipe` and `an escaped last pipe`.
- S2's `gfm_table` half:
  `test_a_row_without_its_closing_pipe_is_read_and_the_rows_below_arrive`,
  whose failing line read `[] != [('Mode', 'shared'), ('Broad gate', 'x')]`.
- The re-pinned `test_a_backslash_against_a_pipe_is_an_escaped_pipe`.
- `Test_table_cells` for `open at the end`, `an escaped last pipe` and
  `a backslash last`.
- `Test_module::test_a_reader_copied_without_the_walk_names_it[without the row splitter]`,
  where the copy imported without error.

Three cases passed at base and pin a reading the old code already gave:
the routing shapes `no closing pipe` and `a third cell`, and
`Test_table_cells`' refusals. `seal mutate` below shows each red with its
guard removed.

**`seal mutate`, run after `3bbd2a46a`, ten mutants, ten red** (executed):

| File | Mutant | Cases run | Red |
|---|---|---|---|
| `lib/tables.py` | the open end's last cell dropped | `test_tables.py -k "table_cells or closing_pipe or escaped_pipe"` | `Test_table_cells` for `open at the end`, `an escaped last pipe` and `a backslash last`; the two `gfm_table` cases above |
| `lib/tables.py` | a blank last piece kept as a cell | the same | red |
| `lib/tables.py` | `tuple(cells) or None` to `tuple(cells)` | the same | red |
| `lib/tables.py` | `CELL` without `\\\Z` | the same | red |
| `lib/tables.py` | `TABLE_ROW` taking any indentation | the same | `Test_table_cells` `four spaces in` alone |
| `lib/routing.py` | the `DELIMITER_ROW` skip removed | `test_routing.py -k table_rows` | the four shapes of `test_reads_each_row_as_cmark_gfm_renders_it` |
| `lib/routing.py` | `table_cells` replaced by the old split at every pipe | `test_routing.py -k "table_rows or escaped_pipe"` | the two escaped shapes and the S1 `parse` case |
| `lib/routing.py` | the `tables.py` sentence's purpose reworded | `test_routing.py -k copied_without` | `[without the row splitter]` |
| `lib/gaps.py` | the body rows split at every pipe | `test_gaps.py -k escaped` | `test_accepts_open_rows_and_the_word_that_closes_one[an escaped pipe]` |
| `skills/settle/scripts/fold_check.py` | `cells_of` returning None | `test_fold_check.py` | four `Test_main` cases |

The batch over `lib/tables.py` printed verdicts alone. Its first and fifth
mutants were run again one at a time to read the failing case names in the
table. The first was also run against
`test_routing.py -k "table_rows or open_row"`, and the routing shape
`no closing pipe` and the S1 `parse` case went red: the open end of
`table_cells` is what holds the routing half of S2. Every command carried
`-p no:xdist`.

**The phase boundary set, at `3bbd2a46a`** (executed, one command,
`xargs bin/test -q < boundary_all.txt` in this phase's scratch directory).
The set holds 90 test files. They are the plan row's nine; every test file
that loads `lib/lines.py`, `lib/routing.py`, `lib/tables.py`, `lib/gaps.py`,
`chain_check.py` or `fold_check.py`, or imports a test file that does; the
test files of the 15 shipped modules that load one of those four `lib/`
modules; and the 66 test files that declare no `TARGET`, which
`CONTRIBUTING.md` names the tree-wide files. The run gave 3819 passed, 10
skipped and 1 failed. The failure was
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
naming this work item. The run started before this phase wrote `gaps.md`.
With the memo in place, `bin/test -q tests/behaviour/test_chain_hooks_hardening.py`
gave 27 passed (executed).

**Rule 19's search, a sample.** `git grep` on `split_row`,
`chain_check.py#table_rows`, `closing pipe`, `outer pipe` and the old
comment's "narrows in exactly one shape" covered `docs`, `templates`,
`skills`, `agents`, `evals`, `lib` and `tests`. Outside this work item's
frame it found the statements this phase rewrote: the module docstrings
of `lib/tables.py`, `lib/lines.py`, `lib/gaps.py`, `fold_check.py` and
`tests/lib/test_lines.py`, and the docstrings of `gfm_table`,
`opens_table` and `table_cells`. `lib/tables.py:185`, `:457`, `:467` and
`:472` still write a stray row as `| … |`. The walk refuses as a stray row
any line that begins with a pipe, so those lines name the shape loosely.
They were loose before this work too, and they stay (read).

**For the next phase.** `lib/routing.py#table_rows` still splits with
`str.splitlines` under its `exempt from splitlines` marker, now at
`:162-163`, and passes TEXT to `shown`. `routing` imports `tables` after
`blocks`, so phase 2's `gfm_lines` call is reachable as `blocks.gfm_lines`.
`tests/lib/test_routing.py`'s copy case is now parametrized over
`blocks.py` and `tables.py`, and #1573 adds `gitcmd.py` to the same
siblings list (`frame/plan.md` *Overlap with the release*).
