# Phase 7: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## What this phase found

### The frame, read against the tree before the build

The frame holds for `tests/skills/test_broad_gate.py` at `d994cc908`. `Test_gate` and `Test_main` ran the fixture's one-test suite through a real `pytest`, as *Grounding* says, and `a_recorded_run` already shared one recorded run among the cases that only read it. *Grounding*'s coordinates `:1510` and `:1669` are those of `ef776317b`, the commit the framer read. The reading cases of `Test_read_record` already read hand-built records, as *Scope* item 7 asks. What cost the seconds stood elsewhere: the gate runs of `Test_gate`, each with all three arms, and the repositories of `Test_main`, built per case.

The aim changed while the phase was built. `1b223b67c` set it at about 38 s, 60 s divided by 1.56, the largest factor between two runs of an unchanged module (*Grounding*, *What a figure of the Windows leg can show*). The phase was started against the earlier aim of about 43 s and closes against 38 s.

### Q1: where the module's seconds went before the rebuild

**On the Windows leg.** Run 45210895409's artifact puts the module at 79.0 s over 204 cases (executed: the sum by case over `1581-dispatch-4/.test_durations` in this session's scratchpad). By class: `Test_gate` 35.9 s, `Test_main` 25.4 s, `Test_compare_at_base` 8.7 s, `Test_moved_line` 2.0 s and `Test_resolve_base` 1.3 s. The 144 cases that start no process locally cost 2.6 s together, and the other 60 cost 76.4 s (executed, against the local counts below). Runs 45206461246 and 45218254995 put the module at 67.6 s and 68.9 s (executed, the same sum).

**On this macOS machine.** `bin/test tests/skills/test_broad_gate.py -q -p no:xdist` over the file at `d994cc908` passed 203 cases and skipped 1 in 13.18 s (executed). A pytest plugin in this phase's scratch (`tmp_spawn_probe.py`) counted the processes each case starts in the test process, and a `git` shim on `PATH` logged every git process, the gate's children among them. Before the rebuild the cases started 367 processes in the test process, 35 of them Python scripts and 17 suite rows through `pytest`, and 547 git processes in all (executed). By class, git: `Test_gate` 266, `Test_main` 177, `Test_compare_at_base` 38 and `Test_moved_line` 28. 37 of the git processes were `commit`s that built a world or a case's base.

A fit of each run's per-case seconds against these counts, over the 60 cases that start a process and with no constant, gives 0.08 s to 0.10 s for each git process, 0.05 s to 0.19 s for each Python script and 0.37 s to 0.48 s for each suite row on the Windows leg, across the three runs (executed: `fit3.py` in this phase's scratch). So the module's seconds stood in three places. Each `Test_gate` case ran every arm of the gate, and the chain arm alone starts about nine git processes. Each `Test_main` case built its repository and ran the shipped gate as a child. Each case whose base failed a file made that base with commits and a merge on its copy.

### What the rebuild changed

`a3331d51f` does the rebuild, and `fa8a00cd7` corrects a docstring of it.

