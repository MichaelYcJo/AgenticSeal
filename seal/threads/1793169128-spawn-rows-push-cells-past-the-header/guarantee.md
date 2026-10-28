# Guarantee: 1793169128-spawn-rows-push-cells-past-the-header

| Field | Value |
|---|---|
| Target SHA | 95f61e54 against 977b6613; earlier run: 6854aa6e withheld |
| Broad gate | 9e3ca54d against 977b6613 |

## Claims re-run

This run audits the commits after the earlier run's `6854aa6e`: `78108d2d`, `9e3ca54d` and `95f61e54`. `git diff --stat 6854aa6e HEAD -- skills tests` prints nothing and exits 0, so no code or test coordinate moved, and the claims the earlier run executed on code stand as it recorded them. They are carried in the rows marked "carried".

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad gate's newest run covers HEAD: only the gate record follows the run's commit | `trail/gate.md:5` | `git log --no-merges --name-only 9e3ca54d..HEAD ^977b6613` and `git merge-base --is-ancestor 9e3ca54d HEAD` | holds: one commit follows, `95f61e54`, and it touches only `seal/threads/1793169128-spawn-rows-push-cells-past-the-header/trail/gate.md`. `9e3ca54d` is an ancestor of HEAD, exit 0 (executed). The run's counts were not re-run, by the sealer's own rule (read). |
| The commits since the earlier run change records only | the coordinator's account of `78108d2d`, `9e3ca54d`, `95f61e54` | `git log --no-merges --name-only 6854aa6e..HEAD` and `git diff --stat 6854aa6e HEAD -- skills tests` | holds: `78108d2d` adds `guarantee.md`, `9e3ca54d` changes `changelog.md` and `frame/plan.md`, `95f61e54` changes `trail/gate.md`. The code and test diff is empty (executed) |
| The pull request body's part above `## Not from the records` is the records' own text | the body file regenerated with `seal pr-body` | `bin/seal pr-body seal/threads/1793169128-spawn-rows-push-cells-past-the-header --body <the body file> --check` | holds: exit 0, "is the records' text" (executed). The body's line 10 carries the new `changelog.md:4` sentence, and its `Broad gate` row reads `9e3ca54d against 977b6613; earlier run: 47a22ea0 against 977b6613` (read) |
| Each description after a label that fit the column now starts one column further right than before, and one after a label longer than the column now starts at that same column | `changelog.md:4`, and the same statement in `frame/plan.md:85-87` | the earlier run's base output and HEAD module run (both executed at `6854aa6e`, code unchanged since), and the description line's format at base and at HEAD | holds. At base the line is `f"  {cycle_label(row):<30}{row['description'][:70]}"`, so a description after a label of 30 or fewer characters starts at column 32, and one after a longer label starts right after it, at column 39 for the issue's own label (executed: `  cycle 1  vercel:performance-optimizerBuild phase 1`). At HEAD the line is `f"  {cycle_label(row):<{LABEL_WIDTH}} {row['description'][:70]}"` with the label cut to 30, so every description starts at column 33 (read, `skills/verify/scripts/session_cost.py:2435`), and the case asserts `  cycle 1  vercel:performance-op Build phase 1` (`tests/skills/test_session_cost.py:3313`, executed passing at `6854aa6e`) |
| No other place states the old sentence | the class of the earlier run's finding | `git grep -n 'one column further right\|one column to the right' HEAD -- seal/threads/1793169128-spawn-rows-push-cells-past-the-header CHANGELOG.md docs skills` | holds: the hits are `changelog.md:4` and `frame/plan.md:86`, both in the new wording, and the earlier `guarantee.md`, which this file replaces (executed) |
| carried: seen red, the new case fails against the base `cycle_label` and `report_spawns` | `trail/phases/phase-1.md:36-39` | earlier run, in a `--no-local` clone at `6854aa6e` with `session_cost.py` restored from `977b6613`: `bin/test tests/skills/test_session_cost.py -q -p no:xdist -k long_agent_name` | holds: exit 1 with `['0.0m'] == ['1.0m']`, the row 7 columns past its header, the description run into the label (executed at `6854aa6e`) |
| carried: the no-call row's pad was unwatched before `77d0d095` and is watched after it | `trail/phases/phase-1.md:40-46` | earlier run, the no-call pad widened to `LABEL_WIDTH + 1` in the clone | holds: red with HEAD's test file, `252 passed` with `53bd30a4`'s (executed at `6854aa6e`) |
| carried: the module passes | `trail/rounds/round-1.md:86-90` | earlier run, `bin/test tests/skills/test_session_cost.py -q` | holds: `252 passed`, exit 0 (executed at `6854aa6e`) |
| carried: Removes rows 1 to 5 stand removed | `frame/design.md:106-110` | earlier run, `git grep -n ':<30' -- skills/verify/scripts/session_cost.py` and `git grep -n 'label column of the per-segment table'` | holds: no `:<30` stands, and the old comment survives only as quotes in this work item's records (executed at `6854aa6e`) |
| carried: the rule-12 enumeration is complete | `frame/design.md:45-58` | earlier run, the design's grep at `977b6613` | holds: every hit is a site of the design's table (executed at `6854aa6e`) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | `cycle_label` cuts to `LABEL_WIDTH`. `report_spawns` pads to it at four sites. The description line gains one space. One new case pins the cut, the cells, the description line and `--json`. `frame/plan.md:84-87` now says a description moves one column right after a label that fit and to that same column after a longer one | the issue's checkbox, the diff, the build, the changelog, the tree | none |
| the build | `trail/phases/phase-1.md`: the frame held, the case went red at base with `0.0m` read for `1.0m`, the no-call pad survived a mutant until `77d0d095` | the spec, the tree | none |
| the last round | `trail/rounds/round-2.md`: round 1's finding on the overflow threshold is fixed at `2752c754`, nothing opened | the changelog's first bullet, `gaps.md:5-9`, the tree | none |
| the changelog | first bullet: a label longer than 30 characters is cut with no mark, so each cell ends under its header, and for a single-digit cycle a name longer than 21 characters overflowed. Second bullet: one space separates label and description, which starts one column further right after a label that fit and at that same column after a longer one | the diff, the base output, the case at HEAD, the spec | none |
| the orchestrator's part of the pull request body | `Closes #712` | the issue's one checkbox: the label is cut and a case with a long `subagent_type` pins every cell under its header | none |

Verdict: sealed
