# Implementation Plan: 1794465688-feature-prs-wait-on-the-macos-runner

## Technical context

The tree as read at `6a3b74ba8`.

`.github/workflows/test.yml` has one `pytest` job whose matrix is `include:` alone, each entry one job (`frame/design.md` G2). GitHub evaluates a job's `if` before the matrix expands, and the `matrix` context is not available there (G3). An `exclude:` runs before `include:`, so it removes no include entry (G4). The legs therefore cannot be chosen per base inside the one job. The approach is to split the legs into two jobs and to put the condition on the job that holds the two legs a feature pull request drops.

What the approach builds on:

- The steps of `pytest`, from `test.yml:82` to the job's end, run unchanged on every leg. They read `matrix.split` and `matrix.store`, which are empty on the ubuntu and macOS entries today, so `pytest-wide` runs them as those entries run them now.
- GitHub reads YAML anchors and aliases in a workflow (G5), and PyYAML's `BaseLoader` resolves an alias to the anchored list (G6). The cases see the same steps under both jobs.
- The release table names a leg by the check name (G8). An explicit `name` on `pytest-wide` keeps those names (G7), so neither side of the table changes.
- No `pytest` check is required by either ruleset (G9), so a skipped `pytest-wide` holds no merge.
- A `pull_request` run reads the workflow from the pull request's merge commit, so this pull request's own run is the first under the new matrix, and each later pull request of the release uses it on its first run after this one merges. This is read from GitHub's documented behaviour and not run here; Q1 of `frame/questions.md` has the orchestrator confirm it on this pull request's run.

Failure scenario of the chosen approach, six months on: a leg added later goes into the wrong job and runs where the decision did not mean it to. The case of *Scope* item 3 holds each job's legs and fails on that edit. A second: someone replaces the alias with a copy of the steps and edits one copy. The same case holds the two jobs' steps equal. A third: GitHub withdraws anchor support. The workflow then fails to parse, and every run fails at once. That fails loudly, and it is not a silent leg.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Two jobs. `pytest` keeps ubuntu 3.12 and the four Windows shards. `pytest-wide` holds ubuntu 3.14 and macOS with `if: ${{ !startsWith(github.base_ref, 'release/') }}`, steps aliased from `pytest`, named as today. | The three scenarios in *Technical context*: a leg in the wrong job, a copy in place of the alias, anchors withdrawn. The case catches the first two, and the third fails every run at once. A skipped `pytest-wide` shows as one skipped check on a release branch's pull request, whose displayed name GitHub decides (Q1). | Chosen. It keeps each matrix include-only, which `matrix_entries` already holds. It adds no job to the path every run waits on. It keeps every check name and every reader of them. |
| A2. A first job computes the matrix as JSON from the base ref, and `pytest` reads `fromJSON(needs.<job>.outputs.matrix)`. This replaces the static `include:` list. | The first job sits on the path of every run, before any leg starts: a runner's queue plus a checkout, added to the median that this work is meant to cut. Where that job fails, no leg runs. The leg list moves from YAML into a script, and each reader of G10 reads the script's output. | Rejected. It costs every run the time the change exists to save, and the premise that keeps the static list holds: the two leg sets are fixed, and only the base ref chooses between them. |
| A3. `include: ${{ fromJSON(startsWith(github.base_ref, 'release/') && '[…the five…]' \|\| '[…every leg…]') }}`, the whole matrix as an expression. | The entries both lists share are written twice, inside JSON strings. PyYAML returns the matrix as one string, so each reader of G10 parses JSON out of an expression. | Rejected: two sources for the shared entries, and every reader reads text where it reads a parsed list now. |
| A4. A matrix `exclude:` keyed on the base ref. | Exclude runs before include, and an include entry that matches no remaining combination becomes a new job (G4). The excluded legs come back. Making it work means rewriting the entries as axes with include entries that augment them. | Rejected: it does not remove the legs. This confirms the orchestrator's claim. |
| A5. A step-level `if` on `matrix.os` that skips every step of the two legs. | The job still waits for its runner before it skips anything, and the macOS queue is the whole cost (G11). | Rejected. |
| A6. Two jobs with the steps copied, not aliased. | About ten steps and their comments stand twice. A case that holds the copies equal is a copy kept in step by a check. | Rejected for A1's alias. |
| A7. The condition `github.event_name != 'pull_request' \|\| github.base_ref == 'main'`. | It also drops the two legs from a pull request into any other base, such as a stacked pull request into a feature branch, which the owner's decision does not name. | Rejected. `!startsWith(github.base_ref, 'release/')` drops them where the decision drops them and keeps every leg of G2 everywhere else. On `push` and `workflow_dispatch`, `github.base_ref` is empty, and the expression is true. |
| A8. `pytest-wide` under its default name, `pytest-wide (…)`, with `release_report.py#PYTEST_JOB` widened to read it. | One reader and its tests change. The documents that say the check names carry the matrix values then describe two name shapes. | Rejected for A1's one `name` line, which keeps the names G7 lists. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1 to 5 of `frame/design.md`. The version move of item 5 is made in the commit that adds `changelog.md`. | The case of *Scope* item 3 seen red against `test.yml` at `6a3b74ba8`, and each generalised case of *Scope* item 2 seen red with one `pytest-wide` entry or line changed (S3, S4). Run narrowly: `bin/test tests/text/test_ci_gives_the_checks_what_they_need.py tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py tests/behaviour/test_release_hygiene.py tests/test_workflows.py tests/github/test_release_report.py -q`. The GitHub side is S1 and S2, read by the orchestrator. | |

