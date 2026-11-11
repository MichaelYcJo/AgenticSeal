# Phase 3: 1794390764-scripts-load-a-reader-from-its-sibling

## What this phase found

**The two items of the fold at `0f9354a3b` come first, each in a commit of
its own.** `tests/behaviour/test_every_entry_point_runs_at_the_floor.py#loaded_by`
now drops every path under `tests/`, and `ruff.toml` loses the eight lines
and the comment phase 2 added (commit `457394c19`). The new case
`test_a_script_reaches_no_module_under_tests` holds S9's second half. It
was red before the arm changed. A mutant that returns `found & tracked`
again turned it and
`test_what_runs_before_any_floor_is_linted_at_the_floor` red (executed:
`seal mutate`). `rules.py#sibling` and a new `release_report.py#module`
guard their lazy `import sibling` (commit `a5b69cd01`). `release_report.py`
had three `import sibling` sites, in `meter`, `floor` and `documents`, and
all of them now call `module`. Each script has a copied-alone case that
runs it with arguments that reach a load and pins exit 2 and the sentence.
Both cases were red before the guard. Four mutants went red, two in each
file: the sentence without its last period, and `SystemExit(1)` in place
of `SystemExit(2)` (executed). Judged against `frame/design.md` *Scope*
items 2 and 10 as the fold left them, and S4 and S9.

**The frame holds for the move, with one exception and one unit it does not
name.** Each unit that *Scope* items 5 to 8 list stood in
`unverified_check.py` at `0f9354a3b` (read). Each now stands where the item
says. `unverified_check.py` keeps `main`, the walk, the path helpers it
prints with and the three root states (*Scope* item 9).

**Exception: S8 says `seal layout --moved` passes, and it cannot.** The
check compares a moved case by its body and by the definitions of the
names the body reads. *Scope* item 10 moves each case "unchanged but for
the module they call", and that one change fails both conditions.
`bin/seal layout --moved a5b69cd01 --from` the old test file and the five
files that received cases, `--to` the eight files at HEAD, exits 1. It
reports 261 failures: 189 bodies not found unchanged, 71 cases whose names
are defined differently, and one count line, 688 items against 689
(executed). A probe was used in its place: `test_tmp_moved.py` in this
phase's scratch directory. It parses each case at `a5b69cd01` and at HEAD
and maps every module name (`UC`, `uc`, `chain`, `settle`, `console`,
`gitcmd`, `READER`, `GAPS`, `ITEMS`, `reader`, `rules`) to one name. It
then compares the trees. 453 cases are identical. Nine differ, and each
difference is a call this phase changed:

- the two `Test_rule_changes_reader` cases, which call the renamed getter;
- three `test_refuses_a_comment_line_at_its_line` cases of
  `test_chain_check.py`, which read `chain.FIELDS.COMMENT_LINE` where they
  read the re-export;
- `Test_rule_changes_read::test_refuses_to_run_where_its_reader_will_not_load`
  and `Test_pins_and_copies_in::test_names_a_test_the_parser_gives_up_on_as_not_read`,
  which patch or call `chain.rule_changes_reader`;
- `Test_module::test_an_absent_reader_is_the_loaders_sentence_alone`,
  which expects `lib/lines.py` to be named;
- one `test_settle.py` case whose docstring cites `lib/lines.py#live_lines`.

One case is gone,
`test_chain_check.py#Test_module::test_every_reader_of_a_retirement_calls_the_one_predicate`,
as *Removes* row 9 says. No case has a name that the old files lack
(executed). `seal layout --check` over the test files the move changed
refuses none and reports only (executed). S8 cannot pass while *Scope*
item 10 rebinds the module, so one of the two has to change. That is a
frame statement for the orchestrator to fold.

**Departure: `under_root` moved to `lib/gitcmd.py`.** *Scope* item 8 and
*Removes* do not name it. It turns a `/`-joined repository-relative path
into a disk path. At the base it had two readers in `unverified_check.py`:
`tree_at`, which moves to `chain_check.py`, and `open_record_rows`, which
moves to `lib/gaps.py`. So it has two readers in two modules. Item 8 says
"the rest to the `lib/` module that owns its kind". `lib/gitcmd.py` already
owns `git_path`, which is the opposite turn, so `under_root` stands beside
it. Its two cases moved to `tests/lib/test_gitcmd.py`. Judged against
`frame/design.md` *Scope* item 8.

