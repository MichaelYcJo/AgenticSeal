# Phase 1: 1794200906-settings-are-read-as-json

## What this phase found

**The frame holds for this phase, with one departure in the writer.** Each unit that `frame/design.md` *Removes* names for phase 1 stood at `fbe490e2` and is gone at `2351e28a` (executed: `grep` of each definition in `git show fbe490e2:<file>` and in the tree). The units are `lib/config.py#CONFIG_TABLE`, `#config_table`, `#config_rows`, `#config_text`, `#rows_named_below`, `#FIRST_CELL` and `#value_of`. They are also the sixteen units of `broad_gate.py` that the row lists, `seal.py#NEW_CONFIG`, `#with_row`, `#doubled_modes`, `#line_ending`, `#ending_of`, `#write_row` and its four re-exports, and `fold_check.py#config_rows`. The departures are below.

**This repository's `seal/config.json` is what the converter writes from `seal/config.md` at `fbe490e2`** (executed: `seal.converted` over `git show fbe490e2:seal/config.md`, then `seal.serialized`, compared with the committed file: equal, with no refusal).

**Departures from the frame, each with its grounds.**

- The writer does not serialize `dict(pairs)`, the form *Data & interfaces* gives. A dict keeps the last of two members with one key, so it would write a file holding one answer of two. `seal.py#doubled_keys` refuses such a file first, and `#serialized` writes `lib/config.py#Members` through `plain`, so every member keeps its place. A value that is not a string, such as an object a person added, keeps its type and its members' order. Judged against design G4 and #867: a key written twice has no value, so no write keeps one of the two.
- `broad_gate.py#missing_row` keeps its name. It now refuses a `Broad gate` key that `config.json` lacks, and it names `config.json`. Judged against design *Scope* item 3: the refusal for an absent key stays. Its walker arms left, as the *Removes* row names.
- `pact_check.py` prints the reader's own sentence after the path on an `UNREADABLE` signer config, not the fixed words "could not be read". A `config.json` can now also fail to parse as JSON, and "could not be read" says nothing about which failure it was. Judged against *Data & interfaces*: a refusal names the path and the parser's message.
- The eval scaffolds were converted in this phase (`c3495c85`), although `frame/plan.md` gives them to phase 5. The reader this phase built refuses a scaffold's `seal/config.md`, so `tests/evals/test_rule_cases.py#Test_main::test_a_sealer_case_body_is_its_own_part_then_its_records` went red at this phase's boundary. Phases 2 to 4 would have closed with a red case that no phase of theirs could clear. Judged against design *Scope* item 8: the scaffolds are generated from `evals/scripts/rule_cases.py#CONFIG` and `#SEALER_CONFIG`, which now hold JSON, so phase 5 owes the scaffolds nothing more.
- The walker's cases over the old table stay in `tests/lib/test_config.py` and run under `Test_gfm_table`, as two base classes, `_Old_config_table` and `_Old_config_shapes`. `seal layout --check` refuses a class whose name names no top-level definition of `lib/config.py`, and `config_rows` and `config_table` left. These cases test the walker the converter reads through, so they move with it in phase 4.

**Cases removed with the code they pinned** (design *Removes*, the row "the cases that pin a walker refusal of a settings table"). A JSON key has no walker cause, so none of these can recur:

- `tests/lib/test_config.py`: `Test_reference_roots::test_a_row_inside_a_fence_is_not_a_row`, `Test_config_text::test_accepts_the_file_as_utf8_text`, `Test_config_value::test_a_fenced_example_of_a_row_does_not_double_the_live_one`, `::test_a_line_that_will_not_parse_is_named_in_the_refusal`, `::test_a_refusal_is_per_item_and_never_an_absent_row`, `::test_refuses_an_item_written_again_below_the_stopping_line`, `::test_an_item_named_under_the_next_heading_is_another_tables`, `::test_a_line_below_the_stop_is_a_line_where_gfm_begins_one`, `Test_declared_mode::test_rows_above_the_header_are_not_rows_of_this_table`, `Test_config_table::test_every_config_reader_is_one_walk_over_the_sixteen_shapes` (its sixteen shapes now run through `seal.converted` in `tests/skills/test_seal.py#Test_converted`), `Test_pact_declaration::test_an_indented_pact_row_is_read_as_cmark_gfm_renders_it`, `::test_a_signer_config_the_walker_refuses_is_refused_after_the_pact`, and `Test_declared_pacts::test_refuses_a_signer_config_the_walker_refuses_with_exit_2`, which became `::test_refuses_a_signer_config_that_will_not_parse_with_exit_2`.
- `tests/skills/test_broad_gate.py`: every case of `Test_names_this_row`, `Test_refused_broad_row`, `Test_stopping_line`, `Test_rows_written_below`, `Test_hidden_row_at`, `Test_fence_left_open` and `Test_walker_refusal`, and the five walker cases of `Test_missing_row` (`test_refuses_to_call_a_fenced_row_absent`, `test_refuses_to_send_a_person_to_move_a_row_a_fence_above_swallowed`, `test_refuses_to_blame_a_fence_left_open_below_the_fenced_row`, `test_refuses_to_call_a_commented_row_absent`, `test_refuses_to_call_a_row_the_walker_did_not_read_absent`).
- `tests/skills/test_seal.py`: every case of `Test_ending_of`, `Test_line_ending`, `Test_doubled_modes`, `Test_with_row` and `Test_write_row`.
- `tests/skills/test_fold_check.py`: `Test_main::test_a_row_the_walker_did_not_read_is_refused_and_nothing_is_checked` and `Test_module::test_a_fold_row_written_again_below_the_stop_has_no_value`.
- `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`: `test_the_refusal_points_at_a_section_the_template_holds`, which read `missing_row`'s fenced-row arm.
- `tests/behaviour/test_a_signer_declares_its_pact.py`: `test_s4_the_configs_this_plugin_writes_or_copies_are_silent` became `test_s4_the_configs_this_plugin_writes_are_silent`. Its template half left, because a person no longer copies the template as the config (*Removes*, the row on `skills/commit-pr-convention/SKILL.md`).
- `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_the_documents_name_every_shape_the_walker_refuses_and_its_edit` lost its third document, `config_rows`' docstring, which left with the function.

**Cases added**, each seen red under `seal mutate` after `2351e28a` (executed; every verdict `red`, exit 0):

