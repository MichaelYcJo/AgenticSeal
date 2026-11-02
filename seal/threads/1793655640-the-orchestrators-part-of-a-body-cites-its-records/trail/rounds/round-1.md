# Review round 1: 1793655640-the-orchestrators-part-of-a-body-cites-its-records

```seal
target: 9461a73e against release/v0.29.0
```

This is the first round, so no earlier round's coordinates were carried, and every fact below was established this round. The work happened in a `git clone --no-local` of the branch worktree at `9461a73e`, under the round's scratch directory `<scratchpad>/1290-round-1/clone`. The target is the branch against `origin/release/v0.29.0` at `d57e9ee7`: five commits, of which `6b7c9a08` changes the five files of *Scope* items 1 to 5 and `9461a73e` adds the orchestrator's `### Process changes` row. No `seal/parity.md` is declared, so the round block has no `original:` line.

The change is text agents read, so every axis was weighed against `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*: one reading, one home for a rule, and who acts and when. The code axes of the comparison table (authorization, query scope, concurrency, security) have nothing to compare in a prose change. The change's own axes were these. Does each rewritten sentence have one reading? Does any other sentence still state how the orchestrator's part states a record's fact? And does the rule say when the orchestrator opens a record, through the whole life of the body?

## Findings

### 1. A second sentence in the same file still tells the orchestrator to cite a phase record by its path alone

```seal
severity: should
location: `skills/writing-style/outside-the-review.md:64`
evidence: read `skills/writing-style/outside-the-review.md:27-30`, `skills/writing-style/outside-the-review.md:64`, `skills/code-review/orchestration.md:369-373`
```

Why it matters: the section *PR 본문에만 해당하는 것* now opens by saying that `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* decides how the orchestrator writes a record's fact above the line (`outside-the-review.md:27-30`). Its subsection *검증한 것을 표로 남긴다* then decides it a second way, for the verification table, which is part of the orchestrator's part: "phase 기록에 적힌 검증이 필요하면 다시 쓰지 않고 그 기록의 경로를 적는다" (`:64`). That sentence differs from the rewritten rule twice. First, it forbids writing the fact again, where the rule allows the record's own sentence. Second, it asks for the path alone, where the rule's coordinate is "its path, and the row, heading, finding or line that holds the fact" (`orchestration.md:370-372`). An orchestrator writing the table now reads two rules and has to choose between them, and the path alone is the form this work replaces: the sealer has to search the phase record for the fact.

The design claimed the line "agrees with the new rule, and the line stays" (`frame/design.md` G10), and phase 1 judged it the same way ("Design G10 judged it in agreement, and it stays", `trail/phases/phase-1.md`, *Other places stating the rule*). The line agrees with the old rule, which said to name the record's path, and not with the new one. The fix is a pointer, like the one at `:27-30`, and it restates none of the rule. The sentence to replace is the fourth of line 64:

```markdown
phase 기록의 본문은 옮겨지지 않으므로, phase 기록에 적힌 검증이 필요하면
`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the sealer seals* 가 기록의 사실을 적으라고 하는 방식대로 적는다.
```

Contract rule 19 asks the same commit to correct what stood on the old judgment: the clause of `frame/design.md` G10 that calls line 64 in agreement.

```seal
verdict: fixed e88b42fd6
answer: The finding holds: the fourth sentence of `skills/writing-style/outside-the-review.md:64` asked for the record's path alone and forbade the record's sentence, which is the old rule. It now reads "phase 기록의 본문은 옮겨지지 않는다. phase 기록에 적힌 검증이 필요할 때 그것을 어떻게 적는지는 `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* 가 정한다.", in my own words: the paste-ready "적으라고 하는 방식대로 적는다" stacks two verbs of writing, and the sentence written mirrors the pointer at `:27-30`, so the section points to the home the same way twice and restates none of it. The paragraph stays on one line, as the other paragraphs of that subsection are. The clause of `frame/design.md` G10 is the orchestrator's to fold, not this pass's; its replacement for "`skills/writing-style/outside-the-review.md:63` asks that a phase record's verification be cited by path and not written again. That agrees with the new rule, and the line stays." is "`skills/writing-style/outside-the-review.md:64` said how the verification table cites a phase record's verification, by the record's path alone, which is the old rule; it now points to item 1's section, as the line at `:27-30` does (round 1, finding 1)." The sentence removed is a copy the frame's `## Removes` did not name, and a row for it there is the orchestrator's to add. `trail/phases/phase-1.md` *Other places stating the rule* still says the line stays; a fix pass writes no phase record, so this block is where the judgment stands corrected.
```

### 2. The rule says when the orchestrator opens a cited record, but not that it opens it again after a record repair

```seal
severity: should
location: `skills/code-review/orchestration.md:372-373`, `skills/code-review/orchestration.md:381-384`
evidence: read `skills/code-review/orchestration.md:369-384`, `seal/threads/1793582903-each-entry-links-its-pull-request/guarantee.md:40-85`
```

Why it matters: the rewritten rule ties opening the record to one moment: "Open that record when you write the sentence, after the last fix pass" (`orchestration.md:372-373`). The section then states the repair loop without changing it: "Run the command again before every later spawn of the sealer and before every `gh api -X PATCH` of the body, so the copy holds the records as the repair left them; your part stays as you wrote it" (`:381-384`). Under the old rule the orchestrator's part held no record's fact, so keeping it as written was safe. Under the new rule it holds record sentences and coordinates down to the line, and a repair after a withhold changes records. The copy is written again, but the part's copy of a repaired sentence, or its `round-1.md:47`, now points at text that is gone or has moved. Nothing in the section asks the orchestrator to open those records again, and "your part stays as you wrote it" reads as an instruction that it need not.

This is the normal flow, not an edge case. #1139's withhold asked for a record repair alongside the body's ("the same words stand in frame/plan.md:100's grounds", `seal/threads/1793582903-each-entry-links-its-pull-request/guarantee.md:56`). The repair commit then touched `frame/plan.md` alone, as the re-audit table of the same file says. The frame's fourth withheld sentence is a copy of a round's wrong sentence (`frame/design.md` G6). Where such a sentence is repaired in the record, the copy of it in the orchestrator's part is the sentence the sealer withholds on next.

The fix rewrites the last clause of the repair sentence in place:

```markdown
is not the records' text at HEAD. **Run the command again before every
later spawn of the sealer and before every `gh api -X PATCH` of the body**,
so the copy holds the records as the repair left them. Your part stays as
you wrote it, except where the repair changed a record a sentence of your
part copies or cites: open that record again, and correct the sentence or
its coordinate.
```

```seal
verdict: fixed e88b42fd6
answer: The finding holds: under the rewritten rule the orchestrator's part holds record sentences and line coordinates, and "your part stays as you wrote it" told the orchestrator to keep them after a repair that moves or changes them. The repair sentence of `skills/code-review/orchestration.md` now ends "so the copy holds the records as the repair left them. Your part stays as you wrote it, except where the repair changed a record that a sentence of your part copies or cites: open that record again, and correct the sentence or its coordinate." That is the paste-ready text with "that" added after "a record", read at the step that runs it: the orchestrator after a withhold whose repair touched a record, before the next spawn of the sealer or the next `gh api -X PATCH`. The sentence at `:372-373` is unchanged, since it governs the first writing and the new sentence governs each repair. Only the sentence the finding names changed, and `git merge-tree --write-tree HEAD af889979` exited 0 against the base with #883 merged (executed). `git grep` outside `seal/threads/` for "stays as you wrote", "part stays", "as the repair left" and the PATCH phrase found only this sentence (executed). `skills/code-review/orchestration.md` *Commit `guarantee.md`* already lists the orchestrator's part as a thing a repair touches, and `skills/code-review/scripts/pr_body.py:37`'s "A rewrite keeps the orchestrator's part byte for byte" is the command's behaviour; both agree and stand. That search is for wordings, so it is a sample in the sense of contract rule 12.
```

### 3. The process row says the 0.29.0 withholds were on sentences written from memory, and their records say each cited a record that does not hold its fact

```seal
severity: should
location: `seal/threads/1793655640-the-orchestrators-part-of-a-body-cites-its-records/changelog.md:9`
evidence: executed `git show origin/fix/1270-a-sha-path-citation-opens-in-no-clone-after-the-squash:seal/threads/1793599988-a-citation-opens-after-the-squash/guarantee.md`, `git show origin/docs/1289-the-milestone-rule-reads-a-count-as-a-ceiling:seal/threads/1793599989-a-release-is-sized-with-no-ceiling/guarantee.md`
```

Why it matters: the row's Why cell says "the sealer withheld twice in 0.28.0, and twice more in 0.29.0 (#1270, #1289), on a sentence of that part written from memory of the run". For the two 0.29.0 withholds, neither guarantee says that. #1270's withheld block (`seal/threads/1793599988-a-citation-opens-after-the-squash/guarantee.md:57` on its branch) says the sentence cited "frame/plan.md A3 and A4", and A3 and A4 do not cover what it said. #1289's (`seal/threads/1793599989-a-release-is-sized-with-no-ceiling/guarantee.md:35` on its branch) says the sentence cited "`frame/design.md` `## Removes`", and the cited row says something else ("refuses the judgment this work states"). So both sentences already carried a path and a row or heading, which is the form the new rule accepts. Each was withheld because the coordinate did not hold the fact, which is the failure the plan names for its chosen approach: "an orchestrator writes a sentence with a coordinate that does not hold the fact" (`frame/plan.md` *Technical context*).

