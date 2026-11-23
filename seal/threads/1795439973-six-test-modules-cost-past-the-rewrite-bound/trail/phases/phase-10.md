# Phase 10: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## What this phase found

### The frame, read against the tree before the build

The frame holds for `tests/skills/test_seal.py` at `b9d8d4ade`. The module, `tests/conftest.py`, `skills/implement/scripts/seal.py` and `lib/` are as they stood at `3e1c2a5d5`, phase 6's Status commit, and at `d994cc908`, the commit run 45218254995 measured (executed: `git log 3e1c2a5d5..b9d8d4ade` over those paths prints nothing). So runs 45218254995, 45224596129 and 45235848444 all measured the file this phase starts from. The 23 cases *Scope* item 12 takes from run 45218254995 stand in the module under their names, and with every case of `Test_pr_checks`, `Test_mode` and `Test_switch` they make 72 instances (executed: `listed.txt` in this phase's scratch, built from that run's artifact and the collected ids). `lib/optin.py#home_at` stands at `:275` and `resolve` asks it at `skills/implement/scripts/seal.py:346`, as item 12 says (read). The phase changes no shipped file.

Two facts the frame does not state. First, `tests/conftest.py` already empties `GIT_TEMPLATE_DIR` for the whole suite (`tests/conftest.py:263`, read), so the module's worlds hold no hook samples, and a world's copy is 28 to 62 files and directories, not more (executed: a count over each world, by a probe removed after the run). Second, `home_at` and `home_paths` read the disk alone where `.git` is a directory (`lib/optin.py#git_common_dir`, read). A case whose fact is the root's name beside a project's own `seal/` package therefore needs the package's files on disk, not its history.

### Q1: where the module's seconds went before the rebuild

**On the Windows leg.** The three runs put the module at 49.5 s, 80.6 s and 69.8 s (executed: the sum by case over `1581-dispatch-5/`, `-6/` and `-7/` `.test_durations` in this session's scratchpad). By class, in that order: `Test_pr_checks` 9.6 s, 10.3 s, 14.4 s; `Test_mode` 7.2 s, 15.9 s, 10.2 s; `Test_switch` 7.1 s, 15.1 s, 10.9 s; `Test_import_` 6.4 s, 16.8 s, 9.1 s; `Test_refusals` 2.6 s, 5.1 s, 4.0 s. Split by what a case does locally, the 130 cases that start a process, in setup or call, cost 39.1 s, 60.9 s and 58.4 s, at a median of 0.20 s, 0.24 s and 0.30 s a case. The 101 that copy a world and start no process cost 8.8 s, 16.8 s and 9.6 s, at a median of 0.04 s to 0.06 s. The 158 that do neither cost 1.6 s, 2.9 s and 1.8 s (executed, against the local counts below).

**On this macOS machine, setup apart from the call.** A pytest plugin in this phase's scratch (`tmp_spawn_probe.py`) timed each case's setup, call and teardown, counted the processes each phase of a case starts in the test process, by subcommand and by the function that started them, and counted the directories each copy walks. `bin/test tests/skills/test_seal.py -q -p no:xdist -p tmp_spawn_probe --durations=0` at `b9d8d4ade` passed 389 cases in 11.38 s, 1.79 s of it in setup and 8.74 s in calls (executed). The cases started 607 processes: 109 in setup and 498 in calls.

- **The build of `_worlds`.** 20 processes and 0.31 s, in the setup of the first case of the file, `Test_module::test_accepts_the_command_a_person_types`, whose call starts one. Three of the 20 were `tests/conftest.py#local_home`'s `git rev-parse --git-common-dir`, one per local root, and one the `rev-parse` of `commit_everything_as_e` for the gitlink worlds' commit.
- **`tests/conftest.py#package` and `#shared`.** 89 processes and 1.31 s, in the setup of 13 instances: 5 for `package` and 8 for `shared`, each instance.
- **The calls.** `main` started 259 processes. The module's own helpers started the rest: `commit_as_e` 64, `status` and `snapshot` 44, `refusals_of` 28, and each case's own git, such as the index states `Test_pr_checks` builds by hand. By class: `Test_pr_checks` 157, `Test_switch` 133, `Test_mode` 117, `Test_import_` 45, `Test_refusals` 35.

A fit of each run's per-case seconds against these counts, with a constant per case, gives 0.046 s, 0.071 s and 0.078 s for a process started in a call, 0.066 s, 0.130 s and 0.087 s for one started in setup, and 0.002 s to 0.003 s for each directory a copy walks (executed: `fit.py` in this phase's scratch). So on the leg the module's seconds stand first in the processes and second in the copies, about 0.05 s a copy. The world's build counts once in this fit, in file order. On the leg each worker that runs a case of the module builds it again. The four cases over 1.5 s in run 45218254995 that start two processes or fewer in their own call carry those builds, and in the two later runs three of them cost 0.02 s to 0.21 s (part 4).

### What the rebuild changed

`c8adb8bcb` does the rebuild.

