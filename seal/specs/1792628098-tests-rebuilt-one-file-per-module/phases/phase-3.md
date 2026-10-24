# Phase 3: 1792628098-tests-rebuilt-one-file-per-module

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | ef753db7 |

## What this phase was asked

`tests/censuses.py` with one function per census that judges one file; `census_case` in `tests/conftest.py`, so that a module file ending `test_census = census_case(TARGET)` runs every census over its target; the stored exemption lists `OUT_OF_CLASS`, `ALLOWED`, `COORDINATE_EXEMPT` and `HEADING_EXEMPT` replaced by a comment on each exempted line, which the census reads and refuses where the line would not have been flagged; and the old census modules placed under the layout, each old case placed or cut with a line. S8 and S9 are seen red first. Phase 3 moves the censuses, so its boundary reaches every module the move touches, and the record names the modules run.

## What this phase found

**Measured at b247a92c, before the first edit** (`executed`).

- `git grep -l "git_listing\|tracked_text_files\|ls-files" tests/` prints 21 files: `tests/conftest.py` and 20 test modules.
- `OUT_OF_CLASS` in `tests/test_every_reader_ends_a_line_where_gfm_does.py` names 49 units and 50 calls in its two blocks, and the tree holds 49 units and 50 `.splitlines(` calls under `hooks/`, `skills/` and `.github/scripts/`.
- `ALLOWED` in `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` is empty. `ENTRY_POINTS_CLASSIFIED` in the same module, which the frame does not name, holds 2 paths.
- `tests/test_a_format_has_one_reader.py` holds `COORDINATE_EXEMPT` with 1 path and `HEADING_EXEMPT` with 7 lines.

**Whether the frame holds.** It holds for what a census is and where it runs. Two parts of its text did not survive the tree, and the build took the reading below.

- **An exemption stands on its own line directly above the line it exempts, not at the end of that line.** The first build put each exemption at the end of the flagged line, as `spec.md` rule 1 says. `ruff format` then split every line the comment pushed past 88 columns and moved the comment after the closing bracket: `if __name__ == "__main__":` became a three-line parenthesised test with the comment on its last line, so the comment no longer stood on the line the census flags. A whole-line comment is one the formatter never moves. The census reads the comment lines directly above a flagged line, refuses one that excuses nothing, refuses one written at the end of a line, and reads no comment that has no reason after its colon.
- **Which censuses moved.** The frame says every census over shipped files. A census moved where it judges one file by reading that file alone, so that it can run with the file's module: `encoding`, `entry_point`, `splitlines`, `coordinate_grammar`, `heading_rule`, `floor_syntax` (which also reads `ruff.toml`), `section_sign` and `real_identifiers`. These stay where they are, and why:
  - the checks that read a document's prose: `test_no_document_names_the_old_roots.py`, `test_a_release_is_sized_by_a_criterion.py` and `test_one_word_one_meaning.py`. They are #923's.
  - the checks that compare files with each other, `test_no_passage_is_pasted_into_a_second_file.py`, or derive a set across files: the set of scripts that run before any floor, in `test_a_script_says_which_interpreter_it_needs.py`, and the shipped paths in `test_the_release_check_watches_what_ships.py`.
  - the checks over records and over markdown against the oracle: `test_the_set_a_work_item_always_has.py` and `test_one_heading_rule_holds_to_commonmark.py`.
  - the other modules `git grep -l "git_listing\|tracked_text_files\|ls-files" tests/` lists build a fixture repository or read git's output, and judge no tracked file.
- `ENTRY_POINTS_CLASSIFIED`, which the frame does not name, was a stored list of exemptions too, and its two paths became comments above the `__main__` lines of `hooks/dispatch.py` and `hooks/launch.py`.
- A census over a file no module file declares still has to run somewhere, or a document and every module not yet rebuilt would lose it. `tests/test_censuses.py` sweeps every tracked file whose module file does not declare it, one git listing per run. When phase 7's batch places the last module, the sweep reads the documents alone.

**What the build changed in shipped files** (`executed`). 60 comment lines were added above the lines the five lists named: 50 `splitlines`, 7 `heading_rule`, 1 `coordinate_grammar` and 2 `entry_point`. Each of the 27 scripts that only gained comments parses to the same AST as at b247a92c, compared by `ast.dump` over `git show b247a92c:<path>` and the file on disk. Two other shipped files changed in what they say. `evals/scripts/noninferiority.py` loads `tests/censuses.py` by path to mask a kept record, because `tests/test_no_real_identifiers.py` is gone and `censuses.py` imports nothing from `conftest`. `.github/scripts/plugin_directory_check.py`'s docstring names the census.

