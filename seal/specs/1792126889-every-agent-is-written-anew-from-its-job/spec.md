# Feature Specification: every agent is written anew from its job (#957)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

This frame was drawn as one work item and split on 2026-10-16, on the
owner's answer to `questions.md` Q1. The mechanics it found in the way — the
red Windows case and the harness's stale sentences, the `Reads:` census and
the rider stamps, the round record's grammar as one table, the closing word
of `## Not verified` — are #964's, framed at
`seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/`,
which merges into `release/v0.22.1` first. This item is rebased onto that
branch after the merge and builds its agents on the tree #964 leaves.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* | Every definition, skill, mark, label and test this frame touches is weighed by what it caught against what it costs, and nothing is kept because it is there. A change rewrites in place and removes what stood on the old fact in the same commit. Nothing is kept beside the tree to stay in step with it, which is why the per-segment numbers leave the definitions and every figure of the proof is read from an eval record |
| `CLAUDE.md` §*The goal a design is chosen against* | No step of this item asks a person mid-run. What needs the owner is in `questions.md`, each row with its default, and the evaluation runs on the orchestrator's account |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The item changes one gate's owner: the broad gate becomes the orchestrator's one command before the sealer is spawned. It names what the sealer's own run caught against its cost, the failure direction, a prompt budget of zero and its `## Removes` rows. The two gates removed and the two changed before this item builds are #964's |
| `docs/the-agent-set.md` | One contract every agent receives, one definition each; the writer of a frame is not its builder; a subagent asks nobody; a spawn's payload is measurable and paid on every spawn. Rewritten in place where this item changes what the sentences describe: the broad gate's owner and the section-number rule of a contract written anew |
| `docs/the-review-record.md` §*The guarantee*, §*The run* | The guarantee's first act, the broad run, moves to the orchestrator's script run before the sealer is spawned. The cap counts from the last design change and no person is asked mid-run. The grammar table under §*The round record* is #964's; this item changes no label or value of it |
| `docs/the-broad-gate.md` §*One act, one owner, and the owner is an agent* | Rewritten in place: the act is one, its owner is the orchestrator's one command before the sealer is spawned, and no agent runs it |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The changelog is this item's `changelog.md` fragment, and it carries the per-agent before-and-after table |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The item alters what every spawn reads, so it sits on the top rung and this frame exists |
| #957's body (the owner, 2026-10-13 to 2026-10-16) | The one source for what was decided: six numbered items, of which 3 and 5 now point to #964, the rules the rewrite states in place, and the two axes of the proof. Where this file and that body differ, the body holds |
| #964's body and frame (the owner, 2026-10-16) | What this item builds on and does not redo. The shared readings of the tree it holds are cited from here by section, because it merges first and is in this item's tree after the rebase |
| #923's `spec.md` §*The agent definitions this item touches*, §*The proof harness, as this item leaves it*, `plan.md` phases 6–9 at 6a40c790 | The frame this one starts from, re-read against the released tree. What still holds is restated here; what moved is named under `## Removes` or in `plan.md`'s Alternatives |
| #940, #941, #942, #945, #956 | What an agent opens on demand, `docs/`, the test layout, the process's cost and the audit of readers are theirs. This item rewrites a file of theirs only where it makes a sentence of it false, and says so in the phase record. §*What the referenced issues already decided* holds what each settled |
| #929, #931, #944 (closed in 0.22.0) | The per-pull-request mutation check is gone and `mutation-check` is a release-time tool; `.test_durations` is measured on every run and this frame refreshes nothing by hand; the record of truth is a test named by an `Enforced by:` line, held by `rules --check`, with no hash or index beside the tree. §*What the referenced issues already decided* holds what each settled |

## Scope

**In.** The five definitions under `agents/` and `skills/agent-contract/SKILL.md`
written anew from their jobs, each `skills:` list cut to `agent-contract`,
and the four skills the lists used to inject (`code-review`, `implement`,
`writing-style`, `legacy-parity`) written to the shape of §*The shape of a
definition* so an agent that opens one at its step reads the current rule
once. Every mark, label and constant an agent writes or a check reads,
judged by §*Marks and labels*, beyond the three #964 disposes of. The broad
gate as the orchestrator's script run before the sealer. The sealer's model
by measurement. The baseline and the per-phase proof, the test modules that
pin the rewritten files, the eval cases that grade them, and the changelog
fragment.

