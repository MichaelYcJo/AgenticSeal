# Review round 5: 1792935671-the-routing-check-moves-to-the-sessions-tools

target: 9fa3c247, fixes 41f0ab5d..9fa3c247

## Findings

The range holds four commits (executed: `git log --oneline 41f0ab5d..9fa3c247`).
`5e171b5f` is the orchestrator's change to `spec.md` and `plan.md` for
round 4 finding 2. `6030237f` is the smith's fix for round 4 finding 1:
`hooks/routing.py#unborn_branch`, the new fallback in `#worktree_branch`,
one case each in `tests/test_seal.py` and `tests/test_routing_edit_gate.py`,
and the rewritten docstring of the detached-HEAD case. `a9203f93` updates
`phases/phase-8.md`, and `9fa3c247` answers round 4. The one new code unit
is `unborn_branch`. The finding below sits outside the fix diff. It was
found by enumerating the other readers that share finding 1's cause, and it
stands in no unit the fix pass added or changed, so it carries no line
naming an earlier finding as regressed or reopened.

### 1. Two more readers resolve the branch with `current_branch`, so on a branch with no commit yet the question gate lets a question through and the smith's spawn leaves no mark

severity: should
location: `hooks/routing.py:424-426`, `hooks/implementer-mark.py:68`, `hooks/question-gate.py:7-11`, `tests/test_question_gate.py`, `tests/test_implementer_mark.py`
evidence: executed `python3 <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-5/test_tmp_round5.py`
verdict: fixed a6740978
answer: The finding holds, and a6740978 takes the record's direction: `hooks/routing.py#declared` and `hooks/implementer-mark.py` resolve the branch through `routing.worktree_branch`, and `hooks/question-gate.py`'s docstring now names that function and the branch with no commit yet. `tests/test_question_gate.py::Test_main::test_refuses_on_a_branch_with_no_commit_yet` and `tests/test_implementer_mark.py::Test_main::test_accepts_a_smith_spawn_on_a_branch_with_no_commit_yet` were red before the fix, and `mutation-check` putting either reader back on `current_branch` turns its case red (executed by the smith). The two other callers stay on `current_branch`: `hooks/implementer-notice.py` runs only after a command that commits, when the branch is born, and a failed first commit owes no notice; `skills/code-review/scripts/chain_check.py` reads `GITHUB_HEAD_REF` first, and locally a branch with no commit has no range to judge (read by the smith and the orchestrator). The orchestrator re-ran the five touched modules at 131706f2: 456 passed (executed).

Round 4 finding 1 has one cause. `routing.current_branch` runs
`git rev-parse --abbrev-ref HEAD`, which fails on a branch with no commit,
so it returns "" there as it does on a detached HEAD. The fix pass closed
that cause in `worktree_branch`, which the edit gate and `seal no-work-item`
call. Two other readers still call `current_branch` directly:
`routing.declared`, which `hooks/question-gate.py:101` reads, and
`hooks/implementer-mark.py:68`. Both read the branch before the first
commit in the case this fix opened. A session in a new repository can now
write its declaration and edit on `main` before any commit, because the
edit gate reads the declaration through `worktree_branch`. The other two
readers still see no branch there.

The probe built a repository with a local root (`.git/seal/`), no commit,
and a declaration naming `main` with `Automation` `yes`. In that repository
the declaration is never committed, so the branch stays unborn until the
first commit of the work. The probe found the following. The edit gate let
an edit through with no no-work-item record, because the declaration names
`main`. `routing.declared` returned None. The question gate was silent for
an ordinary `AskUserQuestion` call, which is the wrong allow its docstring
calls "the stopped run this gate exists to end". A `specseal:smith` spawn
through `hooks/implementer-mark.py` wrote no mark. After the first commit
the question gate denied the same call. `implementer-notice.notify` then
printed "no smith was spawned on this branch", which is false. A control
repository with a commit before the same steps denied the question and
printed no notice. Both readers called `current_branch` at `main` already.
The defect is reachable now because the edit gate accepts an unborn branch
and these two readers do not.

