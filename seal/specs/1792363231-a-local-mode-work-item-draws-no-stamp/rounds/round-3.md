# 1792363231-a-local-mode-work-item-draws-no-stamp — review round 3

target: 68a67d6b, fixes 339ac7dc..68a67d6b

## Findings

### 1. A sealed item copied onto its own declared branch in a second clone is refused and recorded, and the new audit the refusal asks for draws a second stamp

severity: should
location: `docs/the-review-record.md:302-304`, `docs/the-review-record.md:398-403`, `skills/verify/scripts/seal_stamp.py:945-947`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
verdict: open
reopens: round-2#2

Why the close does not hold. Round 2's finding 2 was a `sealed` brought by a
plain commit from a commit no ref holds, which writes a record and then
draws a second stamp. 061dfdc2 closes it on `main`, and the case
`cherry-pick -n of a commit no ref holds` holds that half: the gate stays
quiet off the declared branch, and #975's ancestry refusal queues nothing.
The same copy onto the item's own declared branch is the gate's refused
shape. The gate refuses it and records `<id>-<target>`. The refusal text
then tells the session to "spawn the sealer again at HEAD". That audit's
chain entry is skipped, and `sealed_before` finds no `sealed` in this
clone's history, because the copy never landed. So the new audit draws a
second stamp.

The plan's walk (`plan.md` §*Technical context*) puts round 1's and round
2's copies on `main` only. The documents name the class as a `sealed`
"copied here by hand" (`docs/the-review-record.md:302`,
`seal_stamp.py:945`). Round 1 found that same wording too narrow for copies
made by git commands.

Executed. The probe `tests/test_tmp_976_round3.py` was run once and deleted.
It drew in the first clone, made a `--no-local` second clone, and reset that
clone's `feat/x` to `origin/main`, as a local branch made before the work
was pulled. It then brought the item over in two ways:

- `git checkout origin/feat/x -- seal/specs/<item>`;
- `cherry-pick -n` of the two item commits by SHA, after deleting every ref
  that held them, as `fetch --prune` leaves them.

In both, `pre_commit` exited 1 and wrote one record. The new audit staged
at HEAD with `; earlier run: <target> sealed` then passed the gate, and its
commit drew. That is a second stamp beside the first clone's. At 769f2aa4
the same copy landed, and the chain counted the copied run, so nothing drew
a second time. The gate's record is what opens this path.

Why it matters. It needs a second clone that brings a sealed item onto a
copy of its branch that lacks the audited commit. That is the shape #975 Q9
already accepts as "a second seal on a copy of the branch that had not
fetched the first". So the fix asked here is the statement, not a guard. A
guard would have to tell this copy from a stale row the orchestrator's own
clone writes after a push and a rebase, and both name a commit some ref
holds. The statement has to say what the owner is accepting: any copy,
whatever made it, and that the refusal's own way on is the step that
draws the second stamp.

```markdown
fetched the first. A `sealed` that drew in another clone, brought onto a
copy of its declared branch that does not hold its audited commit, by hand
or by `checkout`, `cherry-pick -n` or `merge --squash`, is refused at its
commit and recorded, and the new audit the refusal asks for draws again
there; it joins that class. The
```

```python
# `sealed` that drew in another clone, brought onto a copy of its declared
# branch that does not hold its audited commit (by hand, `checkout`,
# `cherry-pick -n` or `merge --squash`), refused by the gate and recorded,
# draws again at the new audit the refusal asks for, and joins it.
```

The unchecked paragraph's "A wrong row that names, by coincidence, …"
sentence (`docs/the-review-record.md:400-403`) gains the same shape beside
the coincidence. A case pins the limit the way
`test_a_sealed_committed_past_the_stub_keeps_the_gap` pins its own: the
probe's `checkout` shape, asserting the record and the second file, so that
a change which closes it is seen.

answer:

### 2. A conflicted merge that brings a correct sealed from the merged branch is refused, and the refusal's only way on cannot be taken mid-merge

severity: should
location: `hooks/commitgate.py:283`, `docs/the-commit-gate-inside-git.md:109-110`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
verdict: open

