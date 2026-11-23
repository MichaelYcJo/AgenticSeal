# Phase 11: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## What this phase found

### The frame, read against the tree before the build

The frame holds for `tests/skills/test_settle.py` at `f2fac912b`, with one exception below. `git log dacef7f4b..f2fac912b` over the module, `skills/settle/`, `tests/conftest.py` and `lib/` prints nothing (executed). So runs 45235848444 at `dacef7f4b`, 45244493975 at `b9d8d4ade` and 45249520034 at `f2fac912b` all measured the file this phase starts from. Their artifacts put the module at 126.9 s, 131.0 s and 109.5 s (executed: the sum by case over `1581-dispatch-7/`, `-8/` and `-9/` `.test_durations` in this session's scratchpad). The 88 cases *Scope* item 13 takes from run 45235848444 stand in the module under their names (executed: `listed.txt` in this phase's scratch, built from that artifact and the collected ids). The ten readers `answered` answers are the ten item 13 names (read: `tests/skills/test_settle.py#answered`). The 15 files that import `unanswered` or `past_the_bound` are the 15 `frame/design.md` *Data & interfaces* lists (executed: `git grep -lE "from (tests\.skills\.)?test_settle import" -- tests`). The phase changes no shipped file.

The exception is item 13's rule for a reader's own case. It keeps one only "where no kept run of an arm has it real". A run holds one answer of a reader, not every answer. The merge-order arm run holds `rule_changes._ancestor` answering True on one line of history. No arm run holds it answering neither way, for two commits on branches merged apart. The first commit of this phase, `ac2a79762`, answered `_ancestor` in both cases that read that answer, and a mutant that ignores git's answer, `return a != b and (gitcmd().is_ancestor(root, a, b) or True)`, survived it, and the test file at `f2fac912b` turns it red (executed: `bin/seal mutate` against each test file). `8ba07b5b0` gives `_ancestor` its own case again. The phase reads item 13 as "where no kept run of an arm reads the answer the case's fact is". The orchestrator may fold that wording into `frame/design.md`.

*Grounding*, *Where `test_settle.py`'s seconds stand after phase 8*, estimates the module near 35 s after this phase. That estimate counts the seven arm runs and the reader classes, and takes every other listed case to a call with no process. Item 13 lets a listed case stay over a real history where its fact is a git agreement, and this phase keeps 50 of the 88 that way. So the estimate does not describe what this phase builds; *Q2* below gives the phase's own.

### Q1: where the module's seconds went before the rebuild

**On the Windows leg.** In run 45235848444, the 88 listed cases cost 110.1 s and the other 102 cost 16.8 s. Split by what a case does locally, the 33 cases that start no process cost 2.1 s, the 52 that start processes and copy no world 36.4 s, and the 105 that do both 88.4 s (executed, against the local counts below).

**On this macOS machine.** `tmp_spawn_probe.py` in this phase's scratch is phase 10's probe with this module's names. `bin/test tests/skills/test_settle.py -q -p no:xdist -p tmp_spawn_probe --durations=0` at `f2fac912b` passed 190 cases in 20.54 s, 2.79 s of it in setup and 16.73 s in calls (executed). The cases started 1,263 processes: 140 in setup and 1,123 in calls.

- **By who started them.** `settle.main` 355; the module's functions named `run`, the helper that runs `survey` at HEAD and the wrappers `calls` and `unanswered` install, 222; `tests/conftest.py#git`, `tree`'s build per case among it, 112; `at` 69; `recorded` 40; `removed_plan` 34; `tagged`, `Test_versions`' history, 26. The rest are each case's own `git switch`, `git merge`, `git commit` and `git log`.
- **By class.** `Test_main` 671, `Test_report` 275, `Test_apply` 161, `Test_module` 55, and the reader classes 101.
- **By subcommand.** `git rev-parse` 242, `git log` 156, `git commit` 152, `git add` 149, `git config` 53.

