# Review round 7: 1792935671-the-routing-check-moves-to-the-sessions-tools

target: 807e7015, fixes 2d9f34d1..807e7015

## Findings

This round opens no finding. The range holds three commits (executed:
`git diff --stat 2d9f34d1..807e7015`). `4bb8482c`, by the orchestrator,
rewrites the `implementer-mark` row at `spec.md:269`. `21999f7f`, by the
smith, rewrites the module docstring of `tests/test_question_gate.py` and
adds one paragraph to `phases/phase-8.md`. `807e7015` writes round 6's
verdict and answer lines. The range changes text only: no code unit and no
test case is new or changed, so no unit here takes a `regression:` line.

## Confirmations

confirms: round-6#1
The close holds. The finding named two sentences that described the smith
mark and the question gate as reading the checked-out branch, while both
read `routing.worktree_branch` since round 5's fix. The orchestrator's claim
is that `spec.md:269` now says the mark names the branch checked out, else
the branch a paused rebase names. The row's Does cell reads "writes the name
of the branch checked out, else of the branch a paused rebase names, to
`<git-dir>/specseal-planner` or `<git-dir>/specseal-implementer`" (read).
That matches `hooks/implementer-mark.py:69`, which writes
`routing.worktree_branch(cwd)` for both marks, and the function's docstring
at `hooks/routing.py:354-357`, under which a branch with no commit yet
counts as the one HEAD names (read). Round 5 settled that such a branch
counts as checked out, and that fact is carried, not re-established. The
words differ from the paste-ready text round 6 gave, which also said
"resolved as the edit gate resolves it". The resolution they state is the
same as `spec.md:68`'s, so the row has one reading.

The row sits inside `## Rule changes` and settles into
`docs/the-session-hooks.md`, so it has to parse. The orchestrator's claim is
55 operations and no error. Run again in a `--no-local` clone at `807e7015`,
`rule_changes.parse` returned 55 operations and 0 errors, and exactly one
operation carries the new sentence (executed). This also holds S19.

The smith's claim is that the test module's docstring now names the branch
in `spec.md:68`'s words. `tests/test_question_gate.py:5-8` says the gate
reads the declaration of the branch "resolved as the edit gate resolves it
(the branch checked out, else the branch a paused rebase names), through
`routing.worktree_branch`" (read). The gate reaches that function through
`routing.declared`, which `hooks/question-gate.py:7-10` says too (read), so
the docstring is accurate. The smith left `hooks/implementer-mark.py`
unchanged. Its comment at `:64-68` already says the branch "is resolved as
the edit gate resolves it, so a branch with no commit yet and a paused
rebase get the mark their declaration reads" (read), so the third location
needed no change.

The class was enumerated again. `git grep` over `docs`, `hooks`, `skills`,
`tests` and the work item for "checked-out branch", "checked out branch",
"the branch checked out" and "branch checked out" left one sentence about
the mark or the question gate on the old fact,
`docs/commit-review-gate-spec.md:204` (executed). Settle removes that file
whole (`spec.md:281-283` and `spec.md:759`, read), as round 6 said. Every other hit
describes the edit gate, `seal no-work-item`, `chain_check.py`,
`broad_gate.py`, `current_branch` or a test helper, and none of them is in
this range.

The paragraph `21999f7f` adds at `phases/phase-8.md:34` states the fix as
the tree has it: `spec.md:269` rewritten in `4bb8482c`, the docstring
rewritten, the mark's comment left as it was (read against the diff). With
the fix in place, `tests/test_question_gate.py` and
`tests/test_implementer_mark.py` pass, 35 cases (executed). No behaviour
changed in the range, so the run confirms only that the docstring edit broke
nothing.

confirms: none
The new sentence at `spec.md:269` names the paused rebase, and its section's
`check:` line names `tests/test_implementer_mark.py`. No case in that module
drives a paused rebase (executed: `grep -n rebase tests/test_implementer_mark.py`,
no hit). The clause is still held. The mark's only branch source is
`routing.worktree_branch` (`hooks/implementer-mark.py:69`, read). Round 6's
new case `test_accepts_a_smith_spawn_on_a_branch_with_no_commit_yet` turns
red when the mark goes back to `current_branch`, as round 6 executed. And
`tests/test_routing_edit_gate.py:447` drives the paused-rebase branch of
the same function. Writing the sentence made no new behaviour reachable, so
nothing is raised.

Carried from round 6, not re-established: the probe results for a paused
rebase and an unborn branch (case R and case B), and the reasoning on the
two callers left on `current_branch`. This range changes no code, so the
probe was not written again. The `## Not judged` rows are carried from
round 6. Every other fact above was established in this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at `807e7015` | the branch | the orchestrator's broad run |
| Whether `mutation-check` dropping `--short` turns the `seal` case red, as the smith reports | `tests/test_seal.py:3246` | the smith's record in `phases/phase-8.md`, read by the sealer |
| Q3's live measurement | `questions.md` Q3 | the orchestrator, who ran it |
| Whether GitHub's server-side rebase of a pull request's head records a committer other than the author | `skills/code-review/scripts/chain_check.py:2087-2088` | the orchestrator, on a live pull request |
| Q1 and Q2, both open; the build took default (a) of each | `questions.md` Q1, Q2 | the owner |
| Whether the harness has an edit tool that `Write\|Edit\|NotebookEdit` does not name | `hooks/hooks.json` `pre-edit` matcher | the owner, in a live session |
| The guarantee standing behind HEAD, which `chain-check` reports | `guarantee.md` | the sealer, spawned again after the broad run |

## Probes

| Command | Result |
|---|---|
| `python3 -c` importing `skills/settle/scripts/rule_changes.py` and calling `parse` on the work item's `spec.md` with policy root `docs`, in a `--no-local` clone at `807e7015` | 55 operations, 0 errors; one operation holds "paused rebase names, to" |
| `bin/test -q -p no:cacheprovider tests/test_question_gate.py tests/test_implementer_mark.py` in that clone | 35 passed, exit 0 |
| `bin/rules --check` in that clone | exit 0, all 249 check lines in 62 rule files hold |
| `git grep -n` for the four spellings over `docs hooks skills tests` and the work item | one sentence on the mark or the question gate left on the old fact, `docs/commit-review-gate-spec.md:204`, which settle removes |
| `grep -n rebase tests/test_implementer_mark.py` | no hit |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.4 --root <the branch worktree> --worktree`, with this record in the working tree | exit 1; no line refuses this record. Two lines refuse `broad-gate.md` and `guarantee.md` as behind HEAD, which the orchestrator's broad run and the sealer answer |

The clone and the run output under the round's scratch directory were
removed before hand-back.
