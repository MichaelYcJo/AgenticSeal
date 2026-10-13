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

## Not verified

| Item | Who must answer |
|---|---|
| The whole suite at the branch's final SHA | the sealer, once, after the review rounds |
| That the measuring run finishes inside 55 minutes and uploads `.test_durations` | the run the orchestrator dispatches after phase 1, read in phase 2 |
| That the hook sees the whole collection on GitHub's shards (`questions.md` Q4) | the post-refresh run, read in phase 3 |

## Not done

Nothing yet; phase 3 closes this section.

## Fed back into the spec

none
