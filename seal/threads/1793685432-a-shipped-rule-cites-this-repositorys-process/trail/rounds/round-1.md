# Review round 1: 1793685432-a-shipped-rule-cites-this-repositorys-process

```seal
target: ac205c11b against origin/release/v0.30.1
```

The target is `git diff 0c68b9933...ac205c11b`, read in a `git clone --no-local` of the repository at `ac205c11b`. This is the first round, so no fact was carried from an earlier one; every coordinate below was opened this round. `seal/parity.md` is not declared, so no `original:` line is owed. The request was read whole with `gh issue view 1234 --json title,body,comments`: the body and its two comments (executed).

## Findings

### 1. The never-rebase rule's new home states only the conflict case, and the checklist says it states the rule

```seal
severity: must
location: `skills/code-review/orchestration.md:285-287`, `docs/releasing/release-checklist.md:20-22`
evidence: executed `git show 0c68b9933:docs/releasing/release-checklist.md`, `git diff 0c68b9933...ac205c11b -- skills/code-review/orchestration.md docs/releasing/release-checklist.md`, `git grep -n -i rebase -- skills agents templates hooks bin docs`
```

Why it matters: the issue's *Rule change* paragraph quotes the rule that moves, "Never rebase a work item's branch, for any reason", and says "the home gains the rule". Its *Scope* asks that the rule a skill cites from a process document stand in the skill that applies it. The owner's second comment changes how `docs/` is edited, not what moves. At the base, the skill's reason sentence cited `docs/releasing/release-checklist.md` *0. Before starting*. So an orchestrator in another repository reached the box's rule, which covers any rebase. After this diff that rule stands only in the checklist, which ships as this repository's release-day list.

The frame claims, at `frame/design.md:28` (*Scope*, item 1), that the skill "already states the rule and its reason". The plan claims the same at `frame/plan.md:21`. The skill at `skills/code-review/orchestration.md:285-287` states a narrower rule: "A conflict with the base is integrated by merging the base into the branch, never by a rebase." Its scope is how a conflict is integrated. A rebase made for another reason is outside it, such as one made to pick up something the base holds when nothing conflicts. The checklist box's first half names exactly that case: "only when the branch needs something the release branch holds". Its reason sentence, "A rebase orphans the commits every round record names", does apply to every rebase. But the sentence that states the rule does not. The new line at `docs/releasing/release-checklist.md:21-22` tells its reader that the skill "states the rule and its reason". It states the reason and only part of the rule. That fails A4 (`frame/design.md` *User scenarios & acceptance*): the base text's "for any reason" is lost from the shipped skill's reach.

The fix keeps the sentence `tests/text/test_the_rules_have_one_owner.py` pins at line 329, "A conflict with the base is integrated by merging the base into the branch, never by a rebase.", and widens the reason sentence after it:

```markdown
**A conflict with the base is integrated by merging the base into the
branch, never by a rebase.** A work item's branch is not rebased for any
reason, because a rebase orphans the commits every round record names on
its `target:` line. The orchestrator merges once, after the branch whose
changes conflict with this one has landed on the base. Where the merge
```

The rest of that paragraph stays as it reads, re-wrapped to the line width `tests/behaviour/test_docs_line_wrap.py` holds. Once the skill says it, the checklist line at `docs/releasing/release-checklist.md:21-22` is true and stays as it is.

This snippet does not reach every statement of the fact. The fix pass owes these too:

- The fragment's `### Changed` entry at `changelog.md:3` says the skill "already said a conflict is integrated by a merge, never a rebase". After the fix it also says the skill now states that a branch is not rebased for any reason (`docs/layout/the-record-layout.md` *A commit after the build brings its changelog fragment along*).
- The process row at `changelog.md:10` calls the skill "the one home of the never-rebase rule". That is true after the fix. The row's *Why* cell, "The skill already stated the rule and its reason", is not. It becomes: the skill stated the conflict case and the reason, and now states the rule whole.
- `frame/design.md:28`, `frame/design.md:66` and `frame/plan.md:21` say the skill already states the rule. The frame is the orchestrator's to fold, with a `frame/plan.md` *Judgments of the run* row (`skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*). The crafter's fix pass does not edit it.
- `skills/implement/SKILL.md:304-307` says "a rebase during the work does the same earlier and more quietly" and "the party that rebases the branch re-reads the column after the rebase". That sentence was already at odds with the checklist box at the base, and this diff does not touch it. Once a shipped skill says a branch is not rebased for any reason, it reads as the remedy for a rebase made against the rule. The fix pass judges whether it stands as that remedy or is rewritten to say so. Either way, it says which in its answer.

