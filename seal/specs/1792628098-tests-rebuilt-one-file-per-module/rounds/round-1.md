# 1792628098-tests-rebuilt-one-file-per-module — review round 1

target: 8aa42bf8 against release/v0.22.3

This round reviewed phases 1 to 4 and the frame corrections at 8aa42bf8, read in a scratch clone of that commit. Phases 5 to 7 belong to a later round. No earlier round exists, so no fact is carried; every fact below was established this round.

## Findings

### 1. A test file that declares TARGET but drops its census line takes its module out of every census

severity: must
location: `tests/test_censuses.py:736-749`, `skills/verify/scripts/test_layout.py:206-291`, `tests/test_test_layout.py:33-50`, `CONTRIBUTING.md:244-249`
evidence: executed `bin/test tests/test_release_report.py tests/test_censuses.py -q -p no:xdist`, `bin/test tests/test_release_report.py -q -p no:xdist`
verdict: open

The sweep in `Test_module` skips every tracked file that some test file declares as its `TARGET` (`tests/test_censuses.py:740-747`). It assumes that the declaring file ends with `test_census = census_case(TARGET)`, and nothing checks the assumption. `bin/test-layout --check` does not refuse a declared file without that line, and the sweep reads the declaration, not the census case. Phases 5 to 7 declare `TARGET` in about 140 files, so one dropped line takes a shipped module out of all eight censuses and no case fails.

The probe showed it. In the scratch clone, the last line of `tests/test_release_report.py` was replaced and `PLANTED = "a\nb".splitlines()` was planted in `.github/scripts/release_report.py`. The module and the sweep then passed: 172 cases, exit 0. With the census line restored, the module failed on the planted call at line 315, exit 1.

`CONTRIBUTING.md:248-249` says `--check` refuses a file that declares `TARGET` and "breaks this", and the paragraph that "this" names holds the census line. The fix makes that sentence true. The layout check refuses the omission, and the sweep skips only the targets of files that run the case. `PLACED` in `tests/test_test_layout.py` then needs the census line, and `Test_check` gains a refusing case. `tests/test_censuses.py` imports `ast` at the top for the second half.

```python
# skills/verify/scripts/test_layout.py
CENSUS_CASE = "test_census = census_case(TARGET)"


def runs_the_censuses(tree):
    """Whether TREE assigns `test_census` a call of `census_case` on
    `TARGET` at its top level, called bare or as `conftest.census_case`."""
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        name, call = node.targets[0], node.value
        if not (isinstance(name, ast.Name) and name.id == "test_census"):
            continue
        if not isinstance(call, ast.Call) or len(call.args) != 1:
            continue
        func = call.func
        called = func.id if isinstance(func, ast.Name) else getattr(func, "attr", None)
        argument = call.args[0]
        if (
            called == "census_case"
            and isinstance(argument, ast.Name)
            and argument.id == TARGET_NAME
        ):
            return True
    return False


# check(), directly after `declared.add(rel)`:
        if not runs_the_censuses(tree):
            refused.append(
                f"refused: {rel}: does not assign {CENSUS_CASE}, "
                f"so no census judges {target}"
            )


# tests/test_censuses.py, Test_module, inside the walk:
                    with open(os.path.join(directory, name), encoding="utf-8") as f:
                        source = f.read()
                    if layout.runs_the_censuses(ast.parse(source)):
                        declared.add(layout.declared_target(source))
```

answer:

### 2. The census sweep passes when git lists no file

severity: should
location: `tests/test_censuses.py:738`, `tests/test_censuses.py:749`
evidence: executed `bin/test tests/test_tmp_r1_probe.py -q -p no:xdist`, `git show 6046f062:tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`
verdict: open

`git_listing` runs git with `check=False` and returns an empty list when git fails (`tests/conftest.py:226-245`). An empty listing leaves `found` empty, and the sweep passes having judged nothing. A tree git refuses to read, such as a checkout git calls of dubious ownership inside a container, produces exactly that.

The old censuses held this fact. At 6046f062, `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` line 563 asserted `files` with "git ls-files found no python at all", and line 1248 asserted `verdicts` with "git ls-files found no hook entry point at all". `phases/phase-3.md` records both cases as rewritten into the censuses and says nothing of the two assertions, and no case holds them now. Probe P1 patched the module's `git_listing` to return nothing, and the sweep case passed.

