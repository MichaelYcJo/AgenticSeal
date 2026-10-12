# 1791384152-a-reader-declares-its-input-class — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 94d0e50d |
| Ran by | smith on Opus, as `handoff.md`'s State row records the spawn |

## What this phase was asked

`docs/the-reader-registry.md`: the four classes, the grammar, the population
rule and K1's demoted role, the three ways weighed and the verdict, the
census, module bodies, `## Removes`, the limits, and the counts at landing as
phase 1 read them. Two bullets in `CONTRIBUTING.md` §*What a change to a gate
must carry*, a row in `docs/the-record-layout.md` §*docs/*, this work item's
`changelog.md`, and ledger rows per scenario in
`seal/ledger/1791384152-a-reader-declares-its-input-class.md`. Verified by
`bin/fold-check` exit 0, the eight suite-wide guard modules, the folded
statement module, and the pasted-passage ratchet unchanged.

## What this phase found

**The limits are seven, not six.** The spec's list of what neither check can
read has six entries; the document carries a seventh, a census line put back
by hand, which phase 1 found the check cannot tell from an original
(`overview.md`).

**Three first drafts were refused by the guards, and each refusal was
right.** `tests/test_release_hygiene.py` refused four mentions of the
release's own version number in a loaded document, which would go red the
day that version ships; they are written as what they mean instead.
`tests/test_no_passage_is_pasted_into_a_second_file.py` refused the
policy-document boilerplate sentence four other documents already carry, and
then refused the `## Removes` comment in `templates/sdd-spec.md` for
repeating the document's grammar paragraph; the boilerplate is gone and the
comment now names the document's section instead of restating it. Its
baseline was not touched.

**`bin/fold-check` reads the current directory unless told otherwise.** Run
from the session's own checkout it reported 171 statements in 18 documents —
the main checkout's tree, not this worktree's. With `--root` it reads 185
statements in 19 documents, the new one included, at exit 0. Phase 3's record
claims no fold-check run, so nothing there rests on the wrong reading.

**The ledger rows are held by their tests.** Every scenario row names its
cases as pytest node ids and carries no hash, so no docstring edit drifts
them; D1, the document's own row, is the one hashed anchor, and the phase's
last edit to the document re-stamped it in place.

**Rows a phase-4 edit drifted were read before they were written.** One:
0.18.0's C5, which claims `docs/the-record-layout.md`'s `docs/` table lists
the two documents #727 cut out; the table's new row leaves that true.
