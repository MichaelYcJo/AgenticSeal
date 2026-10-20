# Feature Specification: the smith is written anew from its job (#967)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

This item is one of the four the owner split out of #957 on 2026-10-17. The
frame it builds on is #957's, merged at 2fc33333:
`seal/specs/1792126889-every-agent-is-written-anew-from-its-job/spec.md`
§*The shape of a definition*, §*Rules the rewrite states in place* and §*How
the rewrite is proved not worse*, and its `phases/phase-2.md`, the warden's
rewrite, which is the model this item follows. Those sections are cited here
and not restated.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | No step asks a person mid-run. What needs the owner is a row of `questions.md` with its default, and the evaluation runs on the orchestrator's account |
| `CLAUDE.md` §*Repo rule — a thing more than one party can have is named with whose* | The smith's hand-back names no seal of its own. Once the proof block leaves, `seal` keeps one meaning, the sealer's, and `tests/test_one_word_one_meaning.py` runs on the commit that removes the block |
| `CLAUDE.md` §*Repo rule — a change writes fragments, never the shared file* | The changelog is this item's `changelog.md`, carrying the per-agent table of §*A number in this frame names its moment* |
| `docs/the-agent-set.md` §*One contract every agent receives, and one definition each*, §*What a spawn costs* | The smith's definition is one file in the shape every definition has; what it preloads is the contract alone; a section an agent has no act for is not preloaded into it. The `Orchestrator:` sections of `skills/implement/orchestration.md` reach no smith spawn, which `tests/test_a_section_marked_for_one_role_reaches_only_that_role.py` holds from the `skills:` list |
| `docs/the-agent-set.md` §*What each party writes, and when* | A build phase leaves `phases/phase-N.md`; the fix pass writes two lines of each finding and no phase record; what the work removes is named once, here, under `## Removes` |
| `docs/the-review-record.md` §*The handoff*, §*The per-segment bars* | The hand-back carries the three labels, `executed`, `read`, `unverified` with the answerer named, and the suite labelled `unverified` with the orchestrator as its answerer. The smith has no tools-per-turn bar, so the rewritten definition states no figure |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | The `## Removes` table below is read by the review against the diff |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The item changes what a spawn reads and the instructions an agent acts on, so it sits on the top rung and this frame exists |
| `skills/agent-contract/SKILL.md` §2, §4, §6, §15, §19 | No agent runs the broad gate; every claim carries a label; a definition names its own writes; a new case is seen red first; a change rewrites in place and removes what stood on the old fact in the same commit |
| #957's `spec.md` §*The shape of a definition* (items 1–6, the preload paragraph) | The shape `agents/smith.md` takes and the rule that `implement` and `writing-style` are opened at the step that needs them |
| #957's `spec.md` §*Rules the rewrite states in place* | The smith's rule *a new test starts from its group*, held by `tests/test_a_moved_rule_leaves_its_definition.py` |
| #957's `spec.md` §*How the rewrite is proved not worse*, `evals/README.md` | The five rules of `noninferiority.py#verdict`, every one against the baseline; the suite fixed at af9c924b; a side cut short is no result |
| #957's `spec.md` §*Marks and labels*, rows *the proof block*, *`U+2B1C`*, *emoji in the files an agent reads* | The proof block leaves with its pins; the question status becomes the words `open` and `answered <date> by <who>`; no emoji in a file an agent reads |
| #957's `phases/phase-2.md` | The model: the pins recounted and sorted (its §*The pins (Q7), recounted*), each case seen red with the mutation named, the plugin-root path sentence in step 1, the writing-style step naming two sections by the record's language |
| #957's `questions.md` Q7 | The pins on the rewritten files are the work's to sort: re-pointed where a rule stays, removed with one line in the phase record where the sentence was narration |
| #967's body (the owner, 2026-10-17), guards 1–3 | The baseline is the tree this item starts from; an agent whose read set changed is measured again, here; the milestone's close judges each agent's last side against af9c924b's baseline, which is not this item's act |
| Orchestrator decision 1 (2026-10-18) | `agents/smith.md` is written anew to #957's shape as `agents/warden.md` was: `skills: [agent-contract]`; its build step opens `skills/implement/SKILL.md`; its hand-back and record steps open the `writing-style` section for the record's language; at or under the warden's size (10,527 B today); its rules: a new test starts from its group, commit before you mutate, the three-fix stop, the waiver in one sentence; the RIDER block, the proof block and the emoji leave |
| Orchestrator decision 2 | `skills/implement/SKILL.md` is written to the shape: the layout, the precedence, the ladder, the file set table, test-first, the closing memo, the fix pass; incident narration leaves; `## Proof block` leaves, and so does every other statement that an agent writes a proof block (`skills/verify/SKILL.md` §*Every agent seals what it verified, and one of them is final* and §*Seal block*, `templates/sdd-overview.md`'s applied block); the hand-back's three labels carry the claims and the sealer's `guarantee.md` is the one seal; a test holds that no file an agent reads carries an emoji or a proof block (#957 plan T6) |
| Orchestrator decision 3 | `skills/writing-style/SKILL.md` is restructured, not rewritten in content: the owner's writing rules stay as they are; it is opened, not preloaded; each language's rules form a section an agent can open alone (`## 문장 규칙` and `## English prose rules`); its one emoji goes. Its content is also how the orchestrator writes to the owner, so a rule leaves only where a test or the owner says so |
| Orchestrator decision 4 | The contract changed after #957's phase-3 measurements (2fc33333 rewrote §2's sentence; sha256 `e4f679e3…` in the phase-3 records against `9764cedd…` at HEAD, `executed`), so every agent's read set changed: the baseline is measured at 2fc33333 with `--suite-rev af9c924b` for the smith, the warden (it opens `writing-style` at its record step) and the framer (it preloads `implement` and `writing-style` today). One baseline phase, one or two build phases, one evaluation phase for the three, a close. About $60 a side for the three (#957's phase 3: 5.9980 + 36.6656 + 17.3532) |
| Orchestrator decision 5 | The framer's own rewrite stays #968's. This item measures the framer only because its read set changes here, and a framer `fail` whose cause is in `agents/framer.md` is recorded and carried to #968, not fixed here |
| Orchestrator decision 6 | #969 runs beside this item in its own worktree and moves the broad gate from the sealer to the orchestrator. The rewritten `agents/smith.md` states only that the smith does not run the broad gate (contract §2 holds who does) and names no other party as its runner; it carries neither today's *Then the sealer takes the broad gate once* nor any sentence about who runs it. #969 will not touch `agents/smith.md` |

## Scope

**In.** `agents/smith.md` written anew to the shape. `skills/implement/SKILL.md`
written to the shape with its cited headings kept. `skills/writing-style/SKILL.md`
restructured as decision 3 says. The proof block and every sentence saying an
agent writes one, in `skills/implement/SKILL.md`, `skills/verify/SKILL.md`,
`templates/sdd-overview.md`, `skills/verify/scripts/session_cost.py`'s
docstring, `README.md` and `README.ko.md`. Every emoji in a file T6 reads
except `skills/legacy-parity/SKILL.md`'s: `skills/writing-style/SKILL.md:260`,
`templates/sdd-questions.md:10` with its `Status` words, `skills/audit/SKILL.md:53-58`.
The pins on the three files sorted (Q7). The baseline at 2fc33333 and the
evaluation of the smith, the warden and the framer. `tests/test_docs_line_wrap.py#COVERED`
gaining `agents/smith.md` and `skills/implement/SKILL.md`, written wrapped, as
`agents/warden.md` and `skills/code-review/SKILL.md` joined at their rewrite
(`questions.md` Q2 holds the follow-up row this narrows). The changelog
fragment.

**Out, and whose.** `agents/framer.md`, its `skills:` list, its pins and its
`fail` on rule 5 at #957's phase 3 — #968; its preload shrinks here only
because two files it preloads shrink. `agents/sealer.md`, contract §2's
sentence naming the sealer, `docs/the-broad-gate.md`, `CONTRIBUTING.md:108`
and `skills/code-review/orchestration.md`'s gate order — #969. `agents/scribe.md`
and `skills/legacy-parity/SKILL.md` with its four emoji, which T6 skips by
name until #970 lands — #970. `skills/implement/orchestration.md` and
`skills/writing-style/outside-the-review.md` beyond a pointer the rewrite
keeps true — #940. `docs/` beyond a sentence this item makes false — #941;
`Enforced by:` keeps its spelling. The test layout beyond the modules this
item writes, re-points or deletes — #942. The noise of two runs a case and a
moving baseline — #966. The milestone's close against af9c924b — the release.
The emoji in output a script prints for a person (#957 Q9, the owner kept
them). The history sentences that say what `seal` once named (`CLAUDE.md:69-71`,
`skills/writing-style/SKILL.md` §*여럿이 가질 수 있는 것은 누구 것인지 밝힌다*)
stay as history. The rider's open question, why a 2026-09-08 reading was
zero, stays where the rider says it is, in work item 1788873640's
`questions.md` Q4; the rider itself leaves.

## The tree as it stands, measured

Read at ffd5f467 (= 2fc33333 outside `seal/specs/`); `executed` where a
command produced the number.

- **The three files** (`wc`): `agents/smith.md` 336 lines / 20,829 B, three
  `##` sections (`Phases`, `Boundaries`, `Report`), the RIDER block at lines
  87–125; `skills/implement/SKILL.md` 541 / 32,228, five `##` sections and
  `### 1.` to `### 6.` under `## Procedure`; `skills/writing-style/SKILL.md`
  322 / 21,000 (11,402 characters), seven `##` sections and eighteen `###`,
  eleven of them under `## 문장 규칙`. The model: `agents/warden.md` 167 /
  10,527; `agents/framer.md` 367 / 19,545.
- **Preload per spawn** (`payload-meter --agent`, agent share = total less
  the 13,318 B `CLAUDE.md` pair on this machine): smith 90,728 B (the
  definition, the contract 16,671, `implement`, `writing-style`); framer
  89,444; warden 27,198. #957's phase-3 records read 90,594 / 89,310 /
  27,032 at 93c1878c; the difference is the contract's 134 bytes at 2fc33333.
- **The read sets since #957's phase 3** (`shasum -a 256` against the
  `## New preload` tables of `evals/smith-phase-3.md` and `evals/framer-phase-3.md`):
  `agents/smith.md`, `agents/framer.md`, `skills/implement/SKILL.md` and
  `skills/writing-style/SKILL.md` are byte-identical to the measured ones;
  `skills/agent-contract/SKILL.md` is not (`e4f679e3…` then, `9764cedd…`
  now; `git log 93c1878c..HEAD -- agents/ skills/` names 2fc33333 alone). So
  guard 1 of #967's body fires for all three agents, which is decision 4.
