# Implementation Plan: a head run that pytest stopped with exit 0 does not seal (#883)

## Technical context

All coordinates are in `skills/verify/scripts/broad_gate.py` at f667aca9 (read).

- `RunRecord` (`:1628-1670`) holds `unended`, which counts the sessions that stopped part-way. `read_record` (`:1739-1830`) increments it where a keyed file has no `end` line, an `end` line whose `stopped` is not `[]`, or an `end` line whose `exitstatus` is not in `RAN_TO_ITS_END` (`:1797-1808`). `RAN_TO_ITS_END` and its comment (`:1694-1731`) name the one stop no record shows.
- `Check.failed` (`:1200-1202`) is `self.code != 0`.
- `gate` (`:2895`) runs the row, reads `head = read_record(...)` (`:2999`), then loops over the checks (`:3014-3036`). It skips each check that has not failed. A suite that failed gets `failure_lines(check, verdicts, head)`. With no failures, `write_gate_file` writes `trail/gate.md` (`:3049`) and the panel prints `suite_counts(head)` behind a tick (`panel`, `:2662-2667`).
- `failure_lines` (`:2699-2756`) appends `UNENDED_HERE` (`:2785-2792`) where `record.unended` is not 0. This is the only place a stopped session at `HEAD` reaches the output.
- `compare_at_base` runs only for the record's failing files. A suite that failed at exit 0 has none, so the base is not run.
- Tests: `tests/skills/test_broad_gate.py` has the fixture repository (`_repo_template`, `:2303-2320`, copied per case by `tests/conftest.py#repo`), `args_for`, the recorded-run fixture `a_recorded_run`, `Test_failure_lines` (`:2208`) and `Test_read_record` (`:1504`). `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` pins rule 3's sentences of `templates/setup/config.md`, among them the one on `HEAD` (`:526-528`).

The chosen approach's failure scenario, six months on. A repository whose suite holds a deliberate `pytest.exit(returncode=0)`, such as a conftest that ends a smoke run early, has every broad run fail. The Scope 2 line names the cause, and the remedy is the repository's: a suite that stops is not a suite that passed. Second, a recorder that could not write (a full disk) leaves no `end` line, so a run that finished fails. The recorder's warning `agentic_pytest_record: no record written` stands in `suite.txt`, and the next run after the disk is freed passes. Both fail closed, which `CONTRIBUTING.md` *What a change to a gate must carry* asks a gate change to argue: a wrong deny here costs one more run, and a wrong allow costs a guarantee over unrun tests.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Fail the suite where the row exited 0 and `head.unended` is not 0, and say why in the failure form (Scope 1 and 2) | The two fail-closed cases above. | **Chosen.** It reads one count the gate already computes, with the meaning #849 gave it at the base and `.github/scripts/release_seal.py` gives it at the tag. |
| B. Keep the exit-code verdict, and print `UNENDED_HERE` on the passing panel as well | The run still writes `trail/gate.md`, and the sealer reads that file, which carries only `run: <tree> against <base>`. The count reaches nobody who decides, and the sealer guarantees the suite. `skills/core/SKILL.md` *The rule a mechanism is kept against* keeps report-only for a reading that is noisy or guessed. This reading is exact (`frame/design.md` G5). | Rejected. |
| C. Read `stopped` alone, the field #869 added | A test calling `os._exit(0)` leaves no `end` line, so no `stopped` is written, and the run passes (`frame/design.md` G2, executed). | Rejected. `unended` covers it. |
| D. Replace the structure at the recorder: on a stop, the recorder sets pytest's exit status non-zero | The recorder writes what pytest did and never steers it. The module docstring says nothing a test prints or runs changes a word, and a recorder that changed the row's exit would change the user's run. `os._exit(0)` runs no hook, so the recorder could not act on it. | Rejected. |
| E. Replace the structure at the sealer: the sealer reads `records/` and withholds | The sealer runs nothing broad and reads `trail/gate.md` (`agents/sealer.md` step 1). `records/` stays in the gate's kept output outside the tree, so the sealer cannot open it at HEAD. That would move a script's exact reading into an agent's judgment, against `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*. | Rejected. |
| F. Keep `Check.failed` as the exit code alone, the structure every arm shares | The gate's verdict would rest on the exit alone, and G1 shows an exit of 0 over unrun tests. The premise that keeps `Check` as it is: the chain and mode arms have no record, so their exit code is all there is to read. That holds, so `Check` may stay as it is for them. Whether the suite's verdict is decided in the loop or carried on `Check` is the build's choice (`frame/design.md` *Data & interfaces*). | Kept for the other arms. The suite's verdict changes under A. |
| G. Run the row at the base too, and label the stop pre-existing or new | One more full run on each such failure, and the verdict is the same either way: the gate fails a suite on a failure the base shares as well. | Rejected. Out of scope (`frame/design.md` *Scope*, Out). |
| H. Name each `stopped` entry, or the test the session stopped in, in the failure form | The test would be read off the order of the record's lines, and under xdist that order is not the run order, so the name would be a guess. The entries are in `records/`, and `UNENDED_HERE` points there. | Rejected. Out of scope. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope 1, 2 and 3 of `frame/design.md`, in one commit or in commits that each keep the suite's own pins in step (contract rule 14) | The new cases of S1 and S2 and the Scope 2 unit case in `tests/skills/test_broad_gate.py`, each seen red at 40e6c23e or with the change reverted (contract rule 15). S3 and S4 by the existing cases in `tests/skills/test_broad_gate.py`. The moved pin in `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`. Run as one narrow command over those two modules, and over each module that reads a path the phase changed (contract rule 2). `seal mutate` over the new arm in `broad_gate.py#gate` and `failure_lines`, with each surviving mutant named. The suite is the orchestrator's broad run. | 944c1463 |

## Operational impact

None to deploy: no migration, no new variable, no new dependency. A repository whose suite stops part-way at exit 0 sees its broad run fail from the release that carries this. This repository's own broad run on this branch uses the branch's gate, because the installed gate hands the run to the tree's copy where the tree ships `skills/verify/scripts/broad_gate.py` (`docs/the-broad-gate.md` *The gate that measures a tree is the copy that tree ships*). So the orchestrator's broad run here is also the first run of the new arm over a real suite.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
