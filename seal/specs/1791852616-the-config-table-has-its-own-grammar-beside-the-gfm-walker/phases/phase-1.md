# 1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | bd27b1a6 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

The one walk: `hooks/config.py#config_table` over `gfm_table(text,
CONFIG_TABLE)`; `indexed_config_rows` and `config_rows` as its projections;
`config_value`, `declared_value`, `declared_mode` answering per item (S2);
`pact_declaration` and `pact_lines_not_read` reading the walker's rows and
appending its refusals; `refusal`, `CONFIG_ROW` and `CONFIG_HEADER` removed, (NAME NOT IN TREE)
`CONFIG_SEPARATOR` and `CELL` kept with a comment naming `path_map`; the
oracle case's fourth header pass; `hooks/mode-gate.py` and
`hooks/evidence-advisor.py` pinned silent over shapes 1, 5, 7 (S3); the
docstrings of `config_rows` and `unfenced` rewritten. Red first in the mode
module (shapes 3, 5, 6, 7, 13), the signer module and the oracle's config
pass. The spawn added the seam with #905: a `### Why these rows` sub-heading
directly above the prose paragraph under `spec.md`'s `## Removes`, words
unchanged.

**Direction:** hooks say nothing. **Prompt budget:** zero — the mode gate
reads a refused `Mode` as an answer it cannot act on, on the first call and
the second (`test_a_table_the_walker_refuses_is_silence_from_the_mode_gate`).

## What this phase found

**The frame held, with one *no*: the three removals could not land in this
phase.** `seal.py#table_span` (phase 2's) aliased both stop-rule patterns
(`CONFIG_HEADER` and `CONFIG_ROW`, both gone since phase 3 · NAME NOT IN TREE)
at import, and `broad_gate.py#refusal` (phase 3's) passes
`hooks/config.py#refusal` through. Deleting them here leaves `seal.py`
failing to load. So `refusal`, `refused_row` and the two patterns stay, the
patterns under a comment saying who still reads them, and leave with their
last caller in phase 3. `refused_row` is not in `## Removes`; it has no
caller outside the tests, and its removal in phase 3 is a divergence row in
`overview.md`.

**This phase's boundary is not green outside its own slice, by the plan's
own allocation.** At bd27b1a6 the verifying command (below) is exit 1 on
four writer cases phase 2 owns — `test_the_writer_reads_where_commonmark_breaks`
(LS, FF), `test_the_writer_leaves_a_commented_row_alone`,
`test_seal_mode_still_writes_a_second_mode_row_for_a_bare_pipe` — because
the stop rule's writer and the walker now read two tables and the read-back
guard catches it. Outside the verified modules, phase 3's pins are red too:
the four sealer cases `## Removes` names, the vendored agreement case (3
shapes), and the two pull-request-language table cases. None was re-pinned
here, because each is a case the plan hands to a later phase.

Verified by `bin/test tests/test_the_mode_question_is_asked_once.py
tests/test_a_signer_declares_its_pact.py
tests/test_one_table_walker_reads_what_gfm_renders.py
tests/test_the_hooks_hide_what_a_renderer_hides.py
tests/test_every_reader_ends_a_line_where_gfm_does.py
tests/test_a_reader_declares_its_input_class.py -q` at bd27b1a6: exit 1,
4 failed (the four above), 4,051 passed.

**Q6 is answered: none.** The oracle's config pass, 5,455 shapes, found no
shape where the walker reads rows cmark-gfm does not render (executed).

**Seen red**, every new case, by running the new test files against an
archive of `3bb2ea42` (the base, HEAD never moved): 23 failed, the S1 case
on all sixteen shapes (ten at the `config_rows` assertion, six at
`config_table`), S2, S3 on shape 7 (`['deny', 'ask']`), the shape-6 case,
the two indented-row cases, the signer refusal case and the oracle's header
case.

**What the walker answers differently, case by case, re-pinned in place:**

- an indented row (one to three spaces) is a row cmark-gfm renders, so two
  of #784's `STRAY_WAYS` — W2 and W8 indented — are read, not refused; they
  left that list for a case of their own;
- a line written `| … |` below the table's end is a row the walk never
  reaches, so every signer case with a pipe-line below a blank line gains
  the walker's sentence last, and the blind-side case's *below it* arm is
  refused with `notify` None;
- #667's C5, C7, C8 and C9b: a comment directly under the delimiter row
  ends the table as GFM ends it, so the live rows below are refused; C9a's
  unclosed `<!--` is an HTML block GFM renders no table inside;
- the fence-rule case's fixtures gained a blank line above the live header,
  because the header directly under a fence line is the migration's shape,
  and the case's decisions are about fences — its first assertion pins the
  refusal that made the blank line necessary.

**One wrong-cause sentence, in the refusing direction.** The walker reads
`str.splitlines` pieces, so a `<!--` after U+2028, a form feed or one of the
six other characters only Python ends a line at begins a piece, and
`raw_html_open` reads it as an HTML block left open: the refusal names a
block GFM does not see. No row is read that GFM does not show. Named in
`overview.md` §*Not verified*; the walker's line-ending treatment is out of
this work item.

**Mutations:** seven, one at a time through `mutation-check`. Six red; the
seventh — the doubled-`Pact notify` early return dropping the walker's
sentence — survived, and `test_a_walker_refusal_follows_a_doubled_notify_row_too`
was planted and seen red against it (bd27b1a6).
