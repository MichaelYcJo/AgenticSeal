# 1791876666-the-test-suite-is-held-to-a-budget — review round 3

| Field | Value |
|---|---|
| Target SHA | e90c90d31e82d6eac45ea04a91ab5cae0e421018 |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #939 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are not yet written |
| Fix range | none — the fixes are not yet written |
| Contract changes | none — the fixes are not yet written |
| New units | none — the fixes are not yet written |
| Fix of a fix | second — 🟡 1 at .github/scripts/case_check.py#TRACER_SOURCE, a unit round-2's fixes changed; 🟡 2 at .github/scripts/case_check.py#TRACER_SOURCE, a unit round-2's fixes changed; the fix passes stop here and the work item goes back to its framer |
| Needs a fix | yes — 🟡 1 (a sibling that asserts then skips is no longer run under a mutant, so a case it covers is reported proved), 🟡 2 (an imperative `pytest.xfail()` is named for killing nothing) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Verifying round 3 of #929, the run's last, on the tree rebased onto #931: round 2's fixes (every way a case skips its body named NEVER_RAN; the census claims reworded), the seal/budgets.md conflict resolution, the two lowered slow-file rows under a report family, and nothing #931 brought undone. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | The tracer drops a skipped call's lines from `hits`, and `selected` reads the same `hits`, so a sibling that asserts and then skips its tail is never run under a mutant; a new case that sibling covers is reported `proved — the only killer in its file` | `.github/scripts/case_check.py:188` | open | executed: fixture with `test_partial` in the base and `test_double` added, exit 0 and `proved` at `e90c90d3`, exit 1 and `kills nothing` with the file as it stood before round 2's fix; a fix of a fix in the tracer round 2's fixes changed |
| 🟡 2 | An imperative `pytest.xfail()` in the body carries `wasxfail`, so the hook keeps it as a run and it is named `kills nothing its file does not`; the docstring, `test.yml:221` and `spec.md:91` say such a case is named for never having run | `.github/scripts/case_check.py:180` | open | executed: fixture with `test_by_xfail`, exit 1 with the wrong reason at `e90c90d3`; the fix below names it `not proved` and keeps `@unittest.expectedFailure` a run |
| ⬜ 3 | The `hygiene` workflow's `release` job is red: round 2's `Target SHA` `fffee6b2` is on no ref after the rebase onto #931 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/rounds/round-2.md:5` | open | read: run 38668484688 at `e90c90d3`; `chain_check.py` judges the last record, so round 3's record should clear it, not executed |
| 🟢 | round 2's finding 1 is closed for every spelling it listed — a mark, a body skip, `importorskip`, a fixture skip, `xfail(run=False)`, `skipTest`, and a file skipped at import | `.github/scripts/case_check.py:862` | confirmed | executed: the module's 23 cases pass at `e90c90d3`; a probe added a `@unittest.skip` class and a module `pytestmark` skipif, both named `not proved`; the two spellings that still slip are 🟡 1 and 🟡 2 |
| 🟢 | round 2's finding 2 is closed — the census's claims say what it checks | `CONTRIBUTING.md:124`, `ruff.toml:35` | confirmed | read at `e90c90d3` |
| 🟢 | the `seal/budgets.md` conflict is resolved as both sides meant: this branch's three lowered ceilings, #931's `report` kind | `seal/budgets.md:40`, `seal/budgets.md:60` | confirmed | executed: `budget_check.py --baseline origin/release/v0.22.0` exit 0; readings recomputed from `.test_durations` at both revisions |
| 🟢 | the two lowered `slow-file` file rows still print an over-line when the file regrows, and the branch claims no more for them | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/spec.md:99` | confirmed | read: `budget_check.py` docstring on `report` families and the ratchet; no touched doc calls them a gate |
| 🟢 | nothing #931 brought in is undone | `.github/workflows/test.yml`, `CONTRIBUTING.md`, `tests/test_every_reader_ends_a_line_where_gfm_does.py` | confirmed | executed: every line #931's squash added is present at HEAD; #931's three test modules pass |
| 🟢 | the `cases` job passes at the tip | CI run 38668484642 | confirmed | read: CI's execution at `e90c90d3`, 21 proved, 0 named, 298 s |

## Paste-ready fixes

```python
def pytest_sessionfinish(session):
    with open(os.path.join(_out, f"{os.getpid()}.json"), "w", encoding="utf-8") as f:
        hits = {k: sorted(v) for k, v in _hits.items()}
        json.dump({"hits": hits, "seconds": _seconds, "short": sorted(_skipped)}, f)
```
```python
        except subprocess.TimeoutExpired:
            return None, time.monotonic() - started, "timed out", {}, {}, set()
        seconds = time.monotonic() - started
        hits, calls, short = {}, {}, set()
        for name in os.listdir(out):
            try:
                with open(os.path.join(out, name), encoding="utf-8") as f:
                    found = json.load(f)
                for nodeid, pairs in found["hits"].items():
                    hits.setdefault(nodeid, set()).update(map(tuple, pairs))
                calls.update(found["seconds"])
                short.update(found["short"])
            except (OSError, ValueError, KeyError, AttributeError, TypeError):
                continue
    lines = (done.stdout + done.stderr).strip().splitlines()
    return done.returncode, seconds, lines[-1] if lines else "", hits, calls, short
