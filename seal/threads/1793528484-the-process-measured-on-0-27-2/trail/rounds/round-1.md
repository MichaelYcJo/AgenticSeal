# Review round 1: 1793528484-the-process-measured-on-0-27-2

```seal
target: c8d0714e against release/v0.27.2
```

The branch against `94b03636`, read in a `git clone --no-local` of the branch worktree at `c8d0714e`, with `refs/pull/1113`, `1114`, `1115`, `1248` and `1257` heads and the current `release/v0.27.2` fetched into it. No earlier round exists, so nothing is carried from one. Facts carried from other records rather than re-established: #1038's C11 row (111 findings, 30 recurring, four chains in shipped text), read at `f8d1b8f6` as `trail/phases/phase-2.md` *The decisions* of that work item states it, and #1044's *The record* table (30 work items, 27 withheld runs, 23 whose reason names the body), read from the issue body. Every verdict below is this round's own. The round spent its reading on the three `worse` rows, D4, D5, the rows whose before did not reproduce, and the withhold rows, as the spawn prompt asked.

## Findings

### 1. D5 says every crafter spawn that builds a phase gets 33,989 B of `skills/implement/SKILL.md` through `Read` and reads it whole, where 2 of the 9 phase builds read none of it through `Read` and opened line ranges through `sed`

```seal
severity: should
location: `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md:226`, `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md:231`
evidence: executed `python3 -I test_tmp_segments.py <clone> <session fabe08e7> agentic:crafter --item 1221 --item 1222 --item 1223 --item 1229 --item 1038`, `python3 -I - <each crafter transcript>, listing every Read, Skill and Bash call that names implement`
```

Why it matters: D5 is an issue draft the orchestrator files as it stands. The issue asks whether a crafter needs the whole file or a part of it. The sample already holds two crafters that opened only parts, and D5 says the opposite.

The claim: the title says step 1 "reads it whole", and `phase-3.md:231` says "The on-demand read returns 33,989 B of that file to every crafter spawn that builds a phase". What the transcripts show: the spawn description of every one of the 9 after crafter segments reads `Build #<n> phase <k>`, so all 9 build a phase. The record's own `segments.py`, written again from `trail/phases/phase-2.md` *Commands* and run once, gives (b) 0 B for `agent-a99ed23532f48819f` (#1221 phase 2) and for `agent-aeef3fbe075f90ff0` (#1222 phase 2). The first opened `skills/implement/SKILL.md` with `sed -n 1,140p` and then a second line range. The second ran `sed -n '293,468p'` on it. The same draft's first sentence of that paragraph says "7 of the 9 crafter segments read it through `Read`", so D5 contradicts itself. The medians are not affected: they stand at 34,653 B and 33,989 B, reproduced.

```markdown
Title: `chore: a crafter spawn opens 34,653 B of prose through Read where a smith spawn opened 846 B, since skills/implement/SKILL.md left the preload and step 1 sends the crafter to it`

The cause is one file. `agents/crafter.md` step 1 opens `skills/implement/SKILL.md`. All 9 crafter segments built a phase, and 7 of them read that file whole through `Read`, two of them twice. The other two, phase 2 of #1221 and phase 2 of #1222, opened line ranges of it through `sed`, which these readings do not count. At 0.20.0 the smith received `skills/implement/SKILL.md` in its preload. The crafter's preload fell by 73,242 B, and its first prefix fell from a median of 83,160 tokens to 44,342. Each whole read returns 33,989 B, the file with the line numbers `Read` adds.
```

```seal
verdict: fixed dd0f8454
answer: The finding holds. I listed every tool call naming `implement/SKILL.md` in the two transcripts: `agent-a99ed23532f48819f` (#1221 phase 2) ran `sed -n 1,140p` and a second range, and `agent-aeef3fbe075f90ff0` (#1222 phase 2) ran `sed -n '293,468p'`, with no `Read` of the file. D5's title now ends "step 1 sends the crafter to it", and its second paragraph is the paste-ready text: 7 of the 9 phase builds read the file whole through `Read`, and the two others opened line ranges through `sed -n`. D5's question now also says that two of the nine already opened only parts. Rule 12 sweep: `git grep` over the records for "every crafter", "reads it whole" and "whole" found no other statement of it. D1's row ("one `Read` of `skills/implement/SKILL.md`"), decision 4 and the changelog name the file and no count of readers, and they stand.
```

