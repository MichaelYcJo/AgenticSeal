# 1792473741-dash-shapes-become-field-words — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | ebd9d3d9 |

## What this phase was asked

The release title line (S15 to S17), on the owner's answer to Q1.
`publish_release_note.py#title_line_re` reads
`release: X.Y.Z symptoms: <…>` whole; the fallback's log line names the
expected shape and quotes the line found. The module docstring,
`docs/release-checklist.md` §*5* and §*6*, and `docs/branch-and-release.md`'s
bullet are rewritten in the same commit as the reader. S13's sweep over the
whole tree runs last.

## What this phase found

- **The labels are spelt once, `TITLE_LABEL` and `SYMPTOMS_LABEL`,** and
  both the pattern and the fallback's log line are built from them. The
  log line reads, for a commit carrying the old line, ``the tag name — the
  tagged commit's title line is `release: 1.2.3 symptoms: <the symptoms>`,
  and its first is `release: 1.2.3 — x` ``, and for one carrying none, `it
  carries no `release:` line`.
- **S17 was seen red the other way round.** It passed against the old
  reader and the old document together, which agreed. With the reader
  changed and §*5* not yet, it failed, the title falling back to `v1.2.3`;
  with both changed, it passed.
- **Two mutations needed a case.** Trailing whitespace after the symptoms
  was stripped by no case, so `test_the_line_the_checklist_copies_is_the_line_the_reader_reads`
  now reads the line with two spaces after it. The timing case read a value
  that opened with a space, which the shape refuses at its first character,
  so a nested repeat survived it; it now reads a value of spaced words and
  one long word. With the nested, failing repeat
  `(\S(?:\s*\S+)*)\s*!$` the case timed out after 30 s with no verdict.
  The other four mutations went red on the first cases.
- **S13's sweep** (executed at ebd9d3d9, `git grep -F` outside `seal/specs/`
  and `changelog/`): `release: X.Y.Z —` is found nowhere, and a `| nowhere |`
  cell only in S12's refused-row fixtures at `tests/test_chain_check.py:631`
  and `:636`. `none — <`, `withheld —` and `undecided —` are found in
  `docs/the-review-record.md` §*The guarantee*'s sentence, which
  `## Rule changes` rewrites at the settle; in three comments of
  `unverified_check.py` and one docstring of
  `tests/test_unverified_rows_close.py` that name the old line as what is
  refused; and in the S6 and S9 fixtures of
  `tests/test_the_sealer_guarantees.py`, which are the near misses
  themselves. `does not hold —` is found once, in prose of
  `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` where the
  dash is punctuation.
