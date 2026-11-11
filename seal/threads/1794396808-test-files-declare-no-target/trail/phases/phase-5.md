# Phase 5: 1794396808-test-files-declare-no-target

## What this phase found

**The frame holds for where the cases go, and not for which cases go.**
The phase started at `cf4b4943c`. Design *The files* sends cases of
`tests/behaviour/` to module files under `tests/github/`. Phase 3's probe
ran again over the 51 files at `cf4b4943c` (executed: design G7's script).
A `git grep` over `tests/behaviour/` for `.github/scripts`, for
`".github", "scripts"` and for an import from a module file of
`tests/github/` added the cases that load a script by its path (executed).
Each case either search reached was read whole and ruled by design *The
kinds* (`frame/questions.md` Q1). Five are kind M and moved. The rulings
that differ from design *The files* are in the next table.

| File | Design *The files* | Ruled here | Ground |
|---|---|---|---|
| `test_a_release_publishes_its_note.py` (`:180`) | a case calling `publish_release_note` or `dist_branch` alone moves to its module file under `tests/github/` | `test_the_line_the_checklist_copies_is_the_line_the_reader_reads` moves to `tests/github/test_publish_release_note.py::Test_module`; no case calls `dist_branch.py` | `test_the_dist_job_adds_the_release_to_dist_and_goes_red_where_it_cannot` reads the workflow's `dist` job, and names the script only as the command of a step. `test_the_workflow_fires_on_the_tag_and_writes_one_release_one_asset_one_edit`, the case #1488's *Out* names, reads the workflow too and stays for phase 6. |
| `test_the_release_seal_is_drawn.py` (`:207`) | a case calling `run_tests.py` alone moves to `tests/github/test_run_tests.py` | no case moves | `test_the_publishing_workflow_installs_the_pins_the_runner_holds` holds the publishing workflow's install line against the runner's `MARKDOWN_IT`, `CMARKGFM` and `PYYAML`. *The kinds* says a case that holds a document's sentence against a value it takes from a module is not M. |
| `test_the_suite_has_a_command_that_is_cheap_twice.py` (`:213`) | cases calling `run_tests.py` move to `tests/github/test_run_tests.py` | no case moves | Each of the five cases that read `rt` holds `.github/workflows/test.yml`'s install line or matrix, or `CONTRIBUTING.md` *Running the checks*, against the runner's constants. The same sentence of *The kinds* rules them. |

**Three of the moved cases read a document, and each is kind M.**
`test_the_document_that_teaches_the_rule_carries_no_instance_of_it` runs
`issue_claims_check.py#read` over `docs/releasing/issues-and-milestones.md`.
`test_the_slice_document_resolves_every_target` runs `rules.py#render` over
`docs/layout/the-record-layout.md`. `test_the_line_the_checklist_copies_is_the_line_the_reader_reads`
fills the title command of `docs/releasing/release-checklist.md` and runs
`publish_release_note.py#title_from` on it. Each reads the document to
build the call's input, and its asserts read what the call returned, so
*The kinds* makes it M: "A case that reads a document only to build the
call's input is M." The checklist case also asserts that its filled title
lost the placeholders, which holds the input it built. The proofer reads
these three rulings. `test_every_declared_label_says_which_document_specifies_it`
holds each label `tracker_labels.py#declared` returns to the section it
cites, so its subject is the module's declarations, and it is M too.

The other cases the probe and the grep reached give nothing to
`tests/github/`. `test_a_cited_section_stands_in_its_file.py`'s archive
case walks the tracked files (T1).
`test_a_release_rolls_the_flow_measurement_issue.py` holds the document
against the roll's constants (D, as the design starts it).
`test_docs_line_wrap.py` loads `rules.py` to find every rule file it
measures (T1). `test_every_shipped_agent_and_document_is_measured.py::Test_release_report`
lists `agents/` and `docs/` (T1).
`test_release_hygiene.py#test_the_check_lines_rules_did_not_read_reach_the_pull_request`
runs the hygiene step's own shell over `rules.py`, so the step is its
subject. `test_this_repository_passes_its_own_checks.py::Test_seal_rules`
runs the check over the root (T1).
`test_the_windows_leg_runs_in_shards_that_make_the_whole.py` names
`durations_union.py` only as a step's command, and
`test_every_entry_point_runs_at_the_floor.py` holds several modules to one
floor (T3). The claims file's `test_the_body_reaches_the_script_through_the_environment`
and the label file's workflow case read a workflow. Phase 6 or 7 rules each
again where it files its file.

**What moved.** Five cases moved, five collected items.

| From | Case | To |
|---|---|---|
| `tests/behaviour/test_a_body_naming_two_issues_claims_one.py` | `test_the_document_that_teaches_the_rule_carries_no_instance_of_it` | `tests/github/test_issue_claims_check.py::Test_read` |
| `tests/behaviour/test_a_declared_label_reaches_the_tracker.py` | `test_every_declared_label_says_which_document_specifies_it` | `tests/github/test_tracker_labels.py::Test_module`, since `declared` has no class |
| `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py` | `test_s5_rules_check_excuses_a_section_a_design_under_agentic_seal_removes` | `tests/github/test_rules.py::Test_main` |
| `tests/behaviour/test_a_release_publishes_its_note.py` | `test_the_line_the_checklist_copies_is_the_line_the_reader_reads` | `tests/github/test_publish_release_note.py::Test_module`, since `title_from` has no class |
| `tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py` | `test_the_slice_document_resolves_every_target` | `tests/github/test_rules.py::Test_module`, since `render` has no class |

`OWNER` moved with the label case to `tests/github/test_tracker_labels.py`,
and the label file imports it by name, since its document case still reads
it. `tests/github/test_rules.py` now imports `ITEM` and `write` from
`tests/conftest.py` and `configured` from `tests/skills/test_seal.py`, as
the foreign file did. `tests/github/test_publish_release_note.py` already
bound `SCRIPTS`, `SCRIPT`, `VERSION`, `TAG`, `SYMPTOMS` and `module` as the
publish file did, so the publish file's copies went with the case. Each old
file dropped the imports it no longer reads.

**The deleted file.** `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py`
held no case after the move, and is deleted (design *Scope* item 8). No
check line names it (executed: `git grep` outside `seal/threads/` and
`CHANGELOG.md`). The comment above the world in `tests/conftest.py` named
its `seal rules` case and now names `tests/github/test_rules.py`.

**Departure: the bindings were aligned before the move, and one case was
rewritten.** The foreign file imported `tests/github/test_rules.py`'s
`HELD`, `TESTS`, `doc`, `rule` and `rules` under the aliases `RULES_HELD`,
`RULES_TESTS`, `rules_doc`, `rules_rule` and `RULES`. `81ec9ed53` made it
import them by their own names, and its case passed there (executed).
`CONTRIBUTING.md` *The test layout* asks for one line per old case
rewritten.

- `test_s5_rules_check_excuses_a_section_a_design_under_agentic_seal_removes`
  guarded that `seal rules --check` excuses a refused `check:` line in a
  section a design under `agentic-seal/threads/` removes, and names that
  design by its path under the root. It holds that now in
  `tests/github/test_rules.py::Test_main`, reading the same five names
  unaliased.

**The criterion, design *Scope* item 4.** Phase 3's output of design *The
cases #1488 read* prints two of the five moving cases: the foreign file's
`seal rules` case and the checklist case (executed then, read now). The
other three were read whole here:
`test_the_document_that_teaches_the_rule_carries_no_instance_of_it`,
`test_every_declared_label_says_which_document_specifies_it` and
`test_the_slice_document_resolves_every_target`. None stands in #1488's
*Out*, which names only the publish file's workflow case
(`seal/threads/1794383427-asserts-pin-literal-phrases/frame/design.md:45`,
read). Four of the five files changed after `18a7e18fb` (executed: `git
diff --stat`), so all five cases were read as they stand at `cf4b4943c`.
One assert of the three reads a file of the tree as text. The label case
holds each label's cited heading against the headings of the document it
names. That is a citation a reader resolves, a kind *The criterion* keeps.
`d6452da93` keeps it and extends the comment above it to name who reads
it, before the move. Every other assert of the three reads what
`read`, `declared` or `render` returned, which #1488's *What an assert
reads* puts outside *The criterion*.

**The move check, design *Scope* item 5** (executed, one run for
`tests/github/`, before `21dbe042e` was committed, over the tree it holds):

```
bin/seal layout --moved 81ec9ed53 --from tests/behaviour/test_a_body_naming_two_issues_claims_one.py tests/behaviour/test_a_declared_label_reaches_the_tracker.py tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py tests/behaviour/test_a_release_publishes_its_note.py tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py tests/github/test_issue_claims_check.py tests/github/test_tracker_labels.py tests/github/test_publish_release_note.py tests/github/test_rules.py --to tests/behaviour/test_a_body_naming_two_issues_claims_one.py tests/behaviour/test_a_declared_label_reaches_the_tracker.py tests/behaviour/test_a_release_publishes_its_note.py tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py tests/github/test_issue_claims_check.py tests/github/test_tracker_labels.py tests/github/test_publish_release_note.py tests/github/test_rules.py
seal layout: moved: 120 old cases, 200 items against 200 at 81ec9ed53ce0, 0 failed
```

It exited 0, so no module carries a mutation table. The four old files that
keep cases stand in both lists, and the deleted one in `--from` alone. The
same command from `d6452da93` exited 1 with 2 failures (executed). They
name the rewritten case once as not found unchanged and once as standing
for no old case. That is the change `81ec9ed53` made.

**The cases and seconds before and after** (executed: `bin/test <file> -q
-p no:xdist`, one run each, at `cf4b4943c` and at `21dbe042e`).

| File | At `cf4b4943c` | At `21dbe042e` |
|---|---|---|
| `tests/behaviour/test_a_body_naming_two_issues_claims_one.py` | 4 in 0.02 s | 3 in 0.02 s |
| `tests/behaviour/test_a_declared_label_reaches_the_tracker.py` | 7 in 0.02 s | 6 in 0.02 s |
| `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py` | 1 in 0.94 s | deleted |
| `tests/behaviour/test_a_release_publishes_its_note.py` | 3 in 0.03 s | 2 in 0.02 s |
| `tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py` | 3 in 0.14 s | 2 in 0.01 s |
| `tests/github/test_issue_claims_check.py` | 58 in 0.07 s | 59 in 0.05 s |
| `tests/github/test_tracker_labels.py` | 8 in 0.03 s | 9 in 0.03 s |
| `tests/github/test_publish_release_note.py` | 53 in 4.04 s | 54 in 2.66 s |
| `tests/github/test_rules.py` | 67 in 1.28 s | 69 in 1.53 s |

The nine files held 204 items before and the eight hold 204 after. Each
figure is one run, so the seconds are no finding. One real-git case is
kept: `test_s5_rules_check_excuses_a_section_a_design_under_agentic_seal_removes`
builds `tests/conftest.py`'s `shared` repository, because it holds what
`seal rules --check` reads from a root that git tracks at `agentic-seal/`.
No case was cut.

**No unit adds behaviour, so no `seal mutate` ran.** Every case moved with
its body unchanged, `81ec9ed53` renamed the names one case reads, and
`d6452da93` changed a comment. `skills/verify/SKILL.md` *The narrow command
still has to be able to fail* gives a move no run, and the move check and
the boundary run below stand for it.

**The pairs, design *Scope* item 11.** `bin/seal layout --pairs` gave `142
files read, 43 pairs` at `cf4b4943c` and `141 files read, 43 pairs` at
`21dbe042e`, and the two lists differ in that count line alone (executed:
`diff`). The move makes no pair, so no class docstring owes a reason.

**S6 and S7, and the citations, design *Scope* items 9 and 10**
(executed at `21dbe042e`). `bin/seal rules --check` exits 0, and its last
line is `seal rules: all 177 check lines in 69 rule files hold.`
`bin/seal layout --check` exits 0, and its last line is `141 files read, 0
refused, 76 declare no TARGET`. Against phase 4's `142` and `77`, the
deleted file accounts for one of each. `git grep -n -w` outside
`seal/threads/` and `CHANGELOG.md` on each moved case's name lists only
its new file, and on the deleted file's stem lists nothing. `OWNER` is
defined in `tests/github/test_tracker_labels.py` and in
`tests/behaviour/test_a_release_is_sized_by_a_criterion.py`, which binds
the same path for itself. `git grep` on the four other old files' stems
found these citations:

- `docs/releasing/issues-and-milestones.md:293` names the claims file and
  `tests/github/test_issue_claims_check.py`, and
  `docs/releasing/branch-and-release.md:138` names the publish file and
  `tests/github/test_publish_release_note.py`. Each line already names the
  moved case's new file, and each old file still holds a case of that
  rule's workflow, so both lines stand.
- `tests/behaviour/test_docs_line_wrap.py:324` writes the rules-command
  file's path into a fixture as a wide target. It reads no file there and
  stands.
- The docstrings of `tests/github/test_issue_claims_check.py`,
  `test_publish_release_note.py` and `test_rules.py` said which cases
  their old file keeps, and each now names what it keeps. The one of
  `test_rules.py` gained a sentence on the `shared` repository its moved
  case builds, as phase 4 wrote in the files of `tests/skills/`. Those of
  `test_tracker_labels.py`, `test_close_issues_on_release.py` and
  `test_label_merged_on_release_branch.py` still hold, and stand.
- The four old files' docstrings no longer say their cases wait for #923.
  Each says what it holds and where its moved case stands.

**Overlap with #1484.** `refactor/1484-payload-calibration-reached-by-tests-alone`
changes `tests/github/test_release_report.py` and one file of
`tests/behaviour/` that this phase did not touch (executed: `git diff
--stat` from its merge base). No file of this phase is among them.

**The phase boundary, as one command** (executed at `21dbe042e`, before
these records were written):

```
bin/test tests/text tests/behaviour tests/github/test_issue_claims_check.py tests/github/test_tracker_labels.py tests/github/test_publish_release_note.py tests/github/test_rules.py tests/github/test_close_issues_on_release.py tests/github/test_label_merged_on_release_branch.py tests/test_conftest.py -q
```

It gave `1565 passed, 8 skipped` and exited 0 (S9). The set follows design
*The narrow run*. It holds `tests/text` and `tests/behaviour`, where the 76
files that declare no `TARGET` stand, and the check run and
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` among them.
It holds the four destination files. It holds each test file outside
those directories that names a changed file's stem at `cf4b4943c`
(executed: `git grep -l -w` over `tests/` and `evals/`), and
`tests/test_conftest.py`, since `tests/conftest.py` changed a comment. The
three warnings are pending corrections of other work items, which
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` reports. The
suite beyond the set is `unverified`, and the orchestrator's broad gate
answers it.
