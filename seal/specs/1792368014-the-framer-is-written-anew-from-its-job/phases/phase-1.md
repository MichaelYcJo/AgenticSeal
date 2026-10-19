# 1792368014-the-framer-is-written-anew-from-its-job — phase 1

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 2cb43374 |


## What this phase was asked

Write `agents/framer.md` anew to the four-section shape with
`skills: [agent-contract]`. It opens `implement`'s record-language section,
§1 and §3 at the ladder step, and `writing-style`'s `## English prose rules`
before writing. Follow the shape `agents/smith.md` and `agents/warden.md`
took. Sort the pins: a pin on a rule that stays is re-pointed, and a pin on
narration is removed with one line here. See the new pin for the
replace-or-keep rule red on the old file first. Delete the framer's
`NOT_YET_REWRITTEN` exemption, seen red first. Rewrite both README rows and
re-measure the pasted-passage allowances. Record the preload hashes and
`payload-meter --agent framer` before and after. #970's frame pauses on
`tests/test_every_agent_reads_the_contract.py` and the README agent rows,
and this item lands first. Q1: the restatement of the three answerers
leaves, and the rule that each row says why the tree could not answer it
stays with its pin. Q2: phase 2's paid side waits for #976 and #985.

## What this phase found

**The frame holds where it was checked.** The four preload files hash at
9b5c1be4 exactly as the baseline side's `specseal.preload` map records them
(`executed`, `shasum -a 256` against
`seal/specs/1792251842-the-smith-is-written-anew-from-its-job/evals/framer-phase-4.json`).
Nothing under `agents/`, `skills/`, `templates/` or `docs/` changed from
43cbc361 to 9b5c1be4 (`executed`, `git diff --stat`, empty).
`README.md:38` and `README.ko.md:37` are the framer's rows (`read`). The old
file was 367 lines and 19,545 bytes, as `plan.md` says (`executed`, `wc`).

**The frame did not name four places the rewrite made false.** Each was
corrected in 2cb43374, and `overview.md` holds the divergence rows.

- The README skills row in each edition said the four skills the agents
  follow from their first tool call are in the column to the left. That
  column now holds two. `tests/test_chain_hooks_hardening.py::test_the_readme_group_counts_are_derived_too`
  derives the groups from the `skills:` lists and went red. The rows now
  say two preloaded and fourteen on demand, with `implement` and
  `writing-style` in the list, and the case gained spellings for 2 and 14.
- `skills/implement/orchestration.md:381` and `:416` cited the framer's
  `## When you run` and §*You have no interactive phase*. Both now cite
  `## Job` and the rule *You ask nobody anything*.
- A comment in `tests/test_chain_hooks_hardening.py` cited the framer's
  diagram, and a docstring in `tests/test_waiver_decided_at_start.py` cited
  `## When you run`. Both are re-pointed.
- `tests/test_a_moved_rule_leaves_its_definition.py`'s docstring named the
  framer's 8-word run with §5 as the widest kept application. It is now the
  sealer's 8 words with §2, and the framer's widest is 5 words, with §11
  (`executed`).

**The preload, before and after** (`executed`, `bin/payload-meter --agent
framer`; the CLAUDE.md pair is outside the comparison).

| File | Before (9b5c1be4) | After (2cb43374) |
|---|---|---|
| `agents/framer.md` | 19,545 B, `c2e7a7d7…` | 9,424 B, `f70b2eb3…` |
| `skills/agent-contract/SKILL.md` | 16,603 B, `642b0da6…` | 16,603 B, `642b0da6…` |
| `skills/implement/SKILL.md` | 28,485 B, `dbff9bdf…` | not preloaded |
| `skills/writing-style/SKILL.md` | 21,720 B, `5e1a12a7…` | not preloaded |
| preload | 86,353 B | 26,027 B (−69.9%) |

The sections the steps open measure 14,202 bytes of `implement` (the record
language section 1,589, §1 5,652, §3 6,961) and 2,522 bytes of
`writing-style`'s `## English prose rules` (`executed`, `sed -n | wc -c` at
the headings' lines). A framer that opens all four carries 42,751 bytes
after the opens, against 86,353 at the baseline. Phase 2 reads the actual
opens from the traces.

**The pins, sorted.** Each pin on a rule that stays was re-pointed to the
new sentence.

- `tests/test_waiver_decided_at_start.py::test_the_framer_asks_nobody_and_writes_no_declaration`:
  *You have no interactive phase* became *You ask nobody anything*, and the
  raw `report,\nnever` assert is now read flat.