```python
        tracked, _missing = on_disk(ROOT, git_listing(ROOT, "ls-files", check=True))
        assert tracked, "git ls-files listed no tracked file, so the sweep judged nothing"
```

answer:

### 3. An exemption written at the end of a line no census flags is read as nothing and stays in the tree

severity: should
location: `tests/censuses.py:56-90`, `tests/test_censuses.py:98-117`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:44`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-3.md:23`
evidence: executed `bin/test tests/test_tmp_r1_probe.py -q -p no:xdist`
verdict: open

Claimed: `spec.md:44` and `phases/phase-3.md:23` say the census "refuses one written at the end of a line". Found: `_exempted` reads whole comment lines only (`COMMENT_LINE`, `tests/censuses.py:38`), so a comment that ends a line of code is never read. On a flagged line the census still fails, but only because the flag stands. On a line no census flags it passes. Probe P2 judged `x = 1  # exempt from splitlines: git output` in `hooks/x.py`, and `judge` returned nothing. That is the spent exemption the comment rule exists to remove. It is also the shape the first build of phase 3 wrote, as `phases/phase-3.md:23` tells.

The `at-the-end-or-ending-a-line` row of `Test_judge::test_refuses_an_exemption_out_of_place` passes because line 1 is flagged, so it pins the flag and not a refusal of the comment. With the fix that row names line 1 twice, and a row for an end-of-line exemption on an unflagged line is added.

```python
# tests/censuses.py; `import io` and `import tokenize` join the imports.
def _trailing(text, name):
    """The line numbers where an exemption from NAME ends a line of code.
    Python text only; text tokenize cannot read yields none."""
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
    except (tokenize.TokenError, SyntaxError):
        return []
    return [
        token.start[0]
        for token in tokens
        if token.type == tokenize.COMMENT
        and token.line[: token.start[1]].strip()
        and name in EXEMPTION.findall(token.string)
    ]


# _held(name, rel, text, flagged), before its return:
    if rel.endswith(".py"):
        out += [
            f"{rel}:{number}: {name}: the exemption ends a line, where the "
            "formatter moves it; put it on its own line above the line it exempts"
            for number in _trailing(text, name)
        ]
```

answer:

### 4. One exemption excuses every `.splitlines(` call on the line below it

severity: should
location: `tests/censuses.py:646-663`
evidence: executed `git show 6046f062:tests/test_every_reader_ends_a_line_where_gfm_does.py`, `sed -n 560,700p tests/censuses.py`
verdict: open

The old census counted the calls in each unit and failed on "one more call in a unit it does" list (6046f062, `tests/test_every_reader_ends_a_line_where_gfm_does.py`, the comment above `OUT_OF_CLASS` and the `more` assertion of `test_every_splitlines_call_left_is_named_with_its_reason`). The new census keys its flags by line (`tests/censuses.py:655`), so a second call written on an exempted line, such as `a.splitlines() + b.splitlines()`, passes under the one comment. Only this census narrowed. The old `encoding`, `coordinate_grammar` and `heading_rule` lists excused a whole unit, a whole file or a whole line, so a per-line comment is as strict or stricter for them.

```python
    calls = [
        node.func.end_lineno
        for node in ast.walk(ast.parse(text, rel))
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "splitlines"
    ]
    flagged = {line: MESSAGE for line in calls}  # MESSAGE: the sentence as it stands
    doubled = sorted({line for line in calls if calls.count(line) > 1})
    return _held("splitlines", rel, text, flagged) + [
        f"{rel}:{line}: splitlines: two calls on one line, and an exemption "
        "names one; put each call on a line of its own"
        for line in doubled
    ]
```

answer:

### 5. The twin check never reads `tests/conftest.py`, and a path argument narrows it to that path

severity: should
location: `skills/verify/scripts/test_layout.py:404-425`, `skills/verify/scripts/test_layout.py:455-464`, `skills/verify/scripts/test_layout.py:285-290`
evidence: executed `bin/test tests/test_tmp_r1_probe.py -q -p no:xdist`
verdict: open

`CONTRIBUTING.md:242-243` says a helper two test files use is defined once, in `tests/conftest.py`. The twins phase 4 removed come back as a module file that copies a conftest helper instead of importing it. `_read_tests` takes only `test_*.py`, so that copy is no twin. Probe P4 appended the source of `conftest.flattened` to `tests/test_test_layout.py`, a declared file, and `check` refused nothing. With `tests/conftest.py` added to the files read, the same copy was refused.

