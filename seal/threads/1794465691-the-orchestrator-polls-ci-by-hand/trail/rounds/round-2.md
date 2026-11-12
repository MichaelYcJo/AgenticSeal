# Review round 2: 1794465691-the-orchestrator-polls-ci-by-hand

```seal
target: 1dae28a6f, fixes be4b321da..1dae28a6f
```

This is the verifying round for round 1's five findings. The code reviewed
is the fix range `be4b321da..1dae28a6f`: `a02ca9542`, the two re-wraps
`aa5ee134b` and `cab760882`, the memo paragraph `573882a23`, the frame
folds `e0deb977e` and `1dae28a6f`, and `6d0e13fa4`. That last commit adds
only the five close blocks to round 1's record (executed,
`git diff --stat a381a42a7 6d0e13fa4`: 26 insertions in `round-1.md`). Each
record the work item keeps of the present was read whole at `1dae28a6f`:
`routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`,
`gaps.md`, `changelog.md` and `pr.md`. No `pr.<lang>.md` is owed, since
`seal/config.json` names English. No `seal/parity.json` is declared. The
probes ran in a `git clone --no-local` of the branch at `1dae28a6f` under
this round's scratch directory, and that clone was left as checked out.

Carried from round 1 and not re-established: the reading of G7 in the
framer's copy of `checks.go` and `aggregate.go` at v2.92.0, and the
carried measurements G9 to G12, which Q1 still answers. Round 1's
`evidence: executed` lines were run again here, as the Probes table gives.

## Findings

None. The fix range leaves no defect this round found.

## Confirmations

```seal
confirms: round-1#1
```
What holds: once a `pull_request` check is listed, a read whose head is not
HEAD returns exit 3 at that read and names both commits
(`skills/code-review/scripts/pr_wait.py:336-341`). The sentence that said
the command keeps waiting is gone. The docstring's exit 3 entry
(`pr_wait.py:22-26`), its limit paragraph (`:46-55`) and its head reason
(`:59-66`) say the wait ends. So do the paragraph at
`skills/code-review/orchestration.md:274-278`, row 3 at `:285` and the
exit 3 sentence of `changelog.md:3` (read). The new case
`test_refuses_a_head_that_leaves_the_pushed_commit_after_the_start`
(`tests/skills/test_pr_wait.py:307-327`) passes at `1dae28a6f`. It fails
against `be4b321da`'s `pr_wait.py` (executed, both runs in the Probes
table), which confirms the crafter's claim that it was seen red. The
frame's S4 and its exit 3 row (`frame/design.md:54`, `:85`, `:90`) and
`frame/plan.md` rows 1 and 8 now state the same exit.

```seal
confirms: round-1#2
```
What holds: before the start, an exit 3 under `UNKNOWN` prints only "GitHub
never said within 120 seconds whether the pull request is mergeable"
(`pr_wait.py:350-355`). `main` puts HEAD before that line, so the line still
names the commit. Row 3's act at `orchestration.md:285` now reports "the
cause the output names", so the orchestrator no longer reports a missing
check it never read. That restores the distinction the old paragraphs drew
under `MERGEABLE` alone.

The crafter departed from the paste-ready line, which ended "so no check
on" the SHA "was read". The folded S8 at `frame/design.md:58` asks the line to say
"only that GitHub never said whether the pull request is mergeable, and
nothing about checks it did not read". The line as built follows the frame
and says nothing false, so the departure holds.

The framer's extension is a new unit, and it was reviewed as code. After
the start, `UNKNOWN` reads the checks as `MERGEABLE` does
(`pr_wait.py:342-343`). `state` and `CONFLICTING` are still tested first
(`:330-335`), and a moved head is tested before the extension (`:336-341`),
so the extension can reach neither exits 4 to 6 nor a moved head's checks.
`test_accepts_a_mergeable_that_goes_unknown_after_the_start` and the
rewritten `test_refuses_to_start_while_mergeable_is_never_known` pass at
`1dae28a6f` and fail against `be4b321da`'s code (executed).

```seal
confirms: round-1#3
```
What holds: round 1's executed line was run again. It replaces the
`_answer` guard, the `mergeable` guard and the shape guard
(`pr_wait.py:232`, `:257`, `:262-264`) each by `if False:`. That line,
29 passed at `be4b321da`, now fails four cases: the three parameters of
`Test_once::test_refuses_a_view_gh_does_not_shape` and
`Test_once::test_refuses_an_answer_that_is_not_json_of_its_kind` (executed).
The cases are the paste-ready ones, in `Test_once` (`test_pr_wait.py:508-545`).

`gaps.md:13-20` *Not done* names what still has no case. It claims "four of
the eleven exit 2 guards". There are 11 `raise Unanswered` in the module
(executed, `grep -c`). Three of the four named are raises of their own: the
timeout, the `OSError` from `gh` and the `OSError` from `git`. The fourth,
an entry of `gh pr checks`' list that is not an object, is a branch of the
one raise that the bucket case already reaches. No act rests on the count,
and every guard named is one *Data & interfaces* does not state, so this
is no finding.

