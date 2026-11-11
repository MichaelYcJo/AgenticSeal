# Phase 3: 1794396808-test-files-declare-no-target

## What this phase found

**The frame holds for where the cases go, and not for which cases go.**
The phase started at `9b6c36cf0`. Design *The files* gives seven files of
`tests/behaviour/` a destination under `tests/lib/`, `tests/hooks/` or
`tests/evals/`, from design G7's probe. The probe ran again over the 51
files at `9b6c36cf0` (executed: design G7's script, kept from the framer's
scratch). It names 64 cases that reach a module under `lib/`, `hooks/` or
`evals/`. A `git grep` over `tests/behaviour/` for `"lib"`, `"hooks"`,
`"evals"`, `load_lib_module(` and `sys.path.insert` found no other case
(executed). Each of the 64 was ruled by design *The kinds*
(`frame/questions.md` Q1). Forty-two were read whole. The other 22 are the
cases of `test_a_cited_section_stands_in_its_file.py`, and they were ruled by
the helpers they share. That file reads `lib/config.py` only through
`#policy_root`, in its helper `corrections` (`:203`), which finds the
pending rule changes the file's own citation checker excuses. So each of
the 22 holds that checker, or walks the tree with it, and none is M (read).
Eighteen of the 64 are kind M and moved, and two cases the probe does not
reach moved with the corpus they hold. The rulings that differ from design
*The files* are in the next table.

| File | Design *The files* | Ruled here | Ground |
|---|---|---|---|
| `test_chain_hooks_hardening.py` | the case calling `hooks/core-start.py` moves to `tests/hooks/test_core_start.py` | no case moves | No case runs `hooks/core-start.py`. The case the probe reached, `test_the_plugin_registers_two_hooks_and_writes_none_into_git`, reads `hooks/hooks.json` and the tracked listing, and names the script only as a string. |
| `test_evals_layout.py` | T1, no destination | T1 for `test_the_sealer_cases_are_the_generators_output` too | The case runs `evals/scripts/rule_cases.py`, and its assert holds the output against the whole committed directory `evals/behaviour/sealer/`. A hand edit of that directory fails it with the module unchanged, so it walks a directory of the tree. Nothing moves to `tests/evals/`. |
| `test_the_pull_request_language_is_the_repositorys.py` | cases calling `lib/config.py` move to `tests/lib/test_config.py` | none of the eight moves | Seven assert what the file's own model of `skills/commit-pr-convention/SKILL.md` answers: `config_homes` resolves the root, `configured_language` lands on English, and `the_mirror` and `mirror_to_refuse` name the mirror. `lib/config.py#declared_value` is one step of that model, and `lib/config.py` has no English default or home order. `test_the_existing_mirrors_are_consistent_with_the_rule` also globs `seal/threads/`. The eighth, `test_this_file_loads_the_one_reader_and_not_a_copy_of_it`, holds the loading that model rests on. #942's phase 6 already moved the reader's own cases to `tests/lib/test_config.py`. The file is phase 7's to file. |
| `test_a_signer_declares_its_pact.py` | cases calling `lib/config.py` move to `tests/lib/test_config.py` | none moves in this phase | `test_s4_the_configs_this_plugin_writes_are_silent` holds `skills/implement/scripts/seal.py#serialized`'s output and this repository's `seal/config.json` to the reader, which is a property of two modules. The design sends "the one running `seal`" to phase 4, and this phase leaves it there. The two key cases hold a template's and a skill's sentence against `lib/config.py#PACT_KEY` and `#SIGNERS_KEY`, and *The kinds* says that is not M. |
| `test_one_table_walker_reads_what_gfm_renders.py` | the one calling `lib/config.py` moves to `tests/lib/test_config.py` | `test_the_config_pass_is_the_config_readers_header` moves to `tests/lib/test_tables.py` | The case calls no function of `lib/config.py`. It holds the corpus's `config` header equal to `lib/config.py#OLD_TABLE`, the header the walker is handed. It holds the corpus of `gfm_table`'s cases, and `tests/lib/test_tables.py` already loads `lib/config.py` for that constant. |
| `test_one_table_walker_reads_what_gfm_renders.py` | M | `test_round_3s_shapes_are_inside_the_corpus` and `test_the_corpus_is_counted` move with the corpus | Neither calls shipped code. Each holds the corpus that `gfm_table`'s cases read. The corpus moved, so they moved to `Test_gfm_table` beside it. The three cases that hold `tests/gfm_table_oracle.py` alone stay, as the design says. |
| `test_unverified_rows_close.py` | a case calling `lib/blocks.py` or `lib/tables.py` alone moves | none | `test_the_fence_walks_agree_shape_by_shape` holds three modules' walks to each other, which is T3. The other cases call `skills/verify/scripts/unverified_check.py`, so they are phase 4's. |

