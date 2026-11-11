# Phase 4: 1794396808-test-files-declare-no-target

## What this phase found

**The frame holds for where the cases go, and not for which cases go.**
The phase started at `b33864d97`, after the merge `30e82d2f8` brought #1482
in. Design *The files* sends cases of `tests/behaviour/` to module files
under `tests/skills/`. Phase 3's probe ran again over the 51
files at `b33864d97` (executed: design G7's script). A `git grep` over
`tests/behaviour/` for `.main(`, `subprocess.run(`, `load_module(` and
`spec_from_file_location(` added the cases that load a script by its path
(executed). Each case either search reached was ruled by design *The kinds*
(`frame/questions.md` Q1). Twenty-seven are kind M and moved. The rulings
that differ from design *The files* are in the next table.

| File | Design *The files* | Ruled here | Ground |
|---|---|---|---|
| `test_a_foreign_seal_dir_keeps_the_records_shared.py` (`:174`) | each case moves to `test_seal.py`, `test_chain_check.py`, `test_unverified_check.py`, `test_seal_stamp.py`, `test_pr_body.py`, `test_pact_check.py` or `tests/github/test_rules.py`; the file is deleted | the gate, settle and fold cases go to `tests/skills/test_broad_gate.py`, `test_settle.py` and `test_fold_check.py`; the `seal rules` case stays for phase 5; the file is not deleted in this phase | Each of the three cases runs the script `seal gate`, `seal settle` or `seal fold` hands over to, and its asserts read that script's exit code and output, so the case is kind M for that script. The list in the row names none of the three. The `seal rules` case is bound for `tests/github/test_rules.py`, which is phase 5's (plan *Phases* row 5). The file keeps that one case until then. |
| `test_a_reference_root_is_read_and_never_taken.py` (`:178`) | the case running `seal` moves to `tests/skills/test_seal.py` | no case moves | `test_every_shipped_command_is_classified` lists `bin/` and `skills/implement/scripts/seal.py#TOOLS` and holds both against the file's own table of commands. That is a walk of the tree, kind T1. |
| `test_a_signer_declares_its_pact.py` (`:184`) | the one running `seal` moves to `tests/skills/test_seal.py` in phase 4 | no case moves | `test_s4_the_configs_this_plugin_writes_are_silent` holds what `skills/implement/scripts/seal.py#serialized` writes, and this repository's `seal/config.json`, to `lib/config.py`. That is one property across two modules, kind T3, as `trail/phases/phase-3.md` already found. |
| `test_chain_hooks_hardening.py` (`:187`) | the one calling `fold_check.py` moves to `tests/skills/test_fold_check.py` | no case moves | `test_bin_wrapper_resolves_the_checker_from_any_cwd` holds that `bin/seal` and `bin/seal.cmd` stand, and runs the one the platform executes from `/`. That wrapper reaches `fold_check.py` through `lib/launch.py` and `skills/implement/scripts/seal.py`. Its subject is that chain of files, so it is T3. |
| `test_the_gate_asks_the_range_ci_will_ask.py` (`:202`) | T2, with no destination | `test_the_panel_prints_the_ref_on_the_base_row` moves to `tests/skills/test_broad_gate.py::Test_panel` | The case calls `broad_gate.py#panel` and its asserts read the lines the function returned, so it is kind M. The file's other nine cases hold the workflow's spellings against the gate's, read documents, or drive the file's own reader of the workflow. |
| `test_the_pull_request_language_is_the_repositorys.py` (`:204`) | the one calling `chain_check.py` moves to `tests/skills/test_chain_check.py` | no case moves | `test_every_template_is_named_by_a_document_that_ships` walks `git ls-files`, kind T1. The file's other reads of `chain_check.py` hold a template to that script's constants, which is a rule across files (T2) or across modules (T3). |
| `test_the_stamp_reaches_the_person_it_is_drawn_for.py` (`:212`) | a case calling one of `broad_gate.py` and `seal_stamp.py` alone moves | no case moves | `test_the_stamp_draws_its_sample_and_neither_command_offers_a_scale` runs `seal_stamp.py --shape`, and holds both `seal_stamp.py --help` and `broad_gate.py --help` to one fact, so it is T3. The file's other cases read documents. |

The other files the probe reached give nothing to `tests/skills/`:
`test_the_seal_is_taken_once_by_the_sealer.py`,
`test_the_sealer_guarantees.py`,
`test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`,
`test_a_section_marked_for_one_role_reaches_only_that_role.py`,
`test_a_document_that_names_a_script_says_how_to_reach_it.py`,
`test_release_hygiene.py`, `test_this_repository_passes_its_own_checks.py`,
`test_every_entry_point_runs_at_the_floor.py`,
`test_settle_applies_rule_changes_in_place.py`,
`test_every_reader_ends_a_line_where_gfm_does.py` and
`test_unverified_rows_close.py`. Each case there reads a document, holds
several modules to one fact, or walks the tree. Each is ruled again where
phase 6 or 7 files its file.

**What moved.** Twenty-seven cases moved, 37 collected items.

| From | Cases | To |
|---|---|---|
| `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py` | S1, the two `test_s6_mode_*` cases and `test_s6_a_switch_that_could_not_stage_names_agentic_seal_in_the_command` | `tests/skills/test_seal.py::Test_mode` |
| the same | the two `test_pr_checks_install_*` cases | `tests/skills/test_seal.py::Test_pr_checks` |
| the same | `test_s6_export_in_shared_mode_names_agentic_seal_in_the_way_out` | `tests/skills/test_seal.py::Test_export` |
| the same | `test_s6_a_copy_travels_as_seal_and_lands_under_agentic_seal` and `test_s6_an_import_names_what_blocks_it_in_the_root_by_the_roots_own_name` | `tests/skills/test_seal.py::Test_import_` |
| the same | the seven `test_s3_*` cases | `tests/skills/test_chain_check.py::Test_main` |
| the same | `test_s4_the_stamp_queues_a_sealed_guarantee_under_agentic_seal` | `tests/skills/test_seal_stamp.py::Test_main` |
| the same | `test_s5_pr_body_check_reads_the_seal_and_the_records_under_agentic_seal` | `tests/skills/test_pr_body.py::Test_main` |
| the same | the two `test_s5_unverified_*` cases | `tests/skills/test_unverified_check.py::Test_main` |
| the same | `test_s5_pact_names_the_signers_key_under_agentic_seal` | `tests/skills/test_pact_check.py::Test_check` |
| the same | `test_s5_gate_reads_its_key_from_agentic_seal_and_names_it_where_none_is` | `tests/skills/test_broad_gate.py::Test_main` |
| the same | `test_s5_settle_shows_a_work_item_released_under_agentic_seal` | `tests/skills/test_settle.py::Test_main` |
| the same | `test_s5_fold_reads_its_keys_from_agentic_seal` | `tests/skills/test_fold_check.py::Test_main` |
| `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py` | `test_the_absent_row_refusal_no_longer_tells_the_reader_to_write_one` and `test_the_absent_row_refusal_says_whose_the_row_is_and_where_it_is_answered` | `tests/skills/test_broad_gate.py::Test_missing_row` |
| `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py` | `test_the_panel_prints_the_ref_on_the_base_row` | `tests/skills/test_broad_gate.py::Test_panel` |

The foreign file's world moved to `tests/conftest.py`: `ITEM`, `REMOTE`,
`PACKAGE`, `ROOT_RECORDS`, `records_at`, and the fixtures `package` and
`shared`. Cases in the nine destination files and the case that stays build on
it. `tests/conftest.py` still loads alone, because the world needs only
names that file already defines, so `tests/test_conftest.py` passes
(executed, in the boundary run below). The other helpers moved into one
destination file each: `MODELESS`, `files_under`, `tool` and
`configured` to `tests/skills/test_seal.py`; `DECLARED`, `DECLARATION`,
`NO_GUARANTEE`, the fixture `declared` and `checked` to
`tests/skills/test_chain_check.py`; `flat` and `missing_row_text` to
`tests/skills/test_broad_gate.py`. `test_broad_gate.py`, `test_settle.py`
and `test_fold_check.py` import `tool` or `configured` from
`test_seal.py` by name, as the framer's fold lets a helper stand in one
destination file. The foreign file and the broad-gate-row file import
`configured` and `flat` back the same way.

**A consequence of the move: the seven S3 cases now carry a rule.**
`tests/skills/test_chain_check.py::Test_main` carries
`@pytest.mark.rule("routing-read-first")` on the class, at `b33864d97`
and now. The seven `test_s3_*` cases joined that class, so each now runs under
the rule whose `check:` line stands at
`docs/running/the-review-and-parity-arms.md:44`. No case in the class
changed, and `bin/seal rules --check` holds (below). The proofer reads
whether the S3 cases belong under that rule or under a class of their own.

**Departure: the bindings were aligned before the move, and 11 cases were
rewritten.** Design *Scope* item 5 moves a case's names unchanged. The
destination files bind several names the moving cases read, and bind them
differently.

- `tests/skills/test_chain_check.py` binds `git` as `conftest.git_out`,
  where the foreign file read `conftest.git`. Both run git with
  `check=True`, and the cases discard the result. The moving cases now
  call `git_out`, which keeps them off both meanings of `git`.
- The foreign file bound `SEAL`, `CHAIN`, `UNVERIFIED` and `PACT` under
  its own load names. The destinations bind `SEAL`, `chain`, `UC` and
  `pc`.
- It imported `test_seal_stamp.py`'s and `test_pr_body.py`'s names under
  aliases (`STAMPED`, `STAMPED_ID`, `STAMP`, `BODIED`, `BODY_RECORDS`,
  `MARK_ROW`, `PR_BODY`). In the destinations those are `ITEM_NAME`,
  `ITEM_ID`, `stamp`, `NAME`, `RECORDS`, `ROW` and `PR`.
- Its own `RECORDS` would collide with `test_pr_body.py#RECORDS`, so it
  became `ROOT_RECORDS`.
- `test_the_gate_asks_the_range_ci_will_ask.py` defined its own
  `gate_module` under another load name. It now imports
  `test_broad_gate.py#gate_module`.
- `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py` read
  `conftest.ROOT`, a string. `test_broad_gate.py` binds `ROOT` as a
  `pathlib.Path` of it, and the old file now does the same.

`6adfab9cc` made the three old files bind each name as its destination
does. Their cases passed there, `55 passed` (executed). The move commit
`0a56771a6` then moved the cases. `CONTRIBUTING.md` *A module's old cases
get one verdict each when the module is rebuilt* asks for one line per old
case rewritten. Each of these guarded what its name states, and now holds
it in the class the move table names, reading the same module under the
destination's name.

- `test_s6_mode_moves_agentic_seal_under_the_git_directory_and_back`: reads `ROOT_RECORDS` for `RECORDS`.
- `test_s6_a_copy_travels_as_seal_and_lands_under_agentic_seal`: the same.
- `test_s3_the_check_judges_the_declaration_under_agentic_seal`: `git_out` for `git`.
- `test_s3_the_pull_request_that_adds_agentic_seal_is_judged_under_it`: the same.
- `test_s3_a_branch_nothing_declares_is_told_to_add_it_under_agentic_seal`: the same.
- `test_s3_a_pull_request_deleting_agentic_seal_declares_nothing`: the same, and `chain` for `CHAIN`.
- `test_s4_the_stamp_queues_a_sealed_guarantee_under_agentic_seal`: `ITEM_NAME`, `ITEM_ID` and `stamp` for the aliases.
- `test_s5_pr_body_check_reads_the_seal_and_the_records_under_agentic_seal`: `NAME`, `RECORDS`, `ROW` and `PR` for the aliases.
- `test_s5_unverified_reads_agentic_seal_threads_as_the_roots_own`: `UC` for `UNVERIFIED`.
- `test_s5_unverified_walks_agentic_seal_and_passes_over_the_packages_specs`: the same.
- `test_s5_pact_names_the_signers_key_under_agentic_seal`: `pc` for `PACT`.

The proofer reads `6adfab9cc` as the rewrite it is. No case was cut.

**The criterion, design *Scope* item 4.** Design *The cases #1488 read*
ran in phase 3 over `tests/text/` and `tests/behaviour/` as written from
`18a7e18fb`, and its output is in that phase's scratch (executed then, read
now). Of the 27 moving cases it printed 20: 18 of the foreign file's and
the two `missing_row` cases. The other seven were read whole here:
`test_s3_a_design_the_pull_request_edits_under_agentic_seal_is_read`,
`test_s3_the_pull_request_that_adds_agentic_seal_is_judged_under_it`,
`test_s4_the_stamp_queues_a_sealed_guarantee_under_agentic_seal`,
`test_s5_unverified_reads_agentic_seal_threads_as_the_roots_own`,
`test_s6_a_copy_travels_as_seal_and_lands_under_agentic_seal`,
`test_s6_an_import_names_what_blocks_it_in_the_root_by_the_roots_own_name`
and `test_the_panel_prints_the_ref_on_the_base_row`. None of the three old
files is in #1488's *Out*
(`seal/threads/1794383427-asserts-pin-literal-phrases/frame/design.md`,
read). None of the seven has an assert that reads a file of the tree as
text. Each assert reads an exit code, a command's output, a function's
return, or a file the case itself wrote. #1488's *What an assert reads*
puts each of those outside *The criterion*, so every assert was kept and
no ruling commit was owed. The foreign file did not change between
`18a7e18fb` and `b33864d97`. The other two did (executed: `git diff
--stat`), so the two `missing_row` cases and the panel case were read as
they stand at `b33864d97`.

