# 1791876666-the-test-suite-is-held-to-a-budget — review round 4

| Field | Value |
|---|---|
| Target SHA | 489711470b7a5194e23e1dd61dd0e181e0604c11 |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #939 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `d99c6cee675eebb2bb937f2572920e8b621e2807..8983d41361e48770e877f33508442ce7b605135f`, 2 commits |
| Contract changes | none |
| New units | CLASS_EXPECTED (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (an `@unittest.expectedFailure` on a class is named `not proved` instead of being run under its mutants) |
| Loses a record or crashes | no |
<!-- New units: .github/workflows/test.yml read by the diff-line heuristic and not by the AST -->

- [ ] Pass

## What this round was asked

Round 4 of #929, the first after the reframe: phase 3 over 2aa76b37..48971147 against its plan row and the reframed spec (pytest's call report decides whether a case ran its body; every traced line kept; short ids feed only the never-ran decision), the tryfirst and timeout-case departures, and any live text standing on what #944 removed. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | An `@unittest.expectedFailure` on a `TestCase` class makes its body's raise an expected failure, but the tracer reads `__unittest_expecting_failure__` from the function alone, so such a new case is named `not proved` instead of being run under its mutants | `.github/scripts/case_check.py:190` | **fixed** `3fb8d310` | fixed at 3fb8d310; executed: a fixture adding a class-level expected failure exits 1, `not proved` at `48971147`; with the attribute also read from `item.cls`, `kills nothing its file does not`, and the stopped-short rows still pass; read: `unittest/case.py:637-639`, `_pytest/unittest.py:347-355`, `spec.md:95` |
| ⬜ 2 | The `cases` comment's last two lines were not reflowed after the sentence before them was rewritten | `.github/workflows/test.yml:223` | open | read |
| 🟢 | round 3's finding 1 is closed — a sibling that asserts and then skips keeps its traced lines and kills what it asserted | `.github/scripts/case_check.py:882` | confirmed | executed: the module's 26 cases pass at `48971147`, S16's row among them; read: `hits` is unfiltered at `:199` and only `never_ran` reads `short` |
| 🟢 | round 3's finding 2 is closed — an imperative `pytest.xfail()` is named `not proved`, in a plain function and in a `TestCase` method | `.github/scripts/case_check.py:193` | confirmed | executed: S17's `test_by_xfail` row passes; a probe with `pytest.xfail()` in a `TestCase` method gives `not proved` |
| 🟢 | `tryfirst=True` puts the tracer outside `tests/conftest.py`'s wrapper, as `spec.md:95` asks; its deletion survives only because nothing rewrites a skipped report | `.github/scripts/case_check.py:182` | confirmed | read: pluggy `_hooks.py:464-473`, `_callers.py:93`, `tests/conftest.py:985-997` |
| 🟢 | the added timeout case pins the sixth element `check` unpacks | `tests/test_a_new_case_protects_what_its_file_did_not.py:192` | confirmed | executed: passes in the module run; read: `case_check.py:691`, `:870` |
| 🟢 | the four prose places state the rule in one sentence each and list no spellings | `.github/scripts/case_check.py:76` | confirmed | read: docstring, tracer comment, `test.yml:221`, `changelog.md:36` |
| 🟢 | no live file names `survivor-check`, `survivors.md` or a ledger; the phase-1 and phase-2 passages are history round 1's ⬜ 5 answered | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:464` | confirmed | executed: grep over every `+` line of the branch diff outside `rounds/` |
| ❓ | what the `cases` job says on a CI runner at `48971147` | PR #939 | ❓ out of verified scope | the branch is not pushed; the orchestrating session, which pushes it, reads PR #939's next run |

## Paste-ready fixes

```python
    expected = any(
        getattr(holder, "__unittest_expecting_failure__", False)
        for holder in (getattr(item, "obj", None), getattr(item, "cls", None))
    )
```
```markdown
The one translation is pytest's: its unittest plugin raises the xfail stop itself on behalf of an `@unittest.expectedFailure` whose body raised, and `__unittest_expecting_failure__` on the function or its class says so, as the stdlib reads both, so that case ran its body.
```
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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
