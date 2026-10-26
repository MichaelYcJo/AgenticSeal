# Review round 5: 1792976216-the-records-and-the-pr-checks-are-two-answers

target: 2cf62b72, fixes d0ba9fba..2cf62b72

## Findings

### 1. `seal pr-checks remove` says there is nothing to remove while the index still holds the file `install` staged, and the next commit carries it

severity: should
location: `skills/implement/scripts/seal.py:2002-2003`, `tests/test_seal.py:3239`, `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/spec.md:113-114`
evidence: executed `python3 test_tmp_remove_states.py`
verdict: open

The fix at `83ccc9ae` makes `remove` read the index where the working file
is there. It does not read the index where the working file is gone. The
sealer's defect belongs to a class: `remove` judges the workflow from the
working tree alone, while a commit is made from the index. The fix covered
the members where the working file is present. One member is left.

A person runs `seal pr-checks install`, changes their mind, and deletes
`.github/workflows/hygiene.yml` by hand. They then run `seal pr-checks
remove` to be sure. `remove_workflow` asks `workflow_at` first, which answers
`absent` from `os.path.lexists`. The command prints "there is no
.github/workflows/hygiene.yml, so there is nothing to remove" and exits 0
(`seal.py:2002-2003`, read). The index still holds the staged file. The probe
showed `git status` as `AD .github/workflows/hygiene.yml`. A `git commit`
made right after it carried the workflow at HEAD (executed). So the command
tells the person something false, and they act on it by committing. The same
arm answers a committed workflow deleted by hand (status ` D`). There the
committed copy stays in the next commit unless the person stages the
deletion. `spec.md:113-114` says "Where nothing is there it says so and exits
0", and the code reads "there" as the working tree only.

The probe also ran the git verb the fix needs. `git rm --quiet` on the path,
with the working file gone, exits 0 in both states. Where nothing was
committed it takes the staged file out of the index and leaves `git status`
empty. Where the file was committed it stages the deletion (executed, same
probe).

The shape needs a person to delete the file by hand first, so the frame may
take it as a limit instead. The owner's rule for shapes the normal flow does
not produce allows that. In that case the close is a sentence in
`spec.md` *Out* and a changed reply in this arm that names the index, and no
guard. The fix below takes the file out instead, under the same two
conditions the forced arm uses. A test belongs in `tests/test_seal.py`
`Test_pr_checks`: install, delete the file, remove, then assert exit 0, an
empty `git status`, and the new line. Show it red against the current arm
first.

```python
    if kind == "absent":
        # Gone from the working tree is not gone from the commit: the index
        # may still hold the file `install` staged, or a committed copy whose
        # deletion is not staged. Precondition: `git rm` of a path missing
        # from the working tree exits 0 and drops its index entry (measured,
        # round 5).
        staged = staged_text(repo, WORKFLOW) if tracked(repo, WORKFLOW) else None
        if staged is None:
            return "absent", f"there is no {WORKFLOW}, so there is nothing to remove"
        if PLUGIN_CLONE not in staged or (
            not committed(repo, WORKFLOW) and staged != plugin_workflow()
        ):
            return "kept", (
                f"{WORKFLOW} is gone from the working tree, but the index still "
                "holds a copy this plugin cannot write back, so a commit would "
                "carry it. Look at it with `git diff --cached` and take it out "
                "yourself."
            )
        done = subprocess.run(
            ["git", "-C", repo, "rm", "--quiet", "--", WORKFLOW],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
        if done.returncode != 0:
            return "failed", (
                f"{WORKFLOW} could not be removed: {(done.stderr or '').strip()}"
            )
        return "removed", (
            f"{WORKFLOW} was already gone from the working tree, and the index "
            "held it; took it out of the index, so a commit no longer carries it"
        )
```

answer:

### 2. The module docstring says `remove` stages the removal where git tracked the file, and after `install` the forced removal stages nothing

severity: should
location: `skills/implement/scripts/seal.py:38-39`
evidence: read `skills/implement/scripts/seal.py:38-39`, `skills/implement/scripts/seal.py:1708-1728`, `skills/implement/scripts/seal.py:2042-2075`
verdict: open

The module docstring's command list says `seal pr-checks remove` will "take
out the file this plugin wrote, and stage the removal where git tracked it"
(`seal.py:38-39`). In this file, git tracks a path when the index holds it
(`seal.py#tracked`, lines 1708 to 1728). The forced arm runs only where
`tracked` is true and HEAD lacks the path (`seal.py:2042`). That is the state
`install` leaves. There `git rm --force` takes the file out of the index and
off the disk. Nothing is staged, and `git status` is as it was before
`install`. `test_accepts_remove_straight_after_install_before_a_commit`
asserts exactly that (`tests/test_seal.py:3272-3288`, read and run). The
command's own line there says "took it out of the index", not "staged the
removal" (`seal.py:2071`).

