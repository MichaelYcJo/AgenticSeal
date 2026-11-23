# Design: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## Grounding

The tree as read at `5528a681f`. Its `tests/`, `skills/`, `lib/` and `.github/` are those of `ef776317b` and of `2156a1bb6`, the head of PR #1599 whose CI run is measured below (executed: `git diff --stat ef776317b 5528a681f` names only this work item's `routing.md`; `git diff --stat 2156a1bb6 ef776317b -- tests skills lib .github` prints nothing).

| Policy clause | What it fixes for this work |
|---|---|
| G1. `CONTRIBUTING.md` *The test layout*, the paragraph opening "A module's tests are written anew from the code when its old files cost past the threshold" | The six modules of issue #1581 are past the 60 s threshold, so each is rebuilt by this procedure. The threshold is read from the `test-durations` artifact, so the seconds below are that artifact's, summed by file. |
| G2. The same section, the paragraph opening "A rewritten module builds its world once and reads a command without git" | Two rules bind every phase. A fixture repository is built once in a module-scoped fixture, and a case that writes into it takes a copy, which is the reset. A case about how a command's input is read runs no real git and no real shell, and the real-git cases that stay are the ones showing that the reading and git agree. A case may sample one input of each kind where the mutation table shows the sample kills what the whole input space killed. |
| G3. The same section, the paragraph opening "A module's old cases get one verdict each when the module is rebuilt" | Each old case is placed as it stands, merged, cut or rewritten. A case whose assertion reads a document's prose stays where it is. A case is cut only where the mutation table shows another case kills every mutation it kills, or where its behaviour left the tree. |
| G4. The same section, the paragraph opening "A rebuilt module's record carries its move check or its mutation table" | Each phase record carries the four parts that paragraph lists: the move check or the mutation table, the module's cases and seconds before and after, the real-git cases kept by name, and one line per old case cut or rewritten with what holds its fact now. That last part is what the issue's second *Done when* bullet asks the pull request to name. |
| G5. `CONTRIBUTING.md` *Running the checks*, the paragraph opening "The durations union lives in `actions/cache`" | The artifact is the union of what the four Windows shards measured, each with `pytest-split==0.11.0`'s `--store-durations`. That plugin adds each case's setup, call and teardown seconds into one figure, dropping a setup or teardown past 600 s (read: `pytest_split/plugin.py#pytest_sessionfinish` and `STORE_DURATIONS_SETUP_AND_TEARDOWN_THRESHOLD` in the 0.11.0 wheel, fetched into scratch). So a module-scoped fixture's build is charged to the first case each xdist worker runs, and a module's figure is the sum of its cases' figures. |
| G6. `CONTRIBUTING.md` *The test layout*, its first paragraph, the sentence opening "A helper two test files use is defined once" | Other test files import names from four of the six modules. Each name stays importable at its home (*Data & interfaces*). |
| G7. `CONTRIBUTING.md` *Running the checks*, the paragraph opening "A contributor names a module" | Each phase runs the modules it names. The full suite stays the orchestrator's, run once after the review rounds settle. |
| G8. `seal/follow-up.md` *Schedulable items with nowhere else to go*, the row on `seal layout --moved` | Whether `--moved` is kept is the repository owner's question. This work makes its cases cheaper and does not answer it (*Scope*, out). |

**What each module costs, and where.** Read from the `test-durations` artifact of run 45181872904, the `pull_request` run at `2156a1bb6`, summed by file and by class (executed: `gh run download 45181872904 -n test-durations` into scratch, then a sum by the part of each id before `::`). The issue's own figures, from push run 45016511152 at v0.38.5, were reproduced by the same sum (executed).

| Module | Seconds | Cases | The classes that hold most of it |
|---|---|---|---|
| `tests/skills/test_chain_check.py` | 601 | 252 | `Test_pins_and_copies_in` 102 s, `Test_rule_changes_read` 99 s, `Test_main` 84 s, `Test_body` 84 s, `Test_originals_of` 66 s, `Test_guarantee` 52 s, `Test_check_lines_in` 35 s |
| `tests/skills/test_settle.py` | 253 | 190 | `Test_main` 195 s over 137 cases |
| `tests/skills/test_seal.py` | 107 | 389 | `Test_import_` 33 s, `Test_pr_checks` 17 s, `Test_switch` 13 s, `Test_mode` 12 s |
| `tests/skills/test_test_layout.py` | 106 | 88 | `Test_moved` 106 s over 47 cases |
| `tests/skills/test_broad_gate.py` | 105 | 204 | `Test_main` 42 s over 13 cases, `Test_gate` 38 s over 18, `Test_compare_at_base` 12 s |
| `tests/github/test_release_seal.py` | 95 | 60 | `Test_main` 89 s over 32 cases |

