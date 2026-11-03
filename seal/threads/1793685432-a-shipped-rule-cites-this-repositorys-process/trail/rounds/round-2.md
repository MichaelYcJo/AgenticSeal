# Review round 2: 1793685432-a-shipped-rule-cites-this-repositorys-process

```seal
target: 9b0d988cd, fixes ac205c11b..9b0d988cd
```

This is a verifying round. Its target is the diff of the last fixes, `git diff ac205c11b 9b0d988cd`, read in a `git clone --no-local` of the repository at `9b0d988cd`. The base is `origin/release/v0.30.1` at `0c68b9933` (executed: `git rev-parse` in the clone). The fix diff changes `skills/code-review/orchestration.md`, `skills/implement/SKILL.md` and the work item's records. `seal/parity.md` is not declared (executed: `ls`), so no `original:` line is owed. The request was read whole with `gh issue view 1234 --json body,comments`: the body and its two comments (executed).

Carried from round 1 and not re-established, because the fix diff does not touch them: the `.github/` census, the A4 reads for the fold rule and for when the settle runs, and the base text of the never-rebase box, which round 1's finding 1 quotes. The A1 and A6 commands were run again at HEAD (*Confirmations*).

## Findings

### 1. The frame and the closing memo still name five edited files, and no `## Removes` row names the instruction the fix took out of `skills/implement/SKILL.md`

```seal
severity: should
location: `seal/threads/1793685432-a-shipped-rule-cites-this-repositorys-process/frame/design.md:55`, `seal/threads/1793685432-a-shipped-rule-cites-this-repositorys-process/frame/design.md:62-71`, `seal/threads/1793685432-a-shipped-rule-cites-this-repositorys-process/frame/plan.md:5-11`, `seal/threads/1793685432-a-shipped-rule-cites-this-repositorys-process/gaps.md:9`
evidence: executed `git diff ac205c11b 9b0d988cd -- skills/ seal/`, `git show 0c68b9933:skills/implement/SKILL.md`, `grep -n -E 'five|six' frame/design.md frame/plan.md gaps.md`
regression: round-1#1
```

Why it matters: the unit is the paragraph at `skills/implement/SKILL.md:303-309`, which the fix of round 1's finding 1 rewrote at `620c24798`. The frame's *Scope* item 1 at `frame/design.md:28`, as folded at `10e3ba4e4`, says that sentence "is brought in line with that rule"; the fix did that by taking out the base instruction "**the party that rebases the branch re-reads the column after the rebase**" (`0c68b9933:skills/implement/SKILL.md:306-307`); the fold widened *Scope* item 1 alone and left the frame's other statements of what the work edits and removes as they read before the fix.

So four statements in the records are now false or short:

- `frame/design.md:55` (*Data & interfaces*) says "The edits are prose in" five files and leaves out `skills/implement/SKILL.md`.
- `frame/design.md:62-71` (*Removes*) has six rows and none for the removed instruction. `agents/framer.md` *A removal is named once, at the frame* says the review reads each row against the diff, and that an unnamed removal reaches the reader only as a divergence after the fact. `agents/sealer.md` step 4 reads the design's scope and `Removes` against the diff.
- `frame/plan.md:5` says "The work edits prose in five files at the base", and the list at `frame/plan.md:7-11` has no line for `skills/implement/SKILL.md`.
- `gaps.md:9` names "the five edited paths".

The changelog fragment does name the change, at `changelog.md:3` and `changelog.md:10`, so only the frame and the memo diverge. The sealer reads the frame, the memo and the diff against each other, and this round found the difference from the diff alone.

The frame is the orchestrator's to fold, as round 1 left `frame/design.md:28` to it. `gaps.md` is the crafter's memo. For `frame/design.md:55`:

```markdown
None. No script, hook, check, template or record form changes. The edits are prose in `skills/code-review/orchestration.md`, `skills/implement/orchestration.md`, `skills/implement/SKILL.md`, `skills/settle/SKILL.md`, `docs/releasing/release-checklist.md` and `docs/releasing/issues-and-milestones.md`.
```

A seventh row at the end of the table under `frame/design.md:64`:

