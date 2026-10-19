# Feature Specification: the scribe and legacy-parity are written anew from the scribe's job (#970)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

This item is the last of the four the owner split out of #957 on 2026-10-17
(#967 the smith and #969 the sealer merged in v0.22.1; #968 the framer runs
beside this one). The frame it builds on is #957's
`seal/specs/1792126889-every-agent-is-written-anew-from-its-job/spec.md`
§*The shape of a definition* and §*Marks and labels*, and #967's work item
`seal/specs/1792251842-the-smith-is-written-anew-from-its-job/` is the model
for how a rewrite is pinned and closed. Those are cited here and not
restated.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | No step asks a person mid-run. What needs the owner is a row of `questions.md` with its default |
| `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* | A fact has one source: the migration config's fields live in `templates/parity.md`, and `legacy-parity` points at them rather than copying the table. A skip map left with no entry is a mechanism with nothing to catch, and it leaves |
| `CLAUDE.md` §*Repo rule — a change writes fragments, never the shared file*; `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The changelog is this item's `changelog.md`, with no `## ` line |
| `docs/the-agent-set.md` | One contract every agent receives and one definition each; a subagent asks nobody; a spawn's payload is measurable and paid on every spawn |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | The `## Removes` table below is read by the review against the diff |
| `docs/the-review-and-parity-arms.md` §*Parity arm* | What the parity mark is and when the gate reads it. This item names who writes it and changes nothing the gate does |
| `skills/implement/SKILL.md` §*3. The SDD file set* | An agent's instructions and a skill an agent reads change, so the item sits on the top rung and this frame exists |
| `skills/implement/SKILL.md` §*Document layout — two roots, three lifetimes* | `docs/` holds the ratified norms where a repository has them, and a work item does not create a policy document; `skills/implement/orchestration.md:52-55` says the same of `docs/policies/<domain>/`. This is the layout B5 is checked against |
| `skills/agent-contract/SKILL.md` §4, §6, §12, §15, §19 | Every claim labelled; a definition names its own writes; the class is enumerated; a new case is seen red first; a change rewrites in place and removes what stood on the old fact in the same commit |
| #957's `spec.md` §*The shape of a definition* (items 1–6 and the preload paragraph) | The shape `agents/scribe.md` takes, and *the scribe opens `legacy-parity` at step 1* |
| #957's `spec.md` §*Marks and labels*, the row *Emoji in the files an agent reads*, and §*Data & interfaces* | The parity verdicts become the words `differs`, `grounded`, `equivalent` and `unread`, one lowercase word at the start of the label line, and `legacy-parity`'s Parity review section says so once |
| #957's `spec.md` §*How the rewrite is proved not worse*, and `questions.md` Q3 (answered by the owner, 2026-10-16) | No scribe case is written; the rewrite is measured on bytes, and its outcome is `unverified` with the owner named until a parity run happens |
| #957's `spec.md` §*The shape of a definition*, the preload paragraph: *where a skill is opened at step 1 of every spawn, deferring it saves the bytes of the spawn that never reaches step 1 and nothing else; the saving there is the skill written shorter* | Why the byte measure here is the read set and not the preload alone (§*How the rewrite is measured*) |
| #957's `questions.md` Q7 | The pins on the rewritten files are the work's to sort: re-pointed where a rule stays, removed with one line in the phase record where the sentence was narration |
| #970's body (the owner, 2026-10-17), guards 1–3 | The baseline is the tree this item starts from, 43cbc361. Guard 1 is answered below for the smith and the warden, whose steps name `legacy-parity` |
| #970's comment (the owner, 2026-10-18), items C5 of #2 and B5 of #1 | `legacy-parity` §*Recording the comparison* names who writes the record; `templates/parity.md`'s `Policy root` is checked against today's layout. Both are in this item's scope |
| #2's C1 and C2 (closed) | The smith's definition names no parity mark among its writes, and the scribe is forbidden from judging. The rewritten skill says which of its sections the scribe reads, so a scribe opening it at step 1 is not told to judge or to write |

## Scope

**In.**