The orchestrator made this same correction in `spec.md` at `2cf62b72`. It
changed "forced past git's staged-changes refusal and staged" to "which takes
the file out of the index and off the disk". The docstring still states the
old fact. Contract rule 19 asks the change to correct every sentence that
states it. An agent that reads the list tells a person to commit a removal,
and after `install` then `remove` there is no removal to commit. "Tracked" can
also be read as "committed", and then the line is true. So the line has two
readings, which `CLAUDE.md` *Repo rule: text an agent or a check reads has one
reading* refuses.

```python
  seal pr-checks remove       take out the file this plugin wrote; stage the
                              removal where HEAD carries it
```

answer:

### 3. `overview.md` says the broad run closed the suite at the branch head, and code changed after that run

severity: should
location: `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/overview.md:24`
evidence: executed `git diff --stat 4b63982f 2cf62b72 -- skills tests`, `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.4`
verdict: open

`overview.md:24` closes the row for the full suite, lint and format "at the
branch head" on the broad run at `4b63982f`. `83ccc9ae` came after that run.
It changed `skills/implement/scripts/seal.py` by 53 lines and
`tests/test_seal.py` by 44 (executed). The chain check at `2cf62b72` says the
same of `broad-gate.md`: "the newest broad-gate run is behind HEAD: commit
83ccc9ae after it touches `skills/implement/scripts/seal.py`" (executed). So
the overview labels the suite at the head as verified when no run covers the
head. The sealer reads this row as the implementer's account. The label is
what this round checks, and here it is not honest.

`broad-gate.md` itself records a run at `4b63982f` and says nothing about the
head, so it states its moment truly. The orchestrator's next broad run
rewrites it. The overview row does not change by itself, so it has to go
back to open until that run.

```markdown
| The full suite, the repository-wide lint and format check, and the typecheck at the branch head. The broad run at `4b63982f` predates `83ccc9ae`, which changed `skills/implement/scripts/seal.py` and `tests/test_seal.py`; the repository has no typecheck to run (#951 adds one) | the orchestrator, by `broad-gate`, after the review rounds settle |
```

answer:

## Confirmations

confirms: none
The fix builds `spec.md` *In* item 3 as amended at `91695d46` and
`2cf62b72`, for every state where the working file is present.
`seal.py:2042-2057` forces the removal only where HEAD lacks the path and
both the working copy and the index equal `plugin_workflow()`. Otherwise it
refuses with exit 1 and removes nothing (read). The round ran each state
through the clone's `bin/seal` in scratch repositories (executed). Install
then remove: exit 0, nothing under `.github/`, `git status` empty. The same
on a branch with no commit at all: exit 0, status empty, because
`seal.py#committed` answers False where HEAD does not exist. A staged
`git mv` onto the path from a committed file with the plugin's bytes: the
forced removal takes the new path out, and the old path's deletion stays
staged. HEAD keeps that copy, so nothing is lost. A committed copy is never
forced, because `committed` answers True wherever HEAD carries the path.

confirms: none
The two new cases pin the accepting and refusing states, and they were red
first. With `seal.py` restored from `83ccc9ae^` in the scratch clone, all
three failed (executed). The accepting case failed on exit 1, with git's
"has changes staged in the index". Both refusing parameters failed on the
message alone, because the old code also exited 1 and removed nothing
there. So the round dropped the guard itself with `bin/mutation-check`, in
six mutants, and every one went red (executed). The mutants were: the guard
removed; the index comparison dropped; the working-copy comparison dropped;
the force dropped; `committed` always False; and `committed` always True,
which is the sealer's defect. The last two show the existing committed-path
case, `test_accepts_install_report_and_remove_in_turn`, also pins
`committed`.

confirms: none
No other state of a tracked, staged or committed workflow now removes
something it should not (executed, `python3 test_tmp_remove_states.py`). A
committed file with an unstaged edit, and one with a staged edit, both reach
plain `git rm`. Git refuses both, and the command exits 1 with the file and
the edit kept. A committed file whose index entry was dropped with
`git rm --cached` takes the untracked arm. That arm removes the working copy,
which equals what `install` writes, and HEAD still holds the file. A
committed file pinned to another release, with no local change, is removed
and the removal is staged, and HEAD keeps the old copy. The one wrong answer
the probe found is finding 1, which leaves something in place and does not
remove it.

confirms: none
The fix compares text decoded with universal newlines, not raw bytes
(`seal.py#staged_text`, read). The probe wrote the working copy with CRLF
line endings after `install`, and `remove` forced it out (executed). So the
only edit the force can take is a change of line endings to a file
`install` writes back. The untracked arm has compared this way since phase 2
(`seal.py:2024`, read). On a checkout that writes CRLF, the file `install`
wrote would not equal `plugin_workflow()` byte for byte, so raw bytes would
refuse the sealer's own state there. The word "byte for byte" in `spec.md`
*In* item 3 is read here as the decoded comparison both arms make.

