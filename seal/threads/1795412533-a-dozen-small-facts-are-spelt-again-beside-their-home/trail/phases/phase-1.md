# Phase 1: 1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home

## What this phase found

**The frame holds for this phase.** Each coordinate `frame/design.md` G7, G8 and G9 gives was opened at `5f92a39e4` and stood where the frame read it at `15636c7f0`: the opt-out copies at `settle.py:2129`, `fold_check.py:250` and `seal.py:708-710`, the loop of `broad_gate.py#seal_home`, the `config.json` spellings at `fold_check.py:86`, `broad_gate.py:176` and `pact_check.py:156`, the second read at `fold_check.py:297-298`, the two normalisers, and the two policy-document patterns. `seal/follow-up.md` holds no row. Judged against `skills/implement/SKILL.md` *1. Read the documents that outrank the code first*.

**Decisions settled while writing the code.** Each was judged against `frame/design.md` *Data & interfaces*, which names the public units and leaves the rest to the build.

- The prefix normaliser is `lib/config.py#_prefix`, private, because only `reference_roots` and `declared_policy_root` call it. `reference_roots` takes off a leading `/` after it, as it did before; a comment there says why `policy_root` does not.
- The pattern `policy_group` matches is a module constant, `lib/config.py#POLICY_DOCUMENT`, with the comment that stood over the copy in `rule_changes.py`. S3's search finds it there.
- The sentences that said why the opt-out is a file and not a directory moved from the comment in `home_at` into the docstring of `opted_out`. The comment over `SCRATCH` now points at `opted_out()`.
- `fold_check.py#declared` keeps its inner `stated` for the ceiling key alone, and reads the policy root through `declared_policy_root`, raising `Unusable` on its refusal.
- `rule_changes.py` gains a `config()` getter and the constant `CONFIG_READER = "lib/config.py"`, the name `fold_check.py` and `broad_gate.py` give the same module. It was first committed as `CONFIG` in `fdf59518a`, and renamed in `5899118ce` so that it is not read as `lib/config.py#CONFIG`, the file name.
- `broad_gate.py#missing_row` and `#not_as_written` call `lib/config.py#config_path` through `sibling.load(CONFIG_READER)`, the loader every other read of that module in the gate uses.

**Departures from the frame.**

- `tests/skills/test_fold_check.py#test_a_row_written_twice_is_refused_and_nothing_is_checked` gains the row `Policy root`. No case held `seal fold`'s refusal of a doubled `Policy root` key, which `declared` now takes from `declared_policy_root`. The row passed against `5f92a39e4`, because it pins behaviour the rewrite keeps; mutation m9 below shows it watches the new read.
- `seal layout --check tests` refuses a class with no `test_refuses_` case. The first boundary run failed on it for `Test_policy_group` and `Test_marked_home`. `c694b7031` splits the `policy_group` cases into an accepting and a refusing case, and adds a refusal case to `Test_marked_home`.
- That refusal case first stood a foreign `README.md` in `<repo>/seal/`. Mutation m15 SURVIVED against it: with `seal/` foreign, `home_paths` answers `<repo>/agentic-seal/`, which does not exist, so `marked` was never asked. `e2e83cdf3` stands the foreign README at the local place, `<repo>/.git/seal/`, and m15b is red.
- Two texts outside the frame's list stated a removed name or an old reader, and were corrected: the docstring of `tests/skills/test_pact_check.py#test_no_line_formats_a_path_without_the_helper` named `CONFIG_FILE`, and the docstring of `tests/lib/test_config.py#Test_module.test_the_policy_root_row_reads_as_docs_unless_it_names_a_directory_inside` called `policy_root` the one reader every reader asks.

**Seen red.** The new cases of `opted_out`, `marked_home`, `declared_policy_root` and `policy_group` were run before the code was written, against the tree at `5f92a39e4` with only the cases added: each failed with `AttributeError`, its function absent. Each guard was then shown watched by `seal mutate` after the commit, one break per run. Every verdict below is `red` unless it says otherwise, and each failing line was read for the guard named.

