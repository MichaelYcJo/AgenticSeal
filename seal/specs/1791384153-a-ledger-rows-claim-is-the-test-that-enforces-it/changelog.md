### Added

- **A ledger row may name the test that holds its claim, and such a row never
  drifts (#836).** A row's Code grounds cell can name tests as pytest spells
  them — `tests/test_x.py::test_y`, or `tests/test_x.py::TestA::test_b` for a
  method — in place of `path#anchor@hash`. A hashed row records what the code
  held when somebody read it, so every edit to that code owed a re-read; most
  rows written since 0.18.0 were those re-reads. A test row has no hash.
  Read alone, `evidence-check` holds it where the named `def` or `class` is
  defined in its file once, and is `BROKEN` for a test or file that is gone,
  a constant, or a name defined twice (a method written bare is told its
  spelling); a row mixing a test with a code coordinate is `MALFORMED`, and
  a coordinate whose quoted locator holds `::` stays a coordinate. One line
  says the test rows were read for existence alone. `--reverify` writes
  nothing on a test row. A released row moves onto its test by one
  `Corrected ·` row naming the test, written by the branch whose edit drifted
  it, and a released test row whose test was renamed is re-pointed the same
  way; `--into` names that option once when it writes a `Re-read ·` row, and
  so does the commit advisor's repair line under a frozen ledger. A
  repository that vendors the checker through `evidence-ci` updates its copy
  before writing a test row: an older copy reads one as `MALFORMED`.

- **The broad gate holds a test row only where the run it seals saw the test
  pass (#836).** Its ledger arm hands `evidence-check` the pytest record of
  the suite it just ran (`--suite-record`, `--suite-key`). A cited test is
  held where every line the recorder wrote for it says `passed` — a class
  owns its methods and a function its parametrised cases — and is
  `MALFORMED` otherwise, naming what the run did: not run, skipped, xfailed,
  xpassed, failed or error. Nothing about a test is predicted from its file,
  so a test pytest never collected, or a mark in any spelling, is simply a
  line that is not `passed`. A test the sealing machine skips — a `skipif`
  true there — refuses the seal there; hash that row, or seal where the test
  runs. A preflight runs no suite and reads test rows for existence alone.

### Changed

- **`fold-check` reads an `Enforced by:` target with the ledger's resolver
  (#836).** A method is now written `path::Class::method`, as pytest and a
  test row spell it, and a name is found where it is defined rather than
  anywhere in the file. Every target in this repository's `docs/` resolves as
  before.
