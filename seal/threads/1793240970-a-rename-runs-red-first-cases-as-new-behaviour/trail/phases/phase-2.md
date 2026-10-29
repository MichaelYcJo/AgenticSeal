# Phase 2: 1793240970-a-rename-runs-red-first-cases-as-new-behaviour

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | a2464236 |

## What this phase was asked

Build `plan.md` row 2: the verify row for a change of names or places and
its `check:` line, and the *Scope* table's *Phase boundary* row;
`agents/crafter.md` steps 5 to 8 and its mutation and runner rules;
`skills/implement/SKILL.md` *2. Implement test-first*; contract rule 2; the
*Regression test* row of `skills/code-review/SKILL.md`; the sealer's
`seen red` rule; the four pins of `frame/design.md` *Scope* item 8 pointed
at the new sentences; and `changelog.md` with its `### Process changes` row.
Then run the rename case and `rule-crafter-slugify` against the branch's
definitions, paying as `frame/questions.md` Q1's default says.

## What this phase found

The first narrow run failed six cases in three modules, and each refused a
copy the frame's wording would have made (executed):

- `tests/text/test_a_moved_rule_leaves_its_definition.py` and
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py` refused the
  phase-boundary set written out three times, in contract rule 2, the
  *Scope* row and the crafter's step 7. The set is stated once, in rule 2.
  The *Scope* row reads "the set contract rule 2 names for a phase boundary,
  as one command", and step 7 reads "Run the phase-boundary set contract
  rule 2 names, as one command through the repository's runner". The
  crafter's runner rule says "type step 7's one command, never the whole
  suite", and the pin in
  `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py`
  holds that sentence.
- The same passage check refused step 5's first wording, "its case first,
  seen red ...", as a fourth shared run with `skills/implement/SKILL.md`,
  where three were measured. Step 5 keeps "each case first", the crafter's
  own spelling before this work.
- `tests/text/test_a_language_section_of_writing_style_opens_alone.py`
  refused `## What this phase found` named inside step 8, which it reads as
  a heading of the writing-style skill. So step 5 says where a rename's
  proving cases and census go, and step 8 is unchanged.

`gaps.md` records the last two as divergences from `frame/design.md`
*Scope* items 3 and 5.

`mutation_check.py`'s docstring also stated the crafter's rule, "break every
unit it added". It now says "every unit that adds behaviour". Rule 12's
search found no other statement of the old cadence or scope, outside the
docstring of `test_the_crafters_definition_mandates_mutating_every_unit_it_added`,
which quotes the wording of 2026-09-03 as history. The search was `git grep
-iE` over the tree outside `seal/threads` and `docs/experiments`, for "the
ones it touches", "module at a time", "unit you added", "every unit added",
"one module per", "module by module", "case first, seen red",
"mutation-test", "every unit" and "phase boundary".

The narrow run, one `bin/test` command over the 103 test modules that name
a path this work changed or read every agent, skill, eval case or work-item
record: 4815 passed, 11 skipped, exit 0 (executed). The list came from `git
grep -l` under `tests/` for each changed path's spellings, `crafter.md`,
`sealer.md`, `agent-contract`, `code-review`, `implement`, `verify`,
`mutation_check`, `rule_cases`, `rule-crafter`, `changelog.md` and
`seal/threads`, with the modules that glob `agents/*` or `skills/*` added.
`bin/seal rules --check`: 267 check lines in 55 rule files hold, exit 0
(executed). `uvx ruff check` and `uvx ruff format --check` over the four
changed Python files: exit 0 (executed).

Each re-pointed sentence was put back to its old wording by `seal mutate`,
committed first at a2464236, and every run read `red`, exit 0 (executed):

- step 6, "over each unit you added.":
  `test_the_crafters_definition_mandates_mutating_every_unit_it_added`
  failed;
- the rule's lead, "Mutation-test every unit you added, one command each.":
  that case and
  `test_the_crafters_definition_names_the_command_and_no_directory_to_clear`
  failed;
- the runner rule, "run one module at a time":
  `test_crafter_finds_the_runner_before_inventing_a_command` failed;
- the absence pin, with "Mutation-test every unit that adds behaviour."
  written into `docs/the-review-record.md`:
  `test_the_protocol_no_longer_states_the_rules_it_points_at` failed;
- the verify row's `check:` line pointed at `rule-crafter-renamed/`:
  `bin/seal rules --check` refused it, "holds no case.yaml".

The phase adds no code unit, so no other mutation run is owed.

The paid runs used `--case '*rule-crafter-rename'` and
`--case '*rule-crafter-slugify'`, for the reason phase 1 found (executed):

- `noninferiority.py run --agent crafter --tree <worktree> --suite-rev HEAD
  --case '*rule-crafter-rename' --runs 2 --max-cost-usd 15`, exit 0: every
  grader passed on both runs, and neither run called `seal mutate`. $1.28 in
  all, $0.63 and $0.65 a run, 83 and 80 seconds.
- The same with `--case '*rule-crafter-slugify'`, exit 0: every grader
  passed on both runs, `shape-tested` among them. Run 0 called `seal mutate`
  twice and run 1 once, so the arm that adds behaviour still mutates. $1.19
  in all, $0.52 and $0.67 a run, 78 and 80 seconds.

Both sides ran against a2464236's definitions and suite. Their saved output
is `branch-rename.json`, `branch-slugify.json` and their `.raw/` directories
in the session's scratchpad, beside phase 1's base side. With phase 1's
$1.12, the work item's six runs cost $3.59.
