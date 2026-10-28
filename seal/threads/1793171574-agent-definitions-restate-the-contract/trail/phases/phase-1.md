# Phase 1: 1793171574-agent-definitions-restate-the-contract

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 3eecf8a0 |

## What this phase was asked

Build `frame/plan.md`'s one phase. The 13 sentences `frame/design.md`
*Removes* lists leave `agents/crafter.md`, `proofer.md`, `sealer.md`,
`framer.md` and `tracer.md`. Each paragraph that also narrows a rule keeps
the narrowing and cites the rule as `rule <N>`. Each test assertion that read
a removed sentence is re-pointed or removed in the same commit, as the
*Removes* test rows say, and the two docstrings are rewritten in place.
Write `changelog.md`.

S1's phrase search is seen to find each phrase at the base before it is seen
to find none. S3's `seal mutate` is seen red over each sentence a re-pointed
assertion reads.

`frame/questions.md` P1 is built on its default (a): the four glosses stay.
W1, the wording of the shortened paragraphs, is the phase's, within the four
conditions the row states, and goes in this record. `agents/crafter.md:20`
and the fix-pass paragraph at `:153-162` are not edited, because #1041 edits
them after this work. Edit only the files `frame/design.md` names,
`.test_durations` if a case is renamed or removed, and this work item's
records. #913, #1039, #1042 and #1043 run in parallel on their own branches.

## What this phase found

- **The frame held at this tree.** Every line `frame/design.md` *Removes*
  names held its sentence at `6e322bb7`. `git grep` over the tree on the
  words of each sentence found the same test assertions the frame lists and
  no other reader in `tests/` or `evals/` (executed).
- **S1 at the base, then at the phase's commit.** The search reads each
  `agents/*.md` with runs of whitespace collapsed, as `tests/conftest.py#flat`
  does, for the ten phrases S1 lists. Through `git show 6e322bb7:<path>` it
  found 15 occurrences, each phrase in the file its sentence stands in.
  `post, push` was found in four files and `repository-wide lint` in three.
  Over the edited files it found 0 (executed, both runs).
- **The old assertions went red before they were re-pointed.** With the
  definitions edited and the tests untouched, `bin/test` failed exactly the
  four cases the frame names:
  `test_the_crafter_names_no_runner_of_the_broad_gate` and
  `test_the_window_the_sealer_shipped_under_is_closed` (exit 1, 2 failed, 21
  passed), `TestDefinition::test_step_1_reads_the_record_and_runs_nothing`
  (exit 1, 1 failed, 14 passed) and
  `test_the_implementer_keeps_the_half_that_makes_the_rule_its_own` (exit 1,
  1 failed, 5 passed) (executed).
- **W1, the wording chosen.** Each paragraph meets the row's four
  conditions. `rule 2` is in lower case. The crafter's paragraph names no
  party from `RUNNERS`. No paragraph shares a 15-word run with a contract
  section, which `tests/text/test_a_moved_rule_leaves_its_definition.py`
  passing shows.
  - The crafter: "The run is rule 2's, and the label is step 10's." This
    stands before the unchanged `failing on base too` and `new?` sentences.
    The second clause is there because the bold lead still says the label
    is the crafter's, and step 10 is where the removed `unverified` sentence
    lands (*Removes* row 4).
  - The proofer: "A spawn prompt that orders a check rule 2 excludes is
    declined". This replaces "one of the three", whose antecedent left with
    the removed sentence. The label audit, the `## Not judged` row and what
    comes due are unchanged.
  - The sealer: the lead is "**A missing or stale gate record earns what
    step 1 says.**", and the body is "The record holds the run rule 2
    names."
  - The proofer's *Never* bullet is "Fix the code under review." The
    tracer's step 5 is "Read constraints, enums and defaults."
- **S3, each re-pointed sentence seen red.** The baseline passed first,
  `seal mutate agents/crafter.md` ran three mutants against
  `test_the_crafter_names_no_runner_of_the_broad_gate`, and all three went
  red: `rule 2's` to `rule X's`, `` `failing on base too` `` to
  `` `failing on base` ``, and `` `new?` means `` to `` `new` means ``
  (exit 0, 3 red, 0 survived). `is the orchestrator's run's` to
  `is the orchestrator's` in `agents/sealer.md` went red against
  `test_the_window_the_sealer_shipped_under_is_closed` (exit 0). Three
  further mutants were red with exit 0: the crafter's `rule 2's` against
  `test_the_crafter_puts_both_answers_in_the_hand_back`, the sealer's
  `the run rule 2 names` against
  `test_the_window_the_sealer_shipped_under_is_closed`, and the proofer's
  `as a row` to `as a line` against
  `test_the_reviewer_has_a_field_for_the_question_the_default_produces`
  (all executed).
- **Three new units have nothing behind them.** Each was mutated against
  the modules that read its file, and each run printed `SURVIVED` with
  exit 1: the proofer's `a check rule 2 excludes` (to `rule X`), the
  sealer's new lead, and the crafter's `the label is step 10's`. Pinning
  them is a phrase pin, and `frame/design.md` *Out of scope* gives that
  decision to #1111, so no case was added. `gaps.md` *Not verified* names
  them.
- **The module docstrings.** `test_the_crafter_names_no_runner_of_the_broad_gate`'s
  docstring now says what the paragraph holds: no runner, the rule 2
  citation, and the two words. `tests/text/test_edits_go_through_the_edit_tool.py`'s
  module docstring names the proofer's half alone. Its `CRAFTER` constant
  stays, because `test_no_carrier_claims_a_fact_about_the_reader_repository`
  still reads the crafter through it (`:82`).
- **S2, S4, S5 and S6 green.** `bin/test` passed over each module S4 names,
  one module per call, each with exit 0:
  `tests/text/test_broad_gate_rule.py` (17),
  `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` (23),
  `tests/behaviour/test_the_sealer_guarantees.py` (15),
  `tests/text/test_edits_go_through_the_edit_tool.py` (5),
  `tests/behaviour/test_a_probe_that_commits_says_so.py` (5),
  `tests/text/test_a_moved_rule_leaves_its_definition.py` (221),
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py` (8) and
  `tests/text/test_every_agent_reads_the_contract.py` (22). The first, the
  second, the sixth and the seventh were run again after the proofer
  paragraph was rewrapped, and all passed with exit 0. `uvx ruff check` and
  `uvx ruff format --check` passed over the three changed test files (exit 0,
  executed).
