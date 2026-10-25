# Review round 4: 1792935671-the-routing-check-moves-to-the-sessions-tools

target: 13da3740, fixes 126ee7b5..13da3740

## Findings

The range holds six commits. `df57fee9` is the orchestrator's frame
amendment for `questions.md` Q7, answer (b). `67205fc3`, `587ac6ab`,
`8b6eac03`, `4876c64e` and `13da3740` are the smith's phase 8 (executed:
`git log --oneline 126ee7b5..13da3740`). Phase 8 is a build phase over a
design change, so its units are new work, and neither finding below names
an earlier finding as a regression or a reopening. The code units are
`hooks/routing.py#rebase_branch` (moved from the gate), `#worktree_branch`,
`#no_work_item_branches`, `#no_work_item` and `#record_no_work_item`; the
gate's split refusal texts and `#reason`; and `seal no-work-item` in
`skills/implement/scripts/seal.py` (executed: `git diff 126ee7b5..13da3740 -- hooks skills/implement/scripts/seal.py`).

### 1. On a branch with no commit yet, `seal no-work-item` says HEAD is detached and records nothing, so the route that worked at `126ee7b5` is closed there

severity: should
location: `hooks/routing.py:336-341`, `skills/implement/scripts/seal.py:2450-2456`, `hooks/routing-edit-gate.py:254`, `tests/test_seal.py:3246`
evidence: executed `python3 <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-4/test_tmp_round4.py`
verdict: open

The smith recorded this in `phases/phase-8.md` as a limit with no case, and
asked for a reader. The claim is that `routing.current_branch` returns ""
on an unborn branch, so `seal no-work-item` there reports a detached HEAD.
The probe confirms that claim, and it shows two more facts the phase record
does not state. First, the phase closed a route that worked before it. In a
fresh repository with `seal/` and no commit, `git rev-parse --abbrev-ref
HEAD` exits 128. The new `seal no-work-item` then exits 1 with "HEAD is
detached in ... Check out a branch there first", and the gate denies the
next edit with the detached text. The code at `126ee7b5`, run on the same
repository, records the session and lets the edit through. The declaration
route was already closed there, because `routing.for_branch(top, "")` names
nothing. So after this phase a session in a new opted-in repository has no
way to edit before its first commit. Second, both texts tell the model
something false. HEAD is not detached, and the advice to check out a branch
cannot be followed, because `main` is already checked out. The way on is a
first commit, and neither text names it.

