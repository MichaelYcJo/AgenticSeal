# Phase 6: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## What this phase found

### The frame, read against the tree before the build

The frame holds for `tests/skills/test_seal.py`. Read at `d06a05ce1`: `_worlds` stands at `:131` and `take` at `:171`, as *Grounding* says, and every command case runs `SEAL.main` in the process through `said`. *Scope* item 6 says the cases that ask how input is read become unit calls. For most of this module that is not the cheaper cut: `export`, `import_`, `mode` and `pr_checks` read their input in long functions that take `args` and a working directory, and the git they run before the reading is `optin.toplevel`'s `git rev-parse --show-toplevel` and, for `import_` and `export`, `remote_url`'s `git config --get`. Replacing those two answers for a case, and leaving `main` to read the zip, the config or the workflow as it does, removes the processes without moving a case off the function it calls. The phase does that, and keeps the git whose answer is a case's fact. The departure is named below.

Three parts of the module started git it did not need at `d06a05ce1`. The helpers `roots`, `declared_in`, `config_at` and `refusals_of` called `SEAL.resolve`, which runs `git rev-parse --show-toplevel`, to learn paths that `optin.home_paths` and `optin.home_at` give without git where `.git` is a directory, as it is in every world here. `take` skipped a case where git refused a file-protocol submodule, and the two submodule worlds cloned a third repository with `git submodule add` to put a gitlink in the index. The phase rewrote the helpers and the worlds.

### Q1: where the module's seconds went before the rebuild

**On the Windows leg.** Run 45206461246's artifact puts the module at 107.3 s over 389 cases (executed: the sum by case over `1581-dispatch-3/.test_durations` in this session's scratchpad). By class: `Test_import_` 27.5 s over 58 cases, `Test_pr_checks` 17.1 s over 28, `Test_switch` 13.2 s over 18, `Test_mode` 11.7 s over 16, `Test_module` 6.3 s over 7, `Test_mode_report` 6.1 s over 17, `Test_write_state` 6.0 s over 2, `Test_refusals` 5.8 s over 17 and `Test_export` 3.8 s over 13. 62 cases cost over 0.5 s and 67.0 s together. Three of them hold the world's build, once for each of the three workers: `Test_module::test_accepts_the_command_a_person_types` 6.15 s, `Test_import_::test_accepts_missing_records_as_added_and_asks_nothing` 5.93 s and `Test_write_state::test_accepts_the_manifest_as_json` 5.90 s. The design's table gives `Test_import_` 33 s from another run.

**On this macOS machine.** `bin/test tests/skills/test_seal.py -q -p no:xdist --durations=0` at `d06a05ce1` passed 389 cases in 17.93 s (executed). A pytest plugin in this phase's scratch (`probe/tmp_spawn_probe.py`) counted the processes each case starts: 1181 over the module, 475 of them under `main` and the rest in the helpers and fixtures (executed). By git subcommand: `rev-parse` 510, `status` 212, `add` 92, `ls-files` 90, `commit` 60 and `config` 58. By who started them: `main` 475, `roots` 148, `status` 132, the `package` and `shared` fixtures of `tests/conftest.py` 89, `workflow_in` 48, `refusals_of` 44, `clone_at` 27 and `config_at` 20. A local fit of the artifact's per-case seconds against these counts gives about 0.07 s for each process the case starts and 0.016 s for the case itself on the Windows leg. So the module's seconds stood in the git processes, and most of those were `rev-parse --show-toplevel` asked again by a helper or by `resolve` for a top the case already knew.

### What the rebuild changed

`4c4fde94d` does the rebuild, and `3e1c2a5d5` returns `package` and `shared` to `tests/conftest.py`'s fixtures (see *Departures*).

- **The worlds are copies of one clone.** `_worlds` builds the clone with no root once and copies it into the local-mode, shared-mode and second local-mode worlds, so `git init` and the first commit run once. The two submodule worlds put a gitlink in the index with `git update-index --add --cacheinfo 160000,...` and commit it (`gitlink_at`), which is what `gitlinks_under_root` reads through `git ls-files --stage`. No world clones a repository, and `take` no longer skips.
- **`at_top` gives the top.** A case that runs a command at the top of its copy calls `at_top(repo)`, which replaces `optin.toplevel` for the case and fails it where the command asks for another directory. Given the `origin` the world was built with, it also replaces `remote_url`, in the export and import cases whose fact is not the remote. `Test_resolve` holds that git answers the top `at_top` gives, and `Test_remote_url::test_accepts_an_unset_origin_as_the_empty_answer` now also holds the `HTTPS` origin of the import's world.
- **The helpers read paths with no git.** `roots` reads `optin.home_paths`, and the new `home_of` reads `optin.home_at`; `declared_in`, `config_at` and `refusals_of` go through them. `Test_no_root`, `Test_mode_report` and `Test_switch` read the root through `home_of` where they called `SEAL.resolve`.
- **`tree` reads what a refusal leaves where no git writes the index.** It maps every path under the copy, `.git` among it, to a file's bytes, a link's target or a directory. The import refusals, `Test_mode_report`'s refusals, `seal mode --apply` with no row, and `seal pr-checks install` in local mode compare it in place of `snapshot`, which runs `git status`. The refusals of a switch and of `seal pr-checks remove` keep `snapshot`, since `git status` there is the fact.
- **`commit_as_e` commits with no `rev-parse`.** It runs `git add -A` and the commit, as `tests/conftest.py#commit_everything_as_e` does, and does not ask for the commit's hash, which no case here reads. The world that pins a gitlink to a commit still calls `commit_everything_as_e`.