**Decisions on names, each judged against *Scope* items 8 and 9.**
`chain_check.py`'s loader of `rule_changes.py` is `rule_changes_reader`,
and its class is `Test_rule_changes_reader`. The plain name `rule_changes`
would sit beside `rule_changes_read` and `rule_changes_of`, which take a
reader. The file's other getters are named `check_lines_reader` and
`pr_body_reader`. `chain_check.py` and `settle.py` each have a four-line
`policy_root(root)`. Each asks `lib/config.py#policy_root` of
`lib/optin.py#home_at`, as item 8 says. Neither script loads the other.
`rule_changes.py` gains `grammar`, `blocks` and `fields`,
`coordinates.py` gains `fence_rule`, and `payload_meter.py` gains
`_line_reader`. Each is a getter that only names its module, which
*Removes* row 2 allows. Each was mutated in no run. A getter that loaded
another module would raise `AttributeError` in every case that parses,
because each reads a name that only its own module has.

**`settle.py#policy_root` had nothing behind it, and now has a class.** A
mutant that read the repository root in place of the `seal/` root survived
the whole of `tests/skills/test_settle.py`, 175 cases. No case there writes
a `Policy root` key. At the base the call went through
`unverified_check.py#policy_root`, and no case of `settle.py` reached it
with a key either. `Test_policy_root` now holds one case on each side, and
the same mutant turns the case with the key red (commit `2d46c5d34`,
executed). `chain_check.py#policy_root`'s mutant turned the moved
`Test_policy_root::test_accepts_the_row_a_config_writes` red (executed).

**`chain_check.py#main` asks `lib/optin.py#repo_root`, which answers `""`
where the base's answered `None`.** So the test is `if not root`. `--root`
names a directory, which is the one form `optin.repo_root` reads. Judged
against *Scope* item 8.

**The worlds the moved cases read are imported from
`tests/skills/test_unverified_check.py`.** The fixtures `plain`, `forked`,
`settle` and `joined` are built once for that module. `tests/lib/test_gaps.py`,
`tests/skills/test_chain_check.py` and `tests/skills/test_settle.py` bind
them by assignment, which pytest collects as fixtures of the importing
module. Their helpers and constants come in by `from … import`. Building a
second copy of each world would make a moved case read a different
fixture, which is a change *Scope* item 10 does not allow. #1489 owns the
layout of the test files and may give the worlds a home of their own
(*Overlap with the release*).

**A test file that loaded `unverified_check.py` for a moved name now loads
that name's home** (*Scope* item 10). Thirteen files changed:

- Under `tests/behaviour/`: `test_a_phase_hands_the_next_one_a_record.py`,
  `test_a_section_marked_for_one_role_reaches_only_that_role.py`,
  `test_both_editions_carry_the_same_folds.py`, `test_docs_line_wrap.py`,
  `test_every_reader_ends_a_line_where_gfm_does.py`,
  `test_one_heading_rule_holds_to_commonmark.py`,
  `test_the_pull_request_language_is_the_repositorys.py`,
  `test_the_readers_hide_what_a_renderer_hides.py`,
  `test_the_sealer_guarantees.py`, `test_unverified_rows_close.py` and
  `test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`.
- `tests/skills/test_broad_gate.py` and `tests/skills/test_rule_changes.py`.

Each loads `lib/lines.py`, `lib/blocks.py` or `lib/gaps.py`, whichever
holds what it reads. Three of them need a note:

- `test_whether_a_line_is_live_is_asked_by_what_the_line_does.py` matches
  `docs/checks/the-fold.md` against each reader's spelling. It now matches
  `#live_lines` and `#readable` by name alone, as it already did for
  `#hidden_lines`. The document is written at the settle, and
  `frame/design.md` *Rule changes* carries the two sentences.
- `test_unverified_rows_close.py` adds `lib/gaps.py` to the texts that
  state how a row closes. The paragraph on closing moved from
  `unverified_check.py`'s docstring to `lib/gaps.py`'s, so the rule is
  stated once.
