# Design: 1793240970-a-rename-runs-red-first-cases-as-new-behaviour

Issue #1091, milestone `release: 0.24.1`. The base is `1e82fd0a` on
`release/v0.24.1`, and the branch is
`fix/1091-a-rename-runs-red-first-cases-as-new-behaviour`. Every coordinate
below is read at that base unless it names another commit.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against*: "A rule's proof is the test or behaviour eval its `check:` line names", and "A check gates only a fact it reads; a noisy reading, or one guessed from words, is a report" | The new row is held by a behaviour eval case that reads what a crafter does on a rename, not by a case that reads the row's words. #1111's frame (`seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/frame/design.md` *Grounding*) applied the same sentence to the contract's phrase pins |
| `CLAUDE.md`, the same section: "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact" | Each sentence stating the unconditional cadence is rewritten where it stands, and each case pinning the old sentence is corrected in the same commit |
| `CLAUDE.md`, the same section: "A fact has one source, and every other place links to it" | The rule lives in one place, the new row of `skills/verify/SKILL.md`'s *What changed* table. The crafter, `skills/implement/SKILL.md`, `skills/code-review/SKILL.md` and the sealer cite that section and do not restate the row |
| `docs/the-broad-gate.md` *A check that cannot fail is not a check*: arms are mutated under "the same rule new cases are held to, seen red before it is committed" | The policy speaks of new cases only, so a rename that writes none breaks no clause of it. No `docs/` sentence states the crafter's cadence (executed: `git grep -n -iE 'seen red\|red-first\|red first\|seal mutate\|mutation\|test-first\|What changed' -- docs/` outside `docs/experiments/` gives four hits: `docs/one-root-by-lifetime.md:226`, `docs/release-checklist.md:198`, `docs/the-broad-gate.md:148` and `docs/the-review-record.md:144`, and none states what a build phase runs) |
| `docs/the-review-record.md` *The handoff*: "the form handed over is the narrow one" | One command over the phase's cases and the modules that read a changed path is still the narrow form. The clause says nothing of one module per command, so moving the crafter off `run one module at a time` needs no rule change |
| Contract rule 2 (`skills/agent-contract/SKILL.md:36-46`): "your module and the ones it touches at a phase boundary" | "The ones it touches" is the reading that let #1051's phase 1 run about ninety modules one by one. Rule 12 asks for every statement of the phase-boundary scope, so rule 2 is rewritten in place with the crafter and the *Scope* table. The rule keeps its number |
| Contract rule 15: "A new case is not planted until it has been seen red" | Unchanged. A rename writes no new case, so it owes no red. The eval case this work adds is a new case, so it is seen red against the base's definitions first |
| `skills/implement/SKILL.md` *3. The SDD file set*, the ladder's second rung: "a refactor, a performance pass, a formatting sweep" owes the closing memo only | The ladder already treats a change that alters nothing observable as lighter. The cadence in *2. Implement test-first* does not read it, which is the gap the issue names |
| `CONTRIBUTING.md` *A rebuilt module's record carries its move check or its mutation table*: where `seal layout --moved` exits 0, "the group's cases were only moved and the record has no mutation table" | This repository already exempts a proven move from mutation for test modules. The new row states the same exemption for every rename or move |
| `docs/the-reader-registry.md` *A frame names what its work removes* | `## Removes` below names the three clauses this work takes out |
| `evals/README.md` *The behaviour suite*: "Every grader reads an outcome, never a sentence of a definition", and "The cases are generated, never edited by hand" | The rename case is written by `evals/scripts/rule_cases.py`, and its graders read files and tool calls |

## Scope

**In.**

1. **The rule, in one place.** `skills/verify/SKILL.md` *The narrow command
   still has to be able to fail* gains a row in its *What changed / What can
   fail* table for a change of names or places. What can fail is every file
   that named the old name or path. The existing cases, run at the new name
   or path, prove it, together with a census showing the old spelling is
   gone from the files no case imports. Such a change owes no case written
   new and no `seal mutate` run, because no behaviour was added. A unit whose
   body, signature or output changes beside its name is the *Logic* row, not
   this one. Directly below the table stands one `check:` line naming
   `evals/behaviour/crafter/rule-crafter-rename/`.
2. **The census.** In this row, the census means one of two things. Where the
   repository keeps a census of old spellings, such as this repository's
   `tests/censuses.py#old_names`, the old spelling is added to it. Otherwise
   the search for the old spelling and its empty result go into the phase
   record. Neither is a case written new (`frame/questions.md`, the head).
