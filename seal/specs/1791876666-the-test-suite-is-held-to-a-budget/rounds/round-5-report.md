# 1791876666 — review round 5, report

Target: `f810ee29` on `chore/929-the-test-suite-only-grows` (PR #939, local
tip, not pushed), against `origin/release/v0.22.0` at `642441fc`. This is a
verifying round. Its target is round 4's fix range, `d99c6cee..8983d413`
(`3fb8d310`, `8983d413`), with `f810ee29` closing the record. Reviewed in two
`git clone --no-local` copies of the worktree at `f810ee29`, both under this
session's scratchpad and both deleted when the round was done. Paths are
relative to the repository root. Probes ran on macOS arm64, pytest 9.1.1,
CPython 3.13.9, the worktree's venv.

## How the findings relate

Round 4's fix holds. The tracer now reads the stdlib's mark where the stdlib
reads it, on the `TestCase` instance (so its class and bases) and on the
method. A plain function or a plain pytest class carrying the mark is excused
nothing. The two new rows fail against `d99c6cee`'s checker and pass at the
tip.

- 🟡 1 is the same kind of defect one step further along the excuse the fix
  widened. Under that mark the stdlib takes *any* exception the body raises
  as the expected failure, pytest's own `pytest.skip()`, `importorskip` and
  `pytest.xfail()` included. So a case whose body pytest stopped is read as
  having run, and it is named `kills nothing` instead of `not proved`. With
  the method-level mark this predates the fix (phase 3). The fix makes the
  class-level mark reach it too.
- ⬜ 2 answers the 299-of-300-seconds question. The figure is the report half
  filling the bound by design, not the proofs nearly missing it. The job's
  output gives no way to tell the two apart.

## 🟡 1 — pytest's own stop inside a unittest expected failure is read as a run

`.github/scripts/case_check.py:192-198` (`executed`).

The stdlib decides an expected failure once, before `setUp`, from the
instance and the method (`unittest/case.py:637-639`). It then runs the body
under `_Outcome.testPartExecutor` (`unittest/case.py:54-72`). That executor
catches `KeyboardInterrupt` and `SkipTest` apart, and then catches everything
else with a bare `except:`. When the test is expecting a failure, whatever
was caught becomes `outcome.expectedFailure`. pytest's `Skipped` and
`XFailed` are `BaseException` subclasses (`_pytest/outcomes.py:13`, `:39`,
`:76`), not `SkipTest`, so they land there. `TestCaseFunction.addExpectedFailure`
(`_pytest/unittest.py:347-355`) is then handed that exception, discards it,
and raises `xfail("")`. The tracer sees `stop` true, `expected` true, and
counts the id as having run its body.

**Failure scenario, executed.** The base holds `test_name`. HEAD adds either
of these:

```python
@unittest.expectedFailure
class TestClassSkip(unittest.TestCase):
    def test_class_skip(self):
        pytest.skip("another platform")
        assert m.double(2) == 4


class TestMethodImp(unittest.TestCase):
    @unittest.expectedFailure
    def test_method_importorskip(self):
        pytest.importorskip("a_module_no_runner_has")
        assert m.double(2) == 4
```

`case_check.main` at `f810ee29` exits 1 for each, naming it `kills nothing
its file does not: of the 0 mutants drawn for it, …`. Run directly, pytest
reports each as `XFAIL`. `spec.md:95` and the tracer comment at
`case_check.py:175` both put `pytest.skip()`, `pytest.importorskip` and
`pytest.xfail()` in the body on the stopped-short side, *whatever spelling*.
So the rule says `not proved: none of its ids ran its call to the end on this
runner`. The control rows behave: `self.skipTest()` under a class mark gives
`not proved`, because the stdlib routes `SkipTest` to `addSkip`. A plain
pytest class carrying the mark with `pytest.xfail()` gives `not proved`.

**Why it matters.** The job is red either way, so nothing ships green. The
message points the wrong way, though. The author of a case that does not run
on ubuntu is told it kills nothing, and adding assertions does not fix that.
This is round 1's misreport and round 3's 🟡 2 for one more spelling. Round 4
graded the mirror image of it (a real run named `not proved`) 🟡, and this
round grades it the same. The combination is narrow: a skip or an
`importorskip` inside a body that is also marked as an expected failure. It is
still a supported spelling that the rule names, and `importorskip` inside a
method is an ordinary way to write a platform guard.

**The class, enumerated (§12).** The excuse reads the mark and never what the
stdlib swallowed. Every pytest stop is covered by one type check on the
exception `addExpectedFailure` receives, whatever its spelling: `skip`,
`importorskip` (it raises `Skipped`), `xfail`, under a method mark or a class
mark, through the base class. `pytest.fail()` is a real failure, and it stays
an excused raise: `Failed` is not `XFailed`. `SkipTest` never reaches this
path.

