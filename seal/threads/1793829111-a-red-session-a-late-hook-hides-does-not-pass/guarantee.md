# Guarantee: 1793829111-a-red-session-a-late-hook-hides-does-not-pass

Audited at f398963a against `release/v0.32.1`, which resolves to 3b2190c4 here
(executed: `git rev-parse --verify --quiet 'release/v0.32.1@{upstream}'`). No
earlier `guarantee.md` stood, and `seal/parity.md` is not in git, so no
`original:` line is owed.

`trail/gate.md` names `run: 654c799b against 3b2190c4`. 654c799b is an
ancestor of HEAD, and the commits after it, b1d35a91 and f398963a, touch only
`trail/gate.md` and `gaps.md` under this work item's directory (executed:
`git merge-base --is-ancestor 654c799b HEAD`, exit 0;
`git log --no-merges --name-only 654c799b..HEAD ^3b2190c4`).
`seal pr-body seal/threads/1793829111-a-red-session-a-late-hook-hides-does-not-pass --body <pr-body.md> --check`
exited 0 (executed), so the part below `## From the records` is the records'
text.

The `seen red` claims were re-run in a scratch clone at f398963a with
`skills/verify/scripts/broad_gate.py`,
`skills/verify/scripts/pytest_record/agentic_pytest_record.py` and
`templates/setup/config.md` restored from 3b2190c4 and HEAD's tests kept. The
same clone then took HEAD's code back for the HEAD run and the three mutants,
and was removed after its runs. Each run used this repository's `.venv`
interpreter with `python -m pytest ... -q -p no:xdist -p no:cacheprovider`,
exit code read directly. Nothing in the tree under audit was changed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Seen red: the new and changed cases fail against e44c9b07's gate, 14 failed and 14 passed, with each `LATE_ACTS` shape failing on `assert gate.gate(...) == 1` with `0 == 1` and its output opening `BROAD GATE PASSED` over `suite + 1 failed . 1 passed` | `trail/phases/phase-1.md:17-21` | in the at-base clone, `pytest tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -k "read_record or failure_lines or stopped_at_exit_0 or act_after_the_run_loop or late_hook or told_where_the_row_is_written"` | holds: exit 1, 15 failed and 14 passed, the 15th being the S6 case this command adds to the crafter's `-k`. The four `LATE_ACTS` shapes fail `assert 0 == 1`, and each captured output prints `BROAD GATE PASSED` with `suite   + 1 failed . 1 passed`, which is #1301's defect. S5's case and the four stops fail with `AttributeError` on `unpassed`. The three `failure_lines` cases fail where they build their record, and #883's two gate cases fail (executed) |
| Seen red, S6: the rule-3 pin fails against the old template on its first rewritten sentence, and the old template holds the sentences now asserted gone | `trail/phases/phase-1.md:22` | the same at-base run; `git show 3b2190c4:templates/setup/config.md` and `git show HEAD:templates/setup/config.md`, each through `grep -c -F` for the three gone strings | holds: the case fails `rule 3 does not carry: Where one did, the suite fails even where the row exited 0, ...`, the first rewritten sentence; each of the three gone strings counts 1 at the base and 0 at HEAD (executed) |
| S3 passes before and after and is not a seen-red case | `trail/phases/phase-1.md:21`; design S3 | the at-base run and the HEAD run | holds: `test_accepts_a_green_suite_a_late_hook_exits_with_0` is among the 14 passed at the base and passes at HEAD (executed) |
| The cases pass at HEAD | round 1 *Probes* row 1 | in the clone with HEAD's code back, the same `pytest` command | holds: exit 0, 29 passed (executed, at f398963a) |
| `seal mutate`: `PASSED_EXITS` widened to `(0, 1, 5)` is red | `trail/phases/phase-1.md:24` | that one guard edited in the clone, then `pytest tests/skills/test_broad_gate.py -k "exit_1_passed or act_after_the_run_loop or says_why_it_failed or late_hook"` | holds: exit 1, 5 failed. S5's case fails `(4, 1, 1) == (4, 2, 1)` at the `unpassed` index, and the four shapes fail `assert 0 == 1`. S3 stays green (executed) |
| `seal mutate`: the failures loop reading `head.unended` again is red | `trail/phases/phase-1.md:24` | that one guard edited back, the loop's condition at `broad_gate.py:3100` edited, the same command with `stopped_at_exit_0` added | holds: exit 1, the four shapes fail `assert 0 == 1`. #883's stopped cases stay green, as they should under `unended` (executed) |
| `seal mutate`: `failure_lines` keying the line on `record.unended` again is red | `trail/phases/phase-1.md:24` | that one guard edited back, `broad_gate.py:2790` edited, the first mutant's command | holds: exit 1. `test_accepts_a_suite_that_exited_0_and_says_why_it_failed` fails on its red record's list, and the four shapes fail at the assertion that the `NOT_PASSED_AT_EXIT_0` line is in the output (executed) |
| Q1: run 41924200504 of `tests` on b5d3d855 ended `success` on four Windows, three macOS and one ubuntu `pytest` legs, and only records changed after b5d3d855 | `frame/questions.md` Q1; `gaps.md:7`; the spawn prompt | `gh run view 41924200504 --json headSha,status,conclusion,workflowName,jobs`; `git diff --name-only b5d3d855 HEAD` | holds: head b5d3d8550d95, completed, `success`; the eight `pytest` jobs, `lint`, `durations` and both `arms-grammar` jobs `success`, `release-report` skipped; the diff lists eight files, all under this work item's directory (executed) |
| No new case is skipped on any leg, and the `\|\|` row ran under `cmd.exe` | `gaps.md:7`; the orchestrator's part, *Other platforms* | `gh run view 41924200504 --log` through `grep`; read `tests/skills/test_broad_gate.py` for a platform skip | partly executed, partly read. No `SKIPPED` line names a new case. The ubuntu leg and macOS group 1 name all four shapes in their durations lists, and Windows group 2 names `unconfigure-os-exit-0` alone, because a durations list holds only the slowest calls (executed). The cases carry no skip marker, and `--splits 4` places each item in one Windows group, every one of which ended `success`, so `row-or-interpreter` ran on one of them (read). No log line names `row-or-interpreter` on a Windows leg, so that last step is inferred and is not `executed` |
| `Removes` rows 2 to 7: the late hook named as a stop out of the record's reach, its pin, "is green whenever `tee` is", and `head.unended` as the loop's condition leave the tree | design *Removes* | `git grep -n -F` at HEAD, outside `seal/threads/` and `.test_durations`, for `Two stops are out of the record's reach`, `Two kinds of stop`, `is green whenever`, `` comes after the session's `end` line ``, `runs after the recorder's comes after`, `STOPPED_AT_EXIT_0` and `head.unended` | holds: the only hits are the three gone strings in `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:662-665`, which assert them absent (executed) |
| `Removes` row 1: the late-hook limit in `docs/running/the-broad-gate.md` leaves through `## Rule changes`, at the settle | design *Removes* row 1; changelog's last sentences | read `docs/running/the-broad-gate.md:40-59` | holds: the paragraph still names the late hook, as the `from:` text gives it, so the settle can find it; it goes at the settle, as the design and the changelog both say (read) |
| G2: the recorder writes the `exitstatus` its `pytest_sessionfinish` is handed, and its hook carries no ordering mark | design G2; round 2 *Confirmations* | read `skills/verify/scripts/pytest_record/agentic_pytest_record.py` around `pytest_sessionfinish` | holds (read). The S2 `early-exitstatus-0` shape turning red at the base and green at HEAD is the executed half (rows 1 and 4) |
| This repository's own row runs one pytest under `-n auto`, and an xdist worker registers no `Recorder` | design G12; the orchestrator's part, *What gets refused* | read `.github/scripts/run_tests.py:606`, `agentic_pytest_record.py:179` | holds (read) |
| The broad run at 654c799b passed, `suite ✓ 6348 passed · 12 skipped`, `chain ✓ exit 0` | `trail/gate.md`; `gaps.md:8`; the orchestrator's part, last paragraph | read `trail/gate.md` | the run and its commit hold: the gate writes `trail/gate.md` only after a passing run, and it names 654c799b (read). The counts are not in `trail/gate.md` and were not re-run here, as rule 2 gives. They are `unverified` by this audit, and the orchestrator's run, which printed them, answers for them. `gaps.md:8` cites `trail/gate.md` beside the counts. The file holds the run but not the counts, and nothing in the tree contradicts the counts |
| The phase-boundary run of 42 modules, 2358 passed and 10 skipped | `trail/phases/phase-1.md:26` | not re-run | `unverified` by this audit. It ran before the last comment edit, and the broad run at 654c799b answers for the suite at that code |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `read_record` counts the `HEAD` sessions that did not pass. A session passed on an `end` line with `stopped` `[]` and exit 0 or 5. The gate fails the suite on that count whatever the row exits. The exit-0 line names both causes, and the late-hook limit leaves five places. The rule goes to the settle (`frame/design.md` *Scope*, *Removes*, `## Rule changes`) | the issue body's *Done when*: G6 weighs it under *The rule a mechanism is kept against*, and it is built with cases seen red (rows 1 and 2 above); the issue's *Symptom*, reproduced at the base by row 1; the diff | none |
| the build | `RunRecord.unpassed`, `PASSED_EXITS = (0, 5)` and the line `NOT_PASSED_AT_EXIT_0`, which ties each cause to its own branch. Four `LATE_ACTS` shapes, the `\|\|` row in place of `; true`, and *Scope* 4's rewrites with two more comments in `gate` (`trail/phases/phase-1.md`; the diff) | the design's *Scope* 1 to 4 and every `Removes` row (rows 1, 10 and 11 above); the two departures it names, the *Scope* 3 wording and the `\|\|` spelling, which the frame folds at b5d3d855 and c9a1b1bf now state, so design and build agree at HEAD | none |
| the last round | Round 2, `target: 6b96900d`, confirms round 1's two closes and opens nothing (`trail/rounds/round-2.md`) | the tree: the paste-ready texts stand in `frame/design.md`, `frame/plan.md` and `frame/questions.md`. The commits after 6b96900d touch only this work item's records, and this audit read them: 0185d244 is round 2 itself, 654c799b rewrites the `frame/questions.md:17` reason round 2 noted, and b1d35a91 and f398963a are `trail/gate.md` and `gaps.md` row 2 | none. The round's own note that `gaps.md`'s "every job" is close but not exact still stands in `gaps.md:7`, and no party acts on it |
| the changelog | `seal gate` passed a suite with a failing test where something after pytest's run loop turned the row's exit into 0, and the gate now fails it. The failure form names both causes, a green suite under a late hook passes as before, a masking or rerunning row now fails, one stop stays out of the record's reach, and the rule is written into `docs/running/the-broad-gate.md` at the settle (`changelog.md`) | the diff; `NOT_PASSED_AT_EXIT_0`'s text; the S1 to S3 cases at HEAD (row 4 above); `templates/setup/config.md` rule 3 and the two composition rows | none. Its `\|\| true` and pipe shapes are not cases. The `\|\|` case and G1's `; true` shape are the same act, a part of the row after pytest choosing its exit, and rule 3 names it so |
| the orchestrator's part of the pull request body | The defect and the fix, `Closes #1301`, the frame's choice of the record over one more exit edge, what is refused that passed before, this repository's own row, the rule going to the settle, the two rounds, the CI run on every leg, and the broad run at 654c799b | the issue body; `frame/plan.md` *Alternatives considered* rows 1 and 2; `frame/design.md` G1 and G12; round 1 *Confirmations*; rounds 1 and 2; run 41924200504 (row 8 above); `trail/gate.md` | none. Its `\|\|` row under `cmd.exe` holds by inference from the split and the absent skip, not from a log line (row 9 above). The suite counts it quotes are the orchestrator's own console output, which no file in the tree holds (row 14 above) |

`.claude-plugin/plugin.json` reads 0.32.0 at HEAD. No party of this work
item claims a version move, and the spawn prompt's account that #457 moves it
is a claim about another branch, which this audit did not open.

```seal
target: f398963a against 3b2190c4
Verdict: sealed
```
