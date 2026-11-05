# Review round 2: 1793862999-unverified-baseline-is-run-by-a-person-only

```seal
target: f2298696, fixes c2702707..f2298696
```

This is a verifying round. Its range is `c2702707..f2298696`, the fix pass
of round 1 and the orchestrator's two folds around it: `d45b2977`,
`fb1f126e`, `96ce5e6f`, `78b5e4df` and `f2298696`. The round read that diff
in the branch worktree and ran its commands in a `git clone --no-local` of
the branch at `f2298696`, kept in the round's scratch directory. No
`seal/parity.md` is declared, so the parity comparison does not apply. The
seal root's `config.md` has no `Record language` row, so this record is in
English.

Carried from round 1, not re-established: the coordinates of the two
scripts that read a closed row's second cell
(`skills/verify/scripts/unverified_check.py:807-813`,
`skills/settle/scripts/settle.py:1764`, `:1833`), which this round opened
again at HEAD, and the reading of the two test-pin notices at
`frame/design.md:75`. Every verdict below was reached in this round.

The run of `skills/code-review/scripts/chain_check.py` printed the same two
notices at `frame/design.md:75` as in round 1, the `remove` of *The
unverified record, and the baseline it is read against*. One names "not in
the tree" at `tests/skills/test_settle.py:1738`, and the other names "is not
in the tree" at `tests/text/test_the_release_tail_does_not_end_at_the_tag.py:193`.
This round read both lines again. The first asserts that a settle run's
output lacks the phrase. The second is the message of a check that a
checklist box names an existing script. Neither pins the wording of that
docs section or a fact read from it, so neither is a finding.

The new stage-1 paragraph of `skills/code-review/SKILL.md` is text the
proofer reads at every review, so this round read it as an instruction,
one case at a time. Its three named cases are a closed row's old line, a
directory a settle removes whole, and local mode. The local-mode sentence
is right: contract rule 11 states that nothing under a local-mode root is
committed, so no diff holds a closing memo there. The phrase "the range"
has one reading where the proofer reads it, the target its prompt names.
Two of the paragraph's readings are wrong, and they are the findings below.

## Findings

### 1. The new stage-1 paragraph makes an open row edited in place a finding

