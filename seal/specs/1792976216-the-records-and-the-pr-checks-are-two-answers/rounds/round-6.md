# Review round 6: 1792976216-the-records-and-the-pr-checks-are-two-answers

target: dc07a4ea, fixes 2cf62b72..dc07a4ea

## Findings

### 1. `seal pr-checks remove` drops a staged edit from the index when the working file was deleted by hand, where the same edit with the file present is refused

severity: should
location: `skills/implement/scripts/seal.py:2003-2038`, `tests/test_seal.py:3316-3360`, `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/spec.md:113-119`
evidence: executed `python3 test_tmp_remove_states.py`, `bin/mutation-check skills/implement/scripts/seal.py --replace 'if staged is None or PLUGIN_CLONE not in staged:' 'if PLUGIN_CLONE not in staged:' --tests "bin/test tests/test_seal.py -q -p no:xdist -k 'Test_pr_checks or Test_remove_workflow'"`, `git grep -n deleted_by_hand dc07a4ea -- tests`
verdict: fixed 1fb674c7
regression: round-5#1

The unit is the `kind == "absent"` arm of `remove_workflow`
(`seal.py:2003-2038`). Before `43975a1c` it removed nothing. `43975a1c`
added the `git rm` there, and `0aaa5e41` added the one test it applies: the
index copy carries the clone line (`seal.py:2015`). The frame, `spec.md`
*In* item 3 as amended at `a3fec95a` (lines 113 to 119), says the index copy
of a hand-deleted file is read "by the same rule as a working file". For a
working file staged and never committed, that rule removes only a copy that
is byte for byte what `install` writes now, and it refuses "a staged file
whose index or working copy differs" (lines 104 to 113). The fix read only
the clone line, so the defect comes from how the fix was written and not
from the frame. The frame's colon clause, "one this plugin wrote, carrying
the clone line", read alone names only the clone line, and that is the
reading the fix took. So the sentence also needs one reading. This is the
first regression routed on `remove_workflow` in this run: rounds 1 to 3 put
their `regression:` lines on other units, and round 5's finding 1 carried
none (executed, `grep -n regression: rounds/round-*.md`). The round cap's framer
route for a second regression on one unit does not apply.

What goes wrong. The probe walked each state through the clone's `bin/seal`
in scratch repositories (executed). Two states lose an edit that no other
copy holds.

- The person runs `install`, edits the workflow, stages the edit, then
  deletes the file by hand (status `AD`). `remove` exits 0 and says it "took
  it out of the index". The edited blob is then reachable from nothing
  (`git fsck --unreachable` lists it). With the file still present, the
  same state is refused with exit 1: "removing it would take that edit with
  it" (`seal.py:2084-2091`). A staged copy pinned to an older release takes
  the same path. Hand-deleted, it is removed with exit 0. Present and
  untracked, it is refused because it "may be ... this plugin's from
  another release".
- A committed workflow gets a staged edit and is then deleted by hand
  (status `MD`). `remove` exits 0, stages the deletion, and the staged edit
  is unreachable. With the file present, git's own `rm` refuses the same
  state ("has changes staged in the index"), and the command exits 1. With
  the file gone that refusal does not fire, so the frame's plain `git rm`
  rests on a guarantee that is not there in this arm.

The same arm gives a false reason where git cannot give the index copy at
all. With the path unmerged in the index (three stages, each the plugin's
copy) and the working file gone, `remove` exits 1 and says the copy "does
not carry this plugin's clone line" (executed). Nothing is removed, but the
reason is wrong. No case reaches that branch. A mutant that drops `staged is
None or` from `seal.py:2015` passes every `Test_pr_checks` and
`Test_remove_workflow` case (executed). The two new cases are the only ones
that delete the file by hand (executed, `git grep`), and neither stages an
edit first.

The smith's account says "four mutants of the new condition are all red".
The four are not named in the record. The mutant above survived.

