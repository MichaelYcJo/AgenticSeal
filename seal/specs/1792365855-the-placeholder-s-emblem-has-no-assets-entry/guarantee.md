# 1792365855-the-placeholder-s-emblem-has-no-assets-entry — guarantee

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md, written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` §*The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | 824174e2 against origin/release/v0.22.2 @ 8a100e13; earlier run: 8b3f0c1e withheld |
| Broad gate | 003805d8 against 8a100e13 (`broad-gate.md`). Three commits follow it: 8b3f0c1e, 3a2775a7 and 824174e2. Between them they touch only this work item's `broad-gate.md`, `guarantee.md` and `overview.md` |

The work item is on the second rung: no `spec.md`, `plan.md`, `phases/` or `changelog.md`. The frame is issue #978, and the build's account is `overview.md`. No pull request is open (#983 is closed), so the pull request body audited is the orchestrator's draft, `978-pr.md` in the session scratchpad, as corrected after the earlier run.

This run audits what came after 8b3f0c1e. `git diff --quiet 8b3f0c1e HEAD` outside this work item's directory exits 0, so nothing under `assets/`, `tests/`, `skills/` or anywhere else changed. Rows marked *carried* were executed at 8b3f0c1e and stand as they came. Rows marked *this run* were executed or read at 824174e2.

## Claims re-run

<!-- One row per act of `agents/sealer.md` step 3, whatever the act, and one
per thing the act checks. `Result` reads `holds`, or `does not hold — <what
came back>`, and a `does not hold` is what the verdict names. -->

| Claim | Source | Command | Result |
|---|---|---|---|
| The base resolves, and the broad run is at HEAD apart from this item's records (this run) | `broad-gate.md:5` | `git rev-parse --verify --quiet 'release/v0.22.2@{upstream}'`; `git merge-base --is-ancestor 003805d8 HEAD`; `git log --no-merges --name-only 003805d8..HEAD ^8a100e13`; `git rev-parse origin/docs/978-…` | holds. The base resolves to 8a100e13. The ancestor check exits 0. 8b3f0c1e, 3a2775a7 and 824174e2 name only `seal/specs/1792365855-…/{broad-gate,guarantee,overview}.md`. HEAD 824174e2 equals the pushed branch. Read at 8b3f0c1e: the run's log says `BROAD GATE PASSED`, suite 7491 passed, 14 skipped, chain exit 0 |
| Nothing outside this item changed since the earlier run (this run) | — | `git diff --quiet 8b3f0c1e HEAD -- ':!seal/specs/1792365855-…'`; `git diff 8b3f0c1e HEAD -- <item>/overview.md` | holds. The first exits 0. The overview diff changes two lines, `:17` and `:28` |
| The S's draw-again command writes exactly the committed `.ans`, 5,498 bytes (carried) | `assets/seals/README.md:89-94`; PR body `:18` | README line 90 run verbatim from the repository root with stdout captured, then compared with the committed file; `git status --porcelain`; the same command at `v0.22.0` through `cmp` | holds. Exit 0, 5,498 bytes, byte-equal; porcelain is empty. The v0.22.0 draw gives `cmp` exit 1 |
| The chart is unchanged from v0.20.0 to v0.22.1 and absent before, and it came from #832 through #859 (carried) | `assets/seals/README.md:80-81`, `:84`; PR body `:7` | `git rev-parse <tag>:skills/verify/scripts/seal-mark.txt` for v0.19.0 to v0.22.1; `git log --diff-filter=A`; `gh pr view 859` | holds. Absent at v0.19.0, then `80593dfc` at five tags; added by 149ca9ec `(#832) (#859)`, and #859 is MERGED |
| The disc is cell for cell the same from v0.20.0 to v0.22.1, and only the panel changed (carried) | `assets/seals/README.md:80-82`; PR body `:7`, `:20`; `overview.md:15` | a scratch probe (deleted) drew each tag's `stamp(SAMPLE_ROWS)` with its own chart and compared the first 28 cells of each of the 14 lines with v0.22.1 | holds. 0 differing cells at each tag. `ledger` is present through v0.21.1, gone at v0.22.0, and v0.22.1 has the short panel |
| The S's command needs the chart beside the module and passes no scale, and from 0.21.0 `stamp` takes no scale (carried probe; PR body `:8` re-read this run) | `assets/seals/README.md:27-34`; `overview.md:16`; PR body `:8` | the probe printed `def stamp(...)` and checked for `DEFAULT_SCALE` at each tag | holds. v0.19.0 and v0.20.0 have `stamp(rows, scale=1.0, shape=False)` and `DEFAULT_SCALE`. v0.21.0 to v0.22.1 have `stamp(rows, shape=False, disc=True)` and no `DEFAULT_SCALE`. The body now reads "From 0.20.0 the stamp module reads its chart from a file beside itself when it loads, and from 0.21.0 `stamp` takes no scale argument", which matches. At 8b3f0c1e this row did not hold: the body said 0.20.0 |
| The preview rule redraws the five earlier previews pixel for pixel, and `placeholder-s.png` is drawn by it (carried) | `assets/seals/README.md:17-25`; PR body `:9`, `:19` | `uv run -q --with pillow==12.3.0 python -I <scratchpad>/978/ans_png.py <ans> <out> --size 19 --dim-alpha 128 --compare <png>` over the six committed `.ans`; the S again at `--dim-alpha 127` | holds. `differing pixels 0` for all six. At alpha 127 the S gives 1,473. The renderer lives in the scratchpad, not the tree, as `overview.md:32` says |
| Each preview cell is 12 × 24 pixels (carried) | `assets/seals/README.md:18` | the probe read each PNG's `IHDR` against its `.ans` cell grid | holds. 816 × 336 is 68 × 14 cells, 792 × 504 is 66 × 21, and 972 × 480 is 81 × 20 |
| The dropped sentence was false, and `LOADED` names five root files and no `assets` (carried read; `overview.md:17` re-read this run) | `overview.md:17`; PR body `:10` | read `tests/test_release_hygiene.py:45-55`; read 149ca9ec's message `:242`, `:298` | holds. `LOADED` is `skills`, `agents`, `docs`, `templates` plus five root files (`:50-54`). The page moved from `docs/seals/` to `assets/seals/` inside #832's branch. The overview now says "five root files". At 8b3f0c1e it said four, and this row did not hold |
| What reads `assets/seals/`: nothing the plugin ships; the one reader is `tests/test_one_word_one_meaning.py` (this run) | PR body `:12`; `overview.md:28` | `git grep -n -E "\"seals\"\|'seals'\|assets/seals" -- ':!seal' ':!changelog' ':!CHANGELOG.md' ':!assets'`; read `tests/test_the_release_check_watches_what_ships.py:47-58` | holds. Three lines match. `skills/verify/scripts/seal_stamp.py:208` is a comment. `tests/test_one_word_one_meaning.py:244` is the sweep that reads the README, and `:500` is a comment. `assets` is in `STAYS_HOME` at `:55`. The body now reads "Nothing the plugin ships reads `assets/seals/`", and the overview names the test as the one reader. At 8b3f0c1e both said "no code reads", and this row did not hold |
| The page no longer says the S has no entry, the hygiene sentence is gone, and nothing else in the tree says the S has no entry (carried) | `overview.md:5`, `:17`; issue #978 | `git grep -n -i "has no entry\|no entry here\|test_release_hygiene" -- assets`; `git grep` of the "no entry" patterns outside `seal/` and the changelogs; the first again at 769f2aa4 | holds. Exit 1 at HEAD for both; at 769f2aa4 it finds `assets/seals/README.md:71` |
| No changelog fragment is owed (carried) | `overview.md:28`; PR body `:12` | read `docs/the-record-layout.md` §*A change writes fragments, never a shared file* and §*A commit after the build brings its changelog fragment along*; `STAYS_HOME` | holds. A change that alters nothing a release note states owes no fragment, and `assets` stays home |
| A `seen red` to re-run against the code before the change (carried) | the work item's records | read `overview.md:30` and both rounds | none exists. The overview says "No case", and the item plants no test |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| The spec | none; second rung. Issue #978 is the frame: add the S's `.ans`, `.png` and draw-again command from its tag | the tree: `assets/seals/placeholder-s.{ans,png}` and the README entry with its command are present | none. The issue names the tags through v0.22.0, and the entry is drawn from v0.22.1. `overview.md:15` records that difference, and its grounds hold |
| The build (the diff, `overview.md` at 824174e2) | the S gets an entry drawn from v0.22.1; the false hygiene sentence leaves; the preview rule is written down; no gate, hook or code changes; nothing the plugin ships reads the page | the issue; the tree (`git diff --stat 8a100e13...HEAD` outside this item touches only `assets/seals/`); every row above | none |
| The last round (`rounds/round-2.md`, verifying, at 20783810) | round 1's single `should` is fixed at eba4fa05; nothing new is opened | the tree: eba4fa05 touches only `assets/seals/README.md`, and nothing outside this item has changed since | none |
| The changelog | none, and none is owed | `docs/the-record-layout.md`; `STAYS_HOME` | none |
| The pull request body (`978-pr.md`, corrected) | the S's entry, how it is drawn, the preview rule and one false sentence removed; four verification rows | the tree on `:5` and `:7-12`, and on the rows at `:18-21` (the broad run covers `:21`) | none. The two sentences the earlier run named now hold |

Verdict: sealed
