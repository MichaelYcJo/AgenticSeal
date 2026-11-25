# Phase 1: 1795595957-the-next-round-is-a-fixs-first-reader

## What this phase found

**The frame holds against the tree.** Between `650f9aec4`, the commit the frame read, and `d6dab4d1c`, where this phase started, only `seal/follow-up.md` and this work item's three frame files changed (`git diff --stat 650f9aec4 d6dab4d1c`, executed). Each coordinate *Scope* items 1 to 5 and 8 name stood at `d6dab4d1c`: the table and the sentence opening "The last two rows" in `skills/code-review/SKILL.md` *Comparison axes*; the paragraph of `agents/sealer.md` step 4 opening "A finding of the last record that reads `fixed <commit>`"; the sentence of `agents/proofer.md` at lines 129 to 130; the paragraph opening **On the hand-back that leaves no finding open for a fold**, the *When* row and the sentence opening "The verifying round a regression's fix pass is owed" in `skills/code-review/orchestration.md`; `skills/code-review/scripts/chain_check.py#VERIFYING_ROUND`; and the three cases that open "S4 of #1148" in `tests/skills/test_chain_check.py`. `git grep -n -F 'the sealer, the first reader of each sentence' -- agents skills docs` printed `agents/proofer.md:130` there (executed).

**This phase built *Scope* items 1 to 5 and 8, not 1 to 8 as `frame/plan.md`'s phase 1 row says.** The spawn gave *Scope* item 7, the `seal/follow-up.md` row, to the orchestrator, which committed it at `d6dab4d1c`. *Scope* item 6 is the design's own `## Rule changes`, which the framer wrote at `97acaf4c5`, so nothing of it was built here.

**The orchestration case stands in `tests/behaviour/test_the_sealer_guarantees.py`.** *Scope* item 8 names no file for it. The design's `add` operation names that file on its `check:` line for the rule both reads state, and the file already holds a case on the orchestration that hands the sealer its run, `test_the_orchestration_quotes_the_gates_outputs_line`. The module docstring now names the orchestration among what the file reads. Judged against `agents/crafter.md` *A new test starts from its group* and `frame/design.md` `## Rule changes`.

**The orchestrator's read names the record, not only a finding of it.** *Scope* item 4 says a round reads the pass where the `--worktree` output "names a finding of that record" with the words. `chain_check.py#records` also prints those words on the last record's path, at line 0, for a commit after its `target:` that touches a path outside the work item's records, and such a commit owes a round too. So the paragraph reads "names that record with the words". Judged against `skills/code-review/scripts/chain_check.py#records`.

**The paragraph cites the constant and also types its value.** The orchestrator matches words in the output, so the paragraph quotes them, and the case reads them from `chain.VERIFYING_ROUND`, so a change to the check's line turns it red. Judged against *Scope* item 8.

**Departure: "contract rules 12 and 19" is written as two citations.** The phase boundary run's `test_every_near_miss_in_the_tree_is_reported` warned that the new row's "contract rules 12 and 19" is a spelling the citation check does not read. The row now reads "contract rule 12 and contract rule 19", and `agents/sealer.md` step 4 reads "rule 12 and rule 19", the form `agents/` cites the contract in (`c5b79aa64`). The same warning names `skills/code-review/SKILL.md:261`, the paragraph opening **A paste-ready fix reaches every statement of the fact it repairs, or names where it stops**, which this phase does not change. Judged against `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, which has one contract rule cited per citation.

**Departure: the sentence under the axes table names the record rows instead of counting them.** *Scope* item 1 asks for one sentence saying the record rows are walked over the records the proofer's rule names. Its first wording opened "The four record rows", a count a later row would make false with no word of the list in it, so `22b6a60e6` names each row. Judged against contract rule 19.

**The regression case carries the one marker *Scope* item 8 names.** Its siblings under "S4 of #1148" carry `last-record-at-head` as well; the new case is about the round a regression owes, and `run-ends-with-verifying-round` is that rule's marker (`docs/running/the-run.md` *The run*).

**The regression case covers what its group does not.** `seal mutate skills/code-review/scripts/chain_check.py`, replacing `#records`' `located_in_records(item, f) and records_only(root, item, f.verdict[1])` with the same followed by `and not f.regression`, survived `test_passes_a_last_records_fixed_finding_that_touched_only_its_records` (executed; a coverage probe) and turned the new case red (executed). Before this phase no case would have failed if the arm refused a regression's records-only fix.

**Seen red, each new case with only the clause it reads removed** (executed, `seal mutate` at `5b4710bfc`, whose tree `a36119ca1` carries after the trailer was added; each run passed its baseline first, and the tests ran with `bin/test -q -p no:xdist <module> -k <case>`):

| Case | Break | Verdict |
|---|---|---|
| `test_step_4_reads_a_records_only_fix_over_its_diff` | in `agents/sealer.md`, the `git -C <root> diff` command replaced with "the records," | red |
| the same | the `git -C <root> grep` command replaced with "the search," | red |
| the same | "like any other, and a `withheld`" replaced with "like any other. A" | red |
| `test_the_orchestration_reads_whether_a_round_follows_off_the_check` | in `skills/code-review/orchestration.md`, `python3 skills/code-review/scripts/chain_check.py` replaced with "the check" | red |
| the same | the quoted "a verifying round is owed" removed | red |
| the same | the citation of `chain_check.py#VERIFYING_ROUND` removed | red |
| `test_passes_a_last_records_regression_fixed_in_its_records_alone` | in `chain_check.py#records`, `read_at_head` passing nothing (`False`) | red |
| the same | `read_at_head` refusing a finding with a `regression:` line | red |

Each case's one assertion lists the pinned phrase it misses, or the arm's problems, so each red is the break its row names (read).

**A policy sentence states the order Scope item 4 rewords, and no operation of `## Rule changes` reaches it.** `docs/forms/the-round-record.md`, the paragraph opening **Each finding's close block has one writer, and the blocks written at one step reach the branch in a single commit.**, says the orchestrator commits the round record "before it spawns the verifying round". Where the core's row gives the pass to the sealer, no round is spawned. This work writes the policy root through `## Rule changes`, which the framer writes, so the sentence stands and the hand-back names it for the orchestrator's fold.

**The searches and the read of `frame/plan.md` phase 1's *Verified by* cell** (executed at `22b6a60e6`, with this record, `gaps.md` and `changelog.md` in the working tree): `git grep -n -F 'the sealer, the first reader of each sentence' -- agents skills docs` exited 1; `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.0 --root <this clone> --worktree` exited 0 and printed no line on `frame/design.md` `## Rule changes`, only the lines a work item with no round record, gate record or guarantee yet owes.

**The phase boundary run** (executed at the same tree): `bin/test -q tests/text tests/behaviour tests/skills/test_chain_check.py`, which collects 81 files, the plan row's five modules and the tree-wide files among them, and the whole of `tests/skills/test_chain_check.py` in place of its `run-ends-with-verifying-round` cases alone, since that file changed and reads `agents/proofer.md`. It printed `1144 passed, 9 skipped` and exited 0. The same run before `gaps.md` was written failed `test_every_spec_directory_that_reached_the_ladder_has_an_overview` on this work item alone. No other test file reads a path this phase changed: `tests/evals/test_noninferiority.py`, `tests/github/test_release_report.py` and `tests/skills/test_rules.py` write those paths' names into fixtures they build (read).
