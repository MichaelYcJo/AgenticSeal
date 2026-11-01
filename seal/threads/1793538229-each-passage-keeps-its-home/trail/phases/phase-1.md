# Phase 1: 1793538229-each-passage-keeps-its-home

## What this phase found

### Whether the frame holds

It holds, read at `8d67efc0` before the first edit. Every coordinate `frame/plan.md` *Technical context* gives stands at the line it names: `agents/crafter.md:44-46`, `skills/implement/SKILL.md:53-56`, `:162-169` and `:229-231`, `skills/agent-contract/SKILL.md` rule 5, `docs/one-root-by-lifetime.md` *What the repository decides for itself, and how it is read*, and the module's `shared_counts`, `BASELINE` and the two cases that read the tree's largest pair. The measure's row K2 and *Instances K2* stand at `79252e48` as design G6 quotes them. #1102 is open in `release: 0.29.0` (executed: `gh issue view 1102`). Each reader design G12 names was read, and each keeps the words it needs: "Build the phase as a vertical slice" in `agents/crafter.md`, `` `docs/the-review-record.md` `` and "handoff" and "Record language" in `skills/implement/SKILL.md`, and the one git listing in `corpus`.

### Departures from the frame

- **S3's case is a second parameter of the existing paste case, not a function of its own.** `test_a_paste_is_named_with_the_pair_the_run_and_the_act` already plants twenty words of one rule document into a new one and asserts the pair, the count, the run and the act. S3 asks the same of a definition pasted into a skill, so the case takes `(source, planted)` and runs as `[CONTRIBUTING.md-docs/planted.md]` and `[agents/crafter.md-skills/planted/SKILL.md]`. Judged against `agents/crafter.md` *A new test starts from its group*: a case is added to the group that covers its function.
- **The docstring states the definition pair under *What is counted*, not *What is read*.** `corpus` still reads every definition, and the filter acts in `shared_counts`, so *What is read* is unchanged and *What is counted* says which pairs leave the count and why. Scope item 7 asks for "what is read and left out"; the section that names the act is the one that changed. Judged against `frame/design.md` *Data & interfaces*, which puts the filter in `shared_counts` and leaves `corpus` unchanged.
- **One constant, `DEFINITIONS = "agents/"`, is added beside `TOP_DIRS`.** The filter names it twice, and the comment over it points at the docstring section that gives the grounds. No other unit is added.

### Seen red

- **S4** (`test_a_run_two_definitions_share_is_not_counted_and_one_beside_a_skill_is`), executed: run against the module at the base, before the filter was written, it failed with `Left contains 1 more item: {('agents/a.md', 'agents/b.md'): 1}`. The other eight cases passed in the same run.
- **S3**, executed: `seal mutate` at `43eaa555` replaced `and pair[1].startswith(DEFINITIONS)` with `or pair[1].startswith(DEFINITIONS)`, so every pair holding an `agents/` path left the count. Verdict `red`: `[agents/crafter.md-skills/planted/SKILL.md]` failed at `assert named, found` with `found` empty.
- **The filter itself**, executed: `seal mutate` replaced the same text with `and False`, so no pair left the count. Verdict `red`: S4 failed with the definition pair counted.
- **S5**, executed: `seal mutate` of `over_baseline`'s `if count > allowed:`. To `>=`, verdict `red`: `test_a_count_over_its_baseline_is_named_and_one_at_it_is_not` named the planted pair at 26 runs where 26 were measured. To `!=`, verdict `red`: `test_a_removed_copy_passes_without_a_baseline_edit` named the pair at 18 runs where 26 were measured. Each mutant was restored by `seal mutate` from its held bytes, and `git status` was clean after the four runs.

The planted pair shares 40 placeholder words, 26 windows of 15. The removed-copy case deletes the word at index 7 of the first shared window, which breaks the 8 windows that hold it and leaves 18. A shorter passage would let the deletion break every window, and the case's `0 < after` would then fail for the wrong reason.

### The count after the change

Executed at `43eaa555`: `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py -q -p no:xdist`, 9 passed. With `BASELINE` holding only the two `README.md` entries, `test_no_pair_shares_more_than_it_was_measured_at` passing means no pair the module counts shares a run, except the two `README.md` pairs at or below their entries. The three pairs Scope items 1 to 3 linked, `agents/crafter.md`, `docs/one-root-by-lifetime.md` and `skills/agent-contract/SKILL.md` each with `skills/implement/SKILL.md`, share none, and neither does `README.md` with `skills/parity-setup/SKILL.md`. The case reads "at or below", so it does not show that each `README.md` pair is still at its stored count; design P1 measured both at their counts at the base, and this phase changed neither file.

### The phase-boundary run

Executed at `43eaa555`: one `bin/test -q` over 82 modules, 4985 passed, 9 skipped, 2 failed, in 90.85 s. The set is every module under `tests/` that names `crafter.md`, `skills/implement/SKILL.md` or this module, joined to every module that lists files (`glob`, `listdir`, `ls-files`, `walk`, `iterdir` or `git_listing`) and names `agents`, `skills` or `.md`. That is a `git grep`, so the set is a sample of the modules that read a changed path: a module reaching the files through a path built elsewhere is not on it (contract rule 12). The broad gate is the orchestrator's.

The two failures, each read:

- `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` named this work item: it had no `gaps.md` yet. This phase writes it.
- `tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census` named `seal/threads/1793538229-each-passage-keeps-its-home/frame/design.md:24`: the probes paragraph names the interpreter by a path under a real user's home directory, and the census `real_identifiers` refuses one. The line came with the frame at `8d67efc0`, and `frame/design.md` is not a file this phase writes, so it stands for the orchestrator (`gaps.md` *Not verified*).

### Citations, read

`git grep -n` at `43eaa555` finds each citation S1 names: `agents/crafter.md:45-47` cites `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test*; `skills/implement/SKILL.md:53-55` cites `docs/one-root-by-lifetime.md` *What the repository decides for itself, and how it is read*; `skills/implement/SKILL.md:161-164` keeps the route to `docs/the-review-record.md`'s handoff and cites `contract rule 5`. `tests/behaviour/test_a_cited_section_stands_in_its_file.py` was in the boundary run and passed, so each cited section and rule stands.
