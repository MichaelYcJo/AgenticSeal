# Review round 2: 1795841830-find-leftovers-before-a-round

```iadd
target: 3b5f604e, fixes 4c46218b..3b5f604e
```

Round 2 is a verifying round over the diff of the fixes, `4c46218b..3b5f604e`. That diff holds the framer's fold `3ddb9746`, the fix pass's commits `d9895cc9`, `7c4d45a6` and `6fb4f023`, and the close blocks of `3b5f604e`. The range holds no merge of the base (`git log --merges 4c46218b..3b5f604e` printed nothing, `executed`). Every coordinate below was opened at the target in a `git clone --no-local` under the round's scratch directory.

Stage 1 read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/phases/phase-2.md` and `trail/rounds/round-1.md` whole at the target. `Record language` and `Commit and pull request language` are both English (`agentory/config.json`, `read`), so no `pr.<lang>.md` is owed and none stands. The range changes no `gaps.md`. `agentory/threads/` holds this work item alone, so no other work item's frame is read against it.

Facts carried from round 1 and not re-established: round 1's probe of `## Rule changes` through `skills/settle/scripts/rule_changes.py`, since the range does not change that section (`git diff 4c46218b..3b5f604e` of `frame/design.md`, `read`). Also carried is round 1's run of `tests/skills/test_range_read.py` and `tests/lib/test_optin.py`, since the range changes no Python file. Each verdict below is this round's own.

## Findings

### 1. The builder's sentence writes a rewritten kept line into the rewriting phase's own keep file whether or not that phase's search prints it

