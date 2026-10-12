### Added

- **Every unit of shipped Python declares what it reads, in its own docstring
  (#835).** Each top-level `def` and `class` in a tracked `.py` file outside
  `tests/test_*.py` carries one line: `Reads: owned|observed|guess — <what it
  reads>; unknown refused|passed|mixed`, or `Reads: nothing — <why>`.
  `tests/test_a_reader_declares_its_input_class.py` refuses a unit with no
  line, a line outside the grammar, and a `nothing` line on a unit that opens
  a file, runs a process, reads the environment or hands text to a
  standard-library parser. A module whose top-level statements read declares
  in its module docstring. Every unit is asked, whatever it calls: a list of
  reading calls only catches a `nothing` that contradicts it, and never
  decides who must declare. The 1,587 units undeclared at landing are listed
  in `tests/undeclared_readers.txt` with their ledger hash, and a listed unit
  owes nothing until it changes; then it declares and leaves the list.
  `docs/the-reader-registry.md` is the rule's home.
- **A frame names what its work removes, and `evidence-check` reads it
  (#835).** `templates/sdd-spec.md` carries a `## Removes` section: one row
  per reader, rule or pin the work takes out of the tree, its coordinate in
  the ledger's grammar without a hash, or the one line `nothing — <why>`. The
  records arm reads each row of a live frame as a claim of absence: a
  coordinate that still resolves reads `STANDING`, and a cell the ledger
  would refuse — no coordinate, a test's node id, a bare symbol in a file no
  parser bounds — reads `REFUSED`, never as a removal that happened. Both
  exit 2. A new `seal/config.md` row, `Removes from | <work-item id>`, makes
  the section required for every frame at or above that id; it is read by
  the same reader as `Ledger frozen from` and refused the same way when the
  value is not an id.

### Changed

- **A phase record no longer carries a removal table (#835).**
  `templates/sdd-phase.md`'s *What this phase removes* recorded, once per
  phase, a fact the frame now records once with a check that reads it. A
  removal a phase makes that its frame did not name is a divergence in
  `overview.md`. Phase records already written keep their tables.

  **What an installer sees on upgrade.** A consuming repository whose live
  `spec.md` already holds a `## Removes` heading has its rows read from this
  release on; one that has no `Removes from` row is asked for no section.
  The `Reads:` rule and its census are this repository's own test, and ask
  nothing of a repository that installs the plugin.

  A `seal/config.md` that is there and will not read, or that writes
  `Removes from` twice, now stops a plain `evidence-check` run at exit 2 —
  and so the CI ledger job and the commit advisor — as it already stopped
  `--reverify`: the records arm reads the row through the freeze row's
  reader, which refuses such a file rather than reading it as absent. A
  repository that declares no `Removes from` row meets this too.
