# Design: a red session a late hook hides does not pass (#1301)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| G1 The defect, reproduced in six shapes (executed, this frame). Each shape is a scratch repository with a committed `seal/` root and a `Broad gate` row that runs `python -m pytest -q -p no:cacheprovider tests` on the interpreter of this repository's `.venv` (pytest 9.1.1, Python 3.13.9, macOS). `base` holds one passing test, and `feature` adds the shape. The gate is `skills/verify/scripts/broad_gate.py` at e44c9b07, run from a `git clone --no-local` in the framer's scratch directory as `broad_gate.py --base base --root <repo> --keep-output <dir>` | Every shape makes the gate exit 0 and print `BROAD GATE PASSED`, and none of the six counts a session as stopped. The first five print `suite ✓ 1 failed · 1 passed`, and in each the one head session's `end` line reads `"exitstatus": 1` with `"stopped": []`. Those five, each after a failing test: a conftest `pytest_sessionfinish` marked `trylast` that calls `pytest.exit('late', returncode=0)`, the issue's own case; a plain conftest `pytest_sessionfinish` that sets `session.exitstatus = 0`; the same hook marked `tryfirst`; a conftest `pytest_unconfigure` that calls `os._exit(0)`; and a row ending `; true`. The sixth shape is a row that runs pytest twice, joined by an escaped `\|\|`, over a test that fails on its first run only. It prints `suite ✓ 1 failed · 3 passed`, and its two head sessions' `end` lines read exit 1 and exit 0. |
| G2 The `end` line's exit is the run loop's, whatever runs after it (executed: G1's `tryfirst` and plain shapes; read: `wrap_session` in pytest's own `_pytest/main.py`, as the `.venv`'s pytest 9.1.1 holds it) | `wrap_session` calls `config.hook.pytest_sessionfinish(session=session, exitstatus=session.exitstatus)` once, so every hook is handed the same value. A hook that sets `session.exitstatus` before the recorder's runs still leaves the recorder's `exitstatus` argument at 1, which G1's `tryfirst` shape shows. `wrap_session` then returns `session.exitstatus`, which a hook's assignment or a raised `Exit` has changed. A hook ordered before the recorder's that raises stops the hook call before the recorder writes, so that session has no `end` line, and the gate already counts that as a stop. So the `end` line holds the exit pytest's run loop gave, and nothing after the loop changes it. |
| G3 A late act after a green session hides nothing (executed, this frame, the G1 setup with the `trylast` hook and no failing test) | The gate passes with `suite ✓ 1 passed`, and the `end` line reads exit 0. A `pytest_sessionfinish` hook runs after the run loop and cannot skip a test, so a late hook is no stop. It can only choose the row's exit. Reading the pass off the `end` line refuses nothing here. |
| G4 Why the gate passes today (read: `skills/verify/scripts/broad_gate.py#gate`, the failures loop, and `broad_gate.py#read_record`) | The loop fails the suite where its exit is not 0 or where `head.unended` is not 0. `read_record` adds to `unended` where a session has no `end` line, where `stopped` is not `[]`, or where `exitstatus` is not in `RAN_TO_ITS_END`, which is `(0, 1, 5)`. An `end` line with exit 1 and `stopped` `[]` adds nothing, so a red session is decided on the row's exit. |
| G5 `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A script holds a gate only on a fact it reads exactly: an exit code, a parser's result, or a line of the plugin's own forms in the one spelling the form gives it" | The `end` line is a line of the plugin's own form. `skills/verify/scripts/pytest_record/agentic_pytest_record.py#Recorder` writes it, and `json.loads` parses it. Its `exitstatus` is the integer pytest handed the hook (G2), never a word read off printed output. So the reading is exact and may block. |
| G6 `skills/core/SKILL.md` *The rule a mechanism is kept against*, the weighing the issue's *Done when* asks for: "A mechanism stays only while its record of what it caught outweighs what it costs" | What it caught: #883's round 3 probe, and the six shapes of G1 reproduced at e44c9b07. In each, the gate's own suite row printed `✓` beside `1 failed`, and with `--record` it would have written `trail/gate.md`, which the sealer guarantees a tree on (G8). What it costs: no new run, since `read_record` already reads every `end` line; no question to a person; one count and one condition in an existing arm; and one rewritten line in the failure form. It also removes text: the late-hook limit leaves five places (*Removes*). Its wrong deny falls on a row that masks a red pytest or runs it again over a failure, as G1's last two shapes do. `templates/setup/config.md` *The criterion for choosing a value*, rule 1, already says a red check does not belong in the row. Verdict: build it. |
| G7 #883 (0.29.0), its frame (read at `v0.29.0`: `seal/threads/1793599986-a-stopped-head-run-does-not-seal/frame/design.md`, G4, G5 and *Scope* *Out*) | #883 made a session at `HEAD` that stopped part-way fail the suite whatever the row's exit. It named the late hook as a stop the record cannot see. This work stands on #883's rule and widens it from "stopped" to "did not pass". It departs from #883 on one point, with G2 and G3 as grounds: the late hook is no stop, and its exit is out of the `end` line's reach, not out of the record's. |
| G8 #883 round 3 (read at `v0.29.0`: `trail/rounds/round-3.md` *Not judged*, the second row) and `skills/core/SKILL.md` *Judgment is not licence to skip a party*, the row "No seal without the broad run at HEAD" | Round 3 executed the issue's case and left to the owner whether it became an issue, and #1301 is that issue. The sealer withholds without `trail/gate.md` at `HEAD`, and the gate writes it only after a run with no failures. So failing the suite is enough to stop the seal. Nothing in the sealer or the chain check changes. |
| G9 The class of readers that decide a suite passed, enumerated by construction (executed: `git grep -n 'read_record('` outside `tests/` and `seal/threads/`) | `broad_gate.read_record` has three callers. `broad_gate.py#gate` reads `HEAD` and decides the pass, so it is this work's. `broad_gate.py#compare_at_base` reads the base for words, not for a pass: a red base session's failing lines read `failing on base too` whatever its row's exit, so it is unchanged. `.github/scripts/release_seal.py#suite_counts` already raises where the counts hold a `failed` or an `error`, where `unended` or `unplaced` is not 0, or where a line did not parse (read). So the release seal already reads the pass off the record, and the broad gate at `HEAD` is the one reader left that decides it on the row's exit. |
| G10 `templates/setup/config.md` *Everything else stays legal* (read: the `;` row and the pipe row) and *The criterion for choosing a value*, rule 3 (read) | The `;` row says the row "answers with whatever the composition the repository wrote answers with". The pipe row says `bin/test -q \| tee out.txt` "is green whenever `tee` is". Rule 3 names the late hook as a stop out of the record's reach. Each stands on the old fact and is rewritten in place (*Scope* 4). |
| G11 `docs/running/the-broad-gate.md` *One act, one owner, and the owner is the orchestrator*, the paragraph opening "A suite whose record says a pytest session at `HEAD` stopped part-way has not passed" (read); the unsettled designs (executed: `grep -n -A2 'file: docs/running/the-broad-gate.md' seal/threads/*/frame/design.md`, no line) | That paragraph is the rule in force, and no unsettled design changes the document. This work's subject is the code, so the rule goes to the settle in `## Rule changes` (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). |
| G12 This repository's own row (read: `seal/config.md`, `bin/test`, `.github/scripts/run_tests.py#main`; executed: `git grep -n -i sessionfinish` at e44c9b07, no hit under `tests/`; the build's cases and pins add hits there, and `tests/conftest.py` still holds no such hook) | The row runs `uvx ruff check .`, `uvx ruff format --check .` and `bin/test -q` joined by `&&`. The runner starts one pytest, and no conftest of the suite holds a `pytest_sessionfinish` hook. So the repository's own gate reads a green suite as it does today. |
| G13 `routing.md` (read): Planning framer, Implementation crafter, Automation yes. `seal/follow-up.md` (read): no row waits on this work. The latest GitHub Release, v0.32.0 (executed: `gh release view --json body`): its body has no `### Process changes` heading. The fragments' `### Process changes` rows under `seal/threads/` (read): none changes the gate's verdict | Nothing upstream of the frame moves the scope. The ticket was read as `gh issue view 1301 --json body,comments` gave it on 2026-11-05: one body and no comments. |
| G14 `CONTRIBUTING.md` *What a change to a gate must carry* (read) | The pull request states that the gate blocks more. A wrong deny costs one more gate run once the row is rewritten or the failure is fixed. A wrong allow lets the sealer guarantee a red suite, which it cannot see, because it runs nothing broad. The prompt budget is no question. The platform is macOS with pytest 9.1.1 (G1); Linux and Windows are not probed by this frame. |

