# Phase 1: 1795432997-cases-copy-facts-whose-source-is-code

## What this phase found

**The frame holds for this phase, with three facts it did not state.** Each helper `frame/design.md` G9, G10 and G11 names was opened at `cbe092563`, whose `tests/` and `lib/` are `f885ba546`'s, and stood where the frame read it. `seal/follow-up.md` holds two rows, and neither waits on this phase (G18). The three facts follow. Each was judged against `frame/design.md` *Scope* items 2 to 4 and S2.

- `tests/behaviour/test_a_release_rolls_the_flow_measurement_issue.py#_tracker_section` did not cut a section named by its heading. It cut from a bold lead, `` **`flow-measurement` is a label that is not an index.** ``, to the next `## `. The lead stands inside `## A label answers *what it is about*, and survives the move`. Each of its two cases now reads that section through `section` and starts at the lead, so the text it asserts on is the text it read before.
- `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py#stamp_section` and the cut at the top of `tests/text/test_a_moved_rule_leaves_its_definition.py#crafter_rule` ran to the end of the file, not to the next heading. In both files the section is the last, so the readings agree (S9 below).
- `#_tracker_section` and `tests/skills/test_chain_check.py#template_section` each did more than the call: one starts at the lead, and one asserted that the template's section is empty. S2 names both, so both went and their callers call `section` inline. The emptiness assertion goes with `template_section`. `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py#test_the_spec_template_carries_the_rule_changes_section_above_removes` holds that fact, through `section`.

**Decisions settled while writing the code.** Each was judged against `frame/design.md` *Data & interfaces*, which gives `section`'s contract, and `CONTRIBUTING.md` *The test layout*.

- `section` stands at `tests/conftest.py:876`, beside `read`, `flat` and `flattened`. `lib/lines.py` is loaded once at module level, at `:873`, through `load_lib_module`, as `ROOT_MARKER` loads `lib/optin.py`.
- `section` keeps one guard on its argument, the count of matching headings. A first build also refused a `heading` that is no heading line. That guard could not fail a case: such an argument equals no heading's text, so the count is 0 and the count guard refuses it first. `d685ae9cb` took it out (contract rule 15).
- The block comment over the shared helpers said each "was defined byte-identically in two or more test modules". `section` was not, so the sentence goes and the comment keeps what a module does with them.
- A helper whose body would be only the call goes, as *Scope* item 3 says. That covers `test_the_contributor_has_a_procedure.py#guide_section`, `test_a_segment_feeds_the_flow_log.py#section_body`, and `test_both_editions_carry_the_same_folds.py#under_root`, which only `read` called. `test_a_parallel_agent_names_its_scratch_after_the_work_item.py` defines no wrapper. Each of its seven calls is `flattened(section(read(path), heading))`.
- `tests/skills/test_broad_gate.py#flat` is renamed `unquoted_flat`, for the block-quote marker it drops before it folds whitespace. `tests/skills/test_coordinates.py#section` is renamed `regions`, for the `(start, end)` regions the kernel's `heading_path` returns.
- `tests/lib/test_fields.py` calls `fields.read(text, fields.GUARANTEE)` wherever its `read` took the default, and `tests/github/test_issue_claims_check.py` calls `check.read`. An `ast` walk of each file finds no bare `read(` call, and every `fields.read` call has two arguments.
- Local names `section` in three cases would shadow the import: `test_the_suite_has_a_command_that_is_cheap_twice.py`'s, `test_the_chain_section_has_one_shape.py`'s and `test_a_release_rolls_the_flow_measurement_issue.py`'s. They are renamed `body` or `said`. The locals named `section` that remain are in cases that call no `section`. They stand at `test_the_pull_request_language_is_the_repositorys.py:76`, `test_the_stamp_reaches_the_person_it_is_drawn_for.py:63` and `:231`, and `test_broad_gate_rule.py:33`, and are inline cuts (*Scope* **Out**).

**Departures from the frame.**