**Out, and whose.** The mechanics — the red Windows case and the harness's
two stale sentences, the `Reads:` census and the rider stamps, the round
record's grammar as one table, the `U+2705` closing mark — #964, which
merges first; this item builds on the tree it leaves and reads its
`spec.md` for them. `skills/verify/SKILL.md` beyond the sentences this item
makes false (§*Every agent seals what it verified* and §*Seal block*, which
describe the proof block), `skills/settle/`, the small skills, `templates/`
beyond `sdd-overview.md:9`, `sdd-questions.md` and `sdd-guarantee.md`,
`CONTRIBUTING.md`, `CLAUDE.md` — #940. `docs/` beyond the four documents
named in §*Grounding* — #941; the `Enforced by:` label keeps its spelling in
every file this item writes, because its rename to one lowercase word is
#941's decision with `rules.py` as its reader, and a tree carrying two
spellings is the state the owner's label rule forbids. The test suite's
layout beyond the modules this item writes, re-points or deletes — #942.
The agent-lifetime rule, the folding rule, the process archive — #945. The
audit of every reader of written text — #956. The emoji in output a script
prints for a person and no agent or check reads — `publish_release_note.py`'s
release-note headings, the seal stamp's drawing, the hooks' terminal
messages — stay where they are: `questions.md` Q9 put them in front of the
owner, who kept the default on 2026-10-16, since the owner's rule reaches
text an agent reads or writes and a check reads, and those are neither. The
quotations of old marks inside test fixtures and inside the four 0.22.0
items' round records stay as the history they quote (#923's Q10).

## What the referenced issues already decided

#957's body names eight issues. Each was read whole, with its comments (#957
and #923 have none; their comments were folded into the bodies). What each
decided or owns, this frame neither redoes nor contradicts. This table is
the one place what each issue decided is written down; #964's `spec.md`
holds only what its own frame does with six of them.

| Issue | Already decided or owned | What this frame does with it |
|---|---|---|
| #923 (closed, 0.22.0) | The round record's shape: one file the warden writes, labelled lowercase lines, `must`/`should`, the four verdict values, `confirms:`/`reopens:`/`regression:` by `round-<N>#<n>`, fail-closed reading, no emoji; the sealer as independent guarantor on Opus with `guarantee.md`; the five-arm check; `broad-gate.md` on either routing answer; the cap of three counted from the last design change; Q7 (an item is judged at its own pull request), Q10 (old quotations stay), Q11 (`deferred <where it was repaired>`) | Not reopened. The grammar table that restates the shape in one place is #964's; the sealer's job keeps #923's five steps and loses only the broad run; its Q2, Q4, Q5 and Q6 moved here as Q4–Q8 |
| #929 (closed, 0.22.0) | The commit-gate test cut by a mutation table with a fixed sample; one launcher holding the Python floor; `case_check.py` and the `cases` CI job gone; `mutation-check` a release-time tool with no bound; a check that generates cases to catch the next gap never converges | No per-pull-request mutation check returns; the `mutation-check` runs in `plan.md`'s Verified-by cells are the smith's own narrow runs at its phase, which `agents/smith.md` step 4 already asks for, never a CI job; the suite's size readings stay the release report's, and the figures here are readings at d4552372 |
| #931 (closed, 0.22.0) | `.test_durations` is measured on every run by the Windows shards (`--store-durations --clean-durations`) and unioned by the `durations` job; `test_the_durations_file_prices_the_suite` fails past `STALE_SHARE`; the release checklist's refresh box is settled there | Nothing here refreshes the file by hand or schedules a run. Where a re-pointing phase removes cases the suite no longer collects and the durations case fails, the smith prunes to the collected ids by the method #923's phase 5a used, and nothing is re-measured |
| #940 (open, 0.22.2) | What an agent opens on demand: `skills/verify/SKILL.md`, both `orchestration.md` files, the small skills, `templates/`, `CONTRIBUTING.md`, `CLAUDE.md`; what `CLAUDE.md` holds | This frame touches `skills/code-review/orchestration.md:178-201` (the gate's order), `skills/verify/SKILL.md`'s two proof-block sections, `templates/sdd-overview.md:9`, `templates/sdd-questions.md` and `templates/sdd-guarantee.md`, each because this item makes the sentence false, and nothing else of #940's set |
| #941 (open, 0.22.2) | `docs/` rewritten to the current rule, split by topic past one read, the `<!-- specs/… -->` markers gone, the backlog settled; `Enforced by:` renamed to `check:` with `rules.py` as its reader | `Enforced by:` keeps its spelling in every file this item writes. The four documents this item rewrites in place are named in §*Grounding*, and each edit is the sentence the item makes false |
| #942 (open, 0.22.2) | One test file per shipped module grouped by function, a success and a failure case per group, flows under `tests/e2e/`, duplicates named, a sweep each release with `mutation-check` unbounded; old tests are a reference | This frame re-points or removes the pins on the files it rewrites; it lays out no other module. The smith's rule *a new test starts from its group* names #942's layout as where the group lives |
| #944 (closed, 0.22.0) | The evidence ledger, its fold, re-read, correction and drift machinery, `survivors.md` and the evidence-check skill are gone; the record of truth is a test named by an `Enforced by:` line, `rules --check` holds that each resolves; the coordinate kernel lives at `skills/verify/scripts/coordinates.py`; rules for agents are held by the behaviour evals | Nothing kept beside the tree comes back; the census and the stamps, the same class, left with #964. The evals are the holder of an agent's rules, which is why the proof is run on them and not on sentence pins |
| #945 (open, 0.22.3) | The agent-lifetime rule (a phase is a fresh spawn handed the phase record), the fix pass's resume threshold, the orchestrator's folding rule, the audit of re-checks, the process archive, all written into the orchestration files by #940 | No definition here states a lifetime or a resume rule; `plan.md`'s phases are spawned as the orchestrator decides under #945's rule when it lands |
| #956 (open, 0.22.4) | The audit of every reader of written text, one table in that issue; the fixes it names go to later releases; whether the fail-closed sentence enters `CLAUDE.md` (#923's Q9) is decided with the table | This frame writes no sentence into `CLAUDE.md`, and the definitions it writes state their own rules, not the readers' |
| #947 (open, 0.22.4) | Measures whether 0.22.0 made development lighter, from the release report's trend, `session_cost.py --segments` and the round records; its *Before* table holds the 0.21.x preload bytes | The changelog table of §*A number in this frame* is written so #947 can read this item's preload, tokens and spend at d4552372 and at the close without a hand-filled figure |

