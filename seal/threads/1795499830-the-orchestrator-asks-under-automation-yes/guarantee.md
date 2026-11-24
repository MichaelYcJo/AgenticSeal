# Guarantee: 1795499830-the-orchestrator-asks-under-automation-yes

The audit read the tree at `80d06b8f3` against the base `release/v0.38.8`.
`release/v0.38.8@{upstream}` resolves the base to `7c8f67103`, the v0.38.7
merge on `main` (executed: `git rev-parse --verify --quiet`,
`git merge-base --is-ancestor 7c8f67103 origin/main`). Every diff below is
`git diff 7c8f67103...HEAD`.

`trail/gate.md` names `02bb84db9 against 7c8f67103`. That commit is an
ancestor of HEAD. The one commit after it, `80d06b8f3`, touches only this
work item's `trail/gate.md` (executed:
`git log --no-merges --name-only 02bb84db9..HEAD ^7c8f67103`). The broad
gate itself was not run here (contract rule 2).

`seal pr-body seal/threads/1795499830-the-orchestrator-asks-under-automation-yes --body <the body file> --check`
exited 0 (executed). The issue body was read with
`gh issue view 1608 --json title,body,comments`, and the issue has no
comments (executed). No `seal/parity.json` is tracked (executed,
`git ls-files`), and `routing.md` answers `open the pull request`, so no
parity comparison is owed. `seal/config.json` names English for both
language keys, so no `pr.<lang>.md` is owed.

