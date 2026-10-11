# 1791384153 — review round 3, the redesign's first finding round

Target `d6d614aa302b6e796be560bc16c7ddf3af28afc9`, the range `65f3b822..d6d614aa`
(phases 6–9). Reviewed in a `git clone --no-local` of the worktree at that SHA,
under this session's scratchpad. Rounds 1 and 2 were inherited for their
coordinates. The verdicts below are re-derived.

## How the findings relate

The reframe moved the verdict from reading the test file to reading the sealed
run's record. That is the right move, and round 2's three findings are answered
by it. It also creates a new place where a guess can hide: the step that matches
a record line to a ledger row. Two guesses survive there, and the gate swallows
the line that would show the third case.

```
record line ──(match by node id)──> row ──(held rule)──> OK / MALFORMED
                 🔴 1: `::` in a case id         🟡 2: `passed` is the only word
                 splits the id wrongly           that counts as a pass

no record at all ──> existence only ──> the checker says so ──> 🟡 3: the gate
                                                                 does not show it
```

- 🔴 1 is the one that blocks. This branch's own ledger cites two parametrised
  tests whose case ids contain `::`. Against the record of a real run, both
  read *not run*, so the sealer's ledger arm will exit 2 on this branch.
- ⬜ 4 is why two pytest legs of PR #887 are red right now. A new case is dated
  `2026-10-12`, and CI ran while UTC was still on the 11th.

## 🔴 1 — a case id holding `::` is read as another unit's, so a failing case can hold its row

`suite_record` splits the whole node id on `::` and then strips `[…]` from the
last part (`skills/evidence-check/scripts/evidence_check.py:2416`). pytest
writes a parametrised case's id into the node id verbatim, `::` included.
`test_x[a::b]` therefore splits into `test_x[a` and `b]`, and the regex does
not match `b]`. That line is filed under a unit nobody can cite.

There are two consequences, and both were executed.

- **A failing case is dropped, and the row holds.** In a scratch project, a
  function whose cases are `ok` (passes) and `bad::x` (fails) read `OK`, exit 0.
  A method case with the id `x::y` that failed did the same: its class read
  `failed`, but the method's own row read `OK`. That is an `OK` for a claim the
  run refused, which is exactly what the reframe exists to stop.
- **A test whose every case id holds `::` reads *not run*.** This branch's
  ledger cites
  `tests/test_a_ledger_row_is_held_by_its_test.py::test_a_token_that_is_no_node_id_is_malformed`
  and `tests/test_the_seal_is_taken_once_by_the_sealer.py::test_the_ledger_arm_reads_the_run_it_seals`.
  Both are parametrised over node-id strings, so every case id holds `::`. I
  ran the ledger's 63 cited test tokens under the recorder (173 passed) and read
  the ledger against that record. The result was exit 2 with exactly these two
  rows `MALFORMED`, *not run in the recorded suite*. The sealer's full run
  produces the same node ids, so its ledger arm will refuse this branch.

The smith's `evidence-check --strict .` (7,872 ok) was read without a record, so
it could not see this. Every case in the new module uses ids without `::`.

The fix cuts the id before splitting the names. No `def` or `class` name
contains `[`, so the first `[` after the file is where the id begins. With the
fix, the same record reads the tree exit 0 and 0 malformed, and the scratch
cases read as pytest ran them. The proposed case was red before the fix (four
failed) and green after.

There is an alternative at a deeper level. The recorder could write the unit's
names itself, from the node chain, through the same report attribute it already
uses for the path. Then the reader would parse nothing of pytest's node-id
spelling. The minimal fix is enough because a test row can only cite a `def`
or `class`, but the orchestrator may prefer the deeper one.

## 🟡 2 — a test whose subtests all pass is refused, depending on the row's verbosity

`observed` holds a test only when its categories, less `""`, are exactly
`{"passed"}` (`skills/evidence-check/scripts/evidence_check.py#observed`). That
treats one word as the only word for a pass. pytest 9's built-in subtests (the
`subtests` fixture and `unittest`'s `subTest`) write each passing subtest as a
report of its own. Under `-q` or `-v` that report's category is
`subtests passed`. At the default verbosity it is `""`. This was executed on
pytest 9.1.1, the suite's own build.

The result is that a test whose subtests all pass reads `MALFORMED`, *subtests
passed in the recorded suite*, exit 2, but only when the row carries `-q`.
This repository's row is `bin/test -q`. The same test reads `OK` without the
flag. A verdict that turns on a verbosity flag is still a prediction, made at
the level of words rather than marks.