```markdown
| The instruction "the party that rebases the branch re-reads the column after the rebase" | `skills/implement/SKILL.md` *3. The SDD file set* | A work item's branch is not rebased for any reason, so no party re-reads the column after a rebase. The paragraph now says a rebase would orphan the Status column's commits and the round records' commits, and cites `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* |
```

For `frame/plan.md:5`, and a sixth line after `frame/plan.md:10`:

```markdown
The work edits prose in six files at the base `0c68b9933`. Every line number below was read there.
```

```markdown
- `skills/implement/SKILL.md:303-307`, under *3. The SDD file set*, the sentence on a rebase during the work. Round 1's finding 1 added it (*Judgments of the run*).
```

For `gaps.md:9`, the words "not one of the five edited paths" become "not one of the six edited paths".

This snippet does not reach `frame/plan.md:32`, which says phase 1 delivers "the six rows of its `## Removes`". That cell is phase 1's, and phase 1 delivered those six at `8b14bdbb7`. The seventh row is the fix pass's, which the *Judgments of the run* row at `frame/plan.md:42` records, so the cell stays as it reads.

```seal
verdict: fixed 7867f45cf
answer: The finding holds. The orchestrator folded the frame's part at 9fd639b5f: `frame/design.md` *Data & interfaces* names six files, `## Removes` has a seventh row for the removed instruction, and `frame/plan.md` *Technical context* says six files and lists `skills/implement/SKILL.md:303-307`. The fix pass did not edit the frame. At 7867f45cf the fix pass changed "not one of the five edited paths" in `gaps.md:9` to "not one of the six edited paths", word for word as this record gives it. The row is true at six: round 1's fix pass ran every `tests/*.py` that `git grep -l -F` lists for `skills/implement/SKILL.md`. The pass touched the work item's records alone, so it owes no verifying round.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the never-rebase rule's home now states the rule whole. `skills/code-review/orchestration.md:285-289` carries round 1's snippet word for word. The pinned bold sentence is unchanged, and the next sentence reads "A work item's branch is not rebased for any reason, because a rebase orphans the commits every round record names on its `target:` line" (executed: `git diff ac205c11b 9b0d988cd -- skills/`). The checklist line at `docs/releasing/release-checklist.md:20-22` says the skill "states the rule and its reason", and that is now true (read). The base box said "Never rebase a work item's branch, for any reason" and gave the orphaned `target:` commits as the reason. The skill now says both, so A4 holds for this rule (read, against round 1's quote of the base box). The close claimed that `changelog.md:3` no longer says the skill "already" stated the rule and that it names both skill changes. `changelog.md:3` does both. The close also claimed that the process row at `changelog.md:10` was left to the orchestrator. It was rewritten at `9b0d988cd`: its *Change* cell says the rule was widened to every rebase, and its *Why* cell says the skill stated the conflict case only (read). The frame's *Scope* item 1 and the chosen approach's verdict were folded at `10e3ba4e4`, with a *Judgments of the run* row at `frame/plan.md:42` (read). The pinned sentence and the new citation stay green in the narrow run below (executed). What the fold left unchanged in the frame is finding 1 of this round.

```seal
confirms: round-1#2
```
What holds: `trail/phases/phase-1.md:9` and `trail/phases/phase-1.md:11` carry round 1's two snippets word for word. Line 9 now says the fold rule's sentences moved word for word and that A3 holds because the source paragraph is removed in the same commit. Line 11 now says four lines were re-wrapped (executed: `git show 620c24798 -- seal/`). No other line of the record changed.

```seal
confirms: none
```
What matched: the new sentence in `skills/implement/SKILL.md:303-309` holds together with its paragraph and reads as no permission. The crafter claimed that the remedy sentence was rewritten, not kept. At the base, `0c68b9933:skills/implement/SKILL.md:303-307` told "the party that rebases the branch" to re-read the column. That instruction is gone. The paragraph now says that a squash stops the Status column's commits resolving at the merge, and that this is tolerable because nothing measures from the column. It then says a rebase would orphan those commits earlier and more quietly, and would orphan the round records' commits too, so a work item's branch is never rebased. The "So" does not rest on the harm the paragraph calls tolerable alone: the round records' commits are the added ground, and the cited section states that ground as the rule's reason. "Is never rebased" says the same as the home's "is not rebased for any reason". The clause on the round records restates the home's reason in a dozen words and cites the home, so this round judges it a pointer and not a second home. `tests/text/test_no_passage_is_pasted_into_a_second_file.py` finds no 15-word run shared by the two sentences (executed, in the narrow run). The citation resolves, as `tests/behaviour/test_a_cited_section_stands_in_its_file.py` checks (executed, same run). No case pinned the removed instruction or the moved sentence "Nothing measures from the column" (executed: `git grep -n -E` over `tests evals` on "rebases the branch", "re-reads the column", "Nothing measures from the column", "more quietly" and "rebase during the work", no hit).