```python
        staged = staged_text(repo, WORKFLOW)
        if staged is None:
            return "kept", (
                f"there is no {WORKFLOW} in the working tree, and git could not "
                "give the index's copy of it, so it was left alone. Look at it "
                "with `git status` and take it out yourself."
            )
        if PLUGIN_CLONE not in staged:
            return "kept", (
                f"there is no {WORKFLOW} in the working tree, and the index "
                "holds a copy that does not carry this plugin's clone line, "
                "so it was left alone: the index may hold the only copy of "
                "somebody's file. Look at it with `git diff --cached` and take "
                "it out yourself."
            )
        # The working-file rule, held where git's own refusal does not fire:
        # `git rm` checks a staged change only against a working file that
        # exists, so with the file gone it drops a staged edit unasked
        # (measured, round 6). Precondition: `git diff --cached --quiet`
        # exits 0 where the index equals HEAD and 1 where it differs; any
        # other exit is read as a difference, so the arm fails closed.
        if committed(repo, WORKFLOW):
            same = subprocess.run(
                ["git", "-C", repo, "diff", "--cached", "--quiet", "--", WORKFLOW],
                capture_output=True,
                timeout=30,
            )
            edited = same.returncode != 0
        else:
            edited = staged != plugin_workflow()
        if edited:
            return "kept", (
                f"there is no {WORKFLOW} in the working tree, and the index "
                "holds an edit no other copy keeps: it is neither what HEAD "
                "carries nor byte for byte what this plugin writes NOW, so it "
                "was left alone, since removing it would take that edit with "
                "it. Look at it with `git diff --cached` and take it out "
                "yourself."
            )
```

The cases belong in `tests/test_seal.py` `Test_pr_checks`, beside
`test_refuses_a_staged_file_without_the_clone_line_deleted_by_hand`. One is
parametrised over `AD` with a staged edit, `AD` with an older pin, and `MD`.
Each asserts exit 1, an unchanged `snapshot(repo)`, and the edited blob
still at `:<path>`. A second case covers the unmerged index and pins the new
reason. Show each red against `dc07a4ea` first. In `spec.md` *In* item 3,
the colon clause reads: "a copy this plugin can write back, carrying the
clone line and, where HEAD lacks the path, byte for byte what `install`
writes now, or where HEAD carries it, equal to HEAD's copy, it takes out of
the index with `git rm`".

answer: The finding holds, and it is routed to an ordinary fix pass: it is the first regression on `remove_workflow` in this run, and its comparison sentence places the defect in how the fix was written, against a frame sentence with a second reading. The orchestrator rewrote `spec.md` *In* item 3 at 5a210589 to name the two index copies `remove` may take for a hand-deleted file, the copy HEAD carries or what `install` writes now, and at the next commit added that the copy must carry the clone line first, as the smith found the two cases alone would take somebody else's committed file. The smith fixed it in 1fb674c7: an index copy git cannot give is refused and named unreadable, one without the clone line is refused as before, and the rest leave the index only where `git diff --cached --quiet` says the index equals HEAD or the copy equals `plugin_workflow()`. Four refusing cases were seen red against 5a210589, two new accepting and refusing ids were seen red by mutants, 27 `Test_pr_checks` and `Test_remove_workflow` cases pass, and five mutants of the condition are all red (executed by the smith).

## Confirmations

confirms: round-5#1
The states round 5 reported now remove what the index holds and say so
(executed, `python3 test_tmp_remove_states.py`). `install`, then a delete by
hand, then `remove` exits 0, and `git status` is empty. The same holds on a
branch with no commit. After a committed copy is deleted by hand, `remove`
exits 0 and leaves `D  .github/workflows/hygiene.yml` staged. An index copy
without the clone line is refused with exit 1, and its blob stays at
`:<path>`. This holds both where nothing was committed (`AD`) and where HEAD
carries somebody's own workflow (` D`). The smith claimed that the new cases
were seen red. With `seal.py` restored from `2cf62b72` in the scratch clone,
all three failed. Restored from `5a4011eb`, only the refusing case failed
(executed). The close of the reported defect holds. Finding 1 is a defect
the same fix introduced in the same arm, not the one round 5 reported.

confirms: round-5#2
The command list line now says `remove` takes the file "from the working
tree and the index; where HEAD carries it, the deletion is staged for you to
commit" (`seal.py:38-40`, read). The probe found it true in every state
where `remove` exits 0. After `install` then `remove`, nothing is staged and
HEAD lacks the path. After a committed copy is removed, by `git rm` or by
hand, the deletion is staged. The untracked arm stages nothing, and HEAD
lacks the path there. The frame's two rewritten sentences say the same
(`spec.md:101-102` and the `seal pr-checks remove` row of *Data &
interfaces*, read). A search for `where git tracks it`, `where git tracked
it` and `staged where tracked` outside the round records finds only
`guarantee.md:30`, which quotes the frame as the sealer read it at
`64d54bd4` (executed, `git grep`).

confirms: round-5#3
`overview.md:24` now leaves the suite row open (read). It names the broad
run at `4b63982f`, the later change at `83ccc9ae`, and the orchestrator's
next `broad-gate` run as its answerer. The plugin's `chain_check.py` agrees
that `broad-gate.md` is behind HEAD (executed).