A fit of each run's seconds per case against these counts, with a constant per case, gives 0.087 s, 0.085 s and 0.076 s a process at the three runs' rates (executed: `fit.py` in this phase's scratch). The copy term comes out negative, since nearly every case that copies a world also starts processes, so the fit cannot split the two. On the leg the seconds stand in the processes.

### What the rebuild changed

`ac2a79762` does the rebuild, and `8ba07b5b0` keeps one case of `_ancestor` real, as the first section says.

- **`tree` is built once per module.** `_tree_world` builds `tests/conftest.py#tree`'s world by that fixture's own function, so the world keeps its one definition there. `tree_copy` copies it, history and all, for the four cases whose reader asks git: `released` at a ref that does not see a closure, the paths a row names, a ref that does not resolve, and a released id that is not ASCII. `answered_tree` copies its files with an empty `.git/`, as `drawn` has, so its 16 cases start no process where each paid `tree`'s five.
- **The published-note cases share one fragment.** `noted` copies `_noted_world`, `shared_repo` with `1700000001-a`'s `changelog.md` committed as `feat: a (#42)` and tagged `v1.2.3`. The seven cases that each committed and tagged that fragment take it. The two that also committed a bare work item with `moment` write it with `standing` on disk, where `answered` reads `released`.
- **A history is written by one `git fast-import`.** `imported` writes a list of commits, merges and tags in one process. `committed` writes commits on the current branch and reads their ids in one `git log`; seven `earlier_judgments` cases of `Test_report` write their history with it. `removed_plan` now calls `imported`. `merged_history` writes a base, a side branch, a commit on `main` and their merge, and the five `--from` cases of a merge's shape and the two instances of the parallel-branches case read it. Git reads a merge by its tree and its parents, so the merge carries the tree that `git merge`, or a resolution, would have left.
- **`Test_main` cases whose fact is one reader answer the others.** `answered(…, real={…})` now stands in `test_gh_is_asked_once_for_a_branch_two_items_name`, `test_a_released_at_given_as_the_merge_commit_reaches_it`, `test_the_first_listed_pull_request_the_ref_reaches_is_taken` and `test_a_merge_commit_the_ref_does_not_reach_leaves_the_item` (`released_local`); `test_local_specs_are_listed_in_the_order_their_pull_requests_merged` (`released_local`, `merge_order`, `_ancestor`); and `test_a_named_directory_is_never_written` (`git_fields`). The five merge cases answered the readers but `git_fields` at `f2fac912b` already; what changed in them is the history.
- **Three cases moved to the class of the arm they read through.** The parallel-branches case and `test_two_local_merges_no_ancestry_orders_are_marked_unordered` moved to `Test_report`, and `test_shared_mode_asks_gh_for_no_note_it_cannot_read` to `Test_apply`, each a call of `at`.
- **The comment above `has_history` names each arm's run and each reader's case.** The module's docstring says how `Test_main` now answers the readers a case's fact is not.

After the rebuild the module passes 190 cases and starts 883 processes, against 1,263: 49 in setup and 834 in calls (executed, the same plugin). By class: `Test_main` 444, `Test_report` 187, `Test_apply` 101, `Test_module` 50, and the reader classes 101. `git commit` falls from 152 to 67.

### Departures from the frame

- **`_tree_world` calls `conftest.tree.__wrapped__`.** The spawn bars `tests/conftest.py`, and phase 6 took back module worlds that defined a fixture's world a second time (`trail/phases/phase-6.md`, *Departures from the frame*). Calling the fixture's own function builds the same world from its one definition. `__wrapped__` is what pytest 9.1.1's `FixtureFunctionDefinition` gives for the undecorated function (executed: the module passes). A later pytest that drops it breaks the module at collection, where a person sees it.
- **`answered_tree` holds an empty `.git/`.** At `f2fac912b` it was `tree` with its history and every reader answered. With no history, `answered` makes any process `lib/gitcmd.py` starts raise, so a case that came to lean on git is told.
- **The parallel-branches case keeps two readers real.** Item 13 would have the merge-order arm run hold `_ancestor`. It holds the answer True only, as the first section says, so the case reads `order` and `_ancestor` from git over the history `merged_history` writes, six processes where it started 21.

### The four parts `CONTRIBUTING.md` *The test layout* asks of a rebuilt module

**1. The move check, and the mutation table.**

`bin/seal layout --moved f2fac912b --from tests/skills/test_settle.py --to tests/skills/test_settle.py` exits 1 at `8ba07b5b0` (executed). Its last line reads `seal layout: moved: 139 old cases, 189 items against 189 at f2fac912b244, 90 failed`. 32 items fail on `body: stands for no old case`, 32 on `body: not in the new files unchanged`, 16 on `fixture answered_tree: its definition differs from the base's`, and 10 on `removed_plan` and the helpers it now calls. So the mutation table carries part 1.

The module's mutation table is the records of phases 1, 8 and 11 together. Every set ran again against `8ba07b5b0`, each in one call, `bin/seal mutate <file> --replace … --tests "bin/test tests/skills/test_settle.py -q -x"` (executed). Phase 1's 38, from `run_mutants.py` and `mutants.py` in phase 1's scratch, printed `seal mutate: 38 mutants, 33 red, 5 SURVIVED, 0 with no verdict (142.3s)`. Phase 8's, from `run8.py` and `mutants8.py` in phase 8's scratch, printed `seal mutate: 19 mutants, 18 red, 1 SURVIVED, 0 with no verdict (77.1s)` for `settle.py` and `seal mutate: 5 mutants, 4 red, 1 SURVIVED, 0 with no verdict (23.5s)` for `rule_changes.py`. Every mutant red at phase 1 and at `b928d373e` is red again, and the survivors are those phases' own: 1.2, 1.4, 1.6, 1.18, 1.30, 8.17 and 8.20. Their records say why each lives.

| # | Unit | Mutant | Phase 1 | `b928d373e` | `8ba07b5b0` |
|---|---|---|---|---|---|
| 1.1 | `threads` | the root's own name replaced by `seal` | red | red | red |
| 1.2 | `work_items` | a file directly under the threads directory listed as a work item | SURVIVED | SURVIVED | SURVIVED |
| 1.3 | `show` | the output of a failed `git show` returned as text | red | red | red |
| 1.4 | `released` | a path directly under the threads directory read as a work item | SURVIVED | SURVIVED | SURVIVED |
| 1.5 | `policy_root` | the root's resolution replaced by `""` | red | red | red |
| 1.6 | `adding_commits` | the newest add of a path kept instead of the oldest | SURVIVED | SURVIVED | SURVIVED |
| 1.7 | `adding_commits` | no pull request number read from a subject | red | red | red |
| 1.8 | `merged_pull_requests` | every merge commit read as none | red | red | red |
| 1.9 | `versions` | a tag that peels to something other than a commit taken | red | red | red |
| 1.10 | `versions` | the commits labelled highest tag first | red | red | red |
| 1.11 | `blobs` | an answer other than `blob` read as text | red | red | red |
| 1.12 | `published_releases` | a draft release read as published | red | red | red |
| 1.13 | `carries` | the older notes' marker not read | red | red | red |
| 1.14 | `notes` | a tag with no published release not kept | red | red | red |
| 1.15 | `released_local` | `gh` asked again for a branch already asked | red | red | red |
| 1.16 | `released_local` | a merge commit the ref does not reach taken | red | red | red |
| 1.17 | `named_paths` | a bare file name not read as a path | red | red | red |
| 1.18 | `in_tree` | a path holding `/` looked up among bare file names | SURVIVED | SURVIVED | SURVIVED |
| 1.19 | `misplaced` | a directory or a link to nothing named as a record | red | red | red |
| 1.20 | `misplaced` | a record at its own place named as misplaced | red | red | red |
| 1.21 | `plan_rows` | a near heading not named | red | red | red |
| 1.22 | `earlier_judgments` | the window of two removing commits removed | red | red | red |
| 1.23 | `earlier_judgments` | a path holding a newline asked for | red | red | red |
| 1.24 | `earlier_judgments` | the release tag of the adding commit not looked up | red | red | red |
| 1.25 | `timeline` | a design that does not parse grouped | red | red | red |
| 1.26 | `history` | a merge that adds a document not read as its add | red | red | red |
| 1.27 | `history` | a deletion read as a change | red | red | red |
| 1.28 | `tracked_text` | the work items' own files read as citing files | red | red | red |
| 1.29 | `tracked_text` | a binary file read | red | red | red |
| 1.30 | `citations` | a file outside `tests/` that names the threads directory read as a check | SURVIVED | SURVIVED | SURVIVED |
| 1.31 | `names` | an abbreviated path not read as a citation | red | red | red |
| 1.32 | `draft` | each operation applied to the document as it stands on disk | red | red | red |
| 1.33 | `apply` | a directory kept for its note left out of the exit code | red | red | red |
| 1.34 | `apply` | the published note read in local mode | red | red | red |
| 1.35 | `main` | `--all-earlier` beside `--apply` not refused | red | red | red |
| 1.36 | `main` | a root holding no work item not answered as settled | red | red | red |
| 1.37 | `named_directory` | a directory outside the repository read | red | red | red |
| 1.38 | `report` | the local headings printed in shared mode | red | red | red |

| # | Unit | Mutant | `b928d373e` | `8ba07b5b0` |
|---|---|---|---|---|
| 8.1 | `released` | a ref that does not resolve read as one holding no work item | red | red |
| 8.2 | `released` | each path under the threads directory read as a work item id, not its first part | red | red |
| 8.3 | `resolves` | every ref read as resolving | red | red |
| 8.4 | `show` | the output of a failed `git show` returned as text | red | red |
| 8.5 | `merged_pull_requests` | `gh` asked for every pull request, not the merged ones | red | red |
| 8.6 | `merged_pull_requests` | every merge commit read as none | red | red |
| 8.7 | `merged_pull_requests` | an answer that is no list of pull requests read as none merged | red | red |
| 8.8 | `notes` | an empty `changelog.md` read as a fragment | red | red |
| 8.9 | `notes` | a commit that names no pull request read as one that does | red | red |
| 8.10 | `notes` | a repository that builds no note from the fragments read as one that does | red | red |
| 8.11 | `notes` | a version with no published release read as published | red | red |
| 8.12 | `notes` | a note that does not carry the entry read as carrying it | red | red |
| 8.13 | `notes` | a list with no published release read as holding one | red | red |
| 8.14 | `released_local` | a merge commit the ref does not reach taken | red | red |
| 8.15 | `released_local` | a branch with no merged pull request read as not reached | red | red |
| 8.16 | `released_local` | a work item that names no branch read as naming `main` | red | red |
| 8.17 | `git_fields` | the output of a failed git command split into fields | SURVIVED | SURVIVED |
| 8.18 | `history` | a merge whose status holds an `A` beside another letter read as its add | red | red |
| 8.19 | `history` | a deletion read as a change | red | red |
| 8.20 | `order` | the newest commit adding a design kept, not the oldest | SURVIVED | SURVIVED |
| 8.21 | `order` | the history read newest first | red | red |
| 8.22 | `merge_order` | the pairs left in the order handed | red | red |
| 8.23 | `merge_order` | the commits read newest first | red | red |
| 8.24 | `_ancestor` | any two commits read as ordered | red | red |

Mutants 11.1 to 11.10 sit at the readers the changed cases reach: the `--cc` of `history`, the window and the deletions `earlier_judgments` reads, the order `released_local` reads a branch's pull requests in, the arm `survey` chooses, and `unordered` and `_ancestor`. `mutants8.py` under `mut/` in this phase's scratch holds them, named so phase 8's `run8.py` runs it unchanged. The `settle.py` call printed `seal mutate: 7 mutants, 7 red, 0 SURVIVED, 0 with no verdict (28.5s)` and the `rule_changes.py` call `seal mutate: 3 mutants, 2 red, 1 SURVIVED, 0 with no verdict (15.0s)` (executed, against `8ba07b5b0`). The survivor, 11.9, ran again against the test file at `f2fac912b`, copied to `tests/skills/test_tmp_settle_base.py` and removed after the run, and survived there too (executed: `190 passed` with the mutant in place). 11.10 also ran against that copy, since `ac2a79762` let it survive, and is red there (executed). No case gives two work items one commit, so the `ca == cb` that keeps such a pair ordered has nothing behind it. The phase adds no case for it: the frame rebuilds existing cases (`frame/design.md` *Scope* item 13), and `agents/crafter.md` *Never* bars building beyond the request. `gaps.md` *Not done* names it.

| # | Unit | Mutant | `f2fac912b` | `8ba07b5b0` |
|---|---|---|---|---|
| 11.1 | `history` | the log read without `--cc` | | red |
| 11.2 | `earlier_judgments` | a plan read at every deletion, not the newest | | red |
| 11.3 | `earlier_judgments` | a plan whose directory stands read as removed | | red |
| 11.4 | `earlier_judgments` | a commit that deleted two plans counted twice in the window | | red |
| 11.5 | `earlier_judgments` | the deletions listed without `--no-renames` | | red |
| 11.6 | `released_local` | only the first listed pull request read | | red |
| 11.7 | `survey` | a shared root read as a local one | | red |
| 11.8 | `unordered` | no pair marked | | red |
| 11.9 | `unordered` | two items of one commit not read as ordered | SURVIVED | SURVIVED |
| 11.10 | `_ancestor` | git's answer ignored, every pair ordered | red | red |

**2. Cases and seconds, before and after, on this macOS machine.** The figures are local. `frame/design.md` *Grounding*, *What a figure of the Windows leg can show*, takes no local figure as evidence of a saving on the Windows leg.

| | `f2fac912b` | `8ba07b5b0` |
|---|---|---|
| Cases passed | 190 | 190 |
| `bin/test tests/skills/test_settle.py -q -p no:xdist` | 20.54 s, under the probe | 15.14 s |
| Processes the cases start in the test process, counted by `tmp_spawn_probe.py` under `-p no:xdist` | 1,263 | 883 |
| `git commit` among them | 152 | 67 |
| Cases by class | `Test_main` 89, `Test_report` 46, `Test_apply` 21, `Test_module` 12, others 22 | `Test_main` 85, `Test_report` 49, `Test_apply` 22, `Test_module` 12, others 22 |

Under `-n auto`, `bin/test tests/skills/test_settle.py -q` passes 190 cases in 4.08 s at `8ba07b5b0` (executed).

**3. The real runs kept.** Each arm of `main` keeps one run over a real history with every reader real (read: each case's body holds no `answered` and no `unanswered`):

- The dry run's merge order: `Test_main::test_two_specs_on_one_sentence_are_one_group_in_merge_order`.
- The release at a ref: `Test_main::test_s5_settle_shows_a_work_item_released_under_agentic_seal`, run as the command through `tests/skills/test_seal.py#tool`.
- The published note under `--apply`: `Test_main::test_apply_keeps_a_directory_its_published_note_does_not_carry`.
- The history earlier settles removed: `Test_main::test_the_judgments_earlier_settles_removed_are_read_from_the_history`.
- `--from`: `Test_main::test_from_lists_every_document_of_a_named_directory_in_gits_order`.
- `--draft`: `Test_main::test_draft_writes_each_operation_in_merge_order_and_names_what_it_missed`.
- Local mode: `Test_main::test_local_mode_lists_a_released_and_an_unreleased_item`, with `gh` a script on `PATH`.

Each reader `answered` answers keeps a case of its own over a real history where those runs do not read the answer its fact is:

- `released`: `Test_report::test_a_released_work_item_whose_id_is_not_ascii_is_a_candidate`, over `tree_copy`.
- `show`: `Test_show`.
- `rule_changes.order`: `Test_module`'s `merge_order` cases.
- `rule_changes._ancestor`: `Test_report::test_two_specs_on_parallel_branches_at_one_place_are_one_group_unordered`, for two commits no ancestry orders.
- `resolves`, `released_local` and `rule_changes.merge_order`: the local cases of `Test_main` that keep `released_local` real, and `Test_module`'s `merge_order` cases.
- `earlier_judgments`: the cases of `Test_report` that remove plans in a history.
- `git_fields`: `Test_tracked_text`, the five merge cases of `Test_main`, and `Test_report::test_every_open_row_is_listed_with_the_paths_it_names`.
- `notes`: the cases of `Test_apply` and `Test_main` over `noted`.

The comment above `has_history` in the module names the same runs and cases.

**4. The listed cases, each with its verdict.** Each of the 88 cases *Scope* item 13 takes has one verdict. "Kept" is a case that stays over a real history, with the agreement between the reading and git its fact is. "A call" is a case that now runs `survey` with its readers answered. The seconds are run 45235848444's, the processes this phase's probe counted at each commit (executed). No listed case was cut. Each rewritten case keeps the base's assertions, with the world's name where it names one.

| Case at `f2fac912b` | Run 45235848444 | Processes at `f2fac912b` | Processes at `8ba07b5b0` | Verdict |
|---|---|---|---|---|
| `Test_adding_commit::test_accepts_the_oldest_add_of_each_path` | 0.95 s | 12 | 12 | Kept: the reader class of `adding_commits`, git's `--diff-filter=A` log over a history. |
| `Test_adding_commit::test_refuses_a_number_the_subject_does_not_end_with_and_a_failed_git` | 0.53 s | 6 | 6 | Kept: the reader class of `adding_commits`; a git that fails. |
| `Test_apply::test_a_closure_the_released_ref_has_not_seen_lets_the_directory_go` | 2.13 s | 22 | 17 | Kept real over `tree_copy`: the row is closed on the working branch and open at the released ref, so the fact is what `released` reads at a ref git resolves. `tree` is copied from the module's one build in place of built per case. |
| `Test_apply::test_apply_removes_where_no_published_note_is_built_from_the_fragments` | 1.65 s | 11 | 7 | Kept real: `notes` reads the tag and the adding commit of a `changelog.md` and asks the in-process `gh` for the release list; the other readers are `answered`. Over `noted`, the module's one commit and tag of the fragment, copied. |
| `Test_apply::test_apply_removes_a_directory_its_published_note_carries[link]` | 1.42 s | 11 | 11 | Kept real: `notes` reads the tag and the adding commit of a `changelog.md` and asks the in-process `gh` for the release list; the other readers are `answered`. Over `noted`, the module's one commit and tag of the fragment, copied. This instance carries the build of `_noted_world`. |
| `Test_apply::test_apply_removes_where_the_repository_publishes_no_release[a draft]` | 1.27 s | 11 | 7 | Kept real: `notes` reads the tag and the adding commit of a `changelog.md` and asks the in-process `gh` for the release list; the other readers are `answered`. Over `noted`, the module's one commit and tag of the fragment, copied. |
| `Test_apply::test_apply_keeps_a_directory_whose_tag_has_no_published_release[another]` | 1.11 s | 12 | 8 | Kept real: `notes` reads the tag and the adding commit of a `changelog.md` and asks the in-process `gh` for the release list; the other readers are `answered`. Over `noted`, the module's one commit and tag of the fragment, copied. |
| `Test_apply::test_apply_keeps_a_directory_whose_tag_has_no_published_release[a draft]` | 1.09 s | 12 | 8 | Kept real: `notes` reads the tag and the adding commit of a `changelog.md` and asks the in-process `gh` for the release list; the other readers are `answered`. Over `noted`, the module's one commit and tag of the fragment, copied. |
| `Test_apply::test_apply_leaves_a_team_specs_of_the_same_name_on_disk` | 1.03 s | 7 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_apply::test_apply_removes_where_the_repository_publishes_no_release[none]` | 1.02 s | 11 | 7 | Kept real: `notes` reads the tag and the adding commit of a `changelog.md` and asks the in-process `gh` for the release list; the other readers are `answered`. Over `noted`, the module's one commit and tag of the fragment, copied. |
| `Test_apply::test_keeps_on_the_record_at_its_place_and_names_the_copy` | 0.85 s | 7 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_apply::test_a_removed_record_prints_each_row_it_closed_and_writes_no_document` | 0.83 s | 7 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_apply::test_apply_removes_a_directory_its_published_note_carries[marker]` | 0.80 s | 11 | 7 | Kept real: `notes` reads the tag and the adding commit of a `changelog.md` and asks the in-process `gh` for the release list; the other readers are `answered`. Over `noted`, the module's one commit and tag of the fragment, copied. |
| `Test_apply::test_refuses_an_unreadable_memo_and_keeps_its_directory` | 0.79 s | 7 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_apply::test_accepts_every_released_directory_with_no_open_row` | 0.75 s | 7 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_apply::test_removes_a_directory_whose_gaps_md_is_away_and_names_it` | 0.75 s | 7 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_apply::test_an_unreleased_spec_less_directory_is_not_a_candidate` | 0.71 s | 5 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_apply::test_an_open_row_keeps_its_directory_before_its_note_is_read` | 0.70 s | 5 | 1 | A call over `noted` with every reader answered but `notes`; the open row keeps the directory before `notes` asks, so it starts one process, where the base committed `gaps.md` and a fragment. |
| `Test_apply::test_apply_removes_a_directory_whose_fragment_is_empty` | 0.66 s | 8 | 8 | Kept real: `notes` over a `changelog.md` an empty fragment commit adds, its own commit since the text differs from `noted`'s; the other readers are `answered`. |
| `Test_main::test_a_merge_that_resolved_a_document_is_its_last_change` | 2.80 s | 22 | 8 | Kept real: `git_fields` reads `git log --cc --name-status` at a merge that resolved a conflict; the history is written by one `git fast-import` (`merged_history`), the merge with the tree a resolution leaves, and the other readers are `answered`. |
| `Test_main::test_from_lists_every_document_of_a_named_directory_in_gits_order` | 2.75 s | 30 | 30 | Kept: the `--from` arm's one run with every reader real. |
| `Test_main::test_two_specs_on_one_sentence_are_one_group_in_merge_order` | 2.55 s | 28 | 28 | Kept: the dry run's merge order, one run with every reader real; it also holds `rule_changes._ancestor` True on one line of history. |
| `Test_main::test_a_merge_that_wrote_a_document_no_parent_holds_adds_it` | 2.31 s | 21 | 8 | Kept real, as the resolved merge: `AA` under `--cc` at a merge that wrote a file no parent holds. |
| `Test_main::test_shared_mode_asks_gh_for_no_note_it_cannot_read` | 2.25 s | 32 | 20 | Moved to `Test_apply`, a call of `survey` with `report` and `apply`: `notes` and `released_local` stay real, the rest `answered`, so a shared root read as local would ask `gh`. Its three fragments still commit through the working tree. |
| `Test_main::test_a_merge_that_rewrote_a_document_one_parent_lacks_changes_it` | 2.14 s | 22 | 8 | Kept real, as the resolved merge: `AM` under `--cc`. |
| `Test_main::test_apply_keeps_a_directory_its_published_note_does_not_carry` | 2.12 s | 29 | 29 | Kept: the published note under `--apply`, one run with every reader real. |
| `Test_main::test_a_deletion_is_no_change_to_a_document_head_holds` | 1.98 s | 23 | 8 | Kept real, as the resolved merge: a `D` on one parent's line that the merge does not name. |
| `Test_main::test_two_specs_on_parallel_branches_at_one_place_are_one_group_unordered[S]` | 1.98 s | 21 | 6 | Moved to `Test_report`, a call of `survey` and `report`: the reader case of `rule_changes._ancestor` answering neither way. `merged_history` writes the two branches and the merge in one `git fast-import`, `order` and `_ancestor` read them, and the other readers are `answered`. |
| `Test_main::test_draft_writes_each_operation_in_merge_order_and_names_what_it_missed` | 1.98 s | 23 | 23 | Kept: the `--draft` arm's one run with every reader real. |
| `Test_main::test_a_clean_merge_of_two_edits_is_a_documents_last_change` | 1.96 s | 19 | 8 | Kept real, as the resolved merge: `MM` at a clean merge of two edits, whose tree `merged_history` writes as `git merge` leaves it. |
| `Test_main::test_two_specs_on_parallel_branches_at_one_place_are_one_group_unordered[S child]` | 1.88 s | 21 | 6 | As `[S]`. |
| `Test_main::test_a_named_directory_is_never_written` | 1.79 s | 22 | 12 | Kept as a run of `main` with `--from` then `--apply`, the readers but `git_fields` `answered`: its fact is that the named directory's bytes and `git status` stand, which only git's status reads. |
| `Test_main::test_two_local_merges_no_ancestry_orders_are_marked_unordered` | 1.76 s | 22 | 6 | Moved to `Test_report`: a call over `local_repo` with every reader `answered` and `_ancestor` answering neither way, which `[S]` of the parallel-branches case holds against git; no merge is made. The processes left are `local_repo`'s setup. |
| `Test_main::test_all_earlier_reads_the_plans_of_every_removing_commit` | 1.52 s | 7 | 7 | Unchanged: `--all-earlier` through `main`, the one run of that flag with `earlier_judgments` real; it carries the build of the module's `_removals_world`. |
| `Test_main::test_local_specs_are_listed_in_the_order_their_pull_requests_merged` | 1.44 s | 16 | 13 | Kept real for `released_local`, `merge_order` and `_ancestor`: two merge commits on one line of history, which `_ancestor` orders True; the other readers `answered`. |
| `Test_main::test_local_mode_lists_a_released_and_an_unreleased_item` | 1.39 s | 18 | 12 | Kept: local mode's one run with every reader real and `gh` a script on `PATH`. |
| `Test_main::test_the_judgments_earlier_settles_removed_are_read_from_the_history` | 1.39 s | 14 | 14 | Kept: the history earlier settles removed, one run with every reader real. |
| `Test_main::test_apply_stops_where_the_release_list_cannot_be_read[fails]` | 1.20 s | 15 | 9 | Kept as a run of `main --apply` over `noted`, the readers but `notes` `answered`: the refusal is the in-process `gh` failing, and the run stops before any removal. `standing` writes the bare work item on disk in place of `moment`'s commit, and `noted` holds the tagged fragment the case committed. |
| `Test_main::test_s5_settle_shows_a_work_item_released_under_agentic_seal` | 1.20 s | 9 | 9 | Kept: the release at a ref, run as the command through the `tool` subprocess, every reader real. |
| `Test_main::test_a_merge_commit_the_ref_does_not_reach_leaves_the_item` | 1.18 s | 16 | 10 | Kept real for `released_local`: the merge commit is on a branch `--released-at` does not reach, which `gitcmd.is_ancestor` asks; the other readers `answered`. |
| `Test_main::test_apply_stops_where_the_release_list_cannot_be_read[entry]` | 1.13 s | 15 | 9 | As `[fails]`. |
| `Test_main::test_a_file_under_two_named_directories_is_listed_once` | 1.12 s | 11 | 11 | Unchanged: `--from . --from b` through `main` from a subdirectory, the readers but `git_fields` `answered`; its fact is `git ls-files` over two pathspecs that overlap. |
| `Test_main::test_a_released_at_given_as_the_merge_commit_reaches_it` | 1.03 s | 10 | 6 | Kept real for `released_local`: `is_ancestor` of a commit and itself; the other readers `answered`. |
| `Test_main::test_the_first_listed_pull_request_the_ref_reaches_is_taken` | 1.01 s | 15 | 11 | Kept real for `released_local`: a listed merge commit the ref does not reach and a later one it does; the other readers `answered`. |
| `Test_main::test_apply_stops_where_the_release_list_cannot_be_read[garbled]` | 1.00 s | 15 | 9 | As `[fails]`. |
| `Test_main::test_a_root_with_no_work_item_lists_the_named_documents_and_is_settled[committed]` | 0.90 s | 12 | 12 | Unchanged: a root with no work item through `main`, whose committed instance reads the dates git gives the named documents; it builds its own repository. |
| `Test_main::test_gh_is_asked_once_for_a_branch_two_items_name` | 0.84 s | 11 | 4 | Kept real for `released_local`, whose fact is one `gh` query for two items; the merge commit `gh` names is the world's own `main`, so no merge is made, and the other readers `answered`. |
| `Test_main::test_a_git_that_cannot_read_the_adding_commit_stops_apply` | 0.84 s | 10 | 4 | Kept as a run of `main --apply` over `noted`, the readers but `notes` `answered`, and `adding_commit` raising as a git that exits 128 does. `standing` replaces `moment`'s commit, and `noted` the fragment's. |
| `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line[released]` | 0.72 s | 7 | 7 | Kept: a refusal where git does not answer (`frame/plan.md` A4); it carries the build of `_shared_world` in its worker. |
| `Test_main::test_accepts_a_settled_root_and_says_so[apply-empty]` | 0.66 s | 1 | 1 | Unchanged: one process. Its seconds on the leg stand in no process of its own; a module world built in the setup of the first case each worker runs is the likely cause (inferred, phase 8's record). |
| `Test_main::test_accepts_a_settled_local_root_and_names_it[report]` | 0.56 s | 1 | 1 | Unchanged: one process, as `[apply-empty]` (inferred). |
| `Test_main::test_refuses_a_git_or_gh_that_did_not_answer_in_local_mode[merge_order]` | 0.52 s | 7 | 7 | Kept: a refusal where git does not answer, in local mode. |
| `Test_module::test_the_command_is_reachable_by_the_name_a_document_gives_it` | 3.87 s | 1 | 1 | Unchanged: the launcher run as a process, whose fact is that the name resolves. |
| `Test_module::test_a_spec_moved_into_place_is_ordered_by_the_commit_that_moved_it` | 1.07 s | 11 | 11 | Kept: `rule_changes.order` over a `git mv`, the reader case of `order`. |
| `Test_module::test_merge_order_is_the_commit_that_adds_the_spec` | 0.98 s | 10 | 10 | Kept: the reader case of `rule_changes.order`. |
| `Test_module::test_merge_order_of_local_specs_is_their_merge_commits_place` | 0.93 s | 9 | 9 | Kept: the reader case of `rule_changes.merge_order`. |
| `Test_module::test_a_ref_that_does_not_resolve_is_refused_rather_than_empty` | 0.78 s | 6 | 1 | Kept real over `tree_copy`: `resolves` against a ref git does not have; `tree` copied in place of built. |
| `Test_module::test_merge_order_of_an_id_that_is_not_ascii_is_its_designs_add` | 0.69 s | 7 | 7 | Kept: `order` over a path git quotes unless `-z`. |
| `Test_report::test_a_released_work_item_whose_id_is_not_ascii_is_a_candidate` | 2.21 s | 14 | 9 | Kept real over `tree_copy`: the reader case of `released`, a path git quotes unless `-z`. This instance carries the build of `_tree_world`. |
| `Test_report::test_the_git_calls_do_not_grow_with_the_plans_read` | 1.80 s | 20 | 20 | Unchanged: its fact is the number of git calls, counted over `removals` at `v0.2.0~1` and at `main`, so `earlier_judgments` stays real. |
| `Test_report::test_a_plan_added_where_another_is_deleted_names_its_release` | 1.76 s | 19 | 10 | Kept real: `earlier_judgments` over a history whose commits one `git fast-import` writes (`committed` or `removed_plan`); the other readers are `answered`. `--no-renames` keeps the deletion beside an added plan. |
| `Test_report::test_every_open_row_is_listed_with_the_paths_it_names` | 1.69 s | 15 | 10 | Kept real over `tree_copy`: the reader case of `git_fields`, the paths a row names as git lists them. |
| `Test_report::test_a_plan_is_read_once_at_its_newest_deletion` | 1.66 s | 16 | 7 | Kept real: `earlier_judgments` over a history whose commits one `git fast-import` writes (`committed` or `removed_plan`); the other readers are `answered`. |
| `Test_report::test_a_removing_commit_that_deleted_two_plans_is_one_commit_of_the_window` | 1.43 s | 15 | 7 | Kept real: `earlier_judgments` over a history whose commits one `git fast-import` writes (`committed` or `removed_plan`); the other readers are `answered`. |
| `Test_report::test_the_report_lists_what_an_apply_would_remove` | 1.20 s | 9 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_report::test_lists_a_design_with_a_line_its_reader_did_not_read_to_read_whole` | 1.12 s | 5 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_report::test_prints_the_section_where_it_holds_only_the_line_of_older_commits` | 1.11 s | 10 | 7 | Kept real: `earlier_judgments` over a history whose commits one `git fast-import` writes (`committed` or `removed_plan`); the other readers are `answered`. The window's count is git's list of removing commits. |
| `Test_report::test_a_spec_less_directory_is_listed_as_stating_no_rule` | 1.04 s | 7 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_report::test_a_plan_git_holds_no_text_for_is_named_and_none_of_its_rows_printed` | 1.03 s | 11 | 11 | Kept real: `git cat-file --batch` answers `missing` for a blob the case removes from the object store. |
| `Test_report::test_a_plan_deleted_where_another_is_added_is_still_read` | 1.00 s | 12 | 8 | Kept real: `earlier_judgments` over a history whose commits one `git fast-import` writes (`committed` or `removed_plan`); the other readers are `answered`. One commit deletes a plan and adds another. |
| `Test_report::test_names_a_misplaced_design_and_plan_as_not_read` | 0.99 s | 9 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_report::test_a_deleted_plan_whose_directory_stands_is_not_an_earlier_one` | 0.94 s | 7 | 4 | Kept real: `earlier_judgments` over a history whose commits one `git fast-import` writes (`committed` or `removed_plan`); the other readers are `answered`. |
| `Test_report::test_names_a_gaps_md_away_from_its_place_as_not_read` | 0.92 s | 7 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_report::test_a_removed_plan_of_a_non_ascii_id_is_read` | 0.89 s | 11 | 7 | Kept real: `earlier_judgments` over a history whose commits one `git fast-import` writes (`committed` or `removed_plan`); the other readers are `answered`. The path is one git quotes unless `-z`. |
| `Test_report::test_an_unreleased_work_item_is_not_a_candidate` | 0.87 s | 5 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_report::test_prints_no_section_where_nothing_is_misplaced` | 0.81 s | 7 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_report::test_refuses_nothing_and_writes_and_removes_nothing` | 0.80 s | 7 | 0 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. |
| `Test_report::test_accepts_a_spec_with_no_rule_changes_and_lists_it_to_read_whole` | 0.74 s | 5 | 5 | A call with every reader answered, over `answered_tree`: `tree`'s files copied from the module's one build with an empty `.git/`. The processes were `tree`'s build in this case's setup. This instance carries the build of `_tree_world`. |
| `Test_report::test_names_a_near_heading_in_a_removed_plan_and_reads_none_of_its_rows` | 0.74 s | 8 | 8 | Kept real: `earlier_judgments` over a plan `removed_plan` removes, unchanged. |
| `Test_report::test_names_a_plan_no_tag_holds_and_a_removal_no_number_names[an untagged commit]` | 0.67 s | 7 | 7 | Kept real: `earlier_judgments` and `versions` over a removal no tag holds, unchanged. |
| `Test_report::test_names_a_plan_no_tag_holds_and_a_removal_no_number_names[no commit]` | 0.54 s | 6 | 6 | As `[an untagged commit]`. |
| `Test_show::test_refuses_to_raise_on_a_byte_that_is_not_utf8` | 0.56 s | 8 | 8 | Kept: the reader class of `show`. |
| `Test_tracked_text::test_accepts_each_tracked_text_file_and_no_untracked_one` | 0.84 s | 7 | 7 | Kept: the reader class of `tracked_text`. |
| `Test_tracked_text::test_refuses_a_file_under_the_work_items_and_a_binary_file` | 0.64 s | 4 | 4 | Kept: the reader class of `tracked_text`. |
| `Test_versions::test_refuses_a_tag_of_another_shape_one_on_a_tree_and_an_untagged_commit` | 1.27 s | 16 | 16 | Kept: the reader class of `versions`. |
| `Test_versions::test_accepts_the_lowest_version_tag_by_number_an_annotated_one_peeled` | 1.17 s | 16 | 16 | Kept: the reader class of `versions`. |
| `Test_versions::test_accepts_a_version_tag_of_a_tag_at_the_commit_it_peels_to` | 1.00 s | 12 | 12 | Kept: the reader class of `versions`. |
| `test_census` | 1.35 s | 0 | 0 | Unchanged: it collects the module, its own cost. |

### Q2: the floor for this module

The module stays above 60 s on the Windows leg by every estimate this phase can make. Applied to the counts at `8ba07b5b0`, the fit of *Q1* puts it at 91.5 s, 96.1 s and 77.1 s at the rates of runs 45235848444, 45244493975 and 45249520034 (executed: `fit.py`). The fit's constant per case puts the 102 unlisted cases at 25 s to 31 s, above the 13.6 s to 17.3 s they measured in those runs. Taking those as measured and the 88 listed cases by the fit gives 80.3 s, 82.4 s and 66.1 s. Each figure is an estimate, and only the orchestrator's run at this phase's Status commit measures the module.

By verdict, at run 45235848444's rate (executed, `fit.py` over the verdicts of part 4):

| Verdict | Cases | Processes at `8ba07b5b0` | Seconds by the fit |
|---|---|---|---|
| The seven arm runs | 7 | 145 | 13.0 s |
| The reader classes' listed cases | 8 | 81 | 7.6 s |
| Kept over a real history, each with the agreement its fact is | 50 | 435 | 39.9 s |
| Unchanged, their own cost | 5 | 10 | 1.4 s |
| A call with its readers answered | 18 | 12 | 1.7 s |
| Not listed | 102 | 200 | 27.9 s, 16.8 s as measured at `f2fac912b` |

The floor item 13 states is the first two rows, about 21 s. What holds the module above 60 s is the third row. Each of its 50 cases holds an answer git gives a reader that no other case holds: a merge's `--cc` status of each shape, each answer of `is_ancestor` for a merge commit, each shape of a removed plan's history, and each release-list state beside the tag and adding commit `notes` reads. Answering them would put a description of git's output in place of git, which `frame/plan.md` A4 bars. So the phase keeps them and names each in part 4, as item 13 allows.

Two cuts remain that this phase did not make, and neither brings the module under 60 s by the fit.

- **`notes`' git part answered under the release-list cases.** Seven cases over `noted` vary only the `gh` answer and read the same tag and adding commit, 7 to 11 processes each. A seam under `notes`, answering `adding_commit` and `versions` from the world, would leave one of them reading git, about 4 s by the fit. `answered` answers `notes` whole and has no such seam, so this is a new seam in `settle.py`'s readers, which the frame does not ask for.
- **The conftest changes below**, about 5 s by the fit.

The module's figure above 60 s is the floor `frame/questions.md` Q2's second option names, and this record states why. Whether the module takes no further phase, as `tests/skills/test_chain_check.py` did, is the orchestrator's judgment on the run at the Status commit.

### What a change to `tests/conftest.py` would cut

The spawn bars `tests/conftest.py`. Three changes there would cut this module.

- **A module-scoped template of `#tree`.** This phase builds `tree`'s world once per module through `conftest.tree.__wrapped__`. A template in `tests/conftest.py`, copied per case as `#repo` copies `#_repo_template`, would give the same world without reaching past the fixture. It cuts nothing further here. Phase 8 names it (`gaps.md` *Not done*).
- **No `git rev-parse HEAD` in `#commit_everything`.** 37 call sites in the module still commit through it. Phase 1 names this trim (`gaps.md` *Not done*).
- **A `git fast-import` helper.** `imported` is this module's alone. In `tests/conftest.py` it would let `#commit_everything`'s callers here, and phase 7's `history` in `tests/skills/test_broad_gate.py`, write a history in one process.

### Checks at close

- `bin/test tests/skills/test_settle.py -q` passes 190 cases in 4.08 s, and `-p no:xdist` passes them in 15.14 s (executed, at `8ba07b5b0`).
- `bin/seal layout --check tests/skills/test_settle.py` refuses nothing and exits 0. Its 39 reports, each a function of `settle.py` with no class of its name, are the 39 it prints for the test file at `f2fac912b` (executed, over a copy removed after the run). `bin/seal layout --pairs tests/skills/test_settle.py` names no pair (executed).
- `bin/test <the 15 files that import from this module> -q --co -p no:xdist` collects 1,627 cases (executed; `frame/design.md` S4).
- The phase boundary set, `bin/test tests/skills/test_settle.py tests/behaviour tests/text -q`, passes 1,065 cases and skips 9 (executed, at `8ba07b5b0`).
- `uvx ruff format --check` leaves the file as it is and `uvx ruff check` passes it (executed).
- Every mutant run left `skills/settle/scripts/settle.py` and `skills/settle/scripts/rule_changes.py` as committed, and no probe file stands under `tests/` (executed: `git status --short` printed nothing after the last run).
- The suite as a whole is `unverified`: the broad gate is the orchestrator's.
