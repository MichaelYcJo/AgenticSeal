# Closing memo: 1794271938-follow-up-holds-seven-owner-questions

## Not verified

- nothing
  why: Phases 1, 2 and 3 ran each claim they make, as `trail/phases/phase-1.md`, `trail/phases/phase-2.md` and `trail/phases/phase-3.md` record, and fix pass 1 ran its own, as its close blocks in `trail/rounds/round-1.md` record. The broad gate is the orchestrator's, and `trail/gate.md` will record its run.

## Not done

Phase 1 leaves the `isinstance(a.value, str)` filter of `tests/github/test_close_issues_on_release.py#argv_words` without a case. A `seal mutate` run that removed it survived. No argv in the three scripts holds a constant that is not a string, so a case would need a source written for it, and *Scope* item 1 asks for none (`trail/phases/phase-1.md`).

Fix pass 1 leaves the `ast.Tuple` half of `argv_words` without a case. No script holds a tuple argv, so removing that half leaves the three cases green at HEAD. A tuple argv planted in each script turned each case red, and the same plants stayed green before the fix (`trail/rounds/round-1.md`, finding 1). A case that keeps the half would need a source written for it, as the filter above would, and the finding asks for the reader and its plants, not a case.

Phase 2 left `seal/follow-up.md:44` citing the case by its old name, `test_the_template_PARSES_into_the_three_answers_it_ships`. So `tests/behaviour/test_a_cited_section_stands_in_its_file.py::test_every_cited_name_stands_in_its_file` was red from `4d8031dc0` until `470b27194`, where phase 3 removed the row. Correcting the citation was within reach. It is not a file the crafter's *Job* names, and *Scope* item 5 removed the row whole in phase 3 (`trail/phases/phase-2.md`, `trail/phases/phase-3.md`).

Phase 3 leaves two cases of `tests/test_conftest.py` failing, `Test_census_case::test_accepts_a_target_every_census_passes` and `Test_census_case::test_refuses_a_target_one_census_flags_naming_it`. Both raise `FileNotFoundError` in `tests/censuses.py#_root_names`, which loads `lib/optin.py` from a `ROOT` the cases point at a `tmp_path`. They fail the same way at `8e28e0ff0`, and this branch changes neither file nor the cases, so the failure predates the work item. Repairing it was within reach. It is outside every *Scope* item, and `agents/crafter.md` *Never* forbids building beyond the request; the orchestrator names it as a follow-up (`trail/phases/phase-3.md`).
