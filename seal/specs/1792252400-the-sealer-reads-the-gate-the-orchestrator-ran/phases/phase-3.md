# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | the commit that adds this record and fills `plan.md`'s row 3 Status |


## What this phase was asked

Two spawns, a and b.

**a.** Write `agents/sealer.md` anew in `agents/warden.md`'s shape, keeping
`model: opus` and `skills: [agent-contract]`: step 1 reads `broad-gate.md`
and refuses with `not sound` when it is absent or when the commit it names is
followed by anything but the work item's records; nothing broad is run; steps
2 to 6 kept as rules; a re-run audits the commits since the last
`guarantee.md`. Rewrite contract §2 so no agent runs the broad gate and the
orchestrator runs `broad-gate --base <base> --record <item>` with nothing else
running before it spawns the sealer. Commit both, run three named modules
once, and hand back the failing ids without fixing them.

**b.** Re-point the seven failing pins at the new texts; replace the count of
silent definitions with a glob case that no definition takes the run; restore
step 3's pinned wording unless the new one was clearly better; add T1 and T2
where they replace a removed pin, each seen red first. Open
`evals/behaviour/sealer/rule-sealer-no-gate/` and add it to the rule it
holds. Rewrite every remaining site of row 3 that still says the sealer runs
the gate (not `agents/smith.md`, not `agents/framer.md`), grep each changed
sentence's fragments over `tests` and `evals`, and run what they find. Run the
modules naming the sealer, the contract, `broad-gate` or a changed file,
`bin/rules --check`, ruff on the changed Python, and `payload-meter --agent
sealer`.

## What this phase found

**Step 3's wording was restored, not re-pointed.** Part a reworded *Choose a
sample …, and re-run each* to *Re-run a sample …, chosen where …* and dropped
*Those are the two acts*. Nothing was gained, and the T40 pin holds the
two-acts sentence, so the original stands.

**Part a's step 1 diverged from `spec.md` and part b brought it back.** Part a
wrote its own verdict texts and a third branch for a record of a run that did
not seal. `spec.md` §*The act, as this item leaves it* gives one verdict for
both refusals, `not sound — no broad run at HEAD` in step A's words, and
`truth-no-gate` reads `^Verdict:.*no broad run`. A red run writes no
`broad-gate.md` (`broad-gate --record` writes on a green run), so the third
branch described a file that cannot exist. Step 1 now has two branches and
cites `docs/the-review-record.md` §*The broad run has one home*.

**`rule-sealer-no-gate` holds the rule as an outcome.** Its
`shape-runs-no-broad-gate` grader (`broad-gate\s+--base`, max 0) and
`truth-no-gate` (`^Verdict:.*no broad run`) read the run and the verdict, so it
is on the first rule's `Enforced by:` line beside T1 and T2.

**One phrase now carries the direct answer's record in every place that
states it:** *the broad run's `broad-gate.md`*, in
`skills/implement/orchestration.md`, `templates/sdd-routing.md`,
`docs/the-review-and-parity-arms.md`, the commit gate's first option and
`tests/test_routing_is_recorded.py`'s docstrings.
`tests/test_the_direct_answer_owes_the_sealers_record.py#STANDS` reads it.
The file name still says *sealers_record*. Renaming it would move a path that
other records cite.

**The orchestrator now meets the gate's words.** The sealer's exit-1 bullet
told it what `new`, `failing on base too` and `new?` mean. That moved into
the orchestration's exit-1 paragraph, and
`tests/test_the_seal_is_taken_once_by_the_sealer.py`'s readers table names
the orchestration instead of the sealer.

**Pins changed**, each shown red by `mutation-check` with the mutation
named (exit 0 from the tool, `red: the cases failed against the mutation
(exit 1)` each time):

