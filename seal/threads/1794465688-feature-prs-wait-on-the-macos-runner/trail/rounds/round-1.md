# Review round 1: 1794465688-feature-prs-wait-on-the-macos-runner

```seal
target: 8cca6ed80 against release/v0.38.0
```

The range is `79f815a74..8cca6ed80`, eight commits. No earlier round
stands, so nothing was carried from one. These frame facts were carried and
not established again: GitHub's contexts and matrix references (design G3,
G4, G5), the rulesets that require no `pytest` check (G9), and the counts of
the owner's comment on #1516 (G11 to G13). Every verdict below is this
round's own. Every run was made in a `git clone --no-local` of the
repository at `8cca6ed80`, under the round's scratch directory.

Two sentences are no finding and are named here. `CONTRIBUTING.md:168`
says "Each `pytest` leg in `test.yml` carries a `timeout-minutes`". It is
still true of `pytest`'s legs, and it is silent on `pytest-wide`'s, which
`test_every_pytest_leg_has_a_timeout_and_the_job_reads_it` now holds as
well. The comments at `tests/conftest.py:248` and
`tests/text/test_the_suite_runs_with_gh_logged_out.py:6` keep "CI's pytest
job" in the singular, a wording the build changed to plural at
`CONTRIBUTING.md:189`. Each still reads true of both jobs. The comments at
`.github/workflows/test.yml:193-197` and `:247-249` were rewrapped unevenly.
Line 196 breaks mid-sentence after eight words, and line 248 runs past 100 columns. They
read badly and say nothing false.

## Findings

### 1. `Test_pytest_jobs` holds a case that its own sibling case and the six whole-history cases already hold

```seal
severity: should
location: `tests/test_workflows.py:115-119`
evidence: read `tests/test_workflows.py:80-119`, `tests/text/test_ci_gives_the_checks_what_they_need.py:132-185`; executed `bin/seal layout --pairs`
```

Why it matters: the case adds a run and a fixture read to the suite, and it
can fail only where another case already fails. Two cases already hold it.

`test_refuses_a_job_that_names_pytest_and_runs_nothing` asserts that
`pytest_jobs` returns neither `reads-a-part` (`needs: pytest`) nor
`comments-on-it` (pytest named only in a shell comment). Its sibling,
`test_accepts_each_job_whose_script_runs_pytest_in_the_file_s_order`, reads
the same `SUITE_JOBS` fixture. At `tests/test_workflows.py:112` it asserts
`list(found) == ["first", "second"]`, and that equality fails wherever either
decoy is returned. Outside the class, the six
`test_a_job_that_calls_pytest_any_way_is_held_to_the_whole_history` cases
(`tests/text/test_ci_gives_the_checks_what_they_need.py:161-185`) build a
`needs: pytest` job and a job whose only pytest is in shell comments. Each
decoy has a shallow checkout, and each case asserts
`shallow_pytest_jobs(...) == [job]`. `shallow_pytest_jobs` (`:132`) now
iterates `pytest_jobs`, so a decoy that `pytest_jobs` returned would be
listed there too. `gaps.md:20-24` says those six cases reach the regex
through `pytest_jobs`.

The case holds a fact the frame states (design *Scope* item 2: the function
returns the jobs whose steps run the pytest line), so the exception of
`skills/code-review/SKILL.md` *The record* for a case holding no frame fact
does not apply. `bin/seal layout --pairs` names no pair for either module.
The first case does cover something no other case covers: a job whose
pytest stands on the second line of a `run: |` block, together with the
file's order and the identity of the returned job.

Remove the case. The fixture comment at `tests/test_workflows.py:77-79`
stays true, and the first case's docstring then says that it refuses the
decoys:

```python
class Test_pytest_jobs:
    def test_accepts_each_job_whose_script_runs_pytest_in_the_file_s_order(
        self, tmp_path
    ):
        """The jobs that run the suite are read by what their scripts run,
        so a leg moved into a job of another name is still read (#1516), and
        a job that names pytest in `needs:` or in a shell comment is not."""
        path = tmp_path / "fixture.yml"
        path.write_text(SUITE_JOBS, encoding="utf-8")
        loaded = workflows.load(str(path))
        found = workflows.pytest_jobs(loaded)
        assert list(found) == ["first", "second"], list(found)
        assert found["second"] is loaded["jobs"]["second"]
```