No row in the tree cites a subtest test today, so nothing in this branch is red
from it. The release would still ship a checker that refuses a passing test.

The fix reads what pytest itself decided. Where a line's `outcome` is `passed`
and it carries no `wasxfail`, it counts as a pass whatever its category says.
An `xpassed` line carries `wasxfail` and stays refused. A strict xpass has the
outcome `failed`. A failing subtest has the outcome `failed`. With the fix,
the module's S16 cases (`xpassed` among them) stay green. The proposed case was
red before the fix and green after, with `-q` added to `record_suite`. The
documents' "every line … says `passed`" sentence needs the same change in the
same commit (§14).

## 🟡 3 — a seal over existence alone says nothing on screen

`gate` hands `--suite-record` and the head key whenever the suite ran
(`skills/verify/scripts/broad_gate.py:3569`). `read_record` never returns None,
so this happens even when no pytest claimed the key: a row that replaces
`PYTEST_ADDOPTS`, `tox`, `env -i`. The checker then reads test rows for
existence alone, exits 0, and prints its one line. That line only reaches the
kept `ledger.txt`. The sealed panel shows `ledger ✓ N ok` and the suite row
`exit 0`. `NO_RECORD_HERE` and the `new?` wording are written only by
`failure_lines`, which runs on a failure.

This was executed with the proposed case: a row of `PYTEST_ADDOPTS=-q` plus the
suite runner, one test row. The gate exited 0, sealed, and its stderr carried
no line about existence. The spec's limit says "the gate's own `new?` wording
already tells the sealer the row is unmeasured" (`spec.md:365`, and `:272`).
That is true only when the suite fails.

The fix forwards the checker's line to stderr when a suite ran. It edits
`broad_gate.py#gate` again, so the 86 rows phase 9 re-read on that unit drift
once more. That cost belongs in the fix's commit.

## ⬜ 4 — the two red pytest legs are one case dated in UTC's future

`gh pr checks 887`: `pytest (ubuntu-latest …)` and `pytest (macos-latest …
--group 1 …)` fail, each with `1 failed` on
`tests/test_a_ledger_row_is_held_by_its_test.py::test_reverify_names_what_the_record_refuses_and_writes_nothing`.
The cause is `--checked 2026-10-12 is later than today, 2026-10-11`. The case
passes `--checked 2026-10-12` at lines 1066 and 1079, and the checker refuses a
reading dated after today. The case passed in the clone because local time
there was already the 12th.

The failure clears by itself once UTC reaches the 12th, so the release does not
ship it, which is why this is ⬜. A re-run of those two legs after 00:00 UTC
answers it. Dating the case like its neighbours (`2026-10-08`) removes the race
for good.

## ⬜ 5 — the reader's comment names a field it does not read

The comment above `SUITE_RECORD_OPTION` says four fields are read, `when` among
them (`skills/evidence-check/scripts/evidence_check.py:2334`). `suite_record`
reads three. The overview's divergence row records the drop of `when`, but the
comment was not updated. 🟡 2's fix reads `outcome` and `wasxfail`, so the
comment changes either way.

## ⬜ 6 — the platform consequence is in the spec and not in the documents

Asked: does a test a CI leg skips by platform turn a legitimate seal red?

- **CI legs do not.** They hand no record (Q7, built on its default (a)), so
  they read existence alone.
- **The sealer's platform does.** A test skipped there reads `skipped` and the
  ledger arm refuses it. This was executed: a `skipif` true on darwin read
  `MALFORMED`, *skipped*.
- **Nothing in this tree is affected today.** The recorded run held 61 of the
  63 cited tokens on macOS, and the two refusals are 🔴 1. The one
  platform-conditioned test in a cited module
  (`tests/test_the_seal_is_taken_once_by_the_sealer.py:1535`, skipped on
  Windows) is not cited.
- **Where it is stated.** `spec.md` §limits says so, and gives the remedy:
  write a hashed row, or seal where the test runs.
  `docs/the-evidence-ledger.md:258` and `templates/ledger.md:72` say a skipped
  test is refused, but neither says that the sealer's platform decides it. The
  spec leaves the tree at settle time, and the sentence goes with it.

## Answers to the prompt's other questions

- **Still predicted rather than observed or owned:** 🔴 1 (the node-id parse)
  and 🟡 2 (which word means a pass). Existence is owned and stated: a `def` or
  `class` defined once. Two consequences of that choice are stated and not
  findings. A test inherited from a base class in another module reads
  `BROKEN`. So does a test defined once under each branch of an `if`.
