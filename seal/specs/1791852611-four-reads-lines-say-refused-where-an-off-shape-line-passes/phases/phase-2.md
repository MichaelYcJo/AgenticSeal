# 1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 8879db49 |
| Ran by | specseal:smith on claude-opus-5-5 |

## What this phase was asked

Phase 2 of `plan.md`: `removes_section` hands back the lines under
`## Removes` that are neither a table row nor a `nothing` line;
`removal_findings` refuses each at its line, naming the line, the two
shapes and where prose goes; both docstrings say so and their `Reads:`
lines stay `unknown refused`; new cases in
`tests/test_a_record_states_what_the_tree_has.py`, each seen red before it
is committed; `docs/the-reader-registry.md` §*A frame names what its work
removes* gains the sentence and its `Enforced by:` line the node id;
`templates/sdd-spec.md`'s comment says nothing else sits under the heading
and where prose goes.

With the orchestrator's amendment answering M1 at the spawn: the section
ends at the next heading of any level, and a level-3 heading reading
`Removes` opens none; the refusal says prose goes under a sub-heading after
the table; the template's comment and the registry sentence say the same;
a case pins the heading boundary, seen red; and this frame's own prose line
under `## Removes` moves under a `### Why these rows` sub-heading in the
same phase.

## What this phase found

**How each case was shown red.** The four new tests were written first and
run against `evidence_check.py` as it stood at 3a66113f, which is the base's
copy (`git diff --quiet 321e9de1 HEAD -- skills/evidence-check/scripts/evidence_check.py`
exit 0): `bin/test -q -p no:cacheprovider -p no:xdist
tests/test_a_record_states_what_the_tree_has.py -k "off_shape_line or
belong_under_removes or refused_twice or any_level_ends"` gave 11 failed,
1 passed. Each S1 case failed on `[] == [('REFUSED', 'spec.md:<n>', …)]`,
because the old reader dropped the line. The S3 case failed with only the
empty-section finding. Both boundary cases failed on `[] ==
[('NOT-IN-TREE', 'spec.md:11')]`, because the old reader cut the
sub-heading's prose from the name half. The S2 case passed against the old
code, as it should: it pins what must NOT be refused. It was shown red by
`mutation-check` instead, removing the header-and-rule-row exemption, which
gave `red` (1 failed).

**Mutations over the added units, all through `mutation-check`, all `red`.**
The off-shape list emptied in `removes_section` (9 failed); the loop in
`removal_findings` given `other[:0]` (9 failed); the heading test put back
to `level <= 2` (2 failed); `level == 2` widened to `level >= 2`, so a
`### Removes` would open a section (1 failed, the `### Removes` case).

**A guard survived, and it was dead code.** The first build kept a blank
line out of the off-shape list with `elif text.strip():`. Replacing it with
`else:` SURVIVED, because `claim_lines` drops blank lines before the section
reads them (probed: `claim_lines(['a', '', '  '])` returns `[(1, 'a')]`).
8879db49 removes the guard and says why in the docstring. A blank line in
S2 therefore proves nothing about this unit; the S2 case still holds the
header row, the rule row, a two-line comment and a fence.

**W1 is answered: a fifth element.** `removes_section` returns `(present,
cut, rows, nothing, other)`, and `other` is `[(line number, text)]`. Its one
caller is `removal_findings` (`git grep -n removes_section -- '*.py'`). The
detail names both shapes in one sentence and the sub-heading in a second
clause after a semicolon. The new tests pin it whole through `off_shape()`.

**The amendment moves what the name half reads, and that has a cost for
siblings.** The section now ends at any heading, so a sub-heading's lines
are no longer in `cut`. The name half reads them as it reads the rest of the
frame. Prose that names a removed unit in backticks under `### Why these
rows` is `NOT-IN-TREE` once the unit is gone, unless its line carries
`NAME NOT IN TREE`. `test_a_heading_of_any_level_ends_the_section` pins this
behaviour, and the template's comment says it. Under the old reader the same
prose was cut and read by nothing. A sibling frame whose sub-heading prose
names a unit it removes meets this at the 0.21.1 gather run that M1 names.
The alternative was to keep `cut` running to the next level-2 heading while
refusals stop at any heading. It was not taken: a table under the
sub-heading would then be read neither as a removal nor as a name, which is
the unread record this item exists to end.

**S4 holds.** `git diff -U0 origin/release/v0.21.1 --
skills/evidence-check/scripts/evidence_check.py` has hunks only in
`removes_section` and `removal_findings`. `bin/evidence-check .` exit 1 (the
lenient reading) with 13 drifted. These are the same thirteen phase 1 named:
D1 and twelve rows on `agents/warden.md#"## Role"`. No row names
`file_claims` or `check_records`, and nothing is BROKEN.

**Verification, executed at 8879db49.** `bin/test -q -p no:cacheprovider
tests/test_a_record_states_what_the_tree_has.py
tests/test_a_reader_declares_its_input_class.py
tests/test_a_folded_statement_names_what_enforces_it.py
tests/test_a_phase_hands_the_next_one_a_record.py` exit 0, 271 passed (run
at 6c04efd5, before the guard came out). After the guard came out,
`tests/test_a_record_states_what_the_tree_has.py` alone gave exit 0, 142
passed. `uvx ruff check` and `uvx ruff format --check` on the two changed
`.py` files gave exit 0.