```seal
verdict: fixed 620c24798
answer: The finding holds. The paste-ready snippet is applied word for word in `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*. The pinned bold sentence is unchanged, the sentence after it now says a work item's branch is not rebased for any reason, and the rest of the paragraph is re-wrapped with no word changed. The checklist line at `docs/releasing/release-checklist.md:20-22` is left as it is, since it is now true. The remedy sentence in `skills/implement/SKILL.md` *3. The SDD file set* is rewritten rather than kept: under a rule that no party rebases a work item's branch, "the party that rebases the branch re-reads the column after the rebase" reads as a rebase the workflow allows. It now says a rebase would orphan the Status column's commits earlier and more quietly, and the round records' commits as well, so a work item's branch is never rebased, and it cites the code-review section. That wording is the fix pass's own, since the round gave no snippet for it. The `### Changed` entry at `changelog.md:3` no longer says the skill already stated the rule, and it names both skill changes. The process row at `changelog.md:10` is left to the orchestrator, as the spawn asks, and the frame rows were folded at 10e3ba4e4. The other statements were found with `git grep -n -i rebase` over `skills agents templates hooks bin docs`, each hit read. The rest describe how a hook or the stamp behaves during or after a rebase, and none says the workflow allows one. So they stand.
```

### 2. The phase record says the fold rule was reworded, and the sentences moved verbatim

```seal
severity: should
location: `seal/threads/1793685432-a-shipped-rule-cites-this-repositorys-process/trail/phases/phase-1.md:9`, `seal/threads/1793685432-a-shipped-rule-cites-this-repositorys-process/trail/phases/phase-1.md:11`
evidence: executed `git diff 0c68b9933...ac205c11b -- skills/implement/orchestration.md docs/releasing/issues-and-milestones.md skills/code-review/orchestration.md`
```

Why it matters: the phase record is the account the sealer reads against the tree, and `seal pr-body` copies the records into the pull request body. It claims, at `trail/phases/phase-1.md:9`, that the fold rule's three reasons were "reworded from the removed paragraph so no 15-word run stands in both files". The diff shows the move was verbatim. "and the comment that carried it records why", "A body that contradicts a comment leaves the reader to work out which is current, and a block of updates written above the old text leaves two versions to choose between" and "GitHub keeps the body's edit history, so rewriting it loses nothing" stand in `skills/implement/orchestration.md:62-66` word for word as at the base in `docs/releasing/issues-and-milestones.md`. This round checked that with a whitespace-normalised substring test of both texts (executed). A3 holds because the source paragraph was removed in the same commit, as `frame/design.md` *Grounding*, the row on `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, says it would. It does not hold because of any rewording. There is a second claim in the same account, at `trail/phases/phase-1.md:11`: "the next three lines of that paragraph were re-wrapped". The diff re-wraps four lines after the two that carried the citation. Base lines 289 to 292 become lines 288 to 291. "No word changed there" holds.

```markdown
the sentence that folds a decision into the issue body keeps its words and
gains the rule and its three reasons, moved word for word from the removed
paragraph; no 15-word run stands in both files because that paragraph is
removed in the same commit (`frame/design.md` A3).
```

```markdown
so the next four lines of that paragraph were re-wrapped.
```