### 2. The withhold-over-the-body row reads `better`, -100 per cent, by a sort the before figure was not taken by, and D1 carries that verdict without the literal reading D3 gives

```seal
severity: should
location: `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md:136`, `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md:169`
evidence: executed `git log --no-merges -p refs/pull/1114/head -- <its directory>/guarantee.md`, `git log --no-merges -p refs/pull/1115/head -- <its directory>/guarantee.md`, `gh issue view 1044 --json title,body`
```

Why it matters: D1 becomes the standing section of #51's body, the durable baseline the next reading is held against. Its row names "Withheld runs over the pull request body" and reads `better`. But the count behind it uses a different sort on each side, and under the before's own sort the verdict is `same`.

Grounds. #1044's *The record* counts "Withheld runs whose reason names the pull request body", 23 of 27 runs over 30 work items (read, the issue body). Decision 7 (`phase-3.md:252`) sorts the after side by "the party its reason names as where the error stands". The withheld lines at the heads read as the record says. #1114's names `changelog.md:4` "copied into the pull request body", and #1115's says "the pull request body's `## Questions` copies it as open" (executed). Under #1044's sort those two count as over the body, giving 2 in 3. That is 0.667 per work item against 0.767, -13.0 per cent, `same` in the 20 per cent band. The 23 before runs were not re-sorted by decision 7's rule. The record says this in prose at `phase-3.md:78`, and D3 says it at `phase-3.md:205`. But the reading's row and D1's row state only the -100 per cent. The changelog's "over the hand-written body" is the measure that fits decision 7: before #1103 the whole body was hand-written. The row's label should say that too. The row for 0.27.2's five holds under either sort: #1248's reason names the orchestrator's part of the body.

```markdown
phase-3.md:136, the reading's row:
| Withheld runs over the hand-written body per work item, #1044's 0.22.x figure against the first three after #1103, by decision 7's sort; by #1044's own sort, whose reason names the body, the first three give 2, -13.0 %, `same` | #1044's body, *The record*, and this record's first withhold table | -100 % | runs | better |

phase-3.md:169, D1's row:
| Withheld runs over the hand-written body, per work item | 23 in 30, 0.22.x, from #1044 | 0 in the first 3 after #1103 · 1 in 0.27.2's 5 | better; by #1044's own sort, whose reason names the body, the first 3 give 2, which is the same within 20 % |
```

```seal
verdict: fixed dd0f8454
answer: The finding holds. The before figure was taken by #1044's sort, the after by decision 7's, and only the prose and D3 said so. The reading's row is renamed "over the hand-written body", names decision 7 as its sort, and states the literal reading beside it: by #1044's own sort the first three give 2, -13.0 %, `same`. D1's row carries the same name and the literal reading in its verdict cell. The verdict stays `better` by decision 7, so the tallies 28, 9 and 3 of 40 stand. The row for 0.27.2's five now says it is the same by either sort, since #1248's reason names the orchestrator's part. Rule 12 sweep: `git grep` for "over the body" and "hand-written" over the records and the changelog found D3, the paragraph under the first withhold table and the changelog's "None of the first three work items after #1103 was withheld over the hand-written body". Each already states decision 7's sort or the literal reading, so they stand.
```

### 3. `gaps.md` sends the owner the method behind the 12.3-minute slowest job, which phase 1 traced to one run and a 0.22.0 record

```seal
severity: should
location: `seal/threads/1793528484-the-process-measured-on-0-27-2/gaps.md:8`
evidence: executed `gh api repos/MichaelYcJo/AgenticSeal/actions/runs/38477758775/jobs?per_page=100`, `gh issue view 947 --json body`
```

Why it matters: a `## Not verified` row tells the sealer and the orchestrator what nobody could settle and who answers it. This row names the owner as the only answerer for a figure the branch's own record has already settled. The next reader then either asks a person for nothing, which is the costliest step, or stops trusting the row.

The claim: the row lists "the CI medians with the 12.3-minute slowest job" among four figures for which "No record states it, and no reading phase 1 tried gives them", and "nobody can re-derive it from the tree". What phase 1 found: `phase-1.md:93` says the body's 12.3 min and Windows 42.4 are run `38477758775`'s slowest job and Windows leg, and that `v0.22.0`'s phase record cites that run. This round re-read the run's jobs, which gave slowest 12.3, ubuntu 6.9, Windows 42.4 and macOS 22.7 (executed). #947's body gives the slowest job with no "median" and the legs as medians (executed). So 12.3 has its reading, one run's slowest job. 42.4 is one run's leg, no median, which explains why no median reading gives it. Only ubuntu 9.9, macOS 21.6, the 463 KB and the 160,228 test lines are left with no method. The `not reproduced` labels at `phase-1.md:73-76` hold, since the re-run reading, the median over the day, gives none of them.

