# Review round 1: 1793829111-a-red-session-a-late-hook-hides-does-not-pass

```seal
target: b5d3d85 against release/v0.32.1
```

This round reviewed the branch at b5d3d85 against `release/v0.32.1` (3b2190c4): the build commit b6775862, the records 91f46922 and 54177d4d, and the frame fold b5d3d85. It is round 1, so no earlier round hands it a coordinate. `seal/parity.md` is not declared, so no parity comparison applies.

Facts carried rather than re-established. G1's six shapes at e44c9b07 are the framer's executed runs, and this round did not run them again. The handover says an xdist worker registers no `Recorder`. This round opened that comment at `skills/verify/scripts/pytest_record/agentic_pytest_record.py:178-180` and the claim of the key at `agentic_pytest_record.py:398-406`, and carried the rest of the recorder's xdist behaviour from #825.

Facts re-derived. G2 holds: `.venv/lib/python3.13/site-packages/_pytest/main.py:365-371` calls `pytest_sessionfinish` once with `exitstatus=session.exitstatus` and then returns `session.exitstatus`, which a hook may have changed. The recorder writes the hook's argument, `int(exitstatus)`, at `agentic_pytest_record.py:381-388`, never `session.exitstatus`. So the `end` line holds the run loop's exit.

The handover asked whether anything in the diff changes the one keyed session per row in this repository. Nothing does. The diff touches neither `.github/scripts/run_tests.py`, whose one pytest call is at `run_tests.py:604-607`, nor the recorder's registration, nor `tests/conftest.py`. The new cases write their conftests into the fixture repositories they build, and each inner gate run gets its own key from `skills/verify/scripts/broad_gate.py:1621-1643`.

## Findings

### 1. The rule change's `to` keeps a second copy of rule 3's list of acts after the run loop

