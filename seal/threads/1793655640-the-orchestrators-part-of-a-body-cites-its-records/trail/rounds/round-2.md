# Review round 2: 1793655640-the-orchestrators-part-of-a-body-cites-its-records

```seal
target: 36fce349, fixes 39fa1528..36fce349
```

This is a verifying round. Its target is the diff of the last fixes, four commits: `bce68fe8` (finding 3), `e88b42fd` (findings 1 and 2), `260143ef` (the close blocks) and `36fce349` (the orchestrator's fold into `frame/design.md` and `frame/plan.md`). The work happened in a `git clone --no-local` of the branch worktree at `36fce349`, under `<scratchpad>/1290-round-2/clone`. No `seal/parity.md` is declared, so the round block has no `original:` line.

Carried from round 1 and not re-established: the paths of the two 0.29.0 withheld guarantees on their branches, the two 0.28.0 guarantees G6 cites, and the nine test modules that open the edited files by name. Re-derived this round: every verdict below, the two withheld blocks (read again with `git show`), the rule change's parse, the merge with the base and the narrow run.

The two edited sentences were read against `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*: one reading, one home for a rule, and who acts, when, in which file and when it is done. The fix pass claimed that the new sentence at `skills/writing-style/outside-the-review.md:64` "mirrors the pointer at `:27-30`, so the section points to the home the same way twice and restates none of it". The pointer holds, and the paragraph around it does not (finding 1).

## Findings

### 1. The verification table's paragraph keeps the table to what no record holds, and the pointer between its sentences lets a record's verification into it

```seal
severity: should
location: `skills/writing-style/outside-the-review.md:64`
evidence: read `skills/writing-style/outside-the-review.md:60-64`, `skills/code-review/orchestration.md:363-376`, `seal/threads/1793655640-the-orchestrators-part-of-a-body-cites-its-records/frame/design.md:66-81`
regression: round-1#1
```

The unit is the paragraph at `skills/writing-style/outside-the-review.md:64`, which `e88b42fd` changed. Plan phase 1's Delivers cell gives *Scope* items 1 to 6, and design *Scope* item 2 with the `## Removes` row folded at `36fce349` say the paragraph points to the home and restates none of the rule; `e88b42fd` replaced the paragraph's fourth sentence with a pointer, as round 1's paste-ready text asked, and left its first and last sentences, so the defect came from round 1's fix, which was scoped to one sentence of a paragraph whose two other sentences stand on the same old rule.

Why it matters: the paragraph now says three things about the table. It opens "리뷰 체인을 거친 본문에서는 기록에 없는 검증만 이 표에 적는다". It then says that when a phase record's verification is needed, `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* decides how it is written. It closes "표에 남는 것은 광역 실행이 출력한 숫자, 회차가 끝난 뒤에 돌린 CI 결과처럼 어느 기록에도 없는 것이다". The home allows a record's fact in the orchestrator's part, as "that record's own sentence, or carries the record's coordinate" (`orchestration.md:369-372`). So the paragraph reads two ways. In the first reading, the table holds no record's verification, and the pointer is about some other place in the part, which the paragraph does not name. In the second reading, the pointer sits in the table's subsection and is about the table, so a phase record's verification sentence, copied or cited, goes into the table, and the first and last sentences are then false. The orchestrator who writes the table cannot ask which one is meant.

Before the fix, the paragraph had one reading. The removed sentence asked for the record's path, and a path is no verification, so "어느 기록에도 없는 것" stayed true. The first sentence is also the old rule in another spelling: "기록에 없는 검증만" is the shape of the removed Korean copy "기록에 없는 것만 쓰고" at `:27-29`, and of the policy's "only what no record holds", whose "only" the design's `## Rule changes` takes out (`frame/design.md:71-72`). The S3 search, `git grep -e "기록에 없는 것만" ...`, does not match it, because it searches for one wording. That makes the list of copies a sample, as contract rule 12 says.

The fix rewrites the paragraph so that the table holds what no record holds, and the pointer says it governs a record's verification written into the table:

```markdown
리뷰 체인을 거친 본문의 이 표에는 광역 실행이 출력한 숫자, 회차가 끝난 뒤에 돌린 CI 결과처럼 어느 기록에도 없는 검증을 적는다. 뒷부분에는 `frame/plan.md` 의 `## Phases` 절과 phase 기록의 경로가 옮겨져 있다. 회차 기록마다 `seal` 블록 전부와 각 지적의 제목도 옮겨져 있고, `trail/gate.md` 의 `seal` 블록과 `gaps.md` 의 `## Not verified` 절도 옮겨져 있다. phase 기록의 본문은 옮겨지지 않는다. 기록에 적힌 검증을 이 표에 적을 때 그것을 어떻게 적는지는 `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* 가 정한다.
```

Contract rule 19 asks the orchestrator's fold to follow it: the `## Removes` row at `frame/design.md:81` names only the path-alone sentence, and G10's clause at `:18` says the paragraph "now points to item 1's section". After the fix, both name the "기록에 없는 검증만" clause as well.

```seal
verdict: fixed 96cc18224
answer: The finding holds, and the whole paragraph was the unit. I read every sentence of `skills/writing-style/outside-the-review.md` *PR 본문에만 해당하는 것* against `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*. Only the verification table's paragraph at `:64` spoke of what the orchestrator's part may hold: its first and last sentences kept the table to what no record holds, and its fifth pointed to the home. The opening at `:27-30` points to the home, and the other subsections are prose rules that say nothing of records. The paragraph now reads: "리뷰 체인을 거친 본문에서 이 표는 오케스트레이터가 쓰는 앞부분에 든다. 광역 실행이 출력한 숫자와 회차가 끝난 뒤에 돌린 CI 결과는 어느 기록에도 없으므로 이 표에 적는다." It keeps the two sentences on what the copy holds, then ends "phase 기록의 본문은 옮겨지지 않는다. 기록에 적힌 검증을 이 표에 적을 때 그것을 어떻게 적는지는 `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* 가 정한다." This departs from the paste-ready paragraph in its opening only. The paste-ready "이 표에는 ... 어느 기록에도 없는 검증을 적는다" still names the table's content as one kind, so the closing pointer reads as an exception to it. The sentence written gives the two figures as what goes in because no record holds them, and says the table is in the orchestrator's part, so the home governs the rest of the table. The last sentence, "표에 남는 것은 ... 어느 기록에도 없는 것이다", is folded into the second and removed. Other spellings of the old rule were searched with `git grep -n -i` for "기록에 없는", "어느 기록에도", "only what no record", "what no record holds" and "no record holds" over `skills`, `agents`, `templates`, `evals`, `docs`, `CONTRIBUTING.md` and `README.md` (executed). Beyond this paragraph, the search found only the policy at `docs/the-review-record.md:270`, which the rule change settles, the corrected comment at `evals/scripts/rule_cases.py:827`, the home's list at `orchestration.md:366`, and two rows of `skills/settle/SKILL.md` about measurements, which do not apply here. The section was taken apart sentence by sentence, so the list is whole for this section; outside it, the list is a search for wordings and so a sample (contract rule 12). For the orchestrator's fold of `frame/design.md`, there are two replacements. First, in G10 at `:18`, replace "`skills/writing-style/outside-the-review.md:64` said how the verification table cites a phase record's verification, by the record's path alone, which is the old rule; it now points to item 1's section, as the line at `:27-30` does (round 1, finding 1)." with "`skills/writing-style/outside-the-review.md:64`, the verification table's paragraph, kept the table to verification no record holds ("기록에 없는 검증만") and asked for a phase record's verification by the record's path alone, which is the old rule in two sentences; it now gives the table what no record holds and points to item 1's section for a record's verification written into it, as the line at `:27-30` does (round 1, finding 1; round 2, finding 1)." Second, replace the `## Removes` row at `:81` with "| The clause keeping the verification table to "기록에 없는 검증만", the sentence saying a phase record's verification is cited by its path alone and not written again, and the sentence saying what stays in the table is what no record holds | `skills/writing-style/outside-the-review.md` *PR 본문에만 해당하는 것*, the verification table's paragraph | They stated the old rule. The paragraph now says the table, in the orchestrator's part, holds the figures no record holds, and points to `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* for a record's verification written into it, as the line at `:27-30` does (round 1, finding 1; round 2, finding 1) |".
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: the repair sentence at `skills/code-review/orchestration.md:381-386` now ends "Your part stays as you wrote it, except where the repair changed a record that a sentence of your part copies or cites: open that record again, and correct the sentence or its coordinate." Read against the one-reading rules, it has one reading. The one who acts is "you", the orchestrator, as everywhere in the section. "The repair" has the same antecedent as the "as the repair left them" before it, so the step is the re-run before each later spawn of the sealer and each `gh api -X PATCH`. The file is the body's part above the line, and the act is done when the sentence or its coordinate is corrected. "Copies or cites" names the two forms the rule at `:369-372` allows, and "copied sentence" is the home's own word (`:377`). `git grep -n -i -e "stays as you wrote" -e "part stays" -e "byte for byte"` over `skills agents docs templates` finds this sentence and `skills/code-review/scripts/pr_body.py:37`, which describes the command keeping the part, and no other statement of the old clause (executed). The merge with the base passes at the base's current head: `git merge-tree --write-tree HEAD` against `5e45418f` (`origin/release/v0.29.0`, holding #883's `af889979` and #1304) exited 0 (executed).

```seal
confirms: round-1#3
```
What holds: the Why cell at `changelog.md:9` cites `frame/design.md` G4 for the 0.28.0 bodies and G6 for the two 0.28.0 withholds, and says that in 0.29.0 the sealer withheld for #1270 and #1289 on a sentence "citing a record row that did not hold the fact it stated". Both withheld blocks say that (executed: `git show` of each branch's `guarantee.md`). #1270's `Verdict:` line says the bullet cites `frame/plan.md` A3 and A4, which "cover trail/ and guarantee.md only". #1289's says the line cites `frame/design.md` `## Removes`, whose row says the sweep "refuses the judgment this work states", and that the sweep never refused the sentence the body named. The fix pass claimed each 0.28.0 withhold held at least one sentence no record held. G6 bears that out: the count and the attribution for #1054, and the inference past `round-1.md:47` for #1139 (read). The Change cell did not change.

```seal
confirms: none
```
What matched: the orchestrator's fold at `36fce349`. The new *Judgments of the run* row at `frame/plan.md:38` names its grounds and two sections, and both stand: `skills/implement/orchestration.md:25` and `docs/the-reader-registry.md:7` (read). Its executed claim holds again: `rule_changes.parse` over `frame/design.md` gives one `Op(kind='change')` for `docs/the-review-record.md` *The guarantee*, with `errors=[]` and `unread=[]` (executed). The G10 clause and the `## Removes` row say what `e88b42fd` did, and finding 1 asks both to grow by one clause. `trail/phases/phase-1.md:31` still says line 64 stays. It is the phase's account at `6b7c9a08e`, which round 1's first close block names, and no fix pass writes a phase record, so it is no finding.

```seal
confirms: none
```
What matched: the narrow run in the clone. Round 1's nine modules and `tests/text/test_a_record_carries_no_comment.py`, which reads the work item's records, gave 436 passed, exit 0 (executed, `## Probes`). The fix pass's 1349 passed and 9 skipped is read, not re-run. No test was added or changed, so no test is read against its group. The suite label in `gaps.md` names the orchestrator's broad gate as the suite's answerer and claims no green, so the label is honest. `chain_check.py --baseline d57e9ee7 --root <branch worktree> --worktree`, run before this record was written, printed no notice of a test pin or a copy at a line of `frame/design.md` (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD | `gaps.md` *Not verified* | the orchestrator's broad gate, `seal gate --base release/v0.29.0 --record` this work item, after the round that answers finding 1 |
| G4's count of ten bodies, carried from the framer and not re-run | `frame/design.md` G4 | the sealer, reading the design as a party at its step 4 |
| Whether the next orchestrators give each count, "each", "every" or "all" and each attributed decision its coordinate (design S2) | `skills/code-review/orchestration.md:374-377` | the sealer, reading the orchestrator's part of the next bodies |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist` over `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`, `tests/evals/test_rule_cases.py`, `tests/text/test_a_language_section_of_writing_style_opens_alone.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_the_chain_section_has_one_shape.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/text/test_a_record_carries_no_comment.py`, in the clone | 436 passed, exit 0 |
| `git fetch` of `origin/release/v0.29.0` from the branch worktree into the clone, then `git merge-tree --write-tree HEAD FETCH_HEAD` | the base is `5e45418f`; exit 0 |
| `git grep -n -e "기록에 없는" -e "기록에도 없는" -e "only what no record" -e "what no record holds" -- skills agents templates docs evals hooks` | four hits: `docs/the-review-record.md:270` (the policy), `evals/scripts/rule_cases.py:827` and `skills/code-review/orchestration.md:366`, which agree with the new rule, and `skills/writing-style/outside-the-review.md:64` (finding 1) |
| `python3 -c` calling `rule_changes.parse` over `frame/design.md` | one `change`, `errors=[]`, `unread=[]` |
| `python3 skills/code-review/scripts/chain_check.py --baseline d57e9ee7 --root <branch worktree> --worktree`, before the record | exit 0; no pin or copy notice; it named round 1's two `fixed` findings as owed a verifying round, and the missing gate record and guarantee |
