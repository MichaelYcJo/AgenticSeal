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
| Build: the code, its tests, the phase record; the fix pass | judgment | `smith` | code and tests; `phases/phase-N.md`, `overview.md`, `changelog.md`; the `Verdict` and `Grounds` cells of the round record its fix pass answers |
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
   mutation it says went red. For every round-record row the smith closed
   `fixed <commit>`, confirm the commit is on the branch and touches the row's
   `Location`. For every `## Removes` row of `spec.md` and every removal this
   release names in its changelog fragments, confirm nothing of it stands in
   the tree.
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

A round records **what it reviewed, what it found, and what fixed it**, in one
file the warden writes and the smith's fix pass completes:
`seal/specs/<work-item-id>/rounds/round-N.md`, from `templates/sdd-round.md`.

```
# <work-item-id> — review round N

| Field | Value |
|---|---|
| Target SHA | <sha> against <base> · a verifying round: <sha>, fixes <a>..<b> |

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | <what is wrong, why it matters; `fix of a fix` where the unit is one the fixes under review added or changed> | `path:line` | open | <the clause, the behaviour, the constraint> |
| 🟢 | round N-1's finding 2 is closed — <what> | `path:line` | confirmed | <how it was confirmed> |
| ❓ | <what could not be judged> | `path:line` | ❓ out of verified scope | <why, and who answers it> |

## Paste-ready fixes

<one block per 🔴 and 🟡, the artefact and not a description of it>

## Executed probes

| What was run | Result |
|---|---|
```

Four things about it, each the whole of a rule:

- **The vocabulary is four severities and five verdict words.** 🔴 blocks
  merge, 🟡 fix or justify, 🟢 pass, ❓ out of verified scope. A 🔴 or 🟡 row
  carries a bare-integer id and opens at `open`; the fix pass closes it
  `fixed <commit>`, `answered — <grounds>` or `deferred <home>`. A 🟢 row
  reads `confirmed`. **⬜ leaves.** A sentence an agent reads and acts on is a
  defect when it is wrong, and is 🟡; a sentence in a record that merely reads
  badly is not written as a finding.
- **The warden writes the record, and no generator copies it.** Today the
  warden writes `round-N-report.md` and `round_record.py new` copies its three
  tables into `round-N.md` beside ten fields the warden never wrote. The copy
  is the half of the inherited bytes that says nothing the report did not.
- **The smith's fix pass writes two cells per open row and nothing else in
  the file.** That is its one write into the record, named in its
  definition. There is no fix table handed to a generator and no `close`.
- **The reviewed commit is a fact every check rests on, and it is the one
  field.** The broad gate's run lives in `broad-gate.md`, the sealer's verdict
  in `guarantee.md`, and the pull request knows its own branch.

### What leaves, what stays, and the evidence for each

Judged on what its history shows it caught against what it cost. The 0.22.0
records above are the measured history; where a field's defence is a spec's
citation of an older issue, that is `read` and says so.

| Mechanism | What it caught, as the history shows | What it costs | Verdict |
|---|---|---|---|
| `Target SHA` | every arm of the check rests on it; the proof's replay cases clone at it | one row | **stays** |
| The `Verdicts` table in its five columns | the findings themselves; the proof's `truth-` graders read its rows | the warden writes it anyway | **stays**, unchanged columns, so every record in the tree today reads under the new check |
| `Executed probes` and `Paste-ready fixes` | contract §4 in the record; the smith pastes | the warden writes them anyway | **stay** |
| `round-N-report.md` beside `round-N.md` | nothing: the record was the report's tables copied | 19 files, 303 KB of 564 KB in 0.22.0; half of what a later round inherits | **leaves**; the warden writes `round-N.md` |
| `round_record.py` (`new`, `close`, `notes`, `seal`), `bin/round-record{,.cmd}` | wrote the copy and the derived fields, applied the fix table, counted the notes | 5,596 lines, 35 test modules, the generator's refusals at the keyboard (#503, #866 in `docs/round-record-spec.md`, `read`) | **leaves whole** |
| `Pass` box | whether a row is still open | a box that restates the table | **leaves**; the check reads the rows: no `open` verdict on a ready pull request |
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
`python3 skills/code-review/scripts/chain_check.py --baseline …`, and its
existing records are read: the new check reads `Target SHA` and the `Verdicts`
table, which every record written since the generator shipped carries, and
ignores the fields it no longer judges. `bin/round-record` is gone, and the
orchestration text that named it is rewritten in the same release. The
changelog fragment of this item says so in one paragraph a user reads before
updating.

