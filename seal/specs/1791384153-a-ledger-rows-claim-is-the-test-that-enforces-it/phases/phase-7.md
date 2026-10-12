# 1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it — phase 7

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | 1a6aa945 |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

The record reader (`spec.md` D9, and D10's checker half): two options on
`evidence-check`'s `main`; a reader of the pytest recorder's `test` lines
keyed by the `session` line; the match by the recorded path and a names
prefix with `[…]` stripped; the held rule; MALFORMED details naming the
observation; the one existence line; `--reverify` and `--into` `LEFT`
lines; the record reaching `node_finding`'s three callers the way
`questions.md` Q6 answers. S15–S20 and S22, each over a record the real
recorder wrote. `questions.md` Q5 (the category of a passed setup) was this
phase's measurement.

## What this phase found

**Q5, measured: yes on both builds.** The real recorder, run over a planted
suite (a pass, a skip, an xfail, an xpass, a failure, a setup error, a
parametrised function, a class), wrote `""` for every passed `setup` and
`teardown` report and `passed` for the call alone, under pytest 9.1.1 (this
suite's runner) and under 7.4.4 (`uvx --python 3.12 --with pytest==7.4.4`);
a skip is written on the `setup` report as `skipped`, a setup error as
`error`. `test_the_recorder_writes_a_passed_setup_under_no_category` is the
pin. The held rule is as `spec.md` D9 wrote it.

**Q6, answered: a module value.** `main` sets `SUITE_RECORD` once, before
any ledger is read, and `node_finding` reads it; `held_by_tests`,
`family_view`'s member loop and `reverify`'s call through `held_by_tests`
are unchanged. Measured at 1a6aa945 by `bin/evidence-check --strict .`: 43
coordinates drift, every one `evidence_check.py#main`, which the options
change either way; `check_ledger`, `ledger_families` and `reverify` move by
nothing. A parameter would have moved `check_ledger` and `reverify` too,
which this item's own fragment and 127 released coordinates cite (the
frame's count). `NODES_READ`, a second module value, is what lets `main`
print the existence line only where a ledger held a test row.

**The words.** A refused row's detail is `<observation> in the recorded
suite, so nothing holds the claim — <the remedy>`, the observation one of
`not run`, `skipped`, `xfailed`, `xpassed`, `failed`, `error` — several
named worst first where a class or a parametrised function owns more than
one, and any other word a plugin writes after them. The existence line is
printed once after `total:`: *test rows were read for existence alone: no
suite record was given, so whether each cited test ran and passed was not
read — `broad-gate` hands this check the sealed run's record*, with *no
session under DIR carries the key KEY* in place of the reason where a
directory and key were given and nothing under them carried the key. A
directory without its key, or the reverse, is refused before anything is
read, exit 2.

**The reader is the record's, as `spec.md` §*Data & interfaces* says.**
`suite_record` reads `path`, `nodeid` and `category` of each `test` line
(`when` is not needed: `""` already marks a passed setup or teardown) and
splits the file with this module's own `gfm_lines`, so no new
`splitlines` call meets the line guard. A path is named by `record_name`,
`broad_gate.py#record_path`'s rule, and S19 runs both readers over one
record whose node id (`test_x.py::test_y`, rootdir `tests/`) differs from
the row's spelling.

**S17 needed no line of the checker.** Round 2's spellings —
`xfail(condition=False)`, `xfail(strict=True)`, `skipif(True)`,
`skipif(False)`, a skip under a module `if`, `pytestmark +=` — and round
1's (a module-level `pytest.skip`, a helper module, a class with
`__init__`) are each read as pytest recorded them: the conditional xfail
and the false skipif passed and are held, the strict xfail that passed
reads `failed`, the rest `skipped` or `not run`.
`test_the_checker_names_no_mark` holds that no mark's name stands in the
checker's source.

**Seen red (§15).** The phase-6 checker refuses `--suite-record` as an
unrecognised argument (a probe in the scratchpad, exit 2). Through
`bin/mutation-check` against 1a6aa945: the record never set, 35 red; no
observation refused, 31; the prefix rule made exact, 4; the parametrise
strip removed, 4; `""` counted as an outcome, 4; the existence line never
printed, 4; the key check removed, 2; the path not named by `record_name`,
2; the option pair unchecked, 1; an unowned test held, 8.

Executed, output read: the new module, 120 passed;
`tests/test_the_recorder_writes_what_its_process_ran.py`,
`tests/test_the_lenient_run_says_what_the_broad_gate_will_say.py`,
`tests/test_evidence_check.py`,
`tests/test_a_released_row_is_read_again_in_a_fragment.py`,
`tests/test_a_row_points_by_content.py` and
`tests/test_every_reader_ends_a_line_where_gfm_does.py` with it, 1073
passed; `uvx ruff check` and `uvx ruff format --check` on both files.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| none | none |
