# Feature Specification: every agent, skill and doc states the current rule only

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* | A mechanism stays only while its history shows what it caught against what it costs. Do not avoid the change a problem calls for: before a fix adapts to a structure, ask whether the structure should change; what exists is a reference, not a constraint. A change rewrites in place and removes what stood on the old fact in the same commit. This frame weighs every field of the review record and every agent definition by it, and keeps nothing because it is there |
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here asks a person mid-run. A rewrite is proved not worse by a run nobody scores by hand; a check that fails names the file and line; the sealer's one undecidable case goes to the owner as a written question, after the run |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | Phases 3 and 4 remove gates and move checks: cases seen red, the failure direction (the chain check blocks less and reads fewer fields; what it still reads it reads at the pull request as before), a prompt budget of zero, `## Removes` below |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file*, §*seal/specs/<work-item-id>/* | The changelog is a fragment; the table of a work item's files is rewritten in place here because this item changes what the files are |
| `docs/the-agent-set.md` | One contract every agent receives, one definition each; the writer of a contract is not its executor; a subagent asks nobody. Rewritten in place here: the sealer's job changes and the set is derived from the jobs |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The work alters what every spawn reads and what every pull request is checked against, which is the top rung |
| #923's body, rewritten 2026-10-15 by the owner | The one source for what was decided: the principle, the six things the item builds, the rules the rewrite states in place, the proof's two axes. Where this file and that body differ, the body holds |
| The owner's decision of 2026-10-16, after round 6 | The round record is designed anew from its jobs and not patched again. What the check read was the old generator's table with fields subtracted and a rule added per round, and the check missed one fact four times (rounds 1, 2, 5 and 6) for one reason: it told a finding from a non-finding by an emoji mark in a table that mixed three kinds of row, and every spelling it did not recognise fell to the passing side. What exists is a reference, not a constraint (`CLAUDE.md`). The rule the new shape embodies — a gate fails closed: input it cannot read is refused, never passed — is `questions.md` Q9's to put into `CLAUDE.md` or not |
| #942 (the test layout) | A test file per shipped module, its tests grouped by function, a success and a failure case per group. The test modules this item writes for the chain check and the broad gate follow it; the modules it deletes are listed by what they guarded, one line each |
| #945 §3 | Round-record inheritance moved here (owner, 2026-10-15); the agent-lifetime rule, the orchestrator's folding rule and the process archive stay there |
| #940, #941 | What an agent opens on demand, and `docs/`, are theirs. This item rewrites a file of theirs only where this item makes a sentence of it false |

## What this work is — a new slate, not a trim

The agents and the review chain between them are designed anew from the jobs,
with no loss in what the work gets right (owner, 2026-10-15). Today's files are
a reference, as the old tests are for #942. No heading, section number, field
or agent is kept because it was there. The earlier frames of this item trimmed
files whose structure was the problem; this one asks of each structure whether
it should exist.

Phases 1 and 2 stand and keep their commits: the proof harness is light
(`evals/`), the five pre-0.22.0 eval cases are gone, the budget concept is
gone, `rules --check` holds every `Enforced by:` target and the release table
prints on a release pull request (`plan.md` rows 1 and 2).

## The jobs, and who does each

A job that needs judgment is an agent's; a job that is mechanical is a
script's; a job that needs a person's answer is the session's, before the
first edit.

| Job | Needs | Done by | Its one durable write |
|---|---|---|---|
| Frame: what is built, in which phases, what only a person decides | judgment over the whole tree | `framer` | `spec.md`, `plan.md`, `questions.md` |
| Build: the code, its tests, the phase record; the fix pass | judgment | `smith` | code and tests; `phases/phase-N.md`, `overview.md`, `changelog.md`; the `Verdict:` and `Answer:` lines of each finding its fix pass answers in the round record |
| Review: spec compliance, then quality, against the tree at a commit | judgment | `warden` | `rounds/round-N.md` |
| Final verification: a claim against the fact; the parties against each other | judgment, independent of the smith and the warden | `sealer` on Opus | `guarantee.md` |
| The broad run — suite, lint, typecheck — and its record | mechanics | `broad-gate` (`skills/verify/scripts/broad_gate.py`), run by the sealer as its first act | `broad-gate.md` |
| The check at the pull request: the declared parties left the records they owe, and the records agree with HEAD | mechanics | `chain_check.py` in CI | nothing |
| Fact-finding in a migration: what the original does, with coordinates | judgment over code the plugin cannot read mechanically | `scribe` | nothing — a report |
| Routing, spawning, committing the records, the pull request body, the merge | the person's answer, then the session's acts | the session | `routing.md`, the commits, the pull request |

**The agent set is the same five names, and nothing in it is inherited.**
Every job above that needs judgment has one of them, and no job needs a sixth:
the fix pass is the smith's (whether it resumes or respawns is #945's rule),
the broad run is a script's, and the check at the pull request is a script's.
What changes is the sealer's job, every agent's size and preload, and the
record that passes between them.

## The sealer — the final, independent guarantor

**Its role is: *I verified, independently of the smith and the warden, that
the work before me is sound, and I guarantee it.*** Its reference is the
owner's decision (the issue body) and the tree, never any agent's word or the
orchestrator's summary. It runs after the pull request body and the changelog
fragment are written, so they are audited too. It runs on Opus, the level of
the agents it audits: `agents/sealer.md` is the one definition that pins
`model:`.

Its order of work:

1. Run `broad-gate --base <base> --record <item>`. The script runs the
   repository's broad command and the plugin's checks and, on green, writes
   `seal/specs/<item>/broad-gate.md` (`<sha> against <base>`). A red gate ends
   the audit at `not sound — <the failing check, as the gate printed it>`.
2. Read, itself: the issue body (`gh issue view`), the diff against the base,
   `spec.md`, `plan.md`, every `phases/phase-N.md`, every `rounds/round-N.md`,
   `changelog.md`, and the pull request body (`gh pr view`).
3. **A claim against the fact.** Choose a sample of the smith's `executed` and
   `seen red` claims from the phase records — where the evidence is thinnest,
   or where the outcome rests on it — and re-run each: the test it names, the
   mutation it says went red. For every finding of every round record whose
   `Verdict:` reads `fixed <commit>`, confirm the commit touches the finding's
   `Location:` (that it is on the branch, the check already refuses
   otherwise, §*What a round records*). For every `## Removes` row of `spec.md` and every removal this
   release names in its changelog fragments, confirm nothing of it stands in
   the tree. Each thing checked is one row of `guarantee.md`'s
   `## Claims re-run`, in the template's shape and no other: `Command` the
   command re-run, `Result` `holds` or `does not hold — <what came back>`,
   and a `does not hold` makes the verdict `not sound`. Step 3 states no
   `Result` shape of its own (reframe after round 5; round 5's 🟡 1 was the
   definition and the template giving two). **These acts are listed here and
   in `agents/sealer.md` step 3, and nowhere else** (reframe after round 4):
   `docs/the-review-record.md` §*The guarantee* and
   `templates/sdd-guarantee.md`'s comment over `## Claims re-run` point at
   step 3 — one row per act, whatever the act, and one per thing the act
   checks — and name no act, so an act added to the definition has a row to
   land in and no second and third list to keep in step. Enforced by
   `tests/test_the_sealer_guarantees.py::TestTemplate::test_the_claims_table_takes_a_row_per_act_of_step_3_and_lists_none`
   and `::TestDocument::test_the_guarantee_section_points_at_step_3_and_lists_no_act`.
   **The sealer reads no finding for whether its verdict is one the check
   accepts** (reframe after round 5, kept after round 6): a `Verdict:` the
   check cannot read fails the pull request (§*What a round records*, S3),
   so the duty rounds 3, 4 and 5 each repaired — name such a row, give it a
   home, give the home a shape — is not the sealer's, and its sentence, its
   two pins and its pointers left in phase 5c (`## Removes`).
4. **The parties against each other.** The framer's spec (scope, `Removes`),
   what the smith built (the diff, the phase records), the warden's last
   record, the changelog fragment and the pull request body tell one story.
   Where two disagree, name the one the issue body and the tree contradict.
   Where the issue and the tree cannot decide it, the verdict is
   `undecidable — <the question>`, and the question is for the owner.