## Every agent definition, written anew from its job

**One shape for all five.** Frontmatter: `name`, `description`, `skills:
[agent-contract]`, and `model: opus` in the sealer's alone. Body: the job in
one sentence; where it works; the order of its work as a numbered list; what
it must not do; what it writes; which file it opens at which step; then its
rules, each one paragraph opening with the rule in bold, at most one sentence
of why, ending in `Enforced by: <test ids>` or one link. No story, no
measurement, no account of what a rule used to say. The contract is the same
shape and numbers its rules anew, 1..N; the 35 citations of the old `§N`
outside the rewritten files (`docs/` 18, `hooks/` 10, `templates/` 5,
`CONTRIBUTING.md` 2) are rewritten in the same commit, and the 423 in 89 test
modules move with the modules the agent phases rewrite.

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
| `smith` | build a phase of the frame, or answer a round | 1 read `spec.md`, `plan.md`'s row, the phase record before it; say whether the frame holds · 2 open `skills/implement/SKILL.md` · 3 build in slices, narrow tests as you go, commit at each standing step · 4 write `phases/phase-N.md`; a fix pass instead fills the `Verdict` and `Grounds` cells of the round it answers · 5 open `skills/writing-style/SKILL.md` and hand back | implement at 2, writing-style at 5 | code, tests, `phases/phase-N.md`, `overview.md`, `changelog.md`, two cells per open verdict row | a new test starts from its group — read the function's tests first, extend one where you can, and say in the hand-back which case the group did not cover; a check refusing correct code is the check's defect; a fix pass adds no mechanism; a removal the frame did not name is an `overview.md` divergence |
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
  with those fields. Rule 3 reads shape graders on the new side only, since
  the old side's shape is the old record's by construction; `reach-` graders
  stay at 100 % on both sides.
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

