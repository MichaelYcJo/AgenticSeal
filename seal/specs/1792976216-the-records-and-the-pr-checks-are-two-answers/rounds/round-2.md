# Review round 2: 1792976216-the-records-and-the-pr-checks-are-two-answers

target: d1647de2, fixes 3f2f5a5d..d1647de2

## Findings

### 1. The settle that applies this spec turns two cases red, because the README copies the rule's new sentence

severity: should
location: `README.md:510-514`, `README.ko.md:503-508`, `tests/test_first_setup_asks_once.py:485-502`, `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/spec.md:126-127`
evidence: executed `python3 test_tmp_round2_rules.py --write`, `bin/test tests/test_no_passage_is_pasted_into_a_second_file.py -q`
verdict: fixed ccc786ef
regression: round-1#2

The unit is the paragraph after the by-hand move in `README.md` *Shared or
local*, lines 510 to 514, which `3b5543fb` rewrote. `spec.md` *In* item 4
(amended in `60f3ea14`) asks the two READMEs to "say the same" of a workflow
left after a switch to local. The fix pass wrote the rule change's own
sentence into `README.md`, and the repository's copy check refuses that
sentence once the settle puts it into `docs/one-root-by-lifetime.md`.

This is the class of round 1 finding 3: a case that passes on the branch and
fails at the settle that applies the spec. The round applied all 17 items of
`spec.md` *Rule changes* to `docs/` at `02ee12de` and ran 13 modules that read
those documents. Two cases failed, and 643 passed:
`test_no_passage_is_pasted_into_a_second_file.py::test_no_pair_shares_more_than_it_was_measured_at`
and `::test_a_removed_copy_passes_without_a_baseline_edit`. The message reads
"README.md and docs/one-root-by-lifetime.md share 2 runs of 15 words where 0
were measured; the longest is 16 words: 'one pinned to an older release fails
every pull request there until its --branch line moves'". With `docs/`
restored, the same module passes, 8 of 8 (executed).

The copy is `README.md:512-514` beside the rule change's `to` at
`spec.md:339-341`. The Korean pair, `README.ko.md:506-508` beside
`spec.md:391-393`, is the same copy. The module leaves every `*.ko.md` out as
a sanctioned mirror, so nothing measures it, but it follows the English
README. `tests/test_first_setup_asks_once.py` `LEFT_BEHIND` pins both copies,
so the fix rewrites the pin, seen red first.

The fix links the README to the rule's home, as the module's message asks.
`docs/one-root-by-lifetime.md` holds the old paragraph until the settle, and
the README ships after it.

```markdown
Doing it that way leaves `.github/` alone, as `seal mode` does. Whether a
workflow left behind after a move to local passes depends on the release it
pins: `docs/one-root-by-lifetime.md` *Shared or local* says which pin passes
and how to move one that fails, and `seal mode local` names the pin when it
leaves the file.
```

```markdown
그렇게 해도 `seal mode` 와 마찬가지로 `.github/` 에는 손대지 않습니다.
local 로 옮긴 뒤 남은 워크플로가 통과하는지는 그것이 고정한 릴리스에 달려
있습니다. 어느 고정이 통과하고 실패하는 고정을 어떻게 옮기는지는
`docs/one-root-by-lifetime.ko.md` *shared 인가 local 인가* 가 말하고,
`seal mode local` 은 파일을 남길 때 고정된 릴리스를 알려 줍니다.
```

```python
LEFT_BEHIND = {
    "README.md": (
        "Whether a workflow left behind after a move to local passes depends "
        "on the release it pins",
        "`seal mode local` names the pin when it leaves the file.",
    ),
    "README.ko.md": (
        "local 로 옮긴 뒤 남은 워크플로가 통과하는지는 그것이 고정한 릴리스에 "
        "달려 있습니다.",
        "`seal mode local` 은 파일을 남길 때 고정된 릴리스를 알려 줍니다.",
    ),
}
```

`spec.md:126-127` then reads that the two READMEs name the pin's effect and
link to *Shared or local*, rather than "say the same".