A process row is what the settle reads to judge whether a change to the way of working caught what it was for (`skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both*). Written this way, the row gives the settle two withholds as cases of memory, when the records show them as the case the rule is weakest on. That is the kind of sentence this work is about: a cause stated past what the record holds. The 0.28.0 half of the clause is the design's own reading (`frame/design.md` G6) and stands. The fix rewrites the Why cell so that each half carries what its record says:

```markdown
The old rule said the part restates no record, and every 0.28.0 body stated records' facts above the fold anyway (`frame/design.md` G4); the sealer withheld twice in 0.28.0 on a sentence of that part written from memory of the run (`frame/design.md` G6), and twice in 0.29.0 (#1270, #1289) on a sentence that cited a record which does not hold its fact (each one's `guarantee.md`, the withheld block)
```

```seal
verdict: fixed bce68fe8
answer: Read bce68fe8 against the finding, and it holds. Its Why cell cites `frame/design.md` G4 for the 0.28.0 bodies and G6 for the two 0.28.0 withholds, and says that in 0.29.0 the sealer withheld for #1270 and #1289 on a sentence citing a record row that did not hold the fact it stated. Both withheld blocks say that (executed: `git show` of each branch's `guarantee.md`). #1270's at `:57` cites `frame/plan.md` A3 and A4, which cover `trail/` and `guarantee.md` only. #1289's at `:35` cites `frame/design.md` `## Removes`, whose row says the sweep "refuses the judgment this work states". The 0.28.0 sentence, "on a sentence of that part that a record did not hold", fits G6. Each withhold held at least one sentence no record held: the count and the owner's ask for #1054, and the inference past `round-1.md:47` for #1139. G6's fourth sentence was a record's own wrong sentence, so the row says "a sentence", not "the sentences". Nothing in the cell is still wrong. The orchestrator's wording departs from the paste-ready text and keeps its substance.
```

## Confirmations

```seal
confirms: none
```
What matched: design S1 and *Scope* item 1. The paragraph at `skills/code-review/orchestration.md:369-380` says each of the four points, and no sentence of the section still says the part restates no record (read). Both departures in `trail/phases/phase-1.md` hold. "Attributed to a person" has one reading where "given to a person" had two, and the case it names, "the owner asked", is design G6's "attribution to a person". Joining the fourth point with a colon keeps the frame's words. The list of what no record holds before the new sentences is unchanged, as *Scope* item 1 asks. The next sentence, which opens "A sentence of your part that states a record's fact", is the one that permits such a sentence, and the policy `to` text says the same with "and".

```seal
confirms: none
```
What matched: design S3 and S5. The S3 search, `git grep -n -e "기록에 없는 것만" -e "does not restate it" -e "restates no record" -- skills evals agents templates`, printed nothing and exited 1 (executed). `git diff -U0 85a238c6 HEAD -- skills/code-review/orchestration.md` prints one hunk, `@@ -369,2 +369,11 @@`, so #883's paragraph from `:388` on is untouched (executed). The merge with #883's branch (G11) was not re-run.

```seal
confirms: none
```
What matched: *Scope* items 3 to 5. `skills/commit-pr-convention/SKILL.md:240-244` gives the round's findings to the copy and points to the one home, and states no copy of the rule. `skills/implement/acts.md:75`'s last sentence keeps `still a sentence` and names the sealer's reading against the records and the tree. The comment at `evals/scripts/rule_cases.py:826-829` states the rule change's `to` text in short, and the fixture's text did not change (read).

```seal
confirms: none
```
What matched: design S4. The rule change's `from` text, "only what no record holds", occurs once in `docs/the-review-record.md` (executed: `grep -c`, 1). `chain_check.py --baseline origin/release/v0.29.0 --root <branch worktree> --worktree`, run before this record was written, printed no notice of a test pin or a copy at a line of `frame/design.md` (executed). So no notice gave this round a finding.

```seal
confirms: none
```
What matched: design G6 against the two 0.28.0 guarantees. #1054's withheld block names the count of departures (`seal/threads/1793573496-the-settle-folds-named-directories-the-person-marks/guarantee.md:54`). The rewritten row at `:46` records that the attribution to the owner with no coordinate went with it. #1139's withheld block names the two sentences and `frame/plan.md:100` (`seal/threads/1793582903-each-entry-links-its-pull-request/guarantee.md:56`) (read). The `### Fixed` entry of `changelog.md:3` names three sentences "written from memory of the run". That count matches G6, whose fourth sentence was a copy of a round's sentence and not memory. The tree also holds three 0.27.3 withholds on the orchestrator's part, each on an "each" or "every": `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/guarantee.md:38`, `seal/threads/1793538229-each-passage-keeps-its-home/guarantee.md:38` and `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/guarantee.md:42` (executed: `git tag --contains` on each file's adding commit gives `v0.27.3`). They fall outside the design's "In 0.28.0" and do not contradict it, and they bear out the rule's third point.

