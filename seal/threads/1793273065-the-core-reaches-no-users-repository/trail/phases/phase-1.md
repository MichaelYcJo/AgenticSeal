# Phase 1: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 5a283bd8 |

## What this phase was asked

Phase 1 of `frame/plan.md`, and only that phase. `skills/core/SKILL.md` holds
the core with the one added sentence. `CLAUDE.md` holds *The core* and
nothing else. Every `agents/*.md` lists `core` then `agent-contract` and opens
with the new sentence. The citations at `CONTRIBUTING.md:368`, `:381` and
`:473`, `tests/text/test_a_rider_reaches_its_file.py:66` and
`tests/behaviour/test_chain_hooks_hardening.py:773` name the core's path.
`.github/scripts/release_report.py#DOCUMENTS` gains the core. The tests that
read `CLAUDE.md` for the core read `skills/core/SKILL.md`. The line coordinates
were the framer's at `7280a7cc`, to be opened again before editing. The
block, the installer and the homes of the block's rules belong to phase 2 and
were not started. `frame/questions.md` Q1 and Q2 were built on their recorded
defaults. The owner answered Q1 with A1 while the phase was running, and that
is the default it was built on.

## What this phase found

**The frame held at every coordinate except one.** Each line the plan names
stood where it said at `c4864f48`. The exception is
`tests/behaviour/test_chain_hooks_hardening.py:773`. It said the first
spelling in its list is "`CLAUDE.md:39` verbatim". That spelling,
"questions go in **one batch** before the first edit", left `CLAUDE.md` with
#767 (`git log -S "one batch" -- CLAUDE.md`). Neither `CLAUDE.md` nor the core
holds it now. Giving that line the core's path alone would have stated
something false. The docstring now says the spelling is the one
`CLAUDE.md:39` held then, and that the rule now stands in the core's first
section in other words.

**The design's opening sentence does not fit on one line.** On one line it
is 115 columns. `tests/behaviour/test_docs_line_wrap.py` holds every
`agents/*.md` to 88. The shape case in
`tests/text/test_every_agent_reads_the_contract.py` refused any wrapped
sentence. The words are the design's, with one fixed line break after
"and both", the same in every definition. `SENTENCE` in that module carries
the break. A definition wrapped at any other point is still refused, and
`test_a_sentence_anywhere_but_the_opening_is_caught` plants two such wraps.
The old planted wrap replaced " binds", which the new sentence no longer
contains, so it would have passed against an unchanged definition.

**Four files outside the plan's row stated the old preload or the old home,
and were corrected in the same commit.** The class was enumerated with
`git grep` on "agent-contract` alone", "  - agent-contract", "binds you, and
it arrived", "CLAUDE.md`'s first goal" and the two section headings, outside
`seal/threads/` and `docs/`:

- `README.md` and `README.ko.md`, the agents table's preload column. It now
  reads `core`, `agent-contract`.
  `tests/behaviour/test_chain_hooks_hardening.py` requires every preloaded
  skill to be named in that column.
- `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_the_sealer_preloads_the_core_and_the_contract_and_nothing_else`
  and `tests/behaviour/test_the_sealer_guarantees.py#TestDefinition`. Both
  pinned the sealer's list as `agent-contract` alone.
- `.github/scripts/plugin_directory_check.py:42` and
  `tests/github/test_roll_flow_measurement_issue.py:144`. Each cited
  "`CLAUDE.md`'s first goal".
- `tests/behaviour/test_one_word_one_meaning.py#test_the_start_is_the_moment_before_the_first_edit`
  read `CLAUDE.md` for "before the first edit". It now reads the core.

`docs/branch-and-release.md:99` and `docs/release-checklist.md:193` also cite
"`CLAUDE.md`'s first goal". They are the policy root, which a pull request
does not edit. The design's `## Rule changes` already rewrites both.

**The paste ratchet's sanctioned entries were measured again.** The longer
opening sentence adds four 15-word runs to every pair of definitions, and
nothing else. The ten agent pairs in
`tests/text/test_no_passage_is_pasted_into_a_second_file.py#BASELINE` were set
to the new counts, with a comment naming this phase. No pair involving the
core or `CLAUDE.md` shares a run. `README.md` with
`skills/parity-setup/SKILL.md` measured 0 against its entry of 1. That entry
was left as it stands, because the module lets a drained pair keep its
entry.

**The core's frontmatter carries `user-invocable: false`, in
`agent-contract`'s shape.** `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md`
measured that this flag does not block preloading. The frontmatter has no
`disable-model-invocation` line, so the description carries `NOT for:`, as
`test_auto_firing_skills_declare_when_not_to_fire` requires.

**New cases, each seen red before the code:**
`test_the_sentence_names_the_core` and
`test_a_dropped_or_reordered_core_is_caught` in
`tests/text/test_every_agent_reads_the_contract.py`;
`test_this_repository_imports_no_core_and_names_the_tree_copy` and
`test_an_import_line_is_told_from_a_code_span` in
`tests/behaviour/test_the_installer_writes_the_block_from_its_template.py`
(design S3); and `test_the_core_names_where_the_routing_question_is` in
`tests/text/test_review_axes.py`. Design S4 assigns phase 2 a case reading
the core's routing sentence, and this case is that case. Phase 2 replaces
`test_the_preset_block_carries_the_routing_decision` beside it and writes no
second one. The release report's two-tree case now plants the core and reads
its row.

**`seal mutate`, one run per unit, each red.** The runs removed `- core` from
each of the five definitions, dropped the core from `DOCUMENTS`, and removed
the hook's name and then the section's name from the core's routing
sentence. One run added an `@skills/core/SKILL.md` line to `CLAUDE.md`. One
replaced every mention of the core's path in `CLAUDE.md`. Removing only one
of those three mentions survived, because two remained. The unit is "names
the core", so the run that broke all three is the one that counts.

**`bin/seal payload` after the commit.** Every agent lists
`skills/core/SKILL.md` at 6,711 bytes. The repository's `CLAUDE.md` is now
856 bytes. The framer's total went from 32,471 to 34,243 bytes on this
machine, whose `~/.claude/CLAUDE.md` is unchanged. Phase 3 owns the before
and after numbers the issue asks for.

**Two failures in the phase-boundary set predate this phase.** Both are in
the work item's own records, which this phase does not write.
`tests/behaviour/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`
is red because the work item has no `gaps.md` yet. It was red at `30631816`
without this phase's diff, run in a scratch worktree.
`tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census`
is red on `frame/design.md:33`, a real user path in the grounding table,
committed at `7280a7cc` and unchanged since.