After the rebuild the module starts 607 processes, against 1181 before (executed, the same plugin): `status` 120, `ls-files` 90, `add` 86, `rev-parse` 77, `commit` 56 and `worktree` 36. The rest is the staging of a switch and of `seal pr-checks`, the worlds, and the 89 processes of `package` and `shared`. By the local fit above, that is about 55 s on the Windows leg, under 60 s and above the aim of about 43 s. The fit is an estimate from one run. The figure that judges the phase is the Windows leg's, from the orchestrator's run at this phase's Status commit (`frame/design.md` S1).

### Departures from the frame

- **Most reading cases still call `main`.** *Scope* item 6 has the cases that ask how input is read become unit calls. `at_top` instead removes the git those cases ran before the reading, and the reading stays in the function the case names: `import_`'s bounds and names, `mode_report`'s rows and `pr_checks`'s report have no unit of their own to call, and a unit call would split a case off its class (`CONTRIBUTING.md` *The test layout*, *A case stands in the file of what it holds*). The design's aim is the processes, and the cases start 607 against 1181. `frame/plan.md` A4 bars a fake of git; `at_top` replaces one function of `optin` and one of `seal.py`, each with a case over real git that holds its answer.
- **`package` and `shared` are built per case, as before.** `4c4fde94d` built them once among the worlds under the fixtures' own names, which saved 89 processes. That defines the world of `tests/conftest.py#package` and `#shared` a second time, and `CONTRIBUTING.md` *The test layout* keeps a helper two test files use in one place; phase 3 read the rule the same way for these two fixtures. `3e1c2a5d5` returns the cases to the fixtures. A module-scoped template of each in `tests/conftest.py`, copied per case as `#repo` copies `#_repo_template`, would build them once for this module and for `tests/skills/test_chain_check.py`. The spawn bars `tests/conftest.py`, so `gaps.md` *Not done* names it.
- **`commit_as_e` stands beside `commit_everything_as_e`.** The rule above covers a helper two files use; `commit_as_e` is this module's alone and does a different thing, a commit with no hash read back. Making `tests/conftest.py#commit_everything_as_e` cheaper is the change phase 1 named and left to that file. It would cut 21 more processes here, the `rev-parse` after each commit of `package` and `shared`.

### The four parts `CONTRIBUTING.md` *The test layout* asks of a rebuilt module

**1. The move check, and the mutation table.**

`bin/seal layout --moved d06a05ce1 --from tests/skills/test_seal.py --to tests/skills/test_seal.py` exits 1 at `3e1c2a5d5` (executed). Its last line reads `seal layout: moved: 190 old cases, 388 items against 388 at d06a05ce1a0f, 202 failed`. Every case that takes `at_top`, `tree` or a world changed its body or a fixture, and no case was added or removed. So the mutation table carries part 1.

The mutants sit at the decision points of every function of `skills/implement/scripts/seal.py`, the classes the phase kept as they stand among them (`frame/plan.md` A2). Mutants 1 to 49 cover the functions whose cases the phase rewrote, `resolve`, `export`, `import_`, `pr_checks`, `mode_report`, `mode` and `check`, and the two readers of the rebuilt submodule worlds, `gitlinks_under_root` and `refusals`. Mutants 50 to 97 negate the first one to three conditions of each other function, by a script over the file's syntax tree, and 98 to 114 change the return of each function that holds no condition of its own. Each set ran in one call against `3e1c2a5d5` (executed): `bin/seal mutate skills/implement/scripts/seal.py --replace OLD NEW ... --tests "bin/test tests/skills/test_seal.py -q -x"`, built by `run_mutants.py` from `mutants.py` in this phase's scratch. The first printed `seal mutate: 49 mutants, 43 red, 6 SURVIVED, 0 with no verdict (188.8s)`, and the second `seal mutate: 65 mutants, 63 red, 2 SURVIVED, 0 with no verdict (199.2s)`. Under `-n auto`, `-x` stops the run with exit 2, which is the exit each red line shows. Each row shows the lines the mutant changes, joined. The full OLD and NEW of each are in `mutants.py`. The table measures this test file alone.

The base column is filled for a survivor alone. The eight survivors ran again against the test file at `d06a05ce1`, copied to `tests/skills/test_tmp_seal_base.py` and removed after each run. Those calls printed `seal mutate: 6 mutants, 0 red, 6 SURVIVED, 0 with no verdict (51.4s)` and `seal mutate: 2 mutants, 0 red, 2 SURVIVED, 0 with no verdict (22.6s)` (executed). So each gap is older than this phase, and the phase lost no fact that killed one. Why they live:

- 1, 27, 43 change nothing a case can see. With `if not repo` gone, `resolve` hands `""` to `optin.home_paths` and `optin.home_at`, and each returns empty for an empty root (`lib/optin.py:176`, `:300`). `install_workflow` returns no kind named `refused`. `seal mode`'s argument takes `nargs="?"` with `choices`, so `wanted` is `None` or a mode and never `""`.
- 13: no case hands `seal import` a directory as its zip.
- 14, 15: no case's zip holds exactly one member or one byte past a bound. The cases go past each bound by one record and also carry `manifest.json`, so a bound moved up by one still refuses them.
- 94: `hand_over` runs a tool as a child on Windows alone, and the table ran on macOS.
- 113: no case reads the whole of `both_roots`' text; the cases match its first words.

The phase adds no case for them, as phases 2 to 5 added none for theirs: the frame rebuilds existing cases (`frame/design.md` *Scope* item 6), and `agents/crafter.md` *Never* bars building beyond the request. 14 and 15 sit in `seal import`'s bounds, which keep a zip from costing memory and disk; no gate that refuses a pull request reads them. `gaps.md` *Not done* names the five that are gaps.

| # | Unit | Old | New | New file | `d06a05ce1` |
|---|---|---|---|---|---|
| 1 | `resolve` | `repo = optin.toplevel(cwd) if not repo: return "", "", "", "", ""` | `repo = optin.toplevel(cwd) if False: return "", "", "", "", ""` | survived | survived |
| 2 | `resolve` | `mode = "shared" if home and home == shared else "local" if home else ""` | `mode = "shared" if home else ""` | red |  |
| 3 | `resolve` | `mode = "shared" if home and home == shared else "local" if home else ""` | `mode = "local" if home else ""` | red |  |
| 4 | `export` | `return no_root(repo, shared, local)  if mode == "shared":` | `return no_root(repo, shared, local)  if mode == "none":` | red |  |
| 5 | `export` | `if os.path.isdir(target): target = unused(target, stem, ".zip")` | `if False: target = unused(target, stem, ".zip")` | red |  |
| 6 | `export` | `if gitcmd.inside(target, repo):` | `if not gitcmd.inside(target, repo):` | red |  |
| 7 | `export` | `if not target: print(f"no free name for` | `if target is None: print(f"no free name for` | red |  |
| 8 | `export` | `if not os.path.isdir(directory): print(f"{directory} is not a directory` | `if False: print(f"{directory} is not a directory` | red |  |
| 9 | `export` | `write_state(repo, manifest) print(f"wrote {target}")` | `print(f"wrote {target}")` | red |  |
| 10 | `export` | `for rel in links: print( f"  skipped the symbolic link` | `for rel in links[:0]: print( f"  skipped the symbolic link` | red |  |
| 11 | `export` | `if "remote" in unread:` | `if "head" in unread:` | red |  |
| 12 | `import_` | `repo, home, shared, local, _ = resolve(cwd) if not repo:` | `repo, home, shared, local, _ = resolve(cwd) if False:` | red |  |
| 13 | `import_` | `if not os.path.isfile(path): print(f"{path} is not a file")` | `if not os.path.exists(path): print(f"{path} is not a file")` | survived | survived |
| 14 | `import_` | `if len(members) > MEMBER_COUNT_LIMIT:` | `if len(members) > MEMBER_COUNT_LIMIT + 1:` | survived | survived |
| 15 | `import_` | `if declared > ARCHIVE_LIMIT:` | `if declared > ARCHIVE_LIMIT + 1:` | survived | survived |
| 16 | `import_` | `if info.filename.rstrip("/") == MANIFEST and info.file_size > MEMBER_LIMIT` | `if info.filename == MANIFEST and info.file_size > MEMBER_LIMIT` | red |  |
| 17 | `import_` | `if corrupt: print(f"{path} holds a member this command cannot read` | `if False: print(f"{path} holds a member this command cannot read` | red |  |
| 18 | `import_` | `refusals = [reason for info in members if (reason := unsafe(info))] if refusals:` | `refusals = [reason for info in members if (reason := unsafe(info))] if False:` | red |  |
| 19 | `import_` | `if mine is None: unreadable.append` | `if not mine: unreadable.append` | red |  |
| 20 | `import_` | `the_zip_is_silent = not isinstance(theirs, str)` | `the_zip_is_silent = theirs is None` | red |  |
| 21 | `import_` | `if unreadable and not args.allow_unreadable_remote:` | `if unreadable:` | red |  |
| 22 | `import_` | `if the_zip_is_silent: print( "Re-running this cannot change` | `if not the_zip_is_silent: print( "Re-running this cannot change` | red |  |
| 23 | `import_` | `if here and there and here != there and not args.allow_other_repo:` | `if here != there and not args.allow_other_repo:` | red |  |
| 24 | `import_` | `if here and there and here != there and not args.allow_other_repo:` | `if here and there and here != there:` | red |  |
| 25 | `import_` | `into, why = destination_root(repo, home, shared, local, args.into) if not into:` | `into, why = destination_root(repo, home, shared, local, args.into) if False:` | red |  |
| 26 | `pr_checks` | `repo = optin.toplevel(cwd) if not repo: print("not inside a git repository — seal works on a clone") return 1 if args.action == "install":` | `repo = optin.toplevel(cwd) if False: print("not inside a git repository — seal works on a clone") return 1 if args.action == "install":` | red |  |
| 27 | `pr_checks` | `return 0 if kind in ("written", "installed") else 1` | `return 0 if kind in ("written", "installed", "refused") else 1` | survived | survived |
| 28 | `pr_checks` | `return 0 if kind in ("written", "installed") else 1` | `return 0` | red |  |
| 29 | `pr_checks` | `return 0 if kind in ("removed", "absent") else 1` | `return 0` | red |  |
| 30 | `pr_checks` | `elif kind == "absent": print( f"not installed:` | `elif kind == "plugin": print( f"not installed:` | red |  |
| 31 | `mode_report` | `if kind == "refused": say_report(` | `if kind == "unknown": say_report(` | red |  |
| 32 | `mode_report` | `if kind == "none" and not args.check:` | `if kind == "none":` | red |  |
| 33 | `mode_report` | `if kind == "none" and not args.check:` | `if kind == "unknown" and not args.check:` | red |  |
| 34 | `mode_report` | `kind, value = "mode", current` | (line removed) | red |  |
| 35 | `mode_report` | `return 1 if args.check else 0 if kind == "none":` | `return 0 if kind == "none":` | red |  |
| 36 | `mode_report` | `if value == current: print("\nThey agree.")` | `if value: print("\nThey agree.")` | red |  |
| 37 | `mode_report` | `print(f"  seal mode {current:<11}correct the key to {current}, as the folder is") return 1 if args.check else 0` | `print(f"  seal mode {current:<11}correct the key to {current}, as the folder is") return 0` | red |  |
| 38 | `mode` | `if args.check: if not repo:` | `if args.check: if False:` | red |  |
| 39 | `mode` | `print("no seal/ here, so nothing is declared and nothing can disagree.") return 0` | `print("no seal/ here, so nothing is declared and nothing can disagree.") return 1` | red |  |
| 40 | `mode` | `if kind == "mode": wanted = value` | `if kind == "mode": wanted = None` | red |  |
| 41 | `mode` | `elif kind == "refused": print( f"{mode_refusal(home) or value}, so there is nothing to apply. "` | `elif kind == "unknown": print( f"{mode_refusal(home) or value}, so there is nothing to apply. "` | red |  |
| 42 | `mode` | `if kind == "unknown" else "is not declared"` | `if kind == "none" else "is not declared"` | red |  |
| 43 | `mode` | `if not wanted: return mode_report(` | `if wanted is None: return mode_report(` | survived | survived |
| 44 | `check` | `return no_root(repo, shared, local) if mode == "shared": # Never a failure.` | `return no_root(repo, shared, local) if mode == "local": # Never a failure.` | red |  |
| 45 | `check` | `if not last or not isinstance(last.get("items"), dict):` | `if not last:` | red |  |
| 46 | `check` | `1 for item in now if item in then and now[item] == then[item]` | `1 for item in now if item in then` | red |  |
| 47 | `gitlinks_under_root` | `if line.startswith("160000")` | `if line.startswith("100644")` | red |  |
| 48 | `refusals` | `if optin.marked(shared) and optin.marked(local): return [both_roots(shared, local)]` | `if False: return [both_roots(shared, local)]` | red |  |
| 49 | `refusals` | `if os.path.isdir(source) and os.path.lexists(destination):` | `if False:` | red |  |
| 50 | `git_asked` | `if done.returncode not in answered:` | `if not (done.returncode not in answered):` | red |  |
| 51 | `root_files` | `if os.path.islink(path):` | `if not (os.path.islink(path)):` | red |  |
| 52 | `work_item_of` | `if len(parts) >= 3 and parts[0] == optin.WORK_ITEMS:` | `if not (len(parts) >= 3 and parts[0] == optin.WORK_ITEMS):` | red |  |
| 53 | `work_item_digests` | `if item:` | `if not (item):` | red |  |
| 54 | `manifest_of` | `if url is not None:` | `if not (url is not None):` | red |  |
| 55 | `manifest_of` | `if head is not None:` | `if not (head is not None):` | red |  |
| 56 | `unused` | `if not os.path.lexists(path):` | `if not (not os.path.lexists(path)):` | red |  |
| 57 | `write_zip` | `if os.path.lexists(partial):` | `if not (os.path.lexists(partial)):` | red |  |
| 58 | `display` | `if gitcmd.inside(path, repo):` | `if not (gitcmd.inside(path, repo)):` | red |  |
| 59 | `no_root` | `if optin.opted_out(optin.git_common_dir(repo)):` | `if not (optin.opted_out(optin.git_common_dir(repo))):` | red |  |
| 60 | `read_state` | `if not path or not os.path.isfile(path):` | `if not (not path or not os.path.isfile(path)):` | red |  |
| 61 | `unsafe` | `if not name:` | `if not (not name):` | red |  |
| 62 | `unsafe` | `if "\\" in name:` | `if not ("\\" in name):` | red |  |
| 63 | `linked_path` | `if prefix in seen:` | `if not (prefix in seen):` | red |  |
| 64 | `linked_path` | `if os.path.islink(os.path.join(into, *prefix)):` | `if not (os.path.islink(os.path.join(into, *prefix))):` | red |  |
| 65 | `blocked_path` | `if info.is_dir() or not parts:` | `if not (info.is_dir() or not parts):` | red |  |
| 66 | `blocked_path` | `if prefix in members or (os.path.lexists(here) and not os.path.isdir(here)):` | `if not (prefix in members or (os.path.lexists(here) and not os.path.isdir(here))):` | red |  |
| 67 | `read_manifest` | `if not isinstance(manifest, dict):` | `if not (not isinstance(manifest, dict)):` | red |  |
| 68 | `read_manifest` | `if manifest.get("format") != FORMAT:` | `if not (manifest.get("format") != FORMAT):` | red |  |
| 69 | `place` | `if not os.path.lexists(destination):` | `if not (not os.path.lexists(destination)):` | red |  |
| 70 | `place` | `if not os.path.lexists(candidate):` | `if not (not os.path.lexists(candidate)):` | red |  |
| 71 | `destination_root` | `if optin.marked(shared) and local and optin.marked(local):` | `if not (optin.marked(shared) and local and optin.marked(local)):` | red |  |
| 72 | `destination_root` | `if into:` | `if not (into):` | red |  |
| 73 | `write_members` | `if info.is_dir() or name == MANIFEST:` | `if not (info.is_dir() or name == MANIFEST):` | red |  |
| 74 | `write_members` | `if not parts:` | `if not (not parts):` | red |  |
| 75 | `plain` | `if isinstance(value, repo_config.Members):` | `if not (isinstance(value, repo_config.Members)):` | red |  |
| 76 | `doubled_keys` | `if key in seen and key not in doubled:` | `if not (key in seen and key not in doubled):` | red |  |
| 77 | `write_file` | `if os.path.isdir(path):` | `if not (os.path.isdir(path)):` | red |  |
| 78 | `write_mode` | `if doubled:` | `if not (doubled):` | red |  |
| 79 | `indexed` | `if pair == "??":` | `if not (pair == "??"):` | red |  |
| 80 | `indexed` | `if pair == " M" and line[3:].strip() == f"{name}/{CONFIG}":` | `if not (pair == " M" and line[3:].strip() == f"{name}/{CONFIG}"):` | red |  |
| 81 | `other_worktrees` | `if common:` | `if not (common):` | red |  |
| 82 | `other_worktrees` | `if line.startswith("worktree "):` | `if not (line.startswith("worktree ")):` | red |  |
| 83 | `workflow_at` | `if PLUGIN_CLONE not in text:` | `if not (PLUGIN_CLONE not in text):` | red |  |
| 84 | `left_workflow_line` | `if version and pin == "v" + version:` | `if not (version and pin == "v" + version):` | red |  |
| 85 | `install_workflow` | `if not shared or not optin.marked(shared):` | `if not (not shared or not optin.marked(shared)):` | red |  |
| 86 | `install_workflow` | `if kind != "absent":` | `if not (kind != "absent"):` | red |  |
| 87 | `remove_workflow` | `if kind == "absent":` | `if not (kind == "absent"):` | red |  |
| 88 | `remove_workflow` | `if not tracked(repo, WORKFLOW):` | `if not (not tracked(repo, WORKFLOW)):` | red |  |
| 89 | `remove_workflow` | `if staged is None:` | `if not (staged is None):` | red |  |
| 90 | `say_report` | `elif kind == "unknown":` | `elif not (kind == "unknown"):` | red |  |
| 91 | `switch` | `if stop:` | `if not (stop):` | red |  |
| 92 | `switch` | `if wanted == SHARED:` | `if not (wanted == SHARED):` | red |  |
| 93 | `switch` | `if line[:2] == "??":` | `if not (line[:2] == "??"):` | red |  |
| 94 | `hand_over` | `if os.name == "nt":` | `if not (os.name == "nt"):` | survived | survived |
| 95 | `main` | `if argv and argv[0] in TOOLS:` | `if not (argv and argv[0] in TOOLS):` | red |  |
| 96 | `main` | `if args.command == "pr-checks":` | `if not (args.command == "pr-checks"):` | red |  |
| 97 | `main` | `if args.command == "export":` | `if not (args.command == "export"):` | red |  |
| 98 | `git` | `text, _ = git_asked(root, *args) return text or ""` | `text, _ = git_asked(root, *args) return ""` | red |  |
| 99 | `remote_url` | `"remote.origin.url", answered=(0, 1))` | `"remote.origin.url")` | red |  |
| 100 | `head_sha` | `return git_asked(root, "rev-parse", "HEAD")` | `return git_asked(root, "rev-parse", "HEAD~0")[0], ""` | red |  |
| 101 | `digest` | `running.update(rel.encode("utf-8"))` | (line removed) | red |  |
| 102 | `zip_stem` | `return f"seal-{base}-{when}"` | `return f"seal-{base}"` | red |  |
| 103 | `state_path` | `return os.path.join(common, STATE) if common else ""` | `return os.path.join(common, "x-" + STATE) if common else ""` | red |  |
| 104 | `write_state` | `json.dump(manifest, handle, indent=2, sort_keys=True)` | `json.dump({}, handle, indent=2, sort_keys=True)` | red |  |
| 105 | `serialized` | `return json.dumps(members, indent=2, ensure_ascii=False) + "\n"` | `return json.dumps(members, indent=2, ensure_ascii=False)` | red |  |
| 106 | `porcelain` | `return [line for line in (done.stdout or "").splitlines() if line.strip()]` | `return []` | red |  |
| 107 | `tracked` | `return bool([p for p in (done.stdout or "").split("\0") if p])` | `return True` | red |  |
| 108 | `committed` | `_text, why = git_asked(repo, "cat-file", "-e", f"HEAD:{rel}") return not why` | `_text, why = git_asked(repo, "cat-file", "-e", f"HEAD:{rel}") return True` | red |  |
| 109 | `staged_text` | `return done.stdout if done.returncode == 0 else None` | `return done.stdout` | red |  |
| 110 | `plugin_version` | `return version if isinstance(version, str) else ""` | `return version if version else ""` | red |  |
| 111 | `pinned` | `return found.group(1) if found else ""` | `return found.group(0) if found else ""` | red |  |
| 112 | `mode_refusal` | `return f"{config_path(home)} {doubled}" if doubled else ""` | `return ""` | red |  |
| 113 | `both_roots` | `Switching from here would leave the other where nothing reads it.` | `Switching from here would leave the other where nothing reads it.` | survived | survived |
| 114 | `tool_command` | `return [sys.executable, script, *argv]` | `return [sys.executable, script, *argv[1:]]` | red |  |

