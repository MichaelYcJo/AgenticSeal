# Review round 3: 1793655640-the-orchestrators-part-of-a-body-cites-its-records

```seal
target: d28734cf, fixes 844ca534..d28734cf
```

This is a verifying round. Its target is the diff of the last fixes, three commits: `96cc1822` (round 2, finding 1), `3ba321b2` (the fix pass's close block) and `d28734cf` (the orchestrator's fold into `frame/design.md`). The work happened in a `git clone --no-local` of the branch worktree at `d28734cf`, under `<scratchpad>/1290-round-3/clone`. No `seal/parity.md` is declared, so the round block has no `original:` line.

Carried from round 2 and not re-established: the ten test modules that read the edited files, and the commands of its `## Probes`. Re-derived this round: the verdict below, what the gate record's block holds, the rule change's parse, the narrow run and the chain check.

The one changed paragraph, `skills/writing-style/outside-the-review.md:64`, was read sentence by sentence against `skills/code-review/orchestration.md:363-386` and against `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*: one reading, one home for a rule, and who acts and when. The round stayed inside the fix diff.

## Findings

None. The round opened no finding.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the paragraph at `skills/writing-style/outside-the-review.md:64` now says one thing about the table, and that thing agrees with the rule's home. Its seven sentences, read in order (read):

1. "리뷰 체인을 거친 본문에서 이 표는 오케스트레이터가 쓰는 앞부분에 든다." This puts the table in the orchestrator's part. The section's opening at `:27-30` says the section's rules apply to that part alone, and the home's list of what that part holds (`orchestration.md:366-369`) holds the table's two figures.
2. "광역 실행이 출력한 숫자와 회차가 끝난 뒤에 돌린 CI 결과는 어느 기록에도 없으므로 이 표에 적는다." It gives the two figures and the reason they go in. It has no "만", so it does not keep the table to them. Its reason is true. `trail/gate.md` holds one `seal` block, and `hooks/lib/fields.py:221-235` gives that block one line, `run: <tree> against <base>`, with no count in it (read; a committed `trail/gate.md` under `seal/threads/1793538229-each-passage-keeps-its-home/` holds the one line). So the broad run's printed figures stand in no record, as the home's list says.
3. Sentences three to five say what the copy below the line holds. They are unchanged from the base (`git show d57e9ee7:skills/writing-style/outside-the-review.md`, line 63, executed).
4. Sentence six, "phase 기록의 본문은 옮겨지지 않는다.", is the base's clause with its old consequence cut off, and says only what the copy leaves out.
5. The last sentence: "기록에 적힌 검증을 이 표에 적을 때 그것을 어떻게 적는지는 `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* 가 정한다." It leaves how a record's verification is written into the table to the home, and restates none of the home's rule. It is built like the pointer at `:28-30`, "기록에 있는 사실을 어떻게 적는지는 ... 가 정한다", so the section points to the home in one way, twice.

Round 2 found two readings: a first sentence keeping the table to what no record holds, and a pointer that let a record's verification in. Neither is left. Sentence 2 names what goes in without closing the table, and the last sentence governs what else goes in. So the pointer is no exception to a rule, and the old "only" is gone. The last sentence widens the base's "phase 기록에 적힌 검증" to "기록에 적힌 검증". The home's rule covers a fact from any record (`orchestration.md:369-372`), so the wider reading agrees with it.

The fix pass claimed that only this paragraph of *PR 본문에만 해당하는 것* speaks of what the orchestrator's part may hold, and that the list is whole for the section because the section was taken apart sentence by sentence. Read against `:15-64`, the claim holds. The opening at `:17-30` is the pointer. The four subsections from `:32` to `:58` give rules on plain words, reasons, file lists and operational items, and none of them names a record. Taking the section apart is one of contract rule 12's three methods, and the hand-back calls the search outside the section a sample. The fix pass also departed from round 2's paste-ready opening, and gave its grounds: the paste-ready sentence named the table's content as one kind, so the pointer would read as an exception to it. The wording written avoids that reading, and the departure holds.

`git grep -n -e "기록에 없는 검증" -e "표에 남는" -e "어느 기록에도" -e "기록에 적힌 검증"` outside `seal/threads/` prints the one paragraph (executed). The removed wordings stand nowhere else, and no test pinned them: the narrow run passes (the fourth confirmation).

```seal
confirms: none
```
What matched: the orchestrator's fold at `d28734cf`. The G10 clause at `frame/design.md:18` and the `## Removes` row at `:81` are the two replacements the close block of round 2, finding 1, gives, word for word (read, `git show d28734cf`). Both say what `96cc1822` did. G10 calls the old paragraph "the old rule in two sentences", and the row lists three removed items: the clause "기록에 없는 검증만", the path-alone sentence and the sentence on what stays in the table. That count is the frame's own reading and no finding. No reader acts on it: the settle reads `## Removes`, and the row names all three items.

```seal
confirms: none
```
What matched: design S4 after the fold. `rule_changes.parse(text, "docs")` over `frame/design.md` gives one `Op(kind='change')` for `docs/the-review-record.md` *The guarantee*, with `errors=[]` and `unread=[]` (executed). The fold touched G10 and `## Removes` only, and left `## Rule changes` unchanged.

```seal
confirms: none
```
What matched: the narrow run in the clone. Round 2's ten modules, the ones that open the edited files or the work item's records, gave 436 passed, exit 0 (executed, `## Probes`). The fix pass's 1349 passed and 9 skipped at `96cc1822` is read, not re-run. No test was added or changed, so no test is read against its group. The suite label in `gaps.md` names the orchestrator's broad gate as the suite's answerer and claims no green, so the label is honest. `chain_check.py --baseline d57e9ee7 --root <branch worktree> --worktree`, run before this record was written, printed no notice of a test pin or a copy at a line of `frame/design.md` (executed), so no notice gave this round a finding. This round leaves nothing open. The orchestrator's broad run comes next, and then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD | `gaps.md` *Not verified* | the orchestrator's broad gate, `seal gate --base release/v0.29.0 --record` this work item |
| G4's count of ten bodies, carried from the framer and not re-run | `frame/design.md` G4 | the sealer, reading the design as a party at its step 4 |
| Whether the next orchestrators give each count, "each", "every" or "all" and each attributed decision its coordinate (design S2) | `skills/code-review/orchestration.md:374-377` | the sealer, reading the orchestrator's part of the next bodies |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist` over `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`, `tests/evals/test_rule_cases.py`, `tests/text/test_a_language_section_of_writing_style_opens_alone.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_the_chain_section_has_one_shape.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/text/test_a_record_carries_no_comment.py`, in the clone | 436 passed, exit 0 |
| `git grep -n -e "기록에 없는 검증" -e "표에 남는" -e "어느 기록에도" -e "기록에 적힌 검증" -- . ':!seal/threads'` | one hit, `skills/writing-style/outside-the-review.md:64` |
| `python3 -c` calling `rule_changes.parse` over `frame/design.md` | one `change`, `errors=[]`, `unread=[]` |
| `python3 skills/code-review/scripts/chain_check.py --baseline d57e9ee7 --root <branch worktree> --worktree`, before the record | exit 0; no pin or copy notice; it named round 2's `fixed` finding and `96cc1822` as owed a verifying round, and the missing gate record and guarantee |
