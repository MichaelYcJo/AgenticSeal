# Review round 2: 1795590951-a-fix-builds-a-unit-no-frame-designed

```seal
target: fc096778b, fixes 8562ea70f..fc096778b
```

This is the verifying round. The range read is `8562ea70f..fc096778b`, read in a `git clone --no-local` at the target. It holds seven commits after round 1's record: `6ee02726f`, `d154f13fd`, `0fd12e5ba`, `474d41883`, `6d924dc05`, `a4dbb719e` and `fc096778b`. The code reviewed is the fix diff: `skills/implement/fix-pass.md`, `skills/implement/orchestration.md`, `skills/implement/fold-and-reframe.md`, `skills/implement/SKILL.md`, `skills/code-review/orchestration.md`, `seal/follow-up.md` and one docstring in `tests/text/test_the_rules_have_one_owner.py`. No unit of the fix diff is new by `skills/implement/fix-pass.md:52-69`: every change is a sentence added to a section or a row the tree held, and the test change is a docstring. No case is new, so no test is read against its group.

The work item's records that state the present were each read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`, with `trail/phases/phase-1.md` and `trail/rounds/round-1.md`. No `pr.<lang>.md` stands, since `Commit and pull request language` is English. `seal/parity.json` is not declared.

Carried from round 1 and not re-derived: the coordinates of the sections each finding named; the G11 counts, which this round compared against `seal/follow-up.md:46` and did not measure again; and five rows of `trail/phases/phase-1.md`'s seen-red table. Re-derived here: every verdict below, key `"33 "`'s link (*Probes*), and the passage check that round 1's second *Not judged* row sent to the broad gate, which passed in this round's narrow run.

The orchestrator asked whether its judgment not to fold two places of `frame/design.md` holds. It holds for three of them and not for the fourth, which finding 2 names. The grounds follow.

- The home of the narrowing, `skills/implement/orchestration.md:83-89`, has a fold whose source is a fix remove or narrow the frame sentence HEAD contradicts and write no account of what was built. The orchestrator's own reading, `:105-108`, folds every statement HEAD contradicts. A sentence the target does not contradict owes no fold, and a fold that only adds what the fix built is the restatement this work removes.
- Finding 5 and finding 7 went to the fix pass, not to the frame (`frame/plan.md:72`). Each fix adds sentences to a section the tree holds, which `skills/implement/fix-pass.md:63-65` says adds no unit. So neither is a decision on the list at `skills/implement/orchestration.md:61-74`, and neither owes the framer a fold.
- *Scope* item 1's fifth bullet (`frame/design.md:45`) opens "Once the orchestrator has committed the framer's fold". It states the fold case under its own condition, and the rejection case at `skills/implement/fix-pass.md:79-82` does not contradict it. A1 (`:85`) is the stop's first pass, which comes before any fold or rejection. *Scope* item 2 (`:47-51`) states no deadline for a prevention home, so the deadline at `skills/implement/orchestration.md:170-172` contradicts none of its sentences. This judgment holds for these three.
- *Scope* item 4's first bullet (`:58`) and A2 (`:86`) say without condition that the orchestrator "commits the fold". The frame foresees a rejection (*Scope* item 3, `:55`). Where the framer rejects, the target commits the rejection's row instead (`skills/code-review/orchestration.md:89-91`), so the two sentences state what the work does not do. That is the shape of round 1's finding 6 at the same bullet. The narrowing still owes a fold there: it narrows the sentence and adds nothing. Finding 2 holds the fix.

The judgment stands in the spawn prompt alone. No row of `frame/plan.md` *Judgments of the run* records it, and `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* asks the orchestrator to write it there.

## Findings

### 1. Four statements of the narrowing still give its scope as a fold after a fix, outside the files finding 4's search covered

```seal
severity: should
location: `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/gaps.md:9`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:70`, `seal/follow-up.md:46`, `tests/text/test_the_rules_have_one_owner.py:388-393`
evidence: executed `git grep -n -i -E "after a fix|source is (what )?a fix|whose source|fold after|narrowing"` over the tree and over the work item's records outside `trail/rounds/`, in the clone at the target; read `skills/implement/orchestration.md:76-94`
reopens: round-1#4
```