```seal
severity: should
location: `skills/code-review/SKILL.md:39-41`, `seal/threads/1793862999-unverified-baseline-is-run-by-a-person-only/changelog.md:3`
evidence: executed a one-file probe over `git log --all -p -U0 --diff-filter=M -- '*gaps.md'` in the worktree, pairing each removed `## Not verified` row with the added rows of its commit; executed `git show -U0 7f5fe0a0 caab8bc0 e359beb3 -- '*gaps.md'`; read `skills/code-review/SKILL.md:35-45`, `skills/implement/SKILL.md:376-379`, `seal/threads/1793862999-unverified-baseline-is-run-by-a-person-only/frame/design.md:37`, and `skills/verify/scripts/unverified_check.py:1625-1658` at `a0303ee9`
regression: round-1#2
```

The unit is the paragraph `96ce5e6f` added at
`skills/code-review/SKILL.md:35-45`, the fix of round 1 finding 2. Design
*Scope* item 9, which plan row 2 delivers, asks the proofer to read each
`gaps.md` for "a row or a memo that left without the word `closed`", but
the fix wrote "A row the diff removes is a finding", and a line diff also
removes the old line of a row edited in place, so the defect came from
reading a removed line as a row that left.

Why it matters: the paragraph excepts only a row the diff adds that "carries
the same item opening with the word `closed`". A row that stays open but is
reworded, or gets another answerer, shows in a line diff as one row removed
and one added. That added row does not open with `closed`, so the paragraph
calls the edit a finding. This edit is common. A probe over every local
branch's history found 22 rows removed from a `gaps.md` that stays, where no
`closed` row of the same item was added. The three commits this round opened
are all of that kind. In `7f5fe0a0`, phase 2 of #1393 extends the broad-run
row with its own run. In `caab8bc0`, a commit adds "and the addendum's row
116" to a row. In `e359beb3`, round 1's fix pass of #1381 adds its own run to
two rows. A fix pass extending the broad-run row is what a verifying round's
diff usually holds, so the paragraph raises a finding where nothing left.
The arm this work item removed did not do this.
`compare_at` (`unverified_check.py:1648-1649` at `a0303ee9`) fired only
when the table held fewer rows than at the base, so an edit in place never
fired it. `skills/implement/SKILL.md:376-379` also speaks of "a row that left
without the word `closed`", which is the frame's reading. The changelog
fragment's first item repeats the paragraph's wording ("A row the diff
removes is a finding unless an added row carries the same item opening with
`closed`"), so the fix pass owes that sentence too. The snippet below
covers only the skill's sentence.

Replace the sentence that opens "A row the diff removes is a finding unless"
at `skills/code-review/SKILL.md:39`, up to "that stays." at line 41, with:

```markdown
A line diff shows a row edited in place as one row removed and one added,
so a row the diff removes has left the table only where no row the diff
adds carries the same item, either opening with the word `closed` or still
open with its wording or its answerer changed. A row that left is a
finding, and so is a `gaps.md` removed from a work item directory that
stays.
```

```seal
verdict: fixed b250e66a
answer: The finding holds. A line diff shows a row closed or reworded in place as one line removed and one added, and the paragraph read that removed line as a row that left. Design *Scope* item 9 at f2298696 asks only for a row or a memo that left without `closed`. I wrote the fix in my own words, to that frame line. The paragraph now says stage 1 reads each changed `gaps.md` for a row or a memo that left without `closed`, and raises a finding for each one. It adds that a row closed or reworded in place shows as one line removed and one added, so a row has left only where no added line carries the same item. The paste-ready text listed which edits count as the same item; I left that to the proofer's reading. The changelog fragment's first item says the same in the same commit.
```

### 2. The new stage-1 paragraph reads every whole-directory removal as a settle, and the rule it cites leaves that removal to the review

```seal
severity: should
location: `skills/code-review/SKILL.md:41-43`, `seal/threads/1793862999-unverified-baseline-is-run-by-a-person-only/changelog.md:3`
evidence: read `skills/code-review/SKILL.md:41-43`, `docs/checks/the-fold.md:11-23`, `seal/threads/1793862999-unverified-baseline-is-run-by-a-person-only/frame/design.md:37`
regression: round-1#2
```

The unit is the same paragraph `96ce5e6f` added at
`skills/code-review/SKILL.md:35-45`, the fix of round 1 finding 2. Design
*Scope* item 9, which plan row 2 delivers, asks only for a reading of a row
or memo that left without `closed`, but the fix also restated the fold rule
as "A directory the diff removes whole is a settle, not a deletion" and
dropped that rule's two conditions, so the defect came from summarising the
cited section.

Why it matters: the section the paragraph cites,
`docs/checks/the-fold.md` *The fold, and what tells it from a deletion*,
makes a whole removal a settle only "where the directory stood at the merge
base" (`:11-12`). It then names its own limit: "A pull request outside a
settle that removes a whole work item directory reads as a settle too; its
diff shows the removal to its review" (`:21-23`). The scripts read every
whole removal as a settle, so that sentence leaves a removal made outside a
settle to the review alone. The new paragraph tells the review to read the
same removal as a settle. After it, nothing reads a work item directory that
a branch which is not a settle removes whole. The paragraph also drops the
merge-base condition. In a verifying round's diff, a fix pass that removes a
directory created on the branch reads as a settle too. The settle case the
paragraph names is read rightly. The non-settle case is read wrongly, and in
a work item branch only that case can occur, because only a settle removes
another work item's directory (`docs/checks/the-fold.md:13-15`). The
changelog fragment's first item says "A directory removed whole is a
settle", so the fix pass owes that sentence too. The snippet below covers
only the skill's sentence.

Replace the sentence that opens "A directory the diff removes whole" at
`skills/code-review/SKILL.md:41`, up to "from a deletion*)." at line 43,
with:

```markdown
A work item directory the diff removes whole is a settle, not a deletion,
where the work under review is the settle and the directory stood at the
merge base (`docs/checks/the-fold.md` *The fold, and what tells it from a
deletion*). The scripts read every whole removal as a settle, and no other
step removes another work item's directory, so outside a settle that
removal is a finding only this reading sees.
```

```seal
verdict: fixed b250e66a
answer: The finding holds. `docs/checks/the-fold.md:11-12` treats a whole removal as a settle only where the directory stood at the merge base, and `:21-23` leaves a whole removal outside a settle to the review alone. The paragraph had dropped both conditions. The fix keeps the frame's one reading: a `gaps.md` removed has left, alone or with its whole directory. Its one exception is a directory that the settle under review removes whole, where that directory stood at the merge base, with the cited section as the source. The paragraph also says the scripts read every whole removal as a settle, so outside a settle only this reading sees one. I did not take the paste's "no other step removes another work item's directory", which restates the fold section's own text. The changelog fragment's first item now says a memo removed with its whole directory has left, except in a settle's own pull request.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `skills/implement/SKILL.md:382-386` now says that no check
judges whether the second cell of a closed row says what closed the item.
It also names what each reader does. `seal unverified` refuses the cell
only where it is empty or still the template's placeholder
(`skills/verify/scripts/unverified_check.py:807-813`, read at HEAD), and
`seal settle` prints it as "what closed it" (`skills/settle/scripts/settle.py:1833`,
read). The false statement "No script reads what the second cell of a closed
row says" is gone. A search for it outside the work items' records (executed:
`git grep -n -i 'No script reads'`) finds it in no skill, doc or script.
Design *Scope* item 9 (`frame/design.md:37`), which round 1 said states the
same false fact, was folded at `f2298696` to the new wording. The fix pass
wrote its own wording rather than the paste-ready text, and gave its grounds
in the close. The paragraph now holds one statement of the fact where the
paste held two.

