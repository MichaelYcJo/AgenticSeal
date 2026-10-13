# Survivors — the test durations are refreshed and say when next

`survivor-check --range 744c610f..HEAD` reported five places that still
carry wording this range removed. Each one stands for the reason in its row.
Four are matrix entries that look like the Windows shard entries the
measuring commit removes for one run. The commit after it restores those
entries byte for byte. The fifth is a frame sentence that the ids fix makes
true again.

| Path | Quote | Grounds |
|---|---|---|
| `.github/workflows/test.yml` | `- { os: macos-latest, python: "3.12", split: "--splits 3 --group 1", timeout: 15 }` | A macOS shard entry, which is meant to stay as it is. The removed Windows entries come back in the restore commit |
| `.github/workflows/test.yml` | `- { os: macos-latest, python: "3.12", split: "--splits 3 --group 2", timeout: 15 }` | The same, group 2 |
| `.github/workflows/test.yml` | `- { os: macos-latest, python: "3.12", split: "--splits 3 --group 3", timeout: 15 }` | The same, group 3 |
| `tests/test_ci_gives_the_checks_what_they_need.py` | `- { os: macos-latest, python: "3.12", split: "--splits 2 --group 1", timeout: 5 }` | A fixture matrix in a case. It shares the words of an entry, not a claim |
| `seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/plan.md` | `so a file refreshed at each release's preparation stays under the line through the next cycle` | The frame's ground for `STALE_SHARE`. It was false while 213 ids were spelled per machine. After `fa4e9cce` every id is one spelling, so the statement holds on every leg once the next refresh prices them. The rewritten comment says the same |