- **A switch whose fact is a line it prints or a move it makes answers its guards.** The new fixture `guards_answered` replaces `porcelain` with a clean tree, `gitlinks_under_root` with no submodule and `other_worktrees` with none, so the switch starts git only to stage: `tracked`, then `git rm -r --cached` going local or `git add` going shared. Ten instances take it: the three pin lines of `Test_switch`, the door to shared mode, the rename the filesystem turns down, the three stage steps that do not answer, and the two `--apply` cases of `Test_mode`.
- **The root's name beside the package reads from the disk.** The new helper `beside_the_package` writes the files of `tests/conftest.py#PACKAGE` into a copy of a world and commits nothing. `optin.home_paths` and `optin.home_at` then name `agentic-seal/` as they do over `#package`, and each case asserts what `home_at` reads before it runs the command. Six instances moved off `#package` and `#shared` this way, those whose command asks git nothing past the top and the remote that `at_top` answers, or whose git is the switch's own over a tree with no history of the package: `seal export` in shared mode, `seal pr-checks install` with no root, the two blocked imports, the guard over an index git cannot list, and the switch to shared that git refuses to stage. The two imports read the module's zip in place of an export of their own.
- **Seven instances keep `#package` or `#shared`.** `Test_import_::test_s6_a_copy_travels_as_seal_and_lands_under_agentic_seal` runs `seal export` and `seal import` across a clone. `Test_mode::test_s1_first_setup_beside_the_package_puts_the_shared_root_at_agentic_seal` reads git's status of the committed package. `test_s6_mode_moves_agentic_seal_under_the_git_directory_and_back` stages the root both ways. The two guards over a staged edit and a submodule, and the switch going local under a held `index.lock`, read or write the index under the committed root. `Test_pr_checks::test_pr_checks_install_writes_the_workflow_beside_a_shared_agentic_seal` stages the workflow. So each of the four commands keeps a run over the fixture, as item 12 asks.
- **A file whose reading is the disk's is not committed.** The pin cases and the three instances of `Test_pr_checks::test_refuses_somebody_elses_file_and_leaves_it` write their workflow with `commit=False`. `workflow_at` reads the file on disk, and `install_workflow`, `remove_workflow` and the report decide on it before any git.
- **The worlds ask git less.** `_worlds` marks its three local roots at the place `optin.home_paths` gives, which asks git nothing where `.git` is a directory, in place of `tests/conftest.py#local_home`. The two gitlink worlds name the module's `SHA`, a commit of the submodule's own repository, so the shared world commits through `commit_as_e` with no `rev-parse`. The guard over a submodule under `agentic-seal/` names `SHA` too.

After the rebuild the module passes 389 cases and starts 495 processes, against 607: 66 in setup and 429 in calls (executed, the same plugin). The build of `_worlds` starts 16, the seven instances over `#package` or `#shared` 50, and `main` 207. By class: `Test_pr_checks` 146, `Test_switch` 95, `Test_mode` 84, `Test_import_` 27 and `Test_export` 15.

### Departures from the frame

- **`guards_answered` answers three readers of `seal.py`, not git.** *Scope* item 12 allows a case that keeps `main` "with the git it starts before the reading answered for the case", as item 6 does with `at_top`. The guards and the notes are the switch's reads of git before it moves anything. `frame/plan.md` A4 bars a fake of git's output, and phases 7, 8 and 9 answered a command's readers one level up in the same way (`trail/phases/phase-9.md`, *Departures from the frame*). Each answered reader keeps cases against git: `Test_porcelain`, `Test_gitlinks_under_root`, `Test_other_worktrees` and `Test_refusals`, and the instances of `Test_switch` and `Test_mode` that run the switch with them real (part 4, *Kept*).
- **`beside_the_package` writes the package's files, not its world.** Phase 6 took back module worlds built under the fixtures' own names, since that defined the world of `#package` and `#shared` a second time (`trail/phases/phase-6.md`, *Departures from the frame*). This helper builds no world: it writes `tests/conftest.py#PACKAGE`, imported, into a case's copy of a module world, with no commit, no `origin` and no root. A case that needs the package committed keeps the fixture. `CONTRIBUTING.md` *The test layout* keeps a helper two test files use in one place; the constant stays in `tests/conftest.py`, and `beside_the_package` is this module's alone.
- **Two parametrised cases became four functions.** `Test_mode::test_s6_mode_refuses_to_move_agentic_seal_over_what_its_index_holds` lost its `[an index git cannot list]` instance to `test_s6_mode_refuses_to_move_agentic_seal_over_an_index_git_cannot_list`, which runs beside the package's files, since a fixture a case takes cannot vary by its parameter. `test_s6_a_switch_that_could_not_stage_names_agentic_seal_in_the_command` became `…_going_local`, over `#shared` as before, and `…_going_shared`, beside the package's files. Each keeps the base's assertions, and the two beside the package's files add one on the root `optin` reads there.

### The four parts `CONTRIBUTING.md` *The test layout* asks of a rebuilt module

**1. The move check, and the mutation table.**

`bin/seal layout --moved b9d8d4ade --from tests/skills/test_seal.py --to tests/skills/test_seal.py` exits 1 at `c8adb8bcb` (executed). Its last line reads `seal layout: moved: 190 old cases, 388 items against 388 at b9d8d4adefb9, 127 failed`. 103 of the 127 fail on `fixture _worlds: its definition differs from the base's` alone, 13 on `body: stands for no old case` and 11 on `body: not in the new files unchanged`. So the mutation table carries part 1, as it did in phase 6.

The module's mutation table is the two tables here with `trail/phases/phase-6.md`'s first part, which gives each of mutants 1 to 114 its old and new lines. Each ran again against `c8adb8bcb` in two calls (executed), built by `run_mutants6.py` from a copy of phase 6's `mutants.py` in this phase's scratch: `bin/seal mutate skills/implement/scripts/seal.py --replace OLD NEW ... --tests "bin/test tests/skills/test_seal.py -q -x"`. The first printed `seal mutate: 49 mutants, 43 red, 6 SURVIVED, 0 with no verdict (171.8s)`, and the second `seal mutate: 65 mutants, 63 red, 2 SURVIVED, 0 with no verdict (186.0s)`. Every mutant red at `3e1c2a5d5` is red again, and the eight survivors are phase 6's: 1, 13, 14, 15, 27, 43, 94 and 113. Phase 6's record says why each lives.

