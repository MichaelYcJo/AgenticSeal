# Phase 9: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## What this phase found

### The frame, read against the tree before the build

The frame holds for `tests/skills/test_chain_check.py` at `dacef7f4b`, with one fact it does not state. The 99 cases *Scope* item 11 takes are the cases of run 45203717820's artifact over 0.5 s (executed: the list in this session's scratchpad, `1581-dispatch-2/`, 99 lines). Every one of them stands in the module at `dacef7f4b` under its name (executed: `bin/test --collect-only` over the file at `dacef7f4b`, copied to `tests/skills/test_tmp_chain_check_base.py` and removed after the run). The readers item 11 names stand where it says: `retired` at `skills/code-review/scripts/chain_check.py:2096`, `settled` at `:2063`, `root_name` at `:1842` and `declared_for_this_branch` at `:1887` (read). The phase changes no shipped file.

The fact the frame does not state: five of `Test_retired`'s eight cases have no fact in `retired`. `test_accepts_every_declaration_leaving_with_the_root`, `test_a_root_that_left_for_a_local_root_says_the_check_judged_nothing`, `test_accepts_under_worktree_a_root_the_working_tree_no_longer_has`, `test_judges_a_root_the_working_tree_has_under_worktree` and `test_judges_the_declarations_where_the_working_tree_has_seal_as_a_file` each judge whether the root's entry is gone, which `_checked` decides inline with `git ls-tree HEAD -- <home>`, or `os.path.lexists` under `--worktree` (read: `chain_check.py:2177` to `:2180`). No reader holds that test but `main`, so these cases keep a `main` run (*Departures from the frame*).

### Q1: where the module's seconds went before the rebuild

**On the Windows leg.** `frame/design.md`'s table of runs puts the module at 262 s and 245 s in its two newest columns (read), 245 s being run 45235848444 at `dacef7f4b`, the commit this phase built on. The artifact the spawn names, `1581-dispatch-6/.test_durations`, sums the module to 261.6 s over 252 cases, and `1581-dispatch-7/.test_durations` to 245.0 s (executed: the sum by case). In run 45203717820 the 99 listed cases cost 226 s of 240 s (`frame/plan.md` *Judgments of the run*).

**On this macOS machine.** `bin/test tests/skills/test_chain_check.py -q -p no:xdist --durations=0` at `dacef7f4b` passed 252 cases in 45.36 s, 4.14 s of it in setup and 40.25 s in calls (executed). Phase 8's `tmp_spawn_probe.py`, copied to this phase's scratch, counted 3,229 processes started in the test process. The 99 listed cases started 3,045 of them (executed). By class: `Test_main` 1,039, `Test_rule_changes_read` 607, `Test_retired` 324, `Test_body` 275, `Test_originals_of` 203, `Test_pins_and_copies_in` 148, `Test_routing_trailers` 144 and `Test_guarantee` 140.

One run of `main` over the module's branch, every reader real, started 41 git processes (executed: a probe that recorded the caller of each process, removed after the run). `follows` started 14 of them: the broad gate arm, the guarantee arm and the records arm each ask it, and it starts a `rev-parse`, a `merge-base --is-ancestor`, a `rev-list` and one `diff-tree` per later commit. `read_record` started 8 `git show`, `root_name` 4 more, through `read_record` and the merge base's `show`, and `tracked_declarations` 3. The rest were the top, the baseline, the diff, the merge base, the root's entry, the trailers, the tree the rule-changes arm lists, the current branch and a fixed commit's ancestry, one each. A case commonly ran `main` two or three times, after commits through the working tree at three processes each, and `reviewed_to_head` or `seal` added a round and closing records after each change, seven more.

Seven listed cases start six processes or fewer of their own: their seconds in run 45203717820 were a module-scoped template's build, charged to the first case a worker ran (`frame/design.md` G5). They are `Test_rule_changes_read::test_refuses_a_section_the_parser_refuses_at_its_line[S2-prose-under-items]` and `test_names_a_near_heading_as_not_read_and_passes`, `Test_originals_of::test_refuses_a_direct_guarantee_whose_only_original_is_misspelt` and `test_a_direct_guarantee_owes_nothing_for_the_document_roots_alone`, `Test_guarantee::test_an_opener_quoted_in_a_code_span_hides_no_verdict`, `Test_follows::test_accepts_head_and_record_commits_after_it` and `test_census` (executed: their process counts, 0 to 6, against 0.2 s to 2.2 s in run 45203717820).

### What the rebuild changed

`457799c55` does the rebuild. `191d0f78e` drops a branch of `imported` no case took, a commit of none that only moved a ref, and reflows two of its docstrings; the figures and the mutation table below are `457799c55`'s, and the module passes at `191d0f78e` with the same 253 cases (executed).

