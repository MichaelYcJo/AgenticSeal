# Phase 2: 1795405728-lib-routing-splits-a-row-on-an-escaped-pipe

## What this phase found

**The frame holds against the tree at `179c682bc`.** Phase 1 moved the
coordinates `frame/design.md` gives at `351a28c71`, and nothing else
differed. Search 1 printed `lib/blocks.py:426`, `lib/routing.py:162`,
`lib/tables.py:419` and `:511`, and `pact_check.py:338` and `:358`.
Search 2 printed lines of `lib/blocks.py`, `lib/routing.py:127`,
`lib/tables.py`, `tests/lib/test_blocks.py` and
`tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py:25`.
Search 4 printed `tests/lib/test_routing.py:626` and
`tests/lib/test_tables.py:802`, `:1041` and `:1172` among its lines
(executed). The U+2028 cases *Scope* item 6 names stood at
`tests/lib/test_tables.py:781-886` and `:1154-1170`, and at
`tests/lib/test_routing.py:228-239` (read).

**`frame/questions.md` Q1 is answered by its default.** Once
`tests/commonmark_oracle.py#hidden_text` answers per CommonMark line,
`_starts` and `_starts_in_inline_html` have no caller, so both went. So did
`_tokens`, `SENTINEL` and `SPACES`, which only `_starts_in_inline_html`
read (executed: `git grep` over `tests` for each name prints nothing
outside that file). The Q1 row's Status cell and the oracle's row of
`frame/design.md` `## Removes` are the orchestrator's to fold (judged
against `frame/questions.md` Q1's default).

**Three test files outside *Scope* item 6's list changed.**

- `tests/test_commonmark_oracle.py`'s case on the eight breaks read the
  oracle's per-piece answers. It is re-pinned as
  `test_the_oracle_ends_a_line_where_commonmark_does`: a fenced line
  holding a break is one hidden line, and the text after a break on a line
  that opened inline raw HTML belongs to that shown line. Its three
  assertions on a piece between a tag's attributes, at a closing tag's `>`
  and inside an image description went. Each such text is now one line
  that hides nothing, which the case's first assertion already holds, and
  their guard was the sentinel `_starts_in_inline_html` placed. Seen red
  against the oracle at `179c682bc`, whose failing line read
  `{0, 1, 2, 3} == {0, 1, 2}` (executed).
- `tests/lib/test_blocks.py`'s four `Test_walk_text` cases on pieces went
  with `walk_text`, their guard. `test_where_the_walk_claims_to_be_exact_it_is`
  moved into `Test_walk` and compares `walk` over the lines `as_read` now
  gives, `gfm_lines(text)`, with the oracle.
- `tests/skills/test_pact_check.py` gained a `U+2028` row in
  `test_grades_the_exact_table_and_names_a_near_one_beside_it` and in
  `test_refuses_an_anchor_row_nobody_reads`. `near_headers` and
  `first_table` now count a line where GFM ends one, which is a change of
  behaviour, and no case held it. Each row puts a U+2028 in the heading
  above the second header and expects line 7. Both were seen red against
  `179c682bc`'s code, which named line 8 (executed).

**Each re-pinned reading is held to cmark-gfm in its case.** A probe in
this phase's scratch directory, `test_tmp_cmark.py`, read each shape
through `tests/gfm_table_oracle.py#rows_under` for all eight breaks
(executed). The cases now assert the same answer beside the walker's:

- `test_a_break_commonmark_does_not_honour_hides_no_config_row`: cmark-gfm
  renders `Mode shared` and a one-cell `-->` row. The walk reads
  `Mode shared` and refuses the `-->` line, which holds no pipe. It used to
  refuse at the header.
- `test_a_row_after_a_break_gfm_does_not_honour_is_no_row_of_its_own`:
  cmark-gfm renders `Mode shared` and drops the cells after the second.
  The walk reads the GFM line as five cells, the break between two pipes a
  blank one, and refuses it by its width. It used to read `Mode shared`
  and refuse the piece after the break.
- `test_a_header_after_a_break_gfm_does_not_honour_is_no_table`, both
  positions: cmark-gfm renders no table, and the walk finds no
  `| Item | Value |` header, so its one sentence is the `holds no` one.
- The two cases on a table after a break inside inline HTML, and the case
  on a heading after a break, keep their readings. Each gains the
  cmark-gfm assertion.

Every new reading equals cmark-gfm's or is a refusal, as
`frame/design.md` S4 states (judged against S4 and contract rule 14).

