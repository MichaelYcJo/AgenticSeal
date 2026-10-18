# Feature Specification: the sealer reads the gate the orchestrator ran (#969)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

Split from #957 by the owner on 2026-10-17, one issue per agent. This frame
builds on #957's merged frame at
`seal/specs/1792126889-every-agent-is-written-anew-from-its-job/spec.md`
and cites it by section; what that file decided is not restated here. The
tree this item starts from is `release/v0.22.1` at 2fc33333, after #957
merged; the eval suite's cases are `af9c924b`'s until phase 1 regenerates
the sealer's.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | No step asks a person mid-run. What needs the owner is a row of `questions.md` with its default, and the paid runs go on the orchestrator's account |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The item changes one gate's owner, from the sealer's spawn to the orchestrator's command before it. §*The tree as it stands, measured* names what the sealer's own run cost; the failure direction is stated under S1 and S2; the prompt budget is zero; `## Removes` names what leaves |
| `docs/the-broad-gate.md` §*One act, one owner, and the owner is an agent* | Rewritten in place by this item: the act stays one, its owner becomes the orchestrator's one command, and no agent runs it. The heading's last clause is what this item makes false |
| `docs/the-review-record.md` §*The guarantee*, §*The broad run has one home, `broad-gate.md`, on either routing answer* | The first names the sealer's acts and the verdict words; this item rewrites the words and the first act. The second is the rule the sealer's step 1 applies to the file it reads: *its newest run is HEAD, or only the work item's records follow it* |
| `docs/the-agent-set.md` §*What each party writes, and when* | Says the sealer's broad run writes `broad-gate.md`; rewritten to the orchestrator's run |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The changelog is this item's `changelog.md`; it carries the sealer's row of #957's per-agent table and the paragraph a plugin user reads |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The item alters what a spawn reads, a verdict a check reads and a hook's message, so it sits on the top rung and this frame exists |
| #957's `spec.md` §*The shape of a definition* | The shape `agents/sealer.md` is written to: frontmatter with `skills: [agent-contract]`, the one contract sentence, `## Job`, `## Order of work`, `## Never`, `## Rules` with `Enforced by:` lines, no incident narrative |
| #957's `spec.md` §*The broad gate runs before the sealer* | The order: `broad-gate --base <base> --record <item>` with nothing else running, then the spawn; the sealer's first act is reading `broad-gate.md`; a re-run audits the commits since the last `guarantee.md` and keeps its line as `; earlier run: <sha> <verdict>` |
| #957's `spec.md` §*The sealer's model is decided by measurement* | The three cases on two trees differing in `model:`; Sonnet only where every truth grader passes as often and the spend is lower |
| #957's `spec.md` §*How the rewrite is proved not worse* | The verdict is `noninferiority.py#verdict` as it stands: every rule against the baseline, tokens across every model per tool call. `compare` refuses two sides whose suites differ, which is why the comparison is two steps |
| #957's `spec.md` §*Marks and labels*, the verdict row | The owner's words (2026-10-16): `sealed`, `withheld — <reason>`, `undecided — <question>`; any other spelling, the old words included, refused naming the line; the changelog tells an in-flight work item what to do |
| #969's body (the owner, 2026-10-17) | The baseline is the tree this issue starts from; the suite is fixed inside one comparison; three guards on a moving baseline; #957's phase-3 sealer record is not a baseline. Where this file and the body differ, the body holds |
| Orchestrator's decision 1 (spawn prompt, 2026-10-18) | **The act moves.** `agents/sealer.md` to #957's shape; its step 1 reads `broad-gate.md` and refuses one absent, or naming a commit that is neither HEAD nor followed only by the work item's own records; it runs nothing broad. Contract §2 becomes: no agent runs the broad gate; the orchestrator runs `broad-gate --base <base> --record <item>` with nothing else running, then spawns the sealer. The orchestration file, the two docs sections, `CONTRIBUTING.md` and every message or comment in `bin/`, `hooks/`, `skills/*/scripts/` that says the sealer runs it are rewritten in the same change. A re-run audits the commits since the last `guarantee.md` |
| Orchestrator's decision 2 | `agents/smith.md` is not touched here; #967 rewrites it and states only that the smith does not run the gate |
| Orchestrator's decision 3 | Two steps so the suite is the same on both sides of every comparison. Step A, behaviour: the sealer cases regenerated through `evals/scripts/rule_cases.py` to write `broad-gate.md` at HEAD, verdict words unchanged; the baseline is the sealer at 2fc33333 on that suite; the new side is the rewritten sealer, old words, on Opus and on a copy with `model: sonnet`. Step B, words: the rename in one commit, verified by the tests and one run on the renamed suite, recorded as the reference a later sealer change compares against, never compared with step A |
| Orchestrator's decision 4 | Measurement uses #957's verdict as it stands. About $4 a sealer side; the item's spend stays under $40 |