- `tests/behaviour/test_the_contributor_has_a_procedure.py#test_the_check_can_fail` is removed, a removal `frame/design.md` *Removes* does not name. It held that the module's own `section` raised on a guide without the heading. That helper is gone. `tests/test_conftest.py#Test_section::test_refuses_a_longer_heading_that_begins_with_the_same_words` holds the shared helper's refusal of a text that lacks the heading, and the module's cases now read through that helper.
- `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py` already defines `STAMP`, the path of `seal_stamp.py`. The document's tuple is `STAMP_DOC`. The first boundary run of the changed modules failed on the clash before it was renamed.

**Q1 of `frame/questions.md`, answered by the work.** Every case keeps its assertion. The calls whose heading argument changed now pass the whole heading line, and are these:

| Module | Old argument | Argument now |
|---|---|---|
| `test_the_rules_claude_md_names_have_one_home.py#RULES` | the five headings' text | `### Work accumulates on a release branch`, `## House rules`, `## Orchestrator: what needs a person is asked in one batch, before the first edit`, `### 2. Implement test-first, and let each rule name its test`, `## Orchestrator: the order inside a ticket`; `#unlinked` takes the `#` run off for the link it looks for |
| `test_a_parallel_agent_names_its_scratch_after_the_work_item.py` | `Rules` four times, `17 `, two orchestrator headings' text | `## Rules`, `RULE_17` (the rule's whole heading line), `## Orchestrator: the order inside a ticket`, `## Orchestrator: from the preflight to the open pull request` |
| `test_broad_gate_rule.py` | `SPAWN_SECTION`, `Orchestrator: the order inside a ticket`, `Broad gate`, `The broad gate` | each with `## ` before it; `SPAWN_SECTION` keeps its text for the citation the first case pins |
| `test_a_rider_reaches_its_file.py#rows` | the two headings' text | each with `## ` before it |
| `test_a_release_rolls_the_flow_measurement_issue.py` | the bold lead | `DOC_HEADING`, then the lead inside it |
| `test_the_stamp_reaches_the_person_it_is_drawn_for.py` | `## The stamp ` | `## The stamp` |
| `test_a_moved_rule_leaves_its_definition.py#crafter_rule` | `\n## Rules\n` | `## Rules` |
| `test_chain_check.py` S3 | `\n## Rule changes\n` to `\n## Removes\n` | `## Rule changes` |
| `test_first_setup_asks_once.py`, `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`, `test_a_language_section_of_writing_style_opens_alone.py` | heading and level | heading alone; each heading was already the whole line |

**S9: the calls whose reading changed.** The probe `phase-1/plugin/probe_record.py`, under this work item's scratch directory, wraps each old helper by name. It covers the nine module-level `section` helpers and the item 3 helpers, every binding of the same function object among them, so `test_review_axes.py`'s import is caught too. It records what each call returned, per test node. It ran over the 20 modules at `cbe092563`, in a clone under the same directory, and recorded 117 readings (executed: 661 passed). With the shared `section` wrapped instead, it ran over the same modules on the working tree `7c1dcc2f0` then committed, before a comment of `tests/conftest.py` and the docstring of `Test_section` were reworded, and recorded 118 (executed: 660 passed; the one fewer is `test_the_check_can_fail`). `phase-1/compare.py` holds each old reading against its node's new ones. It folds whitespace and allows the old heading line, so it compares text and not line breaks. A line-reading case is held by its own pass at HEAD. It printed `same 112, changed 5`, and the 5 are these:

| Call | Difference | What the case asserts now |
|---|---|---|
| `test_first_setup_asks_once.py#test_the_readme_gives_the_switch_under_the_first_work_item`, `[README.md]` and `[README.ko.md]` | The old helper stopped only at the next `### `. `### Shared or local` and `### shared 인가 local 인가` ran past `## How it works` and `## 동작 방식`. The shared one stops there | The same six facts, read in the subsection alone; each stands there (executed: the case passes) |
| `test_first_setup_asks_once.py#test_the_readme_states_what_local_mode_leaves_unchecked_under_the_table`, both editions | the same cut | The table and the paragraph under it stand in the subsection (executed: the case passes) |
| `test_a_moved_rule_leaves_its_definition.py#test_the_crafter_reads_its_range_and_the_records_whole_before_it_hands_back` | `crafter_rule` returned the last paragraph of `agents/crafter.md` with its final newline, which the shared reading leaves out | The same phrases, by `in` |

