# Review round 2: 1793457436-row-deletion-check-and-a-symlink

```seal
target: 1fbecdf9, fixes 10b696cd..1fbecdf9
```

This is a verifying round. It reads the fix diff `10b696cd..1fbecdf9`: the fix pass's d64de886 (`skills/verify/scripts/unverified_check.py`, `tests/skills/test_unverified_check.py`, `changelog.md`, `gaps.md`), the close block of round 1's finding 1 (850b357d), and the orchestrator's fold of the frame (1fbecdf9). The work ran in the branch worktree at 1fbecdf9 and in a `git clone --no-local` of it under the round's scratch directory, with worktrees of that clone at 10b696cd and a92c358b.

Carried from round 1 as coordinates and not established again: the presence arm builds `here` from the unresolved paths; `#overviews` resolves each argument once with `real()` and walks without following linked directories; the `linked` fixture runs in both link orders; the two Windows rows of `## Not judged`. Every verdict below was reached this round.

## Findings

### 1. The frame still states two facts the fix made false: no mode read, and two changed report lines

```seal
severity: should
location: `seal/threads/1793457436-row-deletion-check-and-a-symlink/frame/design.md:36`, `seal/threads/1793457436-row-deletion-check-and-a-symlink/frame/plan.md:43`
evidence: read `seal/threads/1793457436-row-deletion-check-and-a-symlink/frame/design.md:36`, `seal/threads/1793457436-row-deletion-check-and-a-symlink/frame/plan.md:43`, `skills/verify/scripts/unverified_check.py:1454-1464`
```

Why it matters: the fold in 1fbecdf9 rewrote `frame/design.md` *Data & interfaces* to state the new mode read and a third changed report line. It left two sentences that stood on the old facts, and both are now false. Contract rule 19 asks a change to correct, in the same commit, every other sentence stating the fact it changed. The sealer reads the frame against the changelog and the tree, and the settle reads the design. Each of them would read a sentence the tree contradicts.

- `frame/design.md:36`, *Scope*, *Out*, the first bullet, gives as its reason for leaving the reverse case alone that it needs "asking git for the path's mode at the base, a read this check does not make today". Since d64de886 the check makes that read: `#mode_at` (`skills/verify/scripts/unverified_check.py:1454-1464`) runs `git ls-tree` at the base for each scanned link. The plan's new *Judgments of the run* row keeps the case out "as *Scope* says", so it rests on that sentence. The case itself still behaves as the frame says: probe P7 below exits 0 at all three revisions with the same `not compared` notice.
- `frame/plan.md:43`, *Operational impact*, says "Two report lines change for a person who reads them" and "The changelog fragment states both under *Fixed*". The folded `frame/design.md` *Data & interfaces* now says three, and the changelog fragment states the third: a loss reported under the link's own path.

The class was listed by `git grep -n -i -E "does not make today|Two report lines|two places|report lines change|mode at the base"` over the work item, `docs/` and `skills/verify/` (executed). It found these two sentences, the folded line, and the plan's judgment row, which is correct. This is a search on wordings, so it is a sample (contract rule 12).

The fix rewrites both sentences in place. In `frame/design.md` *Scope*, *Out*, the first bullet:

```markdown
- **A link at the base replaced by a real file** (probe 5). The run names the file as not compared and exits 0. No row left the record, because the link's target still holds every row. The notice's reason (`no ## Not verified section`) is imprecise. Making it precise means asking `#mode_at` for every scanned real file as well as for each link, one more `git ls-tree` per closing memo, for a case that passes no deletion. It is left as it stands.
```

In `frame/plan.md` *Operational impact*, the second and third sentences:

```markdown
Three report lines change for a person who reads them: a deletion found through a link names the target's path; a link to a file outside the repository is listed under `not compared` with a new reason; and a closing memo that was a file at the base and is a link now is reported under the link's own path where it holds fewer rows. The changelog fragment states all three under *Fixed*.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: a closing memo that was a file at the base and is a link now no longer loses its rows with exit 0. The fix pass claimed the new arm compares such a link at its own path; `skills/verify/scripts/unverified_check.py:1680-1706` does that, after the per-file loop, for each scanned path that `os.path.islink` reports and whose base mode is not `120000`. Round 1's probe was written again from its `## Probes` row as P1 of `test_tmp_round2.sh`, and run against three revisions (executed):

- P1, the link at `specs/a` and at `specs/z` beside `specs/b`, scanning `specs`: exit 1 at 1fbecdf9 in both orders, naming the link's own path with `3 rows at HEAD~1, 1 here`. At 10b696cd both exit 0. At a92c358b `specs/a` exits 1 and `specs/z` exits 0. These are round 1's results, and the changelog's sentence that such a link sorting after its target used to pass is true.
- The rest of the class round 1 named (every scanned path that is a link here and was a file at the base): P2, the link's directory scanned alone, and P9, run from `specs/` with `.`, exit 1 at 1fbecdf9 in both orders. P4, a file replaced by a link to a one-row memo outside the repository, exits 1 at 1fbecdf9 and names the target under the outside notice; it exits 0 at 10b696cd.
- No new refusal: P5, a link new on the branch to an unchanged memo, exits 0 with no notice at every revision. P6, a link that was a link at the base, its target shrinking, reports one deletion under the target only. P8, a link to a memo with no section, is counted unreadable and exits 1 at every revision, as before.