| Run | Unit and break | Case that went red |
|---|---|---|
| m1 | `opted_out`: `bool(common) and` taken out | `Test_opted_out::test_refuses_an_empty_common_directory_wherever_the_process_stands` |
| m2 | `opted_out`: `isfile` read as `exists` | `Test_opted_out::test_accepts_the_file_under_the_common_directory` |
| m3 | `marked_home`: the opt-out read inside it | `Test_marked_home::test_accepts_the_marked_root_where_the_opt_out_stands` |
| m15 | `marked_home`: `and marked(found)` taken out | none: SURVIVED, against the first refusal case |
| m15b | the same break, after `e2e83cdf3` | `Test_marked_home::test_refuses_a_place_whose_readme_is_not_the_marker` |
| m4 | `declared_policy_root`: the refusal dropped beside `docs` | `Test_declared_policy_root::test_refuses_a_key_written_twice_beside_docs` |
| m5 | `declared_policy_root`: `_prefix` not called | `Test_declared_policy_root::test_accepts_the_value_normalised_with_no_refusal` |
| m6b | `policy_group`: `.` and `..` let through as a group | `test_refuses_every_other_path_as_none`, rows `docs/./a.md` and `docs/../a.md` |
| m7b | `policy_group`: POLICY read as a pattern | `test_refuses_every_other_path_as_none`, row `myxdocs/a.md` |
| m8b | `policy_group`: the top level answered None | `test_accepts_a_document_at_the_top_or_in_one_group`, rows `docs/a.md` and `my.docs/a.md` |
| m9 | `fold_check.py#declared`: the refusal of `declared_policy_root` dropped | `test_a_row_written_twice_is_refused_and_nothing_is_checked[Policy root]` |
| m10 | `fold_check.py#groups`: `""` taken as a group | three `Test_main` cases of `tests/skills/test_fold_check.py`, `test_a_group_the_index_names_is_read_and_no_other_directory_is` among them |
| m11 | `rule_changes.py#parse`: every path placed | eight rows of `Test_parse::test_refuses_a_block_that_does_not_match_whole_at_its_line` |
| m12 | `fold_check.py#located`: the opt-out branch never taken | `Test_main::test_an_opted_out_repository_is_told_it_opted_out` |
| m13 | `settle.py#_settled`: the opt-out branch never taken | `Test_main::test_an_opted_out_repository_is_told_which_state_it_is_in` |
| m14 | `seal.py#no_root`: the opt-out branch never taken | `Test_export::test_refuses_without_a_root_or_in_a_throwaway_clone`, `Test_no_root::test_refuses_a_directory_outside_git_and_a_throwaway_clone` |

m6, m7 and m8 ran first against the cases before `c694b7031` split them, and were red on the same rows; m6b, m7b and m8b are the runs against the cases as committed.

**What moved and adds no behaviour.** The opt-out sentences of `settle.py`, `fold_check.py` and `seal.py`, `broad_gate.py#seal_home`, and the readers of `config.json` in `fold_check.py`, `broad_gate.py` and `pact_check.py` print what they printed. The cases `frame/design.md` S16 names pass unchanged, and m12 to m14 show they watch the new call sites. The census of the old spellings is S1, S2 and S3, run at `5899118ce`:

- S1: `git grep -n 'SCRATCH)' -- '*.py' ':!tests'` printed `lib/optin.py:323` alone, and `git grep -n 'isdir(found)' -- '*.py' ':!tests'` printed `lib/optin.py:332` alone.
- S2: `git grep -n -e '"config.json"' -e '"Policy root"' -- '*.py' ':!tests'` printed `lib/config.py:52` and `lib/config.py:339`.
- S3: `git grep -n -F '[^/\\:]+\.md' -- '*.py' ':!tests'` printed `lib/config.py:346` alone.
- `git grep -n -e CONFIG_FILE -e one_deep` over the tree, `seal/threads` left out, printed nothing once the `test_pact_check.py` docstring was corrected.

**The boundary run.** The set is the plan row's eight files, every test file that names a changed path (32 files, listed by `git grep -l` over `tests/` for the eight changed modules' names), and `tests/text` and `tests/behaviour`, in one command through `bin/test`. Its first run failed two cases: the layout refusal above, and `tests/behaviour/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`, which wants this work item's `gaps.md`. After `c694b7031`, `e2e83cdf3`, `5899118ce` and `gaps.md`, the same command passed: 4671 passed, 10 skipped.

**For the next phase.** `lib/config.py` now holds `POLICY_DOCUMENT` and `_prefix` beside `declared_value`, where *Scope* item 6 puts `switch`. `rule_changes.py` loads `lib/config.py`, which it did not before.