- **The three templates are written by `git fast-import`.** `imported` writes a list of commits in one process and returns their ids; `born` makes the repository with its identity written into `.git/config`. `_branch_template` takes three imports, since each record names a commit the one before wrote; `_item_template` two; `_bodied_template` three, with its early body composed between them. `remove_an_earlier_item` writes its three commits, the merge among them, in one import, where it took eleven processes.
- **`_branch_template` carries the root's marker.** `seal/README.md` on `main` opens with `lib/optin.py#MARKER`, as a root first setup leaves does. Without it, `root_name` found no root at HEAD and asked the merge base twice more on every run.
- **A `main` run whose fact is an arm's reading answers three readers.** `answered` replaces `read_record` with a read of the working tree, `tracked_files` with `worktree_files`, and `follows` with an answer that nothing follows. A name in `real` stays the reader's own: the two cases whose fact is a stale run or a guarantee behind HEAD keep `follows`. The top, the baseline, the diff, the merge base, the root's entry, the trailers, the tree the rule-changes arm lists, the current branch, `carried_by` and a fixed commit's ancestry stay git's. One run then starts 12 processes where it started 41 (executed, the same probe). A case no longer adds a round at HEAD or new closing records after its change, since nothing asks git what follows: `reviewed_to_head`, `planted_spec` and `migrating` went from these cases, the last two from the module.
- **The cases of the root's name call its reader.** `root_name` is handed HEAD and the merge base as texts (`test_s3_the_root_is_named_agentic_seal_beside_the_package`, three instances). `declared_for_this_branch` is called with its readers answered for the sentence that names `agentic-seal/threads/`, and over the `repo` world for three sentences `run_check` read. `originals_of` and `edited_work_items` take the paths a pull request under `agentic-seal/` changes.
- **`Test_retired`'s cases about what `retired` reads call it.** `gone_whole` replaces `settled` and records what `retired` hands it. One `main` run over a real removed history stays, every reader real, and a second, `test_refuses_a_deleted_declaration_whose_directory_stays_by_name`, prints the deletion's refusal over the module's branch with its readers answered.
- **The census.** After the rebuild the cases start 1,675 processes (executed, the same probe). By kind of test function, read from each body: 32 run `main` with `answered`, 736 processes; 12 run `main` with every reader real, the ten instances of `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line` among them, 396; the other 163 run no `main`, 543.

### Departures from the frame

- **`answered` replaces `main`'s readers, not git.** *Scope* item 11 names the seams of items 2 and 3: an arm called with its input given, or `read_record` and `git` replaced for the case. `answered` replaces `read_record`, `tracked_files` and `follows` for a whole `main` run, so that `main` still hands each arm what it reads and reads its answer. Phase 7's `arms_answered` and phase 8's `answered` did the same one level up (`trail/phases/phase-7.md`, `trail/phases/phase-8.md`, *Departures from the frame*), and `frame/plan.md` A4 bars only a fake of git's output. Each answered reader keeps cases over a real history: `follows` in `Test_follows`, `Test_broad_gate::test_lets_the_records_follow_the_run_and_refuses_any_other_path`, `Test_main::test_refuses_a_code_commit_after_the_last_record` and `test_refuses_a_broad_gate_file_naming_another_commit`; `read_record` and `tracked_files` in every `main` run kept real, and in `Test_main::test_names_a_record_under_another_name_and_keeps_the_exit`.
- **Five `Test_retired` cases keep a `main` run, with readers answered.** *Scope* item 11 has `Test_retired`'s other cases call `retired`. Their fact is the root's entry, which `_checked` reads inline, so no call to `retired` holds it (*The frame, read against the tree*). They run `main` with `answered`; the root's entry, `settled` and the merge base stay git's.
- **Two cases became one, and one became two.** `Test_declared_for_this_branch::test_accepts_a_shared_root_and_tells_it_to_add_the_file` asserted that the sentence names the file to add and no local mode. `test_the_shared_sentence_says_what_it_searched_and_for_what` reads the same `why` over the same world, so it holds both assertions now. `Test_retired::test_refuses_a_declaration_deleted_beside_a_directory_that_stays` became the call to `retired` and the `main` run over the module's branch that prints the refusal, since no other case read that refusal's words.
- **The package's world went from three cases.** `test_s3_the_pull_request_that_adds_agentic_seal_is_judged_under_it` took `tests/conftest.py#package`, and its two instances are now two of `root_name`'s three. No case of the module takes `package` now.

### The four parts `CONTRIBUTING.md` *The test layout* asks of a rebuilt module

**1. The move check, and the mutation table.**

`bin/seal layout --moved dacef7f4b --from tests/skills/test_chain_check.py --to tests/skills/test_chain_check.py` exits 1 at `191d0f78e` (executed). Its last line reads `seal layout: moved: 206 old cases, 252 items against 251 at dacef7f4baf5, 178 failed`. Most of the 178 find a template or a helper they use changed under them, `_branch_template`, `_item_template`, `_bodied_template` and `put_spec` among them. So the mutation table carries part 1. The module's table is phase 2's 57 mutants (`trail/phases/phase-2.md`, its first part), phase 3's 85 (`trail/phases/phase-3.md`, its first part) and the 20 below.

