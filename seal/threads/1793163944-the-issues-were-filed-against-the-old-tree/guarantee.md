# Guarantee: 1793163944-the-issues-were-filed-against-the-old-tree

| Field | Value |
|---|---|
| Target SHA | 03a57921 against 822d75bb; earlier run: 02aa625f withheld |
| Broad gate | f76272d1 against 822d75bb |

## Claims re-run

The base `origin/release/v0.24.0` resolves through `release/v0.24.0@{upstream}` to 822d75bb. This is a re-run. The earlier run at 02aa625f re-ran 23 claims, and its rows stand at `b8770385:seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/guarantee.md`. Since then three commits came: b8770385 (that `guarantee.md`), f76272d1 (`gaps.md`, two cells) and 03a57921 (`trail/gate.md`). So the claims re-run here are the ones whose coordinates `gaps.md` carries, plus the gate and the body. No phase record claims a `seen red`, so no at-base clone was made. All rows are executed unless the Result says read.

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run is at f76272d1, and only paths under this work item's thread follow it | `trail/gate.md:5` | `git merge-base --is-ancestor f76272d1 HEAD`; `git log --no-merges --name-only f76272d1..HEAD ^822d75bb` | holds: ancestor, exit 0; only 03a57921 follows, touching only `trail/gate.md` |
| Only the closing memo, the gate record and the earlier guarantee changed since the earlier run | the coordinator's message | `git log --no-merges --name-only 02aa625f..HEAD`; `git diff --name-only 822d75bb...HEAD` outside the thread | holds: `guarantee.md`, `gaps.md` and `trail/gate.md` only; nothing outside the thread. No earlier row's coordinate but `gaps.md`'s moved |
| The part of the regenerated pull request body above `## Not from the records` is the records' text | the coordinator's message; `agents/sealer.md` step 2 | `bin/seal pr-body seal/threads/1793163944-the-issues-were-filed-against-the-old-tree --body <scratchpad>/1052-pr-body.md --check` | holds: exit 0, `matches:` |
| That check can fail on this body | the same | the same `--check` over a copy whose copied *Not verified* row reads "#1109 itself closed when #1112 reached `main`" | holds: exit 1, `refused: sealer-tampered2.md:93` |
| The order divergence's chosen cell: after round 1, #1109's body moved its census question to #1110, #1111's body names #956 as its predecessor, and #1109 is closed by #1112, not here | `gaps.md:16`, at f76272d1 | #1109, #1110 and #1111 bodies as read in the earlier run (rows "Round 1 finding 1's fix" and the edit history at `b8770385:.../guarantee.md`); `gh issue view 1109 --json state,updatedAt`; `gh pr view 1112 --json state,mergeCommit` | holds: #1109's third *Done when* bullet sends the census question to #1110's frame, and #1110 holds it. #1111's `## Order` opens "After #956 and #1040". #1109 is open, last updated 06:06:36Z, so nothing changed since that run. #1112 is MERGED at 822d75bb with `Closes #1109`. The cell no longer says this work item left #1109 unedited |
| Milestone 65's "#1109 was fixed directly" holds, and #1109 closes when the release reaches `main` | `gaps.md:26`, at f76272d1 | `git grep -n -i detracer 822d75bb` (earlier run, base unchanged); `gh pr view 1112`; `.github/scripts/release_completeness_check.py:13-14` and `gh pr view 1105 --json closingIssuesReferences` (earlier run) | holds: no `detracer` at the base. #1112 merged into `release/v0.24.0`. A release pull request gathers its carried pull requests' closing keywords, as #1105 closed #857, #1044 and #1060 (read) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | `frame/design.md`, `frame/plan.md` and `frame/questions.md`, unchanged since the earlier run, cover these deliverables: one verdict per open issue of both milestones (22 folded, 3 stand, #1044 done); three new issues; four findings folded; both milestones' order; nine titles. `## Rule changes` and `## Removes` are both nothing | the issue body's three *Done when* items and *Out of scope*; every GitHub reading of the earlier run | none. The title rule sits under *Answered by the tree*, and the owner has not answered whether the eight retitles stand. That is a default disclosed, not two facts, and the tree bears the frame's reading |
| the build | phases 1 to 4, unchanged, and `gaps.md` at f76272d1: the divergences, now with the order-change cell brought up to round 1 and the #1109 row closed by #1112 | the spec; the earlier run's re-run figures and GitHub states; the last round's account of round 1; #1109's and #1111's bodies; #1112's merge | none |
| the last round | `trail/rounds/round-3.md` at 4e635bd4: no finding; round 2's close holds; the retitles and the broad gate not judged | the build, now including `gaps.md`; round 1's two fixes, re-read on GitHub in the earlier run | none |
| the changelog | absent: nothing the plugin ships changes | the diff, which touches no file outside this directory; `docs/the-record-layout.md:57-58` (read) | none |
| the orchestrator's part of the pull request body | the work changes no file outside its records; on GitHub, three new issues, 22 bodies, nine titles and both descriptions; no changelog; the eight retitles rest on the review's default and can be reverted; `Closes #1052` | the earlier run's counts on GitHub; the diff; the rounds' *Not judged* rows on the retitles; the issue number | none. The #1112 bullet left the orchestrator's part, and `gaps.md:26` now carries that fact in the copied part |

Left unverified, and no ground of this verdict: the owner's three decisions after the frame (Q1 answered (b), #1109 fixed directly, #1111 after #956) reach the records only as the orchestrator relays them, and the owner answers whether they were relayed as made. Whether the eight retitles stand is the owner's, through the orchestrator. The broad run was read from `trail/gate.md` and not run here, by rule 2.

Verdict: sealed
