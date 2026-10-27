# Review round 2: 1793057293-root-migrate-removes-every-directory-it-emptied

target: f294b3bd, fixes d3f6aaf7..f294b3bd

This round verifies round 1's fix pass. It read the fix range
`d3f6aaf7..f294b3bd` in a `git clone --no-local` of the branch at
`f294b3bd`, and then the whole diff `fa7d1374...f294b3bd` only for what the
fix range broke. No `seal/parity.md` is declared, so no parity comparison
applies. Carried from round 1 and not re-established: the link probes (a
tracked directory link is moved by `git mv`, an untracked one is not
entered), the simulated failing `os.rmdir` on macOS, and the CI runs
40421812732 and 40423069012. Re-run this round: round 1's five mutants, the
two modules, and the test-layout pairs.

## Findings

### 1. The first divergence row of `overview.md` quotes a frame sentence and a docstring that the fix range both rewrote

severity: should
location: `seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/overview.md:17`
evidence: executed `git grep -n "not something git checks out" f294b3bd -- seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/spec.md seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/overview.md`, `git diff d3f6aaf7..f294b3bd -- seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/spec.md hooks/root-migrate.py`
verdict: open

The row says *In* item 4 of `spec.md` reads "a directory link or a Windows
junction placed under `src` by hand is not something git checks out, and
the walk is not guarded against one". It says the docstring "names only" the
junction. Neither holds at `f294b3bd`. The `git grep` finds the quoted
sentence only in the row itself. beab5ed4 rewrote *In* item 4
(`spec.md:54-62`) to say what the code does: a junction is walked into, and
a directory link needs no sentence. 3fd067a8 then gave the docstring a
second limit (`hooks/root-migrate.py:362-367`), so it no longer names only
the junction. The frame and the code now agree on links, and the row records
a divergence that is gone.

Why it matters: the sealer and the next round read this table as the record
of where the build departed from the frame. A reader who opens *In* item 4
to check the quote finds other words, and must guess which document is
wrong. Contract rule 19 asks that the commit rewriting the frame sentence
also remove what stood on the old one. beab5ed4 touched `spec.md`,
`plan.md` and `questions.md`, and left this row.

The fix deletes the row. The facts its grounds gave are now in *In* item 4,
so nothing is lost.

```diff
--- a/seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/overview.md
+++ b/seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/overview.md
@@ ## Where spec and implementation diverged
 | Divergence | Spec says / code did | Chosen | Grounds |
 |---|---|---|---|
-| What the limit sentence in `move`'s docstring names | *In* item 4: "a directory link or a Windows junction placed under `src` by hand is not something git checks out, and the walk is not guarded against one" / the docstring names only "a Windows junction placed under `src` by hand, which git does not track", which "is walked into, and the empty directories behind it are removed too" | the code | Git tracks a symbolic link, so "git checks out neither" is false for one, and a tracked link is moved by `git mv` with the other files before the walk. An untracked directory link is not entered: `os.walk`'s bottom-up branch says "exclude symlinks to directories if followlinks is False". Its parent's fresh listing names it, so the parent stays. A junction is not a symbolic link to `DirEntry.is_symlink()`, so the walk enters it, which is the limit `plan.md` *Technical context* describes (`phases/phase-2.md`) |
 | Whether S3 stands as a case of its own | ...
```

answer:

### 2. The docstring gained a second limit that the frame's one limit sentence does not name, and no divergence row records it

severity: should
location: `seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/overview.md:13-18`, `hooks/root-migrate.py:358-367`
evidence: executed `grep -n "removal fails\|holds it open" seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/overview.md`, `git diff d3f6aaf7..f294b3bd -- hooks/root-migrate.py seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/overview.md`
verdict: open
regression: round-1