A path argument narrows the comparison too. `bin/test-layout --check tests/test_x.py`, the narrow form a contributor types for one module, compares the file's helpers with that file alone. Today no helper in a test file equals one in `tests/conftest.py` or `tests/censuses.py` (executed, `twins` over all three kinds of file). Phases 5 to 7 write the files where a copy would start.

```python
# main(): helpers are compared over every test file and tests/conftest.py,
# whatever the paths name; the paths still choose the files judged.
    tests = _read_tests(root, args.paths or [os.path.join(root, "tests")])
    peers = _read_tests(root, [os.path.join(root, "tests")])
    shared = _read(root, "tests/conftest.py")
    if shared is not None:
        peers["tests/conftest.py"] = shared
    ...
    refused, reported = check(
        tests, _tracked(root), lambda rel: _read(root, rel), every=args.all,
        peers=peers,
    )


# check(tests, tracked, read, every=False, peers=None):
    for name, files in twins(peers or tests):
        if not set(files) & set(tests):
            continue
        line = f"{name} is defined byte-identically in {', '.join(files)}"
        ...
```

answer:

### 6. `bin/test-layout --check` exits 0 on a path that names nothing

severity: should
location: `skills/verify/scripts/test_layout.py:404-412`, `skills/verify/scripts/test_layout.py:44-46`, `skills/verify/scripts/test_layout.py:449-455`
evidence: executed `bin/test tests/test_tmp_r1_probe.py -q -p no:xdist`
verdict: open

Probe P5 ran `main(["--check", "tests/test_no_such_file.py"])`. It returned 0 and printed `0 files read, 0 refused`. A misspelt module name reads as a pass to an agent that reads the exit code, and the docstring gives exit 2 to arguments that cannot be used. `_read_tests` walks a path that does not exist and finds nothing (`test_layout.py:408-418`).

```python
    missing = [path for path in args.paths if not os.path.exists(path)]
    if missing:
        print(f"test-layout: {', '.join(missing)} names no file or directory", flush=True)
        return 2

# The docstring's exit line:
# `--pairs` 0 whatever it prints. 2 for either: the directory is not inside a
# git repository, a path names no file or directory, or the arguments do not
# parse.
```

answer:

### 7. Phase 2 removed seven slow-case cases without a line each, and two of their facts are held by nothing

severity: should
location: `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-2.md:10`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-2.md:25`, `tests/test_conftest.py:39-49`, `tests/conftest.py:841`
evidence: executed `bin/test tests/test_conftest.py tests/test_ci_gives_the_checks_what_they_need.py -q -p no:xdist`, `git show 6046f062:tests/test_a_slow_case_names_itself.py`
verdict: open

`spec.md` rule 2 and `CONTRIBUTING.md` *The test layout* ask one line per case cut or rewritten, naming what it guarded and what holds it now. `tests/test_a_slow_case_names_itself.py` held eight cases. `phases/phase-2.md` names one, the timeout case that moved, and the other seven appear nowhere in phases 1 to 4 (executed, a listing of every case name gone from its file). Three of the seven guarded `SPECSEAL_CASE_CEILING_S`, which left the tree by design. Two guarded facts that are still in the tree and are now held by nothing.

- `test_the_ceiling_is_the_one_q6_set` asserted the value 90. Every case in `tests/test_conftest.py` sets `SLOW_CASE_S` itself (lines 35, 78 and 89). With `SLOW_CASE_S = 9000` in the scratch clone, both modules passed, 30 cases, exit 0.
- `test_the_hook_fails_a_slow_passing_call_and_nothing_else` ran a slow call that failed. `phases/phase-2.md:25` claims the report names every call past the value, passing or failing. The inner run (`tests/test_conftest.py:39-49`) holds no failing call, so no case pins the claim. Probe P6 shows `slow_lines` names a failed call today.

The fix adds the failing call to the inner run and a case for the value. `phases/phase-2.md` gains one line for each of the seven: the two `over_the_ceiling` cases are held by `Test_slow_lines`; the three variable cases guarded behaviour that left the tree; `test_the_ceiling_is_the_one_q6_set` is held by the new `Test_module` case; and the hook case is held by `Test_pytest_terminal_summary`.

```python
INNER_TESTS = """\
import time


def test_slow():
    time.sleep(0.6)


def test_slow_and_failing():
    time.sleep(0.6)
    assert False, "its own failure"


def test_quick():
    pass
"""