The same modules read 584, 254, 100, 109, 69 and 132 s in the v0.38.5 run (executed). Commits of this release changed two of them between the runs, so the difference is not a measured spread of the runner. The spread a module needs room for was measured after the frame, in the paragraph *What a figure of the Windows leg can show* below.

**Why each module costs what it does.**

- `tests/skills/test_chain_check.py`. The module already builds its main world once (`_branch_template`, `:240`) and copies it per case (`branch`, `:292`). One `chain_check.main` over a copy starts 41 git processes and takes 0.49 s on the framer's macOS machine. A copy takes 0.018 s. `put_spec` and `reviewed_to_head`, the commits a `Test_rule_changes_read` case adds, start 15 more and take 0.20 s (executed: `test_tmp_chain_spawns.py` in scratch, over a `git clone --no-local` at `5528a681f`, counting `subprocess.Popen` calls). The per-case figures of the hot classes on the Windows leg run from 2.2 s to 6.3 s, so most of a case's cost is its `check()` runs and its own commits. Several of those classes ask a question about reading text: what `## Rule changes` holds, what a check line resolves to, which test literal a `from` pins. Their arms can be reached without `main`. `pins_and_copies_in(root, rel, ops, sources)` reads git only where `sources` is empty, and `read_record` reads the disk where `WORKTREE` is set (read: `skills/code-review/scripts/chain_check.py:1267`, `:505`). The `item` fixture (`:2748`) builds a repository with `git init` and two commits for every case that takes it.
- `tests/skills/test_settle.py`. Its `repo` fixture (`:113`) runs `git init` and a commit for every case, through the module's own `git` (`:86`) and `commit` (`:101`). It shadows `tests/conftest.py#repo`, which copies one session-built template (`tests/conftest.py:682` to `:701`). Its `local` fixture (`:514`) shadows `tests/conftest.py#local` the same way. Most `Test_main` cases then commit their own history on that repository.
- `tests/github/test_release_seal.py`. `Test_main` stubs `gh` and git (`wired`, `:338`), so its cost is not git. `wired`'s default suite record holds 7,069 lines (`recorded(tmp_path, {"passed": 7003, "skipped": 66})`). Writing it takes 0.034 s and `suite_counts` over it takes 0.20 s on macOS, against 0.001 s for a record of seven lines (executed: `test_tmp_release_seal_cost.py` in scratch). That accounts for part of the 2.8 s a case costs on Windows, and not all of it.
- `tests/skills/test_test_layout.py`. Each `Test_moved` case runs `layout.main(["--moved", ...])` over a copy of `_moved_world` (`:701`). That adds a git worktree and runs `pytest --collect-only` twice in subprocesses (read: `skills/verify/scripts/test_layout.py#_collected`, `:1044`, and the worktree at `:1131`). The unit those cases are about, `moved(old, new, old_modules, new_modules)` (`:937`), takes texts.
- `tests/skills/test_seal.py`. #942's phase 5 already built its worlds once and copies them (`_worlds`, `:131`; `take`, `:171`). Its cost is `main` running real git in the process, one copy and many commands per case.
- `tests/skills/test_broad_gate.py`. `Test_gate` and `Test_main` run the fixture's one-test suite through a real `pytest` subprocess (the module docstring; `_repo_template`, `:1510`). `a_recorded_run` (`:1669`) already shares one recorded run across the cases that only read it.

**What other files import from these modules** (executed: `git grep` at `ef776317b` for `from <module> import` and `import <module>` under `tests/`). `test_settle`, `test_seal`, `test_broad_gate` and `test_test_layout` each give names to other files, and *Data & interfaces* lists each name with the files that import it.

**The search `frame/plan.md` phase 1 holds to printing nothing.** `git grep -n -E '^def (git|commit|repo)\(' 5528a681f -- tests/skills/test_settle.py` prints three lines, `:86`, `:101` and `:113` (executed). Each is a definition a `## Removes` row names. The pathspec names one test file, so the work item's directory is outside it.