Why it matters: finding 4's class is every statement that gives the narrowing's scope as "after a fix" where its home says "a fix or a build". Its close fixed the four statements it named. Its search ran over `skills/implement/` and `skills/code-review/orchestration.md` alone, and the close calls that search a sample. Four more statements stand outside it.

The home (`skills/implement/orchestration.md:83-89`) says "A fold whose source is what a fix or a build changed removes the frame sentence HEAD contradicts". It names the orchestrator's fold of a statement a crafter's hand-back names, and a build phase's hand-back is one, as this work item's own `947674dfd` shows. The four statements leave the build out:

- `gaps.md:9` asks whether the parties read "the narrowing of every other fold after a fix" the same way. The sealer and the settle read this row for what nobody verified.
- *Scope* item 8's fourth bullet, `frame/design.md:70`, reads the narrowing's record as "each fold commit after a fix pass".
- `seal/follow-up.md:46` reads it the same way: "the narrowing, as each fold commit after a fix pass". The owner weighs the narrowing by this row. A release whose only restating folds come after build phases reads as one where the narrowing "never fired", and the row then sends that rule to the weighing on a count that left its other source out.
- `tests/text/test_the_rules_have_one_owner.py:389-390` says in the comment over key `"33 "` "A fold whose source is a fix removes or narrows", and the key at `:393` is "33 a fold whose source is a fix removes or narrows". That key is the label this round's probe printed when the link broke (*Probes*).

The method that makes this list whole is the search above, built on the words the old scope was written in. It is still a sample: a statement of the scope in other words stands outside it.

`gaps.md:9` is the crafter's file. Its row's last clause:

```markdown
and the narrowing of every other fold whose source is a fix or a build.
```

`frame/design.md:70` is the frame. The narrowing has the orchestrator fold a statement a crafter's hand-back names, so the orchestrator folds this one after the crafter's hand-back names it:

```markdown
   - The narrowing: each fold commit after a fix pass or a build phase, its diff of the frame files read for a sentence it added that describes what was built, and each later finding located in a frame sentence a fold wrote.
```

`seal/follow-up.md:46`, the clause after the held commit. The orchestrator writes it, and it leaves the held-commit clause to finding 3:

```markdown
and the narrowing, as each fold commit after a fix pass or a build phase read for a frame sentence it added that describes what was built,
```

`tests/text/test_the_rules_have_one_owner.py:388-393`:

```python
    # #1614: a fold after a fix wrote down what the fix had built, and the
    # copy was a finding in two rounds of #1612. A fold whose source is a
    # fix or a build removes or narrows, and the two files that said a fold
    # rewrites a frame sentence with the fact cite the paragraph that holds
    # the rule, not only its section, which they cited before it stood.
    "33 a fold whose source is a fix or a build removes or narrows": (
```

`git grep -n -F '33 a fold'` prints only `:393`, so the key's new name breaks no other reference.

```seal
verdict: fixed 34887c899
answer: Two commits close the four statements. `34887c899` applied the round's snippets to `gaps.md:9`, now "the narrowing of every other fold whose source is a fix or a build", and to `tests/text/test_the_rules_have_one_owner.py:388-393`, whose comment and key now read "a fix or a build". The orchestrator's `42e4c8fe2` applied the snippets to `frame/design.md:70` and `seal/follow-up.md:46`. `git grep -n -F '33 a fold'` outside the round records printed only `:393`, and `bin/test -q tests/text tests/behaviour tests/skills/test_passages.py tests/lib/test_gaps.py tests/skills/test_rules.py` exited 0, 1049 passed and 9 skipped, executed. The finding's own search, run again after `34887c899` over `agents`, `skills`, `docs`, `templates`, `tests`, `seal/follow-up.md` and the work item's frame, `gaps.md`, `changelog.md` and `pr.md`, prints three places that stand. `frame/design.md:16`, G6, states the tree at `d13c274e1`. The comment at `tests/text/test_the_rules_have_one_owner.py:388` says what a fold did in #1612, not the rule's scope. The two hits in `tests/github/test_publish_release_note.py:744` and `tests/skills/test_pr_body.py:1301` are on other facts. Every other line it prints already says "a fix or a build" or "a fix pass or a build phase". A statement of the scope in other words stands outside the search, so the list is a sample.
```

