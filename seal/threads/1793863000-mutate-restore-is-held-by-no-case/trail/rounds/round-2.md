# Review round 2: 1793863000-mutate-restore-is-held-by-no-case

```seal
target: 7c51f452, fixes 831e7d6b..7c51f452
```

This is a verifying round. It reviewed `git diff 831e7d6b..7c51f452`, which holds round 1's record (`a524532e`), the fix `c8f227da` and the close block `7c51f452`. The fix is one line: `trail/phases/phase-1.md` line 17, the D4 class paragraph (executed: `git show --stat c8f227da` lists that file alone, one line in and one out; `git show --stat 7c51f452` lists `trail/rounds/round-1.md` alone, five lines in). No code, test or document outside the work item changed after round 1. The round worked in a `git clone --no-local` of the branch checked out at `7c51f452` in the round's scratch directory. `seal/config.md` still has no `Pact` row and no `Record language` row, and the repository declares no `seal/parity.md`.

Carried from round 1, as coordinates: the grep the paragraph names, the merge `5f5d7471` it runs at, the build commit `4aa0aa4c`, and the readings of `tests/skills/test_mutation_check.py` lines 305, 527, 571 and 980 at the merge. Re-established this round: the grep's output at the merge, which hunks the branch changed since the merge, and each of the paragraph's 39 placements against both. Round 1's verdicts on D1 to D4, S7 and S8 were not re-derived, because no code changed after `831e7d6b`, and this round stayed inside the fix diff.

The axes were the fix's own. Is the paragraph's list whole against its grep? Is each hit placed on the side the tree puts it? Does the paragraph state the list anywhere else in the work item? Did the crafter's two departures from round 1's paste-ready text hold against the tree? Does the fix add a defect a regression line would name? The table's axes do not apply to a one-line change to a phase record.

## Findings

No finding.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the paragraph at `trail/phases/phase-1.md:17` now names every hit its grep prints at the merge, on the side the tree puts it. The crafter claimed 39 hits, 10 changed and 29 staying. Executed: `git grep -n -i 'mutated module\|not restored\|NotRestored\|NOT_RESTORED\|mutated file' 5f5d7471 -- ':!seal/threads'` in the clone prints 39 lines. The paragraph names each of them once. Ten are on the changed side: `mutation_check.py` lines 48, 209, 210, 218, 252 and 721, `seal-mutate.md` line 60, and the test module's lines 1112, 1724 and 1730. The other 29 are on the side that stays. They are `mutation_check.py` lines 11, 34, 94, 137, 453, 505, 608, 613, 623, 629, 630, 711, 713 and 735, `seal-mutate.md` line 85, the behaviour module's lines 6 and 50, and the test module's lines 305, 527, 571, 980, 1079, 1095, 1099, 1106, 1132 and 1223, with `agents/crafter.md` line 80 and `.test_durations` line 3709. Executed: `git diff -U0 5f5d7471 7c51f452 -- ':!seal/threads'` prints these hunks on the merge's side. In `mutation_check.py` they are lines 48, 209 to 210, 219 to 220, 253 and 719 to 723. In `seal-mutate.md` they are lines 61 to 62. In the test module they are 1111 to 1112, 1724 and 1730, with insertions after 345, 1651 and 1731. No hit placed as staying falls in a hunk. Each hit placed as changed is in a hunk, or is in a statement a hunk changes. Round 1's three defects are gone. Lines 305, 527, 571 and 980 are named. Line 721 is on the changed side, inside the interrupt comment at lines 719 to 723. Line 1730 is named as the case's `pytest.raises` line. The paragraph is still the only statement of the list in the work item (executed: `grep -rn -i 'D4 class\|1718\|hits\|1730\|grep -n -i'` over the work item outside `trail/rounds/` finds `phase-1.md` lines 15 and 17 and the `frame/design.md` *Grounding* row on the `not restored` class, and none of them repeats the list).

What matched: the crafter claimed two departures from round 1's paste-ready text, and both hold against the tree, so round 1's text was wrong in those two places. The first is that the grep's `seal-mutate.md` hit is line 60, not 61. The grep prints line 60, "land once, or a `.py` mutant does not compile), `not restored`", and the hunk is lines 61 to 62 (executed, the two commands above). The paragraph says this: "line 60, the `not restored` entry, whose text at lines 61 and 62 changed". The second is that line 210 is in the changed docstring. The hunk at the merge's lines 209 to 210 rewrites both lines of `restore`'s docstring, so round 1's text was wrong to place 210 among the hits that stay.

Two hits on the changed side keep their own text, and the paragraph names each one's statement instead. The message hunk is lines 219 to 220, and the hit at 218 is the first line of the same f-string. The paragraph says "line 218, its message". The docstring hunk is line 253, and the hit at 252 is the `class NotRestored` line above it. The paragraph says "line 252, `NotRestored` and its docstring". Each statement changed, and the paragraph names the statement, so neither is a finding. A reader who checks those two numbers alone against `git diff` finds them unchanged. The paragraph spells out the same case for `seal-mutate.md` line 60 and does not spell it out for these two.

No `regression:` line is owed. The fix made no unit of code or test, and the one line it rewrote holds no false placement. The fix diff adds no test, so no new case is read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. This round ran no module of the suite beyond the one text module in `## Probes`, so the suite is `unverified` | the tree at `7c51f452` | the orchestrator, at the broad gate (`seal/config.md` *Broad gate*) |
| Whether the two `no baseline` parameters pass on Windows (`frame/questions.md` Q1), and whether the 1-second bound leaves the timed-out parameters' stand-in time to write on a loaded Linux runner. Carried from round 1 unchanged, since no code changed | `tests/skills/test_mutation_check.py:1680-1700` | the pull request's CI run on its `ubuntu-latest` and `windows-latest` legs |

No finding is left open after this round. What comes due is the orchestrator's broad run, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `git show --stat c8f227da 7c51f452` | `c8f227da` changes `trail/phases/phase-1.md` alone, one line in and one out; `7c51f452` adds five lines to `trail/rounds/round-1.md` alone |
| `git grep -n -i 'mutated module\|not restored\|NotRestored\|NOT_RESTORED\|mutated file' 5f5d7471 -- ':!seal/threads'` | 39 lines, exit 0 |
| `git diff -U0 5f5d7471 7c51f452 -- ':!seal/threads'`, hunk headers | `mutation_check.py` at 48, 209-210, 219-220, 253, 719-723; `seal-mutate.md` at 61-62; the test module at 1111-1112, 1724, 1730 and insertions after 345, 1651 and 1731 |
| `grep -rn -i 'D4 class\|1718\|hits\|1730\|grep -n -i'` over the work item, `trail/rounds/` left out | `phase-1.md` lines 15 and 17 and `frame/design.md` line 21; none repeats the list |
| `bin/test tests/text/test_the_record_is_written_in_words.py -q` in the branch worktree, with this record on disk | 3 passed, exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline 5f5d7471 --root <the branch worktree> --worktree`, from the plugin's root | exit 0; notices only that `trail/gate.md` and `guarantee.md` are not yet written |
