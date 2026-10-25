# Review round 6: 1792935671-the-routing-check-moves-to-the-sessions-tools

target: df076edb, fixes 42aad119..df076edb

## Findings

The range holds three commits (executed: `git log --oneline 42aad119..df076edb`).
`a6740978` is the smith's fix for round 5 finding 1. It changes
`hooks/routing.py#declared` and `hooks/implementer-mark.py:69` to call
`routing.worktree_branch`. It rewrites the docstrings of `declared` and
`hooks/question-gate.py` and the comment above the mark's write, and it adds
one case each to `tests/test_question_gate.py` and
`tests/test_implementer_mark.py`. `131706f2` adds a paragraph to
`phases/phase-8.md`, and `df076edb` answers round 5. The two changed call
sites are the new units. The finding below stands in one of them.

### 1. The settled description of the smith mark still says it writes the checked-out branch, and since the fix it also writes the branch a paused rebase names

severity: should
location: `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:269`, `tests/test_question_gate.py:5-6`, `hooks/implementer-mark.py:64-69`
evidence: executed `bin/test -q -s -p no:xdist -p no:cacheprovider tests/test_tmp_round6.py`, `git grep -n "checked-out branch\|checked out branch\|the branch checked out" -- docs hooks skills`
verdict: fixed 21999f7f
regression: round-5#1

The unit is `hooks/implementer-mark.py:64-69`, the mark's write. The frame
states the old behaviour: `spec.md:269` says the hook "writes the
checked-out branch name", and phase 8's row at `plan.md:59` names only
`seal no-work-item` and the edit gate as readers that resolve the branch as
the edit gate does. The fix moved the mark onto `worktree_branch`, which
also returns the branch a paused rebase names. The sentence describing the
mark was not rewritten, so the defect came from the fix leaving that
sentence on the old fact.

This matters because `spec.md:269` is the text that settles into
`docs/the-session-hooks.md`, the new policy home of the mark (the rule
change at `spec.md:224-275`). `docs/commit-review-gate-spec.md:204` says
the same, and settle removes that file whole at `spec.md:282-283`. During
a paused rebase HEAD is detached and no branch is checked out. Git itself
says so: `git status` reports a rebase of branch `A` in progress, not that
`A` is checked out. The probe drove a conflicted `git rebase main` on a
branch `A` declared with `Implementation` `smith` and `Automation` `yes`.
`current_branch` returned "", `worktree_branch` returned `A`, a smith spawn
through the `pre-agent` group left a mark that stands for `A`, and the
question gate denied a question. At `42aad119` the same spawn wrote no
mark, because `implementer.write` writes nothing for an empty branch
(`hooks/implementer.py:93-94`, read). A reader of the settled sentence would
conclude that a smith spawned mid-rebase is not recorded. The code now
records it.

The project already has a phrase for this resolution. `spec.md:68` says the
branch is "resolved as the edit gate resolves it (the branch checked out,
else the branch a paused rebase names)". Round 5 confirmed that a branch
with no commit yet counts as checked out, so that phrase covers all three
cases. The class was enumerated with `git grep` over `docs`, `hooks` and
`skills` for the three spellings, and over the work item for "checked-out".
Two more sentences describe the mark or the question gate this way.
`tests/test_question_gate.py:5-6`, the module docstring, says the gate
"reads the checked-out branch's declaration". `docs/commit-review-gate-spec.md:204`
is the second, and settle removes it. The other hits describe the edit
gate, `seal no-work-item`, `chain_check.py` or `current_branch` itself,
and none of those changed in this range. `plan.md:21` names `current_branch`
for `declared`, but it sits under "read at `36a78242`" (`plan.md:14`), so
it states the tree at that commit and is no finding.

```text
# seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:269, the Does cell
writes the branch name, resolved as the edit gate resolves it (the branch checked out, else the branch a paused rebase names), to `<git-dir>/specseal-planner` or `<git-dir>/specseal-implementer`, and prints nothing
```

```python
# tests/test_question_gate.py:5-6, the module docstring
(#1002). The gate reads the declaration of the branch the edit gate resolves
(the branch checked out, else the branch a paused rebase names) through
`hooks/routing.py` and refuses `AskUserQuestion` there, except for the routing
```

answer: The finding holds, and the sentence's grounds route it to an ordinary fix pass: the fix applied round 5's paste-ready direction and left the frame's sentence on the old fact, which is how the fix was written, not a frame that is wrong. The orchestrator rewrote `spec.md:269` in 4bb8482c to say the mark names the branch checked out, else the branch a paused rebase names; the spec's rule changes still parse, 55 operations and no error (executed). The smith rewrote the module docstring of `tests/test_question_gate.py` in 21999f7f in the words of `spec.md` line 68, and left `hooks/implementer-mark.py` unchanged because its comment, rewritten in a6740978, already says the branch is resolved as the edit gate resolves it (read by the smith). `docs/commit-review-gate-spec.md:204` keeps the old sentence until the settle removes that file whole, as the finding says. No behaviour changed, and `tests/test_question_gate.py` and `tests/test_implementer_mark.py` pass (executed by the smith).

## Confirmations

