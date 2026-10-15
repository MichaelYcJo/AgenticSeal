# 1791876666 — review round 4, report

Target: `48971147` on `chore/929-the-test-suite-only-grows` (PR #939, local
tip, not pushed), against `origin/release/v0.22.0` at `642441fc`. This is the
first round after the reframe at `17cd0b36`, approved at `2aa76b37`. Its scope
is phase 3, `2aa76b37..48971147`, then a short pass over the branch for prose
that states something the tree does not. Reviewed in a `git clone --no-local`
of the worktree at that SHA. Paths are relative to the repository root.

## How the findings relate

Phase 3 builds the rule the reframe asked for, and round 3's two findings are
closed by it. The rule reads pytest's call report once. Every traced line is
kept. Only the never-ran naming reads the stopped ids. Both departures the
implementer recorded hold up.

- 🟡 1 — one way of marking an expected failure is still read as a stop. The
  tracer asks the test *function* whether it carries
  `__unittest_expecting_failure__`. The stdlib also reads the attribute from
  the *class*, so `@unittest.expectedFailure` on a `TestCase` class is a
  supported spelling. A new case written that way has a body that runs and
  raises, and it is named `not proved`. `spec.md`'s rule calls it a run. This
  is the same class of defect the reframe exists to close: one spelling
  outside what the reader recognises. It is narrower than the ones before it
  and it fails loud.
- ⬜ 2 — `test.yml`'s `cases` comment was rewritten and its last two lines
  were not reflowed.

## 🟡 1 — an expected failure marked on its class is named for never having run

`.github/scripts/case_check.py:190` (`executed`).

```python
    expected = getattr(
        getattr(item, "obj", None), "__unittest_expecting_failure__", False
    )
```

The stdlib decides an expected failure from two places
(`unittest/case.py:637-639` in CPython 3.13.9):
`getattr(self, "__unittest_expecting_failure__", False) or
getattr(testMethod, ...)`. So `@unittest.expectedFailure` on the class, or on
a base class it inherits from, makes every method an expected failure.
pytest's `TestCaseFunction.addExpectedFailure` (`_pytest/unittest.py:347`)
then raises `xfail("")` for it, exactly as it does for the method-level
decorator. The tracer sees `stop` true. Because it reads only the function,
it sees `expected` false, and it adds the id to `_skipped`.

**Failure scenario, executed.** The base holds `test_name`. HEAD adds:

```python
@unittest.expectedFailure
class TestClassExpected(unittest.TestCase):
    def test_by_class_expected_failure(self):
        assert m.double(2) == 5
```

`case_check.main` at `48971147` exits 1 with
`tests/test_m.py::TestClassExpected::test_by_class_expected_failure: not
proved: none of its ids ran its call to the end on this runner (skipped,
deselected or not collected), so no mutant was run against it`. The body ran
and raised. By `spec.md:95` (*`skipped` because the body itself raised and an
expected-failure mark excused the raise*) and S17, the case is a run and
should be named `kills nothing its file does not`.

**Why it matters.** The `cases` job fails a pull request with the wrong
reason. The author is told the case did not run on ubuntu, which is false,
and the fix that message points to (make it run) does nothing. The direction
is loud: the job is red either way, because the case also kills nothing.
But a class-level expected failure whose body a mutant *could* fail would be
refused without any mutant being run. `plan.md:30` names a pytest rename as
the loud risk of alternative M. It does not name this spelling, and
`spec.md:95` states the function attribute as the mechanism.

**What the fix changes, executed in the clone and then reverted.** The
tracer reads the attribute from the function and from `item.cls`, the way
the stdlib reads it from the method and the instance. The probe above then
gives `kills nothing its file does not`. An imperative `pytest.xfail()`
inside a plain `TestCase` method is still `not proved`. The module's
stopped-short rows (`-k "every or unittest or after or expected"`, 4 cases)
pass.

## ⬜ 2 — the `cases` comment in `test.yml` ends on a ragged wrap

`.github/workflows/test.yml:223-224` (`read`). Phase 3 rewrote the sentence
before it, and the line `# install line is the \`pytest\`` stops at column
33, followed by `# job's, so the cases run …`. The behaviour and the fact are
both right. It only reads badly, so `Needs a fix` does not count it.

## The two departures the implementer recorded

**`tryfirst=True` — confirmed (`read`).** The claim was that without it
`tests/conftest.py#pytest_runtest_makereport` would run its tail after the
tracer had read the report. pluggy's `_add_hookimpl`
(`pluggy/_hooks.py:464-473`) puts a non-`tryfirst` wrapper registered later
in front of earlier ones. `_callers.py:93` calls them in reverse, so the
later one is outer and its tail runs last. A conftest is registered after a
`-p` plugin, so the claim is right. The conftest wrapper at
`tests/conftest.py:985` rewrites only a passing call report
(`if report.when != "call" or not report.passed: return`), so no verdict
moves today, which is also what `phases/phase-3.md` says. A `tryfirst`
wrapper goes to the end of the wrapper list and is outermost. That is what
`spec.md:95`'s *after every other implementation* asks for. The deleted
`tryfirst` survives mutation because nothing in the suite rewrites a skipped
report. That is a stated, grounded survivor, not a defect.

