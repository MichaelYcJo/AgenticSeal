# Implementation Plan: a red session a late hook hides does not pass (#1301)

## Technical context

The work builds on four places in the code, as they stood at the base, 3b2190c4; the build's own names are in `trail/phases/phase-1.md`.

- `skills/verify/scripts/broad_gate.py#read_record` reads every keyed record once per run. It already reads each `end` line's `exitstatus` and `stopped` to count `unended`, and its `exitstatus` to count `unplaced_red`.
- `broad_gate.py#gate`'s failures loop fails a check on its exit, and the suite also on `head.unended`.
- `broad_gate.py#failure_lines` prints `STOPPED_AT_EXIT_0` where the suite exited 0 and `record.unended` is not 0. It prints the base words, `UNENDED_HERE` and the counts beneath.
- `broad_gate.py#compare_at_base` and `base_word` read the base's `unended` for the words, and are not touched.

The recorder, `skills/verify/scripts/pytest_record/agentic_pytest_record.py#Recorder`, writes from its `pytest_sessionfinish` the `exitstatus` pytest hands it. G2 of `frame/design.md` shows that value is the run loop's own.

**The constraint.** The `Broad gate` row is one shell command, and the gate cannot split it into parts: `broad_gate.py#not_as_written` reads it whole, and `run` hands it to one shell. So the row's exit keeps failing every check, and the record can only add a failure to it, never take one away.

**The failure scenario of the chosen approach, six months on.** A repository's row reruns its pytest over a flaky failure, as G1's last shape does, and its gate starts failing on the first run's red session. The failure form says why, the row's composition is in `suite.txt`, and the fix is in the row: run the rerun inside one pytest session, or fix the flake. A second scenario is a pytest release that hands `pytest_sessionfinish` a value other than the run loop's exit. The recorder's `exitstatus` would then read what that release handed, and the `early-exitstatus-0` shape of S2 is the case that turns red on it, because its hook sets the session's exit status before the recorder's runs. S1's hook raises after the recorder wrote, and S5's case writes its records by hand, so neither meets that release.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **Read the suite's pass off each `HEAD` session's `end` line.** A session passed where its `end` line has `stopped` `[]` and exit 0 or 5. The suite fails where any session did not pass, whatever the row's exit. #883's rule widens from "stopped" to "did not pass" (`frame/design.md` *Scope* 1 to 3). | A row that masks a red pytest, or runs it again over a failure, now fails at the gate. `templates/setup/config.md` rule 1 already says a red check does not belong in the row, and the failure form says why (`frame/design.md` G6). | Chosen. The verdict comes from pytest's own exit for each session, which is one exact field (G5). It closes every act after the run loop that G1 reproduced, whichever one chose the row's exit. It also removes the late-hook limit from five places instead of narrowing it. |
| **Add one more edge:** fail where the row exited 0 and a `HEAD` session's `end` line reads exit 1, as a count beside `unended`. | On every input it gives the first row's verdict, because a row exit other than 0 already fails the suite. The condition on the row's exit is therefore dead weight. The rule would read as #883's exception plus this one, and the next shape that differs between the row and the record would add a third edge. | Rejected. Same verdict and same cost as the first row, but two rules where one states the fact. The milestone asks for this weighing, and this is its answer. |
| **Read the pass off the record's counts:** fail where `record.counts` holds `failed` or `error`, as `.github/scripts/release_seal.py#suite_counts` does at the tag. | A failing test with no file of its own is written as no line and counts under no category (`unplaced`), so the counts miss it while pytest's exit 1 holds it. A plugin's own category word for a failed report is missed the same way. | Rejected for the broad gate. pytest's exit covers every report, placed or not. The release seal keeps its counts, because it also refuses `unplaced` (G9). |
| **Let the recorder see the late act:** make its `pytest_sessionfinish` a hookwrapper that writes the `end` line after every other hook, recording a raised `Exit` as a stop. | A hook that sets `session.exitstatus = 0` would make the `end` line read 0 over a red session. That hides what the `end` line shows today (G1's plain and `tryfirst` shapes, G2). It still cannot see `os._exit(0)` in `pytest_unconfigure`, nor the row's `; true` (G1). It would also change a recorder whose exits were measured on pytest 6.1, 7.0 and 9.1 (`RAN_TO_ITS_END`'s comment). | Rejected. It reads the exit a hook chose rather than the run loop's, and it sees fewer of G1's shapes than the first row does. |
| **Decide against it, and keep the late hook a named limit.** | The gate keeps printing `✓` beside `1 failed` and writing `trail/gate.md` over a red suite, and the sealer guarantees it (G8). The `tee` row of `templates/setup/config.md` keeps documenting a red suite as green. | Rejected under `skills/core/SKILL.md` *The rule a mechanism is kept against* (G6). The widened refusal costs no run and no question, and it removes text. |
| **Replace the structure: decide the suite on the record alone**, and drop the row's exit wherever a record exists. | A row such as `bin/test -q; uvx ruff check .` with a red lint and a green record would pass. The row's exit is the only fact the gate has about the row's parts that are not pytest. | Rejected. The premise that keeps the row's exit was checked: the gate runs the row as one command and cannot split it (*Technical context*, the constraint). |
| **Replace the structure: fold `unended` and `RAN_TO_ITS_END` into the one count of sessions that did not pass**, at `HEAD` and at the base. | At the base, a red session ran to its end, and its file reads `failing on base too`. A stopped one turns `new` into `new?` with `UNENDED_AT_BASE`. One count cannot tell the two apart, and `UNENDED_HERE` would lose the number it prints. | Rejected. The premise that keeps `unended` was checked: `broad_gate.py#base_word` and `failure_lines` read it, and both need "stopped" apart from "red". |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* 1, 2, 3 and 4, test-first. | `frame/design.md` S1, S2 and S5 as new cases in `tests/skills/test_broad_gate.py`, each seen red at e44c9b07, with how in the phase record. S3 as a case that is green before and after. S4 through #883's cases with the line rewritten. S6 through `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` with its pins moved, seen red against the old sentence. The narrow run of the modules the phase touched. The suite stays `unverified` until the orchestrator's broad run. | b6775862 |

## Operational impact

There is no migration, no new variable, no new dependency and no change to the gate's exit codes. One behaviour changes for a repository that installs the plugin: a `Broad gate` row that masks a red pytest session, with `; true`, `|| true`, a pipe or a second pytest run, now fails at the gate. It passed before. The failure form says why, and `templates/setup/config.md` states it under the row's criterion.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
