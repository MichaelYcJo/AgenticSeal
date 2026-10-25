# Feature Specification: every agent, skill and doc states the current rule only

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* | A mechanism stays only while its history shows what it caught against what it costs. Do not avoid the change a problem calls for: before a fix adapts to a structure, ask whether the structure should change; what exists is a reference, not a constraint. A change rewrites in place and removes what stood on the old fact in the same commit. This frame weighs every field of the review record and every agent definition by it, and keeps nothing because it is there |
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here asks a person mid-run. A check that fails names the file and line; the sealer's one undecidable case goes to the owner as a written question, after the run |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | Phases 3 and 4 remove gates and move checks: cases seen red, the failure direction (the chain check blocks less and reads fewer fields; what it still reads it reads at the pull request as before), a prompt budget of zero, `## Removes` below |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file*, §*seal/specs/<work-item-id>/* | The changelog is a fragment; the table of a work item's files is rewritten in place here because this item changes what the files are |
| `docs/the-agent-set.md` | One contract every agent receives, one definition each; the writer of a contract is not its executor; a subagent asks nobody. Rewritten in place here: the sealer's job changes and the set is derived from the jobs |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The work alters what every spawn reads and what every pull request is checked against, which is the top rung |
| #923's body, rewritten 2026-10-15 by the owner and split on 2026-10-16 | The one source for what was decided: the principle and what this item builds. Where this file and that body differ, the body holds. Since the owner's split of 2026-10-16 the body is part A alone, the review record and the sealer, in 0.22.0; part B — the agents written anew, the rules the rewrite states in place, the proof's two axes, the baseline — is #957, in `release: 0.22.1`, framed on its own after 0.22.0 is installed so old and new rules do not mix in one run. This file frames part A, and names what moved under `## Removes` |
| The owner's ruling of 2026-10-16, on round 7 | A `regression:` line marks a defect a fix pass's own commit introduced. A defect in a phase the framer designed and the owner approved is an ordinary finding of new work, with no `regression:` line, and gets its fix pass. `docs/the-review-record.md` §*The run* states it, pinned by `tests/test_the_rules_have_one_owner.py::test_a_regression_is_a_defect_a_fix_passs_own_commit_made` (`phases/phase-5d.md` §*Round 7 fix pass*) |
| The owner's decision of 2026-10-16, on round 8 | A round names an earlier finding by one of three relations, each a plain English label, and all three are needed now: `confirms: round-<N>#<n>` where the close holds, in `## Confirmations`; `reopens: round-<N>#<n>`, new, on a new finding where the earlier close does not hold — a rejection that was wrong, or a `fixed` commit that did not fix it — and no fix pass's own commit made the defect, an ordinary finding that gets its fix pass; `regression: round-<N>#<n>` on a new finding where a fix pass's own commit introduced the defect. The channel accepts `reopens:` as naming the earlier finding, like the other two, read fail-closed in the same way. Refined the same day: a `regression:` line does not send the work item to its framer by itself; the warden states in the finding's grounds what the frame says, what the fix did and where the defect came from, and the orchestrator routes on that sentence — the frame back to its framer where the fix built what the frame says and the defect is still there, an ordinary fix pass where the fix departed from the frame or the defect came from how the fix was written, and the framer for a second regression on the same unit after a fix-pass route (§*What leaves*'s `Fix of a fix` row states it). Round 8's three findings close `deferred the frame` and this frame takes them together (§*What a round records*, S9, S23, S24, S26, S27; `plan.md` row 5d-v) |
| The owner's decision of 2026-10-16, after round 6 | The round record is designed anew from its jobs and not patched again. What the check read was the old generator's table with fields subtracted and a rule added per round, and the check missed one fact four times (rounds 1, 2, 5 and 6) for one reason: it told a finding from a non-finding by an emoji mark in a table that mixed three kinds of row, and every spelling it did not recognise fell to the passing side. What exists is a reference, not a constraint (`CLAUDE.md`). The rule the new shape embodies — a gate fails closed: input it cannot read is refused, never passed — is `questions.md` Q9's to put into `CLAUDE.md` or not |
| The owner's decisions of 2026-10-16, on the record phase 5d-i built (44ad6eeb) | Six, each written into §*What a round records* and the check's facts below, in place: a `fixed <commit>` touches its finding's location and the check reads it, so the sealer's manual act leaves; the channel between rounds is a fact the check reads, through a reference in one spelling; every label is one lowercase word; the severities are `must` and `should`; no emoji in the record, the template, the findings format or the parties' instructions this item touches; the refusal of an unclosed fence or comment, which 5d-i's smith added, is a check fact here with its limit stated. Then, relayed during 5d-iii and built there: every label and value a plain English word an agent can guess the meaning of — one `target:` line for the field table, a `confirms:` line per confirmation in place of a table, the section optional and two refused, an unconfirmed finding refused at its own heading in its own record, `regression:` for `refixes:`, `rejected` for `answered`. And `questions.md` Q11's answer: a repair outside the tree closes `deferred <where>`, a repair by a commit `fixed <commit>`, and `rejected` means only that the finding does not hold (phase 5d-iv). Frame edits, not reframes: no round stopped the run, so the foot carries no `Reframed` line for them |
| #942 (the test layout) | A test file per shipped module, its tests grouped by function, a success and a failure case per group. The test modules this item writes for the chain check and the broad gate follow it; the modules it deletes are listed by what they guarded, one line each |
| #945 §3 | Round-record inheritance moved here (owner, 2026-10-15); the agent-lifetime rule, the orchestrator's folding rule and the process archive stay there |
| #940, #941 | What an agent opens on demand, and `docs/`, are theirs. This item rewrites a file of theirs only where this item makes a sentence of it false |

## What this work is — a new slate, not a trim

The review chain is designed anew from its jobs, with no loss in what the
work gets right (owner, 2026-10-15): the round record, the check that reads
it, the broad gate's one record file, and the sealer as the final,
independent guarantor. Today's files are a reference, as the old tests are
for #942. No heading, section number or field is kept because it was there.
The earlier frames of this item trimmed files whose structure was the
problem; this one asks of each structure whether it should exist. The agent
definitions written anew from their jobs are #957's (the owner's split,
2026-10-16), and this item rewrites a definition only where it states the
record or the sealer's job (§*The agent definitions this item touches*).

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
| Build: the code, its tests, the phase record; the fix pass | judgment | `smith` | code and tests; `phases/phase-N.md`, `overview.md`, `changelog.md`; the `verdict:` and `answer:` lines of each finding its fix pass answers in the round record |
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
What changes here is the sealer's job and the record that passes between
them; every agent's size and preload is #957's.

## The sealer — the final, independent guarantor

**Its role is: *I verified, independently of the smith and the warden, that
the work before me is sound, and I guarantee it.*** Its reference is the
owner's decision (the issue body) and the tree, never any agent's word or the
orchestrator's summary. It runs after the pull request body and the changelog
fragment are written, so they are audited too. It runs on Opus, the level of
the agents it audits, until #957's evaluation measures it against Sonnet on
the sealer's cases (owner, 2026-10-16): `agents/sealer.md` is the one
definition that pins `model:`.

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
   mutation it says went red. For every `## Removes` row of `spec.md` and
   every removal this release names in its changelog fragments, confirm
   nothing of it stands in the tree. Two acts. Each thing checked is one row
   of `guarantee.md`'s `## Claims re-run`, in the template's shape and no
   other: `Command` the command re-run, `Result` `holds` or `does not hold —
   <what came back>`, and a `does not hold` makes the verdict `not sound`.
   Step 3 states no `Result` shape of its own (reframe after round 5; round
   5's finding 1 was the definition and the template giving two). **These
   acts are listed here and in `agents/sealer.md` step 3, and nowhere else**
   (reframe after round 4): `docs/the-review-record.md` §*The guarantee* and
   `templates/sdd-guarantee.md`'s comment over `## Claims re-run` point at
   step 3 — one row per act, whatever the act, and one per thing the act
   checks — and name no act, so an act added to the definition has a row to
   land in and no second and third list to keep in step. Enforced by
   `tests/test_the_sealer_guarantees.py::TestTemplate::test_the_claims_table_takes_a_row_per_act_of_step_3_and_lists_none`
   and `::TestDocument::test_the_guarantee_section_points_at_step_3_and_lists_no_act`.
   **The sealer reads no finding for whether its verdict is one the check
   accepts, and no `fixed` commit against its finding's location** (reframe
   after round 5, kept after round 6; the owner, 2026-10-16): a `verdict:`
   the check cannot read fails the pull request, and so does a `fixed`
   commit that is not on the branch or touches no path the finding's
   `location:` names (§*What a round records*, S3, S22). The duty rounds 3,
   4 and 5 each repaired — name such a row, give it a home, give the home a
   shape — left in phase 5c, and the act *touches the location it fixes*
   leaves in phase 5d-ii, with its sentences in this file, the definition and
   `docs/the-review-record.md` (`## Removes`). Enforced by
   `tests/test_the_sealer_guarantees.py::TestDefinition::test_step_3_holds_two_acts_and_reads_no_location`
   (T40).
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
| the warden | names the commit it reviewed, and leaves findings — what is wrong, where, why it matters, a paste-ready fix — and the probes it ran | the `target:` line; `## Findings`, one `###` section per finding; `## Probes` |
| the smith's fix pass | answers each finding: the fixing commit, a rejection with its grounds, or where it was deferred | the finding's `verdict:` line and `answer:` line, a coordinate it may append to `location:`, and nothing else in the file |
| the next round's warden | reads the earlier findings and their answers, confirms each that truly closed, reopens one whose close does not hold where no fix pass's commit made the defect, names a regression where a fix pass's own commit introduced the defect, and notes what it could not judge | a `confirms:` line per entry of `## Confirmations`, and the `reopens:` or the `regression:` line of a finding, each naming the earlier finding as `round-<N>#<n>`; `## Not judged`; earlier files are never edited or deleted |
| the check at the pull request | four facts — is any finding without an answer; does each `fixed` commit sit on the branch and touch its finding's location; does the next round confirm, reopen or name as a regression every finding the fix pass closed `fixed` or `rejected`; is the last record at HEAD — and the record's `target:` commit | the `target:` line; every `verdict:`, `location:`, `reopens:` and `regression:` line under `## Findings`; every `confirms:` line of `## Confirmations`; the labels in no other spelling and in no other place |
| the sealer | reads the records as one party's story against the others (step 4); it re-checks no finding's verdict and no `fixed` commit, since the check reads both | nothing of a record that the check does not read |

A round records **what it reviewed, what it found, and what answered it**, in
one file the warden writes and the smith's fix pass completes:
`seal/specs/<work-item-id>/rounds/round-N.md`, from `templates/sdd-round.md`.
Words only: no emoji anywhere in it.

````
# <work-item-id> — review round N

