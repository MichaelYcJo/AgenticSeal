# 1791876666-the-test-suite-is-held-to-a-budget — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | d0429bfd |
| Ran by | smith on Opus 5.5, as `routing.md` names it |

## What this phase was asked

Phase 3 of the plan reframed after round 3 (17cd0b36, approved at 2aa76b37),
exactly as its row reads:

- in `.github/scripts/case_check.py#TRACER_SOURCE`, a
  `pytest_runtest_makereport` hookwrapper that decides once, from pytest's
  call report, which ids stopped short: `skipped` without `wasxfail`, or with
  it where the call's exception is pytest's xfail stop and the function does
  not carry `__unittest_expecting_failure__`;
- every traced line kept for every id, and `pytest_sessionfinish` writing the
  lines and the stopped ids apart;
- `traced_run` returning the stopped set as its sixth element, empty on a
  timeout;
- `check` naming a function never-ran only when none of its ids in `hits` is
  outside the stopped set, while the draw and the choice of siblings under a
  mutant read every traced line;
- the tracer's comment, the module docstring, `test.yml`'s `cases` comment
  and the changelog fragment's `Added` entry stating the rule in one sentence
  each, with no list of spellings;
- the end-to-end rows S16 and S17 in
  `tests/test_a_new_case_protects_what_its_file_did_not.py#test_each_real_path_end_to_end`,
  each seen red before its fix the way the plan's Verified-by says.

Verification was to be narrow: the module whole, the GFM reader module and
the modules reading changed files; round 3's six probes; `case_check.py` as
the `cases` job runs it; `budget_check.py --baseline origin/release/v0.22.0`;
ruff on the changed Python. No full suite.

## What this phase found

**The frame holds.** Every claim `plan.md` §*Technical context* makes about
pytest 9.1.1's reports was borne out by a run: the rows below go red and
green exactly where it predicts. Nothing in `spec.md` needed changing.

**The wrapper is `tryfirst`, which the round-3 paste-ready code was not.**
`tests/conftest.py#pytest_runtest_makereport` is a hookwrapper of its own,
and a conftest is registered after a `-p` plugin. Without `tryfirst` it
would sit outside the tracer, and its tail would run after the tracer had
read the report. That breaks `spec.md`'s *after every other implementation*
on this repository's own suite. Today it rewrites only a passing report, so
no verdict moves. The mutation results:

- `tryfirst` made `trylast`: red, so the order is watched;
- `tryfirst` dropped: survived, because load order alone already puts the
  tracer outside every built-in plugin, and no fixture's conftest rewrites a
  skip.

It stays for the conftest reason above. A case that kills the second
mutation needs a fixture conftest that rewrites a skipped report, and the
frame did not ask for one.

**The timeout's empty set had nothing behind it.** No case reached
`traced_run`'s timeout branch, so a return of five elements survived. The
restructure row ends on `each > left`, not on the timeout. A wrong tuple
there would stop `check` on the unpacking instead of naming the file to
restructure. `test_a_traced_run_that_times_out_hands_back_nothing_it_traced`
runs that branch directly in about a second, and is a case the frame did not
name (`overview.md`).

**The `cases` job cannot draw a mutant from the hook.** `TRACER_SOURCE` is a
string, and the check never mutates a line inside one. So CI proves
`test_each_real_path_end_to_end` by a mutant elsewhere in `case_check.py`
(`:367`), and the tracer's rule is held by the rows below. Each was killed
by `mutation-check` here, by hand. This is the module docstring's *under*
direction, in the check's own file.

### Each row seen red

The tree at 2aa76b37 carries `case_check.py` as it stood at e0e0d485, since
17cd0b36 and 2aa76b37 touch only `plan.md`, `spec.md` and `questions.md`.
The rows were added first and run against it (`executed`):

| Row | Before the fix | After |
|---|---|---|
| T8 *a sibling that skips after its assertions still kills* (S16) | exit 0, `test_double` proved, the only killer in its file of the `m.py:2` mutant `return None` | exit 1, `kills nothing its file does not` |
| T9 `test_by_xfail` in *every way a case skips here names it as one that never ran* (S17) | `test_by_xfail: kills nothing its file does not: of the 1 mutants drawn for it …` | `not proved: none of its ids ran its call to the end on this runner …` |
| T10 *a unittest expected failure whose body raised is a run* (S17) | passes before the fix, as it should | with `(stop and not expected)` made `stop`: `TestExpected::test_by_expected_failure: not proved: …`, red |

Every unit the fix added, broken one at a time with `bin/mutation-check`
over the cases that cover it, after the fix was committed at c5df90d8:

| Mutation | Cases | Result |
|---|---|---|
| `(stop and not expected)` → `stop` | `-k unittest` | red |
| the `if k not in _skipped` filter put back on `hits` | `-k after` | red |
| `or (stop and not expected)` dropped | `-k every` | red |
| `own_ids(through, …)` → `own_ids(hits, …)` | `-k every` | red |
| `short.update(found["short"])` → `found["short"]` | `-k every` | red |
| `"short": sorted(_skipped)` → `"short": []` | `-k every` | red |
| `tryfirst=True` → `trylast=True` | the three rows | red |
| `tryfirst=True` dropped | the three rows | **survived**, kept on the grounds above |
| the timeout's `set()` dropped | `-k times_out` | red |
| the timeout's `set()` → `{"x"}` | `-k times_out` | red |

### Round 3's six probes

They were rebuilt on the module's own fixture helpers, run once against
d0429bfd and deleted (`executed`). Two verdicts moved, S16 and S17's
imperative xfail; the other four are what round 3 recorded at e90c90d3.

| Fixture | Round 3 at e90c90d3 | Here |
|---|---|---|
| a partial sibling in the base, `test_double` added | exit 0, `proved` | exit 1, `kills nothing its file does not` |
| an imperative `pytest.xfail()` | `kills nothing` | `not proved` |
| a `@unittest.skip` class | `not proved` | `not proved` |
| a module `pytestmark` skipif | `not proved` | `not proved` |
| a new case that asserts then skips | `not proved` | `not proved` |
| a `@unittest.expectedFailure` whose body raised | `kills nothing` | `kills nothing` |

### What was run, and what it returned

All `executed` at d0429bfd unless the row says otherwise, on macOS arm64,
pytest 9.1.1, CPython 3.13.9:

| Command | Exit | Result |
|---|---|---|
| `bin/test tests/test_a_new_case_protects_what_its_file_did_not.py -q -p no:xdist` (at c5df90d8) | 0 | 25 passed |
| `bin/test` over that module, `test_every_reader_ends_a_line_where_gfm_does.py`, `test_ci_gives_the_checks_what_they_need.py`, `test_a_budget_ratchets.py`, `test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `test_the_changelog_is_gathered_at_release.py`, `test_a_fragment_left_behind_is_named.py`, `test_release_hygiene.py` | 0 | 517 passed, 2 skipped |
| `python .github/scripts/case_check.py --baseline origin/release/v0.22.0 --runner "python -m pytest -n auto" --bound 5`, the `cases` job's line | 0 | 22 proved, 0 named, in 299 s; 15 changed-line mutants survived and 653 were not run within the bound, both a report |
| `python .github/scripts/budget_check.py --baseline origin/release/v0.22.0` | 0 | every gate row holds; `rounds-bytes` over, a report |
| `uvx ruff check` and `uvx ruff format --check` on `case_check.py` and the test module | 0 | clean |

The full suite, repository-wide lint and typecheck were not run. They are
`unverified` here and are the sealer's, once the rounds settle.