3. **The crafter reads the row first.** `agents/crafter.md` *Order of work*:
   - Step 5 opens by reading that table for what the phase changes. Where
     a unit adds behaviour, step 5 stands as it is today: each case
     first, seen red, then the code, then the case green. Where a unit is
     only renamed or moved, the phase names the existing cases that prove it
     and the census, and writes no case new for it.
   - Step 6 runs `seal mutate` over each unit that adds behaviour. A unit
     that was only renamed or moved owes no run.
   - Step 7 runs, in one command through the repository's runner, the cases
     the phase's plan row names and the test modules that read a path the
     phase changed.
   - Step 8's record says, under `## What this phase found`, which existing
     cases proved a rename or a move.

   In *Rules*, **Mutation-test every unit you added** narrows to the units
   that add behaviour and cites the verify row. **Find the runner, and type
   the narrow form** replaces `run one module at a time` with the one
   command of step 7. A phase that both renames and adds behaviour owes the
   full cadence for the units that add behaviour and none for the units it
   only moved.
4. **The skill that teaches the cadence.** `skills/implement/SKILL.md` *2.
   Implement test-first* says each scenario that adds behaviour is built
   case first, and that a rename or a move is proved as the verify row
   says. It cites the row and does not copy it.
5. **The phase-boundary scope, everywhere it is stated.** Contract rule 2's
   "your module and the ones it touches" and the *Scope* table's *Phase
   boundary* row in `skills/verify/SKILL.md` ("the module the phase changed
   and the ones it touches, in parallel") become step 7's set, in one
   command. Rule 12's enumeration (executed): `git grep -n -iE 'the ones it
   touches|module at a time|phase boundary|module by module|one module per'`
   over `agents`, `skills`, `docs` without `docs/experiments`,
   `CONTRIBUTING.md`, `templates` and `README.md` gives four hits. Three are
   these places, with the crafter's `run one module at a time`. The fourth,
   `skills/code-review/orchestration.md:21`, is about not resuming a crafter
   across phases and states no run.
6. **The review and the seal read the same row.**
   - `skills/code-review/SKILL.md` *Probes and regression tests*: the
     *Regression test* row's judgment, a test that should exist and does
     not, cites the verify row. A rename or a move owes no new case and no
     mutation run, so a review round does not raise one as missing.
   - `agents/sealer.md` *Rules*, **A `seen red` is re-run against the code
     before the change**: a unit the phase record says was only renamed or
     moved claims no `seen red`. Its claim is that the existing cases it names
     pass at HEAD, which the sample re-runs as an `executed` claim. Step 3
     keeps its two acts.
7. **The case that holds the rule.** `evals/scripts/rule_cases.py` gains a
   crafter rename case, written to
   `evals/behaviour/crafter/rule-crafter-rename/`. Its fixture is the
   textutil project every rule case builds. Its frame asks for `shout` to be
   renamed to `exclaim` in `src/textutil.py`, in `tests/test_textutil.py`
   and in one line of `README.md` that the case's scaffold adds. Its graders
   are listed under *Data & interfaces*. The four build cases
   (`rule-crafter-slugify` and the rest) are unchanged and remain the arm
   that adds behaviour: each grades a case written beside the new unit.
8. **What stood on the old sentences.** Each case asserting a sentence this
   work rewrites is corrected in the same commit:
   - `tests/text/test_the_handoff_before_round_one.py:84` and `:128-140`;
   - `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py:76`;
   - `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:354`.

   Each is pointed at the new sentence, because each one guards a fact a
   reader needs: that the mutation rule still exists after a move, and that
   the crafter's runner sentence names a narrow form and not the full
   suite. `rule_cases.py`'s docstring, which says the crafter cases are
   "four one-phase builds", is corrected too.
9. **The changelog fragment.** `changelog.md` carries a `### Process
   changes` row in the shape of `templates/records/process.md`, because this
   work changes the way of working.

**Out.**

- **A rule change in `docs/`.** No section of the policy root states the
  cadence (*Grounding*), so `## Rule changes` holds the no-change block.
- **Contract rule 15's wording.** It is about new cases, and a rename
  writes none.
- **The proofer's own runner sentence**, "Type the narrow form, one module"
  (`agents/proofer.md:142`). It is about the reviewer's runs and probes.
  The issue names the implementing agent's runs, and the review of a rename
  is reached through `skills/code-review/SKILL.md` above.
- **A grader that the build cases run `seal mutate`.** Weighed in `plan.md`
  *Alternatives considered* and rejected there.
- **The phrase pins this work does not touch.** #1111's count of the other
  modules is that work's.
- **A new field in `templates/records/sdd-phase.md`.** The existing
  `## What this phase found` section carries the cases a rename was proved
  by, so no new line grammar is added.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given a phase whose plan row only renames `shout` to `exclaim`, when the crafter builds it, then no Bash call runs `seal mutate`, `tests/test_textutil.py` still holds exactly one test function, `src/textutil.py` defines `exclaim` and names no `shout`, `README.md` names no `shout`, and `trail/phases/phase-1.md` names the existing case that proved it | `evals/behaviour/crafter/rule-crafter-rename/`. Seen red with `python3 evals/scripts/noninferiority.py run --agent crafter --rev 1e82fd0a --suite-rev HEAD --case rule-crafter-rename`, and green with the same command at `--rev HEAD` |
| S2 | Given a phase that adds `slugify`, when the crafter builds it, then a case beside the unit calls `slugify`, and the phase still writes its case first and runs `seal mutate` over the new unit | `evals/behaviour/crafter/rule-crafter-slugify/` (`shape-tested`), unchanged by this work, run on the branch side with `--case rule-crafter-slugify`. That the case came first and was mutated is read by the proofer from the phase record |
| S3 | Given the verify skill, when a reader opens *The narrow command still has to be able to fail*, then its table has a row for a change of names or places, and a `check:` line below the table names the rename case | `bin/seal rules --check` exits 0, which it cannot until `evals/behaviour/crafter/rule-crafter-rename/case.yaml` exists |
| S4 | Given a phase boundary, when the crafter runs its narrow checks, then it runs the plan row's cases and the modules that read a changed path in one command, and contract rule 2 and the *Scope* table state the same set | The corrected case at `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:354`, seen red with the old sentence put back. That rule 2 and the *Scope* table state the crafter's set is read by the proofer at review: no case reads either sentence's set today, and a phrase pin added for it would be the kind #1111 removes. `tests/text/test_broad_gate_rule.py` pins the *Phase boundary* row's label, which stays, so it stays green |
| S5 | Given a rename phase under review or seal, when the proofer judges its tests and the sealer samples its claims, then neither asks the phase for a new case, a `seen red` or a mutation run | Read by the proofer at review. The sealer's sentence stands under the rule whose `check:` names `evals/behaviour/sealer/rule-sealer-false-red/`, which this work does not change |

## Data & interfaces

No schema, endpoint or command changes. The one new data shape is the eval
case, written by a new generator function in `evals/scripts/rule_cases.py`
and added to `cases()`:

| Grader | Kind and reading |
|---|---|
| `reach-crafter` | `behaviour.reach("crafter")`, as every crafter case has |
| `shape-renamed` | regex `^def exclaim\(` over `src/textutil.py` |
| `shape-old-name-gone` | `not_contains` regex `shout` with flag `i`, so the name in any case or inside another name fails it, one grader each over `src/textutil.py`, `tests/test_textutil.py` and `README.md` |
| `shape-no-new-case` | `not_contains` regex matching a second `def test_` in `tests/test_textutil.py` |
| `shape-no-mutation` | `shape_tool("no-mutation", "Bash", ..., input_match=<seal mutate or mutation_check.py>, max=0)`, the existing helper that carries `min: 0` |
| `shape-phase-record` | `file_exists` for the phase record |
| `shape-proved-by` | regex `test_(?:shout\|exclaim)` over the phase record, so the record names the existing case |
| `shape-committed` | the existing commit grader |
| `shape-no-probe-left` | the existing `test_tmp_` grader |

The case's work item id follows the build cases' sequence
(`179000001<n>-<slug>`). Its frame is a design and a one-phase approved plan
built by `one_phase_plan`, like theirs.

## Rule changes

- nothing
  why: no section of the policy root `docs/` states the crafter's cadence, the verify table or the phase-boundary scope. The rule this work changes lives in `skills/verify/SKILL.md`, `agents/crafter.md`, `skills/implement/SKILL.md`, `skills/code-review/SKILL.md`, `agents/sealer.md` and `skills/agent-contract/SKILL.md`, all outside the policy root, and the eval case `evals/behaviour/crafter/rule-crafter-rename/` holds it.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The instruction to run the narrow checks one module per command, `run one module at a time` | `agents/crafter.md` *Rules*, **Find the runner, and type the narrow form.** | Step 7's one command over the plan row's cases and the modules that read a changed path. The orchestrator's broad run is the sweep |
| The phase-boundary set "your module and the ones it touches" | `skills/agent-contract/SKILL.md` *2 Narrow and often; the broad gate is the orchestrator's* | The same set as step 7, in the same rule, which keeps its number |
| The *Phase boundary* row's "the module the phase changed and the ones it touches, in parallel" | `skills/verify/SKILL.md` *Scope: cheap and often, broad and once* | The same row, rewritten to step 7's set in one command |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-29 by framer, before the build.