```seal
confirms: none
```
What matched: the crafter's narrow run, in part. Nine of the phase's 40 modules were run in the clone, the ones that open `orchestration.md`, `commit-pr-convention/SKILL.md`, `outside-the-review.md`, `acts.md` and `rule_cases.py` by name (`## Probes`): 433 passed, exit 0 (executed). The crafter's 1349 passed and 9 skipped over 40 modules is read, not re-run. The suite label in `gaps.md` is honest. It names the orchestrator's broad gate as the answerer for the suite, and it claims no green. No test was added, so no test is read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD, and with them `frame/questions.md` Q1 beyond the narrow run | `gaps.md` *Not verified* | the orchestrator's broad gate, `seal gate --base release/v0.29.0 --record` this work item |
| G4's count, ten bodies merged into `release/v0.28.0` stating record facts above `## From the records`, which the framer took with `gh pr list` and this round did not re-run | `frame/design.md` G4 | the sealer, reading the design as a party at its step 4 |
| Whether the next orchestrators give each count, "each", "every" or "all" and each attributed decision its coordinate (design S2) | `skills/code-review/orchestration.md:373-377` | the sealer, reading the orchestrator's part of the next bodies |
| The merge beside #883 (S5), probed by the framer and not run again | `frame/design.md` G11 | the orchestrator's merge of the base, if #883 lands first |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/text/test_docs_line_wrap.py ...` and the same over the tracked paths, in the clone | `no tests ran`, exit 5, both times: the xdist workers started and collected nothing in this sandbox, so neither call ran a test |
| `bin/test -q -p no:xdist tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_every_orchestrator_act_names_its_delivery.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/evals/test_rule_cases.py tests/text/test_a_language_section_of_writing_style_opens_alone.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_the_chain_section_has_one_shape.py tests/text/test_the_rules_have_one_owner.py`, in the clone | 433 passed, exit 0 |
| `git grep -n -e "기록에 없는 것만" -e "does not restate it" -e "restates no record" -- skills evals agents templates` | nothing printed, exit 1 |
| `git grep -n -i -e "경로를 적는다" -e "cited by path" -e "names the record's path" -e "record's path" -- skills agents templates docs` | four hits; the one stating how the orchestrator's part cites a record is `skills/writing-style/outside-the-review.md:64` (finding 1) |
| `git show <branch>:<guarantee.md> \| grep -n "Verdict:"` over the #1270 and #1289 branches, and over every `guarantee.md` at `origin/release/v0.29.0` | the withheld blocks finding 3 and the fifth confirmation quote |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.29.0 --root <branch worktree> --worktree`, before the record | exit 0; no pin or copy notice; it named the missing round record, gate record and guarantee |
