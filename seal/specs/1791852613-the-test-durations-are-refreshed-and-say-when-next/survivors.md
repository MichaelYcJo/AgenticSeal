# Survivors — the test durations are refreshed and say when next

`survivor-check --range 744c610f..HEAD` reported six places that still
carry wording this range removed. Each one stands for the reason in its row.
Four are matrix entries that look like the Windows shard entries the
measuring commit removed for one run, and `c59c7664` restored those entries
byte for byte. The other two are frame sentences that the ids fix and the
second refresh make true again. A seventh report, Q2's answer in
`questions.md`, was corrected.

| Path | Quote | Grounds |
|---|---|---|
| `.github/workflows/test.yml` | `- { os: macos-latest, python: "3.12", split: "--splits 3 --group 1", timeout: 15 }` | A macOS shard entry, which is meant to stay as it is. The removed Windows entries come back in the restore commit |
| `.github/workflows/test.yml` | `- { os: macos-latest, python: "3.12", split: "--splits 3 --group 2", timeout: 15 }` | The same, group 2 |
| `.github/workflows/test.yml` | `- { os: macos-latest, python: "3.12", split: "--splits 3 --group 3", timeout: 15 }` | The same, group 3 |
| `tests/test_ci_gives_the_checks_what_they_need.py` | `- { os: macos-latest, python: "3.12", split: "--splits 2 --group 1", timeout: 5 }` | A fixture matrix in a case. It shares the words of an entry, not a claim |
| `seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/plan.md` | `so a file refreshed at each release's preparation stays under the line through the next cycle` | The frame's ground for `STALE_SHARE`. It was false while 213 ids were spelled per machine. After `fa4e9cce` every id is one spelling, so the statement holds on every leg once the next refresh prices them. The rewritten comment says the same |
| `seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/spec.md` | `prices every case the tree at the restore commit collects, so the count of unpriced cases is zero there` | S1 as the frame wrote it. It held on Windows alone after the first refresh. At `c59c7664`, run 38342987499's file leaves 0 of 13,482 collected cases unpriced, so it holds as written |
| `seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/questions.md` | `✅ answered by phase 3's reading of run 38335775781, 2026-10-13: each leg's passed plus skipped is ubuntu's 13,480;` | Q3's answer, which matches the corrected Q2 answer only in its opening words. It records run 38335775781 as measured, and that run is still the one Q3 asked about |
| `seal/releases/0.18.1.md` | `"E1 · the work item's"@cb9b7bbd` | A released re-read row, frozen under `Ledger frozen from`, citing `survivor_check.py#corpus` and `#corrected` at the hashes it read. The census lines this range removed from `tests/undeclared_readers.txt` name the same two units at the same hashes, because `4bccb3d3` changed both and they now declare. The row's claim is re-read in this item's fragment |
| `seal/releases/0.18.1.md` | `marker stands on a live line of a changelog at the range's tip` | The same: a released `Corrected ·` row citing the two units at their old hashes, and re-read in the fragment |
| `seal/releases/0.18.1.md` | `"D1 ·"@23b0baf5` | The same: a released re-read row citing the two units at their old hashes, and re-read in the fragment |
