# Implementation Plan: every agent is written anew from its job (#957)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved <date> by <who>, when `smith` was spawned.

## Summary

Every agent definition and the contract are written anew from the job each
does, in one shape: the contract sentence, the job and its one write, the
order of work with the file each step opens, what it never does, and its
rules with what enforces each. Every `skills:` list is cut to the contract,
and the four skills the lists used to inject are written to the same shape
so the agent that opens one at its step reads the current rule once. The
marks nobody reads leave: the proof block, the emoji in every file an agent
reads, the batching numbers copied into the definitions, the `Reads:`
census with its 994-line list and the rider stamps with their checker. The
round record's grammar becomes one table in `docs/the-review-record.md`
that `chain_check.py` loads and matches whole. The broad gate runs as the
orchestrator's one command before the sealer is spawned, and the sealer
reads its record. The sealer's model is measured on Sonnet against Opus. A
baseline is taken once on the released tree, and every phase that changes
an agent's preload proves that agent not worse on outcome and cheaper on
cost before the next agent follows; the warden goes first, alone, as the
proof of the approach on one file.

## Technical context

Read at d4552372, the release this branch is cut from; `executed` where
`spec.md` §*The tree as it stands, measured* says so.

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
  The one emoji a gate reads is `unverified_check.py#CLOSED` (line 75),
  called at `:823` and in two messages at `:1675` and `:1792`.
- **The census.** `docs/the-reader-registry.md` (152 lines) states the
  grammar, the population, K1, the census and the `## Removes` rule;
  `tests/reader_registry.py#GRAMMAR` and
  `tests/test_a_reader_declares_its_input_class.py` read it;
  `CONTRIBUTING.md:247-251` asks for the line. `rider_check.py`'s stamp is
  `Verified <date> against <anchor>@<hash>`, resolved by
  `skills/verify/scripts/coordinates.py`; `tests/test_a_rider_reaches_its_file.py`
  holds the stamp cases beside the `seal/follow-up.md` cases.
