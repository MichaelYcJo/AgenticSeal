# Phase 1: 1794465688-feature-prs-wait-on-the-macos-runner

## What this phase found

**The frame holds against the tree at `fc4ed4f9f`.** The frame read the tree
at `6a3b74ba8`, and `fc4ed4f9f` adds only the frame's own files. Each
coordinate of design G2 and G10 was opened before the build and stands as
the design states it: `test.yml:7` and `:52-79`, the timeout and report
flag cases of `tests/text/test_ci_gives_the_checks_what_they_need.py`,
`pytest_job` and its two readers in
`tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py`,
`matrix_entries` in
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`,
the `needs` assertion at
`tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py:39`,
and `matrix_pythons` in `tests/behaviour/test_release_hygiene.py` (read).
The sentences G14 lists stand at the lines it gives (read). No
`seal/follow-up.md` row waits on this work: both of its tables are empty
(read).

**`tests/workflows.py` holds the one reading of which jobs run the suite,
so the reading that stood in the CI case module moved there.** Design
*Scope* item 2 asks for a function that returns the jobs whose steps run
the pytest line. `tests/text/test_ci_gives_the_checks_what_they_need.py`
already held that reading as `RUNS_PYTEST`, `runs_pytest` and
`job_scripts`, for its whole-history case. A new function beside it would
have been a second reading of the same fact. So `job_scripts` and
`RUNS_PYTEST` moved into `tests/workflows.py` unchanged. `runs_pytest`'s
body became the filter of the new `pytest_jobs`, which returns
`{job name: job}` in the file's order. `shallow_pytest_jobs` now iterates
`pytest_jobs`. Judged against `skills/core/SKILL.md` *The rule a mechanism
is kept against*: a fact has one source. The move removes `runs_pytest`,
which the frame's `## Removes` does not name. It is proved by the cases
that already held it, run at the new path in the phase boundary run: the
six `test_a_job_that_calls_pytest_any_way_is_held_to_the_whole_history`
cases, `test_every_job_that_runs_pytest_has_the_whole_history`, and the
draft and edited event cases that read `job_scripts` through `scripts`
(executed). The census of the old spelling, `git grep -n "runs_pytest"`
outside `seal/threads/`, finds only two case names that contain the words
and no definition or call (executed). `seal layout --check
tests/test_workflows.py` reports that `job_scripts` has no class
`Test_job_scripts`. That line is a report and refuses nothing, and the
unit is a move, which owes no case written new.

**The new case reads every job `pytest_jobs` returns, which holds the union
of design *Scope* item 3 and more.** The item asks for each job's legs
against the owner's decision and for the union of both jobs' legs against
G2. The case asserts that the legs of every job that runs the suite are
exactly `{"pytest": ubuntu 3.12 and four Windows 3.12, "pytest-wide":
ubuntu 3.14 and macOS 3.12}`. That equality implies the union, and it also
refuses a third job that runs the suite. The case also holds `pytest-wide`'s
`runs-on`, `timeout-minutes` and `strategy.fail-fast` to `pytest`'s, as
*Scope* item 1 states them, because a `runs-on` that is not
`${{ matrix.os }}` would run a macOS leg on another system under the same
check name.

**The Windows module reads the shards from `pytest` and the rest from every
job.** Design *Scope* item 2 keeps the shard, upload and cache cases on
`pytest` and generalises the include-only rule and the rule on where a
split or a store stands. `matrix_entries` keeps returning `pytest`'s
entries for the group count, the Windows store check and the `durations`
count. A new `entries_of` refuses a matrix with a key beside `include:`
and names the job. A new `suite_entries` applies it to every job
`pytest_jobs` returns. The split check and the store check read every
non-Windows entry through it. A Windows shard moved into `pytest-wide`
therefore fails the group count, which reads `pytest`, rather than passing
a count read over both jobs.

**Statements the split made false, outside *Scope* item 4, were corrected
in the build.** Each was found by reading `test.yml` and by `git grep -n -i`
over the tree for `three platforms`, `macOS`, `pytest job` and `pytest`
leg. This is a sample, and the part it did not reach is any other wording
of where a leg runs. The `durations` comment in `test.yml` said it runs
"after every pytest job". It runs after `pytest` alone, because the
`needs: pytest` holds the Windows shards. The `release-report` comment now
names both jobs. `CONTRIBUTING.md` *The suite runs with `gh` logged out*
said "CI's pytest job has no token", and now says jobs. The CI case
module's docstring said "Each `pytest` leg", and now says each leg that runs
the suite. `docs/running/the-broad-gate.md:131` and
`.github/scripts/run_tests.py:52` stand as design G14 judges them.
`docs/releasing/release-checklist.md` and `docs/releasing/branch-and-release.md`
stand for the settle, under the design's `## Rule changes`.