```
```python
        code, each, verdict, hits, calls, short = traced_run(root, file, runner, left)
```
```python
        through = {i: pairs for i, pairs in hits.items() if i not in short}
        never_ran = [n for n in names if not own_ids(through, file, functions, n)]
```
```python
# A call that stopped short of its body, as `pytest.skip()`, `importorskip`,
# `skipTest` or `pytest.xfail()` there, started, so its first lines are
# traced. Its lines are kept, since a mutant of one can still fail it before
# it stops, and its id is written apart, so the check names it as one that
# never ran. An expected failure whose body ran is a run.
```
```python
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    report = (yield).get_result()
    if report.when == "call" and report.skipped:
        stopped = call.excinfo is not None and call.excinfo.errisinstance(
            pytest.xfail.Exception
        )
        expected = getattr(
            getattr(item, "obj", None), "__unittest_expecting_failure__", False
        )
        if not hasattr(report, "wasxfail") or (stopped and not expected):
            _skipped.add(report.nodeid)
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_a_new_case_protects_what_its_file_did_not.py tests/test_a_script_says_which_interpreter_it_needs.py tests/test_a_shrunken_corpus_declines_to_judge.py -q` at `e90c90d3` | exit 0, 46 passed |
| `python3 .github/scripts/budget_check.py --baseline origin/release/v0.22.0` at `e90c90d3` | exit 0; `suite-seconds` 6,031 of 7,841; the two file rows 915 of 1,190 and 389 of 506, `report`, holds; `rounds-bytes` over, `report` |
| `.test_durations` summed per file at `642441fc` and `e90c90d3`, divided by 1.132 | base 6,854, 1,178, 946; HEAD 6,031, 389, 915 |
| every `+` line of `git diff 642441fc^ 642441fc`, per file, looked up at HEAD | none missing |
| `bin/test tests/test_ci_gives_the_checks_what_they_need.py tests/test_a_budget_ratchets.py tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q` | exit 0, 212 passed, 2 skipped |
| probe `tests/test_tmp_r3_skip.py` (NAME NOT IN TREE: deleted after the run), `case_check.main` on six fixtures at `e90c90d3` | partial sibling: exit 0, `test_double: proved`; imperative xfail: exit 1, `kills nothing`; `@unittest.skip` class, module `pytestmark` skipif, a new case that asserts then skips: each `not proved`; `@unittest.expectedFailure`: `kills nothing` |
| the same probe with `case_check.py` from `ec152145^` | partial sibling: exit 1, `test_double: kills nothing`; imperative xfail: `kills nothing` |
| the same probe with the paste-ready fix applied in the clone, then reverted | partial sibling: `kills nothing`; imperative xfail: `not proved`; `@unittest.expectedFailure` still a run; the other rows unchanged; the module 23 passed; `tests/test_every_reader_ends_a_line_where_gfm_does.py` 149 passed |
| AST scan of `tests/test_*.py` for a skip or xfail call after another statement in a test body | 27 cases |
| `gh pr checks 939`, the `cases` job log of run 38668484642, the failed log of run 38668484688 (CI's execution, read here) | `cases` pass, 21 proved, 0 named; `hygiene` `release` fails on round 2's `Target SHA`; ubuntu and Windows `pytest` still pending when read |
| Broad gate (full suite, repository-wide lint, typecheck) | not yet: not run by this round, and owed to the sealer once the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `bin/test:35`, `bin/test.cmd:14` | round 1's 🔴 1 — fixed |
| round-1 | `tests/test_a_script_says_which_interpreter_it_needs.py:185`, `skills/verify/scripts/unverified_check.py:641` | round 1's 🟡 2 — fixed |
| round-1 | `.github/scripts/case_check.py:861` | round 1's 🟡 3 — fixed |
| round-1 | `.github/scripts/case_check.py:875` | round 1's 🟡 4 — fixed |
| round-1 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:6` | round 1's ⬜ 5 — open |
| round-1 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/overview.md:7` | round 1's ⬜ 6 — open |
| round-1 | `CONTRIBUTING.md:146` | round 1's ⬜ 7 — open |
| round-1 | CI run 38658107547 | round 1's ❓ — out of verified scope |
| round-2 | `.github/scripts/case_check.py:848` | round 2's 🟡 1 — fixed |
| round-2 | `CONTRIBUTING.md:128`, `ruff.toml:41` | round 2's 🟡 2 — fixed |
| round-2 | `tests/test_a_script_says_which_interpreter_it_needs.py:409` | round 2's ⬜ 3 — open |
| round-2 | `tests/test_a_script_says_which_interpreter_it_needs.py:395` | round 2's ⬜ 4 — open |
| round-2 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/questions.md:25` | round 2's ⬜ 5 — open |
| round-2 | `bin/test:36`, `bin/test.cmd:17` | round 2's 🟢 — confirmed |
| round-2 | `tests/test_a_script_says_which_interpreter_it_needs.py:401`, `ruff.toml:42` | round 2's 🟢 — confirmed |
| round-2 | `.github/scripts/case_check.py:599` | round 2's 🟢 — confirmed |
| round-2 | CI run 38664361183 | round 2's 🟢 — answered |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
