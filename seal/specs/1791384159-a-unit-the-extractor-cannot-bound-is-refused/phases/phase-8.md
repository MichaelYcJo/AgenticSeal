# 1791384159-a-unit-the-extractor-cannot-bound-is-refused — phase 8

| Field | Value |
|---|---|
| Phase | 8 |
| Commit | (the record commit's parent; `plan.md`'s Status cell names it) |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

`plan.md` phase 8: `SKILL.md`'s six sections, `docs/the-evidence-ledger.md`'s
paragraph with `Enforced by:` naming S1 and S3, `rider_check.py`'s docstring,
the docstrings of `bounding_rule`, `resolve_unit`, `file_units`;
`changelog.md` rewritten with the installer paragraph of `spec.md`; the
fragment's U8 row; `overview.md` brought to the redesign. Cases S11, S12.
Verified by `tests/test_a_record_states_what_the_tree_has.py`,
`tests/test_the_fixes_name_their_surface.py` and the eight guard modules.

## What this phase found

**The section keeps its heading.** §*Resolving a unit without a parser* now
says that without a parser a unit is not bounded and the anchor is a quoted
line; renaming the heading would have broken the rows that cite it for a
title, and its first sentence states the turn.

**The docstrings were done where the code changed.** `bounding_rule`,
`resolve_unit`, `file_units` and `text_regions` were rewritten in phases 5
and 6, in the commits that changed what they describe, and the rider check's
docstring in phase 6 (`phases/phase-6.md`). This phase checked each against
S11's words.

**The survivor sweep found two sentences the redesign had left false**, and
both were corrected rather than excused: a docstring in
`tests/test_a_rider_reaches_its_file.py` and #867's rider `Corrected · S1`
row, each naming "only by resurrection" as a BROKEN cause. The row is a
fragment row, so it was corrected in place, with `rider_check.py#region_lines`
added to its coordinates and a Notes trace. The sweep's other 36 places are
fixtures, frozen released rows, other work items' records and true
sentences; one `| Range | Grounds |` row in `survivors.md` holds the
grounds, since the range deletes shipped sections.

**The changelog fragment promises only what holds.** Round 1's 🟡 3 was a
fragment saying "every other row keeps its hash and its verdict" over kinds
that changed. It now names what changes — every bare symbol outside `.py`,
`.pyi` and `.md` reads `BROKEN`, a decorated `.pyi` stub reads `DRIFTED`
once — and limits the promise to `.py` and `.md` rows; S12's case refuses the
old sentence.

**S11 and S12 were red against phase 7's head** (the three document cases)
and green after.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| The skill's suffix table rows for the brace languages and YAML, the bracket-walk and block-rule bullets, the declaration-rule and how-sure-it-is paragraphs, the unsure-place, eighteen-suffix and first-design upgrade bullets | §*Resolving a unit without a parser* as the format, §*What the region is*'s quoted-line row, and one upgrade bullet in §*Known limits* |
| The first design's policy paragraph | the rewritten paragraph under the same marker, `Enforced by:` S1, S3 and S5's cases |
| The first design's changelog fragment | the rewritten fragment |
