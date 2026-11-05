# Phase 3: 1793862999-unverified-baseline-is-run-by-a-person-only

## What this phase found

**The frame held at every coordinate the phase changed.** At `6b925563`,
`settle.py` called `open_record_rows` with `None` at lines 944 and 1795, as
design *Scope* item 12 says. `pr_body.py:448` and
`tests/behaviour/test_the_sealer_guarantees.py:89-90` called `sections` with a
string heading. No file outside `unverified_check.py` and its test module
named `strict_header` or `_text_at`. `parse_section` was not called from
outside the module.

**The U+2705 relaxation stood on two lines, and both went.** The first was
the `and strict_header` on the refusal. The second was
`word in (CLOSED, OLD_MARK)`, which read the mark as closed. Once the
refusal holds whatever the source, no row reaches the second line with
U+2705, so that line now reads `word == CLOSED`. No case can tell the two
spellings of that line apart, so it has no `seal mutate` run. It is part of
the relaxation that `## Removes` names, so it is no departure.

**Three cases were rewritten instead of deleted, and one gained an
assertion.**

- `Test_open_record_rows::test_refuses_to_read_a_section_it_cannot_read_as_nothing_open`
  read the `legacy` fixture at `HEAD`. It now reads a memo written on disk
  under `tmp_path`. A4 needs this case: a section the strict reader cannot
  read is one entry saying so.
- `Test_open_record_rows::test_accepts_every_open_item_of_the_record` drops
  its ref. It also asserts that a directory with no `gaps.md` holds no row.
  `Test__text_at`'s refusal case held that before. It left with `_text_at`,
  and the `OSError` branch now stands in `open_record_rows`.
- Design *Scope* item 12 removes `Test_sections`' regex case. I rewrote it
  as `test_accepts_the_heading_spelt_exactly_and_no_heading_near_it`, so the
  class keeps a case for what the string arm finds. The mutant that matched
  `LOOSE_HEADING` in `sections`, run against `-k Test_sections` alone,
  turned the rewritten case red, and the refusal case too.

**No new case was written.** The plain run always called `check_text` with
`strict_header=True`, and `settle.py` always passed `None`. So removing the
relaxations changes nothing that the plain run or the settle says. Design
*Scope* item 12's last bullet writes a case only for such a change.

**The units that stay say what they do for today's callers.** These texts
were rewritten:

- the `OLD_MARK` comment;
- the docstrings of `_LooseHeading`, `parse_section`, `sections`,
  `check_text` and `open_record_rows`;
- the test module's docstring, which no longer names a clone written before
  the normalisation;
- `Test__LooseHeading`'s docstring.

`LOOSE_HEADING` keeps its class. Its docstring names one use, the hint
`check_text` gives.

**Commits:** `77c2a5a1` (the removal) and `248a465f` (`sections`'
docstring). Executed at `77c2a5a1`:

- Six mutants through one `seal mutate` call on
  `skills/verify/scripts/unverified_check.py`, against
  `-k "Test_parse_section or Test_sections or Test_check_text or Test_open_record_rows"`.
  All six went red. The mutants were these:
  - the header check relaxed to `is_header`;
  - the U+2705 refusal off;
  - the early return on a `none` line restored;
  - `sections` matching `LOOSE_HEADING`;
  - a missing `gaps.md` returning an entry;
  - the unreadable entry dropped.
- Mutants 1, 3 and 5 were run again one at a time. The failing cases were
  `test_refuses_a_section_it_cannot_count_at_its_line[the old column]`,
  `test_refuses_a_section_holding_the_old_line_and_names_the_line` and
  `test_accepts_every_open_item_of_the_record`.
- `git grep -n -w -e strict_header -e _text_at -- ':!seal/threads'` exits 1
  with no output. The same search at `6b925563` names 17 lines.
- `ruff check` and `ruff format --check` on the three changed files exit 0.
- One `bin/test` command ran 39 modules and exited 0, with 2819 passed and
  10 skipped. The 39 are `tests/skills/test_pr_body.py` and every test module
  that `git grep -l` finds naming `unverified_check`, `settle.py` or
  `settle/scripts`.

`248a465f` changes one docstring. On its tree, `bin/test` ran
`tests/skills/test_unverified_check.py` and `tests/skills/test_pr_body.py`
and exited 0, and `ruff check` and `ruff format --check` on the module
exited 0.

**The search for the reading's other statements is a sample.** Outside
`seal/threads` and `.test_durations`, I ran `git grep -n -i` for
`edit a commit`, `old mark`, `U+2705`, `before the corpus`, `was normali`,
`legacy header`, `relaxation`, `old heading` and `at a ref`. It found
`docs/layout/the-record-layout.md:143-144` and
`docs/checks/the-fold.md:139-145`. The design's `## Rule changes` removes
or rewrites both at the settle. It also found these, which still hold:

- `unverified_check.py`'s `readable`: `chain_check.py` reads a record at
  `HEAD`;
- `tree_at` and `show`: `chain_check.py` and `settle.py` read at a ref;
- `closing_word`: the U+2705 refusal names the rest of the cell.