target: <sha> against <base>        (a verifying round: <sha>, fixes <a>..<b>)

## Findings

### 1. <what is wrong, as a symptom, in one line>

severity: must
location: `path:12`
verdict: open
regression: round-<N-1>#<n>        (or reopens: round-<N-1>#<n>; at most one of the two)

<why it matters and the grounds, executed and read labelled apart; where
`regression:` stands, the unit a fix pass's own commit added or changed, first;
where `reopens:` stands, why the earlier close does not hold, first>

```<lang>
<the paste-ready fix: the artefact, not a description of it>
```

answer: <the fix pass: what was done, why the finding does not hold, or where it went>

## Confirmations

confirms: round-<N-1>#2
<what holds, at `path:line`, and how this round confirmed it, executed or read>

confirms: none
<a claim of the frame or the build that matched, at `path:line`, executed or read>

## Not judged

| What | Location | Who answers |
|---|---|---|

## Probes

| Command | Result |
|---|---|
````

Eight things about it, each the whole of a rule, each as the owner's
decisions of 2026-10-16, Q11's answer and the decision on round 8 left it:

- **Every label is one plain lowercase English word at the start of a
  line, followed by `:` and one space, and the check refuses any other
  spelling as unreadable, never skips it.** The reader is mostly an agent,
  so every label and every value is a word whose meaning is guessable
  without this repository's documents (the owner, 2026-10-16). Eight labels:
  `target:` once per record, outside every section; `severity:`,
  `location:`, `verdict:`, `regression:`, `reopens:` and `answer:` inside a
  finding; `confirms:` inside `## Confirmations` (`reopens:` from 5d-v, the
  owner's decision on round 8). A line whose first word,
  case-folded and stripped of `*`, `_` and `` ` ``, is one of the eight or
  an old spelling — `Target SHA`, `refixes`, `fix of a fix` — followed by
  `:`, and which is not the exact form, is refused by path and line as *a
  label in another spelling*, naming the label it would have to read —
  `Verdict:`, `**verdict:**`, `VERDICT:`, `verdict :`, `Reopens:`,
  `Target SHA:` and `refixes:` among them — and the finding is not read
  past it. A finding's
  label outside a finding, a `target:` or `confirms:` line inside one, and
  a `confirms:` line outside `## Confirmations` are refused the same way.
  A label with nothing after it, its trailing space trimmed, is the exact
  form, and its value's reader judges the empty value (S24; T32).
- **The fact the check decides on has one spelling in one place, and the
  check fails closed.** The line is `verdict: <value>`, inside a `###`
  section of the one `## Findings` section, in no table cell and with no mark
  around it. The value is one of four shapes and nothing else: `open` ·
  `fixed <commit>` (seven to forty lowercase hex digits, a commit HEAD
  descends from) · `rejected` (the finding does not hold) · `deferred
  <home>` (a home after the word).
  Anything the check cannot read is refused by name, never passed: a value
  outside the four, a finding with no `verdict:` line or with two, a
  `verdict:` line outside `## Findings`, a record with no `## Findings`
  section or with two, a `fixed` whose commit HEAD does not descend from. A
  `verdict:` inside a fence or a comment is not a line the reader sees, so a
  finding whose only verdict stands in its fix block has none, and is
  refused; **a fence or a comment that never closes is refused at the line
  that opened it** (5d-i's smith, 7d05c9cf; T31), because `reader.readable`
  blanks such a region to the end of the file and every heading and
  `verdict:` after it would vanish. On a ready pull request `open` fails too.
  No emoji, no table cell and no severity is read for the decision. **How it
  errs, stated:** a fence that closes on the wrong line — a fix block's
  opener matched by another block's closer — hides the headings and lines
  between them without being unclosed, and nothing refuses it, because a fix
  block legitimately quotes markdown with `### ` headings in it; the
  orchestrator reads every record against the template before committing it,
  and the next round's warden reads the earlier records whole (5d-i's open
  item, answered here as a limit and not a check).
- **A `fixed <commit>` touches its finding's location, and the check reads
  it.** The `location:` line holds one or more coordinates, each a backticked
  `path`, `path:line` or `path:first-last` with the path relative to the
  repository root, joined by `, `; exactly one such line per finding, and a
  line the check cannot read — no backticks, a bare `:617`, a second line,
  emphasis, a URL — is refused by name for every finding, whatever its
  verdict. For a finding at `fixed <commit>` the check runs the commit's
  changed paths (`git diff-tree --no-commit-id --name-only -r <commit>`, the
  root commit included) and refuses the finding unless at least one changed
  path equals a named path or lies under it. At least one and not every one
  (`plan.md` Alternative AN): the fact the check closes is `fixed accede1`,
  a commit that touches nothing of the finding, and whether a fix that
  touched one of three named places is complete is the verifying round's
  judgment, which is why that round exists. **A fix that lives where the
  warden did not point is named on the same line, in the same spelling.** The
  warden's `location:` names every place the defect shows and the path its
  paste-ready fix goes to, where that differs — a defect that shows in a
  document and is fixed in the code that produces it names both. Where the
  fix pass fixed it somewhere else again, it appends that coordinate to the
  `location:` line, joined by `, `, and its `answer:` says so; the check reads
  the line as it stands, so a commit touching no named path is refused
  whoever wrote the line, and the appended coordinate is what the verifying
  round's warden reads its confirmation against (`plan.md` Alternative AV;
  round 1's finding 5 is this case before the rule, AU). So the fix pass
  writes its two lines and may lengthen one more, and nothing else. The
  sealer's manual act *touches the location it fixes* leaves
  `agents/sealer.md` step 3 and every sentence that stated it
  (`## Removes`). **How it errs:** a commit that touches a named path and
  fixes nothing passes; the verifying round reads the fix, and its
  `confirms:` line is the record of that reading (S22).
- **The channel between rounds is a fact the check reads.** A reference is
  `round-<N>#<n>`, the earlier record's number and the finding's heading
  number, in that spelling and no other (`plan.md` Alternative AO); `round-<N>`
  alone names a round's fix pass where the unit the regression stands in was
  changed by no numbered finding. **A round names an earlier finding by one
  of three relations, each its own label** (the owner, 2026-10-16, on round
  8): `confirms:` where the close holds; `reopens:` on a new finding where
  the earlier close does not hold — a `rejected` finding that holds after
  all, or a `fixed` commit that left the defect standing, in the unit it
  changed or in another — and no fix pass's own commit made the defect, an
  ordinary finding that gets its fix pass;
  `regression:` on a new finding where a fix pass's own commit introduced
  the defect, which the orchestrator routes by the comparison its grounds
  state — to the framer or to an ordinary fix pass (§*What leaves*'s
  `Fix of a fix` row). A reference stands in three places. Each
  entry of `## Confirmations` is a `confirms:` line reading `round-<N>#<n>`,
  or `none` for a claim of the frame or the build that matched, with the
  entry's prose on the lines after it; a table row in the section is
  refused. A finding's `regression:` line reads `round-<N>#<n>` or
  `round-<N>`. A finding's `reopens:` line reads `round-<N>#<n>` alone,
  since a close is a finding's verdict and a fix pass no finding named
  closed nothing to reopen: `reopens: round-<N>` is refused by line. A
  `regression:` or `reopens:` line with nothing after it is read as its
  label and refused at its line for the empty value. **A finding carries
  at most one of `regression:` and `reopens:`**, and one carrying both, a
  bare line among them, or two of either, is refused at the second line,
  naming which line each case takes — the two relations are routed differently,
  one by the comparison with the frame and the other always to a fix pass,
  so a finding holding both says neither. A round with
  nothing to confirm leaves `## Confirmations`
  out, and a record holding two is refused. For every finding of round N
  whose verdict is `fixed <commit>` or `rejected`, the record of round N+1
  must hold a `confirms:`, a `reopens:` or a `regression:` line naming it,
  else the check
  refuses the finding at its own `### N.` heading line in round N's record,
  naming the next record and the reference it owes — the finding's own
  record is where it stands, and the later round is what has to answer it;
  a finding at `deferred <home>` needs no confirmation. A reference the
  check cannot read, one naming a record the item does not have, or a
  finding number that record does not hold, is refused by path and line,
  on any of the three labels.
  Round 1 has no earlier record, so it owes nothing and every reference in
  it is refused: its `confirms:` lines read `none`. **How it errs, stated:**
  the check reads that the earlier finding is named and on which line,
  never whether the relation is true. Which of `reopens:` and `regression:`
  a close that does not hold takes is the warden's reading of which commit
  made the defect; a `reopens:` line written where a fix pass's commit made
  it gets a fix pass the regression rule would have stopped, and the next
  round's warden and the sealer, who read the records whole, are who catch
  it. Nor does the check read the earlier finding's verdict for a
  `reopens:` line, any more than for the other two: a reopened `deferred`
  finding is the warden's claim that the deferral was wrong, which the
  orchestrator reads (`plan.md` Alternative AZ). On a ready pull request
  a `fixed` or `rejected` finding in the last record is refused at its
  `verdict:` line as *a verifying round is owed* — the same words the
  `target:` rule prints — because nothing after it has read the fix or the
  rejection; a last record whose findings all read `deferred <home>`, or
  none, passes (S23; `plan.md` Alternatives AP and AT).
- **Severity is for people, and the check ignores it.** Two words on the
  finding's `severity:` line: `must` (fix before merge) and `should` (fix,
  or say why not), in place of `blocks merge` and `fix or justify`. A
  confirmation is a `confirms:` entry of `## Confirmations` and a thing not
  judged a row of `## Not judged`, with who answers it; neither is a
  finding, and no mark names either. A sentence an agent reads and acts on is a defect when it is
  wrong, and is `should`; a sentence in a record that merely reads badly is
  not written as a finding.
- **The record is written in words, and no emoji stands anywhere in it.**
  The check does not read for one: the record's facts are its labelled
  lines, and an emoji the check does not read cannot mislead it. The template, the review skill's findings format, the warden's
  and the smith's instructions, the orchestration paragraphs and the panel
  lines this item touches carry none, and a test holds the shipped text to
  it (T39, `plan.md` Alternative AQ). Other skills and definitions are #957's
  and #940's, and `## Removes` names what is left to them.
- **The warden writes the record, and no generator copies it.** The fix is
  inside its finding, so the fix pass opens one section and finds the what,
  the where, the why and the paste in one place; a `|` in prose is prose
  again, since no finding is a table cell (#189 is a cost of the cell, not of
  the record). **The smith's fix pass writes two lines per finding and
  nothing else in the file:** it rewrites the finding's `verdict:` line to
  `fixed <commit>`, `rejected` or `deferred <home>`, and writes its `answer:`
  line; where its fix went to a path the `location:` line does not name, it
  appends that coordinate to the line (the location rule above). There is no
  fix table and no `close`. **The word says what happened to the defect.**
  `rejected` means only that the finding does not hold, and `answer:` says
  why. A repair made by a commit closes `fixed <commit>`, a correction to a
  record among them, the record's path on the `location:` line. A finding
  whose defect was real and was repaired outside the tree, with no commit on
  the branch — an issue or a pull request body edited — closes `deferred
  <where it was repaired>`, for example `deferred #956`, and `answer:` says
  what was changed there; like every deferral it owes the next round nothing
  (`questions.md` Q11, the owner, 2026-10-16; phase 5d-iv).
