# Phase 3: 1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home

## What this phase found

**The frame holds for this phase, with one premise that does not.** Each coordinate `frame/design.md` G15 to G17 gives was opened at `17968a565` and stood as the frame read it at `15636c7f0`: the thirteen entry points that import `lib/sibling.py` at import and spell the loop, the loops of `chain_check.py` and `pr_body.py` before their loads, the census's one accepted call form, the copies of `under`, `inside`, `plural` and `declared_branch`, and the three readers of `skills:`. `seal/follow-up.md` holds no row. Judged against `skills/implement/SKILL.md` *1. Read the documents that outrank the code first*.

The premise that does not hold is the one `frame/plan.md` A7 rejects the kept loops on: "the load of `console.py` adds no new way to fail before the answer". It held for ten of the thirteen. `fold_check.py`, `pact_check.py` and `payload_meter.py` imported `lib/sibling.py` at import and loaded every module through it later, inside functions, so `lib/console.py` is the first module each loads at import. And `lib/console.py` imported `lib/gitcmd.py` by its plain name at its top. A script that loaded `gitcmd.py` lazily now met an absent `gitcmd.py` as a `ModuleNotFoundError` traceback out of `console.py`, where it had met `lib/sibling.py`'s sentence at exit 2. `tests/skills/test_broad_gate.py#Test_main.test_refuses_a_copy_without_the_git_helper_in_a_sentence` holds exactly that. Its copy held `lib/sibling.py` alone, so after `208f1a75f` it failed on the sentence naming `console.py`; with `console.py` added to the copy it failed on the traceback. The build kept the frame's approach and removed the new way to fail (below).

**Decisions settled while writing the code.** Each was judged against `frame/design.md` *Scope* and *Data & interfaces*, which name the homes and leave the rest to the build.

- Each entry point binds `console = sibling.load("lib/console.py")` beside its other module-level loads, or alone after its guarded `import sibling` where it had none. `unverified_check.py` held the module as `CONSOLE`; it is now `console`, because the census reads the call only on the name `console`.
- `lib/console.py` imports `lib/gitcmd.py` inside `annotate`, where `git_path` is read, and not at its top. A load of `console.py` then reads nothing beside the standard library, so every entry point that loads it before `gitcmd.py` meets an absent `gitcmd.py` in the loader's sentence. The docstring says so. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*: the structure that made the new failure is the one to change, rather than ordering each script's loads around it.
- `lib/gitcmd.py#inside(path, top)` takes both paths absolute from the directory the process runs in before `commonpath`. `seal.py#display` and `seal.py#export` hand it a path that may be relative, as `seal.py#inside` read it. `settle.py` and `broad_gate.py` resolve both paths first, as the frame says.
- `broad_gate.py#copy_origin` and `#gate_copy` keep the `root is None` answer `broad_gate.py#under` gave, at each call.
- `settle.py#EARLIER_OLDER` takes one field, `{commits}`, filled by `console.plural(older, "older commit")`, where it took `{count}` and `{s}`. The `directory` line passes `'directory', 'directories'`. Every line prints as before; the cases `frame/design.md` S12 names pass.
- The note of `seal.py#plural` on why `check()` prints `1 work items` moved to a comment over that `print`, since it is about that line.
- `settle.py#released_local` reads the work item's `routing.md` through `routing.read_declaration(gitcmd.under_root(...))` inline, with a comment for what the old docstring said.
- `noninferiority.py` loads `payload_meter.py` at import, beside `gitcmd.py` and `console.py`. A definition with no `name:` stops the run with `<file> declares no \`name:\` in its frontmatter`, which also covers a file with no frontmatter, since `frontmatter` reads none there.

**Departures from the frame.**

