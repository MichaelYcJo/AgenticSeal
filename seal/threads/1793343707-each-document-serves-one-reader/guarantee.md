# Guarantee: 1793343707-each-document-serves-one-reader

| Field | Value |
|---|---|
| Target SHA | a6c19da0 against fba13ab2; earlier run: 16000f92 withheld |
| Broad gate | d7d275f9 against fba13ab2 |

The base `release/v0.25.1` resolved through `origin/release/v0.25.1` to
`fba13ab2` (executed; `release/v0.25.1@{upstream}` and `release/v0.25.1`
answer nothing here). `trail/gate.md` names `d7d275f9`, an ancestor of HEAD
(`git merge-base --is-ancestor`, exit 0, executed). `git log --no-merges
--name-only d7d275f9..HEAD ^fba13ab2` names three commits, `16000f92`
(`trail/gate.md`), `0e673d48` (`guarantee.md`) and `a6c19da0`
(`frame/design.md`), each touching only a path under
`seal/threads/1793343707-each-document-serves-one-reader/` (executed). The
gate's log in the scratchpad ends `gate exit=0` (read). `bin/seal pr-body
seal/threads/1793343707-each-document-serves-one-reader --body
<scratchpad>/1793343707-each-document-serves-one-reader/pr-body.md --check`
exited 0 at HEAD (executed). No `seal/parity.md` is declared, so no
`original:` line is owed (executed, `ls`).

This audit follows the one at `16000f92`, whose verdict was `withheld`.
`git diff --quiet 16000f92 HEAD` outside `frame/design.md` and
`guarantee.md` exits 0 (executed), so no shipped file, test, phase record,
round record or the changelog changed since. The earlier run's re-runs of
the phase 2 to 5 `seen red` claims, of phase 4's and phase 7's `executed`
claims, and of the round records' counts rest on coordinates no commit since
touched, and are not re-run here (read: the earlier `guarantee.md` at
`0e673d48`, every one of them `holds`). What is re-run below is what the
repairs touched: the `## Removes` row `a6c19da0` rewrote, and the
orchestrator's part of the pull request body, rewritten outside git.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| "where a reader who stops after that part's first screen still has the numbers" is gone from *Pull request bodies* | `frame/design.md:321`, the `## Removes` row `a6c19da0` rewrote | `git grep -n "first screen" -- ':!seal/threads'` | holds: the one hit is `skills/commit-pr-convention/SKILL.md:196`, "a reader who stops after the body's first screen still has the numbers", the replacement the row's third column names; "that part's first screen" stands nowhere (executed) |
| "the comparison table opens the orchestrator's part" stays, since the table still opens that part under the new order | `frame/design.md:321`, third column | `git grep -n "comparison table opens" -- ':!seal/threads'`; `sed -n 1,38p` of the body file | holds: the sentence stands at `skills/commit-pr-convention/SKILL.md:193-194` and is pinned at `tests/text/test_the_chain_section_has_one_shape.py:81`; the body's orchestrator's part opens with the `Closes` line and then *The run beside the last one*, the table (executed). The row's history note cites the first audit's `:192-193`: the sentence opens at 192 and the phrase ends on 194, which changes nothing it claims (read) |
| No other part of the frame, the changelog or a phase record names the comparison-table sentence as removed | `frame/design.md`, `frame/plan.md`, `changelog.md`, `trail/phases/*.md`, `gaps.md` | `grep -n -i 'comparison table\|first screen'` over those files | holds: the one hit is `frame/design.md:321` itself (executed) |
| 19 commits carry no `Seal-Routing:` trailer: `59b63cfb`, `5183dd26`, and every commit from `fcacd9e5` through `b3b36143`; phase 1's three build commits carry it | the pull request body, *Other things to know*, second item | `git log --reverse --format='%h %ad %(trailers:key=Seal-Routing,valueonly,separator=)\|%s' HEAD ^fba13ab2` | holds: the commits without the trailer are positions 1, 3 and 9 to 25 of 51, `59b63cfb`, `5183dd26` and the seventeen from `fcacd9e5` to `b3b36143`, 19 in all; `74d8a992`, `78848617` and `ceb0a711` carry `Seal-Routing: 1793343707-each-document-serves-one-reader` (executed) |
| Phase 1 had been spawned at `5183dd26` and closed at `ceb0a711` when the framer folded the four proposals at `6be0c1f1`; the step phase 4 adds places the exchange before the first build spawn | the pull request body, *Other things to know*, first item | the same `git log`, its times; `git log -S 'one exchange' fba13ab2..HEAD -- skills agents` | holds: `5183dd26` 16:35:01, `ceb0a711` 16:44:49, `6be0c1f1` 16:49:03; the step's text (`skills/implement/orchestration.md:82-89`, `agents/framer.md:227`) entered at `0dde0fab`, a phase 4 commit by `trail/phases/phase-4.md:60` and `:150` (executed); `frame/plan.md` A14b reads "Chosen after phase 1" (read, at the earlier audit, unchanged since) |
| 51 commits at `a6c19da0`: 32 chore, 9 fix, 6 docs, 3 test, 1 feat | the pull request body, *The run beside the last one*, commits row | `git rev-list --count HEAD ^fba13ab2`; `git log --format=%s HEAD ^fba13ab2 \| sed -E 's/^([a-z]+).*/\1/' \| sort \| uniq -c` | holds: 51; 32, 9, 6, 3, 1 (executed) |
| 2,897 of 4,123 added lines are under `seal/threads/`; outside it 1,226 added and 992 removed; outside `tests/` 601 and 651; in `tests/` 625 and 341 | the pull request body, the records' share row and *Two decisions for the owner* Q2 | `git diff --shortstat fba13ab2...HEAD`; `git diff --numstat fba13ab2...HEAD` summed by path with `awk` | holds: 4,123 insertions, 992 deletions; 2,897 under `seal/threads/`; 1,226 and 992; 601 and 651; 625 and 341 (executed) |
| The token row and the segments row | the pull request body, *The run beside the last one* | none: they come from transcripts | unverified; the orchestrator answers them |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Thirteen scope items as at the earlier audit; its `## Removes` row on `skills/commit-pr-convention/SKILL.md` *Pull request bodies* now names only "where a reader who stops after that part's first screen still has the numbers" as removed, and says "the comparison table opens the orchestrator's part" stays | the issue body's eight decisions and its *Done when*, except the last bullet, which `frame/questions.md` Q2 holds for the owner (read, unchanged since the earlier audit); the tree at the rewritten row (executed above); `frame/design.md:130`, "*Pull request bodies* states the new order" (read) | none |
| the build | Seven phases and the fix passes deliver the design's scope; each phase record names its departures, its `seen red` runs and its mutants | the design, now including the *Pull request bodies* row, since `git diff fba13ab2 HEAD -- skills/commit-pr-convention/SKILL.md` shows the comparison-table sentence kept and "that part's first screen" rewritten to "the body's first screen" (executed), in the section `trail/phases/phase-5.md:4-13` names among the prose homes that now state the new order (read); the earlier audit's re-runs, on coordinates unchanged since | none |
| the last round | Round 5, at `e88426a1`, opens no finding and confirms round 4's three closes; its *Not judged* carries the open owner questions and the broad run | the tree, as at the earlier audit; `trail/rounds/` is unchanged since `16000f92` (executed, `git diff --quiet`) | none |
| the changelog | One `### Changed` entry and thirteen `### Process changes` rows; the version moves to 0.25.1 | the design, the build and the tree, as at the earlier audit; `changelog.md` is unchanged since and names no removal of the comparison-table sentence (executed, `grep`) | none |
| the orchestrator's part of the pull request body | The run's figures at `a6c19da0`; Q2's line counts with the default of accepting the shortfall, and Q1, the behaviour suite not run, for the owner; the frame exchange came after phase 1 and the step phase 4 adds places it before the first build spawn; 19 commits without the trailer, named; three things moved to #1147, #1020 and #1190; the version moves to 0.25.1 | the tree on every figure and sentence re-run above; the issue's comment of 2026-10-30T07:50:20Z on the frame reading and of 10:19:30Z on the prevention home (read, `gh issue view 1148`); the design's `frame/questions.md` Q1 and Q2 | none |

Verdict: sealed
