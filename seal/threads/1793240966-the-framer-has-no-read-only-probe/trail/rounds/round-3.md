# Review round 3: 1793240966-the-framer-has-no-read-only-probe

target: cffd887a, fixes 33596dcd..cffd887a

This round verifies the fix for round 2. The range holds three commits.
`a05f9311` is the orchestrator's fold into `frame/design.md`. `939947d5` is
the fix pass over `gaps.md` and `trail/phases/phase-3.md`. `cffd887a` commits
the round-2 record as the fix pass left it. Carried from earlier rounds
without searching again: round 1's reading of the four paid-run traces, the
two committed side files behind S8, and the removal of
`shape-no-measurement-row` at `7ac24a06`. None of them is in this range.
Re-derived here: every claim the new text makes about who reads
`frame/questions.md`, whether this work item's `frame/questions.md` still
holds no `a measurement` row, and whether any sentence still names a reader
for the rule's no-row half.

## Findings

None.

## Confirmations

confirms: round-2#1
The close holds. The commands and reads behind it:

- The four lines carry round 2's paste-ready text word for word. Executed:
  `git diff 33596dcd..cffd887a` over the work item. The changed lines are
  the second cell of `gaps.md:22`, the third cells of S2 at
  `frame/design.md:45` and S5 at `:48`, and the sentence at
  `trail/phases/phase-3.md:69-71`. The phase record's sentence is rewrapped,
  as the fix pass said, and its words are unchanged.
- `fixed 939947d5` names a commit that changes `gaps.md` and
  `trail/phases/phase-3.md`, both on the finding's `location:` line.
  Executed: `git show --stat` of `a05f9311`, `939947d5` and `cffd887a`.
  `a05f9311` changes `frame/design.md` alone. `cffd887a` changes
  `trail/rounds/round-2.md` alone.
- No sentence outside the round records still names a reader for the
  no-row half. Executed: `git grep` over the work item for "proofer at
  review", "read by the proofer", "Reader: the orchestrator", "the
  orchestrator, which writes" and "the orchestrator, who writes". The hits
  are in `trail/rounds/round-1.md` and `trail/rounds/round-2.md` only. A
  wider `git grep` for "proofer" and "orchestrator" over the work item,
  round records excluded, finds no other sentence about this half. The
  frame, the closing memo and the phase record now say the same thing: no
  reader after round 1. So the class round 2 named under contract rules 12
  and 19 has no instance left.
- Each claim of the new `gaps.md:22` cell holds against the tree at
  `cffd887a`. Executed: `git grep -n questions.md -- skills/implement/orchestration.md`
  finds the file once, at `:24`, where the framer writes it.
  `git grep -n questions.md -- agents/proofer.md skills/code-review/` finds
  only `skills/code-review/scripts/pr_body.py:14`, which copies table lines
  and judges nothing. `git grep -n questions.md -- agents/sealer.md` exits
  1. `git grep` for `no-measurement-row` over `evals/` and `tests/` exits 1,
  so no case reads the half.
- The cell says no agent definition opens the file "to judge a row's reason
  against the rule". The crafter does open it, at `agents/crafter.md:31-32`
  in step 2. Its step 3 at `:37` says "Say whether the frame holds before
  you build to it". That step names no reading of a row's reason against
  `agents/framer.md:146-148`, so the claim holds as worded. Read.
- This work item's own `frame/questions.md` still holds no `a measurement`
  row. Executed: `git grep -n "a measurement"` over the file finds `:15` and
  `:19`, both in the head's prose. The table rows at `:36-38` name `a
  person` for Q1 and `the work` for Q2 and Q3.
- `bin/seal unverified` reads the new row. Executed with `--baseline
  origin/release/v0.24.1` over `gaps.md`. It exited 0 and lists the row as
  open, with "nobody after round 1" as its answerer.

confirms: none
`cffd887a` changes the round-2 record only in two lines of finding 1:
the `verdict:` line and the `answer:` line. Executed: `git diff 33596dcd cffd887a` of
`trail/rounds/round-2.md` shows two lines out and two lines in, and both
pairs are those labels. The answer claims that its phrase search finds the
phrases only in `trail/rounds/round-1.md` and the round-2 record. The search
above, re-run, agrees.

confirms: none
The fold `a05f9311` is a new unit, and two readings of it were weighed and
found not to be defects. First, S5 at `frame/design.md:48` points to
`gaps.md` *Not verified*, and that row's Item names the no-row half, while
S5's fact is that a row's reason says which environment stops a probe. The
row's second cell covers it: no step opens `frame/questions.md` "to judge a
row's reason against the rule". So the pointer reaches S5's fact. Read:
`frame/design.md:48`, `gaps.md:22`. Second, the row names "nobody" as its
answerer, and contract rule 4 refuses a deferral to nobody. This row defers
nothing: it states a limit of the rule, which round 1 and round 2 both
named as an honest close. It is still read once more. Under
`skills/settle/SKILL.md:167` and step 4 at `:187-194`, the settling session
decides every open row of a released record and re-homes a reading no
record holds to an issue. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over the branch: `unverified`, not run by this round under contract rule 2 | the branch at `cffd887a` | the orchestrator, at `seal gate --base release/v0.24.1 --record 1793240966-the-framer-has-no-read-only-probe` |
| Whether the new rule made the other four framer cases worse: carried from round 1, still unmeasured | `evals/behaviour/framer/` | the owner, at #947's milestone run |

This round leaves nothing open. What comes due is the orchestrator's broad
run, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into the round's scratch directory, then a detached checkout of `cffd887a` | exit 0, then 0 |
| `git diff 33596dcd..cffd887a` over the work item, and `git show --stat` of `a05f9311`, `939947d5` and `cffd887a` | exit 0 for each; four files, one per commit as listed above |
| `git grep -n` over the work item for the five reader phrases | exit 0, hits in `trail/rounds/round-1.md` and `trail/rounds/round-2.md` only |
| `git grep -n -e proofer -e orchestrator` over the work item, round records excluded | exit 0, no sentence about the no-row half |
| `git grep -n questions.md -- skills/implement/orchestration.md` | exit 0, one hit, `:24` |
| `git grep -n questions.md -- agents/proofer.md skills/code-review/` | exit 0, one hit, `skills/code-review/scripts/pr_body.py:14` |
| `git grep -n questions.md -- agents/sealer.md` | exit 1, no hit |
| `git grep -n questions.md -- agents/` | exit 0, `agents/crafter.md:32` and five lines of `agents/framer.md` |
| `git grep -n -e no-measurement-row -e no_measurement -- evals/ tests/` | exit 1, no hit |
| `git grep -n "a measurement"` over the work item's `frame/questions.md` | exit 0, `:15` and `:19` only |
| `bin/seal unverified --baseline origin/release/v0.24.1` over the work item's `gaps.md` | exit 0, two rows open |
| `chain_check.py --baseline origin/release/v0.24.1 --worktree` over the branch worktree, with this record in it | exit 0; nothing refused in this record; it names `trail/gate.md` and `guarantee.md` as not yet written, which the orchestrator's broad run and the sealer owe |
