# Phase 6: 1794396808-test-files-declare-no-target

## What this phase found

**The frame holds for the range, and six of its rows do not hold at
`fa911da9c`.** The phase started at `1e499c64d`. Its range is the 28
files of design *The files* from
`tests/behaviour/test_a_body_naming_two_issues_claims_one.py` to
`tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`. The
same 28 stood at `1e499c64d` (executed: `ls tests/behaviour`). The
design's script of *The cases #1488 read* ran over `tests/text/` and
`tests/behaviour/` written from `18a7e18fb` with `git show`, and printed
341 lines (executed). The 28 files held 212 cases at `1e499c64d`. Of
these, 62 carry a printed name and 150 do not, and no case without a
printed name has the body of a printed case of its file at `18a7e18fb`
(executed: `ast` over each file at both commits). Every one of the 212
cases was read whole. That covers the 150 cases *Scope* item 4 rules, and
the printed case #1488's *Out* left unruled:
`test_the_workflow_fires_on_the_tag_and_writes_one_release_one_asset_one_edit`
of `test_a_release_publishes_its_note.py`, which phase 2's record names.

The six rows that do not hold, each against design *The kinds*:

| File | The row says | At `fa911da9c` | Why |
|---|---|---|---|
| `test_a_body_naming_two_issues_claims_one.py` | T2 | D, `TARGET = ".github/workflows/hygiene.yml"` | The ruling removed the one case that read `templates/setup/hygiene.yml`, so both cases left read the hygiene workflow alone. The first also asks whether `.github/scripts/issue_claims_check.py` exists, which reads no file's text. |
| `test_a_release_publishes_its_note.py` | T2 | D, `TARGET = ".github/workflows/publish-release.yml"` | Phase 5 moved the checklist case out, and both cases left read the workflow alone. |
| `test_a_release_is_sized_by_a_criterion.py` | D on `docs/releasing/issues-and-milestones.md` | deleted | Its one case held three clauses of wording and nothing else, so the ruling removed it and *Scope* item 8 deleted the file. |
| `test_one_heading_rule_holds_to_commonmark.py` | T3 | T1 | Both cases list every tracked `.md` file through `git ls-files` and read it against `tests/commonmark_oracle.py`. That is a walk of the tree, not a property held across several shipped modules. |
| `test_one_table_walker_reads_what_gfm_renders.py` | M, with the case left "T3" | a reason line naming the oracle | The three cases left read or call `tests/gfm_table_oracle.py` alone. That module is not shipped, so they are not M. They run its code, so they are not D. One module is not the several shipped modules T3 names. The reason line states that ground: the oracle is a helper of the suite that ships nothing and has no module file. *The kinds* names no kind for a case of a helper under `tests/`. The hand-back names this for the framer. |
| `test_a_section_marked_for_one_role_reaches_only_that_role.py` | T1 | T1, ruled as it stands at `1e499c64d` | The row holds. The file is named here because #1484 rewrites two comments and a docstring in it. This phase added only the reason line, and left untouched every sentence that cites `payload_meter.py#heading_starts` (plan *Overlap with the release*). |

No case of the range is kind M, and phases 3 to 5 left no M case
(read: `trail/phases/phase-3.md` to `phase-5.md`, and each case of the
range). So *Scope* items 5 and 11 apply to no case here. No case moved,
`bin/seal layout --moved` has nothing to compare, and no pair was made.

**The order the design states.** `d0ed5f84d` commits the rulings alone.
`fa911da9c` then gives each file its `TARGET` or its reason line, so the
filing commit changes no assert.

**What the rulings did, file by file.** Each row gives the cases #1488
did not read whole, out of the file's cases at `1e499c64d`. Each assert
a row does not name as removed or changed was kept as it stood. Each
kept assert carries a comment above it that names the fact it holds and
who reads it. The rulings follow #1488's `frame/design.md` *What an
assert reads* and *The criterion*. A file not in the table had no ruled
case changed: `test_a_cited_section_stands_in_its_file.py`,
`test_a_document_that_names_a_script_says_how_to_reach_it.py`,
`test_a_probe_that_commits_says_so.py`,
`test_a_reference_root_is_read_and_never_taken.py`,
`test_a_release_rolls_the_flow_measurement_issue.py` (its two asserts got
comments in `fa911da9c`),
`test_a_section_marked_for_one_role_reaches_only_that_role.py`,
`test_a_shrunken_corpus_declines_to_judge.py`,
`test_a_test_file_takes_the_root_from_the_conftest.py`,
`test_both_editions_carry_the_same_folds.py`, `test_docs_line_wrap.py`,
`test_evals_layout.py`, `test_every_entry_point_runs_at_the_floor.py`,
`test_every_reader_ends_a_line_where_gfm_does.py`,
`test_every_shipped_agent_and_document_is_measured.py`,
`test_every_tracked_file_meets_every_census.py`,
`test_no_document_names_the_old_roots.py` and
`test_one_heading_rule_holds_to_commonmark.py`.

