# 1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | ecb4f8fd |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

The writer: `seal.py#table_span` removed; `with_row` and `doubled_modes`
over `config_table`'s row indices, the insertion point from the walk's own
header and delimiter positions; a refused table is `(None, sentence)` and
`write_row` prints *Nothing was written*; `seal mode --check` exits 2 on it;
`NEW_CONFIG` unchanged. Red first: the writer-and-reader agreement case
extended with shape 7, the bare-pipe limitation case removed and its
inverse planted; `test_the_writer_reads_where_commonmark_breaks` and
`test_the_writer_leaves_a_commented_row_alone` green. Q5 is this phase's.

**Direction:** refuse more, command only. **Prompt budget:** zero.

## What this phase found

**Q5: re-found, not exposed.** `with_row` finds the header as the first line
`unfenced` shows whose `table_cells` are `CONFIG_TABLE` — the line
`gfm_table` itself starts at — and inserts two lines under it where the walk
read no row. `gfm_table`'s return shape is unchanged, so the pact readers
see nothing of this.

**The frame's *green* for two writer cases does not hold.** Both texts are
tables the walker refuses: `test_the_writer_reads_where_commonmark_breaks`
has `-->` under its row, which GFM shows as a row, and C10's comment sits
directly under the delimiter row, so the live `Mode` row under it is a row
the walk never reaches. A writer that reads the reader's table refuses
both. Each case was re-pinned to *nothing written, the file's bytes
unchanged*, which keeps what each was about: no second table appended, and
the commented row not rewritten. `seal mode` on C10 is now a refusal where
it was a write.

**`mode_refusal` refuses the walker's table too**, after the path, so the
switch (`seal mode local` from shared) is refused before the folder moves —
the third of the things `with_row` refuses, beside an unreadable file and a
doubled row.

**New and re-pinned cases, each seen red**, run from archives of the two
earlier trees with the new test files copied in (HEAD never moved). Against
bd27b1a6, phase 1's reader with the stop rule's writer, 8 red: the
agreement case's shape-7 half (the writer inserted a second `Mode` row),
`test_seal_mode_writes_nothing_under_a_bare_pipe_and_names_the_line` (the
write returned `""`), `test_the_writer_inserts_where_the_walk_says_the_table_ends`
(shape 12's indented header was no table to the stop rule, so a second
table was appended), the two re-pinned writer cases (three ids), and the
switch forms `seal mode shared` and `seal mode local` of
`test_a_table_the_walker_refuses_is_refused_and_nothing_is_written`. Its
other two forms and `test_check_exits_2_on_a_table_the_walker_refuses` were
already green there, because phase 1's reader answers `refused`; against
3bb2ea42, the base, all five were red.

Verified by `bin/test tests/test_the_mode_question_is_asked_once.py
tests/test_the_mode_is_a_row_and_a_command.py
tests/test_every_reader_ends_a_line_where_gfm_does.py
tests/test_a_reader_declares_its_input_class.py -q` at ecb4f8fd: exit 0,
467 passed. The modules that load `seal.py` by path
(`test_a_script_copied_alone_exits_2.py`,
`test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`,
`test_a_row_points_by_content.py`, `test_first_setup_asks_once.py`): exit 0,
414 passed.

**Mutations:** five through `mutation-check` — the refused-table arm, the
insertion point after the last row, the insertion point under the
delimiter, `doubled_modes` reading one row, and `mode_refusal` dropping the
walker's sentence. All five red.