Mutants 115 to 126 sit at the readers the rebuilt cases now reach without git: the name `optin.home_paths` gives the shared root, each place `seal.py` prints that name, and the switch's lines past the guards `guards_answered` answers. Each set ran in one call against `c8adb8bcb` (executed), built by `run_mutants10.py` from `mutants10.py` in this phase's scratch. The `lib/optin.py` call printed `seal mutate: 2 mutants, 1 red, 1 SURVIVED, 0 with no verdict (12.8s)`, and the `seal.py` call `seal mutate: 10 mutants, 9 red, 1 SURVIVED, 0 with no verdict (46.2s)`. The two survivors ran again against the test file at `b9d8d4ade`, copied to `tests/skills/test_tmp_seal_base.py` and removed after the run, and each survived there too (executed: each run printed `389 passed` with its mutant in place). So neither gap is this phase's.

- 116 changes nothing `home_paths` returns where a project's own `seal/` stands: with `agentic-seal/` left out of the search for a marked root, `home_paths` falls to its `lexists` test, which names `agentic-seal/` beside any `seal/`. It differs only where a marked `agentic-seal/` stands with no `seal/` beside it, which no case of the module builds.
- 118: no case reads the first line `seal export` prints in shared mode beside the package. The case asserts the way out, which mutant 117 breaks.

The phase adds no case for them: the frame rebuilds existing cases (`frame/design.md` *Scope* item 12), and `agents/crafter.md` *Never* bars building beyond the request. `gaps.md` *Not done* names them.

| # | Unit | `3e1c2a5d5` | `c8adb8bcb` |
|---|---|---|---|
| 1 | `resolve` | survived | survived |
| 2 | `resolve` | red | red |
| 3 | `resolve` | red | red |
| 4 | `export` | red | red |
| 5 | `export` | red | red |
| 6 | `export` | red | red |
| 7 | `export` | red | red |
| 8 | `export` | red | red |
| 9 | `export` | red | red |
| 10 | `export` | red | red |
| 11 | `export` | red | red |
| 12 | `import_` | red | red |
| 13 | `import_` | survived | survived |
| 14 | `import_` | survived | survived |
| 15 | `import_` | survived | survived |
| 16 | `import_` | red | red |
| 17 | `import_` | red | red |
| 18 | `import_` | red | red |
| 19 | `import_` | red | red |
| 20 | `import_` | red | red |
| 21 | `import_` | red | red |
| 22 | `import_` | red | red |
| 23 | `import_` | red | red |
| 24 | `import_` | red | red |
| 25 | `import_` | red | red |
| 26 | `pr_checks` | red | red |
| 27 | `pr_checks` | survived | survived |
| 28 | `pr_checks` | red | red |
| 29 | `pr_checks` | red | red |
| 30 | `pr_checks` | red | red |
| 31 | `mode_report` | red | red |
| 32 | `mode_report` | red | red |
| 33 | `mode_report` | red | red |
| 34 | `mode_report` | red | red |
| 35 | `mode_report` | red | red |
| 36 | `mode_report` | red | red |
| 37 | `mode_report` | red | red |
| 38 | `mode` | red | red |
| 39 | `mode` | red | red |
| 40 | `mode` | red | red |
| 41 | `mode` | red | red |
| 42 | `mode` | red | red |
| 43 | `mode` | survived | survived |
| 44 | `check` | red | red |
| 45 | `check` | red | red |
| 46 | `check` | red | red |
| 47 | `gitlinks_under_root` | red | red |
| 48 | `refusals` | red | red |
| 49 | `refusals` | red | red |
| 50 | `git_asked` | red | red |
| 51 | `root_files` | red | red |
| 52 | `work_item_of` | red | red |
| 53 | `work_item_digests` | red | red |
| 54 | `manifest_of` | red | red |
| 55 | `manifest_of` | red | red |
| 56 | `unused` | red | red |
| 57 | `write_zip` | red | red |
| 58 | `display` | red | red |
| 59 | `no_root` | red | red |
| 60 | `read_state` | red | red |
| 61 | `unsafe` | red | red |
| 62 | `unsafe` | red | red |
| 63 | `linked_path` | red | red |
| 64 | `linked_path` | red | red |
| 65 | `blocked_path` | red | red |
| 66 | `blocked_path` | red | red |
| 67 | `read_manifest` | red | red |
| 68 | `read_manifest` | red | red |
| 69 | `place` | red | red |
| 70 | `place` | red | red |
| 71 | `destination_root` | red | red |
| 72 | `destination_root` | red | red |
| 73 | `write_members` | red | red |
| 74 | `write_members` | red | red |
| 75 | `plain` | red | red |
| 76 | `doubled_keys` | red | red |
| 77 | `write_file` | red | red |
| 78 | `write_mode` | red | red |
| 79 | `indexed` | red | red |
| 80 | `indexed` | red | red |
| 81 | `other_worktrees` | red | red |
| 82 | `other_worktrees` | red | red |
| 83 | `workflow_at` | red | red |
| 84 | `left_workflow_line` | red | red |
| 85 | `install_workflow` | red | red |
| 86 | `install_workflow` | red | red |
| 87 | `remove_workflow` | red | red |
| 88 | `remove_workflow` | red | red |
| 89 | `remove_workflow` | red | red |
| 90 | `say_report` | red | red |
| 91 | `switch` | red | red |
| 92 | `switch` | red | red |
| 93 | `switch` | red | red |
| 94 | `hand_over` | survived | survived |
| 95 | `main` | red | red |
| 96 | `main` | red | red |
| 97 | `main` | red | red |
| 98 | `git` | red | red |
| 99 | `remote_url` | red | red |
| 100 | `head_sha` | red | red |
| 101 | `digest` | red | red |
| 102 | `zip_stem` | red | red |
| 103 | `state_path` | red | red |
| 104 | `write_state` | red | red |
| 105 | `serialized` | red | red |
| 106 | `porcelain` | red | red |
| 107 | `tracked` | red | red |
| 108 | `committed` | red | red |
| 109 | `staged_text` | red | red |
| 110 | `plugin_version` | red | red |
| 111 | `pinned` | red | red |
| 112 | `mode_refusal` | red | red |
| 113 | `both_roots` | survived | survived |
| 114 | `tool_command` | red | red |