## Scope

In:

1. **`read_record` counts the sessions at `HEAD` that did not pass.** A keyed session passed where its record holds an `end` line whose `stopped` is `[]` and whose `exitstatus` is 0 or 5. Every other keyed session adds one to a new `RunRecord` count. That count holds every session `unended` counts, and every session whose `end` line reads exit 1 with `stopped` `[]`. `unended` stays as it is, because the base's words and `UNENDED_HERE` read it (`broad_gate.py#base_word`).
2. **The gate fails the suite where that count is not 0, whatever the row's exit.** In `broad_gate.py#gate`'s failures loop, the count of *Scope* 1 replaces `head.unended` in the condition. A suite that fails this way at exit 0 with a red session holds its failing files in the record, so the base is run for them as on any failing suite. No `trail/gate.md` is written, and the run exits 1 under `BROAD GATE FAILED`. A preflight runs no row and is not affected.
3. **The failure form's exit-0 line names both causes.** `STOPPED_AT_EXIT_0` is rewritten in place, and renamed where its name no longer fits, into one line. That line says that the row exited 0 and that the gate fails the suite all the same, because a pytest session it ran did not pass by its own record. The session either stopped part-way, where the stop itself chose the code, or ended with exit 1 while something after pytest's run loop chose the row's exit: a later hook, or a part of the row. The line is printed where the suite's exit is 0 and the count of *Scope* 1 is not 0, in the place it holds today. Its pin in `tests/skills/test_broad_gate.py` moves with it (contract rule 14).
4. **Every sentence that states the old fact is rewritten in place, with its pin** (contract rule 19). The list was made by `git grep` on `sessionfinish`, `part-way`, `whatever the row`, `own claim about itself` and `STOPPED_AT_EXIT_0` outside `tests/` and `seal/threads/`. It covers the following:
   - `broad_gate.py`'s module docstring, where it says when a run fails.
   - `RAN_TO_ITS_END`'s comment, where it names the late hook among the stops that show in neither field.
   - `failure_lines`' docstring paragraph on `record.unended`.
   - The comment in `gate`'s failures loop.
   - `RunRecord`'s and `read_record`'s docstrings.
   - The recorder's module docstring, where it names the late hook (`agentic_pytest_record.py`, the paragraph opening "The last two are read off the session").
   - `templates/setup/config.md` rule 3: the sentence "Where one did, the suite fails even where the row exited 0" widens to a session that ended with exit 1, and the late-hook stop leaves "Two stops are out of the record's reach".
   - `templates/setup/config.md` *Everything else stays legal*: the `;` row and the pipe row gain the clause that a pytest session the row runs that did not pass by its record fails the suite whatever the composition exits, citing rule 3. The `tee` example's "is green whenever `tee` is" is corrected.
   - The pins of rule 3's sentences in `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`.

   The list is a sample by wording (contract rule 12). The build runs the same `git grep` at its own `HEAD` and names what it found. `skills/code-review/orchestration.md`, at the paragraph opening "On the broad run's exit 1 spawn nothing", and `skills/verify/orchestration.md` *What the comparison says* were read and stay true: the first speaks of a suite that names no file, and the second of the base.
