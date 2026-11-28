# Review round 3: 1795841830-find-leftovers-before-a-round

```iadd
target: f2a0b1a8, fixes 3b5f604e..f2a0b1a8
```

Round 3 is a verifying round over the diff of the fixes, `3b5f604e..f2a0b1a8`. That diff holds the framer's fold `597e88cc`, the fix pass's commit `d5880bac` and the close blocks of `f2a0b1a8`. The range holds no merge of the base (`git log --merges --oneline 3b5f604e..f2a0b1a8` printed nothing, `executed`). Every coordinate below was opened at the target in a `git clone --no-local` under the round's scratch directory.

Stage 1 read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/phases/phase-2.md`, `trail/rounds/round-1.md` and `trail/rounds/round-2.md` whole at the target. `Record language` and `Commit and pull request language` are both English (`agentory/config.json`, `read`), so no `pr.<lang>.md` is owed and none stands. The range changes no `gaps.md`, `changelog.md` or `pr.md`. `agentory/threads/` holds this work item alone (`ls`, `executed`), so no other work item's frame is read against it.

Facts carried and not re-established: round 1's probe of `## Rule changes` through `skills/settle/scripts/rule_changes.py`, since the fold changes `frame/design.md` at lines 39, 40, 80 and 91 alone (`git diff 3b5f604e..f2a0b1a8`, `read`). Also carried is round 1's run of `tests/skills/test_range_read.py` and `tests/lib/test_optin.py` for the Python files, since the range changes no Python file. Round 2's probe of the passage check and the wrap check was run again at the target, not carried. Each verdict below is this round's own.

The orchestrator asked whether one statement with citations everywhere else holds across the frame and the built files. The close of each finding of round 2 holds for the sentence that finding named. The shape does not hold: the home's new sentence says every other statement cites it, and statements that restate it stand in the built files (finding 1) and in the frame (finding 2).

## Findings

### 1. The keep file's rule says every other sentence that says which keep files hold a line cites it, while the file set's row and the records' overview restate it, the overview as the fix rewrote it

