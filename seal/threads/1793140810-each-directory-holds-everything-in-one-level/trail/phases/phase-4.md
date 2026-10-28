# Phase 4: 1793140810-each-directory-holds-everything-in-one-level

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 011adcb2 |

## What this phase was asked

Build `frame/plan.md` row 4 and nothing of phase 5:

- the 91 test files that declare no `TARGET` move by `git mv` into
  `tests/behaviour/` and `tests/text/`, by the criterion in
  `frame/design.md` *Data & interfaces*;
- each moved file imports `ROOT` from `tests/conftest.py`;
- the rider of `hooks/lib/cmdline_base.py`, the census constants, and every
  `check:` line and citation of a moved file name the new path;
- `CONTRIBUTING.md` *The test layout* states that a test file takes its root
  from `conftest.ROOT`;
- every reader that lists `tests/` one level deep reaches the new
  directories.

A moved file owes no new case, no red run and no `seal mutate`. Two cases
are new in `tests/test_conftest.py`, and each is seen red once. The moved
files are collected before and after the move, and the node ids are
compared as file name plus the rest of the id. The phase ends with one
`bin/test` command and with the tree's `bin/seal layout --check` and
`bin/seal rules --check` exiting 0.

## What this phase found

**Nine files sit on the criterion's edge, and they went to `behaviour`.**
The pattern in `frame/design.md` *Data & interfaces* sends 43 files to
`behaviour` and 48 to `text`, the same sets the design lists. The design
also says that a file the pattern sends to `text` goes to `behaviour` where
its cases run shipped code through a helper the pattern does not name. Nine
files do that, each through a helper imported from a module test file:

- `test_a_body_naming_two_issues_claims_one.py`, through
  `tests/github/test_issue_claims_check.py#read`;
- `test_a_declared_label_reaches_the_tracker.py`, through `labels_module`;
- `test_a_release_publishes_its_note.py`, through `module`;
- `test_a_release_rolls_the_flow_measurement_issue.py`, through `_roller`;
- `test_a_rewritten_definition_proved_non_inferior.py`, through
  `truth_regex`, which calls `noninferiority.grader_from`;
- `test_a_unit_is_bounded_where_a_parser_decides.py`, through `places`;
- `test_settle_applies_rule_changes_in_place.py`, through `parse` and
  `rules`;
- `test_the_rules_command_reads_each_rule_off_its_test.py`, through `rules`;
- `test_waiver_decided_at_start.py`, which inserts `hooks/lib` on
  `sys.path` and imports `routing`.

So `tests/behaviour/` holds 52 files and `tests/text/` holds 39.

**The collection, before and after.** `bin/test <the 91 files>
--collect-only -q` collected 1956 node ids at `68c87bb2`. After the move and
the root edits, `bin/test tests/behaviour tests/text --collect-only -q`
collected 1956. Compared as file name plus the rest of the id, the two sets
are the same, with no id added or lost (executed).