## The shape of a definition

Every file under `agents/` has one shape, and so does the contract. A reader
who knows one knows all six.

1. Frontmatter: `name`, `description` (what to spawn it for, in two or three
   sentences), `model` where the definition fixes one, and
   `skills: [agent-contract]` and nothing else.
2. One opening sentence naming the contract, identical in every definition,
   which `tests/test_every_agent_reads_the_contract.py` holds. The paragraph
   that explained the `skills:` mechanism after it leaves: five copies of one
   explanation are the paste the tenet forbids, and the contract's own
   opening says how it arrives.
3. `## Job`: what the agent does and its one durable write, in one paragraph.
   A definition that names no write names none (contract §6 as it stands).
4. `## Order of work`: numbered steps. A step that needs a skill names the
   file to open, in the form *open `skills/code-review/SKILL.md` and follow
   its two stages*, at the step and nowhere else. A step names what it
   produces and where it goes.
5. `## Never`: what the agent must not do, one line each, no incident
   narrative. The incident lives in the changelog or the issue that found it,
   and a line that needs the incident to be understood is rewritten until it
   does not.
6. `## Rules`: one paragraph per rule the definition owns, each ending in
   `Enforced by: <target>` or `Enforced by: nothing — <why>`. A number a rule
   states is a value a person is accountable for, with the moment or the
   bound it was read at; a measurement of a past run belongs in the
   document that owns the table (the per-segment bars are
   `docs/the-review-record.md` §*The per-segment bars*' and leave the
   definitions).

What explains or records — why a rule exists, which round found it, what it
cost — is not in these files. Each sentence an agent reads is a rule, what
enforces it, or at most one sentence of why with a link.

**What a spawn preloads is the contract, and every other skill is opened at
its step.** The warden opens `skills/code-review/SKILL.md` at step 1 and
`skills/writing-style/SKILL.md` before writing the record; the smith opens
`skills/implement/SKILL.md` at step 1 and `writing-style` before writing
`overview.md`, `changelog.md` or a phase record; the framer opens
`implement` at the step that decides the ladder and the file set, and
`writing-style` before writing the three documents; the scribe opens
`legacy-parity` at step 1; the sealer opens nothing. Where a skill is opened
at step 1 of every spawn, deferring it saves the bytes of the spawn that
never reaches step 1 and nothing else; the saving there is the skill written
shorter, and the cost rule of the proof measures both together. The risk is
an agent that does not open what its act needs, and the behaviour cases read
the output that skill shapes: the record in the template's shape, the phase
record, the three framed documents. A skill whose absence makes a case fail
goes back to that agent's `skills:` list, and the phase record says which
case named it.

**The contract is written anew and numbered anew from §1.** Its rules are
the ones that still hold of every agent, each a paragraph with its
`Enforced by:` line and no incident narrative, plus the four #957 names: an
agent cleans up only what it started, by the PIDs and paths it recorded,
never by a command name or a glob over a shared directory; a check that
refuses correct code is fixed or reported, and the code is never bent to
pass it; a change rewrites the text it amends in place and removes what
stood on the old fact in the same commit; the change a problem calls for is
not avoided, and a structure is weighed as a reference, not a constraint.
§2 is rewritten to the fact §*The broad gate runs before the sealer* states:
no agent runs the broad gate, and a definition is not where it is assigned.
The rule *a section number is never reused* holds from this edition on: a
file written anew starts its numbering anew, and `docs/the-agent-set.md`'s
sentence says so. Every `§N` citation in the tree is rewritten to the new
number in the commit that renumbers (128 outside `tests/`, 326 inside, at
d4552372, `executed`); the round records under `seal/specs/` are history and
keep theirs.

## Marks and labels

The owner's rule (2026-10-16): a mark or label an agent writes or a check
reads has a reader that decides something, or it leaves; what stays is one
lowercase plain-English word at the start of a line, exact spelling only,
anything else refused; no emoji anywhere; a word coined here is replaced by
the common one. Each mark in the tree at d4552372, its reader and its
disposition (`executed` where a count is given); an emoji is named by its
code point so that this file carries none. Three marks of the tree are
#964's and are rows of its `spec.md` §*Marks and labels*: the `U+2705`
closing mark, the `Reads:` docstring line and the rider stamp.