**Each old case, and where it went.** Placed means moved as it stood into a class of `tests/test_censuses.py`. Merged means its input now sits in a case of the class that covers the same behaviour. Cut means removed, with the case or tree fact that holds what it guarded.

- From `test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`:
  - `test_every_file_the_plugin_reads_or_writes_names_its_encoding` and `test_every_hook_entry_point_opens_with_to_utf8`: rewritten as the `encoding` and `entry_point` censuses, run by `test_census` in each module file and by `Test_module`'s sweep.
  - `test_each_unnamed_shape_is_reported`, `test_each_named_shape_is_not_reported`, `test_a_receiver_no_import_binds_is_judged_under_every_spelling`, `test_an_aliased_module_is_resolved`, `test_a_function_imported_by_name_is_resolved`, `test_a_local_function_named_run_is_not_a_subprocess_call`, `test_an_import_inside_a_function_is_seen`, `test_the_unit_is_the_enclosing_qualname`: placed in `Test_unnamed_sites`. `test_no_method_is_matched_by_its_dotted_name`: placed in `Test_module`.
  - `test_what_the_walk_cannot_prove_counts_as_unnamed`: merged; its rows join the unnamed shapes' rows in one parametrized case, which the pairs report named as a pair.
  - `test_the_failure_names_the_site_and_the_repair`: merged into `Test_encoding`'s refusing case, which pins the whole line a person reads. `test_the_walk_reaches_a_root_nobody_listed`: merged into the same case, which judges `evals/new.py`.
  - `test_the_call_after_main_is_reported` and `test_the_call_first_is_accepted_and_a_module_is_not_an_entry_point`: merged into `Test_entry_point`'s two cases.
  - `test_every_classification_carries_its_grounds`: cut. A comment with nothing after its colon is no exemption, and `Test_judge`'s row `without-a-reason` holds that.
  - `test_a_classification_of_nothing_is_reported` and `test_an_entry_point_classification_of_nothing_is_reported`: cut. A comment that excuses nothing is refused, and `Test_judge::test_refuses_an_exemption_above_a_line_no_census_flags` holds it (S9). The second case's nested `hooks/sub/deep.py` moved into `Test_entry_point`'s refusing case.
  - `test_a_skipped_file_does_not_read_as_a_lost_classification` and `test_a_deleted_entry_point_declines_rather_than_drops_its_row`: cut. No list is left to lose a row, and the sweep's corpus skips a deleted file through `tests/conftest.py#on_disk`, whose cases are in `tests/test_a_shrunken_corpus_declines_to_judge.py`.
  - `test_the_rule_is_where_a_contributor_reads_it`: left for #923, in the same file, asserting the sentence that now names the censuses. `test_a_mark_that_is_not_utf8_reads_as_text_rather_than_raising`: left in the same file for the batch that places `hooks/commit-review-gate.py`.
- From `test_every_reader_ends_a_line_where_gfm_does.py`: `test_every_splitlines_call_left_is_named_with_its_reason` rewritten as the `splitlines` census, and its count per unit became one exemption per line; `test_the_class_case_sees_a_planted_call` merged into `Test_splitlines`' refusing case.
- From `test_a_format_has_one_reader.py`: the two greps rewritten as `coordinate_grammar` and `heading_rule`, each with a class of fixture cases. `test_every_coordinate_exemption_still_holds_the_fragment_it_excuses` and `test_every_heading_exemption_still_matches_a_line`: cut, held by S9's case.
- From `test_a_script_says_which_interpreter_it_needs.py`: `test_what_runs_before_any_floor_needs_nothing_its_python3_lacks` split three ways. Its planted constructs went to `Test_newer_than`, its globs to `Test_matches`, and its check of each file's constructs became the `floor_syntax` census. What stays, renamed `test_what_runs_before_any_floor_is_linted_at_the_floor`, holds the derived set to `ruff.toml`'s table both ways.
- From `test_no_living_file_writes_the_section_sign.py`: the sweep rewritten as `section_sign`; `test_a_sign_is_refused_at_its_line_and_a_record_is_not_read` placed in `Test_section_sign`, split into its accepting and refusing halves.
- From `test_no_real_identifiers.py`: `test_only_neutral_domains` and `test_only_fixture_user_paths` rewritten as `real_identifiers`. `test_the_sweeps_still_report_nothing_on_a_clean_fixture` merged into `Test_real_identifiers`' accepting case, and `test_the_product_host_is_allowed_bare_and_under_the_directory_only` split between the two cases. `test_the_domain_sweep_survives_a_tracked_file_the_tree_deleted` and `test_the_user_path_sweep_survives_the_same_tree`: cut, held by `on_disk`'s cases as above. The module excluded its own file from its corpus. `censuses.py` needs no exclusion, because it builds its user-path pattern from two halves.