Why it matters. `guarantee_off_history` asks whether the target is an
ancestor of `HEAD` (`commitgate.py:283`). A commit that concludes a merge
has two parents, and its history holds the merged side too. On the declared
branch, a merge whose other side carries the item's guarantee, sealed over
a commit of that side, stages the guarantee against `HEAD`. The gate then
refuses a verdict the commit's own history will hold, and that the pull
request's check accepts. `questions.md` Q5 chose no waiver on the premise
that no commit of this shape is one the pull request would accept, and this
one is. The way on the text names, a new audit at HEAD, cannot be taken
while the merge is unfinished. What is left is `--no-verify` or editing
the row, and the text forbids editing the row. A clean merge runs no
`pre-commit` (no `pre-merge-commit` stub exists under `hooks/git/`), so only
a merge with a conflict meets this.

Executed in the same probe. `declared_guaranteed()` made the repository. A
branch `side` committed work and then a `sealed` over that work, which drew.
`feat/x` committed a conflicting change. `git merge side` exited 1, and the
conflict was resolved and staged. `pre_commit` then exited 1, naming the
side's commit as one "the history of this one does not hold", and it
recorded `<id>-<that commit>`.

Read: the record does no harm here. This clone holds the side's values
file, so `already_queued` blocks, and the merged history carries the side's
`sealed` for `sealed_before`. The defect is the refusal.

The fix asks the merged head too. A `merge --squash` writes no `MERGE_HEAD`,
so it is still judged against `HEAD` alone, as it should be.

```python
        # A merge's commit holds both parents' histories, so a target the
        # merged side holds is in this commit's history too. A squash
        # writes no MERGE_HEAD and is judged against HEAD alone.
        heads = [head]
        merging = gate.git(["rev-parse", "-q", "--verify", "MERGE_HEAD"], cwd)
        if merging and merging.strip():
            heads.append(merging.strip())
        if any(
            gate.git(["merge-base", "--is-ancestor", target, h], cwd) is not None
            for h in heads
        ):
            continue
```