- **The reviewed commit is a fact every check rests on, and it is the one
  line outside the sections.** `target: <sha> against <base>`, or `target:
  <sha>, fixes <a>..<b>` for a verifying round, its first word the reviewed
  commit; a record with no `target:` line, two, or a value of another shape
  is refused by line, and the old `| Target SHA |` row is no `target:` line.
  The broad gate's run lives in `broad-gate.md`, the sealer's verdict in
  `guarantee.md`, and the pull request knows its own branch.

**No reader for the old shape.** The check judges only the work items the
pull request's own commits declare or change (`chain_check.py#main`,
`#carried_by`; `docs/the-review-record.md` §*An item is judged at the pull
request that carries it*), so the 34 records of the other 0.22.0 items were
judged at their own pull requests and are read by nothing again. This item's
six records were rewritten into the shape, mechanically, with every verdict
and every ground unchanged in substance, in the phase that landed the reader
(`plan.md` row 5d-i): a 🔴 or 🟡 row became a finding, its `· fix pass:` or
`· orchestrator:` tail its answer line, its paste block moved inside it; a 🟢
row became a `## Confirmations` entry and a ❓ row a `## Not judged` row. The
test that read every record in the tree went with the shape it read
(`plan.md` Alternative AJ). What a release reads of records
(`.github/scripts/release_seal.py#chain_counts`, the panel's
`broad_gate.py#rounds_rows`) reads the new shape through the check's reader
and reports an old-shape record as *not read*, which is the fail-closed
answer for a count too.

