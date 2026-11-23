# Phase 5: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## What this phase found

### The frame, read against the tree before the build

The frame holds for `tests/skills/test_test_layout.py`. Read at `5172cf10c`: `_moved_world` stands at `:701`, and each case of `Test_moved` that runs `--moved` copies it and calls `layout.main(["--moved", ...])` through `run_moved` (`:724`). `skills/verify/scripts/test_layout.py` is the same file as at `5528a681f`, the commit the framer read, so *Grounding*'s coordinates hold there: `moved` at `:937`, `_collected` at `:1034` with its `pytest --collect-only` run at `:1044`, and the worktree added at `:1131`. `moved(old, new, old_modules, new_modules)` takes texts, as *Scope* item 5 says. The frame names the modules each side reads under `tests/` loosely: `_moved_main` builds them with `_test_modules`, from `git ls-tree -r -z` and `git show` at the base and from a walk of the disk in the working tree, so a unit call that hands `moved` hand-built maps would leave `_test_modules` without a case. The phase builds both maps through `_test_modules` over the texts.

Two statements of the module stood against the tree before the phase. Its docstring said every case but one builds no repository and runs no git, and that `Test_main` holds a case over this repository's own `tests/` that runs `--check`. 47 cases of `Test_moved` ran git at `5172cf10c`, and no case of `Test_main` runs `--check` over the repository; `tests/behaviour/test_this_repository_passes_its_own_checks.py` holds that case. The comment above the world named three old files where it holds nine. The phase rewrote both to state the tree.

### Q1: where the module's seconds went before the rebuild

**On the Windows leg.** Run 45203717820's artifact puts the module at 75.9 s over 88 cases, and `Test_moved` at 75.3 s over 47 (executed: the sum by case over the artifact at `1581-dispatch-2/.test_durations` in this session's scratchpad). 43 of the 47 ran `main --moved` to the end and cost 1.21 s to 2.67 s each. The four others cost 0.25 s, for `test_refuses_a_base_or_a_file_it_cannot_read`, which stops before any worktree, and under 0.01 s for the three rows of `test_refuses_a_new_file_no_to_names`, which stop in `argparse`. Every other class of the module cost 0.6 s together.

**On this macOS machine.** `bin/test tests/skills/test_test_layout.py -q -p no:xdist --durations=0` at `5172cf10c` passed 88 cases in 19.90 s, and `Test_moved`'s calls took 19.46 s of it (executed). A case that runs `main --moved` costs about 0.45 s. Under `cProfile` over `Test_moved` (executed: `before-moved.prof` in this phase's scratch), `_moved_main` took 18.9 s of 20.9 s over 46 calls. Of that, `_collected`'s two `pytest --collect-only` processes per case took 7.9 s, the `git show` that `_test_modules` runs for every module of the base under `tests/`, 13 a case, took 6.9 s, and the other git commands of a case, `rev-parse`, `show` of each old file, `ls-tree`, `worktree add` and `worktree remove`, took the rest of the 10.9 s that 819 git processes cost. `moved` itself took 0.6 s over 43 calls. So a case started about 19 git processes and two Python processes, and the reading its fact was about cost 0.014 s of it. The profiler inflates small calls, so these are shares and not seconds of a plain run.

No cost stood in `tests/conftest.py`. The module takes `ROOT`, `census_case`, `commit_everything_as_e`, `git_out` and `write` from it, and of these only the world's build, once per module and worker, and the cases of `Test_main` that copy the world or start a repository of one file run git (read: `tests/conftest.py:1069` to `:1112`). So no change to that file would cut this module's cost, and the spawn's bar on it cost this phase nothing.

### What the rebuild changed

`88f5a04dd` does the rebuild, and `76e9b8a32` returns one row to a `main` run after the mutation table.

- **`Test_moved` calls `moved` with texts.** `WORLD` holds every file of the base under `tests/` by path, and `_moved_world` commits it, so the world is written in one place. `moved_lines(news, beside, olds)` hands `moved` the old files from `WORLD`, the new files, and each side's modules read through `layout._test_modules`, the base's from `WORLD` and the working tree's from `WORLD` with the case's files written over it. Every one of the 42 rows of the three parametrized cases stays a row of the same case under the same id, and asserts the same `moved:` lines, less the count line that `_moved_main` adds after `pytest` collects. The 42 pass, so for each row the texts read in the process give the lines that `main` printed over git and the disk.
- **`Test_main` holds every case that calls `main`.** `CONTRIBUTING.md` *The test layout* puts a case in the class of the function it calls, and with `Test_moved`'s rows on `moved` the cases that call `main --moved` go to `Test_main`. Eight rows run `main --moved` over a copy of the world: `test_accepts_a_pure_move_and_removes_the_base_worktree` over `every-kind-of-move`, `a-name-imported-from-a-test-file-in-an-area`, `a-name-imported-from-a-test-file-whose-name-is-not-ascii` and `an-old-file-in-both-sets`, `test_refuses_a_moved_group_with_exit_one` over `a-cut`, `a-case-landing-twice` and `a-changed-name-in-another-test-file`, and `test_refuses_to_let_a_removal_git_did_not_answer_replace_the_run`. `test_refuses_a_base_or_a_file_it_cannot_read` and the three rows of `test_refuses_a_new_file_no_to_names` moved there unchanged.
- **`an-old-file-in-both-sets` runs `main` again.** Its unit form let mutant 144 live, `_collected` over the old files in the working tree instead of the base's worktree, and the base file's `main` run of the row killed it. Only a run whose old file also changes in the working tree tells the two apart, so `76e9b8a32` adds the row to the accepting `main` case, where it is red against mutant 144 on its exit code, with the line `moved: count: the new files collect 5 items, the old files 4 at the base` (executed).