**2. Cases and seconds, before and after, on this macOS machine.** The figures are local. `frame/design.md` *Grounding*, *What a figure of the Windows leg can show*, takes no local figure as evidence of a saving on the Windows leg. The module's Windows figure is the orchestrator's `workflow_dispatch` run at this phase's Status commit (`frame/design.md` S1).

| Measure | Before, `d06a05ce1` | After, `3e1c2a5d5` |
|---|---|---|
| Cases of the module | 389 | 389 |
| Processes the cases start, counted by `probe/tmp_spawn_probe.py` under `-p no:xdist` | 1181 | 607 |
| `bin/test tests/skills/test_seal.py -q -p no:xdist`, the module | 17.93 s | 12.15 s |
| The same runs: `Test_import_`, `Test_pr_checks`, `Test_switch`, `Test_mode` | 4.20 s, 3.16 s, 2.45 s, 2.22 s | 1.44 s, 2.51 s, 2.02 s, 1.79 s |
| `bin/test tests/skills/test_seal.py -q`, under `-n auto` | 7.04 s | 4.54 s |
| Windows leg, the module, from the `test-durations` artifacts | 107 s in run 45181872904, 78 s in 45189798316, 92 s in 45203717820 and 107 s in 45206461246 | not measured |

The per-case figures of both local runs are in this phase's scratch, `before-durations.txt` and `after-durations.txt`, and the process counts in `probe/before.json` and `probe/after.json`. The `-n auto` figure before the phase ran over the file at `d06a05ce1` copied to `tests/skills/test_tmp_seal_base.py`, which the survivors' run used and which was removed after it.

