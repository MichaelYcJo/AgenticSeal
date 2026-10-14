# 1791940762-the-record-of-truth-is-tests-not-coordinates — review round 2

| Field | Value |
|---|---|
| Target SHA | 475c666f8733c6198c3c0a8e818096a535c6b426 |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #950 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `04edf1aade6fdeb80bfc480aa3a6bf453dbe1ba8..005919e360e7631dcfdc62543f62b443ae2b7c3f`, 1 commit |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1: `tests/test_pact_check.py`'s slow-file ceiling is listed at its reading, 121, with no headroom; it is 157 by the file's own rule, and the PR body's line moves with it |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Verifying round 2 of #944: each of round 1's eight fixes over 5a3ffdb4..67275a50, round 1's ❓ (W2 and S11 seen red) by mutation-check, the orchestrator's commits 8a63e245 and 6b6c5248 and the PR body's budget lines, and anything the fixes introduced. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | `tests/test_pact_check.py` is listed at a ceiling equal to its reading, 0 headroom, against the 1.3-times rule its own file states, so the next refresh likely fails the gate on an unrelated pull request | `seal/budgets.md:73` | **fixed** `005919e3` | fixed at 005919e3; executed: `budget_check.py` reads 121 s (raw 137 at x1.132) against 121, 0.0 % headroom; this refresh alone moved the file 1.49 times the level; read: `seal/budgets.md:15-17` and `budget_check.py:94` give 157 |
| ⬜ 2 | `overview.md` still says `.test_durations` is unrefreshed and its case red, after 8a63e245 refreshed it | `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/overview.md:56` | open | executed: `test_the_durations_file_prices_the_suite` passes at the tip; also `overview.md:34` and `:77-79`; paperwork, not counted in `Needs a fix` |
| 🟢 | round 1's finding 1 is closed — `rules` resolves in the repository it is typed in, and both READMEs carry its row | `.github/scripts/rules.py:163` | confirmed | executed: mutation red on the subdirectory case; read: `ROOT` gone, the module docstring and `README.md:260`, `README.ko.md:247` |
| 🟢 | round 1's finding 2 is closed — a target under an `if` or a `try` prints its sentence, never a traceback | `.github/scripts/rules.py:62` | confirmed | executed: mutation red on 3 cases; the module passes |
| 🟢 | round 1's finding 3 is closed — indented rule paragraphs are counted, and six ceilings rose by 46 in total | `.github/scripts/budget_check.py:219` | confirmed | executed: mutation red; every `unenforced:` row holds; no visible paragraph opens 4 or more spaces in (§12) |
| 🟢 | round 1's finding 4 is closed — the resolver statement is rewritten in place with its third enforcer | `docs/the-record-layout.md:243` | confirmed | read: the named case exists at `tests/test_a_folded_statement_names_what_enforces_it.py:206`; the module passes |
| 🟢 | round 1's finding 5 is closed — the test-first cadence replaces evidence feedback, and the bootstrap bullet is deleted | `skills/implement/orchestration.md:18` | confirmed | executed: `git grep` for the three phrases outside records is empty |
| 🟢 | round 1's finding 6 is closed — the follow-up row is deleted and the divergence row is rewritten in place | `seal/follow-up.md:74` | confirmed | read: `overview.md:44`; executed: no sweep text remains in the rule files or `seal/follow-up.md` |
| 🟢 | round 1's finding 7 is closed — the F2 citation is gone | `docs/the-record-layout.md:17` | confirmed | executed: no `(F<n>` citation remains in any rule file |
| 🟢 | round 1's finding 8 is closed — the case pins `tests-todo.md` where `process_plan` reads it | `tests/test_the_set_a_work_item_always_has.py:308` | confirmed | read: `settle.py:773` and `:824-856` match the docstring; the module passes; the remaining `evidence-todo.md` strings are near-miss names and #942's fixtures |
| 🟢 | round 1's open question is answered — the W2 kernel cases and the S11 pins were seen red | `tests/test_a_unit_is_bounded_where_a_parser_decides.py` | confirmed | executed: 8 `mutation-check` runs over W2 and S11, each red on the case the phase record names; 13 of the 21 listed were not re-run |
| 🟢 | the fix range's six new units hold as code | `tests/test_the_rules_command_reads_each_rule_off_its_test.py:111` | confirmed | read and executed: no defect; the `[top]` case is red on the pre-fix code by reading |
| 🟢 | 8a63e245 restores the workflow byte for byte, and its durations file prices the suite | `.github/workflows/test.yml:94` | confirmed | executed: blob `db3d18bc` before e05213e0 and at the tip; the durations case passes with 9,214 collected |
| 🟢 | 6b6c5248's price level matches the checker, and the PR body's one line it reads is present | `seal/budgets.md:49` | confirmed | executed: exit 0 with the body, exit 1 with an empty one naming only the `slow-file` raise; the six `unenforced:` lines are inert |