The S3 parameter of `test_chain_check.py#test_refuses_a_section_the_parser_refuses_at_its_line` held `template_section` from collection, before the probe wrapped it. Both readings were run directly on that working tree, and each is `''` (executed). The probe can fail: it printed the five differences above. The copies of `read` and `flat` that *Scope* item 4 removes read the same file and fold whitespace the same way (read). `test_first_setup_asks_once.py#flat` alone differs, by `re.sub`. It kept one space at each end where `flattened` keeps none, and each of its callers asserts with `in` or splits on a phrase, so no assertion reads an end (read).

**Seen red, and `seal mutate`.** The six cases of `Test_section` were run before `section` existed: each failed with `AttributeError: module 'conftest' has no attribute 'section'` (executed). After `d685ae9cb` each guard was broken by `seal mutate tests/conftest.py`, one break per run, with `--tests "bin/test tests/test_conftest.py -q -p no:xdist -k <word>"`. Every verdict was `red`, exit 0, and each failing line was read for the guard named:

| Guard and break | Case that went red |
|---|---|
| `readable` read as `gfm_lines` | `test_accepts_the_live_heading_below_a_fenced_copy`, on the count guard, which found the fenced copy as a second heading; `test_refuses_to_end_a_section_at_a_heading_quoted_in_a_fence`, on a body cut at the fenced `## B` |
| `sections` read as a prefix match | `test_refuses_a_longer_heading_that_begins_with_the_same_words` |
| `len(found) == 1` read as `>= 1` | `test_refuses_a_heading_the_text_holds_twice` |
| `<= level` read as `== level` | `test_refuses_to_run_past_a_heading_above_its_level` |
| the level comparison taken out | `test_accepts_a_deeper_heading_as_part_of_the_body` |
| `start + 1` read as `start` | every case that compares a body |

A first run of the fence break gave `no baseline`, because its `-k` held `or`, which the command splits into separate arguments. It was run again with `-k fence`. No case of the ten converted modules is new, so none owes a red of its own. Their renames and moves are proved by their existing cases at the new names and by the census below.

**The census of the old names.** At `d685ae9cb`, S1's search and S2's search print nothing, and the control `git grep -n '^ *def section(' -- tests/conftest.py` prints `tests/conftest.py:876` (executed). Outside `seal/threads/`, `git grep` for `section_body`, `_tracker_section`, `_governs_nothing`, `stamp_section`, `running_the_checks`, `template_section`, `section_text`, `body_section`, `guide_section`, `test_the_check_can_fail`, `read_at_root` and `DOC_SECTION` prints nothing. It prints only `lib/gitcmd.py#under_root` and its callers, another function (executed). A citation `<test file>.py#<helper>` of any helper this phase moved prints nothing outside this work item's frame (executed). `bin/seal layout --check` exits 0, and `--pairs` names three pairs in `Test_section`, whose class docstring states what each pair differs by (executed).

**For the next phases.** Phase 2 edits four modules this phase touched, so it starts from them as they stand at `d685ae9cb`:

- `test_the_chain_section_has_one_shape.py#test_the_section_names_the_routing_answer_it_holds_for` reads `said` now.
- `test_a_language_section_of_writing_style_opens_alone.py:170` reads `section(text, WRITING_RULES)`, and `WRITING_RULE_CHECKS` still stands for phase 2 to remove.
- `test_waiver_decided_at_start.py` calls `flattened` where it called its own `flat`.
- `test_a_moved_rule_leaves_its_definition.py` imports `section` for `crafter_rule`, beside the `sections` phase 2 removes.

#1581 rewrites `tests/skills/test_broad_gate.py`, whose `flat` is `unquoted_flat` now, and `tests/skills/test_chain_check.py`, whose S3 parameter is a lambda over `section`.
