# the durations refresh has a schedule — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. -->

Framed by `framer` on Fable 5.1, 2026-10-13, under `routing.md`'s `automation`. No row blocks the build.

**Judgments the issue left open that the tree answered** — listed so nobody reopens them; the grounds are in `spec.md` §*Scope* and `plan.md` §*Alternatives considered*.

- When the file is refreshed: when the check says so, and the check now says so in both directions (a twentieth of the cases unpriced, or a twentieth of the seconds dead). Not every release, not on a timer (alternatives A–D).
- How it is measured: on the four Windows shards of every run, for nothing, unioned by a job (E; #914's first way). Not on ubuntu (H), not committed by a bot (F).
- The checklist box goes. A box a person ticks is a prompt, and the check it was the planned moment for is now the whole schedule.
- Gate or report: the check is the gate (its remedy is one download); the shards' seconds, the spread, the live `suite-seconds` and the per-part ratio are reports on every run, because a per-run number carries 1.2× noise (#930 F).
- `STALE_SHARE` stays 0.05 and stays a constant beside #930's rows, not a row (J). #874's Q1 set the value; the cost of a refresh is no longer a ground for it, and the file's age at 3 % is not visible under runner noise, so nothing measured asks for another value.
- Phase 1 commits the first union, once: it is the only way to read the shard-measured file's division after as well as before, and the fresh file is what #930's rows then measure. #931's *measure after #929* is kept for the cost question, which the per-run summary answers from then on.
- Not folded into #930 or #929 (K); phase 1 lands before #929's cuts.
- The `durations` job is a job of its own, not a step in #930's `budgets` job (Q4).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the four parts carry a per-runner skew? Each part is priced on its own runner, and job wall-clock differs 1.1–1.8× between shards of one run | the work — phase 1 reads each part's median price ratio against the committed unsharded file, and phase 2 reads the spread after the union commit | inside the 1.2× run-to-run noise: nothing is built; outside it: the union scales each part to the mean ratio, one function, and the summary line says so | no scaling | ⬜ |
| Q2 | Does a shard's part hold every case of its group, skipped cases included, so the union's key set is the collection? The wheel sums every `TestReport` and #874's unsharded file matched the collection | the work — phase 1: the union's entries against `bin/test tests --collect-only -q` | equal: S2 holds; fewer: the missing ids are read off the parts and the script's reading of skips is fixed before the union is committed | equal | ⬜ |
| Q3 | What do the upload steps and the `durations` job cost per run, and what are the current per-minute prices and their date? The cost column in `plan.md` is an estimate against #929's unverified list | a measurement — the phase-1 run's job times (`gh api …/jobs`), and the price page opened once | the estimate moves; no code | about a minute; #929's figures, labelled unverified | ⬜ |
| Q4 | Two jobs after `pytest`, or one? #930's phase 3 adds a `budgets` job that `needs: pytest`; this item adds `durations` with the same shape. Whichever lands second meets the other in `test.yml` | the work — #930's smith, or this item's, at whichever pull request is second | two jobs: each under a minute, no coupling, and a textual merge in `test.yml`; one job: `durations_union.py` is a step of `budgets`, and #930's row text *moves only when #931's refresh lands* reads *when the file is refreshed, which `test_the_durations_file_prices_the_suite` schedules* | two jobs | ⬜ |
| Q5 | How does a #929 cut pull request bring its fresh file? Its cuts remove seconds the committed file still sums, so `suite-seconds` falls only with the file | the work — #929's smith: once phase 1 is on the release branch, download `test-durations` from the cut pull request's own run and commit it there, so the lower band of `suite-seconds` asks for the ceiling in the same pull request; if #929 lands first, the seconds side of the check fires on the first pull request after both and that one downloads | — | download in the cut pull request | ⬜ |

**`Who can answer` takes one of three values and nothing else** — a person, a measurement, the work — and no row here is a person's. The framer opens rows and does not own their answers; the `Status` column is ticked by whoever answered.
