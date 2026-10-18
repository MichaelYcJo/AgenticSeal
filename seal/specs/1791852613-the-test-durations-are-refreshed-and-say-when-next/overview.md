# 1791852613-the-test-durations-are-refreshed-and-say-when-next — overview

<!-- The closing memo (implement skill, step 4). Opened at phase 1's first
divergence; closed by phase 3. -->

## Why this work exists

`.test_durations` reached 9.4 % unpriced with nothing saying so; a case now
fails past one in twenty, a release box schedules the refresh, and the file
is refreshed by the recipe.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| What counts as the whole collection | `plan.md` §*Declining a partial collection*: "when no argument of `session.config.invocation_params.args` resolves to the `tests` directory, it skips". The code reads `config.args`, which pytest fills with the invocation directory when no path is named, and accepts the repository or `tests` there, with `config.rootpath` the repository's | the code | `seal/config.md`'s `Broad gate` row is `uvx ruff check . && uvx ruff format --check . && bin/test -q`, which names no path, so the plan's rule would skip the case in the one local run of the whole suite. Executed 2026-10-13: `bin/test -q -k test_the_durations_file_prices_the_suite` runs the case. The rootpath condition keeps the plan's third six-month risk (pytest run from inside `tests/`) declining |
| One pure function | `spec.md` §*Data & interfaces*: "one pure function over `(collected, durations)` returning the unpriced ids". The code has `unpriced` (that function) and `staleness` (the share comparison and the sentence) | the code | S2 asks for fixture cases at the boundary; the comparison has to live in a function they can call, and `unpriced` alone holds no boundary |
| The artifact's name | The recipe in `CONTRIBUTING.md` names none | `test-durations` | `actions/upload-artifact@v4` defaults to `artifact`; phase 2's `gh run download <id> -n <artifact>` needs a name somebody can read |
| The test ids, which the spec did not name | `spec.md` S1 asks for zero unpriced cases at the restore commit, and `spec.md` §*Data & interfaces* names no test module beyond the shard module and `conftest.py`. The first refresh left 213 ids unpriced on POSIX: 205 built from a path that Windows writes with `\`, and 8 holding `sys.executable`. Round 1's 🟡 1 took the root fix, which touches six modules outside the frame's list | the root fix | Without it, S1 cannot hold on two legs of three, and the `STALE_SHARE` ground, a whole cycle of growth under the share after a refresh, holds on Windows alone. After `fa4e9cce` and run 38342987499 the count is zero on POSIX, and by construction on Windows too, because the file is Windows' own collection |
| The recipe's `store` value | `spec.md` Out: "Removing the 838 dead entries by hand. The refresh replaces the whole file". Without `--clean-durations`, `pytest-split` 0.11.0 merges into the old file, so the first refresh kept 625 entries | `--clean-durations` added to the recipe | `spec.md` assumed the refresh replaced the file, and the flag is what makes that true. Nothing edits the file by hand. Run 38342987499's file has 13,482 entries and none that the suite does not collect |
| One ledger row per scenario | `plan.md` phase 3: "one row per S1–S7". The fragment has S1–S6 and no S7 | S1–S6 | S7's claim is that the records exist. Its only coordinate would be this directory's `overview.md`, which `settle --retire-process` removes after the release, so the row would break. `evidence-check --strict` exiting 0 is S7's evidence |

## Not verified

| Item | Who must answer |
|---|---|
| The whole suite at the branch's final SHA | the sealer, once, after the review rounds |
| closed That the measuring run finishes inside 55 minutes and uploads `.test_durations` | run 38332345615 at 9ec6faca, read in phase 2 on 2026-10-13: the Windows job took 37 m 21 s and the artifact `test-durations` was there |
| closed That the hook sees the whole collection on GitHub's shards (`questions.md` Q4) | read in phase 3 on 2026-10-13: macOS group 3 of run 38332345615 read 1,276 of 13,480 collected cases, and run 38335775781's seven shards are green |
| That GitHub reads the budgets at the final SHA | the pull request's run at the final SHA |

## Not done

Phase 2 found two problems with the first refresh: 213 ids spelled per
machine, and a recipe that merges instead of replacing. Both were fixed in
this work by round 1's fix pass. Neither is left for an issue.

- **No leg refuses a path id that omits `posix_id`.** A future
  parametrization of paths that omits `ids=posix_id` passes on POSIX. It
  shows up only as cases that are unpriced on ubuntu and macOS after the
  next refresh, and the staleness case reports those only once they reach
  `STALE_SHARE`.
  Refusing a backslash across the collection is not possible, because 1,645
  POSIX ids carry one from escaped characters (round 1's report).

Not built here either: the `workflow_dispatch` input that measures without
a commit (`plan.md` Alternatives E). `spec.md` Out named it as the design to
adopt when the per-release refresh proves costly.

## Fed back into the spec

none