The departure the close names holds. The paste-ready text skipped a base mode of None; the fix skips only `120000`, so a path the base does not hold goes on to `compare_at`, whose `show` answers None (`skills/verify/scripts/unverified_check.py:1472-1474`). P5 shows the same outcome as the proposal for that path. Where `git ls-tree` itself fails, the fix reads the base with `show` rather than skipping, which errs toward reading. `Test_compare_at::test_accepts_a_path_the_base_does_not_hold_as_nothing_to_compare` (`tests/skills/test_unverified_check.py:1793`) pins that branch.

The fix pass claimed `test_refuses_a_memo_replaced_by_a_link_to_one_holding_fewer_rows` exited 0 in both orders against 10b696cd. This round did not run the pytest case against that code. It ran the same fixture shape through the command line in P1: exit 0 in both orders at 10b696cd, so the case's `== 1` assertion would fail there.

The one sibling left open is a link named as the argument itself. P3 runs `specs/a/gaps.md --baseline HEAD~1` and exits 0 at 1fbecdf9, 10b696cd and a92c358b, in both link orders. So the claim that it predates this work holds. Its home is `gaps.md` *Not done* and issue #1225, open (`gh issue list --state open`, executed). Round 1 defined its class as scanned paths, and an argument is resolved before the scan, so the close does not leave its own class open.

```seal
confirms: none
```
What matched: `#mode_at` and `#compare_at`, the two units nobody had reviewed. `mode_at` (`skills/verify/scripts/unverified_check.py:1454-1464`) runs `git -C <root> ls-tree <ref> -- <rel>` and returns the first field, or None on a nonzero exit or empty output. Its docstring names None only for a path the ref does not hold, and the caller treats both Nones alike, as not a link. In the new arm `rel` is never None: each scanned path lies under an argument that `main` refused before the loop where it had no relative form (`unverified_check.py:1605-1617`). A second argument in another repository on the same volume gives a `../` form. There `ls-tree` and `show` both fail, `compare_at` answers None, and the main loop has already named that real path as outside the repository. `compare_at` (`unverified_check.py:1467-1500`) is the body removed from `main`, with the same two messages. It takes the git path `at` and the reported path `rel` apart, so the new arm reads the base at the link's path and reports under the link's display path. Read.

```seal
confirms: none
```
What matched: the new cases, read against their groups. The module gives one class per function (`tests/skills/test_unverified_check.py:1`). `Test_mode_at` covers a link, a file and an absent path. `Test_compare_at` covers fewer rows, as many rows (the `<` boundary), a path the base does not hold, and an unreadable base section. No case repeats another in its class. `bin/seal layout --pairs` exited 0 and names no pair among them. The `Test_main` case (`tests/skills/test_unverified_check.py:2261`) sits beside the link-order case at line 2239 and covers the transition that case does not: a file at the base that is a link here. Executed and read.

```seal
confirms: none
```
What matched: the folded *Data & interfaces* bullet (`frame/design.md:55`) describes the arm at `unverified_check.py:1680-1706` as it stands. The `unique_by_target` docstring (`unverified_check.py:1113-1118`) and the arm's comment were rewritten in place to state the second read. The changelog fragment states the third report line. Read.

```seal
confirms: none
```
What matched: the module runs green through the runner. `bin/test tests/skills/test_unverified_check.py -q` gave 366 passed, exit 0, with no skips on macOS. `uvx ruff check` and `uvx ruff format --check` on the two changed code files exited 0. Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the link cases run or skip on the Windows legs (`frame/questions.md` Q1), carried from round 1 | `tests/skills/test_unverified_check.py` | a measurement: the Windows legs of `.github/workflows/test.yml` on this pull request; naming a skip there is #1221's |
| What Windows `os.path.realpath` and `os.path.islink` answer for a tracked link whose target is on another drive, run end to end, carried from round 1 | `skills/verify/scripts/unverified_check.py:1659`, `skills/verify/scripts/unverified_check.py:1688` | a maintainer with a Windows machine holding two drives |
| The fix pass's four `seal mutate` runs, not re-run this round | `trail/rounds/round-1.md`, the close block of finding 1 | the sealer, at its sample of the crafter's claims |
| The full suite, the repository-wide `ruff check` and `ruff format --check`. The crafter's `unverified` label for them is honest: `gaps.md` names the orchestrator as their answerer | `gaps.md` | the orchestrator, through `seal gate`, once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `sh <scratch>/test_tmp_round2.sh`, seven fixture repositories, each run against `unverified_check.py` at 1fbecdf9, 10b696cd and a92c358b | P1 (file to link, scanning `specs`): 1fbecdf9 exit 1 in both orders naming the link; 10b696cd exit 0 in both; a92c358b exit 1 for `specs/a`, 0 for `specs/z`. P2 (the link's directory alone) and P9 (`.` from `specs/`): 1fbecdf9 exit 1 in both orders. P3 (the link named as the argument): exit 0 at all three revisions in both orders. P4 (file to link outside the repository): 1fbecdf9 exit 1 with the outside notice; 10b696cd exit 0. P5 (new link): exit 0 everywhere. P6 (base link kept, target shrinks): 1fbecdf9 exit 1, one line under the target. P7 (base link replaced by a file): exit 0 with the same notice everywhere. P8 (link to a memo with no section): exit 1, one unreadable, everywhere |
| `bin/test tests/skills/test_unverified_check.py -q`, in the worktree at 1fbecdf9 | 366 passed, exit 0 |
| `bin/seal layout --pairs`, in the worktree | exit 0 |
| `uvx ruff check` and `uvx ruff format --check` on `skills/verify/scripts/unverified_check.py` and `tests/skills/test_unverified_check.py` | exit 0 each |
| `gh issue list --state open --search "link argument unverified"` | #1225, open: the argument-named link |