| Mark | Written by | Read by, and what it decides | Disposition |
|---|---|---|---|
| The proof block (`U+1F4CB implement applied`, `U+1F4CB code-review applied`, the `U+1F50F verify sealed` block) in `skills/implement/SKILL.md`, `skills/code-review/SKILL.md`, `templates/sdd-overview.md:9`, `skills/verify/SKILL.md` §*Seal block* | the smith and the warden at the end of every report | no script or check; `tests/test_the_record_is_written_in_words.py` names its marker only to exempt it from the emoji case, `tests/test_broad_gate_rule.py::test_the_seal_block_asks_for_the_row_too` pins its row, `tests/test_one_word_one_meaning.py` names it as the smith's seal. What it caught: nothing recorded in any round record of 0.21.x or 0.22.0 | leaves, with the three pins and the sentences of `verify` that describe it. The hand-back's three labels below carry what the block carried |
| `executed`, `read`, `unverified` | every agent, on every claim | the sealer's step 3 picks its sample from the smith's `executed` and `seen red` claims; the warden audits the smith's `unverified` suite label; contract §4 | stay, as they are already lowercase words |
| `U+2B1C` in `questions.md`'s `Status` column (`templates/sdd-questions.md:10`) | the framer | nothing in code (`executed`: no reader outside test docstrings quoting old records) | the column reads `open` or `answered <date> by <who>`; the template is rewritten and this item's own `questions.md` writes the words |
| `Framed <date> by <who>, before the build.` and `Reframed …` | the framer | `chain_check.py#REFRAME_RE` and the frame arm, which fail a pull request whose `spec.md` lacks the mark or whose mark disagrees with `routing.md` | stays: a reader decides on it, and its first word is a plain English word |
| The sealer's verdict `sound`, `not sound — <reason>`, `undecidable — <question>` in `guarantee.md` | the sealer | `chain_check.py`'s guarantee arm, which fails a ready pull request on any verdict but the first | the words become `sealed`, `withheld — <reason>` and `undecided — <question>` (owner, 2026-10-16): the verdict names the act of the role, the sealer affixing its seal or withholding it, in plain English. The reader, the template, the definition, the docs and the sealer cases' graders change in phase 5's commit; any other spelling, the old words included, is refused naming the line, and the changelog tells an in-flight work item to rewrite its verdict line. `tests/test_one_word_one_meaning.py` is run on the commit, since `sealed` is the sealer's seal, the one meaning `seal` keeps once the proof block leaves |
| `Approved <date> by <who>, …` and `Answered <date> by <who>, …` | the session | `tests/test_the_set_a_work_item_always_has.py` pins the three feet-lines to one shape; `chain_check.py` reads `Answered <date> by <who>:` under a guarantee's verdict | stay, same grounds |
| The per-segment numbers in the definitions (`agents/warden.md:235` *1.89*, `agents/smith.md:266` *1.08–1.17*, `agents/framer.md` *1.4*) | nobody writes them; they are stated | `session_cost.py --segments`, from `docs/the-review-record.md` §*The per-segment bars*, never from a definition | leave the definitions; the table is the one source |
| Emoji in the files an agent reads: `skills/implement/SKILL.md` 3, `skills/code-review/SKILL.md` 1, `skills/writing-style/SKILL.md` 1, `skills/legacy-parity/SKILL.md` 4 (the parity verdict labels `U+1F534, U+1F7E1, U+1F7E2 and U+2753`), `skills/verify/SKILL.md` 2, `templates/` 4, the two READMEs 4 (`executed`; `agents/` holds 0) | nobody as a mark; the parity labels are written by a parity review | nothing reads the parity labels; `hooks/sealer-stamp.py` draws the seal from values, not from these | leave; the parity verdicts become the words `differs`, `grounded`, `equivalent` and `unread`, one lowercase word at the start of the label line, and `legacy-parity`'s Parity review section says so once |

## The broad gate runs before the sealer

The gate is mechanical, so a script runs it and the sealer reads its record.
The orchestrator runs `broad-gate --base <base> --record <item>` with nothing
else running, then spawns the sealer with the base, the item, the issue and
the pull request. The sealer's first act becomes reading `broad-gate.md`: a
file absent, or naming a commit other than HEAD, is `withheld — no broad run
at HEAD`, written and returned, and the sealer runs nothing broad. A re-run
after a commit audits the commits since the commit the last `guarantee.md`
named, keeps that run's line as `; earlier run: <sha> <verdict>` on the
`Target SHA` row the way `broad-gate.md` keeps its runs, and re-runs no claim
the earlier run already re-ran unless a commit since touched its coordinate.
`skills/code-review/orchestration.md` §*the pull request opens before round
1* says the order; `docs/the-broad-gate.md` §*One act, one owner* says the
owner is the orchestrator's one command; contract §2 says no agent runs it;
`docs/the-review-record.md` §*The guarantee* says what the sealer reads.

## The sealer's model is decided by measurement