- **Matching:**
  - Path normalisation holds. `./tests/…`, a symlinked directory and pytest's
    rootdir set inside `tests/` all matched.
  - A class owns its methods.
  - A test collected twice holds only if both runs passed it. A second pytest
    under the same key that failed it gave `failed`.
  - A parametrised id holds, except for 🔴 1.
- **Is the record the run it sealed:** yes. It is one directory, a key made
  fresh per run by `record_key`, and the same root. A file left there by
  another run carries another key and is passed over. A caller who passes an
  old key by hand gets that old run, because the record names no commit. Only
  `evidence-ci`'s new paragraph invites a hand-wired use, and it describes one
  job. No finding.
- **Existence-only path:** the checker says so in one line, printed once
  beside the totals (executed at the head). The gate does not repeat it
  (🟡 3).

## Round 2's findings

- 🟡 1 (an `xfail` by keyword or strict) is answered. The record decides it.
  `test_round_twos_spellings_are_what_pytest_did` covers `condition=False`
  (held) and strict (`failed`).
- 🟡 2 (a mark under an `if`, `pytestmark +=`) is answered. Both read
  `skipped` off the record.
- ⬜ 3 (the documents over-promise) is answered for the sentences it named. The
  new statement 2 says what the checker reads. 🟡 3 is a different gap, in the
  gate.
- Round 2's ❓ (a module-level skip call) is closed: *not run*, pinned by the
  `a module skipped at collection` case.

## Regression tests to plant

- `tests/test_a_ledger_row_is_held_by_its_test.py`: the planted `IDS` and
  `SUBTESTS` modules, `-q` in `record_suite`, and the two cases in the fences
  below. Each was seen red against the head checker and green with the fix.
- `tests/test_the_seal_is_taken_once_by_the_sealer.py`: the gate case in the
  fences below. It was seen red against the head gate and green with the fix.

## Facts for the evidence ledger

- The record's node id carries a case id verbatim, `::` included (pytest
  9.1.1, executed).
- pytest 9.1.1 writes a passing subtest as a report with the outcome `passed`.
  Its category is `subtests passed` under `-q` and `-v`, and `""` at the
  default verbosity (executed).