## Scope

**In.** `agents/sealer.md` written anew. Contract §2 and its pins. The
orchestration paragraphs that say the sealer runs the gate, in
`skills/code-review/orchestration.md` §*Orchestrator: the pull request opens
before round 1, and a phase is re-run* and `skills/implement/orchestration.md`
(the arrows at line 40 and the routing table at 449–451). The two docs sections
of §*Grounding*, plus the one-sentence sites `docs/the-agent-set.md:60` and
`docs/the-record-layout.md:329-330`. `CONTRIBUTING.md:96, 107-109`. Both
README editions' sealer row (`README.md:42`, `README.ko.md:40`). The comments
and messages: `bin/test:23-25`, `bin/broad-gate:4`, `bin/seal-stamp:7`,
`hooks/commit-review-gate.py:1157`, `hooks/sealer-stamp.py` docstring (lines
2, 4, 21, 25, 53), `hooks/dispatch.py:28`,
`skills/code-review/scripts/chain_check.py:1570`,
`skills/verify/scripts/broad_gate.py:112`. The two `skills/verify/SKILL.md`
passages outside the section #967 holds: *It belongs to the `sealer`*
(397–404) and *What the sealer's seal covers* (428), and line 947.
`templates/sdd-routing.md:27`. `templates/sdd-guarantee.md`: the `Target SHA`
row gains the `; earlier run:` form, and the `Broad gate` cell is rewritten
(§*Data & interfaces*). The verdict words in every reader of §*The tree as it
stands*. `evals/scripts/rule_cases.py`'s sealer generator and the regenerated
cases under `evals/behaviour/sealer/`. `noninferiority.py`'s model decision
(§*Data & interfaces*). The test modules that pin any of the above, re-pointed
where the rule stays and removed with one line in the phase record where they
pinned narration. The eval records under this item's `evals/`, and the
changelog fragment.