These two snippets replace the clauses they name at lines 9 and 11 of the phase record. Nothing else in the record states either fact (executed: `grep -n -E 'reworded|re-wrapped'` over the work item's records).

```seal
verdict: fixed 620c24798
answer: The finding holds. Both snippets replace the clauses they name in `trail/phases/phase-1.md`, word for word. The line-9 clause now says the fold rule's sentences moved word for word, and that A3 holds because the source paragraph is removed in the same commit. The line-11 clause now says four lines were re-wrapped. The crafter's phase-1 hand-back made the same three-lines claim, and this answer corrects it.
```

## Confirmations

```seal
confirms: none
```
What matched: A1. The command `frame/design.md` A1 gives lists exactly `skills/verify/orchestration.md:233` and `skills/verify/scripts/unverified_check.py:112` at `ac205c11b`. At `0c68b9933` it lists those two and the three citations this work removes. No shipped tree names a process document in words alone: `git grep -n -i -E 'checklist|release day|release-day'` over `skills agents templates hooks bin evals` returns nothing (executed).

```seal
confirms: none
```
What matched: A6 and the #1277 decision. `git diff 0c68b9933 -- skills docs | grep -c '^+check: none reader'` prints 0. The removed paragraph's `check: none reader: the framer at every frame` line goes with it, and no moved rule gains a check line (executed).

```seal
confirms: none
```
What matched: A2, A3 and A5. One `bin/test -q` command in the clone ran ten modules and exited 0, with 358 passed and 2 skipped (executed). The modules were the seven `frame/plan.md` row 1 names, plus `tests/text/test_the_rules_claude_md_names_have_one_home.py` and `tests/text/test_broad_gate_rule.py`, which read *Orchestrator: the order inside a ticket*, and `tests/behaviour/test_chain_hooks_hardening.py`, the case the crafter's first run failed. Claimed (`trail/phases/phase-1.md:13`): 40 modules exited 1 on the missing `gaps.md`, then 8 exited 0 with 177 passed. This round re-ran neither count, and its own run is narrow, not the broad gate.

```seal
confirms: none
```
What matched: A4 for the fold rule. Each sentence of the base paragraph at `0c68b9933:docs/releasing/issues-and-milestones.md` (*An issue is its body and its comments together*) has a home at HEAD. The rule and its three reasons stand at `skills/implement/orchestration.md:61-66`. The framer being handed the body as folded and a line naming the comments stands at `skills/implement/orchestration.md:66-69`. "No framer asks whether a comment changes the request" stands at `agents/framer.md:80` as "No row of `frame/questions.md` asks whether a comment changes the request". The later decision folded into the frame stands at `skills/implement/orchestration.md:51-60`. The new sentence at `docs/releasing/issues-and-milestones.md:320-322` cites that section, and the citation resolves (read; resolution executed in the narrow run).

```seal
confirms: none
```
What matched: A4 for when the settle runs. The base's first paragraph of *2b* said the settle runs when the owner calls it, not at every release, and that the work items wait on disk for the settle the owner calls. `skills/settle/SKILL.md:68-70` says both, and keeps "It is invoked, never triggered". *2b* at `docs/releasing/release-checklist.md:33-34` keeps the day's instruction, that a release whose owner has not called the settle skips the step, and cites the skill section. No other file states the timing rule: `git grep -n -i -E 'not at every release|wait on disk|owner calls'` outside `seal/threads/` lists only `skills/settle/SKILL.md:68` (executed).

```seal
confirms: none
```
What matched: the frame's census of the `.github/` lines and of old spellings. The only `.github/` lines naming *2b* are in `.github/scripts/finding_counts.py`, at lines 2, 36 and 177, and they cite the four numbers, which stay in *2b* (executed: `git grep -n -E 2b -- .github`). Each removed spelling the phase record names returns nothing outside `seal/threads/` (executed: `git grep -n -F` on each). The two remaining hits for the citation forms are `docs/releasing/issues-and-milestones.md:213` and `docs/layout/the-record-layout.md:124`. They cite *0. Before starting* and *2b* for acts that stay there, so they do not stand on a moved rule (read).

```seal
confirms: none
```
What matched: the diff changes no test, script, hook or template (executed: `git diff 0c68b9933 --stat -- tests` is empty, and `git diff --stat` lists only the five prose files and the work item's records). So no new test is read against its group. The chain check over the worktree printed no notice at a line of `frame/design.md` naming a test pin or a copy (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. The crafter labels them `unverified`, and the label is honest: `gaps.md:8` names the orchestrator | `seal/config.md` *Broad gate* | the orchestrator, at the broad gate after the rounds settle |
| Whether the test modules that name only another file of `skills/code-review/`, `skills/implement/`, `skills/settle/` or `docs/releasing/` glob a directory this diff edits. `gaps.md:9` says none was read or run. This round did not read them either | `gaps.md:9` | the orchestrator, at the broad gate |
| Whether the merge of `release/v0.30.1` after PR #1320 lands resolves a conflict outside the work item's records. The spawn puts it outside this round's target | `frame/questions.md` Q1 | the orchestrator, at that merge, under `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the ten modules named under *Confirmations*, in the round's clone at `ac205c11b` | exit 0, 358 passed, 2 skipped |
| The A1 command at `ac205c11b` and at `0c68b9933` | two lines at HEAD; five at the base |
| `git diff 0c68b9933 -- skills docs \| grep -c '^+check: none reader'` | 0 |
| A whitespace-normalised substring test of the fold rule's sentences, against `git show 0c68b9933:docs/releasing/issues-and-milestones.md` and `skills/implement/orchestration.md` at HEAD | each sentence is found in both, word for word |
| `git grep -n -i rebase -- skills agents templates hooks bin docs` | the rule that covers any rebase stands only at `docs/releasing/release-checklist.md:20`; the skill at `skills/code-review/orchestration.md:285` states the conflict case; `skills/implement/SKILL.md:304-307` describes a rebase during the work |
