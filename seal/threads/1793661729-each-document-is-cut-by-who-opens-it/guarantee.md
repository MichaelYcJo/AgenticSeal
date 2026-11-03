# Guarantee: 1793661729-each-document-is-cut-by-who-opens-it

| Field | Value |
|---|---|
| Broad gate | 0ebcd944d against 95cbd99a4 |

The base `release/v0.30.0` resolves through `origin/release/v0.30.0` to
95cbd99a4 (executed). `trail/gate.md`'s last block names the run at
0ebcd944d, an ancestor of HEAD, and `git log --no-merges --name-only
0ebcd944d..HEAD ^95cbd99a4` lists only b3872b934, which touches
`trail/gate.md` alone (executed). `seal pr-body <item> --body
pr-1312.md --check` exited 0 (executed). `seal/parity.md` is not tracked
(executed), so no `original:` line is owed.

## Claims re-run

Each `seen red` was re-run in a `git clone --no-local` at b3872b934 under
the scratchpad, with the one changed file restored from 95cbd99a4 and put
back after the case; the clone is removed. Each case passed at HEAD first
(executed).

| Claim | Source | Command | Result |
|---|---|---|---|
| S5 seen red: the group-path case fails at the old reader | `trail/phases/phase-2.md:72-77` | `git checkout 95cbd99a4 -- skills/settle/scripts/rule_changes.py`; `pytest tests/skills/test_rule_changes.py::Test_parse::test_reads_a_file_in_one_group_directory_of_the_root` | holds: 1 failed, "`docs/forms/a.md` is not a top-level docs/ file" |
| S6 seen red: the fold reads no group at the old reader | `trail/phases/phase-2.md:93-97` | `git checkout 95cbd99a4 -- skills/settle/scripts/fold_check.py`; `pytest tests/skills/test_fold_check.py -k test_a_group_the_index_names_is_read_and_no_other_directory_is` | holds: 1 failed, "held 2 documents under docs/ … 0 past it" where 4 and 1 were asserted |
| Phase 3 seen red: a check line beside `SKILL.md` is unread at the old glob | `trail/phases/phase-3.md:166-168` | `git checkout 95cbd99a4 -- .github/scripts/rules.py`; `pytest tests/github/test_rules.py -k test_a_check_line_in_a_skills_supporting_file_is_read` | holds: 1 failed, "all 0 check lines in 0 rule files hold", `assert 0 == 1` |
| Phase 6 seen red: the sealer pin fails against the old step 1 | `trail/phases/phase-6.md:160-163` | `git checkout 95cbd99a4 -- agents/sealer.md`; `pytest tests/behaviour/test_the_sealer_guarantees.py -k test_step_1_reads_the_record_and_runs_nothing` | holds: 1 failed, the full `chain_check.py#follows` path absent |
| Phase 5 seen red: the release report's refuses case catches a walk of every directory | `trail/phases/phase-5.md:12-19` | `seal mutate skills/settle/scripts/fold_check.py --replace 'for group in named' 'for group in os.listdir(os.path.join(root, *policy.split("/")))' --tests "pytest tests/github/test_release_report.py::Test_documents"` | holds: the refuses case failed, the accepts case passed; file restored |
| Phase 1 seen red: the bars case names one owner path | `trail/phases/phase-1.md:48-60` | `seal mutate docs/running/the-run.md --replace` the `skills/verify/orchestration.md` *Measure the segment* citation with `skills/verify/SKILL.md` `--tests "pytest …::test_the_bars_section_cites_the_run_level_tables_owner"` | holds: 1 failed; file restored |
| S2: no agent's preload grows | `trail/phases/phase-6.md:104-112`, `changelog.md:3` | HEAD's `release_report.py#preloads` over `git archive 2d38c75af` and the clone at HEAD | holds: crafter 33203 to 33081, framer 36365 to 36362, proofer 32414 to 32293, sealer 32262 to 31879, tracer 25212 to 25085 |
| S9: no policy document past the ceiling | `trail/phases/phase-7.md:24-30` | `bin/seal fold` at HEAD | holds: 23 documents, 0 past it, the index names every document, exit 0 |
| `seal rules --check` holds | `trail/rounds/round-1.md:232` | `bin/seal rules --check` at HEAD | holds: all 295 check lines in 71 rule files, exit 0 |
| Every citation stands where it points | issue item 5; `frame/design.md` S8 | `pytest tests/behaviour/test_a_cited_section_stands_in_its_file.py` | holds: exit 0 |
| S8: no old policy path outside `seal/` but nine historical lines | `trail/phases/phase-5.md:87-117` | `git grep -n -F "docs/<name>.md" -- ':!seal/' ':!CHANGELOG.md'` for the sixteen names | holds: 0 for fifteen, 9 for `the-review-record` |
| S11: "does not edit it" stands nowhere | `trail/phases/phase-1.md:25-31` | `git grep -n "does not edit it" -- ':!seal/'` | holds: nothing, exit 1 |
| Phase 1 shortened two passages by 129 and 778 bytes | `frame/plan.md:99` | `git diff -U0 2d38c75af 29d8ca6a4^ -- docs/the-review-record.md`, bytes per hunk | holds: -129 and -778 |
| Nine ranged reads cover a shortened passage, one of them the proofer's over the question-gate paragraph | `frame/plan.md:99`; `trail/rounds/round-2.md:46-52` | a read-only probe over the transcripts with phase 7's filter, listing each ranged read of `docs/the-review-record.md` over base lines 288-291 or 531-544, and whether it covers the whole passage; deleted | nine holds (4 and 5). The proofer's read is base lines 541-643: it covers 4 of the paragraph's 14 lines, 276 of its 956 bytes, not the paragraph |
| The replay at the work's end: crafter -6.5%, framer -2.0%, sealer -10.0%, proofer 0 | `changelog.md:9`; `trail/phases/phase-7.md:351-411` | phase 7's script, copied from the record, over 2d38c75af against b1880c1db and against b3872b934; deleted | holds at b1880c1db (crafter -363,892, framer -91,437). At HEAD: crafter -355,513 (-6.3%), framer -87,476 (-1.9%), sealer -9.8% with this sealer's own spawn counted, proofer +0 |

