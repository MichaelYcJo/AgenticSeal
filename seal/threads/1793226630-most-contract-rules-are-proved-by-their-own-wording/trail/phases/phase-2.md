# Phase 2: 1793226630-most-contract-rules-are-proved-by-their-own-wording

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | the commit that adds this record; the next records commit writes its hash here and in `plan.md` |

## What this phase was asked

Count the phrase pins on rule sentences in every `tests/text` module except
`tests/text/test_the_agent_contract_holds_the_universal_rules.py`. Use the
method in `frame/design.md` *Data & interfaces*, at the commit phase 1
closed. Give one row per module, with its number and what it left out by
kind. `frame/questions.md` Q2 stands on its default (c). Each literal that
sits between a rule sentence and a word a checker reads is listed by line in
a column of its own, and the module's number leaves it out. Posting the
count on #1111 is the orchestrator's (contract rule 6), and this phase posts
nothing. No file outside the work item changes.

## The count

Taken at `ee746f3b` over the 39 modules. A row's number counts every
`assert` comparison of the form `<string literal> in <expression>` whose
expression is text read from a Markdown file and whose literal is prose of
that file. An `assert a in x and b in x` counts as two. *Left out* gives the
kinds the method excludes. *Q2* lists the lines another module uses to find
a paragraph. The last two columns are outside the method, and the notes
below say why they are shown.

| Module under `tests/text/` | Phrase pins | Left out, by kind | Q2 | `not in` | Name on the left |
|---|---|---|---|---|---|
| `test_a_document_has_room_for_the_next_fold.py` | 0 | citation 1 | | 2 | 1 |
| `test_a_gate_that_fails_says_so.py` | 1 | check line 1 | | 0 | 0 |
| `test_a_language_section_of_writing_style_opens_alone.py` | 1 | citation 3 | | 0 | 2 |
| `test_a_merged_ticket_says_so_on_the_tracker.py` | 0 | not Markdown 1 | | 0 | 0 |
| `test_a_moved_rule_leaves_its_definition.py` | 12 | heading 1, command 1 | | 1 | 5 |
| `test_a_parallel_agent_names_its_scratch_after_the_work_item.py` | 3 | path 3 | | 1 | 2 |
| `test_a_probe_does_not_outlive_its_round.py` | 5 | | `:41` | 0 | 0 |
| `test_a_question_says_who_can_answer_it.py` | 11 | field or marker 2 | | 2 | 1 |
| `test_a_record_carries_no_comment.py` | 0 | | | 0 | 0 |
| `test_a_release_cannot_ship_an_untrue_milestone.py` | 0 | not Markdown 8 | | 1 | 0 |
| `test_a_rider_reaches_its_file.py` | 9 | field or marker 1, command 1, not Markdown 1 | | 3 | 0 |
| `test_a_segment_feeds_the_flow_log.py` | 32 | citation 1, heading 1, path 4, field or marker 1, command 5 | | 13 | 7 |
| `test_absence_claims.py` | 5 | | | 0 | 0 |
| `test_broad_gate_rule.py` | 31 | citation 4, heading 3, path 2, field or marker 2 | `:105` | 4 | 7 |
| `test_ci_gives_the_checks_what_they_need.py` | 0 | not Markdown 3 | | 0 | 9 |
| `test_edits_go_through_the_edit_tool.py` | 6 | citation 1 | | 0 | 0 |
| `test_every_agent_reads_the_contract.py` | 0 | heading 1 | | 0 | 1 |
| `test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` | 4 | | | 0 | 0 |
| `test_guard_resolves_the_tree_it_judges.py` | 7 | | | 1 | 3 |
| `test_no_case_tells_the_agent_it_is_evaluated.py` | 0 | | | 0 | 1 |
| `test_no_passage_is_pasted_into_a_second_file.py` | 0 | not Markdown 3 | | 0 | 2 |
| `test_review_axes.py` | 10 | heading 1, path 1, field or marker 1, command 1 | `:109` | 3 | 12 |
| `test_settle_reads_before_it_removes.py` | 25 | citation 3, heading 2, path 4, field or marker 2, command 4, not Markdown 2 | | 24 | 2 |
| `test_the_chain_section_has_one_shape.py` | 2 | citation 1, path 1 | | 0 | 1 |
| `test_the_changelog_is_gathered_at_release.py` | 0 | | | 0 | 0 |
| `test_the_direct_answer_owes_the_sealers_record.py` | 3 | | | 0 | 2 |
| `test_the_gate_hands_cmd_a_path_it_can_run.py` | 0 | | | 2 | 1 |
| `test_the_handoff_before_round_one.py` | 24 | citation 5, heading 1, path 1, field or marker 6, command 1, not Markdown 1 | | 1 | 1 |
| `test_the_handoff_names_the_form_it_ran.py` | 2 | | | 0 | 0 |
| `test_the_mode_is_a_row_and_a_command.py` | 0 | heading 1, field or marker 1, fenced 2, command 1, not Markdown 1 | | 1 | 0 |
| `test_the_record_is_written_in_words.py` | 1 | field or marker 2 | | 0 | 0 |
| `test_the_records_can_be_carried_out_and_in.py` | 0 | path 2, command 4 | | 1 | 0 |
| `test_the_release_table_reads_two_trees_and_fails_nothing.py` | 0 | not Markdown 5 | | 0 | 0 |
| `test_the_release_tail_does_not_end_at_the_tag.py` | 25 | citation 1, path 2, command 1 | | 3 | 4 |
| `test_the_rules_claude_md_names_have_one_home.py` | 0 | | | 0 | 3 |
| `test_the_rules_have_one_owner.py` | 24 | heading 1, field or marker 1, command 1 | | 10 | 10 |
| `test_the_settings_have_a_front_door.py` | 12 | path 1, command 4 | | 1 | 2 |
| `test_the_suite_runs_with_gh_logged_out.py` | 0 | | | 1 | 1 |
| `test_the_verifying_round_is_bounded_not_cheapest.py` | 0 | | | 0 | 1 |
| Total | 255 | citation 20, heading 12, path 21, check line 1, field or marker 19, fenced 2, command 24, not Markdown 25 | 3 | 75 | 81 |