| File | Unread of all | Removed | Kept with a change |
|---|---|---|---|
| `test_a_body_naming_two_issues_claims_one.py` | 1 of 3 | `test_the_check_does_not_travel_to_user_repositories`: an absence on `templates/setup/hygiene.yml` that no rule of that template states | none |
| `test_a_commit_names_its_repository.py` | 2 of 5 | `test_no_reason_rests_on_a_gate_reading_the_command`: absences of the rule's removed reasons | none |
| `test_a_declared_label_reaches_the_tracker.py` | 2 of 3 | two clauses of A12, the judgment's timing and the backlog sweep, both wording | the third clause cut to the workflow's path and `` `size: now` ``, as `.github/scripts/close_issues_on_release.py#SPENT_ON_CLOSE` spells it, in a case renamed `test_the_document_names_what_spends_the_label` |
| `test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` | 1 of 3 | "process group", "Windows" and the baseline's sentence, all wording; "300 seconds", which `test_the_default_bound_is_the_one_both_documents_state` already holds in the same file | the command line, the verdicts with their exit codes, `PYTHONDONTWRITEBYTECODE` and `` `no baseline` `` each got a comment, in a case renamed `test_the_verify_skill_says_what_each_verdict_means` |
| `test_a_phase_hands_the_next_one_a_record.py` | 3 of 9 | the template's no-table absence, which no rule of the template states | comments above the title, the heading and the placeholder asserts |
| `test_a_release_is_sized_by_a_criterion.py` | 1 of 1 | its one case, three clauses of wording; the file | none |
| `test_a_release_publishes_its_note.py` | 0 of 2, and the case #1488 left *Out* | the `apt-get` and the JUnit absences, which no rule of the workflow states | the `github.ref_name` absence, with a comment citing the workflow's comment above `publish`'s `outputs`, which says the tag is read from the tag step alone |
| `test_a_signer_declares_its_pact.py` | 3 of 4 | the routing step's sentences of wording | `` `date +%s` ``, `` `git -C` ``, the `Pact signers` key and `separated by` `;`, the last two read from `lib/config.py#SIGNERS_KEY` and `lib/config.py#PACT_SEPARATOR`, in a case renamed `test_the_routing_step_mints_one_id_and_declares_the_signers` |
| `test_chain_hooks_hardening.py` | 18 of 28 | `test_the_policy_says_a_failed_diff_asks` and its one helper `_folded`, wording; `test_user_invoked_skills_do_not_carry_trigger_scaffolding`, an absence with no rule of that text; `COUNT_WORD` and the count absences of the skills row; the `gone` absences of the network case | the skills-row case renamed `test_the_skills_row_lists_the_on_demand_skills`; the network case renamed `test_the_places_that_reach_the_network_are_named`, with each README's sentence kept to locate its passage and `CONTRIBUTING.md` cut to `` `README.md` *What runs on your machine* `` |
| `test_first_setup_asks_once.py` | 14 of 31 | `test_no_definition_carries_its_own_copy_of_the_root_rule`, `test_the_rows_that_read_this_repository_do_not_travel` and `test_the_record_no_longer_says_the_checks_would_refuse`, absences with no rule of their text; `test_the_seal_readme_is_the_template_verbatim`, a two-file equality, which #1488's criterion counts as wording; the drain case's copied-row absences | `SESSION_RULE` cut to the local root's path in its code span; `DERIVED` cut to the three paths in their code spans; `LOCAL_LIMIT` cut to its two citations, asserted in the paragraph under the table; the way-back case cut to its two commands and its citation; the drain case renamed `test_the_seal_readme_points_at_the_drain`; comments above the parity question, which the orchestrator puts to the person word for word, and above the layout-section order |
| `test_one_table_walker_reads_what_gfm_renders.py` | 3 of 3 | none | the oracle's absences, with a comment citing `tests/gfm_table_oracle.py` *It shares nothing with what it checks* |

