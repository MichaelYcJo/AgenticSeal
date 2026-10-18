# Implementation Plan: the smith is written anew from its job (#967)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-18 by the orchestrator under the owner's delegation of that night (a plan that follows the orchestrator's stated design is approved by the orchestrator), when `smith` was spawned.

## Summary

The smith's definition and the two skills it preloads are written to the
shape #957 gave the warden: the definition preloads the contract alone and
opens `skills/implement/SKILL.md` when the build starts and
`skills/writing-style/SKILL.md`'s section for the record's language before a
record or the hand-back. `implement` keeps its cited headings and loses its
narration and its proof block; `writing-style` keeps every rule and gains
one orientation line at the head of each language section. The proof block
leaves everywhere an agent is told to write one, and a test holds that no
file an agent reads carries an emoji or such a block. The three agents whose
read set this changes, the smith, the warden and the framer, are baselined
once at 2fc33333 and measured once after the build, suite af9c924b both
times, by #957's five rules.

## Technical context

Read at ffd5f467; `spec.md` §*The tree as it stands, measured* holds the
counts and says which were executed.

- **The model.** `agents/warden.md` (167 lines, 10,527 B): frontmatter with
  `skills: [agent-contract]`, the contract sentence, `## Job`, `## Order of
  work` (step 1 opens `skills/code-review/SKILL.md` and says the paths are
  the plugin's; step 6 opens `writing-style`'s section by the record's
  language), `## Never`, `## Rules` with an `Enforced by:` line each.
  #957's `phases/phase-2.md` §*The pins (Q7), recounted* is the shape of
  the pin sorting this item repeats.
- **What holds the smith's text today** (18 modules; the sentence each
  holds, from `git grep`):
  `test_a_moved_rule_leaves_its_definition.py` — `MOVED_OUT_OF_SMITH`
  (acts the smith must not claim), *Phase 2 is your caller's spawn*, *and
  say so rather than building*, *A missing frame is not evidence about the
  rung*; `test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`
  — the `mutation-check <file> --replace … --tests "` line, `-p no:xdist`,
  no `tests/__pycache__`, *watch one go red*, the `**Commit before you
  mutate` bullet, `bound (300 s unless \`--timeout\``;
  `test_the_handoff_before_round_one.py` — *Mutation-test every unit …
  over.*, the handoff link in both the smith and `implement`, the smith's
  batching caveat; `test_the_suite_has_a_command_that_is_cheap_twice.py` —
  *Find the runner before you invent a command*, *Type the narrow form, one
  module*, `HANDOFF_LINK`, the coverage-probe sentence (parametrized with the
  warden); `test_broad_gate_rule.py` — `§2`, `§3`, *labeled \`unverified\`*,
  *the orchestrator named as its answerer*, *what was asked, and which rule
  refused it*, *hand-back*; `test_the_seal_is_taken_once_by_the_sealer.py` —
  *Then the sealer takes the broad gate once* (leaves, decision 6), *\`new?\`
  is neither*, `OWNER_NAMED`; `test_a_phase_hands_the_next_one_a_record.py`
  — `phases/phase-N.md`, `templates/sdd-phase.md`, *phase's close*;
  `test_chain_hooks_hardening.py` — *never at a merge*, the frame-holds
  sentence inside the `1. **Requirements**` step; `test_edits_go_through_the_edit_tool.py`
  — `§9`, *waiver*, *RIDER*; `test_waiver_decided_at_start.py` — the routing
  vocabulary absent from the smith; `test_a_reference_root_is_read_and_never_taken.py`
  — the smith cites where `spec.md` cites; `test_the_set_a_work_item_always_has.py`
  — the ladder's phrases and the second-rung list identical in the smith and
  the skill; `test_the_contributor_has_a_procedure.py` — the rider's dated
  sentence; `test_the_record_is_written_in_words.py` — no emoji in the
  smith; `test_every_agent_reads_the_contract.py` — the skip;
  `test_no_passage_is_pasted_into_a_second_file.py` — pair ceilings
  (smith↔implement 46, smith↔warden 153, smith↔framer 72, and others);
  `test_docs_line_wrap.py` — the smith named as uncovered;
  `test_the_payload_meter_says_what_it_measured.py` — the preload derived
  from the `skills:` list; `test_a_section_marked_for_one_role_reaches_only_that_role.py`
  — the same derivation.
- **What holds `implement`'s text** (12 modules): the file-set table's
  `phases/phase-N.md` row and the template it names, *in one batch*, *would
  not change what you build*, the handoff link, the ladder phrases and the
  second-rung examples, the citing of a reference root, the waiver
  sentences, the three-answer routing pointer, `COVERED` of
  `test_no_document_names_the_old_roots.py`, and the two modules reading
  `CLAUDE.md`'s citations of its step 1 and step 2.
- **What holds `writing-style`'s text** (3 modules): line wrap (named as
  uncovered), pasted passages, the payload meter's derivation. The warden's
  step 6 names its two language headings.
- **The eval harness.** `noninferiority.py run --rev <sha> --suite-rev af9c924b`
  extracts the tree, runs the agent's cases twice each, saves per-run
  graders, cost and tool calls; `compare` writes the record `#verdict`
  judges by five rules; `check` recomputes. `preload_files` derives the
  preload from the definition's `skills:` list, so rule 4 reads the new list.
  `compare` refuses two sides whose suites differ (exit 2).
