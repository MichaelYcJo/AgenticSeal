# Review round 3: 1793862999-unverified-baseline-is-run-by-a-person-only

```seal
target: b55f9db2, fixes f2298696..b55f9db2
```

This is a verifying round. Its range is `f2298696..b55f9db2`: round 2's
record and the orchestrator's routing row (`da2e1958`), the fix pass's one
commit `b250e66a`, and the fix pass's close blocks (`b55f9db2`). `b250e66a`
rewrites the stage-1 paragraph of `skills/code-review/SKILL.md` and the
changelog fragment's first item, and nothing else. The round read the diff
in the branch worktree and ran its commands in a `git clone --no-local` of
the branch at `b55f9db2`, kept in the round's scratch directory. No
`seal/parity.md` is declared, and the seal root's `config.md` has no
`Record language` row, so this record is in English.

Carried from round 2, not re-established: the coordinates of the fold
rule's two conditions (`docs/checks/the-fold.md:11-12` and `:21-23`), which
this round read again, and the three commits `7f5fe0a0`, `caab8bc0` and
`e359beb3`, each extending an open row in place. Round 2's probe over every
branch's history was not run again. The fix stops the paragraph from
counting those edits, so the three commits are enough to read the new
sentence against. Every verdict below was reached in this round.

The orchestrator's new Judgments row (`frame/plan.md`, the last row) routes
round 2's two regressions to an ordinary fix pass and holds the fix to
design *Scope* item 9's word "left". The rewritten paragraph now uses that
word (`skills/code-review/SKILL.md:39`).

## Findings

None.

## Confirmations

```seal
confirms: round-2#1
```
What holds: `skills/code-review/SKILL.md:38-42` now tells stage 1 to read
each changed `gaps.md` "for a row or a memo that left without the word
`closed`". That is design *Scope* item 9's reading (`frame/design.md:37`)
and the one at `skills/implement/SKILL.md:376-379`. The next sentence says
that a row closed or reworded in place shows as one line removed and one
added. "So a row has left only where no line the diff adds carries the same
item." Read against the three carried commits, this sentence has one reading.
In `7f5fe0a0` and `e359beb3` the added line carries the broad-run item with
a run appended, and in `caab8bc0` it carries the item with one clause
appended. Each row stays, so none of the three is a finding. A row whose
answerer alone changes keeps its item word for word, so it stays as well.
The fix pass departs from round 2's paste: it lists no kinds of edit that
count as the same item. Its grounds are that this is the proofer's reading,
and they hold. The sentence before already names the two edits, a closing
and a rewording. Whether two wordings are one item is a judgment of
meaning, which `skills/core/SKILL.md` *The first value* leaves to the
agent. The changelog fragment's first item says the same
("A row closed or reworded in place has not left").

```seal
confirms: round-2#2
```
What holds: `skills/code-review/SKILL.md:42-47` keeps both conditions of
`docs/checks/the-fold.md`. A `gaps.md` the diff removes "has left too,
alone or with its whole directory". The one exception is "a directory the
settle under review removes whole, where it stood at the merge base", which
is the fold rule's merge-base condition at `:11-12`. The sentence "The
scripts read every whole removal as a settle, so outside a settle only this
reading sees one" is the limit at `:21-23`, where the review is the reader.
The scripts' side holds at HEAD: `skills/verify/scripts/unverified_check.py#settled`
(`:1160-1174`, read) counts a directory as settled when it held a file at
the merge base and is gone. It reads no other condition. The fix pass also
departs from round 2's paste: it does not repeat that no other step
removes another work item's directory. Its grounds are that the cited
section states it (`docs/checks/the-fold.md:12-14`, read; the clause is at line 13), and they hold,
because the paragraph cites that section by its heading. The changelog
fragment's first item states the same exception.

What matched: the other statements of the fact still agree with the
rewritten paragraph. `skills/implement/SKILL.md:376-379` says a row that
left without `closed` shows in the memo's diff, and so does a memo that left
whole. `skills/verify/SKILL.md:239-241` and the module docstring at
`skills/verify/scripts/unverified_check.py:25-27` send a deleted row or memo
to the proofer (read). The two cited headings stand as spelt, and
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` passed in the
narrow run below (executed).

What was weighed and is no finding: the paragraph says the settle is "the
one exception". The other whole removal of committed memos is the pull
request that moves a root to local mode (`docs/checks/the-pull-request-check.md:136-142`,
read). That pull request leaves no root in the tree, so it declares no work
item and no proofer is spawned for it. The sentence that kept it from
reading as a deletion of records (`docs/checks/the-unverified-record.md:21-23`)
was about the base comparison, and this work item's `## Rule changes`
removes it with that comparison. Round 2's paste had the same reach, so the
case was not opened by `b250e66a`.

What matched: the fix pass's claims that this round ran again.
`bin/seal rules --check` exited 0, with the same one line excused as in
rounds 1 and 2 (executed). `chain_check.py --worktree` exited 0 with this
record in the working tree (executed). This round did not run the crafter's 3328 passed
and 10 skipped over 68 modules. That count stays the crafter's account, and
the broad run answers it. `gaps.md:7` still labels the full suite, lint and
typecheck at HEAD as unverified, with the orchestrator's broad gate as the
answerer, and the fix pass changed neither the suite nor that label.

With no finding open, what comes due is the orchestrator's broad run and
then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `b55f9db2`, and the crafter's 3328 passed and 10 skipped | the `Broad gate` row of `seal/config.md` | the orchestrator, at the broad gate |
| Whether #1240 is the first pull request into `release/v0.32.5`, carried from round 2 unchanged | `.claude-plugin/plugin.json:4`, `seal/threads/1793862999-unverified-baseline-is-run-by-a-person-only/frame/plan.md` *Judgments of the run* | the orchestrator, when it merges the two pull requests |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/text/test_review_axes.py tests/behaviour/test_unverified_rows_close.py -q -p no:randomly`, in the clone at `b55f9db2` | exit 0, 143 passed |
| `bin/seal rules --check`, in the clone | exit 0, 1 excused in 226 check lines of 70 rule files |
| `python3 skills/code-review/scripts/chain_check.py --baseline a0303ee9 --root <the worktree> --worktree`, run with this record in the working tree | exit 0; no refusal of the record; the two test-pin notices at `frame/design.md:75` that rounds 1 and 2 weighed, and the gate and guarantee records named as absent |