- `tests/test_the_handoff_before_round_one.py::test_the_framers_definition_carries_its_opening`:
  `framer_opening` became `framer_rule`, scoped to the rule *Bound each
  call, not the reading.*, and the skeleton is read from the whole file.
- `tests/test_a_question_says_who_can_answer_it.py#report_of` reads the
  hand-back step and the person-row rule in place of `## Report`.
- `tests/test_a_phase_hands_the_next_one_a_record.py::test_the_framer_is_told_it_writes_the_removes_section`:
  the bold report line became plain.
- `tests/test_a_reference_root_is_read_and_never_taken.py#NEVER_LINE`
  gained the framer's `## Never` line.
- These kept their phrases unchanged: `test_the_framers_acts_are_gather_judge_plan`,
  `test_questions_md_is_the_residue_and_every_row_says_why`,
  `test_the_framer_leaves_a_mark_in_the_tree`, rule 16 of
  `tests/test_the_rules_have_one_owner.py`, the settle carrier and the
  utility-skill home.

Each pin on narration left, one line each.

- `test_the_handoff_before_round_one.py::test_the_framers_definition_points_at_its_bar`
  pinned the pointer to the framing bar and *promises no saving*. The bar's
  one source is `docs/the-review-record.md` §*The per-segment bars*.
- The opening case's asserts on *the framers of 0.12.1 and 0.12.2*, on the
  absent *the 0.12.2 framers, never told*, and on the section order pinned
  #456's release readings.
- `test_a_question_says_who_can_answer_it.py::test_the_bound_on_section_five_is_stated_rather_than_assumed`
  pinned the report's §5 paragraph, which `## Removes` sends away. The
  bound's reasoning stays in that module's docstring.

**Seen red first** (`executed`). With the framer's `NOT_YET_REWRITTEN`
entry deleted and the new case written, both ran against the old file:
`2 failed, 25 passed, 1 skipped`. The two were
`test_every_definition_has_the_shape_and_preloads_the_contract_alone[agents/framer.md]`
and `test_the_framer_weighs_replacing_a_structure_as_an_equal_of_keeping_it`.

**The allowances, re-measured** (`executed`, `shared_counts` of
`tests/test_no_passage_is_pasted_into_a_second_file.py` on the new tree).
framer–scribe went from 65 to 0, framer–sealer from 65 to 14, framer–smith
from 72 to 24, and framer–warden from 67 to 31. The pairs with
`skills/implement/orchestration.md` (7), `templates/sdd-questions.md` (4)
and `templates/sdd-spec.md` (8) went to 0. The four kept entries are the
shape's shared sentences, which the baseline comment now names. The three
debt entries left.

**The removed phrases are gone** (`executed`, `git grep -F` outside
`seal/specs/`, `changelog/` and `.test_durations`). These find nothing:
*You have no interactive phase*, *How a frame opens*, *What you read, and
how widely*, *The three writes, and why*, *When you run*, *not the builder's
to draw*, *Do not promise a saving*, *The middle act is the one*, *Every
framer that read*, *its bar is the framing row*, *A row also says*,
*promises no saving*, *The frame is a drawing*, *phase prompt points at a
row*, *Two more skills are yours*, *the framers of 0.12.1* and
`framer_opening`. `## Report` remains only in `agents/scribe.md`, which
#970 rewrites, and in a planted fixture.

**Every unit added was mutated, and each mutation went red** (`executed`,
`bin/mutation-check`, file restored from held bytes each time).

- The replace-or-keep sentence: its case went red.
- The lead of the opening rule: `test_the_framers_definition_carries_its_opening` went red.
- The `Hand back.` step: both report cases went red.
- The `## Never` heading: the shape case, without the exemption, went red.
- The framer's `## Never` reference-root line: the reference-root case went red.
- The spelling 14: the group-count case went red.
- One lowered allowance (31 to 30): the paste check went red.

