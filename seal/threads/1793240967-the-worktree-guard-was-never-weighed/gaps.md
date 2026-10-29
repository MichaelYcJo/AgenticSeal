# Closing memo: 1793240967-the-worktree-guard-was-never-weighed

## Why this work exists

The worktree guard showed no catch in its record against about 7,000 lines of hook code, so it is removed, and the `automation` press reader two other gates read moves to a module of its own.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Five assertions on `consent` did not move with their cases | `frame/design.md` S2 says the moved cases each pass "unchanged in what it asserts". Phase 1 moved `test_accepts_question_1_alone_and_the_boxes_beside_it_as_the_same_press` and `test_refuses_the_boxes_asked_alone_as_giving_or_taking_back_the_press` to `tests/hooks/test_press.py` without their five `wc.consent(...)` assertions | The code: the assertions on `automation_answered` moved, and the five on `consent` were dropped | `consent` is not part of the press reader: `frame/design.md` *Scope* In 1 lists the moved names, and `consent` is not among them. It stays in `hooks/worktree_consent.py` until phase 2 removes it, and `tests/hooks/test_worktree_consent.py#Test_consent` keeps its cases until then |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check over phase 1's commit `ec43e94b` | the orchestrator, at the broad gate |

## Not done

`.test_durations` was left as it was. It still prices the 25 moved cases under `tests/hooks/test_worktree_consent.py` and the labels case under the deleted `tests/behaviour/test_the_guard_asks_once_per_session.py`, and it prices none of the 27 cases of `tests/hooks/test_press.py`. Phase 1's row in `frame/plan.md` names no change to the file. `CONTRIBUTING.md` *Running the checks* says the file is refreshed from the `test-durations` artifact of the branch's latest `tests` run, and that `test_the_durations_file_prices_the_suite` fails only past one case or one second in twenty. Against the 6,774 cases and 1,235.6 s `frame/design.md` *The record* counts, 27 unpriced cases and the 26 stale entries' 9.9 s stay under both shares (read, not run).

## Fed back into the design

none
