# 1791876666-the-test-suite-is-held-to-a-budget — review round 5

| Field | Value |
|---|---|
| Target SHA | f810ee29c5e36ac7aa1d173058df3227a25e087e |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #939 |
| Broad gate | not yet |
| Fixes checked by | round-6 |
| Fix range | `1063ba454e1041d5d6a5bb04ffb349e6e97f71d8..858988e0b309dff665c758f23c833e0f7a0c3ff1`, 2 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | first — 🟡 1 at .github/scripts/case_check.py#TRACER_SOURCE, a unit round-4's fixes changed |
| Needs a fix | yes — 🟡 1 (pytest's own skip, importorskip or xfail inside a unittest expected failure, method or class, is named `kills nothing` instead of `not proved`) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Verifying round 5 of #929: round 4's fix at 3fb8d310 (the unittest expected-failure mark read off the TestCase instance and the method, only for a TestCase item), the records left saying the function, and the 299 of 300 s case-check run. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | Under a `TestCase` expected-failure mark, method or class, a body that pytest's own `skip`, `importorskip` or `xfail` stopped is read as having run, and is named `kills nothing` instead of `not proved` | `.github/scripts/case_check.py:193` | **fixed** `c3931bf8` | fixed at c3931bf8; executed: two fixtures at `f810ee29` exit 1 with `kills nothing … of the 0 mutants drawn`, and pytest reports both `XFAIL`; with the wrapper fix both give `not proved`, and the module's 27 cases pass; read: `unittest/case.py:54-72`, `:637-639`, `_pytest/unittest.py:347-355`, `spec.md:95` |
| ⬜ 2 | The heading and cost lines add the report half's seconds to the proofs' seconds, so the bound always reads as nearly spent and the margin to `restructure` cannot be read off | `.github/scripts/case_check.py:993` | open | read: `:961-994`; executed: local run 299 s with 654 not run; read: CI `cases` logs of runs 38670358090 and 38658107547 |
| 🟢 | round 4's finding is closed — an expected failure marked on its `TestCase` class, or a base, is read as a run, and a plain function carrying the mark is excused nothing | `.github/scripts/case_check.py:192` | confirmed | executed: both new rows red against `d99c6cee`'s checker and green at the tip; probes on base-class, async, plain-class and unexpected-success fixtures; read: `_pytest/python.py:1673-1682`, `_pytest/unittest.py:259`, `:384` |
| 🟢 | `plan.md` and `phases/phase-3.md` saying "the function" are phase 3's history, not live claims | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/plan.md:28` | confirmed | read: `plan.md:28`, `:53`, `:71`, `:88`, `phases/phase-3.md:18`, `spec.md:95` |
| 🟢 | CI is unlikely to hit `restructure` at this tip: 299 s is the report filling the bound | `.github/scripts/case_check.py:871` | confirmed | executed: local `case_check.py` as the job runs it, 22 proved, exit 0; read: CI file 3 traced in 12 s and proved in 35 s, against 30 s and 86 s locally |
| ❓ | what the `cases` job says on a CI runner at `f810ee29` | PR #939 | ❓ out of verified scope | the branch is not pushed; the orchestrating session, which pushes it, reads PR #939's next run |

## Paste-ready fixes

```python
def _watch_expected(item):
    # The stdlib takes whatever a marked body raises for its expected
    # failure, pytest's own skip and xfail stops included, and pytest's
    # unittest plugin then reports an xfail; the exception it is handed says
    # which it was.
    add = getattr(item, "addExpectedFailure", None)
    case = getattr(item, "instance", None)
    if add is None or not isinstance(case, unittest.TestCase):
        return

    def watched(testcase, rawexcinfo, *rest, **named):
        raised = rawexcinfo[1] if isinstance(rawexcinfo, tuple) else None
        if isinstance(raised, (pytest.skip.Exception, pytest.xfail.Exception)):
            _skipped.add(item.nodeid)
        return add(testcase, rawexcinfo, *rest, **named)

    item.addExpectedFailure = watched


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    _now[0] = item.nodeid
    _watch_expected(item)
    began = time.monotonic()
```
```markdown
The one translation is pytest's: its unittest plugin raises the xfail stop itself on behalf of an `@unittest.expectedFailure` whose body raised, and `__unittest_expecting_failure__` on the method or on the `TestCase` instance, and so on its class, says so, as the stdlib reads both, so that case ran its body — unless what the body raised was pytest's own skip or xfail stop, which the stdlib takes for the expected failure too, and which the exception pytest's plugin is handed still names. The same mark on a function that is not a `TestCase` method excuses nothing, because pytest's unittest plugin never ran it.
```
```python
    "\n\n\n@unittest.expectedFailure\n"
    "class TestUnderAClassMark(unittest.TestCase):\n"
    "    def test_by_skip_under_a_unittest_mark(self):\n"
    '        pytest.skip("another platform")\n'
    "        assert m.double(2) == 4\n"
```
```python
    "TestUnderAClassMark::test_by_skip_under_a_unittest_mark",
```
```python
    # after the loop over `pending`, before "The report's half"
    proofs = time.monotonic() - started
    ...
        f"named, in {time.monotonic() - started:.0f} s of a {bound:g}-minute "
        f"bound, the proofs in {proofs:.0f} s",
```

## Executed probes

| What was run | Result |
|---|---|
| `python .github/scripts/case_check.py --baseline 642441fc --runner "python -m pytest -n auto" --bound 5` in the first clone at `f810ee29`, the `cases` job's line | exit 0, 22 proved, 0 named, in 299 s; cost lines: file 1 traced 3 s, 71 mutants in 162 s; file 2 traced 1 s, 27 in 12 s; file 3 traced 30 s, 12 in 86 s; 15 survived, 654 not run; load average 5 at start, 13 at end |
| `python -m pytest tests/test_a_new_case_protects_what_its_file_did_not.py -q -n auto` at `f810ee29` | exit 0, 27 passed |
| the same module, `-k "(marked and class) or (every and way)"`, with `case_check.py` from `d99c6cee` | 2 failed: `CLASS_EXPECTED` named `not proved`; `test_by_xfail_under_a_unittest_mark` missing from the `not proved` lines |
| probe `tests/test_tmp_round5_probe.py` (NAME NOT IN TREE: deleted after the run), `case_check.main` and a plain pytest run on seven fixtures at `f810ee29` | base-class mark: `kills nothing`, pytest XFAIL; class mark + `pytest.skip()`: `kills nothing … 0 mutants`, pytest XFAIL; method mark + `importorskip`: `kills nothing … 0 mutants`, pytest XFAIL; class mark + `skipTest`: `not proved`, pytest SKIPPED; plain class + mark + `pytest.xfail()`: `not proved`; class mark, assertion a mutant makes pass: `proved`; async class mark: `kills nothing` |
| the same probe and the module with 🟡 1's wrapper applied in the second clone, then the clone deleted | module exit 0, 27 passed; class mark + skip and method mark + `importorskip`: `not proved`; the other five unchanged; `uvx ruff check .github/scripts/case_check.py` exit 0 |
| CI logs of the `cases` jobs 116211802590 (run 38670358090, `2aa76b37`) and 116172593664 (run 38658107547, `692cef31`), read through `gh api` | 21 and 19 proved, 0 named, 299 s each; file 3 traced 12 s, 12 mutants in 35 s and 36 s |
| `case_check.py` as the `cases` job runs it, on CI at `f810ee29` | not yet: the branch is not pushed; PR #939's next run answers it |
| Broad gate (full suite, repository-wide lint, typecheck) | not yet: not run by this round, and owed to the sealer once the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `bin/test:35`, `bin/test.cmd:14` | round 1's 🔴 1 — fixed |
| round-1 | `tests/test_a_script_says_which_interpreter_it_needs.py:185`, `skills/verify/scripts/unverified_check.py:641` | round 1's 🟡 2 — fixed |
| round-1 | `.github/scripts/case_check.py:861` | round 1's 🟡 3 — fixed |
| round-1 | `.github/scripts/case_check.py:875` | round 1's 🟡 4 — fixed |
| round-1 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:6` | round 1's ⬜ 5 — answered |
| round-1 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/overview.md:7` | round 1's ⬜ 6 — answered |
| round-1 | `CONTRIBUTING.md:146` | round 1's ⬜ 7 — answered |
| round-1 | CI run 38658107547 | round 1's ❓ — out of verified scope |
| round-2 | `.github/scripts/case_check.py:848` | round 2's 🟡 1 — fixed |
| round-2 | `CONTRIBUTING.md:128`, `ruff.toml:41` | round 2's 🟡 2 — fixed |
| round-2 | `tests/test_a_script_says_which_interpreter_it_needs.py:409` | round 2's ⬜ 3 — answered |
| round-2 | `tests/test_a_script_says_which_interpreter_it_needs.py:395` | round 2's ⬜ 4 — answered |
| round-2 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/questions.md:25` | round 2's ⬜ 5 — answered |
| round-2 | `bin/test:36`, `bin/test.cmd:17` | round 2's 🟢 — confirmed |
| round-2 | `tests/test_a_script_says_which_interpreter_it_needs.py:401`, `ruff.toml:42` | round 2's 🟢 — confirmed |
| round-2 | `.github/scripts/case_check.py:599` | round 2's 🟢 — confirmed |
| round-2 | CI run 38664361183 | round 2's 🟢 — answered |
| round-3 | `.github/scripts/case_check.py:188` | round 3's 🟡 1 — deferred |
| round-3 | `.github/scripts/case_check.py:180` | round 3's 🟡 2 — deferred |
| round-3 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/rounds/round-2.md:5` | round 3's ⬜ 3 — answered |
| round-3 | `.github/scripts/case_check.py:862` | round 3's 🟢 — confirmed |
| round-3 | `CONTRIBUTING.md:124`, `ruff.toml:35` | round 3's 🟢 — confirmed |
| round-3 | `seal/budgets.md:40`, `seal/budgets.md:60` | round 3's 🟢 — confirmed |
| round-3 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/spec.md:99` | round 3's 🟢 — confirmed |
| round-3 | `.github/workflows/test.yml`, `CONTRIBUTING.md`, `tests/test_every_reader_ends_a_line_where_gfm_does.py` | round 3's 🟢 — confirmed |
| round-3 | CI run 38668484642 | round 3's 🟢 — confirmed |
| round-4 | `.github/scripts/case_check.py:190` | round 4's 🟡 1 — fixed |
| round-4 | `.github/workflows/test.yml:223` | round 4's ⬜ 2 — open |
| round-4 | `.github/scripts/case_check.py:882` | round 4's 🟢 — confirmed |
| round-4 | `.github/scripts/case_check.py:193` | round 4's 🟢 — confirmed |
| round-4 | `.github/scripts/case_check.py:182` | round 4's 🟢 — confirmed |
| round-4 | `tests/test_a_new_case_protects_what_its_file_did_not.py:192` | round 4's 🟢 — confirmed |
| round-4 | `.github/scripts/case_check.py:76` | round 4's 🟢 — confirmed |
| round-4 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:464` | round 4's 🟢 — confirmed |
| round-4 | PR #939 | round 4's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