**Q2: the floor.** The phase gives no answer to Q2 for this module, since no local figure is evidence of the Windows leg. What the module keeps is named in the third part below: the staging of a switch and of `seal pr-checks` over real git, the worlds built once for each worker, and `package` and `shared` built per case, 89 processes that a change to `tests/conftest.py` would build once.

**3. The real-git cases kept.** Every case keeps its world's real git; `at_top` replaces the top and the remote alone. These cases run `main` over real git with no `at_top`, and show that a command and git agree:

- `Test_export::test_accepts_a_local_root_as_a_zip_beside_the_clone` and the module's zip, which `_worlds` exports with `SEAL.main` from a copy of the local-mode world. They show that `export` resolves the top, reads the remote and HEAD through git and writes the manifest it records.
- `Test_import_::test_accepts_missing_records_as_added_and_asks_nothing` and `Test_import_::test_s6_a_copy_travels_as_seal_and_lands_under_agentic_seal`. They show that `import_` resolves the top and reads the remote through git and lands the records, the second in a clone `git clone` made.
- `Test_mode_report::test_accepts_check_writing_nothing_where_the_row_is_absent`, for `seal mode --check` through `resolve`'s own git.
- `Test_switch::test_accepts_the_way_back_it_names_from_a_subdirectory` and `Test_switch::test_refuses_to_call_a_stage_git_turned_down_staged`, which run `seal mode` from a subdirectory, and `Test_pr_checks::test_refuses_to_call_an_install_git_turned_down_staged`, which runs `seal pr-checks install` from one.
- `Test_mode::test_refuses_check_where_no_repository_resolves`, `Test_pr_checks::test_refuses_outside_a_repository`, the `not a repository` row of `Test_import_::test_refuses_a_path_that_is_no_zip_or_a_place_that_is_no_clone`, and `Test_main`'s cases as they stood, `test_refuses_a_git_that_did_not_answer_for_the_repository_as_no_repository` among them.

