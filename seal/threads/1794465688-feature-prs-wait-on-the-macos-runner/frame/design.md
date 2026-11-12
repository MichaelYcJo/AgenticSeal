# Design: 1794465688-feature-prs-wait-on-the-macos-runner

## Grounding

The tree as read at `6a3b74ba8`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. Issue #1516 *Decided*, and the owner's decision in [the comment of 2026-11-12](https://github.com/MichaelYcJo/AgenticSeal/issues/1516#issuecomment-6816700780) (read) | A pull request into `release/*` runs ubuntu 3.12 and the four Windows shards. ubuntu 3.14 and macOS run on a pull request into `main`, a push to `main` and `workflow_dispatch`, which run every leg of G2. A defect only those two legs meet is fixed on the release branch. The frame does not reopen it. |
| G2. `.github/workflows/test.yml:7` and `:52-79` (read) | `pull_request:` carries no branch filter. The `pytest` job's matrix has one key, `include:`, and its seven entries in this order: ubuntu 3.12, ubuntu 3.14, macOS 3.12, and Windows 3.12 groups 1 to 4. Each entry is one job. |
| G3. GitHub's contexts reference, the availability table (read, docs.github.com `…/workflows-and-actions/contexts`) | `jobs.<job_id>.if` may read `github`, `needs`, `vars` and `inputs`, and not `matrix`. `jobs.<job_id>.strategy` may read the same four. `jobs.<job_id>.name` may read `matrix`. This confirms the orchestrator's claim: a job's `if` cannot select one matrix entry. |
| G4. GitHub's workflow syntax reference, `strategy.matrix` (read, docs.github.com `…/workflows-and-actions/workflow-syntax`) | "All `include` combinations are processed after `exclude`." An include object that cannot be added to a remaining combination becomes a new one. So an `exclude:` cannot remove an entry of an include-only matrix, which confirms the orchestrator's second claim. |
| G5. GitHub's reference *Reusing workflow configurations* (read) | "You can use YAML anchors and aliases to reduce repetition in your workflows." The page says nothing of merge keys (`<<`), so the frame does not use them. |
| G6. PyYAML 6.0.3 `BaseLoader`, the loader `tests/workflows.py#load` uses (executed, `test_tmp_anchor.py` in the framer's scratch directory under `uvx --with PyYAML==6.0.3`) | A `steps: *pytest-steps` alias loads as the same list object as the anchored `steps: &pytest-steps`. `if: ${{ !startsWith(github.base_ref, 'release/') }}` loads as that string. A bare `if: !startsWith(…)` is refused with a `ParserError`, because `!` opens a YAML tag, so the expression keeps its `${{ }}`. |
| G7. Today's check names, read off run 43143655875, a push to `main` (executed, `gh api …/runs/43143655875/jobs`) | `pytest (ubuntu-latest, 3.12, 5)`, `pytest (ubuntu-latest, 3.14, 5)`, `pytest (macos-latest, 3.12, 10)`, and `pytest (windows-latest, 3.12, --splits 4 --group <N>, --store-durations --clean-durations, 10)` for each group. |
| G8. `.github/scripts/release_report.py:79-80` and `:278` (read) | The release table reads a leg's minutes from the jobs whose name fullmatches `pytest \(([a-z]+)-[^,)]*, ([^,)]+)(?:,.*)?\)`. A job named another way reads as `no run found`, at the tag's side and at this side alike. |
| G9. The rulesets `main` (23858898) and `release` (23856929) (executed, `gh api repos/…/rulesets/<id>`) | Each requires the checks `lint` and `release` and no other. No `pytest` check is required, so a skipped job holds no merge. `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* states the same. |
| G10. The readers of the `pytest` job (executed, `git grep` over the tree less `seal/threads/`) | `tests/text/test_ci_gives_the_checks_what_they_need.py:345-363` (timeouts) and `:365-384` (report flags), `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:26-28` with `:106-130` (install pins) and `:228-243` (the floor per system), `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:74-87` (`matrix_entries`, include-only) with its Windows cases, `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py:39` (`release-report`'s `needs`). `tests/behaviour/test_release_hygiene.py:1017-1027` reads every job's entries. `tests/text/test_ci_gives_the_checks_what_they_need.py:221-234` reads every job that runs pytest. |
| G11. The step 1 count, in the comment of G1 (read) | Over 87 pull requests into `release/*`, macOS met no defect, and its six failed attempts were one run that no runner took. Windows alone met four. Every long wait was a macOS job queued for a runner. |
| G12. ubuntu 3.14's own record over the same window (executed, `test_tmp_314.sh` in the framer's scratch directory: each attempt of the 134 `pull_request` runs of `test.yml` created since 2026-11-03T03:57:40Z, its ubuntu jobs' conclusions) | 87 attempts ran a ubuntu 3.14 job. It failed in two, 42541950791 and 42997459560, and ubuntu 3.12 failed in both. On no attempt did ubuntu 3.14 fail where ubuntu 3.12 passed. |
| G13. The wait before, in the comment of G1 (read, not re-measured) | Over 102 feature pull request runs' first attempts, a median of 3.7 minutes from creation to the last job, at most 15.3. A Windows shard was the last pytest job to finish in 95 of the 102. |
| G14. The sentences that state which legs a pull request runs (executed, `git grep -n -i` for `macOS`, `three platforms` and `Linux, macOS` over the tree less `seal/threads/`) | `CONTRIBUTING.md:32-33`, `:44` and `:145-150`, `.github/PULL_REQUEST_TEMPLATE.md:26`, `docs/releasing/release-checklist.md:155-158`, `docs/releasing/branch-and-release.md:276-279`. `docs/running/the-broad-gate.md:131` and `.github/scripts/run_tests.py:52` say CI runs the suite on three platforms, which stays true of the release's runs, so they stand. |
| G15. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, and `seal/config.json` with no `Policy root` key (read) | The policy root is `docs/`. This work's subject is the CI workflow, so it states its policy changes in `## Rule changes` and does not edit `docs/`. `CONTRIBUTING.md` and the pull request template stand outside the policy root and change in the build. Neither `docs/releasing/` document has a `.ko.md` edition in the index, `docs/README.md:43-45`. |
| G16. The unsettled designs' `## Rule changes` on `docs/releasing/release-checklist.md` *The release pull request* (read, `seal/threads/1794383425-…` and `seal/threads/1794312072-…`) | They remove the `.test_durations` refresh sentences and change the segment-posting sentences. Neither quotes the sentence this design changes, so the `from` below is the policy in force. |
| G17. `CONTRIBUTING.md` *What a change to a gate must carry* (read) | A change under `.github/workflows/` carries a test seen red, a stated failure direction, and what it removes. |

## Scope

In:

1. **`.github/workflows/test.yml` runs the legs per base.** The `pytest` job's `include:` holds five entries, ubuntu 3.12 and the four Windows shards, each as it stands. A new job, `pytest-wide`, holds ubuntu 3.14 and macOS 3.12 as `include:` entries as they stand, with `if: ${{ !startsWith(github.base_ref, 'release/') }}`. Its `name` is `pytest (${{ matrix.os }}, ${{ matrix.python }}, ${{ matrix.timeout }})`, so each check name stays the one G7 lists. Its `strategy.fail-fast`, `runs-on` and `timeout-minutes` are those of `pytest`. Its `steps` is an alias of `pytest`'s, anchored there as `&pytest-steps`, so the steps and their comments stand once. `release-report`'s `needs` names `pytest`, `pytest-wide` and `durations`, so the release table reads macOS's and ubuntu 3.14's minutes after their jobs end. The comment above the matrix says where each leg runs, and why, in the present tense, citing #1516.
2. **One reading of "the jobs that run the suite".** `tests/workflows.py` gains a function that returns the jobs of a loaded workflow whose steps run the pytest line. The cases that hold a property of every leg read every such job: the timeouts, the report flags, the install pins, the floor per system, and the rule that `include:` is a matrix's only key and that only Windows entries carry a split or `store`. The cases about the Windows shards, the upload step and the cache steps keep reading `pytest`, where the shards stand.
3. **A case pins which legs each base runs.** It sits in `tests/text/test_ci_gives_the_checks_what_they_need.py`. It holds the `(os, python)` legs of `pytest` and of `pytest-wide` against the owner's decision, `pytest` with no `if`, `pytest-wide`'s `if` and `name` to the strings of *Scope* item 1, `pytest-wide`'s steps equal to `pytest`'s, and the legs of every job that runs the suite to exactly those two jobs' legs, so the union equals the legs G2 lists and a third such job is refused. Its docstring says which legs a pull request into `release/*` runs and which a pull request into `main` runs. `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py:39` holds the new `needs`.
4. **The contributor's documents state the two leg sets.** `CONTRIBUTING.md:32-33` and `:44` and `.github/PULL_REQUEST_TEMPLATE.md:26` say that a pull request into the release branch runs the suite on Linux and Windows, and that macOS and Python 3.14 run on the release pull request. `CONTRIBUTING.md:145-150` says which jobs run on which pull request. The changes go in place, under contract rule 19.
5. **The version moves from 0.37.5 to 0.38.0** in `.claude-plugin/plugin.json`, in the commit that adds `changelog.md` (`frame/plan.md` *Operational impact*).

Out:

- Which legs run. The owner decided it (G1).
- A pull request into a base other than `release/*` or `main`, such as a stacked pull request into a feature branch. It keeps every leg G2 lists, because the decision names `release/*` as where legs go and `!startsWith` changes nothing elsewhere (`frame/plan.md` *Alternatives considered*, A7).
- `.github/scripts/release_report.py` and its tests. The check names stay as G7 lists them, so the reader of G8 needs no change.
- The `durations` job. It reads the Windows parts by the pattern `test-durations-*` and the count 4, and Windows stays in `pytest`. The parts' artifact names change from `test-durations-3` to `-6` to `test-durations-1` to `-4` with `strategy.job-index`, and nothing reads the number.
- `docs/running/the-broad-gate.md:131` and `.github/scripts/run_tests.py:52` (G14).
- Recording the wait after. The orchestrator records it after the release's feature pull requests have run (`frame/plan.md` *Operational impact*). A build commit can carry no run that has not happened.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A feature pull request | Given this work merged into `release/v0.38.0`, when a pull request into it runs `tests`, then `lint`, the `pytest` jobs of *Scope* item 1 and `durations` run, and `pytest-wide` is skipped. | The case of *Scope* item 3, seen red against `test.yml` at `6a3b74ba8`. On GitHub, the orchestrator reads this pull request's own first `pull_request` run with `gh api …/runs/<id>/jobs` (`frame/questions.md` Q1). |
| S2 The release pull request, a push to `main`, a dispatch | Given the same tree, when a pull request into `main`, a push to `main` or a `workflow_dispatch` runs `tests`, then every leg of G2 runs under the names G7 lists, and `release-report` starts after all of them end. | The case of *Scope* item 3 and the `needs` case. On GitHub, the orchestrator reads the release pull request's run for 0.38.0: a `pytest (…)` job for each leg G7 lists, and release table rows for `macos` and `ubuntu 3.14` that hold minutes, not `no run found`. |
| S3 Every leg is held to the same rules | Given a `pytest-wide` entry with no `timeout`, a step list that drops `--no-fold-skipped`, or macOS moved off the floor, when the suite runs, then the cases of *Scope* item 2 fail and name the leg. | Each generalised case seen red with one `pytest-wide` entry or line changed in a scratch copy, as contract rule 15 asks. |
| S4 The steps stand once | Given `pytest-wide`'s `steps` replaced by a copy that differs in one step, when the case of *Scope* item 3 runs, then it fails. | The case, seen red with one step of the copy edited. |
| S5 A contributor reads what their pull request runs | Given `CONTRIBUTING.md` and the pull request template, when a contributor reads them, then they read that their pull request runs Linux and Windows and that macOS and Python 3.14 run on the release pull request. | The proofer reads the sentences of *Scope* item 4 against `test.yml`. |
| S6 The wait is recorded after | Given the release's feature pull requests have run under the new matrix, when the orchestrator reads their first attempts as the step 1 comment did, then #1516 holds the median and the longest wait after, beside 3.7 and 15.3 minutes before. | A comment on #1516 by the orchestrator (`frame/plan.md` *Operational impact*). |
| S7 The version | Given this pull request, when `hygiene`'s `release` job runs on it, then `.claude-plugin/plugin.json` reads `0.38.0`. | The `release` check on the pull request, and `git show HEAD:.claude-plugin/plugin.json`. |

## Data & interfaces

- `test.yml` jobs: `lint`, `pytest`, `pytest-wide`, `durations`, `release-report`. Job ids are new. The check names are not (G7).
- `pytest-wide.if`: `${{ !startsWith(github.base_ref, 'release/') }}`. `github.base_ref` is empty on `push` and `workflow_dispatch`, so the expression is true there.
- `release-report.needs`: `[pytest, pytest-wide, durations]`.
- `tests/workflows.py`: `pytest_jobs`, returning the jobs that run the pytest line, beside `load`; `job_scripts` and `RUNS_PYTEST` move to it from `tests/text/test_ci_gives_the_checks_what_they_need.py`, whose `runs_pytest` becomes the filter inside `pytest_jobs`.

## Rule changes

- change
  file: docs/releasing/release-checklist.md
  section: The release pull request
  from: Opened after the last merge, it
    runs `tests` once, on the tree the release ships, and what runs only on a
    pull request into `main` answers once: `release-report`, and the
    `hygiene` workflow's version and milestone steps.
  to: Opened after the last merge, it
    runs `tests` once, on the tree the release ships, and what no pull
    request into `release/vX.Y.Z` runs answers once: the `tests` workflow's
    ubuntu 3.14 and macOS legs, `release-report`, and the `hygiene`
    workflow's version and milestone steps. A defect that only the ubuntu
    3.14 or the macOS leg meets is fixed by a pull request into
    `release/vX.Y.Z`, which the release pull request's next run reads.
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: The `pytest`
    job is not required. Its check names carry the matrix values, so a
    required name is a copy of `test.yml` that stops matching when the matrix
    changes,
  to: Neither `pytest` job, `pytest` nor `pytest-wide`, is required. Their
    check names carry the matrix values, so a required name is a copy of
    `test.yml` that stops matching when the matrix changes,

## Removes

This work adds a CI job, its condition, the case of *Scope* item 3, and `tests/workflows.py#pytest_jobs` in the place of `tests/text/test_ci_gives_the_checks_what_they_need.py#runs_pytest`, with the cases of `tests/test_workflows.py#Test_pytest_jobs` that hold it. In return it removes the two legs from every pull request into `release/*`.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The ubuntu 3.14 and macOS legs on a pull request into `release/*` | `.github/workflows/test.yml`, `jobs.pytest.strategy.matrix.include`, the second and third entries | `jobs.pytest-wide`, which runs everywhere but a pull request into `release/*`. Their catch record on feature pull requests: macOS met no defect, and its six failed attempts were one run no runner took (G11). ubuntu 3.14 never failed where ubuntu 3.12 passed (G12). Their cost was every long wait (G11, G13). |
| "Every push to an open pull request runs the suite on Linux, macOS and Windows" | `CONTRIBUTING.md:32-33` | Rewritten in place with the leg set per base (*Scope* item 4). |
| "CI runs the rest, on three platforms." | `CONTRIBUTING.md:44` and `.github/PULL_REQUEST_TEMPLATE.md:26` | Rewritten in place (*Scope* item 4). |
| The cases' reading of `jobs["pytest"]` alone for a property of every leg | `tests/text/test_ci_gives_the_checks_what_they_need.py:349` and `:372`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py#pytest_job`, the include-only reading of `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#matrix_entries`; `tests/text/test_ci_gives_the_checks_what_they_need.py#runs_pytest` | `tests/workflows.py#pytest_jobs`, which those cases read; in the shards module `entries_of` and `suite_entries` read every job that runs the suite, and `matrix_entries` stays for the cases that read `pytest`'s shards alone. |

Framed 2026-11-12 by framer, before the build.
