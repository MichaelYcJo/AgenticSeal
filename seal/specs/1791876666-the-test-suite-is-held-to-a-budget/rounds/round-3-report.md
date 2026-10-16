# 1791876666 — review round 3 (verifying), report

Target: `e90c90d3` on `chore/929-the-test-suite-only-grows` (PR #939),
against `origin/release/v0.22.0` at `642441fc` (#931's squash). Reviewed in a
`git clone --no-local` of the worktree at that SHA. Paths below are relative
to the repository root.

## How the findings relate

Round 2's 🟡 1 fix (`ec152145` on the rebased tree) did what it said. Every
skip spelling it lists is now named `not proved: … never ran`. To get there,
the tracer **drops the traced lines** of any call that ended in a skip. That
one move has two consequences, and they are this round's two findings.

- 🟡 1 — the drop is wider than the naming needs. A sibling that asserts and
  then skips its platform-only tail drops out of "who ran this line". The
  check then never runs it under a mutant. So a new case that sibling already
  covers is reported `proved — the only killer in its file`. Before the fix
  the same tree gave `kills nothing its file does not`, which is the right
  answer. This is a fix of a fix in a unit round 2's fixes changed.
- 🟡 2 — the drop is also narrower than the docstring says. The hook treats
  every call-phase skip that carries `wasxfail` as "an expected failure that
  ran its body". An imperative `pytest.xfail()` in the body carries
  `wasxfail` too. So it is still named `kills nothing its file does not`, the
  same misreport round 2's 🟡 1 closed for `pytest.skip()`.

One fix covers both. Keep every traced line for selection, carry the
short-stopped ids beside them, and use those ids only to decide which cases
never ran.

Everything else the prompt asked about holds. The budgets conflict
resolution, `budget_check.py --baseline` exit 0, #931's lines, round 2's
wording fix and the `cases` job at the tip all check out. The `hygiene`
workflow is red on round 2's paperwork, which is ⬜ 3.

## 🟡 1 — a sibling that asserts and then skips is no longer counted as a killer, so a new case it covers is "proved"

**Where.** `.github/scripts/case_check.py:188`. The tracer's session finish
writes `hits` without every id in `_skipped`. `check` then reads those hits
twice: at `:868`, to decide which new cases never ran, and at `:892` and
`:897`, through `selected`, to decide which other cases ran the mutated line
and must be run under the mutant.

**What is wrong.** Only the first use needs the skipped ids gone. The second
needs them kept. A case that ran a line and then skipped is still a case
that can fail under that line's mutant. Here is a realistic shape, which
`tests/` already carries 27 of (a skip after other statements in the
body):

```python
def test_partial():
    assert m.double(2) == 4
    pytest.skip("the rest runs on windows")
```

On ubuntu this case skips. Under the mutant `return None` it fails at its
assertion, before the skip. So it is a killer of that mutant.

**Failure scenario (executed).** The base holds `test_partial`, and HEAD adds
`test_double` (`assert m.double(2) == 4`). Its only drawn mutant is
`m.py:2` `return None`, and `test_partial` kills that too.

- At `e90c90d3`: exit 0, `tests/test_m.py::test_double: proved — the only
  killer in its file of m.py:2 `return` made `return None``. `ran` held only
  `test_double`, so `rest` was empty, and an empty `rest` counts as
  `SURVIVED`, which reads as "alone".
- With `case_check.py` as it stood before the fix (`ec152145^`): exit 1,
  `test_double: kills nothing its file does not` — correct.

So the fix flipped a correct refusal into a false proof. The job the check
exists for — refusing a case its file already covers — passes it.

**Why it matters.** The gate's errors are documented in `spec.md:91`
("under" for subprocess-only lines, "over" for setup only one case runs).
This one is in neither list, and it errs toward passing.

## 🟡 2 — an imperative `pytest.xfail()` in the body is still named for killing nothing

**Where.** `.github/scripts/case_check.py:180`. The tracer's
`pytest_runtest_logreport` keeps any call-phase skip that has `wasxfail`,
with the comment at `:178`: *An expected failure reports as skipped too and
is kept, since its body ran.*

**What is wrong.** `pytest.xfail("windows only")` called in the body stops
the call there, exactly as `pytest.skip()` does. Its report also carries
`wasxfail`. The hook cannot tell it from a marked xfail whose body ran, so
it keeps it as a run.

**Failure scenario (executed).** HEAD adds:

```python
def test_by_xfail():
    pytest.xfail("windows only")
    assert m.double(2) == 4
```

At `e90c90d3`: exit 1, `test_by_xfail: kills nothing its file does not: of
the 1 mutants drawn for it …`. The docstring at `:76`–`:85`, the workflow
comment at `.github/workflows/test.yml:221` and `spec.md:91` all say a case
that does not run its call to the end is named for never having run. For
this spelling they are false. The author is told the case duplicates a
sibling, when it never ran on this runner.

No case in `tests/` calls `pytest.xfail(` today (grep). This is the one
spelling the round-2 enumeration missed of those I tried. The others are
listed under Executed probes.

**The fix must keep the unittest twin a run.** `@unittest.expectedFailure`
reaches pytest as an `xfail.Exception` too. The probe shows the fix below
keeps it a run (`kills nothing`, as a non-`raises` expected failure should
be).

## ⬜ 3 — the `hygiene` workflow is red on round 2's `Target SHA`

`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/rounds/round-2.md:5`
names `fffee6b2`. The rebase onto #931 left that SHA on no ref, so
`chain_check.py` (`skills/code-review/scripts/chain_check.py:5586`) fails
`release` in run 38668484688 at `e90c90d3`. It judges only the last record.
So round 3's own record, with a reachable `Target SHA`, should clear it. That
is not executed here; the next CI run at the record's commit answers it.
This is paperwork, not a fix.

## What holds (verified)

- **The conflict resolution.** `seal/budgets.md` differs from the base in
  exactly three cells: `suite-seconds` 9185 → 7841 and the two file rows,
  1538 → 1190 and 1479 → 506. `slow-file` stays `one-sided | report`, as
  #931 made it. Each lowered ceiling is 1.3 times its reading at the 1132
  level, rounded up: 6,031 × 1.3 = 7,840.3; 915 × 1.3 = 1,189.5;
  389 × 1.3 = 505.7. The readings at the base (6,854, 1,178, 946) match
  `spec.md:99`–`:101`. `budget_check.py --baseline origin/release/v0.22.0`
  exits 0.
- **What the two lowered rows still mean.** Under a `report` family a
  listed file's row fails nothing, and the ratchet reads only `gate` rows.
  So a later pull request can raise them back without a `Budget raised:`
  line. What they still do is make the summary name the file among the
  report rows past their band the moment it regrows past 1.3 times its
  reading. That is all the branch claims: `spec.md` §*Rows* and S8 say
  "lowered" and "exit 0", the changelog says nothing about them, and no doc
  this branch touches calls them a gate.
- **Nothing #931 brought in is undone.** I checked every line #931's squash
  added, file by file, against HEAD and found none missing. The two lines
  of #931's removals that HEAD still carries are repeated generic lines (`#`,
  `fetch-depth: 0`) present elsewhere in those files. The modules #931 added
  or changed that read files this branch also changed pass at HEAD.
- **Round 2's 🟡 1, as far as it went.** A mark, a body `pytest.skip()`,
  `importorskip`, a fixture skip, `xfail(run=False)`, `skipTest`, a
  `@unittest.skip` class decorator, a module-level `pytestmark` skipif and a
  module skipped at import (exit 5) are each named `not proved: … never
  ran`. An xfail that runs its body is a run.
- **Round 2's 🟡 2.** `CONTRIBUTING.md:124`–`:133` and `ruff.toml:35`–`:41`
  say what the census checks and that `tomllib` or `str | None` passes it.
  Round 2's ⬜ 3–5 are carried open, so I do not report them again.
- **The `cases` job at the tip** (CI's run, read here): 21 proved, 0 named,
  298 s of the 300 s bound, 664 changed-line mutants not run within it.

## Regression tests to plant

Destination: `tests/test_a_new_case_protects_what_its_file_did_not.py`,
in `test_each_real_path_end_to_end`'s parametrization. Both were seen red
at `e90c90d3` (the first proved, the second named for killing nothing) and
pass with the fix below.

```python
PARTIAL = (
    "\nimport pytest\n\n\ndef test_partial():\n    assert m.double(2) == 4\n"
    '    pytest.skip("the rest runs on windows")\n'
)
# in the parametrize list:
pytest.param(
    {"tests/test_m.py": module_text(PARTIAL)},
    {"tests/test_m.py": module_text(PARTIAL, DOUBLE)},
    {},
    1,
    ["tests/test_m.py::test_double: kills nothing its file does not"],
    id="a sibling that skips after its assertions still kills",
),
```

```python
# appended to ELSEWHERE, and "test_by_xfail" appended to NEVER_STARTED:
"\n\n\ndef test_by_xfail():\n"
'    pytest.xfail("another platform")\n    assert m.double(2) == 4\n'
```

## Facts for the evidence ledger

None. The ledger left with #944, and this round checked no released claim.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | The tracer drops a skipped call's lines from `hits`, and `selected` reads the same `hits`, so a sibling that asserts and then skips its tail is never run under a mutant; a new case that sibling covers is reported `proved — the only killer in its file` | `.github/scripts/case_check.py:188` | open | executed: fixture with `test_partial` in the base and `test_double` added, exit 0 and `proved` at `e90c90d3`, exit 1 and `kills nothing` with the file as it stood before round 2's fix; a fix of a fix in the tracer round 2's fixes changed |
| 🟡 2 | An imperative `pytest.xfail()` in the body carries `wasxfail`, so the hook keeps it as a run and it is named `kills nothing its file does not`; the docstring, `test.yml:221` and `spec.md:91` say such a case is named for never having run | `.github/scripts/case_check.py:180` | open | executed: fixture with `test_by_xfail`, exit 1 with the wrong reason at `e90c90d3`; the fix below names it `not proved` and keeps `@unittest.expectedFailure` a run |
| ⬜ 3 | The `hygiene` workflow's `release` job is red: round 2's `Target SHA` `fffee6b2` is on no ref after the rebase onto #931 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/rounds/round-2.md:5` | open | read: run 38668484688 at `e90c90d3`; `chain_check.py` judges the last record, so round 3's record should clear it, not executed |
| 🟢 | round 2's finding 1 is closed for every spelling it listed — a mark, a body skip, `importorskip`, a fixture skip, `xfail(run=False)`, `skipTest`, and a file skipped at import | `.github/scripts/case_check.py:862` | confirmed | executed: the module's 23 cases pass at `e90c90d3`; a probe added a `@unittest.skip` class and a module `pytestmark` skipif, both named `not proved`; the two spellings that still slip are 🟡 1 and 🟡 2 |
| 🟢 | round 2's finding 2 is closed — the census's claims say what it checks | `CONTRIBUTING.md:124`, `ruff.toml:35` | confirmed | read at `e90c90d3` |
| 🟢 | the `seal/budgets.md` conflict is resolved as both sides meant: this branch's three lowered ceilings, #931's `report` kind | `seal/budgets.md:40`, `seal/budgets.md:60` | confirmed | executed: `budget_check.py --baseline origin/release/v0.22.0` exit 0; readings recomputed from `.test_durations` at both revisions |
| 🟢 | the two lowered `slow-file` file rows still print an over-line when the file regrows, and the branch claims no more for them | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/spec.md:99` | confirmed | read: `budget_check.py` docstring on `report` families and the ratchet; no touched doc calls them a gate |
| 🟢 | nothing #931 brought in is undone | `.github/workflows/test.yml`, `CONTRIBUTING.md`, `tests/test_every_reader_ends_a_line_where_gfm_does.py` | confirmed | executed: every line #931's squash added is present at HEAD; #931's three test modules pass |
| 🟢 | the `cases` job passes at the tip | CI run 38668484642 | confirmed | read: CI's execution at `e90c90d3`, 21 proved, 0 named, 298 s |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_a_new_case_protects_what_its_file_did_not.py tests/test_a_script_says_which_interpreter_it_needs.py tests/test_a_shrunken_corpus_declines_to_judge.py -q` at `e90c90d3` | exit 0, 46 passed |
| `python3 .github/scripts/budget_check.py --baseline origin/release/v0.22.0` at `e90c90d3` | exit 0; `suite-seconds` 6,031 of 7,841; the two file rows 915 of 1,190 and 389 of 506, `report`, holds; `rounds-bytes` over, `report` |
| `.test_durations` summed per file at `642441fc` and `e90c90d3`, divided by 1.132 | base 6,854, 1,178, 946; HEAD 6,031, 389, 915 |
| every `+` line of `git diff 642441fc^ 642441fc`, per file, looked up at HEAD | none missing |
| `bin/test tests/test_ci_gives_the_checks_what_they_need.py tests/test_a_budget_ratchets.py tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q` | exit 0, 212 passed, 2 skipped |
| probe `tests/test_tmp_r3_skip.py` (NAME NOT IN TREE: deleted after the run), `case_check.main` on six fixtures at `e90c90d3` | partial sibling: exit 0, `test_double: proved`; imperative xfail: exit 1, `kills nothing`; `@unittest.skip` class, module `pytestmark` skipif, a new case that asserts then skips: each `not proved`; `@unittest.expectedFailure`: `kills nothing` |
| the same probe with `case_check.py` from `ec152145^` | partial sibling: exit 1, `test_double: kills nothing`; imperative xfail: `kills nothing` |
| the same probe with the paste-ready fix applied in the clone, then reverted | partial sibling: `kills nothing`; imperative xfail: `not proved`; `@unittest.expectedFailure` still a run; the other rows unchanged; the module 23 passed; `tests/test_every_reader_ends_a_line_where_gfm_does.py` 149 passed |
| AST scan of `tests/test_*.py` for a skip or xfail call after another statement in a test body | 27 cases |
| `gh pr checks 939`, the `cases` job log of run 38668484642, the failed log of run 38668484688 (CI's execution, read here) | `cases` pass, 21 proved, 0 named; `hygiene` `release` fails on round 2's `Target SHA`; ubuntu and Windows `pytest` still pending when read |
| Broad gate (full suite, repository-wide lint, typecheck) | not yet: not run by this round, and owed to the sealer once the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Paste-ready fixes

### 🟡 1 — keep every traced line, carry the short-stopped ids beside them

In `TRACER_SOURCE`, the session finish writes every id's lines and the ids
separately:

```python
def pytest_sessionfinish(session):
    with open(os.path.join(_out, f"{os.getpid()}.json"), "w", encoding="utf-8") as f:
        hits = {k: sorted(v) for k, v in _hits.items()}
        json.dump({"hits": hits, "seconds": _seconds, "short": sorted(_skipped)}, f)
```

In `traced_run`, the timeout return and the read gain the set, and the
docstring's tuple gains `{nodeid}` of the calls that stopped short:

```python
        except subprocess.TimeoutExpired:
            return None, time.monotonic() - started, "timed out", {}, {}, set()
        seconds = time.monotonic() - started
        hits, calls, short = {}, {}, set()
        for name in os.listdir(out):
            try:
                with open(os.path.join(out, name), encoding="utf-8") as f:
                    found = json.load(f)
                for nodeid, pairs in found["hits"].items():
                    hits.setdefault(nodeid, set()).update(map(tuple, pairs))
                calls.update(found["seconds"])
                short.update(found["short"])
            except (OSError, ValueError, KeyError, AttributeError, TypeError):
                continue
    lines = (done.stdout + done.stderr).strip().splitlines()
    return done.returncode, seconds, lines[-1] if lines else "", hits, calls, short
```

In `check`, only the never-ran decision reads the ids that ran to the end;
`selected` and `mine` keep reading every traced line:

```python
        code, each, verdict, hits, calls, short = traced_run(root, file, runner, left)
```
```python
        through = {i: pairs for i, pairs in hits.items() if i not in short}
        never_ran = [n for n in names if not own_ids(through, file, functions, n)]
```

The tracer's comment above the hook then reads:

```python
# A call that stopped short of its body, as `pytest.skip()`, `importorskip`,
# `skipTest` or `pytest.xfail()` there, started, so its first lines are
# traced. Its lines are kept, since a mutant of one can still fail it before
# it stops, and its id is written apart, so the check names it as one that
# never ran. An expected failure whose body ran is a run.
```

### 🟡 2 — tell an imperative xfail from an expected failure that ran

Replacing `pytest_runtest_logreport` in `TRACER_SOURCE` (`call.excinfo` is
read after every other implementation, so unittest's own replacement of it
has happened):

```python
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    report = (yield).get_result()
    if report.when == "call" and report.skipped:
        stopped = call.excinfo is not None and call.excinfo.errisinstance(
            pytest.xfail.Exception
        )
        expected = getattr(
            getattr(item, "obj", None), "__unittest_expecting_failure__", False
        )
        if not hasattr(report, "wasxfail") or (stopped and not expected):
            _skipped.add(report.nodeid)
```

The module docstring's list at `.github/scripts/case_check.py:79`, the
workflow comment at `.github/workflows/test.yml:221`, `spec.md:91` and the
changelog fragment's list gain `pytest.xfail()` in its body.

Needs a fix: yes — 🟡 1 (a sibling that asserts then skips is no longer run under a mutant, so a case it covers is reported proved), 🟡 2 (an imperative `pytest.xfail()` is named for killing nothing)
Loses a record or crashes: no

## Proof block

Opened: `.github/scripts/case_check.py` (`:73`–`:205`, `:525`–`:700`,
`:811`–`:985`), `.github/scripts/budget_check.py` (docstring),
`.github/workflows/test.yml` (`cases`, `budgets`), `seal/budgets.md` at HEAD
and at the base, `CONTRIBUTING.md:118`–`:150`, `ruff.toml:30`–`:46`,
`tests/test_a_new_case_protects_what_its_file_did_not.py` (`:225`–`:540`),
`tests/test_a_script_says_which_interpreter_it_needs.py:394`–`:416`,
`skills/code-review/scripts/chain_check.py:5545`–`:5600`, the work item's
`spec.md`, `plan.md`, `questions.md`, `changelog.md`, `rounds/round-2.md`,
`rounds/round-2-report.md`; `git show` of `ec152145`, `9cbbce1a` and
`642441fc`.