```markdown
| The method behind four of the body's *Before* figures: the 463 KB of on-demand skills and templates, the 160,228 test lines, and the ubuntu 9.9 and macOS 21.6 leg medians. No record states it, and no reading phase 1 tried gives them (`trail/phases/phase-1.md` *The decisions*, items 2, 4 and 5). The body's slowest job, 12.3 min, and its Windows 42.4 are one run's figures, run `38477758775`, and no median (`trail/phases/phase-1.md` *What the CI before is, where it does not reproduce*). Phase 3's reading rests on the re-run figures, as `frame/plan.md` *Alternatives considered* A1 chooses | nobody can re-derive the four from the tree; the owner, who measured during 0.22.0's framing, is the only answerer, and no comparison waits on it |
```

```seal
verdict: fixed dd0f8454
answer: The finding holds. `trail/phases/phase-1.md` *What the CI before is, where it does not reproduce* traces the body's 12.3 min and Windows 42.4 to run `38477758775`, so the row asked the owner for a figure the record had settled. The `gaps.md` row now names the four figures with no method, the 463 KB, the 160,228 lines, ubuntu 9.9 and macOS 21.6, and says the 12.3 min and the 42.4 are one run's figures, citing that section. Its answerer cell reads "the four". Rule 12 sweep: `git grep` for "12.3" and "CI medians" found D2's "What did not reproduce" bullet in `trail/phases/phase-3.md`, which listed "its CI medians" among the figures no reading gave. It now names the ubuntu and macOS medians and says the slowest job and Windows figure are run `38477758775`'s. `trail/phases/phase-1.md:73` gives the body's 12.3 beside the re-run median under its own label `not reproduced`, which holds, and it stands.
```

### 4. The orchestrator's list of acts posts D1 before filing the issues D1 names, and leaves out D6

```seal
severity: should
location: `seal/threads/1793528484-the-process-measured-on-0-27-2/frame/plan.md:47-52`, `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md:147`
evidence: read `seal/threads/1793528484-the-process-measured-on-0-27-2/frame/plan.md:47-52`, `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md:147-242`
```

Why it matters: `phase-3.md:147` sends the orchestrator to `frame/plan.md` *Operational impact* for the acts. Read in that order, the orchestrator edits #51's body with D1 at step 1, while D1's last sentence names "<D4's number> and <D5's number>". Those issues are filed only at step 3. The list has no step for D6, the comment on #1020 that decision 3 puts in place of an issue draft. D4 and D5 each say "file it, then name its number in D1", and the changelog names "the comments on #51, #1044 and #1020". So the drafts and the list disagree about the order and about what is posted. The frame was written before decision 3 existed, so the list could not name D6. The drafts' header is where the order can be given without a frame edit.

```markdown
The orchestrator takes each act after the seal, in this order, since D1 names D4's and D5's numbers: file D4 and D5, edit #51's body with D1 and post D2 on #51, post D3 on #1044, and post D6 on #1020. `frame/plan.md` *Operational impact* lists the same acts but D6, which decision 3 adds, and orders D1 first. No draft holds a path outside the repository. `<sealed>` stands for the commit the sealer seals, which the orchestrator writes in before it posts.
```

```seal
verdict: fixed dd0f8454
location: `seal/threads/1793528484-the-process-measured-on-0-27-2/frame/plan.md:47-52`, `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md:147`
answer: The finding holds. The orchestrator folded `frame/plan.md` *Operational impact* in place at `b91222b3`: D4 and D5 are filed first, then D1 and D2 go on #51, then D3 on #1044 and D6 on #1020. I did not apply the paste-ready text as given. Since `b91222b3` the plan names D6 and gives that order, so the text's "lists the same acts but D6 … and orders D1 first" no longer holds. The drafts' head in `trail/phases/phase-3.md` now cites the plan's order and states it in the same sequence, and D4's and D5's "file it, then name its number in D1" agree with it. Rule 12 sweep: `git grep` for "Operational impact" over the records found only the drafts' head and `frame/plan.md` itself. The changelog's list of acts names no order, and it stands.
```

## Confirmations

