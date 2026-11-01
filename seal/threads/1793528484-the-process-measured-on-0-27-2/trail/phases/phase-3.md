# Phase 3: 1793528484-the-process-measured-on-0-27-2

## What this phase found

### The measured state

- **The after tree is still `94b03636`**, the head of `origin/release/v0.27.2` after `git fetch origin` when the phase started (executed: `git rev-parse origin/release/v0.27.2`). `git diff --stat 94b03636 origin/release/v0.27.2 -- . ':!seal/threads' ':!seal/follow-up.md'` printed nothing, so no process change landed after the frame. Scenario S8's `git diff --stat origin/release/v0.27.2...HEAD -- . ':!seal/threads/1793528484-the-process-measured-on-0-27-2'` printed nothing at `43076c9f` (both executed).
- **#1038 was read at `f8d1b8f6`, which then merged unchanged.** Pull request #1257 was open at `f8d1b8f6` at 2026-11-01T11:10:16Z (executed: `date -u`, then `gh pr view 1257 --json state,headRefOid,mergedAt,mergeCommit`). Round 1 of this work item found it merged, and the fix pass confirmed it: #1257 merged at 2026-11-01T11:35:14Z as `569780ef` with its head still `f8d1b8f6`, and #1038's directory is the same at both commits (executed: `gh pr view 1257 --json state,mergedAt,mergeCommit,headRefOid`, `git diff --stat f8d1b8f6 569780ef -- seal/threads/1793521558-the-record-decides-each-proposed-verifier`, which printed nothing). So #1038's rounds and withholds below, read at that head, are its merged state.
- **No #1038 segment was added after phase 2's moment.** Session `fabe08e7` held 36 subagent transcripts at 2026-11-01T11:10:16Z: the 35 phase 2 counted, and `agent-a6411a2e819603fbb`, this phase's own (executed: `ls <session>/subagents/*.jsonl | wc -l`, and each `.meta.json`'s `agentType` and description sorted by the transcript's modification time). Phase 2's reading of #1038's six segments stands, so `segments.py` was not run again.
- **The after work items and their directories.** Each directory was matched to its issue by the number its `changelog.md` names, and each one's records at the merge commit equal its pull request's head (executed: `git diff --quiet refs/pull/<n>/head <merge> -- seal/threads/<directory>`).

| Work item | Pull request | Directory | Records read at |
|---|---|---|---|
| #1221 | #1248 | `1793521561-a-windows-run-names-its-skipped-cases` | `ad5246ce` |
| #1222 | #1250 | `1793521560-the-checks-wait-starts-before-a-check-reports` | `161a42aa` |
| #1223 | #1252 | `1793521559-a-finding-is-counted-once` | `a8269d90` |
| #1229 | #1253 | `1793521562-the-proofer-cases-come-from-thread-records` | `94b03636` |
| #1038 | #1257 | `1793521558-the-record-decides-each-proposed-verifier` | `f8d1b8f6`, merged unchanged as `569780ef` |

### Whether the frame holds

Four parts of the frame do not hold as written. Each is decided under *The decisions*.

1. **The before round records are not all at `v0.21.1`.** `frame/design.md` *Scope* item 8 reads each before work item's round records at `v0.21.1`. 22 work items have a directory that a commit of `v0.20.0..v0.21.1` adds under `seal/specs/` (executed). At `v0.21.1`, 14 of them hold no `rounds/` directory: `b914a1c7` (#933, "the process record of the fourteen 0.21.0 work items leaves the tree by settle --retire-process") deleted those directories before the tag (executed: `git log --diff-filter=D v0.20.0..v0.21.1 -- <directory>/rounds/*`).
2. **The round record rule at `v0.21.1` is not in `docs/the-review-record.md`.** That file does not exist at the tag (executed: `git show v0.21.1:docs/the-review-record.md` fails). The rule then stood in `docs/round-record-spec.md`. That document is the authority for the rows of `seal/specs/<work-item-id>/rounds/round-N.md`, and says "The round is already in the file name, `rounds/round-N.md`" (read, at `v0.21.1`). The same directories hold `round-N-report.md` and `round-N-fixes.md` beside each record.
3. ***Scope* item 11 asks for "one issue draft for each chain".** Item 9 finds one chain of three in the five after work items, #1223's. It also cites C11's four chains. #1020 is open in `release: 0.29.0` and is the issue whose design reads recurrence across rounds (executed: `gh issue view 1020 --json title,state,milestone`). #1038's C11 row already drafts its window's chains as comment D3 on #1020.
4. ***Scope* item 11 asks for one issue draft for each `worse` row.** Two of the three `worse` rows are readings (a) and (b) of one measure on one kind, and both come from the same `Read` of `skills/implement/SKILL.md` (`trail/phases/phase-2.md` *The measures*, the paragraph under the prose table).

Phase 1 left a comparison open, and its decision is decision 5 below. `CLAUDE.md` at `94b03636` is 1,143 B, and the plugin's `SessionStart` hook prints the core into each session beside it (`trail/phases/phase-1.md` *The measures*, the paragraph after the preload table).

`templates/records/` holds no changelog template, so this work item's `changelog.md` takes the shape this release's other fragments take: one heading and one bolded entry (read: `ls templates/records/`, and the four fragments of #1221, #1222, #1223 and #1229).

### The measures

Every figure below is `executed` by the command its paragraph names, and each command stands whole under *Commands*.

**Review rounds per work item** (`finding_counts.py` after, `before_rounds.py` before). A round is one round record, which is a `round-<n>.md` file in the work item's rounds directory on both sides.

| Side | Work items | Rounds each | Median | Mean |
|---|---|---|---|---|
| Before, 0.21.0's 14 items, at `2eb472b1` | 14 | 6, 3, 4, 3, 3, 2, 6, 2, 3, 5, 2, 2, 6, 3 | 3 | 3.6 |
| Before, 0.21.1's 8 items, at `2eb472b1` | 8 | 2, 2, 2, 2, 3, 3, 1, 1 | 2 | 2.0 |
| Before, both | 22 | 66 in all | 3 | 3.0 |
| After, the five at the heads named above | 5 | #1221 1, #1222 3, #1223 4, #1229 3, #1038 1 | 3 | 2.4 |

Every before work item's `routing.md` reads `Review` `through the review chain` at `2eb472b1`. The 14 items' round files at `2eb472b1` equal those at `v0.21.0`, and the 8 items' round files equal those at `v0.21.1` (executed: `git diff --stat` of each pair over the items' `rounds/` directories, each printing nothing). `finding_counts.py`'s rows for the five after items, with the other released work items it prints left out:

| work item | findings | regression or reopens | records alone | rounds |
|---|---|---|---|---|
| 1793521561-a-windows-run-names-its-skipped-cases | 2 | 0 | 2 | 1 |
| 1793521560-the-checks-wait-starts-before-a-check-reports | 3 | 1 | 0 | 3 |
| 1793521559-a-finding-is-counted-once | 5 | 2 | 0 | 4 |
| 1793521562-the-proofer-cases-come-from-thread-records | 3 | 2 | 1 | 3 |
| 1793521558-the-record-decides-each-proposed-verifier | 4 | 0 | 4 | 1 |

**Whether runs under the current *The run* paragraph converge** (`recurrence.py`, over the five). For C11's window, the 17 work items merged after PR #1191 through #1244, this work cites #1038's `trail/phases/phase-2.md` *The decisions*, row C11, at `f8d1b8f6`, the head #1257 merged, and counts nothing again. That row counts 111 findings, 30 of them recurring, and four chains of three or more in shipped text, those of #1201, #1203, #1230 and #1241. Shipped text means a `location:` path outside the work item's directory. One fact about the window bears on the question and is not in that row. #1201 is the chain whose plan holds no *Judgments of the run* section, and it merged at 2026-10-31T07:14:33Z. That was before #1202, the design `96c11614` that brought the current paragraph, merged at 07:16:17Z, and `96c11614` is not an ancestor of #1201's head (executed: `gh pr view 1201 --json mergedAt`, `git log -1 --format=%cI 96c11614`, `git merge-base --is-ancestor`). So none of C11's four chains ran under the current paragraph without a *Judgments of the run* section: three had the section take the structural question, as the row says, and #1201's run predates the paragraph. Whether every other run of the window past three finding rounds holds its row is not counted here (`gaps.md` *Not done*).

| Work item | Findings | Recurring, each with its line | Chains of three or more | Rounds holding a finding | Reframed | *Judgments of the run* past or at the third finding round |
|---|---|---|---|---|---|---|
| #1221 | 2 | none | none | 1 | no | not owed |
| #1222 | 3 | `round-2#1 reopens: round-1#1` | none | 1, 2 | no | not owed |
| #1223 | 5 | `round-2#1 regression: round-1#2`, `round-3#1 regression: round-2#1` | `round-1#2` to `round-2#1` to `round-3#1`, all in `.github/scripts/finding_counts.py`, the third also in its `gaps.md` | 1, 2, 3 | no | held: the row "After three finding rounds, the run goes on", naming the counts 2, 2, 1 and this section's paragraphs |
| #1229 | 3 | `round-2#1 regression: round-1#1`, `round-2#2 regression: round-1#1` | none | 1, 2 | no | not owed |
| #1038 | 4 | none | none | 1 | no | not owed |

None of the five has a fourth finding round. #1223's round 4 is a verifying round whose `## Findings` reads "None" (read). #1229's two regressions name one finding in one round, so neither is the second regression after a fix-pass route that the paragraph names as the frame's signal.

**Withholds over the pull request body** (`withholds.py`, in a clone with every `refs/pull/*/head` fetched). The first three work items routed through the review chain whose pull request merged after #1103's, which merged at 2026-10-28T04:43:30Z, are #1052 (PR #1113), #712 (PR #1114) and #920 (PR #1115). The list comes from `gh pr list --state merged --search "merged:>2026-10-28T04:43:30Z"`, sorted by `mergedAt`, with each pull request's `routing.md` read at its head. Four pull requests merged before #1113. #1104 and #1105 are a fragment fold and the release, #1108 is the settle of 0.23.1, which deletes three directories, and #1112 adds no `routing.md` (executed).

The table takes the shape of #1044's comment of 2026-10-28T03:04Z:

| Work item | Withheld runs | Over the body | Over something else |
|---|---|---|---|
| #1052, the issues filed against the old tree (#1113) | 1 | 0 | 1: `gaps.md:16`, the closing memo, stated a fact about #1109 that this work item's own edit had made false |
| #712, the spawn rows (#1114) | 1 | 0 | 1: `changelog.md:4`'s claim about the column a description starts at, which the tree contradicted; `seal pr-body` had copied it into the body |
| #920, the creation row (#1115) | 1 | 0 | 1: `frame/questions.md:43` left W1's `Status` `open` after phase 1 answered it; the body's `## Questions` copied it |

Each of the three heads holds one distinct withheld verdict and ends `Verdict: sealed`. A verdict is sorted by the party its reason names as where the error stands. Two of the three reasons, #712's and #920's, also say the body copied the record. Under #1044's own wording, "whose reason names the pull request body", those two would count as over the body. The error stood in the record each time, and since #1103 the body's factual part is that record's text.

The five after work items, read from each head's `guarantee.md`, which keeps every run's verdict since 0.27.0, and by the same commit reading as a cross-check (both executed):

| Work item | Withheld runs | Over the body | Over something else |
|---|---|---|---|
| #1221 (#1248) | 1 | 1: the orchestrator's part of the body said run `41290162769` had "every job `success`" where `release-report` was `skipped`, and cited `trail/gate.md` for a count that record does not hold | 0 |
| #1222 (#1250) | 0 | 0 | 0 |
| #1223 (#1252) | 0 | 0 | 0 |
| #1229 (#1253) | 0 | 0 | 0 |
| #1038 (#1257) | 0 | 0 | 0 |

The six sealer segments phase 2 counted for these five, two of them #1221's, agree: one run per verdict block (`trail/phases/phase-2.md` *Each segment*).

