# Guarantee: 1793171574-agent-definitions-restate-the-contract

| Field | Value |
|---|---|
| Target SHA | 7cdc9300 against c825fd2c |
| Broad gate | 2bad2cef against c825fd2c |

The base `release/v0.24.0` resolved through `release/v0.24.0@{upstream}` to `c825fd2c` (executed). `trail/gate.md` names `2bad2cef`, an ancestor of HEAD, and the one commit after it, `7cdc9300`, changes only `seal/threads/1793171574-agent-definitions-restate-the-contract/trail/gate.md` (executed, `git log --no-merges --name-only 2bad2cef..HEAD ^c825fd2c`). `seal pr-body 1793171574-agent-definitions-restate-the-contract --body <the body file> --check` exited 0 and printed that the part above `## Not from the records` is the records' text (executed). The claims below were re-run in a `git clone --no-local` of the branch at `7cdc9300` in the sealer's scratch directory, with the worktree's `.venv` interpreter; the clone was removed afterwards.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S1: the ten phrases are found 15 times at the base and 0 times after the change | `trail/phases/phase-1.md`, *What this phase found*, second bullet | `python3 -I` reading each of the five `agents/<name>.md` through `git show <rev>:` with whitespace collapsed, counting the ten S1 phrases, at `6e322bb7`, `c825fd2c` and `7cdc9300` | holds: 15, 15 and 0, each phrase in the file its sentence stood in (executed) |
| The old assertions went red against the edited definitions: exactly four cases fail | `trail/phases/phase-1.md`, third bullet | in the clone, the three changed test modules restored from `6e322bb7` over the definitions at `7cdc9300`, then `python -m pytest -q -p no:cacheprovider -n0` over those three modules | holds: exit 1, 4 failed, 40 passed; the four are `test_the_crafter_names_no_runner_of_the_broad_gate`, `test_the_window_the_sealer_shipped_under_is_closed`, `TestDefinition::test_step_1_reads_the_record_and_runs_nothing` and `test_the_implementer_keeps_the_half_that_makes_the_rule_its_own` (executed) |
| The crafter's `rule 2's`, mutated, turns `test_the_crafter_puts_both_answers_in_the_hand_back` red | `trail/phases/phase-1.md`, *S3* bullet | `seal mutate agents/crafter.md --replace "rule 2's" "rule X's" --tests "<python> -m pytest -q -p no:cacheprovider -n0 tests/text/test_broad_gate_rule.py -k test_the_crafter_puts_both_answers_in_the_hand_back"` | holds: `red`, the case failed at `tests/text/test_broad_gate_rule.py:139` (executed) |
| The sealer's `the run rule 2 names`, mutated, turns `test_the_window_the_sealer_shipped_under_is_closed` red | `trail/phases/phase-1.md`, *S3* bullet | `seal mutate agents/sealer.md --replace "the run rule 2 names" "the run rule X names" --tests "<python> -m pytest ... tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -k test_the_window_the_sealer_shipped_under_is_closed"` | holds: `red`, the case failed at `:997` (executed) |
| The proofer's `as a row`, mutated to `as a line`, turns `test_the_reviewer_has_a_field_for_the_question_the_default_produces` red | `trail/phases/phase-1.md`, *S3* bullet | `seal mutate agents/proofer.md --replace "as a row" "as a line" --tests "<python> -m pytest ... tests/text/test_broad_gate_rule.py -k test_the_reviewer_has_a_field_for_the_question_the_default_produces"` | holds: `red`, the case failed at `tests/text/test_broad_gate_rule.py:332` (executed) |
| The proofer's `a check rule 2 excludes` survives mutation, so no case reads it | `trail/phases/phase-1.md`, *Three new units* bullet; `gaps.md` *Not verified* | `seal mutate agents/proofer.md --replace "a check rule 2 excludes" "a check rule X excludes" --tests "<python> -m pytest -q -p no:cacheprovider <the 30 modules under tests/ that name the proofer's file>"` | holds: `SURVIVED`, exit 1, 1516 passed and 8 skipped against the mutant (executed). The other two survivors were not re-run |
| The changed modules pass at HEAD | `trail/phases/phase-1.md`, *S2, S4, S5 and S6* bullet | `python -m pytest -q -p no:cacheprovider -n0` over `tests/text/test_broad_gate_rule.py`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/behaviour/test_the_sealer_guarantees.py` and `tests/text/test_edits_go_through_the_edit_tool.py` | holds: exit 0, 60 passed (executed) |
| `ruff check` and `ruff format --check` pass over the three changed test files | `trail/phases/phase-1.md`, last bullet | `uvx ruff check` and `uvx ruff format --check` over the three files, in the clone | holds: exit 0 each (executed) |
| Every `## Removes` row stands nowhere in the tree | `frame/design.md` *Removes*, all 17 rows; `changelog.md` | the S1 count above for rows 1 to 12; `git grep -n -F` over `tests`, `evals`, `agents` and `.test_durations` for "You do not run the full suite", "rule 2 holds who does", "the typecheck or `seal gate`", "test_the_implementer_keeps_the_half" and "the forms a shell edit takes"; `git grep -F "the orchestrator runs it"` over the same | holds: the first search exits 1 with no match; the second finds only `tests/text/test_the_rules_have_one_owner.py:212`, which says it of `seal gate` run after `trail/gate.md`, not of a sealer sentence (executed) |
| The rewrap at `27ea4185` changed no word | `trail/rounds/round-2.md`, first confirmation | `git diff --word-diff=porcelain ed313b28 27ea4185 -- agents/proofer.md`, counting added or removed word lines | holds: 0, and `git diff --stat` names `agents/proofer.md` alone, 3 insertions and 2 deletions (executed) |
| The crafter's step 10 holds the `unverified` label that row 4 of `## Removes` lands on, and the sealer's *Job* holds whose the run is | `frame/design.md` *Removes* rows 4 and 9 | read `agents/crafter.md:50-56` and `agents/sealer.md:30-32` at `7cdc9300` | holds (read) |
| Each of the five definitions still lists `agent-contract` under `skills:` | `frame/plan.md` *Technical context*, first bullet | `grep -n agent-contract` over the five definitions | holds: `crafter.md:8`, `proofer.md:8`, `sealer.md:13`, `framer.md:10`, `tracer.md:9` (executed) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | #1040's 13 sentences leave the five definitions; each narrowing stays and cites its rule; every assertion on a removed sentence is re-pointed or removed; the `check:` lines stay; P1 is built on default (a), the four glosses stay | the issue's list and *Done when*; the diff; the S1 count; the old-test run | none |
| the build | phase 1 at `3eecf8a0` removed the sentences, kept the narrowings with `rule 2`, re-pointed two assertions, removed one assertion and one case with its `.test_durations` key, and rewrote two docstrings; three new units survive mutation | the diff `c825fd2c...7cdc9300`; the four re-run mutants; the four-case red; the module runs | none |
| the last round | round 2: the rewrap at `27ea4185` changed no word and fits the 88-column limit; round 1 missed the wrap check; nothing is open | the word diff; the gate record at `2bad2cef`, which follows the rewrap | none |
| the changelog | the five definitions no longer restate rules 2, 6, 7 and 9; no agent's permitted acts change; the crafter, proofer and sealer keep the narrowings it names, the sealer's as the paragraph's bold lead | the diff of `agents/*.md`; the contract preload in all five definitions | none |
| the orchestrator's part of the pull request body | `Closes #1040`, nothing else | the issue number; the records part, which `seal pr-body --check` matched | none |

Not re-run, with who answers each:

- The full suite, the repository-wide lint and the typecheck. `trail/gate.md` records the orchestrator's run at `2bad2cef`, and the sealer read it and did not run it (unverified by the sealer; the orchestrator answers through that run).
- Two of the three survivors: the sealer's new lead and the crafter's `the label is step 10's`. Only the proofer's survivor was re-run. Whether any of the three should be pinned is a phrase-pin decision (unverified; the repository owner answers through #1111).
- The evals `evals/behaviour/sealer/rule-sealer-no-gate/` and `rule-sealer-stale-gate/` were seen to exist and not run (unverified; the repository owner answers through an eval run).
- `frame/questions.md` P1 is open on default (a). This is a scope question for the owner, not a claim that fails.

Verdict: sealed
