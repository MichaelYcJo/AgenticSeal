# Closing memo: 1794271938-follow-up-holds-seven-owner-questions

## Not verified

- nothing
  why: Phases 1 and 2 ran each claim they make, as `trail/phases/phase-1.md` and `trail/phases/phase-2.md` record. The broad gate is the orchestrator's, and `trail/gate.md` will record its run.

## Not done

Phase 1 leaves the `isinstance(a.value, str)` filter of `tests/github/test_close_issues_on_release.py#argv_words` without a case. A `seal mutate` run that removed it survived. No argv in the three scripts holds a constant that is not a string, so a case would need a source written for it, and *Scope* item 1 asks for none (`trail/phases/phase-1.md`).

Phase 2 leaves `seal/follow-up.md:44` citing the case by its old name, `test_the_template_PARSES_into_the_three_answers_it_ships`. So `tests/behaviour/test_a_cited_section_stands_in_its_file.py::test_every_cited_name_stands_in_its_file` is red from `4d8031dc0` until phase 3 removes that row. Correcting the citation was within reach. It is not a file the crafter's *Job* names, and *Scope* item 5 removes the row whole in phase 3 (`trail/phases/phase-2.md`).
