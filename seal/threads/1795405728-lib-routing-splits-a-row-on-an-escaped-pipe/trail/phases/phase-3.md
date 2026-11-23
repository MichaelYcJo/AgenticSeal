# Phase 3: 1795405728-lib-routing-splits-a-row-on-an-escaped-pipe

## What this phase found

**The frame holds against the tree at `357a05b39`.** Phases 1 and 2 left
`skills/settle/scripts/passages.py` as it stood at `351a28c71`
(executed: `git diff --quiet 351a28c71 -- skills/settle/scripts/passages.py`
exited 0). So `FENCE` at `:37`, `_lines` at `:68-70`, the walk in `words`
at `:73-97` and `SECTION` at `:42-44` stood where `frame/design.md` G10
puts them (read). Search 5 printed `:37` and `:68` before the build
(executed). `lib/lines.py#readable` returns `blank_fences(gfm_lines(text))`,
so the walk *Scope* item 7 names already splits at GFM's three line endings
(read).

**`words` takes its lines from `readable` and drops heading lines from
them.** The module loads `lib/lines.py` once, through `lib/sibling.py`, at
the first text it reads, where it loaded it at the first heading line.
`readable` blanks a fenced block's lines rather than dropping them. The
words come out the same, because `str.split` reads a run of blank lines as
one gap (judged against `frame/design.md` *Scope* item 7).

**One helper went that `## Removes` does not name.** `_heading_level`
loaded `lib/lines.py` to ask one question of it. `words` now asks
`readable` and `heading_level` of the same module, so `_reader` returns the
module, and `_heading_level` had no caller left (executed:
`git grep -nw _heading_level` prints nothing).

**S5's case is `Test_words::test_reads_the_words_after_a_backtick_run_four_spaces_in`.**
Its text is `Intro.`, a blank line, three backticks four spaces in, a blank
line, and a run of `WINDOW` words. The case first asks
`tests/commonmark_oracle.py#hidden_text` whether the run's line is shown,
and then asks `words` to read the run. It was seen red against
`passages.py` as `351a28c71` holds it, which `cb69dac5b`'s parent still
held (executed: `bin/test -q -p no:xdist tests/skills/test_passages.py -k four_spaces`).
The failing line was `assert shared(text, run)`, and the oracle's line
above it passed. So the old fence rule is what failed, and markdown-it
shows the line the case expects read.

**Every rule document read under the new `words`, against the old**
(executed: `test_tmp_corpus.py` in this phase's scratch directory, run once
with `python3 -I` over the worktree at `cb69dac5b` and `passages.py` from
`357a05b39`). It printed `71 files; 1 differ`, and the one file was
`docs/releasing/release-checklist.md`. That file gains 21 windows, and no
other corpus file holds any of them. This equals `frame/design.md` G10's
prediction.

**The release checklist's backtick lines are no fence to a renderer
either.** `frame/design.md` G10 calls the lines at `:360-363` a fence.
They stand six spaces in, after a blank line, under a list item whose text
begins two columns in. So a renderer reads them, and the paragraph below
them, as one indented code block (executed:
`tests/commonmark_oracle.py#hidden_text` over the file names lines 360 to
366 `code`, and none `fence`; and `test_tmp_cmark.py` in this phase's
scratch directory, run once under
`uv run --no-project --with cmarkgfm==2025.10.22`, renders lines 353 to
367 with the backtick lines and that paragraph inside one `<pre><code>`). The old `FENCE` hid the four lines from the
opener to its closer. `readable` hides none of them, because
`lib/lines.py#live_lines`' docstring names the indented code block as the
one context it deliberately does not model. So the paste check now
compares words a renderer shows as code, as every reader through
`lib/lines.py` already does. *Scope* item 7 asks for that reading (judged
against `frame/design.md` *Scope* item 7 and G10).

**`seal mutate`, run after `cb69dac5b`, two mutants, two red** (executed,
each with `bin/test -q -p no:xdist tests/skills/test_passages.py -k Test_words`):

| File | Mutant | Red |
|---|---|---|
| `skills/settle/scripts/passages.py` | `reader.readable(text)` to `reader.gfm_lines(text)`, so no fence is blanked | `test_refuses_fences_and_headings_and_reads_case_and_backticks_as_no_words`, on its fenced shape |
| `skills/settle/scripts/passages.py` | the heading filter to `if True` | the same case, on its heading shape |

The tree was clean after both runs (executed: `git status --short` printed
nothing).

**The phase boundary set, at `cb69dac5b`** (executed, one command,
`xargs bin/test -q < boundary.txt` in this phase's scratch directory).
`test_tmp_boundary.py` drew 141 test files. They are the plan row's four;
`tests/skills/test_passages.py`, the one test file this phase changed;
every test file that loads `passages.py`, or a shipped module that loads it
directly or through another, or imports a test file that does; and the 66
test files that declare no `TARGET`. `tests/conftest.py` loads
`skills/settle/scripts/rules.py`, which loads `rule_changes.py`, which loads
`passages.py`, so every test file that imports `conftest` falls in the set.
The run gave 5655 passed and 10 skipped.

**Search 5 of `frame/design.md` prints nothing at `cb69dac5b`** (executed:
`git grep -nE '^FENCE|def _lines' -- skills/settle/scripts/passages.py`
exited 1).

**`seal layout --pairs` names no pair in `tests/skills/test_passages.py`**
(executed).

**Rule 19's search, a sample.** `git grep` over the tree outside `seal/`
for `passages.py#FENCE`, `#_lines`, `_heading_level`, a fence rule named
beside `passages`, and the sentence that fenced blocks and heading lines
are dropped. It found that sentence in
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`'s docstring
and in the existing `Test_words` case. Both still hold, since `readable`
drops fenced blocks. `docs/checks/the-pull-request-check.md:167` and
`docs/running/what-a-script-gates.md:56` name `passages.py` as the reader
and say nothing of its fence rule (read). No file under `evals/` names
`passages` (executed). A statement of the old rule in other words is
outside what these searches reach.
