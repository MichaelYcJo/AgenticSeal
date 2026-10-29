# Phase 3: 1793169127-pact-check-reads-the-retired-grammar

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 3f807db1 |

## What this phase was asked

Build `plan.md`'s phase 3 as its row states: `coordinates.py` keeps what
`pact_check.py` reads. The resolver and its units go, with
`tests/behaviour/test_a_unit_is_bounded_where_a_parser_decides.py` and the
resolver's cases in `tests/skills/test_coordinates.py`.
`tests/censuses.py#coordinate_grammar`, `HASH_AFTER_AT`, its list entry and
`tests/test_censuses.py` *Test_coordinate_grammar* go. The module docstring
says what it holds and who reads it. S11's grep prints nothing. Write the
work item's `changelog.md` fragment in this last phase.

## What this phase found

- `coordinates.py#unescape` left here with `resolve_unit`, its last caller
  (phase 2's record).
- Six of the resolver's cases pinned the heading rule through a quoted
  heading path in a `.md` file: a section's end, a path narrowing, a
  repeated heading, an indented heading, a heading in a fence, and a
  heading three spaces in. Nothing else in the suite asks `heading_path`
  these questions, and `pact_check.py#clause_hash` depends on each answer.
  So those six moved to *Test_heading_path* and ask `heading_path` over
  `markdown_lines` directly, with every assertion's value unchanged.
  `gaps.md` records it against `design.md` *Removes*. The other resolver
  cases, and those of `py_spans` and `text_regions`, went with their units.
- The moved cases were checked by mutants over `heading_path`. The section
  end at a heading of the same level, and a line that is no heading, were
  each red. A part that matches nothing and falls back to its parent's
  region survived `tests/skills/test_coordinates.py`, and was red against
  `tests/skills/test_pact_check.py -k clause_hash`, whose "no clause" case
  holds it. So no case was added.
- Two docstrings that stay named removed units. `markdown_lines` named
  `parsed_spans`' memo and a timing of the ledger's `--strict` run, and
  `gfm_lines` named `ast`. Each now says what holds for the clause reader.
  The review-colour glyph in `markdown_lines`' citation became the word
  `white`, as the other citations in these files write it.
- `docs/the-pact.md:85` names `tests/skills/test_coordinates.py` on a
  `check:` line, and the module still holds the cases that line stands
  for. `docs/` is the settle's.
- S11, the grep `plan.md` *Technical context* writes out, printed nothing
  (exit 1).
- S12: `tests/skills/test_coordinates.py`, `tests/test_censuses.py`,
  `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py`,
  `tests/skills/test_pact_check.py` and
  `tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`,
  which reads `quoted_lines`: 311 passed, exit 0.
