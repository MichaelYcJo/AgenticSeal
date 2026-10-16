# Feature Specification: every agent is written anew from its job (#957)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* | Every definition, skill, mark, label, census line and test this frame touches is weighed by what it caught against what it costs, and nothing is kept because it is there. A change rewrites in place and removes what stood on the old fact in the same commit. Nothing is kept beside the tree to stay in step with it, which is why the `Reads:` census and the rider stamps leave |
| `CLAUDE.md` §*The goal a design is chosen against* | No step of this item asks a person mid-run. What needs the owner is in `questions.md`, each row with its default, and the evaluation runs on the orchestrator's account |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The item removes two gates (the census, the rider check) and changes one (the chain check's grammar reading): each names what it caught against its cost, its failure direction, a prompt budget of zero and its `## Removes` rows. Its own bullet *A `Reads:` line on every unit* leaves with the census |
| `docs/the-agent-set.md` | One contract every agent receives, one definition each; the writer of a frame is not its builder; a subagent asks nobody; a spawn's payload is measurable and paid on every spawn. Rewritten in place where this item changes what the sentences describe: the broad gate's owner and the section-number rule of a contract written anew |
| `docs/the-review-record.md` §*The round record*, §*The guarantee*, §*The run* | The record's grammar, stated here in prose over five paragraphs, becomes one table this document holds and the check reads. The guarantee's first act, the broad run, moves to the orchestrator's script run before the sealer is spawned. The cap counts from the last design change and no person is asked mid-run |
| `docs/the-broad-gate.md` §*One act, one owner, and the owner is an agent* | Rewritten in place: the act is one, its owner is the orchestrator's one command before the sealer is spawned, and no agent runs it |
| `docs/the-reader-registry.md` | Its census rules leave with the census. §*A frame names what its work removes* stays and is this file's `## Removes` |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The changelog is this item's `changelog.md` fragment, and it carries the per-agent before-and-after table |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The item alters what every spawn reads, so it sits on the top rung and this frame exists |
| #957's body (the owner, 2026-10-13 to 2026-10-16) | The one source for what was decided: six numbered items, the rules the rewrite states in place, and the two axes of the proof. Where this file and that body differ, the body holds |
| #923's `spec.md` §*The agent definitions this item touches*, §*The proof harness, as this item leaves it*, `plan.md` phases 6–9 at 6a40c790 | The frame this one starts from, re-read against the released tree. What still holds is restated here; what moved is named under `## Removes` or in `plan.md`'s Alternatives |
| #940, #941, #942, #945, #956 | What an agent opens on demand, `docs/`, the test layout, the process's cost and the audit of readers are theirs. This item rewrites a file of theirs only where it makes a sentence of it false, and says so in the phase record |

## Scope

**In.** The five definitions under `agents/` and `skills/agent-contract/SKILL.md`
written anew from their jobs, each `skills:` list cut to `agent-contract`,
and the four skills the lists used to inject (`code-review`, `implement`,
`writing-style`, `legacy-parity`) written to the shape of §*The shape of a
definition* so an agent that opens one at its step reads the current rule
once. Every mark, label and constant an agent writes or a check reads,
judged by §*Marks and labels*. The `Reads:` census and the rider stamps. The
round record's grammar as one table the check reads whole. The broad gate as
the orchestrator's script run before the sealer. The sealer's model by
measurement. The baseline and the per-phase proof, the test modules that pin
the rewritten files, the eval cases that grade them, and the changelog
fragment. The two cases red on `main` at the release (§*The tree as it
stands, measured*), because every pull request of this item runs the suite
they are in.

