# Implementation Plan: every agent, skill and doc states the current rule only

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-14 by the repository owner, when `smith` was spawned.
Approved 2026-10-15 by the repository owner, when `smith` was spawned for the reframed plan.
Approved 2026-10-15 by the repository owner, for the replanned phases 1–7, when `smith` was spawned for phase 1's second act.
Approved 2026-10-15 by the repository owner, for the new-slate frame split into parts A and B, when `smith` was spawned for phase 3.
Approved 2026-10-15 by the repository owner, for the repair after round 2, when `smith` was spawned for phase 5a.
Approved 2026-10-15 by the repository owner, for the repair after round 4, when `smith` was spawned for phase 5b.

Reframed 2026-10-15 as a new slate, from phase 3 on, against #923's body as
the owner rewrote it that day. Phases 1 and 2 are closed and keep their rows
and commits; every row from 3 on replaces the earlier plan's.

Reframed 2026-10-15 after round 2, inside part A. Round 2 marked two of round
1's fixes `fix of a fix`: the open-row reading of `chain_check.py` (round 1's
🔴 1, round 2's 🔴 1) and the `.test_durations` file (round 1's 🟡 5, round
2's 🟡 2), and deferred a third finding to the same frame (round 2's 🟡 3).
Phases 1–5 keep their rows and commits; phase 5a is the repair, and it adds no
mechanism. What each repair decides is in `spec.md` §*What leaves* and the
Alternatives rows R–U below.