**The session's preload in this repository, beside `CLAUDE.md`** (`core_out.py`). At `94b03636` the core hook's output, `hooks/lib/core.py#output`, is 8,515 B, not counting the path its first line names. That figure is the core's 8,403 B below its frontmatter and a 112 B header line that names the plugin version `0.27.2` and the file's SHA-256 (executed). With `CLAUDE.md`'s 1,143 B, a session in this repository starts with 9,658 B and that path. At `a8d83663`, `hooks/hooks.json` holds one `SessionStart` group, `session-start`. At `94b03636` it holds that group and `session-core`, which runs `hooks/core-start.py` (executed: `git show <commit>:hooks/hooks.json`). `core-start.py` "prints in every session, in any directory" (read, its docstring).

### The reading

A measure read off the tree is `same` within 1 per cent. A measure read off runs or samples is `same` within 20 per cent (`frame/design.md` *Scope* item 11). Each row cites the phase record row its before and after stand in. The change is the after against the before, as a share of the before.

| Measure | Before and after stand in | Change | Band | Verdict |
|---|---|---|---|---|
| Preload, framer and framer | `phase-1.md` *The measures*, preload table, row framer | -63.3 % | tree | better |
| Preload, smith and crafter | the same table, row smith | -68.9 % | tree | better |
| Preload, warden and proofer | the same table, row warden | -68.7 % | tree | better |
| Preload, sealer and sealer | the same table, row sealer | -10.7 % | tree | better |
| Preload, scribe and tracer | the same table, row scribe | -14.7 % | tree | better |
| `CLAUDE.md` | the same table, row `CLAUDE.md` | -87.7 % | tree | better |
| A session's start in this repository: `CLAUDE.md` and the core hook's output | the same table, row `CLAUDE.md`, and this record's *The session's preload* paragraph | +4.3 %, the path the header names not counted | tree | worse |
| `docs/`, files directly under it (D2) | `phase-1.md` *The measures*, docs table, row D2 | -65.8 % | tree | better |
| `docs/`, every file (D1) | the same table, row D1 | -64.9 % | tree | better |
| On-demand skills and templates without `scripts/` (O2) | the same table, row O2 | -21.3 % | tree | better |
| On-demand skills and templates with `scripts/` (O1) | the same table, row O1 | -42.7 % | tree | better |
| Cases, collected | `phase-1.md` *The measures*, suite table, row collected | -54.9 % | tree | better |
| Cases, priced by `.test_durations` | the same table, row priced | -54.2 % | tree | better |
| Windows seconds | the same table, row Windows seconds | -87.3 % | tree | better |
| Test lines, `.py` files | the same table, row `.py` files | -40.9 % | tree | better |
| Test lines, every file | the same table, row every file | -41.4 % | tree | better |
| CI, slowest job | `phase-1.md` *The measures*, CI table, row slowest job | -75.9 % | runs | better |
| CI, ubuntu runner-minutes | the same table, row ubuntu | -84.0 % | runs | better |
| CI, Windows runner-minutes | the same table, row Windows | -78.2 % | runs | better |
| CI, macOS runner-minutes | the same table, row macOS | -81.8 % | runs | better |
| First prefix, framer and framer | `phase-2.md` *The measures*, first prefix table, row framer | -38.6 % | runs | better |
| First prefix, smith and crafter | the same table, row smith | -46.7 % | runs | better |
| First prefix, warden and proofer | the same table, row warden | -41.5 % | runs | better |
| First prefix, sealer and sealer | the same table, row sealer | -24.1 % | runs | better |
| Prose (a), framer and framer | `phase-2.md` *The measures*, prose table, row framer | -100 % | runs | better |
| Prose (a), smith and crafter | the same table, row smith | +3,996 % | runs | worse |
| Prose (a), warden and proofer | the same table, row warden | 0 B on both sides | runs | same |
| Prose (a), sealer and sealer | the same table, row sealer | 0 B on both sides | runs | same |
| Prose (b), framer and framer | the same table, row framer | -100 % | runs | better |
| Prose (b), smith and crafter | the same table, row smith | from 0 B | runs | worse |
| Prose (b), warden and proofer | the same table, row warden | 0 B on both sides | runs | same |
| Prose (b), sealer and sealer | the same table, row sealer | 0 B on both sides | runs | same |
| Review rounds per work item, the median | this record, *The measures*, rounds table, rows "Before, both" and "After" | 0 % | runs | same |
| Recurring findings, as a share of findings | this record, *The measures*, the C11 citation and the rounds table's after rows | +8.8 % | runs | same |
| Chains of three or more, per work item | the same | -15.0 % | runs | same |
| A chain of three or more under the current paragraph, in a run with no *Judgments of the run* row for it | this record, *The measures*, the convergence paragraph and table | none on either side | runs | same |
| Withheld runs over the hand-written body per work item, #1044's 0.22.x figure against the first three after #1103, sorted by decision 7. By #1044's own sort, a reason that names the body, the first three give 2, which is -13.0 % and `same` | #1044's body, *The record*, and this record's first withhold table | -100 % | runs | better |
| Withheld runs per work item, the same pair | the same | +11.1 % | runs | same |
| Withheld runs over the body per work item, #1044's 0.22.x figure against 0.27.2's five, the same by either sort | #1044's body, *The record*, and this record's second withhold table | -73.9 % | runs | better |
| Withheld runs per work item, the same pair | the same | -77.8 % | runs | better |

Of the 40 rows, 28 read `better`, 9 `same` and 3 `worse`. The 3 `worse` rows have two causes, and each cause has an issue draft: D4 for the session's start, and D5 for both crafter prose rows.

Three limits bound every `better` row read off runs. First, the after sample is small: 5 work items for rounds and withholds, 5 CI runs, and 32 segments against 30. Second, the first prefix moved under a harness change too, from Claude Code 2.1.292 to 2.1.316, and no segment separates the harness's share (`trail/phases/phase-2.md` *What the next phase needs*). Third, CI follows a suite that shrank from 13,914 collected cases to 6,277 (`trail/phases/phase-1.md` *What the next phases need*). Prose (a) and (b) read only what an agent opens through `Read`, and in 6 of the 8 cells their median is 0 B. Both samples open most prose through `Bash` (`trail/phases/phase-2.md` *Where the prose before does not reproduce*).