The unit is `move`'s docstring at `hooks/root-migrate.py:358-367`, with the
`overview.md` tables 3fd067a8 changed beside it. `plan.md:83`, the phase 2
row, says the docstring sentence is rewritten "with the limit sentence
(*In* item 4)". `spec.md:54-62` says "One limit sentence follows it", the
junction. Round 1's fix pass, answering that round's Not judged row and no
finding, added "unless its removal fails" to the removal sentence and a
second limit, "Where the removal of a directory fails ... that directory and
every one above it stay". It recorded that under *Not verified*
(`overview.md:26`) and in `phases/phase-2.md:65-76`. It wrote no row under
*Where spec and implementation diverged*. The search finds only the *Not
verified* row. So the defect came from how the fix was written, not from the
frame: the fix departed from the frame and did not record the departure as
one.

Why it matters: the table is where the sealer looks for each place the code
departs from the frame, with both sides quoted and which side won. Round 1
held S3's removal to that shape, and `overview.md:18` meets it. A *Not
verified* row says what nobody ran. It does not say that the frame named one
limit and the code states two, or why the code won. The change itself
follows the owner's direction for edges the one-issue flow cannot produce
(`spec.md:22`), and this round confirms it below. Only the record is
missing.

```diff
--- a/seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/overview.md
+++ b/seal/specs/1793057293-root-migrate-removes-every-directory-it-emptied/overview.md
@@ ## Where spec and implementation diverged
 | Whether S3 stands as a case of its own | ...
+| What `move`'s docstring says where the removal of a directory fails | *In* item 4: every directory under `src` "holding nothing when the walk reaches it is removed", and "One limit sentence follows it", the junction's / 3fd067a8 adds "unless its removal fails" to that sentence and a second limit: "Where the removal of a directory fails, as on Windows when another process holds it open, that directory and every one above it stay, and nothing is removed by mistake." | the code | Round 1's Not judged row named the edge. Its probe simulated a failing `os.rmdir` on macOS: the directory and every one above it stayed, and nothing raised. The owner's direction (`spec.md` *Grounding*, last row) gives an edge the one-issue flow cannot produce a limit sentence and no guard (`phases/phase-2.md`) |
```

answer:

## Confirmations

confirms: round-1#1
The close holds. `Test_run_moves::test_accepts_an_item_merged_into_one_that_exists_and_takes_away_specs`
is gone: `grep -c merged_into_one_that_exists tests/test_root_migrate.py`
printed 0. Round 1's `evidence:` line was re-run over the whole module at
`f294b3bd`, with no `-k` because the case no longer exists. All five mutants
went red: the walk's removal, the test that keeps `src`, the `specs/`
cleanup in `run_moves`, the walk's direction, and the fresh listing. So the
module still catches each of them without S3. The two modules gave 78
passed, one fewer than round 1's 79. `.test_durations` holds no entry for
the case, and `test-layout --pairs` names no pair. `overview.md:18` records
the removal with both sides quoted. The *Not done* sentence that stood on
the case lost its clause in the same commit. A mutation score licenses
*tested*, not *safe*. Executed.

confirms: none
S3 standing in the frame holds as the frame's record of what was decided at
framing time. `skills/implement/SKILL.md` names the framer as `spec.md`'s
writer, and the builder's `overview.md` as where a departure is recorded,
"both sides quoted, which side won, and the grounds". `spec.md:97` (the S3
row), `spec.md:64` ("two are added") and `plan.md:82-83` are framing-time
decisions. The two phase rows are closed records that carry their commits.
`overview.md:18` quotes S3's row against the deletion and names round 1's
mutation run as the grounds. beab5ed4 took the other path for the link
sentence and rewrote the frame in place. That path suits a sentence that was
false when it was framed, as "git checks out neither" was. S3 was a
decision that was true when framed, and a later round reversed it. The two
paths can stand side by side. What beab5ed4 left behind is finding 1. Read.

confirms: none
beab5ed4's rewritten frame sentences agree with the code. `spec.md:58-62`,
`plan.md:58-66` and `questions.md:41-46` say a junction is walked into, git
moves a tracked directory link before the walk, and the walk does not enter
an untracked one. The docstring's junction limit says the same
(`hooks/root-migrate.py:363-365`). The link facts are carried from round 1's
probe and were not re-run. Read.

