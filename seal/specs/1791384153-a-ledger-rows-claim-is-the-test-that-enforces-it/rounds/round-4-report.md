# 1791384153 — review round 4 (verifying round 3's fixes)

Target SHA `7147e5f61e8919077bbbd383e5e3aa1cc69b83db`. The target is the
diff of round 3's fixes, `fa199d96..1cc634a7` (2411821b, 1cc634a7), plus the
table and close commits 1973c1a0 and 7147e5f6. Round 3's seven verdicts are
answered below, and its `New units` were judged as code. Everything was run
in a `git clone --no-local` at the target, under
`<scratchpad>/1791384153/round-4/clone`, and that directory is gone.

## What this round found, in order of cause

1. Round 3's three fixes hold. Each new case is red at fa199d96 and green at
   the head (executed). The ledger's 66 cited test tokens, recorded and read
   back, seal clean (executed).
2. Round 3's 🟡 2 closed one direction of a verbosity-dependent verdict. The
   other direction is still open: under pytest 9's default verbosity, a
   skipped or xfailed subtest holds its row. That is 🟡 1 below.
3. The ledger row for the gate's new line claims a clause no case enforces.
   That is ⬜ 2, a correction to the run's paperwork.
4. The line the gate now prints ends in advice that reads oddly when the gate
   is the one printing it. That is ⬜ 3.

## The answers the prompt asked for

**Cutting at the first `[` is right, including for a case id that holds `[`
itself.** A def or class name in a row is `[A-Za-z_][A-Za-z0-9_]*`
(`skills/evidence-check/scripts/evidence_check.py:2236`), so no name holds `[`, and pytest opens the case
id with the first `[` after the names. The cut takes the path off at the
first `::` before looking for `[`, so a `[` in a directory name cannot move
it. Executed, at the head:

- `ids=['a[b', 'x]::y[z']`, with the second case failing, read *failed*.
- `ids=['[[::]]']`, passing, read `OK`.
- A method under `TestK` with `ids=['q[::r']`, failing, read *failed* both
  when the row cites the class and when it cites the method.

No other reader in `skills/`, `hooks/` or `.github/scripts/` splits a
recorded node id. `skills/settle/scripts/fold_check.py:287` splits a ledger cell's target, which
the row grammar already limits.

**The `outcome`/`wasxfail` rule stays true for a failing subtest.** A
failing subtest is written with `outcome` `failed` and the category
`failed`. The new branch only rewrites `outcome == "passed"`, so it never
reaches that report. Executed on pytest 9.1.1, with both `subTest` and the
`subtests` fixture, at default, `-q` and `-v`: every failing-subtest row
read `MALFORMED`, *failed*. **The rule does not cover the neighbouring
case, though.** A skipped or xfailed subtest at default verbosity reads
`OK` (🟡 1).

**The existence-line search cannot miss or double-print** (read).

- The checker prints the line once, on its own line of stdout, after
  `total:` (`skills/evidence-check/scripts/evidence_check.py:6643`).
- `run` hands back all of stdout and stderr, decoded with universal
  newlines (`skills/verify/scripts/broad_gate.py:1493`). Nothing truncates it the way
  `first_lines` truncates the failure form.
- `find` takes the first match and the gate writes once.
- Every finding line the checker prints is indented, so a quoted claim
  cannot start a line with the phrase.
- If the checker rewords the line, the gate's case fails rather than going
  quiet, because it runs the real checker and asserts the gate's own line.

## 🟡 1 — a skipped or xfailed subtest holds its row at pytest's default verbosity

`skills/evidence-check/scripts/evidence_check.py:2421`

Round 3's 🟡 2 found that a test's verdict depended on the row's verbosity:
a test whose subtests all passed was refused under `-q` and held without
it. The fix made a passed outcome read as a pass, so `-q` now agrees with
the default. The same dependency runs the other way, and the fix did not
reach it.

At pytest 9's default verbosity, the recorder writes a skipped or xfailed
subtest with the category `""`, because pytest sets `count_towards_summary`
false on it. Its `outcome` still says `skipped`, and the xfailed one carries
`wasxfail`. `observed` drops `""` as *a passed setup or teardown*, and the
parent's call report is `passed`. So the row holds. Under `-q` or `-v` the
same subtest is counted as `skipped` or `xfailed` and the row is refused.

Executed on pytest 9.1.1, recorded the way the gate records:

| Row | default | `-q` | `-v` |
|---|---|---|---|
| `subTest` with one case calling `skipTest` | `OK` | *skipped* | *skipped* |
| `subtests` fixture with one case calling `pytest.xfail` | `OK` | *xfailed* | *xfailed* |
| either kind with one failing case | *failed* | *failed* | *failed* |

Why it matters:

- `docs/the-evidence-ledger.md:262` says a mark in any spelling is a line
  that is not `passed`.
- `templates/ledger.md:72` says `broad-gate` refuses a row where the run
  skipped or xfailed its test.
- A repository whose row is plain `pytest` gets a seal over a test that did
  not do all its work. The same tree under `-q` gets a refusal.

This tree is not affected today, because its row is `bin/test -q` and no
cited test uses subtests. The fix keeps the round-3 rule and reads the
`outcome` wherever the category is `""`. I applied it in the clone. With
the fix, the proposed case (default × `-q`, skip × xfail, plugin ×
vendored: 8 cases) is 4 red at the head and 8 green. The whole module
passed (140 passed). The fence below holds both. The changelog fragment, the
docs sentence and T25 will each want a clause on it.

## ⬜ 2 — T26 claims a preflight prints no line, and its cited case does not enforce it

`seal/ledger/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it.md:23`

