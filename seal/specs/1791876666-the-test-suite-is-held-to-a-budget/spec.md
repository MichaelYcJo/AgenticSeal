# Feature Specification: the test suite is held to a budget

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here stops to ask. The one decision only a person can make (which legs run on a pull request) is split into its own item rather than asked mid-run |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | Every case this work adds is seen red first and names the mutation it kills; every unit it adds carries a `Reads:` line |
| `CONTRIBUTING.md` §*Running the checks*, the paragraph opening `**A case has a budget, and so does each leg.**` | The one sentence this work rewrites in place: how a case is proven redundant before it is removed. Nothing is appended |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | Ledger rows go to `seal/ledger/1791876666-….md`, the changelog to the work item's fragment |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* | A removed case a released row cites gets a `Corrected ·` row; a case whose text moved gets a `Re-read ·` row, by `evidence-check --reverify --into` |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below, and the rule a removal the frame did not name is a divergence in `overview.md` |
| `docs/branch-and-release.md` §*Which button, for each direction* | A feature branch's pull request targets `release/vX.Y.Z`; only the release's own targets `main`. This is what "the full matrix only on the release pull request" would select on, in the split-out item |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The work lowers values a contributor is limited by (`slow-file:*`, `ci-minutes:*`), which is the top rung |
| #930's `seal/specs/1791876665-…/spec.md` §*The budgets* | The rows this work moves and the ratchet it moves them under: `measured ≤ ceiling ≤ measured × (1 + slack)`; a lowering lowers the row in the same pull request |

## Scope

**In.** Three heavy test files cut by two patterns and widened to the rest of the `slow-file` list, with each cut proven by a mutation table before and after; the committed `.test_durations` pruned of every case id the work removes; #930's rows lowered in the same pull request; the `CONTRIBUTING.md` paragraph rewritten in place with the removal criterion; the ledger and changelog fragments.

**Out, and whose.** Which legs run on a pull request — a new issue, framed after this item and #930 land, because the tree has no answer and the owner's record (#841) stands against dropping Windows; `plan.md` §*Alternatives considered* D1–D3 holds the comparison it starts from. When `.test_durations` is refreshed (#931; this spec names what #931 depends on). #930's mechanism; what this frame finds wrong with it for the suite is two rows of `questions.md` for #930's smith, not a fork. The 90 s per-case ceiling and the leg `timeout-minutes` (each keeps its reader). The size of `tests/test_the_seal_is_taken_once_by_the_sealer.py` as a file to read (10,180 lines): a reader cost no budget row measures, named here and not split in this work. A measuring run of the Windows leg: no phase dispatches one.

## Where the time is, and what moves

Read from `.test_durations` (Windows seconds) and `gh api …/jobs` at c22f7472 (`executed`, 2026-10-13; commands in `plan.md` §*Technical context*). 13,482 priced cases in 182 files, 7,861.7 s. 1,861 cases (14 %) run ≥ 1 s and hold 6,394 s (81 %); 7,746 (57 %) run under 0.05 s. Sixteen files are at ≥ 120 s and hold 5,390 s (69 %). The time is a few files whose cases each build repositories and spawn git, pytest or bash — not the case count.

| #930 row | Now (`executed`) | Target at the close of | How the row moves |
|---|---|---|---|
| `slow-file:tests/test_the_commit_gate_decides_at_the_commit.py` | 1,137 s · 367 cases; 226 of them one corpus case (946 s), 70 of which skip after building their sandbox | **≤ 400 s** · phase 1 | the file's removed ids leave `.test_durations`; the sum that is left is the row |
| `slow-file:tests/test_the_seal_is_taken_once_by_the_sealer.py` | 1,183 s · 474 cases; 160 at ≥ 5 s hold 1,045 s, 98 call sites run the broad gate end to end | **≤ 700 s** · phase 2 | the same |
| `slow-file:…test_the_fixes_close_the_record.py` · `…test_chain_check_at_the_pull_request.py` · `…test_a_fix_of_a_fix_is_counted.py` | 482 · 375 · 331 s | **≤ 300 · ≤ 230 · ≤ 200 s** · phase 3 | the same |
| the eleven other `slow-file:*` rows | 126–293 s each, 1,892 s together | **each ≤ 60 % of its start, or under 120 s** · phase 4 | the same |
| `suite-seconds` | 7,862 s | falls by exactly the removed ids' seconds at each phase; **≤ 6,400 s** as the committed file reads at phase 4 | the committed file; a case made cheaper rather than removed moves it only at #931's next refresh |
| `ci-minutes:windows` · `:macos` · `:ubuntu` | medians 42.7 · 21.4 · 10.0 over five runs (sums 35.6–44.8 · 19.9–24.0 · 8.8–10.2) | **≤ 36 · ≤ 18.5 · ≤ 8.7** as the median of the branch's last five runs at phase 4 | measured per run by #930's job; the ceiling is re-set to 1.3 × the branch's max, by #930's rule |