**Out, and whose.** `skills/verify/SKILL.md` beyond the sentences this item
makes false (§*Every agent seals what it verified* and §*Seal block*, which
describe the proof block), `skills/settle/`, the small skills, `templates/`
beyond `sdd-overview.md`, `sdd-questions.md`, `sdd-round.md`'s comment and
`config.md`'s literal list, `CONTRIBUTING.md` beyond its census bullet,
`CLAUDE.md` — #940. `docs/` beyond the five documents named in
§*Grounding* — #941; the `Enforced by:` label keeps its spelling in every
file this item writes, because its rename to one lowercase word is #941's
decision with `rules.py` as its reader, and a tree carrying two spellings is
the state the owner's label rule forbids. The test suite's layout beyond the
modules this item writes, re-points or deletes — #942. The agent-lifetime
rule, the folding rule, the process archive — #945. The audit of every
reader of written text — #956; the `Reads:` lines were a self-declaration
and not that audit's input, so removing them takes nothing from it. The
emoji in output a script prints for a person and no agent or check reads —
`publish_release_note.py`'s release-note headings, the seal stamp's drawing,
the hooks' terminal messages — stay where they are and are named in
`questions.md` Q9 for the owner, since the owner's rule reaches text an agent
reads or writes and a check reads, and those are neither. The quotations of
old marks inside test fixtures and inside the four 0.22.0 items' round
records stay as the history they quote (#923's Q10).

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
code point so that this file carries none:

| Mark | Written by | Read by, and what it decides | Disposition |
|---|---|---|---|
| The proof block (`U+1F4CB implement applied`, `U+1F4CB code-review applied`, the `U+1F50F verify sealed` block) in `skills/implement/SKILL.md`, `skills/code-review/SKILL.md`, `templates/sdd-overview.md:9`, `skills/verify/SKILL.md` §*Seal block* | the smith and the warden at the end of every report | no script or check; `tests/test_the_record_is_written_in_words.py` names its marker only to exempt it from the emoji case, `tests/test_broad_gate_rule.py::test_the_seal_block_asks_for_the_row_too` pins its row, `tests/test_one_word_one_meaning.py` names it as the smith's seal. What it caught: nothing recorded in any round record of 0.21.x or 0.22.0 | leaves, with the three pins and the sentences of `verify` that describe it. The hand-back's three labels below carry what the block carried |
| `executed`, `read`, `unverified` | every agent, on every claim | the sealer's step 3 picks its sample from the smith's `executed` and `seen red` claims; the warden audits the smith's `unverified` suite label; contract §4 | stay, as they are already lowercase words |
| `U+2705` closing a `## Not verified` row of `overview.md` (`templates/sdd-overview.md:38`) | the smith or the session, on closing an item | `skills/verify/scripts/unverified_check.py#CLOSED`, a gate in `hygiene.yml` that fails a pull request whose rows left unclosed | becomes the word `closed` as the first word of the row's first cell, read fail-closed; the rows of the four 0.22.0 items' overviews are rewritten once by a one-shot script in the same commit (`questions.md` Q2 holds the owner's say over the default) |
| `U+2B1C` in `questions.md`'s `Status` column (`templates/sdd-questions.md:10`) | the framer | nothing in code (`executed`: no reader outside test docstrings quoting old records) | the column reads `open` or `answered <date> by <who>`; the template is rewritten and this item's own `questions.md` writes the words |
| `Framed <date> by <who>, before the build.` and `Reframed …` | the framer | `chain_check.py#REFRAME_RE` and the frame arm, which fail a pull request whose `spec.md` lacks the mark or whose mark disagrees with `routing.md` | stays: a reader decides on it, and its first word is a plain English word |
| `Approved <date> by <who>, …` and `Answered <date> by <who>, …` | the session | `tests/test_the_set_a_work_item_always_has.py` pins the three feet-lines to one shape; `chain_check.py` reads `Answered <date> by <who>:` under a guarantee's verdict | stay, same grounds |
| The per-segment numbers in the definitions (`agents/warden.md:235` *1.89*, `agents/smith.md:266` *1.08–1.17*, `agents/framer.md` *1.4*) | nobody writes them; they are stated | `session_cost.py --segments`, from `docs/the-review-record.md` §*The per-segment bars*, never from a definition | leave the definitions; the table is the one source |
| Emoji in the files an agent reads: `skills/implement/SKILL.md` 3, `skills/code-review/SKILL.md` 1, `skills/writing-style/SKILL.md` 1, `skills/legacy-parity/SKILL.md` 4 (the parity verdict labels `U+1F534, U+1F7E1, U+1F7E2 and U+2753`), `skills/verify/SKILL.md` 2, `templates/` 4, the two READMEs 4 (`executed`; `agents/` holds 0) | nobody as a mark; the parity labels are written by a parity review | nothing reads the parity labels; `hooks/sealer-stamp.py` draws the seal from values, not from these | leave; the parity verdicts become the words `differs`, `grounded`, `equivalent` and `unread`, one lowercase word at the start of the label line, and `legacy-parity`'s Parity review section says so once |
| The `Reads:` docstring line (364 lines in `.py` files, 31,055 bytes, `executed`) | every unit of shipped Python | `tests/test_a_reader_declares_its_input_class.py`, which leaves (§*The census and the stamps leave*) | leaves with its reader, by a one-shot script, in the same commit |
| The rider stamp `Verified <date> against <anchor>@<hash>` on 55 `RIDER:` comments in 20 files (`executed`) | whoever runs `rider_check.py --reverify` | `.github/scripts/rider_check.py`, exit 2 in CI on a drifted hash | leaves; the `RIDER:` comment stays as a comment with no stamp and no checker, and `seal/follow-up.md`'s header says so |

## The census and the stamps leave

`tests/undeclared_readers.txt` (994 lines, 49,722 bytes) keys every unit
undeclared at the rule's landing by a hash of its source, so a comment edit
asks for a new declaration; `.github/scripts/rider_check.py` (889 lines)
stores a hash and a date per rider and asks for `--reverify` whenever the
unit moves. Both are a list kept beside the tree to stay in step with it,
and both leave with what stood on them: `tests/test_a_reader_declares_its_input_class.py`
(866 lines, 38.4 s of the suite's 3,371 s at d4552372, `executed` from
`.test_durations`), `tests/reader_registry.py` (536), the stamp cases of
`tests/test_a_rider_reaches_its_file.py` (798 lines; its cases over
`seal/follow-up.md`'s rows stay), `CONTRIBUTING.md`'s census bullet,
`docs/the-reader-registry.md`'s three census sections and its *What neither
check can read* list, `seal/follow-up.md`'s four stamp paragraphs, the
`Reads:` lines, the 55 stamps, and `test.yml`'s *Not shallow* comment where
the rider test was its reason. The question the census was built to answer,
which way a reader fails on an input it cannot read, is #956's audit, which
reads the code and not a self-declaration.

Both were gates: the census failed a pull request whose changed unit did not
declare, and the rider check exited 2 on a drifted hash. What each caught:
the census caught a declaration missing, never a reader failing the wrong
way (the four misses of #923's check all carried a `Reads:` line); the rider
check caught drift on one fix pass of #923 (the smith's own account, `read`),
and the drift it reported was a comment edit.

## The record's grammar is one table

`docs/the-review-record.md` §*The round record* states the grammar in prose
over five paragraphs, `templates/sdd-round.md` restates every label and
value in its comment, `templates/config.md` §*What no row governs* lists the
literals a third time, and `chain_check.py` holds the regular expressions a
fourth (`SEVERITY` … `RECORD_TARGET`, `EXACT_LABEL`, `MISSPELT_LABEL`,
`TARGET_VALUE`, `LOCATION_VALUE`, `REFERENCE`, `FIXED_VALUE`,
`DEFERRED_VALUE`, lines 93–191 at d4552372). Three refusals of #923 were
added one at a time after a review found each shape leak, because the labels
were strict while parts of the value and heading reading were lenient.

**The grammar is one table in `docs/the-review-record.md`, and the check
reads it.** One row per line kind: the label, the exact shape of the value
as a regular expression that must match the whole line, where the line may
stand, how many a finding or a record may hold, and what the refusal says.
`chain_check.py` loads that table from the document at its own relative
path, as it already locates `hooks/routing.py`, and matches each line
against the row whole; a table it cannot read, or a document it cannot find,
is exit 2 naming the file, never a pass. In a user's repository the hygiene
template clones this repository into `$RUNNER_TEMP/specseal` and runs the
check from there (`templates/hygiene.yml:59, 92`, `read`), so the document is
beside the script wherever the script runs. The template's comment and
`templates/config.md` point at the table and restate nothing; the language
test derives its literal list from the table. The shapes that leaked —
a `path#unit` coordinate, a heading with no number or a repeated one, a
relation label with no value — stay as fixed example cases (T32, T33, T35,
T36 of #923, re-pointed at the table), and no generated-variant or mutation
case is written for the grammar (#929's finding, the owner's decision).

## The broad gate runs before the sealer

The gate is mechanical, so a script runs it and the sealer reads its record.
The orchestrator runs `broad-gate --base <base> --record <item>` with nothing
else running, then spawns the sealer with the base, the item, the issue and
the pull request. The sealer's first act becomes reading `broad-gate.md`: a
file absent, or naming a commit other than HEAD, is `not sound — no broad run
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
passes where its outcome holds or improves and its cost falls, which is
`evals/scripts/noninferiority.py#verdict`'s five rules as they stand
(recall not fallen, false rate within `FALSE_MARGIN`, every shape and reach
grader passing on the new side, preload bytes below the baseline, tokens and
spend within `COST_MARGIN`).

- **The baseline is taken once**, on the released tree this branch is cut
  from (d4552372), for the warden, the smith, the framer and the sealer, with
  the suite as it stands at the baseline commit (`run --rev d4552372
  --suite-rev HEAD`), and committed as
  `seal/specs/<id>/evals/baseline-<agent>.json`; the raw output stays
  outside the tree. Nothing has been baselined yet (`executed`: the only
  files under #923's `evals/` are two notes).
- **Each phase runs the cases of the agents whose preload it changed**, and
  commits `evals/<agent>-phase-N.md` reading `pass`. An agent's set runs
  again at the close only where its preload changed after its last passing
  record.
- **The scribe has no cases**, and this item writes none: no parity run has
  happened in this repository, and a parity fixture generator is a mechanism
  nobody has asked for. Its rewrite is measured on bytes, and its outcome is
  `unverified` with the owner named (`questions.md` Q3).
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
a command produced the number, `read` where a document or a CI log did.

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
  `tests/` 521 in 69, READMEs 4. `Reads:` lines 364 (31,055 B).
  `undeclared_readers.txt` 994 lines. `RIDER:` comments 55 in 20 files.
  `§N` citations 128 outside `tests/`, 326 inside. `Enforced by:` lines 206
  in `docs/`, `agents/`, `skills/`, `templates/` and `CONTRIBUTING.md`.
- **Pins** (`executed`): 42 test modules name a file under `agents/`
  (37,501 lines, 878 s priced), per agent warden 23, smith 19, framer 12,
  sealer 11, scribe 5; modules naming a preloaded skill: agent-contract 11,
  implement 12, code-review 6, writing-style 3.
- **Suite and CI** (`executed` from `.test_durations` and the job list of
  run 38850511000, the last green `tests` run, 2026-10-16): 7,329 cases
  priced at 3,371 s; one run is ubuntu 5.0 min, three macOS shards 13.1 min,
  four Windows shards 35.5 min, lint and durations 1.5 min — 55 runner
  minutes, wall under 11 minutes, and 208 billable minutes a run if the
  repository went private (Linux 1×, Windows 2×, macOS 10×).
- **The release tree is red** (`read`, the log of run 38852872472 on `main`
  at d4552372): `tests/test_the_sealer_guarantees.py::test_a_verdict_other_than_sound_fails_a_ready_pull_request`
  fails with `StopIteration` on all three operating systems (its `next(…)`
  finds no output line opening `<rel>:`), and
  `tests/test_a_rewritten_definition_proved_non_inferior.py::test_a_side_runs_the_tree_it_measures_and_no_installed_plugin`
  fails on Windows on path separators. Every pull request of this item runs
  both, so they are phase 0.
- **The evaluation** (`executed`): 20 cases, two runs each, `max_turns` 12,
  timeouts 1,200–2,400 s; the warden's and the smith's session model is
  Opus, the framer's Fable, the sealer's case session Sonnet with the
  definition's `model: opus`; `--max-cost-usd` defaults to 100 per
  invocation. `evals/README.md` names a `--list` flag `rule_cases.py` does
  not have (`executed`: unrecognized arguments), and #923's `overview.md`
  says `replay_targets.py` reads a paragraph new records do not carry
  (`read`).
- **The check** (`executed`, `wc`): `chain_check.py` 1,707 lines;
  `broad_gate.py` 3,396; `docs/the-review-record.md` 350.

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
| S8 The closing word | Given an `overview.md` with a closed `## Not verified` row, when `unverified-check` reads it, then a row opening `closed` with what closed it is closed, a bare `closed` is refused, and `U+2705` is refused naming the row | the success and the failure case of `unverified_check.py`'s row reader, rewritten in its test module; the four 0.22.0 items' overviews pass the check after the one-shot rewrite. Protects: the emoji mark read by a gate, which is the class #923 found four times |
| S9 The census is gone | Given the tree, when `git grep -n "Reads: "` runs over `*.py`, then nothing matches, and `tests/undeclared_readers.txt`, `tests/reader_registry.py`, `tests/test_a_reader_declares_its_input_class.py` are not tracked | the grep in the phase record, `git ls-files` for the three paths, `bin/rules --check` exit 0 with the census paragraphs gone. Protects: a stored list coming back beside the tree |
| S10 The stamps are gone | Given the tree, when `git grep -n "Verified .* against"` runs over the 55 riders, then nothing matches; `rider_check.py` is untracked; `tests/test_a_rider_reaches_its_file.py` keeps its follow-up cases and no stamp case | the grep, `git ls-files`, the module's collection. Protects: a hash kept beside the tree |
| S11 One grammar, read whole | Given the table in `docs/the-review-record.md` §*The round record*, when `chain_check.py` loads, then it reads the table into its line readers and refuses a line that does not match a row whole; a table it cannot read is exit 2 naming the file | `tests/test_chain_check.py::TestGrammar` (new): the table loads; a row's regex matches the template's example lines whole; `verdict: fixed abc1234 and more` is refused; a document with a broken row exits 2; the module's constants equal the table's rows. Protects: a fourth statement of the grammar drifting, and a partial match letting a shape through, which #923 met three times |
| S12 The leaked shapes stay as cases | Given the grammar reader, when the three shapes that leaked in #923 are read, then each is refused by name | T32, T33, T35 and T36 of #923 re-pointed at the table, unchanged in what they refuse. Protects: the known leaks reopening under the new reader |
| S13 The gate runs before the sealer | Given a ready pull request, when the orchestrator reaches the sealer's spawn, then `broad-gate --base <base> --record <item>` has run with nothing else running, and the sealer's step 1 reads `broad-gate.md` and refuses one absent or not at HEAD | `tests/test_broad_gate_rule.py` rewritten: no definition assigns the gate; the orchestration section names the run before the spawn; `tests/test_the_sealer_guarantees.py::TestDefinition`: step 1 reads and never runs. The sealer's three cases, whose scaffolds write `broad-gate.md` at HEAD, pass. Protects: the sealer re-running a suite that failed 1.8 s over a ceiling at 240K tokens |
| S14 A re-run audits only what changed | Given a `guarantee.md` from an earlier run, when the sealer runs again at a new HEAD, then its claims re-run are those of commits since the earlier commit, and the earlier run's line is kept | `tests/test_the_sealer_guarantees.py::TestTemplate` and `TestDefinition`: the `; earlier run:` form and the step's sentence. Protects: a full re-audit for a one-line commit |
| S15 The sealer's model by measurement | Given the three sealer cases, when run on Opus and on a `model: sonnet` copy, then `evals/sealer-model.md` holds both sides, and `model:` reads `sonnet` only where every truth grader passes as often on Sonnet and spend is lower | `tests/test_a_rewritten_definition_proved_non_inferior.py` recomputes the record; the phase record names the decision. Protects: a drop decided by cost alone |
| S16 The baseline once | Given the released tree, when the baseline runs, then four `evals/baseline-<agent>.json` files stand, none cut short, each with spend, tokens and preload bytes | the same module's `test_a_cut_short_side_is_no_result_and_never_a_pass` and `test_a_run_records_what_it_cost`. Protects: a baseline with unknown cost, which makes every later verdict `no result` |
| S17 Each phase proves its agents | Given a phase that changed an agent's preload, when it closes, then `evals/<agent>-phase-N.md` reads `pass` under the five rules, and the plan's row names it | the same module's `test_the_verdict_is_recomputed_from_the_records_numbers`. Protects: a `pass` written over failing numbers |
| S18 Every case says what it protects | Given a test or grader this item writes, when read, then its docstring or description names the defect it would catch and why no other case does | the warden's reading of the diff; `Enforced by: nothing — a reading from words is a report`. Protects: a case nobody can map to a defect, which is how a suite grows by default (#942) |
| S19 Nothing asks a person | Given this item's run, when any phase executes, then no step stops for an answer; each `questions.md` row carries its default | `plan.md`'s rows read by the orchestrator; the sealer's step 4 reads the parties. Protects: a run that stops at minute thirty |
| S20 The tree is green first | Given the two red cases of run 38852872472, when phase 0 closes, then both pass on all three legs and `replay_targets.py` reads the new record's shape | CI green on the phase-0 commit; `bin/test tests/test_the_sealer_guarantees.py tests/test_a_rewritten_definition_proved_non_inferior.py -q` exit 0. Protects: a baseline run and every later pull request red on a defect that predates them |
| S21 Rewritten in place | Given a fact this item removes, when the commit lands, then every sentence, pin, comment and copy standing on it leaves in the same commit, enumerated by the `git grep` the phase record names | `bin/rules --check` exit 0; `tests/test_no_passage_is_pasted_into_a_second_file.py` green; the greps in the phase record finding nothing outside `seal/specs/` and `changelog/`. Protects: the stale half of a file misleading the next agent, which is the item's root problem |
| S22 The changelog table | Given the fragment, when the release gathers it, then a per-agent table reads preload bytes, tokens read, spend and outcome at the baseline and at the close, each with its commit | `tests/test_the_pull_request_language_is_the_repositorys.py` and the fragment's heading rule; the sealer reads the fragment against the eval records. Protects: a figure recounted by hand, the loop #923 ran three rounds on |

## Data & interfaces

- **A definition**: frontmatter with `skills: [agent-contract]`; body `#
  <name>`, the contract sentence, `## Job`, `## Order of work`, `## Never`,
  `## Rules`. The contract: `# agent-contract`, one opening paragraph, `## §1
  …` to `## §N …` in the new order, each section a rule paragraph ending in
  `Enforced by:`.
- **The grammar table** in `docs/the-review-record.md` §*The round record*:
  `| Line | Shape | Where | How many | Refused as |`, one row per `target:`,
  `severity:`, `location:`, `verdict:`, `regression:`, `reopens:`, `answer:`,
  `confirms:` and the finding heading. `chain_check.py#grammar(path)` returns
  `{line: (compiled shape, where, how many, refusal)}` from the table and is
  called once at load; `records` reads through it; every former constant from
  `SEVERITY` to `DEFERRED_VALUE` leaves. Exit 2 names the document where the
  table is missing or a row does not parse.
- **The broad gate's order**: `skills/code-review/orchestration.md` §*the
  pull request opens before round 1*: preflight, the pull request body and
  the changelog written, `broad-gate --base <base> --record <item>` with
  nothing else running, then the sealer's spawn. `agents/sealer.md` step 1:
  read `broad-gate.md`; absent or not HEAD is `not sound — no broad run at
  HEAD`. `guarantee.md`'s `Target SHA` row: `<sha> against <base>[; earlier
  run: <sha> <verdict>]`.
- **The closing word**: a `## Not verified` row whose first cell opens
  `closed ` is closed; `unverified_check.py#CLOSED = "closed"`, the bare word
  refused as the bare mark was.
- **The eval records**: `seal/specs/<id>/evals/baseline-<agent>.json`,
  `evals/<agent>-phase-N.md`, `evals/sealer-model.md`; the sealer's
  comparison runs `noninferiority.py run --tree <copy>` on a copy of the tree
  whose `agents/sealer.md` reads `model: sonnet`.
- **The parity verdict words** in `skills/legacy-parity/SKILL.md`:
  `differs`, `grounded`, `equivalent`, `unread`, each one lowercase word at
  the start of its line.

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
| `U+2705` as the closing mark | `skills/verify/scripts/unverified_check.py#CLOSED`, `templates/sdd-overview.md:38`, `templates/config.md:139`, `docs/the-record-layout.md` and `skills/implement/SKILL.md` §4's sentences, the four 0.22.0 items' `overview.md` rows | the word `closed`, read fail-closed; the old rows rewritten once by a script |
| `U+2B1C` as the question status | `templates/sdd-questions.md:10`, `skills/implement/SKILL.md` §4's sentence | the words `open` and `answered <date> by <who>` |
| The parity verdict emoji | `skills/legacy-parity/SKILL.md#"Parity review"` | four lowercase words |
| The `Reads:` docstring lines | 364 lines in `.py` files under `hooks/`, `skills/`, `evals/`, `.github/scripts/`, `tests/` | nothing reads them once the census leaves |
| The census and its reader | `tests/undeclared_readers.txt`, `tests/reader_registry.py`, `tests/test_a_reader_declares_its_input_class.py` | #956 audits readers from the code |
| The census rules | `docs/the-reader-registry.md` §*The four classes*, §*Who declares*, §*The census*, §*What neither check can read*, §*The counts at landing*; `CONTRIBUTING.md:247-251` | §*A frame names what its work removes* stays as the document's one rule |
| The rider stamps and their checker | `.github/scripts/rider_check.py`, the stamp cases of `tests/test_a_rider_reaches_its_file.py`, the `Verified … against …@…` line of 55 riders, `seal/follow-up.md:27-47`, `.github/workflows/test.yml:110-112`'s comment | the `RIDER:` comment stays, unstamped; a rider outliving its fix is the reader's finding |
| The grammar's three restatements and the check's constants | `templates/sdd-round.md:3-14, 32-60`, `templates/config.md` §*What no row governs*' label list, `chain_check.py:93-191` | the one table in `docs/the-review-record.md`, which the check loads |
| The sealer's broad run | `agents/sealer.md` step 1, `docs/the-broad-gate.md` §*One act, one owner, and the owner is an agent*, contract §2's sentence assigning it, `skills/code-review/orchestration.md:180-189` | the orchestrator's `broad-gate --record` before the spawn; the sealer reads the file |
| The pins that said one definition assigns the gate | `tests/test_broad_gate_rule.py::test_only_one_definition_assigns_the_broad_gate`, `::test_the_sealer_counts_the_silent_definitions_from_the_glob`, `::test_the_orchestrator_runs_the_preflight_before_it_spawns_the_sealer`, `docs/the-broad-gate.md`'s `Enforced by:` naming them | rewritten to the new fact: none assigns it, and the orchestrator runs it before the spawn |
| The sealer case model note and the `--list` sentence | `evals/README.md:34-35` | the generators' usage as it is |
| The pins on sentences the rewrites drop | the 42 modules naming `agents/`, the 11 naming the contract, the 12 naming `implement`, the 6 naming `code-review`, the 3 naming `writing-style` | each case re-pointed where its rule stays, removed with one line in the phase record where it pinned narration (`questions.md` Q7) |

## Open questions → questions.md

Every decision the tree could make is made above with its grounds; what
only the owner can settle, what a measurement settles and what the work
settles are the rows of `questions.md`, each with the default this run
takes.

Framed 2026-10-16 by framer, before the build.