The cases that take `at_top` and keep real git for their fact are the switches and removals of `Test_switch`, `Test_mode` and `Test_pr_checks`, which read the index through `git status`, `git ls-files` and `git diff --cached`; the export and import cases about the remote, which take `at_top` with no remote (`Test_export::test_refuses_to_keep_quiet_about_a_remote_it_could_not_read`, `Test_import_::test_accepts_a_remote_absent_by_answer_on_either_side`, `test_accepts_each_flag_past_the_check_it_names`, `test_refuses_a_remote_either_side_could_not_read` and `test_refuses_a_zip_from_another_repository_naming_what_it_compared`); and the HEAD every export records. The unit classes that call a git reader of `seal.py` directly, such as `Test_git_asked`, `Test_remote_url`, `Test_head_sha` and `Test_other_worktrees`, keep their real git.

**4. Old cases cut or rewritten.** No case was cut and none added; 83 functions changed. A script in this phase's scratch, `rewritten.py`, undoes the four substitutions below in each changed body and compares it with the base's, ignoring white space; the bodies it names as changed otherwise are listed with what changed. Each assertion of the module is the base's.

- **`at_top` given, with the world's remote.** `Test_export`: `test_accepts_session_state_beside_the_root_and_leaves_it_out`, `test_accepts_a_link_in_the_root_as_skipped_and_named`, `test_accepts_a_taken_name_as_the_next_one`, `test_accepts_an_output_and_notes_one_inside_the_tree`, `test_refuses_without_a_root_or_in_a_throwaway_clone`, `test_refuses_a_partial_name_somebody_holds` and `test_refuses_an_output_with_no_directory_or_no_free_name`. `Test_import_`: `test_accepts_the_same_zip_twice_as_the_same_bytes`, `test_accepts_a_taken_name_by_landing_beside_it`, `test_accepts_into_either_root_and_defaults_to_local`, `test_accepts_a_manifest_another_machine_wrote_and_says_what_it_read`, `test_accepts_a_name_taken_during_the_write_by_naming_it`, `test_refuses_a_later_format_by_its_format_before_its_names`, `test_refuses_a_link_where_a_record_goes`, `test_accepts_a_broken_link_at_the_fallback_name_by_taking_the_next` and `test_refuses_a_directory_it_cannot_write_into_with_a_line_of_its_own`.
- **`at_top` given with the world's remote, and `tree` in place of `snapshot`.** `Test_import_`: `test_refuses_a_zip_past_a_bound_before_reading_it`, `test_refuses_a_member_that_does_not_read_before_the_manifest`, `test_refuses_a_manifest_this_build_cannot_read`, `test_refuses_a_member_it_has_no_place_for_and_writes_none`, `test_refuses_two_roots_whatever_into_says` and `test_refuses_a_name_one_side_holds_as_a_file`.
- **`at_top` given, and `tree` in place of `snapshot`.** `Test_import_`: `test_refuses_a_remote_either_side_could_not_read`, `test_refuses_a_zip_from_another_repository_naming_what_it_compared`, and `test_refuses_a_path_that_is_no_zip_or_a_place_that_is_no_clone`, which gives the top for every row but `not a repository` and gains a docstring saying so. `Test_mode_report`: `test_accepts_a_row_naming_the_folder_as_agreeing` and `test_refuses_a_config_that_will_not_read_at_exit_2`. `Test_mode::test_refuses_apply_with_no_row_to_act_on`. `Test_pr_checks::test_refuses_install_in_local_mode_and_writes_nothing`.
- **`at_top` given.** `Test_export`: `test_accepts_a_clone_with_no_commit_and_leaves_its_head_out`, `test_refuses_a_shared_root_and_names_the_way_to_local`, `test_refuses_to_keep_quiet_about_a_remote_it_could_not_read` and `test_s6_export_in_shared_mode_names_agentic_seal_in_the_way_out`. `Test_import_`: `test_accepts_a_remote_absent_by_answer_on_either_side`, `test_accepts_each_flag_past_the_check_it_names` and `test_s6_an_import_names_what_blocks_it_in_the_root_by_the_roots_own_name`. `Test_mode_report`: `test_accepts_an_absent_row_by_writing_the_folders_mode_once`, `test_refuses_a_row_naming_the_other_mode_and_names_both_ways_out`, `test_refuses_a_value_that_is_not_a_mode` and `test_refuses_a_row_it_could_not_write_and_still_reports`. `Test_switch`: `test_accepts_shared_to_local_and_names_a_pin_that_is_not_the_installed_release`, `test_accepts_local_to_shared_and_says_the_commit_is_the_door`, `test_accepts_a_run_stopped_after_the_move_as_one_to_finish`, `test_accepts_an_untracked_file_as_travelling_with_the_folder`, `test_accepts_a_root_git_never_tracked_and_another_worktree`, `test_refuses_what_its_refusals_name_and_moves_nothing`, `test_refuses_a_rename_the_filesystem_turns_down_and_names_the_mv` and `test_refuses_to_call_a_stage_git_that_did_not_answer_staged`. `Test_mode`: `test_accepts_apply_moving_the_folder_to_the_row`, `test_accepts_check_where_there_is_no_root`, `test_refuses_without_a_root_naming_both_places`, `test_s1_first_setup_beside_the_package_puts_the_shared_root_at_agentic_seal` and `test_s6_mode_refuses_to_move_agentic_seal_over_what_its_index_holds`. `Test_pr_checks`: `test_accepts_remove_straight_after_install_before_a_commit`, `test_refuses_a_staged_file_that_differs_and_leaves_it`, `test_refuses_an_index_copy_no_other_copy_keeps_deleted_by_hand`, `test_refuses_an_index_entry_it_cannot_read_deleted_by_hand`, `test_accepts_remove_where_the_root_left_the_tree`, `test_refuses_somebody_elses_file_and_leaves_it`, `test_refuses_a_git_that_did_not_answer_and_keeps_the_index`, `test_pr_checks_install_writes_the_workflow_beside_a_shared_agentic_seal` and `test_pr_checks_install_names_agentic_seal_where_no_root_stands_beside_the_package`. `Test_check`: its four cases, through `exported_once`.
- **`at_top` given, and `commit_as_e` in place of `commit_everything_as_e`.** `Test_switch`: `test_accepts_shared_to_local_by_moving_staging_and_writing_the_row` and `test_accepts_a_tracked_config_without_calling_it_untracked`. `Test_mode`: `test_s6_mode_moves_agentic_seal_under_the_git_directory_and_back` and `test_s6_a_switch_that_could_not_stage_names_agentic_seal_in_the_command`. `Test_pr_checks`: `test_accepts_install_report_and_remove_in_turn`, `test_accepts_remove_of_a_file_deleted_by_hand_the_index_still_holds` and `test_refuses_a_staged_file_without_the_clone_line_deleted_by_hand`.
- **`commit_as_e` in place of `commit_everything_as_e`.** `Test_install_workflow::test_refuses_to_overwrite_or_to_write_what_it_cannot_pin_or_stage`, `Test_refusals::test_accepts_a_tree_the_switch_loses_nothing_of`, `Test_other_worktrees`: `test_refuses_the_git_directory_of_a_separate_git_dir_repository` and `test_refuses_the_bare_directory_a_worktree_was_added_to`, `Test_switch`: `test_accepts_the_way_back_it_names_from_a_subdirectory` and `test_refuses_to_call_a_stage_git_turned_down_staged`, and `Test_pr_checks::test_refuses_to_call_an_install_git_turned_down_staged`.
- **The root read through `home_of` or `roots`, where the case called `SEAL.resolve`.** `Test_no_root::test_accepts_a_repository_without_a_root_by_naming_both_places`, `Test_mode_report::test_accepts_check_writing_nothing_where_the_row_is_absent`, and, beside its `at_top`, `Test_mode_report::test_accepts_an_absent_row_by_writing_the_folders_mode_once`, `test_refuses_a_row_it_could_not_write_and_still_reports` and `Test_switch::test_accepts_an_untracked_file_as_travelling_with_the_folder`.
- **An assertion added.** `Test_remote_url::test_accepts_an_unset_origin_as_the_empty_answer` also asserts that the import's world answers its `HTTPS` origin, which `at_top` hands the import cases.

