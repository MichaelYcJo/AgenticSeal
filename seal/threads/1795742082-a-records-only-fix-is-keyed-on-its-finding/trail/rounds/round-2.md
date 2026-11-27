# Review round 2: 1795742082-a-records-only-fix-is-keyed-on-its-finding

```seal
target: 6ae78a7e1, fixes 0fd7ab7cb..6ae78a7e1
```

This is a verifying round. Its fix range holds four commits: the framer's fold `4358a3526` (`frame/design.md:52`), the fix `15c61548e` (`agents/proofer.md:165-168`), the records commit `b07024a14` (`gaps.md:8`) and the close block `6ae78a7e1`. The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md` whole at `6ae78a7e1`. The records language and the commit language are both English, so no `pr.<lang>.md` is owed. `seal/parity.json` is not declared, so no parity comparison is owed.

Carried from round 1 and not established again: where the records arm's key lives (`chain_check.py#located_in_records`, `#finding_of`), which test modules open `agents/proofer.md`, and the base's measurement of the core's size. Round 1's verdicts on the code outside the fix range are not carried. That code is outside this round's bound, and the fix range changes none of it.

## Findings

### 1. The orchestrator's decision to fold round 1's finding 1 into the frame has no row in *Judgments of the run*

```seal
severity: should
location: `seal/threads/1795742082-a-records-only-fix-is-keyed-on-its-finding/frame/plan.md:61-65`
evidence: read `skills/implement/orchestration.md:61-75`, `skills/implement/orchestration.md:119-128`, `skills/implement/SKILL.md:240`, `seal/threads/1795742082-a-records-only-fix-is-keyed-on-its-finding/frame/plan.md:61-65`; executed `git log --format='%h %s' 68bb3d5a9..6ae78a7e1 -- seal/threads/1795742082-a-records-only-fix-is-keyed-on-its-finding/frame/`, `git grep -n -i -E "^\| 2026-11-2[0-9] \|[^|]*(fold|finding [0-9])" 6ae78a7e1 -- 'seal/threads/*/frame/plan.md'`
```

Why it matters: the settle and `seal settle`'s dry run read the orchestrator's judgments from this section, and the guidance improves from that record (`skills/implement/SKILL.md:240`; `skills/core/SKILL.md` *The first value: efficient development through the AgenticSeal process*, the paragraph opening **A judgment stands on a source document**). A decision with no row reaches neither of them.

The grounds. `skills/implement/orchestration.md:61-75` counts "a round finding located in a frame file" as a decision, which the framer folds. Round 1's finding 1 names `frame/design.md:52` on its `location:` line, and the framer folded it at `4358a3526`. `skills/implement/orchestration.md:119-128` says the orchestrator writes each decision, its grounds and the document it judged against as one row of `frame/plan.md` *Judgments of the run* before it sends the decision. At `6ae78a7e1` the section holds only its empty template row (`frame/plan.md:65`). The fold commit changed `frame/design.md` alone, and the worktree holds no uncommitted change (executed: `git status --short` printed nothing). Other work items of the release write this row for the same act. For example, `1795483768-chain-check-asks-git-the-same-question-twice/frame/plan.md:51` reads "Round 1's findings 1 and 2 are folded into `frame/design.md` by the framer", as the second command on the evidence line prints.

The first command on the evidence line lists every commit that changed this work item's frame since the base. It prints two framer folds, `4358a3526` and `e33a593df`, so the list of folds is whole for this branch. `e33a593df` is outside this round's fix range, and round 1 read the commit and opened nothing on it. It also has no row. Whether it was a decision the orchestrator sent, and so owed a row, is the orchestrator's to say, because only its session holds what it sent. The snippet covers `4358a3526`. Where `e33a593df` was such a decision, the orchestrator owes its row in the same edit.

The row is the orchestrator's to write (`skills/implement/SKILL.md:240`), so this finding goes to the orchestrator and not to a crafter's fix pass. It is located in the work item's records alone, so a fix that touches only `frame/plan.md` falls under the row *No fix that no round reads* of `skills/core/SKILL.md` *Judgment is not licence to skip a party*.

```markdown
| 2026-11-27 | Round 1's finding 1 is folded into `frame/design.md` *Scope* item 6 by the framer, before the fix pass, and the fix pass writes `agents/proofer.md` in the fold's words | The finding is located in the frame's bullet at `frame/design.md:52` as well as in the rule that bullet describes, and its grounds say the bullet's phrase has two readings, so the sentence that says what the work does changes | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **A decision made after the frame is committed is folded** |
```

The row replaces the empty row at `frame/plan.md:65`.