- `agents/scribe.md` written anew to #957's shape: `skills: [agent-contract]`,
  the one contract sentence, `## Job`, `## Order of work`, `## Never`,
  `## Rules`, with `skills/legacy-parity/SKILL.md` opened at step 1. Its
  `description` stops saying the smith calls it: no agent spawns an agent
  (contract §6, `agents/smith.md` §*Never*), so the scribe is spawned by the
  session that orchestrates the work, before a phase is built or for a
  parity review.
- `skills/legacy-parity/SKILL.md` written to the same shape: one rule per
  section, its table, at most one sentence of why, and an `Enforced by:` line
  on each rule. Its four verdict labels become the four words. Its
  `## Recording the comparison` names its writer (C5). Its migration-config
  section points at `templates/parity.md` for the fields instead of copying
  them, and keeps the resolution order, with the asking and recording named
  as the caller's act.
- The `Policy root` class (B5), four sites and one sentence that state
  `docs/policies/` as the value a setup ships or proposes:
  `templates/parity.md:16` and `:33`, `skills/legacy-parity/SKILL.md:32`,
  `skills/parity-setup/SKILL.md:42-43`, `skills/implement/orchestration.md:240`.
  Each becomes the directory the repository keeps its ratified policy in, or
  `none`, and none proposes creating one.
