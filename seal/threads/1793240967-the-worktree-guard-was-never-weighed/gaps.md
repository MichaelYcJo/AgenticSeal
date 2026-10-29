# Closing memo: 1793240967-the-worktree-guard-was-never-weighed

## Why this work exists

The worktree guard showed no catch in its record against about 7,000 lines of hook code, so it is removed, and the `automation` press reader two other gates read moves to a module of its own.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Five assertions on `consent` did not move with their cases | `frame/design.md` S2 says the moved cases each pass "unchanged in what it asserts". Phase 1 moved `test_accepts_question_1_alone_and_the_boxes_beside_it_as_the_same_press` and `test_refuses_the_boxes_asked_alone_as_giving_or_taking_back_the_press` to `tests/hooks/test_press.py` without their five `wc.consent(...)` assertions | The code: the assertions on `automation_answered` moved, and the five on `consent` were dropped | `consent` is not part of the press reader: `frame/design.md` *Scope* In 1 lists the moved names, and `consent` is not among them. It stays in `hooks/worktree_consent.py` until phase 2 removes it, and `tests/hooks/test_worktree_consent.py#Test_consent` keeps its cases until then |
| Two cases of the frozen-reading file left in phase 2, not phase 3 | `frame/plan.md` *Phases* row 3 deletes `tests/behaviour/test_the_frozen_reading_never_grows.py`, and row 2 does not name it. The file loaded `hooks/worktree-guard.py` when it was imported, and `test_only_the_two_fallback_arms_read_it` asserted that the guard and the consent writer were the only readers of `hooks/lib/cmdline_base.py` | Phase 2 removed the guard's load, `test_s10_a_switch_is_judged_by_the_guard` and `test_only_the_two_fallback_arms_read_it`. It kept `test_the_bytes_below_the_rider_are_86256492s` for phase 3 | With the guard deleted, the file fails at collection. The kept case stands on `cmdline_base.py` alone, and `.github/workflows/test.yml` and `tests/text/test_ci_gives_the_checks_what_they_need.py` still cite it until phase 3 moves the citation |
| Three citations of the deleted document rewritten in phase 2 | `frame/plan.md` *Phases* row 4 rewrites `skills/implement/orchestration.md:353,357`, and row 3 deletes `hooks/lib/tokens.py`. Both files cited sections of `docs/worktree-guard-spec.md` | Phase 2 rewrote the three citations in the commit that deletes the document. The two in `orchestration.md` now cite `docs/the-routing-check.md` *The edit check*, as row 4 states. The one in `tokens.py` names no document | `tests/behaviour/test_a_cited_section_stands_in_its_file.py#test_every_cited_section_stands_in_its_file` refused all three once the document was gone (executed, exit 1 before the rewrite, exit 0 after) |
| Comments and docstrings rewritten in phase 2, not phase 4 | `frame/plan.md` *Phases* row 4 rewrites the comments in `hooks/dispatch.py`. Neither row names the comment in `tests/conftest.py` *helpers more than one test module uses*, the docstring of `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py`, or the `OLD_NAME` comment in `tests/censuses.py` | Phase 2 rewrote them: the `GROUPS` comments, the `run_gate` comment and the `path_part` and `describe` docstrings of `hooks/dispatch.py`, and the three test texts | Each stated a fact about code or a document phase 2 deleted, in a file phase 2 was already editing. `CLAUDE.md` *The rule a mechanism is kept against* says a change removes in the same commit what stood on the old fact |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check over phase 1's commit `ec43e94b` | the orchestrator, at the broad gate |
| The full suite, the repository-wide lint and the format check over phase 2's commit `f528f7a1` | the orchestrator, at the broad gate |

## Not done

`.test_durations` prices none of the 27 cases of `tests/hooks/test_press.py` and not the `press` parameter of `tests/hooks/test_dispatch.py#Test_draw::test_accepts_every_gate_a_broken_shared_module_breaks_and_no_other`. Phase 2 removed the file's 478 entries for the cases phases 1 and 2 removed or renamed, the 26 old ids of the moved press cases among them, and priced no new case. Neither phase's row in `frame/plan.md` names pricing a case. `CONTRIBUTING.md` *Running the checks* says the file is refreshed from the `test-durations` artifact of the branch's latest `tests` run, and that `test_the_durations_file_prices_the_suite` fails past one unpriced case in twenty or one second in twenty that belongs to entries the suite no longer collects. Against the 6,296 entries left, 28 unpriced cases stay under the first share (read, not run).

## Fed back into the design

none
