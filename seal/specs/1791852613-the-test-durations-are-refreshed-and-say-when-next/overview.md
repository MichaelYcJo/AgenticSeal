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
| Unpriced after the refresh | `spec.md` S1: "prices every case the tree at the restore commit collects, so the count of unpriced cases is zero there". At `3d2324ce` the count against the POSIX collection is 213 (1.58 %) | the file as downloaded | The 213 are parametrized cases whose ids carry a path (`[agents/framer.md-1]` here, `[agents\\framer.md-1]` on Windows). The file is the Windows leg's by policy (`CONTRIBUTING.md` §*Running the checks*), so they are priced under their Windows ids and cannot be priced under their POSIX ones by this recipe. The case is green at 1.58 % |
| The dead entries | `spec.md` Out: "The 838 dead entries leave with the data". The file keeps 625 old entries | the file as downloaded | `pytest-split` 0.11.0's `PytestSplitCachePlugin.pytest_sessionfinish` merges into the old file unless `--clean-durations` is passed, and the recipe does not pass it. `spec.md` Out also forbids editing the file by hand. Of the frame's 838, 235 were Windows-form ids rather than gone cases |
| One ledger row per scenario | `plan.md` phase 3: "one row per S1–S7". The fragment has S1–S6 and no S7 | S1–S6 | S7's claim is that the records exist. Its only coordinate would be this directory's `overview.md`, which `settle --retire-process` removes after the release, so the row would break. `evidence-check --strict` exiting 0 is S7's evidence |

## Not verified

| Item | Who must answer |
|---|---|
| The whole suite at the branch's final SHA | the sealer, once, after the review rounds |
| ✅ That the measuring run finishes inside 55 minutes and uploads `.test_durations` | run 38332345615 at 9ec6faca, read in phase 2 on 2026-10-13: the Windows job took 37 m 21 s and the artifact `test-durations` was there |
| ✅ That the hook sees the whole collection on GitHub's shards (`questions.md` Q4) | read in phase 3 on 2026-10-13: macOS group 3 of run 38332345615 read 1,276 of 13,480 collected cases, and run 38335775781's seven shards are green |
| That GitHub reads the budgets at the final SHA | the pull request's run at the final SHA |

## Not done

Two findings this work measured and left alone. Each is a candidate for an
issue the orchestrator files, and neither widens this item.

- **213 cases are unpriced on ubuntu and macOS after every refresh.** Each
  is a parametrized case whose id carries a path. Windows writes
  `[agents\\framer.md-1]` where POSIX writes `[agents/framer.md-1]`, so a
  file measured on Windows cannot price them for the POSIX legs. They hold
  1.58 % of the 5 % `STALE_SHARE` allows on those legs. The 213 cases sit in
  six modules, and 170 of them are in
  `tests/test_a_moved_rule_leaves_its_definition.py`. One fix is ids built
  from a path's `as_posix()`.
- **The recipe merges into the old file and does not replace it.** Without
  `--clean-durations`, `pytest-split` keeps every entry it loaded, so 625
  entries the suite no longer collects stayed in the refreshed file. They
  cost bytes and nothing else, because the division never reads them.
  Adding `--clean-durations` to the recipe's `store` value would drop them
  at the next refresh.

Not built here either: the `workflow_dispatch` input that measures without
a commit (`plan.md` Alternatives E). `spec.md` Out named it as the design to
adopt when the per-release refresh proves costly.

## Fed back into the spec

none