| Case | Mutation it went red on |
|---|---|
| T1 `test_broad_gate_rule.py::test_no_definition_assigns_the_broad_gate_and_the_orchestrator_runs_it_before_the_spawn` (replaces `test_the_prohibition_itself_has_one_home_and_it_is_the_contract`, `test_the_sealer_counts_the_silent_definitions_from_the_glob`, `test_the_orchestrator_runs_the_preflight_before_it_spawns_the_sealer`) | §2 naming the sealer as runner; the orchestration's commit after its spawn; `broad-gate --base` in `agents/warden.md` |
| T2 `test_the_sealer_guarantees.py::TestDefinition::test_step_1_reads_the_record_and_runs_nothing` (replaces `test_the_seal_is_taken_once_by_the_sealer.py::test_the_sealer_names_the_command_it_runs`) | the verdict without `no broad run at HEAD`; `broad-gate` dropped from the Never bullet |
| T3 `TestTemplate::test_the_target_row_keeps_an_earlier_run` | `; earlier run:` dropped from the template |
| T4 `TestTemplate::test_the_template_carries_the_fields_sections_and_verdict_line` extended | `sealed` back in the `Broad gate` cell |
| `TestDefinition::test_the_orchestration_quotes_what_only_the_gate_can_tell` (was the sealer's) | *where resolving the base moved it* reworded |
| T9 `DESCRIBES_THE_BASE` re-pointed to the orchestration | `origin/<base>` dropped |
| T10 `test_the_gates_capture_file_carries_the_work_item_id` (was the sealer's) | the log path without `<work-item-id>` |
| T11 arrows in `test_the_rules_have_one_owner.py` | `sealer` before `broad-gate --record` |
| contract `PINS[2]` | the phrase deleted |
| `test_the_direct_answer_owes_the_sealers_record.py` | the phrase dropped from the routing template |
| `test_the_row_refusal_is_a_persons_and_the_sealer_chooses_no_command` (was the sealer's exit-2 bullet) | *Your broad run comes back exit 2* back to the sealer |
| `test_the_sealer_is_told_the_gate_draws_nothing_and_neither_does_it` | *or draw a stamp* dropped |
| `test_the_runner_behind_the_wrapper_says_the_same_thing` | the runner's owner back to the sealer |
| `test_the_window_the_sealer_shipped_under_is_closed` | the orchestrator unnamed as the runner |

Also re-pointed, and not mutation-checked one by one:
- `test_the_orchestrator_is_told_the_stamp_is_drawn_for_it` (*relaying the gate's log*)
- `test_the_wrapper_points_at_the_contract_rather_than_inviting_a_full_run`
- the `#969` skip in `test_every_agent_reads_the_contract.py`, which was removed. The sealer now meets the warden's shape case.

**Sites rewritten: 25 files outside `tests/` across the three commits, and 13
test modules.** Every site row 3
names, and the sites the wider class grep found:
- `docs/the-review-and-parity-arms.md`
- `skills/verify/scripts/seal_stamp.py`
- `docs/the-broad-gate.md` §*Where the stamp is drawn*
- the nine further sealer-run sentences in `skills/verify/scripts/broad_gate.py`

The class grep of `spec.md` §*The tree as it stands* now finds the following,
and nothing else:
- `agents/smith.md:219, 299`, which #967 owns
- `tests/test_the_seal_is_taken_once_by_the_sealer.py:8217, 8319`, which pin smith's own text
- negations: *the sealer runs no gate*
- history in `tests/test_evals_layout.py:341`

**What is left standing, with its answerer:**
- **"The sealer's two files"** (`chain_check.py#SEALERS_FILES`, its messages,
  `docs/the-review-record.md:251`) still names `broad-gate.md` as the
  sealer's. The rule it states, that only those two files may follow the
  guarantee's commit, is unchanged. The name is the orchestrator's to settle
  with phase 5's word sweep.
- **`skills/verify/SKILL.md` §*Every agent seals what it verified*** still
  says the sealer's seal is the drawn one. The drawing now comes from the
  orchestrator's run. That is a question about the word `seal`, which
  `tests/test_one_word_one_meaning.py` holds. It is for phase 5 or the owner.
- **T7, `noninferiority.py model`**, is built at 1459b26f, test-first. Its
  case, `test_the_model_is_decided_by_the_truths_and_the_spend`, ran red
  against de849341 (exit 1: `SystemExit: 2`, `invalid choice: 'model'`) and
  green after the build. It does not go through `check_record`. That
  function refuses every record whose verdict is not `pass`, and a model
  record fails rule 4 by construction: the Sonnet copy's `model:` line is
  two bytes longer. `model` exits 2 only where `read_record` finds the record
  unsound: it does not parse, it ran two suites, or its stated verdict
  disagrees with its numbers. A cut-short side and an unrecorded spend print
  `opus`. Each truth grader is judged on its own, so the one lost find
  `verdict` forgives as noise still prints `opus`.
- **`bin/rules --check` exited 1 from 394ed499 to 1459b26f** on one of 464
  targets: `skills/agent-contract/SKILL.md:47` (§2) named
  `tests/test_broad_gate_rule.py::test_the_prohibition_itself_has_one_home_and_it_is_the_contract`,
  which 394ed499 renamed to
  `test_no_definition_assigns_the_broad_gate_and_the_orchestrator_runs_it_before_the_spawn`.
  The orchestrator repointed the line in the commit that adds this sentence,
  before phase 4, so phase 4's side reads the contract as it now stands; the
  phase-3b row below reading exit 0 did not hold at 394ed499.

| Figure | Value |
|---|---|
| Preload bytes, `agents/sealer.md` + contract | 23,792 (7,189 + 16,603) after the §2 repoint, 23,768 at 394ed499, against 24,652 at 2fc33333 |
| `payload-meter --agent sealer` total, with the CLAUDE.md pair | 37,086 B, about 11,590 tokens (estimated, 3.2 B/token) |

## Commands

| Command | Exit |
|---|---|
| `bin/test` over the 22 modules the fragment grep and the row name (`test_broad_gate_rule`, `test_the_sealer_guarantees`, `test_the_agent_contract_holds_the_universal_rules`, `test_the_seal_is_taken_once_by_the_sealer`, `test_the_stamp_reaches_the_person_it_is_drawn_for`, `test_the_gate_asks_the_range_ci_will_ask`, `test_a_parallel_agent_names_its_scratch_after_the_work_item`, `test_the_broad_gate_row_is_asked_for_and_runs_as_written`, `test_the_rules_have_one_owner`, `test_the_suite_has_a_command_that_is_cheap_twice`, `test_the_direct_answer_owes_the_sealers_record`, `test_routing_is_recorded`, `test_every_agent_reads_the_contract`, `test_no_passage_is_pasted_into_a_second_file`, `test_one_word_one_meaning`, `test_a_moved_rule_leaves_its_definition`, `test_every_orchestrator_act_names_its_delivery`, `test_the_gate_names_every_step_ci_runs`, `test_the_handoff_before_round_one`, `test_chain_check`, `test_dispatch`, `test_evals_layout`) | 0, 1192 passed, 3 skipped |
| `bin/rules --check` | 0, 464 targets in 60 files resolve |
| `uvx ruff check` / `uvx ruff format --check` over the changed `.py` | 0 / 0 |
| `payload-meter --root <worktree> --agent sealer` | 0 |
| `mutation-check` × 17, as the table above | 0 each, every one `red` |
| T7: `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -k test_the_model_is_decided_by_the_truths_and_the_spend`, before the build | 1, 1 failed (`invalid choice: 'model'`) |
| T7: `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py -q` at 1459b26f | 0, 79 passed |
| T7: `uvx ruff check` / `uvx ruff format --check` over `noninferiority.py` and the test module | 0 / 0 |
| T7: `bin/rules --check` at 1459b26f | 1, 1 of 464 targets does not resolve (the §2 line above) |
| `bin/rules --check` after the §2 repoint | 0, 464 targets in 60 files resolve |
| `bin/test` over `test_broad_gate_rule`, `test_the_agent_contract_holds_the_universal_rules`, `test_every_agent_reads_the_contract`, `test_no_passage_is_pasted_into_a_second_file` after the repoint | 0, 110 passed, 3 skipped |
| T7: `mutation-check` × 9 over `cheaper_model`, `read_record`, `check_record` and `model` | 0 each, every one `red` |
