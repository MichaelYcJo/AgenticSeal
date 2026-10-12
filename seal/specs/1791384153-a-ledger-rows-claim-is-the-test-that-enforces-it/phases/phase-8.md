# 1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it — phase 8

| Field | Value |
|---|---|
| Phase | 8 |
| Commit | 4136d3ba |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

The gate hands over the record (`spec.md` D10's gate half):
`broad_gate.py#main` adds the record directory and `head_key` to
`checks[LEDGER]` where the suite ran, and neither on a preflight; item 2 of
the module docstring's list says what the arm now reads. S21: the module
that pins `checks[LEDGER]`'s argv, red with the two items missing, and one
gate run over a planted repository whose test row names a test its row
skips, NOT SEALED with the ledger arm named.

## What this phase found

**The call site stays one assignment.** `PARTITION`'s cases read every
`checks[...] = run(...)` in `main`, so the preflight's difference is a list
built just above it, `observed`, empty where `head` is None and
`[EVIDENCE_RECORD, records_dir(keep), EVIDENCE_KEY, head_key]` otherwise,
and spread into the one call. `EVIDENCE_RECORD` and `EVIDENCE_KEY` are new
constants beside `EVIDENCE`, held equal to the checker's own
`SUITE_RECORD_OPTION` and `SUITE_KEY_OPTION` by the pin: the gate does not
load the checker, and a second spelling of an option is what the pin keeps
from drifting.

**`head` is a `RunRecord` wherever the suite ran, even one with no
session**, so the options are handed whenever the suite ran; a row that
loaded no recorder then reaches the checker's *no session under DIR
carries the key KEY* line rather than a refusal of every test row
(`spec.md` D10).

**The two cases.** `test_the_gate_hands_the_ledger_arm_the_run_it_seals`
in `tests/test_the_lenient_run_says_what_the_broad_gate_will_say.py`, beside
the `--strict` pin, reads the call site and the list above it.
`test_the_ledger_arm_reads_the_run_it_seals` in
`tests/test_the_seal_is_taken_once_by_the_sealer.py` uses that module's
template repository: a fragment row naming a skipped test makes the gate
exit 1, NOT SEALED, the kept `ledger.txt` reading *MALFORMED … skipped in
the recorded suite*; a row naming the passing `test_one` leaves the arm
with neither a MALFORMED nor the existence line.

**Seen red (§15), through `bin/mutation-check` against 4136d3ba:** the two
items emptied, 3 red (the pin and both planted cases — the held one too,
since with no record the arm prints the existence line); the preflight
guard removed, the pin red.

Executed, output read: the two gate modules with
`tests/test_the_gate_names_every_step_ci_runs.py`,
`tests/test_the_gate_asks_the_range_ci_will_ask.py`,
`tests/test_the_recorder_writes_what_its_process_ran.py` and
`tests/test_a_script_says_which_interpreter_it_needs.py`, 651 passed;
`uvx ruff check` and `uvx ruff format --check` on the three files.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| none | none |