**The move check, design *Scope* item 5** (executed, one run for
`tests/skills/`, at `0a56771a6`):

```
bin/seal layout --moved 6adfab9cc --from tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py tests/skills/test_seal.py tests/skills/test_chain_check.py tests/skills/test_seal_stamp.py tests/skills/test_pr_body.py tests/skills/test_unverified_check.py tests/skills/test_pact_check.py tests/skills/test_broad_gate.py tests/skills/test_settle.py tests/skills/test_fold_check.py --to <the same 12 files>
seal layout: moved: 1003 old cases, 1598 items against 1598 at 6adfab9ccfe5, 0 failed
```

It exited 0, so no module carries a mutation table. The three old files
stand in both lists: the foreign file keeps a case for phase 5, and the
other two keep the cases that read documents. The same command from
`b33864d97` exited 1 with 40 failures (executed). Twenty-two are the 11
rewritten cases, each named once as not found unchanged and once as
standing for no old case. The other 18 name a binding or the fixture
`declared` that `6adfab9cc` changed. Those are the changes `6adfab9cc`
made.

**The cases and seconds before and after** (executed: `bin/test <file> -q
-p no:xdist`, one run each, at `b33864d97` in a worktree since removed,
and at `0a56771a6`).

| File | At `b33864d97` | At `0a56771a6` |
|---|---|---|
| `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py` | 35 in 15.39 s | 1 in 0.28 s |
| `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py` | 10 in 0.01 s | 8 in 0.02 s |
| `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py` | 10 in 0.68 s | 9 in 0.60 s |
| `tests/skills/test_seal.py` | 391 in 16.47 s | 404 in 16.59 s |
| `tests/skills/test_chain_check.py` | 225 in 102.17 s | 236 in 109.19 s |
| `tests/skills/test_seal_stamp.py` | 192 in 3.44 s | 193 in 4.29 s |
| `tests/skills/test_pr_body.py` | 97 in 5.65 s | 98 in 7.02 s |
| `tests/skills/test_unverified_check.py` | 57 in 2.39 s | 61 in 2.44 s |
| `tests/skills/test_pact_check.py` | 114 in 6.49 s | 115 in 6.55 s |
| `tests/skills/test_broad_gate.py` | 269 in 11.30 s | 273 in 11.46 s |
| `tests/skills/test_settle.py` | 178 in 52.79 s | 179 in 53.07 s |
| `tests/skills/test_fold_check.py` | 29 in 1.54 s | 30 in 1.59 s |