- **The baseline.** No baseline for this tree exists: #957's records were
  taken against a contract whose sha256 differs (`spec.md` §*The tree as it
  stands*), so phase 1 runs 34 cases at 2fc33333. The kept raw output goes
  outside the tree, as #957's did (`SpecSeal-worktrees/967-baseline-raw/`).

**What breaks in six months with the chosen approach.** A smith that skips
its step 1 reads nothing of `implement`, and only a `shape-` grader at the
next run sees it; between runs the loss is invisible, and `evals/README.md`
says nothing makes a later edit owe a run. The one orientation line in each
language section of `writing-style` is a sentence, and a writer who opens
the section by a grep that lands below it still misses the structure rules.
T6's skip map is a list, and a skill added later with an emoji is caught
while a file added outside the three globs is not.

## Alternatives considered

| Approach | Failure scenario (six months on) | Verdict |
|---|---|---|
| A. The smith's definition anew to #957's shape, `implement` to the shape with its cited headings kept, `writing-style` restructured and not rewritten, the proof block gone everywhere, T6, the baseline at 2fc33333 and one evaluation of the three agents | above | **chosen** |
| B. Replace the structure: no `## Rules` in the definition at all; the smith's rules move into `skills/implement/SKILL.md` and the definition is frontmatter, the contract sentence and one step, *open `implement`* (one procedure file per flow, #957's Alternative C) | `implement` is also loaded directly by a session that builds without a smith (its own header says so), so the mutation loop, the runner rule and the hand-back labels would bind a party with no hand-back and no spawn; and a definition with no rule has no `Enforced by:` to resolve, so the first dropped rule is caught by nobody | weighed as an equal and rejected; its half is borrowed: the ladder, the file set and the second-rung list live in `implement` alone, and the smith's copies leave |
| C. One build phase for the three files | T6 cannot be seen red at a moment that matters, since the proof block and the emoji leave in the same commit it lands in; and one diff over three files' 33 pins is the shape #923 took ten rounds over | rejected; two build phases, the smith and `implement` first |
| D. Split `writing-style` into one file per language | the warden's step and `CLAUDE.md:70` name one file's headings; a second file is a second Read on every record; the structure rules are shared and would be copied or pointed at from both | rejected |
| E. Rewrite `writing-style`'s content shorter, as `implement` and `code-review` were | the owner's writing rules are also how the orchestrator writes to the owner; a rule dropped here is a rule the owner never agreed to lose | rejected (decision 3) |
| F. Keep `## Proof block` in `implement` as optional | a block no check reads, paid in every report, and the word `seal` with two meanings again | rejected (decision 2) |
| G. T6 skips `skills/audit/SKILL.md` by name, as it skips `legacy-parity` | a skip entry names the issue that removes it, and audit's five marks have none; a skip to nobody is a mark kept by default | rejected; the five become words here (`questions.md` Q3) |
| H. Measure the smith and the warden only, as #967's body first said | the framer preloads `implement` and `writing-style`, so its read set changes here and guard 1 fires; #968 would then start from a framer measured on a tree that no longer exists | rejected (decision 4) |
| I. Reuse #957's phase-3 records as the baselines | the contract at 2fc33333 is not the one those runs read, so a difference would be two changes read as one | rejected (guard 1; `spec.md` §*The tree as it stands*) |
| J. Two paid runs per agent in phase 4 | #967's body says one, and a `fail` is recorded and its cause fixed once before a second; the noise of two runs a case is #966's | rejected |
| K. The smith keeps `implement` preloaded and the skill is only written shorter | every fix pass pays the whole skill for two lines of a record (#957's Alternative D) | rejected |
| L. The smith names the orchestrator as the gate's runner, ahead of #969 | two worktrees writing the owner into one file; and the sentence is false until #969 merges | rejected (decision 6) |

## Phases

Vertical slices — each phase ends with something runnable and verified. A
phase that changes a file an agent reads runs no paid case of its own; the
three sets run once, in phase 4, against phase 1's records. Every phase
enumerates the class of what it removes by the `git grep` its record names,
and every new case is seen red first (contract §15), with the exit named in
the phase record. The spend of a paid phase is read from the per-run
`total_cost_usd` and stops before the next agent past the figure
`questions.md` Q1 holds.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The baseline at 2fc33333.** `python3 evals/scripts/noninferiority.py run --agent <a> --rev 2fc33333 --suite-rev af9c924b --out seal/specs/<id>/evals/baseline-<a>.json --runs 2 -j 4` for smith, warden and framer, in that order; the raw output kept outside the tree; the three files committed; the phase record names the sha256 of each agent's preload beside #957's phase-3 `## New preload` tables, the spend per agent from `total_cost_usd` (`questions.md` Q4), and `payload-meter --agent <a>` at 2fc33333 | three files, none cut short, each with spend, tokens and preload bytes (`tests/test_a_rewritten_definition_proved_non_inferior.py::test_a_cut_short_side_is_no_result_and_never_a_pass`, `::test_a_run_records_what_it_cost`); `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py -q` exit 0 | 60e3e7f2 |
| 2 | **The smith and `implement`.** `agents/smith.md` written anew to `spec.md` §*The shape this item gives each file*: `skills: [agent-contract]`, step 1 opening `skills/implement/SKILL.md`, the record and hand-back steps opening `writing-style`'s section by the record's language, the rules decision 1 names as `## Rules` paragraphs, no runner of the broad gate named (decision 6), the RIDER block, the batching caveat, the ladder's copy and the proof block gone, at or under 10,527 B. `skills/implement/SKILL.md` written to the shape with `## The language the records are written in`, `## Document layout — two roots, three lifetimes` and `### 1.` to `### 6.` kept as titled, one pointer line to `orchestration.md`, `## Proof block` and the narration of `spec.md` §*Removes* gone. The proof block's other sentences leave in the same commit: `skills/verify/SKILL.md` §*Every agent seals what it verified* and §*Seal block* rewritten to the fact that the hand-back's labels carry the claims and `guarantee.md` is the one seal, `:310` and `:384` with them; `templates/sdd-overview.md:9-12`; `session_cost.py:4`; the README rows. The pins sorted (Q7): the 18 smith modules and the 12 `implement` modules re-pointed where the rule stays, removed with one line in the phase record where the sentence was narration; the two proof-block cases and `test_one_word_one_meaning.py`'s two lines removed; T4 replaces the gate-owner case; T3 plants the four rules; T5 holds `implement`'s cited headings; `NOT_YET_REWRITTEN`'s smith entry deleted; `agents/smith.md` and `skills/implement/SKILL.md` added to `test_docs_line_wrap.py#COVERED` | T1 and T2 red on the old smith, green after; T3, T4, T5 red first by the mutation named in the phase record; `bin/test` over the modules `git grep -l -E "smith|implement/SKILL" -- tests` names, exit 0; `bin/rules --check` exit 0; `uvx ruff check` and `format --check` on the changed `.py`, exit 0; `tests/test_one_word_one_meaning.py` exit 0 on the commit; `git grep -n -i "proof block\|seal block\|implement applied\|verify sealed" -- . ':!seal/specs' ':!changelog'` naming only tests that quote history; `payload-meter --agent smith` in the phase record beside phase 1's | aea8c8e5 |
| 3 | **`writing-style`, the remaining marks, and T6.** `skills/writing-style/SKILL.md` restructured: one orientation line at the head of `## 문장 규칙` and of `## English prose rules`, every rule and heading kept, `:260`'s `U+1F534` the word. `templates/sdd-questions.md:10` `U+2B1C` the word `open` and `:31` rewritten to *written by whoever answered, as `answered <date> by <who>`*, `tests/test_a_question_says_who_can_answer_it.py:106` re-pointed. `skills/audit/SKILL.md:53-58` five marks the words (Q3). T6 planted in `tests/test_the_record_is_written_in_words.py` over `agents/*.md`, `skills/*/SKILL.md`, `templates/*.md`, `legacy-parity` skipped by name for #970, replacing `test_the_template_the_format_and_the_two_definitions_carry_no_emoji`; T7 holds the two language headings and their orientation lines; the 3 `writing-style` modules checked | T6 red on the tree at the phase's start (7 marks in 3 files: `writing-style` 1, `sdd-questions` 1, `audit` 5, with `legacy-parity`'s 4 skipped), green after; T7 red first; `bin/test tests/test_the_record_is_written_in_words.py tests/test_a_question_says_who_can_answer_it.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_the_payload_meter_says_what_it_measured.py tests/test_docs_line_wrap.py -q` exit 0; `bin/rules --check` exit 0; the Python sweep of `spec.md` §*The tree as it stands* over the three globs printing `legacy-parity` alone | 7053c184 |
| 4 | **The evaluation of the three agents.** `noninferiority.py run --agent <a> --rev <phase 3's commit> --suite-rev af9c924b --runs 2 -j 4` for smith, warden and framer, once each, paid; the raw output kept beside phase 1's; `evals/<a>-phase-4.json` by `run --from-raw` and `evals/<a>-phase-4.md` by `compare --phase 4 --old evals/baseline-<a>.json`. A `fail` is recorded as it reads; where its cause is a sentence of `agents/smith.md`, `implement` or `writing-style`, the cause is fixed once in one commit and that agent's set runs a second time; where its cause is `agents/framer.md`, the record is kept, the plan's row says so and the cause goes to #968 (decision 5); no third run. The phase record counts, from the traces, the runs in which the smith opened `skills/implement/SKILL.md` and the runs in which it opened `writing-style` (S3) | `evals/smith-phase-4.md`, `evals/warden-phase-4.md`, `evals/framer-phase-4.md` each reading `pass`, or `fail` with the cause named and the row's disposition (`tests/test_a_rewritten_definition_proved_non_inferior.py::test_the_verdict_is_recomputed_from_the_records_numbers`); `noninferiority.py check` on each; `payload-meter` for the three in the phase record beside phase 1's | 6f3ee98b |
| 5 | **The close.** `overview.md` (one line of purpose, divergences, `## Not verified` closed with the word `closed`, fed-back clauses); `changelog.md` from `templates/sdd-changelog.md`: the paragraph a plugin user reads (the smith preloads the contract alone, opens `implement` at the build and `writing-style` at the record, no proof block anywhere, the question status in words) and the per-agent table of preload bytes, tokens per tool call, spend and verdict at 2fc33333 and at phase 4's commit, each figure with its commit, read from the eval records and `payload-meter`; `questions.md` rows the work and the measurements answered, in words; `seal/follow-up.md`'s row narrowed to the scribe (Q2) | `bin/rules --check` exit 0; `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.1 --root <worktree> --worktree` exit 0; `bin/unverified-check` on this item; the fragment's figures traced to their records in the phase record | beeff829 |

This table is also where the work records how far it got. **Status is empty,
or the commit that closed the phase.** Re-read the column after any rebase.

### Test rows — what each case protects and the mutation it kills

| Case | Protects | Mutation it kills |
|---|---|---|
| T1 `tests/test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_contract_alone`, run on the smith (exists; the skip entry leaves in phase 2) | S1 — a second preload or a lost section | the smith's entry left in `NOT_YET_REWRITTEN`; a second `skills:` entry |
| T2 `…::test_every_file_a_step_names_exists` (exists) | S2 — a dangling path at a step | `skills/implements/SKILL.md` in a step |
| T3 `tests/test_a_moved_rule_leaves_its_definition.py::test_the_smiths_four_rules_stand_with_their_enforcers` (phase 2; NAME NOT IN TREE) | S4 — a new test starts from its group, commit before you mutate, the three-fix stop, the waiver in one sentence, each dropped in a later trim | any of the four paragraphs deleted; an `Enforced by:` line missing under one; the waiver stated in two sentences |
| T4 `tests/test_the_seal_is_taken_once_by_the_sealer.py::test_the_smith_names_no_runner_of_the_broad_gate` (phase 2; replaces `test_the_smith_says_who_takes_the_gate_it_hands_to`) | S5 — an owner sentence written into the smith from either worktree | *the sealer takes* or *the orchestrator runs* within the smith's gate paragraph passed; the *does not run* sentence deleted |
| T5 `tests/test_the_set_a_work_item_always_has.py::test_every_cited_heading_of_implement_exists` (phase 2) | S7 — a renamed step leaving `CLAUDE.md`'s and the hooks' citations dangling | `### 2.` retitled; a `§N` above 6 cited |
| T6 `tests/test_the_record_is_written_in_words.py::test_no_file_an_agent_reads_carries_an_emoji_or_a_proof_block` (phase 3; replaces `test_the_template_the_format_and_the_two_definitions_carry_no_emoji`) | S6 — a mark or a block coming back where an agent reads instruction | one of the three globs dropped; the `applied` pattern dropped; `U+FE0F` left out of the range; the skip map reading a file with no issue |
| T7 `tests/test_the_payload_meter_says_what_it_measured.py::test_each_language_section_of_writing_style_opens_alone` (phase 3), or a new module if the meter's module is the wrong home | S8 — a language heading renamed under the warden's step; the orientation line dropped | `## English prose rules` retitled; the first paragraph of `## 문장 규칙` not naming `## 구성 규칙` |

Each definition rewrite is verified by its eval record, the pins it
re-points, `rules --check` and `payload-meter`, not by a case on its
sentences; a case on a sentence is what held the bloat in place.

## Operational impact

- **What a plugin user sees.** The smith's definition is a page; a smith
  spawn opens `implement` with a `Read` at its first step and
  `writing-style`'s section before a record. The hand-back carries its claims
  under the three labels and no block; a spawn prompt that asks for the
  proof block gets the labels instead. A `questions.md` status reads `open`
  or `answered <date> by <who>`. `implement` loaded directly by a session
  ends no response with a block either.
- **The run.** Two paid phases on the orchestrator's account: about $60 each
  for the three agents by #957's phase-3 figures, plus one second run of one
  agent where a `fail` has a cause in this item's files. The stop rule is
  `questions.md` Q1's. CI pays nothing for the evaluation.
- **The suite.** Cases leave with the proof block and the narration pins;
  where `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py::test_the_durations_file_prices_the_suite`
  then fails past `STALE_SHARE`, the smith prunes `.test_durations` to the
  collected ids by the method #923's phase 5a used, and re-measures nothing
  (#957's `spec.md` §*What the referenced issues already decided*, #931).
- **Compatibility.** `agents/smith.md` names no runner of the broad gate; a
  reader wanting the owner opens contract §2, which #969 rewrites. The
  `writing-style` headings the warden names do not move. No new dependency.