5. Write `seal/specs/<item>/guarantee.md` from `templates/sdd-guarantee.md`:
   the commit and base, the broad gate's result, the claims re-run (claim,
   its source, the command, the result), the stories compared (party, what it
   says, agrees or disagrees and with what), and the verdict — `sound`,
   `not sound — <what>`, or `undecidable — <question>`. Return the file's
   text as its report, every claim labelled `executed`, `read` or
   `unverified`.

**What it does not do.** It does not re-judge the design, which is the
framer's and the owner's, or the code's quality, which is the warden's. It
does not read the orchestrator's summary as a fact. It writes nothing but
`guarantee.md`, and the four acts the contract withholds from every agent stay
withheld.

**What a check reads of it.** On a ready pull request, `chain_check.py` fails
where `guarantee.md` is absent, names a commit other than HEAD, or reads
anything but `sound`. `not sound` and `undecidable` therefore stop the merge
until the orchestrator fixes what was named or the owner answers, and the
answer is written where the question is: a line under the verdict, then the
sealer is spawned again at the new HEAD.

**How it errs, stated.** It samples, so a false claim outside the sample
passes. Whether five stories agree is a judgment, so a disagreement it does not
see is missed. It runs once per ready pull request, so a push after it owes a
new run, which the HEAD rule above is what enforces.

**Its cost** (estimate from the warden's verifying rounds in the suite build,
`phases/phase-2-suite-build.md`, nothing of the sealer itself measured): one
Opus spawn per item reading about 60–100 KB of records and diff and re-running
two to five commands, ≈ $2–4 and 5–10 minutes. The old sealer ran the gate
alone on Sonnet in about 1 minute; the difference is the guarantor's seat,
which was empty.

## The review record, designed anew

### The chain as it stands, measured

`executed` 2026-10-15 at 680142f2 on this branch unless a cell says otherwise;
the scratch scripts were deleted.