5. **The rule is stated for the settle** in `## Rule changes` below.

Out:

- **The recorder's behaviour.** It keeps writing the `exitstatus` its `pytest_sessionfinish` is handed. Writing after every other hook instead would write an exit a hook chose (plan *Alternatives considered*, the fourth row).
- **The release seal.** It already refuses a red record (G9).
- **The base's words.** A red base session is read as `failing on base too` whatever its row's exit (G9).
- **A stop raised before the recorder writes a session's first line.** It leaves no record, stays a limit, and is still named in rule 3, `RAN_TO_ITS_END`'s comment and the recorder's docstring.
- **A hook ordered before the recorder's that raises in `pytest_sessionfinish`.** That session has no `end` line, and the gate counts it as stopped today. This work leaves that unchanged, and this frame did not probe it.
- **Naming the hook or the part of the row that chose the exit.** `records/` and `suite.txt` in the kept output hold what the reader needs, and the gate cannot tell a hook from the row's composition by reading an exact fact.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A late hook turns a red session's exit into 0 | Given the fixture repository of `tests/skills/test_broad_gate.py` with a `feature` commit adding a failing test and a conftest `pytest_sessionfinish` marked `trylast` that calls `pytest.exit(..., returncode=0)`. When the gate runs with `--record`. Then it exits 1, stdout opens `BROAD GATE FAILED`, the suite's lines hold `exit 0`, the line of *Scope* 3, the failing file with its base word, and the counts, and no `trail/gate.md` is written. | A new case in `tests/skills/test_broad_gate.py`, seen red at e44c9b07, where the gate prints `BROAD GATE PASSED` (G1). |
| S2 The other acts after the run loop | Given the same repository with the conftest replaced by one that sets `session.exitstatus = 0` in a `tryfirst` `pytest_sessionfinish`, or by one whose `pytest_unconfigure` calls `os._exit(0)`, or with a row that joins its pytest to a command exiting 0 by an escaped `\|\|` over the failing test, a spelling `/bin/sh` and `cmd.exe` read alike (`trail/phases/phase-1.md`). When the gate runs. Then the same as S1. | The case of S1, parametrized over at least these shapes, each seen red the same way (G1). |
| S3 A late hook after a green session still passes | Given the S1 conftest and no failing test. When the gate runs with `--record`. Then it prints `BROAD GATE PASSED` and writes `trail/gate.md`. | A case in `tests/skills/test_broad_gate.py` (G3). It is green before and after the change, and so pins the absence of a wrong deny. It is not a seen-red case. |
| S4 A stopped session at exit 0 reads as before | Given #883's two stops at exit 0. When the gate runs. Then it fails with the rewritten line of *Scope* 3 and `UNENDED_HERE` with count 1, and runs nothing at the base. | `tests/skills/test_broad_gate.py#test_refuses_a_suite_a_test_stopped_at_exit_0` and the `failure_lines` cases of #883, with the pinned line rewritten. |
| S5 The count reads each `end` line | Given keyed records whose `end` lines read exit 0, exit 5, exit 1 with `stopped` `[]`, and exit 0 with a `stopped` entry. When `read_record` reads them. Then exits 0 and 5 add nothing to the count of *Scope* 1, and the other two add one each, while `unended` counts only the last. | A unit case on `read_record` in `tests/skills/test_broad_gate.py`, seen red with the count removed. |
| S6 The text no longer states the late hook as a limit | `templates/setup/config.md` rule 3 and the two composition rows read as *Scope* 4 says. | `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` with its pins moved, seen red against the old sentence. |
| S7 The rule is in force | `docs/running/the-broad-gate.md` gains the rewritten rule at the settle. | The rule's `check:` line, `tests/skills/test_broad_gate.py`. |