**The six records under the decisions of 2026-10-16** (`plan.md` rows
5d-ii and 5d-iii; `read` at 614e4d66, rewritten at 451dc1f2 and 92991623).
They did not read clean as 5d-i left them, and two one-shot scripts, one per
sub-phase, gave them what their prose already stated, nothing else, every
verdict, reference and commit unchanged. 5d-ii: the labels lowercased;
`blocks merge` made `must` and `fix or justify` made `should`; each `Fix of
a fix:` line's unit moved into the first sentence of the grounds and its
reference written from the fix commits the line names — round 2's findings
1 and 5 name `round-1#1` and `round-1#5`, round 4's finding 2 names
`round-3` (5ea6506c was round 3's fix pass and no finding of round 3), round
5's findings 1 and 2 name `round-4#1` and `round-4#2`, round 6's finding 1
names `round-5#1`; each confirmation's reference written from the lead of
its `What holds` cell (*round N's 🟡 k is closed* and *round 1's 🟡 7's
leftovers* give `round-N#k`; a lead naming no finding, round 5's *round 4's
❓*, gives `none`), the lead kept as prose with its mark respelt; every
`round N's 🔴 k` or `round N's 🟡 k` in prose outside a fence respelt
`round-N#k`; the three shorthand location items of rounds 5 and 6
(`:461-463`, `:617`, `:786-789`) given the path of the item before them.
5d-iii: the field table made one `target:` line with the value it held,
each of the six reference lines made `regression:`, and each of the 35
confirmations a `confirms:` line with its what-holds, location and grounds
on one prose line after it; no finding read the old `answered`, so none
became `rejected`. The channel reads clean: round 2 confirms round 1's
findings 2, 3, 4, 6 and 7 and names 1 and 5 as regressions; round 4
confirms round 3's two; every other finding is `deferred the frame`. **One
location line changed its fact, and it is the only one:** round 1's finding
5 read `location: .github/scripts/release_report.py:113-131` and `fixed
1b875efc`, and 1b875efc touched `.test_durations` and `overview.md` alone
(`git diff-tree`, `executed`); its own `executed` line and its paste name
`.test_durations` as the other half of the fix, and its answer says the fix
went there. The line gained `` `.test_durations` `` as a second coordinate,
by that prose (`plan.md` Alternative AU); the other eight `fixed` commits of
rounds 1 and 3 each touch their path. The quotations of the old marks in
the records' prose — `**🔴 1**`, *a 🟢 row* — stay, since they are what the
findings were about and the check reads none of them, and the six records
leave the tree with the next `settle --retire-process` (`questions.md` Q10,
the owner, 2026-10-16).

### What leaves, what stays, and the evidence for each

Judged on what its history shows it caught against what it cost. The 0.22.0
records above are the measured history; where a field's defence is a spec's
citation of an older issue, that is `read` and says so.

| Mechanism | What it caught, as the history shows | What it costs | Verdict |
|---|---|---|---|
| `Target SHA` | every arm of the check rests on it; the proof's replay cases clone at it | one row | **stays**, as the record's one `target:` line (the owner, 2026-10-16) |
| The `Verdicts` table in its five columns | the findings themselves; the proof's `truth-` graders read its rows | one cell held a finding's whole account and a `\|` in it broke the row (#189); three kinds of row shared one table, so a reader had to sort them by a mark; four of this item's six rounds found a spelling the sorting let through | **leaves** (reframed after round 6). A finding is a `###` section of `## Findings` with its labelled lines; a confirmation is a `confirms:` entry and a not-judged item a row, each in its own section. The `truth-` graders read a line window of the finding's `location:` line (§*The proof harness, as this item leaves it*) |
| `Executed probes` and `Paste-ready fixes` | contract §4 in the record; the smith pastes | the warden writes them anyway | **stay**, as `## Probes` and as the fenced block inside each finding, where the fix pass reads it beside the finding it answers |
| The emoji vocabulary 🔴 🟡 🟢 ❓ as record fields, the `#` cell and the bare-integer id | a severity a person reads at a glance | read by the check to tell a finding from a non-finding, which is the one fact rounds 1, 2, 5 and 6 each found read wrong once (a severity in the Finding cell, a 🟢 or ❓ cell over an `open`, `confirmed` on a 🔴 row, `**🔴 1**`) | **leaves the record** (reframed after round 6; the words set on 2026-10-16). `severity: must` or `should` is for people, and the finding's number is its heading's; the check reads neither, and no emoji stands anywhere in the record |
| `round-N-report.md` beside `round-N.md` | nothing: the record was the report's tables copied | 19 files, 303 KB of 564 KB in 0.22.0; half of what a later round inherits | **leaves**; the warden writes `round-N.md` |
| `round_record.py` (`new`, `close`, `notes`, `seal`), `bin/round-record{,.cmd}` | wrote the copy and the derived fields, applied the fix table, counted the notes | 5,596 lines, 35 test modules, the generator's refusals at the keyboard (#503, #866 in `docs/round-record-spec.md`, `read`) | **leaves whole** |
| `Pass` box | whether a row is still open | a box that restates the table | **leaves**; the check reads the rows: no `open` verdict on a ready pull request |
| The reading of a verdict row — which rows are findings, and which words close one (`chain_check.py#verdict_table`, `#verdict_of`, `#open_findings`, `CLOSES_BY`, `EVERY_CLOSE`, `FINDINGS`, `BLOCKING`, `SHOULD`, `FINDING_WORDS`, `CLOSED_WORDS`, and before phase 5a `#severity_of`, `NOT_FINDINGS`, `FINDING_CLOSES`, the `#` column found by its header) | nothing in the records it read: no 🔴 or 🟡 row of the 36 records at round 2 read a 🟢 or ❓ row's word (round 2's probe, `executed` by the warden). What its four versions carried was the hole each round found: round 1's let a severity outside the first cell hide an `open`; round 2's let a 🟢, ❓ or ⬜ `#` cell hide one; phase 5a's let a 🔴 row close `confirmed`, which rounds 3, 4 and 5 gave the sealer to catch and each found that backstop short; phase 5c's read the mark with `startswith` on the raw cell, so `**🔴 1** … confirmed` passed (round 6's 🟡 1). Each repair read the same cell by one more rule, and every spelling the rule did not know fell to the passing side | four readings in six rounds, three reframes, two word sets, and a rule the documents restated per round | **leaves whole** (reframed after round 6). The decision is what the check decides: whether every finding has an answer. So the record gives it that fact in one line it can read without sorting anything — `verdict: <value>` inside a finding's section — and the check refuses whatever it cannot read (§*What a round records*). The emoji marks, the mixed table, the word sets per mark and the old generator's words `withdrawn`, `not a defect` and `agreed, fixed` go with the reading; nothing reads an old record, so nothing needs them. Since 2026-10-16 the check reads three more facts of the same kind, each a labelled line in one spelling: a `fixed` commit touches a path of the finding's `location:`, the next record's `confirms:`, `reopens:` and `regression:` lines name every finding the fix pass closed `fixed` or `rejected`, and a label in another spelling is refused. **How it errs, stated**: a `fixed <commit>` that touches the path and fixes nothing passes, and the verifying round's warden, whose `confirms:` line the check then requires, is who reads the fix; a fence closed on the wrong line hides what lies between (§*What a round records*). A finding the warden wrote outside `## Findings`, or without a `###` heading, is not a finding to the check: the template, the warden's definition and the eval's shape grader hold that shape, and a section with no `verdict:` line is refused rather than passed |
| `Fixes checked by`, `Needs a fix`, `Written late` | the last fixes read by nobody (the verifying-round rule, #161 `read`); the record committed after its fixes. `Written late` read `no` 19/19 | three rows derived from facts the check can read | **the fields leave; the rule stays** as one check: the last record's `target:` commit is HEAD, or every commit after it touches only `seal/specs/<id>/`. A round after the last fix pass is therefore owed, as today |
| `Fix range`, `Contract changes`, `New units`, the depth refusal, inherited coordinates | the verifying round's finding surface; a fix pass adding a unit nobody reviewed (#194, #211, #366 `read`). `Contract changes` read `none` 17/19; `New units` named in 9/19 | AST walks of the fix range in `round_record.py`, 198 s of tests for the floor and depth alone | **leave**; the warden's definition states that a verifying round reviews the whole fix diff, new units included, and the fix range is written on the `target:` line |
| `Fix of a fix` count and its `second` stop | fired three times in 0.22.0 and sent #929 and #931 back to the framer; what it caught was fixes chasing one mechanism's edge cases, which `CLAUDE.md`'s tenet now states as a rule every agent reads | the count needs the fix range, the units and the depth above; 365 s of tests; four reframe spawns | **the judgment stays, the count leaves**: the warden writes a finding's `regression:` line where the defect is one a fix pass's own commit introduced, naming the earlier finding or fix pass; a defect in a phase the framer designed and the owner approved is an ordinary finding of new work with no such line (the owner, 2026-10-16, on round 7); **a `regression:` line does not send the work item to its framer by itself; the fix is compared with the frame first** (the owner, 2026-10-16, refining the ruling on round 8). The warden who writes the line states the comparison in one sentence of the finding's grounds: what the frame says (the phase's `plan.md` row and `spec.md`), what the fix did, and where the defect came from. No label carries it, and the orchestrator routes on that sentence, at any round of the run. Where the fix built what the frame says and the defect is still there, the frame is wrong: the round gets no fix pass and the work item returns to its framer, who redraws the frame (`Reframed … after round N.` under the mark; `questions.md` Q1, the owner, 2026-10-15), and the run then goes on with the redesign's build and its rounds. Where the fix departed from the frame, or the defect came from how the fix was written — a paste-ready fix taken from a review record among them — the round gets an ordinary fix pass, and the smith is told what the frame says. A second regression on the same unit after a fix-pass route goes to the framer whatever the comparison says, which is the loop guard. Round 8's finding 2 is the measured case: its defect came from round 7's paste-ready fix, applied verbatim at 46cd674a, so under this rule it would have taken a fix pass; this reframe stands because `reopens:` needed a frame anyway (`plan.md`'s reframe paragraph after round 8). A close that does not hold where no fix pass's commit made the defect — a rejection that was wrong, a `fixed` commit that did not fix it — is raised again as an ordinary finding with a `reopens:` line naming it, and gets its fix pass (the owner, 2026-10-16, on round 8). Checked by nothing; the sealer reads the records |
| `Loses a record or crashes` floor, the round cap, the one reopening | #161's 15-round run (`read`); `yes` 2/19 in 0.22.0; no 0.22.0 run reached the cap — the stop above ended them | three rules, 65 + 45 + 117 lines of spec, their arms in the check | **one orchestrator rule replaces them** (`skills/code-review/orchestration.md`): a run has three finding rounds by default, counted from the last design change, a reframe or a new phase the owner approved in `plan.md`, so the first finding round that reviews new work starts the count again at one, and extended one at a time while the latest round found fewer findings than the one before and none is a regression, each extension one line in that round's record (`questions.md` Q1, the owner, 2026-10-15; where the count starts, the owner, 2026-10-16, on round 9); a regression routed to a fix pass is followed by one verifying round, whatever the count, which is not an extension, and a second regression it finds on the same unit goes to the framer; at the cap every open finding takes the filing ladder and reads `deferred <home>`. Checked by nothing at the pull request; the sealer and the person reading it see the count, and `tests/test_the_rules_have_one_owner.py::test_the_cap_counts_from_the_last_design_change` holds the rule's carriers to where the count starts |
| ⬜ notes, `notes --at`, *a note closes once* | prose quality in records and definitions | carried open through every later record (3 → 15 in #929); a command at the run's end; a `chain_check` arm | **leaves** with the severity |
| `Ran by` | nothing that changed an outcome | one row and an arm | **leaves**; `routing.md`'s free text names the models, as it does today |
| `Broad gate` cell, and `broad-gate.md` where the work went straight to the pull request | the broad run happened at HEAD | two homes for one fact, `round_record.py seal`, `kept_broad_gate`, `seal_home` | **one home**, `broad-gate.md`, written by `broad-gate --record` on both routes |
| `PR` field, `## What this round was asked`, `## Inherited coordinates`, `## Deferred` | nothing a reader cannot see in the pull request, the spawn prompt or the earlier records | copies | **leave**; a deferral is a verdict word |
| `tests-todo.md` | a prescribed test | written by 0 of 4 items; a hook and three documents read it | **leaves**; a prescribed test is a 🟡 row and closes `fixed <commit>` |
| `hooks/review-history-guard.py` | a reminder on `gh pr review` and `gh pr merge`; nothing recorded a catch | 303 lines, 6 test modules | **leaves**; the check at the pull request is the enforcement |
| `chain_check.py`'s remaining arms | the declaration's vocabulary; a declared framer left `spec.md`, `plan.md` and the mark, and a `Reframed` line's author matches; a declared chain left at least one record, every verdict is closed, the last record is at HEAD; `broad-gate.md` and `guarantee.md` name HEAD on a ready pull request; a draft prints and fails nothing | one module, this repository's tests for it in one file (#942) | **stay**, rebuilt |
| `pact_notices`, `fragment_left_behind` and the arms over removed things | the pact change records left in 0.22.0 (#944) | dead reads | **leave** |
| `docs/round-record-spec.md`, `docs/review-chain-spec.md`, `docs/review-handoff-protocol.md` | the rules above, and their history | 2,725 lines, 63 test modules between them | **leave**; one `docs/the-review-record.md` states the record, the run's four rules (the verifying round, the cap, the regression stop, the filing ladder) and the handoff rule (coordinates, never prose), each with its `Enforced by:` or its link |

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

## The agent definitions this item touches

Every definition written anew from its job — one shape for all five, the
contract alone preloaded and each skill opened at its step, the contract
numbered anew, the rules #923 once listed for each and now #957's body
lists — is #957's, framed on the released tree (the owner's split,
2026-10-16; `## Removes` names what moved). This item rewrites a definition
only where it states the record or the sealer's job, in place:

| Agent | What this item changes in it | Phase |
|---|---|---|
| `sealer` | written anew to §*The sealer*: `model: opus`, `skills: [agent-contract]`, the five steps, step 3 the one list of its acts (two from 5d-ii), `guarantee.md` its one write | 4; step 3 in 5b, 5c and 5d-ii |
| `warden` | §*Report*: the record at `rounds/round-N.md` in the branch worktree under review, from the template, no separate report; the findings format in the record's lowercase labels, `must` and `should`, words only; a verifying round names every finding the fix pass closed `fixed` or `rejected` on a `confirms:`, a `reopens:` or a `regression:` line, by its `round-<N>#<n>`; a finding whose unit a fix pass's own commits added or changed, and whose defect those commits introduced, carries a `regression:` line, and a defect in a unit a build phase made, which the framer designed and the owner approved, is new work with no such line (the owner, 2026-10-16, on round 7); a finding raising an earlier close that does not hold, where no fix pass's commit made the defect, carries a `reopens:` line; and a finding carrying a `regression:` line states in one sentence of its grounds what the frame says, what the fix did and where the defect came from (the owner, 2026-10-16, on round 8) | 3, 5d-iii, round 7's fix pass, 5d-v |
| `smith` | the fix pass: it rewrites each open finding's `verdict:` line to `fixed <commit>`, `rejected` or `deferred <home>`, a repair outside the tree with no commit `deferred <where it was repaired>`, writes its `answer:` line, and appends a coordinate to `location:` where its fix went elsewhere; the `fixed` commit touches the finding's `location:` | 3, 5d-iii, 5d-iv |
| `framer` | its route back: the fix passes stop and the framer is spawned again where a round marks a regression, and `docs/the-review-record.md` §*The run* owns the rule; from 5d-v, where the orchestrator routes a regression to the framer by the comparison with the frame (§*What leaves*'s `Fix of a fix` row) | 3, 5d-v |

The scribe is unchanged. Of the contract, §11's list of the vocabulary a
checker reads loses the fields the record dropped, and nothing else.

## The proof harness, as this item leaves it

The harness is phase 1's (`evals/`): outcome graders only, cost read from
each run's trace, `noninferiority.py compare` writing the record and
`tests/test_a_rewritten_definition_proved_non_inferior.py` recomputing it.
Proving a rewritten agent not worse with it — the baseline, the pass rule as
the rewrites' gate, the runs and their budget — is #957's, whose body takes
this suite as a reference to rebuild around outcome and cost rather than as
the gate. What this item changes in it:

- **The warden's shape graders point at `rounds/round-N.md`**, and the two
  that read the `Needs a fix:` and `Loses a record or crashes:` lines leave
  with those fields. After round 6 the shape grader reads the `## Findings`
  heading and a `### <n>. ` section with its `verdict:` line, and holds the
  record free of emoji with a `not_contains` pattern over the emoji ranges;
  a `truth-` grader reads a finding's `location:` line for its path and a
  line within ±15 of the truth, a unit's lines placing that window where an
  old location named a unit, and never a `path#unit`, which the check
  refuses (`evals/scripts/behaviour.py`, `replay_targets.py#truth_pattern`,
  `seed_defects.py`; round 7's finding 1, f5ba02f1), in place of the table
  row they read. `noninferiority.py#verdict`'s pass rule 3 reads shape
  graders on the new side only, since the old side's shape is the old
  record's by construction; `reach-` graders stay at 100 % on both sides.
- **The sealer's three cases are redesigned for the guarantor**: a sound
  fixture item (verdict `sound`, `guarantee.md` written, nothing else
  changed); a pull request body claiming a change the tree does not carry
  (`not sound` naming the body); a phase record claiming `seen red` for a
  case that is green against the old code (`not sound` naming the claim). The
  old sealer's job was the broad run, so no baseline comparison applies; the
  sealer's proof is outcome on these cases, with its cost written and not
  judged (`questions.md` Q2 names the first measurement).
- **This item takes no baseline.** It rewrites one definition whole, the
  sealer's, whose cases are new, and the others only where they state the
  record; the baseline and the sealer's run on Sonnet against Opus are
  #957's.

## Scope

**In — this work item, part A of #923, its whole scope** (`plan.md` phases
1–5 and the repairs 5a–5d-v): the proof harness made light and the budget
concept gone (phases 1 and 2); the review record and its checker; the broad
gate's one record file; the sealer as guarantor with its
template, its check arm and its three cases; `docs/the-review-record.md` in
place of the three specs; the record sections of
`skills/code-review/orchestration.md` and the rows of
`skills/implement/orchestration.md`'s delivery table that named removed acts;
`docs/the-agent-set.md`, `docs/the-record-layout.md` §*seal/specs/<work-item-id>/*
and `docs/the-broad-gate.md` rewritten where this item makes a sentence of
them false; `templates/config.md` §*What no row governs*' list of the
literals the check reads, which a test derives from the check's constants;
the warden's shape graders; the tests sorted into #942's layout
with every deleted module's guard named; the changelog fragment. The
record's rules are stated in `docs/the-review-record.md` and restated where
a party's text states them today; stating them once and having every other
file point there is #957's, and phase 5d-v rewrites each statement in place
rather than moving it.

**Moved to #957 — part B, `release: 0.22.1`** (the owner's split,
2026-10-16): the contract and the five definitions written anew, the
`skills:` lists cut, the preloaded skills rewritten where an agent opens
them, the test modules that pin their text, the baseline and the proof that
each rewrite is not worse, with #957's own items — the marks, labels and
constants with no reader, the `Reads:` census and the rider stamps, the
sealer's Sonnet-against-Opus comparison. #957 is framed on its own after
0.22.0 is installed, so the agents are written once, against the record
this item ships; `plan.md` §*Phases* names the commit at which this file's
part-B phases last stood, its starting reference.

**Out, and whose.** `skills/verify/SKILL.md`, `skills/settle/`, the small
skills, `templates/` other than `sdd-round.md`, the new `sdd-guarantee.md`
and `config.md`'s literal list,
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
| S1 a round is one file | a warden reviews a fixture branch | `rounds/round-1.md` exists in the branch worktree with one `target:` line, `## Findings` holding one `###` section per finding with its `severity:`, `location:` and `verdict:` lines and its fenced fix, `## Confirmations` with a `confirms:` line per entry where the round confirmed something, `## Not judged` and `## Probes`, and no emoji in the file; no `round-1-report.md`; the warden eval's shape graders pass on it |
| S2 the fix pass completes the record | a smith answers round 1 | every finding's `verdict:` line reads `fixed <commit>`, `rejected` or `deferred <home>` — a repair made outside the tree with no commit reading `deferred <where it was made>` (Q11) — each `fixed` commit touching a path its `location:` names, and its `answer:` line is filled; where the fix went to a path the warden did not name, the `location:` line gained that coordinate and nothing else; no other line of the file changed (`git diff` of the record shows only those lines) |
| S3 the check reads one line per finding, and refuses what it cannot read | a record whose `## Findings` holds a finding at `verdict: open`; one whose `verdict:` value is outside the four shapes (`confirmed`, `Fixed abc1234`, `fixed` with no commit, `fixed abc1234.`, `deferred` with no home, `**fixed** abc1234`); a finding with no `verdict:` line, or with two; a finding whose only `verdict:` stands inside its fenced fix; a `verdict:` line under `## Confirmations`; a record with no `## Findings`; a `fixed <sha>` naming a commit HEAD does not descend from; a fence or a `<!--` comment that never closes, with an open finding below it; pull request not a draft | `chain_check.py` exit 1 for each, naming the record, the line and the finding's heading, and saying which of the four shapes a value would have to take; the unclosed region named at the line that opened it; a draft prints the same and exits 0. A record whose findings all read `fixed <commit on the branch, touching a located path>`, `rejected` or `deferred <home>`, and one with an empty `## Findings`, pass this reading. `severity:` is read for nothing: a finding at `severity: anything` and `verdict: rejected` passes it (T25–T28, T31) |
| S4 the last fixes are read | the last record's `target:` commit is behind HEAD by a commit touching a file outside `seal/specs/<id>/` | exit 1 naming the commit and *a verifying round is owed*; HEAD moved only by record commits passes |
| S5 the broad gate has one home | `broad-gate --record` on a green run, either routing answer | `seal/specs/<id>/broad-gate.md` reads `<sha> against <base>`; no `Broad gate` row anywhere; a ready pull request whose file names a commit other than HEAD fails |
| S6 the sealer guarantees | a sound fixture item with a pull request body | `guarantee.md` with the five sections and `Verdict: sound`; nothing else in the tree changed; the report labels every claim |
| S7 the sealer catches a story the tree contradicts | a pull request body claims a removal the tree still carries; a phase record claims `seen red` for a case green against the old code | `Verdict: not sound — <the claim>` naming the party and the coordinate, once per case |
| S8 the sealer's verdict gates | `guarantee.md` reads `not sound` or `undecidable`, or names a commit other than HEAD | exit 1 at a ready pull request naming the file and the verdict |
| S9 the regression stop is a judgment, and it is about a fix pass's own commit | a warden's record gives a finding a `regression:` line because a fix pass's own commit introduced the defect, in any round of a run; a round finds a defect in a unit a build phase made, which the framer designed and the owner approved; and a verifying round finds that an earlier `rejected` finding holds after all, or that a `fixed` commit left the defect standing, in the unit it changed or in another, where no fix pass's commit made the defect | `docs/the-review-record.md` §*The run* gives a finding its `regression:` line only where a fix pass's own commits added or changed its unit and those commits introduced its defect, and says the first is routed by the comparison its grounds state (S27), the work item returning to its framer, who redraws the frame, where the fix built what the frame says, that the second is an ordinary finding of new work with no `regression:` line, which gets its fix pass, and that the third is an ordinary finding carrying a `reopens:` line naming the earlier finding, which gets its fix pass and sends nothing to the framer; `tests/test_the_rules_have_one_owner.py::test_a_regression_is_a_defect_a_fix_passs_own_commit_made` holds the document, the template and the warden to the first two, and to "those commits introduced" and "left the defect standing", and `::test_a_close_that_does_not_hold_reopens_it` (T44) holds the document, the template, the warden, the review skill and the orchestration's verifying-round table to the third; `chain_check.py` reads either line as a reference for the channel (S23) and never to stop a fix pass; the sealer's parties check names it |
| S10 nothing kept beside the tree | after phase 3 | no `round_record.py`, `bin/round-record{,.cmd}`, `review-history-guard.py`, `tests-todo.md` reader, `Fix range`, `Contract changes`, `New units`, `Fix of a fix`, `Needs a fix`, `Loses a record`, `Written late`, `Ran by`, `Fixes checked by`, `⬜`, `notes --at` outside `seal/specs/` and `changelog/` (`grep -rn` over the tree) |
| S11 nothing reads an old record, and the check judges only what the pull request carries | a work item another pull request merged, its records in the old shape; a pull request whose own commits declare or change one work item | `chain_check.py` reads the records of the declared item alone and never opens the other items' `rounds/` (`TestMain`, the fixture tree holding a second item with an old-shape record); an old-shape record under a declared item is refused by name (S3). `.github/scripts/release_seal.py#chain_counts` and `broad_gate.py#rounds_rows` count `deferred` findings through the check's reader and report a record they cannot read as *not read*, never as 0 |
| S12 the suite is lighter | after phase 3; after phase 5a | `.test_durations` summed over the modules that name `chain_check`, `broad_gate` is below 1,500 s (from 4,553 s); the deleted modules' guards listed one line each in `phases/phase-3.md`. After phase 5a the file holds no entry for a case the suite does not collect: `bin/test tests -q -k test_the_durations_file_prices_the_suite` exit 0, and `release_report.py#suite_seconds` sums the file as it is |
| S13 one spec for the record | after phase 3 | `docs/the-review-record.md` exists, every rule paragraph ending in `Enforced by:` or a link, `rules --check` exit 0; the three old documents are gone and no file names them |
| S19 nothing asks a person | the whole change | no `AskUserQuestion`, no `input()`, no new prompt; the eval scores itself; the sealer's `undecidable` is a written question, not a stop mid-run |
| S20 every statement of the record's shape is the new one (phase 5d; the severity-keyed rule of phases 5a–5c and 5d-i's capitalised labels are history) | after phase 5d-iii | `git grep` outside `seal/specs/` and `changelog/0.*.md` for `## Verdicts`, `Paste-ready fixes`, `Executed probes`, `verdict_table`, `open_findings`, `CLOSES_BY`, `five-column`, `Grounds` cell, `#` cell, `🔴 or 🟡`, `bare-integer id`, `Severity:`, `Location:`, `Answer:`, `Fix of a fix`, `refixes`, `` `Confirms` cell ``, `blocks merge`, `fix or justify` and `touches the row` finds no statement of the shape — what it finds is a refused spelling the check, its cases, the old-shape fixtures or `docs/the-review-record.md`'s labels paragraph name on purpose, or history in a comment, each hit named in the phase record (from 5d-iv, `tests/test_the_record_is_written_in_words.py`'s docstring no longer among them); `git grep -n "Verdict:"` finds only `guarantee.md`'s line and its readers (`chain_check.py#verdicts_of`, `templates/sdd-guarantee.md`, the sealer's definition, cases and graders), since the guarantee keeps its spelling (`plan.md` Alternative AM); `templates/config.md` §*What no row governs* lists the new literals and `tests/test_the_pull_request_language_is_the_repositorys.py::test_the_exclusion_list_holds_every_string_a_checker_matches` holds them to the check's constants; `bin/rules --check` exit 0 with every `Enforced by:` naming a test in the tree; `agents/sealer.md` step 3, `templates/sdd-guarantee.md`'s comment and `docs/the-review-record.md` §*The guarantee* keep the one-list design (T22, T23 unchanged) |
| S22 a `fixed` commit touches its finding's location | a ready pull request; a record whose finding reads `fixed <sha>` with `<sha>` on the branch and touching only a path its `location:` does not name; one whose commit touches one of the two paths named; one whose `location:` names a directory and the commit changes a file under it; one whose `location:` line the fix pass lengthened by the path its commit touched, the warden's coordinates before it; one whose `location:` the check cannot read (no backticks, a bare `:617`, two `location:` lines, none) at any verdict | exit 1 for the first, naming the finding, the commit and the paths it touched; the second, third and fourth pass; exit 1 for each of the fifth, naming the line and the one spelling; the sealer's definition names no such act (T33, T34, T40) |
| S23 the channel between rounds is read | two records; round 1's findings read `fixed <sha>`, `rejected` and `deferred #9`; round 2's `confirms:`, `reopens:` and `regression:` lines name some of them; a round-2 finding carrying both a `reopens:` and a `regression:` line, one carrying two `reopens:` lines, and one reading `reopens: round-1` | each of the three labels covers the finding it names (5d-v: a `fixed` finding named only by a `reopens:` line, and a `rejected` one named only by a `reopens:` line, owe nothing more); the finding with both lines, the one with two, and `reopens: round-1` are each refused at the line that makes it so, naming which line a case takes or that a reopened close names a finding (T42, T43); exit 1 for each `fixed` or `rejected` finding of round 1 that round 2 names on none of the three, refused at that finding's own `### <n>.` heading line in `round-1.md`, the refusal naming round 2's record and the `round-1#<n>` it owes; the `deferred` one owes nothing; a reference round 2 writes that the check cannot read (`round 1's 3`, `Round-1#3`, `#3`), one naming a record the item has not got, or a number round 1 does not hold, is refused by line, on a `reopens:` line as on the other two; a `confirms:` value outside `round-<N>#<n>` and `none`, a table row in `## Confirmations`, and a second `## Confirmations` are refused; a record with nothing to confirm and no `## Confirmations` passes; a reference in round 1, a `reopens:` one among them, is refused and `confirms: none` there passes; on a ready pull request a `fixed` or `rejected` finding in the last record is refused at its `verdict:` line as *a verifying round is owed*, and a last record of `deferred` findings passes (T35–T37) |
| S24 a label in another spelling is refused, never skipped | a record with `Verdict: open`, `**verdict:** open`, `VERDICT: open`, `verdict : open`, `Fix of a fix: <unit>`, `refixes: round-1#1`, `Reopens: round-1#1`, `**reopens:** round-1#1`, `Target SHA: <sha>`, `Severity: must`, `Location: `path``, `Answer: …`; a `target:` or `confirms:` line inside a finding; a `confirms:` line outside `## Confirmations`; a bare `reopens:` or `regression:` line, and a bare `regression:` line beside `reopens: round-1#1` | exit 1 for each, naming the line and the lowercase label it would have to read — `regression:` for the two old reference spellings, `target:` for `Target SHA` — or the place it belongs; the finding is not read past it (T32 and the out-of-place case); a bare reference line is the exact form, read as its label and refused at its line for the empty value, and the bare `regression:` line is refused as a finding holding both (round 9's fix pass, `tests/test_chain_check.py::TestFindings::test_a_reference_label_with_nothing_after_it_is_refused`) |
| S25 the verdict says what happened to the defect (phase 5d-iv; Q11) | a fix pass meets a finding that held and was repaired by editing an issue or a pull request body, with no commit on the branch; and one that held and was repaired by a commit correcting a record | the first closes `deferred <where it was repaired>` (`deferred #956`) with `answer:` saying what changed there, and owes the next round nothing; the second closes `fixed <commit>`, the record's path on its `location:`; `docs/the-review-record.md` §*The round record* says so and a case pins the sentence (T41); `git grep` outside `seal/specs/` and `changelog/0.*.md`, and over this item's `changelog.md`, finds no sentence sending a repair to `rejected`, which every text this item touches gives one meaning, *the finding does not hold*; `chain_check.py` is unchanged, since it already reads `deferred <home>` and owes such a finding nothing |
| S26 the run ends where the check says it does (phase 5d-v; round 8's findings 1 and 2) | an orchestrator reads `skills/code-review/orchestration.md` §*the run ends with a verifying round* after a verifying round whose `should` finding the smith closed `rejected`; and after a round carrying a `regression:` line | the section says one more verifying round reads that answer and names it on a `confirms:` line where the rejection holds, or raises a finding with a `reopens:` line where it does not, which gets its fix pass and one more verifying round; that a round carrying a `regression:` line is routed by the comparison its grounds state (S27), and where it returns the work item to its framer the run goes on with the redesign's build and rounds, the cap counting finding rounds again from the first that reviews the redesign; that where it gets a fix pass, one verifying round follows that fix whatever the count, and is not an extension, and a second regression that round finds on the same unit goes to the framer; and that the run ends only on a round whose record holds no `open`, `fixed` or `rejected` finding — a verifying round, or the round at the cap whose open findings took the filing ladder and read `deferred <home>` — with no commit outside the item's records after its `target:`, which is what `chain_check.py` refuses at a ready pull request (S4, S23, T37); no sentence of it says the run ends at a round that names a rejection on a `regression:` line (`git grep -n "the run ends at that round"` finds nothing outside `seal/specs/`); T44 holds the section to it |
| S27 a regression is routed by comparing the fix with the frame (phase 5d-v; the owner, 2026-10-16, refining the ruling on round 8) | a round carries a `regression:` line where (a) the fix built what the phase's `plan.md` row and `spec.md` say and the defect is still there; (b) the fix departed from the frame, or the defect came from how it was written, a paste-ready fix taken from a review record among them; (c) a second regression on the same unit after a fix-pass route | the finding's grounds state the comparison in one sentence — what the frame says, what the fix did, where the defect came from — and no new label carries it; (a) gets no fix pass and returns to the framer, (b) gets an ordinary fix pass with the smith told what the frame says, (c) returns to the framer whatever the comparison says; `docs/the-review-record.md` §*The run*'s regression paragraph says so, `skills/code-review/orchestration.md` routes on the sentence where it routes a regression, and `agents/warden.md` writes it where it writes the line; `tests/test_the_rules_have_one_owner.py::test_a_regression_is_routed_by_comparing_the_fix_with_the_frame` (T45) holds the document's paragraph to the three routes and the one sentence, and the orchestration and the warden to naming the comparison; `chain_check.py` reads none of it |
| S21 a number a reader acts on names its moment or goes (narrowed in phase 5c) | the shipped surfaces this item writes: `changelog.md`, and every `docs/` sentence this item rewrote | every figure in them is a measurement naming its commit, round or tag, a bound a named check holds the tree to, or gone (§*A number in this frame*). The frame's three documents are read at 680142f2 (`plan.md` §*Technical context*) and the builder's two at the commit each sentence or phase record names; a figure there is history at that moment, not a finding, and no agent reads it against the tree |

S14–S18 — the agents preload the contract alone, an agent opens its skill at
the step, a rewritten definition is proved not worse, no rule is lost unseen,
the contract numbers anew — were part B's and moved to #957 with the split;
their numbers are not reused here.

## Data & interfaces

`templates/sdd-round.md`: the shape under §*What a round records*, one
comment under the `target:` line documenting its two shapes and the cap's
extension line, `Extended past round <K>, counting from round <S>: …`,
one over `## Findings` documenting the six lowercase
labels a finding holds, the four `verdict:` values, the two severities
`must` and `should`, the `location:` spelling, and the `regression:` and
`reopens:` references with what each marks and that a finding carries at
most one of them (`reopens:` from 5d-v), and one comment each over
`## Confirmations` (a `confirms:` line
per entry, `round-<N>#<n>` or `none`, its prose after it, the section left
out where nothing is confirmed, and every `fixed` or `rejected` finding of
the round before named here or on a `reopens:` or `regression:` line) and
`## Not judged` saying what goes there; no emoji anywhere in it. From 5d-iv the `deferred <home>` value's line says
a home is also where a repair with no commit was made, and the `rejected`
line keeps its one meaning.
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
through one reader, `record_findings(reader, text, rel)`, which runs
`unclosed` (a `<!--` comment or a fence that never closes, refused at its
opener; 5d-i), then `findings(reader, lines, rel)` over `reader.readable`'s
lines, then `record_target(reader, lines, rel)`. `findings` reads the one
`## Findings` section (`FINDINGS_HEADING`), split at its `### ` headings,
each section holding exactly one line matching `^verdict: (.*)$`
(`VERDICT_LABEL`), the value read by `verdict_of(value)` as `OPEN`, `FIXED`
with its commit, `REJECTED` or `DEFERRED` with its home (`deferred_home`,
`issue_of` kept for `release_seal.py` and the panel), else `None`; exactly
one line matching `^location: (.*)$` (`LOCATION_LABEL`), its value read by
`location_of(value)` as the list of paths of one or more `` `path` ``,
`` `path:line` `` or `` `path:first-last` `` items joined by `, `
(`COORDINATE`), else `None`; at most one line matching
`^regression: (.*)$` (`REGRESSION_LABEL`), its value read by
`reference_of(value)` as `(round, finding)` from `round-<N>#<n>` or
`(round, None)` from `round-<N>` (`REFERENCE`), else `None`; from 5d-v, at
most one line matching `^reopens: (.*)$` (`REOPENS` = `"reopens:"`,
`REOPENS_LABEL`), its value read by `reference_of(value)` and refused where
it names no finding (`round-<N>` alone: a reopened close is a finding's);
and returns a
`Finding` per section — its `verdict:` line, heading, heading number,
verdict, located paths, regression reference with that line, reopened
reference with that line, and heading
line. Before any of that, every readable line matching `MISSPELT_LABEL` —
the first word, case-folded and stripped of `*`, `_` and `` ` ``, one of the
eight labels (`EXACT_LABEL`, `reopens` among them from 5d-v) or an old
spelling, `Target SHA`, `refixes` or
`fix of a fix` (`OLD_LABELS`), followed by `:` — that is not the exact
lowercase form is an error naming the line and the label it would have to
read (`spelt_otherwise`). Every `None`, every section with no or two
`verdict:` or `location:` lines, two `regression:` lines, two `reopens:`
lines, or one of each (refused at the later line, the refusal naming
`regression:` for a defect a fix pass's own commit made and `reopens:` for
a close that does not hold otherwise), a finding's
label outside a section of `## Findings`, a `target:` or `confirms:` line
inside one, a `confirms:` line outside `## Confirmations`, and a missing or
doubled `## Findings` is an error the arm names by path, line and the
finding's heading. `record_target` reads the one `target:` line outside
every finding (`TARGET_LABEL`, `TARGET_VALUE`): `<sha> against <base>` or
`<sha>, fixes <a>..<b>`, the commit its first word; none (`NO_TARGET`), two,
or another shape is an error by line. A `FIXED` whose commit HEAD does not
descend from (`is_ancestor`) is refused, and so is one whose changed paths
(`touched(root, commit)`, `git diff-tree --no-commit-id --name-only -r
--root <commit>`) hold none equal to or under a located path; on a ready
pull request an `OPEN` finding fails too. `confirmations(reader, lines,
rel)` reads `## Confirmations` where the record has it — none is no error,
two is `TWO_CONFIRMATIONS` — each `confirms:` line at the start of a line
(`CONFIRMS_LABEL`) read as `none` or, through `reference_of`, as a
`round-<N>#<n>` reference with its line; a value that is neither, and a
table row in the section (`CONFIRMATIONS_TABLE`), are errors by line, and
the prose after each line is read for nothing. `round_of(reader, text, rel,
number)` reads one record for the arm: its findings, its `target:` commit,
its `confirms:` references, and the number of every `### <n>. ` heading,
read or refused, so a reference to a refused finding still names one the
record holds. `channel(rounds)` takes the item's records in number order
and, for each pair N, N+1, refuses every finding of N at `FIXED` or
`REJECTED` that no `confirms:`, `reopens:` or `regression:` line of N+1 names, at
that finding's own heading line in N's record, naming N+1's record and the
reference it owes, its message naming the three labels; it refuses any
reference, on any of the three labels, whose round is not an earlier
record of the item or whose finding number that record does not hold, and
any reference at all in the first record; on a ready pull request it
refuses a `FIXED` or `REJECTED` finding of the last record at its
`verdict:` line with `VERIFYING_ROUND`. A `DEFERRED` finding owes nothing,
which is what makes Q11's `deferred <where it was repaired>` need no reader
change. Nothing of a record's `severity:` or `answer:` value is read, and no
emoji is read for. The reader strips fences and comments first
(`reader.readable`), so a labelled line inside a fix block is not a line; a
fence closed on the wrong line is the stated limit. The panel's
`broad_gate.py#rounds_rows` and `release_seal.py#chain_counts` keep reading
through `record_findings`, so a record with any refusal adds nothing to a
count. `skills/verify/scripts/broad_gate.py`:
`--record <item>` writes `broad-gate.md` (`<sha> against <base>`, newest first,
earlier runs kept) on both routing answers; `round_count`, `sealed_record`,
`kept_broad_gate`, the `round_record` import and `round_record.seal_home`'s
call leave; `seal_home`, the root resolver, stays; the panel and the stamp
values are unchanged, so `rounds_rows`, which draws the panel's `rounds` row,
stays and counts `DEFERRED` findings through `chain_check.findings`, a
record the reader refuses adding nothing. `.github/scripts/release_seal.py#chain_counts`
counts the same way and leaves `deferred` *not read* for such a record.
`agents/sealer.md`: frontmatter `model: opus`; step 3 is the one list of the
sealer's acts (§*The sealer*), two of them from 5d-ii — the sample of the
smith's claims re-run, and the removals confirmed absent — and no reading of
a `fixed` commit against a location.
`docs/the-review-record.md`: the record, the four run rules, the handoff
rule, the sealer's check, each with `Enforced by:`; §*The round record*
states the shape, the eight lowercase labels and the old spellings refused,
the four values, the two severities, the location spelling, the `target:`
line and the channel's reference on its three labels, `confirms:`,
`reopens:` and `regression:` (5d-v), with the touch rule's `Enforced by:` T34
in place of *nothing — the sealer reads*; its fix-pass paragraph says, from
5d-iv, that a repair made outside the tree with no commit closes `deferred
<where it was repaired>` and one made by a commit `fixed <commit>`, its
`Enforced by:` gaining T41; §*What the check reads at the pull request*'s
records paragraph states the labelled lines, the `confirms:` lines, the
fail-closed reading, a finding holding both a `reopens:` and a
`regression:` line refused (5d-v), and how it errs (a touching commit that
fixes nothing; a fence closed on the wrong line), its `Enforced by:` the
check's pins alone; §*The run*'s regression rule names the `regression:`
line and its reference, and says it marks a defect a fix pass's own commit
introduced, and from 5d-v says that a `regression:` line is routed by the
comparison of the fix with the frame its grounds state (S27; its bold
sentence and `tests/test_the_rules_have_one_owner.py`'s rule 16 entry
rewritten to it), and that a close that does not hold where no fix
pass's commit made the defect is raised again on a `reopens:` line as an
ordinary finding that gets its fix pass, its `Enforced by:` gaining T44 and
T45, and its verifying-round rule names the three lines; §*The guarantee* points at `agents/sealer.md` step 3 and step 4
for the acts and lists none. `templates/config.md` §*What no row governs*
lists the literals the check reads — `target:`, `## Findings`, `verdict:`
with `open`, `fixed`, `rejected` and the `deferred` in `deferred <home>`,
`location:`, `regression:`, `reopens:` (5d-v), `## Confirmations`,
`confirms:`, `none`, `round-<N>#<n>` — and the labels the parties and the eval graders read,
`severity:` with `must` and `should`, `answer:`, the `## Not judged` and
`## Probes` headings, beside `guarantee.md`'s own `Target SHA`; the
capitalised labels, `Fix of a fix:`, `refixes:`, `Confirms` and `answered`
leave the list. `evals/scripts/behaviour.py`: the shape grader `shape-findings` reads
`^## Findings` and the first `^### \d+\. ` section's `^verdict: ` line and
holds the record free of emoji; `replay_targets.py#truth_pattern` and
`seed_defects.py` emit `^location: .*<path>:<line window>`, the window ±15
lines of the truth, and never match a `path#unit`; the nine
warden cases and the three sealer cases are regenerated through
`rule_cases.py`, `replay_targets.py --case` and `seed_defects.py --case`,
and `rule_cases.py#SEALER_ROUND` is the new shape.
`skills/code-review/orchestration.md`: §*the run ends
with a verifying round*, §*the cap*, §*a regression sends the work item
back to its framer* (its heading as it stands at 80636f64), §*the pull
request opens before round 1*, §*verify before posting* rewritten to the
record above, and from 5d-v the verifying round's `Job` row and its
closing paragraph to S26, and the regression section, heading and first
paragraph, to S27; §*a note closes once*, §*a fix pass adds the unit*, §*then say
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
that reading's — a planning figure, which #957 counts again on its own
tree where it needs one. The builder's two, `overview.md` and
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

## Rule changes

- nothing
  why: written: the round record, the check and the guarantee, in
    docs/the-review-record.md; internal: the proof harness, held by its tests.

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
| the verdict table and its reader (phase 5d) | `templates/sdd-round.md`'s `## Verdicts` table, `## Paste-ready fixes` and `## Executed probes`; `chain_check.py#verdict_table`, `#verdict_of` as a cell reader, `#deferred_parts`, `#open_findings`, `VERDICTS`, `VERDICT_COLUMN`, `GROUNDS_COLUMN`, `BLOCKING`, `SHOULD`, `FINDINGS`, `CLOSES_BY`, `EVERY_CLOSE`, `FINDING_WORDS`, `CLOSED_WORDS`, `VOCAB`, `MARKER`, `SEPARATORS`, `HOME_MARKS`, `DEFERRED_HEAD_RE`, `OUT_OF_SCOPE`, `NO_HOME`; the words `confirmed`, `out of verified scope`, `withdrawn`, `not a defect`, `agreed, fixed` as verdicts; `tests/test_chain_check.py::TestVerdictTable`, `::TestOpenFindings` (T19, T24), `::TestVerdictOf` as it stands, `::TestDeferredHome` as it stands, `::TestMain::test_the_refusal_names_the_words_that_close_a_row_of_its_mark`, `::TestMain::test_a_record_written_by_the_old_generator_reads` (T13, the corpus run); the table fixtures of `tests/test_broad_gate.py`, `tests/test_the_seal_is_taken_once_by_the_sealer.py` (`VERDICT_HEADER`, `OPEN_ROW`, `record_text`, `deferring_record`) and `tests/test_the_release_seal_is_drawn.py` (`ROUND`); `tests/test_the_pull_request_language_is_the_repositorys.py#ROUND_RECORD_FIELDS` and the constants `_literal_strings` reads; `evals/scripts/behaviour.py`'s `shape-verdicts-table` grader and the `^\| (?:🔴\|🟡) \d+ \|` truth pattern of `replay_targets.py#truth_pattern` and `seed_defects.py`; `rule_cases.py#SEALER_ROUND` and the sealer scaffolds it wrote | §*What a round records*: a finding is a section with a `verdict:` line, read by `chain_check.py#findings`, and the fail-closed reading is T25–T28; the other readers read through it, and the graders read `## Findings` and `location:` |
| the emoji vocabulary and the `#` cell as record rules (phase 5d) | `docs/the-review-record.md` §*The round record*'s vocabulary paragraph and §*What the check reads*' open-row paragraph; `skills/code-review/SKILL.md` §*Findings format*'s four-line block, the bare-integer-id paragraph, the Finding-cell paragraph and the Grounds-cell paragraph (#189); `agents/warden.md`'s `#` cell sentences (its ❓ row paragraph and §*Report*'s last two paragraphs); `templates/config.md`'s literal list rows for the headings, columns and words; `README.md:182`'s *no row left open*, `README.ko.md:173`'s 판정표 sentence, the step comments of `.github/workflows/hygiene.yml` and `templates/hygiene.yml`; this item's `changelog.md` first two entries where they state the table and the marks; `docs/the-agent-set.md:56`'s `Enforced by: tests/test_chain_check.py::TestVerdictTable` | two severities for people, `must` and `should` (the words set on 2026-10-16; 5d-i wrote `blocks merge` and `fix or justify`); a confirmation and a not-judged item are rows of their own sections; the sentences are rewritten in place to the shape and the `Enforced by:` lines name the new groups |
| the sealer's act over a `fixed` commit's location (phase 5d-ii) | `agents/sealer.md` step 3's sentence *For every round-record row closed `fixed <commit>`, confirm the commit is on the branch and touches the row's `Location`*; this file's §*The sealer* step 3 clause and §*What a round records*' sealer row as they stood; `docs/the-review-record.md` §*The round record*'s *Enforced by: nothing — … the sealer reads every `fixed <commit>` against its finding's `Location:`* and §*What the check reads*' *the sealer reads that commit against the finding's `Location:`*; `plan.md` §*Operational impact*'s *its second act reads each `Verdict: fixed <commit>` against the finding's `Location:`* and Alternative AI's *the sealer keeps "touches the `Location:`"* | the check reads it: `chain_check.py#touched` against `location_of`, T33 and T34 (S22); the one-list design keeps its two pins, and T40 pins the two acts |
| the capitalised labels, the two-word `Fix of a fix:` and the severities `blocks merge` and `fix or justify` (phase 5d-ii) | `templates/sdd-round.md`'s `Severity:`, `Location:`, `Verdict:`, `Fix of a fix:`, `Answer:` lines and its comment; `chain_check.py#VERDICT_LABEL` as `^Verdict: `; `docs/the-review-record.md` §*The round record* and §*What the check reads* where they spell them; `templates/config.md` §*What no row governs*' rows for them and `tests/test_the_pull_request_language_is_the_repositorys.py#ROUND_RECORD_FIELDS`; this item's six records' lines; then in 5d-iii `agents/warden.md` §*Report*, `agents/smith.md:190-193`, `skills/implement/SKILL.md` §5, `skills/code-review/SKILL.md` §*Findings format*, `skills/code-review/orchestration.md`'s two-cells paragraph, `evals/scripts/behaviour.py`'s `^Verdict: `, `replay_targets.py#truth_pattern` and `seed_defects.py`'s `^Location: `, `rule_cases.py#SEALER_ROUND`, this item's `changelog.md` | lowercase labels, `must` and `should`, read fail-closed (S24; T32); `guarantee.md`'s `Verdict:` is not a round record's label and keeps its spelling (`plan.md` Alternative AM) |
| the field table, the confirmations table, `refixes:` and `answered` (phase 5d-iii; the owner, 2026-10-16) | `templates/sdd-round.md`'s `\| Field \| Value \|` table with its `Target SHA` row, its `## Confirmations` table with the `Confirms` first column, its `refixes:` line and its `answered` value; `chain_check.py`'s `REFIXES_LABEL`, `ANSWERED`, `#target_of` reading a round record's `Target SHA` row (it reads `guarantee.md`'s alone now), and `#confirmations`' table and `Confirms`-header reading; the unconfirmed finding's refusal at line 0 of the next record; `docs/the-review-record.md`, `templates/config.md` §*What no row governs*, the language test's literals, the parties' texts, the READMEs and this item's `changelog.md` where they spell them; this item's six records' tables, `refixes:` lines and `## Confirmations` rows (rewritten at 92991623) | one `target:` line; a `confirms:` line per confirmation, the section optional and a second refused; `regression:`; `rejected`, owing the next round a `confirms:` or `regression:` line as `answered` did; an unconfirmed finding refused at its own heading in its own record; `Target SHA` and `refixes` read only as old spellings refused by line (S23, S24; T32, T36–T38). The guarantee's `Target SHA` row is the sealer's file and stays |
| the sentences sending a repair with no commit to `rejected` (phase 5d-iv; `questions.md` Q11) | `docs/the-review-record.md` §*The round record*'s *A correction to a record, or a repair made outside the tree, produced no commit on the branch and closes `rejected` with where the repair is*; this item's `changelog.md` migration paragraph's *(`answered` is `rejected` now)*, which maps every old `answered` to `rejected`; `tests/test_the_record_is_written_in_words.py`'s module docstring naming *its `Confirms` cells*; whatever else `git grep` finds of the class at the phase's start | `deferred <where it was repaired>` for a repair outside the tree with no commit, `fixed <commit>` for one a commit made, a record correction among them; `rejected` for a finding that does not hold and nothing else, T41 pinning the document's sentence |
| the two-way channel, and the run ending at a rejection named on a `regression:` line (phase 5d-v; round 8's findings 1 and 2) | `skills/code-review/orchestration.md:113-120`'s closing clause, *and names it on a `confirms:` line, or on a finding's `regression:` line where the rejection does not hold, and the run ends at that round*; every sentence giving a close that does not hold only a `regression:` line — *a finding whose `regression:` line names it where it does not* or the same in other words — at `agents/warden.md:119-123` and `:212-217`, `skills/code-review/SKILL.md:187-191`, `skills/code-review/orchestration.md:96`, `templates/sdd-round.md:62` and `:86-87`, `docs/the-review-record.md:74-77`, `:138` and `:227-228`, and this item's `changelog.md` where it says the same; whatever else `git grep -n "regression:\` line"` finds of the class at the phase's start | three relations, each its own line — `confirms:` where the close holds, `reopens:` where it does not and no fix pass's commit made the defect, `regression:` where one did (§*What a round records*); the run ends only on a round whose record holds no `open`, `fixed` or `rejected` finding (S26); T42–T44 |
| a `regression:` line sending the work item to its framer by itself (phase 5d-v; the owner's refinement of 2026-10-16) | `docs/the-review-record.md` §*The run*'s *A regression stops the fix passes, at any round.* and *A round carrying a `regression:` line gets no fix pass: the work item goes back to its framer*; `templates/sdd-round.md:50-51`'s *A round carrying one gets no fix pass.*; `skills/code-review/orchestration.md:122-127`'s heading *A regression sends the work item back to its framer* and *When a round's warden writes a finding's `regression:` line, no fix pass is commissioned*, with `skills/implement/orchestration.md:637`'s delivery row that names the heading; `agents/framer.md:302-304`'s *When a round's warden gives a finding a `regression:` line, … the fix passes stop*; `tests/test_the_rules_have_one_owner.py`'s rule 16 entry pinning the first sentence; this item's `changelog.md:25-26`'s *a finding with a `regression:` line sends the work item back to its framer* | the comparison of the fix with the frame, stated by the warden in one sentence of the finding's grounds and routed on by the orchestrator: the framer where the fix built what the frame says, a fix pass where it departed or the defect came from how it was written, the framer for a second regression on the same unit after a fix-pass route (S27; T45) |
| the emoji in the shipped text this item touches (phase 5d-iii) | `skills/code-review/SKILL.md` §*Findings format*'s four-line block (`🔴 🟡 🟢 ❓`), its `🟡` sentence, the `#`-cell paragraphs and the proof block's `· verdict:  🔴 n · 🟡 n · 🟢 n · ❓ n` line; `agents/warden.md:150-155` and `:262-264`; `skills/code-review/orchestration.md:112`; `README.md:91` and `README.ko.md:78-80` (the cap paragraph's `🔴`, stale since Q1 as well); the step comments of `.github/workflows/hygiene.yml` and `templates/hygiene.yml` where they name a mark; the panel's `rounds` row text where it names one | words: `must`, `should`, a confirmation, a thing not judged; T39 holds the template, the format and the two definitions to it. **Left to #957 and #940, named here**: the `📋` proof-block marker every skill shares (`skills/code-review/SKILL.md:293`, `skills/implement/SKILL.md:529`), `skills/implement/SKILL.md:79` and `:458`'s `✅` (the `## Not verified` closing mark, `unverified_check.py`'s), `agents/smith.md` and `agents/framer.md` beyond the lines above, the other skills; the history citations in code comments (`broad_gate.py`, `hooks/sealer-stamp.py:118`: *round 1's 🟡 2*) are moments and stay (`overview.md`'s `⬜` row) |
| the `.test_durations` entries the suite no longer collects (phase 5a) | 301 entries, 345.3 s, for cases this branch removed from modules that still exist (`rounds/round-2.md` 🟡 2, `executed`) | pruned by collection — an entry is live when `pytest --collect-only` collects its id — with the round-trip guard 1b875efc used; nothing re-measured, nothing kept in the tree to do it again. The collected cases with no price — held under `STALE_SHARE` by `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py::test_the_durations_file_prices_the_suite`, and counted here by nothing — are priced by the next refresh from a `tests` run, which `CONTRIBUTING.md` §*Running the checks* owns |
| the second and third list of the sealer's acts (phase 5b) | `docs/the-review-record.md` §*The guarantee*'s list of what the sealer re-runs and confirms; `templates/sdd-guarantee.md`'s comment over `## Claims re-run` listing the row kinds | `agents/sealer.md` step 3 lists the acts and §*The sealer* states them; both files point at step 3 and name no act, so `fixed <commit>` outside `seal/specs/` and `changelog/` stands only in the record's vocabulary (`docs/the-review-record.md` §*The round record*, `templates/sdd-round.md`) and in step 3 (`git grep`) |
| the present-tense counts in this item's living documents (phase 5b) | `changelog.md`'s *Lines after* column and its sentence counting test modules and test lines after the branch; `overview.md`'s *the file now holds 7,348 entries … sums to 3,371.9 s* and its S12 row's figures, each unpinned; the frame's own, rewritten by the reframe after round 4: `spec.md`'s *226 collected cases*, *36 records in the tree*, *35 citations*; `questions.md`'s *226 unpriced cases*, *35 citations*; `plan.md`'s *about 3,372 s*, *about 3,000 of its 6,827 seconds*, *68 K lines* | §*A number in this frame*: a figure names its moment or its bound, or leaves |
| the sealer's duty over a 🔴 or 🟡 row closed by another kind's word (phase 5c) | `agents/sealer.md` step 3's sentences from *Read every 🔴 and 🟡 row of every record* to *the verdict is `not sound`*; `tests/test_the_sealer_guarantees.py::TestDefinition::test_the_sealer_reads_every_red_and_yellow_row_not_only_fixed_ones` (round 3's fix) and `::TestDefinition::test_the_sealer_names_such_a_row_in_the_claims_table` (T21, phase 5b); `docs/the-review-record.md` §*What the check reads at the pull request*'s open-row paragraph from *and a 🔴 row that reads `confirmed` passes the check* to *unless a later round answers it*, and the T21 name in its `Enforced by:`; the clause of this item's `changelog.md` sealer entry from *It reads every 🔴 and 🟡 row of every round* to *unless a later round answers it*; `questions.md` Q8 and `plan.md` Alternative Z's deferral; `plan.md` row 9's fourth sealer case `rule-sealer-closed-by-another-kinds-word`; S20's part-B clause | the check refuses the row (S3, S20): the fix pass's three words are the only answer a finding takes, and `chain_check.py` reads that fact at the pull request. The one-list design of the reframe after round 4 stays as it is, since round 4's finding — a list of the acts in three files stales — holds with three acts as with four: `templates/sdd-guarantee.md`'s comment and `docs/the-review-record.md` §*The guarantee* keep their pointers at step 3, and T22 and T23 keep holding them |
| S21's claim of a reader over five documents (phase 5c) | S21's *the sealer's step 4 reads the five documents against the tree* and the same sentence under §*A number in this frame*; `plan.md`'s and `questions.md`'s *the frame's own three documents were rewritten to it at the reframe*; `plan.md` Alternatives X and Y's verdict clauses naming the sealer as the reader | §*A number in this frame*, narrowed: the rule covers the shipped surface, the work item's documents are readings at a moment, and the sealer's step 2 reads three of the five and its step 4 counts nothing. `questions.md`'s *36 records* names round 2's probe, the one frame-time figure whose sentence named no moment anywhere |
| the chain's test modules on removed arms | of the 70 modules naming the three scripts, every module or case whose subject is a removed field, arm or subcommand — `test_the_fixes_close_the_record.py`, `test_a_fix_of_a_fix_is_counted.py`, `test_the_record_is_generated.py`, `test_the_record_is_held_to_the_floor_and_the_depth.py`, `test_a_record_precedes_the_fixes_it_commissions.py` among them; the full list is phase 3's | the guard of each named one line in `phases/phase-3.md`; what still holds has a case in `test_chain_check.py` or `test_broad_gate.py` |
| the old sealer | `agents/sealer.md` as it stands (*it judges nothing*; the `Broad gate` cell as its one write; Sonnet as its model); `evals/behaviour/sealer/rule-sealer-{green,failing-test,record-open}/` | the guarantor above and its three cases |
| two warden shape graders | `evals/behaviour/warden/*/graders/shape-needs-a-fix.md`, `shape-loses-a-record.md`; the report path in every warden shape grader | the fields are gone; the path is `rounds/round-N.md` |
| the orchestrator rows for removed acts | `skills/implement/orchestration.md` §*which of these acts runs itself*: the rows for the note, the fix surface, `Ran by`, *then say who checked them*, *commit the record before commissioning*; `tests/test_every_orchestrator_act_names_its_delivery.py`'s pins of them | the table reads the headings, so the rows go with them |

**Moved to #957, not removed by this item** (the owner's split, 2026-10-16).
None of these is a claim of absence the sealer reads against this item's
tree; each is #957's to frame on the released tree.

- The three removals this table held for part B: the preload beyond the
  contract (every `agents/*.md` `skills:` entry other than `agent-contract`),
  the contract's numbering (`§1`–`§17` and every `§N` citation of them), and
  the five definitions and four skills as written.
- This frame's promises of part B's outcomes, cut from it: §*Every agent
  definition, written anew from its job* (the one shape, the preload rule,
  the six-row table of jobs, orders, openings and rules, the size estimate),
  now §*The agent definitions this item touches*; §*The proof*'s baseline,
  pass rule and run budget; §*Scope*'s part-B paragraph; S14–S18.
- `plan.md` rows 6–9, the test-row sentence on how part B's rewrites are
  verified, Alternative L's per-agent preload decision, and the
  operational-impact bullet on part B; `questions.md` Q4, Q5 and Q6, and the
  owner's run budget for the proof (≈ 120 runs, ≈ $150, 2026-10-14).

## Open questions → questions.md

Framed 2026-10-14 by framer, before the build.
Reframed 2026-10-15 by framer, after round 0.
Reframed 2026-10-15 by framer, after round 2.
Reframed 2026-10-15 by framer, after round 4.
Reframed 2026-10-15 by framer, after round 5.
Reframed 2026-10-16 by framer, after round 6.
Reframed 2026-10-16 by framer, after round 8.