`hooks/question-gate.py:7-11` also says the declaration resolves "the way
`hooks/routing.py` resolves them for every reader". Since phase 8 that is
false for a paused rebase, and since `6030237f` for an unborn branch too.
`routing.py` holds two resolutions, and `declared` uses the narrower one.
With the fix below, the sentence becomes true.

The fix resolves both readers through `worktree_branch`. It has one more
effect: during a paused rebase of a branch declared `Automation` `yes`, the
question gate now refuses a question. That matches the gate's stated
failure direction, "it blocks more". `hooks/implementer-notice.py:150` can
keep `current_branch`, because a commit has just been made where it runs,
so the branch is born. Applied in a `--no-local` clone at `9fa3c247`, the
fix made the probe's question deny before the first commit, made the
smith's mark stand for `main`, and left the notice silent. The modules
`tests/test_question_gate.py`, `tests/test_implementer_mark.py`,
`tests/test_implementer_notice.py`, `tests/test_routing.py`,
`tests/test_routing_edit_gate.py` and
`tests/test_the_implementer_is_recorded.py` passed, 126 cases (executed).

```python
# hooks/routing.py
def declared(cwd, root):
    """The routing answer in force for `cwd`, or None when there is not one.
    The branch is resolved as the edit gate resolves it
    (`worktree_branch`), so a branch with no commit yet and a paused rebase
    read the declaration that names them."""
    return for_branch(root, worktree_branch(cwd))
```

```python
# hooks/implementer-mark.py, line 68
    implementer.write(cwd, routing.worktree_branch(cwd), mark)
```

Two cases belong with the fix, each seen red against `9fa3c247`. In
`tests/test_question_gate.py` `Test_main`: in a repository made with
`git init -b main` and no commit, a declaration naming `main` with
`Automation` `yes` makes the gate deny an ordinary question. In
`tests/test_implementer_mark.py` `Test_main`: in the same kind of
repository, a smith spawn leaves a mark that stands for `main`. Neither
fix crosses an OS boundary that `current_branch` does not already cross.

## Confirmations

confirms: round-4#1
The close holds. In a repository made with `git init -b main`, holding
`seal/` and no commit, `current_branch` returned "", `unborn_branch`
returned `main`, and `worktree_branch` returned `main`. Before any record,
the gate denied the edit with the text for a named branch, which names
`main`, not with the detached text. `seal no-work-item` under `s1` exited 0,
recorded `main\n`, and its success line names `main`. After that the gate
let `s1` edit and denied `s2`. After the first commit `s1` still edited.
This reruns round 4's case 5 against `9fa3c247` (executed: the round-5
probe). The two new cases are red without the fallback. With
`or unborn_branch(cwd)` removed from `hooks/routing.py:361` in a
`--no-local` clone at `9fa3c247`, both
`tests/test_seal.py::Test_no_work_item::test_accepts_a_branch_with_no_commit_yet_and_writes_it`
and
`tests/test_routing_edit_gate.py::Test_main::test_accepts_the_recording_session_on_a_branch_with_no_commit_yet`
failed (executed). The smith's account says the same. This round did not
rerun its `mutation-check` on `--short`. `phases/phase-8.md` now states the
limit as closed by this fix, and that matches the code (read).

confirms: round-4#2
The close holds. `spec.md:176-179` now says the detached refusal's "ways
on start by checking out a branch, and they name `seal no-work-item` only
as a run on that branch". `plan.md:59` says the refusal "names checking out
a branch before `seal no-work-item`". Both match the texts at
`hooks/routing-edit-gate.py:85-91` and `:103-108`. Each says to check out a
branch first, then run `seal no-work-item` on it, and that it records
nothing on a detached HEAD (read). The docstring at
`tests/test_routing_edit_gate.py:197-200` now reads the same way. Its body
pins both texts whole through `attended_detached` and `pressed_detached`
(read). `git grep -n "in place of"` over the work item finds the old phrase
only where `phases/phase-8.md:28` and round 4 quote it as history
(executed). The probe's detached case gave the same result: on a detached
HEAD at a commit no declared branch holds, `symbolic-ref` exited 1 with no
output, `seal no-work-item` exited 1, and the gate's refusal names checking
out a branch (executed).