**actionlint reads the alias and flags three reads of a matrix property
`pytest-wide` does not define.** actionlint 1.7.12, run as
`uvx --from actionlint-py actionlint -shellcheck= .github/workflows/test.yml`,
exits 0 over `test.yml` at `fc4ed4f9f` and exits 1 over the build (executed).
Its three lines are `property "split" is not defined` at the cache restore's
`if` and at the pytest line, and `property "store" is not defined` at the
upload's `if`. Each is in the steps `pytest-wide` runs through the alias.
The ubuntu 3.14 and macOS entries carried neither key before the split, so
those legs already read the same two properties as absent (read). An absent property
should read as `null`, which a loose comparison with `''` treats as equal
and which renders as an empty string, so the two steps stay skipped and the
pytest line ends with two empty expansions, as on those legs before. That
is GitHub's expression semantics as this phase recalls them; the phase did
not open the documentation, so the claim is unverified. Adding `split: ""` and `store: ""` to `pytest-wide`'s
entries would quiet actionlint and fail the Windows module's rule that only
Windows entries carry a split or a store. actionlint is not one of this
repository's checks, so the entries stay as they were. The first run of
`pytest-wide` is on the release pull request for 0.38.0, not on this pull
request, whose base is `release/v0.38.0`. `gaps.md` names it.

**Seen red before the build (contract rule 15).** Each case below ran
against the tree at `fc4ed4f9f` before the code it pins (executed).
`test_a_pull_request_into_a_release_branch_runs_ubuntu_3_12_and_windows`
failed on its `legs ==` line, with all seven legs in `pytest` and no
`pytest-wide`. `test_the_tests_workflow_prints_the_table_only_into_main_after_the_suite`
failed on its `needs` line with `['pytest', 'durations']`. Both
`Test_pytest_jobs` cases failed on `AttributeError` before `pytest_jobs`
existed.

**Each generalised case was seen red with one `pytest-wide` entry or line
changed (S3, S4), through `seal mutate` after the build commit `482da1d03`,
each mutant run alone, and each failing line read for the guard the case
names (executed).**

| Mutant of `test.yml` | Case | Failing line |
|---|---|---|
| `pytest-wide`'s `if` without `!` | the legs case | `assert wide.get("if") == WIDE_IF` |
| `pytest-wide`'s `name` without the first comma | the legs case | `assert wide.get("name") == WIDE_NAME` |
| macOS added to `pytest`'s entries | the legs case | `assert legs == {...}` |
| the alias replaced by a three-step copy (S4) | the legs case | `assert wide["steps"] == release["steps"]` |
| `release-report` needs `[pytest, durations]` | the `needs` case | `assert job["needs"] == [...]` |
| `timeout` taken off `pytest-wide`'s macOS entry | the timeout case | `` `pytest-wide` has a leg with no timeout `` |
| the alias replaced by a copy without `--no-fold-skipped` | the report flags case | `` `pytest-wide`'s pytest line does not pass ['--no-fold-skipped'] `` |
| the alias replaced by a copy installing `PyYAML==6.0.2` | the install pins case | `assert any(rt.PYYAML in words ...)`, naming `pytest-wide` |
| `pytest-wide`'s macOS entry at `3.13` | the floor case | `CI runs the suite on ['macos-latest'] with no entry at the floor 3.12` |
| a `python:` key beside `include:` in `pytest-wide` | the group case, through `suite_entries` | `` `pytest-wide`: a `matrix:` key beside `include:` `` |
| a `split` on `pytest-wide`'s macOS entry | the group case | `assert others and not any("split" in e ...)` |
| a `store` on `pytest-wide`'s ubuntu entry | the store case | `assert others and not any("store" in e ...)` |

The cases as they stood at `fc4ed4f9f` read `jobs["pytest"]` alone, so
none of them opens a `pytest-wide` entry or step. Each mutant above lands
in `pytest-wide`, so it would have survived them (read, not run against the
old cases).

**`pytest_jobs` was mutated twice, and both mutants went red (executed).**
`seal mutate tests/workflows.py` with `if any(` written `if not any(`, and
with the lines of a script cut to its first, ran
`bin/test tests/test_workflows.py -q -p no:xdist -x -k pytest_jobs`. The
second mutant drops the job whose `pytest` stands on the second line of a
`run: |` block. `RUNS_PYTEST` was moved unchanged and was not mutated, as a
move adds no behaviour.

**The phase boundary run.** `bin/test tests/text tests/behaviour
tests/test_workflows.py tests/github/test_release_report.py
tests/e2e/teammate/test_teammate_flow.py -q` holds the plan row's files, each
test file the phase changed, `tests/e2e/teammate/test_teammate_flow.py`
(which imports `tests/workflows.py`), and the tree-wide files
`CONTRIBUTING.md` *The test layout* names. Every other file that names
`CONTRIBUTING.md` or `.claude-plugin/plugin.json` was opened, and each one
writes the name into a fixture it builds. The run at `d3e644ca3` failed
only `test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which asks for this work item's `gaps.md`. This record's commit writes that
file. The run at that commit is the result the hand-back reports
(executed).
