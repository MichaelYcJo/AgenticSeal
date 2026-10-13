# 1791852614-survivor-check-reads-a-range-as-its-own-commits — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 613e6e2d |
| Ran by | unknown — the spawn prompt named no agent or model for this row, and this record transcribes only what it was given |

## What this phase was asked

`plan.md` phase 3: `corrected`'s docstring and the module docstring's
§*What it does not answer* linking the home in a sentence holding no listed
word and stating the inherited limit; the home's new bold statement with
its `Enforced by:` line naming the new module and `corrected`; rule 18's
carriers and the guard's `LINKERS` gaining `survivor_check.py` (S9);
`skills/code-review/orchestration.md` §*Then ask what the fixes left
standing* unchanged unless its sentence states the two-ends reading.

## What this phase found

- **`corrected`'s docstring was written in phase 2**, with the code it
  describes, so this phase added the module docstring's paragraph, the
  refusal in the exit-code line, the home's statement and the pins.
- **One owner-naming sentence, on purpose.** Rule 18 asks that the carrier's
  text holds `… §*A range owns the commits that descend from its start*
  owns`. Phases 1 and 2 had written it twice, in `parse_range` and `owned`,
  so no single deletion could show the carrier case red. `owned` now points
  at `parse_range`'s link, and the case went red with that one sentence
  changed. The other linking sentences (the module docstring's and
  `corrected`'s) say *is* rather than *owns*, and the no-shape guard reads
  all four.
- **`fold-check` does not bind the new statement's `Enforced by:` line.**
  The section carries no `<!-- specs/<id> -->` marker, as the statement
  above it carries none, and the check binds marked statements only. With
  the line removed, `tests/test_a_folded_statement_names_what_enforces_it.py`
  stayed green. A marker was not added: `survivor_check.py#retired_directories`
  reads a marker in `docs/` as a folded work item, and this one has not
  shipped. The line is kept and read by people, like the line above it.
- **The orchestration's sentence is unchanged.** §*Then ask what the fixes
  left standing* says the check reports *every place at the range's tip
  still carrying wording the range removed*, which states no reading of the
  range.
- **How each pin was seen red**, through `bin/mutation-check`: rule 18's
  carrier case with `parse_range`'s *owns which commits those are* changed
  to *says*; the linking-sentence case with *made before the merge* pasted
  into the module docstring's linking sentence; the home case with *a
  sibling* pasted into the new statement.