### Drafts

The orchestrator takes each act after the seal, in the order `frame/plan.md` *Operational impact* gives. D1 names D4's and D5's numbers, so D4 and D5 are filed first. Then the orchestrator edits #51's body with D1 and posts D2 on #51, and last it posts D3 on #1044 and D6 on #1020. No draft holds a path outside the repository. `<sealed>` stands for the commit the sealer seals, which the orchestrator writes in before it posts.

#### D1

Home: #51's body, a new section above `## Also worth measuring, unmeasured so far`. The *Last revised* line in the body's opening is also replaced with the line given below the section. Act: edit the body.

```markdown
## The process at 0.27.2, against 0.21.x

Read on 2026-11-01 at `94b03636`, the head of `release/v0.27.2` that #947 measured, and recorded at `<sealed>` in `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-1.md` to `phase-3.md`. The before is #947's *Before* table, re-run at its source. Where the re-run did not give the body's figure, the comparison uses the re-run (that record's `phase-3.md` *The reading*).

| Measure | 0.21.x | 0.27.2 | Verdict |
|---|---|---|---|
| Preload per spawn, framer · crafter · proofer · sealer · tracer | 99,089 · 106,350 · 102,229 · 36,113 · 29,554 B | 36,402 · 33,108 · 32,008 · 32,262 · 25,198 B | better |
| A session's start in this repository | `CLAUDE.md` 9,261 B | `CLAUDE.md` 1,143 B and the core hook's 8,515 B | worse, +4.3 % |
| First-turn prompt tokens, median, framer · crafter · proofer · sealer | 73,640 · 83,160 · 75,004 · 57,799 | 45,218 · 44,342 · 43,876 · 43,892 | better; Claude Code 2.1.292 then, 2.1.316 now |
| Prose opened through `Read` per spawn, median, crafter | 846 B | 34,653 B | worse; one `Read` of `skills/implement/SKILL.md` |
| `docs/` · on-demand skills and templates | 708,070 · 437,998 B | 242,145 · 344,602 B | better |
| Suite: cases · Windows seconds · test lines | 13,914 · 7,862 s · 160,138 | 6,277 · 995 s · 94,690 | better |
| CI per pull request: slowest job · ubuntu · Windows · macOS, median | 11.6 · 9.4 · 40.8 · 19.8 min | 2.8 · 1.5 · 8.9 · 3.6 min | better |
| Review rounds per work item, median | 3 (22 work items) | 3 (5 work items) | same |
| Recurring findings · chains of three or more | 30 of 111 · 4 in 17 work items, 0.25.1 to 0.27.1, from #1038's C11 row | 5 of 17 · 1 in 5 work items | same |
| Withheld runs over the hand-written body, per work item | 23 in 30, 0.22.x, from #1044 | 0 in the first 3 after #1103 · 1 in 0.27.2's 5 | better. By #1044's own sort, a reason that names the body, the first 3 give 2, which is the same within 20 % |

The after sample is small, a harness release moved the first prefix as well, and CI follows a suite half the size, so a `better` here is the process and its context together. Each `worse` row has an issue: <D4's number> and <D5's number>.
```

The *Last revised* line: "Last revised 2026-11-01, by #947: the section *The process at 0.27.2, against 0.21.x* holds the reading of the process against 0.21.x."

#### D2

Home: a comment on #51. Act: post it.

```markdown
**The process at 0.27.2, against 0.21.x: the evidence for the body's section of that name (#947).**

The records are `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-1.md`, `phase-2.md` and `phase-3.md` at `<sealed>`. Every figure stands there beside the command that printed it, and every probe stands whole under its record's *Commands*. Nothing was added to the tree to measure with.

- **Samples.** The tree: `f95f0ba8` for preload and `v0.21.1` for the other tree measures before, and `94b03636` after. The runs: session `db35d01d`'s 30 segments under plugin 0.20.0 before, and session `fabe08e7`'s 32 segments of #1221, #1222, #1223, #1229 and #1038 under plugin 0.27.1 after. The rounds: the 22 work items 0.21.0 and 0.21.1 added, against the five. The withholds: #1044's 0.22.x figure, against the first three work items after #1103 and the five.
- **What did not reproduce.** No reading tried gave the body's on-demand 463 KB, its 160,228 test lines, its ubuntu and macOS medians, or its first-turn and prose figures. Its slowest job, 12.3 min, and its Windows 42.4 are one run's figures, run `38477758775`, not medians over the day. The comparison uses the re-run for all of them. `phase-1.md` and `phase-2.md` each list the readings tried.
- **What the readings cannot separate.** The first prefix moved under a harness change, from Claude Code 2.1.292 to 2.1.316. CI follows a suite that went from 13,914 collected cases to 6,277. The prose readings count `Read` results only, and both samples open most prose through `Bash`.
- **#1038** was read at its pull request's head `f8d1b8f6`, which merged unchanged.
- **The round cap.** The extending cap #947's body asked to judge was replaced by the three-round default in `docs/the-review-record.md` *The run*. None of the five work items read had a fourth finding round. #1223's run went on at its third with a *Judgments of the run* row, and its chain of three regressions in one script is a comment on #1020. #1038's C11 row holds the chains of the 17 work items before them.
```

#### D3

Home: a comment on #1044. Act: post it.

```markdown
The count this issue's last *Done when* bullet asked for, taken by #947 at `<sealed>` (`seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md` *The measures*). The first three work items routed through the review chain whose pull request merged after #1103's, listed by `gh pr list --state merged --search "merged:>2026-10-28T04:43:30Z"` in merge order, are counted. Every withheld verdict was read from its pull request's head commits:

| Work item | Withheld runs | Over the body | Over something else |
|---|---|---|---|
| #1052, the issues filed against the old tree (#1113) | 1 | 0 | 1: the closing memo stated a fact this work item's own edit had made false |
| #712, the spawn rows (#1114) | 1 | 0 | 1: the changelog fragment's claim about a column, which the tree contradicted |
| #920, the creation row (#1115) | 1 | 0 | 1: a question's `Status` left `open` after the phase answered it |

None of the three withheld runs was over the hand-written body. Two reasons say the body copied the record. Under this issue's own reading, "whose reason names the pull request body", those two would count as over the body, but the error stood in the record each time. 0.27.2's five work items through the chain show 1 withheld run, and it was over the orchestrator's part of the body: a run said to have every job `success` where one was `skipped`. Before #1103, 23 of 27 withheld runs in 30 work items were over the body.
```