class Test_pytest_terminal_summary:
    def test_accepts_a_slow_case_named_and_failing_nothing(self, inner_run):
        code, out = inner_run
        assert code == 1, out
        assert "1 failed, 2 passed" in out, out
        assert "its own failure" in out, out
        assert "slow case: test_inner.py::test_slow ran " in out, out
        assert "slow case: test_inner.py::test_slow_and_failing ran " in out, out


class Test_module:
    def test_the_value_is_the_one_work_item_1791270165_set(self):
        assert conftest.SLOW_CASE_S == 90
```

answer:

### 8. CI fails `test_the_durations_file_prices_the_suite` from phase 3 on, and no phase record says so

severity: should
location: `.test_durations`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/plan.md:55`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:122`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-3.md:85`
evidence: executed `gh run view 39724802385 --json jobs`, `gh run view 39724802385 --log-failed`
verdict: open

CI run 39724802385 at 381d6c0f concluded `failure`. Five of its nine pytest legs failed on two cases. One is the overview census the orchestrator expects. The other is `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py::test_the_durations_file_prices_the_suite`: "507 of the 7538 collected cases (6.7%) have no price in .test_durations ... over the 5% STALE_SHARE". 8aa42bf8 changes only `plan.md` and `spec.md`, so the target is in the same state.

Phase 2's boundary ran this case and it passed. Phases 3 and 4 added and renamed cases, and their boundaries did not run it. `phases/phase-3.md:85` leaves the removed ids for phase 7, while `spec.md:122` says the smith prunes them per batch. `plan.md:55` refreshes the file from CI once at the end, which leaves every pytest leg red until phase 7, and a red leg hides a new failure behind the two known ones. Pruning alone does not clear the case, because the unpriced ids are new ones; only a refresh prices them.

```text
gh run download 39724802385 -n test-durations -D <dir>
then move <dir>/.test_durations over .test_durations and commit it.

spec.md, ## Removes, the third cell of the `.test_durations` row:
refreshed from the `test-durations` artifact of the branch's latest `tests`
run at each phase boundary, which drops the removed ids and prices the new
ones, so CI's durations case reads green between batches

plan.md, ## Operational impact, the second bullet:
- The suite's collected case ids change in every batch, so `.test_durations`
  is refreshed from the branch's latest `tests` run at each phase boundary
  (`CONTRIBUTING.md` *Running the checks* says how).
```

answer:

### 9. `CONTRIBUTING.md` *The test layout* gives three readings of which definitions need a class, and states the rewrite threshold twice

severity: should
location: `CONTRIBUTING.md:233-237`, `CONTRIBUTING.md:264-266`, `skills/verify/scripts/test_layout.py:9-11`
evidence: read `CONTRIBUTING.md:233-237`, `CONTRIBUTING.md:264-266`, `skills/verify/scripts/test_layout.py:9-11`, `skills/verify/scripts/test_layout.py:274-284`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:40`
verdict: open

Three texts name which definitions of a module need a class. `spec.md:40` says one class per function. `CONTRIBUTING.md:233-234` says one per "top-level function or class", and `test_layout.py:9-11` says one per top-level definition. The check reports only a public function without a class (`test_layout.py:274-284`). The smith who rebuilds a module in phases 5 to 7 reads `CONTRIBUTING.md`, so it would write a class for each private helper, which the frame does not ask for and the report never names. `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading* asks one reading.

The heading at `CONTRIBUTING.md:264-265` says "cost a minute" and the next sentence says "60 seconds". That is one value stated twice, and `questions.md` Q2 is the row that would change it.

```markdown
`TARGET = "<tracked path>"`. A file whose cases run a `bin/` command names
the script that command runs. The file holds one class per public top-level
function of the module, `Test_<name>`, with the name spelt as the code spells
it, and a class or a private function of the module may have a class too.
Each such class holds a case named `test_accepts_<what>` for good input and
one named `test_refuses_<what>` for bad input.

**A module's tests are written anew from the code when its old files cost
past the threshold.** The threshold is 60 seconds of the module's old files in
```

The docstring at `test_layout.py:9-11` takes the same wording: "holds one class per public top-level function of that module, `Test_<name>`".

