# 1791382684-every-reader-and-record-is-inventoried — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 8160ad69 |
| Ran by | smith on opus, as the run-level `handoff.md` §*Starting on a new machine* item 4 names the spawn |

## What this phase was asked

The rows in `seal/ledger/1791382684-every-reader-and-record-is-inventoried.md`:
one claim per acceptance row of `spec.md` §*User scenarios & acceptance*
that a test holds, anchored on the test by #836's form where one holds it;
the changelog fragment; `overview.md` opened with the divergences phase 2
met. Verified by `bin/evidence-check .` exit 0, `correction-check` clean and
`survivor-check --range origin/release/v0.21.0...HEAD` clean. Stop when this
phase closes; phase 4 waits for #894 and #896.

## What this phase found

**Two rows, both on one test.** Of the seven acceptance rows, a test holds
two: row 4's grammar half (B1) and row 5 (B2), each by
`tests/test_a_reader_declares_its_input_class.py::test_every_unit_of_shipped_python_declares_or_is_on_the_census`.
Each was seen red by `mutation-check` against the committed tree: a written
line replaced by `pass`, its direction word changed to `dropped`, and one
removed census line put back; all three red, and the file restored by the
tool's own hash comparison. Rows 1 to 3 are read in the inventory and the
issues, row 6 is phase 1's listing, and row 7 is `evidence-check`'s run; none
is a test, so none is a row. The plan's other anchor, "the census file's
heading-less line count", was not written: a count anchored on a quoted line
of a `.txt` file holds the line, not the count, and the count is in B2's
claim beside the test that refuses any line out of step.

**A ledger fragment makes the work item live, and the records arm then
reads `inventory/`.** With the fragment in place, `evidence-check` read this
item's records for the first time and refused 14 names in 10 inventory lines
as `NOT-IN-TREE`: units and constants the inventory read at 5623d728 that
siblings have since removed, a test-helper name and a directory word; the
findings name them, and they are not written out here, where they would be
refused the same way. Each of those lines now ends `· NAME NOT IN TREE`, which is the remedy the finding names and what the line means: the
inventory is a reading of a tree that had them. `spec.md` §*The inventory's
fate* says nothing in the build edits the inventory; the marker changes no
cell's reading, and `overview.md` records the divergence.

**`survivor-check` reads the census as one sentence.** The census is
`path#unit@hash` lines with no blank line between them, so the check took
its first block as one removed sentence and named five places in past work
items' records that mention one of the 189 units. None says a unit is
undeclared; each names code that still stands. They are rows in
`survivors.md`, each with a quote from the standing text.

**What ran at this phase's close.** `bin/evidence-check .` exit 0 (8,397
ok, 0 drifted, the records arm with no finding); `bin/correction-check
--range origin/release/v0.21.0...HEAD` exit 0; `bin/survivor-check --range
origin/release/v0.21.0...HEAD --exempt` this item's `survivors.md` exit 0;
`bin/unverified-check .` exit 0, this item's `overview.md` 3 open; the
eleven suite-wide guards with the registry test, 609 passed; and the 38
modules that walk this tree's work items, with the four that read a phase
record or a question row, 3,475 passed and 79 skipped. The whole suite was
not run; it is the sealer's.