The local figures after the rebuild are in the second part below. The figure that judges the phase is the Windows leg's, from the orchestrator's run at this phase's Status commit (`frame/design.md` S1).

### Departures from the frame

- **The `--moved` runs moved from `Test_moved` to `Test_main`.** *Scope* item 5 names which cases keep `main --moved`, not their class. The grounds are `CONTRIBUTING.md` *The test layout*, *A case stands in the file of what it holds*, which puts a case that calls a function in that function's class. Three cases moved with their bodies unchanged and their names kept, and the record of `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/trail/phases/phase-5.md` names one of them under its old class, as a record of its own time.
- **Each kept `main` row also stays a unit row.** The unit rows hold what `moved` reads, and the `main` rows hold that `_moved_main` hands it the same texts from git and the disk, so each of the eight is two cases with two facts. A unit row costs under 0.01 s.

### The four parts `CONTRIBUTING.md` *The test layout* asks of a rebuilt module

**1. The move check, and the mutation table.**

`bin/seal layout --moved 5172cf10c --from tests/skills/test_test_layout.py --to tests/skills/test_test_layout.py` exits 1 at `76e9b8a32` (executed). Its last line reads `seal layout: moved: 41 old cases, 94 items against 87 at 5172cf10c1c6, 11 failed`. The three parametrized cases of `Test_moved` changed their bodies, the two cases that moved to `Test_main` and take `_moved_world` find its definition changed, and the two new cases of `Test_main` stand for no old case. So the mutation table carries part 1.

The mutants sit at the decision points of every function of `skills/verify/scripts/test_layout.py`, the classes the phase kept as they stand among them (`frame/plan.md` *Alternatives considered*, A2). All 165 ran in one call against `88f5a04dd` (executed): `bin/seal mutate skills/verify/scripts/test_layout.py --replace OLD NEW ... --tests "bin/test tests/skills/test_test_layout.py -q -x"`, built by `run_mutants.py` from `mutants.py` in this phase's scratch. It printed `seal mutate: 165 mutants, 118 red, 47 SURVIVED, 0 with no verdict (236.4s)`. Under `-n auto`, `-x` stops the run with exit 2, which is the exit each red line shows. Each row shows the lines the mutant changes, joined. The full OLD and NEW of each are in `mutants.py`. The table measures this test file alone: a case of another file that runs the script, such as the `--check` over this repository in `tests/behaviour/test_this_repository_passes_its_own_checks.py`, was not run against the mutants.

The base column is filled for a survivor alone. The 47 survivors ran again against the test file at `5172cf10c`, copied to `tests/skills/test_tmp_test_layout_base.py` and removed after the run. That call printed `seal mutate: 47 mutants, 1 red, 46 SURVIVED, 0 with no verdict (250.0s)` (executed). The red one is mutant 144, and `76e9b8a32` gives the new file a case seen red on it, as the paragraph above says. So each of the other 46 is a gap older than this phase, and the phase lost no fact that killed one. Why they live, by what no case gives the unit:

- 1, 36, 58: no case hands `declared_target`, `check`'s read of a target or `pairs` a source that does not parse at the point the handler guards.
- 3, 6, 20, 60: no case's source puts a `from` import before `TARGET` or a non-string expression first, and no case's file holds a class not named `Test...` that `check` would judge or that holds a `test` method.
- 10, 29, 41: no case's target sits under a dot-led directory that shares a stem, no tracked path under `tests/` shares a target's stem, and no target defines a public class with no case class.
- 23, 24, 25, 26, 28: no case's case name holds `accepts` or `refuses` past its prefix, and no case assigns `test_census` with several targets, under another name or with another argument.
- 50: no case of `pairs` reads a parameter of its own as an argument.
- 65, 67, 68, 70, 71, 73, 76, 79: no old file of the world has a positional-only or keyword-only parameter, a `parametrize` of names with spaces or as a list, a non-string `usefixtures` argument, `autouse=False`, a `usefixtures` mark on a case, or an autouse fixture in the conftest.
- 92, 100, 103, 104: no name of the world is bound twice in one body, an attribute is read of a name the node does not read, a relative import binds a name a case reads, or a module imports from itself.
- 114, 115, 120: no row has a fixture requested in the working tree only, and no row's new files reach `moved` out of path order.
- 124, 125: no case runs with `PYTEST_ADDOPTS` set or a collection that fails.
- 128, 130, 131: no world holds two modules of one name at two depths, or a module the reader cannot read.
- 135, 137, 141: no base lists a module `git show` refuses or a module in a subdirectory, and no case's `worktree add` fails.
- 149: `gitcmd.git_path` changes a path on Windows alone, and the table ran on macOS.
- 153, 158, 159, 161, 164, 165: no `--moved` case names a path outside a repository, and no `--check` case of the module reads a peer outside its paths or a conftest helper through `main`, a file path given to `--check` that exists, or a `.py` file under `tests/` not named `test_*`; mutant 161 adds an empty path to the tracked set, which no case asks about.