Phase 2's 57 mutants and phase 3's 85 ran again against `457799c55`, each set in one call (executed): `bin/seal mutate skills/code-review/scripts/chain_check.py --replace OLD NEW ... --tests "bin/test tests/skills/test_chain_check.py -q -x"`, built by each phase's `run_mutants.py` from its `mutants.py`. They printed `seal mutate: 57 mutants, 56 red, 1 SURVIVED, 0 with no verdict (281.3s)` and `seal mutate: 85 mutants, 75 red, 10 SURVIVED, 0 with no verdict (507.8s)`. Each mutant red at phase 2 and phase 3 is red again. The survivors are the same: phase 2's 8, and phase 3's 1, 7, 9, 10, 12, 16, 39, 43, 52 and 70, each of which survived the test file before phase 2 too (`trail/phases/phase-3.md`, the first of its four parts, says why each lives). So the rebuild lost no fact that killed a mutant, and no survivor is re-run against the base here.

The phase adds 20 mutants at the readers the new unit calls reach and at the lines of `_checked` that hand them their input, which `answered` leaves running. They ran in one call against `457799c55` with the same `--tests` (executed: `run_mutants.py` and `mutants.py` in this phase's scratch, which hold each OLD and NEW). It printed `seal mutate: 20 mutants, 19 red, 1 SURVIVED, 0 with no verdict (147.0s)`.

| # | Unit | Mutant | `457799c55` |
|---|---|---|---|
| 1 | `root_name` | the merge base never asked where HEAD has no root | red |
| 2 | `root_name` | the name always `seal` | red |
| 3 | `edited_work_items` | a design at any depth under the work items taken | red |
| 4 | `edited_work_items` | a moved design taken | red |
| 5 | `edited_work_items` | a design another pull request's squash carried taken | red |
| 6 | `retired` | a directory the disk still holds handed to `settled` | red |
| 7 | `retired` | a declaration HEAD carries handed to `settled` | red |
| 8 | `declared_for_this_branch` | `{routing.FILENAME}` spelt `routing.md` in the sentence | SURVIVED |
| 9 | `declared_for_this_branch` | the searched directory spelt `seal/threads/` whatever the root | red |
| 10 | `declared_for_this_branch` | the local root never named | red |
| 11 | `originals_of` | the document roots read as `seal` whatever the root | red |
| 12 | `_checked` | the root's entry never gone at HEAD | red |
| 13 | `_checked` | the root's entry never gone under `--worktree` | red |
| 14 | `_checked` | no declaration read as carried by a squash | red |
| 15 | `_checked` | no removed declaration read as a settle | red |
| 16 | `_checked` | `retired` handed no merge base | red |
| 17 | `_checked` | `originals_of` handed `seal` for the root's name | red |
| 18 | `_checked` | the work items read under `seal/` whatever the root | red |
| 19 | `_checked` | `root_name` handed no merge base | red |
| 20 | `_checked` | no root read as local | red |

Mutant 8 is equivalent: `routing.FILENAME` is `routing.md` (read: `lib/routing.py`), so the sentence reads the same. Every shipped file a run touched is back at HEAD, and no `test_tmp_*` file stands under `tests/` (executed: `git status --short` names neither).

**2. Cases and seconds, before and after, on this macOS machine.** The figures are local. `frame/design.md` *Grounding*, *What a figure of the Windows leg can show*, takes no local figure as evidence of a saving on the Windows leg.

| | `dacef7f4b` | `457799c55` |
|---|---|---|
| Cases passed | 252 | 253 |
| `bin/test tests/skills/test_chain_check.py -q -p no:xdist --durations=0` | 45.36 s (setup 4.14 s, call 40.25 s) | 26.28 s (setup 2.92 s, call 22.41 s) |
| Processes the cases start in the test process, counted by `tmp_spawn_probe.py` under `-p no:xdist` | 3,229 | 1,675 |
| Of them, in `Test_main`, `Test_rule_changes_read`, `Test_retired`, `Test_body` | 1,039, 607, 324, 275 | 486, 216, 177, 201 |

Under `-n auto`, `bin/test tests/skills/test_chain_check.py -q` passed 253 cases in 7.42 s at `457799c55` (executed).

**Q2: the floor.** The phase states no floor for this module, since no local figure is evidence of the Windows leg; the orchestrator's run at this phase's Status commit answers it (`frame/design.md` S1). The estimate points above 60 s. Run 45235848444's 245 s over the 3,229 processes counted at the same commit is 0.076 s a process; at that rate the 1,675 left would read about 127 s (executed: the division; an estimate with no constant per case, as phase 8's). Where the processes stand: 396 in the twelve test functions that run `main` with every reader real, 736 in the 32 that run it with `answered`, and 543 in the cases that run no `main`, most of them the readers that ask git over a real history and the bodied cases, whose `seal pr-body` composition reads the seal at HEAD through git. A run with `answered` still starts 12 processes, and its case commits at three. Bringing the module under 60 s by this estimate would take answering the readers `answered` leaves real, the diff and the merge base among them, in most of the 32, or fewer kept runs per arm. That is a further narrowing of what item 11 keeps real, and it is the framer's and the orchestrator's to weigh (`frame/questions.md` Q2).