| Mutation | The case that went red |
|---|---|
| `config_pairs` reads a `config.md` standing alone as no file | `tests/lib/test_config.py#Test_config_pairs::test_refuses_a_config_md_standing_alone_and_names_seal_mode` |
| `config_pairs` decodes `utf-8` and not `utf-8-sig` | `#Test_config_pairs::test_accepts_a_byte_order_mark` |
| `parse_config` collapses the members through a dict | `#Test_declared_mode::test_refuses_a_mode_row_written_twice`, all three shapes |
| `parse_config` takes a top level that is not an object | `#Test_config_pairs::test_refuses_a_file_that_is_not_one_object_for_every_key`, the array, string and null shapes |
| `config_value` takes a value that is not a string | `#Test_config_value::test_refuses_a_value_that_is_not_a_string_for_that_key_alone`, all five types |
| `config_value` takes a key written twice | `#Test_declared_mode::test_refuses_a_mode_row_written_twice` |
| `serialized` escapes characters outside ASCII | `tests/skills/test_seal.py#Test_serialized::test_accepts_every_member_in_order_with_its_characters_as_written` |
| `doubled_keys` finds no key | `#Test_doubled_keys::test_refuses_each_key_written_twice_naming_it_once` and two shapes of `#Test_write_mode::test_refuses_a_file_it_cannot_write_the_key_into_and_leaves_it` |
| `write_file` follows a symbolic link | `#Test_write_file::test_refuses_a_name_that_is_not_a_file_and_writes_nothing[a link]` and the link shape of `#Test_write_mode` |
| `write_mode` writes over a file `config_pairs` refuses | four shapes of `#Test_write_mode::test_refuses_a_file_it_cannot_write_the_key_into_and_leaves_it` |
| `converted` keeps a row written twice | `#Test_converted::test_refuses_a_row_written_twice` |
| `converted` ignores the walker's refusal | 13 cases of `#Test_converted` |
| `convert` leaves `config.md` in place | `#Test_mode_report::test_converts_an_earlier_releases_config_md_and_removes_it`, both modes |
| `mode_report` never converts | the same case, and `#Test_mode_report::test_refuses_to_convert_a_table_it_cannot_read_whole` |
| `mode_report` prints no note beside both files | `#Test_mode_report::test_reads_config_json_and_names_a_config_md_beside_it` |
| `mode_report --check` passes an unconverted config | `#Test_mode_report::test_check_refuses_an_unconverted_config_and_names_seal_mode` |
| `broad_command` ignores a refusal from `config_pairs` | `tests/skills/test_broad_gate.py#Test_broad_command::test_refuses_a_file_that_will_not_read`, the undecodable, unparseable and unconverted shapes |
| `broad_command` ignores a refusal from `config_value` | `#Test_broad_command::test_refuses_a_row_written_twice`, both shapes |
| `missing_row` names `config.md` | `#Test_missing_row::test_refuses_to_send_a_person_to_the_table_no_command_reads` |
| `fold_check.py#declared` ignores a refusal from `config_pairs` | `tests/skills/test_fold_check.py#Test_main::test_an_unreadable_config_is_refused_not_read_as_no_row`, all four shapes |
| `declared` ignores a refusal from `config_value` | `#Test_main::test_a_row_written_twice_is_refused_and_nothing_is_checked[Document token ceiling]` |
| `pact_check.py` prints "could not be read" | `tests/skills/test_pact_check.py#Test_check::test_refuses_a_signer_config_that_will_not_read`, both shapes, and `tests/lib/test_config.py#Test_declared_pacts::test_refuses_a_signer_config_that_will_not_parse_with_exit_2` |

The other readers (`pr_body.py`, `.github/scripts/release_seal.py`, `.github/scripts/release_report.py`, `chain_check.py`, `unverified_check.py` and `lib/routing.py`) were already reading through `declared_value` or `policy_root`. In them, this phase renamed a constant or reworded a sentence from row to key and added no behaviour, so they owe no mutation run. Their existing cases, rewritten to build `config.json`, pass at `2351e28a` (executed, the plan row's command below).

**What phase 5 still owes these cases.** The cases below read the documents phase 5 rewrites, and they still pin the documents' table wording:

- `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`: `test_the_skill_names_the_file_and_the_row`, `test_the_template_is_one_item_value_table_whose_first_row_is_the_language`, `test_the_documents_name_every_shape_the_walker_refuses_and_its_edit` and `test_the_layout_lists_the_config`. The template's table is read through the walker (`items`) until the template holds JSON.
- `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py#test_the_allowed_list_says_how_a_pipe_is_written`.
- `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_the_template_documents_the_commented_row_sentence` and `#test_the_template_names_every_inline_html_kind_it_reads_as_before`.
- `tests/text/test_the_settings_have_a_front_door.py`, which asserts `<repo>/seal/config.md` in `skills/config/SKILL.md`.

**Verification.** The plan row's command passed (executed, exit 0, 1230 passed and 1 skipped). The phase boundary set, run as one command, holds the row's files, every test file this range changed, every test file naming a changed script or a changed helper of `tests/conftest.py`, and `tests/text tests/behaviour` (executed). It failed in two cases. `tests/evals/test_rule_cases.py#Test_main::test_a_sealer_case_body_is_its_own_part_then_its_records` was the scaffolds' unconverted config, which `c3495c85` cleared (executed: `bin/test tests/evals`, passing). `tests/behaviour/test_every_tracked_file_meets_every_census.py#test_every_file_no_module_file_declares_meets_every_census` names `frame/design.md:30` and `frame/plan.md:56`, which carry a real home path. The frame commit `fbe490e2` wrote both lines, and this range does not change them (executed: `git diff --stat fbe490e2 -- .../frame` is empty), so the case was red before this phase.