- The readers of the scribe's preload and of the setup's asker: `README.md:41`
  and `:43`, `README.ko.md:40` and `:42` (the scribe's `Follows` cell and the
  count of skills the agents follow from their first tool call);
  `README.md:234` and `:421`, `README.ko.md:226` and `:379` (the smith named
  as the party that asks the setup question, which the orchestrator asks
  since #292).
- The pins on the two files sorted (Q7); the skip entries for #970 deleted
  (`tests/test_every_agent_reads_the_contract.py#NOT_YET_REWRITTEN`,
  `tests/test_the_record_is_written_in_words.py#SKIP`); `agents/scribe.md`
  and `skills/legacy-parity/SKILL.md` added to
  `tests/test_docs_line_wrap.py#COVERED`, written wrapped; the follow-up row
  that waited on this item deleted.
- The byte measurement, `overview.md` and the changelog fragment.

**Out, and whose.**

- `agents/framer.md`, its skip entry, its README row — #968, in its own
  worktree. Where the two items edit the same lines, `plan.md` §*Lines
  another item also edits* names them.
- The parity arm's behaviour and the hook messages that name *the
  legacy-parity skill* (`hooks/gate.py:199`, `:252`,
  `hooks/commit-review-gate.py:1217`, `:1228`) and
  `docs/the-review-and-parity-arms.md:210`: each names the procedure the mark
  comes from, which stays true, and none states a writer this item
  contradicts. Hooks are near #976's work.
- Who records the comparison for a smith's commit in a repository that
  declares `seal/parity.md`. The smith's definition names no parity mark
  among its writes and a routing declaration does not quiet the parity arm,
  so such a commit meets the parity ask. That is how the tree stands before
  this item and after it; this item only writes down who the writer is. It
  is reported to the owner as a candidate issue (`questions.md`, the head
  list) and changes nothing built here.
- `docs/one-root-by-lifetime.md:492` and its Korean twin, which count three
  agents under `agents/` where there are five — #941's documents, and not a
  sentence this item makes false.
- `skills/parity-setup/SKILL.md`, `templates/` and `skills/implement/orchestration.md`
  beyond the B5 sentences — #940; the orchestration file's other sections
  — #943.
- An evaluation case for the scribe or for a parity review (#957's Q3,
  answered by the owner).
- `Enforced by:` keeps its spelling; its rename is #941's.

## How the rewrite is measured

The scribe has no case, so the cost axis is the whole measurement, and the
outcome is `unverified` with the owner named as its answerer until a parity
run happens.

- **The preload** — `payload-meter --agent scribe`. At 1d665d48 (43cbc361's
  tree outside `seal/specs/`), `executed`: total 40,466 B, of which
  `agents/scribe.md` 3,763, `skills/agent-contract/SKILL.md` 16,603,
  `skills/legacy-parity/SKILL.md` 5,325 and the `CLAUDE.md` pair on this
  machine 14,775; the agent's share is 25,691 B. After the rewrite
  `legacy-parity` leaves the list, so this figure falls whatever the files
  say.
- **The read set** — the preload plus the files the scribe's steps open in
  every spawn: after the rewrite, `payload-meter`'s figure plus
  `skills/legacy-parity/SKILL.md`'s bytes at the same commit. Because the
  scribe opens `legacy-parity` at step 1, the preload's fall alone is not a
  saving, and #957's preload paragraph says why. **The read set's agent
  share is at or below the baseline's 25,691 B**, read at the build's last
  commit; the contract's bytes are the same on both sides unless a merge
  changes them, in which case the phase record says so and compares the two
  files the item writes, 9,088 B at the baseline.
- **Guard 1 for the smith and the warden.** Both definitions name
  `legacy-parity` at a step that runs only where `seal/parity.md` is declared
  (`agents/smith.md:33-34`, `agents/warden.md:37-39`). No file under `evals/`
  mentions parity (`git grep -l -i parity -- evals/` prints nothing,
  `executed` at 1d665d48), so no case of either agent opens the file, and
  their measured read set does not change here. They are not measured again.

## User scenarios & acceptance *(mandatory)*

Each row says what it protects: the defect it would catch, and why no other
case does.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The scribe has the shape and preloads the contract alone | Given `agents/scribe.md`, when read, then it opens with the one contract sentence, carries `## Job`, `## Order of work`, `## Never`, `## Rules` in order, and lists `agent-contract` alone | `tests/test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_contract_alone`, run on the scribe once its `NOT_YET_REWRITTEN` entry is deleted, red before the rewrite. Protects: `legacy-parity` creeping back onto the list |
| S2 The skill the step names exists | Given the scribe's steps, when one names a `skills/*/SKILL.md`, then the path resolves | `…::test_every_file_a_step_names_exists`. Protects: a renamed skill leaving a dangling step |
| S3 The scribe's rules stand with their enforcers | Given `## Rules`, when read, then each rule of §*Data & interfaces* stands and ends in an `Enforced by:` line that `rules --check` resolves | `bin/rules --check` exit 0; the two re-pointed pins (`tests/test_absence_claims.py::test_the_scribe_does_not_file_an_unrepeatable_absence_as_a_fact`, `tests/test_a_probe_that_commits_says_so.py::test_the_fact_finder_points_at_the_rule_it_no_longer_restates`) green; T3 new. Protects: a rule dropped in a later trim |
| S4 The scribe asks nobody and judges nothing | Given a scribe spawn whose original cannot be resolved, when it reaches the end of the resolution order, then it returns `original not found` naming what it tried, and writes no file and no verdict | T3 holds the sentences; the outcome is `unverified`, the owner named, until a parity run. Protects: the resolution order's last step, *ask the user and record*, read by a subagent that has no way to ask |
| S5 The parity verdicts are four words | Given `legacy-parity`'s Parity review section, when read, then its labels are `differs`, `grounded`, `equivalent` and `unread`, each the first word of its line, and no other label | T4 new, red on the tree as it stands; T6 green with `SKIP` gone. Protects: a mark coming back, or a fifth label nobody reads |
| S6 The record of a comparison names its writer | Given `legacy-parity` §*Recording the comparison*, when read, then it says the warden writes the mark in a review round and a session writes it where it compared itself, and that the scribe and the smith write none | T5 new, red on the tree as it stands. Protects: C5, a smith or a scribe reading *you* and writing the mark |
| S7 The policy root is a placeholder, and nothing proposes creating one | Given the five B5 sites, when read, then none states `docs/policies/` as a value to ship or propose | `git grep -n 'docs/policies' -- ':!seal/specs' ':!changelog' ':!tests' ':!.test_durations'` prints only `skills/implement/orchestration.md:54`, the sentence saying not to create it; `tests/test_chain_hooks_hardening.py::test_parity_declaration_is_bootstrappable_not_hand_written` green. Protects: a template that ships a directory the layout says a work item never creates |
| S8 No emoji where an agent reads, with no file skipped | Given every `agents/*.md`, `skills/*/SKILL.md` and `templates/*.md`, when read, then none carries an emoji or a proof block, and the case skips no file | `tests/test_the_record_is_written_in_words.py::test_no_file_an_agent_reads_carries_an_emoji_or_a_proof_block`, its `SKIP` and the code reading it removed; red first by the skip entry's own assertion once the four emoji are gone. Protects: a skip map kept with nothing in it, which reads as a hole |
| S9 Both files are wrapped | Given `tests/test_docs_line_wrap.py#COVERED`, when it holds both files, then every prose line is inside 88 columns | `tests/test_docs_line_wrap.py`. Protects: the scribe's 160-column line, which `seal/follow-up.md`'s row waited on |
| S10 What a reader of the README sees is true | Given `README.md` and `README.ko.md`, when read, then the scribe's row lists `agent-contract` alone, the skills count matches the rows, and no sentence names the smith as the party that asks a setup question | `git grep -n -i -E 'smith asks|smith works in a repository it asks|smith 가 그 레포' -- README.md README.ko.md` prints nothing; the reader's reading in the phase record. Protects: a plugin user told a subagent asks them something |
| S11 Rewritten in place | Given a fact this item removes, when the commit lands, then every sentence, pin and comment standing on it leaves in the same commit, enumerated by the greps the phase record names | `bin/rules --check` exit 0; `tests/test_no_passage_is_pasted_into_a_second_file.py` green; `git grep -n -w 'scribe\|legacy-parity' -- tests/` re-read in the phase record. Protects: the stale half misleading the next agent |
| S12 Measured on bytes | Given the build's last commit, when `payload-meter --agent scribe` runs, then the preload is below 40,466 B and the read set's agent share is at or below 25,691 B | the phase record and the changelog fragment, each figure with its commit. Protects: a rewrite that moved bytes from the preload to step 1 and called it a saving |
| S13 Nothing asks a person | Given this item's run, when any phase executes, then no step stops for an answer | `plan.md`'s rows; `questions.md`'s rows each with a default |

## Data & interfaces

- **The definition**: frontmatter `name: scribe`, `description` (spawned by
  the session orchestrating the work in a repository that declares
  `seal/parity.md`, to establish what the original does: facts with
  coordinates, no verdicts), `skills: [agent-contract]`; body `# scribe`, the
  contract sentence, `## Job`, `## Order of work`, `## Never`, `## Rules`.
  No `model:` key, as today.
- **`## Job`**: answer *what does the original do?* along the comparison
  axes, with coordinates; return facts, never verdicts; the scribe writes
  nothing durable, and its one output is the report.
- **`## Order of work`**: 1. open `skills/legacy-parity/SKILL.md`, the
  plugin's (the root two directories above the base directory the harness
  printed with the contract, as the warden's and the smith's step 1 say), and
  read the sections that find and trace the original; the judging and
  recording sections are the caller's. 2. resolve the original by the
  skill's order; where none resolves, return `original not found` with what
  was tried. 3. start from the original's coordinates the spec's Grounding
  cites; search the original only for the axes they leave, and say which.
  4. trace to what the original sends the client. 5. read constraints, enums
  and defaults; probe only what reading cannot settle (§7, §8). 6. report:
  per axis the behaviour, its coordinates and `read` or `executed`; then the
  coordinates the spec had wrong, the axes nobody looked at, and what is out
  of verified scope.