```iadd
severity: should
location: `skills/verify/SKILL.md:116-120`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:91`
evidence: read `skills/verify/SKILL.md:63-88`, `skills/verify/SKILL.md:104-120`, `agents/framer.md:181-184`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:80`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:91`; executed `git grep -n -F "into that phase's" -- .` and `git grep -n -F "into its own keep file" -- .`
reopens: round-1#1
```

Why it matters: round 1's finding 1 said the builder's sentence, then at `skills/verify/SKILL.md:108-110`, held only where every phase runs the same search. The fix narrowed "every later phase's keep file" to "the keep file of each later phase whose search prints it" (`d9895cc9`). That relative clause attaches to "each later phase" alone. The first half of the sentence at `skills/verify/SKILL.md:117`, "the builder writes the line into that phase's keep file", still has no such condition. So the close leaves the defect standing in the unit the fixed commit changed.

The case is the one round 1 named. Phase 1 renames one name with search A. Phase 2 renames another with search B and keeps some lines of it. Phase 1 rewraps a paragraph that holds a line search B keeps. By `:116-118`, phase 1's builder writes the rewrapped line into `frame/keep-1.txt`. Search A does not print that line. So phase 1's content command prints it as a `>` line, which `:107-108` reads as "a kept line the phase changed or removed". The command cannot print nothing, and phase 1 cannot close as the rule says it closes. The same holds for "writes a line that holds a kept kind" where the kind is one phase 2 keeps. `agents/framer.md:183-184` states the same fact for a removed line, and it adds the condition: "where an earlier phase's search prints it". The two statements therefore disagree on whether a phase's search decides which keep files hold a line. Round 1's paste-ready snippet carried the same words, so the gap was in the round's own fix as well as in the pass.

The rest of finding 1's close holds. `skills/verify/SKILL.md:63-72` gives a phase at most one content search that keeps lines, with patterns joined into one `-P` pattern over the union of their pathspecs. A *Verifiable how* cell names the phase whose search it rests on. `:78-80` limits "a phase's own lines" to "where an earlier phase runs the same search". The path search of `:80-82` is named in the singular, "the path search", and the file name carries only `<N>`. So the round reads it as one path search per phase whose pathspecs cover each old spelling, and opens no finding for it.

The two searches on the `evidence:` line printed `skills/verify/SKILL.md:117`, `frame/design.md:91`, and `trail/rounds/round-1.md:50`, which is round 1's snippet and stands as that round's record. They are a sample under contract rules 12 and 19, since a statement in other words escapes them. `agents/framer.md:183-184` already holds the condition and needs no change.

In `skills/verify/SKILL.md`, replace lines 116-120, from "names. Where a phase" to "keep files the same way.":

```markdown
names. Where a phase rewrites a kept line, as a rewrap does, or writes a
line that holds a kept kind, the builder writes the line into the keep
file of each phase whose search prints it, from that phase on, in the same
commit. A kept line the tree no longer holds leaves those keep files the
same way.
```

In `frame/design.md` *Data & interfaces* *The keep file*, line 91, which is the framer's to fold where the orchestrator routes it so, replace "it writes the line into its own keep file and into the keep file of each later phase whose search prints it, in the same commit" with:

```markdown
it writes the line into the keep file of each phase whose search prints it, from its own phase on, in the same commit
```

```iadd
verdict: fixed d5880bac
location: `skills/verify/SKILL.md:72-78`, `agents/framer.md:181-187`, `agentory/README.md:94-95`, `templates/setup/agentory-README.md:94-95`
answer: The paste-ready snippet was not applied as written. The orchestrator's last row of `frame/plan.md` *Judgments of the run*, and the fold `597e88cc`, decide that which keep files hold a line is stated once and cited everywhere else, so the pass made the fix that way. In `skills/verify/SKILL.md` *An absence claim is only as good as the search behind it*, the sentence that says what a keep file holds ("The keep file holds each line the search is to print at the phase's close …") is now named as that one statement. The restatement after it, which carried the condition, now says that by it the lines the design keeps and the lines a later phase changes or removes "stand in a keep file alike". The builder's sentence writes a rewritten kept line "into each keep file of its own phase or a later one that holds the line by the statement of what a keep file holds, above". That covers its own phase only where its own search prints the line, as the fold's *Data & interfaces* *The keep file* line 91 now says. In `agents/framer.md` *A search you write into a cell is run before the cell states its result*, the clause "and where an earlier phase's search prints it, that phase's keep file holds it too" is gone. The next sentence says which keep files hold "either line, a line a later phase removes among them", and cites the home. In `agentory/README.md` and `templates/setup/agentory-README.md`, line 95 read "the lines and paths phase N's search keeps", which can be read as the kept lines alone. It now reads "phase N's search is to print, compared by diff", and `diff` of the two files prints nothing. `changelog.md` holds no sentence that states which keep files hold a line under a condition, so it is unchanged. The `evidence:` searches were run again at `d5880bac`. `git grep -n -F "into that phase's" -- .` and `git grep -n -F "into its own keep file" -- .` now print lines of `trail/rounds/round-1.md` and `trail/rounds/round-2.md` alone, which stand as those rounds' records. `git grep -n -e 'whose search prints it' -e "earlier phase's search prints" -e 'closes before the phase' -- agents skills docs templates agentory/README.md` prints nothing, so no built file restates the condition any longer. The set, from the *Verified by* cells of phases 1 and 2, whose paths the fix changes, was `bin/test tests/text tests/behaviour tests/lib/test_optin.py tests/skills/test_agentic.py -q`. `tests/lib/test_optin.py` and `tests/skills/test_agentic.py` open `templates/setup/agentory-README.md`, as phase 2 found. It printed `1341 passed, 10 skipped, 1 warning`, exit 0, at `d5880bac`. Both cells name `bin/test`, and every file of the set belongs to it, so no suite goes unnamed.
```

### 2. Scope item 2 of the frame puts a line a later phase removes in the keep file of every earlier phase, where the rule it builds puts it only in those whose search prints it

```iadd
severity: should
location: `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:40`
evidence: read `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:40`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:80`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/plan.md:45`, `agents/framer.md:181-184`, `skills/verify/SKILL.md:75-78`; executed `git grep -n -F "each phase that closes before" -- .`
regression: round-1#2
```

Why it matters: the unit is *Scope* item 2 of `frame/design.md`, which the framer's fold `3ddb9746` rewrote for round 1's finding 2. Phase 1's plan row (`frame/plan.md:45`) delivers Scope items 1 to 5. The frame's *Data & interfaces* *The keep file* (`frame/design.md:80`) says a line a later phase removes is a line of the keep file "of each phase whose search prints it and that closes before the phase that removes it". The fold wrote Scope item 2 as "each phase that closes before the phase that removes it". That drops the condition its own *Data & interfaces* paragraph carries, so the defect came from the fold restating the rule in a shorter form.

The target contradicts Scope item 2. `agents/framer.md:183-184` says "where an earlier phase's search prints it, that phase's keep file holds it too", and `skills/verify/SKILL.md:76-78` carries the full condition. In the case of round 1's finding 1, where phase 1 runs search A and phase 2 removes a line only search B prints, Scope item 2 puts that line into `frame/keep-1.txt`. Phase 1's command then prints it as a `>` line. The fix pass's close of round 1's finding 2 says its sentence narrows the snippet "as the fold of `3ddb9746` states it". That is true of `frame/design.md:80` and not of `:40`. A reader of the frame, the inspector among them, meets two rules for the same line. The finding takes `regression:` because the fold is part of the diff of the fixes the orchestrator named, and was made for round 1's finding 2. The close of that finding holds in the built files, so a `confirms:` line names it below as well.

The search on the `evidence:` line printed `frame/design.md:40` and `trail/rounds/round-1.md:91`, which is the fix pass's close quoting round 1's snippet and stands as that record. It is a sample under contract rules 12 and 19.

In `frame/design.md` *Scope* item 2, line 40, replace "and is also a line of the keep file of each phase that closes before the phase that removes it" with:

```markdown
and is also a line of the keep file of each phase whose search prints it and that closes before the phase that removes it
```

```iadd
verdict: fixed 597e88cc
location: `agents/framer.md:181-187`
answer: The framer's fold `597e88cc` took the orchestrator's route from the last row of `frame/plan.md` *Judgments of the run*. *Scope* item 2 of `frame/design.md` no longer restates the condition. A line the build removes is named by a *Scope* item or a `## Removes` row, a line the design keeps is a line of a keep file, and "which keep files hold either line, a line a later phase removes among them, the rule cites from Scope item 1's home and does not restate". The built sentence it describes matches since `d5880bac`. `agents/framer.md` *A search you write into a cell is run before the cell states its result* dropped its own restatement and cites `skills/verify/SKILL.md` *An absence claim is only as good as the search behind it*, the fix of finding 1 above. `git grep -n -F "each phase that closes before" -- .`, run again at `d5880bac`, prints `trail/rounds/round-1.md:91` and lines of `trail/rounds/round-2.md` alone. Each stands as that round's record, and `frame/design.md:40` is no longer among them.
```

## Confirmations

```iadd
confirms: round-1#2
```
What holds: `agents/framer.md:181-184` no longer reads "in one of two ways". A line the build removes, or changes so the search no longer matches it, is named by a *Scope* item or a `## Removes` row, and an earlier phase's keep file holds it where that phase's search prints it. A line the design keeps is a line of a keep file, and the sentence cites `skills/verify/SKILL.md` *An absence claim is only as good as the search behind it* for which keep files hold it. The cited section says at `:75-78` that the keep file holds "the lines a later phase changes or removes", with the condition that the phase's search prints the line. So a framer following its definition writes a line phase 2 renames into `frame/keep-1.txt` where phase 1 runs the same search, and phase 1's crafter does not read it as a leftover (`read`). The fix pass did not apply the snippet for `agents/framer.md` as written, and said why. The round read its own wording for one reading. "An earlier phase" is earlier than the phase that removes the line, and "that phase's keep file" is each such phase's file. No other reading stands next to the cited home. The claim that `tests/text/test_no_passage_is_pasted_into_a_second_file.py` refused the `d9895cc9` wording holds. With `agents/framer.md` and `skills/implement/SKILL.md` as `d9895cc9` holds them, that file failed on `test_no_pair_of_rule_documents_shares_a_run`, and `tests/behaviour/test_docs_line_wrap.py` failed on `skills/implement/SKILL.md`. Both files pass at the target (`executed`, `## Probes`). Finding 2 above is in the frame's Scope item 2, not in these files.