answer: The finding holds. The orchestrator amended `spec.md` *In* item 4 in 4cdfef95: the two READMEs say in one sentence that a workflow left after a move to local stays, and link to `docs/one-root-by-lifetime.md` *Shared or local* and its Korean edition, which hold the rule once the settle applies this spec. The smith fixed it in ccc786ef and rewrote the `LEFT_BEHIND` pin, seen red on both READMEs first. In a scratch clone, all 17 rule changes applied to `docs/` with no error, and `tests/test_no_passage_is_pasted_into_a_second_file.py` with `tests/test_first_setup_asks_once.py` gave 57 passed. The same replay with the READMEs at d1647de2 failed the two cases this record names (executed by the smith).

### 2. Under `--worktree` the no-root test reads HEAD while the declarations come from the working tree, so a new uncommitted root goes unjudged with a false cause

severity: should
location: `skills/code-review/scripts/chain_check.py:2181-2186`, `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/spec.md:151-158`, `tests/test_chain_check.py`
evidence: executed `bin/test tests/e2e/teammate/test_tmp_round2_probe.py -p no:xdist -s -q`
verdict: fixed c09d050a
regression: round-1#1

The unit is the no-root test that `2c9e2a19` added to `chain_check.py#main`,
lines 2181 to 2186. `spec.md` *In* item 6 (amended in `60f3ea14`) says "where
HEAD has no top-level `seal` entry" and says nothing of `--worktree`. The fix
asks `git ls-tree HEAD` in both modes, while
`docs/the-review-and-parity-arms.md` *The declaration, and where the check
went* says "`--worktree` reads the working tree instead". So the defect came
from the frame naming HEAD for a check that has two readings.

Under `--worktree`, `changed()` diffs the merge base against the working tree
and counts untracked files as added, and `read_record()` reads from disk. The
new test alone reads HEAD. The probe built two shapes.

- No root at HEAD, and a new untracked root whose `routing.md` names the
  checked-out branch. At `d1647de2` the check judged nothing and printed "no
  `seal/` is at HEAD, so nothing is declared: the routing declarations this
  pull request deletes left the tree with the root". Nothing was deleted: the
  declarations were added. `chain_check.py` at `3f2f5a5d`, run on the same
  repository, judged the declaration and refused its round record, broad-gate
  file and guarantee. So the regression is this fix pass's.
- A shared root at HEAD, and `seal mode local` run and not yet committed. The
  check refused `routing.md` ("git does not carry this file at HEAD"). CI
  accepts the same change once it is committed (round 1 finding 1, confirmed
  below).

Who meets it: a session that runs `chain-check --worktree` before the commit
that carries a new root or a switch. The smith's account calls the first
shape outside the normal flow, because the routing commit carries the root
before the first edit. Read at `skills/implement/orchestration.md`
*Bootstrap*, that holds, and so does the account. Both runs above exit 0
because no pull request was observed, so the check gates nothing here. But it
prints a cause that is false, and nothing in the frame states the shape as a
limit. The cheaper answer is the reading the policy already names.

```python
    # With no `seal` entry in the tree read, nothing is declared, as a
    # pull request moving the root to local mode leaves it. `--worktree`
    # reads the working tree, as `read_record` and `changed` do; there a
    # file, a symbolic link or a directory named `seal` counts as an entry,
    # as `git ls-tree` counts one. Where git cannot answer, `git()` is None
    # and the declarations stay judged.
    home = routing.optin.HOME
    if WORKTREE:
        gone = not os.path.lexists(os.path.join(root, home))
    else:
        gone = git(root, "ls-tree", "HEAD", "--", home) == ""
    if declarations and gone:
        declarations, why = [], ROOT_LEFT_SAYS.format(home=home)
```

The precondition is that `root` is the top level `reader.repo_root` returned,
which `main` already guarantees. `os.path.lexists` does not follow a symbolic
link, so a dangling `seal` link counts as present and the declarations stay
judged. A case in `tests/test_chain_check.py` `Test_retired` runs
`--worktree` on an untracked root that declares the branch, and requires the
declaration to be judged. It is seen red at `d1647de2`. `spec.md` *In* item 6
then says "at HEAD, or in the working tree under `--worktree`". If the fix
pass keeps HEAD instead, the shape goes into `spec.md` *Out* as a limit, with
the false cause named.

