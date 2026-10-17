### Removed

- **The `Reads:` census and the rider stamps are gone (#964).** No pull
  request is refused any more for a unit with no `Reads:` docstring line or
  for a `RIDER:` comment whose stamp has drifted, and
  `rider_check.py --reverify` no longer exists. A `RIDER:` comment stays a
  comment, with no stamp and no checker. There is nothing to do: a `Reads:`
  line or a stamp left in your own files is read by nothing.
  (`1792129100-the-mechanics-leave-before-the-agents-are-rewritten`, #964)

### Changed

- **The round record's grammar is one table, and a line is accepted only
  where it matches its row whole (#964).** `docs/the-review-record.md`
  §*The round record* holds one row per line kind of a
  `rounds/round-N.md`, and `chain_check.py` loads that table and reads nothing
  else for the grammar. `templates/config.md` points at the table instead
  of listing the labels, and `templates/sdd-round.md` keeps what each label
  means and leaves its shape to the table. Two things are now refused that
  passed before: a finding with no `severity:` line, with two, or with one
  whose value is not `must` or `should`, and a finding with no `answer:`
  line or with two.
  A round record in flight that lacks either line adds it before it meets
  this release's check. Where the table itself cannot be read, because the
  document is missing, a row will not parse, or a row the check reads a
  meaning from stands where the check does not look for it or has a
  `How many` the check cannot keep, `chain_check.py` stops with exit 2
  naming the file, never a pass.
  (`1792129100-the-mechanics-leave-before-the-agents-are-rewritten`, #964)
- **A `## Not verified` row is closed by the word `closed` (#964).** The
  row's Item cell opens with `closed`, lower case, then the item, and the
  second cell says what closed it:
  `| closed how the gates render in a TUI | seen on screen, 2026-08-25 |`.
  `unverified-check` refuses a row that opens with the old check-mark
  emoji, naming the row and the edit to make. It also refuses a bare
  `closed` with nothing after it, and `Closed` or `closed:`, which would
  otherwise read as open. The hygiene step reads every `overview.md` under
  `seal/specs/`, released or in flight, until `settle` retires its
  directory. So before you move your `hygiene.yml` pin to this release,
  rewrite every closed row that still opens with the old mark to open with
  the word, in each of them. A base revision still reads the old mark as
  closed, so `--baseline` keeps comparing every base written before the
  word. An open item whose own text begins with the word `closed` reads as
  closed, and nothing refuses it, so word such an item to open with another
  word. The overview template, `templates/config.md` and the implement,
  verify and settle skills show the word.
  (`1792129100-the-mechanics-leave-before-the-agents-are-rewritten`, #964)
