# Review round 2: 1793057294-close-the-mutation-gaps-the-old-tests-had

target: 695f31be, fixes 1bea9d50..695f31be

This is the verifying round for round 1. It read `git diff 1bea9d50..695f31be`
whole, in a `git clone --no-local` of the worktree at `695f31be` kept in the
round's scratch directory. The range touches eight paths: the two test files
the fixes removed a case from, and six records of the work item
(`changelog.md`, `overview.md`, `phases/phase-2.md`, `phases/phase-3.md`,
`phases/phase-7.md` and `rounds/round-1.md`). It changes no path outside
`tests/` and `seal/`. No `seal/parity.md` is declared, so no parity
comparison applies.

Carried from round 1 as coordinates, not as verdicts: the lines of
`hooks/worktree_consent.py` that finding 2 names (`:118-138`, `:426-441`,
`:591-624`), the definition and readers of `LABEL_DESCRIPTION_LIMIT`, and the
ranges finding 3 counted over. This round opened each of them again and
reached its own verdict. It re-ran every `executed` evidence line of the
three findings, and the m6 and k3 pairs through `bin/mutation-check`. It did
not re-run round 1's other 24 sampled mutants, since the fix range touches
none of their modules or cases.

The smith reported two departures from round 1's paste-ready fixes, and both
are judged under the confirmations below. The first is that each case count
is stated at the commit where it was measured. The second is that two
sentences that stood on facts the fixes changed were removed.

## Findings

No finding opened this round.

## Confirmations

confirms: round-1#1
The close by 561151b0 holds. `git grep -n LABEL_DESCRIPTION_LIMIT` at the
head finds the definition at
`.github/scripts/label_merged_on_release_branch.py:113`, the comment at
`.github/scripts/tracker_labels.py:92`, and readers only in
`tests/test_label_merged_on_release_branch.py:384-386` and
`tests/test_tracker_labels.py:13` and `:146`. No shipped code reads it.
`release_completeness_check.py` and `publish_release_note.py`, which load the
module, do not read it either. The case that pinned 100 is gone, and no file
names it outside `rounds/round-1.md`, `.test_durations` included. The m6
pair over both description files prints SURVIVED and exits 1, which matches
the row's new after column at `phases/phase-7.md:91`. The paragraph at
`phases/phase-7.md:151-161`, the module row at `:31` and the outcome sentence
at `:25-26` now say equivalent, and `overview.md:86-89` lists m6 for the owner.
`Test_module` keeps its cap case, which reads the constant as its ruler, so
the number still has one source. Executed with the probe and `git grep`.

confirms: round-1#2
The close by c088d7ec holds. Read at the head, `main` without its
`if not session` test reaches `record(top, session)` at
`hooks/worktree_consent.py:624`. There `consent_path` turns every falsy id
into "" through `str(session or "")` at `:132-133`, and `record` returns
False before it writes (`:433-435`). So no input tells the mutant from the
code. The k3 pair over `tests/test_worktree_consent.py` prints SURVIVED and
exits 1, which matches the row at `phases/phase-3.md:118`. The case that
replaced `record` and its `import io` are gone. `sys` and `json` are still
used in the file, and ruff passes it. The module row at `phases/phase-3.md:34`,
the outcome sentence at `:24-25` and the paragraph at `:173-181` read
equivalent, and `overview.md:90-92` lists k3 for the owner. The contract
rule 13 row at `overview.md:52` counts 7 rows and quotes the rule with
"platform". Its 7 are phase 1's four (`phases/phase-1.md:136`) and phase 2's
three (`phases/phase-2.md:198-202`). Executed with the probe, read for the
code.

confirms: round-1#3
The close by c19f0588 holds. The counts, re-run in the clone, are these.
`git diff 5daa931f...HEAD -- tests` adds 169 lines holding `def test_` and
removes none. `git diff 134d7203 HEAD -- tests` adds 182 and removes none.
`git diff 5daa931f...cfdf2e7b -- tests` adds 171, and
`git diff 134d7203 cfdf2e7b -- tests` adds 184. These are the numbers
`overview.md:100` and `phases/phase-7.md:198-203` state, each at the commit
it names. `phases/phase-2.md:198-202` now reads three rows, two of them
git's, and s4 as the third, which is what the paragraph names. Executed with
the four counts.

confirms: none
The first departure holds. Round 1's paste for `overview.md` *Not verified*
row 3 stated 171 over `5daa931f...HEAD`. That number was true at
`dfd10e1a` and false once findings 1 and 2 removed two cases. The smith
instead states 171 and 184 at cfdf2e7b in `phases/phase-7.md`, and 169 and
182 at the head in `overview.md`. Each number matches its range when re-run.
The phase record states its own commit's count, and the closing memo states
the head's. That is the shape round 1 should have pasted. Executed with the
four counts.