T26's claim ends *and a preflight prints none*. Its only test,
`tests/test_the_seal_is_taken_once_by_the_sealer.py::test_a_seal_over_existence_alone_says_so`,
never runs a preflight. Its grounds also say the case went *red through
`bin/mutation-check` … with its guard removed*. I mutated the guard in the
clone both ways, and each time the cited case stayed green (executed):

- `if head is not None and at >= 0:` became `if at >= 0:`, and the cited
  case passed. The module's 15 preflight cases also passed, because none of
  their fixtures carries a test row.
- `if head is not None and at >= 0:` became `if head is not None:`, and
  the cited case passed.

The behaviour is right by reading: `head` is None on a preflight
(`skills/verify/scripts/broad_gate.py:3559`). The row overstates what its test holds, on this
work item's own subject. Either plant a preflight case over a ledger
holding a test row that asserts the gate's line is absent, or take the
clause out of T26 and say which mutation went red. This goes outside
`Needs a fix`, because the coordinate is the run's paperwork.

## ⬜ 3 — the gate's new line ends by telling the reader that broad-gate hands over the record

`skills/verify/scripts/broad_gate.py:3585`

The gate repeats the checker's line verbatim. That line comes from
`evidence_check.py#existence_line` and ends *— `broad-gate` hands this
check the sealed run's record*. Printed by the checker alone, that is a
pointer. Printed by `broad-gate` right after it handed a record over, it
names neither the cause nor the remedy. The cause is that the row replaced
`PYTEST_ADDOPTS` or `PYTHONPATH`, or ran no pytest. The remedy is in
`templates/config.md` rule 3. The behaviour is right and the fact is right,
so this is ⬜. A tail chosen by caller, or the gate printing only up to the
`—`, would read better.

## Round 3's verdicts, one by one

- **🔴 1, fixed.** The cut is at `skills/evidence-check/scripts/evidence_check.py:2426`. The two IDS cases
  are red at fa199d96 (4 failed across plugin and vendored) and green at the
  head. The 66-token record seals clean (executed).
- **🟡 2, fixed** for the direction it named (executed: two cases red, then
  green). Its other direction is 🟡 1 above.
- **🟡 3, fixed.** The case is red at fa199d96 and green at the head
  (executed). The search is sound (read, above). T26's extra clause is ⬜ 2.
- **⬜ 4, fixed.** Both `--checked` dates are now `2026-10-08`. No other test
  in the tree passes a date after 2026-10-12 to a reader that refuses one.
  The row at `tests/test_the_seal_is_taken_once_by_the_sealer.py:3910` is
  dated `2026-10-12` and ran green on ubuntu on the 11th in round 3's CI, so
  row dates are not refused. CI for this head is still pending (❓).
- **⬜ 5, fixed** (read). `when` is no longer named, and the five fields
  listed are the five read.
- **⬜ 6, fixed** (read). `docs/the-evidence-ledger.md:267` now says the run
  that is sealed decides a skipped test. `templates/ledger.md:72` was not
  touched. Its *the run it seals* already carries the point, so I take the
  finding as closed.
- **⬜ 7, answered** (read). Both spec sentences now say the gate prints the
  line on its own output, which is what 2411821b does.

`New units`, judged as code:

- `EXISTENCE_ALONE` is correct. A reword in the checker turns the gate's
  case red, because the case runs the real checker.
- `IDS` and `SUBTESTS` are correct fixtures. Adding `-q` to `record_suite`
  is what makes `SUBTESTS` exercise the fix.
- The three cases are each red before the fix (executed).
- The one gap among the new units is ⬜ 2.

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

## Paste-ready fixes

### 🟡 1

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

## Regression tests to plant

- `tests/test_a_ledger_row_is_held_by_its_test.py`: 🟡 1's case above. Seen
  red at the head (4 failed at default), green with the fix.
- `tests/test_the_seal_is_taken_once_by_the_sealer.py`: a preflight over a
  ledger holding a test row, asserting the gate prints no
  `broad-gate: ledger: test rows were read for existence alone` line (⬜ 2),
  or T26 loses that clause.

## Facts for the evidence ledger

- With 🟡 1 fixed, T25's claim gains a clause: a report written `""` whose
  `outcome` is `skipped` or `failed` reads as that outcome, `xfailed` where
  it carries `wasxfail`. Its test is 🟡 1's case.
- T26: see ⬜ 2.

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

Needs a fix: yes — 🟡 1 (a skipped or xfailed subtest holds its row at pytest 9's default verbosity)
Loses a record or crashes: no

## Proof block

Files opened this round, at the target or in the clone at it:
`seal/specs/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it/rounds/round-3.md`,
`rounds/round-3-fixes.md`, `rounds/round-3-report.md` (§⬜ 6 and its
verdict table), `skills/evidence-check/scripts/evidence_check.py`
(2234–2240, 2331–2500, 6630–6660),
`skills/verify/scripts/broad_gate.py` (1458–1510, 1875–1912, 2026–2135,
3168–3175, 3530–3600),
`skills/verify/scripts/pytest_record/specseal_pytest_record.py` (296–333),
`tests/test_a_ledger_row_is_held_by_its_test.py` (57–121, 610–860,
950–985, 1120–1145), `tests/test_the_seal_is_taken_once_by_the_sealer.py`
(3900–3950), `templates/ledger.md` (66–80), `docs/the-evidence-ledger.md`
(255–275), `seal/ledger/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it.md`
(T25, T26), the 1791384158 ledger fragment (N2, W10 and the re-stamp diff),
`bin/test`, the diffs of 2411821b, 1cc634a7, 1973c1a0 and 7147e5f6.
Facts carried rather than re-established: none. Every round-3 verdict was
re-derived at this head.