**What "computes the root from `__file__`" reads as.** The new case flags a
`__file__` name inside a `dirname` call, or under a `.parent` or `.parents`
of a path built from it. A `__file__` inside a fixture's source string is no
name, and a loaded module's `module.__file__` is an attribute, so the uses
phase 3 named pass. A file that names itself also passes:
`os.path.basename(__file__)` in
`test_a_document_that_names_a_script_says_how_to_reach_it.py`,
`test_a_release_is_sized_by_a_criterion.py`,
`test_the_release_check_watches_what_ships.py` and
`test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, and
`read(os.path.abspath(__file__))` in
`test_a_release_cannot_ship_an_untrue_milestone.py`.

**The root case reads test files, not every file under `tests/`.** The plan
row says "no file under `tests/` but `conftest.py`". `tests/censuses.py`
computes its own `ROOT` from `__file__`, and its docstring says why it
imports nothing from `tests/conftest.py`: `evals/scripts/noninferiority.py`
loads it by path, without pytest. So the case reads the files named
`test_*.py`, which is the scope `CONTRIBUTING.md` states the rule for. The
case also refused three files the move does not touch, and each now imports
`ROOT`: `tests/test_conftest.py`, `tests/test_censuses.py` and
`tests/e2e/creation/test_creation_flow.py`, whose `HOOKS` climbed
`parents[3]`.

**The name case reads Python files only.** The design's scenario says "no
two files under `tests/` have the same file name". The case reads every
`.py` file under `tests/` on disk, `__pycache__` left out. Only Python files
are imported by name, and a file such as a `.DS_Store` stands in more than
one directory of a macOS checkout.

**Both cases stand in `Test_module`.** They were written first as
`Test_ROOT` and `Test_test_directories_on_the_path`. The tree's
`bin/seal layout --check` refused both, with "class Test_ROOT names no
top-level definition of tests/conftest.py", because `ROOT` is an assignment
and the walk on `sys.path` is module code (executed). What the module does
as a whole goes in `Test_module`, so both cases moved there.

**Readers that list `tests/` or join a test file's own directory
(contract rule 12).** The searches for `tests/*.py`, `glob("test_*`,
`iterdir`, `listdir`, `os.walk` and `"tests"` joins found these, and each
now reaches the new directories:

- `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py` joined
  `block_shapes.py` under its own directory, which after the move is
  `tests/behaviour/`. It joins it under `ROOT` and `tests`.
- `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py#NEIGHBOUR`
  joined its neighbour under its own directory. It joins it under `ROOT`,
  `tests` and `behaviour`.
- `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`
  built its own module path as `tests/<name>`. It is
  `tests/behaviour/<name>`.

These needed no change: the walk in `tests/conftest.py` from phase 3,
`tests/test_censuses.py#Test_module` and the file-name sweep of
`tests/behaviour/test_one_word_one_meaning.py`, which walk the tree;
`git ls-files tests/*.py` in
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, whose `*`
crosses `/`; `ruff.toml`'s `"tests/*"`; `skills/settle/scripts/settle.py#TESTS`,
which is a prefix; and `skills/verify/scripts/test_layout.py`, which walks
`tests/`.

**Citations.** After the `git mv`, `censuses.vacated_paths` over every
tracked file found 355 lines in 131 files, and `censuses.old_names` found 3
lines in `tests/behaviour/test_the_root_migrates_itself.py`, because
`tests/censuses.py#KEPT_FILES` still named its old path (executed, by a
probe). `test_censuses.py`'s sweep skips a file that a module file declares
as its `TARGET`, so the probe read every tracked file. Each spelling was
rewritten to the new path, `KEPT_FILES` among them, and the probe then
found none. No `<commit>:<path>` citation of a moved file exists. Three
citations wrapped across two lines, which the census cannot read, were
rewritten by hand: `hooks/lib/config.py:212`,
`tests/behaviour/test_a_commit_names_its_repository.py:11` and
`tests/skills/test_settle.py:1502`.

**The rider of `hooks/lib/cmdline_base.py`.** Lines 20 and 21 name
`tests/behaviour/test_the_frozen_reading_never_grows.py`. That case passed
after the edit, so the bytes below the rider did not change (executed).

**`CONTRIBUTING.md` *The test layout*** now holds two new paragraphs. The
first states that a test file imports `ROOT` from `tests/conftest.py` and
that no two Python files under `tests/` share a name, with
`check: tests/test_conftest.py`. The second states that a file declaring no
`TARGET` stands in `tests/behaviour/` or `tests/text/` by what its cases
run, with `check: none reader: the proofer at review`, because the design
says the criterion places files and gates nothing.

**New cases, each seen red:**

- `tests/test_conftest.py::Test_module::test_no_test_file_derives_the_root_from_its_own_path`.
  Before the move, at `68c87bb2` with only `tests/test_conftest.py` edited,
  it failed with 95 lines, all in the top-level test files but one,
  `tests/e2e/creation/test_creation_flow.py:47`.
  After the move to `Test_module` it was shown red once more, over a planted
  tree whose `text/test_x.py` assigns `ROOT` from `os.path.dirname(__file__)`.
- `tests/test_conftest.py::Test_module::test_no_two_python_files_under_tests_share_a_name`.
  It passed over the tree. Over a planted tree holding `hooks/test_x.py` and
  `text/test_x.py` it failed with
  `{'test_x.py': ['hooks/test_x.py', 'text/test_x.py']}`.

Each planted tree was a `test_tmp_*` probe that pointed the module's
`TESTS` at a `tmp_path`. Each probe was deleted after its run.

**Existing cases relied on.** One `bin/test` command ran
`tests/behaviour`, `tests/text`, `tests/test_conftest.py`,
`tests/test_censuses.py`, and 41 more files: every file under
`tests/hooks/`, `tests/skills/`, `tests/github/`, `tests/evals/` and
`tests/e2e/` whose text this phase changed, `tests/skills/test_test_layout.py`
and `tests/github/test_rules.py`. It passed 5906 cases and skipped 16
(executed). The tree's `bin/seal layout --check` exited 0 ("158 files read,
0 refused, 91 declare no TARGET"), and `bin/seal rules --check` exited 0
("all 265 check lines in 63 rule files hold"). `ls tests` lists the six
files and two test files *Scope* keeps, `e2e`, the six area directories
and the untracked `__pycache__`.

**A citation that names no file, left as it stands.**
`tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py:38` names
`tests/test_the_lenient_run_says_what_the_broad_gate_will_say.py`, which
`5b1f6fae` (#950) deleted (executed: `git log --diff-filter=D`). It is no
file this work moved.