confirms: none
Every other text that says what `remove` does is true at `2cf62b72` (read).
These are `changelog.md:5`, `README.md:462`, `README.ko.md:457`,
`templates/hygiene.yml:11` and `:20`, `seal/README.md:31`,
`templates/seal-README.md:31`, `skills/implement/orchestration.md:135`,
`skills/config/SKILL.md:148`, `hooks/mode-gate.py:251`, `bin/seal:14`,
`seal.py#left_workflow_line`, the `pr_checks` docstring and its report line,
and the parser's help. Each says `remove` takes out the file this plugin
wrote. None says it stages a removal, except the docstring of finding 2. S3's
"`seal pr-checks remove` then removes the file it wrote" now holds right
after `install`. The sealer said the changelog's sentence was false, and it
is true now. `docs/one-root-by-lifetime.md:110` still carries the old switch
row. That row is one `## Rule changes` retires at the settle, and the build
does not edit `docs/`.

confirms: none
The other commits in the range state the tree truly, except `overview.md:24`
(finding 3). Q2's answer names the run `40264357704`, and `gh run view` gives
head `895db45e` and conclusion `success` (executed). The overview's Windows
row agrees with it. #1033, which the overview's settle row names, is open,
with a title about grouping specs by section (executed, `gh issue view`).
`guarantee.md` records the sealer's withheld verdict at `64d54bd4`, and the
chain check says the sealer runs again at the new head (executed).
`broad-gate.md` records the run at `4b63982f`. `rounds/round-4.md` is round
4's record, as written. The spec diff of the range is one hunk, lines 103
to 113 of *In* item 3 (executed, `git diff --unified=0`). It does not touch
`## Rule changes` or S3, so S8's applied half was not replayed again. That
replay's result is carried from round 4.

confirms: none
The narrow line holds at `2cf62b72` (executed). `bin/test tests/test_seal.py
-q` gave 371 passed. The `Test_pr_checks` and `Test_remove_workflow` cases
gave 18 passed. `uvx ruff check` and `uvx ruff format --check` over the two
changed Python files passed. `chain_check.py --baseline
origin/release/v0.22.4` exited 0 with notices only, listed in the
confirmation above. `bin/test-layout --pairs tests/test_seal.py` printed one
pair, in `Test_pinned`, which the range does not touch. So each new case
covers a state its group, `Test_remove_workflow` and `Test_pr_checks`, did
not reach. Every commit in the range carries the work item's
`SpecSeal-Routing` trailer, and the repository's identity is both author and
committer (executed, `git log`).

These facts were carried from earlier rounds, not re-established: S8's
replay and S9's five mutants from round 4, where the chain step's no-root
test lives, and round 1's list of the states of `spec.md` *In* item 3. Round
1's list did not include a staged file, so this round ran those states
itself. Every verdict above was reached this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `2cf62b72`. Not run, because contract rule 2 gives them to the broad gate after the rounds settle. The run at `4b63982f` predates `83ccc9ae`, so the smith's suite stays `unverified` | the branch | the orchestrator, by `broad-gate` |
| `questions.md` Q1 and Q4 stay open for the owner, built on their defaults (a) | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/questions.md` | the owner, relayed by the orchestrator in the pull request body |
| The settle holds this spec behind specs refused for reasons outside this branch. Carried from round 2, and not replayed | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/overview.md:25` | #1033, and the orchestrator at the settle that applies this release's specs |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_seal.py -q -p no:randomly -k "test_accepts_remove_straight_after_install_before_a_commit or test_refuses_a_staged_file_that_differs_and_leaves_it"`, with `seal.py` restored from `83ccc9ae^` in a scratch clone at `2cf62b72` | exit 1, 3 failed: the accepting case on exit 1 with git's staged-changes refusal, the two refusing parameters on the message; then the file was restored |
| `bin/mutation-check skills/implement/scripts/seal.py --replace ...` six times, with `--tests "bin/test tests/test_seal.py -q -p no:xdist -k 'Test_pr_checks or Test_remove_workflow'"` | baseline passed; 6 mutants, 6 red, 0 survived; the tool restored the file |
| `python3 test_tmp_remove_states.py` in the round's scratch directory: `git init` repositories with a `seal/` root, driven through the clone's `bin/seal` and git from Python | the states as the confirmations and finding 1 give them; `git rm --quiet` with the working file gone exited 0 both where nothing was committed and where the file was committed |
| `bin/test tests/test_seal.py -q`; the same with `-k "Test_pr_checks or Test_remove_workflow"` | 371 passed; 18 passed |
| `bin/test-layout --pairs tests/test_seal.py` | 1 pair, `Test_pinned` |
| `uvx ruff check` and `uvx ruff format --check` over `skills/implement/scripts/seal.py` and `tests/test_seal.py` | both exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.4` in the clone | exit 0; notices that round 4, `broad-gate.md` and `guarantee.md` are behind HEAD |
| `git diff --stat 4b63982f 2cf62b72 -- skills tests` | `seal.py` 53 lines, `tests/test_seal.py` 44 |
| `gh run view 40264357704 --json headSha,conclusion`; `gh issue view 1033 --json number,title,state` | `895db45e`, `success`; open |

The probe file, its repositories and the scratch clone were removed before
the hand-back.