## Paste-ready fixes

```markdown
| tests/test_pact_check.py | 157 |
```
```
Budget raised: slow-file:tests/test_pact_check.py 120 -> 157: measured 121 s at the corrected price level on one Windows run (raw 137 s at x1.132), listed at 1.3 times that reading as seal/budgets.md states for a one-sided row; locally the file takes 22.2 s on both the base and this branch, so the file did not grow
```
```markdown
| `.test_durations` is pruned, then refreshed | `plan.md` phase 4 "`.test_durations` from the run's `test-durations` artifact" / phase 4 removed the deleted files' entries and carried the 54 moved and renamed cases' Windows prices; 8a63e245 replaced the file with run 38646055747's unsharded Windows leg, which dropped 2,655 ids nothing collects | the build, then the orchestrator | no run existed without a push; the refresh came once the pull request was open |
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on the four fixed modules, `tests/test_a_folded_statement_names_what_enforces_it.py` and `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, at 475c666f | 232 passed, 2 skipped (the two need the whole suite collected), exit 0 |
| `bin/test tests -q -k "test_the_durations_file_prices_the_suite or test_no_collected_id_carries_the_interpreters_path"` | 2 passed, 9,212 deselected, exit 0 |
| `budget_check.py --baseline origin/release/v0.22.0 --pr-body-env PRB --base-ref release/v0.22.0` with the PR body | exit 0; `slow-file:tests/test_pact_check.py` 121 against 121, 0.0 % headroom (🟡 1) |
| the same with an empty body | exit 1; only `slow-file:tests/test_pact_check.py 120 -> 121` is asked for |
| the same with the ceiling at 157 and the body's line at `120 -> 157`, the file then restored | exit 0, 36 s headroom; with the body unchanged, exit 1 naming the line |
| `mutation-check`, 11 runs: five W2 kernel units, three S11 pins, three round-1 fixes | all 11 `red`, exit 0; `git status` clean after |
| `git show` of e05213e0 and 8a63e245 for `.github/workflows/test.yml` | `db3d18bc → 8605019a → db3d18bc` |
| `.test_durations` read at base, e05213e0 and HEAD for `tests/test_pact_check.py` | 81.0 s / 81.0 s / 136.6 s over 68 ids; entries 13,482 / 11,863 / 9,208 |
| a scan of the 61 rule files for visible bold-led paragraphs 4 or more spaces in | 5 lines, all inside an HTML comment in `templates/sdd-round.md` |
| the PR's CI | read, not run: at the time of reading, four pytest legs were still pending |
| the broad gate (full suite, lint, typecheck) | not yet — the sealer's, once, after the rounds settle; nothing above stands for it |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `.github/scripts/rules.py:139` | round 1's 🟡 1 — fixed |
| round-1 | `.github/scripts/rules.py:73` | round 1's 🟡 2 — fixed |
| round-1 | `.github/scripts/budget_check.py:219` | round 1's 🟡 3 — fixed |
| round-1 | `docs/the-record-layout.md:243` | round 1's 🟡 4 — fixed |
| round-1 | `skills/implement/orchestration.md:56` | round 1's 🟡 5 — fixed |
| round-1 | `seal/follow-up.md:74` | round 1's 🟡 6 — fixed |
| round-1 | `docs/the-record-layout.md:17` | round 1's 🟡 7 — fixed |
| round-1 | `tests/test_the_set_a_work_item_always_has.py:308` | round 1's 🟡 8 — fixed |
| round-1 | `tests/test_a_unit_is_bounded_where_a_parser_decides.py` | round 1's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
