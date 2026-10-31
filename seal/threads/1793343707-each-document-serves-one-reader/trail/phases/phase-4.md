# Phase 4: 1793343707-each-document-serves-one-reader

## What this phase found

**`skills/implement/orchestration.md` went from 5,971 words to 3,422**
(executed, `wc -w` at `183a31b6` and at `70e52e18`). The design measured
5,959 at `59b63cfb`; phase 3's acts row added the other twelve. The two new
files hold 1,916 words (`skills/implement/acts.md`) and 514
(`skills/implement/multi-repository.md`). Neither is read in every run.

**The frame missed one citation of a moved heading, in the policy root.**
`docs/the-pact.md:59-60` cites `skills/implement/orchestration.md` *A work
item that commits in more than one repository*. The row's `git grep` does
not find it, because the citation wraps after "more than". A pull request
does not edit the policy root, and no rule change in `frame/design.md`
moves the citation. So the pointer sentence that stays in `orchestration.md`
opens with that bold lead: **A work item that commits in more than one
repository** asks the routing question once and points at
`skills/implement/multi-repository.md`.
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads a bold
lead as a section, so the citation resolves, one hop short of the procedure.
`gaps.md` *Not verified* names the orchestrator. It decides whether the
framer adds a rule change for that sentence.

**One departure from the frame: the spawn-prompt rule stayed.** The design
removes *The plan is approved at the spawn* whole, and the replacement it
quotes holds one paragraph. The old section's second paragraph, **The spawn
prompt is text an agent reads.**, is not about the approval line.
`tests/text/test_a_language_section_of_writing_style_opens_alone.py`
requires the orchestrator's spawn step to name the writing rules, and that
paragraph is the one that does. It now stands under the new heading, after
the design's paragraph, which is word for word. The acts row the design
gives gained one sentence for it: nothing reads the spawn prompt's shape
either.

**Where the frame held, the build follows it.**

- `skills/implement/acts.md` holds the section whole. Its opening names the
  five files it tables, this one included. Against the old section, the
  diff is the new row, the multi-repository row's act name and file, the
  table row's file, and "the three files" become the files the opening
  names.
- `skills/implement/multi-repository.md` holds the section whole under
  `## Orchestrator: a work item that commits in more than one repository`.
  The one word changed is "in the shape above". It now cites
  `skills/implement/orchestration.md` *Orchestrator: how the work is
  routed*.
- *What the answer writes* keeps its rows, the `automation` derivation, the
  `Automation` gate, the `Planning` row and the order block. The criterion
  sentences now cite `docs/the-review-and-parity-arms.md` *The declaration,
  and where the check went* and `docs/the-agent-set.md` *What a spawn
  costs*. The placeholder paragraph, the `Implementation` grounds and the
  `Answer pressed` paragraph are gone. So are the four-combinations table
  and the standing-waiver paragraph. Each left one sentence citing the
  policy section that holds it.
- `:33`, `:49-51` and `:268` no longer name the approval line, and
  `skills/code-review/orchestration.md:15` and `:172` cite `acts.md` and say
  the spawn is the approval.
- `agents/framer.md` gained *An orchestrator's reading of the frame is
  answered in one exchange*, word for word, before *The one route back is
  the review chain's*.
- `hooks/lib/launch.py#REFUSAL` ends at the command to type: "so name one
  explicitly: `python3.12 <script> ...`." The colon replaces the comma that
  led into the removed clause.

**The citation census.** `git grep -n 'which of these acts\|more than one
repository\|plan is approved at the spawn'` outside `seal/threads/` at
`70e52e18` gives these hits (executed):

- `skills/code-review/orchestration.md:15` reads `skills/implement/acts.md`.
- `skills/implement/acts.md:12`, `:69`, `:70` and
  `skills/implement/multi-repository.md:7`, `:37` are the moved headings and
  rows.
- `skills/implement/orchestration.md:348` is the pointer sentence.
- The test hits read the new files:
  `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`,
  `tests/behaviour/test_a_signer_declares_its_pact.py:104` and
  `tests/behaviour/test_one_word_one_meaning.py:741`.
- `docs/the-pact.md:3`, `hooks/lib/config.py:703`,
  `skills/verify/scripts/pact_check.py:4`, `templates/setup/config.md:402`
  and `tests/behaviour/test_a_signer_declares_its_pact.py:3` use the words
  in prose and cite no heading.

No hit cites *The plan is approved at the spawn*.

**The direction grep is the rule's own.** `git grep -l
'CONTRIBUTING\|CLAUDE\.md' -- agents templates 'skills/**/*.md'` prints
`skills/update/SKILL.md` alone, and every one of its hits names the user's
own `CLAUDE.md` (executed). `git grep -n CONTRIBUTING -- hooks/lib/launch.py`
prints nothing (executed). The other five shipped files that name
`CONTRIBUTING.md` do so in comments and docstrings. None of them prints its
docstring (executed, `grep -n __doc__`). The folded rule leaves them to
their reader, a contributor.

**Two policy sentences state the old fact until the settle.**
`docs/the-agent-set.md:130-136` says `skills/implement/orchestration.md`
tables the acts of three files. `docs/the-record-layout.md:281` names the
approval line. The design's `## Rule changes` holds the new sentence for
both.

