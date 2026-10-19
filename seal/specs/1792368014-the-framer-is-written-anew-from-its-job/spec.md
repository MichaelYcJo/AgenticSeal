# Feature Specification: the framer is written anew from its job (#968)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| #968's body (the owner, 2026-10-17) and its two comments (2026-10-18) | The change, the baseline that moves one issue at a time, the three guards, one paid run with a `fail` fixed once before a second. Where this file and the body differ, the body holds |
| #957's `spec.md` §*The shape of a definition* (`seal/specs/1792126889-every-agent-is-written-anew-from-its-job/spec.md:92-160`) | The four sections, the one opening sentence, `skills: [agent-contract]`, a skill opened at its step, no incident narration, each rule ending in `Enforced by:`. The framer opens `implement` at the step that decides the ladder and the file set, and `writing-style` before writing the three documents (`:127-142`) |
| #957's `spec.md` §*Rules the rewrite states in place*, last row (`:283`) | The framer weighs the alternative that replaces a structure as an equal of the one that keeps it |
| #957's `questions.md` Q7 | Each pin on the rewritten file is re-pointed where its rule stays and removed, with one line in the phase record, where it pinned narration |
| `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* | Nothing stays in the definition because it is there; a change rewrites in place and removes what stood on the old fact in the same commit |
| `CLAUDE.md` §*The goal a design is chosen against* | No phase asks a person mid-run; every `questions.md` row carries a default |
| `skills/agent-contract/SKILL.md` §6, §10, §19, §20 | The writes a definition names are its whole permission; reads go out together; a change rewrites in place; a structure is a reference, not a constraint |
| `docs/the-agent-set.md` §*A subagent cannot ask anybody anything* | The framer reports a missing `routing.md` and never writes one. `Enforced by: tests/test_chain_check.py::TestFrame` already holds the mark side |
| `docs/the-review-record.md` §*The run* | The one route back to the framer (a routed `regression:`) and the `Reframed …` line. The definition cites it and opens it only on a reframe |
| `skills/implement/SKILL.md` §3 | The work alters an agent's instructions, so it sits on the top rung and this frame exists |
| `evals/scripts/noninferiority.py#verdict` at 43cbc361 | The five rules, rule 3 pooled per agent since #966 (8a100e13), judged against the baseline below |

## Scope

**In.**

- `agents/framer.md` written anew to the shape: frontmatter with
  `skills: [agent-contract]`, the one contract sentence, `## Job`,
  `## Order of work`, `## Never`, `## Rules`, and nothing else.
- The pins on the old file sorted per #957's Q7, the framer's entry in
  `tests/test_every_agent_reads_the_contract.py#NOT_YET_REWRITTEN` deleted,
  and one new pin for the replace-or-keep rule, seen red first.
- The framer's row in both README editions (`README.md:38`,
  `README.ko.md:37`), whose `Follows` cell and one sentence the rewrite makes
  false.
- The allowances `tests/test_no_passage_is_pasted_into_a_second_file.py`
  keeps for `agents/framer.md` (`:205-208`, `:226-228`), re-measured on the
  new file and removed where no longer needed.
- One new side of the framer's eval set, compared against the baseline
  below, and the phase record that reads it. Where it fails, its cause fixed
  once and one second side.
- This work item's `changelog.md` fragment with the framer's before-and-after
  row.

**Out, and why.**

- `skills/implement/SKILL.md` and `skills/writing-style/SKILL.md`. #967
  rewrote both, and the framer only opens them. A sentence of `implement`
  says it is *opened by the `smith` agent at its first step*; that stays true
  and is left as is, because any edit to either file changes the smith's
  read set and re-measures the smith (guard 1) for no rule.
- `skills/agent-contract/SKILL.md`. §20 already states the replace-or-keep
  rule for every agent; the framer's own sentence applies it to the
  Alternatives table.