A limit sentence does not fit this case. The only record of the limit is
`phases/phase-8.md`, and settle removes that file with the work item, so no
reader meets it later (`skills/code-review/SKILL.md` *A finding is not
closed too early* sends a limit to a skill's Known limits). The fix is also
small. `git symbolic-ref -q --short HEAD` names the unborn branch and exits
1 on a detached HEAD, both executed on git 2.50.1 in the probe. Placed in
`worktree_branch` after `current_branch`, it costs nothing on a branch with
a commit, because `current_branch` answers first there. It also leaves the
paused rebase to `rebase_branch`, because HEAD is detached during a rebase.

```python
def unborn_branch(cwd):
    """The branch HEAD names before its first commit, or "" where HEAD is
    detached or git cannot answer. `rev-parse --abbrev-ref HEAD` fails on an
    unborn branch; `symbolic-ref` reads the name HEAD points at without
    resolving it to a commit."""
    # Precondition: `git` on PATH, as `current_branch` assumes; no other OS
    # boundary is crossed.
    try:
        out = subprocess.run(
            ["git", "-C", cwd or ".", "symbolic-ref", "-q", "--short", "HEAD"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout.strip() if out.returncode == 0 else ""


def worktree_branch(cwd):
    """The branch CWD's worktree is on: the one checked out, the one an
    unborn HEAD names, else the one a paused rebase there names, or ""
    where none names one. The edit gate and `seal no-work-item` both resolve
    the branch here, so the record names the branch the gate reads."""
    return current_branch(cwd) or unborn_branch(cwd) or rebase_branch(cwd)
```

Two cases pin it, each seen red against the current code: in
`tests/test_seal.py` `Test_no_work_item`, a run in a repository with no
commit exits 0 and records `main`; in `tests/test_routing_edit_gate.py`,
an edit there is allowed after that run. If the fix pass keeps the limit
instead, the limit sentence and the corrected texts belong in `spec.md`
*Rule changes* *The edit check*, so they land in
`docs/the-routing-check.md` at settle.

answer:

### 2. The frame's sentence on the detached refusal reads two ways, and the code follows only one of them

severity: should
location: `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:175-178`, `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/plan.md:59`
evidence: read `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:175-178`, `hooks/routing-edit-gate.py:85-108`, `tests/test_routing_edit_gate.py:196-207`
verdict: open

This is the smith's first judgement call. `spec.md` *Rule changes*, the
paragraph opening *A refusal is a deny addressed to the model*, says that
where HEAD is detached the refusal "names checking out a branch in place of
`seal no-work-item`, which records nothing there". `plan.md` row 8 repeats
the phrase. Read plainly, "in place of" means the detached refusal does not
name `seal no-work-item`. The texts at `hooks/routing-edit-gate.py:85-108`
name it, as the step after checking out a branch. The test docstring at
`tests/test_routing_edit_gate.py:197-199` takes the other reading: "neither
text offers `seal no-work-item` where HEAD is".

The code's reading is the right one for Q7 (b). A session on a detached
HEAD whose change belongs to no work item needs the command once it has a
branch, and a refusal that dropped it would leave the model without its
second way on. So the code stays and the frame changes. The sentence is
`should` because it is the text settle copies into
`docs/the-routing-check.md`. A later round or a settle reader who compares
the code against it will find a divergence that the phase record no longer
explains, since settle removes that record. The repository's rule that text
an agent reads has one reading (`CLAUDE.md`) is what this breaks.

In `spec.md`, lines 175-178:

```markdown
    under the repository's root, and `seal no-work-item`. Where HEAD is
    detached, its ways on start by checking out a branch, and they name
    `seal no-work-item` only as a run on that branch, because on a detached
    HEAD it records nothing. Where the person
```

In `plan.md` row 8, the clause becomes: "and its detached-HEAD refusal
names checking out a branch before `seal no-work-item`, which records
nothing on a detached HEAD".

answer:

## Confirmations

confirms: none
The S4 claims the frame makes hold, executed by the round-4 probe against
the hooks and `seal.py` at `13da3740`. `seal no-work-item` run by `s1` on
`main` wrote `main\n`. The gate was silent for `s1` on `main` and denied
`s2` there. After a switch to an undeclared branch `B` of the same clone,
the gate denied `s1`, and the refusal named `` `B` ``. A run on `B` made
the record `main\nB\n`. After that, `s1`'s edits were allowed on both
branches. In a linked worktree on `C`, `--root` and a run from a
subdirectory both recorded `C` in the common directory's record. The gate
then allowed `s3` in that worktree and denied it in the main worktree. This
matches *Data & interfaces*: the edited file's worktree decides, at
`hooks/routing-edit-gate.py:254` (read).

confirms: none
A paused rebase records the branch it names. On a branch `A` stopped on a
conflict, `rev-parse --abbrev-ref HEAD` printed `HEAD`. `seal no-work-item`
recorded `A`, the gate let `s5` edit the conflicted file and denied `s6`.
After `rebase --abort`, `s5` still edited on `A`, and on `main` it was
denied (executed: the round-4 probe). `rebase_branch` moved to
`hooks/routing.py:305-333` unchanged except for its own `git` call, and the
gate keeps no copy (executed: `git grep -n "def rebase_branch"` finds only
`hooks/routing.py`).

confirms: none
The prune still runs and spares the session's own record. A second record
backdated two days was removed by the next run, and a fresh one was kept.
The running session's own record, backdated two days and re-run on the
branch it already named, was kept, still read `main\n`, and had a new
modification time. So the rewrite on every run does what
`hooks/routing.py:457-483` says it does (executed: the round-4 probe). A
detached HEAD outside a rebase made `seal no-work-item` exit 1 and left no
record file (executed: the same probe).

confirms: none
The smith's red-first claim holds. In a `--no-local` clone at `df57fee9`
with the three test modules from `13da3740`, the selection the phase record
names ran 11 failed and 13 passed. The 11 were the smith's 9 and the two
`tests/test_routing.py` cases, which fail against `df57fee9` because
`record_no_work_item` and `no_work_item` took no branch there. The phase
record says it showed those two red by `mutation-check`; this round did not
re-run the mutation (executed: `.venv/bin/python -m pytest -q -p no:xdist`
over the clone's three modules with the phase record's `-k` selection
widened by `empty_record or no_branch`). At `13da3740` the three modules
pass (executed: `bin/test -n auto -q tests/test_routing_edit_gate.py tests/test_seal.py tests/test_routing.py`,
419 passed).

confirms: none
The new tests were read against their groups. `Test_record_no_work_item`'s
refusal case holds the empty-branch guard of `record_no_work_item`, which
`seal no-work-item`'s own early exit hides from every other module. Its
accepts case overlaps the gate's
`test_a_record_naming_no_branch_lets_nothing_through` on the empty record's
read. Its write onto an existing empty file is new, so the case covers
something the group does not (read: `tests/test_routing.py:479-504`).
`bin/test-layout --pairs` names one pair, in `Test_parse` of
`tests/test_routing.py`, which predates this range (executed).

confirms: none
The smith's second judgement call holds. `docs/the-review-record.md` and
`templates/sdd-phase.md` define a Status cell as the commit that closed the
phase. Rows 6 and 7 name the last commit that delivers the phase, never the
commit that records it: `9a4e7cb7` sits before `863fd292` (read:
`git log --oneline 6f1bde24 -3`). Phase 8 delivers the prose too, so
`4876c64e` is its closing commit, and `phases/phase-8.md`'s `Commit` row
names the same hash.

confirms: none
The prose the phase names follows the record, and no clone-wide sentence
about it remains. `git grep -n "no-work-item"` outside the tests reaches the
two READMEs, the three skills, `seal.py`'s usage text and help, the
changelog fragment, the gate's docstring and the frame. Each sentence that
states what the record covers now says one session on one branch. Q7
answer (b) is stated in the frame at `spec.md` lines 24, 47, 68 and 156-167
(executed). The bold opening of *The edit check* at `spec.md:131-134` does
not name the branch. The paragraph below it does, and the opening is not
false, so it is no finding.

confirms: none
`bin/rules --check` exits 0 at `13da3740`, so every `check:` target the
frame and the build name still resolves (executed).

Carried from round 3, not re-established: the detached-HEAD exception for a
commit a declared branch holds (`detached_on_declared`), which this range
does not touch (read: the gate diff changes no line of it), and the
`chain_check.py` behaviour, which is not in this range. The `## Not judged`
rows on the GitHub rebase, Q1 and Q2, and the matcher are carried from
round 3 as well. Every other fact above was established in this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at `13da3740` | the branch | the orchestrator's broad run |
| Q3's live measurement, recorded as `yes` by the orchestrator with `claude -p` and `--plugin-dir` at `126ee7b5`; this round has no harness and did not run it again, and phase 8 changes no path the measurement depends on | `questions.md` Q3 | the orchestrator, who ran it |
| Whether GitHub's server-side rebase of a pull request's head records a committer other than the author | `skills/code-review/scripts/chain_check.py:2087-2088` | the orchestrator, on a live pull request |
| Q1 and Q2, both open; the build took default (a) of each | `questions.md` Q1, Q2 | the owner |
| Whether the harness has an edit tool that `Write\|Edit\|NotebookEdit` does not name | `hooks/hooks.json` `pre-edit` matcher | the owner, in a live session |

## Probes

| Command | Result |
|---|---|
| `python3 <scratchpad>/1792935671-the-routing-check-moves-to-the-sessions-tools/round-4/test_tmp_round4.py` | It built repositories under the round's scratch directory, drove git from Python, ran `hooks/routing-edit-gate.py` and `seal.py no-work-item` from the tree at `13da3740`, and for case 5 the same two from a `git archive` of `126ee7b5`. Case 1: one session on `main` and on `B`, and a second session; the decisions and records are as the first confirmation states. Case 2: a linked worktree on `C`. Case 3: a paused rebase of `A`. Case 4: the prune. Case 5: a repository with no commit, where `rev-parse --abbrev-ref HEAD` exited 128, `symbolic-ref -q --short HEAD` printed `main`, the new `seal no-work-item` exited 1 saying HEAD is detached and the gate denied, while the `126ee7b5` code recorded and allowed. Case 6: `symbolic-ref` on a detached HEAD exited 1 with no output. The scratch directory was removed. |
| `.venv/bin/python -m pytest -q -p no:xdist -p no:cacheprovider` over a `--no-local` clone at `df57fee9` holding the three test modules from `13da3740`, with `-k "no_work_item or detached or refuses_an_edit or automation_press or record_naming or empty_record or no_branch"` | 11 failed, 13 passed; the clone was removed |
| `bin/test -n auto -q tests/test_routing_edit_gate.py tests/test_seal.py tests/test_routing.py` | 419 passed |
| `bin/test-layout --pairs` | exit 0; the one pair it names is in `tests/test_routing.py` `Test_parse`, outside this range |
| `bin/rules --check` | exit 0 |