The three old files fell by 15.18 s and the nine destinations grew by
9.96 s. Each figure is one run, so the 5 s between them is no finding.
The 12 files hold 1,607 items before and after: `bin/test <the 12 files>
-q` gave `1606 passed, 1 skipped` at both commits (executed). The cases
that run real git are kept, each built on the `package` or `shared`
fixture: the 24 cases moved from the foreign file other than
`test_s5_rules_check_excuses_a_section_a_design_under_agentic_seal_removes`,
which stays. Each holds what one command does with a root that git
tracks at `agentic-seal/`, so each needs the repository a fixture
commits.

**The pairs, design *Scope* item 11.** `bin/seal layout --pairs` gave
`142 files read, 43 pairs` at `b33864d97` and at `0a56771a6`, and the two
lists are identical (executed). The move makes no pair, so no class
docstring owes a reason.

**S6 and S7, and the citations, design *Scope* items 9 and 10**
(executed at `0a56771a6`). `bin/seal rules --check` exits 0, and its last
line is `seal rules: all 177 check lines in 69 rule files hold.`
`bin/seal layout --check` exits 0, and its last line is `142 files read, 0
refused, 77 declare no TARGET`. That count is the base's, since this phase
deleted no file and declared no `TARGET`. It adds three `report:` lines,
one each for `tests/conftest.py`'s `package`, `records_at` and `shared`,
which have no `Test_` class. Those are reports and refuse nothing, like
the other functions of `tests/conftest.py` it reports. `git grep -l -w`
outside `seal/threads/` and `CHANGELOG.md` on each moved case's name
lists only its new file. `git grep` on the three old files' stems found
these citations:

- `tests/censuses.py:1421-1422` cited the foreign file for its world. It
  now cites the `package` and `shared` fixtures of `tests/conftest.py`.
- `docs/running/the-broad-gate.md:76` is a `check:` line naming
  `test_the_gate_asks_the_range_ci_will_ask.py`. It stands, since that
  file still holds the case comparing the workflow with the gate.
- `skills/verify/scripts/broad_gate.py:428` is a comment citing the same
  file. It stands for the same reason.
- `tests/text/test_the_rules_claude_md_names_have_one_home.py:107` names
  `test_the_gate_asks_the_range_ci_will_ask.py` as a file that carries the
  word `identifiers`. It stands, since the file still carries it, and that
  case passed in the boundary run below.

The three old files' docstrings now say what each holds and where its
moved cases stand. The A10 comment of the broad-gate-row file cited an
executed absent-row case in
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`. No case
there reads `missing_row` at `b33864d97` (executed: `grep`), so the
comment now cites `tests/skills/test_broad_gate.py::Test_missing_row`
alone. Each of the nine destination files' docstrings gained one
sentence: the cases that run the command beside a project's own `seal/`
package build `tests/conftest.py`'s `package` or `shared` repository,
whose root stands at `agentic-seal/`. The comment above that world in
`tests/conftest.py` names the foreign file's `seal rules` case, so phase
5, which moves that case, re-points it.

**How the move was made.** A script under the phase's scratch directory
cut each case and helper by its line range. It checked that each range
parsed to the one definition it named, added `self`, and indented it into
its class. It found each class through `ast`, decorators included, and
every anchor it used asserted one match (contract rule 9). Its first run
stopped at `test_chain_check.py`, whose `Test_main` carries a decorator,
after writing `tests/conftest.py` and `tests/skills/test_seal.py`. Those
two files held no uncommitted work, so they were restored with `git
checkout` and the script now writes every file at its end. Then `ruff
check --select I --fix`, `ruff format` and `ruff check` ran clean over the
14 changed files (executed). The move check above compared every case.

**Overlap with #1484.** `0a56771a6` adds one case to
`tests/skills/test_seal_stamp.py::Test_main` and widens that file's import
from `conftest`. #1484 edits the same file (plan *Overlap with the
release*). Whichever merges second keeps both.

**The phase boundary, as one command** (executed at `0a56771a6`, before
these records were written):

```
bin/test tests/text tests/behaviour tests/skills/test_seal.py tests/skills/test_chain_check.py tests/skills/test_seal_stamp.py tests/skills/test_pr_body.py tests/skills/test_unverified_check.py tests/skills/test_pact_check.py tests/skills/test_broad_gate.py tests/skills/test_settle.py tests/skills/test_fold_check.py tests/skills/test_rule_changes.py tests/skills/test_passages.py tests/test_conftest.py tests/test_censuses.py tests/github/test_rules.py tests/github/test_plugin_directory_check.py tests/lib/test_config.py tests/lib/test_console.py tests/lib/test_gaps.py tests/lib/test_gate.py tests/lib/test_items.py tests/lib/test_lines.py -q
```

It gave `3652 passed, 9 skipped` and exited 0 (S9). The set follows design
*The narrow run*. It holds `tests/text` and `tests/behaviour`, where the 77
files that declare no `TARGET` stand, and the check run and
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` among them.
It holds the nine destination files. It holds each test file outside
those directories that names a changed path's name at `b33864d97`
(executed: `git grep -l` over `tests/`), and `tests/github/test_rules.py`,
since a `check:` line names a changed file. The three warnings are pending
corrections of other work items, which
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` reports. The
suite beyond the set is `unverified`, and the orchestrator's broad gate
answers it.