confirms: round-5#1
The close holds. `hooks/routing.py:424-429` returns
`for_branch(root, worktree_branch(cwd))`, and `hooks/implementer-mark.py:69`
writes `routing.worktree_branch(cwd)` (read). Round 5's case B was written
again from its `## Probes` row and run against `df076edb` in a `--no-local`
clone (executed). The repository had a local root (`.git/seal/`), no commit,
and a declaration naming `main` with `Implementation` `smith` and
`Automation` `yes`. In it `current_branch` returned "", `routing.declared`
found the declaration, and the question gate denied an ordinary question.
A smith spawn through `hooks/dispatch.py pre-agent` left a mark that stands
for `main`. After the first commit the question was still denied, and
`implementer-notice.notify` returned nothing. Round 5 found the question
silent, no mark and a false notice there. Each new case was seen red: with
both readers put back on `current_branch` in the clone,
`test_refuses_on_a_branch_with_no_commit_yet` failed on `'silent' == 'deny'`
and `test_accepts_a_smith_spawn_on_a_branch_with_no_commit_yet` failed on
`stands(...)` returning False (executed). Each case drives one reader only,
so each failure belongs to its own reader. With the fix restored, the six
modules round 5 ran passed, 128 cases, which is round 5's 126 and the two
new ones (executed). The smith's account says the same.

confirms: none
The answer's reasoning for the two callers left on `current_branch` holds.
`hooks/implementer-notice.py:150` runs in `post-bash` after a command that
holds `git commit`. After a successful commit the branch has a commit, so
`current_branch` names it, and case B's notice after the first commit was
silent (executed). After a failed first commit it returns "" and says
nothing, which owes no reminder. During a paused rebase the notice also
reads "" and stays silent, as it did before this range. Once the rebase
ends, the mark the fix now writes stands for the branch and the notice stays
silent (executed: case R aborted the rebase, then `notify` returned "").
A control on a declared branch with no smith spawn printed "no smith was
spawned on this branch", so the silence comes from the mark (executed).
`skills/code-review/scripts/chain_check.py:1999` matches only declarations
that `tracked_declarations` lists from `git ls-tree -r -z HEAD`
(`chain_check.py:1975-1990`, read). On a branch with no commit HEAD names
no tree, so `worktree_branch` there would match nothing either. Its message
calls that state "a detached HEAD". That wording predates this range, and
the fix does not make it reachable, so it is not raised.

confirms: none
`routing.declared` has one caller, `hooks/question-gate.py:102`
(executed: `git grep -n "routing.declared"`). So the change of
`declared` reaches the question gate and no other reader. The new
paused-rebase deny matches the gate's stated failure direction, as round 5
said it would (executed: case R). `phases/phase-8.md`'s new paragraph
states the fix and the two callers left alone as the code has them (read).
The question gate's docstring at `hooks/question-gate.py:7-12` names
`worktree_branch` and the branch with no commit yet (read).

confirms: none
The two new cases were read against their groups. `Test_main` in
`tests/test_question_gate.py` covers a linked worktree, a root under the
common git directory and a checkout no declaration names. The new case is
its only repository with no commit. `Test_main` in
`tests/test_implementer_mark.py` holds no other case on an unborn branch
(read: `tests/test_question_gate.py:202-233`,
`tests/test_implementer_mark.py:43-66`). `bin/test-layout --pairs` names no
pair in either module (executed).

Carried from round 5, not re-established: the `unborn_branch` behaviour on
an orphan branch, a linked worktree and a HEAD pointing outside
`refs/heads/`, and the S4 record behaviour. This range changes none of that
code. The `## Not judged` rows below are carried from round 5 except the
first. Every other fact above was established in this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at `df076edb` | the branch | the orchestrator's broad run |
| Whether `mutation-check` dropping `--short` turns the `seal` case red, as the smith reports | `tests/test_seal.py:3246` | the smith's record in `phases/phase-8.md`, read by the sealer |
| Q3's live measurement | `questions.md` Q3 | the orchestrator, who ran it |
| Whether GitHub's server-side rebase of a pull request's head records a committer other than the author | `skills/code-review/scripts/chain_check.py:2087-2088` | the orchestrator, on a live pull request |
| Q1 and Q2, both open; the build took default (a) of each | `questions.md` Q1, Q2 | the owner |
| Whether the harness has an edit tool that `Write\|Edit\|NotebookEdit` does not name | `hooks/hooks.json` `pre-edit` matcher | the owner, in a live session |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:cacheprovider tests/test_question_gate.py tests/test_implementer_mark.py tests/test_implementer_notice.py tests/test_routing.py tests/test_routing_edit_gate.py tests/test_the_implementer_is_recorded.py` in a `--no-local` clone at `df076edb` | 128 passed, exit 0 |
| `bin/test -q -p no:xdist -p no:cacheprovider` over the two new cases, in that clone with `routing.declared` and `hooks/implementer-mark.py:69` put back on `current_branch` | 2 failed: the question gate's case on `'silent' == 'deny'`, the mark's case on `stands` returning False; both edits were then reverted |
| `bin/test -q -s -p no:xdist -p no:cacheprovider tests/test_tmp_round6.py` in that clone | 3 passed. Case B, unborn `main` in a local root: `deny`, mark for `main`, `deny` after the first commit, notice "". Case R, a paused rebase of declared `A`: `current_branch` "", `worktree_branch` `A`, question `deny`, mark for `A`, notice "" during the pause and after `rebase --abort`. Case R0, a declared branch with no spawn: the notice printed "no smith was spawned on this branch". Repositories sat under pytest's temporary directory with an empty global git config, and git was driven from Python |
| `bin/test-layout --pairs` | exit 0; no pair in `tests/test_question_gate.py` or `tests/test_implementer_mark.py` |
| `bin/rules --check` | exit 0, all 249 check lines hold |

The probe file, the clone and the run output under the round's scratch
directory were removed before hand-back.