**The timeout case — confirmed (`executed`).**
`test_a_traced_run_that_times_out_hands_back_nothing_it_traced` reaches
`traced_run`'s `TimeoutExpired` branch with a one-second timeout. It asserts
the six-element shape `check` unpacks at `.github/scripts/case_check.py:870`.
Without it, a five-element return there would make `check` raise on the
unpacking instead of naming the file to restructure. `subprocess.run` kills
the child on timeout, so it leaves no process behind. It passes in the
module run.

## The rest of phase 3, against its plan row

All read at `48971147`, and executed where the probe table says.

- The hookwrapper decides once per id, at `case_check.py:182-195`, from the
  finished report and `call.excinfo`. This follows `plan.md:28`'s reading of
  `_pytest/skipping.py:277-312` and `_pytest/unittest.py:508-523`, both of
  which I opened in the worktree's pytest 9.1.1.
- `pytest_sessionfinish` writes every id's lines with no filter, and the
  stopped ids under `"short"`.
- `short` is read at one place, `case_check.py:882`, for `never_ran`. `drawn`,
  `own_ids` at `:906` and `selected` read `hits` whole. A parametrized case
  with one id that skips in its body and one that runs is `proved` (probe).
- The docstring (`case_check.py:76-85`), the tracer comment (`:175-181`),
  `test.yml:221-223` and the changelog fragment's `Added` entry
  (`changelog.md:36-39`) each state the rule in one sentence: ran its body,
  or pytest never started its call or its own stop ended it. None lists
  spellings. `CONTRIBUTING.md` does not state the rule at all, so it has
  nothing to drift.
- S16 and S17's rows are in `test_each_real_path_end_to_end`. Their red-first
  account in `phases/phase-3.md` is the implementer's claim, and I did not
  re-run it against `e0e0d485`. The rows pass at the tip, and T10 stays
  green with the 🟡 1 fix applied, so the fix does not undo it.

## The branch, briefly — prose against the tree

- `survivors.md` is gone at `48971147`. No line this branch adds outside
  `rounds/` names `survivor-check`, `survivors.md` or a ledger, except the
  passages in `phases/phase-1.md:157-175` and `phases/phase-2.md:445-465`.
  Those are history of what was run before #944. Round 1's ⬜ 5 answered
  them, and `phase-2.md:464` says #944 removes the ledger. Carried, not
  re-reported.
- `phases/phase-3.md`'s claim that `17cd0b36` and `2aa76b37` touch only
  `plan.md`, `spec.md` and `questions.md` holds (`git diff --stat e0e0d485
  2aa76b37`, executed).
- `overview.md:67`'s *the cases that plan's T8 and T9 would have been* refers
  back to *the plan as it stood then* two lines up, so it does not collide
  with `plan.md:86-87`'s new T8 and T9.
- `overview.md:44` leaves the `cases` job at the tip to PR #939's next CI
  run. That is honest: the branch is not pushed, and I read no CI for
  `48971147`.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | An `@unittest.expectedFailure` on a `TestCase` class makes its body's raise an expected failure, but the tracer reads `__unittest_expecting_failure__` from the function alone, so such a new case is named `not proved` instead of being run under its mutants | `.github/scripts/case_check.py:190` | open | executed: a fixture adding a class-level expected failure exits 1, `not proved` at `48971147`; with the attribute also read from `item.cls`, `kills nothing its file does not`, and the stopped-short rows still pass; read: `unittest/case.py:637-639`, `_pytest/unittest.py:347-355`, `spec.md:95` |