**The narrow runs** (`executed`). These 22 modules, in one `bin/test`
command, exit 0 with `1226 passed, 1 skipped` (the skip is the scribe's
shape case): `test_every_agent_reads_the_contract`,
`test_waiver_decided_at_start`, `test_the_handoff_before_round_one`,
`test_a_question_says_who_can_answer_it`,
`test_a_phase_hands_the_next_one_a_record`, `test_the_rules_have_one_owner`,
`test_chain_hooks_hardening`, `test_a_reference_root_is_read_and_never_taken`,
`test_one_word_one_meaning`, `test_docs_line_wrap`,
`test_settle_retires_the_process_record`,
`test_no_passage_is_pasted_into_a_second_file`,
`test_a_moved_rule_leaves_its_definition`,
`test_a_language_section_of_writing_style_opens_alone`,
`test_a_section_marked_for_one_role_reaches_only_that_role`,
`test_the_record_is_written_in_words`, `test_broad_gate_rule`,
`test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout`,
`test_a_segment_feeds_the_flow_log`, `test_unverified_rows_close`,
`test_the_set_a_work_item_always_has` and `test_chain_check`.
`bin/rules --check` exits 0 with all 508 targets resolving.
`uvx ruff check` and `uvx ruff format --check` over the nine changed test
files exit 0. The full suite is not run here (contract §2).

**For phase 2.** The new definition opens `implement` by three headings and
says to read the file whole where a heading is not found. The traces will
show whether a framer read the three sections by range or the file whole,
which is the context half of rule 5 that `spec.md` §*What moves rule 5*
reads. The batching rule stays as the rule *Bound each call, not the
reading.*

**Addendum: the merge of `release/v0.22.2` (461f00c6).** The orchestrator
asked for a merge commit after #976, #971, #943 and #970 landed, so that
2cb43374 and 14867ace keep the SHAs `plan.md` names. 461f00c6 merges
c26a791e into 91ada4be. Four files conflicted, and each resolution keeps
both sides' facts.

- `tests/test_every_agent_reads_the_contract.py`: #970 left the framer as
  the one entry in `NOT_YET_REWRITTEN`, and this branch left the scribe.
  With both rewritten, the dict is empty. The dict, the shape case's skip
  and `test_every_definition_preloads_the_contract` were removed. That case
  existed only to hold the skipped definitions to the contract. With
  nothing skipped, the shape case's `skills: == [agent-contract]` holds
  every definition, and its docstring now says so. No `Enforced by:` line
  named the removed case (`executed`, `git grep`).
- `README.md` and `README.ko.md`, the skills row: this branch said two
  preloaded and fourteen on demand, and #970 said three and thirteen.
  Recounted from the rows at the merge, every agent's `Follows` cell reads
  `agent-contract` alone. So one skill is preloaded, and fifteen are on
  demand: the twelve, plus `implement`, `legacy-parity` and
  `writing-style`. Six are typed. The two agent rows merged without a
  conflict.
- `tests/test_chain_hooks_hardening.py#test_the_readme_group_counts_are_derived_too`:
  both sides' spellings are kept (2, 3, 13, 14), 1 and 15 are added, and
  the docstring reads `22 = 1 + 15 + 6`.

Two changes outside the conflicts went into the merge commit.

- `tests/test_no_passage_is_pasted_into_a_second_file.py#BASELINE` gained
  framer–scribe at 4. #970's scribe carries the step sentence saying whose
  `skills/` paths are, so the pair shares four 15-word runs. The framer's
  other pairs measure as before (14, 24, 31) (`executed`).
- `skills/implement/orchestration.md:381` now reads *the framer runs only
  where §3 calls for a `spec.md`*. 2cb43374 had re-wrapped *and nowhere
  else* onto one line, and `tests/test_first_setup_asks_once.py::test_the_sentence_that_said_nowhere_else_is_gone`
  refuses that phrase in `implement`'s two files. Phase 1 did not run that
  module, so 2cb43374 left it red. The check reads the raw text, so a line
  break still hides the phrase, although its docstring says the words are
  matched one at a time. The check was not changed here.

After the merge, the framer's read set is unchanged. `agents/framer.md`,
the contract, `implement`, `writing-style` and the three templates hash as
they did at 2cb43374. `bin/payload-meter --agent framer` reads 9,424 and
16,603 bytes, so the preload is still 26,027 bytes (`executed`). The
release did not touch any of the seven files (`executed`,
`git diff --stat 43cbc361 c26a791e`, empty).

Narrow runs on the merged tree (`executed`). The test modules the release
changed, plus every module naming the framer, a README, an
`orchestration.md` or the `agents/*.md` glob, plus phase 1's modules: 72
modules in one `bin/test` command. They exit 0 with
`3998 passed, 9 skipped`. `bin/rules --check` exits 0 with 541 targets.
`uvx ruff check` and `uvx ruff format --check` over the three resolved
test files exit 0.