answer:

## Confirmations

confirms: none
The 27 shipped scripts that gained only comments parse to the same AST as at 6046f062. Executed: an `ast.dump` comparison over every non-test `.py` the branch changed. 29 files compare equal. 27 changed only by added comment lines. `skills/implement/scripts/seal.py` also had one comprehension split across three lines, and `skills/verify/scripts/unverified_check.py` also lost the two-line comment naming the old module. Three files differ by design: `.github/scripts/plugin_directory_check.py` (its docstring), `.github/scripts/release_report.py` and `evals/scripts/noninferiority.py`. The tree holds 60 exemption comments in 29 files: 50 `splitlines`, 7 `heading_rule`, 1 `coordinate_grammar` and 2 `entry_point`, as `phases/phase-3.md` claims.

confirms: none
The sweep catches what the old censuses caught, apart from findings 2 and 4. Executed in the scratch clone: removing the exemption above `if __name__` in `hooks/dispatch.py`, moving the exemption in `skills/verify/scripts/coordinates.py` up one line, and writing the section sign into `evals/README.md` made the sweep fail at `hooks/dispatch.py:632`, `coordinates.py:36` and `:38`, and `evals/README.md:121`. A planted `.splitlines(` call in `.github/scripts/release_report.py` failed `test_census` at line 315. Read: the old encoding and entry-point corpora were `git ls-files` listings, as the new one is; the old `splitlines`, `coordinate_grammar` and `heading_rule` censuses walked the disk, so an untracked file is no longer judged by the sweep, which CI does not see.

confirms: none
Every old census case and every moved case is named in `phases/phase-3.md`, apart from the two format greps, which it calls "the two greps" and places as `coordinate_grammar` and `heading_rule`. Executed: a listing of every case name present at 6046f062 and gone from its file at 8aa42bf8, set against the text of the four phase records. Phase 2's cases are finding 7.

confirms: none
Each of the 28 helpers in `tests/conftest.py` behaves as every copy it replaced, apart from the differences `phases/phase-4.md` names. Executed: the 46 twin groups and 141 definitions at 6046f062 were listed with each body, and each module that held a copy was read for the name it binds at 8aa42bf8. Read: `projects` patches `sys.modules["worktree_consent"]`, the module the old copies reached as `wg.worktree_consent` or by name; the two `repo` fixtures became `_repo_template` fixtures that `tests/conftest.py#repo` copies; the autouse `_installer_writes` became `usefixtures("git_hooks_installed")` in `pytestmark`.

confirms: none
No survived mutation in `phases/phase-4.md` is a gap phase 4 opened. Each helper moved with the body its copies had, so the same mutation of any old copy survives the same cases. Executed for h4: `git` in `tests/conftest.py` forced to check every exit code, run over the seven modules that reach its `check` argument through `git`, `branch_of` or `git_dir`; 418 passed. Before the move `branch_of` and `git_dir` ran git without a check, so a check added there would have survived the same modules.

confirms: none
Phase 2's report fails nothing, as the owner directed. Read: `tests/conftest.py:856-862` writes lines and touches no outcome; `tests/test_conftest.py:98-100` asserts the inner run exits 0 with a slow case named. Executed: `git grep` over 8aa42bf8 outside the records finds no `SPECSEAL_CASE_CEILING_S` and no `CASE_CEILING_S`, and the timeout case stands in `tests/test_ci_gives_the_checks_what_they_need.py`.

confirms: none
The layout check reads what it claims for the refusals S1 to S4 and the reports. Executed in the scratch clone: `bin/test-layout --check` exits 0 and ends `145 files read, 0 refused, 141 declare no TARGET`; `--pairs` exits 0 with 0 pairs; `--check --all` exits 1. Read: `tests/test_test_layout.py` holds a case for each refusal and for each report, and `Test_main` runs the check over this repository's `tests/`.