- **Pins** (`git grep -l` over `tests/`): 18 modules name `agents/smith.md`
  (#957 counted 19 at d4552372), 12 name `skills/implement/SKILL.md`, 3 name
  `skills/writing-style/SKILL.md`. `tests/test_every_agent_reads_the_contract.py#NOT_YET_REWRITTEN`
  skips the smith's shape case by name for #967. The sentences the modules
  hold are listed in `plan.md` §*Technical context*.
- **Citations of `implement`'s headings outside `tests/` and `seal/specs/`**
  (`git grep`): 12 sites in 9 files — `CLAUDE.md` 2 (§*1. Read the spec
  before the code*, §*2. Implement test-first, and let each rule name its
  test*), `CONTRIBUTING.md` 1, `agents/framer.md` 3, `agents/smith.md` 1,
  `docs/the-record-layout.md` 1, `hooks/commit-review-gate.py` 1,
  `hooks/mode-gate.py` 1, `skills/implement/orchestration.md` 1,
  `templates/sdd-routing.md` 1 — every one of them §1, §2 or §3 by number
  or title; 2 test modules cite a heading by number. The contract's §11
  cites `## The language the records are written in` by title. Of
  `writing-style`'s headings, `agents/warden.md:40-43` names `## English prose rules`
  and `## 문장 규칙`, and `CLAUDE.md:70` names §*여럿이 가질 수 있는 것은
  누구 것인지 밝힌다*.
- **Marks in T6's corpus** — `agents/*.md`, `skills/*/SKILL.md`, `templates/*.md`
  (a Python sweep over the emoji blocks and the variation selector): 14 in
  7 files. `skills/implement/SKILL.md:534` `U+1F4CB`; `skills/verify/SKILL.md:584`
  `U+1F50F`; `skills/writing-style/SKILL.md:260` `U+1F534`;
  `templates/sdd-overview.md:9` `U+1F4CB`; `templates/sdd-questions.md:10`
  `U+2B1C`; `skills/audit/SKILL.md:53-58` five (`U+2705`, `U+26A0 U+FE0F`,
  `U+274C` twice); `skills/legacy-parity/SKILL.md:91-94` four (#970's).
  `agents/` holds none; the two READMEs hold none.
- **What says an agent writes a proof block** (`git grep -i`):
  `skills/implement/SKILL.md:527-541`, `skills/verify/SKILL.md:239-268`,
  `:310`, `:384`, `:578-610`, `templates/sdd-overview.md:9-12`,
  `skills/verify/scripts/session_cost.py:4`, `agents/smith.md:336`,
  `README.md:11`, `:39`, `:591-595`, `README.ko.md:11`, `:37`, `:583`;
  in `tests/`: `test_broad_gate_rule.py`, `test_one_word_one_meaning.py`,
  `test_a_segment_feeds_the_flow_log.py`.
- **The evaluation**: smith 4 cases × 6 graders (one `reach-`, five
  `shape-`: `built`, `committed`, `no-probe-left`, `phase-record`, `tested`),
  framer 4 × 8, warden 9 cases; two runs a case; 34 runs a side for the
  three. Spend of one side at #957's phase 3: $60.0168.

## A number in this frame names its moment or its bound

Every figure above is a reading at ffd5f467. The changelog fragment states
each before-and-after figure with the commit it was read at, from the eval
records and `payload-meter`, and nothing recounts a figure by hand. The
size target for `agents/smith.md`, at or under 10,527 B, is decision 1's and
is a target the phase record reads the file against, not a pass rule; the
pass rules are the eval's five.

## The shape this item gives each file

**`agents/smith.md`** takes #957's shape. `## Job`: builds one phase of one
work item or runs one fix pass, and its writes are the code and tests of the
phase, `phases/phase-N.md`, `plan.md`'s Status cell, `overview.md` and
`changelog.md` where the plan's row asks, and the two lines of each finding
in a fix pass. `## Order of work`: open `skills/implement/SKILL.md` and
follow it (the paths are the plugin's, as the warden's step 1 says); read
the work item and the handoff's coordinates, and say whether the frame holds
before building to it, a *no* going to the phase record and the hand-back;
stop where `routing.md` declares a framer and no `spec.md` exists; build the
phase as a vertical slice, each case seen red first; commit, then
`mutation-check` each unit added; run the narrow checks through the
repository's runner; close the phase, opening `skills/writing-style/SKILL.md`'s
section for the record's language before the record; in a fix pass, read the
round record first and write its two lines; hand back under the three
labels, the suite `unverified` with the orchestrator named, each declined
instruction as one line. `## Never`: ask a person or write `routing.md`;
present approaches or wait for a go; run the full suite, the lint or the
typecheck; name any party as the broad gate's runner (decision 6); build
beyond the request; spawn, post, push or open a pull request; edit through
the shell; restore a mutated file from HEAD; put an emoji or a proof block
in anything it writes; write in a reference root. `## Rules`, each with its
`Enforced by:`: a new test starts from its group; commit before you mutate,
and restore from `mutation-check`'s copy; mutation-test every unit added,
one command each, `-p no:xdist`, the 300 s bound; the three-fix stop, and
three returns through the broad gate read the same way; the waiver is one
sentence (`: '[no-review]'; git commit …`, or `git -c specseal.waive=review commit …`,
the last way past and never the first); find the runner, type the narrow
form; the broad gate is not yours and its label is, with the gate's per-file
words (`failing on base too`, `new?`) read when a failure is handed to you;
the frame is judged before it is built to; the handoff's facts are
coordinates to open; the phase record at each close; the fix pass's two
lines and the `location:` coordinate, then what the fixes left standing
(§12); the chain ends at a pull request, never a merge.

**`skills/implement/SKILL.md`** keeps the headings other files cite — `## The
language the records are written in`, `## Document layout — two roots, three
lifetimes`, `## Procedure` with `### 1.` to `### 6.` as titled today — and
one pointer line to `skills/implement/orchestration.md` in place of the
section about it. What each section holds is the rule, its table and at most
one sentence of why with a link. What leaves is named under `## Removes`.

**`skills/writing-style/SKILL.md`** keeps every rule and every heading. Each
of `## 문장 규칙` and `## English prose rules` opens with one line naming
what else applies to a writer who opened that section alone: `## 먼저`, `##
구성 규칙`, and the per-document section for the text being written. The
`U+1F534` at line 260 becomes the word. No section moves across a file
boundary and no rule leaves (decision 3).

**T6**, `tests/test_the_record_is_written_in_words.py::test_no_file_an_agent_reads_carries_an_emoji_or_a_proof_block`,
reads every `agents/*.md`, every `skills/*/SKILL.md` and every
`templates/*.md` for an emoji (the blocks `U+1F000`–`U+1FAFF`,
`U+2600`–`U+27BF`, `U+2B00`–`U+2BFF`, `U+2300`–`U+23FF`, and `U+FE0F`) and
for an `applied` or `sealed @` block; `skills/legacy-parity/SKILL.md` is
skipped by name for #970 the way `NOT_YET_REWRITTEN` skips a definition,
and the entry leaves with #970. It replaces
`test_the_template_the_format_and_the_two_definitions_carry_no_emoji`.

## User scenarios & acceptance *(mandatory)*

Each row says what it protects: the defect it would catch, and why no other
case does.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The smith has the shape and preloads the contract alone | Given `agents/smith.md`, when read, then it opens with the one contract sentence, carries `## Job`, `## Order of work`, `## Never`, `## Rules`, and lists `agent-contract` alone | `tests/test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_contract_alone`, its `NOT_YET_REWRITTEN` entry for the smith deleted. Protects: `implement` creeping back onto the list, which no eval sees while the output is right |
| S2 Each step names a file that exists | Given the smith's steps, when one names a `skills/*/SKILL.md`, then the path resolves | `…::test_every_file_a_step_names_exists`. Protects: a renamed skill leaving a dangling instruction |
| S3 The skill is opened when its act comes | Given a smith spawn, when it builds and when it writes a record, then its output has the shape `implement` and `writing-style` give it | the smith's five `shape-` graders pass on the new side at least as often as on the baseline (`evals/smith-phase-4.md` rule 3); the traces show `skills/implement/SKILL.md` opened in every run (the phase record counts them). Protects: a definition that names the skill and an agent that never opens it, which S2 cannot see |
| S4 The smith's rules stand with their enforcers | Given `## Rules`, when read, then each paragraph of §*The shape this item gives each file* stands and ends in an `Enforced by:` line that `rules --check` resolves | `bin/rules --check` exit 0; the re-pointed pins green (`plan.md` §*Technical context* lists them); new cases for the four rules decision 1 names (T3). Protects: a rule dropped in a later trim, #107's failure |
| S5 No runner of the broad gate is named | Given `agents/smith.md`, when read, then it says the smith does not run the broad gate and names no agent or party as its runner | T4, a case in `tests/test_the_seal_is_taken_once_by_the_sealer.py` replacing `test_the_smith_says_who_takes_the_gate_it_hands_to`; `OWNER_NAMED` empty. Protects: this item and #969 writing the owner into the same file from two worktrees, and a stale owner sentence after #969 |
| S6 No emoji and no proof block where an agent reads | Given every `agents/*.md`, `skills/*/SKILL.md` and `templates/*.md`, when read, then none carries an emoji or an `applied`/`sealed @` block, `legacy-parity` skipped by name | T6, red on the tree at phase 3's start (7 marks in 3 files after phase 2), green after. Protects: the block or a mark coming back as a habit |
| S7 `implement`'s cited headings stand | Given every citation of `skills/implement/SKILL.md` §N or §*title* outside `seal/specs/` and `changelog/`, when read, then the heading exists in the file | T5, a case in `tests/test_the_set_a_work_item_always_has.py`. Protects: a step renamed in the rewrite leaving `CLAUDE.md`'s two citations and the hooks' pointing at nothing |
| S8 Each language's rules open alone | Given `skills/writing-style/SKILL.md`, when `## 문장 규칙` or `## English prose rules` is read by range, then its first paragraph names the sections that also apply, and both headings are the ones `agents/warden.md:40-43` names | T7, a case in `tests/test_the_payload_meter_says_what_it_measured.py` or a new module; the warden's `shape-words-only` and record graders on the new side. Protects: an agent reading one section and missing the structure rules, or a heading renamed under the warden's step |
| S9 The baseline once, at 2fc33333 | Given the tree this item starts from, when phase 1 runs, then `evals/baseline-smith.json`, `-warden.json`, `-framer.json` stand under this item, none cut short, each with spend, tokens and preload bytes, suite af9c924b | `tests/test_a_rewritten_definition_proved_non_inferior.py::test_a_cut_short_side_is_no_result_and_never_a_pass`, `::test_a_run_records_what_it_cost`. Protects: a verdict read against #957's records, whose contract differs |
| S10 Each of the three agents proved not worse | Given the build, when phase 4 runs, then `evals/<agent>-phase-4.md` reads `pass` for the smith, the warden and the framer under the five rules, or reads `fail` with the cause named and the plan's row says what was done | `…::test_the_verdict_is_recomputed_from_the_records_numbers`; `noninferiority.py check` exit 0 on each. Protects: a `pass` written over failing numbers |
| S11 Rewritten in place | Given a fact this item removes, when the commit lands, then every sentence, pin, docstring and copy standing on it leaves in the same commit, enumerated by the greps the phase record names | `bin/rules --check` exit 0; `tests/test_no_passage_is_pasted_into_a_second_file.py` green; `git grep -n -i "proof block\|seal block\|implement applied\|verify sealed"` finding nothing outside `seal/specs/`, `changelog/` and the tests that quote history. Protects: the stale half of a file misleading the next agent |
| S12 The question status in words | Given `templates/sdd-questions.md`, when read, then the `Status` cell reads `open` or `answered <date> by <who>` and the template says so | `tests/test_a_question_says_who_can_answer_it.py:106` re-pointed to the new sentence; T6. Protects: `U+2B1C` coming back through the template |
| S13 Nothing asks a person | Given this item's run, when any phase executes, then no step stops for an answer | `plan.md`'s rows; `questions.md`'s rows each with a default. Protects: a run that stops at minute thirty |
| S14 The changelog table | Given the fragment, when the release gathers it, then a per-agent table reads preload bytes, tokens per tool call, spend and verdict at 2fc33333 and at the close, each with its commit | the sealer reads the fragment against the eval records; `tests/test_the_pull_request_language_is_the_repositorys.py`. Protects: a figure recounted by hand |

## Data & interfaces

- **A definition**: frontmatter `name`, `description`, `skills: [agent-contract]`;
  body `# smith`, the contract sentence, `## Job`, `## Order of work`,
  `## Never`, `## Rules` (#957's `spec.md` §*Data & interfaces*).
- **What the smith opens, and when**: `skills/implement/SKILL.md` at step 1;
  `skills/writing-style/SKILL.md` §`## English prose rules`, or §`## 문장 규칙`
  where `Record language` in the `seal/` root's `config.md` is Korean, before
  a phase record, `overview.md`, `changelog.md` or the hand-back;
  `templates/sdd-phase.md`, `templates/sdd-overview.md`, `templates/sdd-changelog.md`
  as `implement` §3 names them.
- **The hand-back**: the three labels of contract §4, the suite as
  `unverified` with the orchestrator named, each declined instruction as one
  line, changed files with absolute paths, what only a person can answer.
  No block.
- **The eval records**: `seal/specs/<id>/evals/baseline-<agent>.json` from
  `noninferiority.py run --agent <a> --rev 2fc33333 --suite-rev af9c924b --runs 2 -j 4`;
  `evals/<agent>-phase-4.json` and `-phase-4.md` from `run --rev <build> --suite-rev af9c924b`
  and `compare --phase 4`.
- **The question status words**: `open`; `answered <date> by <who>`.
- **T6's skip map**: `{"skills/legacy-parity/SKILL.md": "#970"}`.

## Rule changes

- nothing
  why: written outside docs/: the smith's job, in agents/smith.md; the agent split, in
    docs/the-agent-set.md.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `skills:` entries `implement` and `writing-style` | `agents/smith.md:9-10` | steps 1 and the record and hand-back steps name the files |
| The paragraph explaining how the contract arrives, and the opening's account of the skill | `agents/smith.md:15-28` | the one contract sentence; the mechanism is the contract's opening |
| The RIDER block and the waiver's narration | `agents/smith.md:76-86`, `:87-125`, `:127-129`, `:172-178` | one rule sentence; the rider's measurements are history, and its open question stays in work item 1788873640's `questions.md` Q4 |
| The design-gate narration and the ladder's copy | `agents/smith.md:57-75`, `:130-167` | the stop rule stays as one rule; the ladder and the second-rung list are `skills/implement/SKILL.md` §3's alone |
| *Then the sealer takes the broad gate once …* and the gate's owner | `agents/smith.md:299-303`, `:305-312`'s owner clauses | the smith does not run it, contract §2 holds who does (decision 6); the per-file words stay as a rule |
| *End with the `implement` proof block* | `agents/smith.md:336` | the three labels |
| `## Proof block` | `skills/implement/SKILL.md:527-541` | contract §4's labels carry the claims |
| The incident narration in `implement` | `skills/implement/SKILL.md:27-47` (#292's section, to one pointer line), `#"128 shell edits across 47 files"` (:296), `#"this repo's own history has two features"` (:315), `#"warden-persona-accuracy"` (:330), `#"Seven branches were measured"` (:341), `#"Two of the original four"` (:376), `#"The objection that sent task lists elsewhere"` (:408-422), `#"The directory used to be deleted here"` (:518-526) | the rules stay; the incidents are in the changelog and the issues |
| The sentences saying an agent writes a proof or seal block | `skills/verify/SKILL.md:239-268` (§*Every agent seals what it verified, and one of them is final*), `:310`, `:384`, `:578-610` (§*Seal block*); `skills/verify/scripts/session_cost.py:4` | the hand-back's labels carry the claims; the sealer's `guarantee.md` is the one seal; the `broad gate` row's fact is `docs/the-broad-gate.md`'s and the round record's |
| The applied block | `templates/sdd-overview.md:9-12` | nothing; the memo's four sections carry what the diff cannot show |
| `U+2B1C` and *ticked by whoever answered* | `templates/sdd-questions.md:10`, `:31` | `open`; `answered <date> by <who>`, written by whoever answered |
| `U+1F534` | `skills/writing-style/SKILL.md:260` | the word `CRITICAL` |
| The five emoji of the audit result block | `skills/audit/SKILL.md:53-58` | the words `passed`, `warnings`, `violations` at the start of each line (`questions.md` Q3) |
| The proof block's readers in `README.md` and `README.ko.md` | `README.md:11`, `:39`, `:591-595`; `README.ko.md:11`, `:37`, `:583` | the smith's row lists `agent-contract`; the trace a smith leaves is its hand-back under the three labels |
| The pins on the proof block | `tests/test_broad_gate_rule.py::test_the_seal_block_asks_for_the_row_too`, `::test_the_seal_reports_what_the_checks_cost`; `tests/test_one_word_one_meaning.py:181`, `:302`; `tests/test_a_segment_feeds_the_flow_log.py`'s mention | leave with the block |
| The pin on the gate's owner in the smith | `tests/test_the_seal_is_taken_once_by_the_sealer.py::test_the_smith_says_who_takes_the_gate_it_hands_to`, `#OWNER_NAMED` | T4 replaces it: no runner named |
| The pins on narration in the smith | `tests/test_the_contributor_has_a_procedure.py:195` (the rider's dated sentence); `tests/test_edits_go_through_the_edit_tool.py::test_the_implementer_keeps_the_half_that_makes_the_rule_its_own`'s `"RIDER"` assert; `tests/test_the_set_a_work_item_always_has.py::test_smith_and_the_skill_list_the_same_second_rung_work` (the copy leaves); `tests/test_a_moved_rule_leaves_its_definition.py:320` *Phase 2 is your caller's spawn*; `tests/test_chain_hooks_hardening.py::test_the_smith_says_whether_the_frame_holds_before_building_to_it`'s `1. **Requirements**` anchor | re-pointed to the rule's new sentence where the rule stays; removed with one line in the phase record where it pinned narration (Q7) |
| The emoji case T6 replaces | `tests/test_the_record_is_written_in_words.py::test_the_template_the_format_and_the_two_definitions_carry_no_emoji` | T6 |
| The smith's skip entry | `tests/test_every_agent_reads_the_contract.py#NOT_YET_REWRITTEN["agents/smith.md"]` | the shape case runs on the smith |
| The follow-up row's half about the smith | `seal/follow-up.md` §*Schedulable items*, the `test_docs_line_wrap.py` row | the smith joins `COVERED` at its rewrite; the row is narrowed to the scribe for #970 (`questions.md` Q2) |

## Open questions → questions.md

Every decision the tree could make is made above with its grounds; what only
the owner can settle, what a measurement settles and what the work settles
are the rows of `questions.md`, each with the default this run takes.

Framed 2026-10-18 by framer, before the build.