**3. The real-git cases kept.** These cases run git, and each shows that a reader and git agree.

- `main` with every reader real: `Test_main::test_accepts_a_reviewed_branch_on_a_ready_pull_request`, the one run that holds every reader `answered` replaces against git; `Test_rule_changes_read::test_refuses_another_work_items_spec_the_branch_adds_or_changes`, the design `main` hands the arm from git's diff of a branch that edits it; `Test_originals_of::test_refuses_to_run_where_the_parity_readers_will_not_load`; `Test_guarantee::test_names_a_near_opener_and_reads_no_verdict`; `Test_body::test_accepts_the_body_at_a_merge_past_a_later_base_commit`, the mark read against a base given as a SHA at the merge commit CI checks out; `Test_retired::test_accepts_a_declaration_a_settle_removed`, over a real removed history; `Test_main::test_s3_the_check_judges_the_declaration_under_agentic_seal`, over `tests/conftest.py#shared`; `Test_declared_for_this_branch::test_refuses_a_local_declaration_and_says_it_is_local_mode`, over a local root; `Test_routing_trailers`' two runs at a local root and with the commits unreadable; and `Test_main::test_refuses_a_baseline_that_does_not_resolve_with_exit_2`, a ref git does not resolve.
- `main` with `answered`, the reader of the case's fact kept real: `follows` in `Test_main::test_refuses_a_broad_gate_file_naming_another_commit` and `Test_retired::test_judges_a_root_the_working_tree_has_under_worktree`; `carried_by` and the ancestry of a fixed commit in `Test_main::test_accepts_a_release_pull_request_leaving_a_squashed_item_to_its_own` and `Test_rule_changes_read::test_accepts_a_spec_another_pull_requests_squash_carried_unread`; the trailers in `Test_routing_trailers::test_refuses_a_commit_naming_a_work_item_no_declaration_names`; the root's entry in the five `Test_retired` cases and in `Test_main::test_s3_a_pull_request_deleting_agentic_seal_declares_nothing`, two instances.
- `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line`, ten instances: each git read past the bound, which only a real read through `lib/gitcmd.py`'s runner reaches.
- The readers that ask git, each over a real history: `Test_follows`, `Test_changed`, `Test_carried_by`, `Test_merge_base`, `Test_tree_at`, `Test_settled`, `Test_commit_of`, `Test_policy_root`, the trailer cases of `Test_routing_trailers` that call `routing_trailers`, `Test_declared_for_this_branch`'s cases over committed declarations, and the records arm's cases about what a commit touched or descends from.

**4. Each listed case, with what holds its fact now.** The 99 cases of run 45203717820 over 0.5 s, in that run's order. *Before* and *after* are the processes the case starts locally (executed, the probe at `dacef7f4b` and at `457799c55`). A case's assertions are the base's, but where its line says otherwise. "Answered" is a `main` run with `answered`; "kept" is a case that keeps its reading of git, with the agreement it holds.