| ⬜ 2 | The `cases` comment's last two lines were not reflowed after the sentence before them was rewritten | `.github/workflows/test.yml:223` | open | read |
| 🟢 | round 3's finding 1 is closed — a sibling that asserts and then skips keeps its traced lines and kills what it asserted | `.github/scripts/case_check.py:882` | confirmed | executed: the module's 26 cases pass at `48971147`, S16's row among them; read: `hits` is unfiltered at `:199` and only `never_ran` reads `short` |
| 🟢 | round 3's finding 2 is closed — an imperative `pytest.xfail()` is named `not proved`, in a plain function and in a `TestCase` method | `.github/scripts/case_check.py:193` | confirmed | executed: S17's `test_by_xfail` row passes; a probe with `pytest.xfail()` in a `TestCase` method gives `not proved` |
| 🟢 | `tryfirst=True` puts the tracer outside `tests/conftest.py`'s wrapper, as `spec.md:95` asks; its deletion survives only because nothing rewrites a skipped report | `.github/scripts/case_check.py:182` | confirmed | read: pluggy `_hooks.py:464-473`, `_callers.py:93`, `tests/conftest.py:985-997` |
| 🟢 | the added timeout case pins the sixth element `check` unpacks | `tests/test_a_new_case_protects_what_its_file_did_not.py:192` | confirmed | executed: passes in the module run; read: `case_check.py:691`, `:870` |
| 🟢 | the four prose places state the rule in one sentence each and list no spellings | `.github/scripts/case_check.py:76` | confirmed | read: docstring, tracer comment, `test.yml:221`, `changelog.md:36` |
| 🟢 | no live file names `survivor-check`, `survivors.md` or a ledger; the phase-1 and phase-2 passages are history round 1's ⬜ 5 answered | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:464` | confirmed | executed: grep over every `+` line of the branch diff outside `rounds/` |
| ❓ | what the `cases` job says on a CI runner at `48971147` | PR #939 | ❓ out of verified scope | the branch is not pushed; the orchestrating session, which pushes it, reads PR #939's next run |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_a_new_case_protects_what_its_file_did_not.py -q` at `48971147` | exit 0, 26 passed |
| `bin/test tests/test_every_reader_ends_a_line_where_gfm_does.py -q` at `48971147` | exit 0, 149 passed |
| `uvx ruff check` on `case_check.py` and the case module | exit 0 |
| probe `tests/test_tmp_round4_probe.py` (NAME NOT IN TREE: deleted after the run), `case_check.main` on four fixtures at `48971147` | class-level `@unittest.expectedFailure` whose body raised: exit 1, `not proved`; `pytest.xfail()` in a `TestCase` method: exit 1, `not proved`; a parametrized case with one id skipping in its body: exit 0, `proved`; `xfail(strict=True)` whose body calls `pytest.skip()`: exit 1, `not proved` |
| the same probe's first two fixtures with the 🟡 1 fix applied in the clone, then reverted | class-level expected failure: `kills nothing its file does not`; `TestCase` with `pytest.xfail()`: `not proved` |
| `bin/test tests/test_a_new_case_protects_what_its_file_did_not.py -q -k "every or unittest or after or expected"` with the 🟡 1 fix applied | exit 0, 4 passed |
| `git diff --stat e0e0d485 2aa76b37` | only `plan.md`, `questions.md`, `spec.md` |
| `case_check.py` as the `cases` job runs it | not yet: not run by this round; `phases/phase-3.md` records 22 proved locally, a claim; PR #939's next CI run answers it |
| Broad gate (full suite, repository-wide lint, typecheck) | not yet: not run by this round, and owed to the sealer once the rounds settle |

## Paste-ready fixes

### 🟡 1

`.github/scripts/case_check.py`, inside `TRACER_SOURCE`:

```python
    expected = any(
        getattr(holder, "__unittest_expecting_failure__", False)
        for holder in (getattr(item, "obj", None), getattr(item, "cls", None))
    )
```

`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/spec.md:95`, the
sentence beginning `The one translation is pytest's`:

```markdown
The one translation is pytest's: its unittest plugin raises the xfail stop itself on behalf of an `@unittest.expectedFailure` whose body raised, and `__unittest_expecting_failure__` on the function or its class says so, as the stdlib reads both, so that case ran its body.
```

`tests/test_a_new_case_protects_what_its_file_did_not.py`, a constant beside
`UNITTEST_EXPECTED` and a row after *a unittest expected failure whose body
raised is a run*. Seen red at `48971147`: the expected line is absent and the
output names the case `not proved`.

```python
CLASS_EXPECTED = (
    "\nimport unittest\n\n\n@unittest.expectedFailure\n"
    "class TestClassExpected(unittest.TestCase):\n"
    "    def test_by_class_expected_failure(self):\n"
    "        assert m.double(2) == 5\n"
)
```

```python
        pytest.param(
            {"tests/test_m.py": module_text(NAME)},
            {"tests/test_m.py": module_text(NAME, CLASS_EXPECTED)},
            {},
            1,
            [
                "tests/test_m.py::TestClassExpected::"
                "test_by_class_expected_failure: kills nothing its file does not"
            ],
            id="a unittest expected failure marked on its class is a run",
        ),
```

## Regression tests to plant

- `tests/test_a_new_case_protects_what_its_file_did_not.py`, the row above in
  `test_each_real_path_end_to_end`. It belongs with S17.

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

Needs a fix: yes — 🟡 1 (an `@unittest.expectedFailure` on a class is named `not proved` instead of being run under its mutants)
Loses a record or crashes: no

When 🟡 1 is fixed and a verifying round confirms it, nothing is left open,
and the sealer's spawn comes due.

## Proof block

Files opened: `.github/scripts/case_check.py` (`:76-85`, `:120-200`,
`:600-705`, `:855-935`), `.github/workflows/test.yml:212-230`,
`tests/test_a_new_case_protects_what_its_file_did_not.py` (`:20-32`,
`:189-200`, `:270-356`, `:354-600`), `tests/conftest.py:983-998`,
`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/` `spec.md`,
`plan.md`, `phases/phase-3.md`, `phases/phase-1.md:150-180`,
`phases/phase-2.md:440-470`, `overview.md`, `changelog.md`,
`rounds/round-3.md`, `rounds/round-3-report.md:1-22`; pytest 9.1.1
`_pytest/skipping.py:277-321`, `_pytest/unittest.py:330-365` and `:505-523`;
pluggy `_hooks.py:451-473`; CPython 3.13.9 `unittest/case.py` (grep at
`:185`, `:637-659`).
