# 1791876666-the-test-suite-is-held-to-a-budget — review round 6

| Field | Value |
|---|---|
| Target SHA | f3eea4fe1b531e3c7d09f8982b2f829b7afb5e81 |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #939 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | `dd22f4f01679b48aeedf9ddc93c55fbbb794e629..dd22f4f01679b48aeedf9ddc93c55fbbb794e629`, 0 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | second — 🟡 1 at .github/scripts/case_check.py#TRACER_SOURCE, a unit round-5's fixes changed; the fix passes stop here and the work item goes back to its framer |
| Needs a fix | yes — 🟡 1 (a case one of whose subtests pytest's own stop ended is named `not proved`, though pytest reports its call `passed`) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Verifying round 6 of #929, the run's last: round 5's fix at c3931bf8 (a pytest stop inside a unittest expected failure is stopped short) and note 858988e0 (the proofs' seconds in the header), against pytest 9.1.1 and the stdlib, and whether the item says only what its tree does. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | A case one of whose subtests pytest's own stop ended is read as having stopped short, and is named `not proved` although pytest reports its call `passed` | `.github/scripts/case_check.py:208` | deferred the frame | the frame — the second fix of a fix since the reframe stops the fix passes; the owner decided on 2026-10-15 that the reframe takes the never-ran tracer and the cases gate out; executed: a `subtests` fixture and a unittest `self.subTest()` fixture each exit 1 with `not proved` at `f3eea4fe`, pytest reports both `PASSED`, and the no-skip control is `proved`; with the paste-ready guard both are `proved`. Read: `_pytest/subtests.py:257`, `_pytest/unittest.py:456`, `unittest/case.py:73`, `_pytest/runner.py:249-254`. Line 208 dates from `c5df90d8`, inside `TRACER_SOURCE`, which round 5's fixes changed |
| 🟢 | round 5's finding 1 is closed — pytest's own skip, importorskip or xfail inside a unittest expected failure, method or class, is named `not proved` | `.github/scripts/case_check.py:160` | confirmed | executed: seven fixtures under two runners on CPython 3.12.12 and 3.13.9, four flipping and three controls not when the call is removed; the new row seen red; read: `unittest/case.py:568-576`, `_pytest/unittest.py:347-355`, `:391`, `:410` |
| 🟢 | the heading's proofs figure is taken before the report half, and its pin is seen red | `.github/scripts/case_check.py:985` | confirmed | executed: with the figure removed, all 15 end-to-end rows fail; read: `:982-1016` |
| ⬜ 2 | The heading assertion pins the words "the proofs in", not the figure, so a mutant that prints the whole run's seconds passes | `tests/test_a_new_case_protects_what_its_file_did_not.py:610` | deferred the frame | the frame — the cases header goes with the gate the reframe removes; executed: with `{proofs:.0f}` replaced by the whole run's seconds, 27 of 27 pass |
| ⬜ 3 | The module docstring says the tracer decides the stopped ids from pytest's call report, and since `c3931bf8` it also reads the exception handed to `addExpectedFailure` | `.github/scripts/case_check.py:80` | deferred the frame | the frame — the tracer docstring goes with the tracer the reframe removes; read: `:80`, `:160-176`, `spec.md:95` |
| ⬜ 4 | `plan.md` names two unstable names the stopped-short rule rests on; the wrapper adds a third, pytest handing the item to the stdlib as its result | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/plan.md:30` | deferred the frame | the frame — plan.md is rewritten by the reframe; read: `plan.md:30`, `_pytest/unittest.py:391`, `:410`; a correction to the run's paperwork |
| 🟢 | nothing else in the fix range changes behaviour, and `spec.md:95` says what the tracer does | `.github/scripts/case_check.py:194` | confirmed | read: the whole diff `1063ba45..f3eea4fe`; executed: the module's 27 cases pass at `f3eea4fe` on 3.13.9 and 3.12.12, and ruff 0.17.0 check and format are clean on both changed `.py` files |
| 🟢 | round 5's record closes on its fix table: the fix range and its two commits are the ones on the branch | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/rounds/round-5.md:11` | confirmed | read: `git log 1063ba45..858988e0`, `round-5.md:7-31` |
| 🟢 | the fix range adds no live reference to the tooling removed in 0.22.0 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/spec.md:95` | confirmed | executed: grep over the range's `+` lines; the branch's other occurrences are carried as round 1's ⬜ 5 answered |
| ❓ | what the `cases` job says on a CI runner at `f3eea4fe` | PR #939 | ❓ out of verified scope | the branch is not pushed; the orchestrating session, which pushes it, reads PR #939's next run |

## Paste-ready fixes

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
| round-4 | `.github/workflows/test.yml:223` | round 4's ⬜ 2 — answered |
| round-4 | `.github/scripts/case_check.py:882` | round 4's 🟢 — confirmed |
| round-4 | `.github/scripts/case_check.py:193` | round 4's 🟢 — confirmed |
| round-4 | `.github/scripts/case_check.py:182` | round 4's 🟢 — confirmed |
| round-4 | `tests/test_a_new_case_protects_what_its_file_did_not.py:192` | round 4's 🟢 — confirmed |
| round-4 | `.github/scripts/case_check.py:76` | round 4's 🟢 — confirmed |
| round-4 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:464` | round 4's 🟢 — confirmed |
| round-4 | PR #939 | round 4's ❓ — out of verified scope |
| round-5 | `.github/scripts/case_check.py:993` | round 5's ⬜ 2 — answered |
| round-5 | `.github/scripts/case_check.py:192` | round 5's 🟢 — confirmed |
| round-5 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/plan.md:28` | round 5's 🟢 — confirmed |
| round-5 | `.github/scripts/case_check.py:871` | round 5's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| 🟡 1, a skipped subtest read as the case stopping short | a new issue, as the spawn prompt says, or the frame: `round-record new`, run on a copy of this report in the clone, reads 🟡 1 as a second fix of a fix, because `TRACER_SOURCE` is one unit and round 5's fixes changed it, though line 208 dates from `c5df90d8` | the orchestrating session of #929, which chooses between the two as the run ends; the issue's assignee or the framer then fixes `TRACER_SOURCE` |