```seal
severity: should
location: `seal/threads/1793829111-a-red-session-a-late-hook-hides-does-not-pass/frame/design.md:93-119`, `templates/setup/config.md:371`
evidence: read `seal/threads/1793829111-a-red-session-a-late-hook-hides-does-not-pass/frame/design.md:93-119`, `templates/setup/config.md:371`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:467-470`
```

Why it matters: after the settle, the `to` paragraph and rule 3 would each state the same list of acts that turn the row's exit into 0. They would also each state the reason the `end` line survives those acts. The `to` says "A later `pytest_sessionfinish` hook can raise `pytest.exit()` or set the session's exit status, a `pytest_unconfigure` hook can end the process, and a part of the row after pytest, such as `; true` or a pipe, can exit for it" (`design.md:99-102`). Rule 3 at HEAD says "Such an act is a hook that sets the session's exit status, a later `pytest_sessionfinish` hook that raises `pytest.exit()`, a `pytest_unconfigure` hook that ends the process, or a part of the row after pytest, such as `; true` or a pipe" (`templates/setup/config.md:371`). The pin's docstring calls rule 3 "the one home of how the gate measures a row ... and which rows it cannot measure" (`test_the_seal_is_taken_once_by_the_sealer.py:467-470`). `skills/core/SKILL.md` *The rule a mechanism is kept against* says a fact has one source and every other place links to it. The next change to the list would have to find both homes, and only rule 3's copy is pinned. The `to` already cites rule 3 for the configure-time stop. It can cite rule 3 for the acts too, and keep only the rule, the reason in one clause, and the counts it decides on. The chain check printed no notice at `design.md`, so this finding comes from reading, not from a notice.

The fix replaces the whole `to:` item. It touches no other statement: the `from:` text stays the document's current paragraph, which the round matched after normalising whitespace.

```markdown
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
```

```seal
verdict: fixed c9a1b1bf
answer: The orchestrator replaced the whole `to:` item of `frame/design.md` `## Rule changes` with the paste-ready text at c9a1b1bf, so the list of acts after the run loop and the reason the `end` line survives them now stand in rule 3 alone. The crafter read the claim the new `to:` sends a reader to against `templates/setup/config.md` rule 3 at HEAD, and it holds. Rule 3 names the four acts ("Such an act is a hook that sets the session's exit status, a later `pytest_sessionfinish` hook that raises `pytest.exit()`, a `pytest_unconfigure` hook that ends the process, or a part of the row after pytest, such as `; true` or a pipe"). It also says how the gate reads a run with the configure-time stop ("so the gate reads the run as though that session never started: it judges the run on the row's exit and on the records the row's other sessions left"). So rule 3 needs no change. The sweep read `gaps.md`, `changelog.md` and `trail/phases/phase-1.md` whole. The changelog fragment names G1's reproduced shapes as the defect's instances; it states what was measured, holds no rule, and stays.
```

### 2. The plan and the questions name cases that cannot turn red on the scenario they are named for

```seal
severity: should
location: `seal/threads/1793829111-a-red-session-a-late-hook-hides-does-not-pass/frame/plan.md:16`, `seal/threads/1793829111-a-red-session-a-late-hook-hides-does-not-pass/frame/questions.md:11`, `seal/threads/1793829111-a-red-session-a-late-hook-hides-does-not-pass/frame/questions.md:15`
evidence: read `tests/skills/test_broad_gate.py:1561-1573`, `tests/skills/test_broad_gate.py:135-141`, `tests/skills/test_broad_gate.py:2493-2511`, `skills/verify/scripts/pytest_record/agentic_pytest_record.py:381-388`, `seal/threads/1793829111-a-red-session-a-late-hook-hides-does-not-pass/trail/phases/phase-1.md:11-13`
```

Why it matters: the plan's second failure scenario is a pytest release that hands `pytest_sessionfinish` a value other than the run loop's exit. Of that scenario the plan says "the cases of S1 and S5 are what turn red on it" (`plan.md:16`). `questions.md:11` says a different answer on another build "would turn the cases of S1 and S5 red there". At HEAD neither case can do that. S5's case, `test_refuses_to_call_a_session_that_ended_with_exit_1_passed` (`tests/skills/test_broad_gate.py:1561-1573`), writes its `end` lines by hand through `end()` (`test_broad_gate.py:135-141`) and starts no pytest. S1's shape, `late-pytest-exit-0` (`test_broad_gate.py:2494-2499`), is a `trylast` hook that raises after the recorder has written its line, so the recorder reads 1 whatever the release hands later hooks. The case that turns red is S2's `early-exitstatus-0` shape (`test_broad_gate.py:2500-2504`), because its `tryfirst` hook sets the session's exit status before the recorder's hook runs. The phase record says so at `phase-1.md:13`, and the fold at b5d3d85 left the two frame sentences as they were. A reader who meets that release, or the settle weighing which case guards the assumption, is pointed at two cases that stay green. The same fold left Q1's question cell saying "on Windows the S2 row's `; true` reaches `cmd.exe`" (`questions.md:15`), while S2 and the case now spell that shape as `||` and the interpreter (`design.md:57`, `test_broad_gate.py:2510`).

How the list was made: this round read the three frame files whole and checked each sentence that names a case or a shape against HEAD. These three are the ones HEAD contradicts. The list covers a closed set, so it is complete.

`frame/plan.md:16`, the last sentence, becomes:

```markdown
The recorder's `exitstatus` would then read what that release handed, and the `early-exitstatus-0` shape of S2 is the case that turns red on it, because its hook sets the session's exit status before the recorder's runs. S1's hook raises after the recorder wrote, and S5's case writes its records by hand, so neither meets that release.
```

`frame/questions.md:11`, the second sentence, becomes:

```markdown
A different answer on another build would turn the `early-exitstatus-0` shape of S2 red there, and it would not change what gets built.
```

`frame/questions.md:15`, the second sentence of Q1's question cell, becomes:

```markdown
Each case starts a pytest subprocess whose conftest holds a hook, or whose row joins pytest to the interpreter by an escaped `\|\|`, which reaches `cmd.exe` on Windows.
```

```seal
verdict: fixed c9a1b1bf
answer: The orchestrator applied the three paste-ready sentences at c9a1b1bf: `frame/plan.md`'s second failure scenario and `frame/questions.md`'s assumption sentence now name the `early-exitstatus-0` shape of S2, and Q1's question cell names the escaped `\|\|` row. The crafter read each against `tests/skills/test_broad_gate.py` `LATE_ACTS` at HEAD, and they hold. The sweep over the records the crafter writes found two more statements of the old frame state, and commit 9a5386d6 corrected both. `trail/phases/phase-1.md` said in the present tense that S2 names a row ending `; true` and that the frame's *Scope* 3 sentence reads as at e06313c5. It now names e06313c5 and the fold at b5d3d855, and records that CI run 41924200504 ran the case on every leg. `gaps.md`'s row on the ubuntu and Windows legs is closed with that run as its answer: every job ended `success`, and no new case is skipped in its log. Neither record names S1 or S5 as the cases a different pytest `exitstatus` turns red.
```

## Confirmations

What matched: *Scope* 1 holds. `read_record` adds one to `unpassed` for every session it counts as stopped, and for every session whose `end` exit is outside `PASSED_EXITS = (0, 5)` (`skills/verify/scripts/broad_gate.py:1770`, `broad_gate.py:1846-1856`). `unended` is unchanged, and its readers `base_word` (`broad_gate.py:2040-2041`) and `UNENDED_HERE` (`broad_gate.py:2806-2807`) still read it. Read, and executed through the narrow run under `## Probes`.

What matched: *Scope* 2 holds. The failures loop now reads `head.unpassed` where it read `head.unended` (`broad_gate.py:3100`). A red session at exit 0 gets its failing files compared at the base (`broad_gate.py:3114-3118`). A preflight sets `checks[SUITE]` nowhere, so the loop never reads `head` there, as before. Read.

What matched: *Scope* 3 holds. `NOT_PASSED_AT_EXIT_0` is printed on `record.unpassed` at exit 0 (`broad_gate.py:2790-2791`), and its text (`broad_gate.py:2861-2868`) ties each cause to its own branch, as the folded *Scope* 3 now says (`design.md:28`). The phase record says why the build departed from the first wording of *Scope* 3 (`phase-1.md:9`). That departure was folded into the frame and holds.