The phase adds no case for them, as phases 2 to 4 added none for theirs: the frame rebuilds existing cases (`frame/design.md` *Scope* item 5), and `agents/crafter.md` *Never* bars building beyond the request. None sits in a gate that refuses a ready pull request: `--moved` is the move check a contributor runs for a phase record, and `--check` runs in this repository's suite. `gaps.md` *Not done* names the 46.

| # | Unit | Old | New | New file | `5172cf10c` |
|---|---|---|---|---|---|
| 1 | `declared_target` | `except SyntaxError: return None return _declared(tree)` | `except ValueError: return None return _declared(tree)` | survived | survived |
| 2 | `_declared` | `if body and _is_docstring(body[0]): body = body[1:]` | `if False: body = body[1:]` | red |  |
| 3 | `_declared` | `while body and isinstance(body[0], (ast.Import, ast.ImportFrom)):` | `while body and isinstance(body[0], ast.Import):` | survived | survived |
| 4 | `_declared` | `if not isinstance(name, ast.Name) or name.id != TARGET_NAME:` | `if not isinstance(name, ast.Name):` | red |  |
| 5 | `_declared` | `if not isinstance(node.value, ast.Constant) or not isinstance( node.value.value, str ):` | `if not isinstance(node.value, ast.Constant):` | red |  |
| 6 | `_is_docstring` | `and isinstance(node.value.value, str) )` | `)` | survived | survived |
| 7 | `_stem` | `return base.rsplit(".", 1)[0].replace("-", "_")` | `return base.rsplit(".", 1)[0]` | red |  |
| 8 | `file_name_for` | `if not target.endswith(".py"): return None stem` | `if False: return None stem` | red |  |
| 9 | `file_name_for` | `if any(_stem(other) == stem for other in shipped if other != target):` | `if any(_stem(other) == stem for other in shipped):` | red |  |
| 10 | `file_name_for` | `parent = parent.lstrip(".").replace("-", "_")` | `parent = parent.replace("-", "_")` | survived | survived |
| 11 | `_area` | `first = first.lstrip(".")` | (line removed) | red |  |
| 12 | `_area` | `if not rest or first + "/" == TESTS:` | `if not rest:` | red |  |
| 13 | `definitions` | `found[node.name] = "function"` | `found[node.name] = "class"` | red |  |
| 14 | `definitions` | `if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)): found[node.name] = "function"` | `if isinstance(node, ast.FunctionDef): found[node.name] = "function"` | red |  |
| 15 | `_helpers` | `if node.name.startswith("test"): continue # From column 0` | `if False: continue # From column 0` | red |  |
| 16 | `_helpers` | `lineno=min([node.lineno] + [d.lineno for d in node.decorator_list]),` | `lineno=node.lineno,` | red |  |
| 17 | `_helpers` | `except SyntaxError: return []` | `except ValueError: return []` | red |  |
| 18 | `twins` | `(name, files) for (name, _text), files in where.items() if len(files) > 1` | `(name, files) for (name, _text), files in where.items() if len(files) > 2` | red |  |
| 19 | `twins` | `if rel not in files: files.append(rel)` | `if True: files.append(rel)` | red |  |
| 20 | `_test_classes` | `if isinstance(node, ast.ClassDef) and node.name.startswith("Test") ]` | `if isinstance(node, ast.ClassDef) ]` | survived | survived |
| 21 | `_cases` | `if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test") ]` | `if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) ]` | red |  |
| 22 | `_missing_kinds` | `for prefix in (ACCEPTS, REFUSES)` | `for prefix in (ACCEPTS,)` | red |  |
| 23 | `_missing_kinds` | `if not any(name.startswith(prefix) for name in names)` | `if not any(prefix in name for name in names)` | survived | survived |
| 24 | `runs_the_censuses` | `if not isinstance(node, ast.Assign) or len(node.targets) != 1:` | `if not isinstance(node, ast.Assign):` | survived | survived |
| 25 | `runs_the_censuses` | `if not (isinstance(name, ast.Name) and name.id == "test_census"):` | `if not isinstance(name, ast.Name):` | survived | survived |
| 26 | `runs_the_censuses` | `if not isinstance(call, ast.Call) or len(call.args) != 1:` | `if not isinstance(call, ast.Call):` | survived | survived |
| 27 | `runs_the_censuses` | `called = func.id if isinstance(func, ast.Name) else getattr(func, "attr", None)` | `called = func.id if isinstance(func, ast.Name) else None` | red |  |
| 28 | `runs_the_censuses` | `and isinstance(argument, ast.Name) and argument.id == TARGET_NAME` | `and isinstance(argument, ast.Name)` | survived | survived |
| 29 | `check` | `p for p in tracked if p.endswith(".py") and not p.startswith(TESTS)` | `p for p in tracked if p.endswith(".py")` | survived | survived |
| 30 | `check` | `if not runs_the_censuses(tree):` | `if False:` | red |  |
| 31 | `check` | `if target not in tracked:` | `if False:` | red |  |
| 32 | `check` | `flow = rel.startswith(E2E)` | `flow = False` | red |  |
| 33 | `check` | `module = target.endswith(".py") and not flow` | `module = not flow` | red |  |
| 34 | `check` | `if posixpath.basename(rel) != expected:` | `if False:` | red |  |
| 35 | `check` | `if posixpath.dirname(rel) + "/" != area:` | `if False:` | red |  |
| 36 | `check` | `except SyntaxError: refused.append(f"refused: {rel}: {TARGET_NAME} {target} does not parse")` | `except ValueError: refused.append(f"refused: {rel}: {TARGET_NAME} {target} does not parse")` | survived | survived |
| 37 | `check` | `if cls.name == MODULE_CLASS: continue` | `if False: continue` | red |  |
| 38 | `check` | `if name not in defs:` | `if False:` | red |  |
| 39 | `check` | `elif not flow: continue` | `elif False: continue` | red |  |
| 40 | `check` | `and not name.startswith("_")` | (line removed) | red |  |
| 41 | `check` | `defs[name] == "function"` | `True` | survived | survived |
| 42 | `check` | `if not set(files) & set(tests): continue` | `if False: continue` | red |  |
| 43 | `check` | `if declared.intersection(files):` | `if True:` | red |  |
| 44 | `check` | `for name, files in twins(peers or tests):` | `for name, files in twins(tests):` | red |  |
| 45 | `_Normalised` | `if isinstance(node.value, str): return ast.copy_location(ast.Constant(value=""), node)` | `if False: return ast.copy_location(ast.Constant(value=""), node)` | red |  |
| 46 | `_Normalised` | `return ast.copy_location(ast.Name(id="_", ctx=node.ctx), node)` | `return node` | red |  |
| 47 | `_carries_no_input` | `return not argument.elts` | `return False` | red |  |
| 48 | `_carries_no_input` | `return not argument.keys` | `return False` | red |  |
| 49 | `_carries_no_input` | `return isinstance(argument, ast.Constant) and argument.value is None` | `return False` | red |  |
| 50 | `_calls` | `local = {arg.arg for arg in ast.walk(case.args) if isinstance(arg, ast.arg)}` | `local = set()` | survived | survived |
| 51 | `_calls` | `if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store) }` | `if False }` | red |  |
| 52 | `_calls` | `isinstance(callee, ast.Attribute) and callee.attr == function )` | `False )` | red |  |
| 53 | `_calls` | `if named and given and not reads & local:` | `if named and given:` | red |  |
| 54 | `_calls` | `if named and given and not reads & local:` | `if named and not reads & local:` | red |  |
| 55 | `pairs` | `if function and _calls(first, function) & _calls(second, function):` | `if False:` | red |  |
| 56 | `pairs` | `elif _body(first) == _body(second):` | `elif False:` | red |  |
| 57 | `pairs` | `for second in cases[i + 1 :]:` | `for second in cases[i:]:` | red |  |
| 58 | `pairs` | `except SyntaxError: continue for cls in _test_classes(tree): function` | `except ValueError: continue for cls in _test_classes(tree): function` | survived | survived |
| 59 | `_all_cases` | `if node.name.startswith("test"): found.append((node.name, None, node))` | `if True: found.append((node.name, None, node))` | red |  |
| 60 | `_all_cases` | `elif isinstance(node, ast.ClassDef) and node.name.startswith("Test"):` | `elif isinstance(node, ast.ClassDef):` | survived | survived |
| 61 | `_without_docstring` | `return body[1:] if body and _is_docstring(body[0]) else body` | `return body` | red |  |
| 62 | `_moved_form` | `node.name = ""` | (line removed) | red |  |
| 63 | `_moved_form` | `inner.body = _without_docstring(inner.body) or [ast.Pass()]` | `pass` | red |  |
| 64 | `_moved_form` | `if params and params[0].arg == "self": del params[0]` | `if False: del params[0]` | red |  |
| 65 | `_moved_form` | `params = node.args.posonlyargs or node.args.args` | `params = node.args.args` | survived | survived |
| 66 | `_parametrized` | `and getattr(mark.func, "attr", None) == "parametrize"` | `and getattr(mark.func, "attr", None) == "parametrized"` | red |  |
| 67 | `_parametrized` | `names \|= {n.strip() for n in first.value.split(",")}` | `names \|= {first.value}` | survived | survived |
| 68 | `_parametrized` | `elif isinstance(first, (ast.List, ast.Tuple)):` | `elif False:` | survived | survived |
| 69 | `_used` | `and getattr(call.func, "attr", None) == "usefixtures"` | `and getattr(call.func, "attr", None) == "usefixture"` | red |  |
| 70 | `_used` | `if isinstance(a, ast.Constant) and isinstance(a.value, str) }` | `if isinstance(a, ast.Constant) }` | survived | survived |
| 71 | `_parameters` | `return [a.arg for a in args.posonlyargs + args.args + args.kwonlyargs]` | `return [a.arg for a in args.args]` | survived | survived |
| 72 | `_fixtures` | `if getattr(func, "attr", None) != "fixture":` | `if False:` | red |  |
| 73 | `_fixtures` | `k.arg == "autouse" and getattr(k.value, "value", False) is True` | `k.arg == "autouse"` | survived | survived |
| 74 | `_fixtures` | `func = call.func if call else mark` | `func = mark` | red |  |
| 75 | `_requested` | `names = set(_parameters(case)) - {"self"} - _parametrized(case)` | `names = set(_parameters(case)) - {"self"}` | red |  |
| 76 | `_requested` | `names \|= _used(case.decorator_list)` | (line removed) | survived | survived |
| 77 | `_requested` | `if cls is not None: names \|= _used(cls.decorator_list)` | `if False: names \|= _used(cls.decorator_list)` | red |  |
| 78 | `_requested` | `isinstance(t, ast.Name) and t.id == "pytestmark" for t in node.targets` | `False for t in node.targets` | red |  |
| 79 | `_requested` | `if conftest is not None: scopes.append(conftest.body)` | `if False: scopes.append(conftest.body)` | survived | survived |
| 80 | `_requested` | `names \|= {n for n, (_d, auto) in _fixtures(body).items() if auto}` | `names \|= set()` | red |  |
| 81 | `_resolver` | `scopes = ([(label, cls)] if cls is not None else []) + [(label, None)]` | `scopes = [(label, None)]` | red |  |
| 82 | `_resolver` | `if conftest is not None: scopes.append((CONFTEST_MODULE, None))` | `if False: scopes.append((CONFTEST_MODULE, None))` | red |  |
| 83 | `_resolver` | `requests = set(_parameters(node)) - {"request"}` | `requests = set()` | red |  |
| 84 | `_reached` | `todo += sorted(hit[1] - seen)` | `pass` | red |  |
| 85 | `_reached` | `if hit is not None: found.append(hit[2])` | `if False: found.append(hit[2])` | red |  |
| 86 | `_alias_name` | `return (alias.asname or alias.name).split(".")[0]` | `return alias.name.split(".")[0]` | red |  |
| 87 | `_binds` | `names.add(inner.name) continue` | `names.add(inner.name)` | red |  |
| 88 | `_binds` | `if isinstance(inner, ast.Name) and not isinstance(inner.ctx, ast.Load):` | `if isinstance(inner, ast.Name):` | red |  |
| 89 | `_binds` | `names \|= {_alias_name(a) for a in inner.names}` | `pass` | red |  |
| 90 | `_form` | `getattr(statement, "module", None),` | (line removed) | red |  |
| 91 | `_form` | `if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)): return _moved_form(statement)` | `if False: return _moved_form(statement)` | red |  |
| 92 | `_Names.binders` | `found.setdefault(name, []).append(statement)` | `found[name] = [statement]` | survived | survived |
| 93 | `_Names.reads` | `names = {s.get_name() for s in table.get_symbols() if s.is_referenced()}` | `names = {s.get_name() for s in table.get_symbols()}` | red |  |
| 94 | `_Names.reads` | `if s.is_referenced() and s.is_global()` | `if s.is_referenced()` | red |  |
| 95 | `_Names.reads` | `) and "self" in _parameters(inner): continue` | `) and False: continue` | red |  |
| 96 | `_Names.reads` | `and inner.value.id == "self"` | (line removed) | red |  |
| 97 | `_Names.reads` | `if _alias_name(alias) in loaded` | (line removed) | red |  |
| 98 | `_Names.reads` | `if owner == _alias_name(alias)` | (line removed) | red |  |
| 99 | `_Names.items` | `found += [(label, cls, f"self.{name}", name) for name in sorted(own)]` | `pass` | red |  |
| 100 | `_Names.items` | `if owner in names:` | `if True:` | survived | survived |
| 101 | `_Names.items` | `if _alias_name(alias) == owner and alias.name in self.modules` | `if _alias_name(alias) == owner` | red |  |
| 102 | `_Names.items` | `if module in self.modules ]` | `]` | red |  |
| 103 | `_Names.forms` | `and not statement.level` | (line removed) | survived | survived |
| 104 | `_Names.forms` | `and statement.module != label` | (line removed) | survived | survived |
| 105 | `_Names.forms` | `todo += self.items(label, cls, statement)` | `pass` | red |  |
| 106 | `_Names.forms` | `return {key: sorted(set(forms)) for key, forms in found.items()}` | `return {key: forms for key, forms in found.items()}` | red |  |
| 107 | `_name_change` | `apart = sorted(k for k in before.keys() & after.keys() if before[k] != after[k])` | `apart = []` | red |  |
| 108 | `_name_change` | `return apart + sorted(before.keys() ^ after.keys())` | `return apart` | red |  |
| 109 | `_fixture_change` | `if before is None and after is None: continue` | `if False: continue` | red |  |
| 110 | `_fixture_change` | `return name, "defined in the working tree only"` | `return name, "defined at the base only"` | red |  |
| 111 | `_fixture_change` | `if before[0] != after[0]:` | `if False:` | red |  |
| 112 | `_fixture_change` | `todo += sorted(before[1] - seen)` | `pass` | red |  |
| 113 | `moved` | `if not match:` | `if match is None:` | red |  |
| 114 | `moved` | `apart = sorted(before ^ after)` | `apart = sorted(before - after)` | survived | survived |
| 115 | `moved` | `side = "at the base" if apart[0] in before else "in the working tree"` | `side = "at the base"` | survived | survived |
| 116 | `moved` | `if change:` | `if False:` | red |  |
| 117 | `moved` | `if len(names) == 1:` | `if len(names) >= 1:` | red |  |
| 118 | `moved` | `for at, at_class, fixture in _reached(resolve, before): todo += side.items(at, at_class, fixture)` | `for at, at_class, fixture in _reached(resolve, before): pass` | red |  |
| 119 | `moved` | `lines += [ f"moved: {place}: body: stands for no old case" for place, *_rest in left ]` | `pass` | red |  |
| 120 | `moved` | `for new_rel in sorted(new):` | `for new_rel in new:` | survived | survived |
| 121 | `moved` | `_place, new_rel, new_cls, new_case = match.pop(0)` | `_place, new_rel, new_cls, new_case = match.pop()` | red |  |
| 122 | `moved` | `old_conf = before_side.trees.get(CONFTEST_MODULE)` | `old_conf = None` | red |  |
| 123 | `_interpreter` | `if importlib.util.find_spec("pytest") is not None: return sys.executable` | `if False: return sys.executable` | red |  |
| 124 | `_collected` | `if k not in ("PYTEST_ADDOPTS", "PYTEST_PLUGINS")` | `if True` | survived | survived |
| 125 | `_collected` | `if run.returncode != 0:` | `if False:` | survived | survived |
| 126 | `_collected` | `if not line.strip(): break` | `if False: break` | red |  |
| 127 | `_collected` | `return sum(1 for item in items if item.rsplit("::", 1)[-1] != "test_census")` | `return len(items)` | red |  |
| 128 | `_test_modules` | `for path in sorted(paths, key=lambda p: (p.count("/"), p)):` | `for path in sorted(paths):` | survived | survived |
| 129 | `_test_modules` | `if name.endswith(".py"):` | `if True:` | red |  |
| 130 | `_test_modules` | `if source is not None:` | `if True:` | survived | survived |
| 131 | `_test_modules` | `found.setdefault(name[: -len(".py")], source)` | `found[name[: -len(".py")]] = source` | survived | survived |
| 132 | `_moved_main` | `if sha.returncode != 0: raise Unreadable(f"{base} names no commit")` | `if False: raise Unreadable(f"{base} names no commit")` | red |  |
| 133 | `_moved_main` | `if shown.returncode != 0: raise Unreadable(f"{path} is not a file at {sha[:12]}")` | `if False: raise Unreadable(f"{path} is not a file at {sha[:12]}")` | red |  |
| 134 | `_moved_main` | `if new[path] is None:` | `if False:` | red |  |
| 135 | `_moved_main` | `return shown.stdout if shown.returncode == 0 else None` | `return shown.stdout` | survived | survived |
| 136 | `_moved_main` | `listed = gitcmd.git(root, "ls-tree", "-r", "-z", "--name-only", sha, TESTS).stdout` | `listed = gitcmd.git(root, "ls-tree", "-r", "--name-only", sha, TESTS).stdout` | red |  |
| 137 | `_moved_main` | `listed = gitcmd.git(root, "ls-tree", "-r", "-z", "--name-only", sha, TESTS).stdout` | `listed = gitcmd.git(root, "ls-tree", "-z", "--name-only", sha, TESTS).stdout` | survived | survived |
| 138 | `_moved_main` | `subdirectories[:] = sorted(d for d in subdirectories if d != "__pycache__") present +=` | `subdirectories[:] = [] present +=` | red |  |
| 139 | `_moved_main` | `_test_modules(listed, shown_at_base),` | `_test_modules(listed, lambda p: _read(root, p)),` | red |  |
| 140 | `_moved_main` | `_test_modules(present, lambda p: _read(root, p)),` | `_test_modules(listed, lambda p: _read(root, p)),` | red |  |
| 141 | `_moved_main` | `if added.returncode != 0:` | `if False:` | survived | survived |
| 142 | `_moved_main` | `gitcmd.git(root, "worktree", "remove", "--force", tree)` | `pass` | red |  |
| 143 | `_moved_main` | `except gitcmd.Failed as unanswered: print(` | `except ZeroDivisionError as unanswered: print(` | red |  |
| 144 | `_moved_main` | `before = _collected(python, tree, old_rels)` | `before = _collected(python, root, old_rels)` | survived; red after `76e9b8a32` | red |
| 145 | `_moved_main` | `after = _collected(python, root, new_rels)` | `after = _collected(python, root, old_rels)` | red |  |
| 146 | `_moved_main` | `if after != before:` | `if after < before:` | red |  |
| 147 | `_moved_main` | `cases = sum(len(_all_cases(ast.parse(source))) for source in old.values())` | `cases = 0` | red |  |
| 148 | `_moved_main` | `return 1 if lines else 0` | `return 0` | red |  |
| 149 | `_moved_main` | `return gitcmd.git_path(os.path.relpath(os.path.abspath(path), root))` | `return os.path.relpath(os.path.abspath(path), root)` | survived | survived |
| 150 | `main` | `if (args.olds or args.news) and args.moved is None:` | `if False:` | red |  |
| 151 | `main` | `if args.moved is not None and (not args.olds or not args.news or args.paths):` | `if args.moved is not None and (not args.olds or not args.news):` | red |  |
| 152 | `main` | `return _laid_out(args) except gitcmd.Failed as unanswered:` | `return _laid_out(args) except ZeroDivisionError as unanswered:` | red |  |
| 153 | `_laid_out` | `if not root: print(f"seal layout: {start} is not inside a git repository", flush=True) return 2 try:` | `if False: print(f"seal layout: {start} is not inside a git repository", flush=True) return 2 try:` | survived | survived |
| 154 | `_laid_out` | `except Unreadable as exc:` | `except ZeroDivisionError as exc:` | red |  |
| 155 | `_laid_out` | `start = first if os.path.isdir(first) else os.path.dirname(os.path.abspath(first))` | `start = first` | red |  |
| 156 | `_laid_out` | `if missing:` | `if False:` | red |  |
| 157 | `_laid_out` | `if args.pairs:` | `if False:` | red |  |
| 158 | `_laid_out` | `peers = _read_tests(root, [os.path.join(root, "tests")])` | `peers = dict(tests)` | survived | survived |
| 159 | `_laid_out` | `if shared is not None: peers["tests/conftest.py"] = shared` | `if False: peers["tests/conftest.py"] = shared` | survived | survived |
| 160 | `_laid_out` | `return 1 if refused else 0` | `return 0` | red |  |
| 161 | `_tracked` | `return {path for path in result.stdout.split("\0") if path}` | `return set(result.stdout.split("\0"))` | survived | survived |
| 162 | `_tracked` | `result = gitcmd.git(root, "ls-files", "-z", check=True)` | `result = gitcmd.git(root, "ls-files", "-z")` | red |  |
| 163 | `_read` | `except OSError: return None   def _read_tests` | `except ValueError: return None   def _read_tests` | red |  |
| 164 | `_read_tests` | `if os.path.isfile(path): files.append(path) continue` | `if False: files.append(path) continue` | survived | survived |
| 165 | `_read_tests` | `if name.startswith("test_") and name.endswith(".py")` | `if name.endswith(".py")` | survived | survived |