confirms: none
The second limit holds in substance. At `hooks/root-migrate.py:400-405` one
`try` passes over an `OSError` from `os.listdir` or `os.rmdir`. A directory
whose removal fails stays, so its parent's fresh listing names it, and every
directory above stays too. Nothing is removed that holds anything. The
changelog fragment's *Limits* line carries the same sentence word for word.
The walk's code is unchanged in the fix range: 3fd067a8 touches only the
docstring. The smith's reading of round 1's delete-pending clause also
holds. The docstring's test is that a directory "holds nothing when the walk
reaches it" (`hooks/root-migrate.py:360-361`). Where a removed child is
delete-pending and still listed, its parent holds an entry at that moment.
By the docstring's own test it is not removed. The removal sentence already
states that case, and the second limit does not need to. Read. Neither case
ran on Windows (*Not judged*).

confirms: none
The fix range broke nothing else in the whole diff. Its code change is
3fd067a8's docstring and e6d6fcf2's deleted case. `ruff check` and
`ruff format --check` over `hooks/root-migrate.py` and
`tests/test_root_migrate.py` exited 0. The deleted case left no helper or
import unused. The two modules passed. `phases/phase-2.md:65-76` labels the
new paragraph `read` and the Windows behaviour `unverified`. Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The held-open limit and the delete-pending case on Windows. This round read both and ran neither, and round 1 simulated only the failing `os.rmdir`, on macOS | `hooks/root-migrate.py:358-367`, `hooks/root-migrate.py:400-405` | the repository owner, as `overview.md` *Not verified* names |
| The junction limit, carried from round 1 and still not run on Windows | `hooks/root-migrate.py:363-365` | the repository owner, as `overview.md` *Not verified* names |
| A `tests` run on CI at `f294b3bd`. `gh run list` for the branch shows runs at `07638965` and `d3f6aaf7` only. The fix range changed a docstring, deleted one case and changed records | the branch's `tests` workflow | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three | `broad-gate.md` | the orchestrator, by `broad-gate` once the rounds settle |
| `questions.md` Q2, the line for a moved item's directory that an ignored file keeps | `questions.md` Q2 | a person, at the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_root_migrate.py tests/test_the_root_migrates_itself.py -q -p no:xdist` | exit 0, 78 passed |
| `bin/mutation-check hooks/root-migrate.py --replace "                os.rmdir(here)" "                pass" --replace "if not os.listdir(here):" "if not os.listdir(here) and here != under(root, src):" --replace "    for old in (OLD_HOME, OLD_ITEMS):" "    for old in (OLD_HOME,):" --replace "topdown=False" "topdown=True" --replace "if not os.listdir(here):" "if True:" --tests "bin/test tests/test_root_migrate.py -q -p no:xdist -x"` | exit 0, "5 mutants, 5 red, 0 SURVIVED, 0 with no verdict"; the clone clean afterwards |
| `bin/test-layout --pairs tests/test_root_migrate.py` | exit 0, 1 file read, 0 pairs |
| `uvx ruff check tests/test_root_migrate.py hooks/root-migrate.py` and `uvx ruff format --check` over the same two files | exit 0 both; "2 files already formatted" |
| `grep -c merged_into_one_that_exists` over `tests/test_root_migrate.py` and `.test_durations` | 0 and 0 |
| `git grep -n "not something git checks out" f294b3bd` over the work item's `spec.md` and `overview.md` | one hit, `overview.md:17` |
| `grep -n "removal fails\|holds it open"` over the work item's `overview.md` | one hit, `overview.md:26`, the *Not verified* row |
| `gh run list --branch fix/1016-root-migrate-removes-every-directory-it-emptied --limit 5` | two `tests` runs: 40423069012 at `d3f6aaf7`, success; 40421812732 at `07638965`, failure |