### 2. *Scope* item 4's first bullet and A2 say the orchestrator commits the fold, where the target commits the rejection's row when the framer rejects

```seal
severity: should
location: `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:58`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:86`
evidence: read `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:45`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:55`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:58`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:86`, `skills/code-review/orchestration.md:87-92`, `skills/implement/fix-pass.md:79-82`, `skills/implement/orchestration.md:83-89`
regression: round-1#5
```

Why it matters: the sealer and the next fold read *Scope* and the acceptance rows for what the work does. These two sentences give the work an act it does not take in a case the frame itself foresees.

The unit is the paragraph of `skills/code-review/orchestration.md` that opens **The fix pass then finds what the fixes left standing.** At `:89-91` it now says the orchestrator "commits the fold, or its row that records the framer's rejection, and resumes the fix pass". `frame/design.md` *Scope* item 4's first bullet says "The orchestrator sends the finding to the framer, commits the fold, and resumes the fix pass", and finding 5's fix in `474d41883` added the rejection's row beside the fold. The defect came from the fold after the fix pass, which left the frame stating the fold for every hand-back where the target now gives the rejection its own act. *Scope* item 3's third bullet (`:55`) lets the framer reject, so the frame's own case falls under the bullet. A2 (`:86`) has the same Then: given any hand-back that leaves a finding open for a fold, "commits the fold".

The crafter's hand-back named this place. The orchestrator judged that it contradicts no part of HEAD. It does contradict HEAD in the rejection case, as round 1's finding 6 found "the resumed pass builds the unit" did in the fresh-spawn case. The narrowing (`skills/implement/orchestration.md:83-89`) owes a fold here, by the orchestrator, of a statement a crafter's hand-back names. The fold narrows the sentence to the case where it holds and writes no account of the rejection path, which `skills/implement/fix-pass.md:79-82` and the close of round 1's finding 5 hold. *Scope* item 1's fifth bullet (`:45`) already states its condition, so it stays as it is.

`frame/design.md:58`, the second sentence of the bullet:

```markdown
The orchestrator sends the finding to the framer, commits the fold where the framer designs the unit, and resumes the fix pass, or spawns it fresh at the context threshold.
```

`frame/design.md:86`, A2's Then:

```markdown
then it sends the finding to the framer, commits the fold where the framer designs the unit, resumes the fix pass or spawns it fresh at the context threshold, and commits the round record after the hand-back that leaves no finding open for a fold
```

```seal
verdict: fixed 42e4c8fe2
answer: The orchestrator's fold applied both snippets. At HEAD `frame/design.md` *Scope* item 4's first bullet and A2's Then each say the orchestrator "commits the fold where the framer designs the unit", read. No tree change was owed.
```

### 3. The follow-up row's held-commit clause sends "#1614's rejected hook" to the weighing, and the frame row that describes the hook goes with the settle

```seal
severity: should
location: `seal/follow-up.md:46`
evidence: executed `git show --word-diff=plain 0fd12e5ba -- seal/follow-up.md`; read `seal/follow-up.md:46`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:69`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/plan.md:35`
regression: round-1#9
```

Why it matters: the owner answers this row at the next release, after the settle has removed the work item's directory. The row then asks the owner to weigh a hook it does not describe, and names no commit where its description stands.

