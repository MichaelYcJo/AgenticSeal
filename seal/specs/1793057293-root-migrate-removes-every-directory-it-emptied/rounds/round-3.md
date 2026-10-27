# Review round 3: 1793057293-root-migrate-removes-every-directory-it-emptied

target: 087d676e, fixes f294b3bd..087d676e

This round verifies round 2's fix pass. It read the fix range
`f294b3bd..087d676e` in the branch worktree at `087d676e`. It then read the
whole diff `fa7d1374...087d676e` only for what the fix range broke. No
`seal/parity.md` is declared, so no parity comparison applies. The fix range
changes records only: 3de79fd3 changes `overview.md`, and 79f675cf and
087d676e change the `answer:` and `verdict:` lines of `rounds/round-2.md`.
`hooks/` and `tests/` are unchanged since `f294b3bd`. So this round carried,
and did not re-run, what rounds 1 and 2 established about the code: the five
mutants, the two modules' 78 passed, the link probes, the simulated failing
`os.rmdir` on macOS, and CI run 40423069012 at `d3f6aaf7`.

## Findings

none

## Confirmations

confirms: round-2#1
The close holds. 3de79fd3 deletes the row that quoted *In* item 4's old link
sentence, and nothing else in `overview.md`. The answer claimed that a
`git grep` for "not something git checks out" over the work item, rounds
left out, finds only `phases/phase-2.md:44`. This round ran it at
`087d676e` and found that one hit. The facts the row gave stand in
`spec.md:58-62` and in `phases/phase-2.md:39-53`, so nothing is lost. One
sentence in the phase record still stands on the deleted row:
`phases/phase-2.md:52` says "`overview.md` records it as a divergence". That
was true at `d3f6aaf7`, when phase 2 closed. A fix pass "writes no phase
record", and "The build's phases keep theirs" (`skills/implement/SKILL.md`,
the paragraph on what a fix pass writes). So the sentence reads as phase 2's
state, as `phases/phase-2.md:44` does, and this round raises nothing on it.
3fd067a8 did add a paragraph to that record (`phases/phase-2.md:65-76`),
which the same rule does not provide for. That commit is round 1's fix
range. Round 2 read the paragraph, and its text is accurate. Executed.

confirms: round-2#2
The close holds. 3de79fd3 adds the row at `overview.md:18`. The answer
claimed that the fix pass took round 2's fenced row word for word. The diff
line and round 2's fenced line match. Each quote was checked against its
source. "holding nothing when the walk reaches it is removed" and "One limit
sentence follows it" stand in `spec.md:56-58`, *In* item 4. "unless its removal fails"
and the second limit's sentence stand in `hooks/root-migrate.py:358-367`,
word for word. *Grounding*'s last row (`spec.md:22`) carries the owner's
direction the grounds name. Round 1's Not judged row and its probe row
(`rounds/round-1.md:145`, `rounds/round-1.md:155`) carry the macOS
simulation. Every row of the table from its header to `overview.md:18` has
four cells. Executed and read.

confirms: none
The fix range broke nothing else in the whole diff. Deleting one row and
adding one keeps every later line of `overview.md` in place, so
`overview.md:26`, the held-open row of *Not verified*, is where round 2
cited it. The S3 row moved from line 18 to line 17. `rounds/round-2.md`
cites it as `overview.md:18` at `f294b3bd`, which is that record's target,
so the citation holds. `bin/unverified-check` over the work item read the
same four *Not verified* rows, all open, and none unreadable. The other two
places that state the held-open limit, `changelog.md:4` and
`phases/phase-2.md:73`, are unchanged by the fix range. CI's `tests` run
40425810821 at `087d676e` completed with conclusion success on every
pytest leg of Linux, macOS and Windows. Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The held-open limit and the delete-pending case on Windows. Carried from rounds 1 and 2: read, and never run on Windows | `hooks/root-migrate.py:358-367`, `hooks/root-migrate.py:400-405` | the repository owner, as `overview.md` *Not verified* names |
| The junction limit, carried from round 1 and still not run on Windows | `hooks/root-migrate.py:363-365` | the repository owner, as `overview.md` *Not verified* names |
| `overview.md` *Not verified*'s first row, the fix and S4 on the Linux and Windows legs. It still reads open. Run 40425810821 at this head succeeded on every pytest leg, and this round read only its job conclusions, not which cases each leg ran | `overview.md:24` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three | `broad-gate.md` | the orchestrator, by `broad-gate` once the rounds settle |
| `questions.md` Q2, the line for a moved item's directory that an ignored file keeps | `questions.md` Q2 | a person, at the pull request |

## Probes

| Command | Result |
|---|---|
| `git diff --stat f294b3bd..087d676e` | two files: the work item's `overview.md` (1 insertion, 1 deletion) and `rounds/round-2.md` |
| `git show --stat 3de79fd3 79f675cf 087d676e` | 3de79fd3 touches `overview.md` only; 79f675cf and 087d676e touch `rounds/round-2.md` only, 2 lines each |
| `git diff 183fba40..087d676e` over `rounds/round-2.md` | the two `verdict:` lines and the two `answer:` lines changed, nothing else |
| `git diff f294b3bd..087d676e` over `overview.md` | the link-limit row removed, the held-open row added under the S3 row |
| `git grep -n "not something git checks out" 087d676e` over the work item, rounds left out | one hit, `phases/phase-2.md:44` |
| `git grep -n "removal fails\|holds it open" 087d676e` over the work item, rounds left out | four hits: `changelog.md:4`, `overview.md:18`, `overview.md:26`, `phases/phase-2.md:73` |
| `git grep -n -i "divergence\|diverged" 087d676e` over the work item, rounds left out | `overview.md:13`, `overview.md:15`, `phases/phase-2.md:52` |
| `awk -F'\|'` cell count over `overview.md` lines 15 to 18 | four cells on each line |
| `bin/unverified-check` over the work item | exit 0; 1 overview, 4 open, 0 closed, 0 unreadable |
| `gh run view 40425810821`, first read | in progress at `087d676e`; lint, both arm-check-grammar legs and four of the eight pytest legs had passed |
| `gh run view 40425810821 --json status,conclusion,jobs`, read again before the record was finished | completed, conclusion success; every job succeeded except `release-report`, which was skipped |