- **`## Never`**: ask a person anything or record an answer for one; write
  a file outside a probe, the parity mark and `parity-paths.md` included;
  give a verdict, a recommendation or a severity; compare against an
  original that was guessed; spawn an agent, post, push or open a pull
  request; put an emoji in the report.
- **`## Rules`**, each with its `Enforced by:`: facts, never verdicts; a
  guessed original proves nothing; start from the spec's coordinates and
  report the axis nobody looked at; constraints, enums and defaults are read,
  not probed; an absence carries its search, and one reported without it
  goes under what nobody has looked at.
- **The parity verdict words**, in `legacy-parity` §*Parity review*:
  `differs` (no grounds; align with the original), `grounded` (differs with
  grounds; quote them and confirm intent), `equivalent` (a different
  implementation, the same observable behaviour), `unread` (the original or
  the policy was not found; never a pass). One lowercase word at the start of
  the line.
- **The writer of the parity mark**: the party that compared and whose
  definition names the write. In a review round that is the warden
  (`agents/warden.md` §*Job*, step 5); where a session compared without one,
  the session. The scribe and the smith write none.
- **The `Policy root` value**: `<the directory the repository keeps its
  ratified policy in, such as docs/, or none>`; the setup reads it from the
  tree and never proposes creating one.
- **The skip maps**: `NOT_YET_REWRITTEN` loses `agents/scribe.md`; `SKIP`
  in `tests/test_the_record_is_written_in_words.py` leaves with the code
  that reads it.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `skills:` entry `legacy-parity` | `agents/scribe.md:10` | step 1 names the file |