**The moved reasoning is read where the policy in force holds it.** Four
cases of `tests/behaviour/test_waiver_decided_at_start.py` pinned the
grounds in `orchestration.md`. A new helper, `in_force`, reads them as the
policy in force: the section as `docs/` holds it, with each pending rule
change for that section applied. The four cases are
`test_the_preset_and_the_boxes_are_told_apart_in_the_file`,
`test_the_optional_row_ships_the_criterion_that_decides_it`,
`test_the_skill_states_all_four_combinations` and
`test_the_skill_refuses_a_standing_waiver_and_says_why_this_is_not_one`.
The same reading holds before the settle and after it. Each case also holds
the skill's citation of the section. Two assertions of the criterion case
left with no new home: "That is a step and not an answer to this row" and
"never deleted because the work is discovery". The policy's new sentence
"The row is deleted only for a work item that has no answer to give" now
carries the second.

**Removals `## Removes` did not name.**

- The `skills/implement/orchestration.md` entry of `DIRECT_REQUIRES` in
  `tests/text/test_the_direct_answer_owes_the_sealers_record.py`. It
  pinned the four-combinations table, which left. That module's
  closing-paragraph case now reads the skill's waiver sentence and the
  policy's.
- The counts "three" and "five" in the acts section's prose. Their mutant
  stayed green, and a count beside the list it counts is a copy, so the
  sentences now say "the files this file's opening names".

**The moves needed no case of their own.** The existing cases prove them at
the new paths:

- `test_every_orchestrator_act_names_its_delivery.py`, with `FILES` naming
  both new files and `TABLE_FILE` naming `acts.md`; its planted trees write
  the table there;
- `test_the_routing_step_mints_one_id_and_declares_only_in_gated_repositories`;
- the pact cases of `test_one_word_one_meaning.py`;
- `test_the_acts_table_row_names_the_preflight_and_stays_a_sentence`;
- `test_the_acts_table_says_no_commit_holds_who_wrote_the_two_lines`;
- the paste baseline, whose `README.md` pair moved from `orchestration.md`
  to `acts.md` at the same count of 1.

`tests/behaviour/test_docs_line_wrap.py` covers both new files from birth.

**Assumptions made under `automation`.** The new section of
`orchestration.md` carries no `check:` line. The design's text has none,
and its acts row reads `still a sentence`. The pointer sentences' wording
is this phase's. So is the launcher's colon.

**Four cases are new, and each was seen red first.**

- `test_an_orchestrators_reading_of_the_frame_is_answered_in_one_exchange`
  holds the framer's rule and the orchestration's section to the same
  three answers and the same bound.
- `test_a_redesign_is_approved_by_the_spawn_that_builds_it` holds
  `skills/code-review/orchestration.md`'s redesign row.
- `test_the_tables_opening_names_every_file_it_reads` holds `acts.md`'s
  opening to `FILES`.
- The `Answer pressed` sentence's pin was added to
  `test_the_preset_and_the_boxes_are_told_apart_in_the_file`.

The rewritten cases were shown red against the sources of `183a31b6`: the
four changed files written from it and the two new files moved aside, from
a backup kept in the scratchpad and restored by `cp` and checked by `cmp`
afterwards. The run gave exit 1, `24 failed, 170 passed` (executed).
The redesign case failed against `183a31b6`'s
`skills/code-review/orchestration.md` (exit 1) and passed after (exit 0).
The opening case and the `Answer pressed` pin were seen red through their
mutants below.

**Fourteen mutants, twelve red** (executed, `seal mutate` at `0dde0fab`
and the last two at `70e52e18`, each red run exit 0). Each red one broke
one unit:

- the framer's "one message each way";
- the section's "One exchange is the bound";
- the launcher's refusal given its `CONTRIBUTING.md` clause back;
- the criterion's citation of *What a spawn costs*;
- "The declaration moves the check and waives nothing";
- "nothing runs at the end";
- the new acts row's name;
- step 2's citation of the new heading;
- the fold line's "below the title";
- the redesign row's "the spawn is the approval";
- `acts.md`'s opening without `multi-repository.md`;
- the `Answer pressed` sentence reworded.

Two stayed green, exit 1. One was the acts prose's "five files", which
nothing pins and which is now gone (above). The other added a citation to
the `Answer pressed` sentence. Adding is no break, and nothing pinned the
sentence. The pin above was added, and its mutant went red. The tree was
clean after the last run.

**The phase-boundary set is 70 modules, run as one command.** It holds the
eleven modules row 4 names, every module that names a changed path or globs
`agents/` or `skills/`, and the modules that read this work item's records.
At `70e52e18` it gave exit 0, `3055 passed, 10 skipped` (executed). The
first narrow run over the 26 modules that read `orchestration.md` gave
exit 1, `17 failed, 784 passed`. Each failure was a pin on moved or removed
text, and each is listed above. `ruff check` and `ruff format --check`
passed over the twelve changed Python files (executed). `seal layout
--pairs` over the four modules that gained a case found 0 pairs (executed).

**Two edits went through the shell, each asserting its match** (contract
rule 9). One cut the acts section off the end of `orchestration.md`, after
the `Edit` tool did not match the 64-line block. The other made seven
substitutions in the acts test, each asserted to match once.