```seal
confirms: none
```
What matched: no other shipped sentence contradicts "a work item's branch is not rebased for any reason". The method was word searches, so the list is a sample. The words were "rebase" in every spelling, "orphan", and the history-rewriting forms "pull --rebase", "rebase-merge", "--onto", "force-push", "push --force", "force-with-lease", "--amend" and "rewrite history", over `skills agents templates hooks bin docs evals` (executed: `git grep -n -i` on each). Every "rebase" hit outside the two edited sentences describes a state a person or a platform can reach. In `docs/checks/the-routing-check.md:28-51` and `hooks/lib/routing.py:305-361` a paused rebase names the branch for the edit gate. In `docs/checks/the-routing-check.md:129` and `skills/code-review/scripts/chain_check.py:1809` a person's rebase, or GitHub's rebase-merge, carries a trailer its committer did not write. In `docs/checks/the-stamp.md:64`, `:112` and `:123` the stamp sees a verdict whose commit a rebase moved. None tells a party to rebase a work item's branch, or how to carry on after one. The "orphan" hits outside the two edited files are about the squash at the merge. The `--amend` hits are in eval fixtures that build seeded repositories (`evals/scripts/seed_defects.py:390` and four `evals/behaviour/proofer/seeded-*/scaffold.sh:20` lines), and the force-push hit at `docs/releasing/branch-and-release.md:321` is not about a work item's branch (read). A sentence that implies a rebase without using any of these words falls outside the sample, and that domain is unbounded.

```seal
confirms: none
```
What matched: A1 and A6 at HEAD, and the edited sections' cases. The A1 command lists exactly `skills/verify/orchestration.md:233` and `skills/verify/scripts/unverified_check.py:112`. The A6 command prints 0, so no moved rule gained a `check: none reader:` line, as the owner's decision for this release asks (executed). One `bin/test -q` command in the clone ran the 19 test modules that `git grep -l -F` lists for `skills/implement/SKILL.md` or `skills/code-review/orchestration.md`, plus `tests/behaviour/test_chain_hooks_hardening.py`. It exited 0, with 582 passed (executed). Claimed by the crafter: one 21-module run, exit 0, 594 passed. This round did not re-run that count, and its own run is narrow, not the broad gate.

```seal
confirms: none
```
What matched: the fix diff adds no test (executed: `git diff ac205c11b 9b0d988cd --stat -- tests` is empty), so there is no new test to read against its group. The diff leaves the `## Rule changes` no-change block of `frame/design.md` as it was, and the issue's *Done when* holds at HEAD: no document under `skills/` cites a process document for a rule an agent applies in another repository (read, with the A1 run).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. The crafter labels them `unverified` and names the orchestrator at `gaps.md:8`, and the label is honest | `seal/config.md` *Broad gate* | the orchestrator, at the broad gate after the rounds settle |
| The crafter's fix-pass run of 21 modules, exit 0, 594 passed. It is the crafter's claim, and this round ran its own narrow selection instead | the crafter's fix-pass hand-back | the orchestrator, at the broad gate |
| Whether the merge of `release/v0.30.1` after PR #1320 lands resolves a conflict outside the work item's records. Carried from round 1, and outside this round's target | `frame/questions.md` Q1 | the orchestrator, at that merge, under `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the 19 modules `git grep -l -F` lists for the two edited skill files, plus `tests/behaviour/test_chain_hooks_hardening.py`, in the round's clone at `9b0d988cd` | exit 0, 582 passed |
| The A1 command at `9b0d988cd` | two lines, `skills/verify/orchestration.md:233` and `skills/verify/scripts/unverified_check.py:112` |
| `git diff 0c68b9933 -- skills docs \| grep -c '^+check: none reader'` | 0 |
| `git grep -n -i` on "rebase", "orphan" and the history-rewriting forms over `skills agents templates hooks bin docs evals` | no hit tells a party to rebase a work item's branch or how to carry on after one |
| `git grep -n -E` over `tests evals` on the removed and moved sentences of `skills/implement/SKILL.md` | no hit |
