# 1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it — review round 4

| Field | Value |
|---|---|
| Target SHA | 7147e5f61e8919077bbbd383e5e3aa1cc69b83db |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 887 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are not yet written |
| Fix range | none — the fixes are not yet written |
| Contract changes | none — the fixes are not yet written |
| New units | none — the fixes are not yet written |
| Fix of a fix | second — 🟡 1 at skills/evidence-check/scripts/evidence_check.py#suite_record, a unit round-3's fixes changed; the fix passes stop here and the work item goes back to its framer |
| Needs a fix | yes — 🟡 1 (a skipped or xfailed subtest holds its row at pytest 9's default verbosity) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Verifying round 4 of round 3's fixes: fa199d96..1cc634a7 plus the table and the close at 7147e5f6. The job was the answers to round 3's seven verdicts; round 3's new units were a finding surface. The spawn named four things to judge. First, re-running the 66-token record check. Second, whether cutting at the first [ is right for a case id that holds [. Third, whether the outcome/wasxfail rule stays true for a failing subtest. Fourth, whether the existence-line search can miss or double-print. It also ran the eight guard modules once. Facts arrived labelled. Read from the smith: the cut, the outcome rule, the gate's stderr line, the date fix, two pinned sentences, and the 66-token record check at exit 0.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | A skipped or xfailed subtest is written `""` at pytest 9's default verbosity and holds its row; under `-q` or `-v` the same subtest is refused | `skills/evidence-check/scripts/evidence_check.py:2421` | open | executed on pytest 9.1.1 at three verbosities (table above); the proposed case is 4 red at the head and 8 green with the fix, and the module passed 140 with it; this tree's row is `-q` and no cited test uses subtests |
| ⬜ 2 | T26 claims *a preflight prints none* and *red with its guard removed*; its one cited case never runs a preflight and stays green under either guard mutation | `seal/ledger/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it.md:23` | open | executed: both mutations in the clone, the cited case passed each time, and the module's 15 preflight cases passed with the `head` guard removed; the behaviour is right by reading; a correction to the run's paperwork, outside `Needs a fix` |
| ⬜ 3 | The line the gate repeats ends *`broad-gate` hands this check the sealed run's record*, which names neither the cause nor the remedy when the gate is the one printing it | `skills/verify/scripts/broad_gate.py:3585` | open | read; the line comes from `evidence_check.py#existence_line` |
| 🟢 | round 3's blocking finding 1 is closed — a case id holding `::` or `[` belongs to its function | `skills/evidence-check/scripts/evidence_check.py:2426` | confirmed | executed: the two cases red at fa199d96 and green at the head; a probe with ids `a[b`, `x]::y[z`, `[[::]]` and `q[::r` read as expected; the 66-token record sealed with checker exit 0 |
| 🟢 | round 3's finding 2 is closed in the direction it named — a test whose subtests all passed is held under `-q` | `skills/evidence-check/scripts/evidence_check.py:2421` | confirmed | executed: the case red at fa199d96 and green at the head; failing subtests stay refused at every verbosity; the other direction is 🟡 1 |
| 🟢 | round 3's finding 3 is closed — the gate repeats the checker's existence line on its own output | `skills/verify/scripts/broad_gate.py:3583` | confirmed | executed: the case red at fa199d96 and green at the head; read: the search by line head cannot miss or double-print |
| 🟢 | round 3's finding 4 is closed — the `--checked` date is one every timezone has reached | `tests/test_a_ledger_row_is_held_by_its_test.py:1128` | confirmed | read; CI for this head is pending (❓ below) |
| 🟢 | round 3's finding 5 is closed — the comment names the five fields read | `skills/evidence-check/scripts/evidence_check.py:2334` | confirmed | read |
| 🟢 | round 3's finding 6 is closed — the documents say the sealed run decides a skipped test | `docs/the-evidence-ledger.md:267` | confirmed | read; `templates/ledger.md:72` already says *the run it seals* |
| 🟢 | round 3's finding 7 is closed — the spec says the gate prints the line on a passing run | `seal/specs/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it/spec.md:365` | confirmed | read |
| ❓ | The full suite, the repository-wide lint and the typecheck at the head | the head | ❓ out of verified scope | the broad gate; the sealer answers it after the rounds settle |
| ❓ | The nine pytest legs of PR #887 at this head | PR #887 | ❓ out of verified scope | all nine were pending when read; CI answers it |

## Paste-ready fixes

```python
# skills/evidence-check/scripts/evidence_check.py, suite_record, in place of
#     if value.get("outcome") == "passed" and "wasxfail" not in value:
#         category = "passed" if category else ""
            outcome = value.get("outcome")
            if outcome == "passed" and "wasxfail" not in value:
                category = "passed" if category else ""
            # A report pytest leaves off its summary line is written `""`
            # (`count_towards_summary` false: a subtest's, under pytest 9's
            # default verbosity), and its outcome still says what it was: a
            # skip, an xfail or a failure is not the passed phase `""` stands
            # for in `observed` (round 4, 🟡 1).
            elif category == "" and outcome in ("failed", "skipped"):
                category = "xfailed" if "wasxfail" in value else outcome
```
```python
# tests/test_a_ledger_row_is_held_by_its_test.py, record_suite takes the
# verbosity, defaulting to what it runs today:
def record_suite(project, records, verbosity=("-q",)):
    ...
            # The verbosity a row commonly carries, and this repository's
            # (`bin/test -q`): on pytest 9 it is what makes a passed subtest
            # a counted report (round 3, 🟡 2).
            *verbosity,
            "tests",


# before test_a_test_whose_subtests_all_passed_is_held:
MARKED_SUBTESTS = (
    "import pytest\n"
    "import unittest\n"
    "\n"
    "class TestSkip(unittest.TestCase):\n"
    "    def test_each(self):\n"
    "        for i in range(2):\n"
    "            with self.subTest(i=i):\n"
    "                if i:\n"
    "                    self.skipTest('not here')\n"
    "\n"
    "def test_xfail(subtests):\n"
    "    with subtests.test(i=0):\n"
    "        pytest.xfail('known')\n"
)


@pytest.mark.parametrize("verbosity", [(), ("-q",)], ids=["default", "-q"])
@pytest.mark.parametrize(
    "node, seen",
    [
        ("tests/test_marked.py::TestSkip", "skipped"),
        ("tests/test_marked.py::test_xfail", "xfailed"),
    ],
    ids=["a skipped subtest", "an xfailed subtest"],
)
def test_a_marked_subtest_is_refused_at_every_verbosity(
    tmp_path, script, verbosity, node, seen
):
    """Round 4, 🟡 1: under pytest 9's default verbosity a skipped or
    xfailed subtest is written with the category `""` -- it is left off the
    summary line -- and its outcome says what it was. It is refused there as
    it is under `-q`. Red before the fix at default: held."""
    if int(pytest.__version__.split(".")[0]) < 9:
        pytest.skip("below pytest 9 a subtest writes no report of its own")
    project = tmp_path / "proj"
    (project / "tests").mkdir(parents=True)
    (project / "tests" / "test_marked.py").write_text(MARKED_SUBTESTS, encoding="utf-8")
    records = tmp_path / "records"
    record_suite(project, records, verbosity)
    out = observe((project, records), script, [held(f"`{node}`")])
    assert findings(out.stdout) == [
        ("MALFORMED", node, f"{seen} in the recorded suite{UNHELD}")
    ], out.stdout
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` over the eight guard modules the prompt named, in the clone at the head | 437 passed, exit 0 |
| The ledger's cited test tokens, collected from `evidence_check`'s own reader in process, run through `bin/test -q` with the gate's `recording_env`, then `evidence_check.py --strict --suite-record … --suite-key … .` | 66 tokens in 7 files; pytest 182 passed, exit 0; checker exit 0, `total: 7875 ok · 0 drifted · 0 broken · 0 external · 0 old-format · 0 malformed · 0 overflow`, no existence line; with no record, the same total and exit 0 |
| `bin/test tests/test_a_ledger_row_is_held_by_its_test.py -p no:xdist -k …` (the new cases and their neighbours) and `bin/test tests/test_the_seal_is_taken_once_by_the_sealer.py -k "existence_alone or ledger_arm_reads_the_run"` at the head | 36 passed; 3 passed |
| The same new cases with `evidence_check.py` and `broad_gate.py` checked out at fa199d96 | 6 failed (both IDS cases and the subtests case, each under plugin and vendored); the gate case failed |
| Subtests and case-id probe: pytest 9.1.1, a scratch project recorded under the gate's environment at default, `-q` and `-v`, eight rows each | see the block below |
| 🟡 1's proposed case at the head, then with the proposed fix | head: 4 failed (default), 4 passed (`-q`); fixed: `tests/test_a_ledger_row_is_held_by_its_test.py` 140 passed. `ruff` is not installed in the runner's venv or on PATH, so the fence is not linted |
| ⬜ 2's mutations of the guard at `skills/verify/scripts/broad_gate.py:3583`, with the cited case and the module's preflight cases | `if at >= 0:`: cited case 1 passed, preflight cases 15 passed; `if head is not None:`: cited case 1 passed |
| `gh pr checks 887 --repo MichaelYcJo/SpecSeal` | lint, ledger, release, arm-check-grammar 3.13 and 3.14 pass; all nine pytest legs pending |
| The full suite (the broad gate) | not yet run, by anyone in this round |

```
row                                       default            -q / -v
TestU::test_one_fails   (subTest fails)   failed             failed
TestU::test_one_skips   (subTest skips)   OK                 skipped
test_fixture_fails      (fixture fails)   failed             failed
test_fixture_xfail      (fixture xfails)  OK                 xfailed
test_brk   ids a[b, x]::y[z (2nd fails)   failed             failed
test_ok    ids [[::]]                     OK                 OK
TestK      (method id q[::r fails)        failed             failed
TestK::test_m                             failed             failed

records at default verbosity, call phase:
  skipped subtest   outcome skipped  category ""   wasxfail no
  xfailed subtest   outcome skipped  category ""   wasxfail yes
  passed subtest    outcome passed   category ""   wasxfail no
  failed subtest    outcome failed   category failed
```

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `skills/evidence-check/scripts/evidence_check.py:1690` | round 1's 🔴 1 — fixed |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:2319` | round 1's 🟡 2 — fixed |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:2251` | round 1's 🟡 3 — fixed |
| round-1 | `skills/settle/scripts/fold_check.py:308` | round 1's ⬜ 4 — fixed |
| round-1 | `seal/ledger/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it.md:14` | round 1's ⬜ 5 — answered |
| round-1 | `seal/ledger/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it.md:15` | round 1's 🟢 — confirmed |
| round-1 | `seal/ledger/1791384156-config-rows-coordinates-and-headings-have-one-reader.md` | round 1's 🟢 — confirmed |
| round-1 | the head | round 1's ❓ — out of verified scope |
| round-1 | PR #887 | round 1's ❓ — out of verified scope |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:2387` | round 2's 🟡 1 — deferred |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:2413` | round 2's 🟡 2 — deferred |
| round-2 | `docs/the-evidence-ledger.md:256` | round 2's ⬜ 3 — deferred |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:1692` | round 2's 🟢 — confirmed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:2343` | round 2's 🟢 — confirmed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:2262` | round 2's 🟢 — confirmed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:2322` | round 2's 🟢 — confirmed |
| round-2 | `seal/ledger/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it.md:18` | round 2's 🟢 — confirmed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:2390` | round 2's ❓ — out of verified scope |
| round-3 | `skills/evidence-check/scripts/evidence_check.py:2416` | round 3's 🔴 1 — fixed |
| round-3 | `skills/evidence-check/scripts/evidence_check.py#observed` | round 3's 🟡 2 — fixed |
| round-3 | `skills/verify/scripts/broad_gate.py:3569` | round 3's 🟡 3 — fixed |
| round-3 | `tests/test_a_ledger_row_is_held_by_its_test.py:1066` | round 3's ⬜ 4 — fixed |
| round-3 | `skills/evidence-check/scripts/evidence_check.py:2334` | round 3's ⬜ 5 — fixed |
| round-3 | `docs/the-evidence-ledger.md:258` | round 3's ⬜ 6 — fixed |
| round-3 | `seal/specs/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it/spec.md:365` | round 3's ⬜ 7 — answered |
| round-3 | `docs/the-evidence-ledger.md:255` | round 3's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
