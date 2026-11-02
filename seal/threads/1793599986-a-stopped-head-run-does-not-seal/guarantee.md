# Guarantee: 1793599986-a-stopped-head-run-does-not-seal

| Field | Value |
|---|---|
| Broad gate | a4c4e7f34 against d57e9ee7a |

The base `release/v0.29.0` has no local branch and no upstream here, so it
resolves as `origin/release/v0.29.0` at d57e9ee7a (executed: `git rev-parse
--verify --quiet` over the three forms). `trail/gate.md` holds one run block,
`run: a4c4e7f34 against d57e9ee7a`. a4c4e7f34 is an ancestor of HEAD
b02f58688, and `git log --no-merges --name-only a4c4e7f34..HEAD ^d57e9ee7a`
lists two commits, e477e565e (`trail/gate.md`) and b02f58688
(`frame/questions.md`), both under this work item's directory alone
(executed). `broad_gate.py#gate` calls `write_gate_file` only after a run
with no failures (read: `skills/verify/scripts/broad_gate.py:3072-3086`), and
`git diff a4c4e7f34 HEAD` touches only those two record files (executed), so
the run block stands for a passing run over the tree HEAD carries. The
counts the spawn prompt gives for that run, 6346 passed and 12 skipped, are
in no record and are `unverified` by this audit; the orchestrator's kept
gate output answers them. `seal pr-body <item> --body <file> --check` exited
0, saying the body below `## From the records` is the records' text
(executed).

## Claims re-run

The sample: every `seen red` the phase record makes for the new cases, the
rule 3 pin, the mutants over the new arm, the orchestrator's claims about its
commits and the merge, and the claim that the new cases pass at HEAD. Each
ran in a `git clone --no-local` of the branch worktree at b02f58688, under
the scratchpad's `1793599986-a-stopped-head-run-does-not-seal/at-base/`,
removed after the runs. The tree under audit was not changed (executed: `git
status --short` empty, HEAD b02f58688, after the runs).

| Claim | Source | Command | Result |
|---|---|---|---|
| The two new modules pass at HEAD | `trail/phases/phase-1.md` *The phase-boundary run* | `bin/test tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -q` at b02f58688 | holds: exit 0, 341 passed, 1 skipped (executed) |
| The four new cases and the preflight case pass at HEAD | `trail/phases/phase-1.md` *Seen red*, *`seal mutate`* | `bin/test tests/skills/test_broad_gate.py -q -p no:xdist -rA -k "stopped_at_exit_0 or exited_0_and_says_why or exit_0_line_above_the_files or test_accepts_a_preflight_that_runs_no_row"` | holds: 5 passed, each named PASSED, both parametrizations of `test_refuses_a_suite_a_test_stopped_at_exit_0` among them (executed) |
| Seen red: `Test_gate::test_refuses_a_suite_a_test_stopped_at_exit_0`, `pytest-exit-0` and `os-exit-0`, fail on `assert 0 == 1` against the gate before the change, the panel reading `suite   + 1 passed` | `trail/phases/phase-1.md` *Seen red* | in the clone, `git checkout d57e9ee7a -- skills/verify/scripts/broad_gate.py templates/setup/config.md`, then the `-k` command above | holds: both FAILED on `AssertionError: assert 0 == 1`, the gate returning 0, captured output `suite   + 1 passed` (executed) |
| Seen red: `Test_failure_lines::test_accepts_a_suite_that_exited_0_and_says_why_it_failed` fails on the list comparison because the new line is missing | `trail/phases/phase-1.md` *Seen red* | the same run against the base's `broad_gate.py` | holds: FAILED, at index 2 `UNENDED_HERE` stands where `STOPPED_AT_EXIT_0` is expected (executed) |
| `Test_failure_lines::test_accepts_the_exit_0_line_above_the_files_and_at_no_other_exit` pins the line's place above the file list | `trail/rounds/round-1.md` finding 3, `verdict: fixed cb60fc2e` | the same run against the base's `broad_gate.py` | holds: FAILED, at index 2 `COMPARED_AT_BASE` stands where `STOPPED_AT_EXIT_0` is expected (executed) |
| The rule 3 pin goes red where rule 3 lacks the new sentence | `trail/rounds/round-1.md` finding 1 answer; `trail/rounds/round-3.md` *Confirmations* | against the base's `templates/setup/config.md`, `bin/test tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -q -p no:xdist -k test_the_measurement_its_cost_and_its_limits_are_told_where_the_row_is_written` | holds: exit 1, `rule 3 does not carry: Where one did, the suite fails even where the row exited 0, ...` (executed) |
| Third batch at 944c1463: the append replaced by `pass`, `check.code == 0` removed and `record.unended` removed, each red; first batch's mutant 1, the loop condition cut back to `if not check.failed:`, red | `trail/phases/phase-1.md` *`seal mutate`* | #898's `bin/seal mutate` over the clone's `skills/verify/scripts/broad_gate.py`, `--cwd` the clone, `--tests "bin/test tests/skills/test_broad_gate.py -q -p no:xdist -k 'Test_failure_lines or Test_gate'"`, four `--replace` pairs naming those four mutants | holds: baseline passed, 4 mutants, 4 red, 0 SURVIVED, 0 with no verdict (executed) |
| The orchestrator's commits touch only the work item's records, except the merge | the pull request body's first part, *The orchestrator's commits* | `git show --name-only` over every non-merge commit in `d57e9ee7a..HEAD`, filtering paths under `seal/threads/1793599986-a-stopped-head-run-does-not-seal/` | holds: the only commits with paths outside the records are the crafter's `fix:` and `refactor:` commits 56e81a6c, 6382f67c, 944c1463, cb60fc2e, d43beea9 and 3de5c6c8 (executed) |
| The merge a4c4e7f34 of `release/v0.29.0` resolved no conflict | the pull request body's first part, *The merge* | `git show --remerge-diff a4c4e7f34` | holds: parents 93c256dbe and d57e9ee7a, remerge diff empty (executed) |
| The broad run at a4c4e7f34 ran the new arm | the pull request body's first part, *Failure direction*; `frame/questions.md` Q1 | `git grep STOPPED_AT_EXIT_0 a4c4e7f34 -- skills/verify/scripts/broad_gate.py`; `docs/the-broad-gate.md:89-96` | holds: the arm stands at a4c4e7f34 (`:2747`), and the installed gate hands the run to the tree's copy where the tree ships one (executed; read: the installed 0.28.0 `broad_gate.py:292-299`) |
| The records hold no unread finding and the chain agrees with HEAD | `trail/rounds/round-3.md` | `python3 skills/code-review/scripts/chain_check.py --baseline d57e9ee7a --root <branch worktree> --sealing` | holds: exit 0; notices only that the pull request's state is unknown and that git carries no `guarantee.md` yet (executed) |
| The phase-boundary run, 3812 passed and 12 skipped, and the fix pass's 97-module set | `trail/phases/phase-1.md`; `trail/rounds/round-3.md` *Not judged* | not re-run | `unverified`: aggregates, superseded by the orchestrator's broad run at a4c4e7f34 |
| The two new gate cases on Linux and Windows | `gaps.md` *Not verified* | not re-run | `unverified`: the pull request's CI test job answers it |