- `tests/behaviour/test_release_hygiene.py` asserts `"lib/lines.py" in
  check` where it asserted `"unverified_check.py"`. *Overlap with the
  release* rules that phase 3 rewrites the assert to the reader
  `chain_check.py` loads, because #1488 has not merged into this branch.

`test_payload_meter.py`'s copied-alone case for a `CLAUDE.md` now expects
`lib/blocks.py`, the first module that run loads.

**`ruff.toml` no longer lints `unverified_check.py` at the floor.** After
the move, no run below the floor reaches it. The floor case named the line
stale (executed). The floor table at HEAD equals the one at `333fb9def`
without that one line (executed: a `diff` of the two tables), which is
what S9's first half allows.

**The sentences on moved units, *Scope* item 11, are in the move's commit
`27d2476c1`.** They cover:

- the docstrings and comments of the scripts of G8 and of
  `unverified_check.py`;
- `lib/blocks.py` `:20` and `:122`, `lib/fields.py` `:44` and `:240`, and
  `lib/sibling.py`'s example;
- `tests/censuses.py#heading_rule` with its case in `tests/test_censuses.py`;
- the comments in `tests/lib/test_blocks.py`;
- `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`,
  which now names `chain_check.py` and `settle.py` as the loaders of
  `rule_changes.py`;
- the citations in `tests/skills/test_payload_meter.py` and
  `tests/skills/test_settle.py`.

The list comes from these runs:

- `git grep` of `unverified_check` across the tree outside `seal/threads/`
  and `docs/`;
- `git grep` of `unverified_check(.py)?#` and `by path`, outside
  `seal/threads/` and `docs/`;
- `git grep` of `SHARED_READER`, `rules.reader()` and `shared_reader`.

It is a sample. A sentence that names a moved unit without the script's
name is not reached by it. The citations left in `docs/` are the five that
*Rule changes* carries. `docs/README.md:59` and
`docs/checks/the-unverified-record.md:3` name what the command reads, and
the command still reads it.

**The scenarios this phase owes.**

- S1 (executed: `test_tmp_count.py` in this phase's scratch directory. It
  runs `settle.py` of a `git archive` of `333fb9def` and of a clone of HEAD
  as `__main__`, both with the clone as the working directory). With no
  argument, HEAD executes 12 files once each. `lib/gaps.py`,
  `lib/items.py` and `lib/lines.py` are among them, and
  `unverified_check.py` is not. The base executed 9 files 165 times. With
  `--all-earlier`, HEAD executes the same 12 once each, where the base
  executed 760. Stdout is byte-identical by `cmp`: 108,864 bytes and
  308,784 bytes.
- S2 (executed: `git grep -n unverified_check -- '*.py'` outside the
  script and its test file). Each hit is one of four things: the
  `unverified` row of `seal.py#TOOLS`; a sentence naming `absent_root`,
  `display_path`, `repo_relative` or `main`, which the script keeps; the
  load in `test_a_foreign_seal_dir_keeps_the_records_shared.py`, which
  runs the command's `main`; or a test's history sentence or an import of
  `test_unverified_check`. No script loads it.
- S3 (executed): `spec_from_file_location` outside `tests/` is
  `lib/sibling.py:86` alone. `def _?load(` is `lib/sibling.py#load` and
  `session_cost.py#load` alone.
- S4 for `rules.py` and `release_report.py` (executed): see the first
  paragraph. Copied alone and run with no argument and with `--help`, each
  keeps its exit code and its first line of stderr from `457394c19`:
  `rules.py` 2 and 0, `release_report.py` 2 on its usage and 0, with no
  traceback (executed).
- S8: see the exception above.
- S9 (executed): both halves, as above.
- `frame/questions.md` Q1, in part. `tests/skills/test_chain_check.py`,
  `tests/skills/test_settle.py`, `tests/lib/test_console.py`,
  `tests/lib/test_gitcmd.py` and the three new `tests/lib/` files pass
  serially in one process each (executed). The phase-boundary set ran
  under pytest-xdist, so it does not answer Q1 for the rest.
- The phase-boundary set (executed, one `bin/test` command): the files the
  plan's row 3 names, with the test module of each script of G8, every
  test file this phase edited, and `tests/github/test_finding_counts.py`
  and `tests/github/test_release_seal.py`, whose scripts read
  `chain_check.SHARED_READER`. 2,419 passed, 8 skipped.