| # | File | Unit | Old | New | `c8adb8bcb` | `b9d8d4ade` |
|---|---|---|---|---|---|---|
| 115 | `lib/optin.py` | `home_paths` | `shared = SECOND_HOME if os.path.lexists(os.path.join(root, HOME)) else HOME` | `shared = HOME` | red |  |
| 116 | `lib/optin.py` | `home_name_in` | `for name in (HOME, SECOND_HOME):` | `for name in (HOME,):` | survived | survived |
| 117 | `skills/implement/scripts/seal.py` | `export` | `name = display(repo, shared) print( "\nTo switch` | `name = optin.HOME print( "\nTo switch` | red |  |
| 118 | `skills/implement/scripts/seal.py` | `export` | `f"shared mode: the records are committed at {display(repo, shared)}/, "` | `f"shared mode: the records are committed at {optin.HOME}/, "` | survived | survived |
| 119 | `skills/implement/scripts/seal.py` | `install_workflow` | `name = display(repo, shared) or optin.HOME` | `name = optin.HOME` | red |  |
| 120 | `skills/implement/scripts/seal.py` | `import_` | `root_name = os.path.basename(into)` | `root_name = optin.HOME` | red |  |
| 121 | `skills/implement/scripts/seal.py` | `refusals` | `` # or reads: `optin.SECOND_HOME` where the project's own `seal/` stands. name = display(repo, shared) `` | `` # or reads: `optin.SECOND_HOME` where the project's own `seal/` stands. name = optin.HOME `` | red |  |
| 122 | `skills/implement/scripts/seal.py` | `switch` | `` # `home_paths` put it: the pathspec every git command below stages. name = display(repo, shared) `` | `` # `home_paths` put it: the pathspec every git command below stages. name = optin.HOME `` | red |  |
| 123 | `skills/implement/scripts/seal.py` | `switch` | `for path in other_worktrees(repo):` | `for path in other_worktrees(repo)[:0]:` | red |  |
| 124 | `skills/implement/scripts/seal.py` | `switch` | `print(f"  {left_workflow_line(text)}")` | `pass` | red |  |
| 125 | `skills/implement/scripts/seal.py` | `switch` | `for line in porcelain(repo, name): # `??` itself` | `for line in porcelain(repo, "seal"): # `??` itself` | red |  |
| 126 | `skills/implement/scripts/seal.py` | `switch` | `if workflow_at(repo)[0] == "absent":` | `if workflow_at(repo)[0] != "absent":` | red |  |

**2. Cases and seconds, before and after, on this macOS machine.** The figures are local. `frame/design.md` *Grounding*, *What a figure of the Windows leg can show*, takes no local figure as evidence of a saving on the Windows leg. The module's Windows figure is the orchestrator's `workflow_dispatch` run at this phase's Status commit (`frame/design.md` S1).

| | Cases | `-p no:xdist` | Setup | Calls | Processes |
|---|---|---|---|---|---|
| `b9d8d4ade` | 389 | 11.38 s | 1.79 s | 8.74 s | 607 |
| `c8adb8bcb` | 389 | 9.93 s | 1.16 s | 7.73 s | 495 |

