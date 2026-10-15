# Implementation Plan: every agent, skill and doc states the current rule only

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-14 by the repository owner, when `smith` was spawned.
Approved 2026-10-15 by the repository owner, when `smith` was spawned for the reframed plan.
Approved 2026-10-15 by the repository owner, for the replanned phases 1–7, when `smith` was spawned for phase 1's second act.
Approved 2026-10-15 by the repository owner, for the new-slate frame split into parts A and B, when `smith` was spawned for phase 3.

Reframed 2026-10-15 as a new slate, from phase 3 on, against #923's body as
the owner rewrote it that day. Phases 1 and 2 are closed and keep their rows
and commits; every row from 3 on replaces the earlier plan's.

## Summary

The review chain is designed from the jobs. A round record is one file the
warden writes — the commit it reviewed, its findings in the five-column table
it already writes, its probes and its paste-ready fixes — and the smith's fix
pass closes each open row with two cells. Nothing is generated, copied or
derived: `round_record.py`, eleven fields, four sections, the ⬜ severity and
the reviewer's separate report leave, and the check at the pull request reads
five facts — the declaration, the frame, the records, the broad gate's file,
the sealer's verdict. The sealer becomes the final independent guarantor on
Opus: it runs the gate, re-runs a sample of the smith's claims, and reads the
framer's, the smith's, the warden's, the changelog's and the pull request's
stories against the issue and the tree, writing `guarantee.md`. Then the five
definitions and the contract are written anew from their jobs, preloading the
contract alone and opening each skill at the step that needs it, each phase
proved on the agents' behaviour cases against a baseline taken once. The
agents are written once, against the new record, which is why the record
comes first and the agents second, as a second work item.

## Technical context

Read at 680142f2; `executed` where `spec.md` §*The chain as it stands,
measured* says so.

- `skills/code-review/scripts/chain_check.py` (6,153 lines): `main` runs the
  declaration, frame, records, broad-gate, pact and fragment arms; the records
  arm reads thirteen fields and eleven of them judge something this plan
  removes. `round_record.py` (5,596): `new` copies the report's tables and
  derives `Fix of a fix`; `close` applies the fix table and measures the fix
  surface by AST over the range; `notes` closes ⬜ rows; `seal` writes the
  `Broad gate` cell. `broad_gate.py` (3,640): the run, the panel, the stamp
  values, and the record arms (`seal_home`, `round_count`, `rounds_rows`,
  `sealed_record`, `kept_broad_gate`) that call `round_record.seal`.
- The record is read by: `chain_check.py`, `round_record.py`, `broad_gate.py`,
  `hooks/review-history-guard.py` (reminders), `skills/settle/scripts/settle.py`
  (`--retire-process`, and the `tests-todo.md` open-row rule),
  `hooks/routing.py`, `hooks/config.py`, `hooks/root-migrate.py` (path
  constants). CI: `hygiene.yml`'s step *a declared review chain has the round
  record it claimed* runs `chain_check.py --baseline origin/<base>`, after a
  fetch of `refs/pull/*/head`.
- Tests: 70 modules name one of the three scripts, 3,758 cases, 4,553 of
  6,827 suite seconds, 68,783 lines; `docs/review-handoff-protocol.md` is
  named by 26 modules, `templates/sdd-round.md` by 24, the two specs by 20 and
  17. `tests/test_every_orchestrator_act_names_its_delivery.py` holds the
  delivery table of `skills/implement/orchestration.md` against every
  `Orchestrator:` heading of both orchestration files, so a removed section
  removes its row.
- The warden's eval cases (`evals/behaviour/warden/`) grade the report at
  `rounds/round-N-report.md`: `shape-report-exists`, `shape-verdicts-table`,
  `shape-needs-a-fix`, `shape-loses-a-record`, `reach-warden`, `truth-N`. The
  sealer's three cases grade the `Broad gate` cell write. `noninferiority.py
  #verdict`'s rule 3 reads shape and reach on both sides.
- Today's five definitions: warden 32,110 B · smith 25,400 · framer 19,700 ·
  sealer 15,188 · scribe 3,763; the contract 20,409; `code-review` 26,139 ·
  `implement` 34,283 · `writing-style` 21,000 · `legacy-parity` 5,325. Preload
  (agent share): warden 99,658 · smith 101,092 · framer 95,392 · sealer
  35,597 · scribe 29,497 (`release_report.py`, `executed`). Test modules
  naming an `agents/` file: 52, 55,041 lines; `§N` citations of the contract:
  agents 43, skills 77, docs 18, templates 5, hooks 10, `CONTRIBUTING.md` 2,
  tests 423 in 89 modules.