**In — part A, this work item** (`plan.md` phases 3–5): the review record and
its checker; the broad gate's one record file; the sealer as guarantor with its
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
| S1 a round is one file | a warden reviews a fixture branch | `rounds/round-1.md` exists in the branch worktree with `Target SHA`, the five-column `Verdicts` table, `Paste-ready fixes`, `Executed probes`; no `round-1-report.md`; the warden eval's shape graders pass on it |
| S2 the fix pass completes the record | a smith answers round 1 | every 🔴/🟡 row's `Verdict` reads `fixed <commit>`, `answered — …` or `deferred <home>`; no other line of the file changed (`git diff` of the record shows only those cells) |
| S3 an open verdict stops a ready pull request | a record with a row at `open`, pull request not a draft | `chain_check.py` exit 1 naming the record, the row id and the word; a draft prints the same and exits 0 |
| S4 the last fixes are read | the last record's `Target SHA` is behind HEAD by a commit touching a file outside `seal/specs/<id>/` | exit 1 naming the commit and *a verifying round is owed*; HEAD moved only by record commits passes |
| S5 the broad gate has one home | `broad-gate --record` on a green run, either routing answer | `seal/specs/<id>/broad-gate.md` reads `<sha> against <base>`; no `Broad gate` row anywhere; a ready pull request whose file names a commit other than HEAD fails |
| S6 the sealer guarantees | a sound fixture item with a pull request body | `guarantee.md` with the five sections and `Verdict: sound`; nothing else in the tree changed; the report labels every claim |
| S7 the sealer catches a story the tree contradicts | a pull request body claims a removal the tree still carries; a phase record claims `seen red` for a case green against the old code | `Verdict: not sound — <the claim>` naming the party and the coordinate, once per case |
| S8 the sealer's verdict gates | `guarantee.md` reads `not sound` or `undecidable`, or names a commit other than HEAD | exit 1 at a ready pull request naming the file and the verdict |
| S9 the `fix of a fix` stop is a judgment | a warden's record marks a finding `fix of a fix`, in any round of a run | the orchestration text says no fix pass runs and the work item returns to its framer, who redraws the frame; `chain_check.py` reads nothing of the mark; the sealer's parties check names it |
| S10 nothing kept beside the tree | after phase 3 | no `round_record.py`, `bin/round-record{,.cmd}`, `review-history-guard.py`, `tests-todo.md` reader, `Fix range`, `Contract changes`, `New units`, `Fix of a fix`, `Needs a fix`, `Loses a record`, `Written late`, `Ran by`, `Fixes checked by`, `⬜`, `notes --at` outside `seal/specs/` and `changelog/` (`grep -rn` over the tree) |
| S11 old records still read | the four 0.22.0 items' records (`rounds/round-N.md` as they stand) | `chain_check.py --root` over a copy whose declaration names one of them: every arm reads `Target SHA` and the table and refuses nothing for the fields it no longer judges |
| S12 the suite is lighter | after phase 3 | `.test_durations` summed over the modules that name `chain_check`, `broad_gate` is below 1,500 s (from 4,553 s); the deleted modules' guards listed one line each in `phases/phase-3.md` |
| S13 one spec for the record | after phase 3 | `docs/the-review-record.md` exists, every rule paragraph ending in `Enforced by:` or a link, `rules --check` exit 0; the three old documents are gone and no file names them |
| S14 the agents preload the contract alone | part B | every `agents/*.md` `skills:` list is `[agent-contract]`; `payload_meter --agent <a>` shows two files in the agent share |
| S15 an agent opens its skill at the step | part B | the behaviour cases of each agent pass on the new side; a case that reads a skill-shaped output (the warden's findings format, the smith's phase record) is named per agent in the phase record |
| S16 a rewritten definition is proved not worse | each part B phase | `evals/<agent>-phase-N.md` with `Verdict: pass`; the record test green |
| S17 no rule is lost unseen | each rewritten file | the phase record lists every bold-led rule of the old file with its new coordinate or its removal and why; every test that pinned a sentence is green on the new one or removed with a row |
| S18 the contract numbers anew | part B | `skills/agent-contract/SKILL.md` rules 1..N in order; no `§` citation outside it names a number it no longer carries (`grep -rn "§[0-9]"`) |
| S19 nothing asks a person | the whole change | no `AskUserQuestion`, no `input()`, no new prompt; the eval scores itself; the sealer's `undecidable` is a written question, not a stop mid-run |

## Data & interfaces

`templates/sdd-round.md`: the shape under §*What a round records*, comments
documenting the four verdict words and the `fix of a fix` mark.
`templates/sdd-guarantee.md`: `| Field | Value |` with `Target SHA`,
`Broad gate`; `## Claims re-run` (`| Claim | Source | Command | Result |`);
`## The parties` (`| Party | Says | Agrees with | Disagrees with |`);
`Verdict: sound` · `not sound — <what>` · `undecidable — <question>`, one line,
and an `Answered <date> by <who>: …` line under it where the owner answered.
`skills/code-review/scripts/chain_check.py`: `main(argv)` with `--baseline`,
`--root`, `--worktree` as today; arms `declaration`, `frame`, `records`,
`broad_gate`, `guarantee`; exit 0 · 1 naming `path:line: why` · 2 unreadable;
a draft prints every arm and exits 0. `skills/verify/scripts/broad_gate.py`:
`--record <item>` writes `broad-gate.md` (`<sha> against <base>`, newest first,
earlier runs kept) on both routing answers; `round_count`, `sealed_record`,
`kept_broad_gate`, the `round_record` import and `round_record.seal_home`'s
call leave; `seal_home`, the root resolver, stays; the panel and the stamp
values are unchanged, so `rounds_rows`, which draws the panel's `rounds` row,
stays and reads only the verdict tables.
`agents/sealer.md`: frontmatter `model: opus`. `docs/the-review-record.md`:
the record, the four run rules, the handoff rule, the sealer's check, each
with `Enforced by:`. `skills/code-review/orchestration.md`: §*the run ends
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