The other cases that the move check names as changed keep their bodies, and find `_worlds`, `take`, `roots`, `config_at` or `declared_in` changed under them. The classes of units that read no git are placed as they stand (`frame/plan.md` A2), and so is `test_census`. No case of the module reads a document's prose as its fact, and none waits for another module's rebuild.

### Checks at the phase's close

- `bin/test tests/skills/test_seal.py -q -p no:xdist --durations=0` at `3e1c2a5d5`: 389 passed in 12.15 s (executed, file order).
- `bin/test tests/skills/test_seal.py -q`: 389 passed in 4.54 s at `3e1c2a5d5` (executed, under `-n auto`).
- `bin/seal layout --check tests/skills/test_seal.py`: exit 0, `seal layout: 1 files read, 0 refused, 0 declare no TARGET` (executed). It prints seven `report:` lines, functions of `seal.py` with no class of their own, `both_roots`, `committed`, `hand_over`, `left_workflow_line`, `plain`, `staged_text` and `tool_command`; the file at `d06a05ce1` prints the same seven. A report line refuses nothing.
- `bin/seal layout --pairs tests/skills/test_seal.py` names one pair at `3e1c2a5d5` and the same pair at `d06a05ce1`, in `Test_pinned` (executed). The phase did not change that class.
- `bin/test tests/skills/test_broad_gate.py tests/skills/test_fold_check.py tests/skills/test_rules.py tests/skills/test_settle.py -q --co`: 491 collected (executed), so `configured` and `tool` still import (*Scope* item 9, S4).
- The *Phase boundary* set, `bin/test tests/skills/test_seal.py tests/behaviour tests/text -q`: 1264 passed, 9 skipped (executed, at `3e1c2a5d5`). Its six warnings name citations that other work items' pending rule changes correct, as at phase 5.
- `uvx ruff format` and `uvx ruff check` over the changed file: clean (executed).
- `skills/implement/scripts/seal.py` is at HEAD after the mutation runs, `git worktree list` names the repository's own worktree alone after the move check, and no `test_tmp_*` file stands under `tests/` (executed).
- The suite: `unverified`. The broad gate is the orchestrator's, once the review rounds settle.