## Data & interfaces

No schema change. The recorder's lines are unchanged. `RunRecord` gains one integer field, the count of *Scope* 1, with its name and docstring chosen by the build. `RunRecord.unended` is unchanged. `broad_gate.py#gate` reads the new field where it read `head.unended`. `failure_lines` prints the rewritten line on the new field at exit 0. `UNENDED_HERE` stays keyed on `unended`. The gate's exit codes keep their meaning: 0 passed, 1 a check failed, and 2 nothing ran.

## Rule changes

- change
  file: docs/running/the-broad-gate.md
  section: One act, one owner, and the owner is the orchestrator
  from: **A suite whose record says a pytest session at `HEAD` stopped
    part-way has not passed, whatever the row's exit.** An exit of 0 does
    not say that the session ran every test it collected, and where a stop
    chose that code, as `pytest.exit()` and `os._exit()` do, it does not say
    that nothing the session ran failed either. A test that calls
    `pytest.exit()` with a return code of 0, or ends its process with
    `os._exit(0)`, stops the session there with the row still at exit 0. A
    run passed on that exit would write `trail/gate.md`, and the sealer
    would guarantee a suite nobody finished. So the gate reads the stop off
    its own recorder's record, as it does at the base. It counts a session
    as stopped part-way where its record holds no `end` line, where that
    line's `stopped` is not an empty list, or where its exit is not 0, 1
    or 5. Where any session at `HEAD` reads so, the run fails, writes no
    `trail/gate.md`, and its failure form says that the row exited 0 and how
    many sessions stopped. Two kinds of
    stop stay out of the record's reach: a `pytest.exit()` raised by a
    `pytest_sessionfinish` hook that runs after the recorder's, and a stop
    raised before the recorder writes a session's first line.
    `templates/setup/config.md` *The criterion for choosing a value*, rule
    3, says how the gate reads a run with each.
  to: **A suite whose record says a pytest session at `HEAD` did not pass
    has not passed, whatever the row's exit.** A session passed where its
    record holds an `end` line whose `stopped` is an empty list and whose
    exit is 0 or 5. That exit is the one pytest's run loop gave, and what
    runs after the loop can change the row's exit and not that one. So an
    exit of 0 from the row does not say that nothing the session ran
    failed. Where a stop chose that code, as a test that calls
    `pytest.exit()` with a return code of 0 or `os._exit(0)` does, it does
    not say that the session ran every test it collected either. A run
    passed on that exit would write `trail/gate.md`, and the sealer would
    guarantee a suite that failed or that nobody finished. So the gate
    reads the pass off its own recorder's record. It counts a session as
    stopped part-way where its record holds no `end` line, where that
    line's `stopped` is not an empty list, or where its exit is not 0, 1
    or 5, as it does at the base. It counts a session as red where that
    line's `stopped` is an empty list and its exit is 1. Where any session
    at `HEAD` reads either way, the run fails and writes no
    `trail/gate.md`. Where the row exited 0, its failure form says so
    first, and the failing files and the count of sessions that stopped
    follow as on any failing suite. One kind of stop stays out of the
    record's reach: a stop raised before the recorder writes a session's
    first line. `templates/setup/config.md` *The criterion for choosing a
    value*, rule 3, names the acts after the run loop that can turn the
    row's exit into 0, and says how the gate reads a run with that stop.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The late hook named as a stop out of the record's reach | `docs/running/the-broad-gate.md` *One act, one owner, and the owner is the orchestrator*, through `## Rule changes` | The late hook is no stop, and its exit cannot hide a red session from the `end` line (G2, G3). The configure-time stop stays as the one limit. |
