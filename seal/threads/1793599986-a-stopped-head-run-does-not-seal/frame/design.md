# Design: a head run that pytest stopped with exit 0 does not seal (#883)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| G1 The defect, reproduced (executed, this frame). A scratch repository with a local `seal/` root, a `Broad gate` row that runs plain pytest, and `test_stop.py` holding `test_a` (passes), `test_b` (calls `pytest.exit("stopping here", returncode=0)`) and `test_c` (fails). The tree's gate at f667aca9, run from a `git clone --no-local` with `broad_gate.py --base main --root <repo>` | The gate exits 0 and prints `BROAD GATE PASSED` with `suite ✓ 2 passed`. `test_c` never ran. The recorder's `end` line reads `"exitstatus": 0` and `"stopped": [{"by": "exit", "what": "Exit: stopping here (returncode 0)"}]`. `broad_gate.read_record` over that record gives `sessions 1 unended 1`, and `suite_counts` gives `2 passed`. With `--record`, the same run would write `trail/gate.md`. |
| G2 A second stop at exit 0 that `stopped` does not show (executed, this frame). A test calling `os._exit(0)` under plain pytest, with the recorder loaded | pytest exits 0. The record holds no `end` line, so `stopped` is never written. `read_record` gives `unended 1` and `suite_counts` gives `1 passed`. A refusal that read `stopped` alone would pass this run. So the refusal reads `RunRecord.unended`, the gate's one count of a session that stopped part-way, which covers no `end` line, a `stopped` that is not an empty list, and an exit outside `RAN_TO_ITS_END`. |
| G3 Runs that finish are not refused (executed, this frame) | A one-test passing run and a `--collect-only` run each exit 0 with `"stopped": []` and give `unended 0`. This repository's own suite at the v0.28.0 tag also gave `unended 0` under `pytest tests/ -q -n auto` (executed: `gh release view v0.28.0`, whose note reads `SEALED v0.28.0 ... the suite at 6328 passed and 12 skipped`; read: `.github/scripts/release_seal.py#suite_counts` raises before giving counts where `record.unended` is not 0, and `.github/workflows/publish-release.yml` runs that step over the recorder's record). |
| G4 Why the gate passes today (read: `skills/verify/scripts/broad_gate.py#gate`, the failures loop and what follows it) | The loop skips every check whose `Check.failed` is false, and `Check.failed` is `code != 0`. `head.unended` reaches the output only through `failure_lines`, which runs for a failed check. After the loop, a run with no failures calls `write_gate_file` and prints `GATE_PASSED` with the panel, whose `suite` row prints `suite_counts(head)` behind a tick. |
| G5 `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A script holds a gate only on a fact it reads exactly: an exit code, a parser's result, or a line of the plugin's own forms in the one spelling the form gives it", and "A reading that is noisy or guessed from words is reported, never used to block" | The recorder's `end` line is a line of the plugin's own form, written by `skills/verify/scripts/pytest_record/agentic_pytest_record.py` and parsed by `json.loads`. Its `stopped` entries come from pytest's own `pytest_keyboard_interrupt` hook and the session's `shouldfail` and `shouldstop` flags, never from printed output. The absence of an `end` line is a fact of the file. So `unended` is an exact reading and may block. It is not noisy at exit 0: the one over-strictness named in `RAN_TO_ITS_END`'s comment needs `shouldfail`, which pytest sets only after a failure, and a failure exits 1. |
| G6 `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*, and `docs/the-broad-gate.md` *One act, one owner, and the owner is the orchestrator*: "The run judges nothing" | Whether a session ran to its end is not a question of meaning, so the gate answers it and the orchestrator waits on the exit code. The run still judges nothing: it reads a field and reports. Its heads stay `BROAD GATE PASSED` and `BROAD GATE FAILED` (#975). |
| G7 `skills/core/SKILL.md` *Judgment is not licence to skip a party*, the row "No seal without the broad run at HEAD", held by `agents/sealer.md` step 1 (read) | The sealer withholds without `trail/gate.md` at HEAD, and the gate writes that file only after a run with no failures (G4). So a failed suite check is enough to stop the seal. Nothing in the sealer or the chain check changes. |
| G8 #869, PR #880, work item 1791384158 (read at `v0.21.0`: `seal/specs/1791384158-the-broad-gate-reads-its-counts-from-the-recorder/overview.md` *Not done*, `rounds/round-1.md` finding 6, `rounds/round-1-fixes.md` *Deferred*) | #869 gave the recorder its `stopped` field and filed this issue from round 1's finding 6, reproduced there as "exit 0, `unended` 1, counts `1 passed`". Its overview left it out because "Closing it changes when the gate seals, which no scope item of this work names". This work item is that scope. It builds on the field as #869 wrote it and changes nothing in the recorder. |
| G9 #852 (closed by PR #880; read: `gh issue view 852`) and #849, PR #851 (read: the `read_record` comment and `UNENDED_AT_BASE`'s comment) | #852 settled that a stop is observed from pytest's own hooks and flags, never from output. #849 made a base session that stopped part-way turn `new` into `new?`: a measurement the gate cannot vouch for is never read as finished. This work applies the same count with the same meaning at `HEAD`. No departure. |
| G10 #975, PR #977 (read: commit f1c9932da) and the issue's comment of 2026-10-18 (executed: `gh issue view 883 --json body,comments`) | Since #975 the gate draws no stamp, so the issue's stamp half is legacy and out of scope. What stands is the gate's verdict. This work keeps #975's two heads and adds no verdict word. |
| G11 `.github/scripts/release_seal.py#suite_counts` (read) | The release seal already refuses a record whose `unended` is not 0, because "a `SEALED` above a red or a short suite would be false". The broad gate is the one reader at `HEAD` that still passes such a record. The release seal reads it after the merge and cannot stop one, so it stays as it is. |
| G12 `CONTRIBUTING.md` *What a change to a gate must carry* (read) | The pull request states: the gate blocks more; the wrong deny costs one more gate run once the stop is removed, and the wrong allow lets the sealer guarantee a suite nobody finished, which the sealer cannot see because it runs nothing broad. Prompt budget: no question to a person. Platform: the probes ran on macOS with pytest 9.2.0; #869 measured the `stopped` entries on pytest 6.1, 7.0 and 9.1 and under xdist (read: `RAN_TO_ITS_END`'s comment). Linux and Windows are not probed by this frame. What it reads: the recorder's `end` line through `read_record`, which already counts a line that does not parse in `unread`. |
| G13 `docs/what-a-script-gates.md` *The checks*, the row for `seal gate`'s `Broad gate` row and arm 3 (read) | Its Reads cell already names "the gate's pytest recorder", and its Agent cell says the orchestrator acts on what is reported. The row stays true and is not changed. |
| G14 `routing.md` (read): Planning framer, Automation yes; `seal/follow-up.md` (read): its table holds no row; the unsettled designs under `seal/threads/` (read: their `## Rule changes` `file:` lines) | No unsettled design changes `docs/the-broad-gate.md`. No follow-up row waits on this work. |

## Scope

In:

1. **The gate fails the suite where the row exited 0 and its record at `HEAD` counts a session that stopped part-way.** In `skills/verify/scripts/broad_gate.py#gate`, the suite check counts as failed where `head.unended` is not 0, whatever its exit. The run then exits 1 and prints the failure form under `BROAD GATE FAILED`, and writes no `trail/gate.md`. The base is not run, because the record holds no failing file to compare (`compare_at_base` runs only for failing files). A preflight runs no row and is not affected.
2. **The failure form says why a suite that exited 0 failed.** In `failure_lines`, where the check is the suite and its exit is 0, one new line comes after `exit 0` and the first lines, ahead of `UNENDED_HERE`. It says that the row exited 0, that the gate fails the suite all the same because a pytest session it ran stopped part-way, and that a stop which chooses the exit code says neither that the session ran every test it collected nor that nothing it ran failed. `UNENDED_HERE` follows with the count, as on any failing suite. The new line is a module constant, pinned by a case (contract rule 14).
3. **Every sentence that states when the gate passes is rewritten in place, with its pin** (contract rule 19). The list, made by `git grep` on `BROAD GATE PASSED`, `unended`, `UNENDED_HERE` and `part-way` outside `tests/` and `seal/threads/`: the module docstring of `broad_gate.py` where it says what a run that passes and one that fails print; `failure_lines`' docstring paragraph on `record.unended`; the comment in `gate`'s failures loop; `templates/setup/config.md` *The criterion for choosing a value*, rule 3, the sentence "The gate also says there how many sessions at `HEAD` stopped part-way, because the test such a session stopped in may be in no list.", which gains that a run whose row exited 0 fails where one did; and `skills/code-review/orchestration.md`, the paragraph opening "On the broad run's exit 1 spawn nothing", which gains one sentence for a failing suite that names no file: the session stopped part-way, `records/` in the kept output says what stopped it, and a stop the branch added is this work's to repair. The pin of rule 3's sentence in `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` moves with it. The list is a sample by wording (contract rule 12): the build runs the same `git grep` at its own HEAD and names what it found.
4. **The rule is stated for the settle** in `## Rule changes` below.

Out:

- **The stamp half of the issue.** Since #975 the gate draws no stamp (G10).
- **Naming what stopped the session, or the test it stopped in, in the failure form.** `records/` in the kept output holds each `stopped` entry, and `UNENDED_HERE` already points there. The test a session stopped in would be read off the order of the record's lines, and under xdist that order is not the order the tests ran in, so the name would be a guess.
- **Running the row at the base to say whether the base stops too.** The verdict is the same either way: the gate fails a suite with a failure the base shares as well. It would cost one more full run. Where the orchestrator needs the answer, `skills/verify/orchestration.md` already says to run at the base in a `git worktree add`.
- **`unread` and `unplaced` at exit 0.** Neither says that a test went unrun. A cut `end` line leaves no `end` line, which `unended` counts already.
- **The stops no record shows.** A `pytest.exit()` raised by a `pytest_sessionfinish` hook that runs after the recorder's is raised after the `end` line was written. A stop raised before the recorder writes its `session` line, such as a `pytest.exit()` in a conftest's `pytest_configure`, leaves no record. Both stay the limits `RAN_TO_ITS_END`'s comment and the recorder's docstring name.
- **The recorder, `RAN_TO_ITS_END`, the base's words, the panel's layout and `.github/scripts/release_seal.py`.** None changes.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A test calls `pytest.exit()` with return code 0 | Given the fixture repository of `tests/skills/test_broad_gate.py` with a `feature` commit adding a test that calls `pytest.exit("...", returncode=0)` before a later test. When the gate runs with `--record`. Then it exits 1, stdout opens `BROAD GATE FAILED`, the suite's lines hold `exit 0`, the new line of Scope 2 and `UNENDED_HERE` with count 1, and no `trail/gate.md` is written. | A new case in `tests/skills/test_broad_gate.py` over the fixture repository, seen red at 40e6c23e, where the gate prints `BROAD GATE PASSED` (G1). |
| S2 A test ends its process with `os._exit(0)` | Given the same repository with a test calling `os._exit(0)`. When the gate runs. Then the same as S1: the record holds no `end` line and still fails the suite. | The case of S1, parametrized over the two stops, seen red the same way (G2). |
| S3 A run that finishes still passes | Given a suite whose sessions all wrote an `end` line with `"stopped": []` and an exit in `RAN_TO_ITS_END`. When the gate runs at exit 0. Then it prints `BROAD GATE PASSED` and writes `trail/gate.md` as before. | The existing cases over the `a_recorded_run` fixture in `tests/skills/test_broad_gate.py`, unchanged and green. |
| S4 A failing suite with a stopped session reads as before | Given a suite that exits 1 and whose record counts a stopped session. Then its lines are those of today, without the Scope 2 line. | `tests/skills/test_broad_gate.py` *Test_failure_lines*, the case at `:2250`, plus a unit case that the Scope 2 line appears for exit 0 alone. |
| S5 The rule is in force | `docs/the-broad-gate.md` gains the rule at the settle. | `check: tests/skills/test_broad_gate.py`, the line on the rule below. |

## Data & interfaces

No schema changes. The recorder's lines and `RunRecord`'s fields stay as they are. `RunRecord.unended` gains one reader, at `broad_gate.py#gate`. `broad_gate.py` gains one string constant, the line of Scope 2. The gate's exit codes keep their meaning: 0 passed, 1 a check failed, 2 nothing ran. The `Check` class may keep `failed` as `code != 0`, with the suite's record read where the loop decides, or carry the record's verdict itself. The build chooses, and its phase record says which.

## Rule changes

- add
  file: docs/the-broad-gate.md
  section: One act, one owner, and the owner is the orchestrator
  to: **A suite whose record says a pytest session at `HEAD` stopped
    part-way has not passed, whatever the row's exit.** An exit of 0 does
    not say that the session ran every test it collected, and where a stop
    chose that code, as `pytest.exit()` and `os._exit()` do, it does not say
    that nothing the session ran failed either. A test that calls `pytest.exit()` with a
    return code of 0, or ends its process with `os._exit(0)`, stops the
    session there with the row still at exit 0. A run passed on that exit
    would write `trail/gate.md`, and the sealer would guarantee a suite
    nobody finished. So the gate reads the stop off its own recorder's
    record, as it does at the base. It counts a session as stopped part-way
    where its record holds no `end` line, where that line's `stopped` is not
    an empty list, or where its exit is not 0, 1 or 5. Where any session at `HEAD`
    reads so, the run fails, writes no `trail/gate.md`, and its failure form
    says that the row exited 0 and how many sessions stopped. Two kinds of
    stop stay out of the record's reach. A `pytest.exit()` raised by a
    `pytest_sessionfinish` hook that runs after the recorder's comes after
    the session's `end` line, so the session reads as one that ran to its
    end. A stop raised before the recorder writes a session's first line,
    such as a `pytest.exit()` in a conftest's `pytest_configure`, leaves no
    record, so the run reads as one that started no pytest and is judged on
    its exit alone.
    check: tests/skills/test_broad_gate.py

## Removes

- nothing
  why: The work adds one refusal to an existing gate arm and removes nothing, because nothing in the tree reads a stopped session at `HEAD` on a run that exits 0. `UNENDED_HERE` stays: a suite that fails at a non-zero exit still needs its count. `.github/scripts/release_seal.py`'s refusal stays: it reads the suite at the tag after the merge and stops no pull request. The catch record for the refusal is #869 round 1's finding 6, reproduced there, and G1 and G2 of this frame, reproduced again at f667aca9.

Framed 2026-11-02 by framer, before the build.