The `seen red` claims were re-run in a `git clone --no-local` at
`80d06b8f3` under the scratchpad. In that clone the changed code was
restored from `7c8f67103`, or one guard was removed from HEAD's code, and
the clone was restored after each run. `git status --short` printed nothing
after the last run (executed). The tree under audit was not changed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Every new case fails against the code before the change: the hook's module at collection, the cases of `Test_open_declarations` with `AttributeError` (`seen red`) | `trail/phases/phase-1.md:27` | `git restore --source=7c8f67103 --staged --worktree -- hooks lib`, then `bin/test tests/hooks/test_ask_under_automation.py -q -p no:xdist` and `bin/test tests/lib/test_routing.py -q -p no:xdist -k Test_open_declarations` | holds: exit 2, `FileNotFoundError` on `hooks/ask-under-automation.py` at collection; exit 1, 8 failed, each `AttributeError: module 'agentic_routing' has no attribute 'open_declarations'` (executed) |
| S8: the registration case fails without the `PreToolUse` entry (`seen red`) | `trail/phases/phase-1.md:31`, row S8 | the same restore, then `bin/test tests/behaviour/test_chain_hooks_hardening.py -q -p no:xdist -k registers_its_hooks` | holds: exit 1, `assert ['SessionStart', 'Stop'] == ['PreToolUse'...tart', 'Stop']` (executed) |
| R1: the released-branch case holds the branch test of `open_declarations` (`seen red`, a case asserting a declaration is not let through) | `trail/phases/phase-1.md:39` | HEAD's code with `parsed["branch"] in checked_out and` removed through the `Edit` tool, then `bin/test tests/lib/test_routing.py tests/hooks/test_ask_under_automation.py -q -p no:xdist` | holds: exit 1. `test_refuses_a_branch_no_worktree_has_checked_out` fails with the `feature/released` declaration on the left of `== []`, and the hook's S5 case fails on the `released` tree printing a deny object. Both failing lines name the branch test (executed) |
| R6b: the non-zero exit case holds the `done.returncode` guard (`seen red`) | `trail/phases/phase-1.md:44-45` | HEAD's code with `if done.returncode:` read as `if False:` through the `Edit` tool, then `bin/test tests/lib/test_routing.py -q -p no:xdist -k Test_open_declarations` | holds: exit 1, 1 failed, 7 passed. `test_refuses_a_listing_from_a_git_that_exited_non_zero` fails at `tests/lib/test_routing.py:654` with the `feature/x` declaration on the left of `== []` (executed) |
| Round 1 finding 2's close: the dedupe case holds the hook's naming of each item once (`seen red`) | `trail/rounds/round-1.md:86`; `trail/rounds/round-2.md:83` | HEAD's hook with ` and item not in items` removed through the `Edit` tool, then `bin/test tests/hooks/test_ask_under_automation.py -q -p no:xdist` | holds: exit 1, 1 failed, 10 passed. `test_refuses_naming_a_work_item_once_whatever_worktrees_hold_copies` fails at `tests/hooks/test_ask_under_automation.py:144`, `assert 2 == 1` (executed) |
| S7: the no-list case is held by the shape test and the `__main__` catch together, and fails with both removed (`seen red`) | `trail/phases/phase-1.md:29`, rows H11 and H12 | HEAD's hook with the shape test's `if not isinstance(found, list) or not found:` read as `if False:` and `except BaseException:` read as `except ZeroDivisionError:`, through the `Edit` tool, then `bin/test tests/hooks/test_ask_under_automation.py -q -p no:xdist -k no_question_list` | holds: exit 1. The case fails on `(1, '... TypeError: 'NoneType' object is not iterable')` against `(0, '')`, which is what the phase's probe reports (executed) |
| R1 to R4 and round 1 finding 1's close: the branch test, the exit guard, `normpath`, the real-path dedupe and the catch of `gitcmd.Failed` are each held by a case | `trail/phases/phase-1.md:39-45`; `trail/rounds/round-1.md:39` | `bin/seal mutate lib/routing.py` with five `--replace` pairs, one per guard, `--tests "bin/test tests/lib/test_routing.py -q -p no:xdist -k Test_open_declarations"` | holds: baseline passes, 5 mutants, 5 red, 0 SURVIVED (executed). Verdicts only; the failing lines of R1 and R6b are read in the rows above |
| H2, H3, H4, H6, H8 and round 2 finding 1's close: the first-question narrowing, the near-spelling sentence, the same-line rule, `CLAUDE_PLUGIN_ROOT`, the `yes` filter and the condition of the sentence on what ends the refusal are each held by a case | `trail/phases/phase-1.md:46-53`; `trail/rounds/round-2.md:46` | `bin/seal mutate hooks/ask-under-automation.py` with six `--replace` pairs, one per guard, `--tests "bin/test tests/hooks/test_ask_under_automation.py -q -p no:xdist"` | holds: baseline passes, 6 mutants, 6 red, 0 SURVIVED (executed). Verdicts only; round 3 read the failing line of the last mutant (`trail/rounds/round-3.md:47`) |
| The changed modules pass at HEAD | `frame/plan.md` *Phases* row 1 | `bin/test tests/hooks/test_ask_under_automation.py tests/lib/test_routing.py tests/hooks/test_core_start.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py -q -p no:xdist` at `80d06b8f3` | holds: 123 passed, exit 0 (executed) |
| Phase 2's narrow command passed 94 cases at `e130d7656` | `trail/phases/phase-2.md:27` | the plan's phase 2 command at `e130d7656`, and with `test_every_entry_point_runs_at_the_floor.py` and `test_both_editions_carry_the_same_folds.py` added at `80d06b8f3` | holds: 94 passed at `e130d7656`; 107 passed at `80d06b8f3` (executed) |
| The hook refuses in this repository for the one open work item and lets a stated question through | #1608 *Done when* item 1; `frame/design.md` *Scope* item 2 | the clone's hook run with `CLAUDE_PLUGIN_ROOT` at this checkout and `cwd` at this checkout, once with a question lacking the marker and once with `No default: the key is the owner's.` | holds: the first prints a `deny` whose open-items part names this work item on `fix/1608-the-orchestrator-asks-under-automation-yes` alone, out of the 50 directories under `seal/threads/`; the second prints nothing; both exit 0 (executed) |
| S10: no sentence says no script decides on `Automation` | `frame/design.md` S10; `trail/phases/phase-2.md:25` | `git grep -n -i -E 'decides anything on it' HEAD -- . ':!seal/threads'` | holds: no line, exit 1 (executed) |
| S11: the hook count stands only in the settle's two lines | `frame/design.md` S11; `trail/phases/phase-1.md:31` | the count search of `frame/design.md` *Grounding* at HEAD, and a wider `git grep -i -E '\b(two\|both\|neither\|either)\b.{0,25}\bhooks?\b'` outside the records | holds: `docs/running/measuring-a-run.md:140` and `:143` alone; the wider search prints nothing outside that file. Both are wording searches, so the list is a sample (executed) |
| The version moves to 0.38.8 in `.claude-plugin/plugin.json` alone | `frame/design.md` G9; `trail/phases/phase-2.md:26` | `git grep -n '0\.38\.8' HEAD -- ':!seal/threads'` and the same for `0\.38\.7` | holds: `.claude-plugin/plugin.json:4` alone; the old version nowhere (executed) |
| `## Removes` rows 1 and 2: the sentence and the code comment that no script decides on `Automation` | `frame/design.md` *Removes* | S10's search; `grep -n 'is a record, and no script' skills/implement/orchestration.md` | holds: no line for either (executed). `lib/routing.py:103-107` and `:208-211` now say the check decides nothing and the hook reads a `yes` (read, diff) |
| `## Removes` row 3 and the changelog's last *Changed* item: each count of the hooks outside the README lists | `frame/design.md` *Removes*; `changelog.md:10` | S11's searches; `grep -n -E 'ships three hooks\|훅 세 개' README.md README.ko.md` | holds: the count stands at `README.md:340` and `README.ko.md:339` alone (executed) |
| `## Removes` row 4: the count in `docs/running/measuring-a-run.md` is left for the settle, and every `## Rule changes` `from` still stands where it points | `frame/design.md:123-165` | `grep -n` of each `from` text's opening in `docs/running/the-run.md` and `docs/running/measuring-a-run.md` | holds: `docs/running/the-run.md:49`, `docs/running/measuring-a-run.md:140` and `:143` (executed); the item names the settle, so nothing of it is owed in this tree |
| `gaps.md`'s closed Windows row: run 45343775784 passed on every leg | `gaps.md:9` | `gh run view 45343775784 --json conclusion,status,headSha,workflowName,jobs` | holds: `tests`, `success`, `completed` at `61513fa00`, four Windows 3.12 groups among nine `success` jobs, `release-report` skipped (executed). The durations half is round 2's download, not re-run |
| `frame/questions.md` Q1: Claude Code 2.1.331 honours the hook's deny in the main session | `frame/questions.md:13`; `pr.md` quote 2 | not re-run | unverified. The measurement needs an interactive session, which this audit did not start. The orchestrator measured it; the first session on 0.38.8 that asks while an open work item reads `yes` answers it again |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| The design | A `PreToolUse` hook on `AskUserQuestion` refuses a call while a work item whose branch is checked out in a worktree reads `Automation` `yes`, unless each question holds `No default:` and a reason on its line; `lib/routing.py#open_declarations` reads the open items; the orchestrator's skill takes three passages; the hook count stands once per README; three policy documents change at the settle | #1608 *Done when* items 1 to 4 (read). The reading of open as a checked-out branch is the frame's, with grounds at `frame/plan.md:9` and `:16-19`, and the orchestrator answered round 1's `## Not judged` row on it against the issue's "the `seal/` root of the session's repository and its worktrees" (`frame/plan.md:62`). The diff and the re-runs above | none |
| The build | Phase 1 delivers *Scope* items 1 to 6 with five departures (a renamed hardening case, two added cases, a sentence in `CONTRIBUTING.md` on how the hook refuses, a third consequence in `lib/launch.py`); phase 2 delivers items 7 and 8 with none | the diff (read); the `seen red` re-runs above; `routing.md` reads `Implementation` `crafter`, and both phases whose Status cell holds a commit, `752164072` and `e130d7656`, have their `trail/phases/phase-N.md` | none |
| The last round | Round 3 at `7a56bbc2d` opens no finding and confirms round 2's two closes | the diff of `61513fa00..7a56bbc2d` (read); the mutant of round 2 finding 1 re-run red above; every commit after `7a56bbc2d` touches only this work item's directory (executed, `git log --name-only`). Round 3 carries no `fixed` finding, so no fix stands unread | none. Its `## Not judged` rows name answerers: the broad gate, now `trail/gate.md`; Q1, carried; Windows `py -3`, the owner; the settle's row of `gaps.md:10` |
| The changelog | *Added* the hook and what its refusal carries; *Changed* the skill's three passages, the hook count and the version; the three documents follow at the settle; three `### Process changes` rows | the diff, item by item (read); the live run of the hook above; the `Removes` re-runs | none |
| The orchestrator's part of the pull request body | Three quotes with coordinates and `Closes #1608.` | each quote stands at its coordinate: `frame/plan.md:60`, the Status cell of `frame/questions.md:13`, and `gaps.md:8` (read); `seal pr-body --check` exit 0 (executed); `routing.md` *Why this way*, whose grounds name a new hook script and its reader in `lib/routing.py`, `hooks/hooks.json`, two sections of `skills/implement/orchestration.md`, every passage outside `docs/` that counted the hooks, seven test files and `plugin.json`, which is what the diff changes (read, `git diff --stat`) | none |

Read, and not a reason to withhold: `gaps.md:11` and `:12` still read open
with "the orchestrator's broad gate" as their answerer. `trail/gate.md`
records that gate passing at `02bb84db9`, so the answer stands in the
records. The settle decides those rows with the memo's other open rows.

```seal
target: 80d06b8f3 against 7c8f67103
Verdict: sealed
```