The other cases of the 64 stay as design *The files* starts them, and each
is ruled again where its file is filed.
`test_waiver_decided_at_start.py#test_the_policy_tables_the_review_answers_and_the_skill_cites_it`
reads `lib/config.py` only to find the policy in force, and holds
documents. The three cases of
`test_whether_a_line_is_live_is_asked_by_what_the_line_does.py` hold four
readers of three modules to one table and to a document, which is T3. The
three cases of `test_no_document_names_the_old_roots.py` hold documents
against `lib/optin.py#SECOND_HOME`.
`test_every_entry_point_runs_at_the_floor.py#test_the_floor_has_one_source`
lists the floor's carriers over the tracked files.
`test_this_repository_passes_its_own_checks.py::Test_routing_declarations`
parses every committed declaration.
`test_every_reader_ends_a_line_where_gfm_does.py#test_every_copy_of_the_splitter_is_the_readers`
holds two modules under `skills/verify/scripts/` to each other. The grep
added three cases the probe does not reach:
`test_waiver_decided_at_start.py`'s three `test_the_template_PARSES_into_*`
cases import `lib/routing.py` through `sys.path`. Each parses
`templates/records/sdd-routing.md` and holds the template's placeholders to
the parser's vocabulary, so the template is its subject, and #1488 read
each of them whole.

**What moved.** Twenty cases moved: the 18 of kind M under design *The
kinds*, and the two corpus cases that hold what those cases read.

| From | Cases | To |
|---|---|---|
| `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py` | the 12 that call `tables.gfm_table`, the two corpus cases and the config-header case | `tests/lib/test_tables.py::Test_gfm_table` |
| `tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py` | `test_the_table_walker_never_leaves_both_readings` | `tests/lib/test_tables.py::Test_unfenced` |
| the same | `test_the_walk_is_exact_somewhere` | `tests/lib/test_blocks.py::Test_walk` |
| the same | `test_where_the_walk_claims_to_be_exact_it_is` | `tests/lib/test_blocks.py::Test_walk_text` |
| the same | `test_the_routing_reader_never_leaves_both_readings` and `test_the_routing_reader_hides_something` | `tests/lib/test_routing.py::Test_module`, since `lib/routing.py#shown` has no class |

The walker's corpus (`HEADERS` to `disagreement`, `GENERATOR_SEED`,
`GENERATOR_DOCUMENTS` and `vocabulary`) moved to `tests/lib/test_tables.py`,
and so did `shared_rule`, `uc`, `walker_base` and `leaves_both`. The readers'
corpus (`NBSP` to `CORPUS`), `as_read` and `disagreements` moved to
`tests/lib/test_blocks.py`. `tests/lib/test_tables.py` had imported
`HEADERS`, `INDENTS`, `KINDS` and `document` from the walker file, and now
defines them itself. The two oracle files keep the oracle's own cases: 3
and 7.

