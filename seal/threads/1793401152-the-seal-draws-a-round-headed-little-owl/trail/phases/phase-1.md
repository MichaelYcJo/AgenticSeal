# Phase 1: 1793401152-the-seal-draws-a-round-headed-little-owl

## What this phase found

**The frame held, with one claim that does not.** Every coordinate row 1
names was where the plan put it at `56c94b6f`: the colours at
`seal_stamp.py:92-139`, the geometry at `:187-201`, `read_sprite`'s bound
at `:249`, `build` at `:286-335`, the test's reference at
`tests/skills/test_seal_stamp.py:46-238`, and the docstring pins at
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:224-228`. No
other file names a removed constant (`git grep` over the tree outside
`seal/threads/`, executed). The claim that does not hold is S3's `git diff
efb91989 -M --stat shows the move`. The destination `seal-mark.txt` already
existed, so git reports a deletion and a modification, with `-M` and also
with `-B -M` (executed). The move is shown by the blobs instead: `git
rev-parse efb91989:assets/seals/candidates/little-owl-16.txt
HEAD:skills/verify/scripts/seal-mark.txt` prints `993b924c` twice
(executed).

**The plan carries no approval line, and the tree says it needs none.** The
installed crafter definition calls `plan.md`'s approval line the gate. The
tree's `skills/implement/SKILL.md` since `aa9221d3` says that reading
`plan.md` and spawning the build is the approval, and that no line records
it. The build followed the tree. This record and `gaps.md` start from the
tree's `templates/records/sdd-phase.md` and `sdd-gaps.md`, for the same
reason.

**The reference was transcribed from the approved stream.** The file read
is `<scratchpad>/owl/f1/stamp.ans` (sha256 `62b56aeb…7130d`), where
`<scratchpad>` is the orchestrating session's scratchpad directory. `cmp`
of it with the durable copy in the owner's private brand repository,
`candidates/little-owl-16-on-wax.ans` under its brand skill, exits 0
(executed). The command, run from the repository's top directory, was:

```
python3 -I <scratchpad>/1793401152/phase-1/transcribe.py <scratchpad>/owl/f1/stamp.ans tests/skills/test_seal_stamp.py
```

The script parses the stream's SGR codes into 28 x 28 half-cells. It maps
each colour to its letter by the table in `frame/design.md` *Data &
interfaces*, which the script carries itself. It takes the twin's text half
from the test module's existing `REFERENCE_TWIN`, read with `ast`, because
the approved stream drew the disc alone. It never opens `seal_stamp.py`. It
reported 15 colours plus `None`, painted columns 1 to 27 and half-rows 0 to
26, and the ring's counts past 9.8 cells from the centre: `[208, 46, 67,
50, 57, 8, 24, 24]` for `None` and the seven frame colours. Those counts
are `Test_build`'s. The script lives in the session scratchpad and does not
outlive it.

**`build` reads the rule in a different order from the prototype, and
gives the same cells.** `build` tests the edge, then reads `lit` once for
everything past `R - STEP_INSET`, and splits that into the outer edge, the
step ring and the lip. The test's `owners_disc` follows the prototype's
order: edge, outer edge, lip, step ring, field. `Test_build` compares the
two over all 784 cells, and `Test_compose` compares `build` with the
approved picture cell for cell. The wobble sums its terms from `RADIUS`
left to right, as the prototype does, so the floating-point edge is the
same number.

**Seen red against the relief disc, before the code changed** (executed,
`bin/test tests/skills/test_seal_stamp.py -p no:xdist -q -k "Test_read_sprite or Test_build or Test_disc_cell or Test_disc_cells or Test_letter_row or Test_compose or Test_colour_row or Test_stamp"`):
7 failed. They were `Test_build`'s cell case, `Test_disc_cells`'s row
case, `Test_letter_row`'s letters case, `Test_compose`'s three layout
cases and its reference case. `test_the_docstrings_describe_the_letter_and_the_rows_it_carries`
failed on `every cell exactly one of fifteen colours`. Three rewritten
cases passed against the old disc, and none of their verdicts reads the
disc's colours. `Test_disc_cell` only renames `FACE` to `BREAST`, with the
same value. `Test_stamp`'s change is its docstring's figure. In
`Test_read_sprite`, the old and new bounds are both 9.8.

**The sprite's bound had nothing behind it, and one parameter now pins
it.** `seal mutate` moved `read_sprite`'s bound from `RADIUS - STEP_INSET`
(9.8) to `RADIUS - LIP_INSET` (10.6), and then to `DISC_CELLS / 2 -
STEP_INSET` (10.3). `Test_read_sprite` stayed green under both. The
`on-the-rim` parameter drew line 1 column 1, a cell 10.61 cells from the
centre, so any bound below 10.61 refused it. It now draws line 2 column 1,
at 9.92. That is the nearest a sprite cell comes to 9.8 from outside, since
a cell's offsets from the centre are half-integers within the sprite's 16
columns. Its id is now `on-the-step-ring`, and the shadow case's id is
`its-shadow-on-the-step-ring` (`18bf3119`). Both mutations then went red.

**Every unit was mutated after its commit, one command each**
(`bin/seal mutate skills/verify/scripts/seal_stamp.py --replace <old> <new>
--tests "bin/test tests/skills/test_seal_stamp.py -p no:xdist -q -k <cases>"`,
executed at `18bf3119`, all ten `red`, the tree clean after):

| Unit | Mutation | Cases |
|---|---|---|
| `read_sprite`'s bound | `RADIUS - STEP_INSET` to `RADIUS - LIP_INSET` | `Test_read_sprite` |
| `read_sprite`'s bound | `RADIUS - STEP_INSET` to `DISC_CELLS / 2 - STEP_INSET` | `Test_read_sprite` |
| the wobble | `EDGE_WOBBLE` loses its second term | `Test_build` |
| the gloss streak | `% 360` dropped from the angle | `Test_build` |
| the lip's dark | `>=` to `>` at `LIP_DARK_FROM` | `Test_build` |
| the step ring | its dark and lit swapped | `Test_build` |
| the outer edge | `EDGE_DARK_FROM` to 0 | `Test_build` |
| `KEY` | `GLOSS` written `h` | `Test_letter_row or Test_compose` |
| the field | `FIELD` given the pupil's value | `Test_build or Test_compose` |
| the pupil | `PUPIL` given the field's value | `Test_build or Test_compose` |

A first batch ran before the code was committed, because the first commit,
`34664525`, carried only the staged sprite move. That commit was amended
into `9266b5bf` before anything read it, and the ten runs above are the
ones taken over the committed tree.

**The stamp's size is probe P1's** (executed): the widest reference panel
with its label is 5,725 UTF-16 units, and `stamp(SAMPLE_ROWS)` plus a
newline is 5,931 bytes. `Test_stamp`'s docstring states 5,725 against the
relief disc's 5,959.

**The phase-boundary set** (executed, one command, exit 0, 1106 passed and
1 skipped):

```
bin/test tests/skills/test_seal_stamp.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/hooks/test_sealer_stamp.py tests/hooks/test_sealer_stamp_queue.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/skills/test_broad_gate.py tests/behaviour/test_one_word_one_meaning.py tests/hooks/test_dispatch.py tests/behaviour/test_release_hygiene.py tests/github/test_release_seal.py tests/skills/test_seal.py -q
```

The last four modules are not on row 1's list. Each one loads or names
`skills/verify/scripts/seal_stamp.py`, which this phase changed. The set
left out `tests/test_censuses.py`, which reads every tracked file. This
record was one, and round 1's finding 1 found the paths in it that the
census refuses.

**S10, held to this phase's files** (executed): `git grep -n -i` for
`scratchpad`, `wax3`, `owl_final` and the private brand repository's name
over `skills/verify/scripts/`, `tests/skills/test_seal_stamp.py` and
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, and `git
grep -n 'little-owl-16' -- ':!seal/threads'`, each exit 1 with no match.

**For phase 2.** `assets/seals/README.md` still describes the relief disc
and its nine colours, and its *The owl* entry still names `owl.ans` and the
icon as the horned owl's. `seal stamp --shape` now prints the little owl on
the wax (executed), so the new entry's `owl.ans` is drawn from this phase's
`seal_stamp.py`. That is `18bf3119` or a later commit that leaves
`skills/verify/scripts/` alone.
