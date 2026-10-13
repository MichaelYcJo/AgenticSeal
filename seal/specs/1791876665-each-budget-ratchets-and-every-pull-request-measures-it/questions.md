# each budget ratchets and every pull request measures it — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. -->

**Judgments the tickets left open that the tree answered** — listed so nobody reopens them; the grounds are in `spec.md` and `plan.md` §*Alternatives considered*.

- Gate or report, per budget: gate for every number the pull request's own files determine (`preload:*`, `docs-history:*`, `suite-seconds`, `slow-file:*`) and for the one per-run number of the suite (`ci-minutes:*`, with a 1.3× noise allowance); report for `rounds-bytes` and `ledger-rereads`, whose numbers the pull request cannot fix without rewriting a committed record.
- The unit is bytes, not tokens; the calibration is stated once in `spec.md` (alternative E).
- Where the file lives: `seal/budgets.md`, beside `seal/config.md`, whose `Document line ceiling` row is the precedent for a ceiling a reader holds; the reader is this repository's own, under `.github/scripts/`, because the budgets are this repository's.
- How a raise is declared: a `Budget raised:` line in the pull request body, read through `env:` as the issue-claims step reads it; a release pull request is exempt as the survivor step is.
- How a lowering is recorded: the lower band fails until the cleanup's own pull request lowers the row.
- Where the reading goes: the job summary, not a comment (alternative G).
- What #930 holds for docs: the `docs-history:*` ratchet, the `docs/the-record-layout.md` §*seal/* row, and the in-place rewrites of the sentences the new job makes false; the rewrite itself is #923's.
- Not split (alternative H).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | What are the current GitHub Actions per-minute prices and their date? The cost table in `plan.md` uses #929's mid-2026 figures ($0.008 / $0.016 / $0.08) and labels them unverified | a measurement — open the price list once and write the date into the summary's billable line | the numbers change the dollar line only; no code | #929's figures, labelled unverified | ⬜ |
| Q2 | What is the real bytes-per-token ratio per agent today? `payload_meter.py --calibrate` needs a session that spawned the `general-purpose` baseline, and none of the recent main transcripts did | a measurement — the orchestrator spawns the baseline once (`use no tools, reply with one word`) and runs `--calibrate`; a subagent cannot spawn | the ratio is printed beside the byte budgets, not gated | the two-point fit in `spec.md`, 2.43 B/token above a 35,037-token harness share | ⬜ |
| Q3 | Does the default `GITHUB_TOKEN` of `test.yml` carry `actions: read`? The workflow declares no `permissions:` block, and the repository's default is a setting nobody here has read (`hygiene.yml`'s own comment) | the work — phase 3 declares `permissions: actions: read` on the job, so the answer is written into the file rather than depended on | — | declare it | ⬜ |
| Q4 | Is the `Corrected ·` count 62 or 27 for 0.21.1? #908's comment says 27 corrected rows; the frame's substring count over `seal/releases/0.21.1.md` says 62, so one of the two reads a row that carries both markers twice | the work — phase 4's reader defines the count by marker position (a row counted once, by its first marker) and the summary says which | — | count each row once, by its first marker | ⬜ |
| Q6 | Phase 2 was told to read the seconds rows in the base's prices, dividing by the ratio a refreshed `.test_durations` moved by. Divided by that ratio alone, every pull request after the refresh reads the new prices against the old ceilings and fails. Is a `## Price level` row that the refresh restates, one number checked against the measured ratio, the way the orchestrator wants it held? | the orchestrator, who decided the price reading | **the row (built)**: a refresh edits one number the run names, no `Budget raised:` line, and the level cannot move without the file. **Restate every seconds ceiling at the refresh**: no extra row, 17 numbers moved per refresh, and a raise and a restatement read alike. **The base's ratio alone**: the refresh's pull request passes and the next one fails | the row, as built in phase 2 | ✅ answered 2026-10-14 by the orchestrator: the row is accepted, because the literal decision fails every pull request after a refresh |
| Q5 | Should the slack values (2 % bytes, +0 lines, 5 % suite, 10 % per file, 60 % minutes) move after phase 1 shows the noise? | the work — phase 1 writes the first measured headroom into `phases/phase-1.md`; a slack that fails a quiet pull request is lowered or raised there, with the reason in the row | — | the values in `spec.md` | ⬜ |

No row waits on a person: nothing in the frame blocks the build. The three kinds are the template's.
