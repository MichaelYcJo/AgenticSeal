# Implementation Plan: every agent is written anew from its job (#957)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-17 by the repository owner, when `smith` was spawned, with the baseline taken at af9c924b (`release/v0.22.1` after #964 merged) rather than d4552372, so that #964's changes to the texts an agent reads are not counted as this rewrite's.

## Summary

Every agent definition and the contract are written anew from the job each
does, in one shape: the contract sentence, the job and its one write, the
order of work with the file each step opens, what it never does, and its
rules with what enforces each. Every `skills:` list is cut to the contract,
and the four skills the lists used to inject are written to the same shape
so the agent that opens one at its step reads the current rule once. The
marks nobody reads leave: the proof block, the emoji in every file an agent
reads, the batching numbers copied into the definitions. The broad gate runs
as the orchestrator's one command before the sealer is spawned, and the
sealer reads its record. The sealer's model is measured on Sonnet against
Opus. A baseline is taken once on the released tree, and every phase that
changes an agent's preload proves that agent not worse on outcome and
cheaper on cost before the next agent follows; the warden goes first, alone,
as the proof of the approach on one file. The mechanics this rewrite would
otherwise meet first — a red case, a census and stamps that refuse unit
edits, a grammar stated four times, an emoji a gate reads — are #964's and
have merged before this item's first phase.

## Technical context

Read at d4552372, the release this branch is cut from; `executed` where
`spec.md` §*The tree as it stands, measured* says so. The readings #964's
phases act on are in #964's `spec.md`, not here.

- **The definitions and their preloads.** `agents/warden.md` (305 lines)
  preloads `agent-contract`, `code-review` and `writing-style`: 76,019 B of
  the agent's own share. `agents/smith.md` (341) and `agents/framer.md`
  (371) preload `agent-contract`, `implement` and `writing-style`: 94,493
  and 93,195 B. `agents/sealer.md` (143) preloads the contract alone:
  28,358 B. `agents/scribe.md` (71) preloads the contract and
  `legacy-parity`: 29,456 B. The `CLAUDE.md` pair adds 14,775 B to every
  spawn and is not this item's. The contract is 369 lines in 17 numbered
  sections, several of them an incident account with the rule at its end.
- **What holds the definitions' text.** 42 test modules name a file under
  `agents/`, 11 the contract, 12 `implement`, 6 `code-review`, 3
  `writing-style`. `tests/test_every_agent_reads_the_contract.py#PINS` holds
  the opening paragraph's four sentences identical in every definition;
  `tests/test_a_moved_rule_leaves_its_definition.py` and
  `tests/test_broad_gate_rule.py` pin the rule sentences of the smith and
  the warden; `tests/test_the_sealer_guarantees.py::TestDefinition` the
  sealer's steps; `tests/test_a_section_marked_for_one_role_reaches_only_that_role.py`
  derives the preload from each `skills:` list.
  `tests/test_a_question_says_who_can_answer_it.py:106` asserts the
  questions template's sentence *`Status` column is ticked by whoever
  answered*, which the template rewrite re-points.
- **The marks and their readers** are `spec.md` §*Marks and labels*' table.
  None of the marks this item disposes of is read by a gate; the one that
  was, the closing mark, is #964's.
- **The gate and the sealer.** `agents/sealer.md` step 1 runs `broad-gate
  --base <base> --record <item>`; `skills/code-review/orchestration.md:178-201`
  has the orchestrator run `--preflight` and spawn; `broad_gate.py` (3,396
  lines) writes `broad-gate.md` on `--record` and keeps earlier runs as
  `; earlier run:`; `hooks/sealer-stamp.py` draws the stamp from the file
  at the end of the spawning session's turn, so the owner of the run moving
  to the orchestrator changes nothing in the drawing.
  `tests/test_broad_gate_rule.py` holds 24 cases on the one-owner rule,
  three of them on the sealer being that owner.