confirms: none
The four new modules pass, and the rules hold. Executed in the scratch clone: `bin/test tests/test_test_layout.py tests/test_censuses.py tests/test_conftest.py tests/test_release_report.py -q -p no:xdist`, 212 passed; `bin/rules --check`, all 249 check lines in 62 rule files hold.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `--pairs` drops one argument or the whole call when an argument reads a local. `spec.md:73` says "leaving out an argument"; the code leaves out the call. Both read as a report, so no case can fail on either | `skills/verify/scripts/test_layout.py:312-340` | the orchestrator, for the frame |
| The survived mutations h2 and h6, re-run over every module that held their twins; only h4 was re-run | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-4.md:46-48` | the orchestrator |
| CI at 8aa42bf8 itself; this round read the run at 381d6c0f | `.github/workflows/test.yml` | the orchestrator |
| The overview census, which fails at each phase boundary and in CI run 39724802385 because `overview.md` is not in the target; the phase 5 smith writes it, and it is no finding | `tests/test_chain_hooks_hardening.py` | the orchestrator |
| The full suite, the lint and the typecheck, labelled unverified; the smith ran repository-wide ruff, so no lint result from the smith counts | the whole tree | the orchestrator, at the broad gate |
| `bin/test-layout.cmd` on Windows, not run | `bin/test-layout.cmd` | the Windows CI leg |
| Phases 5 to 7 | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/plan.md` | a later round |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_test_layout.py tests/test_censuses.py tests/test_conftest.py tests/test_release_report.py -q -p no:xdist` in a scratch clone at 8aa42bf8 | 212 passed, exit 0 |
| `bin/test tests/test_tmp_r1_probe.py -q -p no:xdist`, six cases P1 to P6, deleted after the run | 6 passed. P1: the sweep passed with `git_listing` returning nothing. P2: `x = 1  # exempt from splitlines: git output` judged as nothing. P3: an exemption a blank line above its call refused at lines 3 and 1. P4: a copy of `conftest.flattened` in a declared file refused only once `tests/conftest.py` was read. P5: `main` on a missing path returned 0 with 0 files read. P6: `slow_lines` named a failed call of 100 s |
| The census line of `tests/test_release_report.py` replaced and a `.splitlines(` call planted in `.github/scripts/release_report.py`, then `bin/test tests/test_release_report.py tests/test_censuses.py -q -p no:xdist`; restored by `git checkout` | 172 passed, exit 0. With the census line back, `bin/test tests/test_release_report.py -q -p no:xdist` failed at line 315, exit 1 |
| Three census facts broken in `hooks/dispatch.py`, `skills/verify/scripts/coordinates.py` and `evals/README.md`, then `bin/test tests/test_censuses.py -q -p no:xdist -k test_every_file_no_module_file_declares`; restored by `git checkout` | exit 1, naming `hooks/dispatch.py:632` entry_point, `coordinates.py:36` and `:38` coordinate_grammar, `evals/README.md:121` section_sign |
| `check=check` in `tests/conftest.py#git` replaced by `check=True`, then `bin/test` over the seven modules that reach the argument; restored by `git checkout` | 418 passed, exit 0: h4 survives every module that reaches it |
| `SLOW_CASE_S = 9000` in `tests/conftest.py`, then `bin/test tests/test_conftest.py tests/test_ci_gives_the_checks_what_they_need.py -q -p no:xdist`; restored by `git checkout` | 30 passed, exit 0 |
| A script outside the clone comparing `ast.dump` of each non-test `.py` the branch changed, at 6046f062 and 8aa42bf8, and counting exemption comments | 29 equal, 3 differ by design, 60 exemptions in 29 files |
| A script outside the clone listing the twin groups at 6046f062 through `test_layout._helpers`, and each module's binding at 8aa42bf8 | 46 groups, 141 definitions, each bound to a `tests/conftest.py` helper, a `functools.partial` of one, or a conftest fixture |
| A script outside the clone listing every case name gone from its file between 6046f062 and 8aa42bf8, set against the phase records | 44 names gone; 7 of `tests/test_a_slow_case_names_itself.py` and the two format greps unnamed |
| A script outside the clone running `twins` over the test files with `tests/conftest.py` and `tests/censuses.py` | no twin with either file today |
| `bin/test-layout --check`, `bin/test-layout --pairs` and `bin/test-layout --check --all` in the scratch clone | exit 0 with 145 read, 0 refused, 141 undeclared; exit 0 with 0 pairs; exit 1 |
| `bin/rules --check` in the scratch clone | exit 0, 249 check lines hold |
| `gh run view 39724802385 --json jobs` and `gh run view 39724802385 --log-failed` | failure at 381d6c0f; five pytest legs fail on the overview census and on `test_the_durations_file_prices_the_suite`, 507 of 7538 cases unpriced |