(executed: `bin/test tests/skills/test_seal.py -q -p no:xdist -p tmp_spawn_probe --durations=0`, one run at each commit.) Under the default `-n auto` the module passes 389 cases in 3.23 s at `c8adb8bcb` (executed). The fit of *Q1*, applied to the counts at `c8adb8bcb`, puts the module at 43.6 s, 70.2 s and 60.7 s against the 49.5 s, 80.4 s and 69.6 s the three runs read for the same ids (executed: `predict.py` in this phase's scratch). That is an estimate of a cut of about 12 %, and it stands above the aim of about 37 s in each run.

**3. The real-git cases kept, by name.** The cases `trail/phases/phase-6.md`'s third part names stay: the export of the module's zip, the import over a copy, `mode --check` with `resolve`, the runs from a subdirectory and the runs outside any repository. Of the cases item 12 lists, 43 instances keep git real for the fact named in their verdict (part 4, *Kept*). They start 332 of the 364 processes the listed cases start. The four commands each keep one run beside the package over `tests/conftest.py#package` or `#shared`: `seal export` and `seal import` in `Test_import_::test_s6_a_copy_travels_as_seal_and_lands_under_agentic_seal`, `seal mode` in `Test_mode::test_s6_mode_moves_agentic_seal_under_the_git_directory_and_back` and `test_s1_first_setup_beside_the_package_puts_the_shared_root_at_agentic_seal`, and `seal pr-checks` in `Test_pr_checks::test_pr_checks_install_writes_the_workflow_beside_a_shared_agentic_seal`.

**4. One verdict per listed case.** The list is the 23 cases over 0.5 s in run 45218254995, then every case of `Test_switch`, `Test_mode` and `Test_pr_checks` not among them, 72 instances (`frame/design.md` *Scope* item 12). *Run 45218254995* is the case's seconds there. *Before* and *After* are the processes it starts in setup and call at `b9d8d4ade` and at `c8adb8bcb`, under its new name where it has one (executed, the plugin of *Q1*). A verdict is one of three: *Kept*, a real-git case with the agreement between the command and git it holds; `main` with readers answered, the git before the reading answered for the case; or a call to the reader whose fact the case is, here `optin.home_at`. *Unchanged* marks a case that already ran with its git answered, or a carrier of the build of `_worlds`, whose body stays as item 12 says. *As* gives a row the verdict of the instance it names.

| Case | Run 45218254995 | Before | After | Verdict |
|---|---|---|---|---|
| `Test_porcelain::test_accepts_a_tree_as_the_lines_under_the_paths_asked` | 2.03 s | 2 | 2 | Unchanged: it starts two processes of its own; its seconds in run 45218254995 were the build of `_worlds` it carried as the first case of its worker (1.5 s to 2.0 s there, 0.13 s and 0.21 s in runs 45224596129 and 45235848444). |
| `Test_module::test_accepts_the_command_a_person_types` | 1.58 s | 21 | 17 | Kept: the script run as a process from a subdirectory, the one case of the command a person types. It carries the build of `_worlds` in every run read (1.58 s, 2.01 s, 2.20 s), as the first case of the file. |
| `Test_mode_report::test_refuses_a_row_it_could_not_write_and_still_reports` | 1.54 s | 0 | 0 | Unchanged: it starts no process of its own; its seconds in run 45218254995 were the build of `_worlds` it carried as the first case of its worker (1.5 s to 2.0 s there, 0.02 s and 0.05 s in runs 45224596129 and 45235848444). |
| `Test_no_root::test_refuses_a_directory_outside_git_and_a_throwaway_clone` | 1.50 s | 0 | 0 | Unchanged: it starts no process of its own; its seconds in run 45218254995 were the build of `_worlds` it carried as the first case of its worker (1.5 s to 2.0 s there, 0.02 s and 0.03 s in runs 45224596129 and 45235848444). |
| `Test_mode::test_s6_mode_moves_agentic_seal_under_the_git_directory_and_back` | 1.47 s | 27 | 27 | Kept over `#shared`: `seal mode local` and `seal mode shared` stage the removal and the addition of `agentic-seal/` in git's index, the package untouched; the switch's one run each way beside the package. |
| `Test_mode::test_s6_a_switch_that_could_not_stage_names_agentic_seal_in_the_command[shared]` | 1.38 s | 21 | 5 | Became `test_s6_a_switch_that_could_not_stage_names_agentic_seal_going_shared`: a copy of the local world with the package's files on disk and an ignore rule over `agentic-seal/`; `git add` refuses the root `optin.home_paths` names, which the case now asserts. The first switch to local and its commit, which only set the state up, went. |
| `test_census` | 1.00 s | 0 | 0 | Unchanged: it reads the module's text and starts nothing; its own cost (1.0 s, 0.56 s, 0.96 s). |
| `Test_import_::test_refuses_a_zip_past_a_bound_before_reading_it[members]` | 0.84 s | 0 | 0 | Unchanged: it starts nothing; its seconds are writing and reading a zip of 20,001 members, which is the bound it holds. |
| `Test_switch::test_accepts_shared_to_local_by_moving_staging_and_writing_the_row` | 0.81 s | 17 | 17 | Kept: the switch's real staging both ways (`D  seal/` in git's status) with the committed workflow left out of the index; the guards and the notes real. |
| `Test_import_::test_s6_a_copy_travels_as_seal_and_lands_under_agentic_seal` | 0.80 s | 13 | 13 | Kept over `#package`: `seal export` and `seal import --into shared` across a clone `git clone` made, the one run of each command beside the package. |
| `Test_switch::test_accepts_the_way_back_it_names_from_a_subdirectory` | 0.79 s | 16 | 16 | Kept: run from a subdirectory through `resolve`'s own git, and the `git reset -- :/seal` it prints run by git there. |
| `Test_mode::test_s6_a_switch_that_could_not_stage_names_agentic_seal_in_the_command[local]` | 0.79 s | 14 | 14 | Became `test_s6_a_switch_that_could_not_stage_names_agentic_seal_going_local`, its body unchanged, over `#shared`: git refuses `git rm -r --cached agentic-seal` under a held `index.lock`; it needs the root committed beside the committed package. |
| `Test_import_::test_s6_an_import_names_what_blocks_it_in_the_root_by_the_roots_own_name[a file-is not a directory]` | 0.74 s | 9 | 0 | `home_at` called, then `main` with the top and remote answered and no git, both instances: a copy of the plain world with the package's files on disk and a marked `agentic-seal/`, and the module's zip in place of an export of its own; `optin.home_at` asserted to read `agentic-seal/`. `import_` asks git nothing past the top and the remote, which `at_top` answers. |
| `Test_pr_checks::test_refuses_a_staged_file_without_the_clone_line_deleted_by_hand[ D]` | 0.71 s | 8 | 8 | Kept: `remove` against the index git leaves holding somebody's committed file, deleted by hand. |
| `Test_pr_checks::test_pr_checks_install_writes_the_workflow_beside_a_shared_agentic_seal` | 0.66 s | 10 | 10 | Kept over `#shared`: `seal pr-checks install` writes and stages the workflow beside a committed `agentic-seal/`, the command's one run beside the package. |
| `Test_mode::test_s6_mode_refuses_to_move_agentic_seal_over_what_its_index_holds[a submodule]` | 0.65 s | 12 | 11 | Kept over `#shared`: `git ls-files --stage -- agentic-seal` lists the gitlink. The gitlink names the module's `SHA` where it named HEAD, one `rev-parse` fewer. |
| `Test_mode::test_s6_mode_refuses_to_move_agentic_seal_over_what_its_index_holds[a staged edit]` | 0.64 s | 11 | 11 | Kept over `#shared`: `git status -- agentic-seal` reads the staged edit under the root's own name. |
| `Test_pr_checks::test_pr_checks_install_names_agentic_seal_where_no_root_stands_beside_the_package` | 0.64 s | 5 | 0 | `home_at` called, then `main` with the top answered: a copy of the plain world with the package's files on disk; `optin.home_at` asserted to read no root, and `install_workflow` names `agentic-seal/`. No git. |
| `Test_mode::test_s1_first_setup_beside_the_package_puts_the_shared_root_at_agentic_seal` | 0.60 s | 11 | 11 | Kept over `#package`: first setup beside the committed package, whose `git status` shows nothing under `seal/` changed, and the switch's `nothing under agentic-seal/ was tracked` from git. |
| `Test_export::test_s6_export_in_shared_mode_names_agentic_seal_in_the_way_out` | 0.57 s | 8 | 0 | `home_at` called, then `main` with the top answered: a copy of the plain world with the package's files and a root at `agentic-seal/` on disk; `optin.home_at` asserted to read it. Export in shared mode asks git nothing past the top. |
| `Test_mode::test_s6_mode_refuses_to_move_agentic_seal_over_what_its_index_holds[an index git cannot list]` | 0.55 s | 9 | 1 | Became `test_s6_mode_refuses_to_move_agentic_seal_over_an_index_git_cannot_list`: a copy of the plain world with the package's files and a root at `agentic-seal/` on disk; `optin.home_at` asserted to read it, and `git ls-files --stage -- agentic-seal` raised as before; `main` starts one git process. |
| `Test_switch::test_accepts_shared_to_local_and_names_a_pin_that_is_not_the_installed_release[an-older-release]` | 0.54 s | 8 | 2 | `main` with `guards_answered`; the workflow written and not committed, since `workflow_at` reads the disk. `tracked` and `git rm --cached` stay git's. Same for the three instances. |
| `Test_other_worktrees::test_refuses_the_bare_directory_a_worktree_was_added_to` | 0.51 s | 7 | 7 | Kept: `other_worktrees` against `git worktree list` of a bare repository with a worktree added. |
| `Test_switch::test_accepts_shared_to_local_and_names_a_pin_that_is_not_the_installed_release[no-release-named]` | 0.50 s | 8 | 2 | As `[an-older-release]`. |
| `Test_switch::test_accepts_shared_to_local_and_names_a_pin_that_is_not_the_installed_release[a-version-it-cannot-read]` | 0.42 s | 8 | 2 | As `[an-older-release]`. |
| `Test_switch::test_accepts_local_to_shared_and_says_the_commit_is_the_door` | 0.36 s | 6 | 2 | `main` with `guards_answered`; `git add -- seal` stays git's, and `staged` reads what it staged. |
| `Test_switch::test_accepts_a_run_stopped_after_the_move_as_one_to_finish[local]` | 0.32 s | 7 | 7 | Kept: `indexed`'s moved arm over the pure deletions git's status shows after a move by hand, then the staging. |
| `Test_switch::test_accepts_a_run_stopped_after_the_move_as_one_to_finish[shared]` | 0.31 s | 5 | 5 | Kept, as `[local]`. |
| `Test_switch::test_accepts_an_untracked_file_as_travelling_with_the_folder[shared]` | 0.30 s | 6 | 6 | Kept: the note reads `??` from git's status under the root. |
| `Test_switch::test_accepts_an_untracked_file_as_travelling_with_the_folder[local]` | 0.35 s | 5 | 5 | Kept: the untracked file moves with the root and `git add` stages it. |
| `Test_switch::test_accepts_a_root_git_never_tracked_and_another_worktree` | 0.46 s | 6 | 6 | Kept: `tracked` reads nothing under `seal/` and `other_worktrees` a worktree `git worktree add` made. |
| `Test_switch::test_accepts_a_tracked_config_without_calling_it_untracked` | 0.50 s | 9 | 9 | Kept: git's status names the key `seal mode` wrote as ` M seal/config.json`, which the guard and the note read. |
| `Test_switch::test_refuses_what_its_refusals_name_and_moves_nothing` | 0.30 s | 5 | 5 | Kept: the guard reads a staged edit from git's status. |
| `Test_switch::test_refuses_a_rename_the_filesystem_turns_down_and_names_the_mv` | 0.05 s | 6 | 2 | `main` with `guards_answered`; its fact is the rename the filesystem turns down. `snapshot` still reads git's status before and after. |
| `Test_switch::test_refuses_to_call_a_stage_git_turned_down_staged` | 0.46 s | 8 | 8 | Kept: git refuses `git add -- seal` under an ignore rule, run from a subdirectory. |
| `Test_switch::test_refuses_to_call_a_stage_git_that_did_not_answer_staged[git rm going local]` | 0.23 s | 5 | 1 | `main` with `guards_answered`; the stage step's own git, `tracked` and the step that does not answer, is the case's. Same for the three instances. |
| `Test_switch::test_refuses_to_call_a_stage_git_that_did_not_answer_staged[git ls-files going local]` | 0.20 s | 4 | 0 | As `[git rm going local]`. |
| `Test_switch::test_refuses_to_call_a_stage_git_that_did_not_answer_staged[git add going shared]` | 0.18 s | 4 | 0 | As `[git rm going local]`. |
| `Test_mode::test_accepts_apply_moving_the_folder_to_the_row[shared-local]` | 0.29 s | 6 | 2 | `main` with `guards_answered`; its fact is the folder `--apply` moves; the staging stays git's. Same for both instances. |
| `Test_mode::test_accepts_apply_moving_the_folder_to_the_row[local-shared]` | 0.29 s | 5 | 1 | As `[shared-local]`. |
| `Test_mode::test_accepts_check_where_there_is_no_root` | 0.02 s | 0 | 0 | Unchanged: `main` with the top answered, no git. |
| `Test_mode::test_refuses_without_a_root_naming_both_places[argv0]` | 0.02 s | 0 | 0 | Unchanged: `main` with the top answered, no git; both instances. |
| `Test_mode::test_refuses_without_a_root_naming_both_places[argv1]` | 0.34 s | 0 | 0 | As `[argv0]`. |
| `Test_mode::test_refuses_check_where_no_repository_resolves` | 0.04 s | 1 | 1 | Kept: `git rev-parse --show-toplevel` outside any repository. |
| `Test_mode::test_refuses_apply_with_no_row_to_act_on[no row]` | 0.03 s | 0 | 0 | Unchanged: `main` with the top answered, no git; the three instances. |
| `Test_mode::test_refuses_apply_with_no_row_to_act_on[no mode]` | 0.03 s | 0 | 0 | As `[no row]`. |
| `Test_mode::test_refuses_apply_with_no_row_to_act_on[two rows]` | 0.05 s | 0 | 0 | As `[no row]`. |
| `Test_pr_checks::test_accepts_install_report_and_remove_in_turn` | 0.46 s | 7 | 7 | Kept: install stages, the commit holds it, and remove stages its removal, each against git. |
| `Test_pr_checks::test_accepts_remove_straight_after_install_before_a_commit` | 0.35 s | 7 | 7 | Kept: `remove` against the index git leaves after install staged a file never committed, and `git rm --force` restores the status. |
| `Test_pr_checks::test_refuses_a_staged_file_that_differs_and_leaves_it[index]` | 0.37 s | 7 | 7 | Kept: `remove` against the index git leaves holding an edited staged copy; both instances. |
| `Test_pr_checks::test_refuses_a_staged_file_that_differs_and_leaves_it[working copy]` | 0.27 s | 5 | 5 | As `[index]`. |
| `Test_pr_checks::test_accepts_remove_of_a_file_deleted_by_hand_the_index_still_holds[AD]` | 0.33 s | 7 | 7 | Kept: `remove` against the index git leaves holding a copy whose file was deleted by hand, and `git rm` takes it out; the three instances. |
| `Test_pr_checks::test_accepts_remove_of_a_file_deleted_by_hand_the_index_still_holds[ D]` | 0.49 s | 9 | 9 | As `[AD]`. |
| `Test_pr_checks::test_accepts_remove_of_a_file_deleted_by_hand_the_index_still_holds[ D, another release]` | 0.45 s | 8 | 8 | As `[AD]`. |
| `Test_pr_checks::test_refuses_a_staged_file_without_the_clone_line_deleted_by_hand[AD]` | 0.30 s | 6 | 6 | Kept: `remove` against the index git leaves holding somebody's staged file, deleted by hand. |
| `Test_pr_checks::test_refuses_an_index_copy_no_other_copy_keeps_deleted_by_hand[AD, a staged edit]` | 0.41 s | 8 | 8 | Kept: `remove` against the index git leaves holding a copy neither HEAD's nor the plugin's, read through `git diff --cached`; the three instances. |
| `Test_pr_checks::test_refuses_an_index_copy_no_other_copy_keeps_deleted_by_hand[AD, another release]` | 0.34 s | 7 | 7 | As `[AD, a staged edit]`. |
| `Test_pr_checks::test_refuses_an_index_copy_no_other_copy_keeps_deleted_by_hand[MD, a staged edit]` | 0.48 s | 9 | 9 | As `[AD, a staged edit]`. |
| `Test_pr_checks::test_refuses_an_index_entry_it_cannot_read_deleted_by_hand` | 0.40 s | 8 | 8 | Kept: `remove` against the index git leaves unmerged at three stages, which `git cat-file blob` cannot give. |
| `Test_pr_checks::test_accepts_remove_where_the_root_left_the_tree` | 0.36 s | 6 | 6 | Kept: `remove` against the index git leaves after a committed workflow is removed in local mode, a staged deletion. |
| `Test_pr_checks::test_refuses_install_in_local_mode_and_writes_nothing` | 0.03 s | 0 | 0 | Unchanged: `main` with the top answered, no git. |
| `Test_pr_checks::test_refuses_somebody_elses_file_and_leaves_it[]` | 0.16 s | 2 | 0 | `main` with the top answered and the file written and not committed, since whose file it is reads the disk before any git; no git, the three instances. |
| `Test_pr_checks::test_refuses_somebody_elses_file_and_leaves_it[install]` | 0.19 s | 2 | 0 | As `[]`. |
| `Test_pr_checks::test_refuses_somebody_elses_file_and_leaves_it[remove]` | 0.22 s | 2 | 0 | As `[]`. |
| `Test_pr_checks::test_refuses_to_call_an_install_git_turned_down_staged` | 0.39 s | 7 | 7 | Kept: git refuses `git add` under an ignore rule, from a subdirectory, and the `git add -f` the line names stages it there. |
| `Test_pr_checks::test_refuses_outside_a_repository` | 0.04 s | 1 | 1 | Kept: `git rev-parse --show-toplevel` outside any repository. |
| `Test_pr_checks::test_refuses_a_git_that_did_not_answer_and_keeps_the_index[install's git add]` | 0.16 s | 2 | 2 | Kept: one git run answered as not answering, the rest real, and `staged` reads the index unchanged; the six instances. |
| `Test_pr_checks::test_refuses_a_git_that_did_not_answer_and_keeps_the_index[install's git add refused with nothing on stderr]` | 0.13 s | 2 | 2 | As `[install's git add]`. |
| `Test_pr_checks::test_refuses_a_git_that_did_not_answer_and_keeps_the_index[remove's git diff --cached]` | 0.31 s | 6 | 6 | As `[install's git add]`. |
| `Test_pr_checks::test_refuses_a_git_that_did_not_answer_and_keeps_the_index[remove's git cat-file of a copy deleted by hand]` | 0.22 s | 4 | 4 | As `[install's git add]`. |
| `Test_pr_checks::test_refuses_a_git_that_did_not_answer_and_keeps_the_index[remove's git rm of a copy deleted by hand]` | 0.33 s | 6 | 6 | As `[install's git add]`. |
| `Test_pr_checks::test_refuses_a_git_that_did_not_answer_and_keeps_the_index[remove's git rm]` | 0.38 s | 6 | 6 | As `[install's git add]`. |