```seal
confirms: round-1#2
```
What holds: the proofer's own procedure now asks for the reading the
implement and verify skills name. `skills/code-review/SKILL.md:35-45`
stands in stage 1, after the paragraph on the phase records and `gaps.md`.
It tells the proofer to read the diff of each `gaps.md` and names a
`gaps.md` removed from a directory that stays as a finding (read). The two
headings it cites stand as spelt, at `skills/implement/SKILL.md:329` and
`docs/checks/the-fold.md:6` (read), and
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` passed in the
narrow run below (executed). The fix pass left severity to the proofer and
named the local-mode limit. Both choices hold: the local-mode sentence is
true by contract rule 11. The finding closes, because the proofer is now
told to do the reading. Findings 1 and 2 of this round are defects in the
wording of that new instruction, and each names `round-1#2` on its
`regression:` line.

What matched: the version move. `.claude-plugin/plugin.json:4` reads
`0.32.5`, and `a0303ee9` held `0.32.4` (executed: `git show`).
`git grep -n '0\.32\.4' -- ':!seal/threads'` prints nothing at HEAD, and
`0\.32\.5` stands only in `plugin.json` (executed).
`.claude-plugin/marketplace.json` holds no version (read).
`docs/releasing/branch-and-release.md` *The version moves at the start of a
release* puts the move in the first pull request into the release branch.
`origin/release/v0.32.5` is still at `a0303ee9` (executed: `git log` after
`git fetch`), so no pull request has entered it yet. The same section names
the orchestrator and the commit that adds the release's first changelog
fragment. Here the move is in the fix pass's commit `96ce5e6f`, which edits
the fragment. `frame/plan.md`'s *Operational impact* line and the Judgments
row dated 2026-11-05 record that departure and its grounds. The `hygiene`
workflow holds only that a release pull request into `main` moves the
version (`.github/workflows/hygiene.yml:70-107`, read). Which work item
enters the release branch first is in *Not judged*.

What matched: the fix pass's claims that this round ran again.
`bin/seal rules --check` exited 0 with the same one excused line as in
round 1 (executed). `chain_check.py --worktree` exited 0 before this record
existed (executed). The crafter's run of 3492 passed and 10 skipped over 74
modules was not run again. It stays the crafter's account, and the broad run
answers it. `gaps.md:7` still labels the full suite, lint and typecheck at
HEAD as unverified, with the orchestrator's broad gate as the answerer. The
fix pass changed neither the suite nor the label, so the label is honest.

No case pins the wording of either new paragraph. A pin that held a rule's
wording would itself be a defect, and neither paragraph states a fact a
script reads, so that is no gap.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `f2298696`, and the crafter's 3492 passed and 10 skipped | the `Broad gate` row of `seal/config.md` | the orchestrator, at the broad gate |
| Whether #1240 is the first pull request into `release/v0.32.5`, which would make the move match *The version moves at the start of a release*, or follows #1393, where the plan's Judgments row stands as the recorded departure | `.claude-plugin/plugin.json:4`, `seal/threads/1793862999-unverified-baseline-is-run-by-a-person-only/frame/plan.md` *Judgments of the run* | the orchestrator, when it merges the two pull requests |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/text/test_review_axes.py tests/behaviour/test_unverified_rows_close.py tests/behaviour/test_the_release_check_watches_what_ships.py tests/skills/test_payload_meter.py -q -p no:randomly`, in the clone at `f2298696` | exit 0, 235 passed |
| `bin/seal rules --check`, in the clone | exit 0, 1 excused in 226 check lines of 70 rule files |
| `test_tmp_edited_rows.py`, a one-file probe outside the clone, over `git log -p -U0 --diff-filter=M --format=... a0303ee9 -- '*gaps.md'` in the worktree | 0 rows. The squashed history of the base holds each `gaps.md` as one added file, and only 2 later commits change one |
| the same probe over `--all` | 22 rows removed from a `gaps.md` that stays with no `closed` row of the same item added. `7f5fe0a0`, `caab8bc0` and `e359beb3`, read with `git show -U0`, each extend an open row in place |
| `git grep -n '0\.32\.4' -- ':!seal/threads'`; `git grep -n '0\.32\.5' -- ':!seal/threads'` | no output; `.claude-plugin/plugin.json:4` alone |
| `python3 skills/code-review/scripts/chain_check.py --baseline a0303ee9 --root <the worktree> --worktree`, run before this record existed | exit 0; the two test-pin notices at `frame/design.md:75` weighed above, round 1's two `fixed` findings and its target named as owing a verifying round, and the gate and guarantee records named as absent |