`## Removes` of `frame/design.md` holds one row, `nothing`, and the changelog
names no removal, so no removal is owed in the tree (read).

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | The suite fails where `head.unended` is not 0, whatever the row's exit; the failure form gains one pinned line after the first lines and ahead of `UNENDED_HERE`; rule 3, the orchestration paragraph, the module docstring, the `failure_lines` docstring and the loop comment are rewritten; the recorder's code, `RAN_TO_ITS_END`, the base's words and `release_seal.py` stay; two stops stay limits | the issue body, which asks whether a head run stopped part-way at exit 0 is refused and what the refusal says; the tree: `broad_gate.py:3051` and `:2744-2747`, `RAN_TO_ITS_END = (0, 1, 5)` at `:1739`, the recorder changed in its docstring alone | *Scope* item 1 says "The base is not run, because the record holds no failing file to compare". The tree runs `compare_at_base` where a test failed before the stop (`broad_gate.py:3063-3067`). The build names this correction (`trail/phases/phase-1.md` *The frame, checked before the build*), the changelog states the tree's behaviour, and the `to:` the settle writes does not carry the sentence. The tree and the build decide it; the issue does not speak to it |
| the build | The loop decides the suite's verdict and `Check` stays; `STOPPED_AT_EXIT_0` comes directly under the first lines; the name test was dropped after a mutant survived; three cases seen red at the base | the tree at HEAD; the re-runs above (seen red, mutants, pin) | none |
| the last round | Round 3 at 13290690: no findings; confirms round-2#1 and round-2#2; the late-hook case predates the branch and goes to the owner | the tree: rule 3 at `templates/setup/config.md:366` carries both limit sentences, and the pin goes red without the new sentence (executed above); #1301 is open with that late-hook title (executed: `gh issue view 1301`) | none |
| the changelog | The gate failed nothing over a suite pytest stopped at exit 0; now the suite fails, the run exits 1 with `BROAD GATE FAILED` and writes no `trail/gate.md`; the base runs only where a test failed before the stop; two stops stay out of reach, stated in rule 3 | the tree (`broad_gate.py:3051-3067`, `UNENDED_HERE` naming `records/`), the design's `to:`, the re-run cases | none |
| the orchestrator's part of the pull request body | Closes #883; what the gate reads; it refuses more; the broad run passed with the new arm; nothing removed; two limits; three rounds as recorded; #1301 filed for the late-hook case; the merge clean; the orchestrator's commits touch the records alone | the records it cites, read against each: `changelog.md`, `frame/plan.md` C, D and E, `frame/questions.md` Q1, the three round records; the tree and git facts re-run above | none |

`gaps.md` *Not verified* still names Q1 as open and the base as
`release/v0.28.1`. It was written before the broad run and before the
milestone's rename; `frame/questions.md` Q1 now carries the answer, and no
party states the old base as current (read).

```seal
target: b02f58688 against d57e9ee7a
Verdict: sealed
```