The `ci-minutes` targets are read off a proportional model (case seconds removed over case seconds held, with the per-job setup minutes held fixed), not measured; the phase that closes measures them. A cut that makes a case cheaper shows on `ci-minutes:*` the same pull request and on `suite-seconds`/`slow-file:*` only when #931's refresh re-prices it — so between refreshes those two rows undercount what this work did, never overcount.

**Where #930 has not landed when a phase runs.** The numbers go in `phases/phase-N.md` and the ledger fragment as they would have gone in the rows, and whichever of the two pull requests merges second lowers the rows to what the tree then measures (#930's `plan.md` already re-measures every starting value at its own SHA).

**What #931 depends on from here.** The unpriced share after this work: every id this work removes leaves both the file and the collection (share unchanged by it), and every case this work adds is unpriced until the next refresh. Phase 4 records the count of added cases and the share `test_the_durations_file_prices_the_suite` reports at its SHA.

## The removal criterion

A case is removed only when a mutation table shows it guards nothing alone: a battery of mutations of the unit under test, each killed (`mutation-check` exit 0) by the file as it stands, is still killed by the file without the case. The battery is drawn from what the file's cases say they guard — each case's docstring names the sentence, and the mutation is that sentence's negation — and a candidate whose guarded sentence no mutation in the battery negates gets its mutation added before anything is removed. A case whose bare run shows it asserts nothing (the 70 corpus rows that skip) is removed on that showing. Judgment alone removes nothing. The table — mutation · killed before · killed after — is in each phase's `phases/phase-N.md`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 one file first | phase 1 closes on `test_the_commit_gate_decides_at_the_commit.py` | `phases/phase-1.md` holds: seconds before and after (local, `executed`, with the machine and SHA; the Windows figure as the removed ids' sum), the mutation table with every row red before and after, the sampled rows named |
| S2 the sample cannot rot | a family of the full corpus (`ns`, `shape`, `handed`, `position`, `#686`, `#686 ;`) gains or loses rows upstream | a pinned case fails when a family has no sampled row, or a sampled name is not in the corpus |
| S3 a vacuous row is not run | a corpus row whose bare run commits into no undeclared repository | it is not in the sample; the sample's rows all land in `main` or `u` without hooks |
| S4 the file prices only what exists | `.test_durations` after each phase | no id the phase removed is in it; `test_the_durations_file_prices_the_suite` passes |
| S5 the rows move with the cut | #930's `seal/budgets.md` is in the tree at the phase's SHA | the phase's pull request lowers the row to ≤ measured × (1 + slack); `budget_check.py` exits 0. Where the file is not in the tree, S1's numbers stand in for it |
| S6 the ledger follows | a removed function a released row cites; a case whose text moved | `Corrected ·` and `Re-read ·` rows in `seal/ledger/1791876666-….md`; `evidence-check` exit 0 |
| S7 docs state the rule, not the history | the `CONTRIBUTING.md` paragraph | rewritten in place; no `docs/*.md` gains a history line (#930's `docs-history:*` at +0) |
| S8 nothing asks a person | the whole change | no `AskUserQuestion`, no prompt; the one person's decision is the split-out item |
| S9 a new case names its mutant | every case this work adds | `plan.md` §*Test rows* names the mutation; the phase record says how it was seen red |
| S10 the minutes fell | phase 4 closes | `ci-minutes` medians of the branch's last five runs ≤ the targets above, run ids in `phases/phase-4.md`; or the miss and its reason |

## Data & interfaces

No new file, no new reader, no new budget row. `seal/budgets.md` rows lowered (where present). `.test_durations` pruned by id. One sampled-corpus constant beside `CORPUS` in the phase-1 file, one pinned case over it. Ledger rows: S1–S10 anchored to the cases and the pinned constant, in `seal/ledger/1791876666-….md`.

## Removes

nothing — the frame names no unit: which cases leave is decided by each phase's mutation table, so every removed function is a divergence row in `overview.md` with its `Corrected ·` ledger row, as `docs/the-reader-registry.md` §*A frame names what its work removes* has it. The `CONTRIBUTING.md` paragraph is rewritten, not removed.

## Open questions → questions.md

Framed 2026-10-13 by framer, before the build.