| The paragraph explaining how the contract arrives | `agents/scribe.md:15-20` | the one contract sentence; the mechanism is the contract's opening |
| *Called by smith during implementation* | `agents/scribe.md:6-7` | the session spawns the scribe; no agent spawns an agent (contract §6) |
| The parenthesis on why worker findings are pre-verification, and the paragraph restating §6 | `agents/scribe.md:26-28`, `:30-33` | `## Job` names no durable write; contract §6 |
| The four emoji verdict labels | `skills/legacy-parity/SKILL.md:91-94` | the four words |
| The copy of the migration config's field table | `skills/legacy-parity/SKILL.md:28-33` | `templates/parity.md`, the one source |
| *ask the user and record the answer* as a step the reader of the skill takes | `skills/legacy-parity/SKILL.md:37-40` | the caller's act; the scribe returns `original not found` |
| The narration under the three-way table (*Inflating the open-questions count …*) | `skills/legacy-parity/SKILL.md:54-56` | the rule *inherit before raising* stays in one sentence |
| `docs/policies/` as the value shipped or proposed | `templates/parity.md:16`, `:33`; `skills/legacy-parity/SKILL.md:32`; `skills/parity-setup/SKILL.md:42-43`; `skills/implement/orchestration.md:240` | the placeholder and `none`; `implement`'s layout and `orchestration.md:52-55` |
| The scribe's skip entry | `tests/test_every_agent_reads_the_contract.py#NOT_YET_REWRITTEN["agents/scribe.md"]` and the docstring's *#968 to #970* (`:11-14`, `:139-141`) | the shape case runs on the scribe |
| The skip map of the emoji case | `tests/test_the_record_is_written_in_words.py#SKIP`, its comment (`:39-42`) and the loop reading it (`:73-84`) | nothing is skipped; the mechanism has nothing left to catch |
| The scribe's line in the line-wrap docstring, and the comment saying why it was not covered | `tests/test_docs_line_wrap.py:21`, `:146-147`, `:152-154` | the scribe and `legacy-parity` join `COVERED` |
| The follow-up row that waited on this item | `seal/follow-up.md` §*Schedulable items with nowhere else to go*, the `agents/scribe.md` line-wrap row | done here (`implement` §1: delete the row) |
| `legacy-parity` in the scribe's README row, and *The four the agents follow* | `README.md:41`, `:43`; `README.ko.md:40`, `:42` | `agent-contract` alone; the count read off the rows at the build's commit |
| *The smith asks* the setup question | `README.md:234`, `:421`; `README.ko.md:226`, `:379` | the session that orchestrates the work asks it (`skills/implement/orchestration.md` §*Orchestrator: Parity setup*) |
| Pins on narration in the scribe | whichever of the scribe's five pins (`tests/test_absence_claims.py:33-37`, `tests/test_a_probe_that_commits_says_so.py:127-135`, the ones above) pin a sentence no rule keeps | re-pointed where the rule stays, removed with one line in the phase record where it pinned narration (Q7) |

## Open questions → questions.md

Every decision the tree could make is made above with its grounds; what only
the owner can settle, what a measurement settles and what the work settles
are the rows of `questions.md`, each with the default this run takes.

Framed 2026-10-19 by framer, before the build.