The unit is the clause `0fd12e5ba` added to the row at `seal/follow-up.md:46`: "the held commit, as each round spawned while an earlier record of the work item held a finding left open for a fold, one or more of which sends #1614's rejected hook at the proofer's spawn to the same weighing". `frame/design.md` *Scope* item 8's third bullet (`:69`), which the fold of finding 9 at `d154f13fd` wrote, sends "the `frame/plan.md` *Alternatives considered* row on a hook at the proofer's spawn" to the weighing. The orchestrator's commit carried that pointer into a row that outlives the frame. The defect came from copying a coordinate that only holds inside the frame. The row that describes the hook is `frame/plan.md:35`: a `PreToolUse` hook on the orchestrator's `Agent` call that spawns `agentic:proofer`, denying it while the work item's newest round record holds a finding with no close block. Round 1's finding 8 found the same defect in the same row for G11, and `6ee02726f` fixed it by writing the counts into the row. The other mechanisms the row names are the fix pass's stop, the orchestrator's sort and the narrowing. Each is described in the row or stands in a file the settle keeps.

`seal/follow-up.md:46`, the held-commit clause:

```markdown
the held commit, as each round spawned while an earlier record of the work item held a finding left open for a fold, one or more of which sends to the same weighing a `PreToolUse` hook on the orchestrator's `Agent` call that spawns `agentic:proofer` and denies the spawn while the work item's newest round record holds a finding with no close block, which #1614 weighed and rejected;
```