**2. Cases and seconds, before and after, on this macOS machine.** The figures are local. `frame/design.md` *Grounding*, *What a figure of the Windows leg can show*, takes no local figure as evidence of a saving on the Windows leg. The module's Windows figure is the orchestrator's `workflow_dispatch` run at this phase's Status commit (`frame/design.md` S1).

| Measure | Before, `5172cf10c` | After, `76e9b8a32` |
|---|---|---|
| Cases of the module | 88 | 95 |
| `bin/test tests/skills/test_test_layout.py -q -p no:xdist`, the module | 19.90 s | 4.62 s |
| The same runs, the cases that run `main --moved` to the end | 43 cases, about 0.45 s each | 8 cases, 0.47 s to 0.52 s each |
| The same runs, `Test_moved`'s cases | 19.46 s | 0.23 s |
| `bin/test tests/skills/test_test_layout.py -q`, under `-n auto` | not run | 1.58 s |
| Windows leg, the module, from the three runs' `test-durations` artifacts | 106 s, 103 s and 76 s in runs 45181872904, 45189798316 and 45203717820 | not measured |

The per-case figures of both local runs are in this phase's scratch, `before-durations.txt` and `after-durations.txt`. The seven cases the module gained are the seven rows of `Test_main`'s two new cases. No old case left: the 42 rows of `Test_moved` stay, and its five other cases moved to `Test_main`.

