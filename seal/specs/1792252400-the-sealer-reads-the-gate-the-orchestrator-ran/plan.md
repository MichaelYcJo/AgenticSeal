# Implementation Plan: the sealer reads the gate the orchestrator ran (#969)

Approved 2026-10-18 by the orchestrator under the owner's delegation of that night (a plan that follows the orchestrator's stated design is approved by the orchestrator), when `smith` was spawned. Q1 and Q2 run on their defaults until the owner answers.

## Summary

The broad gate stops being the sealer's first act and becomes the
orchestrator's one command before the sealer is spawned; the sealer's first
act becomes reading the record that run wrote and refusing one that is not at
HEAD. The verdict words become `sealed`, `withheld`, `undecided`. The
sealer's model is decided by a measurement on two trees that differ in one
line. Build phases cost nothing and run in the smith's spawn; paid phases run
`noninferiority.py` on the orchestrator's account, and the two never share a
phase, so a side's spend is never mixed with a build's commits.

The comparison is two steps because `compare` refuses two sides whose suites
differ (`noninferiority.py:912-920`, exit 2). Step A (phases 1 to 4) changes
the sealer's behaviour on a suite whose verdict words are the old ones and
measures it against the sealer at 2fc33333 on that same suite. Step B (phases
5 and 6) renames the words everywhere in one commit and runs the sealer once
on the renamed suite as the reference a later sealer change compares against.
Nothing from step B is compared with anything from step A.

## Technical context

- `agents/sealer.md:40-55` is the run; `:106-110` the rule that assigns it;
  `tests/test_broad_gate_rule.py:179-283` and `:437-454` pin the interim
  state #957 left (§2 naming the sealer and #969). `tests/test_every_agent_reads_the_contract.py:38`
  skips the sealer by name for this issue.
- `skills/code-review/orchestration.md:178-249` is where the orchestrator's
  run is written; the preflight paragraph (206–215) stays; the stamp
  paragraph (217–236) and the refusal paragraph (238–249) are rewritten to
  the orchestrator meeting both directly. `hooks/sealer-stamp.py` draws the
  stamp at the main session's `Stop` from a values file keyed by the main
  session's id, whatever process wrote it, so the orchestrator's own run is
  drawn the same way the sealer's was (`hooks/sealer-stamp.py:6-11`, `read`).
- `docs/the-review-record.md:202-206` holds the rule the sealer's step 1
  applies; `chain_check.py#broad_gate` (1560–1581) applies the same rule at
  the pull request through `follows(root, sha, base, item)`.
- `rule_cases.py#sealer_case` (570–672) writes each case from `SEALER_RUNS`;
  `behaviour.write_case` writes `case.yaml`, `prompt.md`, `scaffold.sh` and
  `graders/`; nothing pins the committed cases to the generator's output.
- `noninferiority.py run --tree DIR` copies a directory in place of a git
  revision (`run_side`, 422–476) and records `rev` as the directory's
  absolute path; `--suite-rev` is extracted from git, so the regenerated
  cases must be committed before any side runs. `compare` reads both sides'
  `suite_tree`.
- #957's sealer figures: a side is 6 runs, $3.04 to $4.08, about 580 wall
  seconds at `-j 4`; with a fourth case about a third more.
- **What breaks in six months.** A new orchestrator paragraph, written in a
  prompt rather than read from the file, spawns the sealer without running
  the gate; the sealer returns `withheld — no broad run at HEAD` and the run
  stops with a sentence a person can act on. That is the failure direction
  chosen: the gate is never run twice and never run by an agent, and the
  cost of forgetting it is one spawn that reads a record and returns.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **Step 1 as a run of `chain_check.py --baseline <base> --sealing`**, reading the printed broad-gate arm instead of `git log --name-only` | `--sealing` prints and does not fail on that arm, so the sealer parses prose for a refusal; the arm's wording is pinned by nobody for this reader, and a change to it leaves the sealer reading nothing and sealing | Rejected. The sealer applies the doc's one-sentence rule with one `git log`; the rule's home stays `docs/the-review-record.md` §*The broad run has one home*, cited not restated |