```seal
confirms: none
```
What matched: the `worse` row for a session's start, `phase-3.md:106`, and D4's figures. The core's text below its frontmatter at `94b03636` is 8,403 B. The header line with no path is 112 B, newline included, so the total is 8,515 B (executed, with the frontmatter pattern of `hooks/lib/core.py`). `CLAUDE.md` is 1,143 B at `94b03636` and 9,261 B at `a8d83663`, and its block between the `specseal:start` and `specseal:end` markers is 4,694 B (executed). `install.sh` at `a8d83663` writes that block (read). (9,658 - 9,261) / 9,261 is +4.3 per cent, past the 1 per cent tree band, so `worse` follows from the band. At `a8d83663` the `session-start` group runs `version-check.py`, `root-migrate.py`, `ledger-migrate.py` and `hook-install.py`. At `94b03636` it runs `version-check.py` alone, and `session-core` runs `core-start.py` (read, `hooks/dispatch.py` at both). `gaps.md:25` says the group stands on both sides, which holds, and its contents differ.

```seal
confirms: none
```
What matched: the two crafter prose rows, `phase-3.md:125` and `129`. The record's `segments.py`, written again as a probe, gives the after crafter medians 34,653 B (a) and 33,989 B (b), and the before smith medians 846 B and 0 B. It gives the framer and smith first-prefix medians 73,640 and 83,160, and the after crafter's 44,342 (executed). `agents/smith.md` at `v0.20.0` lists `agent-contract`, `implement` and `writing-style`. `agents/crafter.md` in the 0.27.1 the after segments ran lists `core` and `agent-contract`, and its step 1, line 28, opens `skills/implement/SKILL.md` (read). D5's cause holds. The preload plus the (b) read falls from 106,350 B to 67,097 B per crafter, so the `worse` rows are bytes moved from one measure to the other, which D5's second paragraph states in parts.

```seal
confirms: none
```
What matched: the rows whose before did not reproduce. At `a8d83663` and at `f95f0ba8`, one commit later, the `tests/` `.py` files hold 160,138 lines, and `.test_durations` prices 13,482 cases at 7,861.7 s (executed). A scan of the six commits after `a8d83663` through `v0.22.0` that touch `tests/` finds no 160,228 (executed). So `phase-1.md:64` and `:66` keep their `not reproduced` labels. The after CI, re-read from the five branches' `tests` runs, gives one completed, uncancelled run per branch. Its medians are slowest 2.8, ubuntu 1.5, Windows 8.9 and macOS 3.6 (executed), as `phase-1.md:73-76` gives them. `docs/` directly under it is 708,070 B at `a8d83663` and 242,145 B at `94b03636`. The after preload is 36,402, 33,108, 32,008, 32,262 and 25,198 B (executed).

```seal
confirms: none
```
What matched: the round and convergence rows. `finding_counts.py --released-at 94b03636` in the clone gives the four after rows as `phase-3.md:50-53` holds them (executed). At `2eb472b1` the 22 before items hold 6, 3, 4, 3, 3, 2, 6, 2, 3, 5, 2, 2, 6, 3, 2, 2, 2, 2, 3, 3, 1 and 1 round files, median 3 (executed). `v0.21.1` holds no `docs/the-review-record.md`, `docs/round-record-spec.md` says the round is in the file name, and `b914a1c7` deleted the 14 items' round files (executed), so departures 1 and 2 of phase 3 stand on what they cite. #1223's three findings and their `regression:` lines, and its *Judgments of the run* row at the third finding round, read as D6 states them at `a8269d90` (read). #1201 merged at 2026-10-31T07:14:33Z, before #1202's 07:16:17Z (executed).

```seal
confirms: none
```
What matched: the withhold tables. The added `Verdict: withheld` lines at the heads of #1113, #1114, #1115 and #1248 are one each, with the reasons `phase-3.md:74-76` and `:84` summarise (executed). #1044's title and *The record* give 27, 23 and 30 (executed).

```seal
confirms: none
```
What matched: scenario S8 and S9 at the target. `git diff --stat 94b03636 HEAD -- . ':!seal/threads/1793528484-the-process-measured-on-0-27-2'` prints nothing, and the branch adds 9 files, all in this work item's directory. `bin/test tests/test_censuses.py -q -p no:xdist` gives 176 passed (both executed). The tallies 28, 9 and 3 of 40 match the table at `phase-3.md:100-139` (read). Sampled changes recompute as given: +4.3, +3,996, -13.0 for the literal withhold reading, -73.9 and -77.8 (executed by hand from the cited figures).

