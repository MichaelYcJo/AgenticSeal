# Questions for the planner: 1793521561-a-windows-run-names-its-skipped-cases

Judgments the ticket left open that the tree answered:

- Which rung of the ladder this sits on: `frame/design.md` *Grounding*, the `skills/implement/SKILL.md` *3. The SDD file set* row.
- Whether `-rs` is the flag, as the issue offers: `plan.md` *Alternatives considered*, row 2, on `frame/design.md` *Grounding*'s probe row.
- Whether the flags go on the Windows legs alone or on every leg: `plan.md` *Alternatives considered*, rows 1 and 3.
- Whether the flags stay after the reading or leave: `plan.md` *Alternatives considered*, row 4, and `frame/design.md` *Grounding*, the `skills/core/SKILL.md` *The rule a mechanism is kept against* row.
- Which run is read, and who records the reading where: `plan.md` *Alternatives considered*, rows 8 and 9, and `frame/design.md` *Scope* item 3.
- Whether the pin may stand outside `.github/workflows/`, which the milestone note names as the item's only directory: `frame/design.md` *Grounding*, the sibling-frames row.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the three cases of #1221, and the link cases of `tests/skills/test_unverified_check.py`, pass or skip on the `windows-latest` legs? The answer is a behaviour of a CI leg on another platform. No probe can run it from a framer, which can neither push nor start a workflow. | a measurement: the run of `tests` the orchestrator dispatches on phase 1's commit, read in phase 2 | Passed: `tests/conftest.py#symlink_or_skip`'s docstring holds for the runner, and the open Windows rows of the two released work items close at the settle as answered. Skipped: the cases are unproved on Windows, the docstring's claim about the runner is false, and Q2 applies. | Phase 2 reads the run, and the record says which | open |
| Q2 | Where does a case go that phase 2 finds skipped on Windows? Before the run, nobody can know whether one will be. | the work: phase 2 records the skip; the orchestrator judges its home as a leftover | A new issue that weighs `plan.md` *Alternatives considered* row 6 and corrects the docstring. Or a row of `gaps.md` *Not verified* with that issue as its answerer. Repairing it in this work is out of *Scope*. | Phase 2 names each skipped case with pytest's reason in `trail/phases/phase-2.md` and adds a `gaps.md` *Not verified* row for it. The orchestrator files one issue for all of them and writes its number into that row as the answerer, with a row in `plan.md` *Judgments of the run* | open |