answer: The finding holds, and the record's first fix is taken: under `--worktree` the check reads the working tree for the `seal` entry, the tree it reads the declarations from. The orchestrator amended `spec.md` *In* item 6 and the three rule changes in 4cdfef95. The smith fixed it in c09d050a with `os.path.lexists` under `--worktree` and `git ls-tree HEAD` otherwise, and added two cases to `tests/test_chain_check.py` `Test_retired`: a root on disk and not at HEAD is judged, seen red against the old code, and a `seal` that is a file in the working tree is judged, seen red by a mutation from `lexists` to `isdir` (executed by the smith).

### 3. The rule changes state when nothing is declared in three terms, and one of them is false at a `seal` that is not a directory

severity: should
location: `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/spec.md:418-435`, `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/spec.md:155-156`, `skills/code-review/scripts/chain_check.py:2181-2182`
evidence: executed `bin/test tests/e2e/teammate/test_tmp_round2_probe.py -p no:xdist -s -q`, `python3 test_tmp_round2_rules.py`
verdict: fixed 14031ecd
regression: round-1#1

The unit is the `add` and the first `change` to `docs/the-review-record.md`
*What the check reads at the pull request* (`spec.md:418-435`), from
`60f3ea14` and `64a73e7b`. `spec.md` *In* item 6 names the condition as "no
top-level `seal` entry" at HEAD. The fix pass's rule text states that
condition three ways in one section, and the code comment repeats the false
one.

The round replayed the 17 items onto `docs/` at `02ee12de` and read the
section as the settle leaves it (executed). The paragraph *The check reads
the diff as declarations* now ends "the deletion is judged, wherever HEAD
still has a `seal` root". Two paragraphs on, the `add` says "Where HEAD has no
top-level `seal` entry, the check reads nothing as declared", and goes on "as
the unverified check reads the same tree". That is three spellings of one
condition. "A `seal` root" and "a top-level `seal` entry" are not the same
fact. A root is a directory of records, and an entry is anything git carries
at that name.

The probe made the difference real. On a pull request that replaces the
shared root with a regular file named `seal`, `chain_check.py` exited 1 and
refused the deleted `routing.md`. An entry is there, so the declarations are
judged, as the code means. `unverified_check.py` exited 0, "no `seal/` root
in this tree", because `absent_root` asks `os.path.isdir`. So "as the
unverified check reads the same tree" is false on this tree, and "wherever
HEAD still has a `seal` root" reads as not judged where the code judges. The
code fails closed, so nothing escapes. But a person who frames the next change
to this check from the policy reads two rules. `CLAUDE.md` *Repo rule: text
an agent or a check reads has one reading* asks for one term and no fact
stated twice. The `change` to `docs/the-review-and-parity-arms.md`
(`spec.md:436-442`) already uses the one term and links to the home, and it
stays.

The fix keeps one statement in the `add` and points the `change` at it.

```markdown
- add
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  to: **Where HEAD has no top-level `seal` entry, the check reads nothing as
    declared.** The pull request that moves a root to local mode deletes
    every `routing.md` with the root, and a deleted declaration HEAD does
    not carry is otherwise refused. With no such entry there is nothing to
    declare, so the check judges the trailers as for any pull request that
    declares nothing. Where git cannot say whether HEAD has the entry, the
    declarations stay judged.
    check: nothing-declared-nothing-owed
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: is two declarations and the deletion is judged.
  to: is two declarations and the deletion is judged, unless HEAD has no
    top-level `seal` entry, as the paragraph below on that case states.
```

`spec.md:155-156` drops "as `unverified_check.py`'s no-root state does", and
the comment at `chain_check.py:2181-2182` drops "as
`unverified_check.py#absent_root` reads the same tree", or both name the
difference at a `seal` that is not a directory. Finding 2's fix, if taken,
adds the `--worktree` reading to the same `add`.

answer: The finding holds. The orchestrator rewrote the `add` and the two `change` items in 4cdfef95 so the condition has one term, the tree the check reads has no top-level `seal` entry, with the `add` as its one statement. The sentence saying the check reads the tree as the unverified check does is gone, and `spec.md` *In* item 6 says the two are not one reading. All 17 items parse and place against `docs/` (executed). The smith used the same term in the code comment (c09d050a), and in `ROOT_LEFT_SAYS`, the module docstring and the changelog fragment (14031ecd), with the case's pin seen red first (executed by the smith).