**#1598's search inside the six modules.** #1598's own search (`git grep -n -E '\.split\("## |\.split\(heading|text\.split\(f?"#' -- 'tests/*.py'`, executed at `ef776317b`) prints two lines in these modules, `tests/skills/test_chain_check.py:5003` and `:5007`. Both cut a section of a document whose prose the case reads, so by G3 both cases stay as they stand and stay #1598's.

**What a figure of the Windows leg can show, measured after the frame.** The `workflow_dispatch` run 45189798316 at `2d343a752`, after phase 1, is the first CI figure of the branch. Between run 45181872904 and that run, `tests/skills/test_settle.py` is the one tested path that changed (executed: `git diff --stat 2156a1bb6 2d343a752 -- tests skills lib .github bin hooks` names that file alone). The orchestrator summed both artifacts by module, and the framer summed them again with the same result (executed):

| Module | Run 45181872904 | Run 45189798316 | Ratio |
|---|---|---|---|
| `tests/skills/test_chain_check.py` | 601 s | 502 s | 0.84 |
| `tests/skills/test_settle.py` | 253 s | 208 s | 0.82 |
| `tests/github/test_release_seal.py` | 95 s | 93 s | 0.98 |
| `tests/skills/test_test_layout.py` | 106 s | 103 s | 0.97 |
| `tests/skills/test_seal.py` | 107 s | 78 s | 0.74 |
| `tests/skills/test_broad_gate.py` | 105 s | 79 s | 0.74 |
| the rest of the suite | 574 s | 540 s | 0.94 |

The modules of the rest that cost more than 20 s in run 45181872904 moved by 0.82 to 1.01 between the same two runs (executed, the same sums). Every later phase, and the orchestrator reading its figure, works by three readings of this table:

- With nothing changed, a module's seconds on the Windows leg move by up to about a quarter from one run to the next. A module's ratio between two runs is a saving only where it falls below the ratios that the modules no phase has changed show between the same two runs. Phase 1's ratio of 0.82 falls inside that range, so the leg shows no saving from phase 1.
- The bound is read in one run, and that run can be slower than another by the same spread. A phase therefore aims its module at about 44 s, which is 60 s times the lowest ratio above, so that the module stays under 60 s in a run that much slower.
- A local figure is no evidence of a saving on the Windows leg. Phase 1's local run fell from 57.7 s to 38.4 s, and 13.2 s of the 57.7 s was the first run of a newly written `gh` stub, a cost of macOS that the Windows leg did not show (read: `trail/phases/phase-1.md`, *Q1* and the second of the four parts). The local figures still serve the phase record's second part and the profile `frame/questions.md` Q1 asks for.

## Scope

In scope, numbered for `frame/plan.md`'s *Delivers* cells:

