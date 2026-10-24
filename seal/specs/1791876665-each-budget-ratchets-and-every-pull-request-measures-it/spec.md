# Feature Specification: each budget ratchets and every pull request measures it

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here may stop to ask a person. A raise is declared in the pull request body, read by CI; nothing prompts |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The checker is a gate: the PR carries a test seen red, the failure direction (it blocks more), a prompt budget of zero, platform honesty, a `Reads:` line per unit |
| `docs/the-record-layout.md` §*The size a reader takes whole*, §*seal/* | The budgets extend the one size rule the tree has (1,000 lines, 64 KB); `seal/budgets.md` is a new permanent machine-read file and takes a row in the §*seal/* table |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | Ledger rows go to `seal/ledger/<id>.md`, the changelog to the work item's fragment |
| `docs/the-agent-set.md` §*What a spawn costs* | The preload is already measured by `skills/verify/scripts/payload_meter.py`; the budget reads that meter and adds nothing to it |
| `docs/measuring-a-run.md` §*Where a reading goes* | A measurement nobody posted is one nobody has: every run writes the readings to the job summary, and the release reads the trend off the file's diff |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* | The ledger budget counts `Re-read ·` and `Corrected ·` rows of a release file; released files never change, so the count is final at the release |
| `docs/the-reader-registry.md` §*Who declares* | Every unit the checker adds carries a `Reads:` line |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The work names values a contributor is limited by, which is the top rung |

## Scope

**In.** One file, `seal/budgets.md`, that names every budget with its unit, ceiling, slack and kind; one reader, `.github/scripts/budget_check.py`, that measures each budget from the tree or from a run, compares, and enforces the ratchet; the places it runs (a `hygiene.yml` step, a `test.yml` job after the suite, one pytest case); the job summary every pull request gets; the trend a release pull request gets. The in-place rewrites of sentences the new checks make false (`CONTRIBUTING.md` §*Running the checks* "CI runs five jobs", `docs/the-record-layout.md` §*seal/* table, `docs/release-checklist.md` §*2*'s trend line).

**Out, and whose.** The suite's cuts, the heavy fixtures and which legs run on a pull request (#929 — it lowers `suite-seconds`, `slow-file:*` and `ci-minutes:*` rows). When `.test_durations` is refreshed and whether the checklist box stays (#931 — it decides the cadence at which `suite-seconds` and `slow-file:*` are re-measured). The rewrite of `docs/`, `skills/`, `agents/` to current-rule shape and the ledger anchors it moves (#923, 0.22.1 — it lowers `preload:*` and `docs-history:*` rows). Records that summarise rather than accumulate (#923). Folding this spec into a `docs/` policy (`settle`, after release). No new `docs/` file: a work item does not create one.

## The budgets

A row read off the tree is a ratchet: `measured ≤ ceiling ≤ measured × (1 + slack)` (or `+ slack` lines where slack is absolute). The left inequality is the ceiling; the right one is what records a lowering — a cleanup that drops the measurement below the band fails until the same pull request lowers the ceiling. A row read off one run — a CI run's minutes, or `.test_durations`, one run's union — is `one-sided`: its ceiling is 1.3 times its reading, and the release lowers it from the trend line. A ceiling that is higher at `HEAD` than at the merge base, a slack that is wider, or a row that is gone, fails unless the pull request body carries `Budget raised: <name> <old> -> <new>: <reason>` (`Budget removed: <name>: <reason>` for a row), the one place a raise is declared and the reason lives. A pull request into `main` is exempt from the body rule, as `hygiene.yml`'s survivor step is: each work item carried its own line at its own pull request. A new row needs no line. Exit 0 holds, 1 names each broken row, 2 cannot read (missing file, malformed row, no baseline): closed, never silent.

| Budget | Unit | Measured by | Kind · why | Starting ceiling · slack |
|---|---|---|---|---|
| `preload:framer`, `:scribe`, `:sealer`, `:smith`, `:warden` | bytes of `agents/<a>.md` + each `skills/<s>/SKILL.md` its `skills:` list names | `payload_meter.py --json --root .`, the per-file rows without the `CLAUDE.md` pair | gate · deterministic from the tree; the file that grows is the file the PR edited | 99,089 · 29,554 · 36,113 · 106,350 · 102,229 (`executed` at f95f0ba8) · 2 % |
| `preload:claude-md` | bytes of `CLAUDE.md` | `wc -c` equivalent in the checker | gate · it is in every prefix, the orchestrator's included; `~/.claude/CLAUDE.md` is not in the tree and is not measured | 9,261 (`executed`) · 2 % |
| `docs-history:<file>`, one per `docs/*.md` | history lines: a line outside a fence, a comment, a heading and a rule block that matches `#\d{2,}`, `round \d`, `20\d\d-\d\d-\d\d` or `[Mm]easured` | the classifier in the checker (§*The docs classifier*) | gate · an appended change narrative fails; #923 lowers the rows | per file, 0–38, total 246 (`executed`); slack +0 lines |
| `suite-seconds` | seconds summed over `.test_durations`, divided by its price level | the checker reads the file | gate · one run's union, so one-sided: one refresh moved its 19 test files of 100 s or more 0.76–1.14 of the level it moved the whole by, and its 72 of 10 s or more 0.46–1.54 | 10,221, 1.3 × the 7,862 read (`executed`) · one-sided |
| `slow-file:<path>`, one per file whose reading × 1.3 reaches 120 s | seconds of one test file in `.test_durations`, divided by its price level | the checker sums the file's cases | report · one union of the Windows shards' parts moves a single file 0.67 to 1.72 times the level from the next (#931), past the 1.3 band on files nobody changed, so each row prints in the summary and fails nothing; `suite-seconds`, the sum, is the gate | 20 files, each at 1.3 × its reading, 1,538 s down to 128 s (`executed`) · one-sided |
| `ci-minutes:ubuntu`, `:windows`, `:macos` | runner-minutes of one `test.yml` run, summed over the leg's `pytest` jobs | `gh api repos/<r>/actions/runs/<id>/jobs`, read by a job that `needs: pytest` | gate · the one measurement of the suite taken on every pull request; noise is 1.08–1.21 max/median over 12 runs, so the ceiling sits at 1.3 × the max | 15 · 59 · 32 (`executed`: max 11.1 · 45.2 · 24.0 over 12 runs on 2026-10-13) · one-sided |
| `rounds-bytes` | bytes of `seal/specs/<id>/rounds/` per open work item | the checker walks the tree | report · the number is the review chain's, written mid-run; a red pull request would have no fix that does not rewrite a committed record. Gated once records summarise (#923) | largest 142,823 B over 3 rounds; a round-3 reviewer inherited 100,425 B (`executed`) |

**Tokens are not the unit.** The unit is bytes, because CI must measure the same number on every machine and no tokenizer in CI is Claude's. The calibration from transcripts: a first-turn prefix of 56,975 tokens (sealer) to 85,253 (smith) against 53,416–123,653 bytes of files fits 2.43 bytes per token above a 35,037-token harness share (`executed`, two-point fit, residual 8 % on warden); #292 measured 2.7–3.4 bytes per token with the baseline spawned. The real measurement is `payload_meter.py --calibrate <main transcript>` on a session that spawned the `general-purpose` baseline — an orchestrator's act, none of this build's.

**The per-case ceiling, the leg timeouts and `Document line ceiling` stay where they are.** Each has one reader already; the budgets sit beside them and the summary prints them for comparison.

## The docs classifier

A line is a **rule line** from a line opening with `**` to the next `Enforced by:` line inclusive. A line is a **history line** when it is not a rule line, not blank, not inside a fence, not a `<!--` comment and not a heading, and matches `#\d{2,}`, `round \d`, `20\d\d-\d\d-\d\d` or `[Mm]easured`. Everything else is other. How it errs: a rule's own grounds citing an issue count as history (over); a narrative sentence with none of the four marks counts as other (under); the `.ko.md` file is read by the same marks. The budget is the history count per file; the rule/history ratio is printed, not gated.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a file grows past its ceiling | `agents/warden.md` gains bytes past `preload:warden`; the checker runs | exit 1, the row, measured and ceiling named; the hygiene step is red |
| S2 a raise without its line | `seal/budgets.md` raises a ceiling, the body has no `Budget raised:` line for that row | exit 1 naming the row and the line to write |
| S3 a raise with its line | the body carries `Budget raised: preload:warden 102229 -> 110000: <reason>` | exit 0; the summary shows the raise |
| S4 a cleanup lands | the file shrinks below the band; the ceiling is unchanged | exit 1 saying lower the ceiling to ≤ `measured × (1 + slack)` |
| S5 every pull request reads its numbers | any run | the job summary holds one line per budget: measured, ceiling, headroom, kind |
| S6 a pull request into `main` | a release pull request whose ceilings differ from `main`'s | no body line is asked for; measured-vs-ceiling still holds; the trend against the last release tag is in the summary |
| S7 a slow file appears | a test file not listed reaches ≥ 120 s in `.test_durations` | exit 0: the family is a `report` row (#931), so its summary line reads `over` and the list of report rows past their band names the file |
| S8 a docs file gains a narrative line | a `docs/*.md` line citing `#NNN` is added | exit 1 naming the file and the line |
| S9 the suite's minutes | a `test.yml` run completes its `pytest` jobs | the `budgets` job sums each leg and compares; red past a ceiling; the summary carries the billable-minute line labelled with its price date as unverified |
| S10 nothing asks a person | the whole change | no `AskUserQuestion`, no `input()`, no `read` from a terminal in anything added; every check exits and prints |
| S11 the checker cannot read | `seal/budgets.md` missing or a row malformed | exit 2 naming the row; never 0 |
| S12 a new unit declares | every `def`/`class` added | `Reads:` line present; the census test passes unchanged |

## Data & interfaces

`seal/budgets.md` — a `## Budgets` table `| Budget | Unit | Ceiling | Slack | Kind |`, and two per-file tables, `## Slow test files` `| File | Seconds ceiling |` and `## Docs history lines` `| File | Lines ceiling |`, each read by the one checker through the repository's GFM table walker (`hooks/config.py`). `budget_check.py` — `--baseline <ref>` (merge base, as `unverified_check.py` resolves it), `--pr-body-env <VAR>`, `--base-ref <branch>`, `--ci-jobs <file>`, `--trend <tag>`; writes `$GITHUB_STEP_SUMMARY` when set, stdout otherwise; names no machine path. Ledger rows: this spec's clauses anchored to the checker's units and their tests, in `seal/ledger/1791876665-….md`.

## Rule changes

- nothing
  why: overturned: seal/budgets.md, budget_check.py and their job left the tree at 8350c578.

## Removes

nothing — every existing ceiling (`timeout-minutes`, `CASE_CEILING_S`, `Document line ceiling`) keeps its reader; the budgets sit beside them, and the one `CONTRIBUTING.md` sentence the new job makes false is rewritten in place, not removed.

## Open questions → questions.md

Framed 2026-10-13 by framer, before the build.
