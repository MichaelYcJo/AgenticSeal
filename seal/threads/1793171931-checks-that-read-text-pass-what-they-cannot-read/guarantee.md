# Guarantee: 1793171931-checks-that-read-text-pass-what-they-cannot-read

| Field | Value |
|---|---|
| Target SHA | 94ad44c2 against 5287dd42 |
| Broad gate | 441bb9fd against 5287dd42 |

## Claims re-run

The probes ran from a clone of the branch at `94ad44c2`. Outside this work item's directory, that tree is the same as `c825fd2c`, so it holds the code the audit read. The clone, the two probe files, their output and every scratch repository they made were deleted by their recorded paths after a single run. The audit adds no test case, so no record holds a `seen red` claim to re-run.

| Claim | Source | Command | Result |
|---|---|---|---|
| The gate's run is at HEAD, or only this directory changes after it | `trail/gate.md:5` | `git log --no-merges --name-only 441bb9fd..HEAD ^5287dd42`, with the base resolved from `release/v0.24.0@{upstream}`; `git merge-base --is-ancestor 441bb9fd HEAD` | holds. Exit 0. The one commit after the run, `94ad44c2`, changes `trail/gate.md` alone |
| The body's part above `## Not from the records` is the records' text | the body file the orchestrator handed over | `bin/seal pr-body <item> --body <file> --check` with the tree's script, then again with the installed `seal` | holds, exit 0 both times. The orchestrator's part is `Closes #956` alone |
| S9: no tree file changes outside this directory | `frame/design.md:235`, `trail/phases/phase-5.md:124-126` | `git diff --name-only c825fd2c..HEAD -- . ':!seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read'`; `git status --porcelain` | holds. Both commands printed nothing. `git diff --stat 5287dd42...HEAD` lists 14 files, all in this directory |
| S7: the comment on #956 matches the phase 5 section byte for byte | `trail/phases/phase-5.md:23-73`, `trail/rounds/round-3.md` *Confirmations* | `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6464014816`, with the body compared to `phase-5.md` lines 25 to 73 | holds. Updated at 2026-10-28T08:36:37Z, 15,378 bytes. The body is lines 25 to 73 plus their closing newline |
| Eleven issues are filed into `release: 0.24.1` and name their rows | `trail/phases/phase-5.md:77-91` | `gh issue view <N> --json number,title,state,milestone,body` for #1121 to #1129, #1132 and #1133 | holds. All are open in `release: 0.24.1`, each title has a commit prefix, and each body states *Done when* and names the rows table 5 gives it. #1121's body names R3, R9 and R11. Comment 6464431981 on #1121 adds R8 (`gh api`) |
| R2: a blank line cuts the old-spellings table, and that spelling then reads as prose | `trail/phases/phase-1.md:28` | probe: `chain_check.grammar` over `docs/the-review-record.md` and over a copy with a blank line before line 61 | holds. The full table reads `Target SHA:`, `fix of a fix:` and `refixes:`. The cut table loads without an error and reads only `Target SHA:` and `refixes:` |
| R4: every near miss of the verdict line is refused | `trail/phases/phase-1.md:30` | probe: `chain_check.verdicts_of` and `#verdict_word` over seven lines | holds. Only `Verdict: sealed` reads `sealed`. Emphasis on the label or the word, `Sealed`, a trailing period and a blockquote each read as a verdict line with no word. A Cyrillic `е` in the label gives no verdict line |
| R10: the question gate lets a question through where `Automation` reads `Yes` | `trail/phases/phase-1.md:36` | probe: `hooks/question-gate.py` fed an `AskUserQuestion` payload in three scratch repositories whose `routing.md` differ only in `Automation` | holds. `yes` gives `deny`. `Yes` and `**yes**` give no output, exit 0 |
| R23: the worktree guard does not see a switch spelled by a parameter | `trail/phases/phase-2.md:34` | probe: `hooks/worktree-guard.py` on a single-stream scratch repository with a tracked change, `HOME` set to a scratch folder | holds. `git switch feature` gives `ask`. `G=git; $G switch feature`, `$(echo git) switch feature` and `git rebase {main,feature}` give no output |
| R25: a fragment at another path passes `--check` | `trail/phases/phase-3.md:24` | probe: `gather_changelog.py --check --root <scratch>`, with one fragment gathered and a second at three paths | holds. `frame/changelog.md` and `changelog.markdown` both exit 0 with "1 changelog fragments, all gathered". As a control, `changelog.md` exits 1 and names the fragment |
| R32: no line opening `Reads:` stands | `trail/phases/phase-4.md:34` | `git grep -c -E '^\s*(#\s*)?Reads:' c825fd2c -- . ':!seal' ':!changelog' ':!CHANGELOG.md'` | holds, exit 1 |
| R34: the citation at `gather_changelog.py:43-44` is a real miss | `trail/phases/phase-4.md:21-28` | probe: lines 41 to 44 read, then `docs/the-record-layout.md` searched for the cited words | holds. Lines 43-44 cite `docs/the-record-layout.md`'s *A marker counts only on a live line*. The document has no heading and no bold lead with those words, and the phrase does not appear in it |
| R36: #1043 has not landed at the release tip | `trail/phases/phase-4.md:38` | `git ls-remote origin refs/heads/release/v0.24.0`; `gh issue view 1043 --json state` | holds. The tip is still `5287dd42` and #1043 is open |
| R40: the no-probe grader matches one spelling only | `trail/phases/phase-4.md:42` | probe: the grader's `pattern` and `match` read from `shape-no-probe-left.md`, then run through `re.search` over four names | holds. The grader is `test_tmp_` with `not_contains`. Only `test_tmp_x.py` matches. `tmp_test_x.py`, `test-tmp-x.py` and `Test_tmp_x.py` do not |
| The plan's real user path is gone after the census fix | `frame/plan.md:31-32`, `441bb9fd` | `git show 441bb9fd` | holds. The worktree's absolute path is replaced by its branch name, and `441bb9fd` changes only `frame/plan.md` |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | `frame/design.md` audits R1 to R43 at `c825fd2c` with one executed probe per row. It posts the table as a comment on #956 and files each fix into `release: 0.24.1`, or `#1038` where no one work item can carry it. It changes no tree file, and both `## Rule changes` and `## Removes` read `nothing` | issue #956 *The change*, which asks for one table reported and not fixed, with fixes filed into 0.24.1 or left to #1038; the tree, where S9 printed nothing (executed) | none. #956's "33 of 311" is replaced by a count at `c825fd2c`, and `frame/design.md` *The citation reader, re-based* gives the reason: #1005's records hold no command that could be re-run |
| the build | `trail/phases/phase-1.md` to `phase-5.md` hold 43 rows. They count 8 `refuses`, 3 `passes`, 7 `skips`, 24 `mixed`, and R36 not landed; and 18 `yes`, 7 `limit`, 17 `no`. Eleven issues are filed and the comment is posted | the spec's columns and words; GitHub, where the comment matches and all eleven issues are in `release: 0.24.1` (executed); the ten probe claims re-run above (executed). Round 1 re-ran R3, R11, R14, R29 and R24, and round 2 re-ran R24 at `5287dd42` | none found. `gaps.md` records six departures from the frame (R2, R3, R5, R10, R16 and R24), each grounded in a probe or a reading |
| the last round | `trail/rounds/round-3.md` opens no finding. It confirms that round 2's R8 finding is fixed in `bedaa645`, and that the patched comment still matches `phase-5.md` | the tree: R8's `Fix` cell reads `#1121` at `phase-5.md:36` (read), and comment 6464431981 stands on #1121 (executed); GitHub at 08:36:37Z (executed) | none |
| the changelog | there is no `changelog.md`. `gaps.md` *Not done* says the audit changes no shipped file, so no release note would state anything | the spec's empty `## Rule changes` and `## Removes`; S9 (executed) | none |
| the orchestrator's part of the pull request body | `Closes #956` | #956 asks for an audit whose result is a table on the issue, with the fixes filed. Both stand on GitHub (executed). Q1, the `CLAUDE.md` rule, is the owner's to decide after the audit by #956's own words, and stays open on its default (a) | none |

The commits before round 2, `b683992b` to `6adbca75`, carry no `Seal-Routing:` trailer (executed, `git log --format='%(trailers:key=Seal-Routing)'`). Every commit from `c5eddfb9` onward carries it. Round 2 raised this under *Not judged*, and round 3 recorded the orchestrator's decision not to rewrite those commits. No party claims the trailers are there, so this is disclosed and does not contradict any claim.

Verdict: sealed