The sealer runs on Opus from 0.22.0. This item runs the three sealer cases on
two trees that differ in one line, `agents/sealer.md`'s `model:`, two runs
each, and writes the comparison as `evals/sealer-model.md` with both sides'
truth graders and cost. The model drops to Sonnet only where every truth
grader passes on the Sonnet side as often as on the Opus side and the Sonnet
side's spend is lower; a difference in any truth grader keeps Opus, whatever
the cost. Whether the eval honours a definition's `model:` key for the
subagent is a measurement the first run makes (`questions.md` Q6).

## How the rewrite is proved not worse

Two axes, decided by the owner on 2026-10-14. **Outcome**: the real defects a
replayed round finds, the seeded defects it catches, its false findings, and
the sealer's verdict — the `truth-` graders, the false-finding rate and the
`shape-` and `reach-` graders of `evals/behaviour/<agent>/`. **Cost**: the
bytes a spawn reads, the tokens its runs read and the spend. A rewrite
passes where its outcome holds or improves and its tokens fall, every one of
them judged against the baseline and none against an absolute (owner,
2026-10-17: the baseline is the reference, not a bar; the focus is fewer
tokens and a better outcome, and time spent is not judged). That is
`evals/scripts/noninferiority.py#verdict`'s rules after phase 1b: recall not
fallen, false rate within `FALSE_MARGIN` of the baseline's, the shape and
reach graders as rule 3 of `evals/README.md` §*The behaviour suite* states
them (#957's phases judged each grader on its own; #966 pooled them per
agent in 0.22.2), preload bytes below the baseline, and the tokens the run
read across every
model — the session's and the agent's under test, `modelUsage` — per tool
call below the baseline's (owner, 2026-10-17, after phase 2's first run: the
warden read 17.8% more tokens in all and found 17 truths where the baseline
found 13; the decision was taken on a hand count of the calls, 34% more and
12.3% less per call, which the trace corrects to 19.3% more tool calls
(746 to 890) and 1.25% less per call, `phases/phase-2.md`). A run's tokens are about
its calls times the context each call carries: the rewrite controls the
context, which the per-call figure reads, and how many calls the agent makes
is its behaviour, which the outcome rules judge. Tokens per true find was
weighed and not chosen, because its divisor is the recall, which moves by a
find or two between runs of the same agent. This rule holds unchanged for
every later phase. Total tokens, tokens per true find, spend and wall
seconds are recorded beside them and judge nothing.