**The cases, and how each was seen red** (`executed`). Before `tests/censuses.py` existed, the four layout modules stopped at collection. After it, `bin/mutation-check` broke each new unit, with `bin/test tests/test_censuses.py -q -p no:xdist` as the command unless the row names another. S8 is k18 and k20, S9 is k5.

| # | Mutation | Verdict |
|---|---|---|
| k1 | any comment line exempts from every census | red |
| k2 | an exemption applied to no line | red |
| k3 | an exemption at the end of the file not refused | red |
| k4 | an exemption read in the middle of a comment line | SURVIVED, then red after cb7eba8e |
| k5 | a comment that excuses nothing not refused | red |
| k6 | a flagged line passed whatever stands above it | red |
| k7 | a census's directories not read | red |
| k8 | `encoding` returns nothing | red |
| k9 | no `__main__` block flagged | red |
| k10 | `entry_point` reads files outside `hooks/` | red |
| k11 | `splitlines` flags the call's first line, not the line naming it | red |
| k12 | `tests/` read as shipped | red |
| k13 | no coordinate fragment flagged | red |
| k14 | no heading spelling flagged | red |
| k15 | a docstring and a whole-line comment read as code | red |
| k16 | the floor read as 3.12 | red |
| k17 | a tree with no `ruff.toml` read | red |
| k18 | `judge` returns nothing | red |
| k19 | a file no floor pattern names judged | red |
| k20 | `census_case` judges nothing, with `tests/test_conftest.py` | red |
| k21 | a record read for the sign | red |
| k22 | no line flagged for the sign | red |
| k23 | an image read for identifiers | SURVIVED, then red after cb7eba8e |
| k24 | a flagged identifier line dropped | red |
| k25 | a file that is not UTF-8 text read | red |
| k26 | an exemption with no reason read as one | red |

k4 and k23 survived the first run: no case quoted the exemption's form inside a comment, and no case put an image in front of `real_identifiers`. cb7eba8e added both cases and both mutations are red against it. `git status` was clean after every run.

**The cost** (`executed`, macOS arm64, `-p no:xdist`). Before, at b247a92c in an archive of that commit: the old census modules and the cases this phase moved run 166 cases in 3.67 s, and 10 of them each built a fixture repository with git. After, at ef753db7: `tests/test_censuses.py`, the floor case that stays and the four `test_census` cases run 174 cases in 2.59 s. No case builds a repository. The one git call is the sweep's listing of the tracked files. `.test_durations` still prices the removed ids at about 12 Windows seconds; phase 7 prunes them.

**What the layout check prints** (`executed`, at ef753db7). `bin/test-layout --check` ends `test-layout: 145 files read, 0 refused, 141 declare no TARGET`. `bin/test-layout --pairs` printed four pairs after the move: three in `tests/test_censuses.py` and one in `tests/test_conftest.py`. The three were cases with one body and two inputs, now parametrized. The fourth was two cases passing one path to `census_case` over two different files, and the refusing case now names another path. It prints 0 pairs.

**The phase boundary** (`executed`). The prompt asks this phase's boundary to reach every module, because `tests/conftest.py` changed and every module imports it. Running all 145 modules is the full suite, which contract rule 2 leaves to the orchestrator, so the boundary ran the modules this phase can reach, named in the hand-back: 81 modules. They are phase 1's 69, every test module this phase edited, every module that imports `censuses` or calls `census_case`, the 23 modules that read the text of a script this phase changed, the 4 that read a shipped script's source through `inspect` or a content hash, `tests/test_console_is_not_utf8.py` and the release table's module. At 197bc2a0: 4,557 passed, 11 skipped and 3 failed. Two failures were this phase's. `test_no_instructing_document_leaves_an_instance_anonymous` refused an exemption's wording, and `test_each_home_states_its_rule_under_its_section` refused a reworded House rules sentence. ec216773 fixed both, and the two modules pass. The third is the overview census, as at phases 1 and 2. `bin/rules --check`, `bin/unverified-check seal/specs/` and `chain_check.py --baseline release/v0.22.3 --worktree` each exit 0 at ec216773.
