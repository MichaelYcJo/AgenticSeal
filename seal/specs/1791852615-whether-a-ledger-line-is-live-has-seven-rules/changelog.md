### Changed

- Whether a ledger or record line is live is stated once, in
  `docs/the-evidence-ledger.md`, and it has three answers because seven
  readers read three kinds of line (#872). A line that holds a claim, an
  anchor or a rider is read when its reader is in doubt, so a parked or
  malformed row is reported and never dropped. A line that excuses or
  declares something, a fold marker or a config row, is not taken on doubt,
  so nothing is excused by a line nobody wrote live. A line a record's rows
  are counted on is blanked the same way on both sides of a comparison. No
  reader's behaviour changed: each of the seven now says in its own
  docstring which answer it gives and what the wrong one costs, and one test
  holds all seven side by side on eight shapes of line, so a reader whose
  answer moves turns a named cell red. `hooks/config.py` is the one reader
  of the second kind that still reads a row below a comment opener nobody
  closed, because it keeps the reading it gave before its walk was added,
  and the statement says so.