confirms: none
`unborn_branch` works correctly with the paths the spawn prompt named,
executed by the round-5 probe against the tree at `9fa3c247`. During a
paused rebase of `A`, `symbolic-ref -q --short HEAD` exited 1, because a
rebase detaches HEAD. So `worktree_branch` fell through to `rebase_branch`
and named `A`, `seal no-work-item` recorded `A`, and the gate let that
session edit. An orphan branch made with `git switch --orphan` in a
repository with history resolved to its name. In a linked worktree added
with `git worktree add --orphan -b neu`, the linked worktree resolved `neu`
and the main worktree `main`. A `seal no-work-item` run in the linked
worktree let that session edit there and not in the main worktree.
`detached_on_declared` is reached only where `worktree_branch` returned ""
(`hooks/routing-edit-gate.py:254-258`, read). An unborn branch now has a
name, so that path never meets it, and before the fix the path returned
False there anyway, because `merge-base --is-ancestor HEAD` cannot resolve
an unborn HEAD.

confirms: none
`symbolic-ref --short` on a HEAD that points outside `refs/heads/` agrees
with `current_branch`, executed by the round-5 probe. `git symbolic-ref
HEAD` refuses a target outside `refs/` with exit 128. Pointed at an
existing `refs/remotes/origin/feat` or `refs/tags/v1`, both readers return
`origin/feat` and `v1`. Pointed at a missing ref outside `refs/heads/`,
`current_branch` returns "" and `unborn_branch` returns the short name, such
as `gone` or `other/x`. Only `rebase_branch` keeps its `refs/heads/` prefix
check, because a rebase always writes a branch ref to `head-name`. Only a
plumbing `symbolic-ref` call can point HEAD at a missing ref outside
`refs/heads/`. A switch or checkout cannot. A name read there lets an edit
through only after a declaration names it or `seal no-work-item` records
it, and both are deliberate. So this is no finding. With a tag `main`
beside an unborn `main`, `unborn_branch` returns `heads/main`. A born
`main` beside a tag `main` gives `heads/main` from `current_branch` too.
So the fallback gives the same name before and after the first commit.

confirms: none
The sentences that state how the branch is resolved still hold. The
docstring of `seal no-work-item` at `skills/implement/scripts/seal.py:2433-2435`
and the parenthesis at `spec.md:68` both say "the branch checked out, else
the branch a paused rebase names". Git calls a branch with no commit
checked out: HEAD names it, and `git status` reports it as the current
branch. So neither sentence became false, and settle copies no wrong
sentence (read). The gate's module docstring, `hooks/routing-edit-gate.py:21-27`,
says only a detached HEAD names no branch, which still holds (read).

confirms: none
The two new cases were read against their groups. `Test_no_work_item` in
`tests/test_seal.py` had no case for a repository with no commit. The new
case pins the recorded line `main\n` and the exit code. `Test_main` in
`tests/test_routing_edit_gate.py` holds the detached and paused-rebase
cases. The new case is the only one in which the gate reads a record on an
unborn branch (read: `tests/test_seal.py:3246-3256`,
`tests/test_routing_edit_gate.py:333-345`). `bin/test-layout --pairs`
names no pair in either module. The one pair in `tests/test_routing.py`
`Test_parse` predates this range (executed).

