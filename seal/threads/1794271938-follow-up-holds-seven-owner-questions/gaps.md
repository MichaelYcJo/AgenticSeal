# Closing memo: 1794271938-follow-up-holds-seven-owner-questions

## Not verified

- nothing
  why: Phases 1, 2 and 3 ran each claim they make, as `trail/phases/phase-1.md`, `trail/phases/phase-2.md` and `trail/phases/phase-3.md` record, and fix passes 1, 2, 3 and 4 ran their own, as their close blocks in `trail/rounds/round-1.md`, `trail/rounds/round-2.md`, `trail/rounds/round-3.md` and `trail/rounds/round-4.md` record. The broad gate is the orchestrator's, and `trail/gate.md` will record its run.

## Not done

Phase 2 left `seal/follow-up.md:44` citing the case by its old name, `test_the_template_PARSES_into_the_three_answers_it_ships`. So `tests/behaviour/test_a_cited_section_stands_in_its_file.py::test_every_cited_name_stands_in_its_file` was red from `4d8031dc0` until `470b27194`, where phase 3 removed the row. Correcting the citation was within reach. It is not a file the crafter's *Job* names, and *Scope* item 5 removed the row whole in phase 3 (`trail/phases/phase-2.md`, `trail/phases/phase-3.md`).

Phase 3 leaves two cases of `tests/test_conftest.py` failing, `Test_census_case::test_accepts_a_target_every_census_passes` and `Test_census_case::test_refuses_a_target_one_census_flags_naming_it`. Both raise `FileNotFoundError` in `tests/censuses.py#_root_names`, which loads `lib/optin.py` from a `ROOT` the cases point at a `tmp_path`. They fail the same way at `8e28e0ff0`, and this branch changes neither file nor the cases, so the failure predates the work item. Repairing it was within reach. It is outside every *Scope* item, and `agents/crafter.md` *Never* forbids building beyond the request; the orchestrator names it as a follow-up (`trail/phases/phase-3.md`).