- **The check.** `chain_check.py:93-191` holds the label constants, the
  exact and misspelt label patterns, and the value patterns; `records`
  (`:1230` on) reads through them; `ROUTING` (`:63`) shows how the script
  finds a sibling file by relative path, which the grammar loader reuses.
  `templates/sdd-round.md:3-14, 32-60` and `templates/config.md` §*What no
  row governs* restate the labels; `tests/test_the_pull_request_language_is_the_repositorys.py#ROUND_RECORD_FIELDS`
  derives the literal list. The user's hygiene workflow clones this
  repository at the pinned tag into `$RUNNER_TEMP/specseal` and runs the
  check from there (`templates/hygiene.yml:58-59, 92`), so the document is
  beside the script wherever it runs.
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
  recomputes. No baseline exists. One case this item owns is red on `main`
  at d4552372 (run 38852872472, `read`): the Windows path case at
  `tests/test_a_rewritten_definition_proved_non_inferior.py:623`. The same
  run's sealer-guarantees case is fixed by #963 outside this item (the
  fixture clears `GITHUB_ACTIONS`, under which the check prints `::error`
  annotations), and this plan does not touch it.
  `evals/README.md:34-35` names a `--list` flag that does not exist, and
  `replay_targets.py` reads a round's asked paragraph from a section new
  records do not carry (#923 `overview.md` §*Not done*, `read`).
- **The suite and CI.** 7,329 cases priced at 3,371 s; one run is 55 runner
  minutes over three legs, under 11 minutes wall, 208 billable minutes if
  private. The census module is 38.4 s of that, the rider module 3.5 s, the
  42 agent-pin modules 878 s together (most of which stays).

**What breaks in six months with the chosen approach.** A definition that
names a skill at a step and an agent that skips the step reads nothing of
the skill, and the only thing that sees it is a `shape-` grader at the next
run of that agent's cases; between runs the loss is invisible, and
`evals/README.md` says nothing in the tree makes a later edit owe a run. A
later change that appends a paragraph to a definition is caught by nobody
mechanical: the cost rule reads bytes only when somebody runs the suite, and
the warden's reading of the diff is what holds the shape. The grammar table
is read by the check from a document under `docs/`, so a `docs/` rewrite
(#941) that moves the heading or splits the file breaks the check loudly, at
exit 2, in CI, which is the direction chosen. The orchestrator's gate run
before the sealer is a sentence in `orchestration.md`, and a session that
spawns the sealer without it meets a `not sound — no broad run at HEAD` and
runs the gate then, one spawn late. A `closed` word read fail-closed refuses
every `U+2705` row a user's in-flight overview still carries at the moment they
move their hygiene pin, and the changelog is where they learn the edit.

## Alternatives considered

CI cost is the billable minutes a private repository would pay per pull
request (Linux 1×, Windows 2×, macOS 10×), against the 208 measured at
d4552372. The suite's priced seconds are the share this item moves.

| Approach | Failure scenario (six months on) | CI cost if private | Verdict |
|---|---|---|---|
| A. Each definition and the contract written anew in one shape; the contract alone preloaded and each skill opened at its step; the marks without a reader gone; the census and the stamps gone; the grammar one table the check loads; the gate the orchestrator's run before the sealer; a baseline and a per-phase proof, the warden first | above | ≈ −1 minute a run: 42 s of priced cases leave (the census and stamp modules), a handful of document-reading cases arrive; the 208 is the macOS multiplier's, which this item does not touch | **chosen** |
| B. Trim each definition in place: delete the narrative, keep the headings and the preloads | the next six changes append where the last six did, and the files are back at today's size with today's structure; three frames of #923 trimmed files whose structure was the problem and each trim was undone by the next round | none | rejected (the owner: a structure that stays compact, not a one-time trim) |
| C. Replace the structure outright: no per-agent definition body, one procedure file per flow (frame, build, review, guarantee) that the frontmatter points at, and no `skills:` list anywhere | a procedure file two agents read (the smith's fix pass and the warden's verifying round both read the record's rules) carries a per-role exception, which `docs/the-agent-set.md` refuses of a shared file; and a pointer the harness does not preload is a Read every spawn pays before its first act, so the contract would arrive by habit again, which is #107's failure | none | rejected, and its shape is borrowed: the definitions become short and point at the skills they open, while the contract still arrives by the `skills:` mechanism |
| D. Keep the skills preloaded and only write them shorter | every spawn pays every skill whether or not its act comes: a fix pass pays `implement` and `writing-style` for two lines of a record; and no run ever shows which skill an agent needed, so the lists never shrink | none | rejected; a case decides it per agent, and a skill a failing case names goes back on the list |
| E. Open the contract on demand too, preload nothing | the exit-code rule arrived at round 2 of one item and the venv line at round 3 because nothing delivered them before the first tool call; a rule read by habit is the failure the contract ends | none | rejected |
| F. Keep the contract's 17 numbers and retire sections to one-liners, as its own rule says | five one-line slots paid on every spawn forever, and a file that carries its own history, which is the item's root problem | none | rejected; the file written anew starts at §1, the rule holds from this edition, and every citation is rewritten in the same commit |
| G. Rewrite the contract and the warden in one phase | 18 fewer runs, and a case that fails cannot be laid at the contract or the definition | none | rejected; attribution over about 18 runs |
| H. Keep the `Reads:` lines as documentation once the census leaves | a line no check reads goes stale the way the registry's own limit 5 says, and a stale claim about which way a reader fails misleads #956's auditor; 31 KB read by whoever opens the files | none | rejected |
| I. Keep the rider stamps, drop the census alone | the same hash kept beside the tree, asking `--reverify` on a comment edit, as it did on #923's round 1 fix pass | none | rejected |
| J. The grammar as a constant in the script, with a test that the document's table equals it | two statements held in step by a pin, where the tenet asks one source; the document's reader then reads the script's constant | none | rejected; the document is the source and the script loads it |
| K. A generated-variant or mutation test over the grammar | #929 measured a generator chasing the next gap never converging | seconds a run | rejected (the owner) |
| L. The sealer keeps the broad run and retries once on a failing check | a 240K-token guarantor run spent again on a second that went 1.8 s over a ceiling; the mechanical act stays inside the judgment agent | none | rejected |
| M. The sealer drops to Sonnet now | the audit is judgment at the level of the agents it audits, and nothing has measured Sonnet on the three cases | none | rejected (the owner: measured first) |
| N. No baseline; judge the new side on its shape graders alone | a rewrite that lost a defect the old side found passes, because nothing compares recall | none | rejected |
| O. A scribe case, with a parity fixture generator | one more generator for an agent no run in this repository has spawned; a mechanism nobody asked for | none | rejected; the scribe is measured on bytes and its outcome is `unverified` (Q3) |
| P. `U+2705` stays as the one emoji a check reads | the one exception to the owner's rule, in the one place the rule came from: a mark a gate reads | none | rejected; the word `closed`, Q2 for the owner |
| Q. `## Not verified` redesigned into labelled lines, as the round record was | a second 1,800-line checker rewritten in an item already this size, for a table one reader reads with its own spec; the word in the cell is the change the rule asks for | none | rejected here; a labelled-line redesign is #940's or #956's to weigh |
| R. The definitions point at `docs/` for their rules and state none | an agent opens a 350-line document for one sentence at every step; the rule an agent needs at its step is written where it reads it | none | rejected; a definition states its own rules, `docs/` states the repository's |
| S. `writing-style` stays preloaded for the warden, since the record needs its English rules | 21,000 B on every warden spawn for one section of about 1,300 B read at one step | none | rejected; opened at the record step, and the `shape-words-only` grader and the round's reading say whether the record suffered |
| T. Rename `Enforced by:` to one lowercase word in the files this item writes | two spellings in one tree until #941, with `rules.py` reading one of them | none | rejected; #941 renames it with its reader |
| U. The grammar document read by the check from `docs/` breaks in a user's repository where no `docs/` is checked out | the hygiene template clones this repository whole at the pinned tag and runs the script from there (`templates/hygiene.yml:58-59`); a clone with no `docs/` is exit 2 naming the file, never a pass | none | not a failure of A; stated so the loader's refusal is read as intended |

## The split

| Work item | Holds | Why it stands alone | Order |
|---|---|---|---|
| 1 — the mechanics | phases 0, 1, 2 and 8: the red tree, the census and the stamps, the grammar table, the closing word | checks, scripts and tests, verified by CI alone and by no paid run; it removes the census refusals every later unit edit would meet, and it changes the word the smith writes into `overview.md` before any smith of item 2 writes one | first |
| 2 — the agents | phases 3 to 7 and 9: the baseline, the warden, the contract, the smith and the framer, the sealer and the scribe, the close | one review chain over the five definitions, the contract, the four skills and their pins, each phase carrying its eval record | after item 1 merges into `release/v0.22.1` |

The measurement that asks for it is #923's: a 10-round chain over one diff
that did many things, and the lesson in its `plan.md` Alternative J. This
item's `routing.md` names one branch, so the split is the owner's to make by
opening a second work item (`questions.md` Q1). Where it is not made, the
phases below run in this order on this branch and the boundary costs
nothing: phase 8 can close before phase 3 opens, since nothing in 3–7
depends on it.

## Phases

Vertical slices — each phase ends with something runnable and verified. Each
phase that changes a file under `agents/` or a skill a definition opens
runs that agent's cases and commits the record; a phase that changes none
runs no case. Every phase enumerates the class of what it removes by the
`git grep` its record names, and every new case is seen red first (contract
§15), with the exit named in the phase record.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 0 | **The tree is green and the harness reads the record.** The Windows-red case of run 38852872472 fixed where the defect is: `test_a_side_runs_the_tree_it_measures_and_no_installed_plugin`'s path comparison on Windows, or `noninferiority.py#side_path` where the harness is what is wrong (the sealer-guarantees case of the same run is #963's, already fixed outside this item). `evals/scripts/replay_targets.py` reads the asked paragraph the new record carries, or none, and the four replay cases are regenerated through `--case`. `evals/README.md:34-35` rewritten to the generators' usage as it is | `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py -q` exit 0; CI green on all three legs at the phase's commit; the regenerated cases read by hand against `templates/sdd-round.md` | |
| 1 | **The census and the stamps leave.** `tests/undeclared_readers.txt`, `tests/reader_registry.py`, `tests/test_a_reader_declares_its_input_class.py` and `.github/scripts/rider_check.py` removed; the 364 `Reads:` lines and the 55 stamp lines removed by one-shot scripts under the scratch directory, run once and deleted (contract §7), each asserting its count before and after; the stamp cases of `tests/test_a_rider_reaches_its_file.py` removed and its `seal/follow-up.md` cases kept; `docs/the-reader-registry.md` rewritten in place to §*A frame names what its work removes* alone; `CONTRIBUTING.md:247-251` removed; `seal/follow-up.md:27-47` rewritten to *a rider is a comment, and a rider outliving its fix is the reader's finding*; `.github/workflows/test.yml:110-112`'s comment rewritten to the reason that stays, or removed with `fetch-depth` where none does; `spec.md` §*Removes*' rows for the census read against the diff | `git grep -n "Reads: " -- '*.py'` finds nothing; `git grep -n -E "Verified [0-9-]+ against"` finds nothing outside `seal/specs/` and `changelog/`; `git ls-files` names none of the four removed paths; `bin/rules --check` exit 0 with every `Enforced by:` that named the census module gone from its paragraph; `bin/test tests/test_a_rider_reaches_its_file.py tests/test_the_rules_have_one_owner.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py -q` exit 0; `ruff check` and `ruff format --check` on the touched `.py` files | |
| 2 | **The grammar is one table, and the check reads it whole.** `docs/the-review-record.md` §*The round record* gains the table of `spec.md` §*Data & interfaces* and its five prose paragraphs are rewritten to point at the rows they stated; `chain_check.py#grammar(path)` loads it at import from `docs/the-review-record.md` beside the script, exit 2 naming the file where the document or a row cannot be read, and `records` matches every labelled line and heading against its row whole, the constants at `:93-191` gone; `templates/sdd-round.md`'s comment and `templates/config.md` §*What no row governs* point at the table and restate nothing; `ROUND_RECORD_FIELDS` of the language test derived from the table. Test-first in `tests/test_chain_check.py::TestGrammar` (T8): the table loads and its rows are the eight labels and the heading; each row's shape matches the template's example line whole and refuses the line with a trailing word; a document with a broken row is exit 2 naming it; T32, T33, T35 and T36 re-pointed at the table unchanged in what they refuse | T8 red on d4552372's reader (no loader), green after; `mutation-check` red for: `fullmatch` loosened to `match` (T8's trailing-word case), the loader's exit 2 dropped (T8), a row's shape read by `search` (T33); `bin/test tests/test_chain_check.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_the_record_is_written_in_words.py tests/test_docs_line_wrap.py tests/test_the_rules_have_one_owner.py -q` exit 0; `chain_check.py --baseline origin/release/v0.22.1 --root <worktree>` exit 0 on this branch; `ruff check` and `ruff format --check` | |
| 3 | **The baseline.** `noninferiority.py run --agent <a> --rev d4552372 --suite-rev HEAD --out seal/specs/<id>/evals/baseline-<a>.json` for warden, smith, framer and sealer, `--runs 2 -j 4`; the raw output outside the tree; the four files committed; the cost fields of the per-run JSON and the trace's `result` event read and named in the phase record (Q5), with the spend per agent (Q4) and whether the trace names the subagent's model (Q6) | four files, none cut short, each with spend, tokens and preload bytes (`test_a_cut_short_side_is_no_result_and_never_a_pass`, `test_a_run_records_what_it_cost`); the phase record's table of runs, spend and seconds per agent | |
| 4 | **The proof on one file: the warden.** `agents/warden.md` written anew to `spec.md` §*The shape of a definition*, `skills: [agent-contract]`, step 1 opening `skills/code-review/SKILL.md`, the record step opening `skills/writing-style/SKILL.md`'s section for the record's language; the six rules of the warden kept as `## Rules` paragraphs (the branch worktree's record path, the new-test-against-its-group reading, the verifying round, the carried-fact table, the clone, the probe rules); the batching number gone; `skills/code-review/SKILL.md` written anew to the shape: two stages, the axes, probes against regression tests, the record pointing at the template and the table, no proof block, no orchestrator section pointer beyond one line; the 23 modules naming the warden and the 6 naming `code-review` re-pointed where the rule stays and removed with one line in the phase record where the sentence was narration (Q7); `tests/test_every_agent_reads_the_contract.py` rewritten to S1 and S2 (T1, T2) for every definition, red on the four not yet rewritten and skipped by name for them until phase 7 closes, which the phase record says | the warden set run against `baseline-warden.json`, `evals/warden-phase-4.md` reading `pass`; T1 and T2 red then green on the warden; `bin/rules --check` exit 0; `bin/test` over the re-pointed modules exit 0; `payload-meter --agent warden` in the phase record beside the baseline's | |
| 5 | **The contract.** `skills/agent-contract/SKILL.md` written anew: one opening paragraph, §1 to §N in the new order, each a rule paragraph with `Enforced by:`, the four new rules of `spec.md` §*The shape of a definition*, §2 stating that no agent runs the broad gate and that the orchestrator runs it before the sealer; `docs/the-agent-set.md`'s section-number sentence rewritten to *from this edition*; every `§N` citation outside `seal/specs/` and `changelog/` rewritten to the new number in the same commit, the 128 prose sites and the 326 test sites enumerated by `git grep -n -E "§[0-9]+"`; T3, T4 and T5 (S4, S5, S6) in `tests/test_the_agent_contract_holds_the_universal_rules.py` and `tests/test_a_moved_rule_leaves_its_definition.py`, red first; the 11 modules naming the contract re-pointed | all four sets run (every preload changed), `evals/<agent>-phase-5.md` reading `pass` for each; T3–T5 red then green; `bin/rules --check` exit 0; `git grep -n -E "§[0-9]+"` over `agents/ skills/ docs/ templates/ hooks/ tests/ CONTRIBUTING.md` naming only sections the contract has, which T3 holds | |
| 6 | **The smith, the framer and their skills.** `agents/smith.md` and `agents/framer.md` written anew to the shape: the smith's steps (requirements and whether the frame holds; build test-first, the phase record; the fix pass's two lines; verify and mutate; hand back with the three labels), its rules (a new test starts from its group; commit before you mutate; the three-fix stop; the waiver as one sentence), the RIDER block and the batching number gone; the framer's steps (gather, judge, plan, report), its rules (asks nobody; writes three files; do not avoid the change; the residue), the batching number gone. `skills/implement/SKILL.md` to the shape: the layout, the precedence, the ladder, the file set table, test-first, the closing memo, the fix pass, no proof block, the `U+2705` and `U+2B1C` sentences to the words; `skills/writing-style/SKILL.md` to the shape, its English rules a section an English writer opens, its one emoji gone; `templates/sdd-overview.md:9` and `templates/sdd-questions.md`'s `U+2B1C` to the words `open` and `answered <date> by <who>`, `tests/test_a_question_says_who_can_answer_it.py:106` re-pointed; `skills/verify/SKILL.md` §*Every agent seals what it verified* and §*Seal block* rewritten to the fact that the hand-back's three labels carry the claims and the sealer's `guarantee.md` is the one seal, and no more of that file; T6 (S7) over every file under `agents/`, every `skills/*/SKILL.md` and `templates/`; the 19 and 12 modules naming the smith and the framer, the 12 naming `implement` and the 3 naming `writing-style` re-pointed or removed with a line (Q7); the three proof-block pins removed | the smith and the framer sets run, `evals/smith-phase-6.md` and `evals/framer-phase-6.md` reading `pass`; T6 red on the tree before the rewrite, green after; `bin/rules --check` exit 0; `bin/test` over the re-pointed modules exit 0; `payload-meter` for both in the phase record | |
| 7 | **The sealer with the gate before it, its model measured, and the scribe.** `agents/sealer.md` written anew to the shape: step 1 reads `broad-gate.md` and refuses one absent or not at HEAD, steps 2–5 as 0.22.0 left them, a re-run audits the commits since the last `guarantee.md`'s commit and keeps its line (S14); `skills/code-review/orchestration.md:178-201` rewritten: the orchestrator runs `broad-gate --base <base> --record <item>` with nothing else running, then spawns; `docs/the-broad-gate.md` §*One act, one owner* and `docs/the-review-record.md` §*The guarantee* rewritten in place; `templates/sdd-guarantee.md`'s `Target SHA` row gains the `; earlier run:` form; `tests/test_broad_gate_rule.py` rewritten to the new fact (T9), `tests/test_the_sealer_guarantees.py::TestDefinition` and `TestTemplate` to the step and the row (T10, T11); the three sealer cases regenerated with scaffolds that write `broad-gate.md` at HEAD; the sealer set run on Opus against `baseline-sealer.json`, then on a copy of the tree with `model: sonnet`, `evals/sealer-model.md` written by `compare` over the two sides (T12), and `model:` set by `spec.md` §*The sealer's model is decided by measurement*. `agents/scribe.md` to the shape and `skills/legacy-parity/SKILL.md` to the shape with the four verdict words; the scribe measured by `payload-meter` only, its outcome `unverified` with the owner named in the phase record (Q3); the 11 and 5 modules naming the sealer and the scribe re-pointed | `evals/sealer-phase-7.md` reading `pass` on Opus; `evals/sealer-model.md` with both sides and the decision quoted in the phase record; T9–T12 red then green; `bin/test tests/test_broad_gate_rule.py tests/test_the_sealer_guarantees.py tests/test_evals_layout.py -q` exit 0; `bin/rules --check` exit 0; T1 and T2 green for all five definitions with the skips of phase 4 gone | |
| 8 | **The closing word.** `unverified_check.py#CLOSED` reads `closed` as the first word of the row's first cell, a bare `closed` refused as the bare mark was, `U+2705` refused naming the row and the edit; its messages at `:1675` and `:1792` in words; the test module's success and failure case per changed function (T7); `templates/sdd-overview.md:38`, `templates/config.md:139`, `docs/the-record-layout.md`'s and `skills/implement/SKILL.md` §4's sentences to the word; the `## Not verified` rows of the four 0.22.0 items' overviews rewritten once by a one-shot script, its diff read whole by the smith (Q2's default) | T7 red on the reader as it stands, green after; `mutation-check` red for the bare word accepted and for `U+2705` accepted; `bin/test tests/test_the_unverified_record_is_readable.py -q` (or the module that owns the reader, named in the record) exit 0; `unverified-check seal/specs/ --baseline origin/release/v0.22.1` exit 0 on this branch with every closed row counted closed; the hygiene step green at the pull request | |
| 9 | **The close.** Any agent's set run again where its preload changed after its last passing record; `overview.md` (one line of purpose, divergences, `## Not verified` in the new word, fed-back clauses); `changelog.md`: the paragraph a plugin user reads (what a spawn preloads now, where each skill is opened, the `closed` word and the edit an in-flight overview owes, the grammar table, the gate before the sealer, the census and the stamps gone, the sealer's model) and the per-agent table of preload bytes, tokens read, spend and outcome at d4552372 and at the close, each figure with its commit, read from the eval records and `payload-meter`; `questions.md` rows the work and the measurements answered ticked in words | a `pass` record for every agent whose preload changed, or its last record naming its finished preload; `bin/rules --check` exit 0; `chain_check.py --baseline origin/release/v0.22.1 --root <worktree>` exit 0; the fragment's figures traced to their records in the phase record | |

This table is also where the work records how far it got. **Status is empty,
or the commit that closed the phase.** Re-read the column after any rebase.

### Test rows — what each case protects and the mutation it kills

| Case | Protects | Mutation it kills |
|---|---|---|
| T1 `tests/test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_contract_alone` (NAME NOT IN TREE until phase 4; skipped by name for the four definitions until phase 7) | S1 — a sixth preload or a lost section, which no eval sees while the output is right | a second `skills:` entry accepted; a missing `## Order of work` passed; the opening sentence matched anywhere in the file |
| T2 `…::test_every_file_a_step_names_exists` (phase 4) | S2 — a renamed skill leaving a dangling instruction | a backticked `skills/x/SKILL.md` not resolved; a path outside `skills/` ignored |
| T3 `tests/test_the_agent_contract_holds_the_universal_rules.py::test_every_cited_section_exists` (phase 5) | S4 — a citation left at an old number | `§N` read only in `agents/`; a number above the last heading passed |
| T4 `…::test_the_four_rules_stand_with_their_enforcers` (phase 5) | S5 — a new rule dropped in a later trim | any of the four paragraphs deleted; an `Enforced by:` line missing under one |
| T5 `tests/test_a_moved_rule_leaves_its_definition.py::test_no_definition_states_a_tools_per_turn_figure` (phase 5) | S6 — the second copy of a bar | `tools per turn` with a number in any definition passed |
| T6 `tests/test_the_record_is_written_in_words.py::test_no_file_an_agent_reads_carries_an_emoji_or_a_proof_block` (phase 6; replaces `test_the_template_the_format_and_the_two_definitions_carry_no_emoji`) | S7 — a mark coming back where an agent reads instruction | one of the three globs dropped; the `applied` block pattern dropped; the variation selector left out of the range |
| T7 `tests/test_the_unverified_record_is_readable.py::TestClosedRow::test_the_word_closes_and_the_mark_and_the_bare_word_are_refused` (phase 8; the module name is the one that owns `unverified_check.py`, named in the phase record) | S8 — the emoji mark read by a gate | `U+2705` still accepted; `closed` with nothing after it accepted; `Closed` accepted |
| T8 `tests/test_chain_check.py::TestGrammar::test_the_table_loads_and_every_line_matches_its_row_whole` and `::test_a_document_the_check_cannot_read_is_exit_2_naming_it` (phase 2) | S11 — a fourth statement drifting, and a partial match | `fullmatch` loosened to `match`; the loader's exit 2 dropped; a row's label read case-insensitively |
| T32, T33, T35, T36 of #923 (re-pointed in phase 2) | S12 — the known leaks reopening | unchanged |
| T9 `tests/test_broad_gate_rule.py::test_no_definition_assigns_the_broad_gate_and_the_orchestrator_runs_it_before_the_spawn` (phase 7; replaces `test_only_one_definition_assigns_the_broad_gate`, `test_the_sealer_counts_the_silent_definitions_from_the_glob`, `test_the_orchestrator_runs_the_preflight_before_it_spawns_the_sealer`) | S13 — a definition taking the run back | a definition handing itself the suite passed; the orchestration section's run sentence after the spawn sentence passed |
| T10 `tests/test_the_sealer_guarantees.py::TestDefinition::test_step_1_reads_the_record_and_runs_nothing` (phase 7) | S13 — the sealer running the gate | `broad-gate --base` in step 1 passed; the `not HEAD` refusal dropped |
| T11 `…::TestTemplate::test_the_target_row_keeps_an_earlier_run` (phase 7) | S14 — a full re-audit | the `; earlier run:` form absent from the template passed |
| T12 `tests/test_a_rewritten_definition_proved_non_inferior.py::test_a_two_sided_compare_of_one_suite_on_two_trees_reads_both_costs` (phase 7) | S15 — a model drop decided by cost alone | the truth graders of one side dropped from the record; a cheaper side with a lost truth read as `pass` |
| T13 `tests/test_a_rider_reaches_its_file.py` as it stands after phase 1, its stamp cases gone | S10 — a coordinate-tied row back in `seal/follow-up.md` | unchanged |

Each definition rewrite is verified by its eval record, the pins it
re-points, `rules --check` and `payload-meter`, not by a case on its
sentences; a case on a sentence is what held the bloat in place.

## Operational impact

- **What a plugin user sees.** Each agent's definition is a page; a warden,
  smith or framer spawn opens a skill with a `Read` at the step that needs
  it, which appears in the transcript as one call. The hand-back carries its
  claims under the three labels and no proof block. A `## Not verified` row
  closes with the word `closed`, and an overview in flight with `U+2705` rows
  fails the hygiene step naming the row and the edit when the user moves
  their `hygiene.yml` pin to this release (`templates/hygiene.yml:58`); the
  changelog says so. A `questions.md` status reads `open` or `answered`.
- **The check.** `chain_check.py` loads its grammar from
  `docs/the-review-record.md` beside itself and exits 2 naming the file
  where it cannot; the hygiene template's clone carries the document. A
  record's lines are matched whole, so a value with a trailing word is
  refused where it passed before. The refusal names the line and the row.
- **The run.** The orchestrator runs `broad-gate --base <base> --record
  <item>` before spawning the sealer, with nothing else running; the sealer
  reads the file and runs nothing broad; a re-run audits the commits since
  the last guarantee. The stamp is drawn as before, from the file, at the end
  of the spawning session's turn.
- **The census and the stamps.** No pull request is refused for a missing
  `Reads:` line or a drifted rider hash; `grep -rn "RIDER:"` is still the
  list of riders, unstamped.
- **The proof.** 126 runs on the orchestrator's account, by the case counts
  at d4552372; the spend is measured at phase 3 and named in that phase's
  record. CI pays nothing for the evaluation and about a minute less a run
  for the suite.
- **Compatibility.** The contract's section numbers change; a spawn prompt
  or a record citing an old `§N` reads the new contract wrong until
  rewritten, and the tree's own citations are rewritten in phase 5. A user
  repository's `CLAUDE.md` block (`templates/claude-md-block.md`) is #940's
  and is read for `§N` in phase 5's grep.
- No new dependency; stdlib Python at the floor.