### Q2: the floor for this module

By the fit the module stands at 43.6 s, 70.2 s and 60.7 s at the three runs' rates: above the aim in each, and above 60 s in two. What stays is the floor this phase's verdicts leave. Of the 495 processes at `c8adb8bcb`, 332 stand in the 43 listed instances that keep git real, 16 of them the build of `_worlds` the first of them carries. 32 stand in the other listed instances, and 131 in cases item 12 does not list, `Test_refusals` (35), `Test_export` (15) and `Test_import_` (14) the largest (executed, the plugin of *Q1*). The kept instances hold facts only git gives: what `git rm --cached` and `git add` leave in the index after a switch, the index states `seal pr-checks remove` reads through `git diff --cached` and `git cat-file`, a gitlink or an unmerged entry under the root, and the refusals git gives under an ignore rule or a held `index.lock`. Answering them would put a description of git's index in place of git, which `frame/plan.md` A4 bars. The copies of the module's worlds, 210 a run, cost about 0.05 s each on the leg by the fit, 10 s or so in all.

Two cuts remain that this phase did not make. 58 of the 210 copies are left as the module built them by their case (executed: `tmp_write_probe.py` in this phase's scratch compared each world before and after its case). Handing those cases the module's world itself would save about 3 s by the fit, but a command that came to write there would change the world every later case of its worker reads, and no check would name the case that wrote. The second is the conftest change below.

### What a change to `tests/conftest.py` would cut

The spawn bars `tests/conftest.py`. Two changes there would cut this module.

- **Module-scoped templates of `#package` and `#shared`**, copied per case as `#repo` copies `#_repo_template`. The seven instances that keep the fixtures start 50 processes in setup; templates would leave one build of each per worker, 13 processes. Phases 3, 6 and 9 name the same change for their modules (`gaps.md` *Not done*).
- **No `git rev-parse HEAD` in `#commit_everything_as_e`.** The fixtures start it after each commit, 12 of the 50. Phase 1 names this trim (`gaps.md` *Not done*).

### Checks at close

- `bin/test tests/skills/test_seal.py -q` passes 389 cases in 4.44 s, and `-p no:xdist` passes them in 10.87 s (executed, at `c8adb8bcb`).
- `bin/seal layout --check tests/skills/test_seal.py` refuses nothing and exits 0; its two reports, no `Test_staged_text` and no `Test_tool_command`, stand against the test file at `b9d8d4ade` too (executed, over a copy of it removed after the run). `bin/seal layout --pairs tests/skills/test_seal.py` names one pair, `Test_pinned`'s two cases, which this phase did not touch (executed).
- `bin/test tests/skills/test_broad_gate.py tests/skills/test_fold_check.py tests/skills/test_rules.py tests/skills/test_settle.py -q --co` collects 490 cases (executed; `frame/design.md` S4). The four are every file under `tests/` that imports from this module (executed: `grep -rln "test_seal import" tests`).
- The phase boundary set, `bin/test tests/skills/test_seal.py tests/behaviour tests/text -q`, passes 1264 cases and skips 9 (executed).
- `uvx ruff format` leaves the file unchanged and `uvx ruff check` passes it (executed).
- Every mutant run left `skills/implement/scripts/seal.py` and `lib/optin.py` as committed, and no probe file stands under `tests/` (executed: `git status --short` prints nothing after the last run).
- The suite as a whole is `unverified`: the broad gate is the orchestrator's.
