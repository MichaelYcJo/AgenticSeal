# 1791876666 — review round 6, report

Target: `f3eea4fe` on `chore/929-the-test-suite-only-grows` (PR #939, local
tip, not pushed), against `origin/release/v0.22.0` at `642441fc`. This is the
run's last round, a verifying one. Its target is round 5's fix range,
`1063ba45..858988e0` (`c3931bf8`, `858988e0`), with `f3eea4fe` closing round
5's record. Reviewed in a `git clone --no-local` of the worktree at
`f3eea4fe`, under this session's scratchpad, deleted when the round was done.
Paths are relative to the repository root. Probes ran on macOS arm64 with
pytest 9.1.1, on CPython 3.13.9 (the worktree's venv) and on CPython 3.12.12
(a `uv` venv built in the clone, the version the `cases` job sets up).

## How the findings relate

Both of round 5's fixes hold. The `addExpectedFailure` wrapper reads the
exception the stdlib took for the expected failure, and the new heading
figure is taken before the report half starts. Nothing else in the range
changes behaviour.

- 🟡 1 is the same class one spelling further on, and it sits in the
  `pytest_runtest_makereport` wrapper that phase 3 wrote (`c5df90d8`), not
  in either fix. pytest 9 makes a call-phase report for every subtest through
  that same hook, while the case's call is still running. A subtest that
  pytest's own stop ended is read as the case stopping short, although the
  body went on and pytest reports the case `passed`. The job then names a
  case that would be proved as `not proved`, and fails.
- ⬜ 2, ⬜ 3 and ⬜ 4 are notes on what the fixes left saying. The new
  heading assertion pins the words but not the figure. The module docstring
  still says the tracer decides from the call report alone. `plan.md:30`
  counts two unstable names where the tree now rests on three.

## 🟡 1 — a case whose subtest pytest skipped is named for never having run

`.github/scripts/case_check.py:208` (`executed`).

**What the code does.** The tracer's wrapper returns early unless the report
is a call-phase one that is skipped. Otherwise it adds `report.nodeid` to
the stopped set, unless an expected-failure excuse applies
(`case_check.py:206-219`). It does not ask whether the report is the call's
own report.

**What pytest 9.1.1 does.** pytest 9 ships subtests itself. The `subtests`
fixture's `__exit__` builds a `CallInfo` with `when="call"` and passes it to
`pytest_runtest_makereport` for the case's own item
(`_pytest/subtests.py:257`). It then returns `True`, which swallows the skip,
so the body goes on (`:280-284`). `TestCaseFunction.addSubTest` does the same
for a unittest `self.subTest()` block (`_pytest/unittest.py:456`). The stdlib
reaches it there for any exception other than `SkipTest`, pytest's `Skipped`
included (`unittest/case.py:73`). Both reports are made inside
`pytest_runtest_call`, while `_now[0]` still holds the id. The call's own
report comes after the call returns (`_pytest/runner.py:249-254`). Each
subtest report carries the item's `nodeid`. So one skipped subtest puts the
whole id in the stopped set.

**Failure scenario, executed.** The base holds `test_name`, and HEAD adds:

```python
def test_sub(subtests):
    with subtests.test(p="here"):
        assert m.double(2) == 4
    with subtests.test(p="elsewhere"):
        pytest.skip("x")
```

`case_check.main` at `f3eea4fe` exits 1 with `tests/test_m.py::test_sub: not
proved: none of its ids ran its call to the end on this runner (skipped,
deselected or not collected), so no mutant was run against it`. Run directly,
pytest reports `PASSED tests/test_m.py::test_sub`. The same body without the
second subtest is proved by the mutant that makes line 2 of `m.py` return
`None`, exit 0. A `unittest.TestCase` method that calls
`pytest.skip()` inside its second `self.subTest()` gives the same
`not proved`, and pytest reports it `PASSED` too.

**Why it matters.** This is the mirror of round 4's 🟡: a body that ran is
named as one that did not. It is worse than round 5's 🟡, which only changed
which red message appeared. Here a case that would be proved turns the job
red, and the message tells its author that nothing ran, which no edit to the
case's assertions can fix. `spec.md:95` says an id ran its body when pytest
wrote a call-phase report whose outcome is `passed`, and pytest wrote exactly
that. A subtest per platform, one of them skipped on ubuntu, is the ordinary
use of the feature. pytest 9 provides it without a plugin, and the job
installs pytest unpinned (`.github/workflows/test.yml:239`). No case in
`tests/` uses subtests today, so nothing is red now.

**The class, enumerated (§12).** Every report pytest makes through
`pytest_runtest_makereport` before the call has returned is a subtest's.
That covers the `subtests` fixture, a unittest `self.subTest()` with
`pytest.skip()`, `importorskip` or `pytest.xfail()` inside it, and any
plugin that reports a sub-step the same way. The tracer already knows when
the call is running, so one condition covers them all and no spelling list
is involved. The one shape it leaves as stopped short is a unittest
`self.skipTest()` inside `self.subTest()`. There pytest's `addSkip` stores
the skip as the case's own exception (`_pytest/unittest.py:330-333`), and
pytest reports the whole case `skipped`. That is pytest's own call report,
so the rule as written reads it as stopped short.

**Its depth.** Line 208 dates from `c5df90d8`, phase 3's build, and neither
of round 5's commits touched it. It sits inside `TRACER_SOURCE`, though,
which is one unit to the round-record generator, and `c3931bf8` changed that
unit. `round-record new`, run on a copy of this report in the clone, reads
the finding as a second fix of a fix and sends the item to its framer. The
spawn prompt says an open finding goes to an issue. Which one applies is the
orchestrator's decision.

**The fix, executed in the clone and then removed.** Return early when the
report is made while `_now[0]` is set. With it, both subtest fixtures are
`proved` and the no-skip control stays `proved`. All seven expected-failure
probes below keep their verdicts under both runners, and the module's 27
cases pass on 3.12. The fenced fix is below.

## Round 5's 🟡 1 is closed

`.github/scripts/case_check.py:160-182` (`executed`, and `read` against
pytest and the stdlib).

The stdlib calls `result.addExpectedFailure(self, exc_info)` with `getattr`
(`unittest/case.py:568-576`), and the result is the item itself
(`_pytest/unittest.py:391`, `:410`). An attribute set on the item instance is
therefore what the stdlib calls. `exc_info` is a `sys.exc_info()` tuple. The
check is `isinstance` against `pytest.skip.Exception` (`Skipped`, which
`importorskip` also raises) and `pytest.xfail.Exception` (`XFailed`).
`pytest.fail()` raises `Failed`, which is neither, so it stays an excused
raise. `SkipTest` never reaches this path. A twisted `Failure` is not a
tuple, reads as no stop, and is passed through unchanged.

Executed on both interpreters, each fixture added at HEAD over a base holding
`test_name`, under the `-p no:xdist` runner and under `-n 2`:

| Fixture | Verdict at `f3eea4fe` | Without the `_watch_expected(item)` call |
|---|---|---|
| method mark, `pytest.importorskip` | `not proved` | `kills nothing` |
| class mark, `pytest.xfail()` | `not proved` | `kills nothing` |
| `IsolatedAsyncioTestCase`, method mark, `pytest.skip()` | `not proved` | `kills nothing` |
| mark on a base class, `pytest.skip()` in the subclass | `not proved` | `kills nothing` |
| method mark, asserts then `pytest.fail()` | `kills nothing` | `kills nothing` |
| class mark, the body's own `AssertionError` | `kills nothing` | `kills nothing` |
| `setUp` calls `pytest.skip()`, method mark | `not proved` | `not proved` |

The four rows that should flip do flip, and the three controls do not. The
new row `TestUnderAClassMark::test_by_skip_under_a_unittest_mark` is seen
red: with the call removed, only `test_each_real_path_end_to_end[every way a
case skips here names it as one that never ran]` fails, naming that id
`kills nothing its file does not`. `spec.md:95` now says what the code does,
and so does the tracer comment at `case_check.py:194-205`.

## The heading figure — the unit at `858988e0`

`.github/scripts/case_check.py:985`, `:1014-1016` (`executed`).

`proofs` is read after every file's proof loop and before the report half,
so it is the proofs' seconds, the traced runs included. The heading's first
figure is still the whole run. The cost lines are unchanged and stay
consistent: each line's mutant count and seconds both include the report
half. With the figure removed, every one of the 15 end-to-end rows fails on
the new assertion, so the pin is seen red.

## ⬜ 2 — the heading pin holds the words, not the figure

`tests/test_a_new_case_protects_what_its_file_did_not.py:610` (`executed`).

With `{proofs:.0f}` replaced by `{time.monotonic() - started:.0f}`, which is
the figure round 5's ⬜ 2 was about, all 27 cases pass. Every fixture run
takes under a second, so both figures read `0`. The sentence is right today.
A later edit that moves `proofs =` below the report loop would bring the
old reading back with nothing red. Pinning the value would need a clock
under the test's control. This is a note, and nothing ships wrong while it
stands.

## ⬜ 3 — the module docstring says the call report decides alone

`.github/scripts/case_check.py:80` (`read`).

*The tracer decides it once per id from pytest's call report.* Since
`c3931bf8`, a `TestCase` item under an expected-failure mark is also decided
by the exception handed to `addExpectedFailure`, which is not the call
report. `spec.md:95` and the tracer comment both name that second reader,
and the docstring does not. The behaviour is right. Only the sentence is
incomplete.

## ⬜ 4 — `plan.md:30` counts two unstable names, and the tree rests on three

`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/plan.md:30`
(`read`). This is a correction to the run's paperwork.

*The stopped-short rule rests on two names pytest and the stdlib do not
document as stable: `report.wasxfail` and `__unittest_expecting_failure__`.*
The wrapper adds a third: pytest passing the item itself to the stdlib as
its result, so that the item's `addExpectedFailure` is what the stdlib calls.
Round 5's report said this (*with `addExpectedFailure` added beside it*), and
the fix range left `plan.md` as it was. The failure mode is different too. A
pytest that hands the stdlib some other result object leaves the wrapper
unused. pytest's own stop under the mark then reads as a run again, and the
case is named `kills nothing`. That is quiet rather than loud, though the
job is still red and the new end-to-end row goes red on CI's unpinned
pytest.

## What was carried

- Round 5's ⬜ 2 (`case_check.py:993`, the heading and cost lines) is carried
  open, and it closes at the run's end. `858988e0` answers its heading half,
  as confirmed above.
- Round 4's ⬜ 2 (`.github/workflows/test.yml:223`) is carried open.
- Lines the branch adds that name `evidence-check`, `survivor-check`,
  `survivors.md`, `evidence-todo.md`, `--reverify` or a ledger sit in the
  phase-1 and phase-2 records, in round reports, and in `.test_durations` ids
  of tests that exist on the base. That is history, and round 1's ⬜ 5
  answered it. Carried, not re-derived. The fix range itself adds none
  (`executed`: grep over the range's `+` lines).
- Where pytest reads an expected failure (`_pytest/unittest.py:347-355`,
  `:509-512`, `unittest/case.py:54-72`, `:637-639`) is carried from round 5's
  coordinates. Each one was re-opened at pytest 9.1.1 and still holds.

## Regression tests to plant

- `tests/test_a_new_case_protects_what_its_file_did_not.py`, a row of
  `test_each_real_path_end_to_end`: a case one of whose subtests pytest
  skips is `proved`, exit 0. The row and its fixture are fenced below. The
  same fixture was seen red at `f3eea4fe` and green with the fix, as a probe.

## Facts for the record

- pytest 9.1.1 calls `pytest_runtest_makereport` once per subtest, with
  `when="call"`, on the case's own item, from inside `pytest_runtest_call`
  (`_pytest/subtests.py:257`, `_pytest/unittest.py:456`). A hook wrapper on
  `pytest_runtest_makereport` sees those reports before the call's own one.
- The `cases` job installs pytest without a pin
  (`.github/workflows/test.yml:239`), so the tracer meets whichever pytest is
  current when the job runs.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | A case one of whose subtests pytest's own stop ended is read as having stopped short, and is named `not proved` although pytest reports its call `passed` | `.github/scripts/case_check.py:208` | open | executed: a `subtests` fixture and a unittest `self.subTest()` fixture each exit 1 with `not proved` at `f3eea4fe`, pytest reports both `PASSED`, and the no-skip control is `proved`; with the paste-ready guard both are `proved`. Read: `_pytest/subtests.py:257`, `_pytest/unittest.py:456`, `unittest/case.py:73`, `_pytest/runner.py:249-254`. Line 208 dates from `c5df90d8`, inside `TRACER_SOURCE`, which round 5's fixes changed |
| 🟢 | round 5's finding 1 is closed — pytest's own skip, importorskip or xfail inside a unittest expected failure, method or class, is named `not proved` | `.github/scripts/case_check.py:160` | confirmed | executed: seven fixtures under two runners on CPython 3.12.12 and 3.13.9, four flipping and three controls not when the call is removed; the new row seen red; read: `unittest/case.py:568-576`, `_pytest/unittest.py:347-355`, `:391`, `:410` |
| 🟢 | the heading's proofs figure is taken before the report half, and its pin is seen red | `.github/scripts/case_check.py:985` | confirmed | executed: with the figure removed, all 15 end-to-end rows fail; read: `:982-1016` |
| ⬜ 2 | The heading assertion pins the words "the proofs in", not the figure, so a mutant that prints the whole run's seconds passes | `tests/test_a_new_case_protects_what_its_file_did_not.py:610` | open | executed: with `{proofs:.0f}` replaced by the whole run's seconds, 27 of 27 pass |
| ⬜ 3 | The module docstring says the tracer decides the stopped ids from pytest's call report, and since `c3931bf8` it also reads the exception handed to `addExpectedFailure` | `.github/scripts/case_check.py:80` | open | read: `:80`, `:160-176`, `spec.md:95` |
| ⬜ 4 | `plan.md` names two unstable names the stopped-short rule rests on; the wrapper adds a third, pytest handing the item to the stdlib as its result | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/plan.md:30` | open | read: `plan.md:30`, `_pytest/unittest.py:391`, `:410`; a correction to the run's paperwork |
| 🟢 | nothing else in the fix range changes behaviour, and `spec.md:95` says what the tracer does | `.github/scripts/case_check.py:194` | confirmed | read: the whole diff `1063ba45..f3eea4fe`; executed: the module's 27 cases pass at `f3eea4fe` on 3.13.9 and 3.12.12, and ruff 0.17.0 check and format are clean on both changed `.py` files |
| 🟢 | round 5's record closes on its fix table: the fix range and its two commits are the ones on the branch | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/rounds/round-5.md:11` | confirmed | read: `git log 1063ba45..858988e0`, `round-5.md:7-31` |
| 🟢 | the fix range adds no live reference to the tooling removed in 0.22.0 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/spec.md:95` | confirmed | executed: grep over the range's `+` lines; the branch's other occurrences are carried as round 1's ⬜ 5 answered |
| ❓ | what the `cases` job says on a CI runner at `f3eea4fe` | PR #939 | ❓ out of verified scope | the branch is not pushed; the orchestrating session, which pushes it, reads PR #939's next run |

## Paste-ready fixes

### 🟡 1 — `.github/scripts/case_check.py`, inside `TRACER_SOURCE`

```python
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    report = (yield).get_result()
    # A report made while the call is still running is a subtest's, which
    # pytest makes through this hook for the case's own item; the call's own
    # report comes after the call returns.
    if _now[0] is not None or report.when != "call" or not report.skipped:
        return
```

### 🟡 1 — the row, `tests/test_a_new_case_protects_what_its_file_did_not.py`

```python
# A case one of whose subtests pytest's own stop ended: the stop ends that
# subtest, the body goes on, and pytest reports the call passed.
SUBTEST_SKIP = (
    "\nimport pytest\n\n\ndef test_by_subtests(subtests):\n"
    '    with subtests.test(p="here"):\n'
    "        assert m.double(2) == 4\n"
    '    with subtests.test(p="elsewhere"):\n'
    '        pytest.skip("another platform")\n'
)
```

```python
        pytest.param(
            {"tests/test_m.py": module_text(NAME)},
            {"tests/test_m.py": module_text(NAME, SUBTEST_SKIP)},
            {},
            0,
            [
                "tests/test_m.py::test_by_subtests: proved — the only killer in "
                "its file of m.py:2"
            ],
            id="a case one of whose subtests skips still ran its body",
        ),
```

### 🟡 1 — `spec.md:95`, after "…an expected-failure mark excused the raise."

```markdown
A report pytest makes for a subtest, through the same hook while the call is
still running, is not the call's report: a subtest that pytest's own stop
ended ends that subtest, and the body goes on.
```

## Executed probes

| What was run | Result |
|---|---|
| `tests/test_a_new_case_protects_what_its_file_did_not.py`, `-n 4`, at `f3eea4fe`, CPython 3.13.9 and 3.12.12 | 27 passed on each, exit 0 |
| the same module with `_watch_expected(item)` removed from the tracer | exit 1; only the row `every way a case skips here names it as one that never ran` fails, naming `TestUnderAClassMark::test_by_skip_under_a_unittest_mark` `kills nothing` |
| the same module with the heading's `the proofs in` figure removed | exit 1; 15 failed, 12 passed |
| the same module with `{proofs:.0f}` replaced by the whole run's seconds | exit 0; 27 passed (⬜ 2) |
| a `test_tmp_*` probe: seven expected-failure fixtures through `case_check.main`, each under `-p no:xdist` and under `-n 2`, on 3.13.9 and 3.12.12 | 14 of 14 as the table above says; with `_watch_expected(item)` removed, the four stop rows fail and the three controls pass |
| the same probe: a `subtests` fixture and a unittest `self.subTest()` fixture, each with one subtest skipped, and a no-skip control | at `f3eea4fe`: both `not proved`, exit 1, pytest `PASSED` directly; the control `proved`, exit 0 |
| the same probe with the paste-ready guard in the tracer, 3.12.12 | 17 of 17 pass; the module's 27 pass |
| `uvx ruff check` and `ruff format --check` on the two changed `.py` files, ruff 0.17.0 | `All checks passed!`, `2 files already formatted` |
| broad gate: the full suite, the repository-wide lint and the typecheck | not yet — this round ran none of them, and the sealer runs them once the run ends |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| 🟡 1, a skipped subtest read as the case stopping short | a new issue, as the spawn prompt says, or the frame: `round-record new`, run on a copy of this report in the clone, reads 🟡 1 as a second fix of a fix, because `TRACER_SOURCE` is one unit and round 5's fixes changed it, though line 208 dates from `c5df90d8` | the orchestrating session of #929, which chooses between the two as the run ends; the issue's assignee or the framer then fixes `TRACER_SOURCE` |

Needs a fix: yes — 🟡 1 (a case one of whose subtests pytest's own stop ended is named `not proved`, though pytest reports its call `passed`)
Loses a record or crashes: no

The broad gate comes due once the orchestrator has deferred 🟡 1, since this
record ends the run. What comes due is the sealer's spawn.

## Proof block

Files opened this round: `.github/scripts/case_check.py` (`:1-268`,
`:840-1040`), `tests/test_a_new_case_protects_what_its_file_did_not.py`
(`:1-32`, `:282-420`, `:420-630`), `.github/workflows/test.yml`
(`:220-266`), `CONTRIBUTING.md` (`:155-185`),
`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/spec.md:95` (as
diffed), `plan.md` (`:20-40`), `overview.md`, `changelog.md`,
`rounds/round-5.md`, `rounds/round-5-report.md` (`:1-140`); in the
worktree's venv, `_pytest/unittest.py` (`:225-420`, `:420-480`, `:495-530`),
`_pytest/subtests.py` (`:225-300`), `_pytest/runner.py` (grep), and
`unittest/case.py` (grep at `:47-81`, `:185`, `:568-576`, `:637-661`).