**Out, and whose.** `agents/smith.md:299` (*Then the sealer takes the broad
gate once*) — #967, which rewrites the file now in the main checkout, and
whose rewrite states that the smith does not run the gate (decision 2).
`agents/framer.md:24` (*`sealer` runs the broad gate over what is left*) —
#968, which rewrites that file whole; a one-word edit here would put the
framer's preload in this item's read set and, by #969's guard 1, buy a
framer measurement (about $17 at #957's phase 3) for one word. `skills/verify/SKILL.md`
§*Every agent seals what it verified, and one of them is final* — #967,
whose rewrite already states the fact this item needs (the hand-back's three
labels carry the claims and `guarantee.md` is the sealer's seal); its *Form*
bullet, which says the sealer's seal is the drawn one, becomes false here
and true again under #967's wording, so it is not edited twice. The hook's
file name `hooks/sealer-stamp.py` and `bin/seal-stamp` — kept; `plan.md`'s
Alternatives weighs the rename. The emoji in `hooks/` and the scripts, and the
history in `changelog/`, `seal/specs/*/rounds/` and `hooks/config.py:273`
(a past-tense docstring about #401) — stay as history, #957 Q9 and Q10. The
scribe — #970. The per-grader rule's sample size — #966. The warden, smith
and framer measurements guard 1 would ask for — `questions.md` Q1.

## What the referenced items already decided

| Item | Already decided | What this frame does with it |
|---|---|---|
| #957 (merged at 2fc33333) | The shape; the gate before the sealer; the verdict words; the model by measurement; the two axes and five rules of the proof; the baseline once at af9c924b; the four new contract rules; §2 left saying *no agent but the sealer* with #969 named as what moves it (`tests/test_broad_gate_rule.py:179-246`) | Not reopened. §2 is rewritten here to the fact #957 reserved for this item, and the four pins that held the interim wording are rewritten with it |
| #957 phase 3 (`phases/phase-3.md` §*The sealer*) | The sealer's record measures a definition the contract contradicted; in 6 of 6 runs a side the sealer's first act was `broad-gate --record`, every first call exited 134 on the eval sandbox's interpreter block, and one run wrote no `guarantee.md` after reading the refusal | The record is not a baseline (#969 body). The sandbox block is a fact about the gate in the eval and leaves with the gate; whether the sealer's step-3 re-run of a case meets it is `questions.md` Q3 |
| #957 `questions.md` Q6 (answered 2026-10-17) | `claude plugin eval` honours a definition's `model:` for the subagent; every assistant event names `message.model` | The Sonnet side varies one line of a tree copy, as planned; Q4 of this item's `questions.md` reads the copy's first trace to confirm `--tree` behaves as `--rev` did |
| #964 (merged) | The round record's grammar as one table; the `Reads:` census and the rider stamps gone; the closing word | Nothing here writes a stamp, a census or a ledger row |
| #923 Q7 | An item is judged at its own pull request | A `fail` on a cost rule alone is recorded as it reads and the item goes to its pull request with the record; the owner reads it there (#957 did this for the framer) |

## The tree as it stands, measured

Read at 2fc33333 in the worktree, `executed` where a command produced the
number (`git grep`, `wc`, `ls`), `read` where a document did.

- **Sites that say the sealer runs the gate or owns its run** (`executed`:
  `git grep -n -i -E "sealer.{0,60}(runs?|running|takes?|owns?).{0,40}(broad gate|broad-gate|suite)|(broad gate|broad-gate).{0,60}sealer"` plus a
  `git grep -n -i sealer` over `bin/ hooks/ skills/*/scripts/`, each hit
  opened): 22 files outside `tests/`, `seal/specs/` and `changelog/`, of
  which two are other issues' (`agents/smith.md:299` #967,
  `agents/framer.md:24` #968). The twenty this item rewrites are the files
  §*Scope* lists under *In*, and `agents/sealer.md` itself holds the rule
  (*The broad gate is yours*, lines 106–110) and the step (40–55).
- **Test modules that assert the sealer's run or its owner** (`executed`):
  8 — `tests/test_broad_gate_rule.py` (four cases: 179, 248, 285, 437),
  `tests/test_the_sealer_guarantees.py::TestDefinition` (four cases, 253–292),
  `tests/test_the_rules_have_one_owner.py:183` (the arrows),
  `tests/test_the_suite_has_a_command_that_is_cheap_twice.py:189, 207, 1231`
  (`bin/test` and `CONTRIBUTING.md` say the suite is the sealer's),
  `tests/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:78-93`
  (the sealer's capture file and the `outputs kept under` quote),
  `tests/test_the_gate_asks_the_range_ci_will_ask.py:733-785, 821, 1129`
  (the sealer describes the base's resolution),
  `tests/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:549-570`
  (the sealer meets the row's exit-2 refusal),
  `tests/test_one_word_one_meaning.py:292-294` (*You take the last seal*).
  Two more hold comments only (`tests/test_the_seal_is_taken_once_by_the_sealer.py:7853, 8224`;
  `tests/test_evals_layout.py:122, 146`), and that module's `:8318` pins
  `agents/smith.md`'s sentence, which stays until #967.
- **Readers of the verdict words** `sound`, `not sound`, `undecidable`
  (`executed`, `git grep -n -E "not sound|undecidable|\bsound\b"`, history
  excluded): 12 files — `skills/code-review/scripts/chain_check.py` (constants
  83–85, `verdict_word` 1594–1603, the refusal 1645–1652),
  `templates/sdd-guarantee.md:29-33`, `agents/sealer.md:8, 49, 70, 112`,
  `docs/the-review-record.md:243-244, 252`, `docs/the-record-layout.md:330`,
  `skills/code-review/orchestration.md:190-191, 199`,
  `evals/scripts/rule_cases.py:556, 563` and its `shape-verdict` regex,
  the three `evals/behaviour/sealer/*/graders/shape-verdict.md`,
  `tests/test_the_sealer_guarantees.py:155, 179-180, 228-235`,
  `README.md:42`, `README.ko.md:40`, and the comment at
  `.github/workflows/hygiene.yml:172`.
- **The sealer's cases and their generator** (`executed`): 3 cases under
  `evals/behaviour/sealer/` (`rule-sealer-sound`, `-untrue-body`,
  `-false-red`), 5 graders each plus a `truth-` grader on the last two (17 in
  all: 3 reach, 12 shape, 2 truth), each case 2 runs, `max_turns` 12,
  timeout 1,800 s, the case session on Sonnet with the definition's `model:
  opus`; written by `rule_cases.py#sealer_case` from `SEALER_RUNS` (lines
  553–568), 708 lines, with no pin that the committed cases equal the
  generator's output.
- **The pins on `agents/sealer.md`** (`executed`, `git grep -l`): 14 test
  modules name the file by path; 27 mention the word. `tests/test_every_agent_reads_the_contract.py:38`
  skips the sealer by name for `#969`; `tests/test_no_passage_is_pasted_into_a_second_file.py:206-230`
  holds its pairwise thresholds (65 with each definition, 3 with
  `code-review/orchestration.md`, 1 with `verify/SKILL.md`);
  `tests/test_docs_line_wrap.py:149` wraps it.
- **The definition** (`executed`, `wc`): 143 lines, 7,990 bytes; preload with
  the contract 28,358 bytes at af9c924b (`baseline-sealer.json`, `read`).
  **The cost of a sealer side** (`read`, `#957/evals/sealer-phase-3.md`): 6
  runs, $3.04 and 3,324,087 tokens over 97 tool calls on the baseline; $4.08
  and 3,096,365 over 84 on the new side; 577 wall seconds each. Rule 5 read
  34,268.9 against 36,861.5 tokens per call, and the run that lost a truth
  was the one that stopped at the gate's refusal.
- **What the sealer's own run cost in the flow** (`read`, #957's
  `guarantee.md` and `questions.md`): the owner already ran the gate before
  spawning #957's sealer (its `Target SHA` row carries `; earlier run:
  1e833533 not sound`), so the new order has run once in this repository
  under the old definition.
- **The orchestration's shape today** (`read`): `skills/code-review/orchestration.md:178-201`
  says the orchestrator runs `broad-gate --preflight`, spawns the sealer, and
  the sealer runs `broad-gate --record`; 206–215 the preflight; 217–236 the
  stamp drawn at the spawning session's turn end; 238–249 the row's exit-2
  refusal arriving through the sealer.

## The act, as this item leaves it

The orchestrator, once the pull request body and `changelog.md` are written
and `broad-gate --preflight --base <base>` has exited 0, runs `broad-gate
--base <base> --record <item>` with nothing else running, sends its output to
`<scratchpad>/<work-item-id>/broad-gate.log`, reads the whole log and the exit
code directly, and on exit 0 commits `broad-gate.md` and spawns the sealer
with the base, the item, the issue and the pull request. On exit 1 nothing is
spawned: the failing check is repaired, reviewed where it touched a file
outside the item's records, and the gate runs again. On exit 2 the refusal
about the `Broad gate` row goes to a person as the orchestration already
says. The gate's lines that only it can tell — the moved base, the tree's
copy, `outputs kept under` — reach the person in that session's own output,
and the `SEALED` stamp is drawn by the same `Stop` hook at the end of the same
turn, so nothing relays them.

The sealer's step 1 reads `broad-gate.md` in the work item's directory, takes
the newest run's SHA, and applies `docs/the-review-record.md` §*The broad run
has one home*: `git log --name-only <sha>..HEAD` lists paths under
`seal/specs/<item>/` and nothing else, or the file is absent, or its SHA is
behind that rule — then the sealer writes `guarantee.md` with the verdict
`withheld — no broad run at HEAD` (step A: `not sound — no broad run at
HEAD`) and returns; it runs nothing broad in any case. Steps 2 to 5 stay as
0.22.0 left them. A re-run at a new HEAD, where an earlier `guarantee.md`
stands, re-runs only the claims whose coordinates a commit since the earlier
`Target SHA` touched, keeps the earlier verdict as `; earlier run: <sha>
<verdict>` on its `Target SHA` row, and reads the parties again.

## User scenarios & acceptance *(mandatory)*

Each row says what it protects: the defect it would catch, and why no other
case does.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The sealer runs nothing broad | Given a sealer spawn, when it reaches step 1, then it reads `broad-gate.md` and runs no `broad-gate --base`, no suite, no lint | `tests/test_the_sealer_guarantees.py::TestDefinition::test_step_1_reads_the_record_and_runs_nothing` (no `broad-gate --base` in the definition's steps; the refusal named); the `shape-runs-no-broad-gate` grader on every sealer case (`tool_used` Bash, `broad-gate\s+--base`, max 0) passing on the new side. Protects: the sealer re-running a suite the orchestrator just ran, the 240K-token second run #957 found; a sentence pin alone cannot see a sealer that reads the sentence and runs anyway, which phase 3 measured in 6 of 6 runs |
| S2 No definition assigns the gate; the orchestrator runs it before the spawn | Given the contract and the five definitions, when read, then §2 says no agent runs the broad gate and names the orchestrator's command; no file under `agents/` hands itself the suite; the orchestration section names the run, its log and its commit before the sentence that spawns | `tests/test_broad_gate_rule.py::test_no_definition_assigns_the_broad_gate_and_the_orchestrator_runs_it_before_the_spawn`, replacing `test_the_prohibition_itself_has_one_home_and_it_is_the_contract`, `test_the_sealer_counts_the_silent_definitions_from_the_glob` and `test_the_orchestrator_runs_the_preflight_before_it_spawns_the_sealer`; `tests/test_the_rules_have_one_owner.py` arrows case rewritten. Protects: a definition taking the run back, and the orchestration spawning before the run |
| S3 An absent or stale record is a withheld verdict | Given no `broad-gate.md`, or one whose newest run is followed by a commit outside the item's records, when the sealer is spawned, then `guarantee.md` reads `withheld — no broad run at HEAD` and nothing else was written | the fourth sealer case `rule-sealer-no-gate` (scaffold writes no `broad-gate.md`), `truth-no-gate` reading the verdict line's reason. Protects: a sealer that seals over a run that never happened, which S1 cannot see — a sealer that runs nothing and writes `sealed` passes S1 |
| S4 The three cases hold their truths without the gate | Given the regenerated `sound`, `untrue-body` and `false-red` cases, whose scaffolds commit `broad-gate.md` at HEAD with the run's SHA followed only by that record, when run, then each truth and shape grader passes on the new side at least as often as on the baseline | `evals/sealer-phase-4.md` reading `pass`, or a `fail` on a cost rule alone with the outcome rules passing (§*What a fail means here*). Protects: a step 1 that refuses a record the rule accepts (the record commit after the run's SHA is the common case) |
| S5 A re-run audits only what changed | Given an earlier `guarantee.md`, when the sealer runs again at a new HEAD, then its `Target SHA` row carries `; earlier run: <sha> <verdict>` and its claims re-run are those a commit since touched | `tests/test_the_sealer_guarantees.py::TestTemplate::test_the_target_row_keeps_an_earlier_run` and `TestDefinition`'s step sentence; `chain_check.py#target_of` reading the first SHA (exists). Protects: a full re-audit for a records-only commit |
| S6 The orchestrator reads the base, the log and the stamp | Given the orchestration file, when read, then it tells the orchestrator to pass the base as a plain branch name, where the gate's output goes, what to quote, and that the stamp is drawn at its own turn's end | `tests/test_the_gate_asks_the_range_ci_will_ask.py` with `DESCRIBES_THE_BASE` re-pointed from `agents/sealer.md` to the orchestration file; `tests/test_a_parallel_agent_names_its_scratch_after_the_work_item.py` re-pointed. Protects: the base-resolution rule leaving the tree with the sealer's step that carried it |
| S7 The sealer's model by measurement, and not by cost alone | Given `evals/sealer-phase-4.json` on Opus and `evals/sealer-sonnet-phase-4.json` on a copy with `model: sonnet`, when `compare` writes `evals/sealer-model.md`, then `noninferiority.py model` reads `sonnet` only where every truth grader and every shape and reach grader passes on the Sonnet side at least as often and its spend is lower, and `agents/sealer.md`'s `model:` reads that word | `tests/test_a_rewritten_definition_proved_non_inferior.py::test_the_model_is_decided_by_the_truths_and_the_spend` over fixture records (a lost truth on the cheaper side → `opus`; equal graders and lower spend → `sonnet`; higher spend → `opus`); the phase record quotes the rows. Protects: a drop decided by cost alone (#957 S10), and a cheaper model that commits or writes outside its file, which the truth graders cannot see |
| S8 The words | Given the reader, the template, the docs, the definition, the generator and the graders, when read after phase 5, then the verdict words are `sealed`, `withheld — <reason>`, `undecided — <question>`, and `sound`, `not sound` and `undecidable` are refused naming the line | `tests/test_the_sealer_guarantees.py`: `TestVerdictsOf` and `test_a_verdict_other_than_sealed_fails_a_ready_pull_request` rewritten, plus one case that `Verdict: sound` is refused naming the line; `tests/test_evals_layout.py::test_every_sealer_case_grades_the_guarantee` reading the new word; `git grep -n -E "\bsound\b|not sound|undecidable"` over the tree outside `seal/specs/`, `changelog/` and `tests/` fixtures quoting history finding nothing. Protects: two spellings in one tree, where a check accepts one and a person writes the other |
| S9 `sealed` has one meaning in `guarantee.md` | Given the template, when read, then `sealed` appears on the `Verdict:` line alone and the `Broad gate` cell quotes the run `broad-gate.md` names | `tests/test_the_sealer_guarantees.py::TestTemplate::test_the_template_carries_the_fields_sections_and_verdict_line` extended; `tests/test_one_word_one_meaning.py` green. Protects: a reader taking the gate's cell for the sealer's verdict, the overload #331 measured for `seal` |
| S10 The suite is the same on both sides of every comparison | Given the regenerated cases committed in phase 1, when any side runs, then `--suite-rev` names that commit for every step-A side and the phase-5 commit for the reference, and `compare` is never asked across the two | `noninferiority.py compare` exit 0 for `sealer-phase-4.md` and `sealer-model.md`; the reference side's `suite_tree` named in the phase record and never passed to `compare`. Protects: a rename read as a changed agent, which `compare` refuses at exit 2 and a hand table would not |
| S11 The committed cases are the generator's | Given `evals/behaviour/sealer/`, when `rule_cases.py --out <tmp>` runs, then its sealer directories equal the committed ones | `tests/test_evals_layout.py::test_the_sealer_cases_are_the_generators_output` (new). Protects: a hand edit to a grader that the generator then overwrites, which is how the baseline and a later side silently run different suites |
| S12 Nothing in the tree says the sealer runs the gate | Given the twenty files of §*Scope*, when the phase closes, then the class grep of §*The tree as it stands* finds nothing outside `seal/specs/`, `changelog/`, `agents/smith.md` and `agents/framer.md` | the grep named in the phase record, `bin/rules --check` exit 0, `tests/test_no_passage_is_pasted_into_a_second_file.py` green. Protects: the stale half of a file misleading the next session, the item's root problem |
| S13 Every case says what it protects | Given a test or grader this item writes, when read, then its docstring or description names the defect and why no other case catches it | the warden's reading of the diff; `Enforced by: nothing — a reading from words is a report`. Protects: a suite that grows by default (#942) |
| S14 Nothing asks a person | Given this run, when any phase executes, then no step stops for an answer; each `questions.md` row carries its default | `plan.md`'s rows read by the orchestrator; the sealer's step 4 reads the parties. Protects: a run that stops at minute thirty |
| S15 The changelog tells a plugin user what changes for them | Given the fragment, when read, then it says where the gate runs now, what the sealer refuses, what the verdict words are, what an in-flight `guarantee.md` reading `sound` does at a ready pull request, and the sealer's model, with the sealer's row of the per-agent table at 2fc33333 and at the close | `tests/test_the_pull_request_language_is_the_repositorys.py` and the fragment's heading rule; the sealer reads the fragment against the eval records. Protects: a user whose sealer comes back `withheld` with no idea why |

## What a fail means here

`noninferiority.py#verdict` has five rules; the first three are outcome, the
last two cost. A record reading `fail` on rule 4 or 5 alone, every outcome
rule passing, is written as it reads, quoted in the phase record and the
changelog table, and the item goes on to phase 5 and to its pull request,
where the owner reads it (#957 did this for the framer's rule 5; #923 Q7
says an item is judged at its own pull request). A `fail` on rule 1, 2 or 3
stops phase 4: the definition is revised once against what the losing runs
did, the Opus side runs again, and the record of that second side is the
one the item ships with, pass or fail. Nothing here asks the owner mid-run.

## Data & interfaces

- **`agents/sealer.md`**: frontmatter `name`, `description`, `model: <the
  word phase 4 decides>`, `skills: [agent-contract]`; body `# sealer`, the
  contract sentence identical to `agents/warden.md:13`, `## Job` (verify
  independently, guarantee, one durable write: `guarantee.md`), `## Order of
  work` (1 read `broad-gate.md` and apply the one-home rule; 2 read the
  issue, the diff and the records; 3 the two acts; 4 the parties; 5 write
  `guarantee.md`; 6 return the file's text with every claim labelled),
  `## Never` (run the broad gate, lint or typecheck; re-judge design or
  quality; take a party's account as fact; change the tree but its file;
  choose a `Broad gate` command; draw a stamp), `## Rules` (a verdict names
  what it rests on; a `seen red` is re-run at base in
  `<scratchpad>/<work-item-id>/at-base/`; name the command and bind to a
  tree state; `sealed` is earned by the run; the guarantee covers HEAD and a
  re-run audits what changed). The rules on quoting the gate's lines and the
  capture log leave with the run.
- **Contract §2**: *Narrow and often; the broad gate is one act, run by the
  orchestrator before the sealer is spawned.* No agent runs any of the
  three. `broad-gate --base <base> --record <item>` is the command. Hand over
  with the suite labelled `unverified` and the orchestrator named. The number
  2 is kept (#957: a section number is never reused).
- **The orchestration** (`skills/code-review/orchestration.md` §*the pull
  request opens before round 1*): preflight → `broad-gate --record`, nothing
  else running, log at `<scratchpad>/<work-item-id>/broad-gate.log`, exit
  read directly → commit `broad-gate.md` → spawn the sealer → commit
  `guarantee.md`; the base passed as a plain branch name and the lines only
  the gate can tell quoted, moved here from the sealer's step 1; the stamp
  paragraph rewritten to the orchestrator's own run; the exit-2 refusal met
  by the orchestrator directly. `skills/implement/orchestration.md:40`'s
  arrows gain `broad-gate --record, yours →` before `sealer`, and the table
  at 449–451 says *your one broad run*.
- **`templates/sdd-guarantee.md`**: `| Target SHA | <sha> against <base>[;
  earlier run: <sha> <verdict>] |`; `| Broad gate | <the run broad-gate.md
  names, `<sha> against <base>`> |`; the verdict comment and line in the new
  words after phase 5.
- **`chain_check.py`**: `SEALED = "sealed"`, `WITHHELD = "withheld"`,
  `UNDECIDED = "undecided"`; `verdict_word` reads the three; the refusal
  names `sealed`; the broad-gate arm's message says the orchestrator runs
  the command.
- **`rule_cases.py`**: `SEALER_RUNS` gains `("no-gate", True, "", <withheld
  word>, r"^Verdict:.*no broad run")`, each sealer scaffold ends by writing
  `seal/specs/<item>/broad-gate.md` with `| Broad gate | $build against
  $(git rev-parse main) |` and committing it (the no-gate case skips this),
  and every sealer case gains `shape_tool("runs-no-broad-gate", "Bash", …,
  input_match=r"broad-gate\s+--base", max=0)`. Step A writes the old words;
  phase 5 the new.
- **`noninferiority.py`**: a `model RECORD.md` subcommand, printing `sonnet`
  where every grader's new passed count is at least the old's and the new
  spend is lower, else `opus`, exit 0; exit 2 where the record does not
  parse. The rule's one home, so S7 is recomputed rather than read.
- **The eval records** under `seal/specs/<id>/evals/`: `baseline-sealer.json`
  (the sealer at 2fc33333 on the phase-1 suite), `sealer-phase-4.json` and
  `.md` (Opus), `sealer-sonnet-phase-4.json`, `sealer-model.md` (the two
  model sides), `reference-sealer.json` (phase 6, the renamed suite on the
  decided model). Raw output stays outside the tree.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The sealer's broad run: step 1 as a run, the rule *The broad gate is yours*, the exit-0/1/2 bullets, the capture log, the rule to quote the gate's lines, the row-refusal bullet | `agents/sealer.md:40-55, 94-110, 135-138` | the orchestrator's run in `skills/code-review/orchestration.md`; the base rule, the log path and the quoted lines move there; the exit-2 refusal is already the orchestrator's paragraph |
| The description's *it runs the broad gate* and `model: opus` as a fixed value | `agents/sealer.md:4-10` | the description says it reads the run's record; `model:` reads the word phase 4 decides |
| §2's interim sentences: *No agent runs any of the three but the sealer, whose definition hands it that run; #969 moves the run to the orchestrator* | `skills/agent-contract/SKILL.md:37-48` | the fact: no agent runs it, the orchestrator runs the command before the spawn |
| The four pins on the interim §2 and on the sealer as owner | `tests/test_broad_gate_rule.py::test_the_prohibition_itself_has_one_home_and_it_is_the_contract`, `::test_the_sealer_counts_the_silent_definitions_from_the_glob`, `::test_the_orchestrator_runs_the_preflight_before_it_spawns_the_sealer`, `::test_no_definition_promises_the_suite_once_the_rounds_settle`'s docstring sentence about the sealer, `ASSIGNS_THE_GATE`, `SILENT_IN_WORDS`, `STAY_SILENT` | one case: no definition assigns it, the orchestration runs it before the spawn (S2) |
| The sealer runs `broad-gate --record` and takes the one broad pass | `skills/code-review/orchestration.md:178-201` two paragraphs, `:206` *the sealer's run*, `:217-236` *the sealer's pipe*, *relaying the sealer's log*, `:238-249` *The sealer comes back exit 2* | the orchestrator's run, in the same section, before the spawn sentence |
| *the owner is an agent* and the paragraph assigning the act to the sealer's definition | `docs/the-broad-gate.md:11-28` | the section says the owner is the orchestrator's one command and no agent runs it; its `Enforced by:` names the new case |
| *the sealer's broad run writes `broad-gate.md`*, *the sealer's one broad run* | `docs/the-agent-set.md:60`, `docs/the-record-layout.md:329`, `templates/sdd-routing.md:27`, `skills/implement/orchestration.md:40, 449-451` | the orchestrator's run |
| *The full suite is the sealer's* and *`agents/sealer.md` is the agent it is assigned to* | `CONTRIBUTING.md:96, 107-109`, `bin/test:23-25`, `bin/broad-gate:4`, `bin/seal-stamp:7`, `hooks/dispatch.py:28`, `hooks/sealer-stamp.py:2, 4, 21, 25, 53`, `hooks/commit-review-gate.py:1157`, `chain_check.py:1570`, `broad_gate.py:112`, `skills/verify/SKILL.md:397-404, 428, 947` | each sentence rewritten to the orchestrator's run; the pins in `tests/test_the_suite_has_a_command_that_is_cheap_twice.py` re-pointed |
| The README rows' *it runs the one broad gate* and *(subagent, Opus)* where the model changes | `README.md:42`, `README.ko.md:40` | *reads the record of the one broad gate the orchestrator ran*; the model word phase 4 decides |
| The pins that read the sealer as the describer of the base, the holder of the capture file and the party meeting exit 2 | `tests/test_the_gate_asks_the_range_ci_will_ask.py#DESCRIBES_THE_BASE` and its five sites, `tests/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:78-93`, `tests/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:549-570` | re-pointed to `skills/code-review/orchestration.md`, where the sentences now stand |
| `TestDefinition`'s four cases on the old steps | `tests/test_the_sealer_guarantees.py:253-292` | `test_step_1_reads_the_record_and_runs_nothing`, the model case reading a word, the template case kept, step 3's case kept |
| The `#969` skip of the sealer | `tests/test_every_agent_reads_the_contract.py:38` | the sealer meets S1 and S2 of #957 like the warden |
| The verdict words `sound`, `not sound`, `undecidable` | the 12 files of §*The tree as it stands* | `sealed`, `withheld — <reason>`, `undecided — <question>`, in one commit (phase 5) |
| `sealed` / `not sealed — …` as the `Broad gate` cell's values | `templates/sdd-guarantee.md:11` | the cell quotes the run `broad-gate.md` names; the sealer sees no gate output to quote |
| The three committed sealer cases as they stand | `evals/behaviour/sealer/rule-sealer-{sound,untrue-body,false-red}/` | regenerated with `broad-gate.md` at HEAD and the new grader; a fourth case beside them |
| The pin that the sealer runs on Opus | `tests/test_the_sealer_guarantees.py::TestDefinition::test_the_sealer_runs_on_opus_with_the_contract_alone` | a case that `model:` is one word and the preload is the contract alone |

## Open questions → questions.md

Every decision the tree could make is made above with its grounds; what
only the owner can settle, what a measurement settles and what the work
settles are the rows of `questions.md`, each with the default this run
takes.

Framed 2026-10-18 by framer, before the build.