```seal
confirms: round-1#4
```
What holds: the rollup reason now cites `pkg/cmd/pr/checks/checks.go` at
v2.92.0 (`pr_wait.py:67-73`). In the framer's copy, `populateStatusChecks`
returns its error at `checks.go:184-187`, before the exporter at `:189-190`
writes anything, and `no checks reported` is that error at `:302-303`
(read). The `pull_request` reason cites
`.github/workflows/label-merged-on-release-branch.yml` (`pr_wait.py:74-81`).
Its trigger is `push` on `release/*` (`label-merged-on-release-branch.yml:20-22`,
read), so a pull request from a release branch lists its check, as the
docstring says.

The crafter did not take the citation of #1222 for the head reason.
`git show v0.27.2:seal/threads/1793521560-the-checks-wait-starts-before-a-check-reports/frame/design.md`
line 13 labels the asynchronous head move "unverified: no read-only probe
can push" (executed). Citing it would give an unmeasured claim a source.
The head reason now rests on what `gh pr checks` lists and says the delay
is unmeasured (`pr_wait.py:59-66`). `frame/design.md:32`, folded at
`1dae28a6f`, says exactly that, so the frame and the target agree.

```seal
confirms: round-1#5
```
What holds: `frame/design.md:92`, folded at `e0deb977e`, names the commit
each line carries: HEAD for the wait, the pull request's head under
`--once`, and none for an exit 2 before any read. That matches
`pr_wait.py#main` and `#once`, and the cases at
`test_pr_wait.py:564-608` that pin both lines (read).

What matched: the records of the present agree with the target. The
changelog's exit 3 sentence and its sentence on `UNKNOWN` after the start
(`changelog.md:3`) agree with `pr_wait.py#wait`. The design's S4, S8,
*Data & interfaces* read 2, the exit 3 row and *Out*'s time-limit bullet
agree with it too (read). `frame/plan.md` *Judgments of the run* gains three
rows for the frame changes, each with its grounds and its document. Each
quote of `pr.md` still stands word for word at its coordinate, in
`frame/plan.md` *Operational impact* bullets three and four, Q2's default
and the title row (read).

What matched: the module's cases and the pin pass at `1dae28a6f`: 60
passed (executed, `bin/test -q tests/skills/test_pr_wait.py
tests/text/test_the_rules_have_one_owner.py`). The two changed Python files
pass `ruff check` and `ruff format --check` (executed, the two files
alone). The paragraph's prose lines at `orchestration.md:266-278` stay
within 79 characters (executed).

What matched: each new case was read against its group. The moved-head
case is the after-the-start counterpart of the two S4 cases before it, and
it covers what they do not. The `UNKNOWN`-after-the-start case covers the
extension, which no other case reaches. The two `Test_once` cases cover the
three guards round 1 found unheld. None duplicates a case of its class.

The closing memo's third row, which asks the proofer to read the paragraph
against the old ones, still reads as open in `gaps.md:9`. Round 1 answered
it, and this round confirms the answer holds at `1dae28a6f`. Marking the row
`closed` is the orchestrator's or the fix pass's act, not this round's.

Nothing is left open by this round. What comes due next is the
orchestrator's broad run and, after it, the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| What follows a moved head's exit 3. Row 3 has the orchestrator report and wait no longer. After GitHub's "Update branch", the local branch is behind the remote and the head is a merge commit outside the records, which the paragraph on merging the base speaks to. Whether row 3 should point there is a judgment of the procedure | `skills/code-review/orchestration.md:285`, `:290-307` | the orchestrator |
| What the orchestrator does at exit 2 from `--once` before a push, carried from round 1 | `skills/code-review/orchestration.md:284` | the orchestrator, or the owner |
| The command against a real pull request, and G9 to G12 | `frame/questions.md` Q1 | the orchestrator, at this pull request's first `seal pr-wait` run |
| `gh pr checks --json event` on GitHub Enterprise Server | `frame/questions.md` Q2 | whoever runs the plugin against one |
| `tests/skills/test_pr_wait.py` on Linux, Windows, Python 3.12 and 3.14 | `gaps.md:8` | the pull request's `tests` workflow |
| The whole suite, the repository-wide lint and the format check at HEAD; the label `unverified` stands | `gaps.md:7` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/skills/test_pr_wait.py tests/text/test_the_rules_have_one_owner.py` in the clone at `1dae28a6f` | 60 passed, exit 0 |
| `bin/test -q -p no:xdist tests/skills/test_pr_wait.py` with `pr_wait.py:232`, `:257` and `:262-264` each replaced by `if False:`, round 1's executed line for finding 3 | 4 failed, 31 passed, exit 1: the three `test_refuses_a_view_gh_does_not_shape` parameters and `test_refuses_an_answer_that_is_not_json_of_its_kind`; the file was restored with `git checkout` |
| The same module with `pr_wait.py` taken from `be4b321da`, standing for round 1's probe file for findings 1 and 2 | 3 failed, 32 passed, exit 1: `test_refuses_a_head_that_leaves_the_pushed_commit_after_the_start`, `test_refuses_to_start_while_mergeable_is_never_known`, `test_accepts_a_mergeable_that_goes_unknown_after_the_start`; the file was restored with `git checkout` |
| `uvx ruff check` and `uvx ruff format --check` on `pr_wait.py` and `test_pr_wait.py` | exit 0 and exit 0 |