**The fix, executed in a clone and then removed.** The tracer wraps the
item's `addExpectedFailure` for a `TestCase` item before the call. Where the
exception it is handed is pytest's skip or xfail stop, the wrapper adds the id
to the stopped set. With it, both fixtures above give `not proved`. The base-
class, async and unexpected-success fixtures keep their verdicts (`kills
nothing`, `kills nothing`, `proved`). The module's 27 cases pass, and ruff is
clean. The wrapper is set on the item instance and nowhere else, so nothing in
pytest is patched globally. It rests on the same unstable name the plan
already lists (`plan.md:30`), with `addExpectedFailure` added beside it: a
pytest that stops calling it leaves the wrapper unused, and behaviour falls
back to today's.

## ⬜ 2 — "299 of 300 s" is the report filling the bound, and the output cannot say so

`.github/scripts/case_check.py:961-994` (`read`), with the timings `executed`
locally and `read` from CI logs.

Once every file's proofs are done, `check` runs mutants of the changed shipped
lines while at least one traced run of the file is left in the bound
(`:971-972`, `left < each`). Here there are 654 of them that it never reaches.
Any run with work left over therefore ends within one file-run of 300 s,
whether the proofs took 60 s or 290 s. The cost lines (`:988`) and the
heading (`:993`) both add the report's seconds to the proof's seconds. So
"299 s" carries no information about how close a proof came to `restructure`.

What does decide `restructure` is each file's share (`:871`) against its
traced run (`:875`) and its proof (`:905`, `:952`). The measurements:

| Run | proved | file 3 (`test_the_commit_gate_decides_at_the_commit.py`) | file 1, everything it spent |
|---|---|---|---|
| this round, local, load 5–14, `f810ee29` | 22, 0 named | traced 30 s, 12 mutants in 86 s | 71 mutants in 162 s |
| CI run 38670358090 (`cases` job), `2aa76b37` | 21, 0 named | traced 12 s, 12 mutants in 35 s | 125 mutants in 228 s |
| CI run 38658107547 (`cases` job), `692cef31` | 19, 0 named | traced 12 s, 12 mutants in 36 s | 161 mutants in 234 s |

CI's runner is faster than this machine on this job, not slower: the slowest
file's traced run is 12 s there against 30 s here. CI also ran more report
mutants inside the same 299 s. That is the bound being filled. The last file
to prove got its share after the first two had proved, and spent 47 s of it
on CI. **Judgement: CI is unlikely to hit `restructure` at `f810ee29`.** The
fix range adds one end-to-end row to file 1, which ran in about a second
locally. It adds no new pending file.

**What the item should do.** Nothing about the bound. If the owner wants the
risk to be readable rather than argued about, the heading can say when the
proofs ended. The snippet below is a suggestion and is not counted in `Needs
a fix`. The open number is `overview.md:44`'s row, *what the `cases` job says
on a CI runner at phase 3's tip*. It stays open until the branch is pushed.

## The fix itself — confirmed

- `item.instance` is pytest's `Function.instance` (`_pytest/python.py:1673-1682`).
  For a `TestCaseFunction` it is the `TestCase` that `runtest` runs
  (`_pytest/unittest.py:384`). Teardown deletes it (`:259`) only after the
  call report is made, and the wrapper returns before reading it for any
  report other than a skipped call. `executed`: base-class inheritance and an
  `IsolatedAsyncioTestCase` under a class mark both read as runs.
- The other direction holds. A module-level function and a plain pytest class
  carrying the mark are excused nothing, and pytest gives neither of them
  unittest semantics (`executed`: the `test_by_xfail_under_a_unittest_mark`
  row and a probe on a plain class).
- `executed`: both new rows fail against `d99c6cee`'s `case_check.py` and
  pass at the tip. `CLASS_EXPECTED` is named `not proved`, and
  `test_by_xfail_under_a_unittest_mark` is read as a run. Round 4's
  implementer claimed this, and it holds.
- `executed`: a class-marked case whose assertion a mutant makes pass, so the
  test succeeds unexpectedly, is `proved`. So the class-level case really is
  run under mutants.
- `spec.md:95`'s rewrite states the two places the mark is read from and the
  plain-function case. It does not yet state 🟡 1's exception.
  `test.yml:221-225` now reflows cleanly. Round 4's ⬜ 2 is carried to the
  run's end and not re-reported here.

## The records that say "the function"

`plan.md:53`, `:71`, `:88` and `phases/phase-3.md:18` are phase 3's record:
an alternatives row, the phase's assignment, its test row, and the phase's
restatement of its own ask. They describe what phase 3 was built to and do
not claim to describe the tip. `plan.md:28` is technical context dated and
labelled `read`, and its sentence (`expectedFailure` sets the attribute on the
function it decorates) is true of the function-level decorator. The rule the
code is held to is `spec.md:95`, and round 4's fix rewrote that. These are
history, not live claims. Nothing in the fix range names anything 0.22.0
removed (`read`, over `git diff d99c6cee f810ee29`).

## Regression tests to plant

`tests/test_a_new_case_protects_what_its_file_did_not.py`: one more spelling
in `ELSEWHERE`, and its name in `NEVER_STARTED` (fenced below). Against
`f810ee29` it gives `kills nothing`, so the row fails. That is this round's
probe `class_skip`.