**Departure: the shared corpus is not in `tests/conftest.py`.** Design
*Scope* item 5 puts a helper that cases bound for two files use into
`tests/conftest.py`. The first build did that. Then
`tests/test_conftest.py::Test_pytest_terminal_summary::test_accepts_a_slow_case_named_and_failing_nothing`
failed with `ModuleNotFoundError: No module named 'block_shapes'`
(executed). That case loads `tests/conftest.py` from a directory where
`tests/` is not on `sys.path`, and the corpus needs `block_shapes` imported
at module level. Loading `block_shapes` another way would change the
definitions the move check compares. So the corpus stands in
`tests/lib/test_blocks.py`, and `leaves_both` in `tests/lib/test_tables.py`.
`tests/lib/test_tables.py` and `tests/lib/test_routing.py` import them by
name. `CONTRIBUTING.md` *The test layout* allows it: "A helper two test
files use is defined once, in `tests/conftest.py` or in one of the two
files, which the other imports by its name." This phase does not change
`tests/conftest.py`. So the frame's *Overlap with the release* row for
#1482 no longer holds where it says phase 3 adds a helper there.

**Departure: the module bindings were aligned before the move, and one
case was rewritten.** Design *Scope* item 5 moves a case's names
unchanged. Each destination file already binds its module under a name the
moving cases read: `tables`, `config`, `blocks` and `routing`. Its
definition differs from the old file's only in the name `load_lib_module`
registers. The old walker file bound `tables` as
`load_lib_module("tables.py", "tables_for_the_table_walker")`, and
`tests/lib/test_tables.py` binds it as `load_lib_module("tables.py",
"tables_under_test")`. Both names are one variable, so neither file can
keep both definitions. `tests/lib/test_tables.py` also had to bind `oracle`
to `tests/gfm_table_oracle.py` for the walker's cases, while
`test_the_table_walker_never_leaves_both_readings` read `oracle` as
`tests/commonmark_oracle.py`. `20a9460fa` made the old files bind each
module as its destination does, and made that one case read the CommonMark
oracle as `commonmark_oracle`. The cases of both old files passed there,
`571 passed` (executed). `7a2c58b2c` then moved the cases.
`CONTRIBUTING.md` *The test layout* asks one line per old case rewritten:
`test_the_table_walker_never_leaves_both_readings` guarded that
`lib/tables.py#unfenced` never leaves both its base reading and the
renderer's, and it holds that now in `Test_unfenced`, reading the same
module under its module name. The proofer reads `20a9460fa` as the
rewrite it is.

**The criterion, design *Scope* item 4.** Design *The cases #1488 read* ran
over `tests/text/` and `tests/behaviour/`, both written from `18a7e18fb`
with `git show` (executed). It printed 341 lines. Of the 20 moving cases it
printed one, `test_a_heading_inside_the_list_item_does_not_end_it`. The
other 19 were read whole. Neither file is in #1488's *Out*
(`seal/threads/1794383427-asserts-pin-literal-phrases/frame/design.md:45`,
read). None of the 19 has an assert that reads a file of the tree as text.
Each assert reads what `lib/tables.py`, `lib/blocks.py` or `lib/routing.py`
returned for a text the case built, an oracle's answer, the corpus, or
`lib/config.py#OLD_TABLE`. #1488's *What an assert reads* puts each of
those outside *The criterion*, so every assert was kept. No ruling commit
was owed. Neither file changed between `18a7e18fb` and `9b6c36cf0`
(executed: `git diff --stat`).

**The move check, design *Scope* item 5** (executed, one run for `lib/`):

```
bin/seal layout --moved 20a9460fa --from tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py tests/lib/test_tables.py tests/lib/test_blocks.py tests/lib/test_routing.py --to tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py tests/lib/test_tables.py tests/lib/test_blocks.py tests/lib/test_routing.py
seal layout: moved: 77 old cases, 753 items against 753 at 20a9460fa145, 0 failed
```

It exited 0, so no module carries a mutation table. The same command at
`9b6c36cf0` exited 1 with 19 failures (executed). Eighteen name `tables`,
`config`, `blocks`, `routing` or `load_lib` as a definition that differs.
The 19th is the rewritten case, which stands for no old case. Those are
the changes `20a9460fa` made.

**The cases and seconds before and after** (executed: `bin/test <file> -q
-p no:xdist`, one run each, at `9b6c36cf0` in a worktree since removed, and
at `7a2c58b2c`).