What matched: *Scope* 4 holds. Every place the list names was rewritten in place, and the two extra comments in `gate` the phase record names are at `broad_gate.py:3065-3069` and `broad_gate.py:3104-3113`. This round ran `git grep` at HEAD outside `seal/threads/`, `tests/` and `.test_durations` for `after the recorder`, `two kinds of stop`, `two stops`, `late hook`, `record's reach`, `green whenever`, `STOPPED_AT_EXIT_0`, `sessionfinish`, `part-way`, `whatever the row`, `row exited 0`, `fails the suite` and `the row's exit`. The only statement of the old fact still standing is `docs/running/the-broad-gate.md:55-56`, which goes to the settle. Like the crafter's list, this is a sample by wording. Other hits were read and stay true. `skills/code-review/orchestration.md:419-427` and `skills/verify/orchestration.md:112-142` speak of a file list and of the base. The `&` row of `templates/setup/config.md:360` says the backgrounded command's status is discarded and claims no verdict, so it does not rest on the old fact. `.github/scripts/release_seal.py:240-280` reads the record's counts, and its workflow hands it the suite step's outcome (`.github/workflows/publish-release.yml:138-163`).

What matched: the new cases hold the frame's facts. S1 and S2 are the four `LATE_ACTS` shapes (`tests/skills/test_broad_gate.py:2493-2511`, `test_broad_gate.py:2614-2642`). S3 is `test_broad_gate.py:2644-2658`, S5 is `test_broad_gate.py:1561-1573`, and S4 is #883's cases with the line renamed. Read against their groups, each covers what the group did not. The existing gate case for a red suite, `test_refuses_a_failing_test_the_base_lacks_as_new`, runs at exit 1, and the new ones run at exit 0. The existing `read_record` stop cases hold `unended` and now `unpassed`, and the new unit case holds exit 1 apart from 0 and 5. `seal layout --pairs` names no pair in `tests/skills/test_broad_gate.py`. The crafter claims the new cases were seen red at e44c9b07 (14 failed, 14 passed) and that the three mutants were all red. This round did not re-run either. They read consistent with G1's executed shapes and with the condition at the base, which read `head.unended`.

What matched: `frame/questions.md` Q1 has a measurement. Run 41924200504 on b5d3d85 completed `success` on every leg (executed, `gh run view 41924200504`). The ubuntu leg's durations list names all four `LATE_ACTS` shapes as calls. The Windows group 2 list names `unconfigure-os-exit-0`, and no `SKIPPED` line in the run names a new case. Updating Q1's status is the orchestrator's.

What matched: the `## Rule changes` `from:` text stands in `docs/running/the-broad-gate.md:40-59` once whitespace is normalised (executed, the comparison under `## Probes`), so the settle can find it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD; the suite stays `unverified` until then | `seal/config.md` `Broad gate` row | the orchestrator's broad run, then the sealer's spawn |
| The crafter's phase-boundary aggregate (42 modules, 2358 passed, 10 skipped) and its seen-red count at e44c9b07; neither was re-run this round | `seal/threads/1793829111-a-red-session-a-late-hook-hides-does-not-pass/trail/phases/phase-1.md:17-26` | the orchestrator's broad run for the first; the sealer's sample for the second |
| A conftest `pytest_runtestloop` hookwrapper that sets `session.testsfailed = 0` changes the run loop's own exit (`.venv/lib/python3.13/site-packages/_pytest/main.py`, `_main`), so the `end` line reads 0 over a `failed` report and the gate still passes with `1 failed` among its counts. That act lies inside the run loop, which the frame's rule trusts, so it is outside #1301's frame and no finding here. Whether it is worth a follow-up issue is a question | `skills/verify/scripts/broad_gate.py:1770` | the orchestrator, with the owner where a follow-up is opened |
| G2 on pytest 6.1 and 7.0, the recorder's other measured builds; the frame probed 9.1.1, and CI runs the latest pytest | `seal/threads/1793829111-a-red-session-a-late-hook-hides-does-not-pass/frame/questions.md:11` | the orchestrator, as the frame's named assumption |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -q -k "read_record or failure_lines or stopped_at_exit_0 or act_after_the_run_loop or late_hook or told_where_the_row_is_written"` | 29 passed, exit 0, under `-n auto` on macOS |
| `gh run view 41924200504`, with `--json status,conclusion,jobs` and `--log` | completed, conclusion `success` on every job; the durations lists name the new cases as calls, and no `SKIPPED` line names one |
| `bin/seal layout --pairs` | exit 0; no pair names `tests/skills/test_broad_gate.py` |
| `python3 skills/code-review/scripts/chain_check.py --baseline release/v0.32.1 --root <the worktree> --worktree`, before the record was written | exit 0; no notice at a line of `frame/design.md` |
| A whitespace-normalised containment check of the `from:` text in `docs/running/the-broad-gate.md`, run with `python3` | `True` |
| `git grep` over the words listed under the *Scope* 4 confirmation, outside `seal/threads/`, `tests/` and `.test_durations` | the only old-fact statement left is `docs/running/the-broad-gate.md:55-56` |