- **The baseline is taken once, at one reference, and nothing is compared
  against anything else** (owner, 2026-10-17): the tree and the suite both at
  af9c924b, `release/v0.22.1` after #964 merged, for the warden, the smith,
  the framer and the sealer (`run --rev af9c924b --suite-rev af9c924b`).
  Every new side of every phase runs with `--suite-rev af9c924b` too, and
  `compare` refuses two sides whose suites differ (exit 2), so a changed case
  can never be read as a changed agent. It is committed as
  `seal/specs/<id>/evals/baseline-<agent>.json`; the raw output stays
  outside the tree. Nothing has been baselined yet (`executed`: the only
  files under #923's `evals/` are two notes). The harness that runs it is
  green and reads the 0.22.0 record once #964's phase 1 has merged.
- **Each phase runs the cases of the agents whose preload it changed**, and
  commits `evals/<agent>-phase-N.md` reading `pass`. An agent's set runs
  again at the close only where its preload changed after its last passing
  record.
- **The scribe has no cases**, and this item writes none: no parity run has
  happened in this repository, and a parity fixture generator is a mechanism
  nobody has asked for. Its rewrite is measured on bytes, and its outcome is
  `unverified` with the owner named (`questions.md` Q3, answered).
- **The runs.** Twenty cases at two runs each is forty runs a full pass
  (`executed`: warden 9, smith 4, framer 4, sealer 3). The phases below run
  the baseline (40), the warden (18), the contract (40, every preload), the
  smith and the framer (16), the sealer on Opus and on Sonnet (12): 126 runs.
  The owner's figure of about 120 runs holds; the figure of about $150
  (#923's `questions.md:149`, `read`) is nobody's measurement until the
  baseline's `total_cost_usd` fields are read, which is `questions.md` Q4.

## Rules the rewrite states in place

Each came out of the 0.22.0 run (the owner, 2026-10-14 and 2026-10-15), and
each is a sentence in the file named, not a mechanism.

| Rule | File | Held by |
|---|---|---|
| The record is written to the branch worktree's `seal/specs/<item>/rounds/`, the tree under review, never the main checkout | `agents/warden.md` (its *Where you work* already says so; the rewrite keeps the sentence and the eval's `shape-report-exists` grader reads the path) | `evals/behaviour/warden/*/graders/shape-report-exists.md` |
| A new test starts from its group: the smith reads the tests of the function it calls, extends one where it can, and a new test says in the hand-back which case the group lacked | `agents/smith.md` | `tests/test_a_moved_rule_leaves_its_definition.py` (the pin module for the smith's rules, re-pointed) |
| Each new test is read against its group and against any pair the duplicate check names; a test covering nothing its group does not is a finding | `agents/warden.md` | the warden's pin module |
| An agent cleans up only the processes and files it started: it records its PIDs and paths and never kills by command name or deletes a shared directory by glob | `skills/agent-contract/SKILL.md` | `tests/test_the_agent_contract_holds_the_universal_rules.py` (re-pointed) |
| When a check refuses correct code, the agent fixes the check or reports it, and never bends the code to pass | `skills/agent-contract/SKILL.md` | the same |
| Do not avoid the change a problem calls for: a structure is a reference, not a constraint; a framer weighs replacing a structure as an equal of keeping it; an agent concluding something should stay checks the premise first | `agents/framer.md` and `skills/agent-contract/SKILL.md` | the same, and the framer cases' `shape-` graders (the Alternatives table carries a replacing alternative) |

## The tree as it stands, measured

Read at d4552372 (= 9632e5ea's tree outside `seal/specs/`); `executed` where
a command produced the number, `read` where a document or a CI log did. The
frame measured the tree once, and the readings are split by the phase that
acts on each: the suite's size and CI cost, the red case, the harness's
stale sentences, the census, the stamps and the closing mark's reader are
#964's `spec.md` §*The tree as it stands, measured*, cited and not restated.

- **Definitions** (`executed`, `wc`): framer 371 lines / 19,857 B; smith 341 /
  21,155; warden 305 / 18,031; sealer 143 / 7,990; scribe 71 / 3,763; total
  1,231 / 70,796. **Preloaded skills**: agent-contract 369 / 20,368;
  implement 538 / 31,970; code-review 303 / 16,620; writing-style 322 /
  21,000 (11,402 characters); legacy-parity 117 / 5,325.
- **Preload per spawn** (`executed`, `payload-meter --agent`, bytes; tokens
  estimated at 3.2 B/token, uncalibrated): framer 107,970 (33,740 tokens);
  smith 109,268 (34,146); warden 90,794 (28,373); sealer 43,133 (13,479);
  scribe 44,231 (13,822). Each total holds the `CLAUDE.md` pair (14,775 B),
  which is not this item's; the agent's share is 93,195 / 94,493 / 76,019 /
  28,358 / 29,456.
- **Marks** (`executed`): emoji in `agents/` 0, `skills/` 18 in 7 files,
  `templates/` 4 in 3, `docs/` 10 in 5, `hooks/` 30 in 15, scripts 101 in 15,
  `tests/` 521 in 69, READMEs 4. `§N` citations 128 outside `tests/`, 326
  inside. `Enforced by:` lines 206 in `docs/`, `agents/`, `skills/`,
  `templates/` and `CONTRIBUTING.md`.
- **Pins** (`executed`): 42 test modules name a file under `agents/`
  (37,501 lines, 878 s priced), per agent warden 23, smith 19, framer 12,
  sealer 11, scribe 5; modules naming a preloaded skill: agent-contract 11,
  implement 12, code-review 6, writing-style 3.
- **The evaluation** (`executed`): 20 cases, two runs each, `max_turns` 12,
  timeouts 1,200–2,400 s; the warden's and the smith's session model is
  Opus, the framer's Fable, the sealer's case session Sonnet with the
  definition's `model: opus`; `--max-cost-usd` defaults to 100 per
  invocation.
- **The gate's script** (`executed`, `wc`): `broad_gate.py` 3,396 lines.

## A number in this frame names its moment or its bound

Every figure above is a reading at d4552372, and `plan.md`'s rows that quote
one say so. The changelog fragment states each before-and-after figure with
the commit it was read at, from the eval records and `payload-meter`, and
nothing recounts a figure by hand.

## User scenarios & acceptance *(mandatory)*

Each row says what it protects: the defect it would catch, and why no other
case does.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 One shape, one preload | Given any file under `agents/`, when it is read, then it opens with the one contract sentence, carries the four sections of §*The shape of a definition* and lists `agent-contract` alone under `skills:` | `tests/test_every_agent_reads_the_contract.py`, rewritten: the opening sentence is one line and identical; the `skills:` list equals `[agent-contract]`; the four headings stand. Protects: a sixth preload creeping back into a list, which no eval sees as long as the output is right |
| S2 A step names what it opens | Given a definition's `## Order of work`, when a step needs a skill, then the step names the file by path and the path resolves | a case of the same module: every backticked `skills/*/SKILL.md` a definition names exists. Protects: a renamed skill leaving a dangling instruction, which an agent meets as *file not found* mid-run |
| S3 The skill is opened when its act comes | Given a warden, smith or framer spawn, when the agent reaches the step, then its output has the shape the skill gives it | the `shape-` graders of each agent's cases (the record's `## Findings` and `verdict:` line; the phase record; the three documents with the mark and the `Verified by` column) pass on the new side. Protects: a definition that names the skill and an agent that never opens it, which S2 cannot see |
| S4 The contract numbered anew, no dangling citation | Given the rewritten contract, when `§N` is cited anywhere outside `seal/specs/`, then section N exists and means what the citation says | a case of `tests/test_the_agent_contract_holds_the_universal_rules.py`: every `§N` outside `seal/specs/` and `changelog/` names a heading the contract has. Protects: a citation left at the old number after the renumbering, which reads as a rule and points at another |
| S5 The four new rules | Given the contract, when read, then the own-cleanup, the check-refuses-correct-code, the rewrite-in-place and the do-not-avoid rules each stand as a paragraph with an `Enforced by:` line | the same module, one case per rule reading its paragraph's first sentence. Protects: a rule dropped in a later trim, the failure #107 recorded for a moved rule |
| S6 No per-agent batching number | Given any definition, when read, then no tools-per-turn figure stands in it, and `docs/the-review-record.md` §*The per-segment bars* is the one source | `tests/test_the_handoff_before_round_one.py::test_the_scripts_bars_are_the_protocols` (exists) and a case of `tests/test_a_moved_rule_leaves_its_definition.py` refusing a `tools per turn` figure in `agents/`. Protects: the second copy drifting from the table |
| S7 The proof block leaves | Given `skills/implement/SKILL.md`, `skills/code-review/SKILL.md`, `templates/sdd-overview.md` and `skills/verify/SKILL.md`, when read, then no proof-block template or sentence describing one stands | `tests/test_the_record_is_written_in_words.py` extended over every file under `agents/`, every `skills/*/SKILL.md` and `templates/`: no emoji, and no `applied` block. Protects: the block coming back as a habit, which costs every report its lines and catches nothing |
| S8 The gate runs before the sealer | Given a ready pull request, when the orchestrator reaches the sealer's spawn, then `broad-gate --base <base> --record <item>` has run with nothing else running, and the sealer's step 1 reads `broad-gate.md` and refuses one absent or not at HEAD | `tests/test_broad_gate_rule.py` rewritten: no definition assigns the gate; the orchestration section names the run before the spawn; `tests/test_the_sealer_guarantees.py::TestDefinition`: step 1 reads and never runs. The sealer's three cases, whose scaffolds write `broad-gate.md` at HEAD, pass. Protects: the sealer re-running a suite that failed 1.8 s over a ceiling at 240K tokens |
| S9 A re-run audits only what changed | Given a `guarantee.md` from an earlier run, when the sealer runs again at a new HEAD, then its claims re-run are those of commits since the earlier commit, and the earlier run's line is kept | `tests/test_the_sealer_guarantees.py::TestTemplate` and `TestDefinition`: the `; earlier run:` form and the step's sentence. Protects: a full re-audit for a one-line commit |
| S10 The sealer's model by measurement | Given the three sealer cases, when run on Opus and on a `model: sonnet` copy, then `evals/sealer-model.md` holds both sides, and `model:` reads `sonnet` only where every truth grader passes as often on Sonnet and spend is lower | `tests/test_a_rewritten_definition_proved_non_inferior.py` recomputes the record; the phase record names the decision. Protects: a drop decided by cost alone |
| S11 The baseline once | Given the released tree, when the baseline runs, then four `evals/baseline-<agent>.json` files stand, none cut short, each with spend, tokens and preload bytes | the same module's `test_a_cut_short_side_is_no_result_and_never_a_pass` and `test_a_run_records_what_it_cost`. Protects: a baseline with unknown cost, which makes every later verdict `no result` |
| S12 Each phase proves its agents | Given a phase that changed an agent's preload, when it closes, then `evals/<agent>-phase-N.md` reads `pass` under the five rules, and the plan's row names it | the same module's `test_the_verdict_is_recomputed_from_the_records_numbers`. Protects: a `pass` written over failing numbers |
| S13 Every case says what it protects | Given a test or grader this item writes, when read, then its docstring or description names the defect it would catch and why no other case does | the warden's reading of the diff; `Enforced by: nothing — a reading from words is a report`. Protects: a case nobody can map to a defect, which is how a suite grows by default (#942) |
| S14 Nothing asks a person | Given this item's run, when any phase executes, then no step stops for an answer; each `questions.md` row carries its default or its answer | `plan.md`'s rows read by the orchestrator; the sealer's step 4 reads the parties. Protects: a run that stops at minute thirty |
| S15 Rewritten in place | Given a fact this item removes, when the commit lands, then every sentence, pin, comment and copy standing on it leaves in the same commit, enumerated by the `git grep` the phase record names | `bin/rules --check` exit 0; `tests/test_no_passage_is_pasted_into_a_second_file.py` green; the greps in the phase record finding nothing outside `seal/specs/` and `changelog/`. Protects: the stale half of a file misleading the next agent, which is the item's root problem |
| S16 The changelog table | Given the fragment, when the release gathers it, then a per-agent table reads preload bytes, tokens read, spend and outcome at the baseline and at the close, each with its commit | `tests/test_the_pull_request_language_is_the_repositorys.py` and the fragment's heading rule; the sealer reads the fragment against the eval records. Protects: a figure recounted by hand, the loop #923 ran three rounds on |

## Data & interfaces

- **A definition**: frontmatter with `skills: [agent-contract]`; body `#
  <name>`, the contract sentence, `## Job`, `## Order of work`, `## Never`,
  `## Rules`. The contract: `# agent-contract`, one opening paragraph, `## §1
  …` to `## §N …` in the new order, each section a rule paragraph ending in
  `Enforced by:`.
- **The broad gate's order**: `skills/code-review/orchestration.md` §*the
  pull request opens before round 1*: preflight, the pull request body and
  the changelog written, `broad-gate --base <base> --record <item>` with
  nothing else running, then the sealer's spawn. `agents/sealer.md` step 1:
  read `broad-gate.md`; absent or not HEAD is `withheld — no broad run at
  HEAD`. `guarantee.md`'s `Target SHA` row: `<sha> against <base>[; earlier
  run: <sha> <verdict>]`.
- **The eval records**: `seal/specs/<id>/evals/baseline-<agent>.json`,
  `evals/<agent>-phase-N.md`, `evals/sealer-model.md`; the sealer's
  comparison runs `noninferiority.py run --tree <copy>` on a copy of the tree
  whose `agents/sealer.md` reads `model: sonnet`.
- **The parity verdict words** in `skills/legacy-parity/SKILL.md`:
  `differs`, `grounded`, `equivalent`, `unread`, each one lowercase word at
  the start of its line.
- **The closing word** a smith of this item writes into `overview.md` is
  #964's: `closed` as the first word of the row's first cell.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `skills:` entries beyond `agent-contract` | `agents/framer.md:8-11`, `agents/smith.md:8-11`, `agents/warden.md:8-11`, `agents/scribe.md:8-10` | each definition's `## Order of work` names the file at the step |
| The paragraph explaining how the contract arrives, five copies | `agents/*.md`, lines 15–20 of each | one sentence stays; the mechanism is the contract's opening |
| The per-segment numbers in the definitions | `agents/warden.md:235-238`, `agents/smith.md:266-269`, `agents/framer.md#"Your number is 1.4 tools per turn"` | `docs/the-review-record.md` §*The per-segment bars* is the one source |
| The RIDER block and the waiver incident narrative in the smith's design-gate step | `agents/smith.md:87-126` | the rule stays as one sentence; the measurements are history in that rider's own issue |
| The contract's incident paragraphs and its 17-slot numbering | `skills/agent-contract/SKILL.md` | the rules, numbered anew, each with its `Enforced by:`; the incidents stay in the changelog and the issues |
| Every `§N` citation at an old number | 128 sites outside `tests/`, 326 inside, at d4552372 | rewritten to the new number in the renumbering commit; `seal/specs/*/rounds/` keep theirs as history |
| The proof block and the sentences describing it | `skills/implement/SKILL.md#"Proof block"`, `skills/code-review/SKILL.md:295-303`, `templates/sdd-overview.md:9`, `skills/verify/SKILL.md#"Every agent seals what it verified, and one of them is final"`, `#"Seal block"` | the hand-back's `executed`, `read`, `unverified` labels carry the claims; the sealer's `guarantee.md` is the one seal |
| The pins on the proof block | `tests/test_broad_gate_rule.py::test_the_seal_block_asks_for_the_row_too`, `::test_the_seal_reports_what_the_checks_cost`, `tests/test_the_record_is_written_in_words.py#SHARED_MARKER`, `tests/test_one_word_one_meaning.py:181, 302` | leave with the block |
| `U+2B1C` as the question status | `templates/sdd-questions.md:10`, `skills/implement/SKILL.md` §4's sentence | the words `open` and `answered <date> by <who>` |
| The parity verdict emoji | `skills/legacy-parity/SKILL.md#"Parity review"` | four lowercase words |
| The verdict words `sound`, `not sound`, `undecidable` | `chain_check.py`'s guarantee arm, `templates/sdd-guarantee.md`, `agents/sealer.md`, `docs/the-review-record.md` §*The guarantee*, `skills/code-review/orchestration.md`, `evals/behaviour/sealer/*/graders/shape-verdict.md`, `evals/scripts/rule_cases.py`, `tests/test_the_sealer_guarantees.py`, the READMEs | `sealed`, `withheld — <reason>`, `undecided — <question>` |
| The sealer's broad run | `agents/sealer.md` step 1, `docs/the-broad-gate.md` §*One act, one owner, and the owner is an agent*, contract §2's sentence assigning it, `skills/code-review/orchestration.md:180-189` | the orchestrator's `broad-gate --record` before the spawn; the sealer reads the file |
| The pins that said one definition assigns the gate | `tests/test_broad_gate_rule.py::test_only_one_definition_assigns_the_broad_gate`, `::test_the_sealer_counts_the_silent_definitions_from_the_glob`, `::test_the_orchestrator_runs_the_preflight_before_it_spawns_the_sealer`, `docs/the-broad-gate.md`'s `Enforced by:` naming them | rewritten to the new fact: none assigns it, and the orchestrator runs it before the spawn |
| The pins on sentences the rewrites drop | the 42 modules naming `agents/`, the 11 naming the contract, the 12 naming `implement`, the 6 naming `code-review`, the 3 naming `writing-style` | each case re-pointed where its rule stays, removed with one line in the phase record where it pinned narration (`questions.md` Q7) |

## Open questions → questions.md

Every decision the tree could make is made above with its grounds; what
only the owner can settle, what a measurement settles and what the work
settles are the rows of `questions.md`, each with the default this run
takes or the answer the owner gave.

Framed 2026-10-16 by framer, before the build.