The three columns before `not in` add up to every candidate: 255 counted,
124 left out and 3 in Q2 make 382.

**Where each left-out literal stands**, by line at `ee746f3b`. A line with
two literals is written twice.

| Module | Lines, by kind |
|---|---|
| `test_a_document_has_room_for_the_next_fold.py` | citation `:22` |
| `test_a_gate_that_fails_says_so.py` | check line `:31` |
| `test_a_language_section_of_writing_style_opens_alone.py` | citation `:163`, `:172`, `:181` |
| `test_a_merged_ticket_says_so_on_the_tracker.py` | not Markdown `:76` |
| `test_a_moved_rule_leaves_its_definition.py` | heading `:570`; command `:423` |
| `test_a_parallel_agent_names_its_scratch_after_the_work_item.py` | path `:85`, `:95`, `:111` |
| `test_a_question_says_who_can_answer_it.py` | field or marker `:65`, `:78` |
| `test_a_release_cannot_ship_an_untrue_milestone.py` | not Markdown `:33`, `:50`, `:61`, `:94`, `:99`, `:131`, `:135`, `:154` |
| `test_a_rider_reaches_its_file.py` | field or marker `:131`; command `:60`; not Markdown `:124` |
| `test_a_segment_feeds_the_flow_log.py` | citation `:707`; heading `:144`; path `:145`, `:153`, `:391`, `:541`; field or marker `:217`; command `:179`, `:188`, `:188`, `:274`, `:641` |
| `test_broad_gate_rule.py` | citation `:81`, `:117`, `:139`, `:139`; heading `:36`, `:49`, `:103`; path `:344`, `:443`; field or marker `:359`, `:403` |
| `test_ci_gives_the_checks_what_they_need.py` | not Markdown `:602`, `:627`, `:643` |
| `test_edits_go_through_the_edit_tool.py` | citation `:104` |
| `test_every_agent_reads_the_contract.py` | heading `:100` |
| `test_no_passage_is_pasted_into_a_second_file.py` | not Markdown `:257`, `:258`, `:260` |
| `test_review_axes.py` | heading `:49`; path `:110`; field or marker `:112`; command `:111` |
| `test_settle_reads_before_it_removes.py` | citation `:237`, `:256`, `:279`; heading `:165`, `:278`; path `:40`, `:140`, `:203`, `:252`; field or marker `:137`, `:168`; command `:167`, `:203`, `:246`, `:272`; not Markdown `:296`, `:297` |
| `test_the_chain_section_has_one_shape.py` | citation `:99`; path `:95` |
| `test_the_handoff_before_round_one.py` | citation `:52`, `:52`, `:180`, `:220`, `:347`; heading `:28`; path `:160`; field or marker `:32`, `:247`, `:251`, `:252`, `:256`, `:300`; command `:228`; not Markdown `:465` |
| `test_the_mode_is_a_row_and_a_command.py` | heading `:47`; field or marker `:46`; fenced `:30`, `:30`; command `:23`; not Markdown `:59` |
| `test_the_record_is_written_in_words.py` | field or marker `:126`, `:135` |
| `test_the_records_can_be_carried_out_and_in.py` | path `:29`, `:43`; command `:28`, `:28`, `:42`, `:42` |
| `test_the_release_table_reads_two_trees_and_fails_nothing.py` | not Markdown `:36`, `:37`, `:38`, `:39`, `:40` |
| `test_the_release_tail_does_not_end_at_the_tag.py` | citation `:269`; path `:131`, `:220`; command `:140` |
| `test_the_rules_have_one_owner.py` | heading `:601`; field or marker `:550`; command `:319` |
| `test_the_settings_have_a_front_door.py` | path `:133`; command `:119`, `:134`, `:140`, `:177` |