Reframed 2026-10-15 after round 4, inside part A. Round 4 marked one finding
`fix of a fix`: round 3's fix pass corrected a stored count of unpriced cases
in `spec.md` and `questions.md` that its own two commits had already made
false again (round 4's 🟡 2), the third round running that a figure in this
item's documents was recounted by hand. It deferred a second finding to the
frame: the sealer's step-3 duty from round 3's fix is in `agents/sealer.md`
alone, while `docs/the-review-record.md` §*The guarantee* and
`templates/sdd-guarantee.md` still list its old three acts, so a row the
sealer is told to name has nowhere to go (round 4's 🟡 1). Phases 1–5a keep
their rows and commits; phase 5b is the repair, and it adds no mechanism and
touches no code. What it decides is `spec.md` §*The sealer* (one list of the
acts, in the definition; the row lands in `## Claims re-run`), §*A number in
this frame names its moment or its bound*, and the Alternatives rows V–Z
below. Phase 5b rewrote the builder's two documents, `overview.md` and
`changelog.md`, to it.

Reframed 2026-10-15 after round 5, inside part A — the third reframe of this
run and the second in a row on one mechanism, so this one asks what the
mechanism decides rather than where its edge is. Round 5 marked both its
findings `fix of a fix`: the sealer's step 3 and the guarantee template gave
two shapes for one `Result` cell (round 5's 🟡 1), and S21 claimed a reader
and a compliance that the tree did not show (round 5's 🟡 2). Read as a
chain, 🟡 1 is the third repair of one trade. The reframe after round 2 had
the check pass a 🔴 or 🟡 row closed by a 🟢 or ❓ row's word and named the
sealer as the backstop; round 3 found the sealer not told, round 4 found the
row it was told to name had no home, round 5 found the home had two shapes.
The trade is closed where the fact is read: the check refuses such a row,
the sealer's duty leaves, and with it its pins, its pointers, Q8 and the
part-B case. S21 is narrowed to the surfaces a reader acts on — the changelog
fragment and the rewritten `docs/` sentences — and the work item's documents
are readings at a moment. Phases 1–5b keep their rows and commits; phase 5c
is the repair, the one code change being `chain_check.py#open_findings`
reading one more fact. What it decides is `spec.md` §*What leaves* (the
severity-keyed row), S3, S20, S21, §*A number in this frame*, and the
Alternatives rows AA–AC below.

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
| R. The open-row reading keeps sorting rows into findings and non-findings — by the `#` cell (round 1's fix), by a 🔴 or 🟡 anywhere in the row (the base, round 2's paste), or both | each sorting is a guess from words about which rows a fix pass owed, and each guess had an edge the next round found: a severity in the Finding cell, an empty `#` cell, a `No.` header, a ⬜ cell over a 🔴 text. The finding-only word set caught nothing in the 36 records in the tree (round 2's probe); the sorting is what the two fix rounds chased | none | rejected (reframe after round 2); the check reads the `Verdict` cell alone, and every row must close. Narrowed after round 5 (AA): no row is sorted out of the reading, and a row whose first cell carries a finding's mark closes by the fix pass's words alone |
| S. `release_report.py#suite_seconds` prices only the cases whose module file exists (round 1's paste) | module existence is not collection: 301 of the stale entries sat in modules that still exist (round 2's 🟡 2). A sum that drops entries by a guess hides the staleness the durations case exists to show | none | rejected |
| T. `suite_seconds` prices only the cases the suite collects | the report reads two trees at tags and collects neither; a second reading of the one fact `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#dead` already holds, kept in a reader that is a report | none | rejected; the fix is in the data, and the reader sums the file as it is |
| U. `STALE_SHARE` raised, or the durations case excused for this branch | the case caught what it is for: a branch that removed a twentieth of the suite's time without refreshing the file | none | rejected |
| V. The sealer's act list kept in the document and the template, extended to four (round 4's paste) | three statements of one list held in step by two pins; round 3's fix pass reached one of the three, which is how a list in three files stales. The next act added meets the same three edits | none | rejected (reframe after round 4); `agents/sealer.md` step 3 lists the acts, the document and the template point at it and name none |
| W. The sealer names a 🔴 or 🟡 row closed by another kind's word in `## The parties`, as the warden's last record disagreeing with itself | a party row holds one party's story; such a row is a claim about one finding, and a second one has no second row. `## Claims re-run`'s four columns already hold a claim, its coordinate, what was done and whether it holds | none | rejected; one `## Claims re-run` row per such row, `Result` the answering row or `does not hold` |
| X. The counts in this item's documents kept and recounted at each fix pass, or each pinned to a commit after the fact | a figure pinned to its commit is history and stays; an unpinned one in a shipped surface is a claim about HEAD that every later commit can make false. Recounting is the loop rounds 3 and 4 ran, and a pin added after the fact is a recount with a date | none | rejected; a figure in the changelog or the docs names its moment or its bound at the sentence that states it, or leaves (`spec.md` §*A number in this frame*) |
| Y. A check over the five documents that refuses an unpinned figure | which figures are counts of the tree is read from their sentences, and a reading guessed from words is a report, not a gate (`CLAUDE.md`) | seconds | rejected; each round's warden reads the documents, and nothing counts them against the tree (narrowed after round 5, AC) |
| Z. A behaviour eval in part A for the sealer's step-3 duty | one more case and two runs on the owner's budget, against a definition part B's phase 9 rewrites and re-runs; the wording pins hold the sentence until then | none in CI; ≈ $4–8 on the orchestrator's account | left with the duty (reframe after round 5, AA): the rule is the check's, its proof is `tests/test_chain_check.py`, and no sealer case is owed in either part |
| AA. The sealer keeps the duty over a 🔴 or 🟡 row closed by another kind's word, and the template takes step 3's `Result` shape (round 5's paste) | a fourth repair on one trade's edge: the reframe after round 2 traded a 🔴 row at `confirmed` passing the check for one reading, and rounds 3, 4 and 5 each repaired the backstop that trade needed — not told, no home, two shapes. The duty makes an agent read a fact a script can read, after the suite, once per ready pull request, with `questions.md` Q8 asking the owner to pay for an eval of it. The mark is already read by the check to word its refusal (`CLOSES_BY`), so reading it to narrow the closing words adds no reading guessed from prose | none | rejected; the check refuses the row (`spec.md` §*What leaves*, S3, S20) and the duty, its two pins, its pointers, Q8 and the part-B case leave |
| AB. The check reads a 🔴 or 🟡 anywhere in the row as the finding's mark (the base's `open_blocking`, round 2's paste) | a 🟢 row's Finding cell names the earlier round's 🔴 or 🟡 it closes — *round 4's 🟡 1 is closed* — so the reading refuses `confirmed` on most 🟢 rows in the tree (204 at 81e8d785, `executed`), which is round 2's guess from words again | none | rejected; the first cell alone, where the template puts the mark; a row whose severity stands only in its Finding cell closes as phase 5a reads it, and `spec.md` §*What leaves* says so |
| AC. S21 kept over the five work-item documents, with the sealer's step 4 as its reader | the sealer's step 2 reads `spec.md`, `plan.md` and `changelog.md` and neither `questions.md` nor `overview.md`, so the reader the rule named reads three of five; and a frame-time figure in `plan.md`'s Technical context or a question's wording is a reading at 680142f2 that nobody acts on, so a rule that makes it a finding spends a round on paperwork (round 5's 🟡 2, five sentences, one of them wrong) | none | rejected; S21 covers the shipped surface, and the work item's documents are readings at a moment (`spec.md` §*A number in this frame*) |

## The split

| Part | Holds | Where it takes over |
|---|---|---|
| A — this work item, phases 3–5, 5a, 5b and 5c | the record, the five-arm check, the broad gate's one file, the sealer as guarantor with its template, arm and cases, `docs/the-review-record.md`, the orchestration sections, the tests sorted into #942's layout, the changelog fragment | — |
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
| 3 | **The record is the warden's file, and the check reads five facts.** `templates/sdd-round.md` to `spec.md` §*What a round records*. `chain_check.py` rebuilt to the five arms of §*Data & interfaces*, reading `Target SHA` and the `Verdicts` table of every record written to date and nothing else of them. `broad_gate.py` writing `broad-gate.md` on both routing answers, its record arms and the `round_record` import gone. `round_record.py`, `bin/round-record{,.cmd}`, `hooks/review-history-guard.py` and its dispatch, the `tests-todo.md` readers in `settle.py` and the documents, gone. `docs/the-review-record.md` written — the record, the verifying round, the cap (Q1's default), the `fix of a fix` stop, the filing ladder, the handoff rule (coordinates, never prose), each with `Enforced by:` or a link; `docs/round-record-spec.md`, `docs/review-chain-spec.md`, `docs/review-handoff-protocol.md` gone and no file naming them. `docs/the-record-layout.md` §*seal/specs/<work-item-id>/*, `docs/the-broad-gate.md`'s cell paragraphs, `docs/the-agent-set.md` §*What each party writes* rewritten in place. `skills/code-review/orchestration.md`'s record sections rewritten or removed as §*Data & interfaces* lists, and the delivery table's rows with them; `skills/code-review/SKILL.md` §*Findings format*'s ⬜ line and §*Cross-session records* rewritten in place to the new record (the skill is written whole in part B). `agents/warden.md` §*Report* and `agents/smith.md` §*Phases* step 5 rewritten in place to the record path and the two cells (the definitions are written whole in part B). The warden's shape graders re-pointed at `rounds/round-N.md`, the two field graders gone, `noninferiority.py#verdict` rule 3 reading shape on the new side. The 70 test modules sorted: `tests/test_chain_check.py` and `tests/test_broad_gate.py` in #942's layout for what still holds; every deleted module's guard one line in `phases/phase-3.md` | the new modules' cases seen red first (S3, S4, S5, S11, T11–T15); S10's `grep`; S12's durations sum under 1,500 s; S13's `rules --check` exit 0; `bin/test tests/test_chain_check.py tests/test_broad_gate.py tests/test_every_orchestrator_act_names_its_delivery.py tests/test_evals_layout.py -q` green; `chain_check.py --baseline origin/release/v0.22.0` exit 0 on this branch | 1912e63d |
| 4 | **The sealer guarantees.** `agents/sealer.md` written anew to `spec.md` §*The sealer*, `model: opus`, `skills: [agent-contract]`. `templates/sdd-guarantee.md`. `chain_check.py`'s `guarantee` arm. `evals/behaviour/sealer/` replaced by the three guarantor cases through `rule_cases.py`. `docs/the-review-record.md`'s sealer section and `docs/the-agent-set.md`'s sealer paragraph. `skills/code-review/orchestration.md` §*the pull request opens before round 1* naming the sealer's spawn after the body and the changelog | the arm's cases seen red (S8, T16); the three sealer cases run on this tree with S6 and S7 green and the cost written (Q2); `tests/test_the_sealer_guarantees.py` green; `payload_meter --agent sealer` in `phases/phase-4.md` | f1ccf61a |
| 5 | **Part A closes.** `overview.md`; `changelog.md` — the paragraph a plugin user reads (the record, `bin/round-record` gone, the sealer's verdict file, how old records read) and the per-script before/after lines; `questions.md` rows the work answered ticked; this branch's own review chain run on the new record (the installed warden still writes `round-N-report.md`; the orchestrator moves the file to `rounds/round-N.md` unchanged, which the new check reads) | `chain_check.py` exit 0 on this branch's own records at the pull request; the release table on the pull request; S19 | d3da26dd |
| 5a | **The repair after round 2 — part A's last phase.** (i) `chain_check.py#open_findings` reads one fact per row: the `Verdict` cell is a word of `CLOSED_WORDS` (`deferred` with a home), or the row fails a ready pull request — whatever its `#` cell, which only names the row in the refusal (`spec.md` §*What leaves*, S3). `severity_of`, `NOT_FINDINGS`, `FINDING_CLOSES` and the `ID_COLUMN` lookup leave; `FINDINGS`, `BLOCKING`, `SHOULD` stay as the vocabulary. `tests/test_chain_check.py::TestOpenFindings` rewritten to the one reading, its two sides a 🟢, ❓ and ⬜ row at `open` (fails) and a 🔴 row at `confirmed` with a bare-number row at `fixed <sha>` (pass); `TestMain::test_an_open_verdict_fails_a_ready_pull_request` kept. Every sentence stating the severity-keyed rule rewritten in place, the class enumerated by `git grep` for `🔴 or 🟡 row`, `🔴·🟡`, `` `#` cell `` and `lost its severity` outside `seal/specs/`: `docs/the-review-record.md` §*What the check reads at the pull request* (its `Enforced by:` unchanged), `templates/sdd-round.md:35`, `chain_check.py:17`, `README.md:182`, `README.ko.md:173`, `.github/workflows/hygiene.yml:169`, `templates/hygiene.yml:83`, this item's `changelog.md:30-33`. (ii) `.test_durations` pruned to the ids `pytest --collect-only -q` collects, by a script run once from the repository root and deleted (contract §7), with 1b875efc's round-trip guard; nothing re-measured and nothing added to the tree; `overview.md`'s S12 row, round 1's 🟡 5 account and the changelog's suite figure recounted. (iii) `tests/test_one_word_one_meaning.py:472`: five `.py` members → four. `phases/phase-5a.md`; the changelog fragment's line counts recounted | the rewritten `TestOpenFindings` cases seen red on 2f0b4460's `open_findings` (a ⬜, 🟢 or ❓ row at `open` passes there) and green after; `bin/test tests/test_chain_check.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_one_word_one_meaning.py tests/test_the_release_table_reads_two_trees_and_fails_nothing.py -q` exit 0; `chain_check.py --baseline origin/release/v0.22.0` exit 0 on this branch with no open row in the 36 records; `bin/test tests -q -k test_the_durations_file_prices_the_suite` exit 0, its output naming 0 entries gone; the `git grep` above finding nothing outside `seal/specs/`; `bin/rules --check` exit 0; `ruff check` and `ruff format --check` on the touched files | 4632eeea |
| 5b | **The repair after round 4 — part A's last phase, no code.** (i) **One list of the sealer's acts, and a row for the fourth.** `agents/sealer.md` step 3: "Name each one" becomes *write each one as a row of `## Claims re-run`, its `Result` the later round's row that answers it or `does not hold`*, the `not sound` clause kept. `docs/the-review-record.md` §*What the check reads at the pull request*, the open-row paragraph: its last sentence says the sealer names such a row in `guarantee.md`'s `## Claims re-run` and reads it as `not sound` unless a later round answers it, and its `Enforced by:` gains `tests/test_the_sealer_guarantees.py::TestDefinition::test_the_sealer_names_such_a_row_in_the_claims_table`. §*The guarantee*'s second paragraph keeps its bold sentence and *It does not re-judge…*, and between them says the acts are `agents/sealer.md` step 3's and step 4's, each act one row of `## Claims re-run` or `## The parties`, listing none; it gains `Enforced by: …::TestDocument::test_the_guarantee_section_points_at_step_3_and_lists_no_act`. `templates/sdd-guarantee.md`'s comment over `## Claims re-run`: *One row per act of `agents/sealer.md` step 3, whatever the act. `Result` reads `holds`, or `does not hold — <what came back>`, and a `does not hold` is what the verdict names.* The three cases (T21–T23) in `tests/test_the_sealer_guarantees.py`, each seen red on the tree before its sentence: T21 on the definition without the `## Claims re-run` clause, T22 on the template as it stands (`fixed <commit>` in its comment), T23 on the document as it stands (`:120`). The changelog's sealer entry says where the row lands. (ii) **The stored counts leave the builder's two documents** (`spec.md` §*A number in this frame*; the frame's three were rewritten at the reframe): `changelog.md`'s *Lines after* column leaves and the *Lines before* column stays, headed as counted at ce448bbe; its sentence counting test modules and test lines after the branch leaves; `overview.md:56`'s *now holds … sums to* and `:79`'s S12 figures name 4632eeea as their moment, and §*Part A and part B* names 5a and 5b. (iii) `phases/phase-5b.md`; `rounds/round-4.md` is not edited | T21–T23 red then green (`bin/test tests/test_the_sealer_guarantees.py -q -p no:xdist`, the red run with the sentence absent, each exit named in the phase record); `bin/rules --check --root <worktree>` exit 0 with the two new targets resolving; `git grep -n "fixed <commit>"` outside `seal/specs/` and `changelog/` finds only `docs/the-review-record.md` §*The round record*, `templates/sdd-round.md` and `agents/sealer.md` step 3; `bin/test tests/test_the_sealer_guarantees.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_the_rules_have_one_owner.py tests/test_a_document_that_names_a_script_says_how_to_reach_it.py -q` exit 0; `chain_check.py --baseline origin/release/v0.22.0` exit 0 on this branch; the five documents re-read against §*A number in this frame*'s three kinds, with every figure that stays naming its moment or its bound, listed in the phase record | 704395b1 |
| 5c | **The repair after round 5 — part A's last phase: the trade closes in the check, and the sealer's duty over it leaves.** (i) **One more fact in the check.** `chain_check.py#open_findings`: a row whose first cell opens with a mark of `FINDINGS` closes only by `fixed` followed by a commit (`SHA_RE` in the cell), `answered`, or `deferred` with a home; every other row closes by any word of `CLOSED_WORDS` as phase 5a reads it; `deferred` with no home stays open for every mark. The refusal's wording is unchanged, since `CLOSES_BY` already lists the fix pass's three for a 🔴 or 🟡 row. The module docstring (`chain_check.py:17-18`), `open_findings`'s docstring and the comment over `CLOSES_BY` ("It picks the message only") rewritten in place to the new reading. Test-first in `tests/test_chain_check.py`: `TestOpenFindings::test_a_closing_word_closes_a_row_of_any_mark` (T20) becomes `test_a_finding_row_closes_only_by_a_fix_passs_word` (T24) — named: `🔴 1 … confirmed`, `🟡 2 … ❓ out of verified scope`, `🔴 3 … fixed` with no commit; passing: `🟢 … confirmed`, `❓ … ❓ out of verified scope`, `⬜ 3 … answered`, `4 … fixed abc1234`, `carried … withdrawn`, an empty first cell at `deferred <home>`, `🟡 5 … deferred the frame` — seen red on 704395b1's `open_findings`; T19 unchanged; `TestMain::test_the_refusal_names_the_words_that_close_a_row_of_its_mark` gains a `🔴 1 … confirmed` row, named with the fix pass's three; `test_a_record_written_by_the_old_generator_reads` is the corpus run, every record in the tree under the new reading (83 🔴 and 🟡 rows at 81e8d785 all `fixed <sha>`, `answered` or `deferred <home>`, framer's probe). (ii) **The duty leaves, and the documents say the rule once.** `agents/sealer.md` step 3: the sentences from *Read every 🔴 and 🟡 row of every record* to *the verdict is `not sound`* leave; the three acts stay, and the step gains no `Result` shape (the template's holds: `holds` or `does not hold — <what came back>`). `tests/test_the_sealer_guarantees.py::TestDefinition::test_the_sealer_reads_every_red_and_yellow_row_not_only_fixed_ones` and `::test_the_sealer_names_such_a_row_in_the_claims_table` (T21) leave; T22 and T23 stay and are green unchanged. `templates/sdd-guarantee.md`'s comment over `## Claims re-run`: *One row per act of `agents/sealer.md` step 3, whatever the act, and one per thing the act checks. `Result` reads `holds`, or `does not hold — <what came back>`, and a `does not hold` is what the verdict names.* `docs/the-review-record.md` §*What the check reads at the pull request*, the open-row paragraph: its last two sentences say the mark narrows the words for a 🔴 or 🟡 row, so a 🟢 row at `open` and a 🔴 row at `confirmed` both fail, and its `Enforced by:` drops the T21 name and gains T24; §*The round record*'s vocabulary paragraph gains T24 beside `TestOpenFindings`. `templates/sdd-round.md:34-36`'s closing comment: a 🔴 or 🟡 row fails while it reads anything but the fix pass's three, any row while it reads a word outside the five. The class enumerated by `git grep` for `whatever its mark`, `whatever mark`, `reads the word and not the mark`, `another kind's word` and `answers nothing` outside `seal/specs/`: the README, both `hygiene.yml` copies and `docs/the-agent-set.md` say *a row still open* and stay true, and each hit that states the old reading is rewritten in place. (iii) **The builder's documents.** This item's `changelog.md`: the check entry's sentence on the words a row closes by says the finding's three and the other two marks' one each; the sealer entry's clause from *It reads every 🔴 and 🟡 row of every round* to *unless a later round answers it* leaves. `overview.md`: one divergence row for the 5c decision (what phase 5b built that this phase removes, and why), and the row *What the class check for the sealer's acts finds* re-read. (iv) `phases/phase-5c.md`; `rounds/round-5.md` is not edited; part B is out of scope | T24 red on 704395b1's `open_findings` (exit named in the phase record), green after; `bin/test tests/test_chain_check.py tests/test_the_sealer_guarantees.py -q` exit 0, T21 and round 3's pin absent from the collection; `mutation-check` red for: the `FINDINGS` narrowing dropped (T24), `fixed` with no commit accepted (T24), the narrowing applied to every mark (T24's 🟢 row); `bin/rules --check --root <worktree>` exit 0 with the T21 target gone from every `Enforced by:`; the `git grep` above finding no sentence of the old reading outside `seal/specs/`; `chain_check.py --baseline origin/release/v0.22.0` exit 0 on this branch (every record in the tree under the stricter reading); `ruff check` and `ruff format --check` on the two touched `.py` files | |
| 6 | **Part B opens: the baseline, then the contract.** The baseline once, on the tree after part A merges: warden, smith, framer sets, `--runs 2 -j 4`, `evals/baseline-<agent>.json` committed, `.raw/` outside the tree. `skills/agent-contract/SKILL.md` written anew: rules 1..N, each a paragraph with its `Enforced by:` or link; the four rules #923 names for it (own cleanup, a check refusing correct code, rewrite in place, do not avoid the change); the 35 `§N` citations outside the rewritten files rewritten in the same commit; the contract's pin modules rewritten in #942's layout | three baseline files, none cut short, their cost fields read (Q6); the contract is every spawn's, so all three sets run and `evals/<agent>-phase-6.md` says `pass` for each; S18; the sealer's cases re-run (its preload changed) | |
| 7 | **The warden and the reviewer's skill.** `agents/warden.md` written anew to the table's row, `skills: [agent-contract]`, opening `code-review` at step 1 and `writing-style` at the record; `skills/code-review/SKILL.md` to the shape; the 32 modules pinning the definition re-pointed or removed with a row; S17's rule list in `phases/phase-7.md` | the warden set `pass`; S14, S15, S17; `rules --check` exit 0 | |
| 8 | **The smith, the framer and their skills.** `agents/smith.md`, `agents/framer.md` written anew; `skills/implement/SKILL.md` and `skills/writing-style/SKILL.md` to the shape; their pin modules | the smith and framer sets `pass`; S14, S15, S17 | |
| 9 | **The sealer and the scribe to the shape, and the close.** `agents/sealer.md` to the shape (its job unchanged from phases 4 and 5c: three acts in step 3, the sealer's three cases); `agents/scribe.md` and `skills/legacy-parity/SKILL.md`; an agent's set re-run only where a preload file changed after its last passing record; `overview.md`, the changelog fragment with the per-agent before/after table (bytes, tokens read, spend, outcome both sides) | a `pass` record for every agent re-run, or its last record naming its finished preload; `rules --check` exit 0; `payload_meter` for all five in the fragment | |

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
| T19 `tests/test_chain_check.py::TestOpenFindings::test_every_row_closes_by_a_closing_word_whatever_its_id_cell` (NAME NOT IN TREE until phase 5a) | S3 | a 🟢, ❓ or ⬜ `#` cell skipping the row; the severity read back to pick a word set; `deferred` with no home closing; a row's `#` cell dropped from the refusal |
| T20 `…::TestOpenFindings::test_a_closing_word_closes_a_row_of_any_mark` (phase 5a; REPLACED by T24 in phase 5c) | S3, S11 | `confirmed` or `out of verified scope` refused on a 🔴 row, which would fail records the check must read; a bare-number row at `fixed <sha>` refused. Phase 5c overturns its premise for a finding's mark, and T24 takes its passing rows |
| T21 `tests/test_the_sealer_guarantees.py::TestDefinition::test_the_sealer_names_such_a_row_in_the_claims_table` (phase 5b; LEAVES in phase 5c) | S20 as it stood | the `## Claims re-run` clause dropped from step 3 while "every 🔴 and 🟡 row" stays; the `does not hold` result dropped. Leaves with the duty it pinned, as does round 3's `test_the_sealer_reads_every_red_and_yellow_row_not_only_fixed_ones` |
| T24 `tests/test_chain_check.py::TestOpenFindings::test_a_finding_row_closes_only_by_a_fix_passs_word` (NAME NOT IN TREE until phase 5c) | S3, S20, S11 | the `FINDINGS` narrowing dropped, so `🔴 1 … confirmed` passes (phase 5b's reading); a bare `fixed` with no commit accepted on a 🔴 row; the narrowing applied to every mark, so `🟢 … confirmed` or `carried … withdrawn` fails, which would refuse records the check must read; `deferred` with a home refused on a 🟡 row |
| T22 `…::TestTemplate::test_the_claims_table_takes_a_row_per_act_of_step_3_and_lists_none` (NAME NOT IN TREE until phase 5b) | S20 | the comment naming an act again (`fixed <commit>` back in the template); the pointer at `agents/sealer.md` step 3 dropped |
| T23 `…::TestDocument::test_the_guarantee_section_points_at_step_3_and_lists_no_act` (NAME NOT IN TREE until phase 5b) | S20 | §*The guarantee* listing the acts again (`fixed <commit>` between its heading and `## The run`); the pointer at step 3 dropped. The record's vocabulary paragraph in §*The round record* keeps its `fixed <commit>` and is outside the slice read |

Each definition rewrite in part B is verified by its eval record, the pins it
re-points and `rules --check`, not by a new case.

## Operational impact

- From phase 3, a review round costs one file instead of two and no generator
  command; a fix pass edits two cells per open row; the orchestrator commits
  what the agents wrote. A pull request fails for an open verdict, an unread
  last fix, a stale or absent broad-gate file, or a verdict other than `sound`,
  each naming the file and line. The hygiene step's command is unchanged.
- The chain's tests fall under S12's bound, below 1,500 s from the 4,553 s
  measured at 680142f2, with each deleted module's guard named once in
  `phases/phase-3.md`; CI per run falls by the same share on all three legs.
- A plugin user on 0.22.0 keeps their records and their workflow file; they
  lose `bin/round-record` and gain `guarantee.md`, and the changelog says so.
- Part A's own review runs with the installed 0.21.1 warden, whose report the
  orchestrator moves to `rounds/round-N.md` unchanged; the new check reads it.
- From phase 5a, a ready pull request fails for any row of any record whose
  verdict is not a closing word, whatever mark the row carries; from phase
  5c, a row whose first cell opens with 🔴 or 🟡 fails as well unless it
  reads `fixed <commit>`, `answered` or `deferred <home>`, so a finding the
  warden closed with a 🟢 row's word stops the pull request instead of
  reaching the sealer. The release table prices the suite at what
  `.test_durations` holds for collected cases until the first refresh from a
  `tests` run prices the cases this branch added; the unpriced share is held
  under `STALE_SHARE` by the durations case, and no figure for it is kept here.
- From phase 5b, the sealer's acts are listed in its definition alone, and
  the document and the template point at that list. From phase 5c the list
  holds three acts: the sealer reads no 🔴 or 🟡 row for its closing word,
  since the check refuses one closed by another kind's word, and every row of
  `## Claims re-run` has the template's one `Result` shape. A figure in the
  changelog fragment or in a rewritten `docs/` sentence names its moment or
  its bound; a figure in the work item's own documents is a reading at the
  moment the document names.
- Part B changes what every spawn reads; a rule a rewrite dropped fails its
  agent's cases where an output shows it, and is a row of the phase record
  where none does. The proof costs the orchestrator's account ≈ $150 and CI
  nothing.
- No new dependency; stdlib Python at the floor. The tree loses two scripts'
  worth of record machinery and three documents, and gains one document, one
  template and two test modules.