#### D4

Home: a new issue, with the label `measurement` and no milestone (`frame/questions.md` Q1, default (a)). Act: file it, then name its number in D1 and in the pull request body.

Title: `chore: a session in this repository starts with 9,658 B of plugin text where 0.21.1 started with 9,261 B, since the core hook prints the core beside a shorter CLAUDE.md`

```markdown
#947 measured the session's start at `94b03636` against `v0.21.1` (`seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md` at `<sealed>`, *The reading*, the row for a session's start).

At `v0.21.1`, `CLAUDE.md` was 9,261 B. 4,694 B of it was the block `install.sh` distributed into a user's `CLAUDE.md`. At `94b03636`, `CLAUDE.md` is 1,143 B, and the `session-core` hook group runs `hooks/core-start.py`. That hook prints the core, `skills/core/SKILL.md` below its frontmatter, under a header line: 8,515 B, plus the path the header names. Its docstring says it "prints in every session, in any directory". A session in this repository therefore starts with 9,658 B and that path, 4.3 per cent more than before. The agents' preload fell by 11 to 69 per cent over the same span.

What this issue asks: whether every session needs the whole core printed at its start, including a session that does no work through the workflow, which the core says it does not bind. The measurement is the comparison above, and it records no design.
```

#### D5

Home: a new issue, with the label `measurement` and no milestone (`frame/questions.md` Q1, default (a)). Act: file it, then name its number in D1 and in the pull request body.

Title: `chore: a crafter spawn opens 34,653 B of prose through Read where a smith spawn opened 846 B, since skills/implement/SKILL.md left the preload and step 1 sends the crafter to it`

```markdown
#947 measured the prose an agent opens through `Read` per spawn (`seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-2.md` at `<sealed>`, *The measures*, and `phase-3.md` *The reading*, the two crafter prose rows). The median over 9 crafter segments under plugin 0.27.1 is 34,653 B for every `.md` file and 33,989 B for the plugin's prose. The median over 4 smith segments under plugin 0.20.0 is 846 B and 0 B.

The cause is one file. `agents/crafter.md` step 1 opens `skills/implement/SKILL.md`. All 9 crafter segments built a phase, and 7 of them read that file whole through `Read`, two of them twice. The other two, phase 2 of #1221 and phase 2 of #1222, opened line ranges of it through `sed -n`, which these readings do not count. At 0.20.0 the smith received `skills/implement/SKILL.md` in its preload. The crafter's preload fell by 73,242 B, and its first prefix fell from a median of 83,160 tokens to 44,342. Each whole read returns 33,989 B, the file with the line numbers `Read` adds.

What this issue asks: whether a crafter needs the whole of `skills/implement/SKILL.md` at each spawn, or a part of it. Two of the nine crafters already opened only parts of it. That skill also holds the orchestrator's sections and the document layout. The readings count `Read` results only, and both samples open most prose through `Bash`, so the before may read low.
```

#### D6

Home: a comment on #1020, in place of the issue draft *Scope* item 11 names for a chain (decision 3). Act: post it.