- **Each world is one `git fast-import`.** `history` (`tests/skills/test_broad_gate.py:159`) writes a repository's commits and refs in one process. `refs`, `_repo_template` and the new `_sealable_template` use it. `_repo_template` also carries two branches from `base` that no case checks out: `red-base`, which fails `tests/test_two.py`, and `red-elsewhere`, which fails `tests/test_red.py`. They are the bases `Test_compare_at_base` and `Test_gate` ask about, so no case commits to make a base.
- **A case's failing file stays in the working tree.** `failing_here` writes `tests/test_two.py` and commits nothing. The row runs over the working tree, and `compare_at_base` checks out the base's commit, never HEAD's. The mode arm and the workflow case read the working tree the same way.
- **A case whose fact is one arm has the others answered.** `arms_answered` replaces `gate.run` for the arms it names with a passed `Check` and runs every other command for real, the row at the base among them. `suite_alone` answers the chain and mode arms. `a_recorded_run`, `a_sealed_run`, the preflight and the runs of a copied plugin keep every arm real.
- **The recorder's cases for a session an act ended run in `Test_read_record`.** `recorded` runs the row through `gate.run` with the recorder loaded, in a directory with no repository, and reads the record back through `read_record`. Five gate runs became these five record readings (part 4).
- **`Test_main` builds its repository once.** `_sealable_template` is read as it stands by the cases that only run the gate, since a run with no `--record` writes nothing into it (executed: `readonly_probe.py` in this phase's scratch compared every file under the repository, `.git` among it, before and after a run). `sealable` copies it for a case that writes. `a_sealed_run` is one run of the shipped gate over it, read by two cases. The mode-row and workflow cases call `main` in the process through `gated`, as `run_gate` calls the script, with `--shape`. `run_gate` passes `clean_env()`, as `a_recorded_run` does, since `a_sealed_run` is module-scoped too.
- **The `#1059` case runs the command once.** `test_s5_…` runs `seal gate --preflight` beside the package through `tool` for the refusal, and reads the root and the key the gate would take through `seal_home` and `broad_command`, the two readers `gate` asks before it runs anything.

After the rebuild the cases start 180 processes in the test process, 16 of them Python scripts and 12 suite rows, and 220 git processes in all (executed, the same plugin and shim). Two `commit`s remain, those of `tests/conftest.py#package`. By the fit above, the module would read 32.5 s, 36.4 s and 35.3 s in the three runs, under the aim of about 38 s. The fit is an estimate. It counts each module-scoped world and each shared run once, as a run in file order pays them, and on the leg each worker that runs a case of them builds them again (`frame/plan.md` *Technical context*), so the leg may read more. The figure that judges the phase is the Windows leg's, from the orchestrator's run at this phase's Status commit (`frame/design.md` S1).

### Departures from the frame

- **Five cases read a record a real `pytest` wrote.** *Scope* item 7 has a case about how the gate reads a record read a hand-built one. The five cases this phase moved into `Test_read_record` hold what the recorder writes when pytest runs a hook in a given order: a late `pytest.exit(0)`, an early `session.exitstatus = 0`, an `os._exit(0)` in `pytest_unconfigure` or in a test. A hand-built record would hold what `read_record` does with a record the case's author wrote, which the class's other cases already hold. These cases run a shell and a `pytest` and no git, as the real-git cases G2 keeps show that a command and git agree (`CONTRIBUTING.md` *The test layout*).
- **`arms_answered` replaces the gate's `run` for an arm, not git.** `frame/plan.md` A4 bars a fake of git's output. The cases that answer an arm keep the real row and the real comparison at the base, and the arm they answer is the one their fact is not. `d994cc908` folded phase 6's like seam, `at_top`, into *Scope* item 6; item 7 does not name this one.
- **`history` is this module's own helper.** It builds a world in one process where `tests/conftest.py#commit_everything_as_e` takes three for each commit. The spawn bars `tests/conftest.py`, and no other test file builds a world with it, so it does not define a helper two files use (`CONTRIBUTING.md` *The test layout*).

### The four parts `CONTRIBUTING.md` *The test layout* asks of a rebuilt module

**1. The move check, and the mutation table.**

`bin/seal layout --moved d994cc908 --from tests/skills/test_broad_gate.py --to tests/skills/test_broad_gate.py` exits 1 at `a3331d51f` (executed). Its last line reads `seal layout: moved: 135 old cases, 202 items against 203 at d994cc90835d, 58 failed`. The cases over `refs` and `_repo_template` find those fixtures changed, two cases were cut, three were added and thirteen changed their bodies. So the mutation table carries part 1.

The mutants sit in `skills/verify/scripts/broad_gate.py` and, for the five cases that now read a real record, in `skills/verify/scripts/pytest_record/agentic_pytest_record.py`. Mutants 1 to 78 are written by hand at the decision points of the units whose cases the phase rewrote: `resolve_base`, `moved_line`, `short_commit`, `names_a_branch` and `a_runner_could_hold` over `refs`, `seal_home`, `broad_command`, `run`, `recording_env`, `record_path`, `read_record`, `base_word`, `compare_at_base`, `uncommitted_line`, `gate` and `main`. Mutants 79 to 125 negate the first one to three single-line conditions of each other function, or change the return of a function with none, by a script over the file's syntax tree (`gen.py`). Mutants 126 to 129 are the recorder's. Each set ran in one call against `a3331d51f` (executed): `bin/seal mutate <file> --replace OLD NEW ... --tests "bin/test tests/skills/test_broad_gate.py -q -x"`, built by `run_mutants.py` from `mutants.py` and `ast_mutants.py` in this phase's scratch under `mut/`. They printed `seal mutate: 78 mutants, 70 red, 8 SURVIVED, 0 with no verdict (202.9s)`, `seal mutate: 47 mutants, 47 red, 0 SURVIVED, 0 with no verdict (62.9s)` and `seal mutate: 4 mutants, 4 red, 0 SURVIVED, 0 with no verdict (15.4s)`. Under `-n auto`, `-x` stops the run with exit 2. Each row shows the lines the mutant changes, joined. The table measures this test file alone.

The base column is filled for a survivor alone. The eight survivors ran again against the test file at `d994cc908`, copied to `tests/skills/test_tmp_broad_gate_base.py` and removed after the run. That call printed `seal mutate: 8 mutants, 0 red, 8 SURVIVED, 0 with no verdict (56.6s)` (executed). So each gap is older than this phase, and the phase lost no fact that killed one. Why they live:

- 51 and 54: no case gives `gate` a repository with no commit, or a `--record` that is not a directory.
- 55: no case runs `gate` over a base whose resolution moved. `Test_moved_line` holds the line itself.
- 62 and 65: no case runs a row that fails and writes no record, a row that is not `pytest`.
- 66: no case runs a preflight whose arm fails.
- 70: no case compares the report's marks under `--shape` with the marks of a console that wants UTF-8.
- 74: no case reads the copy row of a run that a tree's own copy took over.

The phase adds no case for them: the frame rebuilds existing cases (`frame/design.md` *Scope* item 7), and `agents/crafter.md` *Never* bars building beyond the request. `gaps.md` *Not done* names the eight.

Each case the phase added or moved was seen red against a break of what it holds, by `bin/seal mutate` with `-p no:xdist` and `-k` naming the case (executed). The three `test_refuses_a_red_session_…` cases go red against the recorder's `"exitstatus": int(exitstatus)` made `0` and against `"outcome": report.outcome` made `"passed"`. `test_refuses_a_session_a_test_ended_with_os_exit_0` goes red against `stopped = not ends or any(` made `stopped = any(`, and `test_accepts_a_green_session_a_late_hook_exits_with_0` against it made `stopped = True or any(`. `test_s5_…` goes red against mutants 14 and 15.

| # | Unit | Old | New | New file | `d994cc908` |
|---|---|---|---|---|---|
| 1 | `resolve_base` | `if names_a_branch(root, given): tracked` | `if False: tracked` | red |  |
| 2 | `resolve_base` | `if tracked and tracked.strip():` | `if False:` | red |  |
| 3 | `resolve_base` | `return Base(given, given_commit, name, commit)` | `return Base(given, given_commit, given, commit)` | red |  |
| 4 | `resolve_base` | `return Base(given, given_commit, REMOTE_LABEL.format(ref=given), commit)` | `return Base(given, given_commit, given, given_commit)` | red |  |
| 5 | `resolve_base` | `return Base(given, given_commit, given, given_commit)` | `return Base(given, given_commit, given, None)` | red |  |
| 6 | `moved_line` | `if not base.moved: return None` | `if False: return None` | red |  |
| 7 | `moved_line` | `if base.ref == runner:` | `if base.ref != runner:` | red |  |
| 8 | `moved_line` | `elif a_runner_could_hold(root, runner):` | `elif True:` | red |  |
| 9 | `moved_line` | `if base.given_commit is None: return (` | `if False: return (` | red |  |
| 10 | `moved_line` | `apart = f" — {base.ref} is {ahead} ahead and {behind} behind {base.given}"` | `apart = f" — {base.ref} is {behind} ahead and {ahead} behind {base.given}"` | red |  |
| 11 | `short_commit` | `return out.strip() if out and out.strip() else None` | `return out.strip() if out and out.strip() else ""` | red |  |
| 12 | `names_a_branch` | `return git(root, "check-ref-format", "--branch", given) is not None` | `return True` | red |  |
| 13 | `a_runner_could_hold` | `return git(root, "check-ref-format", ref) is not None` | `return True` | red |  |
| 14 | `seal_home` | `return sibling.load(OPTIN).marked_home(root) or None` | `return root` | red |  |
| 15 | `broad_command` | `return value or None` | `return None` | red |  |
| 16 | `run` | `handle.write(f"exit {r.returncode}\n\n")` | `handle.write("\n")` | red |  |
| 17 | `run` | `text = r.stdout + ("\n" if r.stdout and r.stderr else "") + r.stderr` | `text = r.stdout` | red |  |
| 18 | `recording_env` | `env["PYTEST_ADDOPTS"] = f"{env.get('PYTEST_ADDOPTS', '')} -p {RECORDER}".lstrip()` | `env["PYTEST_ADDOPTS"] = env.get('PYTEST_ADDOPTS', '')` | red |  |
| 19 | `recording_env` | `env[RECORD_KEY_VARIABLE] = key` | `env[RECORD_KEY_VARIABLE] = "other"` | red |  |
| 20 | `record_path` | `if rel.split(os.sep)[0] == os.pardir: return real` | `if False: return real` | red |  |
| 21 | `read_record` | `if not parsed or parsed[0].get("key") != key:` | `if not parsed:` | red |  |
| 22 | `read_record` | `if stopped: record.unended += 1` | `if False: record.unended += 1` | red |  |
| 23 | `read_record` | `end.get("stopped") != [] or end.get("exitstatus") not in RAN_TO_ITS_END` | `end.get("exitstatus") not in RAN_TO_ITS_END` | red |  |
| 24 | `read_record` | `end.get("stopped") != [] or end.get("exitstatus") not in RAN_TO_ITS_END` | `end.get("stopped") != []` | red |  |
| 25 | `read_record` | `stopped = not ends or any(` | `stopped = any(` | red |  |
| 26 | `read_record` | `if stopped or any(end.get("exitstatus") not in PASSED_EXITS for end in ends):` | `if stopped:` | red |  |
| 27 | `read_record` | `if value.get("outcome") == "failed": record.failing.setdefault(named, None)` | `if False: record.failing.setdefault(named, None)` | red |  |
| 28 | `read_record` | `if value.get("exitstatus") != 0:` | `if False:` | red |  |
| 29 | `read_record` | `if seen not in collections:` | `if True:` | red |  |
| 30 | `read_record` | `record.counts[category] = record.counts.get(category, 0) + 1` | `record.counts[category] = 1` | red |  |
| 31 | `read_record` | `record.sessions += 1` | `record.sessions = 1` | red |  |
| 32 | `read_record` | `record.unread += unread` | `record.unread += 0` | red |  |
| 33 | `base_word` | `if not record.sessions: return NO_RECORD` | `if False: return NO_RECORD` | red |  |
| 34 | `base_word` | `if path in record.failing: return ON_BASE` | `if False: return ON_BASE` | red |  |
| 35 | `base_word` | `if path in record.collected or code == 0:` | `if path in record.collected:` | red |  |
| 36 | `base_word` | `if path in record.collected or code == 0:` | `if code == 0:` | red |  |
| 37 | `base_word` | `if record.unplaced_red:` | `if False:` | red |  |
| 38 | `base_word` | `if record.unended: return UNENDED_AT_BASE` | `if False: return UNENDED_AT_BASE` | red |  |
| 39 | `base_word` | `if record.unread: return UNREAD_AT_BASE` | `if False: return UNREAD_AT_BASE` | red |  |
| 40 | `compare_at_base` | `if added is None:` | `if False:` | red |  |
| 41 | `compare_at_base` | `record = read_record(records_dir(keep), key, scratch)` | `record = read_record(records_dir(keep), key, root)` | red |  |
| 42 | `compare_at_base` | `added = git(root, "worktree", "add", "--detach", scratch, base)` | `added = git(root, "worktree", "add", "--detach", scratch, "HEAD")` | red |  |
| 43 | `compare_at_base` | `return {f: base_word(record, ran.code, f) for f in files}` | `return {f: base_word(record, 0, f) for f in files}` | red |  |
| 44 | `compare_at_base` | `git(root, "worktree", "remove", "--force", scratch)` | `git(root, "worktree", "list")` | red |  |
| 45 | `uncommitted_line` | `if not (status and status.strip()): return None` | `if False: return None` | red |  |
| 46 | `uncommitted_line` | `if path is None: return None # Both by realpath` | `if False: return None # Both by realpath` | red |  |
| 47 | `gate` | `if not root: raise Refused( f"seal gate: {args.root or os.getcwd()} is not in a git repository` | `if False: raise Refused( f"seal gate: {args.root or os.getcwd()} is not in a git repository` | red |  |
| 48 | `gate` | `home = seal_home(root) if home is None:` | `home = seal_home(root) if False:` | red |  |
| 49 | `gate` | `if command is None: raise Refused(missing_row(home))` | `if False: raise Refused(missing_row(home))` | red |  |
| 50 | `gate` | `if unrunnable: raise Refused(unrunnable)` | `if False: raise Refused(unrunnable)` | red |  |
| 51 | `gate` | `if head is None: raise Refused(f"seal gate: {root} has no HEAD` | `if False: raise Refused(f"seal gate: {root} has no HEAD` | survived | survived |
| 52 | `gate` | `if base.commit is None: raise Refused( f"seal gate: --base {base.given} does not resolve` | `if False: raise Refused( f"seal gate: --base {base.given} does not resolve` | red |  |
| 53 | `gate` | `if args.preflight: raise Refused(PREFLIGHT_RECORD)` | `if False: raise Refused(PREFLIGHT_RECORD)` | red |  |
| 54 | `gate` | `if not os.path.isdir(item):` | `if False:` | survived | survived |
| 55 | `gate` | `if said: sys.stderr.write(said + "\n")` | `if False: sys.stderr.write(said + "\n")` | survived | survived |
| 56 | `gate` | `if not args.preflight: checks[SUITE] = run(` | `if True: checks[SUITE] = run(` | red |  |
| 57 | `gate` | `head = read_record(records_dir(keep), head_key, root)` | `head = read_record(records_dir(keep), record_key("head"), root)` | red |  |
| 58 | `gate` | `[py, CHAIN, "--baseline", base.commit, "--root", root, sealing],` | `[py, CHAIN, "--baseline", base.given, "--root", root, sealing],` | red |  |
| 59 | `gate` | `sealing = sibling.load(CHAIN_CHECK).SEALING` | `sealing = "--help"` | red |  |
| 60 | `gate` | `[py, SEAL_SCRIPT, "mode", "--check"]` | `[py, SEAL_SCRIPT, "mode"]` | red |  |
| 61 | `gate` | `if not check.failed and not (name == SUITE and head.unpassed):` | `if not check.failed:` | red |  |
| 62 | `gate` | `if head.sessions: files` | `if True: files` | survived | survived |
| 63 | `gate` | `if files: verdicts = compare_at_base(` | `if False: verdicts = compare_at_base(` | red |  |
| 64 | `gate` | `verdicts = compare_at_base(root, base.commit, command, files, keep)` | `verdicts = compare_at_base(root, "HEAD", command, files, keep)` | red |  |
| 65 | `gate` | `verdicts = {f: NO_RECORD_AT_HEAD for f in failing_files(check.text)}` | `verdicts = None` | survived | survived |
| 66 | `gate` | `form[0] = preflight_line(PREFLIGHT_FAILED, tree, base.commit)` | `pass` | survived | survived |
| 67 | `gate` | `if args.preflight: sys.stdout.write(preflight_line(PREFLIGHT_PASSED` | `if False: sys.stdout.write(preflight_line(PREFLIGHT_PASSED` | red |  |
| 68 | `gate` | `written = write_gate_file(item, tree, base.commit) if item is not None else None` | `written = None` | red |  |
| 69 | `gate` | `uncommitted = uncommitted_line(root, written) if uncommitted:` | `uncommitted = uncommitted_line(root, written) if False:` | red |  |
| 70 | `gate` | `lines += report_lines(rows, ascii_marks=args.shape or ascii_marks)` | `lines += report_lines(rows, ascii_marks=ascii_marks)` | survived | survived |
| 71 | `main` | `if root: shipped = shipped_gate(root)` | `if False: shipped = shipped_gate(root)` | red |  |
| 72 | `main` | `if shipped is not None:` | `if False:` | red |  |
| 73 | `main` | `handed = sys.argv[1:] if argv is None else list(argv)` | `handed = []` | red |  |
| 74 | `main` | `env = {**os.environ, INVOKED_AS_VAR: os.path.realpath(__file__)}` | `env = dict(os.environ)` | survived | survived |
| 75 | `main` | `sibling.load(CHAIN_CHECK) return gate(` | `return gate(` | red |  |
| 76 | `main` | `sys.stderr.write(str(exc) + "\n") return 2` | `sys.stderr.write(str(exc) + "\n") return 1` | red |  |
| 77 | `main` | `sys.stderr.write(f"seal gate: {unanswered.line}\n") return 2` | `sys.stderr.write(f"seal gate: {unanswered.line}\n") return 0` | red |  |
| 78 | `main` | `args.invoked_as = os.environ.pop(INVOKED_AS_VAR, None) or None` | `args.invoked_as = None` | red |  |
| 79 | `stamp_module` | `return sibling.load(STAMP)` | `return None` | red |  |
| 80 | `gitcmd_module` | `return sibling.load("lib/gitcmd.py")` | `return None` | red |  |
| 81 | `git` | `return r.stdout if r.returncode == 0 else None` | `return None` | red |  |
| 82 | `shipped_gate` | `if not os.path.isfile(candidate):` | `if not (not os.path.isfile(candidate)):` | red |  |
| 83 | `shipped_gate` | `if os.path.realpath(candidate) == os.path.realpath(__file__):` | `if not (os.path.realpath(candidate) == os.path.realpath(__file__)):` | red |  |
| 84 | `plugin_version` | `return str(version) if version else "?"` | `return None` | red |  |
| 85 | `copy_origin` | `return stamp_module().fit(f"{origin} {plugin_version(plugin)}")` | `return None` | red |  |
| 86 | `gate_copy` | `if installed:` | `if not (installed):` | red |  |
| 87 | `gate_copy` | `if mine.read() == theirs.read():` | `if not (mine.read() == theirs.read()):` | red |  |
| 88 | `running_line` | `return f"seal gate: gate {os.path.realpath(__file__)} ({copy_origin(root)})"` | `return None` | red |  |
| 89 | `Base.moved` | `return self.commit != self.given_commit` | `return None` | red |  |
| 90 | `wholly_substituted` | `if len(value) > 1 and value[0] == "`" == value[-1]:` | `if not (len(value) > 1 and value[0] == "`" == value[-1]):` | red |  |
| 91 | `wholly_substituted` | `if not value.startswith("$(") or not value.endswith(")"):` | `if not (not value.startswith("$(") or not value.endswith(")")):` | red |  |
| 92 | `wholly_substituted` | `if char == "(":` | `if not (char == "("):` | red |  |
| 93 | `cmd_exe_reads` | `if windows is None:` | `if not (windows is None):` | red |  |
| 94 | `cmd_exe_reads` | `if not windows:` | `if not (not windows):` | red |  |
| 95 | `cmd_exe_reads` | `if comspec is None:` | `if not (comspec is None):` | red |  |
| 96 | `cmd_cut` | `return min(found, default=len(value))` | `return None` | red |  |
| 97 | `command_names` | `if before is None or before in CMD_SEPARATORS:` | `if not (before is None or before in CMD_SEPARATORS):` | red |  |
| 98 | `names_in_a_directory` | `if "/" in word and is_directory(word.split("/", 1)[0]):` | `if not ("/" in word and is_directory(word.split("/", 1)[0])):` | red |  |
| 99 | `listed` | `return f"{', '.join(rest)} and {last}" if rest else last` | `return None` | red |  |
| 100 | `backslashed` | `if at + len(word) <= cut and word in refused:` | `if not (at + len(word) <= cut and word in refused):` | red |  |
| 101 | `in_root` | `return lambda part: os.path.isdir(os.path.join(root, part))` | `return None` | red |  |
| 102 | `not_read_line` | `if not not_read:` | `if not (not not_read):` | red |  |
| 103 | `not_as_written` | `if opener == "`":` | `if not (opener == "`"):` | red |  |
| 104 | `not_as_written` | `elif opener == "$(":` | `elif not (opener == "$("):` | red |  |
| 105 | `not_as_written` | `elif value.endswith("&") and not value.endswith("&&"):` | `elif not (value.endswith("&") and not value.endswith("&&")):` | red |  |
| 106 | `Check.failed` | `return self.code != 0` | `return None` | red |  |
| 107 | `Check.first_lines` | `return lines[:n]` | `return None` | red |  |
| 108 | `record_key` | `return f"{kind}-{secrets.token_hex(8)}"` | `return None` | red |  |
| 109 | `records_dir` | `return os.path.join(os.path.abspath(keep), RECORDS)` | `return None` | red |  |
| 110 | `failing_files` | `return list(dict.fromkeys(FAILED_RE.findall(text)))` | `return None` | red |  |
| 111 | `suite_counts` | `if not record.sessions or record.unread or record.unplaced or not record.counts:` | `if not (not record.sessions or record.unread or record.unplaced or not record.counts):` | red |  |
| 112 | `write_gate_file` | `if after.refusals:` | `if not (after.refusals):` | red |  |
| 113 | `write_gate_file` | `if not after.blocks or after.blocks[-1].fields[fields.RUN].value != value:` | `if not (not after.blocks or after.blocks[-1].fields[fields.RUN].value != value):` | red |  |
| 114 | `write_gate_file` | `if same:` | `if not (same):` | red |  |
| 115 | `rounds_rows` | `if kind != chain.DEFERRED:` | `if not (kind != chain.DEFERRED):` | red |  |
| 116 | `rounds_rows` | `if home not in homes:` | `if not (home not in homes):` | red |  |
| 117 | `rounds_rows` | `if count and homes:` | `if not (count and homes):` | red |  |
| 118 | `panel` | `if branch:` | `if not (branch):` | red |  |
| 119 | `panel` | `if stamp.ref_is_commit(base.ref, base.commit):` | `if not (stamp.ref_is_commit(base.ref, base.commit)):` | red |  |
| 120 | `panel` | `if copy:` | `if not (copy):` | red |  |
| 121 | `failure_lines` | `if check.code == 0 and record is not None and record.unpassed:` | `if not (check.code == 0 and record is not None and record.unpassed):` | red |  |
| 122 | `failure_lines` | `if verdicts:` | `if not (verdicts):` | red |  |
| 123 | `failure_lines` | `if words == {NO_RECORD_AT_HEAD}:` | `if not (words == {NO_RECORD_AT_HEAD}):` | red |  |
| 124 | `report_lines` | `if ascii_marks:` | `if not (ascii_marks):` | red |  |
| 125 | `preflight_line` | `return head.format(tree=tree, base=base) + PREFLIGHT_TAIL` | `return None` | red |  |
| 126 | `pytest_sessionfinish` | `"exitstatus": int(exitstatus),` | `"exitstatus": 0,` | red |  |
| 127 | `pytest_sessionfinish` | `"stopped": self.stopped(session),` | `"stopped": [],` | red |  |
| 128 | `pytest_runtest_logreport` | `"outcome": report.outcome, "path": path, "category"` | `"outcome": "passed", "path": path, "category"` | red |  |
| 129 | `pytest_keyboard_interrupt` | `self.stops.append({"by": "exit", "what": what})` | `pass` | red |  |

**2. Cases and seconds, before and after, on this macOS machine.** The figures are local. `frame/design.md` *Grounding*, *What a figure of the Windows leg can show*, takes no local figure as evidence of a saving on the Windows leg. The module's Windows figure is the orchestrator's `workflow_dispatch` run at this phase's Status commit (`frame/design.md` S1).

| Measure | Before, `d994cc908` | After, `a3331d51f` |
|---|---|---|
| Cases of the module, passed and skipped | 203 and 1 | 202 and 1 |
| Processes the cases start in the test process, counted by `tmp_spawn_probe.py` under `-p no:xdist` | 367 | 180 |
| Git processes in all, logged by the shim | 547 | 220 |
| `bin/test tests/skills/test_broad_gate.py -q -p no:xdist`, the module | 13.18 s | 6.96 s |
| The same runs: `Test_gate`, `Test_main`, `Test_compare_at_base`, `Test_read_record` | 6.82 s, 3.46 s, 1.04 s, under 0.01 s | 2.50 s, 1.68 s, 0.72 s, 0.49 s |
| `bin/test tests/skills/test_broad_gate.py -q`, under `-n auto` | 5.70 s | 3.42 s |
| Windows leg, the module, from the `test-durations` artifacts | 105 s in run 45181872904, 79 s in 45189798316, 83 s in 45203717820, 68 s in 45206461246, 79 s in 45210895409 and 69 s in 45218254995 | not measured |

The per-case figures of both local runs are in this phase's scratch, `before-plain.txt` and `after-plain.txt`, and the process counts in `before.json`, `after.json`, `gitlog-before.txt` and `gitlog-after.txt`. Each figure before the phase ran over the file at `d994cc908` copied to `tests/skills/test_tmp_broad_gate_base.py`, which was removed after each run.

**Q2: the floor.** The phase gives no answer to Q2 for this module, since no local figure is evidence of the Windows leg. What the module keeps is named in the third part below. By the fit in *Q1*, the costliest cases left are the full gate runs: `a_recorded_run` and the green case that carries it, the preflight, `a_sealed_run`, the copied plugin's run, and the gate's case of a new failing file with its run at the base, each about 1.8 s to 2.3 s on the slow run.

**3. The real-git cases kept.** These cases run git, a real row or the gate as a person starts it, and show that the gate and git, or the gate and `pytest`, agree:

- `Test_moved_line`, `Test_short_commit`, `Test_names_a_branch`, `Test_a_runner_could_hold` and `Test_resolve_base`, over `refs`. Their fact is what git answers for a ref.
- `Test_compare_at_base`'s five cases, which ask git for a worktree at the base, run the row in it and remove it. In `test_refuses_to_compare_at_a_base_that_cannot_be_checked_out` git refuses the worktree, and `test_refuses_to_let_a_removal_git_did_not_answer_replace_the_words` answers the removal alone.
- `Test_uncommitted_line`'s two cases, which read `git status`.
- `a_recorded_run`, the shipped gate started as a person starts it with `--record`, every arm real, and `Test_gate::test_accepts_a_green_tree_and_runs_every_check_in_order`, which reads it.
- `Test_gate::test_accepts_a_preflight_that_runs_no_row_and_writes_nothing`, in the process with the chain and mode arms real.
- `Test_gate::test_refuses_a_failing_test_the_base_lacks_as_new`, `test_refuses_a_suite_a_test_stopped_at_exit_0` and `test_refuses_a_red_suite_an_act_after_the_run_loop_turned_to_exit_0`, each with the real row and, where a file fails, the real run at the base; the chain and mode arms are answered.
- `a_sealed_run`, the shipped gate over `_sealable_template` with every arm real, read by `Test_main::test_the_fixture_branch_passes` and `test_a_malformed_sprite_leaves_the_verdict_and_the_report_as_they_were`, whose own run is a copied plugin's with every arm real.
- `Test_main::test_refuses_a_copy_without_its_chain_check_before_any_arm` and `test_accepts_the_trees_own_copy_with_the_same_arguments`, which start a gate as a child.
- `Test_main::test_a_mode_row_that_disagrees_with_the_folder_fails_the_gate`, the real mode arm over the working tree; the chain arm is answered.
- `Test_main::test_s5_gate_reads_its_key_from_agentic_seal_and_names_it_where_none_is`, `seal gate --preflight` through `tool` beside the package.
- `Test_read_record`'s five cases over a real `pytest` with the recorder, which run no git.

**4. Old cases cut or rewritten.** Two cases were cut, three added and thirteen rewritten (executed: a comparison of each case's syntax tree at `d994cc908` and at `a3331d51f`). Each assertion of a rewritten case is the base's, except where a line below names the change.

- **Cut: `Test_gate::test_accepts_a_failure_the_base_shares_as_failing_on_base_too`.** It held that the gate prints `failing on base too` where the base fails the file, and alone killed a mutant that hands `compare_at_base` HEAD in place of the base's commit. `Test_gate::test_refuses_a_red_suite_an_act_after_the_run_loop_turned_to_exit_0` now runs over `red-base` and asserts that line in place of `new`, and mutant 64 is red. `Test_compare_at_base::test_accepts_a_file_the_base_fails_too` holds the comparison's own word.
- **Cut, and held in `Test_read_record`: `Test_gate::test_accepts_a_green_suite_a_late_hook_exits_with_0`.** `Test_read_record::test_accepts_a_green_session_a_late_hook_exits_with_0` holds that such a session's record reads passed and stopped nothing. That the gate passes a record like it and writes `trail/gate.md` is `a_recorded_run`'s case.
- **Rewritten: `Test_gate::test_refuses_a_suite_a_test_stopped_at_exit_0`.** Its `pytest-exit-0` instance stays in `Test_gate` with `suite_alone` and an uncommitted test file. Its `os-exit-0` instance is `Test_read_record::test_refuses_a_session_a_test_ended_with_os_exit_0`, which holds that the record reads a session that did not pass, did not end and failed no file. The gate's reading of an unended session, `UNENDED_HERE` and no run at the base, is the `pytest-exit-0` case's.
- **Rewritten: `Test_gate::test_refuses_a_red_suite_an_act_after_the_run_loop_turned_to_exit_0`.** Its `row-or-interpreter` instance stays in `Test_gate`, with `suite_alone`, the row in the working tree's config, and `red-base` as its base, so it asserts `failing on base too` where it asserted `new`. Its three other instances are `Test_read_record::test_refuses_a_red_session_an_act_after_the_run_loop_turned_to_exit_0`, which holds that the record reads a session that did not pass, ran to its end and names `tests/test_two.py` with one failed and one passed. The gate's reading of such a record is the `Test_gate` case's. `Test_gate::test_refuses_a_failing_test_the_base_lacks_as_new` still asserts `new`.
- **Rewritten, `suite_alone` and an uncommitted failing file: `Test_gate::test_refuses_a_failing_test_the_base_lacks_as_new`.**
- **Rewritten, the base given by `_repo_template` and nothing committed:** `Test_compare_at_base`'s `test_accepts_a_file_the_base_never_had_as_new`, `test_accepts_a_file_the_base_fails_too`, `test_refuses_new_for_a_file_a_red_base_never_collected` and `test_refuses_to_let_a_removal_git_did_not_answer_replace_the_words`.
- **Rewritten, over `_sealable_template` or `a_sealed_run`:** `Test_main::test_refuses_a_copy_without_its_chain_check_before_any_arm`, `test_the_fixture_branch_passes`, and `test_a_malformed_sprite_leaves_the_verdict_and_the_report_as_they_were`, which compares the cut sprite's run with `a_sealed_run`, the tree's gate over the same repository, where it compared it with the copied plugin's run before the cut.
- **Rewritten, `main` in the process over a copy, nothing committed and arms answered:** `Test_main::test_a_mode_row_that_disagrees_with_the_folder_fails_the_gate`, the chain arm answered, and `test_a_workflow_with_a_release_job_leaves_the_run_as_it_was`, the chain and mode arms answered. Each reads `gated`'s exit code, stdout and stderr where it read the child's.
- **Rewritten, one run of the command: `Test_main::test_s5_gate_reads_its_key_from_agentic_seal_and_names_it_where_none_is`.** Its second `seal gate --preflight` run, after a commit of the root, asserted the stderr line that quotes the key. The case now asserts that `seal_home` gives the root at `agentic-seal/` and `broad_command` its key. `Test_gate::test_accepts_a_preflight_that_runs_no_row_and_writes_nothing` holds the line, `gate.ROW_NOT_RUN` in stderr.

The other cases that the move check names as changed keep their bodies, and find `refs` or `_repo_template` changed under them. The classes of units that read no git are placed as they stand (`frame/plan.md` A2), and so is `test_census`. No case of the module reads a document's prose as its fact.

**`tests/conftest.py`.** `test_s5_…` builds `tests/conftest.py#package` for itself, two commits and the `git rev-parse HEAD` after each, the one case here that takes it. A module-scoped template of `package` would build it once for that one case, so it would not cut this module. The trim of `commit_everything_as_e` that phase 1 names in `gaps.md` *Not done* would cut two processes here.

### Checks at the phase's close

- `bin/test tests/skills/test_broad_gate.py -q -p no:xdist --durations=0` at `a3331d51f`: 202 passed and 1 skipped in 6.96 s (executed, file order).
- `bin/test tests/skills/test_broad_gate.py -q`: 202 passed and 1 skipped in 3.42 s at `fa8a00cd7` (executed, under `-n auto`).
- `bin/seal layout --check tests/skills/test_broad_gate.py`: exit 0, `seal layout: 1 files read, 0 refused, 0 declare no TARGET` (executed). It prints fourteen `report:` lines, functions of `broad_gate.py` with no class of their own. A report line refuses nothing.
- `bin/seal layout --pairs tests/skills/test_broad_gate.py`: `seal layout: 1 files read, 0 pairs` (executed).
- `bin/test tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py -q --co`: 15 collected (executed), so `unquoted_flat` and `gate_module` still import (*Scope* item 9, S4). The module still imports `configured` and `tool` from `tests/skills/test_seal.py`.
- The *Phase boundary* set, `bin/test tests/skills/test_broad_gate.py tests/behaviour tests/text -q`: 1077 passed, 10 skipped (executed, at `a3331d51f`). Its six warnings name citations that other work items' pending rule changes correct, as at phases 5 and 6.
- `uvx ruff format` and `uvx ruff check` over the changed file: clean (executed).
- `skills/verify/scripts/broad_gate.py` and the recorder are at HEAD after the mutation runs, `git worktree list` names the repository's own worktree alone, and no `test_tmp_*` file stands under `tests/` (executed).
- The suite: `unverified`. The broad gate is the orchestrator's, once the review rounds settle.
