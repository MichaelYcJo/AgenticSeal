# 1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it — review round 3

| Field | Value |
|---|---|
| Target SHA | d6d614aa302b6e796be560bc16c7ddf3af28afc9 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 887 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `fa199d969cf56b57cda09e5793c258f5d9f80a2f..1cc634a7bfc26df55036654427c5868d2eaac20c`, 2 commits |
| Contract changes | none |
| New units | EXISTENCE_ALONE (depth 1); IDS (depth 1); SUBTESTS (depth 1); test_a_case_id_holding_the_separator_is_its_functions (depth 1); test_a_test_whose_subtests_all_passed_is_held (depth 1); test_a_seal_over_existence_alone_says_so (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🔴 1 (a case id holding `::` is split as names, so a failing case holds its row and this branch's two such rows refuse its own seal), 🟡 2 (a test whose subtests all pass is refused under `-q`), 🟡 3 (a seal over existence alone says nothing on screen) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 3, the redesign's first finding round after the owner reframed the collection half on 2026-10-12 against 0.21.0's theme. Its target is 65f3b822..d6d614aa, phases 6 to 9: existence-only static reading, the recorder-record reader, the gate handing the record, and the records. Rounds 1 and 2 were inherited, and round 2's three deferred findings were the agenda. The spawn named five things to judge. First, whether anything is still predicted. Second, how a test's record lines are matched to its row: path normalisation, parametrised ids, classes and double collection. Third, whether a platform skipif turns a legitimate seal red. Fourth, whether the record is the sealed run's. Fifth, whether the existence-only path says so. It also ran the eight guard modules once. Facts arrived labelled. Read from the smith: the removals, the reader, the gate wiring, Q7 at its default, 7,872 ok with no record, and 615 passed.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | A case id holding `::` is split as names: a failing case is dropped and its row holds, and a test whose every case id holds `::` reads *not run*; this branch's two such rows refuse its own seal | `skills/evidence-check/scripts/evidence_check.py:2416` | **fixed** `2411821b` | fixed at 2411821b; executed: the ledger's 63 cited tokens run under the recorder, then `--strict` with that record, exit 2 with exactly these two rows; matching probe, `bad::x` failing read `OK`; the fix gives exit 0, and the proposed case went red, then green |
| 🟡 2 | A test whose subtests all pass reads `MALFORMED`, *subtests passed*, under `-q` (this repository's row) and `OK` without it | `skills/evidence-check/scripts/evidence_check.py#observed` | **fixed** `2411821b` | fixed at 2411821b; executed on pytest 9.1.1: the subtests probe at three verbosities; the proposed case went red, then green; no row in the tree cites a subtest test today |
| 🟡 3 | Where the row loads no recorder, the gate seals over test rows read for existence alone, and nothing on screen says so; the spec's "`new?` already tells the sealer" holds only on a failure | `skills/verify/scripts/broad_gate.py:3569` | **fixed** `2411821b` | fixed at 2411821b; executed: proposed case, a row replacing `PYTEST_ADDOPTS`, exit 0 and no line in stderr before the fix, the line present after |
| ⬜ 4 | The two red pytest legs of PR #887 are one case passing `--checked 2026-10-12` while UTC was on the 11th | `tests/test_a_ledger_row_is_held_by_its_test.py:1066` | **fixed** `2411821b` | fixed at 2411821b; executed: `gh pr checks 887` and both jobs' logs; clears itself after 00:00 UTC on 2026-10-12, so no release defect |
| ⬜ 5 | The reader's comment says four fields are read, `when` among them; three are | `skills/evidence-check/scripts/evidence_check.py:2334` | **fixed** `2411821b` | fixed at 2411821b; read |
| ⬜ 6 | That the sealer's platform decides a skipped test is in `spec.md` §limits and not in the documents or the template | `docs/the-evidence-ledger.md:258` | **fixed** `2411821b` | fixed at 2411821b; read; executed, matching probe: a `skipif` true on darwin read `MALFORMED`; no cited test is skipped on macOS today |
| ⬜ 7 | `spec.md` says the gate's `new?` wording tells the sealer a row is unmeasured; on a passing run nothing does | `seal/specs/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it/spec.md:365` | answered | corrected at 2411821b; read; a correction to the run's paperwork, with `spec.md:272`, outside `Needs a fix` |
| 🟢 | round 2's finding 1 is closed — an `xfail` by keyword or strict is decided by the record, not by the file | `skills/evidence-check/scripts/evidence_check.py#observed` | confirmed | executed: the module at the head, 124 passed, `test_round_twos_spellings_are_what_pytest_did` among them |
| 🟢 | round 2's finding 2 is closed — a mark under an `if` and `pytestmark +=` read `skipped` off the record | `skills/evidence-check/scripts/evidence_check.py#observed` | confirmed | executed: same run |
| 🟢 | round 2's finding 3 is closed — the documents say the checker reads existence and the record says whether the test passed | `docs/the-evidence-ledger.md:255` | confirmed | read at the head; the gate's gap is 🟡 3 |
| 🟢 | round 2's open question is closed — a module-level skip call reads *not run* | `skills/evidence-check/scripts/evidence_check.py#observed` | confirmed | executed: the `a module skipped at collection` case in the same run |
| ❓ | The full suite, the repository-wide lint and the typecheck at the head | the head | ❓ out of verified scope | the broad gate; the sealer answers it after the rounds settle. 🔴 1 predicts its ledger arm exits 2 |
| ❓ | The Windows pytest legs of PR #887 | PR #887 | ❓ out of verified scope | pending when read; CI answers it |

## Paste-ready fixes

```python
# skills/evidence-check/scripts/evidence_check.py, suite_record, in place of
#     parts = nodeid.split(NODE_SEP)[1:]
#     parts[-1] = PARAMETRISED_RE.sub("", parts[-1])
# and delete the PARAMETRISED_RE constant, which then has no reader:
            # pytest's own outcome says the report passed and no xfail was
            # expected of it: a plugin's word for it (`subtests passed`,
            # which pytest 9 counts under `-q` and not without it) is a pass
            # (round 3, 🟡 2).
            if value.get("outcome") == "passed" and "wasxfail" not in value:
                category = "passed" if category else ""
            # A case id is written verbatim, `::` included, and no name of a
            # def or class holds `[`: the first `[` after the file begins
            # the id, so it is cut before the names split (round 3, 🔴 1).
            qualified = nodeid.partition(NODE_SEP)[2].partition("[")[0]
            parts = qualified.split(NODE_SEP)
```
```python
# skills/evidence-check/scripts/evidence_check.py, the comment above
# SUITE_RECORD_OPTION, in place of its "Four fields" sentence (⬜ 5):
# Five fields of a `test` line are read -- `path`, `nodeid`, `category`,
# `outcome` and whether it carries `wasxfail` -- so a field the recorder adds
# changes nothing here. `category` is the word pytest's own summary counts the
# report under, which the recorder asks of pytest; a report whose `outcome` is
# `passed` with no `wasxfail` is a pass whatever its word.
```
```python
# tests/test_a_ledger_row_is_held_by_its_test.py, before PLANTED:
# A case id is written verbatim into the node id, `::` included (round 3).
IDS = (
    "import pytest\n"
    "\n"
    "@pytest.mark.parametrize('v', [1, 2], ids=['ok', 'tests/x.py::y'])\n"
    "def test_mixed(v):\n"
    "    assert v == 1\n"
    "\n"
    "@pytest.mark.parametrize('v', [1], ids=['a::b'])\n"
    "def test_colon(v):\n"
    "    assert v == 1\n"
)
# Subtests that all pass; pytest 9 reports each under `subtests passed`
# (round 3). Below pytest 9 a `subTest` writes no report of its own.
SUBTESTS = (
    "import unittest\n"
    "\n"
    "class TestSub(unittest.TestCase):\n"
    "    def test_each(self):\n"
    "        for i in range(2):\n"
    "            with self.subTest(i=i):\n"
    "                self.assertTrue(True)\n"
)
# and in PLANTED:
    "test_ids.py": IDS,
    "test_subtests.py": SUBTESTS,

# record_suite, between "no:xdist" and "tests":
            # The verbosity a row commonly carries, and this repository's
            # (`bin/test -q`): on pytest 9 it is what makes a passed subtest
            # a counted report (round 3, 🟡 2).
            "-q",


# after test_a_class_and_a_parametrised_function_own_their_lines:
@pytest.mark.parametrize(
    "node, seen",
    [
        ("tests/test_ids.py::test_mixed", "failed"),
        ("tests/test_ids.py::test_colon", None),
    ],
    ids=["a failing case whose id holds ::", "every case id holds ::"],
)
def test_a_case_id_holding_the_separator_is_its_functions(suite, script, node, seen):
    """Round 3, 🔴 1: pytest writes a case id verbatim, so `::` inside the
    brackets is no separator. Red before the fix: the failing case was read
    as another unit's and the row held; the passing one read *not run*."""
    out = observe(suite, script, [held(f"`{node}`")])
    if seen is None:
        assert out.returncode == 0, out.stdout + out.stderr
        assert findings(out.stdout) == [], out.stdout
    else:
        assert findings(out.stdout) == [
            ("MALFORMED", node, f"{seen} in the recorded suite{UNHELD}")
        ], out.stdout


def test_a_test_whose_subtests_all_passed_is_held(suite, script):
    """Round 3, 🟡 2: a report pytest's own outcome calls passed, with no
    xfail expected of it, is a pass whatever word a plugin counts it under.
    Red before the fix on pytest 9: MALFORMED, *subtests passed*."""
    out = observe(suite, script, [held("`tests/test_subtests.py::TestSub`")])
    assert out.returncode == 0, out.stdout + out.stderr
    assert findings(out.stdout) == [], out.stdout
```
```python
# skills/verify/scripts/broad_gate.py, after EVIDENCE_KEY:
# How `evidence_check.py#existence_line` begins.
EXISTENCE_ALONE = "test rows were read for existence alone"

# gate, directly after checks[LEDGER] = run(...):
    # A row that left no session under the key leaves the arm reading test
    # rows for existence alone, and the panel's `ok` cannot say so: the
    # checker's own line goes beside the command line (round 3, 🟡 3).
    if head is not None:
        for line in checks[LEDGER].text.splitlines():
            if line.startswith(EXISTENCE_ALONE):
                sys.stderr.write(f"broad-gate: {LEDGER}: {line}\n")
```
```python
# tests/test_the_seal_is_taken_once_by_the_sealer.py, after
# test_the_ledger_arm_reads_the_run_it_seals:
def test_a_seal_over_existence_alone_says_so(repo):
    """Round 3, 🟡 3: a row that replaces `PYTEST_ADDOPTS` leaves no session
    under the key, so the ledger arm reads test rows for existence alone. The
    run still seals, and the checker's line reaches the person reading it.
    Red before the fix: the line was only in the kept `ledger.txt`."""
    write(
        repo,
        "seal/ledger/1799000000-a-sealed-work-item.md",
        "| T1 · the claim | `tests/test_one.py::test_one` | seen red, then "
        "green | 2026-10-08 | |\n",
    )
    commit(repo, "a ledger row held by a test")
    out = run_gate(set_row(repo, f"PYTEST_ADDOPTS=-q {SUITE_ROW}"))
    assert out.returncode == 0, f"exit {out.returncode}\n{out.stdout}\n{out.stderr}"
    assert "test rows were read for existence alone: no session under" in out.stderr, (
        out.stderr
    )
```
```python
# tests/test_a_ledger_row_is_held_by_its_test.py,
# test_reverify_names_what_the_record_refuses_and_writes_nothing, both calls:
    out = run(["--reverify", "--checked", "2026-10-08", *record, "."], project)
            ["--reverify", "--into", FRAGMENT, "--checked", "2026-10-08", *record, "."],
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` over the eight guard modules the prompt named, in the clone at the head | 437 passed, exit 0 |
| `bin/test tests/test_a_ledger_row_is_held_by_its_test.py tests/test_the_lenient_run_says_what_the_broad_gate_will_say.py` at the head | 143 passed |
| `bin/test tests/test_the_seal_is_taken_once_by_the_sealer.py -k ledger_arm_reads_the_run_it_seals` at the head | 2 passed |
| `evidence_check.py --strict .` at the head, no record | exit 0; `total: 7872 ok · 0 drifted · 0 broken`; the existence line once, after the totals |
| The ledger's 63 cited test tokens through `bin/test -q` with the recorder loaded, then `evidence_check.py --strict --suite-record … --suite-key … .` | pytest 173 passed, exit 0; checker exit 2, two `MALFORMED` *not run* (🔴 1's rows), the rest held |
| The same record with 🔴 1's fix in the clone | exit 0, 0 malformed |
| Matching probe: a scratch project recorded by two pytest runs under one key, ten rows read one at a time | see the first block below |
| Subtests probe: pytest 9.1.1, `subtests` fixture and `subTest`, at default, `-q` and `-v` | see the second block below |
| The three proposed cases, against the head code, then with the fixes | head: 6 failed (checker module), 1 failed (gate case); fixed: 149 passed over the two modules, 3 passed over the gate cases; `ruff check` and `ruff format --check` clean on the four files |
| `gh pr checks 887` and the two failing jobs' logs | lint, ledger, release, arm-check-grammar 3.13 and 3.14 pass; macOS groups 2 and 3 pass; ubuntu and macOS group 1 fail on ⬜ 4's case; four Windows legs pending |
| The full suite (the broad gate) | not yet run, by anyone in this round |

```
pytest 1 exit 1 3 failed, 6 passed, 1 skipped
pytest 2 exit 1 1 failed            (test_twice, failed on its second run)
tests/test_p.py::test_mixed       exit=0 OK            cases ok, bad::x (failed)
tests/test_p.py::test_all_colon   exit=2 MALFORMED     not run in the recorded suite
tests/test_p.py::TestC            exit=2 MALFORMED     failed
tests/test_p.py::TestC::test_m    exit=0 OK            cases fine, x::y (failed)
tests/test_p.py::test_bracket     exit=2 MALFORMED     failed (id "brk][")
tests/test_p.py::test_platform    exit=2 MALFORMED     skipped (skipif darwin)
tests/test_p.py::test_ok          exit=0 OK
./tests/test_p.py::test_ok        exit=0 OK
linked/test_p.py::test_ok         exit=0 OK            (a symlinked directory)
tests/test_twice.py::test_twice   exit=2 MALFORMED     failed
with 🔴 1's fix: test_mixed and TestC::test_m read failed; test_all_colon OK
```
```
verbosity default: categories "" x4, passed x1
verbosity -q:      categories "" x2, passed x1, "subtests passed" x2
verbosity -v:      categories "" x2, passed x1, "subtests passed" x2
under -q, at the head:
tests/test_s.py::test_fixture     exit=2 MALFORMED  subtests passed in the recorded suite
tests/test_s.py::TestU::test_sub  exit=2 MALFORMED  subtests passed in the recorded suite
with 🟡 2's fix: both OK
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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