- `tests/skills/test_seal.py#Test_plural`, `#Test_inside` and `tests/skills/test_broad_gate.py#Test_under` go with the units they held. `frame/design.md` *Removes* does not name them. The new `Test_plural` of `tests/lib/test_console.py` and `Test_inside` of `tests/lib/test_gitcmd.py` cover what each held: one and other counts, the sibling sharing a prefix, a parent, and two drives. `broad_gate.py`'s `None` root is held by `Test_copy_origin.test_refuses_to_call_a_copy_elsewhere_the_trees`. Judged against `CONTRIBUTING.md` *A module's old cases get one verdict each when the module is rebuilt*: the behaviour each guarded left its module.
- Three cases outside the frame's list changed their fixtures, each because an entry point now loads `console.py` at import. `test_refuses_a_copy_without_the_git_helper_in_a_sentence` copies `console.py` into its plugin (`1046512dc`). `tests/skills/test_payload_meter.py#Test_module.test_a_copy_without_the_scan_exits_2_on_a_run_that_reads_a_claude_md` does too (`38722d184`). `tests/skills/test_pact_check.py#Test_module.test_accepts_the_map_named_in_posix_form_under_windows_joins` loaded the script under `ntpath.join`, and the loader then joined a path to `console.py` no POSIX disk holds and raised `Absent`. It now joins a path that starts at the disk's root with this platform's join and every other path with Windows' (`4d5f85094`). Mutant k1 below shows it still watches the map's spelling.
- `tests/text/test_every_agent_reads_the_contract.py` gains `test_the_preloaded_set_holds_the_skills_the_lists_name` (`6364b6e13`). Mutant t2 below, a `preloaded()` that read no `skills:` list, survived the whole file: the check-line case ran over the definitions alone and passed. That gap stood before this phase too, with the old reader.
- `frame/plan.md` row 3 names `tests/test_censuses.py` to prove *Scope* item 9. That file holds the census's own cases and does not run it over the tree. A probe removed `console.to_utf8()` from `fold_check.py`: `tests/test_censuses.py` passed against it, and `tests/skills/test_fold_check.py::test_census` with `tests/behaviour/test_every_tracked_file_meets_every_census.py` went red on the `entry_point` line. The census over the tree is what holds S10's answer.

**Seen red.** The new cases of `plural`, `inside` and `read_declaration` were run before their code, against the tree at `208f1a75f` with only the cases added: all ten failed with `AttributeError`, the function absent. S13's case and the rewritten refusal case of `noninferiority.py` were run against the tree at `38722d184` with only the cases changed: the flow form read no skill on both line ends, `['agents/proofer.md']`, and the refusal case failed on its sentence and on `DID NOT RAISE` for a frontmatter with no `name:`. These trees hold the same text of each unit as `15636c7f0`, which the plan row names: `lib/gitcmd.py` and `lib/routing.py` hash the same at both, `lib/console.py` differed only in its docstring and held no `plural`, and `noninferiority.py#preload_files` hashes the same.

**Mutation runs.** Each ran after its commit through `bin/seal mutate`. Several first ran as one call of several mutants of one file, whose output names no case, and s1 to s4 and e1 to e2 first ran under xdist, where `-x` ends a run at exit 2, which `seal mutate` also reads as red. So each mutant below was run again alone with `-x -p no:xdist`, and the table names the case its run failed on, read for the guard named. Every verdict is `red` unless it says otherwise.

| Run | Unit and break | Case that went red |
|---|---|---|
| c1 | `plural`: one read as `<= 1` | `Test_plural.test_accepts_one_as_the_word_and_any_other_count_as_its_plural[0-issue-None-0 issues]` |
| c2 | `plural`: MANY ignored | `test_refuses_to_add_an_s_to_a_plural_it_was_given`, on `'2 directors' == '2 directories'` |
| c3 | `plural`: no `s` added | the same accepting case, row `2 files` |
| g1 | `inside`: the paths not taken absolute | `test_accepts_the_top_itself_and_a_path_under_it`, on the relative path |
| g2 | `inside`: `startswith` for `commonpath` | `test_refuses_a_sibling_sharing_its_prefix_a_parent_and_two_drives` |
| g3 | `inside`: two drives answered True | the same case |
| r1 | `read_declaration`: `UnicodeDecodeError` not caught | `Test_read_declaration.test_refuses_an_absent_file_and_one_that_cannot_be_decoded` |
| r2 | `declarations`: the file not read | `Test_declarations.test_accepts_a_declaration_under_the_repositorys_root` |
| i1 | `console.py`: `gitcmd` imported at its top again | `test_refuses_a_copy_without_the_git_helper_in_a_sentence`, on the traceback |
| s1 | `settle.py#released_local`: `review` read for `branch` | `Test_main.test_local_mode_lists_a_released_and_an_unreleased_item` |
| s2 | `settle.py`: `directories` not given | `Test_apply.test_accepts_every_released_directory_with_no_open_row` |
| s3 | `settle.py`: `older commits` for `older commit` | `Test_main.test_reads_the_plans_of_the_two_newest_removing_commits_and_names_the_rest` |
| s4 | `settle.py#named_directory`: `inside`'s arguments swapped | `Test_main.test_refuses_a_git_that_did_not_answer_in_one_line[from]`: `--from` was refused before git was asked |
| e1 | `seal.py#display`: `inside`'s arguments swapped | `Test_display.test_accepts_a_path_inside_as_slash_joined_and_relative` |
| e2 | `seal.py#export`: `inside`'s arguments swapped | `Test_export.test_accepts_an_output_and_notes_one_inside_the_tree` |
| b1 | `broad_gate.py#copy_origin`: the origin always `plugin` | `Test_copy_origin.test_accepts_a_copy_under_the_root_as_the_trees` |
| b2 | `broad_gate.py#gate_copy`: the negation of `inside` dropped | `Test_gate_copy.test_accepts_a_tree_copy_whose_bytes_differ_from_the_invoked` |
| p1, p2 | `release_seal.py#release_rows`: `rounds`, `issues` for the singular | `Test_release_rows.test_accepts_the_fixed_set_of_rows_in_order_and_fits_the_panel` |
| p3 | `publish_release_note.py`: `pull requests` for the singular | `Test_main.test_the_theme_follows_the_notes_header` |
| f1 | `fold_check.py`: `documents` for the singular | `Test_main.test_a_document_past_the_ceiling_is_named_and_the_run_exits_0` |
| n1 | `preload_files`: the `name:` stop taken out | `Test_preload_files.test_refuses_a_definition_that_declares_no_name[no frontmatter]` |
| n2 | `preload_files`: the list read as empty | `Test_preload_files.test_accepts_a_definition_and_every_skill_it_lists[one skill]` |
| t1 | the contract case: `shape_problems` given `PRELOADS` | `test_a_second_preload_is_caught` |
| t2 | the contract case: `preloaded()` given no skills | none: SURVIVED the whole file at `cfd0e1648` |
| t2b | the same break, after `6364b6e13` | `test_the_preloaded_set_holds_the_skills_the_lists_name` |
| k1 | `pact_check.py#MAP_SHOWN` built from `MAP` | `test_accepts_the_map_named_in_posix_form_under_windows_joins`, on `~/.claude\agentic\pact-paths.json` |