| File | At `9b6c36cf0` | At `7a2c58b2c` |
|---|---|---|
| `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py` | 453 in 1.78 s | 3 in 0.01 s |
| `tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py` | 118 in 5.14 s | 113 in 0.11 s |
| `tests/lib/test_tables.py` | 122 in 0.22 s | 573 in 3.08 s |
| `tests/lib/test_blocks.py` | 15 in 0.05 s | 17 in 1.76 s |
| `tests/lib/test_routing.py` | 48 in 3.99 s | 50 in 1.95 s |

There were 756 items before and 756 after. No moved case runs git, so no
real-git case was kept. No case was cut.

**The pair the move makes, design *Scope* item 11.** `bin/seal layout
--pairs` gave `138 files read, 42 pairs` at `9b6c36cf0` and `138 files
read, 43 pairs` at `7a2c58b2c` (executed). The one new line is
`tests/lib/test_tables.py::Test_gfm_table:
test_an_indented_table_with_no_list_above_is_read and
test_a_list_marker_in_indented_code_is_no_list_item have equal bodies once
names and strings are normalised`. `Test_gfm_table`'s docstring now states
the input the two differ by: the lines above the indented header.

**S6 and S7, and the citations, design *Scope* items 9 and 10**
(executed at `7a2c58b2c`). `bin/seal rules --check` exits 0. Its last line
is `seal rules: all 177 check lines in 69 rule files hold.`
`bin/seal layout --check` exits 0, and its last line is `138 files read, 0
refused, 77 declare no TARGET`. That count is phase 2's, because this phase
deleted no file and declared no `TARGET`. No check line names either old
file. `git grep -l -w` outside `seal/threads/` and `CHANGELOG.md` on each
moved case's name lists only its new file. `git grep -l -w` on each moved
helper's name lists only its new file and files that define the same word
for themselves. That second group is `KINDS`, `CLAUSE`, `vocabulary`,
`disagreement`, `disagreements`, `CORPUS`, `ALPHABET`, `CORPUS_SIZE` and
`FOUND`, each read in its file. `git grep` on the two old files' stems
found eight citations, all prose. Five were re-pointed:
`lib/blocks.py:76`, `lib/routing.py:106`, `lib/tables.py:146` and `:243`,
and `tests/block_shapes.py:7`. The docstrings of the five test files now
say what each holds and where the moved cases stand. The citations in
`tests/commonmark_oracle.py:10` and `tests/gfm_table_oracle.py:10` still
hold, since each oracle's import case stayed. The two comments that cite
`test_the_walk_is_exact_somewhere` in the readers' corpus now stand in the
same file as that case.

**How the move was made.** A script under the phase's scratch directory
cut each case and helper by its line range. It checked that each range
parsed to the one definition it named, added `self`, and indented it into
its class. Every anchor it used asserted one match (contract rule 9). Then
`ruff check --select I --fix` sorted the imports and `ruff format`
re-indented. The move check above compared every case.

**The phase boundary, as one command** (executed at `7a2c58b2c`, before
these records were written):

```
bin/test tests/text tests/behaviour tests/lib tests/test_conftest.py tests/test_censuses.py tests/github/test_finding_counts.py tests/github/test_rules.py tests/skills/test_chain_check.py tests/skills/test_fold_check.py tests/skills/test_payload_meter.py tests/skills/test_seal.py tests/skills/test_settle.py tests/skills/test_unverified_check.py tests/skills/test_test_layout.py -q
```

It gave `3847 passed, 8 skipped` and exited 0 (S9). The set follows design
*The narrow run*. It holds `tests/text` and `tests/behaviour`, where the 77
files that declare no `TARGET` stand, and the check run, the census sweep
and `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` among
them. It holds `tests/lib` whole, for the three destination files and the
three modules whose docstrings changed. It holds each test file outside
those directories that names a changed path's name at `9b6c36cf0`
(executed: `git grep -l` over `tests/` and `evals/`). The three warnings are
pending corrections of other work items, which
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` reports. The
suite beyond the set is `unverified`, and the orchestrator's broad gate
answers it.