Each `## Removes` row of `frame/design.md` was checked against the tree
(executed): the core holds none of the three words of the routing
sentence; rule 20 is one retirement line; `agents/sealer.md` names neither
the check's section nor its document and cites `chain_check.py#follows`;
`seal_stamp.py`, `hooks/sealer-stamp.py`, `chain_check.py` and
`skills/code-review/orchestration.md` cite `docs/checks/the-stamp.md` or
`docs/forms/the-guarantee.md`; `docs/running/the-run.md` names the
question gate's docstring and holds no "single-select";
`docs/the-review-record.md` is absent; `docs/` holds `README.md` alone at
its top beside the five groups and `experiments/`; `rule_changes.py#parse`
reads one group directory; "by topic" and "own headings" stand only at
`skills/settle/named-directories.md:37`, a different rule;
`skills/implement/SKILL.md` holds none of the batch, the ladder or the
drain, and `skills/implement/orchestration.md` holds all three under
`Orchestrator:` headings. `ls seal/threads` lists this work item alone
(executed), so no other design's operation is owed a re-point.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | D1-D9: the core states the cut rule, three skills are cut, the policy root is cut and grouped into five groups under the subject boundary, no preload grows | the issue's five items and its boundary paragraph, read; it departs openly from item 2's "each states its reader at its top" for the fifteen moved documents, giving each group's reader once over its index table, which item 4 leaves to the frame | none |
| the build | phases 1-7 build D1-D9 with the departures each record names | the design, and the tree on every claim re-run above | `frame/plan.md:99`, the round-2 fix pass's row (below) |
| the last round | round 2 confirms round 1's three findings and closes its one finding `fixed 540cb8515`, which touched `frame/plan.md` alone (executed) | round 1, the tree | the row it closed with, which no round read: `frame/plan.md:99` says "The proofer's +0 of 375,093 bytes rests on 7 such reads, one over the question-gate paragraph, so its total lies between 778 bytes fewer and 265 more". The proofer's read is base lines 541-643, which takes 276 of the paragraph's 956 bytes, so that read loses at most 276 bytes and the bound is 276 fewer to 1,043 more (7 × 149). "Under 0.3% either way" still holds (1,043 of 375,093). `trail/rounds/round-2.md:71`, the fix pass's answer, states the same figures |
| the changelog | the core's rule, the subject boundary, the grouped root, the readers of group directories, the cut skills, the copies, the reading | the tree on the preloads, the groups, the refusal text, `seal fold` and the largest document (about 11,884 tokens) | `changelog.md:7` "A framer that follows its citation of the grammar opens 7,383 bytes where it opened 43,620": at HEAD `skills/settle/rule-changes.md` is 7,564 bytes, and at the base 95cbd99a4 `skills/settle/SKILL.md` is 43,170 (43,620 is phase 2's own tree at cb98bb899). `changelog.md:7` "A crafter's whole read of `skills/implement/SKILL.md` is 5,388 bytes smaller": 30,663 at the base and 25,406 at HEAD, 5,257 (170372c72 grew it by 131). `changelog.md:9` "replayed against the tree before this work and at its end … fell 6.5% for the crafter, 2.0% for the framer and 10.0% for the sealer": those figures are the replay against b1880c1db; against HEAD they are 6.3%, 1.9% and about 9.9% |
| the orchestrator's part of the pull request body | the owner's decisions, eleven `## Removes` rows, preloads, the reading, two rounds, six record-only commits | the issue, the design's eleven rows, #1313 in `release: 0.31.0` (executed), and each of 384e4f1f3, 316c608b4, 350048ba0, 2d531a293, 0ebcd944d, b3872b934 touching the work item's records alone (executed) | its *The reading* bullet quotes `changelog.md:9`'s percentages, so it carries that line's figures |

```seal
target: b3872b934 against 95cbd99a4
Verdict: withheld reason: three figures do not hold at HEAD; the changelog (`changelog.md:7`) says a framer opens 7,383 bytes where it opened 43,620 (HEAD `skills/settle/rule-changes.md` 7,564, base `skills/settle/SKILL.md` 43,170) and that the crafter's whole read of `skills/implement/SKILL.md` is 5,388 bytes smaller (30,663 to 25,406, 5,257); the changelog (`changelog.md:9`) gives the replay "at its end" as -6.5%, -2.0%, -10.0%, which is b1880c1db, not HEAD (-6.3%, -1.9%, about -9.9%), and the body's *The reading* bullet quotes it; the round-2 fix pass's row (`frame/plan.md:99`) bounds the proofer at 778 fewer to 265 more on a read "over the question-gate paragraph", but that read is base lines 541-643, 276 of the paragraph's 956 bytes, so the bound is 276 fewer to 1,043 more, still under 0.3%
```
