# Implementation Plan: 1793240970-a-rename-runs-red-first-cases-as-new-behaviour

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 and 2.

## Summary

The crafter writes a case first and runs `seal mutate` on every phase,
whatever the phase changes, so a rename or a move pays for proof its
existing cases already give. This work states, in one row of
`skills/verify/SKILL.md`'s *What changed* table, what proves a change of
names or places: the existing cases at the new name or path, and a census
showing the old spelling is gone. The crafter's steps 5 to 8, the
implement skill's test-first section, the review's regression-test judgment
and the sealer's `seen red` rule read that row. The phase-boundary run
becomes one command over the plan row's cases and the modules that read a
changed path, in the crafter, in contract rule 2 and in the *Scope* table.
A new crafter eval case holds the row and is seen red against the base's
definitions before the text changes.

## Technical context

The existing text this builds on, at `1e82fd0a`:

- `agents/crafter.md:40-43`: step 5, "each case first, seen red against the
  tree as it stands"; step 6, "Commit, then run `seal mutate` over each unit
  you added"; step 7, "Run the narrow checks through the repository's
  runner". `:107-119`: **Mutation-test every unit you added, one command
  each.** `:127-132`: **Find the runner, and type the narrow form.**, which
  ends "run one module at a time".
- `skills/verify/SKILL.md:326-337`: the *What changed / What can fail*
  table, four rows and no row for names or places. `:293-299`: the *Scope*
  table, whose *Phase boundary* row reads "the module the phase changed and
  the ones it touches, in parallel". The file carries no `check:` line
  today, and `.github/scripts/rules.py#RULE_FILES` reads it as a rule file
  (`skills/*/SKILL.md`).
- `skills/implement/SKILL.md:229-236`: "Each scenario is built the same way:
  its case first, seen red against the tree as it stands".
- `skills/agent-contract/SKILL.md:38-39`: "your module and the ones it
  touches at a phase boundary".
- `skills/code-review/SKILL.md:72-76`: the *Probes and regression tests*
  table, whose *Regression test* row is "a test that should exist and does
  not".
- `agents/sealer.md:132-136`: **A `seen red` is re-run against the code
  before the change.**
- `evals/scripts/rule_cases.py:325-449`: `CRAFTER_BUILDS` and
  `crafter_case`, the four build cases. `:237-242`: `shape_tool`, whose
  `max: 0` already carries `min: 0`. `:797-803`: `cases()`.
- `evals/scripts/noninferiority.py:1557-1567`: `run` takes `--rev`,
  `--suite-rev`, `--case`, `--runs` and `--max-cost-usd`, so one case can
  be run against the base's definitions with the branch's suite.
- The cases that pin sentences this work rewrites:
  `tests/text/test_the_handoff_before_round_one.py:84` and `:128-140`,
  `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py:76`,
  and `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:350-358`.
  `tests/behaviour/test_chain_hooks_hardening.py:1065` finds step 5 by
  "Build the phase as a vertical slice", and
  `tests/behaviour/test_the_sealer_guarantees.py:288-300` holds step 3 of
  the sealer to two acts and no word `touches`. Both constrain where the new
  sentences stand.