- **The evaluation.** `evals/behaviour/` holds 20 cases (warden 4 replay, 4
  seeded, 1 fixture; smith 4; framer 4; sealer 3), two runs each, generated
  by `replay_targets.py`, `seed_defects.py` and `rule_cases.py#MODELS`.
  `noninferiority.py run --rev <sha> | --tree <dir>` extracts the tree,
  takes the suite from `--suite-rev` (HEAD by default), runs `claude plugin
  eval` with `--max-cost-usd 100`, and saves spend, seconds and tokens from
  the trace's `result` event; `compare` writes the record `#verdict` judges
  by five rules and `tests/test_a_rewritten_definition_proved_non_inferior.py`
  recomputes. The baseline is phase 1's, at af9c924b. The harness is green
  on Windows and reads the 0.22.0 record since #964's phase 1; this item
  touches it once, in phase 1b, where `verdict` judges every rule against
  the baseline and counts every model's tokens.
- **The suite and CI.** 7,329 cases priced at 3,371 s; one run is 55 runner
  minutes over three legs, under 11 minutes wall, 208 billable minutes if
  private (#964's `spec.md` holds the reading). The 42 agent-pin modules
  are 878 s of that together, most of which stays.

**What breaks in six months with the chosen approach.** A definition that
names a skill at a step and an agent that skips the step reads nothing of
the skill, and the only thing that sees it is a `shape-` grader at the next
run of that agent's cases; between runs the loss is invisible, and
`evals/README.md` says nothing in the tree makes a later edit owe a run. A
later change that appends a paragraph to a definition is caught by nobody
mechanical: the cost rule reads bytes only when somebody runs the suite, and
the warden's reading of the diff is what holds the shape. The orchestrator's
gate run before the sealer is a sentence in `orchestration.md`, and a
session that spawns the sealer without it meets a `withheld — no broad run
at HEAD` and runs the gate then, one spawn late.

## Alternatives considered

CI cost is the billable minutes a private repository would pay per pull
request (Linux 1×, Windows 2×, macOS 10×), against the 208 measured at
d4552372. The suite's priced seconds are the share this item moves.

| Approach | Failure scenario (six months on) | CI cost if private | Verdict |
|---|---|---|---|
| A. Each definition and the contract written anew in one shape; the contract alone preloaded and each skill opened at its step; the marks without a reader gone; the gate the orchestrator's run before the sealer; a baseline and a per-phase proof, the warden first | above | none: no priced module leaves or arrives beyond the re-pointed pins; the minute #964 saves is its own, and the 208 is the macOS multiplier's, which this item does not touch | **chosen** |
| B. Trim each definition in place: delete the narrative, keep the headings and the preloads | the next six changes append where the last six did, and the files are back at today's size with today's structure; three frames of #923 trimmed files whose structure was the problem and each trim was undone by the next round | none | rejected (the owner: a structure that stays compact, not a one-time trim) |
| C. Replace the structure outright: no per-agent definition body, one procedure file per flow (frame, build, review, guarantee) that the frontmatter points at, and no `skills:` list anywhere | a procedure file two agents read (the smith's fix pass and the warden's verifying round both read the record's rules) carries a per-role exception, which `docs/the-agent-set.md` refuses of a shared file; and a pointer the harness does not preload is a Read every spawn pays before its first act, so the contract would arrive by habit again, which is #107's failure | none | rejected, and its shape is borrowed: the definitions become short and point at the skills they open, while the contract still arrives by the `skills:` mechanism |
| D. Keep the skills preloaded and only write them shorter | every spawn pays every skill whether or not its act comes: a fix pass pays `implement` and `writing-style` for two lines of a record; and no run ever shows which skill an agent needed, so the lists never shrink | none | rejected; a case decides it per agent, and a skill a failing case names goes back on the list |
| E. Open the contract on demand too, preload nothing | the exit-code rule arrived at round 2 of one item and the venv line at round 3 because nothing delivered them before the first tool call; a rule read by habit is the failure the contract ends | none | rejected |
| F. Keep the contract's 17 numbers and retire sections to one-liners, as its own rule says | five one-line slots paid on every spawn forever, and a file that carries its own history, which is the item's root problem | none | rejected; the file written anew starts at §1, the rule holds from this edition, and every citation is rewritten in the same commit |
| G. Rewrite the contract and the warden in one phase | 18 fewer runs, and a case that fails cannot be laid at the contract or the definition | none | rejected; attribution over about 18 runs |
| H. The sealer keeps the broad run and retries once on a failing check | a 240K-token guarantor run spent again on a second that went 1.8 s over a ceiling; the mechanical act stays inside the judgment agent | none | rejected |
| I. The sealer drops to Sonnet now | the audit is judgment at the level of the agents it audits, and nothing has measured Sonnet on the three cases | none | rejected (the owner: measured first) |
| J. No baseline; judge the new side on its shape graders alone | a rewrite that lost a defect the old side found passes, because nothing compares recall | none | rejected |
| K. A scribe case, with a parity fixture generator | one more generator for an agent no run in this repository has spawned; a mechanism nobody asked for | none | rejected; the scribe is measured on bytes and its outcome is `unverified` (Q3, answered) |
| L. The definitions point at `docs/` for their rules and state none | an agent opens a 350-line document for one sentence at every step; the rule an agent needs at its step is written where it reads it | none | rejected; a definition states its own rules, `docs/` states the repository's |
| M. `writing-style` stays preloaded for the warden, since the record needs its English rules | 21,000 B on every warden spawn for one section of about 1,300 B read at one step | none | rejected; opened at the record step, and the `shape-words-only` grader and the round's reading say whether the record suffered |
| N. Rename `Enforced by:` to one lowercase word in the files this item writes | two spellings in one tree until #941, with `rules.py` reading one of them | none | rejected; #941 renames it with its reader |

The alternatives about the `Reads:` lines, the stamps, the grammar's
placement, a generated-variant test and the closing mark moved with their
phases to #964's `plan.md`.

## The split

The split is made. The owner answered `questions.md` Q1 on 2026-10-16: two
work items, both in milestone `release: 0.22.1`.

| Work item | Holds | Order |
|---|---|---|
| #964 — the mechanics (`seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/`) | the red tree and the harness, the census and the stamps, the grammar table, the closing word: checks, scripts and tests verified by CI alone, which remove the census refusals every unit edit here would meet and change the word the smith writes into `overview.md` before any smith of this item writes one | merges into `release/v0.22.1` first |
| #957 — the agents (this directory) | the baseline, the warden, the contract, the smith and the framer, the sealer and the scribe, the close: one review chain over the five definitions, the contract, the four skills and their pins, each phase carrying its eval record | rebased onto `release/v0.22.1` after #964 merges, then built |

The measurement that asked for it is #923's: a 10-round chain over one diff
that did many things, and the lesson in its `plan.md` Alternative J. The
first phase below does not open until the rebase has happened, which the
phase record of phase 1 says by naming the commit it stands on.

## Phases

Vertical slices — each phase ends with something runnable and verified. Each
phase that changes a file under `agents/` or a skill a definition opens
runs that agent's cases and commits the record; a phase that changes none
runs no case. Every phase enumerates the class of what it removes by the
`git grep` its record names, and every new case is seen red first (contract
§15), with the exit named in the phase record.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The baseline.** `noninferiority.py run --agent <a> --rev af9c924b --suite-rev af9c924b --out seal/specs/<id>/evals/baseline-<a>.json` for warden, smith, framer and sealer, `--runs 2 -j 4`; the raw output outside the tree; the four files committed; the cost fields of the per-run JSON and the trace's `result` event read and named in the phase record (Q5), with the spend per agent (Q4) and whether the trace names the subagent's model (Q6) | four files, none cut short, each with spend, tokens and preload bytes (`test_a_cut_short_side_is_no_result_and_never_a_pass`, `test_a_run_records_what_it_cost`); the phase record's table of runs, spend and seconds per agent | f5a71276 |
| 1b | **The verdict judges against the baseline, and counts the agent's tokens** (owner, 2026-10-17, after phase 1 showed the warden baseline failing rule 3 itself and `usage` holding 1.9–11.6% of the tokens). `noninferiority.py#verdict`: a shape or reach grader fails only where the new side passes it less often than the baseline; tokens are read across every model from the session's `result` event `modelUsage` and must fall below the baseline's; spend and wall seconds are recorded and judge nothing; `COST_MARGIN` leaves where nothing reads it. The four baseline files re-derived by `run --from-raw` from the kept raw output (no new run, no spend), the same runs at the same reference. `evals/README.md` and every other text stating the rules rewritten in place | new and changed cases in `tests/test_a_rewritten_definition_proved_non_inferior.py` red first, then green; the four re-derived files differ from phase 1's in the token fields alone (`diff` named in the phase record); `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py -q` exit 0; `bin/rules --check` exit 0 | ad1a93a2 |
| 2 | **The proof on one file: the warden.** `agents/warden.md` written anew to `spec.md` §*The shape of a definition*, `skills: [agent-contract]`, step 1 opening `skills/code-review/SKILL.md`, the record step opening `skills/writing-style/SKILL.md`'s section for the record's language; the six rules of the warden kept as `## Rules` paragraphs (the branch worktree's record path, the new-test-against-its-group reading, the verifying round, the carried-fact table, the clone, the probe rules); the batching number gone; `skills/code-review/SKILL.md` written anew to the shape: two stages, the axes, probes against regression tests, the record pointing at the template and the table, no proof block, no orchestrator section pointer beyond one line; the 23 modules naming the warden and the 6 naming `code-review` re-pointed where the rule stays and removed with one line in the phase record where the sentence was narration (Q7); `tests/test_every_agent_reads_the_contract.py` rewritten to S1 and S2 (T1, T2) for every definition, red on the four not yet rewritten and skipped by name for them until phase 5 closes, which the phase record says | the warden set run against `baseline-warden.json`, `evals/warden-phase-2.md` reading `pass`; T1 and T2 red then green on the warden; `bin/rules --check` exit 0; `bin/test` over the re-pointed modules exit 0; `payload-meter --agent warden` in the phase record beside the baseline's | 074a67c4, closed by the orchestrator on a `fail` of one grader by one run (`phases/phase-2.md` §*The orchestrator closes the phase*) |
| 3 | **The contract.** `skills/agent-contract/SKILL.md` written anew: one opening paragraph, §1 to §N in the new order, each a rule paragraph with `Enforced by:`, the four new rules of `spec.md` §*The shape of a definition*, §2 stating that no agent runs the broad gate and that the orchestrator runs it before the sealer; `docs/the-agent-set.md`'s section-number sentence rewritten to *from this edition*; every `§N` citation outside `seal/specs/` and `changelog/` rewritten to the new number in the same commit, the 128 prose sites and the 326 test sites enumerated by `git grep -n -E "§[0-9]+"`; T3, T4 and T5 (S4, S5, S6) in `tests/test_the_agent_contract_holds_the_universal_rules.py` and `tests/test_a_moved_rule_leaves_its_definition.py`, red first; the 11 modules naming the contract re-pointed; `agents/warden.md`'s record step gains one sentence: read the record through `chain_check.py` before handing back and correct what it refuses (phase 2's one failing grader, a record with no `verdict:` line, read again in this phase's warden record) | all four sets run (every preload changed), `evals/<agent>-phase-3.md` reading `pass` for each; T3–T5 red then green; `bin/rules --check` exit 0; `git grep -n -E "§[0-9]+"` over `agents/ skills/ docs/ templates/ hooks/ tests/ CONTRIBUTING.md` naming only sections the contract has, which T3 holds | 314f6166, closed by the orchestrator: the warden and the smith read `pass`, the framer `fail` on rule 5 (carried to #968 and to the milestone's close against af9c924b), the sealer's record not read (its definition contradicted the contract until #969) |
| 4 | **The smith, the framer and their skills.** `agents/smith.md` and `agents/framer.md` written anew to the shape: the smith's steps (requirements and whether the frame holds; build test-first, the phase record; the fix pass's two lines; verify and mutate; hand back with the three labels), its rules (a new test starts from its group; commit before you mutate; the three-fix stop; the waiver as one sentence), the RIDER block and the batching number gone; the framer's steps (gather, judge, plan, report), its rules (asks nobody; writes three files; do not avoid the change; the residue), the batching number gone. `skills/implement/SKILL.md` to the shape: the layout, the precedence, the ladder, the file set table, test-first, the closing memo, the fix pass, no proof block, the `U+2B1C` sentence to the words; `skills/writing-style/SKILL.md` to the shape, its English rules a section an English writer opens, its one emoji gone; `templates/sdd-overview.md:9` and `templates/sdd-questions.md`'s `U+2B1C` to the words `open` and `answered <date> by <who>`, `tests/test_a_question_says_who_can_answer_it.py:106` re-pointed; `skills/verify/SKILL.md` §*Every agent seals what it verified* and §*Seal block* rewritten to the fact that the hand-back's three labels carry the claims and the sealer's `guarantee.md` is the one seal, and no more of that file; T6 (S7) over every file under `agents/`, every `skills/*/SKILL.md` and `templates/`; the 19 and 12 modules naming the smith and the framer, the 12 naming `implement` and the 3 naming `writing-style` re-pointed or removed with a line (Q7); the three proof-block pins removed | the smith and the framer sets run, `evals/smith-phase-4.md` and `evals/framer-phase-4.md` reading `pass`; T6 red on the tree before the rewrite, green after; `bin/rules --check` exit 0; `bin/test` over the re-pointed modules exit 0; `payload-meter` for both in the phase record | moved to #967 (the smith, `implement`, `writing-style`) and #968 (the framer), owner, 2026-10-17 |
| 5 | **The sealer with the gate before it, its model measured, and the scribe.** `agents/sealer.md` written anew to the shape: step 1 reads `broad-gate.md` and refuses one absent or not at HEAD, the verdict words `sealed`, `withheld — <reason>` and `undecided — <question>` replacing `sound`, `not sound` and `undecidable` in the reader, the template, the docs and the graders in one commit (spec.md §*Marks and labels*; the baseline's sealer runs graded on the old words, the new runs on the new, the truth graders unchanged), steps 2–5 as 0.22.0 left them, a re-run audits the commits since the last `guarantee.md`'s commit and keeps its line (S9); `skills/code-review/orchestration.md:178-201` rewritten: the orchestrator runs `broad-gate --base <base> --record <item>` with nothing else running, then spawns; `docs/the-broad-gate.md` §*One act, one owner* and `docs/the-review-record.md` §*The guarantee* rewritten in place; `templates/sdd-guarantee.md`'s `Target SHA` row gains the `; earlier run:` form; `tests/test_broad_gate_rule.py` rewritten to the new fact (T7), `tests/test_the_sealer_guarantees.py::TestDefinition` and `TestTemplate` to the step and the row (T8, T9); the three sealer cases regenerated with scaffolds that write `broad-gate.md` at HEAD; the sealer set run on Opus against `baseline-sealer.json`, then on a copy of the tree with `model: sonnet`, `evals/sealer-model.md` written by `compare` over the two sides (T10), and `model:` set by `spec.md` §*The sealer's model is decided by measurement*. `agents/scribe.md` to the shape and `skills/legacy-parity/SKILL.md` to the shape with the four verdict words; the scribe measured by `payload-meter` only, its outcome `unverified` with the owner named in the phase record (Q3); the 11 and 5 modules naming the sealer and the scribe re-pointed | `evals/sealer-phase-5.md` reading `pass` on Opus; `evals/sealer-model.md` with both sides and the decision quoted in the phase record; T7–T10 red then green; `bin/test tests/test_broad_gate_rule.py tests/test_the_sealer_guarantees.py tests/test_evals_layout.py -q` exit 0; `bin/rules --check` exit 0; T1 and T2 green for all five definitions with the skips of phase 2 gone | moved to #969 (the sealer) and #970 (the scribe), owner, 2026-10-17 |
| 6 | **The close.** Any agent's set run again where its preload changed after its last passing record; `overview.md` (one line of purpose, divergences, `## Not verified` closed with the word #964 made the mark, fed-back clauses); `changelog.md`: the paragraph a plugin user reads (what a spawn preloads now, where each skill is opened, the proof block gone, the gate before the sealer, the sealer's model) and the per-agent table of preload bytes, tokens read, spend and outcome at af9c924b and at the close, each figure with its commit, read from the eval records and `payload-meter`; `questions.md` rows the work and the measurements answered, in words | a `pass` record for every agent whose preload changed, or its last record naming its finished preload; `bin/rules --check` exit 0; `chain_check.py --baseline origin/release/v0.22.1 --root <worktree>` exit 0; the fragment's figures traced to their records in the phase record | narrowed to this item's close: `overview.md` and `changelog.md` for phases 1 to 3; each later issue closes its own |

This table is also where the work records how far it got. **Status is empty,
or the commit that closed the phase.** Re-read the column after any rebase.

### Test rows — what each case protects and the mutation it kills

| Case | Protects | Mutation it kills |
|---|---|---|
| T1 `tests/test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_contract_alone` (NAME NOT IN TREE until phase 2; skipped by name for the four definitions until phase 5) | S1 — a sixth preload or a lost section, which no eval sees while the output is right | a second `skills:` entry accepted; a missing `## Order of work` passed; the opening sentence matched anywhere in the file |
| T2 `…::test_every_file_a_step_names_exists` (phase 2) | S2 — a renamed skill leaving a dangling instruction | a backticked `skills/x/SKILL.md` not resolved; a path outside `skills/` ignored |
| T3 `tests/test_the_agent_contract_holds_the_universal_rules.py::test_every_cited_section_exists` (phase 3) | S4 — a citation left at an old number | `§N` read only in `agents/`; a number above the last heading passed |
| T4 `…::test_the_four_rules_stand_with_their_enforcers` (phase 3) | S5 — a new rule dropped in a later trim | any of the four paragraphs deleted; an `Enforced by:` line missing under one |
| T5 `tests/test_a_moved_rule_leaves_its_definition.py::test_no_definition_states_a_tools_per_turn_figure` (phase 3) | S6 — the second copy of a bar | `tools per turn` with a number in any definition passed |
| T6 `tests/test_the_record_is_written_in_words.py::test_no_file_an_agent_reads_carries_an_emoji_or_a_proof_block` (phase 4; replaces `test_the_template_the_format_and_the_two_definitions_carry_no_emoji`) | S7 — a mark coming back where an agent reads instruction | one of the three globs dropped; the `applied` block pattern dropped; the variation selector left out of the range |
| T7 `tests/test_broad_gate_rule.py::test_no_definition_assigns_the_broad_gate_and_the_orchestrator_runs_it_before_the_spawn` (phase 5; replaces `test_only_one_definition_assigns_the_broad_gate`, `test_the_sealer_counts_the_silent_definitions_from_the_glob`, `test_the_orchestrator_runs_the_preflight_before_it_spawns_the_sealer`) | S8 — a definition taking the run back | a definition handing itself the suite passed; the orchestration section's run sentence after the spawn sentence passed |
| T8 `tests/test_the_sealer_guarantees.py::TestDefinition::test_step_1_reads_the_record_and_runs_nothing` (phase 5) | S8 — the sealer running the gate | `broad-gate --base` in step 1 passed; the `not HEAD` refusal dropped |
| T9 `…::TestTemplate::test_the_target_row_keeps_an_earlier_run` (phase 5) | S9 — a full re-audit | the `; earlier run:` form absent from the template passed |
| T10 `tests/test_a_rewritten_definition_proved_non_inferior.py::test_a_two_sided_compare_of_one_suite_on_two_trees_reads_both_costs` (phase 5) | S10 — a model drop decided by cost alone | the truth graders of one side dropped from the record; a cheaper side with a lost truth read as `pass` |

Each definition rewrite is verified by its eval record, the pins it
re-points, `rules --check` and `payload-meter`, not by a case on its
sentences; a case on a sentence is what held the bloat in place.

## Operational impact

- **What a plugin user sees.** Each agent's definition is a page; a warden,
  smith or framer spawn opens a skill with a `Read` at the step that needs
  it, which appears in the transcript as one call. The hand-back carries its
  claims under the three labels and no proof block. A `questions.md` status
  reads `open` or `answered`.
- **The run.** The orchestrator runs `broad-gate --base <base> --record
  <item>` before spawning the sealer, with nothing else running; the sealer
  reads the file and runs nothing broad; a re-run audits the commits since
  the last guarantee. The stamp is drawn as before, from the file, at the end
  of the spawning session's turn.
- **The proof.** 126 runs on the orchestrator's account, by the case counts
  at d4552372; the spend is measured at phase 1 and named in that phase's
  record. CI pays nothing for the evaluation.
- **Compatibility.** The contract's section numbers change; a spawn prompt
  or a record citing an old `§N` reads the new contract wrong until
  rewritten, and the tree's own citations are rewritten in phase 3. A user
  repository's `CLAUDE.md` block (`templates/claude-md-block.md`) is #940's
  and is read for `§N` in phase 3's grep.
- No new dependency; stdlib Python at the floor.
