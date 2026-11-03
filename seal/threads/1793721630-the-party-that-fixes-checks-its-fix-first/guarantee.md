# Guarantee: 1793721630-the-party-that-fixes-checks-its-fix-first

| Field | Value |
|---|---|
| Broad gate | `12e288e3d against 6ca420572` (read: `trail/gate.md`, its one `seal` block). `git log --no-merges --name-only 12e288e3d..HEAD ^6ca420572` lists `77878f68c` alone, touching `trail/gate.md` alone, so only the work item's records follow the run (executed) |

The audit is of `77878f68c`, HEAD of `fix/1318-the-party-that-fixes-checks-its-fix-first`, against `release/v0.31.0`, which `release/v0.31.0@{upstream}` resolves to `6ca420572` (executed). `seal pr-body seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first --body <the prompt's pr-body.md> --check` exited 0, with the installed plugin's `seal` and with the tree's `bin/seal` (executed). `seal/parity.md` is not in git, so no comparison with an original is owed. No earlier `guarantee.md` stood.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The new crafter rule's case was seen red: the case fails without the rule | `trail/phases/phase-1.md:64-72` | In a `git clone --no-local` at `77878f68c` under the scratchpad's `at-base/`, `git checkout 6ca420572 -- agents/crafter.md skills/implement/orchestration.md skills/code-review/orchestration.md skills/agent-contract/SKILL.md`, then `bin/test` on the four cases below, `-q` | holds: `test_the_crafter_reads_its_range_and_the_records_whole_before_it_hands_back` failed, "`agents/crafter.md` lost its rule on reading the range whole" (executed) |
| The fix-pass case's new citation clause was seen red | `trail/phases/phase-1.md:68-72` | the same run | holds: `test_the_crafters_fix_pass_appends_a_close_block_and_sweeps_what_its_range_reworded` failed, "the fix-pass rule lost \"Once the fixes are committed, make the reading ...\"" (executed) |
| The fold paragraph's clauses were seen red | `trail/phases/phase-1.md:73-75` | the same run | holds: `test_a_decision_after_the_frame_is_folded_into_it` failed on the whole-file fold clause (executed) |
| The review file's changed clauses were seen red | `trail/phases/phase-1.md:76-77`; round 2's close at `trail/rounds/round-2.md:47` | the same run | holds: `test_the_fix_pass_reads_the_implementers_context_before_it_resumes` failed on the fold clause "the orchestrator folds each file that holds such a statement, read whole" (executed). 4 failed of 4 |
| `crafter_rule` had to join a wrapped lead: the new case went red with "lost its rule" before the helper changed | `trail/phases/phase-1.md:34-39` | in the clone at HEAD, `bin/seal mutate tests/text/test_a_moved_rule_leaves_its_definition.py --replace 'if " ".join(paragraph.split()).startswith(f"**{lead}**"):' 'if paragraph.startswith(f"**{lead}**"):' --tests "bin/test ... -k reads_its_range"` | holds: red, the case failed with "lost its rule on reading the range whole" (executed) |
| 9 of 9 mutants red over `agents/crafter.md`, two not sampled by a round: the `## Not done` sentence and the `check:` line | `trail/phases/phase-1.md:68-72` | in the clone at HEAD, `bin/seal mutate agents/crafter.md` with two `--replace` pairs, one deleting "What you did not finish goes to `gaps.md` `## Not done` with why.", one deleting the rule's `check:` line, `--tests "bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -q -k reads_its_range"` | holds: baseline passed, 2 mutants, 2 red; `git status --short` printed nothing (executed) |
| S7's seven modules pass, 355 cases | `trail/phases/phase-1.md:89-92`; `trail/rounds/round-3.md:56` | `bin/test` over the seven modules `frame/design.md` S7 names, `-q`, in the clone at HEAD | holds: exit 0, 355 passed (executed) |
| S1: rule 12 holds "proofer's share" and no "open part of a sample" | `trail/phases/phase-1.md:86-88` | `git grep -n -e 'open part of a sample' -e "proofer's share" -- skills/agent-contract/SKILL.md`, and the four edited texts with their newlines joined, searched for each removed phrase | holds: one line, `skills/agent-contract/SKILL.md:171`; no removed phrase across a wrap (executed) |
| S3 and S5: the sweep's copy and the one-statement fold are gone | `trail/phases/phase-1.md:88-89` | `git grep -n 'find every other place stating' -- agents skills docs`; `git grep -n -e 'by its words and by the' -e 'folds that statement' -e 'folds it as' -e 'reads that list against' -- skills/code-review/orchestration.md` | holds: both exit 1, nothing printed (executed) |
| S6: outside `seal/`, the four texts and the two test modules alone | `trail/phases/phase-1.md:89-90` | `git diff --name-only 6ca420572...HEAD -- ':!seal/'` | holds: the six paths and nothing else (executed) |
| `## Removes` rows 1 to 5 and the changelog's removals ("the fix pass's own copy of the search is gone", rule 12's exit, "keeps no copy of the crafter's search") stand nowhere in the tree | `frame/design.md:87-95`; `changelog.md:3` | the S1, S3 and S5 commands above, `git grep -n 'find every other place stating each rule your range reworded' -- tests`, `git grep -n -e 'statements beside each' -e 'each one left returns as a round' -- agents skills docs` | holds: each exit 1 or, for S1, the kept phrase alone (executed) |
| G9's split, sampled (round 1 left it to the sealer, `trail/rounds/round-1.md:164`): #1273 2 (0, 1, 1), #1287 4 (0, 4, 0), #1320 3 (3, 0, 0) | `frame/design.md:36` | each work item's round records read at the first tag holding it (`v0.27.3`, `v0.28.0`, `v0.30.1`) for finding blocks with a `regression:` line and their `location:` paths; `refs/pull/1273/head` and `refs/pull/1287/head` fetched from `origin`'s URL into the clone; `git diff --name-only` over each `fixes <a>..<b>` range | holds: #1273 round 2 finding 1 names `skills/code-review/scripts/chain_check.py`, outside `c2535dcd..afde315b`, and finding 2 names `hooks/lib/console.py`, inside it; #1287's four regressions name only paths inside their fix ranges; #1320's three name only paths under its work item's directory (executed). A sample of 3 of 18 work items, 9 of 37 regressions; the other 15 rows were not re-derived |
| The broad run passed with 6349 passed and 12 skipped | the orchestrator's part of the pull request body, its last paragraph | none: the sealer runs nothing broad | `unverified` by the sealer; `trail/gate.md` holds the run and not the counts, and the orchestrator's `gate.log` in the scratchpad prints those counts (read). The orchestrator answers it |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `frame/design.md` *Scope* items 1 to 8: rule 12 rewritten for the closed set, one crafter rule in place of the sweep with *Job* giving a fix pass `changelog.md`, step 10 and the fix-pass paragraph citing it, the fold home reading each named file whole, the review paragraph citing both, the two test modules; no check; `## Removes` rows 1 to 5 | the build (the diff matches each item, read); the issue's items 1 to 3, with *Done when* bullet 1 met by citation and the departure argued at `frame/plan.md` *Alternatives considered* row 7; G9's sampled rows | `frame/plan.md:10`, the *Technical context* line `12e288e3d` rewrote after round 3, which no round read: "No case pins the sentences this work rewrites ... `test_the_fix_pass_reads_the_implementers_context_before_it_resumes` pins its close-block sentence, which *Scope* item 6 keeps". At `6ca420572` that case pinned "answered, after its fix commits and those corrections" (`git show 6ca420572:tests/text/test_the_rules_have_one_owner.py`, line 210, executed), the clause *Scope* item 6 (`frame/design.md:47`) rewrites to "the corrections its read made", as `trail/phases/phase-1.md:43-47` and `:76-77` record. So a case did pin a sentence the work rewrites |
| the build | the diff `6ca420572...HEAD` and `trail/phases/phase-1.md`: the six paths of S6, the new case of its own beside the fix-pass case, the wrapped-lead helper, four case clauses seen red | the design, the claims re-run above, the changelog | none |
| the last round | `trail/rounds/round-3.md`: confirms round 2's finding 1, opens nothing, reads `frame/plan.md:10` as a base reading outside the fix diff | the tree at its target `9bc5519e5`; the claims re-run above | none at its target; the line it flagged was then rewritten at `12e288e3d`, see the design's row |
| the changelog | `changelog.md`: the *Changed* entry and two *Process changes* rows state the five texts' new rules and G9's 35 of 37 with its coordinate | the diff and the design (read); G9's sampled rows | none |
| the orchestrator's part of the pull request body | the work, `Closes #1318`, the departure from *Done when* bullet 1, the prefix, the three rounds, the folds, the broad run | the issue, the design, the rounds and `trail/gate.md` on every point but two | its *For the reviewer* paragraph cites "`frame/plan.md` *Judgments of the run* row 4" for round 2's routing to an ordinary fix pass, and "rows 1, 2 and 5" for the folds after the build and after each fix pass. The table at `frame/plan.md:50-55` has four data rows: the routing is row 3, and the folds are rows 1, 2 and 4; no row 5 exists (executed: the rows counted with `awk`, 4) |

