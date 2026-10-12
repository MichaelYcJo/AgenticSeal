# 1791384155-a-round-record-cell-has-one-reader — phase 7

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | ab58c26f |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

The closing: `docs/round-record-spec.md`'s opening sentence on the one
reader; the input-class table in `spec.md` §*Data & interfaces* checked
against what was built; `changelog.md`; the ledger rows for the new units and
the last re-read; `overview.md`. Verified by S13 and S14, `fold-check`,
`evidence-check` and the text-hygiene modules, run narrow. The spawn added
the hand-back checks: the eight guard modules, `survivor-check`,
`evidence-check --strict` and `correction-check`.

## What this phase found

- The opening sentence took `docs/round-record-spec.md` to 1,000 lines,
  which `fold-check` holds as at the ceiling and not over it (exit 0). Both
  documents this work edits are now full; the next edit to either cuts it.
- #835's registry is not on `origin/release/v0.21.0`, so the class table
  stays in `spec.md`, with a row for the five names the build added beside
  the proposed ones (`questions.md` W3).
- `survivor-check` over the branch named 35 places. Two were false — test
  docstrings saying the generator told the check `draft`, and a 2026-09-14
  measurement of where the fix table strips a home — and were corrected
  (d74339d7). The other 33 are true where they stand, mostly released rows
  and released work items' records, and are rows in `survivors.md`.
- `evidence-check --strict` exits 2 on the release branch's own 33 drifted
  rows and on nothing else; `correction-check` exits 0.
- The changelog fragment is one `### Changed` entry (the no-payload exit) and
  one `### Fixed` entry (the five readers).
- The phase's own commit is b251dafe; the survivor corrections and rows that
  followed it end at ab58c26f, which this record names because the checks
  above were read there.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| none | none |
