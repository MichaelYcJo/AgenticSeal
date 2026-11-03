# Guarantee: 1793714292-one-kind-of-finding-recurs-across-review-rounds

| Field | Value |
|---|---|
| Broad gate | `7996f1630 against 5d89ba07a`, the last block of `trail/gate.md`. Only `b98c6ddfa` follows it, and that commit touches `trail/gate.md` alone (executed: `git log --no-merges --name-only 7996f1630..HEAD ^5d89ba07a`; `git merge-base --is-ancestor 7996f1630 HEAD` exited 0) |

The base `release/v0.31.0` resolves to `5d89ba07a4e72a74a035a4fccaa44f74f21c17f5` through `release/v0.31.0@{upstream}` (executed). `seal pr-body <item> --body <file> --check` exited 0, both the installed 0.30.1 copy and the tree's `bin/seal` (executed). No `seal/parity.md` stands, so no comparison with an original is owed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S1: no shipped text names #1020's check | `trail/phases/phase-1.md` *The commands and their results*, S1 | `git grep -n '#1020' -- docs skills agents templates README.md CONTRIBUTING.md hooks bin` at `b98c6ddfa` | holds: nothing printed, exit 1 (executed) |
| S2: *The run* states the zero-finding round once | the same list, S2 | `grep -c 'loop having converged' docs/running/the-run.md` | holds: `1` (executed) |
| S3: no "Table B" citation, and the cited heading stands | the same list, S3 | `git grep -n -i 'table b' -- docs skills agents`; `grep -n '^\*\*Judgment is not licence to skip a party' skills/core/SKILL.md` | holds: the only match in `docs/running/the-run.md:17` is "the table of", every other match is "table below"; the heading stands at line 95 and its row *No fix that no round reads* at line 104 (executed) |
| S4: outside `seal/` the diff holds the two documents and the version move | the same list, S4, and the S4 departure | `git diff --stat 5d89ba07a...HEAD -- ':!seal/'`; `git show 5d89ba07a:.claude-plugin/plugin.json`; `git log --first-parent origin/main..5d89ba07a` | holds: `.claude-plugin/plugin.json`, `docs/releasing/release-checklist.md`, `docs/running/the-run.md`; the base reads `0.30.1` and holds no commit beyond `main`, so this is the release's first work item (executed) |
| S5: the cases that read the two documents pass | the same list, S5 and the phase boundary | `bin/test -q tests/github/test_finding_counts.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_a_cited_commit_outlives_the_squash.py tests/behaviour/test_docs_line_wrap.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_the_set_a_work_item_always_has.py` at `b98c6ddfa` | holds: 166 passed, exit 0 (executed). The phase's 44-module run was not re-run (unverified; the orchestrator's broad run covers it) |
| No `seen red` claim stands to re-run | `trail/phases/phase-1.md` *The phase adds no behaviour* | `grep -n -i 'seen red' trail/phases/phase-1.md` | holds: no match, exit 1; the phase adds no case (executed) |
| Every `## Removes` row, and every removal `changelog.md` names, is gone | `frame/design.md` *Removes*; `changelog.md` entries 2 and 3 | `git grep -n -e 'is then the next step' -e 'files no other' -e 'counts toward nothing' -e 'Table B of the core' -- . ':!seal/threads'` | holds: nothing printed, exit 1 (executed) |
| G8: 111 findings, 30 recurring, 20 in shipped text, four chains of three or more | `frame/design.md:16` | read `git show 569780eff:seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-2.md`, row C11 and *Command C11*'s printed output | holds: the printed output gives the same counts and the chains #1201, #1203, #1230 and #1241, each linked across three or more rounds (read) |
| G9: `96c11614`'s date and ancestry | `frame/design.md:17` | `git log -1 --format=%cI 96c11614`; `git merge-base --is-ancestor 96c11614 HEAD` | holds: `2026-10-31T16:16:17+09:00`, exit 0 (executed) |
| G10: 34 pull requests, 114 findings, 32 recurring, 13 records alone and 19 shipped text, and five chains of three or more | `frame/design.md:18`; the round 1 *Not judged* row that names the sealer | `gh pr list --state merged --search 'merged:>2026-11-01T09:19:59Z'`, the 42 listed less 6 into `main` and 2 settles; each `refs/pull/<n>/head` fetched in a `--no-local` clone under the scratchpad; *Command C11*'s parse over each work item's rounds, joining every `regression:` and `reopens:` link into components | holds: 34 pull requests, 114 findings, 32 recurring, 13 and 19 (executed). The components whose links span three rounds are #1252, #1276, #1284, #1287 and #1320, G10's five, so its list is whole for the window. Three more components hold three findings within two rounds, each round 1 finding regressed twice in round 2: #1253, #1273 and #1305. Each holds a judgment row at round 2, and each run ended at a round 3 that opened nothing (read: each plan's *Judgments of the run* and each round's `### ` count), so the changelog's first entry holds under either reading of "chain" |
| The five chains have a judgment row at or before their third finding | `frame/plan.md:23`; `changelog.md:3` | `git show refs/pull/<n>/head:<item>/frame/plan.md`, *Judgments of the run*, for #1252, #1276, #1284 and #1320 | holds: #1252 and #1276 each hold a row at the third finding round, #1284 a row at round 2 deciding what the reader reads, and #1320 rows at rounds 2 and 3 (read). #1287's row was read by round 1 and not again here |
| The owner's candidate "fires in 11 work items over the two windows" | `frame/plan.md:20`, *Alternatives considered* row 2 | *Command C11*'s printed output for the G8 window; the parse above for the G10 window; `git grep -n -E '^(reopens\|regression): ' refs/pull/1237/head -- 'seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/rounds/'` | **does not hold**: 12 work items carry a `reopens:` line. In G8's window they are #1201, #1203, #1210, #1211, #1230 and #1237, and in G10's #1250, #1278, #1284, #1287, #1303 and #1320. #1237 is in neither the row's six nor its longer chains: `round-2.md:49` reads `reopens: round-1#5` and `round-3.md:148` reads `reopens: round-2#3` at `refs/pull/1237/head` (executed) |
| The milestone keeps the check only if the record still shows the loop | the orchestrator's part of the body, paragraph 1 | `gh issue view 1020 --json milestone` | holds: "the recurrence check (#1020), kept only if the record the 0.27.x releases leave still shows the loop" (executed) |
| The broad run's counts, 6348 passed and 12 skipped, chain exit 0 | the orchestrator's part of the body, its *Broad run* line | none: rule 2 keeps the suite from the sealer, and `trail/gate.md` holds only `run: 7996f1630 against 5d89ba07a` | unverified: the orchestrator answers it. The record it cites holds the run's commit and base, which `seal gate --record` writes only on success (`skills/verify/scripts/broad_gate.py:92`, read), and not the counts |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | build no recurrence check and no exchange, rewrite three sentences of `docs/`, and close #1020 with *Done when* bullet 1 unmet; #97 stays open | the build, the last round, the changelog and the orchestrator's part on what was built. The issue's owner left whether a check is built to this frame: the milestone keeps it "only if the record ... still shows the loop", the comment of 2026-10-29 says the same, and #1038's row C11 cited by the comment of 2026-11-01 leaves "whether the exchange or the check adds anything" to "#1020's frame to weigh" (read). The record the frame weighs holds where re-run (G8 to G10 above), so closing #1020 with bullet 1 unmet stands on the owner's own condition. The frame's absorb-and-leave reading of #97's three levers matches #97's body and the owner's comment of 2026-11-03 (read) | the tree, at `frame/plan.md:20`: the count of work items where the owner's candidate fires is 12, not 11, and #1237 is left out. This row is the cost comparison the owner's comment of 2026-10-30 asked for ("Compare it ... on cost and on what each catches"), and the miscount does not change its verdict |
| the build | the three sentences are rewritten in place, no case pinned them, and the version moves to 0.31.0 | the design's *Scope* items 1 to 3 as folded at `36d347848`, and the diff (read: `git diff 5d89ba07a...HEAD`); S1 to S5 (executed above) | none |
| the last round | round 2 at `88aabb168` opens nothing and confirms `round-1#1` | the diff: the checklist's issue now names the file the lesson belongs in, and the row at `skills/implement/orchestration.md:486` gives "an issue that names the home" for "a lesson or a decision whose home no work item in progress changes" (read). Only `trail/gate.md` follows the round, so no finding of it reads `fixed` unread | none |
| the changelog | no check; *The run* states the zero-finding round once and cites the core's table; the checklist files an issue naming the lesson's file | the diff and the design. Its first entry's claim that every chain of three or more had its row at or before its third finding holds on the two windows as re-run above | none |
| the orchestrator's part of the pull request body | builds no check or exchange, `Closes #1020`, no `Closes #97`, a `fix:` prefix, and the broad run at `7996f1630` | the design, the build, the rounds and the milestone. The planned `fix:` title matches `frame/plan.md` *Operational impact*: the diff adds no step and no refusal. #1020's retitle to `fix:` is an act still to come, since the issue reads `feat:` (unverified; the orchestrator answers it) | none the tree contradicts. Its *Broad run* line cites `trail/gate.md` for counts that file does not hold. Earlier bodies write the same line "as `seal gate` printed it" (#1320, #1321, #1322; read) |

```seal
target: b98c6ddfa against 5d89ba07a
Verdict: withheld reason: the framer's claim at frame/plan.md:20 (Alternatives considered, row 2) that the owner's candidate "fires in 11 work items over the two windows" does not hold; 12 work items carry a reopens: line, and #1237 (1793490088-each-kind-of-restatement-is-measured, round-2.md:49 reopens: round-1#5 and round-3.md:148 reopens: round-2#3 at refs/pull/1237/head) stands in neither the row's six nor its longer chains
```

## Re-audit at 77266f6b4

| Field | Value |
|---|---|
| Broad gate | `7996f1630 against 5d89ba07a`, still the last block of `trail/gate.md`. The commits after it are `b98c6ddfa` (`trail/gate.md`), `8e1ab3424` (`guarantee.md`) and `77266f6b4` (`frame/plan.md`), all under the work item's directory (executed: `git log --no-merges --name-only 7996f1630..HEAD ^5d89ba07a`; `git merge-base --is-ancestor 7996f1630 HEAD` exited 0) |

The base resolves to `5d89ba07a4e72a74a035a4fccaa44f74f21c17f5` as before. `bin/seal pr-body <item> --body <file> --check` exited 0 on the rewritten body file (executed). After the earlier block's target, `git diff b98c6ddfa..HEAD` changes only `frame/plan.md` *Alternatives considered* row 2 and adds *Judgments of the run* row 3 (executed). Those two rows are the only claims this run re-runs. The others stand as the tables above give them.

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The owner's candidate "fires in 12 work items over the two windows" | `frame/plan.md:20` | the census of the earlier run, *Command C11*'s printed output for G8's window and the parse over G10's 34 pull requests, already executed at `b98c6ddfa`. The row's coordinates in those records did not change | holds: 12, the work items listed in the earlier row of this file (executed) |
| "In 7 of them the reopened finding's chain ended at two findings", #1237 among them, and "#1237's two, `round-2#2` and `round-3#5`, stood in its records alone" | `frame/plan.md:20` | `gh api repos/MichaelYcJo/AgenticSeal/contents/seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/rounds/round-<n>.md?ref=08ea31268` for rounds 1 to 4, at #1237's head, parsed for each finding's `regression:`, `reopens:` and `location:` lines | holds (executed). `round-2#2` reopens `round-1#5` and `round-3#5` reopens `round-2#3`. No finding of rounds 3 or 4 names `round-2#2` or `round-3#5`: round 4's two name `round-3#2` and `round-3#1`. Every `location:` path of `round-1#5`, `round-2#2`, `round-2#3` and `round-3#5` stands under that work item's directory. `round-2#1` also regresses `round-1#5`, so three findings sit under `round-1#5` within two rounds. "Chain" is read here as findings linked across rounds, as G10's five are read, and the reopening's chain is two findings long |
| The repair's judgment row: its grounds and the act it records | `frame/plan.md:49`, *Judgments of the run* row 3 | the same reads | holds: the grounds the row gives match what the reads above printed (executed) |
| No other copy of the count stands in the work item | the orchestrator's message | `git grep -n -e '11 work items' -e 'fires in' -- seal/threads/1793714292-one-kind-of-finding-recurs-across-review-rounds ':!*/guarantee.md'` | holds: only `frame/plan.md:20`, which reads 12 (executed) |
| The *Broad run* line now quotes what `seal gate` printed | the orchestrator's part of the body | read the body file above `## From the records` | the line quotes the three printed lines, attributes them to the command, and says `trail/gate.md` records the run at `7996f1630`, which that file holds (read). The counts themselves stay unverified, and the orchestrator answers them, since rule 2 keeps the suite from the sealer |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | as the earlier table gives it, with row 2's count now 12 | the tree at `frame/plan.md:20` and the records of #1237 and the two windows; the row's `rejected` stands on the same grounds | none |
| the build | unchanged since `b98c6ddfa` | as the earlier table gives it | none |
| the last round | round 2 at `88aabb168`, unchanged | as the earlier table gives it. `77266f6b4` touched the work item's records alone, and no round's `fixed` finding is in question, so no round owes reading it | none |
| the changelog | unchanged; it states no count of the exchange's firings | the design and the diff | none |
| the orchestrator's part of the pull request body | as before, with the *Broad run* line quoting `seal gate`'s output | the design, the build, the rounds, the milestone and `trail/gate.md`. *For the reviewer* names *Judgments of the run* rows 1 and 2 for the two folds, and they still record them. Row 3 records the repair this message describes. #1020's retitle to `fix:` is still an act to come (unverified; the orchestrator answers it) | none |

```seal
target: 77266f6b4 against 5d89ba07a
Verdict: sealed
```