```seal
target: 77878f68c against 6ca420572
Verdict: withheld reason: the orchestrator's part of the pull request body, its "For the reviewer" paragraph, cites `frame/plan.md` "Judgments of the run" row 4 for round 2's routing and rows 1, 2 and 5 for the folds, where the table at `frame/plan.md:50-55` holds four rows, the routing at row 3 and the folds at rows 1, 2 and 4; and `frame/plan.md:10`, rewritten at 12e288e3d and read by no round, says no case pinned a sentence this work rewrites, where `6ca420572:tests/text/test_the_rules_have_one_owner.py:210` pinned "after its fix commits and those corrections", the clause `frame/design.md:47` (Scope item 6) rewrites
```

## Re-audit at 1fcd7ba4e

| Field | Value |
|---|---|
| Broad gate | `12e288e3d against 6ca420572` (read: `trail/gate.md`, unchanged). `git log --no-merges --name-only 12e288e3d..HEAD ^6ca420572` lists `77878f68c` (`trail/gate.md`), `6739ec9c0` (`guarantee.md`) and `1fcd7ba4e` (`frame/plan.md`), each touching only the work item's directory (executed) |

Since the first block's `target:` `77878f68c`, the commits touch `guarantee.md` and `frame/plan.md` alone, so this run re-ran only the claims at those coordinates and read the parties again. Nothing outside `seal/` changed: `git diff --stat 6ca420572...HEAD -- ':!seal/'` still lists the six paths, 163 insertions and 46 deletions (executed). The claims of the first run above stand on a tree no commit since has touched. `seal pr-body seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first --body <the prompt's pr-body.md> --check` exited 0 with the installed `seal` and the tree's `bin/seal` (executed). `6739ec9c0` holds the first run's file as written (`git status --short` was empty before this append, executed).

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The base's fix-pass case pinned "after its fix commits and those corrections", the clause *Scope* item 6 rewrites | `frame/plan.md:10` | `git show 6ca420572:tests/text/test_the_rules_have_one_owner.py \| sed -n 210p`; `frame/design.md:47` read | holds: line 210 is `"answered, after its fix commits and those corrections",`, and *Scope* item 6 rewrites "those corrections" to "the corrections its read made" (executed; read) |
| No case pinned the sweep and fold sentences this work rewrites, at the base | `frame/plan.md:10` | `git show 6ca420572:tests/text/test_the_rules_have_one_owner.py \| sed -n 190,220p`; `git grep -n -e 'every other place stating it' -e 'reads that list against' -e 'which the fix pass does not edit' -e 'so the round and the next crafter read one rule' 6ca420572 -- tests evals` | holds: the case's clauses are the context, threshold, close-block and round-record sentences, and the grep printed nothing (executed) |
| *Judgments of the run* row 3 is round 2's routing, rows 1, 2 and 4 the folds, row 5 the *Technical context* repair | the orchestrator's part of the pull request body, *For the reviewer* | `awk` over `frame/plan.md` *Judgments of the run*, numbering its data rows | holds: five rows; row 3 routes round 2's finding 1 to an ordinary fix pass, rows 1, 2 and 4 fold the frame after the build and after each fix pass, row 5 records `1fcd7ba4e`'s repair (executed) |
| Row 5's document judged against exists | `frame/plan.md:56` | `grep -n 'Orchestrator: the pull request opens once the sealer seals' skills/code-review/orchestration.md` | holds: `:222` (executed) |
| The broad run passed with 6349 passed and 12 skipped | the orchestrator's part of the pull request body, its last paragraph | none: the sealer runs nothing broad | `unverified` by the sealer, as in the first run; the orchestrator answers it |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | as in the first run; `frame/plan.md:10` now says no case pinned the sweep and fold sentences, and the base's fix-pass case pinned the close-block sentence with the clause *Scope* item 6 rewrites; row 5 records the repair | the base's test file at line 210, *Scope* item 6, `trail/phases/phase-1.md:43-47` | none |
| the build | unchanged since the first run | the design, the claims re-run | none |
| the last round | `trail/rounds/round-3.md`, unchanged | the tree at its target `9bc5519e5` | none |
| the changelog | `changelog.md`, unchanged | the diff and the design | none |
| the orchestrator's part of the pull request body | as in the first run, with *For the reviewer* citing row 3 for the routing, rows 1, 2 and 4 for the folds, and row 5 for the *Technical context* correction after round 3 and after the first verdict | `frame/plan.md` *Judgments of the run*, rounds 1 to 3, `trail/gate.md`, the issue | none. Row 5 records the second correction; the first, `12e288e3d`, has no row of its own, and the body's sentence does not say it has one |

```seal
target: 1fcd7ba4e against 6ca420572
Verdict: sealed
```