```iadd
severity: should
location: `skills/verify/SKILL.md:75-76`, `skills/implement/SKILL.md:354`, `agentory/README.md:94-95`, `templates/setup/agentory-README.md:94-95`
evidence: read `skills/verify/SKILL.md:63-88`, `skills/verify/SKILL.md:113-120`, `skills/implement/SKILL.md:347-354`, `agentory/README.md:92-96`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/plan.md:71`, `agentory/threads/1795841830-find-leftovers-before-a-round/trail/rounds/round-2.md:51`; executed `git grep -n -o -i -e "prints at that phase's close" -e "to print at the phase's close" -e "to print at that phase's close" -e "search is to print" -e "search keeps" -- . ':!agentory/threads/1795841830-find-leftovers-before-a-round/trail'` and `git grep -n -e 'whose search prints it' -e "earlier phase's search prints" -e 'closes before the phase' -- agents skills docs templates agentory/README.md`
regression: round-2#1
```

Why it matters: the unit is the paragraph of `skills/verify/SKILL.md` *An absence claim is only as good as the search behind it* that `d5880bac` rewrote, together with the line of the records' overview that the same commit rewrote in both README files. The last row of `frame/plan.md` *Judgments of the run* and `frame/design.md:80` say which keep files hold a line is stated once and every other statement in the frame and the built files cites it. The fix wrote that universal into the home at `:75-76`, rewrote the overview line as a second statement of the fact, and left the file set's row stating it. So the defect came from how the fix listed the statements, not from what the frame says.

Two built statements say which keep file holds which lines and cite nothing for it. `skills/implement/SKILL.md:354`, the *Holds* cell of the keep files' row, reads "the lines, and the paths, the search of phase `<N>` prints at that phase's close". That is the home's sentence in other words, the condition included. The row's *Starts from* cell cites the section for "the form", and nothing in the row cites it for what the file holds. `agentory/README.md:94-95` and `templates/setup/agentory-README.md:94-95` read "the lines and paths phase N's search is to print, compared by diff". That restatement leaves out "at that phase's close", and round-1#2 turned on that condition: an earlier phase's search prints a line a later phase removes at the earlier phase's close, and not after. So the restatement had drifted from the home in the same commit that wrote the home's sentence saying no other sentence states the fact.

An agent acts on `:75-76`. The next change to what a keep file holds reads that sentence, trusts it, and edits the home alone. `:354` and the overview then state the old fact, which is the defect the run's decision was made against, in the form contract rule 19 names.

The method is a finding too. The close of round-2#1 says that `git grep -n -e 'whose search prints it' -e "earlier phase's search prints" -e 'closes before the phase' -- agents skills docs templates agentory/README.md` prints nothing, "so no built file restates the condition any longer". That search lists the words of the cross-phase restatement the fix removed. It cannot print a statement of the home's sentence itself, and it printed nothing again at the target. The first search on the `evidence:` line printed `:354` and both overview lines. The list was a sample handed back as a whole list.

The first search also printed `skills/verify/SKILL.md:73` and `:82`, which are the home and the paths sentence that says "the same way". It printed `agents/framer.md:41` and the last cell of `skills/implement/SKILL.md:354`, "for each phase whose search keeps a line", which say which phases have a keep file and cite the section. It also printed lines of the work item's records, which finding 2 takes. The search is a sample under contract rules 12 and 19, since a statement in other words escapes it.

In `skills/implement/SKILL.md:354`, replace the *Holds* cell "the lines, and the paths, the search of phase `<N>` prints at that phase's close" with:

```markdown
the lines, and the paths, that section says the keep file of phase `<N>` holds
```

In `agentory/README.md` and in `templates/setup/agentory-README.md`, replace lines 94-95 with these three lines, the same in both, so that `diff` of the two files still prints nothing. `frame/design.md` *Scope* item 13 still holds, since the lines name what each file holds in a few words. The fix pass runs `tests/lib/test_optin.py` and `tests/skills/test_agentic.py` again, since both open the template:

```text
    ├── frame/keep-N.txt, frame/keep-N-paths.txt   phase N's lines and paths
    │                      that `skills/verify/SKILL.md` in the plugin says
    │                      each holds, compared by diff
```

### 2. The frame says every other sentence of it that says which keep files hold a line cites *What it holds*, while *Scope* item 4 and three `## Rule changes` operations restate it, one with the "keeps" the fix took out of the overview

```iadd
severity: should
location: `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:80`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:42`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:120`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:124`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:134`
evidence: read `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:42`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:80`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:115-139`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/plan.md:71`, `agentory/threads/1795841830-find-leftovers-before-a-round/trail/rounds/round-2.md:51`; executed the first search on finding 1's `evidence:` line
regression: round-2#2
```

Why it matters: the unit is the sentence the fold `597e88cc` wrote into `frame/design.md:80`, *Data & interfaces* *The keep file*: "That sentence is the one statement of which keep files hold a line, and every other sentence of the frame and of the rule that says so cites it." The last row of `frame/plan.md` *Judgments of the run* has the fold state the fact once and every other statement in the frame cite it. The fold rewrote *Scope* items 1 and 2 and line 91 to cite it, and left *Scope* item 4 and three `## Rule changes` operations stating it. So the defect came from the fold's list of the frame's statements, not from the decision.

The first search on finding 1's `evidence:` line printed these frame lines:

- `:42`, *Scope* item 4, says the built row holds "the lines the search of phase `<N>` prints at that phase's close". It restates the fact, and it describes the cell finding 1 changes.
- `:120`, the `to:` of the first `add`, says the keep file holds "which lines the content search of phase N's *Verified by* cell prints at that phase's close". It restates the fact and cites the home in parentheses.
- `:124`, the `to:` of the second `add`, restates the fact for the paths file and cites nothing.
- `:134`, the `to:` of the *leave together* `change`, reads "Which lines and paths a phase's search keeps is that phase's keep file's." The close of round-2#1 changed the overview's "phase N's search keeps" because it "can be read as the kept lines alone" (`trail/rounds/round-2.md:51`). The same word stands here. Read that way, a line a later phase removes is not the earlier phase's keep file's, which is round-1#2's defect. The settle writes this `to:` into `docs/layout/the-record-layout.md`, the policy root, which outranks the skill it would then contradict.