- The base: `origin/release/v0.22.0` at ce448bbe (#930, #944, #931, #929
  merged); this branch is rebased on it (0 behind, 46 ahead). Open pull
  requests touching the set: #915 (`agents/warden.md`, draft, into `main`).

**What breaks in 6 months with the chosen approach.** A warden that writes a
record with a sixth verdict word is refused at the pull request by name, and
the fix is the record, not the check. A run that loops is stopped by nothing
mechanical: the cap and the `fix of a fix` stop are the orchestrator's and the
warden's sentences, and a session that ignores both ends at the sealer, which
reads the records and names the count; if that happens twice, the count
becomes an arm, with the two runs as its history. The sealer samples, so a
false claim it did not draw ships; the sample is written in `guarantee.md`, so
the miss is findable afterwards. A definition that opens its skill late or not
at all does worse on its cases, and the case names the skill that goes back
to the list. The behaviour cases go stale as the record shape moves, and the
first baseline after a shape change is where that shows; part B's baseline is
taken after part A's shape lands for that reason.

## Alternatives considered

CI cost is the added minutes a private repository would bill per pull request
(Windows 2×, macOS 10× a Linux minute); the latest green run billed ≈ 182
minutes that way (`spec.md`, `executed`). A test share is estimated from the
suite seconds the tests concerned hold today.

