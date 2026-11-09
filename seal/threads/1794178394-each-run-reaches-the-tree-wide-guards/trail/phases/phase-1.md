# Phase 1: 1794178394-each-run-reaches-the-tree-wide-guards

## What this phase found

**The frame holds for this phase, with one sentence of *Scope* item 2
deferred to phase 2.** Every coordinate the phase 1 row stands on was where
the frame says at `288e3db5`. The *Grounding* row on tree-wide cases in
`TARGET` files was a sample, as it says, and the enumeration below found
five tree-wide cases it did not list.

### The enumeration (`frame/questions.md` Q1)

The method takes the artefact apart into its parts. Each case of each of
the 52 test files that declare `TARGET` at `288e3db5` was read by an `ast`
script under the scratchpad. The script followed each case through the
module-level helpers, constants and fixtures it reaches, and listed the
ways it can name this repository's root:

- `ROOT` passed whole, as an argument, a keyword or an argv item.
- `ROOT` joined to a directory rather than to a file.
- A walk: `os.walk`, `listdir`, `scandir`, `glob`, `rglob`, `iterdir` or
  `rules.markers`, with `ast.walk` left out.
- A git listing (`ls-files`, `git_listing`), or a conftest walker
  (`rule_carriers`, `imported_roots`, `review_chain_text`).
- A helper whose root parameter defaults to `ROOT`.

`CONTRIBUTING.md` *The test layout* makes `ROOT` from `tests/conftest.py`
the one way a test file names the root. Every case the script flagged was
then read by hand. So was every case that takes no temporary directory and
runs a command, 174 of them: such a case reads either strings it builds or
the real tree. The five shipped commands whose `--root` defaults to the
tree were checked for a call without `--root`, and the one such call is
the payload meter's case below. What this method cannot rule out is a case
that takes a temporary directory and still reaches the tree through a
command's default root without naming `ROOT`. `gaps.md` *Not verified*
carries that row.

Fourteen cases moved, thirteen tree-wide and one that tests a moved helper.
Each body is unchanged. Each new class or file is named for the rule its
cases hold, as Q1's default asks.

