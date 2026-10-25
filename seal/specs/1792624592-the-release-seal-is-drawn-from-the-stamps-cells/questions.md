# Questions for the planner: the release seal is drawn from the stamp's cells (#1009)

## What the ticket left open and the tree answered

Nobody needs to reopen these; each names where its answer was read.

1. **What one cell is in the PNG.** One grid point of
   `seal_stamp.py#build`, which is half of one terminal character and square,
   by the comment above `DISC_CELLS`. The PNG shows the disc 28 cells across
   and 28 tall, as the stamp does.
2. **How many pixels one cell is.** `CELL_PX`, whose value and grounds
   `spec.md` *Data & interfaces* states. A cell must be a whole number of
   pixels, and today's display width at density 2 is not a whole multiple
   of 28 cells (`plan.md` A8), so the width moves a little. A different
   size changes one constant and nothing else, so this is written down and
   not asked.
3. **May `release_seal.py` import Pillow.** Yes, inside `draw` only. It is a
   release script and not a gate (`CONTRIBUTING.md` *Running the checks*),
   and the `seal` job's pip step installs `PILLOW` before the draw.
4. **How `seal_stamp.py` exposes its cells without a copy.** Through
   `build()`, which its own `compose` already reads; `release_seal.py` loads
   the module by path as it loads `broad_gate.py`.
5. **What shows outside the disc.** Transparency, as the terminal shows its
   own background there.
6. **Pillow or a hand-written encoder.** Pillow, as the owner wrote in the
   issue (`plan.md` A3).
7. **The `docs/` sentences.** Changed through `spec.md`'s `## Rule changes`,
   by the standing rule in `skills/implement/SKILL.md` *Document layout*;
   Q1 below offers the owner the exception.
8. **The two cases pinning those `docs/` sentences.** Their `rsvg-convert`
   assertions are dropped now and every other assertion stays (`plan.md`
   A6).

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Should this pull request edit the three `docs/` sentences that name `rsvg-convert` and the SVG directly, as work item 1792473741 did on its owner's answer, rather than through `spec.md`'s `## Rule changes`? The tree cannot answer it because the standing rule says a pull request does not edit `docs/`, and only the owner grants an exception to it. It matters for this release: v0.22.3's own checklist box, the one a person follows if the seal job fails, will say `rsvg-convert` until the settle after the release. | a person | **Through `## Rule changes`** (the rule): `docs/` is untouched in this diff; the three sentences stay false from the merge to the owner's settle, and the settle applies them. **Edited in this diff** (the exception): the sentences are true at the merge; the three `## Rule changes` items become the no-change block, and the two pins can assert the new sentences instead of dropping theirs. | Through `## Rule changes`; the build proceeds on it. | open |

**`Who can answer` takes one of three values and nothing else.**

- **a person**: what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement**: a probe, a command or a count settles it, so a person is
  the wrong instrument, and queueing the row behind one wastes a round trip.
- **the work**: unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing, and the
`Status` column is written by whoever answered, as `answered <date> by <who>`,
never by whoever asked. Sorting the rows this way also keeps the batch short
enough to answer in one sitting: two of the three kinds never need a person.

The orchestrator carries each answered row into `spec.md`'s `## Rule
changes` (a policy clause or an open-questions section) when it drains the
work item's rows, at the moment `skills/implement/SKILL.md` *6. Drain the
rows before the broad run, and keep the records* names.