## Confirmations

confirms: round-1#1
The pull request that moves the root to local mode with the checks kept now
passes every step. The round re-ran round 1's case through the new flow
helper, `switching_repository`: no step failed, and the chain step exited 0
with the `ROOT_LEFT_SAYS` notice. Then it disabled the test at
`chain_check.py:2185`. With it disabled, both new cases failed on "git does
not carry this file at HEAD": `Test_retired::test_accepts_every_declaration_leaving_with_the_root`
and the flow's `test_accepts_the_pull_request_that_moves_the_root_to_local_mode`.
The file was then restored. So the smith's claim that the cases were seen red
holds (executed). `spec.md` *In* items 6 and 7, *Places*, *Out* and
`questions.md` answered item 2 say the new rule, read at `spec.md:135-181`,
`spec.md:213-214`, `spec.md:221-223` and `questions.md:14-20`. The `git()` None branch keeps the declarations
judged. The new case's second half pins that, and it passed in the narrow run
(executed).

confirms: round-1#2
`seal mode local` names a pin that is not the installed release. The round
re-ran round 1's case: a committed workflow pinned to `v0.22.2`, then the
switch. `seal pr-checks` reported "pinned to v0.22.2". The switch printed
"stays, pinned to v0.22.2 and not to the installed v0.22.3: a release before
this one fails every pull request with no seal/ in the tree. Move its
`--branch` line to v0.22.3, or run `seal pr-checks remove`" (executed). The
mode gate's *Local* option (`hooks/mode-gate.py:246-252`), both READMEs and
the changelog's *Compatibility* line say the same (read). Finding 1 above is
about where the README sentence goes once the settle runs, not about what it
says. `left_workflow_line`'s three branches are pinned by the new
`Test_switch` parameters and the existing pass-line case (read
`tests/test_seal.py:3006-3042`; both passed in the narrow run).

confirms: round-1#3
`test_the_record_no_longer_says_the_checks_would_refuse` keeps only its first
assert (read `tests/test_first_setup_asks_once.py:679-681`). With all 17
rule changes applied to `docs/`, `tests/test_first_setup_asks_once.py` passed
in the 13-module run (executed). Only finding 1's two cases failed there.

confirms: none
Reading no top-level `seal` entry at HEAD as nothing declared lets no pull
request escape the declaration its own work owes. The round asked whether a
pull request can get its own work past the check by deleting the root. Every
shape it built that deletes or replaces the shared root, beyond the switch,
was run through the chain and unverified steps (executed).

- The root deleted whole, a code file changed, and the commit carrying
  `SpecSeal-Routing: 1790000000-work`: the chain step exited 1, because the
  trailer names a work item no judged declaration names.
- The same with no trailer: both steps exited 0.
- The root replaced by a regular file named `seal`: the chain step exited 1
  on the deleted `routing.md`.

A commit with no trailer is judged by nothing on any pull request
(`chain_check.py` module docstring, the `routing` arm), so the second shape
owes no more than a pull request that never declared. What it newly passes is
the deletion of declarations that earlier pull requests made and were judged
at. `plan.md:64` (row H) accepts that for the unverified step, "the diff
shows the whole root leaving", and the chain step now reads that tree the
same way. So no gap is opened in work a work item owns. That is the line
`CLAUDE.md` *The rule a mechanism is kept against* draws.

confirms: none
The 17 items of `spec.md` *Rule changes* parse with `rule_changes.py#parse`
with no error. Each placed in order with `apply_op` against `docs/` at
`02ee12de`, the new `add` and two `change` items included (executed).
`git diff --stat 02ee12de HEAD -- docs` is empty, so that is still the policy
in force (executed). No other unsettled spec changes the two qualified
sentences, "the deletion is judged" and "the refusal stands". The search was
`rule_changes.py#overlapping` over every spec's operations, then the
operations at each overlapping place read by eye (executed, then read). The
merge-order replay was run over every unsettled spec, dropping each spec
refused at a line of its own and replaying again. This spec then applied
after every earlier spec that applied (executed). `bin/rules --check` over
the applied documents printed "all 253 check lines in 62 rule files hold"
(executed). So the new `add`'s marker `nothing-declared-nothing-owed` names
cases that exist.