**What the deletion took with it** (*Scope* items 8 and 9). The check
line `check: tests/behaviour/test_a_release_is_sized_by_a_criterion.py`
at `docs/releasing/issues-and-milestones.md:68` named that file alone,
so it went. The document has no Korean edition. No unsettled design's
operation holds the line (executed: `git grep` on the file's name over
each `frame/design.md` under `seal/threads/`). The docstring of
`tests/text/test_the_release_tail_does_not_end_at_the_tag.py` cited the
file as the reader it shares, and that clause went. The docstring of
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`,
phase 7's, said `test_first_setup_asks_once.py` pins that `seal/README.md`
equals its template. That case is removed, so the sentence now says the
README is written from the template (contract rule 19).

**The filing.** The three D files declare `TARGET` first after their
imports and end with `test_census = census_case(TARGET)`. Each constant
that stated the same path derives from it through `TARGET.split("/")`.
The 24 other files carry one `# No TARGET: ` line in its place. Three
of the lines as first written did not name what their cases read, and
were corrected before `fa911da9c`. The heading rule's line now names its
walk of the tracked `.md` files. The splitter's names its two modules.
The floor's names the files its cases read.

**Item 10, the docstrings.** The roll's file no longer says its cases
wait for #923, and it says `docs/releasing/issues-and-milestones.md`
names it on one `check:` line, which is the count at `fa911da9c`. The
census sweep no longer calls a module that declares no `TARGET` one not
yet in the layout. The docstrings of every file whose cases changed say
what the file now holds. Six docstrings said where their file's cases
came from, or that a phase moved cases out of the file. They were
`test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`,
`test_a_test_file_takes_the_root_from_the_conftest.py`,
`test_every_entry_point_runs_at_the_floor.py`,
`test_every_shipped_agent_and_document_is_measured.py`,
`test_every_tracked_file_meets_every_census.py` and
`test_one_table_walker_reads_what_gfm_renders.py`. The read of the range
against HEAD after `8496e6664`, the records' first commit, found them, and
`662760c6b` makes each say where those cases stand.

**The rulings shown red** (executed after `d0ed5f84d`, each command
exited 0). Each ran as `bin/seal mutate <file> --replace <old> <new>
--tests "bin/test <module> -q -p no:xdist -x -k <cases>"`. No shipped
unit changed in this phase, so the runs break the fact a kept or changed
assert holds, in the file it reads.

| Fact broken | File | Cases | Verdict |
|---|---|---|---|
| the workflow's path renamed in the spend sentence | `docs/releasing/issues-and-milestones.md` | `test_a_declared_label_reaches_the_tracker.py -k spends_the_label` | red |
| `` `no baseline` `` without its backticks; `red` given exit 1 | `skills/verify/seal-mutate.md` | `test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py -k each_verdict_means` | red, both mutants |
| the title as `# Phase <N> of <work-item-id>` | `templates/records/sdd-phase.md` | `test_a_phase_hands_the_next_one_a_record.py -k title_and_the_found` | red |
| the note step's `TAG` read from `github.ref_name` | `.github/workflows/publish-release.yml` | `test_a_release_publishes_its_note.py -k fires_on_the_tag` | red, at the `github.ref_name` assert |
| `separated by` `;` written as commas | `skills/implement/multi-repository.md` | `test_a_signer_declares_its_pact.py -k declares_the_signers` | red |
| the citation's heading dropped | `CONTRIBUTING.md` | `test_chain_hooks_hardening.py -k reach_the_network` | red |
| the local root's path without its code span | `skills/implement/SKILL.md` | `test_first_setup_asks_once.py -k "session_rule_names_both_places or layout_section"` | red |
| `agents/sealer.md` replaced by words | `README.md` | `test_first_setup_asks_once.py -k leaves_unchecked` | red |
| `seal mode local` without its code span | `skills/config/SKILL.md` | `test_first_setup_asks_once.py -k way_back_before` | red |
| `Makefile` without its code span; the parity question respelt | `skills/implement/bootstrap.md` | `test_first_setup_asks_once.py -k "proposes_candidates or parity_question"` | red, both mutants |
| the drain heading changed in the citation | `templates/setup/seal-README.md` | `test_first_setup_asks_once.py -k points_at_the_drain` | red |
| `sys.path` written into a comment of the oracle's code | `tests/gfm_table_oracle.py` | `test_one_table_walker_reads_what_gfm_renders.py -k nothing_of_this` | red, at the absence loop |