## Facts for the record

- pytest 9.1.1 `TestCaseFunction.addExpectedFailure` discards the exception it
  is handed and raises `xfail("")`. The stdlib hands it whatever the marked
  body raised, apart from `SkipTest` and `KeyboardInterrupt`, pytest's
  outcome exceptions included (`unittest/case.py:54-72`, CPython 3.13.9).
- On CI the `cases` job's slowest pending file is traced in 12 s, not the 30 s
  measured here (CI runs 38670358090 and 38658107547).

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | Under a `TestCase` expected-failure mark, method or class, a body that pytest's own `skip`, `importorskip` or `xfail` stopped is read as having run, and is named `kills nothing` instead of `not proved` | `.github/scripts/case_check.py:193` | open | executed: two fixtures at `f810ee29` exit 1 with `kills nothing … of the 0 mutants drawn`, and pytest reports both `XFAIL`; with the wrapper fix both give `not proved`, and the module's 27 cases pass; read: `unittest/case.py:54-72`, `:637-639`, `_pytest/unittest.py:347-355`, `spec.md:95` |
| ⬜ 2 | The heading and cost lines add the report half's seconds to the proofs' seconds, so the bound always reads as nearly spent and the margin to `restructure` cannot be read off | `.github/scripts/case_check.py:993` | open | read: `:961-994`; executed: local run 299 s with 654 not run; read: CI `cases` logs of runs 38670358090 and 38658107547 |
| 🟢 | round 4's finding is closed — an expected failure marked on its `TestCase` class, or a base, is read as a run, and a plain function carrying the mark is excused nothing | `.github/scripts/case_check.py:192` | confirmed | executed: both new rows red against `d99c6cee`'s checker and green at the tip; probes on base-class, async, plain-class and unexpected-success fixtures; read: `_pytest/python.py:1673-1682`, `_pytest/unittest.py:259`, `:384` |
| 🟢 | `plan.md` and `phases/phase-3.md` saying "the function" are phase 3's history, not live claims | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/plan.md:28` | confirmed | read: `plan.md:28`, `:53`, `:71`, `:88`, `phases/phase-3.md:18`, `spec.md:95` |
| 🟢 | CI is unlikely to hit `restructure` at this tip: 299 s is the report filling the bound | `.github/scripts/case_check.py:871` | confirmed | executed: local `case_check.py` as the job runs it, 22 proved, exit 0; read: CI file 3 traced in 12 s and proved in 35 s, against 30 s and 86 s locally |
| ❓ | what the `cases` job says on a CI runner at `f810ee29` | PR #939 | ❓ out of verified scope | the branch is not pushed; the orchestrating session, which pushes it, reads PR #939's next run |

## Paste-ready fixes

### 🟡 1 — in `TRACER_SOURCE`, before `pytest_runtest_call`, and called from it

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

### 🟡 1 — `spec.md:95`, the sentence after "The one translation is pytest's"

```markdown
The one translation is pytest's: its unittest plugin raises the xfail stop itself on behalf of an `@unittest.expectedFailure` whose body raised, and `__unittest_expecting_failure__` on the method or on the `TestCase` instance, and so on its class, says so, as the stdlib reads both, so that case ran its body — unless what the body raised was pytest's own skip or xfail stop, which the stdlib takes for the expected failure too, and which the exception pytest's plugin is handed still names. The same mark on a function that is not a `TestCase` method excuses nothing, because pytest's unittest plugin never ran it.
```

### 🟡 1 — the row to plant, appended to `ELSEWHERE`, its name to `NEVER_STARTED`

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

### ⬜ 2 — a suggestion, not counted: the heading says when the proofs ended

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

Needs a fix: yes — 🟡 1 (pytest's own skip, importorskip or xfail inside a unittest expected failure, method or class, is named `kills nothing` instead of `not proved`)
Loses a record or crashes: no

## Proof block

Opened this round: `.github/scripts/case_check.py` (`:60-90`, `:110-260`,
`:828-1003`, at `f810ee29`; the tracer at `d99c6cee` through the diff),
`.github/workflows/test.yml:205-245`,
`tests/test_a_new_case_protects_what_its_file_did_not.py` (`:19-32`,
`:282-420`, the row ids, `test_each_real_path_end_to_end`),
`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/` `spec.md:95`
(through the diff), `plan.md:28`, `:30`, `:53`, `:55`, `:61`, `:71`, `:88`,
`phases/phase-3.md:1-40`, `:110-175`, `overview.md:28-44`,
`rounds/round-4.md`, `rounds/round-4-report.md`; pytest 9.1.1
`_pytest/unittest.py:230-262`, `:290-360`, `:378-420`, `:505-530`,
`_pytest/python.py:1665-1690`, `_pytest/outcomes.py` class heads; CPython
3.13.9 `unittest/case.py:40-80`, `:625-690`; `bin/test`; the two CI job logs
named above.
