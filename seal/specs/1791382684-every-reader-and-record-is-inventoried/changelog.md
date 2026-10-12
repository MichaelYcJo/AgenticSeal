### Added

- **Every reader and record of 0.20.0 is inventoried (#834).** The work
  item's `inventory/` holds 1,467 reader rows across six parts — each unit,
  what it reads, what it decides, its input class (`owned`, `observed`,
  `guess`), what it does with input it does not understand, and where the
  same judgment is copied — beside 35 record mechanisms with what each cost
  since 0.18.0, and the 63 issues since 0.18.0 by family. The decisions it
  led to are their own issues in this release.

### Changed

- **189 units of shipped Python now say what they read, from the
  inventory's rows (#834).** Each carries a `Reads:` line in its own
  docstring, in the grammar `docs/the-reader-registry.md` states, and has
  left `tests/undeclared_readers.txt`, which goes from 1,584 lines to 1,395.
  Where an inventory row named several units, a unit other than the one
  doing the row's reading says what its own code reads.
  These are the inventory's units whose code has not changed since the
  inventory read it and which no released ledger row cites, so no released
  row owes a re-read. A unit whose code moved since keeps its census line
  and declares when next touched. `hooks/cmdline_base.py`'s units stay on
  the census because that file is pinned byte for byte, and
  `hooks/worktree-guard.py`'s wait for the two changes now rewriting it. No
  reader's behaviour changes.