| **Rename the comparison's reader: fold the sealer's step 1 into `broad-gate` itself** (the gate writes the `Target SHA` and `Broad gate` rows of `guarantee.md`, the sealer fills the rest) | Two writers of one file; `chain_check.py#guarantee` reads a file the sealer did not write whole, and the sealer's §6 write stops being one file | Rejected: a structure that replaces two files with two half-writers of one |
| **Replace the structure: no sealer agent; `guarantee.md` written by a script** that re-runs every `seen red` claim and diffs the parties' nouns | Steps 3 and 4 are judgments (which claims are thinnest, whether five accounts tell one story); a script does either all claims (the whole suite again) or none, and #957 S10's measurement would be of nothing | Weighed as an equal and rejected on the judgment steps; the mechanical half, the gate, is exactly what this item moves to a script |
| **Replace the structure: rename `hooks/sealer-stamp.py` and `bin/seal-stamp`** to the gate's name, since the stamp is the gate's run and the orchestrator now runs it | `dispatch.GROUPS["stop"]` (`hooks/dispatch.py:118`), `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:500` and the docs name the file; a rename is a hook-registration change under `CONTRIBUTING.md`'s gate bar for a name no reader decides on | Rejected for this item; the docstring is rewritten so the file says what it does. An owner who wants the rename gets one commit and three pins |
| **One step: rename the words first, regenerate, then measure** the rewritten sealer against the sealer at 2fc33333 on the renamed suite | The old sealer writes `sound` on a suite whose `shape-verdict` grader wants `sealed`: every shape-verdict and both truth graders fail on the baseline, so rule 3 and rule 1 pass trivially and the comparison measures the rename, not the behaviour | Rejected; this is the reason decision 3 is two steps |
| **Measure the model drop on the baseline suite only** (no fourth case, no new grader) | A Sonnet sealer that writes `sealed` without reading the record passes every grader the three cases have; nothing grades the one rule this item exists for | Rejected: `rule-sealer-no-gate` and `shape-runs-no-broad-gate` are added in phase 1, before the baseline, so both sides run them. Cost about $1.30 a side, inside decision 4's budget |
| **Decide the model by hand from the two records** | The decision reads seven rows across two files and is written in prose; a later reader cannot recompute it, which is #957 S10's defect | Rejected: `noninferiority.py model RECORD.md` holds the rule, about twenty lines with three fixture cases |
| **Measure the warden, smith and framer again here**, since §2 is in every preload (#969 guard 1) | About $59 at #957's phase-3 spends, over decision 4's $40; #967 and #968 measure the smith and the framer on trees that carry this §2 once they rebase | `questions.md` Q1, default: not here |
| **Edit `agents/framer.md:24` and `agents/smith.md:299` here**, one sentence each, under the rewrite-in-place rule | Touching either puts that agent's preload in this item's read set and guard 1 asks for its measurement; both files are being rewritten whole by #967 and #968 now | Rejected; decision 2 settles the smith's and the same grounds settle the framer's. The class grep in the phase record names both as the two sites left |

## Phases

Vertical slices. **B** is a build phase, the smith's, costing no spend;
**P** is a paid phase, run by the orchestrator on its own account with
`noninferiority.py`, and no build commit lands inside it. Every build phase
enumerates the class it removes by the `git grep` its record names, and
every new case is seen red first (contract §15), with the exit named in the
phase record. The `--suite-rev` of every step-A side is phase 1's commit.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 (B) | **The suite.** `rule_cases.py`: each sealer scaffold ends by writing `seal/specs/<item>/broad-gate.md` naming `$build against $(git rev-parse main)` and committing it as the item's record, so the run's SHA is followed by one records-only commit (the common case of the rule); `SEALER_RUNS` gains `rule-sealer-no-gate` (a `sound`-shaped item with no `broad-gate.md`, verdict `not sound`, truth `^Verdict:.*no broad run`); every sealer case gains `shape-runs-no-broad-gate` (`tool_used` Bash `broad-gate\s+--base`, max 0); the four directories regenerated and committed; `tests/test_evals_layout.py::test_the_sealer_cases_are_the_generators_output` (S11) and `sealer_grade_gaps` reading the new grader | `bin/test tests/test_evals_layout.py -q` exit 0; `python3 evals/scripts/rule_cases.py --out <scratch>` then `diff -r <scratch>/sealer evals/behaviour/sealer` exit 0; the new case seen red against the committed cases before regeneration; `bin/rules --check` exit 0 | c2544c8f |
| 2 (P) | **The baseline.** `noninferiority.py run --agent sealer --rev 2fc33333 --suite-rev <phase 1> --out seal/specs/<id>/evals/baseline-sealer.json --runs 2 -j 4`; raw output outside the tree; the file committed; spend, tokens, calls and `cut_short` read from it into the phase record. Independent of phase 3 and may run beside it | `cut_short` false; 8 runs; the spend named (Q5); `test_a_run_records_what_it_cost` holds the shape | 9184881a |
| 3 (B) | **The act moves.** `agents/sealer.md` written anew to #957's shape with the old verdict words, step 1 reading and refusing, step 3's re-run rule for a later run, `model: opus` until phase 4; contract §2 rewritten; `skills/code-review/orchestration.md:178-249` to the orchestrator's run, log, commit, quoted lines and stamp; `skills/implement/orchestration.md:40, 449-451`; `docs/the-broad-gate.md` §*One act, one owner* heading and body; `docs/the-review-record.md` §*The guarantee*'s first paragraph; `docs/the-agent-set.md:60`; `docs/the-record-layout.md:329`; `CONTRIBUTING.md:96, 107-109`; both README rows; `bin/test`, `bin/broad-gate`, `bin/seal-stamp`, `hooks/sealer-stamp.py`, `hooks/dispatch.py:28`, `hooks/commit-review-gate.py:1157`, `chain_check.py:1570`, `broad_gate.py:112`, `skills/verify/SKILL.md:397-404, 428, 947`, `templates/sdd-routing.md:27`; `templates/sdd-guarantee.md`'s `Target SHA` form and `Broad gate` cell; the pins: `tests/test_broad_gate_rule.py` (S2's one case replacing four), `tests/test_the_sealer_guarantees.py::TestDefinition` and `::TestTemplate` (S1, S5, S9), `tests/test_the_rules_have_one_owner.py:183`, `tests/test_the_suite_has_a_command_that_is_cheap_twice.py`, `tests/test_the_gate_asks_the_range_ci_will_ask.py#DESCRIBES_THE_BASE`, `tests/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`, `tests/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:549-570`, `tests/test_one_word_one_meaning.py:292-294`, `tests/test_every_agent_reads_the_contract.py:38`'s skip removed, `tests/test_no_passage_is_pasted_into_a_second_file.py` thresholds re-read; `hooks/commit-review-gate.py`'s message pin found by `git grep "CI still requires"` | the new cases red first then green; `bin/test` over every module named in this row exit 0; `bin/rules --check` exit 0; the class grep of `spec.md` §*The tree as it stands* finding only `agents/smith.md:299`, `agents/framer.md:24` and history; `payload-meter --agent sealer` in the phase record beside 28,358 | 1459b26f |
| 4 (P) | **The proof and the model.** `run --agent sealer --rev <phase 3> --suite-rev <phase 1> --out evals/sealer-phase-4.json`; `compare --agent sealer --phase 4 --old evals/baseline-sealer.json --new evals/sealer-phase-4.json --out evals/sealer-phase-4.md`; then a copy of the tree at phase 3 with `agents/sealer.md`'s `model: sonnet`, `run --tree <copy> --suite-rev <phase 1> --out evals/sealer-sonnet-phase-4.json`; `compare --old evals/sealer-phase-4.json --new evals/sealer-sonnet-phase-4.json --out evals/sealer-model.md`; `noninferiority.py model evals/sealer-model.md` (built in phase 3's commit, S7) prints the word; `agents/sealer.md` `model:` and both README rows set to it in one commit with the records; §*What a fail means here* applied | `sealer-phase-4.md` reading `pass`, or `fail` on rule 4 or 5 alone quoted in the record; `sealer-model.md` with both sides' graders and spend; `noninferiority.py check` exit codes named; the decision quoted; the Sonnet side's first trace naming `message.model` as Sonnet (Q4); `bin/test tests/test_the_sealer_guarantees.py -q` exit 0 after the `model:` edit | d27f7994 |
| 5 (B) | **The words.** `sealed`, `withheld — <reason>`, `undecided — <question>` in `chain_check.py` (constants, `verdict_word`, the refusal), `templates/sdd-guarantee.md`, `agents/sealer.md`, `docs/the-review-record.md:243-244, 252`, `docs/the-record-layout.md:330`, `skills/code-review/orchestration.md:190-199`, both READMEs, `.github/workflows/hygiene.yml:172`'s comment, `rule_cases.py#SEALER_RUNS` and the `shape-verdict` regex, the four cases regenerated; `tests/test_the_sealer_guarantees.py` rewritten (S8, with the case refusing `Verdict: sound` by line); the changelog fragment's paragraph for an in-flight item; `tests/test_one_word_one_meaning.py` run | the new case red against phase 4's tree then green; `bin/test tests/test_the_sealer_guarantees.py tests/test_evals_layout.py tests/test_one_word_one_meaning.py tests/test_chain_check.py -q` exit 0; `git grep -n -E "\bsound\b|not sound|undecidable"` outside `seal/specs/`, `changelog/` and history-quoting fixtures finding nothing; the generator diff of phase 1 exit 0; `bin/rules --check` exit 0 | ea61172c |
| 6 (P) | **The reference.** `run --agent sealer --rev <phase 5> --suite-rev <phase 5> --out evals/reference-sealer.json --runs 2 -j 4`, the model phase 4 decided; committed; its `suite_tree` named in the phase record as the one a later sealer change passes to `compare --old` | `cut_short` false; every grader's passed count read from the side's report rows at least phase 4's on the same model, by the phase record's table (no `compare`: the suites differ by design, S10); spend named | cb1940e3 |
| 7 (B) | **The close.** `overview.md` (purpose, divergences, `## Not verified` closed with #964's word, fed-back clauses); `changelog.md`: the paragraph a plugin user reads (S15) and the sealer's row of #957's per-agent table at 2fc33333 and at the close, each figure with its commit, read from `evals/`; `questions.md` rows the work and the measurements answered, in words | `bin/rules --check` exit 0; `chain_check.py --baseline origin/release/v0.22.1 --root <worktree> --worktree` exit 0 at the last round's commit; the fragment's figures traced to their records in the phase record | ba56ba60 |

This table is also where the work records how far it got. **Status is empty,
or the commit that closed the phase.** Re-read the column after any rebase:
`release/v0.22.1` moves when #967, #968 or #970 merge, and the class grep of
phase 3 is re-run after each rebase (Q7).

### Test rows — what each case protects and the mutation it kills

| Case | Protects | Mutation it kills |
|---|---|---|
| T1 `tests/test_broad_gate_rule.py::test_no_definition_assigns_the_broad_gate_and_the_orchestrator_runs_it_before_the_spawn` (phase 3; replaces three cases and the interim §2 case) | S2 — a definition taking the run back; the spawn written before the run | `broad-gate --base` inside any `agents/*.md` step passed; the orchestration's run sentence after its spawn sentence passed; §2 naming an agent as runner passed |
| T2 `tests/test_the_sealer_guarantees.py::TestDefinition::test_step_1_reads_the_record_and_runs_nothing` (phase 3) | S1 — the sealer running the gate | `broad-gate --base` in step 1 passed; the refusal for an absent or stale record dropped |
| T3 `…::TestTemplate::test_the_target_row_keeps_an_earlier_run` (phase 3) | S5 — a full re-audit | `; earlier run:` absent from the template passed |
| T4 `…::TestTemplate::test_the_template_carries_the_fields_sections_and_verdict_line` extended (phase 3) | S9 — `sealed` twice with two meanings | `sealed` in the `Broad gate` cell passed |
| T5 `tests/test_evals_layout.py::test_the_sealer_cases_are_the_generators_output` (phase 1) | S11 — a hand-edited grader | a committed grader differing from the generator's passed |
| T6 `tests/test_evals_layout.py::sealer_grade_gaps` extended (phase 1) | S1 — a sealer case without the no-run grader | a case lacking `shape-runs-no-broad-gate` passed |
| T7 `tests/test_a_rewritten_definition_proved_non_inferior.py::test_the_model_is_decided_by_the_truths_and_the_spend` (phase 3) | S7 — a drop decided by cost alone | a lost truth on the cheaper side printing `sonnet`; a lost shape grader printing `sonnet`; a higher spend printing `sonnet` |
| T8 `tests/test_the_sealer_guarantees.py::test_a_verdict_other_than_sealed_fails_a_ready_pull_request` and `::TestVerdictsOf` rewritten, plus `::test_the_old_words_are_refused_by_line` (phase 5) | S8 — two spellings in one tree | `sound` accepted; `withheld` without its reason read as `sealed`; `Verdict: sound` refused without naming the line |
| T9 `tests/test_the_gate_asks_the_range_ci_will_ask.py` with `DESCRIBES_THE_BASE` re-pointed (phase 3) | S6 — the base rule leaving with the sealer's step | the orchestration not telling the orchestrator to pass a plain branch name |
| T10 `tests/test_a_parallel_agent_names_its_scratch_after_the_work_item.py` re-pointed (phase 3) | S6 — two work items' gate logs in one file | the log path without `<work-item-id>` passed |
| T11 `tests/test_the_rules_have_one_owner.py` arrows case (phase 3) | S2 — the order in `skills/implement/orchestration.md` | `sealer` before `broad-gate --record` in the arrows passed |

The eval records verify the sealer's behaviour, S1 and S3 among them; a
case on a sentence holds the definition's words and never its conduct, which
is what #957 phase 3 measured in six of six runs.

## Operational impact

- **For a plugin user, the compatibility cost is a verdict word in an
  in-flight `guarantee.md`.** A work item whose `guarantee.md` reads `sound`
  at the update, with its pull request not yet merged, is refused by
  `chain_check.py` at a ready pull request naming the line, and by
  `broad-gate --preflight`'s record arms. The release note must say: do not
  edit the word; run `broad-gate --base <base> --record <item>` yourself,
  commit `broad-gate.md`, and spawn the sealer again at HEAD, which writes
  `sealed` and keeps the earlier verdict on its `Target SHA` row. The
  changelog fragment carries this paragraph.
- **A session that spawns the sealer the old way** — without running the gate
  first — gets `withheld — no broad run at HEAD` back and nothing broad has
  run. The note says the gate is the orchestrator's command now and names
  the order: preflight, `broad-gate --record`, commit, spawn.
- **The stamp** is drawn as before, at the end of the turn of the session
  that ran the gate, which is now the same session that spawns the sealer;
  nothing changes on screen.
- **Spend.** Where phase 4 decides Sonnet, a sealer spawn costs a Sonnet
  session; the note says which model the definition carries. The eval runs
  of this item: four sides at about $4 to $5.50 each with the fourth case,
  under $25 against decision 4's $40 (Q5 reads the real figure).
- **A `broad-gate.md` written before the update** is read by the new sealer
  unchanged; the file's shape does not move.
- No migration, no new dependency, no new environment variable.
