# Review round 2: 1794383425-a-committed-durations-file-turns-ci-red

```seal
target: 2815d6f7c, fixes 335cc0e75..2815d6f7c
```

This round verifies the fixes. It reviews the diff from the base merge `335cc0e75` to `2815d6f7c`, made of `bd4ec54d8`, `62a2fb4f1`, `e11652441`, `1e0704773` and `2815d6f7c`. It also reads this work item's records whole at `2815d6f7c`. The base is now `1a01c761a`, which brought #1481 (#1526) in at `335cc0e75`. This round re-ran the facts round 1 executed: the `union_step` probe and the narrow shard module. The only weighing it carried is round 1's weighing of the `chain_check.py` notices, which `## Confirmations` names.

## Findings

### 1. The plan says #1481 meets nothing here, and both now change step 5 of the settle skill

```seal
severity: should
location: `seal/threads/1794383425-a-committed-durations-file-turns-ci-red/frame/plan.md:73-75`
evidence: executed `git show --stat 1a01c761a -- skills` (`skills/settle/SKILL.md`, 73 lines), `git show 1a01c761a -- skills/settle/SKILL.md` (its hunk stands in step 5 and keeps the clause "A settle's commit or a durations refresh carries"), `git show --remerge-diff --stat 335cc0e75` (no conflict), and `git diff 335cc0e75 2815d6f7c -- skills` (`62a2fb4f1` edits step 5); read `frame/plan.md:62-86`
```

Why it matters: `frame/plan.md` *Overlap with the release* says: "#1481 changes `skills/settle/scripts/settle.py` and `tests/skills/test_settle.py` and meets nothing here". At the target, both halves of that sentence are wrong.

- #1481 merged as `1a01c761a` and also rewrote `skills/settle/SKILL.md`. Its hunk lies in step 5 of *The settling session's procedure*, in the paragraph on judgments that earlier settles removed. That paragraph ends in the sentence round 1's finding 3 named.
- This work now changes the same paragraph. The fix for round 1's finding 3, `62a2fb4f1`, takes "or a durations refresh" out of it. That fix was applied after the merge `335cc0e75` took #1481, and the merge has no conflict.

The section defines two items as meeting where both change a file. This pair meets by that definition, and the section's other rows record each such pair with which one merged first. A sealer who reads the overlap reads that the settle skill is untouched by any other item.

The fix for round 1's finding 3 owed this sentence too, since the fix made `skills/settle/SKILL.md` a file this work changes. The framer's fold at `1e0704773` added the clause to *Scope* item 7 and `## Removes` and left this section as it stood. Round 1's closes hold for what each named, so this round names no `regression:` or `reopens:` line. The defect is a sentence that the fix and the merge together made false, and no fix commit changed that sentence.

The fix deletes the sentence at `:73-75` and adds a row beside #1498's, in the order of the other merged rows:

```markdown
| #1481 | `skills/settle/SKILL.md` step 5: it rewrote the paragraph on the judgments earlier settles removed, and this work takes "or a durations refresh" out of the same paragraph (`62a2fb4f1`). Its frame reads the `--stale-fails` verdict this work removes only to conclude that its new cases do not cross it. | #1481 | #1481 merged first (#1526, `1a01c761a`), and this branch took it at `335cc0e75` with no conflict; `62a2fb4f1` edits the merged text. |
```

The paragraph's first sentence, "#1481 at `d2040b335`", names the commit the framer read, so it stays.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:165-181` (`bd4ec54d8`) pairs `words[2::2]` with `words[3::2]`. It asserts equal lengths, a `--` on every name and on no value. A probe handed `union_step` four commands: `--stale-fails` at the end, `--stale-fails` at the start, `--stale-fails --committed` in the middle, and the old `${{ ... && '--stale-fails' || '' }}` expression. Each one raised `AssertionError` with "no value after it". `union_step` over the real `durations` job still returns `{"--parts": "parts", "--count": "4", "--out": ".test_durations"}`. Round 1's probe returned the three options for the trailing flag at `ef4732d70`, so the guard is shown red against the old body (executed, `## Probes`). The new body is a unit that no one had reviewed, and this round reviewed it as code. `zip(..., strict=True)` needs Python 3.10, and the floor is 3.12. The `strict` argument repeats the length assertion before it and costs nothing. The docstring states the refusal. The S3 row at `frame/design.md:61` now holds as written.

```seal
confirms: round-1#2
```
What holds: `frame/design.md:39` now says the release-note module's third case left with #1483 (`eec0bd040`), which this branch took at `3ed9a1bff`. `git log -S` in round 1 found that commit. `frame/design.md:44`, `frame/plan.md:60`, S2 at `:60`, S11 at `:69`, and `frame/questions.md` Q2 and Q3 each name the dispatch run 42996432567 at `25133f410` as the after reading's source. That matches `trail/phases/phase-5.md` and the run's `workflow_dispatch` event, which round 1 executed. No sentence in the four frame files still says the reading came from a pull request run (read, each file whole at `2815d6f7c`).

```seal
confirms: round-1#3
```
What holds: `skills/settle/SKILL.md:233-234` now reads "A settle's commit carries that trailer with no route chosen and is not one." `git grep -n -i 'durations refresh'` at the target finds the phrase only in this work item's records. It stands in `changelog.md:3`, *Scope* item 7 at `frame/design.md:43` and the `## Removes` row at `:158`, each of which describes the removal, and in round 1's record (executed). *Scope* item 7 and the new `## Removes` row name the clause, and *The settling session's procedure* is the heading step 5 stands under (read, `skills/settle/SKILL.md:185`, `:216`). The changelog sentence that `62a2fb4f1` added says the same thing. `tests/text/test_settle_reads_before_it_removes.py`, which reads the skill, passes (executed).

What matched: `frame/plan.md` *Judgments of the run* gains the row for the framer's fold, and its grounds match `1e0704773` (read). `pr.md` quotes no row that changed, and its four quotes still stand word for word at `frame/plan.md` rows A and *Judgments of the run* 2 to 4 (read). `gaps.md` and the five phase records did not change in the range. `chain_check.py` prints the same five notices at `frame/design.md:137` that round 1 weighed, and the range touches neither the `## Rule changes` entry nor the tests they name, so the weighing stands. This is the one fact this round carried rather than re-established.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub's workflow parser refuses a mapping key written twice. This round carried the row from round 1 and did not open it again | `gaps.md` `## Not done`, the first paragraph | the orchestrator, from GitHub's workflow syntax documentation or one dispatched run |
| A Windows shard restoring the union an ubuntu job saved (`frame/questions.md` Q1) | `.github/workflows/test.yml:128-134` | the orchestrator, from the restore step's log in the first pull request run after a push to `main` |
| The full suite, lint and format over the tree, which every record labels `unverified` | the whole tree | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_tmp_union_step_probe.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/text/test_settle_reads_before_it_removes.py -q -p no:xdist` in the round's clone at `2815d6f7c`. The probe has four bare-flag shapes, each expected to raise, and one read of the real `durations` job | 25 passed, 1 skipped, exit 0: every shape was refused, and the real command read as three options |