**What breaks in six months.** A crafter calls a change a rename when it
also changed a default, an argument or an output, and skips the case that
change owed. The row names that case as the *Logic* row, and the proofer
reads the diff against the phase record's claim. The second failure: the
rename case is a paid eval, and nothing in CI runs it (`evals/README.md`:
"Nothing in the tree makes a later edit owe a run"). A later rewording that
brings the old cadence back is caught at the next preload comparison of the
crafter, not at its own pull request.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the structure: the cadence stays unconditional, and the orchestrator tells each rename phase in its spawn prompt to skip it | The issue's own record: a spawn prompt is the only place that instruction lives, so the next work item meets the old cadence. #1051's phase 1 ran nine mutation runs and about ninety modules one per command before the orchestrator stepped in | Rejected. The premise that keeps it, that the prompt reaches every phase, is false by the issue's coordinate `4420ebd5:seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/phases/phase-1.md` |
| Replace the structure: the cadence reads what changed, from one new row of the verify table, and every party cites that row | A crafter misfiles a behaviour change as a rename (*What breaks in six months*) | Chosen. One source, and the four readers cite it |
| Exempt by the ladder's rung: a work item on the refactor rung owes no red-first case | The rung is set per work item from whether anything observable changes. A work item that adds behaviour and renames sits on the top rung, so its renames would still owe the full cadence, which is #1051's shape | Rejected. What decides the proof is what can fail, which the verify table already sorts by |
| Hold the new row with a `tests/text` case that reads its words | It pins the row's wording and reads nothing a crafter does. #1111 removed this shape from the contract module for that reason | Rejected |
| Hold the new row with a crafter eval case that renames, graded on files and tool calls | Paid to run, and run by no CI (*What breaks in six months*) | Chosen. It is the only reader of what a crafter does under the row, and `evals/README.md` names graders over outcomes as the suite's rule |
| Also give the four build cases a `shape-mutated` grader (`seal mutate`, `min: 1`), so the arm that adds behaviour is graded on its mutation run | It changes four cases' grader sets, which `evals/README.md` rule 3 then requires to pass on every run of every later side. It can be seen red only by paying for runs of a definition with step 6 deleted. The arm it would hold is a sentence this work keeps | Rejected. The build cases keep `shape-tested`, which grades the case written beside a new unit |
| The census as a new test written by every rename | Contradicts the issue's first *Done when*, "writes no new case". In a repository with no census it adds a test module per rename | Rejected. The census is an entry in an existing census or the search and its empty result in the phase record (`frame/questions.md`, the head) |
| A `Proved by` field in `templates/records/sdd-phase.md` | A new line grammar for a fact `## What this phase found` already carries | Rejected |
| Keep `run one module at a time` for the phase-boundary run | The premise that keeps it is that one module is the narrow form, as opposed to the suite. A named list in one command is narrow too, and `bin/test` runs either form with `-n auto` (`bin/test:25-27`, read). One module per command is what cost #1051's phase 1 about 39 minutes | Rejected. One command over the plan row's cases and the modules that read a changed path |
| Re-point each pin on a rewritten sentence, or remove it as #1111 did | Removed, the mutation rule and the narrow runner sentence could leave `agents/crafter.md` with nothing turning red. `test_the_handoff_before_round_one.py:93-117` records that happening once, in #107 | Re-point. Each pin guards that a rule still exists after it moved, which is a fact a reader needs |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The rename case, seen red. `evals/scripts/rule_cases.py` gains the crafter rename case of `frame/design.md` *Data & interfaces*, added to `cases()`, with the module docstring's crafter line corrected. `evals/behaviour/crafter/rule-crafter-rename/` is written by running the generator, and no other case changes | `python3 evals/scripts/rule_cases.py`, then `git status --short evals/behaviour` lists only the new directory. `bin/test tests/behaviour/test_evals_layout.py tests/evals/test_rule_cases.py tests/text/test_no_case_tells_the_agent_it_is_evaluated.py -q`. Then `python3 evals/scripts/noninferiority.py run --agent crafter --rev 1e82fd0a --suite-rev HEAD --case rule-crafter-rename --runs 2 --max-cost-usd 15 --out <scratchpad>/1793240970-a-rename-runs-red-first-cases-as-new-behaviour/base-rename.json`, with `shape-no-mutation` or `shape-no-new-case` failing on a run (`frame/questions.md` Q1 to Q3) | 771ab8c4 |
| 2 | The rule and what stood on it. The verify row and its `check:` line, and the *Scope* row; `agents/crafter.md` steps 5 to 8 and its two rules; `skills/implement/SKILL.md` *2.*; contract rule 2; `skills/code-review/SKILL.md`'s *Regression test* judgment; `agents/sealer.md`'s `seen red` rule; the four pins of `frame/design.md` *Scope* item 8 pointed at the new sentences; `changelog.md` with its `### Process changes` row | One `bin/test` command over the modules `git grep -l` finds under `tests/` naming each changed path, each re-pointed pin seen red with its old sentence put back. `bin/seal rules --check` exits 0. Then `noninferiority.py run --agent crafter --tree . --suite-rev HEAD --case rule-crafter-rename` and the same with `--case rule-crafter-slugify`, `--runs 2 --max-cost-usd 15` each, every grader passing | |

## Operational impact

No migration, environment variable, dependency or compatibility break. The
crafter's eval suite grows from four cases to five, so each later crafter
comparison pays for two more runs on each side. Every agent's preload
changes by contract rule 2's rewording, which the next preload comparison
measures. The changelog fragment carries a `### Process changes` row,
because a rename or a move stops owing a new case and a mutation run.