**Q2: the floor.** The phase gives no answer to Q2 for this module, since no local figure is evidence of the Windows leg. The real processes the module keeps are the eight `main --moved` rows, each a worktree and two `pytest --collect-only` runs, which cost 1.21 s to 2.67 s each in run 45203717820, so about 10 s to 21 s by that run's figures, and the cases of `Test_main` that start a repository of one file, which cost under 0.3 s together there. The orchestrator reads the module's figure at this phase's Status commit against the modules no phase changed in the same run, as `frame/design.md` *Grounding* says.

**3. The real-git cases kept.** Each runs `main` over real git:

- `Test_main::test_accepts_a_pure_move_and_removes_the_base_worktree`, rows `every-kind-of-move`, `a-name-imported-from-a-test-file-in-an-area`, `a-name-imported-from-a-test-file-whose-name-is-not-ascii` and `an-old-file-in-both-sets`. They show that `_moved_main` reads the base through `git show` and `git ls-tree -z` and the working tree from a walk of the disk at every depth, that `pytest` collects as many items on both sides, the census case left out, that the old files are collected at the base, that the last line counts the old cases, and that the base's worktree is removed.
- `Test_main::test_refuses_a_moved_group_with_exit_one`, rows `a-cut`, `a-case-landing-twice` and `a-changed-name-in-another-test-file`. They show the count line where the new files collect fewer items and where they collect more, exit 1 with the last line counting the failures, and a module read at the base through git against the one the working tree holds.
- `Test_main::test_refuses_to_let_a_removal_git_did_not_answer_replace_the_run` (#1573), `Test_main::test_refuses_a_base_or_a_file_it_cannot_read`, and `Test_main`'s `--check` cases that start a repository of one file, `test_refuses_a_git_that_did_not_answer_in_one_line` and `test_refuses_a_listing_git_refused_in_one_line`, as they stood.

**4. Old cases cut or rewritten.** No case was cut. The classes `Test_declared_target`, `Test_file_name_for`, `Test_definitions`, `Test_twins`, `Test_check`, `Test_pairs` and the cases of `Test_main` that call `--check` or `--pairs` are placed as they stand, and so is `test_census`. No case of the module reads a document's prose as its fact, and none waits for another module's rebuild.

- `Test_moved::test_accepts_a_pure_move`, its 12 rows: each ran `main --moved` over a copy of the world and asserted exit 0, no `moved:` line, the last line with its old cases and items, and no worktree left behind. Each now asserts that `moved_lines` gives no line, under the same id. The exit code, the last line and the worktree are held by `Test_main::test_accepts_a_pure_move_and_removes_the_base_worktree`, which runs `every-kind-of-move`, `a-name-imported-from-a-test-file-in-an-area` and `a-name-imported-from-a-test-file-whose-name-is-not-ascii` through `main` with the old assertions. Only `Test_main`'s `--moved` runs reach `_moved_main`, so its mutants that the table reads red, 144 among them after `76e9b8a32`, are red against those runs.
- `Test_moved::test_accepts_an_old_file_split_across_two_new_files`, its 2 rows: each asserted exit 0, `0 failed` and no worktree left. Each now asserts that `moved_lines` gives no line. `an-old-file-in-both-sets` also runs through `main` in `Test_main::test_accepts_a_pure_move_and_removes_the_base_worktree`, which holds the old files collected at the base (mutant 144).
- `Test_moved::test_refuses_a_cut_a_merge_an_edited_body_and_a_changed_fixture`, its 28 rows: each asserted exit 1, its `moved:` lines, the count of failures on the last line, and no worktree left. Each now asserts the same `moved:` lines from `moved_lines`, less the count line, which `a-cut`, `a-merge`, `two-alike-merged` and `a-case-landing-twice` carried. `Test_main::test_refuses_a_moved_group_with_exit_one` holds the count line, fewer over `a-cut` and more over `a-case-landing-twice`, the exit code and the worktree, and holds the base's module read through git over `a-changed-name-in-another-test-file`. Mutants 139, 140, 145 and 146 change what `_moved_main` reads or counts, and each is red, against the `--moved` runs alone that reach it.
- `Test_moved::test_refuses_to_let_a_removal_git_did_not_answer_replace_the_run`, `Test_moved::test_refuses_a_base_or_a_file_it_cannot_read` and the 3 rows of `Test_moved::test_refuses_a_new_file_no_to_names`: moved to `Test_main` under the same names, their bodies unchanged.

### Checks at the phase's close

- `bin/test tests/skills/test_test_layout.py -q -p no:xdist --durations=0` at `76e9b8a32`: 95 passed in 4.62 s (executed, file order).
- `bin/test tests/skills/test_test_layout.py -q`: 95 passed in 1.58 s at `76e9b8a32` (executed, under `-n auto`).
- `bin/seal layout --check tests/skills/test_test_layout.py`: exit 0, `seal layout: 1 files read, 0 refused, 0 declare no TARGET` (executed). It prints one `report:` line, `function runs_the_censuses has no class Test_runs_the_censuses`, which stands at the base too. A report line refuses nothing.
- `bin/seal layout --pairs tests/skills/test_test_layout.py` names the same three pairs of `Test_main` at `88f5a04dd` as at `5172cf10c`, and the class's docstring states the world they differ by (executed).
- `bin/test tests/behaviour/test_this_repository_passes_its_own_checks.py -q --co`: 5 collected (executed), so `layout` still imports from the module (*Scope* item 9, S4).
- The *Phase boundary* set, `bin/test tests/skills/test_test_layout.py tests/behaviour tests/text -q`: 970 passed, 9 skipped (executed, at `76e9b8a32`). Its six warnings name citations that other work items' pending rule changes correct, as at phase 4.
- `uvx ruff format --check` and `uvx ruff check` over the changed file: clean (executed).
- `git worktree list` names the repository's own worktree alone after the mutation runs and the move check (executed), and no `test_tmp_*` file stands under `tests/`.
- The suite: `unverified`. The broad gate is the orchestrator's, once the review rounds settle.