### 2. The title judgment `chore:` does not stand on the prefix table it cites

```seal
severity: should
location: `seal/threads/1794465688-feature-prs-wait-on-the-macos-runner/frame/plan.md:60`, `seal/threads/1794465688-feature-prs-wait-on-the-macos-runner/pr.md:5`
evidence: read `skills/commit-pr-convention/SKILL.md:130-174`, `seal/threads/1794465688-feature-prs-wait-on-the-macos-runner/frame/plan.md:60`, `.github/workflows/test.yml:176-191`, `CONTRIBUTING.md:31-46`
```

Why it matters: the squash merge takes the pull request's title. The
sealer's step 4 reads the title against the table, so a wrong prefix comes
back as a disagreement at the seal, after the rounds have settled.
`pr.md:5` quotes the judgment, so it reaches the body as well.

The row judges `chore:` because "nothing the plugin ships to a user
changes" and "the issue was filed as `chore:`". The table at
`skills/commit-pr-convention/SKILL.md:130-141` asks what "whoever meets it
after the merge, a user or a party working on a later change" meets.
`chore:` there is "upkeep that changes nothing anyone meets". Someone does
meet this change. Every contributor's pull request into `release/*` now
reports a different set of checks and waits on no macOS runner
(`test.yml:177`). The party preparing a release now meets the macOS and
ubuntu 3.14 legs for the first time on the release pull request, and fixes
what they meet on the release branch (design *Rule changes*, first
operation). The `refactor:` row, "the same kinds of outcome, reached another
way", lists as an example "a gate retired because what it caught did not
outweigh its cost". That example describes this change: the two legs leave
the feature pull request because they caught nothing there and caused every
long wait (design G11 to G13). The second ground does not stand either.
`:173-176` says the issue's title follows the pull request's prefix, and
the pull request's prefix does not follow the issue.

The row of `frame/plan.md` *Judgments of the run*:

```markdown
| 2026-11-12 | The title takes `refactor:` | The diff retires the ubuntu 3.14 and macOS legs from every pull request into `release/*` because, on those pull requests, they caught nothing and caused every long wait (`frame/design.md` G11 to G13). That is the table's `refactor:` example "a gate retired because what it caught did not outweigh its cost". A contributor's pull request and the release pull request meet the change, so it is not `chore:`, and `CONTRIBUTING.md`'s rewrite, `docs:`, stands lower in the table | `skills/commit-pr-convention/SKILL.md` |
```

`pr.md:5` then quotes "The title takes `refactor:`". By the same file's
`:173-176`, the orchestrator retitles #1516 when it titles the pull request.
The fix pass owes that act, and this snippet does not cover it.

### 3. The closing memo waits for the release pull request to run `pytest-wide`, when a dispatch on this branch runs it before the merge

```seal
severity: should
location: `seal/threads/1794465688-feature-prs-wait-on-the-macos-runner/gaps.md:9`, `seal/threads/1794465688-feature-prs-wait-on-the-macos-runner/trail/phases/phase-1.md:100-102`
evidence: read `.github/workflows/test.yml:3-12`, `.github/workflows/test.yml:177`, `seal/threads/1794465688-feature-prs-wait-on-the-macos-runner/frame/design.md:61`; executed `gh api repos/{owner}/{repo}/actions/runs/43143655875/jobs`
```

Why it matters: the row tells the orchestrator that the first run of
`pytest-wide` is the release pull request for 0.38.0. `pytest-wide` is the
one job of this work that nothing runs before the merge. A defect in its
check names, its alias or its `name` expansion would then first show on the
release pull request, after every feature pull request of the release has
merged on top of it, and its fix would be one more pull request into the
release branch.

`phase-1.md:100-102` says "The first run of `pytest-wide` is on the release
pull request for 0.38.0, not on this pull request", and `gaps.md:9` names
that run as the answer. But `test.yml:12` takes `workflow_dispatch:`, and
its comment at `:8-11` says what a dispatch on a pushed branch is for.
`github.base_ref` is empty on a dispatch (design *Data & interfaces*,
`:61`), so `pytest-wide`'s `if` at `:177` is true there, and a dispatch of
`tests` on this branch runs both of its legs from this branch's `test.yml`.
The phase record is the crafter's history and stays as written. The row in
`gaps.md` is where the fix lands.

Half of the row is already settled. Run 43143655875, a push to `main`, ran
the steps `pytest-wide` now aliases on two entries that defined neither
`split` nor `store`: job 130936327013 (`pytest (macos-latest, 3.12, 10)`)
and job 130936327217 (`pytest (ubuntu-latest, 3.14, 5)`). In each, the
cache restore and the upload were `skipped`, and the pytest step ran as
`pytest tests/ -q -n auto --durations=50 -rfEs --no-fold-skipped` with two
empty expansions after it. A matrix context lacking a key behaves the same
on any entry, so what is left for a run is the check names and GitHub's
reading of the alias.

```markdown
| whether GitHub reads the `&pytest-steps` alias for `pytest-wide` and its legs report under the names G7 lists. The cache restore and the upload skip, and the pytest line ends with two empty expansions, on an entry with no `split` or `store`, as run 43143655875 showed (round 1). actionlint 1.7.12 reports the same two properties as undefined, and it is not a check of this repository | the orchestrator, from a `workflow_dispatch` run of `tests` on this branch before the pull request merges (`gh workflow run test.yml --ref chore/1516-feature-prs-wait-on-the-macos-runner`, then `gh api …/runs/<id>/jobs`): `github.base_ref` is empty on a dispatch, so `pytest-wide` runs |
```

### 4. The design says the work adds one case, and the target adds three

```seal
severity: should
location: `seal/threads/1794465688-feature-prs-wait-on-the-macos-runner/frame/design.md:94`
evidence: executed `git diff --stat 79f815a74..8cca6ed80`; read `tests/test_workflows.py:103-119`, `tests/text/test_ci_gives_the_checks_what_they_need.py:379-410`
```

Why it matters: the sentence opens `## Removes`, which is the answer
`CONTRIBUTING.md` *What a change to a gate must carry* asks for: what a
change adds against what it removes. The sealer weighs that answer, and the
settle reads it. The fold at `9e97fbfbd` rewrote the table row under the
sentence to name `pytest_jobs`, but not the sentence above it.

`frame/design.md:94` says "This work adds a CI job, its condition and one
case." The target adds the legs case
`test_a_pull_request_into_a_release_branch_runs_ubuntu_3_12_and_windows`
and the two `Test_pytest_jobs` cases. It also adds
`tests/workflows.py#pytest_jobs`, which replaces `runs_pytest`. With
finding 1 applied, the work adds two cases.

```markdown
This work adds a CI job, its condition, the case of *Scope* item 3, and `tests/workflows.py#pytest_jobs` in the place of `runs_pytest`, with the case of `tests/test_workflows.py#Test_pytest_jobs` that holds it. In return it removes the two legs from every pull request into `release/*`.
```

## Confirmations

What matched: *Scope* item 1 holds at `.github/workflows/test.yml:35-191`.
`pytest`'s `include:` holds ubuntu 3.12 and the four Windows shards as they
stood. `pytest-wide` holds ubuntu 3.14 and macOS 3.12 with the `if`, the
`name`, `fail-fast`, `runs-on` and `timeout-minutes` the design gives, and
`steps: *pytest-steps` against the anchor at `:87`. `release-report` needs
`[pytest, pytest-wide, durations]` at `:254`, and its `!cancelled()` at
`:255` keeps it running whatever those jobs conclude. The explicit `name` at
`:178` spells the check names of design G7 for the two moved legs, which
the pattern of `.github/scripts/release_report.py:79-80` reads unchanged
(read).

What matched: the crafter weighed actionlint as the hand-back says, and the
weighing holds. Run over `test.yml`, actionlint 1.7.12 exits 1 with the
three lines at `:133:13`, `:153:82` and `:162:25`. `git grep -n -i
actionlint` finds no reference outside `seal/threads/`, so no check of this
repository runs it. Run 43143655875 shows that an entry without `split` and
`store` runs these steps correctly (finding 3). Adding `split: ""` and
`store: ""` to `pytest-wide` would fail
`test_every_group_of_each_sharded_leg_runs_exactly_once` at
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:123-124`,
which refuses the `split` key itself and not only a non-empty value. Leaving
the code as it is and reporting the refusal is what contract rule 18 asks
(executed).

What matched: phase 1's seen-red claim for the two cases that pin the new
behaviour holds. With `test.yml` taken from `fc4ed4f9f`, the legs case
failed on its `legs ==` assertion, holding all seven legs in `pytest`, and
the `needs` case failed with `['pytest', 'durations']`. The other 38 cases
of the four modules passed (executed). The twelve mutant rows at
`phase-1.md:118-131` were read against the cases: each failing line the
table names stands in the case it names at `8cca6ed80`. They were not run
again (read).

What matched: *Scope* item 2 holds. The timeout, report-flag, install-pin
and floor cases iterate `pytest_jobs` (`tests/text/test_ci_gives_the_checks_what_they_need.py:312-360`,
`tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:26-32`).
The split and store rules read every suite job through `suite_entries`
(`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:75-103`),
and the shard, upload and cache cases from `:127` on keep reading
`job("pytest")` (read). `job_scripts` and `RUNS_PYTEST` moved unchanged except the comment's
history clause, and `git grep -n runs_pytest` finds two case names and no
definition or call (executed).

What matched: *Scope* items 4 and 5. `CONTRIBUTING.md:31-46` and `:147-155`
and `.github/PULL_REQUEST_TEMPLATE.md:25-28` state the two leg sets as
`test.yml` runs them. `.claude-plugin/plugin.json` reads `0.38.0` and moves
in `d3e644ca3` beside `changelog.md`, and no other file holds `0.37.5` outside
`seal/threads/` and `CHANGELOG.md` (executed).

What matched: the work item's records were read whole at `8cca6ed80`. The
two `from:` passages of design `## Rule changes` stand word for word at
`docs/releasing/release-checklist.md` *The release pull request* and
`docs/releasing/branch-and-release.md` *Work accumulates on a release
branch*. Each of `pr.md`'s five quotes stands word for word at the
coordinate it names. `changelog.md` says nothing `test.yml` or the cases
contradict. With `Commit and pull request language` English, no
`pr.<lang>.md` is owed (read). Apart from findings 2 to 4, no sentence of
`routing.md`, the frame, `gaps.md`, `changelog.md` or `pr.md` is
contradicted by the target.

What matched: the hand-back labels the suite honestly. `gaps.md:7` leaves
the suite, the lint and the format check beyond phase 1's boundary set to
the orchestrator's broad gate. The plan row's narrow command passes at
`8cca6ed80`, and ruff's check and format pass on the six changed Python
files (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub accepts the `&pytest-steps` alias, runs `pytest`'s five legs and skips `pytest-wide` on this pull request's first run, and how the skipped check is named | `frame/questions.md` Q1, `gaps.md:8` | the orchestrator, from this pull request's first `pull_request` run |
| The suite, the repository-wide lint and the format check at HEAD | `gaps.md:7` | the orchestrator's broad gate |
| The release table's minutes for `macos` and `ubuntu 3.14` with `release-report` waiting on `pytest-wide` | design S2 | the orchestrator, from the release pull request's run for 0.38.0 |
| The wait after the change | design S6, `frame/plan.md` *Operational impact* | the orchestrator, after #1494 merges |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_ci_gives_the_checks_what_they_need.py tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py tests/behaviour/test_release_hygiene.py tests/test_workflows.py tests/github/test_release_report.py -q` | exit 0: 111 passed, 1 skipped |
| `git checkout fc4ed4f9f -- .github/workflows/test.yml`, then `bin/test` over the first four of those modules `-q -p no:xdist`, then `git checkout HEAD -- .github/workflows/test.yml` | exit 1: the legs case and the `needs` case failed, 38 passed, 1 skipped; the clone's status was clean afterwards |
| `uvx ruff check` and `uvx ruff format --check` over the six Python files the range changes | exit 0 and exit 0 |
| `uvx --from actionlint-py actionlint -shellcheck= .github/workflows/test.yml` (1.7.12) | exit 1: `property "split" is not defined` at 133:13 and 153:82, `property "store" is not defined` at 162:25 |
| `git grep -n -i actionlint 8cca6ed80 -- ':!seal/threads'` | no line |
| `gh api repos/{owner}/{repo}/actions/runs/43143655875/jobs` | the macOS 3.12 and ubuntu 3.14 jobs: cache restore `skipped`, upload `skipped`, pytest step run with the flags alone, both `success` |
| `bin/seal layout --check tests/test_workflows.py` | exit 0, one report: `job_scripts` has no class `Test_job_scripts` |
| `bin/seal layout --pairs` | no pair names `tests/test_workflows.py` or the CI case module |