| Case | Before | After | Verdict |
|---|---|---|---|
| `Test_rule_changes_read::test_accepts_a_spec_another_pull_requests_squash_carried_unread` | 104 | 41 | Answered; `carried_by` and the squash stay git's (part 3). One commit of both specs replaces three commits and a round. |
| `Test_rule_changes_read::test_accepts_a_draft_or_an_unseen_pull_request_with_a_notice` | 140 | 37 | Answered, its three runs; the spec committed once, no closing records after it. |
| `Test_rule_changes_read::test_accepts_a_spec_only_moved_and_a_file_beside_or_below_one` | 66 | 0 | Unit call: `edited_work_items` handed the diff as `changed` gives it, the move's two names in `moved`, `carried_by` answering None. It asserts the one design the branch edits is the one read, where it asserted no line for four directories. `Test_changed` holds the move against git. |
| `Test_carried_by::test_accepts_a_declaration_only_a_squash_merge_touched` | 32 | 15 | Kept: `carried_by` against a squash GitHub committed. Unchanged; its processes fell with the template's build it carried. |
| `Test_pins_and_copies_in::test_names_a_pin_at_the_froms_line_and_no_docstring_or_three_words` | 105 | 29 | Answered, its two runs; `_read_tree` lists the planted test through git. |
| `Test_originals_of::test_refuses_a_record_with_no_original_line_on_a_ready_pull_request` | 100 | 23 | Answered, its two runs. The branch commits the config itself, where `migrating` merged it from `main` and sealed again; the arm reads it at HEAD either way. |
| `Test_rule_changes_read::test_names_a_near_heading_in_another_work_items_spec_the_branch_edits` | 55 | 14 | Answered; no round at HEAD after the commit. |
| `Test_rule_changes_read::test_refuses_to_run_where_its_reader_will_not_load` | 71 | 24 | Answered, its two runs; no round at HEAD after the commit. |
| `Test_rule_changes_read::test_refuses_another_work_items_spec_the_branch_adds_or_changes` | 61 | 58 | Kept, every reader real: the design `main` hands the arm comes from git's diff of a branch that edits one the base parsed. |
| `Test_guarantee::test_a_verdict_other_than_sealed_fails_a_ready_pull_request` | 92 | 33 | Answered, its three runs. |
| `Test_routing_trailers::test_accepts_a_commit_naming_the_work_item_its_declaration_names` | 50 | 13 | Answered; the trailers stay git's. No new closing records after the commit. |
| `Test_check_lines_in::test_refuses_a_line_the_reader_refuses_at_its_line_in_the_design` | 53 | 16 | Answered; the spec committed once, no closing records after it. |
| `Test_follows::test_accepts_head_and_record_commits_after_it` | 6 | 6 | Kept: `follows` over the template. Unchanged; a carrier of the template's build in run 45203717820. |
| `Test_rule_changes_read::test_refuses_the_spec_of_a_framer_drawn_frame_the_same_way` | 53 | 14 | Answered; one commit of the frame. |
| `Test_main::test_accepts_a_release_pull_request_leaving_a_squashed_item_to_its_own` | 85 | 33 | Answered, its three runs; `carried_by` and the ancestry of a fixed commit stay git's (part 3). |
| `Test_main::test_names_a_line_it_did_not_read_as_a_notice_and_keeps_the_exit` | 88 | 20 | Answered, its two runs over the template; the record handed over through `reading` as before. |
| `Test_originals_of::test_refuses_a_direct_guarantee_with_no_original_line_and_accepts_one` | 61 | 24 | Answered, its two runs over the template. |
| `Test_main::test_names_a_record_under_another_name_and_keeps_the_exit` | 15 | 15 | Kept: `tracked_files` against `git ls-tree` at HEAD, which lists `Round-2.md` beside `round-1.md`. Unchanged. |
| `Test_retired::test_refuses_a_declaration_deleted_beside_a_directory_that_stays` | 56 | 0 | Unit call: `retired` over a disk holding the directory's `frame/design.md`, `settled` replaced, hands it no directory. The refusal's words moved to the new `test_refuses_a_deleted_declaration_whose_directory_stays_by_name`, answered, 15 processes. |
| `Test_retired::test_accepts_a_declaration_a_settle_removed[an-open-row-and-no-rule-in-docs]` | 58 | gone | Kept, every reader real, as `test_accepts_a_declaration_a_settle_removed`, one instance over a real removed history (47 processes): `main` hands `retired` the merge base and the texts at HEAD and prints the notice. |
| `Test_rule_changes_read::test_accepts_a_pull_request_that_declares_nothing_reading_no_spec` | 17 | 12 | Answered. |
| `Test_main::test_refuses_a_chain_with_no_record_and_prints_it_on_a_draft` | 66 | 20 | Answered, its two runs. |
| `Test_retired::test_accepts_a_declaration_a_settle_removed[a-closed-record-and-its-rule-in-docs]` | 58 | gone | Unit call: `test_hands_settled_each_directory_gone_whole_and_reads_nothing_else`, two instances, `retired` over a disk with and without the rule in `docs/`, `settled` replaced, hands it the gone directory and the merge base, 0 processes. The open row lives at the merge base, which `settled` reads, so the kept run holds it. |
| `Test_body::test_refuses_a_body_sent_before_the_seal_at_the_mark` | 54 | 26 | Answered, over the template. |
| `Test_routing_trailers::test_refuses_a_commit_naming_a_work_item_no_declaration_names` | 40 | 36 | Answered, its two runs; the trailers stay git's, which is its fact. |
| `Test_main::test_refuses_a_broad_gate_file_naming_another_commit` | 74 | 42 | Answered with `follows` real, its fact: the stale run's commit against git. |
| `Test_rule_changes_read::test_refuses_another_work_items_spec_straight_to_the_pr` | 37 | 13 | Answered; no new closing records after the commit. |
| `Test_body::test_accepts_the_body_at_a_merge_past_a_later_base_commit` | 52 | 52 | Kept, every reader real: the mark read against a base given as a SHA at the merge commit CI checks out. |
| `Test_retired::test_accepts_every_declaration_leaving_with_the_root` | 47 | 30 | Answered, its two runs; the root's entry and `settled` stay git's. The removed history is one import. |
| `Test_main::test_s3_a_change_to_the_package_reaches_outside_the_document_roots[records]` | 32 | 0 | Unit call: `originals_of` with home `agentic-seal` and the paths under it, the config handed over; 0 processes. |
| `Test_originals_of::test_refuses_to_run_where_the_parity_readers_will_not_load` | 36 | 33 | Kept, every reader real: the originals arm's `main` run over a real branch. |
| `Test_main::test_s3_the_check_judges_the_declaration_under_agentic_seal[None]` | 32 | gone | Kept, every reader real, as `test_s3_the_check_judges_the_declaration_under_agentic_seal`, over `tests/conftest.py#shared`: `main` reads the root's name at `agentic-seal/` and judges the declaration under it. |
| `Test_main::test_refuses_an_open_finding_on_a_ready_pull_request` | 53 | 8 | Answered, over the template. |
| `Test_main::test_refuses_a_fixed_commit_that_touches_nothing_of_the_finding` | 31 | 31 | Kept: `touched` against each commit git lists. Unchanged. |
| `Test_rule_changes_read::test_refuses_a_section_the_parser_refuses_at_its_line[S2-prose-under-items]` | 0 | 0 | Unit call already, unchanged: a carrier of the template's build. |
| `Test_rule_changes_read::test_names_a_near_heading_as_not_read_and_passes` | 0 | 0 | Unit call already, unchanged: a carrier of the template's build. |
| `Test_main::test_s3_a_branch_nothing_declares_is_told_to_add_it_under_agentic_seal` | 24 | 0 | Unit call: `declared_for_this_branch` under `agentic-seal/threads`, the branch from `GITHUB_HEAD_REF`, no committed declaration and no local root; it asserts the same sentence in the `why` `main` prints. 0 processes. |
| `Test_main::test_s3_a_pull_request_deleting_agentic_seal_declares_nothing[HEAD]` | 30 | 28 | Answered over `#shared`; the root's entry stays git's. |
| `Test_main::test_s3_the_check_judges_the_declaration_under_agentic_seal[agentic-seal/README.md]` | 35 | gone | Unit call: `test_s3_the_root_is_named_agentic_seal_beside_the_package[only-the-marker-deleted]`, `root_name` handed HEAD without the marker and the merge base with it. |
| `Test_main::test_s3_a_change_to_the_package_reaches_outside_the_document_roots[the package]` | 32 | gone | Unit call: `originals_of`, as the `[records]` instance, with `seal/__init__.py` among the paths. |
| `Test_main::test_s3_a_design_the_pull_request_edits_under_agentic_seal_is_read` | 34 | 0 | Unit call: `edited_work_items` under `agentic-seal/threads` gives the other item, and `rule_changes_read` refuses its design, handed over (`read_spec`). |
| `Test_retired::test_a_root_that_left_for_a_local_root_says_the_check_judged_nothing` | 30 | 21 | Answered; the root's entry and the local root stay git's. |
| `Test_retired::test_judges_a_root_the_working_tree_has_under_worktree` | 37 | 36 | Answered with `follows` real: the guarantee behind HEAD is its fact. |
| `Test_main::test_accepts_a_reviewed_branch_on_a_ready_pull_request` | 41 | 38 | Kept, every reader real: the one run that holds against git each reader `answered` replaces. |
| `Test_main::test_refuses_a_code_commit_after_the_last_record` | 31 | 31 | Kept: `follows` against a code commit after the last record. Unchanged. |
| `Test_main::test_refuses_a_straight_to_the_pr_item_without_the_sealers_two_files` | 40 | 16 | Answered, its two runs over the template. |
| `Test_retired::test_accepts_under_worktree_a_root_the_working_tree_no_longer_has` | 25 | 16 | Answered; the root's entry on disk is its fact. |
| `Test_follows::test_refuses_another_items_records_and_a_commit_off_the_branch` | 17 | 17 | Kept: `follows` over real commits. Unchanged. |
| `Test_main::test_refuses_an_unreadable_declaration_and_accepts_none` | 32 | 21 | Answered, its two runs. |
| `Test_main::test_s3_a_pull_request_deleting_agentic_seal_declares_nothing[--worktree]` | 26 | 26 | Answered over `#shared`; the root's entry on disk stays the run's. |
| `Test_main::test_s3_the_pull_request_that_adds_agentic_seal_is_judged_under_it[removed]` | 26 | gone | Unit call: `test_s3_the_root_is_named_agentic_seal_beside_the_package[added-the-package-gone]`. The base asserted `main`'s refusal of the missing guarantee; that `main` judges the declaration under the name `root_name` gives is held by the kept `#shared` run. |
| `Test_guarantee::test_an_opener_quoted_in_a_code_span_hides_no_verdict` | 4 | 4 | Unit call already, unchanged: a carrier of the template's build. |
| `Test_changed::test_accepts_a_move_committed_or_not_yet_committed_as_a_move` | 15 | 15 | Kept: `changed` against git's diff. Unchanged. |
| `Test_body::test_prints_the_refusal_on_a_draft_and_exits_0` | 32 | 14 | Answered, over the template. |
| `Test_carried_by::test_refuses_the_items_own_commits_a_persons_squash_and_an_unnumbered_one` | 12 | 12 | Kept: `carried_by` against real squashes. Unchanged. |
| `Test_body::test_accepts_a_folded_body_naming_the_fold` | 26 | 26 | Unit call already, unchanged: its processes are `seal pr-body`'s composition, which reads the seal at HEAD through git. A carrier in run 45203717820 too. |
| `Test_main::test_s3_the_pull_request_that_adds_agentic_seal_is_judged_under_it[kept]` | 25 | gone | Unit call: `test_s3_the_root_is_named_agentic_seal_beside_the_package[the-root-added]`, as the `[removed]` instance. |
| `Test_broad_gate::test_lets_the_records_follow_the_run_and_refuses_any_other_path` | 25 | 25 | Kept: `follows` over real commits after the run. Unchanged. |
| `Test_body::test_prints_a_difference_as_a_notice_under_sealing` | 32 | 14 | Answered, over the template. |
| `Test_guarantee::test_names_a_near_opener_and_reads_no_verdict` | 21 | 21 | Kept, every reader real: the guarantee arm's `main` run over the sealed template. |
| `Test_originals_of::test_refuses_a_direct_guarantee_whose_only_original_is_misspelt` | 0 | 0 | Unit call already, unchanged: a carrier of the template's build. |
| `Test_tree_at::test_accepts_a_directory_at_a_ref_and_on_disk` | 9 | 9 | Kept: `tree_at` against `git ls-tree`. Unchanged. |
| `Test_merge_base::test_accepts_the_fork_point_of_a_moved_base` | 16 | 16 | Kept: `merge_base` against git. Unchanged. |
| `Test_main::test_refuses_an_old_shape_record_and_an_unclosed_fence` | 24 | 0 | Unit call (`records_read`) with `answered`: its fact is the record's shape, and no commit it names is asked of git. |
| `Test_body::test_reads_the_translation_as_the_bodys_first_lines` | 20 | 20 | Unit call already, unchanged: its processes are `seal pr-body`'s composition. |
| `Test_declared_for_this_branch::test_refuses_a_local_declaration_and_says_it_is_local_mode` | 18 | 18 | Kept, every reader real: the class's one `main` run, over a local root. |
| `Test_originals_of::test_a_direct_guarantee_owes_nothing_for_the_document_roots_alone` | 0 | 0 | Unit call already, unchanged: a carrier of the template's build. |
| `test_census` | 0 | 0 | Unchanged: it reads the module's own text and starts nothing; a carrier in run 45203717820. |
| `Test_follows::test_refuses_a_code_commit_after_it_and_an_unseen_commit` | 11 | 11 | Kept: `follows` over real commits. Unchanged. |
| `Test_main::test_refuses_a_fixed_commit_head_does_not_descend_from` | 17 | 17 | Kept: the ancestry of a fixed commit against git. Unchanged. |
| `Test_declared_for_this_branch::test_refuses_two_committed_declarations_naming_the_branch` | 7 | 7 | Kept: `tracked_declarations` against `git ls-tree`. Unchanged. |
| `Test_main::test_passes_a_last_records_fixed_finding_that_touched_only_its_records` | 13 | 13 | Kept: `touched` against a commit of the records alone. Unchanged. |
| `Test_routing_trailers::test_a_commit_its_author_did_not_commit_is_not_judged` | 7 | 7 | Kept: `routing_trailers` against a cherry-pick by another committer. Unchanged. |
| `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line[is_ancestor]` | 18 | 15 | Kept: the read past the bound reaches `lib/gitcmd.py`'s runner. Unchanged; fewer processes from the template. |
| `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line[touched]` | 19 | 16 | Kept, as `[is_ancestor]`. |
| `Test_main::test_refuses_a_last_records_code_finding_fixed_in_its_records_alone` | 12 | 12 | Kept: `touched` against a commit of the records alone. Unchanged. |
| `Test_routing_trailers::test_a_work_item_trailer_at_a_local_root_is_printed_not_refused` | 15 | 15 | Kept, every reader real: the trailer at a local root under the git directory. Unchanged. |
| `Test_guarantee::test_refuses_absent_unfilled_and_behind_head_by_name` | 9 | 9 | Kept: `follows` names the guarantee behind HEAD. Unchanged. |
| `Test_declared_for_this_branch::test_accepts_the_one_routing_md_under_the_work_items_beside_a_decoy[another-file-of-a-work-item]` | 6 | 6 | Kept: `tracked_declarations` against `git ls-tree`. Unchanged. |
| `Test_body::test_names_the_body_as_not_read_under_worktree` | 19 | 9 | Answered, over the template. |
| `Test_routing_trailers::test_a_merge_and_a_squash_github_committed_are_not_its_own` | 10 | 10 | Kept: `routing_trailers` against a merge and a squash. Unchanged. |
| `Test_body::test_refuses_the_mark_where_the_row_gives_none[the key absent]` | 2 | 2 | Unit call already, unchanged: two processes of `seal pr-body`'s composition. |
| `Test_retired::test_judges_the_declarations_where_the_working_tree_has_seal_as_a_file` | 13 | 12 | Answered; the root's entry on disk stays the run's, and `settled` git's. |
| `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line[rule_changes_read]` | 15 | 12 | Kept, as `[is_ancestor]`. |
| `Test_pins_and_copies_in::test_names_a_test_the_parser_gives_up_on_as_not_read[MemoryError]` | 3 | 3 | Unit call already, unchanged: `planted` stages the test through git. |
| `Test_pins_and_copies_in::test_names_a_test_the_parser_gives_up_on_as_not_read[RecursionError]` | 3 | 3 | Unit call already, unchanged, as `[MemoryError]`. |
| `Test_main::test_refuses_a_last_records_fixed_finding_owing_a_verifying_round` | 15 | 2 | Unit call (`records_read`) with `answered`: its fact is the last record's verdict, not what follows it. |
| `Test_declared_for_this_branch::test_local_mode_says_the_check_judged_nothing` | 13 | 3 | Unit call: `declared_for_this_branch` over the local root; it asserts the same words in the `why` `main` prints, where it read `main`'s output. |
| `Test_policy_root::test_accepts_the_row_a_config_writes` | 4 | 4 | Kept: `policy_root` over a real repository. Unchanged. |
| `Test_declared_for_this_branch::test_the_shared_sentence_says_what_it_searched_and_for_what` | 12 | 2 | Unit call: `declared_for_this_branch` over the `repo` world; it holds the assertions of `test_accepts_a_shared_root_and_tells_it_to_add_the_file` too. |
| `Test_guarantee::test_accepts_the_newest_of_two_runs` | 9 | 9 | Kept: `follows` reads the newest run's commit. Unchanged. |
| `Test_declared_for_this_branch::test_accepts_the_one_routing_md_under_the_work_items_beside_a_decoy[a-routing-md-outside-the-work-items]` | 6 | 6 | Kept, as `[another-file-of-a-work-item]`. |
| `Test_main::test_names_no_line_inside_a_fence` | 12 | 2 | Unit call (`records_read`, `unread`) with `answered`: its fact is the fences. |
| `Test_declared_for_this_branch::test_accepts_a_shared_root_and_tells_it_to_add_the_file` | 12 | gone | Cut: `test_the_shared_sentence_says_what_it_searched_and_for_what` reads the same `why` over the same world and holds its two assertions. |
| `Test_body::test_refuses_a_missing_pr_md_at_its_path` | 6 | 6 | Unit call already, unchanged: `seal pr-body`'s composition. |
| `Test_declared_for_this_branch::test_a_repository_with_no_root_is_told_to_add_the_file` | 12 | 2 | Unit call: `root_name` reads the working tree's no root as `seal`, and `declared_for_this_branch` under it gives the sentence. |
| `Test_main::test_refuses_a_last_records_fixed_finding_that_also_touched_code` | 8 | 8 | Kept: `touched` against a commit of code and records. Unchanged. |
| `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line[trailers]` | 13 | 10 | Kept, as `[is_ancestor]`. |
| `Test_declared_for_this_branch::test_refuses_a_detached_head_with_no_head_ref_as_no_branch` | 5 | 5 | Kept: `current_branch` against a detached HEAD. Unchanged. |