- A new grader in `evals/behaviour/framer/`. The suite stays af9c924b's for
  every issue (#968's body), so a grader added now is not run by any side of
  this milestone. #957 named the framer cases' `shape-` graders as a holder
  of the replace-or-keep rule; until the suite moves, a test pin holds it.
  Whoever moves the suite after 0.22.x answers whether the grader is added.
- The framer's model. It has no `model:` key and runs on its session's;
  a model change would be measured as a definition change.
- `session_cost.py`'s framing bar (`"framer": ("framing", 1.4)`) and
  `docs/the-review-record.md` §*The per-segment bars*. The definition stops
  pointing at the bar; the bar and its reader stay where they are.
- The milestone close's guard 2 comparison against af9c924b (the issue's
  second comment). It is the milestone's act, read at no cost from kept raw
  output; this item keeps its raw output so the close can.

## The baseline, decided by guard 1

**The baseline is #967's last framer side,
`seal/specs/1792251842-the-smith-is-written-anew-from-its-job/evals/framer-phase-4.json`,
and no baseline run is taken.** It measured the tree af716289 on suite
af9c924b: 3,258,508 tokens across every model over 109 tool calls (29,894.6
per call), 86,353 preload bytes, $16.1196, 64 of 64 graders.

The framer's read set has not changed since that side was measured:

- **The preload.** The four files' sha256 at 43cbc361 equal the side's
  `specseal.preload` map byte for byte: `agents/framer.md` `c2e7a7d7…`, the
  contract `642b0da6…`, `implement` `dbff9bdf…`, `writing-style` `5e1a12a7…`
  (`executed`, `shasum -a 256` against the JSON).