```seal
confirms: none
```
What matched, after the phases read it: #1257 merged at 2026-11-01T11:35:14Z as `569780ef`, with its head still `f8d1b8f6` (executed, `gh pr view 1257`). `release/v0.27.2` is now `569780ef`. The diff from `94b03636` to it outside `seal/threads` and `seal/follow-up.md` prints nothing, and #1038's directory is the same at `f8d1b8f6` and at `569780ef` (executed). So every `before its merge` reading equals its merged state, which answers `gaps.md:12`. The branch is not based on `569780ef`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The before CI sample's 60 runs and `subsets.py` were not re-run; one run of it, `38477758775`, was re-read | `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-1.md:71-93` | the sealer, at its sample of the crafter's claims |
| The before warden and sealer first-prefix and prose medians, and every after kind but the crafter and framer, were not re-run | `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-2.md:30-44` | the sealer, at its sample |
| The O1 and O2 sums and phase 1's search for 463 KB were not re-run | `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-1.md:56-57` | the sealer, at its sample |
| #1038's C11 counts are carried from that work item's record and not re-counted, as `frame/design.md` *Scope* item 9 directs | `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md:56` | nobody: the frame cites the row |
| The full suite, the repository-wide lint and the format check at the head, labelled `unverified` in `gaps.md:7` | `seal/threads/1793528484-the-process-measured-on-0-27-2/gaps.md:7` | the orchestrator, by `seal gate` once the rounds settle |
| Whether the pull request is rebased onto `569780ef` before the gate, now that #1257 merged | `release/v0.27.2` | the orchestrator |
| A phase's scratch files outlive their phase. The work item's scratch directory still holds `phase2/` with `segments.py`, `search.py`, `survey.py`, `after.tsv`, `before.tsv` and `boundary.log`, against contract rule 7. This round did not start them and removed nothing | the session's scratch directory for this work item | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `test_tmp_ci.py`, run once in the clone and deleted: each of the five branches' `tests` runs on a `pull_request` event, and the job minutes of each completed, uncancelled one | one run per branch, all `success`; medians slowest 2.8, ubuntu 1.5, Windows 8.9, macOS 3.6 |
| `test_tmp_segments.py`, phase 2's `segments.py` written again from its record, run once over `db35d01d`'s smiths and framers and `fabe08e7`'s crafters and framers of the five, and deleted | smith medians prefix 83,160, (a) 846, (b) 0; framer 73,640, 6,340, 1,070; crafter 44,342, 34,653, 33,989, with (b) 0 for `agent-a99ed23532f48819f` and `agent-aeef3fbe075f90ff0`; after framer 45,218, 0, 0 |
| `python3 -I -` over three crafter transcripts, listing each `Read`, `Skill` and `Bash` call naming `implement` | `agent-a99ed23532f48819f` and `agent-aeef3fbe075f90ff0` open `skills/implement/SKILL.md` through `sed -n` line ranges, and `agent-a4313ae6247730ba9` through `Read` |
| `gh api .../runs/38477758775/jobs?per_page=100`, summed per leg | slowest 12.3; ubuntu 6.9, Windows 42.4, macOS 22.7 |
| `git show <c>:<p> \| wc -l` over `tests/**.py`, and a `json.load` of `.test_durations`, at `a8d83663`, `f95f0ba8`, `v0.21.0`, `v0.22.0` and each `tests/`-touching commit through `v0.22.0` | 160,138 at `a8d83663` and `f95f0ba8`; no commit gives 160,228 |
| `python3 .github/scripts/finding_counts.py --released-at 94b03636` in the clone at `94b03636` | 12 rows, exit 0; the four after rows as recorded |
| `git ls-tree` of each before item's `rounds/` at `2eb472b1` | 22 items, the counts recorded, median 3 |
| `git log --no-merges -p refs/pull/<n>/head -- <dir>/guarantee.md`, the added `Verdict: withheld` lines, for 1113, 1114, 1115 and 1248 | one distinct withheld line each, reasons as recorded |
| `bin/test tests/test_censuses.py -q -p no:xdist` in the clone at `c8d0714e` | 176 passed |
| `gh pr view 1257 --json mergedAt,mergeCommit`, then `git diff --stat 94b03636 569780ef -- . ':!seal/threads' ':!seal/follow-up.md'` | merged 2026-11-01T11:35:14Z as `569780ef`; the diff prints nothing |