```markdown
One more chain for this issue's baseline, after the window #1038's C11 row read (#947, `seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md` at `<sealed>`, *The measures*). In #1223's work item `1793521559-a-finding-is-counted-once`, `round-1#2` (a `routing.md` that is missing or does not parse leaves no row and no line) was followed by `round-2#1` (`regression: round-1#2`: a `routing.md` that cannot be opened prints the absolute path). That was followed by `round-3#1` (`regression: round-2#1`: `why_not`'s fallback is pinned by no case). All three are in `.github/scripts/finding_counts.py`. The orchestrator's row at the third finding round named the counts 2, 2 and 1 and routed an ordinary fix pass, and round 4 found nothing. #1221, #1222, #1229 and #1038 hold no chain of three. Over the five, 5 of 17 findings carry a `regression:` or `reopens:` line.
```

### The decisions, each with its grounds

1. **The before round records are read at `2eb472b1`, the parent of `b914a1c7`.** It is the last commit of `v0.20.0..v0.21.1` that holds all 22 directories. There the 14 items' round files equal `v0.21.0`'s, and the 8 items' equal `v0.21.1`'s, so the reading gives the rounds each release shipped. Judged against: `frame/design.md` *Scope* item 1, "read at `v0.21.1`", and item 8, read for what it asks, which is each before work item's rounds.
2. **A round is one `round-<n>.md` file on the before side**, by `docs/round-record-spec.md` at `v0.21.1`. That document names the round file `rounds/round-N.md` and is the authority for its rows. `round-N-report.md` and `round-N-fixes.md` are the reviewer's report and the fix table of the same round. Judged against: `frame/design.md` *Scope* item 8, "counted by the round record rule … at that tag".
3. **#1223's chain is drafted as a comment on #1020 (D6), not as an issue.** #1020 is open and planned in `release: 0.29.0`, and its subject is the class this chain is an instance of. #1038's C11 row decided `build` for it and drafts its window's chains as a comment there, so a new issue would give one question two homes. The chain also converged under the paragraph: the row at the third finding round stands, and round 4 found nothing. The frame's other source of drafts in item 9, C11's four chains, is carried by #1038's D3 on #1020, and this work drafts nothing for them. Judged against: `skills/core/SKILL.md` *The rule a mechanism is kept against*, "A fact has one source", and `frame/design.md` *Out*, "#1038's C11 decided `build` for #1020's recurrence check (G7), which is where a loop is caught".
4. **The two crafter prose rows take one issue draft, D5.** Reading (b) is reading (a) restricted to the plugin's prose, and one `Read` of one file gives both rows, so one cause has one issue. Judged against: `skills/agent-contract/SKILL.md` rule 12, a defect is owed to its class.
5. **A session's start in this repository is its own row, beside `CLAUDE.md`, and it reads `worse`.** The body measured `CLAUDE.md` as the session's share of the preload. Between the trees, most of that text moved into the core, which a hook now prints into every session, so the `CLAUDE.md` row alone shows the move as a saving. The row adds the hook's bytes at `94b03636` and leaves out the path its header names, which varies by machine. The `session-start` group stands on both sides and is not measured on either (`gaps.md` *Not done*). Judged against: `frame/design.md` *Scope* item 2, and `trail/phases/phase-1.md` *The measures*, "Phase 3 decides how the reading compares the two sides".
6. **Item 9's rows take the band for runs, 20 per cent.** *Scope* item 11 assigns a band to items 2 to 8 and 10 and names none for item 9. Item 9 reads the findings of runs, which are samples in the same sense as items 5 to 8. Judged against: `frame/design.md` *Scope* item 11.
7. **A withheld verdict is sorted by the party its reason names as where the error stands.** #1044's figure sorted by whether the reason "names the pull request body". Since #1103 the body's factual part is a copy of the records, so a record's error also stands in the body. The literal reading is given beside the count in this record and in D3. Judged against: #1044's body, *What changes*: the body's factual part "is generated from the records it restates".
8. **Rounds compare on the median, which is the same, and the mean stands beside it.** *Scope* item 8 names the median. The mean falls from 3.0 to 2.4, which is -20.0 per cent, at the band's edge. Judged against: `frame/design.md` *Scope* items 8 and 11.

### Commands

Every command ran with the working directory at this worktree, or at a clone where a row says so. `$PROJECT` is the harness's project directory for this repository's main checkout, as in `trail/phases/phase-2.md` *Commands*. `$SCRATCH` is the session's scratch directory for this work item, and the probes are saved there under their file names and run with `python3 -I`. `after` is a `git clone --no-local` of this worktree checked out at `94b03636`. `i1038` is the same clone with `pull/1257/head` fetched from GitHub and checked out at `f8d1b8f6`. `pulls` is the same clone with every `refs/pull/*/head` fetched, by `trail/phases/phase-1.md`'s method in #1038's records, *Command C7* (b).

```sh
git fetch origin && git rev-parse origin/release/v0.27.2
git diff --stat 94b03636 origin/release/v0.27.2 -- . ':!seal/threads' ':!seal/follow-up.md'
git diff --stat origin/release/v0.27.2...HEAD -- . ':!seal/threads/1793528484-the-process-measured-on-0-27-2'
date -u +%FT%TZ; gh pr view 1257 --json state,headRefOid,mergedAt,mergeCommit
ls $PROJECT/fabe08e7*/subagents/*.jsonl | wc -l
git clone -q --no-local "$PWD" $SCRATCH/after && git -C $SCRATCH/after checkout -q 94b03636
(cd $SCRATCH/after && python3 .github/scripts/finding_counts.py --released-at 94b03636)
git clone -q --no-local "$PWD" $SCRATCH/i1038 && git -C $SCRATCH/i1038 fetch -q https://github.com/MichaelYcJo/AgenticSeal.git pull/1257/head && git -C $SCRATCH/i1038 checkout -q f8d1b8f6
python3 $SCRATCH/after/.github/scripts/finding_counts.py --released-at f8d1b8f6 --root $SCRATCH/i1038
git log --diff-filter=A --name-only --format= v0.20.0..v0.21.1 -- 'seal/specs/*' | awk -F/ 'NF>3{print $3}' | sort -u > before-items.txt
git log --diff-filter=D --format='%h %ci %s' v0.20.0..v0.21.1 -- 'seal/specs/1791382684-every-reader-and-record-is-inventoried/rounds/*'
git show v0.21.1:docs/the-review-record.md; git show v0.21.1:docs/round-record-spec.md
python3 -I before_rounds.py 2eb472b1 before-items.txt
python3 -I before_rounds.py v0.21.0 <(head -14 before-items.txt); python3 -I before_rounds.py v0.21.1 <(tail -8 before-items.txt)
git diff --stat v0.21.0 2eb472b1 -- <the 14 items' rounds directories>; git diff --stat 2eb472b1 v0.21.1 -- <the 8 items' rounds directories>
python3 -I recurrence.py $SCRATCH/after $SCRATCH/after/seal/threads/1793521561-a-windows-run-names-its-skipped-cases $SCRATCH/after/seal/threads/1793521560-the-checks-wait-starts-before-a-check-reports $SCRATCH/after/seal/threads/1793521559-a-finding-is-counted-once $SCRATCH/after/seal/threads/1793521562-the-proofer-cases-come-from-thread-records $SCRATCH/i1038/seal/threads/1793521558-the-record-decides-each-proposed-verifier
gh pr view 1201 --json mergedAt,mergeCommit; git log -1 --format='%h %cI %s' 96c11614; git merge-base --is-ancestor 96c11614 c6b8e35b
gh issue view 1020 --json title,state,milestone
git clone -q --no-local "$PWD" $SCRATCH/pulls && git -C $SCRATCH/pulls remote set-url origin https://github.com/MichaelYcJo/AgenticSeal.git && git -C $SCRATCH/pulls fetch -q origin '+refs/pull/*/head:refs/pull/*/head'
gh pr list --state merged --search "merged:>2026-10-28T04:43:30Z" --limit 300 --json number,mergedAt,baseRefName,headRefName,headRefOid -q 'sort_by(.mergedAt)[] | [.number,.mergedAt,.baseRefName,.headRefName,.headRefOid[0:8]]|@tsv'
for n in 1104 1105 1108 1112 1113 1114 1115; do gh pr view $n --json files -q '.files[].path' | grep -E 'seal/(specs|threads)/[^/]+/routing.md$'; done
git show a8d83663:CLAUDE.md | python3 -c "import sys; t=sys.stdin.buffer.read(); s=t.index(b'<!-- specseal:start -->'); e=t.index(b'<!-- specseal:end -->')+len(b'<!-- specseal:end -->'); print(len(t), e-s)"
(cd $SCRATCH/pulls && python3 -I $SCRATCH/withholds.py 1113:seal/threads/1793163944-the-issues-were-filed-against-the-old-tree 1114:seal/threads/1793169128-spawn-rows-push-cells-past-the-header 1115:seal/threads/1793169129-the-creation-row-still-says-retry-with-worktree-ok)
(cd $SCRATCH/pulls && python3 -I $SCRATCH/withholds.py 1248:seal/threads/1793521561-a-windows-run-names-its-skipped-cases 1250:seal/threads/1793521560-the-checks-wait-starts-before-a-check-reports 1252:seal/threads/1793521559-a-finding-is-counted-once 1253:seal/threads/1793521562-the-proofer-cases-come-from-thread-records 1257:seal/threads/1793521558-the-record-decides-each-proposed-verifier)
for x in 1248:ad5246ce 1250:161a42aa 1252:a8269d90 1253:94b03636; do git -C $SCRATCH/pulls diff --quiet refs/pull/${x%%:*}/head ${x##*:} -- seal/threads/<its directory>; done
for c in a8d83663 94b03636; do git show "${c}:hooks/hooks.json"; done
python3 -I core_out.py $SCRATCH/after
```

`finding_counts.py` at `94b03636` printed 12 rows and exited 0. At `f8d1b8f6` it printed 9 rows, #1038's among them, and exited 0. `before_rounds.py` printed `items 22; median rounds 3.0; total 66`, and over the two releases apart `items 14; median rounds 3.0; total 50` and `items 8; median rounds 2.0; total 16`. Both `git diff --stat` runs over the before rounds printed nothing. `core_out.py` printed `output 8694 B; path 179 B; without the path 8515 B`. The `CLAUDE.md` one-liner printed `9261 4694`, the file and the block between its `specseal:start` and `specseal:end` markers.

`before_rounds.py`:

```python
"""Rounds per before work item: the round-<n>.md files under each work item's
rounds/ directory at one commit, and its routing.md's Review row, read with
git ls-tree and git show. Usage: before_rounds.py <commit> <list of ids>"""
import re
import statistics
import subprocess
import sys

c, listing = sys.argv[1], sys.argv[2]


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True).stdout


counts = []
for item in open(listing).read().split():
    names = git("ls-tree", "--name-only", f"{c}:seal/specs/{item}/rounds/").split()
    rounds = sorted(int(m.group(1)) for n in names if (m := re.fullmatch(r"round-(\d+)\.md", n)))
    routing = git("show", f"{c}:seal/specs/{item}/routing.md")
    review = re.search(r"^\|\s*Review\s*\|\s*([^|]*?)\s*\|", routing, re.M)
    print(f"{item}\t{len(rounds)}\t{rounds}\t{review.group(1) if review else '-'}")
    counts.append(len(rounds))
print(f"items {len(counts)}; median rounds {statistics.median(counts)}; total {sum(counts)}")
```

`recurrence.py`:

```python
"""For each work item directory: every finding of its round records as
skills/code-review/scripts/chain_check.py#record_findings reads it (loaded
from <code>), the findings with a regression: or reopens: line, the chains
those lines make (a finding linked to the finding it names, followed to its
end), the rounds holding a finding, the Reframed lines under the design's
mark, and the rows of frame/plan.md's Judgments of the run. Read-only.
Usage: recurrence.py <code checkout> <work item directory>..."""
import importlib.util
import os
import re
import sys

code, dirs = sys.argv[1], sys.argv[2:]
spec = importlib.util.spec_from_file_location("cc", os.path.join(code, "skills/code-review/scripts/chain_check.py"))
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)

for d in dirs:
    rdir = os.path.join(d, "trail", "rounds")
    names = sorted((n for n in os.listdir(rdir) if re.fullmatch(r"round-\d+\.md", n)),
                   key=lambda n: int(re.search(r"\d+", n).group()))
    links, with_findings, total = {}, [], 0
    for n in names:
        rn = int(re.search(r"\d+", n).group())
        findings, errors = cc.record_findings(cc.SHARED_READER, open(os.path.join(rdir, n)).read(), n)
        assert not errors, errors
        total += len(findings)
        if findings:
            with_findings.append(rn)
        for f in findings:
            key = f"round-{rn}#{f.number}"
            for kind, ref in (("regression", f.regression), ("reopens", f.reopens)):
                if ref:
                    links[key] = (kind, f"round-{ref[0]}#{ref[1]}" if isinstance(ref, tuple) else str(ref), f.verdict)
    # a chain: follow each link back to a finding that names nothing
    def back(k):
        out = [k]
        while out[-1] in links:
            ref = links[out[-1]][1]
            if ref in out:
                break
            out.append(ref)
        return out
    heads = [k for k in links if k not in {v[1] for v in links.values()}]
    chains = [back(k) for k in heads]
    design = open(os.path.join(d, "frame", "design.md")).read()
    reframed = re.findall(r"^Reframed .*$", design, re.M)
    plan = open(os.path.join(d, "frame", "plan.md")).read()
    m = re.search(r"^## Judgments of the run\s*$(.*?)(?=^## |\Z)", plan, re.M | re.S)
    judgments = [r for r in (m.group(1).splitlines() if m else []) if r.startswith("| 2")]
    print(f"== {os.path.basename(d)}: {len(names)} rounds, {total} findings, rounds holding a finding {with_findings}")
    for k, (kind, ref, verdict) in links.items():
        print(f"   {k} {kind}: {ref} ({verdict})")
    for c in chains:
        print(f"   chain of {len(c)}: {' <- '.join(reversed(c))}")
    print(f"   Reframed lines: {reframed or 'none'}; Judgments of the run rows: {len(judgments)}")
    for j in judgments:
        print(f"     {j[:230]}")
```

It printed, per work item, the rounds, findings and links the convergence table holds: `1793521559-a-finding-is-counted-once: 4 rounds, 5 findings, rounds holding a finding [1, 2, 3]` with `chain of 3: round-1#2 <- round-2#1 <- round-3#1`, and no chain of three for the other four.

`withholds.py`:

```python
"""Withheld verdicts per work item, by #1038's Command C7 (b) method: in a
clone with every refs/pull/*/head fetched, every commit on the pull request's
head that adds a `Verdict: withheld` line to the work item's guarantee.md,
and the distinct verdict lines those commits add. Also prints the Review row
of the work item's routing.md at that head, and the Verdict: lines of the
guarantee.md the head holds. Read-only.
Usage (in the clone): withholds.py <pr>:<work item directory> ..."""
import re
import subprocess
import sys


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True).stdout


for arg in sys.argv[1:]:
    pr, d = arg.split(":", 1)
    ref = f"refs/pull/{pr}/head"
    routing = git("show", f"{ref}:{d}/routing.md")
    review = re.search(r"^\|\s*Review\s*\|\s*([^|]*?)\s*\|", routing, re.M)
    commits = git("log", "--no-merges", "-G", "^Verdict: withheld", "--format=%h", ref, "--", f"{d}/guarantee.md").split()
    lines = []
    for h in commits:
        for ln in git("show", "--format=", h, "--", f"{d}/guarantee.md").splitlines():
            if ln.startswith("+Verdict: withheld") and ln[1:] not in lines:
                lines.append(ln[1:])
    final = [ln for ln in git("show", f"{ref}:{d}/guarantee.md").splitlines() if ln.startswith("Verdict:")]
    print(f"== PR #{pr} {d} head {git('rev-parse', '--short=8', ref).strip()} review: {review.group(1) if review else '-'}")
    print(f"   commits adding a withheld verdict: {len(commits)} {commits}")
    print(f"   distinct withheld verdicts: {len(lines)}")
    for i, ln in enumerate(lines, 1):
        print(f"   W{i}: {ln}")
    print(f"   Verdict: lines in the head's guarantee.md: {len(final)}")
    for ln in final:
        print(f"   F: {ln[:200]}")
```

`-G` matches a commit that removes the pattern as well as one that adds it, so the commit count includes the commit that replaced the withheld verdict. The distinct added lines are the count. It printed one distinct withheld verdict for each of #1113, #1114, #1115 and #1248, none for #1250, #1252, #1253 and #1257, and `review: through the review chain` for all eight.

`core_out.py`:

```python
"""The bytes the SessionStart core hook prints at one checkout, with the path
its header names left out: hooks/lib/core.py#output, run with the checkout as
the session's directory and the plugin root. Read-only.
Usage: core_out.py <checkout>"""
import os
import sys

root = os.path.abspath(sys.argv[1])
sys.path.insert(0, os.path.join(root, "hooks", "lib"))
import core  # noqa: E402

out = core.output(root, root)
path = core.parse(out).path
print(f"output {len(out.encode())} B; path {len(path.encode())} B; without the path {len(out.encode()) - len(path.encode())} B")
print(out.split(chr(10), 1)[0].replace(path, "<path>"))
```

`fourth.py`, run over C11's 17 work items, each directory taken by `git archive refs/pull/<n>/head <directory>` from `pulls` into `$SCRATCH/win/<n>/`, to see what a count beyond C11's row would take:

```python
"""For each exported work item directory: the rounds holding a finding as
chain_check.py#record_findings reads them (loaded from <code>), any record it
refuses a line of, the Reframed lines under the design's mark, and the count
of rows in frame/plan.md's Judgments of the run. Read-only.
Usage: fourth.py <code checkout> <directory>..."""
import importlib.util
import os
import re
import sys

code, dirs = sys.argv[1], sys.argv[2:]
spec = importlib.util.spec_from_file_location("cc", os.path.join(code, "skills/code-review/scripts/chain_check.py"))
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)
for d in dirs:
    rdir = os.path.join(d, "trail", "rounds")
    names = sorted((n for n in os.listdir(rdir) if re.fullmatch(r"round-\d+\.md", n)), key=lambda n: int(re.search(r"\d+", n).group())) if os.path.isdir(rdir) else []
    held, refused = [], []
    for n in names:
        f, e = cc.record_findings(cc.SHARED_READER, open(os.path.join(rdir, n)).read(), n)
        if e:
            refused.append(n)
        if f:
            held.append(int(re.search(r"\d+", n).group()))
    design = open(os.path.join(d, "frame", "design.md")).read() if os.path.exists(os.path.join(d, "frame", "design.md")) else ""
    plan = open(os.path.join(d, "frame", "plan.md")).read() if os.path.exists(os.path.join(d, "frame", "plan.md")) else ""
    m = re.search(r"^## Judgments of the run\s*$(.*?)(?=^## |\Z)", plan, re.M | re.S)
    rows = [r for r in (m.group(1).splitlines() if m else []) if r.startswith("| 2")]
    print(f"{os.path.basename(d)}\trounds {len(names)}\tholding a finding {held}\trefused {refused}\treframed {re.findall(r'^Reframed .*$', design, re.M)}\tjudgment rows {len(rows) if m else 'no section'}")
```

`python3 -I fourth.py $SCRATCH/after $SCRATCH/win/*/seal/threads/*` printed 17 lines. For 8 of the 17 work items, those merged through #1210, the reader at `94b03636` refuses every round record, which predates the finding blocks it reads. So the count beyond C11's chains would need another reader for those records, and it was not taken (`gaps.md` *Not done*).

The phase-boundary set ran as one command with this phase's records staged: `bin/test tests/test_censuses.py $(git grep -l 'seal/threads' -- tests | grep -v '^tests/test_censuses.py$' | grep '\.py$' | grep '/test_') -q -p no:xdist`. That is the census module and the other 44 test modules that name `seal/threads`. It exited 0 with `3715 passed, 1 skipped in 275.55s` (executed). It is no broad gate, and the full suite is the orchestrator's (`gaps.md` *Not verified*).

The percentages of *The reading* were computed from the figures the cited rows hold, as `100 * (after - before) / before`, in one `python3` run over those pairs (executed).