```seal
verdict: fixed 4575154aa
answer: The orchestrator wrote the row in the finding's words for `4358a3526`, and a row for `e33a593df`, which was a decision the orchestrator sent: after phase 1 it resumed the framer to fold the *Overlap with the release* row the crafter reported HEAD contradicted. Both rows replace the empty template row and stand at `frame/plan.md:65-66`. The evidence line's first command, run again at `4575154aa`, prints the framer's frame commits `0db259108`, `e33a593df` and `4358a3526`, the crafter's Status cell commit `bc491e5a8`, and `4575154aa`; each fold among them now has its row. Its second command, run again at `4575154aa`, prints both new rows of this work item, at lines 65 and 66. The commit touches `frame/plan.md` alone
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the sentence at `agents/proofer.md:164-168` has one reading at `6ae78a7e1` (read). It reads "a finding located in the file that holds it, the file of this work item's diff for a unit and the file of its records for a sentence, and never in the merged-in text, which the finding names on `evidence:`". The pronoun "it" has the unit or the sentence as its antecedent, and the appositive names which file each takes. A code unit is therefore located in its code file, and a record sentence in its record file. That agrees with `chain_check.py#located_in_records`, which gives a records-only fix to the sealer only where the finding block names a record path. The relative "which" attaches to "the merged-in text", and "the finding" is named, so the clause has one subject. The bullet at `frame/design.md:52`, folded at `4358a3526`, states the same words (read: the two hunks of `git diff 0fd7ab7cb..6ae78a7e1`). The evidence line's search from round 1, run again at `6ae78a7e1`, prints no line of `agents/`, `skills/`, `docs/` or `templates/`. In `seal/threads/` it prints round 1's own quotes and the four lines of three other work items that the close block's answer names, at the coordinates it gives (executed). Each of those four describes its own work item's findings, and none states this rule.

What matched, on the crafter's claim. Claimed: the pass did not apply round 1's snippet as written, because in "never in the merged-in text, which it names on `evidence:`" the pronoun could point at the finding or at the file. Found: the snippet opens "is a finding located in the file of this work item's diff or records that holds it". So the finding, the file, and the unit or sentence that "holds it" names are each an antecedent for the second "it". The departure is grounded in `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, and the words used are the fold's (read).

What matched: the close block's claim that `tests/skills/test_chain_check.py` is the one module outside `tests/text` and `tests/behaviour` that opens the tree's `agents/proofer.md`. The other modules that hold the path, `tests/skills/test_rules.py`, `tests/evals/test_noninferiority.py` and `tests/github/test_release_report.py`, write it into fixtures under `tmp_path` (executed: `git grep -l -F "proofer.md"` over `tests/`, then each hit read). The 17 modules under `tests/text` and `tests/behaviour` that hold the path ran as one command, the paste check and the line-wrap check among them: 254 passed and 8 skipped (executed, `## Probes`).

What matched: `gaps.md:8` now gives the main checkout's path as 43 characters, and the path is 43 characters (executed: `printf %s` of the path through `wc -c`). The 9919 the row gives is the figure round 1 projected at 43, so the row's answerer and its action stand. `trail/phases/phase-1.md:12` still writes 42. It is the phase's account at its close, which `skills/implement/SKILL.md:243` dates to that moment. No party acts from that line, since the row in `gaps.md` is where the orchestrator acts, and round 1's record and `gaps.md:8` both carry 43. So this round opens no finding on it.

What matched: the other records the round read whole state nothing `6ae78a7e1` contradicts (read). `changelog.md:3` says the new rule "holds the work item's diff and records against the merged tree", which the fix leaves true. `frame/questions.md` Q1, `gaps.md:9-10` and `pr.md:1` are unchanged by the fix range and still hold. The fix range adds no test and no unit of code, so no new test is read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` at `6ae78a7e1` beyond the 17 modules this round ran | the `Broad gate` key of `seal/config.json` | the orchestrator's broad run, after finding 1 is closed |
| Whether `e33a593df` was a decision the orchestrator sent to the framer, and so owes a row of *Judgments of the run* | `seal/threads/1795742082-a-records-only-fix-is-keyed-on-its-finding/frame/plan.md:65` | the orchestrator, which holds what it sent |
| Whether a sealer in a real run withholds where a records-only fix left an outside path the finding asked to change (`frame/questions.md` Q1) | `seal/follow-up.md:47` | the repository owner, at the next release |

## Probes

| Command | Result |
|---|---|
| `bin/test -q $(cat <scratchpad>/1795742082-a-records-only-fix-is-keyed-on-its-finding/round-2/modules.txt)`, the list written by `git grep -l -F "proofer.md" HEAD -- tests/text tests/behaviour` | 254 passed, 8 skipped, exit 0 |
| `git grep -n -e "located in this work" -e "item's file, with the merged-in" 6ae78a7e1 -- agents skills docs templates seal` | no line outside `seal/threads/`; four lines of three other work items and round 1's own quotes |
| `printf %s <the main checkout's path> \| wc -c` | 43 |