`docs/the-commit-gate-inside-git.md:109` then reads "`git merge-base
--is-ancestor <target>` exits 0 for neither `HEAD` nor, while a merge is
being concluded, `MERGE_HEAD`". The probe's merge shape is planted as a
given of `test_the_guarantee_refusal_is_quiet_off_its_one_fact`, red at
68a67d6b.

answer:

### 3. An amend that folds the guarantee into the audited commit passes the gate, lands a row its history does not hold, and no stated limit names it

severity: should
location: `docs/the-review-record.md:392-394`, `docs/the-commit-gate-inside-git.md:122-123`
verdict: open

Why it matters. `pre-commit` runs before an amend with `HEAD` still at the
commit being replaced, and nothing in its environment says the commit is an
amend. So a `sealed` over `HEAD`, folded into `HEAD` by
`git commit --amend`, passes the ancestry check. The commit that lands has
`HEAD^` as its parent and no longer holds the audited commit. After that,
`post-commit`'s ancestry refusal queues nothing, `sealed_before` counts the
landed `sealed`, and the new audit draws nothing. That is a missing stamp,
Q8's direction, but it goes through the gate. The limits the documents
state are all places where the stub does not run (`--no-verify`, a foreign
slot, an older plugin, a person's own commit, an unreached clone). A reader
told the gate stops every such row on the declared branch would not look
for this one.

Executed in the same probe. `declared_guaranteed()` made the repository,
and a `sealed` over `HEAD` was staged. `pre_commit` exited 0. `git commit
--amend --no-edit` then left the audited commit out of the history, and
`post-commit` queued nothing.

Read: the gate cannot tell an amend from a plain commit inside
`pre-commit`, so the fix is the stated limit. The pull request's check still
refuses the landed row as stale, which forces a new audit in shared mode.

```markdown
was committed past the commit gate: under `--no-verify`, in a foreign hooks
slot, under a plugin older than the gate, as a person's own commit, or in a
clone no session has reached (`docs/the-commit-gate-inside-git.md`); or
where an amend folded the guarantee into the very commit it audited, which
`pre-commit` sees as that commit's child and cannot tell from a plain one.
```

The same clause joins `docs/the-commit-gate-inside-git.md:122` ("Where the
stub does not run, … the row lands"), as the one shape where the stub runs
and the row still lands.

answer:

## Confirmations

confirms: round-2#1
The close holds. 061dfdc2 deleted `_guarantee_on_another_ref` with
`_stamped_nowhere_else`, `plain_commit` and `post-commit`'s record write.
The gate records the row it refuses, and it reads no other ref
(`hooks/commitgate.py:232-290`, read). Executed:
`test_a_tracking_ref_left_by_a_rebase_withholds_nothing` passed in the
narrow run below. It pushes, rebases, refuses `deadbee` with a record, and
draws one stamp at the new audit. A tracking ref holding a pre-rebase
`sealed` that drew withholds nothing either, and `sealed_before` counts the
rebased copy: `test_a_refused_row_over_a_drawn_seal_does_not_draw_again`
passed. Its docstring says it was seen red with `sealed_before` replaced by
`False` (read).

confirms: none
Round 1's three copies onto `main`, and round 2's pruned pick onto `main`,
land quiet and record nothing, and their re-seals queue nothing. The four
`_copied` givens of `test_the_guarantee_refusal_is_quiet_off_its_one_fact`
passed (executed). Finding 1 is the declared-branch half.

confirms: none
Round 5's two shapes are untouched. Executed: an AST comparison of the
fourteen #975 cases found 14 of 14 bodies identical at 769f2aa4 and
68a67d6b. `git diff --stat 769f2aa4 68a67d6b -- hooks/git/` names
`pre-commit.py` alone, its docstring. `git grep` for `PLAIN_COMMITS`,
`_stamped_nowhere_else` and `_guarantee_on_another_ref` in `*.py` found
none. Its one hit is `test_a_plain_commit_carries_no_chdir`, an unrelated
name containing `plain_commit`.

confirms: none
The gate is quiet where the brief asked about a wrong refusal, apart from
finding 2's merge:

- a correct `sealed` at `HEAD` or at an ancestor;
- the sequencer's own commit;
- an unborn branch;
- a `seal_stamp.py` that will not load;
- no `routing.md`, or no `Branch` row, in the index.

Each is a given of `test_the_guarantee_refusal_is_quiet_off_its_one_fact`,
and each passed (executed). Read: a guarantee staged for another item is
judged against that item's own `routing.md`, so an item declaring another
branch is skipped (`commitgate.py:276-280`). A rebase's picks run on a
detached `HEAD`, where `routing.current_branch` answers "" and nothing is
judged.

confirms: none
On the declared branch, a refusal leaves the run a way on that needs no
person: a new audit at `HEAD`, whose commit passes the gate and draws once.
Executed: `test_a_sealed_over_a_commit_the_branch_does_not_hold_is_refused_at_the_commit`,
in both forms, passed. The orchestration's sealer step names that way on
(`skills/code-review/orchestration.md:226-230`, read). Finding 2's merge is
the one shape found with no way on but a person.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. The suite stays `unverified` here | the branch at 68a67d6b | the orchestrator's `broad-gate --base <base> --record <item>`, after the rounds settle |
| `git show :<path>` reading the right index for a pathspec commit on git versions other than the ones #692 measured (`questions.md` Q6) | `hooks/commitgate.py:267` | the orchestrator, from CI's legs |
| The latency figures phase 6 wrote into `docs/the-commit-gate-inside-git.md` | `docs/the-commit-gate-inside-git.md` latency bullet | read here; the sealer samples them |
| The first real refusal read on a screen, and the local `NOT_ON_BRANCH` line as the edit hook's message | `hooks/gate.py#guarantee_refusal`, `seal_stamp.NOT_ON_BRANCH` | the owner, on the first run after the release |
| An octopus merge, whose `MERGE_HEAD` holds several heads; finding 2's fix reads the first | `hooks/commitgate.py:283` | the fix pass, if it widens the fix |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_976_round3.py -q -s -p no:xdist` (probe file written, run once, deleted) | 4 passed. A copy by `checkout` onto the second clone's own `feat/x`: gate exit 1, one record, the new audit's gate exit 0, and the second clone drew while the first had drawn. The same for `cherry-pick -n` by SHA with every holding ref deleted. An amend folding a `sealed` over `HEAD`: gate exit 0, the target out of the landed history, nothing drawn. A conflicted merge of a side branch whose `sealed` drew: gate exit 1 naming the side's commit, one record |
| `bin/test tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_the_commit_gate_decides_at_the_commit.py -q` | exit 0, 286 passed |
| `python3 -I <scratchpad>/bodies.py <worktree> 68a67d6b` (an AST comparison, deleted) | 14 of 14 #975 case bodies identical to 769f2aa4 |
| `git diff --stat 769f2aa4 68a67d6b -- hooks/git/` | `hooks/git/pre-commit.py` alone, 12 lines |
| `git grep -n -e plain_commit -e _stamped_nowhere_else -e _guarantee_on_another_ref -e PLAIN_COMMITS 68a67d6b -- '*.py'` | one hit, `tests/test_gate_judges_the_repo_it_commits_to.py:144`, an unrelated test name |