1. `tests/skills/test_settle.py` is rebuilt by G1 to G4. Its repositories are built once per module, one for each kind of world its classes need, such as a shared root with a merge history or a local root with the `gh` stub. A case that writes takes a copy. The module's own `git`, `commit` and `repo` go, and so does the shadowing `local` where a module world replaces it.
2. `tests/skills/test_chain_check.py`, the arm classes: `Test_pins_and_copies_in`, `Test_rule_changes_read`, `Test_check_lines_in`, `Test_body`, `Test_originals_of`, `Test_guarantee` and `Test_broad_gate`. A case about what an arm reads calls that arm with its input given in the process: the design text, the `sources` dict, a working tree read under `WORKTREE`, or `read_record` and `git` replaced for the case. An arm keeps the cases that run `main` over a real repository where their fact is what `main` hands the arm, such as which design `Test_rule_changes_read` receives, and at least one where the base held one, to show that `main` reaches the arm and that the reading and git agree; `Test_broad_gate` ran no `main` at the base and runs none (`trail/phases/phase-2.md`). The `item` world is built once per module and copied per case, as `branch` copies `_branch_template`.
3. `tests/skills/test_chain_check.py`, every other class, `Test_main` and the git predicates among them, by the same rules, and the module's record for items 2 and 3 together.
4. `tests/github/test_release_seal.py`. The phase first measures where `Test_main`'s seconds go. Each case then gets the smallest suite record that holds its fact, and the cases that need a wide count keep it.
5. `tests/skills/test_test_layout.py`. A `Test_moved` case about which old case the new files hold calls `moved` with texts. The cases that run `main --moved` are the ones about the count `pytest` collects, the worktree's removal and the exit code.
6. `tests/skills/test_seal.py`. The cases of `main` that ask how input is read become unit calls. The real-git runs that stay are those showing that a command and git agree.
7. `tests/skills/test_broad_gate.py`. A case about how the gate reads a run's record reads a hand-built record (`a_record`, `jsonl`, `a_test`). The real `pytest` runs that stay are one per kind of answer the gate gives a run, shared through module-scoped fixtures where cases only read them.
8. Each phase's record holds G4's four parts. The second part also gives the module's figure in run 45181872904's artifact, and the local figures come from `bin/test <module> -q -p no:xdist`. With xdist off, pytest's wall time is the sum of the cases' setup, call and teardown, the quantity G5 says the artifact sums. `CONTRIBUTING.md`'s `bin/test <files> -q` runs under `-n auto`, which divides that sum by the workers. The local figures show where the time went on the machine that built the phase, and are no evidence of a saving on the Windows leg (*Grounding*, *What a figure of the Windows leg can show*). The module's Windows figure after the phase is the orchestrator's, by S1.
9. Every name in *Data & interfaces* stays importable at its home with its behaviour.
10. `tests/skills/test_settle.py`, the further rebuild the orchestrator decided after run 45189798316 (`frame/plan.md` *Judgments of the run*). A case of `Test_main`, `Test_report`, `Test_apply` or `Test_module` whose fact is how `settle.py` reads its input calls the reader with that input given in the process, as item 2 does for `test_chain_check.py`. The seams are `settle.py`'s own. `plan_rows`, `carries`, `work_items`, `misplaced` and `judgments` take text or records, and `report`, `draft` and `apply` take the result of `survey`, so cases that judge one world's report can share one survey of it (read: `skills/settle/scripts/settle.py:1168`, `:625`, `:279`, `:1092`, `:1119`, `:1725`, `:1863`, `:1940`, `:1474`). A reader that itself asks git, such as `adding_commits`, `versions`, `history` or `earlier_judgments`, keeps its cases over a real history, since those show that the reading and git agree. Each arm of `main` keeps a few runs over a real history, and the phase record names each: the dry run's merge order, the release at a ref, the published note under `--apply`, the history earlier settles removed, `--from`, `--draft` and local mode. A change to `tests/conftest.py`, such as to `#tree` or `#commit_everything`, stays out, for the reason `gaps.md` *Not done* gives.

Out of scope:

- Moving inline section cuts onto `tests/conftest.py#section`, which is #1598's. A case this work writes or rewrites and that cuts a section calls `tests/conftest.py#section`, so the work adds no inline cut. The two cuts G3 keeps stay for #1598.
- Whether `seal layout --moved` is kept (G8).
- Any shipped module. No file under `lib/`, `skills/`, `.github/scripts/`, `bin/` or `hooks/` changes. Where a case can reach a fact only through `main`, it stays a real-git case, and the phase record says so (`frame/plan.md` *Alternatives considered*, A3).
- `tests/conftest.py#SLOW_CASE_S`, the legs' `timeout-minutes`, and the shard count of `.github/workflows/test.yml`.
- The modules under 60 s, such as `tests/skills/test_session_cost.py` at 49 s.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The six modules cost less than the threshold | Given the branch after each phase that closes a module, and after the last phase. When the Windows leg of `tests` measures it. Then each module a closed phase rebuilt sums under 60 s, or the phase record that rebuilt it states why it cannot, as G1's paragraph allows. | The orchestrator pushes the branch and runs `gh workflow run tests --ref perf/1581-six-test-modules-cost-past-the-60-s-rewrite-bound` at the Status commit of each phase that closes a module, phases 1, 3, 4, 5, 6, 7 and 8 of `frame/plan.md`, and once more after the review rounds settle, beside the broad run. For each run it calls `gh run download <that run's id> -n test-durations -D <dir>`, then `python3 -c "import collections, json, sys; d = json.load(open(sys.argv[1])); t = collections.Counter(); [t.update({k.split('::')[0]: v}) for k, v in d.items()]; [print(round(t[m]), m) for m in sys.argv[2:]]" <dir>/.test_durations tests/skills/test_chain_check.py tests/skills/test_settle.py tests/github/test_release_seal.py tests/skills/test_test_layout.py tests/skills/test_seal.py tests/skills/test_broad_gate.py`. It reads the phase's module against the modules no phase has changed in the same run, as *Grounding*, *What a figure of the Windows leg can show*, states, and writes its judgment with the run's id in `frame/plan.md` *Judgments of the run*. The same sum over the pull request's own run measures the six again. The issue's *Done when* reads the first push run on `main` after the release, which `frame/questions.md` Q4 hands to the repository owner. No local figure stands in for any of these runs. |
| S2. No old case leaves without its fact held | Given an old case of one of the six modules. When the rebuild cuts or rewrites it. Then the phase record names it, what it guarded, and the case or tree fact that holds it now, and the mutation table shows that every mutant it killed is killed. | The proofer reads each phase record's fourth part against `git diff <base>..<phase commit> -- <module>`. |
| S3. The rebuilt module is in the layout and passes | Given a phase's commit. When its module runs alone. Then every case passes and the layout check refuses nothing for the file and exits 0; its `report:` lines, which name functions with no class and stand at the base too, are not refusals. | `bin/test <module> -q` and `bin/seal layout --check <module>`, run by the crafter at the phase's close. |
| S4. The files that import from a module still import | Given a phase that rebuilt `test_settle.py`, `test_seal.py`, `test_broad_gate.py` or `test_test_layout.py`. When each file that imports from it is collected. Then collection succeeds. | `bin/test <each importing file> -q --co`, run by the crafter at the phase's close. The importers are listed under *Data & interfaces*. |
| S5. A world shared by cases is not changed by any of them | Given a module-scoped world. When the module's cases run in any order and on any number of workers. Then no case sees another case's writes. | Each module passes under `bin/test <module> -q`, which runs `-n auto`, and under `bin/test <module> -q -p no:xdist`, which runs its cases in file order. The proofer reads each case that writes for the copy it writes into. |

## Data & interfaces

No shipped interface changes. The test-side names other files import, which stay at their homes with their behaviour (Scope item 9):

- `tests/skills/test_settle.py#unanswered`, imported by `tests/evals/test_noninferiority.py`, `tests/github/test_close_issues_on_release.py`, `tests/github/test_dist_branch.py`, `tests/github/test_plugin_directory_check.py`, `tests/github/test_publish_release_note.py`, `tests/github/test_release_seal.py`, `tests/github/test_roll_flow_measurement_issue.py`, `tests/github/test_tag_release.py`, `tests/skills/test_broad_gate.py`, `tests/skills/test_chain_check.py`, `tests/skills/test_pact_check.py`, `tests/skills/test_pr_wait.py`, `tests/skills/test_seal_stamp.py`, `tests/skills/test_session_cost.py` and `tests/skills/test_test_layout.py`.
- `tests/skills/test_settle.py#past_the_bound`, imported by each file of that list that stands under `tests/skills/`.
- `tests/skills/test_seal.py#configured`, imported by `tests/skills/test_broad_gate.py`, `tests/skills/test_fold_check.py` and `tests/skills/test_rules.py`.
- `tests/skills/test_seal.py#tool`, imported by `tests/skills/test_broad_gate.py`, `tests/skills/test_fold_check.py` and `tests/skills/test_settle.py`.
- `tests/skills/test_broad_gate.py#unquoted_flat`, imported by `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`.
- `tests/skills/test_broad_gate.py#gate_module`, imported by `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py`.
- `tests/skills/test_test_layout.py#layout`, imported by `tests/behaviour/test_this_repository_passes_its_own_checks.py`.

## Rule changes

- nothing
  why: The work rewrites six test modules by the procedure `CONTRIBUTING.md` *The test layout* already states, and changes no rule of the policy root.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The module's own git runner | `tests/skills/test_settle.py#git` | `tests/conftest.py#git` and `#git_out`, the runners every other module uses |
| The module's own commit helper | `tests/skills/test_settle.py#commit` | `tests/conftest.py#commit_everything` |
| A repository built with `git init` and a commit for every case, shadowing the shared fixture | `tests/skills/test_settle.py#repo` | module-scoped worlds of Scope item 1, copied per case |
| The per-case `git init` and commits inside the fixture | `tests/skills/test_chain_check.py#item` | a module-scoped template copied per case, as `#branch` copies `#_branch_template`; the fixture's name may stay |
| Real-git `main` runs in cases whose fact is how an arm reads its input | the classes Scope items 2, 3, 5, 6, 7 and 10 name | unit calls on the arm, with the real-git `main` cases each arm keeps under its *Scope* item named in the phase record |
| Old cases whose fact another case holds | the six modules | each named, with the case that holds its fact, in the fourth part of its phase record (G4) |

The work adds no gate, check, hook, CI step, rule, line grammar, label or mark, so it owes no removal in return.

Framed 2026-11-23 by framer, before the build.
