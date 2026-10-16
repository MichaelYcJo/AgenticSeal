# 1791876665-each-budget-ratchets-and-every-pull-request-measures-it — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 8b5dcd53 |
| Ran by | smith on Opus 5.5, as `routing.md`'s models line gives it |

## What this phase was asked

Mark `questions.md` Q6 answered by the orchestrator on 2026-10-14: the price
level row is accepted because the literal decision fails every pull request
after a refresh. Then build phase 3 and stop before phase 4: the
`ci-minutes:*` rows; the `budgets` job in `test.yml` (`needs: pytest`, `if:
!cancelled()`, `permissions: actions: read`); the jobs reader, the per-leg
sum and the billable line; T11 and T14; `CONTRIBUTING.md`'s "CI runs five
jobs" rewritten in place. Apply the owner's approved default for #929 Q2: a
per-run row is one-sided, a ceiling and no lower band, and say here how a
cleanup is recorded for these rows instead. Take #931's change to
`tests/test_ci_gives_the_checks_what_they_need.py` into account without
copying it: give the `budgets` job what the case on this branch asks, or note
the textual merge. The phase's verification is this pull request's run, read
by the orchestrator after the push.

## What this phase found

**The frame holds, with two readings settled.** The jobs endpoint, the job
names and the token scope are as `plan.md` §*Technical context* says. Read on
the live API (`executed`, `gh api …/runs/38477758775/jobs --paginate --jq
'.jobs[]'`, a run of #931's branch): every job is one JSON object a line; a
pytest job's name is `pytest (<os>-latest, 3.12, [<split>,] <timeout>)`; its
`runner_name` is `GitHub Actions <n>`, which carries no operating system, so
the leg is read off the name. A run still going has pytest jobs with no
`completed_at`, which the reader refuses at exit 2: the `budgets` job reads
the run after `needs: pytest` has let every leg end.

1. **`--ci-jobs FILE`, not `--ci-run ID`.** The workflow step fetches the job
   list with the job's token and hands the file over, so the checker reads
   no network and a case drives it from a file. With the flag it holds the
   run's rows alone; without it, the tree's run, in the hygiene step and in
   the suite case, shows those rows as `not this run`.
2. **The `budgets` job carries `fetch-depth: 0`, which it does not use.**
   On this branch `test_every_job_that_runs_pytest_has_the_whole_history`
   picks a job by the word `pytest` in its text, and `needs: pytest` is that
   word. #931's branch picks by a line that invokes pytest, a name this
   branch does not have (NAME NOT IN TREE: `RUNS_PYTEST`).
   Whichever of the two pull requests lands second meets the other's change
   in that module and in `test.yml`, and with #931's rule in place the
   setting can go. The job's comment says this.

Each is a row of `overview.md` §*Where spec and implementation diverged*.

**One-sided, and where a cleanup goes instead.** A `ci-minutes` row's slack
cell reads `one-sided`; it fails a run over its ceiling and asks for no
lower ceiling under it, and no other family may write `one-sided`. A cleanup
that makes the suite cheaper therefore leaves the ceiling where it was, and
recording it is not the pull request's job. It is the release's: phase 4's
`--trend <tag>` prints each budget against the last release, and
`docs/release-checklist.md` §2 gains the step that reads that line, so a
ceiling far over the minutes a release's runs took is lowered there, with
the runs it rests on, once per release rather than on one noisy run.

**The numbers** (`executed`, the checker run with `--ci-jobs` on run
38477758775's job list): ubuntu 6.9, Windows 42.4 and macOS 22.7 minutes,
under 15, 59 and 32; billable 7 × 1 + 44 × 2 + 24 × 10 = 335 Linux-equivalent
minutes, US$2.68 at the $0.008 #929 read. The ceilings are the frame's
(1.3 times the largest of 12 runs, 2026-10-13), not re-derived here: a run
of this branch is the orchestrator's to read. On run 38479956336, still
going when it was fetched, the reader refused at exit 2 naming the macOS
job with no end time.

**Every case seen red** (`executed`, `bin/mutation-check` on committed
trees, 21 mutations, every one `red`). T11: the leg read off `runner_name`,
the Windows and macOS multiples swapped, jobs not rounded up to their
minute, a leg read as its longest job, a lower band put back on run rows.
An unknown leg priced. The tree's run measuring run rows, and the run's job
holding every row. The refusals: `one-sided` not tied to run rows, an
unknown leg, a run row in another unit, a leg the run lacks, a job line that
is no JSON, a nameless job, a job with no end read, a job list read for no
row, a missing job list. T14: the `budgets` job without `needs: pytest`,
without `actions: read`, without `if: ${{ !cancelled() }}`, and the hygiene
step without `--baseline`.

**`CONTRIBUTING.md`** says six jobs now, the sixth being each leg's minutes
against its row. Nine released rows cite its §*Running the checks*; each was
read, none claims the count, and each has a `Re-read ·` row in the fragment.

**Owed at the push.** The `budgets` job on this pull request's `tests` run:
that it runs after the legs, that the token reads the job list, and that its
summary shows the three legs against 15, 59 and 32 with the billable line.