Carried from round 4, not re-established: the S4 record behaviour on a
branch with a commit, the prune, and the linked-worktree root. This range
changes none of their code. The `## Not judged` rows on Q1, Q2, Q3, the
GitHub rebase and the edit-tool matcher are also carried from round 4.
Every other fact above was established in this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at `9fa3c247` | the branch | the orchestrator's broad run |
| Whether `mutation-check` dropping `--short` turns the `seal` case red, as the smith reports; this round reran only the fallback's removal | `tests/test_seal.py:3246` | the smith's record in `phases/phase-8.md`, read by the sealer |
| Q3's live measurement, carried from round 4 | `questions.md` Q3 | the orchestrator, who ran it |
| Whether GitHub's server-side rebase of a pull request's head records a committer other than the author | `skills/code-review/scripts/chain_check.py:2087-2088` | the orchestrator, on a live pull request |
| Q1 and Q2, both open; the build took default (a) of each | `questions.md` Q1, Q2 | the owner |
| Whether the harness has an edit tool that `Write\|Edit\|NotebookEdit` does not name | `hooks/hooks.json` `pre-edit` matcher | the owner, in a live session |

## Probes

| Command | Result |
|---|---|
| `python3 <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-5/test_tmp_round5.py` | It built repositories under the round's scratch directory, with an empty global git config, and drove git from Python. It ran `hooks/routing-edit-gate.py`, `hooks/question-gate.py`, `hooks/implementer-mark.py` and `seal.py no-work-item` from the tree at `9fa3c247`, and imported `routing` and `implementer-notice`. Case A, unborn `main` in a shared root: as the first confirmation states. Case B, unborn `main` in a local root with a declaration naming `main` and `Automation` `yes`: edit allowed, `declared()` None, question silent, no smith mark; after the first commit the question was denied and the notice printed "no smith was spawned on this branch". Case B2, the same steps after a first commit: question denied, no notice. Case C, a detached HEAD: `symbolic-ref` exit 1, `seal` exit 1, refusal names checking out a branch. Case D, a paused rebase of `A`: `symbolic-ref` exit 1, `worktree_branch` `A`, `seal` recorded `A`, edit allowed. Case E, HEAD pointing outside `refs/heads/`: as the fourth confirmation states. Case F, an orphan branch: `neu`. Case G, an unborn `main` beside a tag `main`: `heads/main`, the same as `current_branch` on a born `main`. Case H, a linked worktree on an orphan branch: `neu` there, `main` in the main worktree, the record allowed the edit only in the linked worktree. Its repositories were removed by the script. |
| The same script with the clone's tree as its argument, after `routing.declared` and `hooks/implementer-mark.py:68` were changed to `worktree_branch` in a `--no-local` clone at `9fa3c247` | Case B: `declared()` found the declaration, the question was denied before and after the first commit, the smith mark stood for `main`, and the notice was silent. |
| `.venv/bin/python -m pytest -q -p no:cacheprovider -n auto tests/test_question_gate.py tests/test_implementer_mark.py tests/test_implementer_notice.py tests/test_routing.py tests/test_routing_edit_gate.py tests/test_the_implementer_is_recorded.py` in that clone with the fix applied | 126 passed |
| `.venv/bin/python -m pytest -q -p no:xdist -p no:cacheprovider` over the two new cases in a `--no-local` clone at `9fa3c247` with `or unborn_branch(cwd)` removed from `hooks/routing.py:361` | 2 failed |
| `bin/test -n auto -q tests/test_routing_edit_gate.py tests/test_seal.py tests/test_routing.py tests/test_question_gate.py tests/test_implementer_mark.py tests/test_implementer_notice.py` at `9fa3c247` | 471 passed |
| `bin/test-layout --pairs` | exit 0; no pair in `tests/test_seal.py` or `tests/test_routing_edit_gate.py`, and the one in `tests/test_routing.py` `Test_parse` predates this range |
| `bin/rules --check` | exit 0 |

The clone, the probe script and the files the runs wrote under the round's
scratch directory were removed before hand-back.