The first calls of b1 and b2 swapped `inside`'s arguments at both call sites, and were red; that text stands twice in the file, so the runs alone break each site another way.

**What moved and adds no behaviour.** *Scope* item 9 moves the stream answer from a loop to a call, and `seal.py#under` and `settle.py#under` are `gitcmd.under_root` renamed. The existing cases prove them: each entry point's `test_census` and `tests/behaviour/test_every_tracked_file_meets_every_census.py` read the call, and the S12 cases read every line `under_root` builds a path for. The census of the old spellings is the design's searches, run at `4d5f85094`; at `17968a565` each found its target.

- S10: `git grep -l "[.]reconfigure(" -- '*.py' ':!tests' ':!evals/behaviour'` printed the twelve files S10 lists, and no other. `git grep -n "[.]reconfigure(" -- tests/run_tests.py` printed nothing.
- S11: the definitions search printed `lib/console.py:131`, `lib/gitcmd.py:107`, `skills/code-review/scripts/chain_check.py:968` and `skills/verify/scripts/session_cost.py:2006`, the last two out by *Scope*. At `17968a565` it found 13 definitions in 8 files.
- S13: `git grep -n -F '^skills:' -- '*.py'` printed `payload_meter.py:168` and `:176` alone. At `17968a565` it also printed `noninferiority.py:98` and two lines of `test_every_agent_reads_the_contract.py`.
- `git grep -n -e listed_skills -e declared_branch -e 'has no frontmatter'` over the tree, `seal/threads` left out, printed nothing.

**The boundary run.** The set is the plan row's twenty files, every test file this phase changed, every test file under `tests/` that names a changed module's file, `tests/lib/test_sibling.py`, which copies scripts alone, and `tests/text` and `tests/behaviour`: 46 arguments to one `bin/test -q` command. A check after the run, `git grep -l -F` over the base names of the eighteen modules this phase changed outside `tests/`, found one test file the set had missed, `tests/e2e/teammate/test_teammate_flow.py`; it and `tests/test_run_tests.py` passed at `4d5f85094` in one more command, 64 passed. Its first run, at `6364b6e13`, failed one case, the Windows-joins case of `pact_check` above. At `4d5f85094` the same command passed: 5266 passed, 10 skipped, and 5 warnings, each a `UserWarning` from `tests/behaviour/test_a_cited_section_stands_in_its_file.py` about another work item's pending rule change. `bin/seal layout --pairs tests` names no pair among this phase's new cases, and `bin/seal layout --check tests` refuses no file.

**For the next phase.** `tests/run_tests.py` now loads `lib/console.py` at import, after `lib/launch.py`, and its `__main__` block opens with `console.to_utf8()`; *Scope* item 12 rewrites the same file. The changelog entry *Scope* item 13 asks for the reading of *Scope* item 11 also changes the sentence a definition with no `name:` stops the run with.