- **The templates it opens.** `templates/sdd-spec.md`, `sdd-plan.md` and
  `sdd-questions.md` are untouched from f6ae6db6 (#967's merge) to 43cbc361
  (`executed`, `git diff --stat`), and none of #967's round fixes after
  af716289 names a template in its `location:` (`read`,
  `rounds/round-1.md` to `round-3.md`). af716289 does not resolve in this
  clone, because the branch was squashed (`executed`), so the hashes above
  are the comparison.
- **The sections it is told to open.** Two files it cites changed after
  f6ae6db6, both in f1c9932d (#975): `docs/the-review-record.md` gained
  §*The stamp* and nothing else, and `templates/config.md` changed at lines
  24, 223, 312 and 341, outside §*Reference specs* at 363 (`executed`,
  `git diff`). §*The run*, §*The per-segment bars* and §*Reference specs*
  are as they were.

Guard 1 counts a section its steps open, so the side stands. The reading at
file granularity would re-measure for those two files; `questions.md` Q2
holds that difference.

## What moves rule 5, and what the record shows if it does not

The framer failed rule 5 alone in #957 (28,253.1 → 33,595.1) and in #967
(27,296.7 → 29,894.6, +9.5%) with every grader passing and, in #967, total
tokens down 0.5% (`read`, the two records). The quantity the rule reads
splits in two:

> tokens per tool call = tokens per request ÷ tool calls per request

**Tokens per request is the context each request carries**, and the rewrite
controls it. At the baseline every request carries the 86,353-byte preload.
After the rewrite the preload is the definition and the contract, about
26–27 KB at the smith's and the warden's size (10,276 and 10,570 bytes plus
the contract's 16,603, `executed`, `wc -c`). The framer then opens three
sections of `implement` (the record language, §1 and §3, about 14 KB of
28,485) at the step that decides the ladder and the file set, and one
section of `writing-style` (`## English prose rules`, 2,522 bytes of 21,720,
or `## 문장 규칙` where `Record language` is Korean) before it writes. Every
request before the first open carries about 60 KB less, and every request
after both carries about 43 KB less. In tokens that is an estimate at
`payload-meter`'s uncalibrated 3.2 bytes a token, and nobody has measured it.

**Tool calls per request is batching**, and the rewrite does not control it
directly. #967's framer made 11 fewer tool calls on almost the same total
tokens, which is what raised its per-call figure. The rewrite keeps the
opening rule that governs batching (the spawn prompt's files in one call,
each later call bounded at about six reads, a long file read by range) so
that this half does not move for a reason the rewrite introduced.

The smith is the nearest precedent: 70.7% less preload gave 16.4% fewer
tokens per call, with both skills opened whole in all eight runs (#967's
`phases/phase-4.md`, `read`). The framer opens less of each skill than the
smith did, so the expectation is a larger fall. It is an expectation, and
the side decides.

**If rule 5 does not pass**, the phase record holds, per run and read from
the kept traces: the framer's requests, its tool calls, tools per request,
tokens per request, and the request at which it opened each skill with the
bytes it read. Beside them it holds the side-level totals against the
baseline's. The baseline's per-request figures cannot be recovered: #967's
raw output is not kept, and the side file records only the case session's
`turns` (`executed`, the JSON's run keys). So the reading against the
baseline is at the side level. Total tokens fell and calls fell further
means the cause is batching, as in #967. Total tokens that did not fall
means the cause is context: a skill read whole, or a wider reading. The fix
follows that reading, in one commit, and one second side is run.

## The read set after the rewrite (guard 3)

What the rewritten framer reads, in every run of its eval set: its
definition and the contract (preload); `skills/implement/SKILL.md` and
`skills/writing-style/SKILL.md` (opened); `templates/sdd-spec.md`,
`sdd-plan.md` and `sdd-questions.md` (opened). Where a frame calls for them:
`skills/confidence-check/SKILL.md`, `skills/feature-planner/SKILL.md`,
`templates/config.md` §*Reference specs*. On a reframe only:
`docs/the-review-record.md` §*The run*.

The concurrent work items, read from their issues and branches at the time
of framing (`executed`: no branch has a commit touching any of these files
yet):

| Item | What it is expected to touch | Meets the framer's read set |
|---|---|---|
| #976 | `docs/the-review-record.md` §*The stamp*, `skills/implement/orchestration.md:241-265`, stamp hooks | the file `docs/the-review-record.md`, not the section the framer opens; `orchestration.md` is not read by the framer |
| #985 | `docs/the-review-record.md` §*The round record*, `agents/warden.md`, the round record grammar | the same file, not the section; a sentence added to the contract would meet the preload |
| #943 | `skills/implement/orchestration.md` near :37, CI docs | no |
| #970 | `agents/scribe.md`, `skills/legacy-parity/` | no |
| #971 | `evals/scripts/` | not the read set. A change to `noninferiority.py#verdict` or to the side format changes how the comparison reads, and the compare is re-run at no cost |

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 One shape, one preload | Given `agents/framer.md`, when read, then it opens with the one contract sentence, carries exactly `## Job`, `## Order of work`, `## Never`, `## Rules`, and lists `agent-contract` alone under `skills:` | `tests/test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_contract_alone` with the framer's `NOT_YET_REWRITTEN` entry deleted, seen red on the old file first. Protects: the old shape surviving under an exemption nobody removes |
| S2 A step names what it opens, and the path resolves | Given the order of work, when a step needs `implement`, `writing-style`, `confidence-check` or `feature-planner`, then it names `skills/<name>/SKILL.md` and the file exists | `…::test_every_file_a_step_names_exists`; `tests/test_chain_hooks_hardening.py::test_each_utility_skill_is_callable_from_exactly_one_definition` keeps `framer.md` as the one home of the two utility skills. Protects: a dangling instruction an agent meets mid-run |
| S3 The skills are opened at their step | Given a framer spawn, when it reaches the step, then `implement` is opened before the frame is written and `writing-style` before the three documents | every shape and reach grader of the four framer cases passes on the new side (64 of 64 at the baseline); the phase record counts, from the traces, the runs that opened each skill. Protects: a definition naming a skill that the agent never opens, which S2 cannot see |
| S4 It asks nobody and writes no declaration | Given a spawn with or without `routing.md`, when the framer runs, then it asks nobody and a missing `routing.md` is reported, never written | `tests/test_waiver_decided_at_start.py::test_the_framer_asks_nobody_and_writes_no_declaration` and `::test_no_agent_definition_tells_an_agent_to_ask_a_person`, re-pointed to the new sentences. Protects: a framer writing an answer nobody gave |
| S5 Three writes and the mark | Given a frame, when written, then `spec.md`, `plan.md` and `questions.md` stand from their templates, `spec.md` carries `## Removes` and ends with the mark, and nothing else is written | the `shape-writes-*`, `shape-marks-the-spec`, `shape-builds-nothing-*` graders; `tests/test_waiver_decided_at_start.py::test_the_framer_leaves_a_mark_in_the_tree`, `tests/test_a_phase_hands_the_next_one_a_record.py::test_the_framer_is_told_it_writes_the_removes_section`, re-pointed. Protects: a frame with no evidence it was framed |
| S6 Replace weighed as an equal of keep | Given a frame that keeps or changes a structure, when the Alternatives table is written, then it carries the alternative that replaces the structure | a new case in the module holding the framer's rules, red against the old file (which has no such sentence), green after. `Enforced by:` names it. Protects: the rule #957 gave the framer being stated nowhere in its file |
| S7 The questions are the residue, and the report reproduces a person's row | Given `questions.md`, when written, then each row says why the tree could not answer it and who can; the report reproduces a person's row in full and gives the other two kinds as a path and a count | `tests/test_a_question_says_who_can_answer_it.py`'s three framer cases and `tests/test_waiver_decided_at_start.py::test_questions_md_is_the_residue_and_every_row_says_why`, re-pointed from `## Report` and the old section to the step and the rule. Protects: an approval given against a count of questions |
| S8 No per-segment figure, no narration | Given the definition, when read, then no tools-per-turn figure, release reading or incident account stands in it | `tests/test_a_moved_rule_leaves_its_definition.py::test_no_definition_states_a_tools_per_turn_figure` (exists); the narration pins removed with a line each in the phase record. Protects: a second copy of the bar drifting from `docs/the-review-record.md` |
| S9 Not worse | Given the new side on suite af9c924b, when compared with the baseline, then `evals/framer-phase-2.md` reads `pass` under the five rules, or `fail` with its cause read as §*What moves rule 5* says, fixed once, and `evals/framer-phase-3.md` reads the second side | `tests/test_a_rewritten_definition_proved_non_inferior.py::test_the_verdict_is_recomputed_from_the_records_numbers`; `noninferiority.py check` exit 0 on each record. Protects: a `pass` written over failing numbers |
| S10 The record can decompose rule 5 | Given the new side, when its record is written, then it holds tokens per request and tool calls per request per run, read from traces kept outside the tree at a named path | the phase record's table and the path; `Enforced by: nothing — a reading of traces, recorded once`. Protects: a second `fail` nobody can attribute, which is where #967 left this agent |
| S11 The READMEs state the preload | Given `README.md` and `README.ko.md`, when the framer's row is read, then `Follows` reads `agent-contract` and the row says the framer judges what the tree answers and leaves the rest to `questions.md` | `Enforced by: nothing — no case reads the README rows`; the warden's reading. Protects: the README telling a user the framer preloads two skills it does not |
| S12 A rebase that meets the read set re-measures | Given a rebase before the pull request, when it changes a whole file of the read set above or a section the framer opens, then the framer's side is taken again on the rebased tree | the orchestrator's sha256 comparison of the read set against the side's tree, recorded in the closing phase; `Enforced by: nothing — the orchestrator's act`. Protects: a pull request whose `pass` measured a tree it no longer has |
| S13 Rewritten in place | Given a sentence this item removes, when its commit lands, then every pin, copy and citation standing on it leaves in the same commit | `bin/rules --check` exit 0; `tests/test_no_passage_is_pasted_into_a_second_file.py` green; the phase record's `git grep` of each removed phrase finding nothing outside `seal/specs/` and `changelog/`. Protects: a pin that keeps a removed sentence's ghost |

## Data & interfaces

**The definition.** Frontmatter: `name: framer`, the existing
`description`, `skills:` with `agent-contract` alone, no `model:`. Body:
`# framer`, the sentence
`` `skills/agent-contract/SKILL.md` binds you, and it arrived before your first tool call. ``,
then the four sections.

- `## Job`: draw the frame for one work item, gather, judge, plan, report;
  the three writes and the mark; a write not named is not made.
- `## Order of work`, in this order: read `routing.md` (absent: report);
  write the skeleton `spec.md`; open `implement`'s three sections; read wide
  in the order of authority; judge, weighing replace against keep; where
  readiness or decomposition is in doubt, open `confidence-check` or
  `feature-planner`; before writing, open `writing-style`'s section for the
  record language; write `spec.md`, `plan.md`, `questions.md`; report. On a
  reframe, open `docs/the-review-record.md` §*The run* and rewrite as it
  says. Every `skills/`, `templates/` and `docs/` path is the plugin's, in
  the sentence `agents/smith.md` and `agents/warden.md` already carry.
- `## Never`: one line each, no incident.
- `## Rules`: one paragraph each, ending in `Enforced by:`.

**The paid runs**, scheduled by the orchestrator:

```
noninferiority.py run --agent framer --rev <commit> --suite-rev af9c924b \
  --out <scratch>/framer-phase-N.json --runs 2 -j 4 --max-cost-usd 25
noninferiority.py run --agent framer --from-raw <kept raw> --out $E/framer-phase-N.json
noninferiority.py compare --agent framer --phase N \
  --old $E/baseline-framer.json --new $E/framer-phase-N.json --out $E/framer-phase-N.md
```

`$E` is this work item's `evals/`. `baseline-framer.json` is a byte copy of
#967's `evals/framer-phase-4.json` (`cmp` exit 0), so this item's record
does not depend on a directory the next `settle` retires.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `skills:` entries `implement` and `writing-style` | `agents/framer.md:10-11` | the order of work opens each at its step |
| The paragraph explaining how the contract arrives | `agents/framer.md:16-25` | one sentence; the contract's own opening says how it arrives |
| The saving that was measured flat, and *Do not promise a saving* | `agents/framer.md#"Why the frame is not the builder's to draw">"Do not promise a saving"` | narration about the definition; #84 holds the measurement |
| The history of the judge act | `agents/framer.md#"What you are">"The middle act is the one this definition used to leave out"` | narration; the act stays as a step |
| The opening's release readings and the pointer to the framing bar | `agents/framer.md#"How a frame opens">"Every framer that read 1.00–1.12"`, `>"its bar is the framing row"` | narration; `docs/the-review-record.md` §*The per-segment bars* is the one source. The skeleton, the per-call bound and the read-by-range rule stay |
| The three-answerer explanation | `agents/framer.md#"questions.md is the residue, not a collection">"A row also says **who can answer it**"` | `templates/sdd-questions.md`, which the framer opens to write the file; the reason-per-row rule stays (Q1) |
| The sequence diagram and the account of the missing tool's measurement | `agents/framer.md#"You have no interactive phase, and you ask nobody anything"` | the rule stays in one line with *has no `AskUserQuestion`*; the measurement is in the docstring of the test that holds it |
| The `## Report` section's §5 paragraph and the README-editions incident | `agents/framer.md#"Report"` | the report's items become the last step; the person-row rule stays as a rule |
| `## When you run` | `agents/framer.md#"When you run"` | one line of `## Job`: the ladder of `implement` §3 decides it |
| The framer's shape exemption | `tests/test_every_agent_reads_the_contract.py#NOT_YET_REWRITTEN` `"agents/framer.md"` and the docstring's *#968 to #970* | the shape case holds the framer |
| The pins on the sentences above | `tests/test_the_handoff_before_round_one.py::test_the_framers_definition_points_at_its_bar`, the narration asserts of `::test_the_framers_definition_carries_its_opening`, and each other pin the sort finds on narration | removed with one line each in the phase record (#957's Q7, this item's Q3); a pin on a rule that stays is re-pointed |
| Allowances no longer needed | `tests/test_no_passage_is_pasted_into_a_second_file.py:205-208`, `:226-228` | re-measured on the new file; an entry the new file no longer needs leaves, and a lower one is written lower |
| The framer's preload and the batch sentence in the READMEs | `README.md:38`, `README.ko.md:37` | `agent-contract`; the framer judges from the tree, and the session asks the routing batch |

## Open questions → questions.md

Every decision the tree could make is made above with its grounds. What only
the owner can settle, what a measurement settles and what the work settles
are the rows of `questions.md`, each with the default this run takes.

Framed 2026-10-19 by framer, before the build.