confirms: none
The second departure holds. Two sentences were removed. The tail of the
contract rule 13 row in `overview.md`, which said phase 2 "says four of its
rows rest on such a guarantee and names three", would have been false once
c19f0588 corrected phase 2 to three. The sentence "The k3 case runs `main`
in the process, with stdin replaced" in the platform-fakes paragraph of
`phases/phase-3.md` stood on the case c088d7ec removed. Removing each in the
commit that changed its fact is what contract rule 19 asks. The smith's
hand-back says both stood on the old phase-2 count. Only the first did. The
second stood on the removed case. The records themselves are correct either
way. Read at `overview.md:52` and `phases/phase-3.md:218-222`.

confirms: none
The totals add up wherever they stand. The phase rows of `overview.md:19-28`
sum by column to 180 rows, 121 killed, 9 already closed, 16 equivalent, 34
left the tree and 0 findings, and 121, 9, 16 and 34 sum to 180. Phase 3's
module table sums to 14, 3 and 4. Phase 7's sums to 14, 1, 1 and 1. Each
matches its outcome sentence and its row in the overview. "Of the 121 kills,
118 are by an added case, 2 by an existing case ... and 1 by a rewritten
case" sums to 121. `changelog.md:3` and `overview.md:8` read 121 and 16. A
search for 123, 122, 15 and 14 used as counts across the work item's
records, round records aside, finds no stale total. At 561151b0
`changelog.md` read 122 and 15, as that commit's answer says. Executed with
`git grep -nwE` over the work item and `git show 561151b0:<changelog>`.

confirms: none
The two edited test files still pass the repository's layout and lint
checks. `bin/test-layout --check` over them reads 2 files and refuses none.
`--pairs` prints one pair, `Test_existing_labels`, which phase 7 names and
which no removed case was part of. `uvx ruff check` and
`uvx ruff format --check` over the two files exit 0. `bin/test` over
`tests/test_label_merged_on_release_branch.py`, `tests/test_tracker_labels.py`
and `tests/test_worktree_consent.py` passes 89, exit 0. This is a narrow run
and no seal of the suite. Executed with the probe.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three | `broad-gate.md` | the orchestrator, by `broad-gate --base release/v0.22.4 --record` now that this round leaves nothing open |
| Round 1's other 24 sampled mutants, the before verdicts of every row and the 119 mutants round 1 did not rebuild. Carried from round 1 and the phase records. The fix range touches none of their modules or cases | `phases/phase-1.md` to `phases/phase-7.md` | the sealer, in its sample of claims |
| t5's equivalence, which rests on phase 3's probe over 1,488 commands, carried and not re-run | `phases/phase-3.md:148-155` | the sealer, in its sample of claims |
| Whether `.test_durations` prices none of the 169 new cases, as `overview.md` *Not verified* row 3 says. Carried from round 1's collection run, not re-run | `overview.md:100` | the orchestrator's broad gate, through `test_the_durations_file_prices_the_suite` |

## Probes

| Command | Result |
|---|---|
| `bin/mutation-check .github/scripts/label_merged_on_release_branch.py --replace 'LABEL_DESCRIPTION_LIMIT = 100' 'LABEL_DESCRIPTION_LIMIT = 1000' --tests "bin/test tests/test_label_merged_on_release_branch.py tests/test_tracker_labels.py -q -x -p no:xdist"` | SURVIVED, exit 1, after a baseline of 35 passed |
| `bin/mutation-check hooks/worktree_consent.py` with the k3 pair of `phases/phase-3.md:118` and `--tests "bin/test tests/test_worktree_consent.py -q -x -p no:xdist"` | SURVIVED, exit 1, after a baseline of 54 passed |
| `bin/test tests/test_label_merged_on_release_branch.py tests/test_tracker_labels.py tests/test_worktree_consent.py -q -p no:xdist` | 89 passed, exit 0 |
| `bin/test-layout --check` and `--pairs` over the two edited test files | 2 files read, 0 refused; 1 pair, `Test_existing_labels` |
| `uvx ruff check` and `uvx ruff format --check` over the two edited test files | both exit 0 |
| `git diff 5daa931f...HEAD -- tests`, `git diff 134d7203 HEAD -- tests`, `git diff 5daa931f...cfdf2e7b -- tests` and `git diff 134d7203 cfdf2e7b -- tests`, each through `grep -c` for added and removed `def test_` lines | 169, 182, 171 and 184 added; none removed at the head |
| `git grep -n LABEL_DESCRIPTION_LIMIT` and `git grep -n` for the two removed case names | no shipped reader of the constant; the two names stand only in `rounds/round-1.md` |
| `git status --porcelain` in the clone after the probe | empty; the probe file and the clone are deleted |