A first oracle run added `import importlib`. It went red at the
`imported_roots` assert, before the absence loop, so it was run again
with the comment above.

**S6 and S7** (executed at `fa911da9c`). `bin/seal rules --check` gives
`all 176 check lines in 69 rule files hold.` and exits 0. `git grep -n`
outside `seal/threads/` and `CHANGELOG.md`, on each removed or renamed
case, on `COUNT_WORD` and `_folded`, and on the deleted file's stem,
lists only two names that contain `_folded` as part of a longer name.
`bin/seal layout --check` exits 0, and its last line is `140 files
read, 0 refused, 72 declare no TARGET`. Against phase 5's `141` and
`76`, the deleted file accounts for one of each, and the three new
`TARGET` lines for the other three. `bin/seal layout --pairs` gives
`140 files read, 43 pairs`, the same pair count as at phase 5.
`git grep -c '^# No TARGET: ' -- tests | wc -l` gives 50.

**The phase boundary, as one command** (executed at `fa911da9c`, before
these records were written). The set follows design *The narrow run*.
It holds the 29 changed test modules. It also holds each module under
`tests/` that named a changed file's name at `1e499c64d` (executed:
`git grep -l` per changed path). With them come the check run, the
census sweep and `tests/github/test_rules.py`:

```
bin/test tests/behaviour/test_a_body_naming_two_issues_claims_one.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_a_commit_names_its_repository.py tests/behaviour/test_a_declared_label_reaches_the_tracker.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py tests/behaviour/test_a_phase_hands_the_next_one_a_record.py tests/behaviour/test_a_probe_that_commits_says_so.py tests/behaviour/test_a_reference_root_is_read_and_never_taken.py tests/behaviour/test_a_release_publishes_its_note.py tests/behaviour/test_a_release_rolls_the_flow_measurement_issue.py tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/behaviour/test_a_signer_declares_its_pact.py tests/behaviour/test_a_test_file_takes_the_root_from_the_conftest.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_evals_layout.py tests/behaviour/test_every_entry_point_runs_at_the_floor.py tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py tests/behaviour/test_every_shipped_agent_and_document_is_measured.py tests/behaviour/test_every_tracked_file_meets_every_census.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_no_document_names_the_old_roots.py tests/behaviour/test_one_heading_rule_holds_to_commonmark.py tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py tests/behaviour/test_release_hygiene.py tests/behaviour/test_the_contributor_has_a_procedure.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_this_repository_passes_its_own_checks.py tests/censuses.py tests/conftest.py tests/gfm_table_oracle.py tests/github/test_close_issues_on_release.py tests/github/test_dist_branch.py tests/github/test_issue_claims_check.py tests/github/test_label_merged_on_release_branch.py tests/github/test_publish_release_note.py tests/github/test_release_completeness_check.py tests/github/test_roll_flow_measurement_issue.py tests/github/test_rules.py tests/github/test_tracker_labels.py tests/hooks/test_core_start.py tests/lib/test_blocks.py tests/lib/test_config.py tests/lib/test_launch.py tests/lib/test_lines.py tests/lib/test_tables.py tests/skills/test_chain_check.py tests/skills/test_fold_check.py tests/skills/test_mutation_check.py tests/skills/test_payload_meter.py tests/skills/test_seal_stamp.py tests/skills/test_seal.py tests/skills/test_settle.py tests/test_censuses.py tests/test_conftest.py tests/text/test_a_cited_commit_outlives_the_squash.py tests/text/test_a_language_section_of_writing_style_opens_alone.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_settle_reads_before_it_removes.py tests/text/test_the_chain_section_has_one_shape.py tests/text/test_the_records_can_be_carried_out_and_in.py tests/text/test_the_release_tail_does_not_end_at_the_tag.py tests/text/test_the_rules_have_one_owner.py -q
```

It gave `3320 passed, 7 skipped` and exited 0 (S9). At `662760c6b`,
which changes six docstrings and no assert, the same command gave
`3320 passed, 7 skipped` and exited 0, and the four counts above came out
the same (all executed). The suite beyond the set is `unverified`, and
the orchestrator's broad gate answers it.