```seal
verdict: fixed 42e4c8fe2
answer: The orchestrator's commit applied the snippet. At HEAD `seal/follow-up.md:46` describes the hook in the row itself, a `PreToolUse` hook on the orchestrator's `Agent` call that spawns `agentic:proofer` and denies the spawn while the newest round record holds a finding with no close block, and no longer says "#1614's rejected hook", read. No tree change was owed.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `skills/implement/fix-pass.md:52-57` defines a unit as "a new name or path that the frame holds nowhere", new where the tree at the round's `target:` holds no part by it. `:63-65` says a change to the body of a part the tree already holds adds no unit "whether or not the frame names the part", with "a sentence added to a section" as its example. That answers both readings round 1 named: an existing part the frame never names, and a rule sentence added to a section. A new heading stays a unit (`:55`). The stop reads "a unit the frame does not hold" (`:71`), and the route table cell reads "add a unit the frame does not hold" (`skills/code-review/orchestration.md:229`). *Scope* item 1's first three bullets (`frame/design.md:41-43`) hold the same sentences, and the changelog's first item states them. All read. The heading and bold lead still say "does not name", and `:57-59` defines the frame holding a unit as writing its name or path, so the two words read one way.

```seal
confirms: round-1#2
```
What holds: `skills/implement/fix-pass.md:57-61` has the frame hold a unit where a frame section "writes the unit's name or path", and "A helper whose job the frame states, but whose name the frame does not hold, is a unit". That is reading B. `git grep -n -i "by what it does" -- skills agents docs` printed nothing (executed). The frame's second bullet (`frame/design.md:42`) matches, and `frame/plan.md:38` records the rejected reading. All read.

```seal
confirms: round-1#3
```
What holds: `skills/implement/fix-pass.md:65-67` exempts "a part only the tests read, such as a test module, or a helper, a fixture or a constant in one", and `:67-69` names inlining as the stop's stated limit. That answers round 1's first *Not judged* row. `frame/design.md:43`, `frame/plan.md:39-40` and `frame/questions.md:5` ground the exemption on G11 and G12 counting nothing in the tests. All read.

```seal
confirms: round-1#5
```
What holds: `skills/implement/fix-pass.md:79-82` has the fix pass that follows a rejection answer the finding by the route the orchestrator's row of `frame/plan.md` *Judgments of the run* gives it. `skills/code-review/orchestration.md:89-91` has the orchestrator commit "the fold, or its row that records the framer's rejection" before it resumes or spawns the pass. Both agree with `skills/implement/orchestration.md:139-143`, where the orchestrator rewrites its row to record the rejection and the finding's route. All read. The frame sentences this fix left stating the fold alone are finding 2.

```seal
confirms: round-1#6
```
What holds: `frame/design.md:45` reads "the fix pass that follows builds the unit", `:58` "resumes the fix pass, or spawns it fresh at the context threshold", and A2 at `:86` "resumes the fix pass or spawns it fresh at the context threshold". All read.

```seal
confirms: round-1#7
```
What holds: `skills/implement/orchestration.md:170-172` gives the prevention home "before the next spawn or resume". `git grep -n -i "prevention home\|before the next spawn" -- skills agents docs templates tests` printed no other statement of the deadline (executed). The deadline's other statements, `:145-148`, `:565-569` and `skills/implement/fold-and-reframe.md:17`, give the fold and the home but no deadline. The docstring at `tests/text/test_the_rules_have_one_owner.py:696-699` says the same, and the case's two pinned strings are unchanged, read.

```seal
confirms: round-1#8
```
What holds: `seal/follow-up.md:46` carries the counts in the row: 7 of 14 and 127 of 522 in this repository, 20 of 36 and 31 of 147 in owlery. They agree with `frame/design.md:21` G11, read. The row's held-commit clause, added later by `0fd12e5ba`, is finding 3.

```seal
confirms: round-1#9
```
What holds: `frame/plan.md:17` narrows the chosen row's ground to "The crafter's stop is read at the call". It names each backstop of the orchestrator's two acts, and `:34-37` weighs four mechanisms on the orchestrator's half, the `chain_check.py` check among them, each rejected. Row `:36` rests on the check refusing at the ready pull request. That matches `skills/core/SKILL.md` *Judgment is not licence to skip a party*: the check refuses only a ready pull request. The proofer's own `--worktree` run already prints an earlier record's open finding, so the rejection holds. `pr.md:1` quotes `:17` word for word. `frame/questions.md:10` names the new rows. All read. The follow-up clause this fold led to is finding 3.

```seal
confirms: round-1#10
```
What holds: `frame/design.md:105-114` no longer carries the reason or the close-block clause, and it cites `skills/implement/fix-pass.md` for the stop and its reason. `python3 -I skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.0 --root <the branch worktree> --worktree` printed no notice that this design's `to` repeats a passage or names a test pin, executed.

What matched: `pr.md:2` stands word for word at `frame/questions.md:14`, read. Each list item of `changelog.md` and each *Process changes* row was read against the target, and none is contradicted. The changelog's fourth item and second row give the narrowing as "a fix or a build", read.

What matched: `gaps.md:8`, the fix pass's new row, names the run it took, and that run exited 0 with 1049 passed and 9 skipped in this round's clone at the target, executed. Its label for the rest of the suite, the lint and the format check is `unverified`, with the broad gate as its answerer, which is honest.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite beyond this round's two runs, the repository-wide lint and the format check, `unverified` | the tree at `fc096778b` | the orchestrator's broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/text/test_the_rules_have_one_owner.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/skills/test_passages.py`, in the clone at the target | exit 0, 189 passed |
| `bin/test -q tests/text tests/behaviour tests/skills/test_passages.py tests/lib/test_gaps.py tests/skills/test_rules.py`, in the clone at the target | exit 0, 1049 passed, 9 skipped |
| `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py -k test_every_link_names_the_owner`, with "the paragraph opening" removed before **The framer writes a decision's fold** in both `skills/implement/fold-and-reframe.md` and `skills/implement/SKILL.md` through `Edit`, then restored with `git checkout` | exit 1, one case failed, key `"33 "`, on a line naming `skills/implement/fold-and-reframe.md` and `skills/implement/orchestration.md` as its owner; the clone's `git status --short` then printed nothing |
| `python3 -I skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.0 --root <the branch worktree> --worktree`, before this record was written | exit 0; round 1's closed findings read as owed a verifying round, and no notice at a line of `frame/design.md` |