The search printed other lines of the records that stand. `frame/design.md:18` is a *Grounding* row dated to the framer's commit. `frame/plan.md:21` and `:32` describe alternatives. The scenario at `frame/design.md:69` names a case's outcome under its own condition, "phase 1 and phase 2 that run the same search", and its *Verifiable how* cell sends the reader to *The keep file*. `changelog.md:3` and `:16` are release notes that people read, and `:3` names the line a later phase changes or removes. The search is a sample under contract rules 12 and 19.

The fix is the framer's fold, where the orchestrator routes it so. In `frame/design.md` *Scope* item 4, line 42, replace "holding the lines the search of phase `<N>` prints at that phase's close" with:

```markdown
holding what Scope item 1's home says a keep file holds
```

In `## Rule changes`, replace the `to:` lines at 120, 124 and 134 with these, in that order. Their `from:` lines do not change, so `apply_op` places them where round 1's probe placed them. The next round runs that probe again from round 1's `## Probes`, since the `to:` text changes:

```markdown
  to: | `frame/keep-<N>.txt` | the lines of the content search of phase N's *Verified by* cell that `skills/verify/SKILL.md` *An absence claim is only as good as the search behind it* says it holds, one line each as `git grep` prints it with no line number; `diff` compares it, and `agentic range` prints the lines a range changes in it |
  to: | `frame/keep-<N>-paths.txt` | the paths of the path search of phase N's *Verified by* cell that `skills/verify/SKILL.md` *An absence claim is only as good as the search behind it* says it holds, where the old spelling stands in a path |
  to: In which phases, by which approach and with which commit each closed is `frame/plan.md`'s. Which lines and paths a phase's keep files hold is `skills/verify/SKILL.md` *An absence claim is only as good as the search behind it*'s.
```

## Confirmations

```iadd
confirms: round-2#1
```
What holds: the builder's sentence at `skills/verify/SKILL.md:116-120` writes a rewritten kept line "into each keep file of its own phase or a later one that holds the line by the statement of what a keep file holds, above". The clause "that holds the line" fits a keep file and not a phase, so it bounds the rewriting phase's own keep file as well as a later one's. In round 2's case, phase 1 rewraps a line that only phase 2's search prints, and the sentence now puts the line into `frame/keep-2.txt` and not into `frame/keep-1.txt` (`read`). `frame/design.md:91` says the same and cites *What it holds*. `agents/framer.md:181-187` no longer restates the condition, and cites the home for which keep files hold "either line, a line a later phase removes among them" (`read`). `git grep -n -F "into that phase's" -- .` and `git grep -n -F "into its own keep file" -- .` print lines of `trail/rounds/round-1.md` and `trail/rounds/round-2.md` alone (`executed`). The passage check and the wrap check pass over the rewritten files at the target (`executed`, `## Probes`). The fix pass's whole set, `1341 passed` at `d5880bac`, was not run again. Finding 1 is in the sentence the fix added beside this one, and in the overview line.

```iadd
confirms: round-2#2
```
What holds: *Scope* item 2 at `frame/design.md:40` no longer restates the condition. A line the build removes or changes is named by a *Scope* item or a `## Removes` row, a line the design keeps is a line of a keep file, and which keep files hold either line "the rule cites from Scope item 1's home and does not restate". That matches `agents/framer.md:181-187` at the target (`read`). `git grep -n -F "each phase that closes before" -- .` prints lines of `trail/rounds/round-1.md` and `trail/rounds/round-2.md` alone (`executed`). The close's `location:` names `agents/framer.md:181-187`, which `597e88cc` does not touch (`git show --stat 597e88cc`, `executed`). Its `answer:` says the change to that file came in `d5880bac`, so the reader is not misled, and the round opens nothing for it. Finding 2 is in the frame's other statements of the fact.