```iadd
confirms: round-1#3
```
What holds: `skills/implement/fix-pass.md:95-102` runs the *Review rounds 1..n* set with one command for each suite. The commands come from the *Verified by* cells of the phases whose paths the fixes changed. Where a file belongs to a suite none of those cells names, the pass runs it under that suite and names the command in the `answer:` of the close block of the finding whose fix changed it. `skills/implement/SKILL.md:203-210` names both sources: the *Phase boundary* row for a phase, and `fix-pass.md` for a fix pass. `agents/crafter.md:71-73`, step 9, sends a fix pass to `fix-pass.md` in place of step 7's run, so the rule for a missing suite now reaches a fix pass. A fix that changes a path no phase changed finds no cell, and every file of its set then falls under the missing-suite sentence, which runs it and names it. That is a reading with one outcome (`read`). `frame/design.md` *Scope* items 6 and 8, the scenario *A fix pass runs each file under the suite of its phase*, `frame/plan.md`'s rejected row for the last phase's commands, and `changelog.md:8` and `:17` all say the same (`read`). The fix pass's account of its own set, `2 failed, 965 passed` at `d9895cc9` and green at `7c4d45a6` and `6fb4f023`, was not re-run whole. The two refusals it names were reproduced (`## Probes`).

What matched: the fold `3ddb9746`. `frame/design.md` *Data & interfaces* *The keep file* (`:80`), *Scope* items 1, 6 and 8, the three new scenario rows, `frame/plan.md`'s four new *Alternatives considered* rows and its new *Judgments of the run* row, and `frame/questions.md`'s first line state what `skills/verify/SKILL.md:63-88` and `skills/implement/fix-pass.md:95-102` do at the target (`read`). The exceptions are finding 1's sentence at `frame/design.md:91` and finding 2's at `:40`. The fold marked Q2 answered by round 1's probe, which is what round 1 recorded (`read`).