| Old place | New place |
|---|---|
| `tests/github/test_rules.py::Test_main::test_every_check_line_in_the_tree_holds` | `tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_seal_rules::test_every_check_line_in_the_tree_holds` |
| `tests/skills/test_test_layout.py::Test_main::test_accepts_this_repositorys_tests` | `tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_seal_layout::test_accepts_this_repositorys_tests` |
| `tests/skills/test_fold_check.py::Test_main::test_accepts_this_repository_with_no_flags` (not in the frame's list) | `tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_seal_fold::test_accepts_this_repository_with_no_flags` |
| `tests/skills/test_unverified_check.py::Test_module::test_this_repositorys_own_overviews_are_all_readable` (not in the frame's list) | `tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_seal_unverified::test_this_repositorys_own_overviews_are_all_readable` |
| `tests/lib/test_routing.py::Test_parse::test_every_declaration_in_this_repository_still_parses` | `tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_routing_declarations::test_every_declaration_in_this_repository_still_parses` |
| `tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census` | `tests/behaviour/test_every_tracked_file_meets_every_census.py::test_every_file_no_module_file_declares_meets_every_census` |
| `tests/test_conftest.py::Test_module::test_no_test_file_derives_the_root_from_its_own_path` | `tests/behaviour/test_a_test_file_takes_the_root_from_the_conftest.py::test_no_test_file_derives_the_root_from_its_own_path` |
| `tests/test_conftest.py::Test_module::test_no_two_python_files_under_tests_share_a_name` | `tests/behaviour/test_a_test_file_takes_the_root_from_the_conftest.py::test_no_two_python_files_under_tests_share_a_name` |
| `tests/lib/test_launch.py::Test_module::test_the_floor_has_one_source` | `tests/behaviour/test_every_entry_point_runs_at_the_floor.py::test_the_floor_has_one_source` |
| `tests/lib/test_launch.py::Test_module::test_what_runs_before_any_floor_is_linted_at_the_floor` | `tests/behaviour/test_every_entry_point_runs_at_the_floor.py::test_what_runs_before_any_floor_is_linted_at_the_floor` |
| `tests/lib/test_launch.py::Test_module::test_every_wrapper_runs_its_script_through_the_launcher` (not in the frame's list) | `tests/behaviour/test_every_entry_point_runs_at_the_floor.py::test_every_wrapper_runs_its_script_through_the_launcher` |
| `tests/lib/test_launch.py::Test_module::test_a_script_reaches_the_modules_under_lib` (not tree-wide; tests the moved helper `loaded_by`) | `tests/behaviour/test_every_entry_point_runs_at_the_floor.py::test_a_script_reaches_the_modules_under_lib` |
| `tests/github/test_release_report.py::Test_module::test_the_table_reads_this_tree_against_the_last_tag` (not in the frame's list) | `tests/behaviour/test_every_shipped_agent_and_document_is_measured.py::Test_release_report::test_the_table_reads_this_tree_against_the_last_tag` |
| `tests/skills/test_payload_meter.py::Test_module::test_the_real_tree_runs_and_names_every_shipped_agent` (not in the frame's list) | `tests/behaviour/test_every_shipped_agent_and_document_is_measured.py::Test_payload_meter::test_the_real_tree_runs_and_names_every_shipped_agent` |

The helpers only moved cases read moved with them. They are
`POLICY_DOCUMENTS`, `declared`, `_LAYOUT` and `layout` of the census file,
`python_files`, `own_path_directories`, `shared_names`, and the floor
derivation of `tests/lib/test_launch.py`: `BIN`, `RUNNER`, `RUFF`,
`floor_carriers`, `INTERPRETERS`, `launches`, `RUNS_ITS_RUNNER_DIRECTLY`,
`HOOKS`, `PLUGIN_ROOT`, `ASSIGNED`, `VARIABLE`, `BARE_SCRIPT`,
`handed_first`, `loaded_by`, `hooked` and `before_any_floor`. The helpers a
case that stays also reads are imported from the old file, which keeps
them. That is the form fifteen files under `tests/behaviour/` already use,
`from test_rules import rules` among them. It also keeps five scripts from
loading when `tests/conftest.py` is imported. `CONTRIBUTING.md` *The test
layout* says "A helper two test files use is defined once, in
`tests/conftest.py`", and those fifteen files stood against that sentence
before this phase. `test_a_script_reaches_the_modules_under_lib` is not
tree-wide. It moved because `loaded_by`, the helper it tests, moved, and a
case left behind would import its own subject from another test file. The
frame's `## Removes` names neither that case nor the class
`tests/github/test_release_report.py::Test_module`, which phase 1 removed
because the move left it empty.

None of the fourteen sits in
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`,
the file #1444 works in.

### The pair the move left empty

`bin/seal layout --check tests/skills/test_fold_check.py` refused the file
after the move: `class Test_main has no test_accepts_ case` (executed, exit
1). Q1 allows keeping a remaining case of the same kind. So
`Test_main::test_an_index_naming_each_document_once_passes`, a case that
accepts a fixture tree at exit 0, is renamed
`test_accepts_an_index_naming_each_document_once`, body unchanged. No case
was written new, so contract rule 15 asks no red. The other classes a case
left keep their pairs. `Test_main` of `tests/skills/test_test_layout.py`
keeps `test_accepts_a_pair_and_exits_zero`, `Test_main` of
`tests/github/test_rules.py` keeps `test_accepts_a_check_line_in_grammar`,
and `Test_parse` of `tests/lib/test_routing.py` keeps six accepting cases.

### *Scope* item 2, and the sentence deferred

`CONTRIBUTING.md` *The test layout*, the paragraph that opens **A test file
that declares no `TARGET` stands by what its cases run.**, gains the two
sentences. The second stops at "are this repository's tree-wide files". The
frame's clause after it says that `skills/verify/SKILL.md` *Scope: cheap and
often, broad and once* runs those files at every phase boundary and every
fix pass. At this phase's commits that table still gives the glob clause and
"what the fix touches". The clause would be a statement HEAD contradicts, so
it waits for phase 2. Phase 2 adds it in the commit that rewrites the two
rows. The ground is `agents/crafter.md` *Before you hand back, your range
and the work item's records are read whole against HEAD*.

### The citations the move changed

Each statement that named a moved case's old place now names its new one.

- `CONTRIBUTING.md`: the `check:` line under **A test file takes the
  repository root from `tests/conftest.py`.**, which named
  `tests/test_conftest.py`, whose remaining cases hold none of that
  paragraph. Also the floor paragraph of *Running the checks*, which named
  `tests/lib/test_launch.py` as what derives the set.
- `.github/workflows/hygiene.yml`, the comment above the step that prints
  the `check:` lines `rules.py` did not read.
- `lib/launch.py`'s docstring, `ruff.toml`'s comment, and two comments of
  `tests/censuses.py`.
- The docstrings of `tests/github/test_rules.py`, `tests/test_censuses.py`,
  `tests/lib/test_launch.py` and
  `tests/behaviour/test_chain_hooks_hardening.py#test_the_plugin_registers_two_hooks_and_writes_none_into_git`.
- Three keys of `APPLIES_THE_SHARED_GUARD` in
  `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`.

`docs/running/what-a-script-gates.md`, the row of `seal rules --check`, says
the check runs "through `tests/github/test_rules.py`". The case that runs it
over the tree now stands in
`tests/behaviour/test_this_repository_passes_its_own_checks.py`. That file
is in the policy root, which this work item's design changes only through
`## Rule changes`, so the hand-back names it for the orchestrator. Mentions
in other work items' records under `seal/threads/` state the commits those
records name and stand. The search was `git grep` on each moved case's name,
on each moved helper's name and on each old file's path. It is a sample of
the statements across the tree, and a statement that names a moved case by
describing it, without its name or its file, is the part it did not reach.

### The proof of the move (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*, the rename-or-move row)

All of the following were executed.

- `bin/seal layout --moved 288e3db5 --from <the ten old files> --to <the ten
  old files> <the five new files>` exited 0. Its last line: `seal layout:
  moved: 432 old cases, 877 items against 877 at 288e3db561a1, 0 failed`.
  The ten old files are `tests/github/test_rules.py`,
  `tests/skills/test_test_layout.py`, `tests/skills/test_fold_check.py`,
  `tests/lib/test_routing.py`, `tests/skills/test_unverified_check.py`,
  `tests/test_censuses.py`, `tests/test_conftest.py`,
  `tests/lib/test_launch.py`, `tests/github/test_release_report.py` and
  `tests/skills/test_payload_meter.py`. The run covers the renamed fold case.
- `bin/seal layout --check` exited 0: `seal layout: 139 files read, 0
  refused, 87 declare no TARGET`.
- `bin/test` over the five new files: 14 passed, exit 0.
- `git grep -l -F <name>` for each moved case's name, outside
  `seal/threads/` and `.test_durations`, finds it only in its new file. One
  name also appears in `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`,
  as its new coordinate. The renamed fold case's old name is found nowhere.
- `uvx ruff check` and `uvx ruff format --check` over the changed Python
  files exited 0.

The phase adds no behaviour, so it owes no case written new and no
`seal mutate` run.

### The phase boundary

The frame has this phase run the set *Scope* item 3 describes for its own
paths. Its parts:

1. The cases the plan row names: the fourteen, in the five new files.
2. The test files the phase changed: the ten old files and the files under
   `tests/behaviour/`.
3. The test files that read a changed path that is not a test file. Here
   phase 1 judged "names a changed path in full" as reading it.
   `tests/skills/test_broad_gate.py` reads `.github/workflows/hygiene.yml`
   under `ROOT`. `tests/skills/test_passages.py` lists `CONTRIBUTING.md`
   and costs 0.1 s, so it went in. `tests/skills/test_seal.py`,
   `tests/skills/test_chain_check.py` and the other files that write
   `CONTRIBUTING.md` or `.github/workflows/hygiene.yml` only into a
   fixture or a docstring were left out. `ruff.toml` and `lib/launch.py`
   are read only by files already in the set.
   `tests/censuses.py` changed in two comments, and every run imports it,
   which is what such a change can break (`skills/verify/SKILL.md` *The
   narrow command still has to be able to fail*, the comment row).
4. `tests/text/` and `tests/behaviour/`.

The command was `bin/test tests/text tests/behaviour
tests/github/test_rules.py tests/skills/test_test_layout.py
tests/skills/test_fold_check.py tests/lib/test_routing.py
tests/skills/test_unverified_check.py tests/test_censuses.py
tests/test_conftest.py tests/lib/test_launch.py
tests/github/test_release_report.py tests/skills/test_payload_meter.py
tests/skills/test_broad_gate.py tests/skills/test_passages.py -q`.

Its first run, at `35e9f7d2` without this record, exited 1 after 54 s:
2 failed, 3,026 passed, 10 skipped. One failure was
`tests/behaviour/test_docs_line_wrap.py`, on a 111-column line the phase
wrote into `CONTRIBUTING.md`. `f40ab296` wraps it. The other was
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
because `gaps.md` did not yet exist. This record writes it.

The second run, at `f40ab296` with this record, `gaps.md` and the Status
cell on disk, ran 99 test files. It exited 0 in 22 s of wall clock: 3,028
passed, 10 skipped (executed).

### What phase 2 needs

- The tree-wide files are `tests/text/` and `tests/behaviour/`, now with
  the five new files above. No case in a file that declares `TARGET` reads
  the tree by the enumeration's method.
- The clause *Scope* item 2 deferred, for the paragraph above, in the
  commit that rewrites the `Phase boundary` and `Review rounds 1..n` rows.
- Part 3 of the set needed a judgment that a text search does not make. A
  file that writes a changed path into a fixture names it in full without
  reading it, and `tests/skills/test_chain_check.py` (408.1 s stored) is
  one. The new row's third part has to say whether "names" means reading
  the file or writing its name.
- The fourteen cases carry 36.3 s of stored price in `.test_durations`
  under their old ids, against the frame's estimate of about 34 s.
