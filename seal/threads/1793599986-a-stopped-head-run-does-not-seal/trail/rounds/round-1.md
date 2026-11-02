# Review round 1: 1793599986-a-stopped-head-run-does-not-seal

```seal
target: 7768896c against release/v0.28.1
```

The round read the branch against `origin/release/v0.28.1` (40e6c23e), in a
`git clone --no-local` of the branch worktree at 7768896c. This is the first
round, so no fact was carried from an earlier one: every coordinate below
was opened this round. `seal/parity.md` is not declared, so the round block
carries no `original:` line. Every mutant this round planted ran through the
`seal` of the #898 worktree (`fix/898-a-mutant-that-does-not-compile-reads-as-caught/bin/seal mutate`),
which refuses a mutant that does not compile before it runs any case.

## Findings

### 1. The new failure line says an exit of 0 means nothing the session ran failed, and the same exit-0 suite lists a failing file and "1 failed" right below it

```seal
severity: should
location: `skills/verify/scripts/broad_gate.py:2808-2812`, `skills/verify/scripts/broad_gate.py:84-86`, `skills/verify/scripts/broad_gate.py:2719-2722`, `tests/skills/test_broad_gate.py:2200-2206`, `templates/setup/config.md:366`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:529-534`, `seal/threads/1793599986-a-stopped-head-run-does-not-seal/changelog.md:3`, `seal/threads/1793599986-a-stopped-head-run-does-not-seal/frame/design.md:27`, `seal/threads/1793599986-a-stopped-head-run-does-not-seal/frame/design.md:60-62`
evidence: executed `bin/test tests/skills/test_tmp_883_probe.py -q -p no:xdist --tb=short`
```

Why it matters: the line exists to tell the person reading a failed broad
run why a suite that exited 0 failed, and it states a false rule about what
an exit of 0 means. Both stops the line is written for choose the exit code
themselves. `pytest.exit(..., returncode=0)` sets the session's exit status
to 0 whatever failed before it, and `os._exit(0)` ends the process with 0
whatever failed before it. So an exit of 0 from such a session says nothing
about whether a test failed.

The crafter's own phase record says so: `trail/phases/phase-1.md` *The frame,
checked before the build* corrects *Scope* 1 because "A test that fails before
a later test calls `pytest.exit("...", returncode=0)` leaves the row at exit 0
with a failing file in the record". The sentence the build wrote into the
constant, the docstrings, rule 3 of `templates/setup/config.md`, the
changelog and the rule's `to:` text still says the opposite.

The probe ran the gate over the fixture repository of
`tests/skills/test_broad_gate.py` with `test_a` failing, `test_b` stopping
the session at exit 0, and `test_c` never reached, once for each stop. Both
runs returned 1 and printed this, in this order, under `suite    exit 0`:

- `the row exited 0, and the gate fails the suite all the same because a pytest session it ran stopped part-way: an exit of 0 says only that nothing the session ran failed, not that it ran every test it collected`
- `failing test files, compared at the base:` over `tests/test_stop.py  new`
- the `UNENDED_HERE` line with count 1
- `1 failed, 1 passed`

A reader who takes the first line at its word reads past the file list. The
path itself is right: the gate fails the suite, runs the base for the
failing file, and writes no `trail/gate.md`. Only the sentence is wrong.

The fix rewrites the clause in each place it stands and moves both pins with
it. Finding 3's case pins the exit-0 suite that also lists a file, so this
wording has a case where it is read beside a failure.

```python
# skills/verify/scripts/broad_gate.py, and the same text at tests/skills/test_broad_gate.py:2202
STOPPED_AT_EXIT_0 = (
    "the row exited 0, and the gate fails the suite all the same because a "
    "pytest session it ran stopped part-way: an exit of 0 does not say that "
    "the session ran every test it collected, and where the stop chose the "
    "code, as pytest.exit() and os._exit() do, it does not say that nothing "
    "the session ran failed either"
)
```

```text
broad_gate.py module docstring, lines 84-86:
  fails where a check exits non-zero, and where the suite's record at `HEAD`
  counts a pytest session that stopped part-way, whatever the row's exit
  (#883): an exit of 0 does not say that the session ran every test it
  collected. A run

failure_lines' docstring, the end of the `record.unended` paragraph:
  ... why it failed (`STOPPED_AT_EXIT_0`): an exit of 0 does not say that
  the session ran every test it collected.

templates/setup/config.md rule 3, and its pin at
tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:530-534:
  Where one did, the suite fails even where the row exited 0, as it does
  when a test calls `pytest.exit()` with a return code of 0 or `os._exit(0)`,
  because a stop that chooses the exit code says neither that the session
  ran every test it collected nor that nothing it ran failed; the failure
  form says so, and no `trail/gate.md` is written.

changelog.md:
  Under the suite's own lines, the failure form says that the row exited 0
  and that an exit of 0 does not say the session ran every test it
  collected.

frame/design.md *Rule changes*, the `to:` text, lines 60-62:
  An exit of 0 does not say that the session ran every test it collected,
  and where a stop chose that code it does not say that nothing the session
  ran failed either.
```

### 2. The rule and the changelog say one stop stays out of the record's reach, and a conftest's `pytest_configure` calling `pytest.exit(returncode=0)` is a second: the gate passes it and writes `trail/gate.md`

```seal
severity: should
location: `seal/threads/1793599986-a-stopped-head-run-does-not-seal/frame/design.md:71-73`, `seal/threads/1793599986-a-stopped-head-run-does-not-seal/frame/design.md:37`, `seal/threads/1793599986-a-stopped-head-run-does-not-seal/changelog.md:3`
evidence: executed `bin/test tests/skills/test_tmp_883_probe.py::test_tmp_a_stop_before_the_session_line -q -p no:xdist --tb=line`
```

Why it matters: the rule this work item hands the settle ends "One stop
stays out of the record's reach: a `pytest.exit()` raised by a
`pytest_sessionfinish` hook that runs after the recorder's." The changelog
says the same. A reader takes "one" as a whole list. It is a sample.

The probe gave the fixture repository `tests/conftest.py` holding
`def pytest_configure(config): pytest.exit('at configure', returncode=0)`
and a failing `tests/test_never.py`. The gate returned 0. It printed
`BROAD GATE PASSED`, with `suite   exit 0` and no count. It wrote
`trail/gate.md`, and `records/` was empty. `suite.txt` holds `exit 0` and
`Exit: at configure`. No test ran.

The cause, read in the recorder and in pytest's `wrap_session`:
`agentic_pytest_record.py:392` registers the `Recorder` from the module's
own `pytest_configure`. pytest calls `pytest_configure` implementations
last-registered first, and a conftest is registered after a `-p` plugin. So
the conftest's `pytest_configure` runs first. Its `Exit` is caught in
`wrap_session` with the session's exit status set to 0, before
`pytest_sessionstart`. The recorder never writes its `session` line, and the
run reads as a row that started no pytest. That is a pass at exit 0, as it
must be for a repository whose suite is not pytest.

Contract rule 12 asks for the class to be listed from what produces it.
Here that is every stop that comes before the recorder writes its `session`
line. Read from `wrap_session`, that is a `pytest_configure` ordered ahead
of the recorder module's, which the probe ran, and a `pytest_sessionstart`
marked `tryfirst` ahead of the `Recorder`'s, which this round read and did
not run. The probe's other case, `pytest.exit(returncode=0)` at a conftest's
import, exits 4, and the gate already fails it.

`docs/the-broad-gate.md` gets this rule at the settle, so the limit sentence
should be whole before then. Edge cases outside the normal flow take a limit
sentence rather than a guard, and the cheapest fix is that sentence. The
structural alternative is for the recorder to claim the key and write its
`session` line from a `tryfirst` `pytest_configure`. A later stop would
then leave a keyed file with no `end` line, which `unended` already counts.
That changes the recorder, which *Scope* Out keeps as it is, so it is the
fix pass's choice to weigh, not a requirement.

```text
frame/design.md *Rule changes*, the end of the `to:` text (lines 71-73),
and the matching sentence of changelog.md:
  Two stops stay out of the record's reach: a `pytest.exit()` raised by a
  `pytest_sessionfinish` hook that runs after the recorder's, which reads as
  a session that ran to its end; and a stop raised before the recorder
  writes its `session` line, such as a `pytest.exit()` in a conftest's
  `pytest_configure`, which leaves no record, so the run reads as one that
  started no pytest and passes on its exit.

frame/design.md *Scope*, Out, the bullet at line 37:
  - **The stops no record shows.** A `pytest.exit()` raised by a
    `pytest_sessionfinish` hook that runs after the recorder's is raised
    after the `end` line was written. One raised before the recorder's
    `session` line, from a `pytest_configure` ordered ahead of the
    recorder's or a `tryfirst` `pytest_sessionstart`, leaves no record.
    Both stay limits.
```

### 3. Two boundaries of the new line are watched by no case: its place above the file list, and its absence at an exit other than 0 or 1

```seal
severity: should
location: `tests/skills/test_broad_gate.py:2256-2281`
evidence: executed `seal mutate skills/verify/scripts/broad_gate.py --replace "if check.code == 0 and record is not None and record.unended:" "if check.code != 1 and record is not None and record.unended:" --tests "bin/test tests/skills/test_broad_gate.py -q -p no:xdist -k 'Test_failure_lines or Test_gate'"`, `seal mutate skills/verify/scripts/broad_gate.py --replace <the STOPPED_AT_EXIT_0 append moved below the verdicts block> --tests "bin/test tests/skills/test_broad_gate.py -q -p no:xdist -k 'Test_failure_lines or Test_gate'"`
```

Why it matters: the phase record makes two decisions about the line.
*Decision: the new line comes directly after the check's first lines* puts
it above the heading and the file list. The condition `check.code == 0`
keeps it to an exit of 0. Neither is pinned.

Both mutants compiled and SURVIVED against every case of `Test_failure_lines`
and `Test_gate`. With the append moved below the verdicts block, the line
follows the file list, and nothing goes red. The only case with verdicts is
the exit-1 case at `:2256`. With `check.code != 1`, a suite at exit 2 or 3
with a stopped session, which an interrupt or an internal error gives, is
told "the row exited 0" under `exit 2`. Nothing goes red, because the only
case pinning the line's absence is that same exit-1 case.

The crafter's third batch removed `check.code == 0` outright and saw it red
(claimed in `trail/phases/phase-1.md`). That run watches exit 1, not the
other exits. Finding 1's wording also needs a case where an exit-0 suite
lists a file, and this one gives it. The case below passes at 7768896c and
turns both mutants red (executed, as a probe file in the clone with the same
two mutants).

```python
    def test_accepts_the_exit_0_line_above_the_files_and_at_no_other_exit(self):
        """#883: a test failed before the stop, so the suite at exit 0 lists a
        file; the line still comes directly under the check's first lines.
        At an exit other than 0 the line is never said."""
        record = a_record(sessions=1, counts={"failed": 1, "passed": 1}, unended=1)
        check = gate.Check(gate.SUITE, 0, "first\n", "/k/suite.txt")
        lines = gate.failure_lines(check, {"t/a.py": gate.NEW}, record)
        assert lines[:5] == [
            "exit 0",
            "first",
            STOPPED_AT_EXIT_0,
            gate.COMPARED_AT_BASE,
            "  t/a.py  new",
        ]
        for code in (2, 3, 4):
            check = gate.Check(gate.SUITE, code, "first\n", "/k/suite.txt")
            assert STOPPED_AT_EXIT_0 not in gate.failure_lines(check, None, record)
```

## Confirmations

```seal
confirms: none
```
What matched: the claim that `broad_gate.py#gate` fails the suite where
`head.unended` is not 0 whatever the exit. `broad_gate.py:3042` skips a
check only where `not check.failed and not (name == SUITE and
head.unended)`. A preflight never reaches `head.unended`, because
`checks[SUITE]` is set only under `if not args.preflight:` at `:3016`, so
`name == SUITE` is false for every preflight check (read). The claim that
`Check.failed` is unchanged also holds: it is `code != 0` at `:1203-1205`
(read).

```seal
confirms: none
```
What matched: the claim that the three new cases are red against the old
gate. With `skills/verify/scripts/broad_gate.py` checked out at 40e6c23e,
`Test_failure_lines::test_accepts_a_suite_that_exited_0_and_says_why_it_failed`
and both parametrizations of `Test_gate::test_refuses_a_suite_a_test_stopped_at_exit_0`
failed, and the old gate printed `suite   + 1 passed`. The file was restored
afterwards (executed).

```seal
confirms: none
```
What matched: the frame correction the phase record makes to *Scope* 1. A
suite that a test failed before an exit-0 stop runs `compare_at_base` for
the failing file through the existing path at `broad_gate.py:3055-3058`. The
probe of finding 1 printed `failing test files, compared at the base:` over
`tests/test_stop.py  new`, with the gate at exit 1 and no `trail/gate.md`
(executed). `gaps.md` *Not done* says this path is the existing one, and the
probe shows it working. Only the wording of finding 1 is wrong there.

```seal
confirms: none
```
What matched: the new arm is watched at the loop. A mutant turning
`head.unended` into `head.unended > 1` at `broad_gate.py:3042` went red, and
so did removing the `STOPPED_AT_EXIT_0` append from `failure_lines`
(executed, the #898 worktree's `seal mutate`). That licenses "tested", not
"safe".

```seal
confirms: none
```
What matched: the two modules the phase changed and pinned pass at
7768896c. `bin/test tests/skills/test_broad_gate.py
tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -q` gave 340
passed and 1 skipped (executed). The rule 3 pin at
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:530-534`
moved with the sentence at `templates/setup/config.md:366` (read).

```seal
confirms: none
```
What matched: the `skills/code-review/orchestration.md:384-387` sentence
and the changelog's `### Process changes` row are present and say the same
thing (read). The crafter's sweep of sentences stating when the gate passes
is labelled a sample by wording, as contract rule 12 asks. This round ran a
second search with other words over `docs/`, `skills/`, `agents/`,
`templates/`, `hooks/`, `README.md` and `CONTRIBUTING.md`: `BROAD GATE
PASSED`, `gate passes`, `exits 0`, `exited 0`, `exit 0`. It found nothing
the change makes false outside the places finding 1 names.
`docs/what-a-script-gates.md:43` still reads true: its Reads cell names the
recorder (read). `seal layout --pairs` names no pair for either new case
(executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether this repository's `Broad gate` row, `bin/test -q`, leaves a pytest session at `HEAD` stopped part-way, so the new arm fails this branch's own broad run (`frame/questions.md` Q1). The suite is labelled `unverified` in the hand-back, and that label is honest. | `seal/threads/1793599986-a-stopped-head-run-does-not-seal/gaps.md` | the orchestrator's broad run, `seal gate --base release/v0.28.1 --record` this work item |
| The new gate cases on Linux and Windows. This round ran them on macOS with pytest 9.2.0 only. | `tests/skills/test_broad_gate.py:2509-2538` | the pull request's CI test job |
| The phase record's phase-boundary counts, 3812 passed and 12 skipped over 77 modules and 1215 passed over 20 more. They are aggregates, and this round did not re-run them. | `seal/threads/1793599986-a-stopped-head-run-does-not-seal/trail/phases/phase-1.md` | the orchestrator's broad run |
| The `tryfirst` `pytest_sessionstart` instance of finding 2. It was read from pytest's `wrap_session` and not probed. | `skills/verify/scripts/pytest_record/agentic_pytest_record.py:271` | the fix pass, where it writes the limit or moves the session line |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_883_probe.py -q -p no:xdist --tb=short`: the gate over the fixture repository, with a failing test before a `pytest.exit('...', returncode=0)` and before an `os._exit(0)` | Both runs: gate exit 1, `suite    exit 0`, the `STOPPED_AT_EXIT_0` line, then `tests/test_stop.py  new` compared at the base, the unended count 1, and `1 failed, 1 passed`. No `trail/gate.md`. |
| `bin/test tests/skills/test_tmp_883_probe.py::test_tmp_a_stop_before_the_session_line -q -p no:xdist --tb=line`: the gate with a conftest calling `pytest.exit(..., returncode=0)` at import, then in `pytest_configure` | At import: pytest exit 4, gate exit 1, no record. In `pytest_configure`: pytest exit 0, gate exit 0, `BROAD GATE PASSED`, `trail/gate.md` written, `records/` empty. |
| `bin/test tests/skills/test_broad_gate.py -q -p no:xdist -k "stopped_at_exit_0 or exited_0_and_says_why or test_records_a_failing_suite or Test_failure_lines"` with `broad_gate.py` at 40e6c23e | 3 failed, 9 passed: the three new cases. |
| `bin/test tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -q` at 7768896c | 340 passed, 1 skipped. |
| The #898 worktree's `seal mutate` over `broad_gate.py` with three mutants, against `Test_failure_lines or Test_gate` | `head.unended > 1`: red. `check.code != 1`: SURVIVED. The `STOPPED_AT_EXIT_0` append removed: red. |
| The same `seal mutate` with the append moved below the verdicts block, against the same cases | SURVIVED. |
| The same `seal mutate` with both survivors, against a probe file holding finding 3's case | Baseline passed. Both mutants red. |