| The same sentence | `templates/setup/config.md` *The criterion for choosing a value*, rule 3, "A `pytest.exit()` raised by a `pytest_sessionfinish` hook that runs after the recorder's comes after the session's `end` line" | The same grounds. Rule 3's sentence on a session that stopped part-way, widened by *Scope* 4, now owns what the gate does with such a session. |
| The same sentence | `skills/verify/scripts/broad_gate.py#RAN_TO_ITS_END`, its comment, "Two kinds of stop show in neither" | The same grounds. The comment keeps the configure-time stop. |
| The same sentence | `skills/verify/scripts/pytest_record/agentic_pytest_record.py`, the module docstring, "Two kinds of stop show in neither" | The same grounds. The docstring keeps the configure-time stop. |
| The pin of that sentence | `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, the pinned sentence opening "Two stops are out of the record's reach" | It pins a sentence that leaves rule 3. The pin of the rewritten sentence takes its place. |
| "is green whenever `tee` is" | `templates/setup/config.md` *Everything else stays legal*, the pipe row | It is false once a red pytest session under the pipe fails the suite. The rewritten row and rule 3 own the fact. |
| `head.unended` as the failures loop's condition | `skills/verify/scripts/broad_gate.py#gate` | The count of *Scope* 1 replaces it and holds every session `unended` counts. `unended` keeps its other readers. |

The mechanism this work widens is the suite arm's refusal. What it takes out in return is the late-hook limit in the five places above. Its catch record is #883's round 3 probe (G8) and G1's six shapes at e44c9b07.

Framed 2026-11-05 by framer, before the build.