| Approach | Failure scenario (six months on) | CI cost if private | Verdict |
|---|---|---|---|
| A. The record is the warden's one file; the smith fills two cells; the check reads five facts; the sealer guarantees on Opus; the contract alone is preloaded; the record lands first and the agents second | above | the chain-machinery tests fall from 4,553 s to under 1,500 s (S12), ≈ −45 % of suite seconds, ≈ **−80 billable minutes a run** (estimate from the share); the sealer runs on the orchestrator's account, not CI | **chosen** |
| B. Keep the generator and trim it to the fields that fired in 0.22.0 | each kept field keeps its refusal at the keyboard and its arm; the copy of the report stays and a later round still inherits two files; the earlier frames of this item chose this and the owner refused it | today's | rejected (owner, 2026-10-15) |
| C. No record in the tree; the pull request's review comments are the record | a record keyed by the pull request's number does not exist while the rounds run — the directory this plugin once named that way was never created (`docs/review-handoff-protocol.md`, `read`); a squash leaves the comments pointing at commits that are gone | none | rejected |
| D. The orchestrator writes `round-N.md` from the warden's report, by hand | a retyped verdict row carries retyped coordinates, and inheritance carries the paraphrase into the next round (#228, `read`); the generator existed to end that | none | rejected; the warden writes the record |
| E. Keep the mechanical `Fix of a fix` count from the fix range | it needs `Fix range`, the AST unit walk and the depth; 365 s of tests; its three 0.22.0 stops each named one unit the warden had already written in the finding, so the judgment carried the same information | ≈ 6 billable minutes a run (share of the suite) | rejected; the warden marks, the orchestrator stops |
| F. Keep the cap, the floor and the one reopening as checked arms | no 0.22.0 run reached the cap; the arms are where 8 of 14 failed October hygiene runs stopped, and what each refused is unverified; three rules and 227 spec lines for a bound a sentence states | ≈ 2.7 s a run as today | rejected; one orchestrator rule with one number (Q1) |
| G. The sealer as today, with the warden auditing the pull request body in its last round | the auditor is a party to the story; on 2026-10-15 the untrue statements were the parties' own, and only chance caught them (#923 item 2) | none | rejected |
| H. The guarantor on Sonnet | the audit is judgment at the level of the agents it audits; a cheaper reader of five stories misses the disagreement it is for | none | rejected (owner, 2026-10-15) |
| I. The sealer posts its verdict as a pull request comment | contract §6 withholds posting from every agent; the check at the pull request cannot read a comment without `gh` and a token | none | rejected; `guarantee.md` in the tree |
| J. One pull request for the record and the agents | ≈ 85 K deleted lines, three documents replaced and ten preloads rewritten in one diff; #929's run of 7 rounds was a tenth of that; the warden's baseline would be taken on a tree whose record shape is moving under its own cases | none | rejected; part A then part B |
| K. The agents first, the record second | the definitions would be written against today's record and then rewritten — the owner's reason for one design (#923 item 3) | none | rejected |
| L. The warden keeps `code-review` preloaded, the smith `implement` | 26 KB and 34 KB paid on every spawn before any case shows the opened form falls short; #923 item 4 puts the proof the other way — cut, then restore the skill a failing case names | none | rejected; a case decides it per agent |
| M. The check counts records against the cap and reads the `fix of a fix` mark | both are facts a script can read, but the stop's value was the reframe, which no script judges, and no 0.22.0 run needed the cap; an arm with no catch history | seconds | rejected; written down so the first looping run can overturn it |
| N. A sixth agent for the fix pass | a sixth preload and a sixth definition for a job the smith does; whether a fix pass resumes or respawns is #945's | none | rejected |
| O. `Ran by` stays so the record names the model | read by nothing that changed an outcome in 19 records; `routing.md`'s free text already names the models | none | rejected |
| P. `tests-todo.md` stays | written by 0 of 4 items; a prescribed test is a 🟡 row that closes `fixed <commit>` | none | rejected |
| Q. ⬜ stays as a severity | 3 → 15 open notes carried through #929's seven records, closed by a command at the run's end; a wrong sentence an agent acts on is 🟡 already | none | rejected |

## The split

| Part | Holds | Where it takes over |
|---|---|---|
| A — this work item, phases 3–5 | the record, the five-arm check, the broad gate's one file, the sealer as guarantor with its template, arm and cases, `docs/the-review-record.md`, the orchestration sections, the tests sorted into #942's layout, the changelog fragment | — |
| B — a second work item under #923, phases 6–9 | the contract and the five definitions written anew, the `skills:` lists cut to the contract, the four preloaded skills rewritten to the shape, the pin modules, the baseline and the per-phase proof | a branch cut from the release branch after part A merges; its `spec.md` cites this file's §*Every agent definition* and adds nothing |
| #940 | what an agent opens on demand, the orchestration files beyond the record sections, `templates/` beyond the two here, `CONTRIBUTING.md`, `CLAUDE.md` | after part A merges, for the orchestration files |
| #941 | `docs/` beyond the files this item makes false | with part A |
| #945 | the agent-lifetime rule, the folding rule, the process archive | after part A merges |

The measurement that asks for the split is the size of part A's diff (≈ 85 K
lines leave) against the review chain's own capacity (#929: 7 rounds on a
diff a tenth that size), and the proof's need for a settled record shape
under the warden's cases before a baseline is taken. The split keeps the
owner's condition: the agents are written once, against the record part A
built, and this frame describes both parts so nothing is designed twice.

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The proof made light.** (i) Built at a4952d90..6cfea707: every `rule-*.md` grader removed and `rule_cases.py` writing outcome graders only; `census_problems`, `owed_records`, T10 and T12 removed; `noninferiority.py run` recording `total_cost_usd`, `duration_ms` and `usage` per run, `compare` and `verdict` carrying pass rule 4, a run with no cost pooling to unknown; `replay-1791852615-r2` and `seeded-770d721f` replaced through the generators' `--case`; `tests/test_evals_layout.py#KINDS` without `rule`; `evals/README.md` rewritten in place. (ii) The five eval cases that predate 0.22.0 removed, each on the grounds in `overview.md`, and the layout test applying the measured schema to every case under `evals/` (#946) | (i) the record test's rule-4 cases seen red first, T10 and T12 gone, the layout test green; (ii) the layout test red on a top-level `max_turns` and on an inline scaffold before the fix, green after | c7d8bcc8 |
| 2 | **The budget concept leaves; `rules --check` and the release table stay.** `rules.py --check` resolving every shown `Enforced by:` target of every rule file; `release_report.py` and the `release-report` job printing one table on a pull request into `main`; `seal/budgets.md`, `budget_check.py`, `test_a_budget_ratchets.py`, the hygiene budget step, the `PARTITION` row and the `FEATURE_UNANSWERED` entry removed; every budget sentence rewritten in place; #930's changelog fragment rewritten to what ships | T5–T8 seen red first; the tree-level resolution case green and red on a renamed target; the `grep` over the tree finding nothing outside `seal/specs/`; the gate's step counts at 4 and 7; the release table's cases green | 14b937f5 |
| 3 | **The record is the warden's file, and the check reads five facts.** `templates/sdd-round.md` to `spec.md` §*What a round records*. `chain_check.py` rebuilt to the five arms of §*Data & interfaces*, reading `Target SHA` and the `Verdicts` table of every record written to date and nothing else of them. `broad_gate.py` writing `broad-gate.md` on both routing answers, its record arms and the `round_record` import gone. `round_record.py`, `bin/round-record{,.cmd}`, `hooks/review-history-guard.py` and its dispatch, the `tests-todo.md` readers in `settle.py` and the documents, gone. `docs/the-review-record.md` written — the record, the verifying round, the cap (Q1's default), the `fix of a fix` stop, the filing ladder, the handoff rule (coordinates, never prose), each with `Enforced by:` or a link; `docs/round-record-spec.md`, `docs/review-chain-spec.md`, `docs/review-handoff-protocol.md` gone and no file naming them. `docs/the-record-layout.md` §*seal/specs/<work-item-id>/*, `docs/the-broad-gate.md`'s cell paragraphs, `docs/the-agent-set.md` §*What each party writes* rewritten in place. `skills/code-review/orchestration.md`'s record sections rewritten or removed as §*Data & interfaces* lists, and the delivery table's rows with them; `skills/code-review/SKILL.md` §*Findings format*'s ⬜ line and §*Cross-session records* rewritten in place to the new record (the skill is written whole in part B). `agents/warden.md` §*Report* and `agents/smith.md` §*Phases* step 5 rewritten in place to the record path and the two cells (the definitions are written whole in part B). The warden's shape graders re-pointed at `rounds/round-N.md`, the two field graders gone, `noninferiority.py#verdict` rule 3 reading shape on the new side. The 70 test modules sorted: `tests/test_chain_check.py` and `tests/test_broad_gate.py` in #942's layout for what still holds; every deleted module's guard one line in `phases/phase-3.md` | the new modules' cases seen red first (S3, S4, S5, S11, T11–T15); S10's `grep`; S12's durations sum under 1,500 s; S13's `rules --check` exit 0; `bin/test tests/test_chain_check.py tests/test_broad_gate.py tests/test_every_orchestrator_act_names_its_delivery.py tests/test_evals_layout.py -q` green; `chain_check.py --baseline origin/release/v0.22.0` exit 0 on this branch | |
| 4 | **The sealer guarantees.** `agents/sealer.md` written anew to `spec.md` §*The sealer*, `model: opus`, `skills: [agent-contract]`. `templates/sdd-guarantee.md`. `chain_check.py`'s `guarantee` arm. `evals/behaviour/sealer/` replaced by the three guarantor cases through `rule_cases.py`. `docs/the-review-record.md`'s sealer section and `docs/the-agent-set.md`'s sealer paragraph. `skills/code-review/orchestration.md` §*the pull request opens before round 1* naming the sealer's spawn after the body and the changelog | the arm's cases seen red (S8, T16); the three sealer cases run on this tree with S6 and S7 green and the cost written (Q2); `tests/test_the_sealer_guarantees.py` green; `payload_meter --agent sealer` in `phases/phase-4.md` | |
| 5 | **Part A closes.** `overview.md`; `changelog.md` — the paragraph a plugin user reads (the record, `bin/round-record` gone, the sealer's verdict file, how old records read) and the per-script before/after lines; `questions.md` rows the work answered ticked; this branch's own review chain run on the new record (the installed warden still writes `round-N-report.md`; the orchestrator moves the file to `rounds/round-N.md` unchanged, which the new check reads) | `chain_check.py` exit 0 on this branch's own records at the pull request; the release table on the pull request; S19 | |
| 6 | **Part B opens: the baseline, then the contract.** The baseline once, on the tree after part A merges: warden, smith, framer sets, `--runs 2 -j 4`, `evals/baseline-<agent>.json` committed, `.raw/` outside the tree. `skills/agent-contract/SKILL.md` written anew: rules 1..N, each a paragraph with its `Enforced by:` or link; the four rules #923 names for it (own cleanup, a check refusing correct code, rewrite in place, do not avoid the change); the 35 `§N` citations outside the rewritten files rewritten in the same commit; the contract's pin modules rewritten in #942's layout | three baseline files, none cut short, their cost fields read (Q6); the contract is every spawn's, so all three sets run and `evals/<agent>-phase-6.md` says `pass` for each; S18; the sealer's cases re-run (its preload changed) | |
| 7 | **The warden and the reviewer's skill.** `agents/warden.md` written anew to the table's row, `skills: [agent-contract]`, opening `code-review` at step 1 and `writing-style` at the record; `skills/code-review/SKILL.md` to the shape; the 32 modules pinning the definition re-pointed or removed with a row; S17's rule list in `phases/phase-7.md` | the warden set `pass`; S14, S15, S17; `rules --check` exit 0 | |
| 8 | **The smith, the framer and their skills.** `agents/smith.md`, `agents/framer.md` written anew; `skills/implement/SKILL.md` and `skills/writing-style/SKILL.md` to the shape; their pin modules | the smith and framer sets `pass`; S14, S15, S17 | |
| 9 | **The sealer and the scribe to the shape, and the close.** `agents/sealer.md` to the shape (its job unchanged from phase 4); `agents/scribe.md` and `skills/legacy-parity/SKILL.md`; an agent's set re-run only where a preload file changed after its last passing record; `overview.md`, the changelog fragment with the per-agent before/after table (bytes, tokens read, spend, outcome both sides) | a `pass` record for every agent re-run, or its last record naming its finished preload; `rules --check` exit 0; `payload_meter` for all five in the fragment | |

This table is also where the work records how far it got. **Status is empty,
or the commit that closed the phase.** Re-read the column after any rebase.
Rows 6–9 are built in part B's work item and their Status cells are filled
there; they stand here so the design is read in one place.

### Test rows — the mutation each case kills

| Case | Guards | Mutation it kills |
|---|---|---|
| T11 `tests/test_chain_check.py::test_an_open_verdict_fails_a_ready_pull_request` (NAME NOT IN TREE until phase 3) | S3 | the arm reading `Pass` instead of the rows; a draft refused; the row id or the word dropped from the message |
| T12 `…::test_the_last_record_is_at_head_or_only_record_commits_follow` | S4 | a code commit after the last record passing; a record commit after it failing |
| T13 `…::test_a_record_written_by_the_old_generator_reads` | S11 | the arm refusing a field it no longer judges; a record with `Needs a fix` read as malformed |
| T14 `tests/test_broad_gate.py::test_a_green_run_writes_the_file_on_either_route` | S5 | the file written only where `Review` is `straight to the PR`; a cell write attempted |
| T15 `…::test_a_file_naming_another_commit_fails_a_ready_pull_request` | S5 | HEAD not compared; a stale run accepted |
| T16 `tests/test_the_sealer_guarantees.py::test_a_verdict_other_than_sound_fails_a_ready_pull_request` | S8 | `not sound` or `undecidable` passing; a file at another commit passing; the template's placeholder passing |
| T17 `tests/test_a_rewritten_definition_proved_non_inferior.py[rule 3]` (re-pointed) | the proof | shape read on the old side; reach read on one side |
| T18 `tests/test_evals_layout.py` (extended) | the sealer's cases | a case under `evals/behaviour/sealer/` grading a `Broad gate` cell |

Each definition rewrite in part B is verified by its eval record, the pins it
re-points and `rules --check`, not by a new case.

## Operational impact

- From phase 3, a review round costs one file instead of two and no generator
  command; a fix pass edits two cells per open row; the orchestrator commits
  what the agents wrote. A pull request fails for an open verdict, an unread
  last fix, a stale or absent broad-gate file, or a verdict other than `sound`,
  each naming the file and line. The hygiene step's command is unchanged.
- The suite loses about 3,000 of its 6,827 seconds (S12) and 68 K lines of
  tests, with each deleted module's guard named once; CI per run falls by the
  same share on all three legs.
- A plugin user on 0.22.0 keeps their records and their workflow file; they
  lose `bin/round-record` and gain `guarantee.md`, and the changelog says so.
- Part A's own review runs with the installed 0.21.1 warden, whose report the
  orchestrator moves to `rounds/round-N.md` unchanged; the new check reads it.
- Part B changes what every spawn reads; a rule a rewrite dropped fails its
  agent's cases where an output shows it, and is a row of the phase record
  where none does. The proof costs the orchestrator's account ≈ $150 and CI
  nothing.
- No new dependency; stdlib Python at the floor. The tree loses two scripts'
  worth of record machinery and three documents, and gains one document, one
  template and two test modules.