## What this phase found

- **How the candidates were listed.** A probe in the session's scratchpad,
  `test_tmp_pin_candidates.py`, ran once and was deleted (executed). It
  parsed every module at `ee746f3b` and listed each `assert` comparison with
  a string constant or an f-string on the left of `in` or `not in`. That
  gave 382 `in` comparisons and 75 `not in` ones. Each `in` comparison was
  then decided by reading it beside its module's reader.
- **A command is a kind of its own.** The method's list of excluded kinds
  does not name a command spelling, such as `gh issue comment` or `seal
  mode --check`. `frame/questions.md` judgment 2 calls a command spelling
  an agent copies into a shell a fact a reader needs fixed. This phase built
  on that judgment, so the 24 command literals are left out. Counted as
  prose, they would make the total 279.
- **What *not Markdown* holds.** These literals are read from YAML
  workflows, from a Python script's docstring or source, or from a check's
  own output. *Field or marker* holds table separators and table-cell
  values, the verdict spellings `fixed <commit>` and `deferred <where it
  was repaired>`, the labels `executed`, `read` and `unverified`, the
  `Seal-Routing` trailer, an HTML marker, the `reopens:` field, a GitHub
  label, and the bar values that
  `tests/text/test_the_handoff_before_round_one.py` checks against
  `session_cost.py`.
- **Q2 is built on its default (c).** Three literals are bold leads that
  another module uses to find a paragraph:
  `test_a_probe_does_not_outlive_its_round.py:41` ("Commit before you
  mutate", found at
  `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py:82`),
  `test_broad_gate_rule.py:105` ("Capture once, filter locally", found at
  `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:109`)
  and `test_review_axes.py:109` ("Routing, decided at the start", found at
  `tests/behaviour/test_first_setup_asks_once.py:813`). Eleven other bold or
  lead literals were searched with `git grep -F` across `tests/` (executed).
  Two of them appear in another module, one as a pin and one in a comment.
  No other module uses any of the eleven to find a paragraph, so they are
  counted.
- **The issue's 182 does not bound the count.** `frame/design.md` says the
  issue's rough figure of 182 bounds the count from above. Under the method,
  255 literals count. A line grep for `assert "<literal>" in` over the same
  39 files finds 320 lines (executed), so no line count gives 182 either.
  How the issue reached 182 is not on record here. The owner, who wrote
  the figure, answers that.
- **Single words are counted.** Literals such as `never`, `two`,
  `orchestrator`, `discarded` and `overturned` are words of a rule sentence,
  and no checker reads them. Each one counts as a phrase pin.
- **The two columns the method does not count.** `not in` comparisons are
  negative pins, which are #956's row R37 and owned by #1038.
  *Name on the left* counts `in` comparisons whose left side is a name, such
  as a loop over a tuple of phrases. The method counts none of them, and
  some are phrase pins of the same kind, for example the loop over
  `CRAFTERS_FOUR_RULES` in `test_a_moved_rule_leaves_its_definition.py:481`.
  A phrase list checked through a comprehension and `assert not missing`,
  as in `test_the_rules_have_one_owner.py:272-284`, appears in neither
  column.
