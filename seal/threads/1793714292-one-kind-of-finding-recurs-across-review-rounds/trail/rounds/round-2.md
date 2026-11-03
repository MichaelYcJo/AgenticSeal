# Review round 2: 1793714292-one-kind-of-finding-recurs-across-review-rounds

```seal
target: 88aabb168, fixes 295df2fef..88aabb168
```

This is the verifying round after round 1's fix pass. It reads the diff `295df2fef..88aabb168` in a `--no-local` clone at `88aabb168`. That diff holds three commits. `d4697987e` is the fix pass: it changes `docs/releasing/release-checklist.md` *2b. Settle what earlier releases left behind*, the work item's `changelog.md` and the first row of `gaps.md` *Not verified*. `36d347848` is the orchestrator's fold of `frame/design.md` *Scope* item 1, with its row in `frame/plan.md` *Judgments of the run*. `88aabb168` is round 1's close block.

Two coordinates are carried from round 1 and were not searched for again. The first is the cited table row at `skills/implement/orchestration.md:486`. The second is the checklist paragraph's `check:` target, `tests/github/test_finding_counts.py`, which reads the count's script and no sentence of the step. This round opened both at `88aabb168`, and both still stand there. Every verdict below is this round's own. Round 1's two `## Not judged` rows that name the sealer stand as round 1 wrote them. They lie outside this fix diff, and this round does not reopen them.

The axes fixed before starting were these. The first is whether the checklist's new sentences describe the issue the cited row describes. The second is whether every other statement of that issue's contents moved with the fix (contract rule 12 and rule 19). The third is whether the fold changes *Scope* item 1 to match the build, and whether its judgment row stands on a source. The fourth is whether the reflowed last sentence of the paragraph kept its words. The table's code axes, such as inputs, authorization and concurrency, have no subject in a diff of prose.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the checklist's issue step now describes the issue the cited row describes. The row at `skills/implement/orchestration.md:486` has the orchestrator write "a lesson or a decision whose home no work item in progress changes" into "an issue that names the home" (read). `docs/releasing/release-checklist.md:99-102` now has the session file one issue that names "each such stale copy, the record it stood in, and the file the lesson belongs in". It says an issue naming that file is where the cited section "writes a lesson whose home no work item in progress changes" (read). So the issue names the home, a file, and the row's condition carries "whose home", which were the two departures round 1 named. The new sentence says the cited section writes the lesson, where the row's column says the orchestrator writes it. That reads loosely, but it sends a settling session to the same issue, so it is no finding. The paragraph's words before and after the change were compared in `git diff 295df2fef..88aabb168 -- docs/releasing/release-checklist.md`. The last sentence, from "The step is" to "`flow-baseline` log.", keeps every word and only moves its line breaks, as the close block says. The `check:` line is unchanged (executed). The narrow run under `## Probes` passes at `88aabb168`. Among its modules are the line-wrap module, the cited-section module and the module for the paragraph's `check:` target (executed).

```seal
confirms: none
```
What matched: the fix pass's departure from round 1's paste-ready text. The crafter claimed that round 1's sentence "That issue is the home ... gives a lesson whose home no work item in progress changes" still made the issue the home. Round 1's own text, at `trail/rounds/round-1.md:30-32`, reads that way. The row at `skills/implement/orchestration.md:486` makes the home a file, in the left cell, and the issue the place the orchestrator writes the lesson, in the right cell (read). So the paste-ready sentence used "home" in two senses, and the applied wording gives the word one sense. The departure is right.

```seal
confirms: none
```
What matched: every other statement of the issue's contents moved with the fix. The method takes the artefact apart. The issue's contents are a fact this branch introduced, so outside the records of earlier rounds they can stand only in a file the branch changed. `git diff --stat 5d89ba07a..88aabb168` lists those files (executed). Each one that could state the fact was read at `88aabb168`. They are `changelog.md:5`, `gaps.md:7`, `frame/design.md:27`, `:49` and `:68`, `frame/plan.md:48`, `trail/phases/phase-1.md:37-41`, the checklist itself, `docs/running/the-run.md` and `.claude-plugin/plugin.json`. The checklist, `changelog.md:5`, `gaps.md:7` and `frame/design.md:27` now name the file the lesson belongs in (read). `frame/design.md:49`, *S1*, and `:68`, the *Removes* row, state no contents of the issue, and both still hold (read). `trail/phases/phase-1.md:37-41` keeps the old wording as the record of what phase 1 built at `df433eee2`, as round 1 allowed. A whole-tree `git grep -n -e 'stale cop' -e 'files one issue' -e 'lesson belongs' -e 'no work item in' -e 'record it stood'` found no other statement (executed). The crafter called its own grep a sample, which is honest: a search on wording is a sample under rule 12. The list above is whole because it was made by taking the diff apart.

```seal
confirms: none
```
What matched: the orchestrator's fold `36d347848`. It changes only `frame/design.md:27` and adds one row at `frame/plan.md:48` (executed, `git show --stat 36d347848`). *Scope* item 1's second and third sentences now match the checklist's sentences word for word, except that the frame says "each stale copy that kept the count up" (read). The row's grounds hold. The close block at `trail/rounds/round-1.md:40` leaves `frame/design.md:27` for the orchestrator to fold. The row's source, `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*, has the orchestrator fold a frame statement the hand-back names, "in place, in a commit of its own, before it spawns the verifying round" (read, `skills/code-review/orchestration.md:78-81`). The fold's commit holds nothing else.

```seal
confirms: none
```
What matched: round 1's close block. The crafter claimed that the block reads under `hooks/lib/fields.py` with no refusal. The run of `skills/code-review/scripts/chain_check.py` under `## Probes` read this work item's records with the block in place and refused nothing in it (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite and the lint across the repository: `unverified`, since rule 2 keeps the broad gate from every agent. The crafter's 11 modules with 658 passed at `d4697987e` were not run again. This round ran its own narrow set, listed under `## Probes` | `seal/config.md` `Broad gate` row | the orchestrator, at its broad run |

This round leaves nothing open. What comes due is the orchestrator's broad run, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/github/test_finding_counts.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/text/test_a_cited_commit_outlives_the_squash.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/text/test_settle_reads_before_it_removes.py tests/text/test_the_rules_claude_md_names_have_one_home.py tests/text/test_the_release_tail_does_not_end_at_the_tag.py`, in the clone at `88aabb168` | 238 passed, 9 skipped, exit 0 |
| `git grep -n -e 'stale cop' -e 'files one issue' -e 'lesson belongs' -e 'no work item in' -e 'record it stood'`, in the clone at `88aabb168` | the checklist, `changelog.md:5`, `frame/design.md:27`, `frame/plan.md:48`, `gaps.md:7`, `trail/phases/phase-1.md:37-40`, `trail/rounds/round-1.md`, `skills/implement/orchestration.md:486`, and `skills/update/SKILL.md:67`, which is about a different stale copy |
| `python3 skills/code-review/scripts/chain_check.py --baseline 5d89ba07a --root . --worktree`, in the branch worktree with this record in place | exit 0. It printed no refusal of either round record. Its two lines name the `trail/gate.md` the orchestrator's broad run writes and the `guarantee.md` the sealer writes, and neither is owed yet |