What matched: `changelog.md`. Its first bullet now says a phase has at most one search that keeps lines, with patterns joined, and that a keep file holds a line a later phase changes or removes, which `skills/verify/SKILL.md:63-78` says (`read`). The bullet on suites and the second process row now say a fix pass takes its commands from the cells of the phases whose paths its fixes change, which `skills/implement/fix-pass.md:95-102` says (`read`).

What matched: `pr.md` is unchanged in the range, and the two records it quotes, `routing.md` *Why this way* and `frame/plan.md` *Judgments of the run* row of `feat:`, still hold each quoted sentence word for word at the target (`read`).

What matched: round 1's listing commands for finding 1, run again at the target, print the lines the fix pass's close names. `agents/framer.md:41-42`, `:114`, `skills/implement/SKILL.md:354`, `templates/setup/agentory-README.md:94-95`, `agentory/README.md:94-95` and `lib/optin.py:55` each name one search per phase, which the rule now states (`executed`).

`chain_check.py --worktree`, run after this record was written, printed no notice at a line of `frame/design.md` naming a test pin or a copy (`executed`, `## Probes`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check. The suite stays `unverified` here, and the fix pass's whole *Review rounds 1..n* run was not repeated | `agentory/config.json` `Broad gate` | the orchestrator |
| Whether a framer, a crafter and an orchestrator follow the rules this work wrote in a later run. A round reads each rule for one reading and runs no agent | `gaps.md` `## Not verified`, its second and third rows | the repository owner, through the row this work adds to `agentory/follow-up.md` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py -q`, in the scratch clone at `3b5f604e` | exit 0, 58 passed |
| `git checkout d9895cc9 -- agents/framer.md skills/implement/SKILL.md`, the same `bin/test` command, then `git checkout HEAD --` of both files, in the scratch clone | exit 1, 2 failed and 56 passed: `test_no_pair_of_rule_documents_shares_a_run` and `test_prose_stays_within_the_wrap_limit[skills/implement/SKILL.md]`; `git status --short` printed nothing after the restore |
| `git grep -n -e "keep-<N>" -e "keep-N" -e "keep file" -- agents skills templates agentory/README.md docs lib` and `git grep -n -i -e "search of phase" -e "phase's search" -e "phase N's search" -e "a phase's search" -e "phase's keep file" -- . ':!agentory/threads/1795841830-find-leftovers-before-a-round'`, at `3b5f604e` | the lines the confirmation of round 1's listing names, and `agents/framer.md:183-184` and `skills/verify/SKILL.md:80` |
| `git grep -n -F "into that phase's" -- .`, `git grep -n -F "into its own keep file" -- .` and `git grep -n -F "each phase that closes before" -- .`, at `3b5f604e` | the lines findings 1 and 2 name |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.41.0 --root <the branch worktree> --worktree`, after this record was written, with the installed plugin's copy and with the tree's | exit 0 from each; each names findings 1 and 2 of this record as open for having no close block, and the missing gate record and inspection, and prints no notice at `frame/design.md` |