**S3's case is a shape of `Test_table_rows`, not a `parse` case.**
`frame/design.md` S3 says `parse` reads the branch. `parse` takes the
branch from the second cell `table_rows` gives (read: `lib/routing.py#parse`),
and `test_reads_each_row_as_cmark_gfm_renders_it` holds each of its shapes
to cmark-gfm. So the shape `a U+2028 inside a cell` went there, beside S1's
and S2's (judged against the crafter's rule *A new test starts from its
group*). Seen red against `351a28c71`'s `lib/` under this phase's tests,
unpacked in this phase's scratch directory, and run with
`-p no:xdist -p no:cacheprovider`: the failing line read
`('Branch', 'fix/a') != ('Branch', 'fix/a b')`. It is red against
`179c682bc`'s code too (executed).

**Docstrings past *Scope* item 5's list described pieces too.** They are
`lib/blocks.py`'s module docstring, where the inline-HTML paragraph and the
list of uncertain contexts each named a piece of a line, and
`lib/tables.py#hidden_lines`, whose list of uncertain contexts did the
same. The `ALPHABET` and `FOUND` comments in `tests/lib/test_blocks.py`
are reworded the same way. `lib/lines.py`'s comment now says the census
holds every other split to a marker naming the text it splits, which is
not markdown, as `frame/design.md` G13 reads the markers (read).

**`pact_check.py` reaches `gfm_lines` through `tables.blocks`.** Both
functions are handed the loaded `lib/tables.py`, which imports
`lib/blocks.py` by name, so the walk's own split is one attribute away and
no second load is needed (judged against `frame/design.md` *Scope* item 4
and `skills/core/SKILL.md`, "A fact has one source").

**`seal mutate`, run after `1054c3816`, four mutants, four red**
(executed, each with `-p no:xdist`):

| File | Mutant | Cases run | Red |
|---|---|---|---|
| `lib/tables.py` | `gfm_table` splits with `text.splitlines()` | `test_tables.py -k "break or piece or heading_piece"` | the eight-break cases on a `<!--` after a break, a row after one and a header after one, and the heading case |
| `lib/routing.py` | `table_rows` splits with `text.splitlines()` | `test_routing.py -k "U+2028 or break_commonmark"` | S3's shape, and the eight cases on a declaration after a break |
| `pact_check.py` | `near_headers` splits with `text.splitlines()` | `test_pact_check.py -k "U+2028"` | `[a heading holding a U+2028]` |
| `pact_check.py` | `first_table` splits with `text.splitlines()` | the same | `[a second table under a heading holding a U+2028]` |

The two cases on a table after a break inside inline HTML stay green
under the first mutant. There the fence run before the table never
closes, and the base reading hides everything below it, so a second guard
holds them. They pin the shape's reading, which equals cmark-gfm's, and
not the line split.

**The phase boundary set, at `1054c3816`** (executed, one command,
`xargs bin/test -q < boundary.txt` in this phase's scratch directory).
`test_tmp_boundary.py` drew 141 test files. They are the plan row's 13;
every test file this phase changed; every test file that loads
`lib/blocks.py`, `lib/lines.py`, `lib/routing.py`, `lib/tables.py` or
`pact_check.py`, imports `tests/commonmark_oracle.py`, or imports a test
file that does; the test files of the 22 shipped modules that load one of
those four `lib/` modules; and the 66 test files that declare no `TARGET`.
The run gave 5654 passed and 10 skipped. `be0de7118` after it rewrapped
`lib/tables.py#hidden_lines`' docstring alone, and
`bin/test -q tests/lib/test_tables.py tests/behaviour/test_docs_line_wrap.py`
gave 635 passed over that tree (executed).

**Searches 1, 2 and 4 of `frame/design.md` print nothing at `be0de7118`**
(executed).

**Rule 19's search, a sample.** `git grep` on `walk_text`,
`gfm_line_starts`, `GFM_LINE_ENDS`, `_starts_in_inline_html`,
`reader line`, `a piece of a`, `Test_walk_text`, `TEXT is the file`, the
two removed refusals' words and `text=None` covered the whole tree outside
`seal/` and `evals/`. What it found outside this phase's rewritten text
uses "piece" or "on a line of its own" of something else, and three
re-pinned docstrings in `tests/lib/test_tables.py` that state the old
reading as history. `docs`, `templates`, `agents`, the skills' `.md`
files, `CONTRIBUTING.md` and `README.md` hold none of `splitlines`,
`U+2028`, `walk_text`, `gfm_lines` or `form feed` (executed).
`evals/behaviour/proofer/seeded-7a8899d5/graders/truth-seeded.md:7` still
names `walk_text`, which search 2's pathspec leaves out as `frame/design.md`
states.

**For the next phase.** `skills/settle/scripts/passages.py` is untouched,
and search 5 still prints its two lines. `lib/lines.py#readable` reads
`gfm_lines`, so the walk phase 3 moves `passages.py` onto already splits
as every reader now does.
