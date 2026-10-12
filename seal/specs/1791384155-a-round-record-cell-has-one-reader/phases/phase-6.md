# 1791384155-a-round-record-cell-has-one-reader — phase 6

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | c71b6fbb |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

J5 of `spec.md`, the rest: one ancestry comparison for the `broad_gate` arm
and `seal`; one reader of `close`'s prefixes for `doubled_grounds` and
`close`; one count of field rows and `Pass` boxes under `field`,
`pass_checked`, `field_index`, `close` and `seal`, with the duplicate error
in `check_round`; `docs/round-record-spec.md` by replacement. Verified by
S11 and S12 red first and three modules green. The resumed session was also
told to check each phase against the owner's review: one reader per cell is
consolidation, and no reader may predict a format nothing owns.

## What this phase found

- **Every reader this phase added reads a format a writer in this
  repository owns**: the `Target SHA` and `Broad gate` cells, the `fixed at
  <hex>` prefix `close` writes and the `; ` it joins with, and the field and
  box shapes `new` writes. None predicts a foreign tool, so nothing here
  needed to be left out under the owner's review.
- **The field-row refusal runs on every record, not in `check_round`.**
  `check_round` reads the last record alone, and a doubled row on an earlier
  record would otherwise have reached its arms as an absent row — a cause
  that is not the cause. `doubled_fields` runs beside `doubled_grounds` in
  the per-record walk; the second box is `check_round`'s, where `Pass` is
  read.
- **`round_record.field_index` keeps its own line walk.** It needs the line
  index it then replaces, which `fields` over the table rows cannot give, and
  it already applied the same one-row rule. The three box counts in `close`,
  `notes` and `seal` read `pass_boxes`.
- **A prefix after the reviewer's grounds began is the reviewer's.** The
  first test shape only proved prose quoting a close mid-segment; a
  `continue` in place of the `break` survived it, so a case with a later
  segment beginning `fixed at` was added.
- A note holding `; ` ends the prefix run early, so such a cell reads as
  fewer closes than it holds — stated in `close_prefixes`' docstring as the
  permissive side.
- `--reverify` now runs on a later date than the earlier phases, so the
  stray re-stamps of the release branch's own drifted rows also appended
  `· 2026-10-12` to four sibling rows' dates; those were put back with the
  hashes.
- The whole-tree chain check reads the same as before the phase: no
  committed record carries a doubled row, box or close.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| the ancestry loop in the `broad_gate` arm and the one in `seal` | `chain_check.gate_before_review` |
| `doubled_grounds`' search of the whole cell, and `close`'s and `notes`' anchored prefix match | `chain_check.close_prefixes` |
| first-wins in `field` and `pass_checked`, and the three box scans in the generator | `fields`, `pass_boxes`, `doubled_fields`, `check_round` |