**`tests/conftest.py`.** Two changes there would cut this module, and the spawn barred each. `#shared`, function-scoped, runs `git init` and its commits for each of the three cases that still take it, through `declared`: 28 to 32 processes a case. A module-scoped template copied per case would build it once per worker. `#commit_everything`'s `git rev-parse HEAD` after each commit is the trim phase 1 names in `gaps.md` *Not done*; the module's cases still commit through it.

### Checks at the phase's close

- `bin/test tests/skills/test_chain_check.py -q -p no:xdist --durations=0`: 253 passed in 26.28 s at `457799c55` (executed, file order); `-p no:xdist` at `191d0f78e`: 253 passed in 26.90 s (executed).
- `bin/test tests/skills/test_chain_check.py -q`: 253 passed in 7.42 s at `457799c55` and 7.33 s at `191d0f78e` (executed, under `-n auto`).
- `bin/seal layout --check tests/skills/test_chain_check.py`: exit 0, `seal layout: 1 files read, 0 refused, 0 declare no TARGET` (executed). Its `report:` lines name functions of `chain_check.py` with no class of their own, `root_name` and `edited_work_items` among them, and refuse nothing.
- `bin/seal layout --pairs tests/skills/test_chain_check.py`: `seal layout: 1 files read, 0 pairs` (executed).
- The *Phase boundary* set, `bin/test tests/skills/test_chain_check.py tests/behaviour tests/text -q`: 1128 passed, 9 skipped, at `457799c55` and at `191d0f78e` (executed). It prints six warnings, as at phases 5 to 8; this phase changes no document they cite, and did not read them further. The set holds `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, which reads `test_refuses_a_git_that_did_not_answer_in_one_line` by name; the case keeps it.
- `uvx ruff format` and `uvx ruff check` over the changed file: clean (executed).
- The suite: `unverified`. The broad gate is the orchestrator's, once the review rounds settle.
</content>
</invoke>