| What | Value |
|---|---|
| The scripts | `skills/code-review/scripts/chain_check.py` 6,153 lines · `round_record.py` 5,596 · `skills/verify/scripts/broad_gate.py` 3,640; `chain_check.py` once over this branch, 2.7 s wall |
| The specs | `docs/round-record-spec.md` 998 lines, 69,538 B · `docs/review-chain-spec.md` 880 lines, 61,091 B · `docs/review-handoff-protocol.md` 847 lines, 54,904 B (still titled *draft 1.2*) |
| The tests that name one of the three scripts | 70 of 174 modules · 3,758 of 8,981 cases · **4,553 of the suite's 6,827 seconds (67 %)** · 68,783 lines. The eight heaviest modules of the whole suite are all theirs: `test_the_seal_is_taken_once_by_the_sealer.py` 1,036 s, `test_the_fixes_close_the_record.py` 560, `test_chain_check_at_the_pull_request.py` 423, `test_a_fix_of_a_fix_is_counted.py` 365, `test_the_record_is_generated.py` 220, `test_the_record_is_held_to_the_floor_and_the_depth.py` 198, `test_a_fragment_left_behind_is_named.py` 195, `test_a_record_precedes_the_fixes_it_commissions.py` 194 |
| The tests that pin the record's documents | `docs/review-handoff-protocol.md` 26 modules · `templates/sdd-round.md` 24 · `docs/review-chain-spec.md` 20 · `docs/round-record-spec.md` 17 · `docs/the-record-layout.md` 17 · `skills/code-review/orchestration.md` 12 |
| CI, the latest green `tests` run (38685457056) | `ubuntu` 5.4 min · `windows` 25.8 min over 4 shards · `macos` 12.5 min over 3 shards. Billed as a private repository (Windows 2×, macOS 10×) ≈ 5.4 + 51.6 + 125 = **182 minutes a run**. The hygiene run beside it: 17 s |
| 0.22.0's four reviewed items (#930, #929, #931, #944) | **19 round records and 19 reviewer reports, 564,146 B.** A record is 4–15 KB, a report 5–27 KB. #929 ran 7 rounds: its round-7 reviewer inherited 6 records and 6 reports, 193,857 B |
| The 13 fields, across the 19 records | `Target SHA` filled 19/19 · `Written late` `no` 19/19 · `Contract changes` `none` 17/19 · `New units` named 9/19 · `Fix of a fix` `first` 5, `second` 3 (#929 r3 and r6, #931 r4) · `Needs a fix` `yes` 14/19 · `Loses a record or crashes` `yes` 2/19 (#931 r1, #944 r1) · `Broad gate` written on the 4 last records · `Ran by` 19/19, read by nothing that changed an outcome · ⬜ notes carried open: #929 3 → 15 across its 7 records, #931 0 → 12 |
| The reframes the `second` stop caused | #929 three (`after round 0`, `3`, `6`), #931 one (`after round 4`). #929 was then closed by the owner at its phase 2 and the rest moved to #942 |
| `tests-todo.md` | written by 0 of the 4 items |
| CI refusals in October (`gh run list`, step conclusions) | 25 failed hygiene runs since 2026-10-01; of the 14 inspected, 8 failed at the step *a declared review chain has the round record it claimed*, on the #929, #931 and #944 branches. What each refused is `unverified`: one log was readable and printed notices (`Fix range` ends unseen after a squash, `Fixes checked by` nobody), the rest returned nothing to `--log-failed`. Answerer: the orchestrator, from the run pages |
| The owner's observation, 2026-10-15 (`read`, #923 item 3) | fitting the bookkeeping cost more turns than the reviews |
| The flow log (`read`, #935) | 0.22.0's first long segment: 30 spawns, 1,514 min, 492 tool calls, 4,607 turns; 9 framers, 18 smiths, 2 wardens, 1 sealer |

### What a round records

Reframed after round 6. The shape is derived from what each party does with
the record, and from nothing that was there before:

| Who | What they do with the record | Where in the record |
|---|---|---|
| the warden | leaves findings — what is wrong, where, why it matters, a paste-ready fix — and the probes it ran | `## Findings`, one `###` section per finding; `## Probes` |
| the smith's fix pass | answers each finding: the fixing commit, a rebuttal, or where it was deferred | the finding's `Verdict:` line and `Answer:` line, and nothing else in the file |
| the next round's warden | reads the earlier findings and their answers, confirms each that truly closed, and notes what it could not judge | `## Confirmations` and `## Not judged` of its own record; earlier files are never edited or deleted |
| the check at the pull request | one fact — is any finding without an answer — and the record's `Target SHA` | every `Verdict:` line under `## Findings`; the `Target SHA` row |
| the sealer | re-checks each `fixed <commit>` against its finding's location | the `Verdict:` and `Location:` lines |

A round records **what it reviewed, what it found, and what answered it**, in
one file the warden writes and the smith's fix pass completes:
`seal/specs/<work-item-id>/rounds/round-N.md`, from `templates/sdd-round.md`.

````
# <work-item-id> — review round N

| Field | Value |
|---|---|
| Target SHA | <sha> against <base> · a verifying round: <sha>, fixes <a>..<b> |

## Findings

### 1. <what is wrong, as a symptom, in one line>

Severity: blocks merge
Location: `path:line`
Verdict: open
Fix of a fix: <the unit the fixes under review added or changed — this line only where it applies>

<why it matters and the grounds, executed and read labelled apart>

```<lang>
<the paste-ready fix: the artefact, not a description of it>
```

Answer: <the fix pass: what was done, why the finding does not hold, or where it went>

## Confirmations

| What holds | Location | Grounds |
|---|---|---|
| round N-1's 2 is closed — <what> | `path:line` | <how this round confirmed it, executed or read> |

## Not judged

| What | Location | Who answers |
|---|---|---|

## Probes

| Command | Result |
|---|---|
````

Five things about it, each the whole of a rule:

- **The fact the check reads has one spelling in one place, and the check
  fails closed.** The one line is `Verdict: <value>`, at the start of a line,
  inside a `###` section of `## Findings`, with no emphasis, no table cell and
  no mark around it. The value is one of four shapes and nothing else:
  `open` · `fixed <commit>` (seven to forty hex digits, a commit HEAD descends
  from) · `answered` · `deferred <home>` (a home after the word). Anything
  the check cannot read is refused by name, never passed: a value outside the
  four, a `Verdict:` with emphasis or a different case, a finding with no
  `Verdict:` line or with two, a `Verdict:` line outside `## Findings`, a
  record with no `## Findings` section, a `fixed` whose commit HEAD does not
  descend from. A `Verdict:` inside a fence or a comment is not a line the
  reader sees, so a finding whose only verdict stands in its fix block has
  none, and is refused. On a ready pull request `open` fails too. No emoji,
  no table cell and no severity is read for the decision.
- **Severity is for people, and the check ignores it.** Two words,
  `blocks merge` and `fix or justify`, on the finding's `Severity:` line. The
  emoji vocabulary leaves the record: 🟢 was never a finding and is a row of
  `## Confirmations`; ❓ was never a finding and is a row of `## Not judged`,
  with who answers it; ⬜ left at the first frame. A sentence an agent reads
  and acts on is a defect when it is wrong, and is `fix or justify`; a
  sentence in a record that merely reads badly is not written as a finding.
- **The warden writes the record, and no generator copies it.** The fix is
  inside its finding, so the fix pass opens one section and finds the what,
  the where, the why and the paste in one place; a `|` in prose is prose
  again, since no finding is a table cell (#189 is a cost of the cell, not of
  the record).
- **The smith's fix pass writes two lines per finding and nothing else in
  the file.** It rewrites the finding's `Verdict:` line to `fixed <commit>`,
  `answered` or `deferred <home>`, and writes its `Answer:` line. There is no
  fix table and no `close`.
- **The reviewed commit is a fact every check rests on, and it is the one
  field.** The broad gate's run lives in `broad-gate.md`, the sealer's verdict
  in `guarantee.md`, and the pull request knows its own branch.

**No reader for the old shape.** The check judges only the work items the
pull request's own commits declare or change (`chain_check.py#main`,
`#carried_by`; `docs/the-review-record.md` §*An item is judged at the pull
request that carries it*), so the 34 records of the other 0.22.0 items were
judged at their own pull requests and are read by nothing again. This item's
six records are rewritten into the shape, mechanically, with every verdict
and every ground unchanged in substance, in the phase that lands the reader
(`plan.md` row 5d-i): a 🔴 or 🟡 row becomes a finding, its `· fix pass:` or
`· orchestrator:` tail its `Answer:`, its paste block moves inside it; a 🟢
row becomes a `## Confirmations` row and a ❓ row a `## Not judged` row. The
test that read every record in the tree goes with the shape it read
(`plan.md` Alternative AJ). What a release reads of records
(`.github/scripts/release_seal.py#chain_counts`, the panel's
`broad_gate.py#rounds_rows`) reads the new shape through the check's reader
and reports an old-shape record as *not read*, which is the fail-closed
answer for a count too.

### What leaves, what stays, and the evidence for each

Judged on what its history shows it caught against what it cost. The 0.22.0
records above are the measured history; where a field's defence is a spec's
citation of an older issue, that is `read` and says so.

| Mechanism | What it caught, as the history shows | What it costs | Verdict |
|---|---|---|---|
| `Target SHA` | every arm of the check rests on it; the proof's replay cases clone at it | one row | **stays** |
| The `Verdicts` table in its five columns | the findings themselves; the proof's `truth-` graders read its rows | one cell held a finding's whole account and a `\|` in it broke the row (#189); three kinds of row shared one table, so a reader had to sort them by a mark; four of this item's six rounds found a spelling the sorting let through | **leaves** (reframed after round 6). A finding is a `###` section of `## Findings` with four labelled lines; a confirmation and a not-judged item are rows of their own sections. The `truth-` graders read the finding's `Location:` line (§*The proof*) |
| `Executed probes` and `Paste-ready fixes` | contract §4 in the record; the smith pastes | the warden writes them anyway | **stay**, as `## Probes` and as the fenced block inside each finding, where the fix pass reads it beside the finding it answers |
| The emoji vocabulary 🔴 🟡 🟢 ❓ as record fields, the `#` cell and the bare-integer id | a severity a person reads at a glance | read by the check to tell a finding from a non-finding, which is the one fact rounds 1, 2, 5 and 6 each found read wrong once (a severity in the Finding cell, a 🟢 or ❓ cell over an `open`, `confirmed` on a 🔴 row, `**🔴 1**`) | **leaves the record** (reframed after round 6). `Severity: blocks merge` or `fix or justify` is for people, and the finding's number is its heading's; the check reads neither |
| `round-N-report.md` beside `round-N.md` | nothing: the record was the report's tables copied | 19 files, 303 KB of 564 KB in 0.22.0; half of what a later round inherits | **leaves**; the warden writes `round-N.md` |
| `round_record.py` (`new`, `close`, `notes`, `seal`), `bin/round-record{,.cmd}` | wrote the copy and the derived fields, applied the fix table, counted the notes | 5,596 lines, 35 test modules, the generator's refusals at the keyboard (#503, #866 in `docs/round-record-spec.md`, `read`) | **leaves whole** |
| `Pass` box | whether a row is still open | a box that restates the table | **leaves**; the check reads the rows: no `open` verdict on a ready pull request |
| The reading of a verdict row — which rows are findings, and which words close one (`chain_check.py#verdict_table`, `#verdict_of`, `#open_findings`, `CLOSES_BY`, `EVERY_CLOSE`, `FINDINGS`, `BLOCKING`, `SHOULD`, `FINDING_WORDS`, `CLOSED_WORDS`, and before phase 5a `#severity_of`, `NOT_FINDINGS`, `FINDING_CLOSES`, the `#` column found by its header) | nothing in the records it read: no 🔴 or 🟡 row of the 36 records at round 2 read a 🟢 or ❓ row's word (round 2's probe, `executed` by the warden). What its four versions carried was the hole each round found: round 1's let a severity outside the first cell hide an `open`; round 2's let a 🟢, ❓ or ⬜ `#` cell hide one; phase 5a's let a 🔴 row close `confirmed`, which rounds 3, 4 and 5 gave the sealer to catch and each found that backstop short; phase 5c's read the mark with `startswith` on the raw cell, so `**🔴 1** … confirmed` passed (round 6's 🟡 1). Each repair read the same cell by one more rule, and every spelling the rule did not know fell to the passing side | four readings in six rounds, three reframes, two word sets, and a rule the documents restated per round | **leaves whole** (reframed after round 6). The decision is what the check decides: whether every finding has an answer. So the record gives it that fact in one line it can read without sorting anything — `Verdict: <value>` inside a finding's section — and the check refuses whatever it cannot read (§*What a round records*). The emoji marks, the mixed table, the word sets per mark and the old generator's words `withdrawn`, `not a defect` and `agreed, fixed` go with the reading; nothing reads an old record, so nothing needs them. **How it errs, stated**: it reads a line's shape, so a `fixed <commit>` whose commit is on the branch and touches nothing of the finding passes the check; the sealer's step 3 reads the commit against the `Location:`. A finding the warden wrote outside `## Findings`, or without a `###` heading, is not a finding to the check: the template, the warden's definition and the eval's shape grader hold that shape, and a section with no `Verdict:` line is refused rather than passed |
| `Fixes checked by`, `Needs a fix`, `Written late` | the last fixes read by nobody (the verifying-round rule, #161 `read`); the record committed after its fixes. `Written late` read `no` 19/19 | three rows derived from facts the check can read | **the fields leave; the rule stays** as one check: the last record's `Target SHA` is HEAD, or every commit after it touches only `seal/specs/<id>/`. A round after the last fix pass is therefore owed, as today |
| `Fix range`, `Contract changes`, `New units`, the depth refusal, inherited coordinates | the verifying round's finding surface; a fix pass adding a unit nobody reviewed (#194, #211, #366 `read`). `Contract changes` read `none` 17/19; `New units` named in 9/19 | AST walks of the fix range in `round_record.py`, 198 s of tests for the floor and depth alone | **leave**; the warden's definition states that a verifying round reviews the whole fix diff, new units included, and the fix range is written in `Target SHA` |
| `Fix of a fix` count and its `second` stop | fired three times in 0.22.0 and sent #929 and #931 back to the framer; what it caught was fixes chasing one mechanism's edge cases, which `CLAUDE.md`'s tenet now states as a rule every agent reads | the count needs the fix range, the units and the depth above; 365 s of tests; four reframe spawns | **the judgment stays, the count leaves**: the warden marks a finding `fix of a fix` in its Finding cell; a round carrying the mark gets no fix pass, at any round of the run, and the work item returns to its framer, who redraws the frame (`Reframed … after round N.` under the mark; `questions.md` Q1, the owner, 2026-10-15). Checked by nothing; the sealer reads the records |
| `Loses a record or crashes` floor, the round cap, the one reopening | #161's 15-round run (`read`); `yes` 2/19 in 0.22.0; no 0.22.0 run reached the cap — the stop above ended them | three rules, 65 + 45 + 117 lines of spec, their arms in the check | **one orchestrator rule replaces them** (`skills/code-review/orchestration.md`): a run has three finding rounds by default, extended one at a time while the latest round found fewer findings than the one before and none is a fix of a fix, each extension one line in that round's record (`questions.md` Q1, the owner, 2026-10-15); at the cap every open finding takes the filing ladder and reads `deferred <home>`. Checked by nothing at the pull request; the sealer and the person reading it see the count |
| ⬜ notes, `notes --at`, *a note closes once* | prose quality in records and definitions | carried open through every later record (3 → 15 in #929); a command at the run's end; a `chain_check` arm | **leaves** with the severity |
| `Ran by` | nothing that changed an outcome | one row and an arm | **leaves**; `routing.md`'s free text names the models, as it does today |
| `Broad gate` cell, and `broad-gate.md` where the work went straight to the pull request | the broad run happened at HEAD | two homes for one fact, `round_record.py seal`, `kept_broad_gate`, `seal_home` | **one home**, `broad-gate.md`, written by `broad-gate --record` on both routes |
| `PR` field, `## What this round was asked`, `## Inherited coordinates`, `## Deferred` | nothing a reader cannot see in the pull request, the spawn prompt or the earlier records | copies | **leave**; a deferral is a verdict word |
| `tests-todo.md` | a prescribed test | written by 0 of 4 items; a hook and three documents read it | **leaves**; a prescribed test is a 🟡 row and closes `fixed <commit>` |
| `hooks/review-history-guard.py` | a reminder on `gh pr review` and `gh pr merge`; nothing recorded a catch | 303 lines, 6 test modules | **leaves**; the check at the pull request is the enforcement |
| `chain_check.py`'s remaining arms | the declaration's vocabulary; a declared framer left `spec.md`, `plan.md` and the mark, and a `Reframed` line's author matches; a declared chain left at least one record, every verdict is closed, the last record is at HEAD; `broad-gate.md` and `guarantee.md` name HEAD on a ready pull request; a draft prints and fails nothing | one module, this repository's tests for it in one file (#942) | **stay**, rebuilt |
| `pact_notices`, `fragment_left_behind` and the arms over removed things | the pact change records left in 0.22.0 (#944) | dead reads | **leave** |
| `docs/round-record-spec.md`, `docs/review-chain-spec.md`, `docs/review-handoff-protocol.md` | the rules above, and their history | 2,725 lines, 63 test modules between them | **leave**; one `docs/the-review-record.md` states the record, the run's four rules (the verifying round, the cap, the `fix of a fix` stop, the filing ladder) and the handoff rule (coordinates, never prose), each with its `Enforced by:` or its link |

### How the change reaches users of the plugin

It ships in 0.22.0. A repository's `hygiene.yml` copy runs the same command,
`python3 skills/code-review/scripts/chain_check.py --baseline …`. The check
judges only the work items a pull request's own commits declare or change, so
a record a merged pull request left behind is read by nothing again, whatever
its shape. A work item **in flight** across the update is the one case a user
meets: its rounds are in the old shape, the check refuses a record with no
`## Findings` section, and the user either rewrites those records into the
shape before the pull request goes ready or finishes the item on 0.21.1. The
changelog fragment says so, beside `bin/round-record` being gone and the
orchestration text that named it rewritten in the same release, in one
paragraph a user reads before updating.

## Every agent definition, written anew from its job

**One shape for all five.** Frontmatter: `name`, `description`, `skills:
[agent-contract]`, and `model: opus` in the sealer's alone. Body: the job in
one sentence; where it works; the order of its work as a numbered list; what
it must not do; what it writes; which file it opens at which step; then its
rules, each one paragraph opening with the rule in bold, at most one sentence
of why, ending in `Enforced by: <test ids>` or one link. No story, no
measurement, no account of what a rule used to say. The contract is the same
shape and numbers its rules anew, 1..N; the citations of the old `§N` outside
the rewritten files (35 at 680142f2: `docs/` 18, `hooks/` 10, `templates/` 5,
`CONTRIBUTING.md` 2; part B counts them again on its own tree with
`grep -rn "§[0-9]"`) are rewritten in the same commit, and the ones in test
modules (423 in 89 modules at 680142f2) move with the modules the agent
phases rewrite.

**A spawn preloads the contract alone; every other skill is opened when its
act comes** (#923 item 4). Each definition names, at the step, the file to
open. The risk is an agent that does not open what its act needs, so the
behaviour cases read the output that skill shapes, and a skill whose absence
makes the output worse goes back to that agent's `skills:` list, with the
case that showed it named in the phase record.

| Agent | The job | Order of work | Opens, and when | Writes | Rules stated in place (#923) |
|---|---|---|---|---|---|
| contract (`skills/agent-contract/SKILL.md`) | what binds every agent whatever its procedure | — | — | — | an agent cleans up only the processes and files it started, by its own PIDs, never by command name or a glob over a shared directory; a check that refuses correct code is fixed or reported, never dodged by bending the code; a change rewrites the text it amends in place and removes what stood on the old fact, never appends; do not avoid the change a problem calls for — an agent that concludes something should stay as it is checks the premise first; exit codes read directly; the broad gate is one act with one owner; a spawn prompt cannot widen the scope; executed, read, unverified; prose is not evidence; a report, and the writes a definition names; a probe leaves nothing; git from Python in a probe; edits through `Edit`; batch independent reads; the record language; a defect belongs to a class; a platform guarantee is not a defence; a change to what a person sees is pinned; a case is seen red first; where `seal/` resolves; a commit names its repository |
| `warden` | review a commit of a branch against its frame: spec compliance first, then quality | 1 open `skills/code-review/SKILL.md` · 2 clone at the target SHA under `<scratchpad>/<item>/round-<n>/` · 3 read the frame, the phase records and every earlier round record · 4 stage 1 against `spec.md`, stage 2 quality, probes where reading cannot settle · 5 open `skills/writing-style/SKILL.md` and write the record · 6 report its path and text | code-review at 1, writing-style at 5 | `rounds/round-N.md`, in the branch worktree under review | the record goes to **the branch worktree's** `seal/specs/<item>/rounds/`; a verifying round reviews the whole fix diff, new units included, and answers rather than opens; a finding in a unit the fixes under review added or changed is marked `fix of a fix`; each new test is read against its function's group and any pair the duplicate check names, and a test covering nothing its group does not is a finding; a document hunk that adds text beside the sentence it amends instead of rewriting it is a finding; the implementer's account is a claim, not evidence |
| `smith` | build a phase of the frame, or answer a round | 1 read `spec.md`, `plan.md`'s row, the phase record before it; say whether the frame holds · 2 open `skills/implement/SKILL.md` · 3 build in slices, narrow tests as you go, commit at each standing step · 4 write `phases/phase-N.md`; a fix pass instead writes the `Verdict:` and `Answer:` lines of each finding of the round it answers · 5 open `skills/writing-style/SKILL.md` and hand back | implement at 2, writing-style at 5 | code, tests, `phases/phase-N.md`, `overview.md`, `changelog.md`, two lines per finding it answers | a new test starts from its group — read the function's tests first, extend one where you can, and say in the hand-back which case the group did not cover; a check refusing correct code is the check's defect; a fix pass adds no mechanism; a removal the frame did not name is an `overview.md` divergence |
| `framer` | draw the frame before anybody builds | 1 skeleton `spec.md` · 2 gather widely · 3 open `skills/implement/SKILL.md` §1–§3 and judge what the tree answers · 4 `spec.md`, `plan.md`, `questions.md` · 5 open `skills/writing-style/SKILL.md` and report | implement at 3, writing-style at 5 | the three files; the mark and a `Reframed` line | do not avoid the change a problem calls for: an alternative that replaces a structure is weighed as an equal of one that keeps it; a question the tree can answer is not a question; nobody is asked; the frame names what the work removes |
| `sealer` | the final, independent guarantor, above | the five steps above | none — its procedure is its definition | `guarantee.md` | its reference is the issue and the tree; it re-judges neither design nor quality; a claim is re-run, not read |
| `scribe` | facts about an original, with coordinates and no verdict | 1 open `skills/legacy-parity/SKILL.md` · 2 read `seal/parity.md` and the original · 3 report facts with coordinates, each labelled | legacy-parity at 1 | nothing | an absence carries its search; constraints are read, not probed |

The size a definition reaches is written in its phase record and the release
table and held by no ceiling. The estimate, from 20–35 rules at ≤ 8 lines plus
one fence: 5–9 KB a definition, 6–8 KB the contract, so a spawn's preload falls
from 95–101 KB (warden, smith, framer, `executed` with `payload_meter`) to
about 12–17 KB. The proof's rule 4 is what judges it.

## The proof — outcome not worse, cost lower

The harness is phase 1's (`evals/`): outcome graders only, cost read from
each run's trace, `noninferiority.py compare` writing the record and
`tests/test_a_rewritten_definition_proved_non_inferior.py` recomputing it.
What this frame changes in it:

- **The warden's shape graders point at `rounds/round-N.md`**, and the two
  that read the `Needs a fix:` and `Loses a record or crashes:` lines leave
  with those fields. After round 6 the shape grader reads the `## Findings`
  heading and a `### <n>. ` section with its `Verdict:` line, and a `truth-`
  grader reads a finding's `Location:` line for the path and unit or line
  (`evals/scripts/behaviour.py`, `replay_targets.py#truth_pattern`,
  `seed_defects.py`), in place of the table row they read. Rule 3 reads
  shape graders on the new side only, since the old side's shape is the old
  record's by construction; `reach-` graders stay at 100 % on both sides.
- **The sealer's three cases are redesigned for the guarantor**: a sound
  fixture item (verdict `sound`, `guarantee.md` written, nothing else
  changed); a pull request body claiming a change the tree does not carry
  (`not sound` naming the body); a phase record claiming `seen red` for a
  case that is green against the old code (`not sound` naming the claim). The
  old sealer's job was the broad run, so no baseline comparison applies; the
  sealer's proof is outcome on these cases, with its cost written and not
  judged (`questions.md` Q2 names the first measurement).
- **The baseline is taken once, on the tree where it applies.** Part A
  (`plan.md` §*The split*) changes no preload but the sealer's, whose cases
  are new, so part A takes no baseline. Part B's baseline is taken as its
  first act, on the tree after part A merges, for the warden, smith and framer
  sets; the scribe has no case and is proved through the contract phase's
  other three.
- **The pass rule** per agent, pooled over its cases × N = 2 runs a side:
  (1) recall of truth findings, new ≥ old, a deficit of one noise; (2) false
  findings, new ≤ old + 0.05; (3) shape graders 100 % on the new side, reach
  100 % on both; (4) **cost falls** — preload bytes below the old, pooled
  tokens read and spend ≤ 1.1 × the old; (5) a side cut by `--max-cost-usd`
  or a timeout is no result. The fix on a failure is to restore the rule the
  output lost, in the shape; the bar never moves.
- **The proof is smaller than what it proves.** Part B's runs: the baseline
  ≈ 38 runs; the contract phase all four sets; the warden phase its set; the
  smith and framer phases theirs; the close re-runs an agent only where its
  preload changed after its last passing record. ≈ 120 runs and ≈ $150 over
  the item (Q6 of the earlier frame, accepted; the suite build measured one
  warden replay at ≈ $2.5 and 300–500 s), on the orchestrator's account. CI
  runs none of it.

## Scope

**In — part A, this work item** (`plan.md` phases 3–5 and the repairs 5a–5d):
the review record and its checker; the broad gate's one record file; the sealer as guarantor with its
template, its check arm and its three cases; `docs/the-review-record.md` in
place of the three specs; the record sections of
`skills/code-review/orchestration.md` and the rows of
`skills/implement/orchestration.md`'s delivery table that named removed acts;
`docs/the-agent-set.md`, `docs/the-record-layout.md` §*seal/specs/<work-item-id>/*
and `docs/the-broad-gate.md` rewritten where this item makes a sentence of
them false; the warden's shape graders; the tests sorted into #942's layout
with every deleted module's guard named; the changelog fragment.

**In — part B, a second work item under #923, begun after part A merges**
(`plan.md` phases 6–9): the contract and the five definitions written anew to
the table above, the `skills:` lists cut to the contract, the preloaded skills
(`code-review`, `implement`, `writing-style`, `legacy-parity`) rewritten to the
shape where an agent opens them, the test modules that pin their text
re-pointed or removed with a row, each phase proved on its agents' cases
against the baseline. Part B's `spec.md` cites this file's §*Every agent
definition* by path and adds nothing to it: the agents are written once,
against the record part A built.

**Out, and whose.** `skills/verify/SKILL.md`, `skills/settle/`, the small
skills, `templates/` other than `sdd-round.md` and the new `sdd-guarantee.md`,
`CONTRIBUTING.md`, `CLAUDE.md` — #940. `docs/` other than the files named
above — #941. The agent-lifetime rule, the folding rule, the process archive
— #945. The test suite's own layout beyond the modules this item writes or
deletes — #942. The sealer's stamp (`hooks/sealer-stamp.py`) keeps drawing the
gate's panel; whether a row of it carries the guarantor's verdict is a frame
for a later item. The work item records under `seal/specs/` are history by
design.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a round is one file | a warden reviews a fixture branch | `rounds/round-1.md` exists in the branch worktree with `Target SHA`, `## Findings` holding one `###` section per finding with its `Severity:`, `Location:` and `Verdict:` lines and its fenced fix, `## Confirmations`, `## Not judged` and `## Probes`; no `round-1-report.md`; the warden eval's shape graders pass on it |
| S2 the fix pass completes the record | a smith answers round 1 | every finding's `Verdict:` line reads `fixed <commit>`, `answered` or `deferred <home>` and its `Answer:` line is filled; no other line of the file changed (`git diff` of the record shows only those lines) |
| S3 the check reads one line per finding, and refuses what it cannot read | a record whose `## Findings` holds a finding at `Verdict: open`; one whose `Verdict:` value is outside the four shapes (`confirmed`, `Fixed abc1234`, `fixed` with no commit, `fixed abc1234.`, `deferred` with no home, `**fixed** abc1234`, `verdict: open`); a finding with no `Verdict:` line, or with two; a finding whose only `Verdict:` stands inside its fenced fix; a `Verdict:` line under `## Confirmations`; a record with no `## Findings`; a `fixed <sha>` naming a commit HEAD does not descend from; pull request not a draft | `chain_check.py` exit 1 for each, naming the record, the line and the finding's heading, and saying which of the four shapes a value would have to take; a draft prints the same and exits 0. A record whose findings all read `fixed <commit on the branch>`, `answered` or `deferred <home>`, and one with an empty `## Findings`, pass. `Severity:` is read for nothing: a finding at `Severity: anything` and `Verdict: answered` passes (T25–T28) |
| S4 the last fixes are read | the last record's `Target SHA` is behind HEAD by a commit touching a file outside `seal/specs/<id>/` | exit 1 naming the commit and *a verifying round is owed*; HEAD moved only by record commits passes |
| S5 the broad gate has one home | `broad-gate --record` on a green run, either routing answer | `seal/specs/<id>/broad-gate.md` reads `<sha> against <base>`; no `Broad gate` row anywhere; a ready pull request whose file names a commit other than HEAD fails |
| S6 the sealer guarantees | a sound fixture item with a pull request body | `guarantee.md` with the five sections and `Verdict: sound`; nothing else in the tree changed; the report labels every claim |
| S7 the sealer catches a story the tree contradicts | a pull request body claims a removal the tree still carries; a phase record claims `seen red` for a case green against the old code | `Verdict: not sound — <the claim>` naming the party and the coordinate, once per case |
| S8 the sealer's verdict gates | `guarantee.md` reads `not sound` or `undecidable`, or names a commit other than HEAD | exit 1 at a ready pull request naming the file and the verdict |
| S9 the `fix of a fix` stop is a judgment | a warden's record marks a finding `fix of a fix`, in any round of a run | the orchestration text says no fix pass runs and the work item returns to its framer, who redraws the frame; `chain_check.py` reads nothing of the mark; the sealer's parties check names it |
| S10 nothing kept beside the tree | after phase 3 | no `round_record.py`, `bin/round-record{,.cmd}`, `review-history-guard.py`, `tests-todo.md` reader, `Fix range`, `Contract changes`, `New units`, `Fix of a fix`, `Needs a fix`, `Loses a record`, `Written late`, `Ran by`, `Fixes checked by`, `⬜`, `notes --at` outside `seal/specs/` and `changelog/` (`grep -rn` over the tree) |
| S11 nothing reads an old record, and the check judges only what the pull request carries | a work item another pull request merged, its records in the old shape; a pull request whose own commits declare or change one work item | `chain_check.py` reads the records of the declared item alone and never opens the other items' `rounds/` (`TestMain`, the fixture tree holding a second item with an old-shape record); an old-shape record under a declared item is refused by name (S3). `.github/scripts/release_seal.py#chain_counts` and `broad_gate.py#rounds_rows` count `deferred` findings through the check's reader and report a record they cannot read as *not read*, never as 0 |
| S12 the suite is lighter | after phase 3; after phase 5a | `.test_durations` summed over the modules that name `chain_check`, `broad_gate` is below 1,500 s (from 4,553 s); the deleted modules' guards listed one line each in `phases/phase-3.md`. After phase 5a the file holds no entry for a case the suite does not collect: `bin/test tests -q -k test_the_durations_file_prices_the_suite` exit 0, and `release_report.py#suite_seconds` sums the file as it is |
| S13 one spec for the record | after phase 3 | `docs/the-review-record.md` exists, every rule paragraph ending in `Enforced by:` or a link, `rules --check` exit 0; the three old documents are gone and no file names them |
| S14 the agents preload the contract alone | part B | every `agents/*.md` `skills:` list is `[agent-contract]`; `payload_meter --agent <a>` shows two files in the agent share |
| S15 an agent opens its skill at the step | part B | the behaviour cases of each agent pass on the new side; a case that reads a skill-shaped output (the warden's findings format, the smith's phase record) is named per agent in the phase record |
| S16 a rewritten definition is proved not worse | each part B phase | `evals/<agent>-phase-N.md` with `Verdict: pass`; the record test green |
| S17 no rule is lost unseen | each rewritten file | the phase record lists every bold-led rule of the old file with its new coordinate or its removal and why; every test that pinned a sentence is green on the new one or removed with a row |
| S18 the contract numbers anew | part B | `skills/agent-contract/SKILL.md` rules 1..N in order; no `§` citation outside it names a number it no longer carries (`grep -rn "§[0-9]"`) |
| S19 nothing asks a person | the whole change | no `AskUserQuestion`, no `input()`, no new prompt; the eval scores itself; the sealer's `undecidable` is a written question, not a stop mid-run |
| S20 every statement of the record's shape is the new one (phase 5d; the severity-keyed rule of phases 5a–5c is history) | after phase 5d-ii | `git grep` outside `seal/specs/` and `changelog/0.*.md` for `## Verdicts`, `Paste-ready fixes`, `Executed probes`, `verdict_table`, `open_findings`, `CLOSES_BY`, `five-column`, `Grounds` cell, `#` cell, `🔴 or 🟡` and `bare-integer id` finds nothing; `templates/config.md` §*What no row governs* lists the new literals and `tests/test_the_pull_request_language_is_the_repositorys.py::test_the_exclusion_list_holds_every_string_a_checker_matches` holds them to the check's constants; `bin/rules --check` exit 0 with every `Enforced by:` naming a test in the tree; `agents/sealer.md` step 3, `templates/sdd-guarantee.md`'s comment and `docs/the-review-record.md` §*The guarantee* keep the one-list design (T22, T23 unchanged) |
| S21 a number a reader acts on names its moment or goes (narrowed in phase 5c) | the shipped surfaces this item writes: `changelog.md`, and every `docs/` sentence this item rewrote | every figure in them is a measurement naming its commit, round or tag, a bound a named check holds the tree to, or gone (§*A number in this frame*). The frame's three documents are read at 680142f2 (`plan.md` §*Technical context*) and the builder's two at the commit each sentence or phase record names; a figure there is history at that moment, not a finding, and no agent reads it against the tree |

## Data & interfaces

`templates/sdd-round.md`: the shape under §*What a round records*, one
comment over `## Findings` documenting the four labelled lines, the four
`Verdict:` values, the two severities and the `Fix of a fix:` line, and one
line each over `## Confirmations` and `## Not judged` saying what goes there.
`templates/sdd-guarantee.md`: `| Field | Value |` with `Target SHA`,
`Broad gate`; `## Claims re-run` (`| Claim | Source | Command | Result |`, its
comment reading *one row per act of `agents/sealer.md` step 3, whatever the
act, and one per thing the act checks*, `Result` `holds` or `does not hold —
<what came back>`, and naming no act); `## The parties` (`| Party | Says |
Agrees with | Disagrees with |`);
`Verdict: sound` · `not sound — <what>` · `undecidable — <question>`, one line,
and an `Answered <date> by <who>: …` line under it where the owner answered.
`skills/code-review/scripts/chain_check.py`: `main(argv)` with `--baseline`,
`--root`, `--worktree` as today; arms `declaration`, `frame`, `records`,
`broad_gate`, `guarantee`; exit 0 · 1 naming `path:line: why` · 2 unreadable;
a draft prints every arm and exits 0. The `records` arm reads each record
through one reader, `findings(reader, lines, rel)`: the one `## Findings`
section (`FINDINGS_HEADING`), split at its `### ` headings, each section
holding exactly one line matching `^Verdict: (.*)$` (`VERDICT_LABEL`), the
value read by `verdict_of(value)` as `OPEN`, `FIXED` with its commit,
`ANSWERED` or `DEFERRED` with its home (`deferred_home`, `issue_of` kept for
`release_seal.py` and the panel), else `None`. Every `None`, every section
with no or two `Verdict:` lines, every `Verdict:` line outside a section of
`## Findings`, and a missing or doubled `## Findings` is an error the arm
names by path, line and the finding's heading, and a `FIXED` whose commit
HEAD does not descend from (`is_ancestor`) is refused the same way; on a
ready pull request an `OPEN` finding fails too. Nothing of a record's
`Severity:`, `Location:` or `Answer:` is read. The reader strips fences and
comments first (`reader.readable`), so a `Verdict:` inside a fix block is
not a line. `skills/verify/scripts/broad_gate.py`:
`--record <item>` writes `broad-gate.md` (`<sha> against <base>`, newest first,
earlier runs kept) on both routing answers; `round_count`, `sealed_record`,
`kept_broad_gate`, the `round_record` import and `round_record.seal_home`'s
call leave; `seal_home`, the root resolver, stays; the panel and the stamp
values are unchanged, so `rounds_rows`, which draws the panel's `rounds` row,
stays and counts `DEFERRED` findings through `chain_check.findings`, a
record the reader refuses adding nothing. `.github/scripts/release_seal.py#chain_counts`
counts the same way and leaves `deferred` *not read* for such a record.
`agents/sealer.md`: frontmatter `model: opus`; step 3 is the one list of the
sealer's acts (§*The sealer*), three of them, the second reading each
finding's `Verdict: fixed <commit>` against its `Location:`.
`docs/the-review-record.md`: the record, the four run rules, the handoff
rule, the sealer's check, each with `Enforced by:`; §*The round record*
states the shape, the four values and the two severities; §*What the check
reads at the pull request*'s records paragraph states the one line, the
fail-closed reading and how it errs, its `Enforced by:` the check's pins
alone; §*The guarantee* points at `agents/sealer.md` step 3 and step 4 for
the acts and lists none. `templates/config.md` §*What no row governs* lists
the literals the check reads — `Target SHA`, `## Findings`, `Verdict:`,
`open`, `fixed`, `answered`, `deferred` — and the labels the parties and the
eval graders read, `Severity:`, `Location:`, `Answer:`, `Fix of a fix:`, the
`## Confirmations`, `## Not judged` and `## Probes` headings; the old
generator's words leave the list. `evals/scripts/behaviour.py`: the shape
grader `shape-findings` reads `^## Findings` and the first `^### \d+\. `
section's `^Verdict: ` line; `replay_targets.py#truth_pattern` and
`seed_defects.py` emit `^Location: .*<path and unit or lines>`; the nine
warden cases and the three sealer cases are regenerated through
`rule_cases.py`, `replay_targets.py --case` and `seed_defects.py --case`,
and `rule_cases.py#SEALER_ROUND` is the new shape.
`skills/code-review/orchestration.md`: §*the run ends
with a verifying round*, §*the cap*, §*a fix of a fix*, §*the pull
request opens before round 1*, §*verify before posting* rewritten to the
record above; §*a note closes once*, §*a fix pass adds the unit*, §*then say
who checked them*, §*and name the fix surface*, §*and say what ran the
round*, §*and commit the record before commissioning the fixes* removed with
the mechanisms; `skills/implement/orchestration.md` §*which of these acts runs
itself*: their rows go. `skills/settle/scripts/settle.py`: the `tests-todo.md`
reading leaves. `tests/`: `test_chain_check.py` and `test_broad_gate.py` in
#942's layout (one file per module, a group per function, a success and a
failure case each); `test_the_sealer_guarantees.py` for the template and the
arm; the 70 modules sorted — kept where they test the gate's run and panel,
deleted where they tested a removed arm, each deletion's guard one line in the
phase record. `evals/behaviour/sealer/`: the three cases above, generated by
`rule_cases.py`. `evals/scripts/noninferiority.py#verdict`: rule 3 as above.
`.github/workflows/hygiene.yml`: the step's command unchanged. `hooks/`:
`review-history-guard.py` leaves and `hooks.json`'s dispatch of it; `routing.py`,
`config.py`, `root-migrate.py` keep their path constants where they still name
a live file.

## A number in this frame names its moment or its bound

Reframe after round 4, narrowed after round 5. `CLAUDE.md` §*The rule a
mechanism is kept against*: *nothing is kept beside the tree to stay in step
with it, such as a stored count*. Rounds 3 and 4 each found a count in this
item's documents that the commits between them had made false, and round 4's
was a count the fix pass for round 3 had itself just corrected. The cause is
the kind of sentence, not the arithmetic, so the frame says what kind a
figure may be.

**The rule is about what a reader acts on, and that is the shipped surface.**
A figure in `changelog.md`, or in a `docs/` sentence this item rewrote, is
one of three things, and its sentence says which:

| Kind | Example | What happens to it |
|---|---|---|
| a measurement at a named moment — a commit, a round's probe, a tag | *6,153 lines at ce448bbe*; *301 entries (`rounds/round-2.md` 🟡 2)* | history; it stays and is never recounted |
| a bound a named check holds the tree to | *under `STALE_SHARE`*, held by `test_the_durations_file_prices_the_suite`; S12's *below 1,500 s* | the bound and the check are stated, not the current value |
| a count of what the tree holds now, with no moment named | *the 226 collected cases with no price*; *the file now holds 7,348 entries*; a *Lines after* column | leaves — replaced by the bound, by the command that computes it, or by nothing |

**The work item's own documents are each a reading at a moment, and a
figure in them is history, not a finding** (reframe after round 5; round 5's
🟡 2 read S21 as it then stood against `questions.md` and `plan.md` and found
five sentences short of its letter that nobody acts on). `rounds/round-N.md`
and `phases/phase-N.md` are moments by construction. The frame's three,
`spec.md`, `plan.md` and `questions.md`, were read at 680142f2 (`plan.md`
§*Technical context*), and a figure in them that names no other moment is
that reading's — a planning figure, which part B's phases count again on
their own tree where a row says so. The builder's two, `overview.md` and
`changelog.md`, name the commit or the phase record each figure was taken at
(phase 5b). A sentence that is wrong at its own moment is still a 🟡; a
sentence that was true at its moment and is not true at HEAD is not. The
figures phase 5b listed as the framer's to rewrite (`phases/phase-5b.md`
§*Where the frame does not hold*) are of the second kind, and the one of them
whose sentence named a moment nowhere, `questions.md`'s *36 records*, now
names round 2's probe.

Enforced by: nothing — a reading that sorts figures by their sentences is a
report, not a gate (`CLAUDE.md`). Each round's warden reads the five
documents; the sealer reads `spec.md`, `plan.md`, every phase record, every
round record and `changelog.md` in its step 2 (`agents/sealer.md`), and
`questions.md` and `overview.md` only inside the diff. Its step 4 compares
the parties' stories; it counts nothing against the tree.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the record generator | `skills/code-review/scripts/round_record.py` (5,596 lines), `bin/round-record`, `bin/round-record.cmd` | the warden writes the record and the smith fills two cells; nothing is derived |
| the reviewer's separate report | `rounds/round-N-report.md` as a file kind; `agents/warden.md` §*Report*'s path | the record is the report |
| eleven fields of the record | `templates/sdd-round.md` rows `Written late`, `Ran by`, `PR`, `Broad gate`, `Fixes checked by`, `Fix range`, `Contract changes`, `New units`, `Fix of a fix`, `Needs a fix`, `Loses a record or crashes` | §*What leaves* above, row by row |
| four sections of the record | `templates/sdd-round.md` §*What this round was asked*, §*Inherited coordinates*, §*Deferred*, the `## Fixes` table shape | copies of what the pull request, the spawn prompt and the earlier records show; a deferral is a verdict word |
| the ⬜ severity and the notes machinery | `skills/code-review/SKILL.md` §*Findings format* ⬜ line; `round_record.py notes`; `chain_check.py#notes_of`, `#carried_notes`, `#open_notes`; `skills/code-review/orchestration.md` §*A note closes once, at the run's end* | a wrong sentence an agent acts on is 🟡; a sentence in a record is not a finding |
| the chain check's arms over removed fields | `chain_check.py#fix_range`, `#fix_surface`, `#depth_problems`, `#fix_of_a_fix`, `#fix_of_a_fix_count`, `#floor_walks`, `#stopping_floor`, `#written_late`, `#ran_by`, `#runner_problem`, `#checked_by`, `#pass_boxes`, `#pass_checked`, `#says_reopened`, `#cut_runs`, `#pact_notices`, `#fragment_left_behind`, `#direct_seal`, `#stray_records`, `#doubled_grounds`, `#doubled_fields` and what only they call | the five arms of §*Data & interfaces* are what the pull request needs |
| the broad gate's record arms | `broad_gate.py#round_count`, `#sealed_record`, `#kept_broad_gate`-through-`round_record`, the `round_record.seal_home` call, the `Broad gate` cell write | `broad-gate.md`, one home; `#seal_home`, the root resolver the gate reads `config.md` through, and `#rounds_rows`, the panel's `rounds` row that §*Data & interfaces* keeps, stay |
| the review reminder hook | `hooks/review-history-guard.py` (303 lines), its `hooks.json` dispatch, `tests/test_chain_hooks.py`, `tests/test_chain_hooks_hardening.py`, `tests/test_handoff_outlives_the_merge.py` and the cases of three other modules that read it | the check at the pull request |
| `tests-todo.md` | the file kind; `docs/the-record-layout.md` row; `skills/implement/SKILL.md` §5 table row; `settle.py`'s reading | a prescribed test is a 🟡 row |
| the three record documents | `docs/round-record-spec.md`, `docs/review-chain-spec.md`, `docs/review-handoff-protocol.md` | `docs/the-review-record.md`; the handoff rule in the orchestration file |
| the severity-keyed reading of a verdict row (phase 5a) | `chain_check.py#severity_of`, `NOT_FINDINGS`, `FINDING_CLOSES`, the `ID_COLUMN` lookup in `#open_findings`; the `#`-cell rule as `docs/the-review-record.md` §*What the check reads at the pull request* stated it, `templates/sdd-round.md`'s closing comment, `chain_check.py`'s module docstring, `README.md`, `README.ko.md`, `.github/workflows/hygiene.yml` and `templates/hygiene.yml` where they said "no 🔴 or 🟡 row left open", and this item's `changelog.md` sentence | phase 5a replaced it with one reading of the `Verdict` cell; phase 5d removes that reading too, with the table (the rows below) |
| the verdict table and its reader (phase 5d) | `templates/sdd-round.md`'s `## Verdicts` table, `## Paste-ready fixes` and `## Executed probes`; `chain_check.py#verdict_table`, `#verdict_of` as a cell reader, `#deferred_parts`, `#open_findings`, `VERDICTS`, `VERDICT_COLUMN`, `GROUNDS_COLUMN`, `BLOCKING`, `SHOULD`, `FINDINGS`, `CLOSES_BY`, `EVERY_CLOSE`, `FINDING_WORDS`, `CLOSED_WORDS`, `VOCAB`, `MARKER`, `SEPARATORS`, `HOME_MARKS`, `DEFERRED_HEAD_RE`, `OUT_OF_SCOPE`, `NO_HOME`; the words `confirmed`, `out of verified scope`, `withdrawn`, `not a defect`, `agreed, fixed` as verdicts; `tests/test_chain_check.py::TestVerdictTable`, `::TestOpenFindings` (T19, T24), `::TestVerdictOf` as it stands, `::TestDeferredHome` as it stands, `::TestMain::test_the_refusal_names_the_words_that_close_a_row_of_its_mark`, `::TestMain::test_a_record_written_by_the_old_generator_reads` (T13, the corpus run); the table fixtures of `tests/test_broad_gate.py`, `tests/test_the_seal_is_taken_once_by_the_sealer.py` (`VERDICT_HEADER`, `OPEN_ROW`, `record_text`, `deferring_record`) and `tests/test_the_release_seal_is_drawn.py` (`ROUND`); `tests/test_the_pull_request_language_is_the_repositorys.py#ROUND_RECORD_FIELDS` and the constants `_literal_strings` reads; `evals/scripts/behaviour.py`'s `shape-verdicts-table` grader and the `^\| (?:🔴\|🟡) \d+ \|` truth pattern of `replay_targets.py#truth_pattern` and `seed_defects.py`; `rule_cases.py#SEALER_ROUND` and the sealer scaffolds it wrote | §*What a round records*: a finding is a section with a `Verdict:` line, read by `chain_check.py#findings`, and the fail-closed reading is T25–T28; the other readers read through it, and the graders read `## Findings` and `Location:` |
| the emoji vocabulary and the `#` cell as record rules (phase 5d) | `docs/the-review-record.md` §*The round record*'s vocabulary paragraph and §*What the check reads*' open-row paragraph; `skills/code-review/SKILL.md` §*Findings format*'s four-line block, the bare-integer-id paragraph, the Finding-cell paragraph and the Grounds-cell paragraph (#189); `agents/warden.md`'s `#` cell sentences (its ❓ row paragraph and §*Report*'s last two paragraphs); `templates/config.md`'s literal list rows for the headings, columns and words; `README.md:182`'s *no row left open*, `README.ko.md:173`'s 판정표 sentence, the step comments of `.github/workflows/hygiene.yml` and `templates/hygiene.yml`; this item's `changelog.md` first two entries where they state the table and the marks; `docs/the-agent-set.md:56`'s `Enforced by: tests/test_chain_check.py::TestVerdictTable` | two severities for people, `blocks merge` and `fix or justify`; a confirmation and a not-judged item are rows of their own sections; the sentences are rewritten in place to the shape and the `Enforced by:` lines name the new groups |
| the `.test_durations` entries the suite no longer collects (phase 5a) | 301 entries, 345.3 s, for cases this branch removed from modules that still exist (`rounds/round-2.md` 🟡 2, `executed`) | pruned by collection — an entry is live when `pytest --collect-only` collects its id — with the round-trip guard 1b875efc used; nothing re-measured, nothing kept in the tree to do it again. The collected cases with no price — held under `STALE_SHARE` by `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py::test_the_durations_file_prices_the_suite`, and counted here by nothing — are priced by the next refresh from a `tests` run, which `CONTRIBUTING.md` §*Running the checks* owns |
| the second and third list of the sealer's acts (phase 5b) | `docs/the-review-record.md` §*The guarantee*'s list of what the sealer re-runs and confirms; `templates/sdd-guarantee.md`'s comment over `## Claims re-run` listing the row kinds | `agents/sealer.md` step 3 lists the acts and §*The sealer* states them; both files point at step 3 and name no act, so `fixed <commit>` outside `seal/specs/` and `changelog/` stands only in the record's vocabulary (`docs/the-review-record.md` §*The round record*, `templates/sdd-round.md`) and in step 3 (`git grep`) |
| the present-tense counts in this item's living documents (phase 5b) | `changelog.md`'s *Lines after* column and its sentence counting test modules and test lines after the branch; `overview.md`'s *the file now holds 7,348 entries … sums to 3,371.9 s* and its S12 row's figures, each unpinned; the frame's own, rewritten by the reframe after round 4: `spec.md`'s *226 collected cases*, *36 records in the tree*, *35 citations*; `questions.md`'s *226 unpriced cases*, *35 citations*; `plan.md`'s *about 3,372 s*, *about 3,000 of its 6,827 seconds*, *68 K lines* | §*A number in this frame*: a figure names its moment or its bound, or leaves |
| the sealer's duty over a 🔴 or 🟡 row closed by another kind's word (phase 5c) | `agents/sealer.md` step 3's sentences from *Read every 🔴 and 🟡 row of every record* to *the verdict is `not sound`*; `tests/test_the_sealer_guarantees.py::TestDefinition::test_the_sealer_reads_every_red_and_yellow_row_not_only_fixed_ones` (round 3's fix) and `::TestDefinition::test_the_sealer_names_such_a_row_in_the_claims_table` (T21, phase 5b); `docs/the-review-record.md` §*What the check reads at the pull request*'s open-row paragraph from *and a 🔴 row that reads `confirmed` passes the check* to *unless a later round answers it*, and the T21 name in its `Enforced by:`; the clause of this item's `changelog.md` sealer entry from *It reads every 🔴 and 🟡 row of every round* to *unless a later round answers it*; `questions.md` Q8 and `plan.md` Alternative Z's deferral; `plan.md` row 9's fourth sealer case `rule-sealer-closed-by-another-kinds-word`; S20's part-B clause | the check refuses the row (S3, S20): the fix pass's three words are the only answer a finding takes, and `chain_check.py` reads that fact at the pull request. The one-list design of the reframe after round 4 stays as it is, since round 4's finding — a list of the acts in three files stales — holds with three acts as with four: `templates/sdd-guarantee.md`'s comment and `docs/the-review-record.md` §*The guarantee* keep their pointers at step 3, and T22 and T23 keep holding them |
| S21's claim of a reader over five documents (phase 5c) | S21's *the sealer's step 4 reads the five documents against the tree* and the same sentence under §*A number in this frame*; `plan.md`'s and `questions.md`'s *the frame's own three documents were rewritten to it at the reframe*; `plan.md` Alternatives X and Y's verdict clauses naming the sealer as the reader | §*A number in this frame*, narrowed: the rule covers the shipped surface, the work item's documents are readings at a moment, and the sealer's step 2 reads three of the five and its step 4 counts nothing. `questions.md`'s *36 records* names round 2's probe, the one frame-time figure whose sentence named no moment anywhere |
| the chain's test modules on removed arms | of the 70 modules naming the three scripts, every module or case whose subject is a removed field, arm or subcommand — `test_the_fixes_close_the_record.py`, `test_a_fix_of_a_fix_is_counted.py`, `test_the_record_is_generated.py`, `test_the_record_is_held_to_the_floor_and_the_depth.py`, `test_a_record_precedes_the_fixes_it_commissions.py` among them; the full list is phase 3's | the guard of each named one line in `phases/phase-3.md`; what still holds has a case in `test_chain_check.py` or `test_broad_gate.py` |
| the old sealer | `agents/sealer.md` as it stands (*it judges nothing*; the `Broad gate` cell as its one write; Sonnet as its model); `evals/behaviour/sealer/rule-sealer-{green,failing-test,record-open}/` | the guarantor above and its three cases |
| two warden shape graders | `evals/behaviour/warden/*/graders/shape-needs-a-fix.md`, `shape-loses-a-record.md`; the report path in every warden shape grader | the fields are gone; the path is `rounds/round-N.md` |
| the orchestrator rows for removed acts | `skills/implement/orchestration.md` §*which of these acts runs itself*: the rows for the note, the fix surface, `Ran by`, *then say who checked them*, *commit the record before commissioning*; `tests/test_every_orchestrator_act_names_its_delivery.py`'s pins of them | the table reads the headings, so the rows go with them |
| the preload beyond the contract (part B) | every `agents/*.md` `skills:` entry other than `agent-contract` | opened at the step |
| the contract's numbering (part B) | `§1`–`§17` as numbers, and every `§N` citation of them | rules 1..N, every citation rewritten |
| the five definitions and four skills as written (part B) | `agents/{warden,smith,framer,sealer,scribe}.md`, `skills/{agent-contract,code-review,implement,writing-style}/SKILL.md` | written anew; each old rule's disposition in the phase record (S17) |

## Open questions → questions.md

Framed 2026-10-14 by framer, before the build.
Reframed 2026-10-15 by framer, after round 0.
Reframed 2026-10-15 by framer, after round 2.
Reframed 2026-10-15 by framer, after round 4.
Reframed 2026-10-15 by framer, after round 5.
Reframed 2026-10-16 by framer, after round 6.