- The gate's sealed panel carries no line from the ledger arm beyond its
  totals (`skills/verify/scripts/broad_gate.py#ledger_counts`, read).

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | A case id holding `::` is split as names: a failing case is dropped and its row holds, and a test whose every case id holds `::` reads *not run*; this branch's two such rows refuse its own seal | `skills/evidence-check/scripts/evidence_check.py:2416` | open | executed: the ledger's 63 cited tokens run under the recorder, then `--strict` with that record, exit 2 with exactly these two rows; matching probe, `bad::x` failing read `OK`; the fix gives exit 0, and the proposed case went red, then green |
| 🟡 2 | A test whose subtests all pass reads `MALFORMED`, *subtests passed*, under `-q` (this repository's row) and `OK` without it | `skills/evidence-check/scripts/evidence_check.py#observed` | open | executed on pytest 9.1.1: the subtests probe at three verbosities; the proposed case went red, then green; no row in the tree cites a subtest test today |
| 🟡 3 | Where the row loads no recorder, the gate seals over test rows read for existence alone, and nothing on screen says so; the spec's "`new?` already tells the sealer" holds only on a failure | `skills/verify/scripts/broad_gate.py:3569` | open | executed: proposed case, a row replacing `PYTEST_ADDOPTS`, exit 0 and no line in stderr before the fix, the line present after |
| ⬜ 4 | The two red pytest legs of PR #887 are one case passing `--checked 2026-10-12` while UTC was on the 11th | `tests/test_a_ledger_row_is_held_by_its_test.py:1066` | open | executed: `gh pr checks 887` and both jobs' logs; clears itself after 00:00 UTC on 2026-10-12, so no release defect |
| ⬜ 5 | The reader's comment says four fields are read, `when` among them; three are | `skills/evidence-check/scripts/evidence_check.py:2334` | open | read |
| ⬜ 6 | That the sealer's platform decides a skipped test is in `spec.md` §limits and not in the documents or the template | `docs/the-evidence-ledger.md:258` | open | read; executed, matching probe: a `skipif` true on darwin read `MALFORMED`; no cited test is skipped on macOS today |
| ⬜ 7 | `spec.md` says the gate's `new?` wording tells the sealer a row is unmeasured; on a passing run nothing does | `seal/specs/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it/spec.md:365` | open | read; a correction to the run's paperwork, with `spec.md:272`, outside `Needs a fix` |
| 🟢 | round 2's finding 1 is closed — an `xfail` by keyword or strict is decided by the record, not by the file | `skills/evidence-check/scripts/evidence_check.py#observed` | confirmed | executed: the module at the head, 124 passed, `test_round_twos_spellings_are_what_pytest_did` among them |
| 🟢 | round 2's finding 2 is closed — a mark under an `if` and `pytestmark +=` read `skipped` off the record | `skills/evidence-check/scripts/evidence_check.py#observed` | confirmed | executed: same run |
| 🟢 | round 2's finding 3 is closed — the documents say the checker reads existence and the record says whether the test passed | `docs/the-evidence-ledger.md:255` | confirmed | read at the head; the gate's gap is 🟡 3 |
| 🟢 | round 2's open question is closed — a module-level skip call reads *not run* | `skills/evidence-check/scripts/evidence_check.py#observed` | confirmed | executed: the `a module skipped at collection` case in the same run |
| ❓ | The full suite, the repository-wide lint and the typecheck at the head | the head | ❓ out of verified scope | the broad gate; the sealer answers it after the rounds settle. 🔴 1 predicts its ledger arm exits 2 |
| ❓ | The Windows pytest legs of PR #887 | PR #887 | ❓ out of verified scope | pending when read; CI answers it |

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

### Matching probe, at the head

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

### Subtests probe, pytest 9.1.1

```
verbosity default: categories "" x4, passed x1
verbosity -q:      categories "" x2, passed x1, "subtests passed" x2
verbosity -v:      categories "" x2, passed x1, "subtests passed" x2
under -q, at the head:
tests/test_s.py::test_fixture     exit=2 MALFORMED  subtests passed in the recorded suite
tests/test_s.py::TestU::test_sub  exit=2 MALFORMED  subtests passed in the recorded suite
with 🟡 2's fix: both OK
```

## Paste-ready fixes

### 🔴 1 and 🟡 2 — `suite_record`

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

### 🟡 3 — the gate repeats the existence line

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

### ⬜ 4 — date the case in the past

```python
# tests/test_a_ledger_row_is_held_by_its_test.py,
# test_reverify_names_what_the_record_refuses_and_writes_nothing, both calls:
    out = run(["--reverify", "--checked", "2026-10-08", *record, "."], project)
            ["--reverify", "--into", FRAGMENT, "--checked", "2026-10-08", *record, "."],
```

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

Needs a fix: yes — 🔴 1 (a case id holding `::` is split as names, so a failing case holds its row and this branch's two such rows refuse its own seal), 🟡 2 (a test whose subtests all pass is refused under `-q`), 🟡 3 (a seal over existence alone says nothing on screen)
Loses a record or crashes: no

## Proof block

Files opened in this round, in the clone at `d6d614aa` unless named:
`rounds/round-1.md` (its head), `rounds/round-2.md`; `spec.md` D9, D10 and
§limits; `plan.md` and `questions.md` (the diff); `overview.md` lines 30–60;
`skills/evidence-check/scripts/evidence_check.py`: the diff, `place`,
`node_finding`, `held_by_tests`, `suite_record`, `observed`, `existence_line`,
`main`'s two options; `skills/verify/scripts/broad_gate.py`: the diff,
`record_key`, `records_dir`, `recording_env`, `RunRecord`, `record_path`,
`read_record`, `base_word`, `suite_counts`, `ledger_counts`, `ledger_total`,
`failure_lines`' tail, `panel`'s ledger rows, `gate` from the base resolution
to the drawing; `skills/verify/scripts/pytest_record/specseal_pytest_record.py`;
the diffs of `docs/the-evidence-ledger.md`, `skills/evidence-check/SKILL.md`,
`skills/evidence-ci/SKILL.md`, `templates/ledger.md`,
`tests/test_the_lenient_run_says_what_the_broad_gate_will_say.py` and
`tests/test_the_seal_is_taken_once_by_the_sealer.py`;
`tests/test_a_ledger_row_is_held_by_its_test.py` lines 1–140 and 560–1100;
`tests/test_the_seal_is_taken_once_by_the_sealer.py`'s `config`, `set_row`,
`run_gate` and `repo`; `bin/test`; `seal/config.md`'s `Broad gate` row;
the logs of PR #887's ubuntu and macOS group 1 jobs.