## Overlap with the release

The spawn named three other work items. When this frame was written, #1510's frame stood at `d742802f6` and #1496's at `c368121de`, each on its branch, and #1494's branch held its `routing.md` alone (executed, `git log` and `git diff --stat 79f815a74...<branch>`), so #1494 is judged from its issue. #1510 changes `skills/verify/scripts/session_cost.py`, its tests and `skills/verify/orchestration.md`, and meets nothing this work changes or reads.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1494 | Its `seal pr-wait` reads the checks a pull request's run reports. This work changes that set: on a pull request into `release/v0.38.0`, only the `pytest (…)` checks of `frame/design.md` *Scope* item 1 run and `pytest-wide` reports as skipped. | #1516 | `pr-wait` is then built and tested against the check set every later pull request of the release shows, a skipped check among them, and needs no second pass when this lands. The milestone orders #1494 last for the same reason. |
| #1496 | Both designs carry a rule change on `docs/releasing/branch-and-release.md`. #1496's design, at `c368121de`, changes *Cutting a release*. This work changes *Work accumulates on a release branch*. | #1516 | The milestone orders #1516 first. The two operations quote different text in different sections, so the settle applies both in either order. No file of the tree is changed by both pull requests: #1496's frame names `.github/scripts/publish_release_note.py`, `.github/scripts/release_seal.py` and their tests. |

A later pull request of the release needs no merge of the release branch to run under the new matrix: its next `pull_request` run reads the merge commit with `release/v0.38.0`, which then holds this work.

## Operational impact

- **The version moves from 0.37.5 to 0.38.0.** This is the first pull request into `release/v0.38.0`. Phase 1's crafter moves `.claude-plugin/plugin.json` in the commit that adds `changelog.md` (*Scope* item 5).
- **What a feature pull request waits on changes.** A pull request into `release/*` runs the `pytest` jobs of `frame/design.md` *Scope* item 1 and not the two of `pytest-wide`. The release pull request into `main` is now the first run of ubuntu 3.14 and macOS on the release's code, and a defect only those legs meet is fixed by a pull request into the release branch (the first operation of `frame/design.md` *Rule changes*).
- **The wait after is recorded by the orchestrator, once.** It reads the first attempts of the `pull_request` runs into `release/v0.38.0` once the release's last feature pull request (#1494) has merged and before it opens the release pull request. This pull request's own first run is the earliest of them. It measures as the step 1 comment did, from a run's creation to its last job, and posts the count of runs, the median and the longest wait as a comment on #1516, beside 3.7 and 15.3 minutes. A Windows shard was the last job in 95 of the 102 runs before (G13), so the median should move little, and the longest wait is the figure the change is for. The comment answers *Done when*'s third item, which no build commit can, because the runs it reads happen after this pull request opens.
- No migration, no new environment variable, no new dependency.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