confirms: none
Every other state of the workflow path is removed or kept as the frame says,
with a true line (executed, `python3 test_tmp_remove_states.py`). With
nothing anywhere, the command exits 0 with the nothing-to-remove line. With
the deletion already staged (`D `), it gives the same line, and that is
true: the index no longer holds the path. An untracked copy equal to what
`install` writes is deleted, exit 0. An untracked copy with an edit, or with
an older pin, is kept, exit 1. `install` then `remove` is forced out, exit
0, status empty. A never-committed copy with a staged edit and the file
present is kept, exit 1. A committed clean copy is removed and the removal
staged. A committed copy with an unstaged edit, and one with a staged edit,
are kept by git's refusal, exit 1. A symbolic link is kept, exit 1. A
committed file with mode 000 is kept as unreadable, exit 1. The only wrong
outcomes are the three of finding 1.

confirms: none
The narrow line holds at `dc07a4ea` (executed). `bin/test tests/test_seal.py
-q -p no:randomly` gave 374 passed. The `Test_pr_checks` and
`Test_remove_workflow` cases gave 21 passed. `uvx ruff check` and `uvx ruff
format --check` over the two changed Python files exited 0. `bin/test-layout
--pairs tests/test_seal.py` printed one pair, in `Test_pinned`, which the
range does not touch. So each new case covers a state that no other case in
its group, `Test_pr_checks`, reached: the absent arm with the index holding
the path. Of the four mutants this round ran on that arm, three went red:
the clone-line test reduced to `staged is None`, `git rm` given
`--dry-run`, and the tracked test made always true. The fourth is finding
1's. Every commit in the range carries the work item's `SpecSeal-Routing`
trailer, and the repository's identity is both author and committer
(executed, `git log`).

These facts were carried from earlier rounds, not re-established: S8's
replay and S9's mutants from round 4, and round 5's result that `git rm` of
a path missing from the working tree exits 0 in the `AD` and ` D` states.
This round's probe showed that result again in passing. Every verdict above
was reached this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `dc07a4ea`. Not run, because contract rule 2 gives them to the broad gate after the rounds settle. The run at `4b63982f` predates `83ccc9ae` and this range, so the smith's suite stays `unverified` | the branch | the orchestrator, by `broad-gate` |
| `questions.md` Q1 and Q4 stay open for the owner, built on their defaults (a). Carried from round 5 | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/questions.md` | the owner, relayed by the orchestrator in the pull request body |
| The settle holds this spec behind specs refused for reasons outside this branch. Carried from round 2, and not replayed | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/overview.md:25` | #1033, and the orchestrator at the settle that applies this release's specs |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_remove_states.py` in the round's scratch directory: `git init` repositories with a `seal/` directory, driven through the scratch clone's `bin/seal` at `dc07a4ea`, and git from Python | 21 states as the confirmations and finding 1 give them; `AD` with a staged edit, `AD` with an older pin and `MD` exited 0 and left the edited blob unreachable; the unmerged index exited 1 with the clone-line reason |
| `bin/test tests/test_seal.py -q -p no:randomly -k "test_accepts_remove_of_a_file_deleted_by_hand_the_index_still_holds or test_refuses_a_staged_file_without_the_clone_line_deleted_by_hand"`, with `seal.py` restored from `2cf62b72`, then from `5a4011eb`, in the scratch clone | 3 failed; then 1 failed and 2 passed, the refusing case failing; then the file was restored to `dc07a4ea` and `git status` was empty |
| `bin/mutation-check skills/implement/scripts/seal.py` with four `--replace` pairs on the absent arm and `--tests "bin/test tests/test_seal.py -q -p no:xdist -k 'Test_pr_checks or Test_remove_workflow'"` | baseline passed; 4 mutants, 3 red, 1 survived: `staged is None or` dropped; the tool restored the file |
| `bin/test tests/test_seal.py -q -p no:randomly`; the same with `-k "Test_pr_checks or Test_remove_workflow"` | 374 passed; 21 passed |
| `bin/test-layout --pairs tests/test_seal.py` | 1 pair, `Test_pinned` |
| `uvx ruff check` and `uvx ruff format --check` over `skills/implement/scripts/seal.py` and `tests/test_seal.py` | both exit 0 |
| `git grep -n deleted_by_hand dc07a4ea -- tests`; `git grep` for the three old spellings of where `remove` stages | two cases, lines 3317 and 3339; only `guarantee.md:30` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.4 --root <the branch worktree> --worktree`, the plugin's copy exit 0; finding 1 reading `open` is named, and the notices that `broad-gate.md` and `guarantee.md` are behind HEAD and the sealer's verdict reads withheld |

The probe file, its repositories and the scratch clone were removed before
the hand-back.