What matched: `frame/plan.md`'s two new *Alternatives considered* rows (`:31`, `:32`) and its new *Judgments of the run* row (`:71`) state what the fold and the fix set out to do. The list in `:32`, `skills/verify/SKILL.md` lines 116 to 120, `frame/design.md` line 91 and *Scope* item 2, is what round 2's two findings name (`read`).

What matched: a phase whose search prints, at its close, only lines a later phase removes, as in a rename split into one phase per name family under one pattern. `skills/verify/SKILL.md:63-70` gives a keep file to "a content search that is to print lines the design keeps at its close", and `:77` sets the lines the design keeps beside the lines a later phase removes. Read alone, those two sentences could leave such a phase with no keep file. `agents/framer.md:183-186` sends the framer to the home for which keep files hold "a line a later phase removes", and the home's only case with no keep file is "a search that is to print no line" (`:69-70`). So a framer following the rule writes the earlier phase's keep file with those lines, which is what the scenario at `frame/design.md:69` asks (`read`). The round reads one outcome and opens no finding. A fold of finding 1 or 2 that touches the home's paragraph can still state the case in so many words.

What matched: `agentory/README.md` and `templates/setup/agentory-README.md` are byte-identical at the target (`diff` printed nothing, `executed`). `pr.md` is unchanged in the range, and `routing.md` *Why this way* and the `feat:` row of `frame/plan.md` *Judgments of the run* still hold each quoted sentence word for word (`read`). `changelog.md`'s first bullet says what the home says, a line a later phase changes or removes among the keep file's lines (`read`).

`chain_check.py --worktree`, run after this record was written, printed no notice at a line of `frame/design.md` naming a test pin or a copy (`executed`, `## Probes`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check. The suite stays `unverified` here, and the fix pass's whole *Review rounds 1..n* run was not repeated | `agentory/config.json` `Broad gate` | the orchestrator |
| Whether a framer, a crafter and an orchestrator follow the rules this work wrote in a later run. A round reads each rule for one reading and runs no agent | `gaps.md` `## Not verified`, its second and third rows | the repository owner, through the row this work adds to `agentory/follow-up.md` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/lib/test_optin.py -q`, in the scratch clone at `f2a0b1a8` | exit 0, 126 passed |
| `git log --merges --oneline 3b5f604e..f2a0b1a8` and `git show --stat 597e88cc d5880bac f2a0b1a8`, in the scratch clone | no merge; `597e88cc` changes `frame/design.md` and `frame/plan.md` alone, `d5880bac` changes the two README files, `agents/framer.md` and `skills/verify/SKILL.md`, and `f2a0b1a8` changes `trail/rounds/round-2.md` alone |
| finding 1's first search, at `f2a0b1a8` | the lines findings 1 and 2 name, and the lines each says stand |
| `git grep -n -e 'whose search prints it' -e "earlier phase's search prints" -e 'closes before the phase' -- agents skills docs templates agentory/README.md`, at `f2a0b1a8` | nothing, exit 1 |
| `git grep -n -F "into that phase's" -- .`, `git grep -n -F "into its own keep file" -- .` and `git grep -n -F "each phase that closes before" -- .`, at `f2a0b1a8` | lines of `trail/rounds/round-1.md` and `trail/rounds/round-2.md` alone |
| `diff templates/setup/agentory-README.md agentory/README.md`, at `f2a0b1a8` | nothing, exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.41.0 --root <the branch worktree> --worktree`, after this record was written, with the installed plugin's copy and with the tree's | exit 0 from each; each names findings 1 and 2 of this record as open for having no close block, and the missing gate record and inspection, and prints no notice at `frame/design.md` |
