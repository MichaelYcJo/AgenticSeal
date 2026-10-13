# Implementation Plan: the test suite is held to a budget

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-14 by the repository owner, when `smith` was spawned.

## Summary

Two patterns, proven on one file before they widen. **Sample a corpus** where one parametrized case replays hundreds of command shapes against a mechanism that cannot see the shape (phase 1). **Share a run** where many cases read different lines of the same end-to-end run (phase 2). Then the same two patterns across the round-record files (phase 3) and the rest of the `slow-file` list (phase 4). Every removal is proven by a mutation table before and after, never by judgment; every phase prunes the removed ids from `.test_durations` and lowers #930's rows in the same pull request.

## Technical context

Read at c22f7472 unless marked `executed`.

- `tests/test_the_commit_gate_decides_at_the_commit.py#corpus` (line 262) builds `CORPUS`: 226 rows — `ns` 28, `shape` 63, `handed` 109, `position` 14, `#686` 6, `#686 ;` 6 (`executed`, by importing the module) — from the corpora of three other test modules, which test the *text reader* against those shapes. `#_run_corpus_row` (375) builds three clones (`#_sandbox`), runs the row under a parent named `claude` (`#_as_a_session`) and reads whether HEAD moved. `#test_s2_a_commit_bash_makes_into_an_undeclared_repository_does_not_land` (489) runs it twice per row, bare then hooked, and **skips when the bare run commits nowhere undeclared**. The hook judges inside git, in the worktree the commit lands in (the module docstring, #692), so the text's shape is not what it sees.
- **Timed locally** (`executed`, `bin/test tests/test_the_commit_gate_decides_at_the_commit.py -q --durations=25 -rs`, macOS arm64, 12 cores, c22f7472): 297 passed, 70 skipped in 78.19 s wall; CPU user 174.9 s, sys 270.1 s; slowest case 6.07 s; the 25 slowest are all S2 rows at 4.8–6.1 s. All 70 skips are S2 rows (`bash commits into no undeclared repository with this command`): 70 sandboxes built to assert nothing. In `.test_durations` the S2 case is 946.4 of the file's 1,137.0 Windows seconds.
- **Mutation coverage** (`executed`, `bin/mutation-check hooks/gate.py --replace … --tests "bin/test tests/test_the_commit_gate_decides_at_the_commit.py -q"`): m1, the review arm never missing (`and not routing.declared(cwd, top)` → `and False and …` in `#arms_missing`): **red, 204 of the 297 running cases fail** — the 156 landing S2 rows and 48 others. One mutant, 156 killers among the S2 rows alone: that is the duplication the sample removes. m2, a declaration ignored (`→ and True`, run with `-x`): **red**, the first failure `test_s1_a_commit_lands_in_the_declared_worktree_with_no_stop` — so the declaration is guarded by S1, and no S2 row is needed for it. `hooks/gate.py` was restored byte for byte after each (`git status` clean). The battery phase 1 runs before and after is m1–m4 of its row below.
- `tests/test_the_seal_is_taken_once_by_the_sealer.py`: `#build_repo` (1260), a session `_template` and a per-case `repo` copy (1342–1351), `#run_gate` (1353) runs `broad_gate.py --base base --root <repo> --shape`, whose row `SUITE_ROW` (`python -m pytest -q -p no:cacheprovider tests`) runs at HEAD and once more at the base under the recorder (`skills/verify/scripts/pytest_record`); 98 call sites, 160 cases at ≥ 5 s holding 1,045 of 1,183 s, the largest `#test_every_layout_the_first_build_reopened_reads_the_word_the_base_gives` (7826) at 55 rows · 240 s. `#a_sealed_run` (1435) is the precedent: six cases that each ran the gate to read one line now share one run (#841). A one-test pytest child starts in 0.11 s here with plugin autoload and 0.12–0.28 s without (`executed`), so the cost is the gate's own work times the spawn price, not pytest's import.
- `tests/test_the_fixes_close_the_record.py#close` (118) and `#generator_run` (149), `tests/test_a_fix_of_a_fix_is_counted.py#a_round` (94), `tests/test_chain_check_at_the_pull_request.py` (session `_template` at 106): `round_record.py` as a subprocess per case, 3.8–5.4 s a case on Windows.
- `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#staleness` counts only collected ids (`test_an_entry_nobody_collects_is_not_counted`), so pruning removed ids from `.test_durations` moves no verdict; `pytest-split` prices a missing id at the mean.
- Released ledger rows citing the five files: 192 · 23 · 32 · 34 · 13 rows in 17 · 5 · 10 · 15 · 3 release files (`executed`, grep). A removed cited function owes a `Corrected ·` row; a changed one a `Re-read ·` row.
- Leg minutes (`executed`, `gh api repos/<r>/actions/runs/<id>/jobs`, five pull-request runs of 2026-10-13: 38359441348, 38355857651, 38353159958, 38352603728, 38359676917): Windows 42.7 · 44.8 · 35.6 · 41.2 · 43.8; macOS 21.3 · 22.3 · 24.0 · 21.4 · 19.9; ubuntu 10.1 · 10.0 · 9.5 · 8.8 · 10.2. The slowest single job in each run is a Windows shard (12.7 min), so the wait is Windows's.
- Platform guards in the suite (`executed`, grep): 25 of 185 test files carry `os.name`, `sys.platform` or a `skipif`; nothing marks the other 160 as platform-free. Windows-only defects are named in five release files and two docs (`read`).
- `.github/workflows/test.yml` matrix: ubuntu one job, macOS three shards, Windows four, each shard's `timeout`; `docs/branch-and-release.md` §*Which button*: a feature branch's pull request targets `release/vX.Y.Z`, only the release's targets `main`.

**What breaks in 6 months with the chosen approach.** A red S2 row is answered by taking the row out of `SAMPLE` instead of fixing the hook; T1 catches it only when a family empties, so the warden reads any `SAMPLE` edit as a removal. Second: a case made cheaper keeps its old Windows price until #931's refresh, so a cut nobody re-measures looks like nothing happened and the `slow-file` rows stay where phase 4 left them; the refresh is the instrument, and #931 names its cadence. Third: the shared-run memo is keyed on the signature the phase defines, and a case that mutates the shared repository corrupts every later reader on its worker — the rule is the one `#a_sealed_run` already states (a case that writes keeps its own `repo`), pinned by T4.

## Alternatives considered

| Approach | Failure scenario (six months on) | Verdict |
|---|---|---|
| A. Sample the corpus by family with a pinned representative set; share one run per signature; remove only mutation-proven duplicates; prune ids; lower rows | above | **chosen** |
| B. Delete by judgment | a guard goes with the case and the defect returns; #841's 165 s case was asked to be deleted and held a guard a released row cited | rejected |
| C. Move the heavy files to a nightly or `main`-only job | the nightly goes red with nobody on the pull request that broke it; a red that reaches no pull request is ignored | rejected |
| D1. OS-specific cases only on their OS | needs a marker over 13,482 cases or a path rule; 160 files carry no guard today, and a Windows-only defect lands in an unmarked case — #841 kept Windows for that reason | not decided here; item B |
| D2. Full matrix only on the release pull request (base `main`), ubuntu on feature pull requests | a Windows failure surfaces at the release, after every work item squashed in, and the fix belongs to no branch; the release waits twice | not decided here; item B |
| D3. macOS on a smaller slice (one shard of three, or the spawn-heavy files) | the slice is a list that rots; a macOS-only defect in an unlisted file is found at the release | not decided here; item B |
| D4. Keep all legs on every pull request, hold them by `ci-minutes:*` | the cost stays where it is and the wait is Windows's slowest shard; nothing rots | **default until item B decides** |
| E. Call the hook in process instead of through git and bash | loses the oracle (what git did) the corpus exists for; kept only where a case asserts a verdict word of `round_record.py` and one end-to-end case per exit code remains | partly taken, phase 3 |
| F. Cheaper pytest children (`PYTEST_DISABLE_PLUGIN_AUTOLOAD`) | measured 0.11 s against 0.12–0.28 s locally: nothing to gain; Windows unmeasured | rejected · NAME NOT IN TREE: a pytest environment variable |
| G. A `suite-cases` row in `seal/budgets.md` | the only cheap source is `.test_durations`, which moves at a refresh, so the row would go red on the refresh pull request rather than on the one that added the cases; a true count needs a collection run every pull request | rejected |
| H. Split: this item (phases 1–4) and item B (which legs run on a pull request) | item B is framed against the post-cut numbers and #930's billable line, which is the order #931 already argues; nothing in this item waits on it | **chosen** |

**CI cost if this repository goes private** (`executed` for the medians; prices `read` from #929, mid-2026, $0.008 · $0.016 · $0.08 per Linux · Windows · macOS minute — the date is unverified, #930's Q1). Per pull request at the median: 10.0 + 2 × 42.7 + 10 × 21.4 = 309 Linux-equivalent minutes ≈ US$2.48. At this item's targets: 8.7 + 2 × 36 + 10 × 18.5 = 266 ≈ $2.13 (−14 %). D2: 8.7 ≈ $0.07 on a feature pull request. D3 at one macOS shard: 8.7 + 72 + 62 = 143 ≈ $1.14. At #929's 40 runs a day: $99 today, $85 after this item, $46 under D3, $3 under D2. macOS is 69 % of today's figure, and item B is where that number is decided.

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `test_the_commit_gate_decides_at_the_commit.py`: a `SAMPLE` beside `CORPUS` — one row per subgroup of each family (`ns` by row kind; `shape` by wrapper/reserved word; `handed` by HANDED, SUBSTITUTED, REDIRECTED, EVALS; `position`; both `#686` forms), every sampled row one whose bare run lands in `main` or `u`, about 30–40 rows; S2 parametrized over `SAMPLE`, a sampled row that commits nowhere undeclared failing rather than skipping; T1–T3; the mutation table m1–m4 (m3: the stub written without its execute bit in `hooks/hook-install.py#write_stubs`; m4: the lease not read in the hook) before and after; the dropped ids pruned from `.test_durations`; the `slow-file` row lowered where the file exists | local wall and CPU before (78.19 s · 445 s) and after; the dropped ids' Windows seconds ≥ 737 so the row reads ≤ 400; every mutation red after as before, with the count of killers before and after; T1–T3 seen red by their mutations; all in `phases/phase-1.md` | cf77665c |
| 2 | `test_the_seal_is_taken_once_by_the_sealer.py`: the inventory of the 98 `run_gate` call sites by (template state, arguments, environment); a memoized module-scoped run per signature on the `#a_sealed_run` pattern for cases that only read; the mutation table over `broad_gate.py`'s words (`NOT_REACHED`, `NEW`, `ON_BASE`, `NO_RECORD`), exit codes and the stamp, with duplicates removed on it; T4; ids pruned; row lowered to ≤ 700 | before/after local timing; the table; the inventory's counts in `phases/phase-2.md` (and the target re-set there if the inventory shows fewer shareable signatures than the target assumes, with the reason) | |
| 3 | `test_the_fixes_close_the_record.py`, `test_chain_check_at_the_pull_request.py`, `test_a_fix_of_a_fix_is_counted.py`: `round_record.py` called in process where the case asserts a verdict, one end-to-end case per exit code kept; shared templates; the mutation table per file; T5; ids pruned; rows ≤ 300 · ≤ 230 · ≤ 200 | before/after timing per file; the tables; `evidence-check` exit 0 over the fragment's `Re-read ·`/`Corrected ·` rows so far | |
| 4 | The two patterns across the eleven remaining `slow-file` rows (each ≤ 60 % of its start or under 120 s); the `CONTRIBUTING.md` paragraph rewritten in place with the removal criterion; the final prune; every row lowered, `ci-minutes:*` ceilings re-set to 1.3 × the branch's max over its last five runs; the ledger fragment; the changelog fragment; the added-case count and the unpriced share for #931 | `budget_check.py` exit 0 where present; `evidence-check` exit 0; the five run ids and per-leg medians in `phases/phase-4.md` against ≤ 36 · ≤ 18.5 · ≤ 8.7, or the miss and why; `docs-history:*` unchanged | |

This table is also where the work records how far it got. **Status is empty, or the commit that closed the phase.** Re-read the column after any rebase.

### Test rows — the mutation each case kills

| Case | Guards | Mutation it kills |
|---|---|---|
| T1 `test_every_corpus_family_has_a_sampled_row` | S2 | every `#686 ;` row removed from `SAMPLE`: the family is in `CORPUS` and has no representative |
| T2 `test_a_sampled_row_that_commits_nowhere_undeclared_fails_rather_than_skips` | S3 | the `pytest.skip` restored for sampled rows; a vacuous row put in `SAMPLE` must fail, not skip |
| T3 `test_every_sampled_name_is_a_corpus_row` | S2 | one `SAMPLE` name misspelled: a representative that selects nothing |
| T4 `one_shared_run_per_signature_and_a_writer_keeps_its_own` | phase 2's memo | the memo keyed on arguments alone (two signatures differing only by environment share a run); a case marked as writing handed the shared run · NAME NOT IN TREE: planted in phase 2 |
| T5 `the_in_process_close_and_the_cli_agree_on_each_exit_code` | phase 3 | the in-process path's exit mapping changed for one code; the CLI case is the oracle · NAME NOT IN TREE: planted in phase 3 |

Each is seen red by its mutation before it is committed, and the phase record says how.

## Operational impact

- No new dependency, file, reader or budget row. `seal/budgets.md` rows are lowered where #930 is in the tree; otherwise the numbers wait in the phase records and the ledger fragment, and the second of the two pull requests to merge lowers them.
- `.test_durations` is edited by hand (ids removed), which shifts the shard division by at most the removed seconds; no case is dropped by it.
- Released ledger rows citing removed or changed cases are answered in `seal/ledger/1791876666-….md`, never edited in place.
- `SAMPLE` is a list a contributor edits when a corpus gains a family; T1 says so when it is forgotten.