confirms: none
The plan's narrow set plus `tests/test_chain_check.py` exits 0 at
`d1647de2`: `bin/test tests/e2e/teammate/test_teammate_flow.py
tests/test_unverified_check.py tests/test_mode_gate.py
tests/test_first_setup_asks_once.py tests/test_seal.py
tests/test_chain_check.py -q` gave 1046 passed, nothing skipped (executed).
`bin/test-layout --pairs` over the five changed test files names one pair,
in `Test_pinned` of `tests/test_seal.py`, which phase 2 made and this fix
diff did not touch. No new case is named (executed). Each new case covers a
branch its group did not: the no-root branch in `Test_retired`, the switching
pull request in the flow, and the three non-matching pins in `Test_switch`
(read).

Facts carried from round 1 rather than re-established: where the chain
step's declaration arm lives (`chain_check.py#main`), the merge-order hold
behind `1792628098`, and `questions.md` Q2. Every verdict above was reached
this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the flow cases run or skip on the Windows legs of `.github/workflows/test.yml` (`questions.md` Q2), now two cases | `tests/e2e/teammate/test_teammate_flow.py` | the pull request's CI run on `windows-latest`, read by the orchestrator |
| The settle holds this spec behind specs refused for reasons outside this branch. The merge-order replay refuses `1792619408-an-automation-run-stops-at-the-parity-arm` at its line 192, `1792627930-the-section-sign-is-still-syntax` at its line 279, and, once both are dropped, `1792935671-the-routing-check-moves-to-the-sessions-tools` at its line 292, whose `from` is not in `docs/README.md` section *docs/*. The third was not named in round 1. The new items add `docs/the-review-record.md` *What the check reads at the pull request* and `docs/the-review-and-parity-arms.md` *The declaration, and where the check went* to the places this spec shares with the first and third | `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:292` | the orchestrator |
| A workflow pinned to a release newer than the installed one gets the "move its `--branch` line" advice, which then names an older release. No case reaches this, and whether the line should treat a newer pin differently was not judged | `skills/implement/scripts/seal.py:1842-1868` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck: not run, as contract rule 2 gives them to the broad gate after the rounds settle; the smith's suite stays `unverified` | the branch | the orchestrator, by `broad-gate` |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_round2_rules.py`, in a clone at `d1647de2`: parse and place the 17 items against `docs/` at `02ee12de`, print the two qualified sections as applied, run the overlap search over every unsettled spec, and the merge-order replay | 17 placed, no parse error; no other spec changes the two qualified sentences; three stale `from` specs dropped in turn, then this spec applied (finding 3 read from the printed sections) |
| `python3 test_tmp_round2_rules.py --write`, then `bin/test` over 13 modules that read the changed documents, then `bin/rules --check`, then `git checkout HEAD -- docs` | 2 failed, 643 passed, both failures in `test_no_passage_is_pasted_into_a_second_file.py` (finding 1); rules check exit 0 |
| `bin/test tests/test_no_passage_is_pasted_into_a_second_file.py -q` with `docs/` restored | exit 0, 8 passed |
| `bin/test tests/e2e/teammate/test_tmp_round2_probe.py -p no:xdist -s -q`: the switching pull request, the root deleted with and without a trailer, `seal` as a file, `--worktree` on an untracked root at `d1647de2` and with `chain_check.py` from a temporary worktree at `3f2f5a5d`, `--worktree` after an uncommitted switch, and the `v0.22.2` pin through `seal mode local` | as stated in findings 2 and 3 and the confirmations. It ran twice, because the first run's output filter hid the lines printed without `GITHUB_ACTIONS`; the second printed every line |
| `chain_check.py:2185` disabled, then `bin/test` on the two new finding-1 cases, then `git checkout HEAD -- skills/code-review/scripts/chain_check.py` | exit 1: both cases fail on "git does not carry this file at HEAD" |
| `bin/test` over the five plan modules and `tests/test_chain_check.py`; `bin/test-layout --pairs` over the five changed test files | 1046 passed; one pair, outside the fix diff |

The two probe files, the temporary worktree at `3f2f5a5d` and the scratch
repositories they built were removed after their runs. `git status --short`
in the clone was empty afterwards, and `git worktree list` named the clone
alone (executed). The clone itself is removed before the hand-back.
