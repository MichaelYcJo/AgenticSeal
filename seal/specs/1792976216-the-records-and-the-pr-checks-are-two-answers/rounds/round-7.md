# Review round 7: 1792976216-the-records-and-the-pr-checks-are-two-answers

target: 352fc126, fixes dc07a4ea..352fc126

## Findings

This round opens no finding. It read `dc07a4ea..352fc126`: the frame's
rewrite of `spec.md` *In* item 3 at `5a210589` and `352fc126`, the smith's
fix at `1fb674c7` in `skills/implement/scripts/seal.py` and
`tests/test_seal.py`, and round 6's `answer:` line. It read them against
`spec.md` *In* item 3 (lines 101 to 125) and the `seal pr-checks remove` row
of *Data & interfaces*. No new regression stands on `remove_workflow`, so
the round cap's route for a second regression on one unit does not apply.

## Confirmations

confirms: round-6#1
The three states round 6 reported now keep the edit and say why (executed,
`python3 test_tmp_remove_states.py`). In each one, the index held an edit
and the working file had been deleted by hand. With a staged edit after
`install` (`AD`), the command exits 1 and the status stays `AD`, and the same
holds on a branch with no commit. With a copy pinned to an older release
(`AD`), it exits 1. With a committed copy carrying a staged edit (`MD`), it
exits 1. The status is unchanged in each, and no index blob became
unreachable. Each prints the new refusal: the index copy "is neither byte for
byte the copy HEAD carries nor byte for byte what this plugin writes NOW"
(`seal.py:2040-2048`). The unmerged index with the working file gone now
exits 1 with the unreadable reason (`seal.py:2016-2022`), not the clone-line
reason, and its three stages stay. The smith claimed that the four refusing
cases were seen red against `5a210589`. That commit changes only `spec.md`
and the round record (executed, `git diff --stat dc07a4ea 5a210589`). With
`seal.py` restored from `dc07a4ea` in the scratch clone, exactly those four
failed: the three ids of
`test_refuses_an_index_copy_no_other_copy_keeps_deleted_by_hand` and
`test_refuses_an_index_entry_it_cannot_read_deleted_by_hand`. The other five
`deleted_by_hand` cases passed (executed). The smith also claimed five
mutants of the condition were red, and did not name them. This round ran
seven mutants of its own on the arm. Six went red and one survived. The
survivor is the confirmation entry on edges below, and it changes nothing in
any state this round could build. The close holds.

confirms: none
`spec.md` *In* item 3 as rewritten (lines 113 to 123) names one order: the
clone line first, then exactly two copies the index may give up, HEAD's copy
or what `install` writes now. `seal.py:2015-2048` reads in that order
(read). The probe shows why the order matters. A committed file without the
clone line, deleted by hand (` D`), equals HEAD's copy. It is refused with
exit 1 by the clone-line test, before the HEAD test could take it
(executed). This is the state round 6's `answer:` line says the smith found.
The sentence "Either way a copy survives the removal" holds in every state
that exits 0 (executed). There, each index blob the command dropped is
either byte for byte what this plugin writes now or HEAD's own blob, apart
from the CRLF state the next entry judges. The old
rule's wording, "the same rule as a working file" and "by the rule a working
file is", stands nowhere in the tree outside the round records (executed,
`git grep`). The comment above the arm and the docstring of the refusing
case at `tests/test_seal.py:3347` were rewritten in the same commit (read).

confirms: none
Every other state of the workflow path is removed or kept as the frame says,
with a true line (executed, `python3 test_tmp_remove_states.py`, 37 states
in all). With nothing anywhere, and with the deletion already staged (`D `),
it exits 0 with the nothing-to-remove line. An untracked copy equal to what
`install` writes is deleted, exit 0. An untracked copy with an edit, an older
pin or no clone line is kept, exit 1. `install` then `remove` is forced out,
exit 0, status empty, on a branch with and without a commit. A never-committed
copy is kept with exit 1 in three cases: a staged edit, a working edit over
the plugin's index copy, and the plugin's working copy over an edited index.
A committed clean copy is removed and the removal staged. A committed copy
with an unstaged or a staged edit is kept by git's refusal, exit 1. A
symbolic link is kept, exit 1. A committed file with mode 000 is kept as
unreadable, exit 1. A committed file without the clone line is kept, exit
1. With the working file gone, the plugin's copy staged by `install` (`AD`)
leaves the index, exit 0, status empty, on both branches. So does a
committed copy whose deletion was not staged (` D`), whether it is the
plugin's copy, an older pin, or a committed edit, and the deletion is then
staged. An index copy that is the plugin's copy now over an older pin in
HEAD (`MD`) leaves the index and the deletion is staged. An index copy
without the clone line, with HEAD lacking the path (`AD`) or carrying it
(` D`), is kept, exit 1. An index copy pinned to an older release over
somebody's committed file is kept, exit 1.

confirms: none
Five edge states were judged, and none is a finding.

- HEAD carries somebody's workflow without the clone line, and the index
  holds the plugin's copy now, with the working file gone (`MD`). The
  command exits 0 and stages the deletion of somebody's committed file
  (executed). The frame's second case allows this, since the index copy is
  byte for byte what `install` writes now. HEAD still holds somebody's
  file. With the file present, git's own refusal keeps the same state with
  exit 1, so the absent arm is the looser of the two. Nothing is lost,
  though: the index entry can be written back by `install`, and somebody's
  file stays in HEAD. To reach the state, the person must first take
  somebody's file out themselves, because `install` refuses over it
  (`seal.py:1922-1927`, read).
- An index entry whose mode alone differs from HEAD's (100755 over 100644,
  an older pin) is kept, exit 1 (executed). The refusal says the copy is not
  "byte for byte the copy HEAD carries", but the bytes are the same and only
  the mode differs. The comment at `seal.py:2031-2034` says the test reads
  the blob and the mode. Refusing keeps the one edit only the index holds,
  the mode, so the arm fails closed. No flow of this command makes the
  state.
- An intent-to-add entry (`git add -N`) with the file gone is kept with the
  clone-line reason, exit 1 (executed). The entry holds no content, so the
  reason is loose, but nothing is removed.
- An index copy with CRLF line endings that are otherwise the plugin's copy
  now leaves the index, exit 0 (executed). The CRLF blob is then
  unreachable. `staged_text` decodes in text mode (`seal.py:1738-1757`, read).
  `install` writes in text mode too (`seal.py:1956`, read), so on Windows
  with `core.autocrlf` off the copy `install` stages is that CRLF blob, and
  the comparison has to read it as the plugin's. On POSIX the only bytes
  lost are carriage returns, which `install` writes back as plain line
  feeds. The Windows half is read only, and it is a row of `## Not judged`.
- A committed copy marked skip-worktree, with the file gone, is kept, exit
  1. Git's `rm` refuses a path outside the sparse-checkout definition, and
  the command prints git's reason (executed).

The surviving mutant turns `as_head.returncode == 0` into
`as_head.returncode != 1`, which would read a git failure as "HEAD's"
(executed, `bin/mutation-check`). A second probe pointed HEAD at an object
git does not have. There, `git diff --cached --quiet` still exited 1, and a
staged edit with the file gone was kept, exit 1 (executed, `python3
test_tmp_bad_head.py`). This round could build no state where the
comparison exits outside 0 and 1 while the index copy reads. So the mutant
is equivalent in every state measured, and the fail-closed reading the
comment claims is read, not pinned.

confirms: none
The narrow line holds at `352fc126` (executed). `bin/test tests/test_seal.py
-q -p no:randomly -k "Test_pr_checks or Test_remove_workflow"` gave 27
passed. `uvx ruff check` and `uvx ruff format --check` over the two changed
Python files exited 0. `bin/test-layout --pairs tests/test_seal.py` printed
one pair, in `Test_pinned`, which the range does not touch. The two new
tests in `Test_pr_checks` each cover a state no other case in the group
reached: four of their ids failed against `dc07a4ea`'s `seal.py`. The two
new ids of the existing cases, ` D, another release` among the accepting
ids and ` D` among the clone-line refusals, are the ones the mutants that
drop the HEAD test and the clone-line test reach (read, against the
`bin/mutation-check` result). Every commit in the range carries the work
item's `SpecSeal-Routing` trailer. The repository's identity is both author
and committer (executed, `git log`).

These facts were carried from earlier rounds, not re-established. One is
S8's applied replay from round 4: this range changes no `## Rule changes`
item, nothing under `docs/` and neither README (executed, `git diff
--stat`). Another is round 5's result that `git rm` of a path missing from
the working tree exits 0 in the `AD` and ` D` states. The smith's
measurement is the third: on a branch with no commit, git 2.50.1 compares
the index with the empty tree. This round's probe showed the second and the
third again in passing. Every verdict above was reached this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `352fc126`. Not run, because contract rule 2 gives them to the broad gate after the rounds settle. The run `broad-gate.md` holds predates `83ccc9ae`, `0aaa5e41` and `1fb674c7`, which each change `skills/implement/scripts/seal.py`, so the smith's suite stays `unverified`. This round leaves nothing open, so the broad run is now due, and the sealer's spawn after it | the branch | the orchestrator, by `broad-gate` |
| Whether, on Windows with `core.autocrlf` off, the index copy `install` stages compares equal to `plugin_workflow()` in the hand-deleted arm. Read only: no case reaches that state, and this round ran on macOS | `skills/implement/scripts/seal.py:2040` | the orchestrator, who decides whether a Windows case is owed |
| `questions.md` Q1 and Q4 stay open for the owner, built on their defaults (a). Carried from round 6 | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/questions.md` | the owner, relayed by the orchestrator in the pull request body |
| The settle holds this spec behind specs refused for reasons outside this branch. Carried from round 2, and not replayed | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/overview.md:25` | #1033, and the orchestrator at the settle that applies this release's specs |
| `guarantee.md` is behind HEAD and its verdict reads withheld, on the defect `83ccc9ae` answered | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/guarantee.md:36` | the sealer, at its next run after the broad gate |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_remove_states.py` in the round's scratch directory: `git init` repositories driven through the scratch clone's `bin/seal` at `352fc126`, git from Python, `git fsck --unreachable --no-reflogs` after each run | 37 states, as the confirmations give them; every blob left unreachable decoded as the plugin's copy now, the CRLF one only after newline decoding, and the three states of round 6's finding exited 1 with their blobs in the index |
| `python3 test_tmp_bad_head.py`: HEAD's ref set to an object git lacks, a staged edit, the file gone | `git diff --cached --quiet` exited 1; `remove` exited 1 with the neither-copy refusal; the index entry stayed |
| `bin/test tests/test_seal.py -q -p no:randomly -p no:xdist -k deleted_by_hand -rA`, with `seal.py` checked out from `dc07a4ea` in the scratch clone, then from `352fc126` again | 4 failed, 5 passed: the three ids of the no-other-copy case and the unreadable case failed; `git status` was empty after the restore |
| `bin/mutation-check skills/implement/scripts/seal.py` with seven `--replace` pairs on the absent arm and `--tests "bin/test tests/test_seal.py -q -p no:xdist -k 'Test_pr_checks or Test_remove_workflow'"` | baseline passed; 6 red, 1 survived: the HEAD test dropped, the install test dropped, the refusal made `False`, the clone-line test made `False`, `--cached` dropped, and the unreadable reason's wording, all red; `returncode == 0` turned into `returncode != 1` survived |
| `bin/test tests/test_seal.py -q -p no:randomly -k "Test_pr_checks or Test_remove_workflow"` | 27 passed |
| `bin/test-layout --pairs tests/test_seal.py` | 1 pair, `Test_pinned` |
| `uvx ruff check` and `uvx ruff format --check` over `skills/implement/scripts/seal.py` and `tests/test_seal.py` | both exit 0 |
| `git diff --stat dc07a4ea 5a210589`; `git diff --stat dc07a4ea..352fc126`; `git grep` for the old rule's two spellings; `git log` with author, committer and trailers over the range | `5a210589` touches only `spec.md` and the round record; the range touches `spec.md`, the round record, `seal.py` and `test_seal.py`; the old spellings stand nowhere outside the round records; every commit carries the trailer under the repository's identity |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.4 --root <the branch worktree> --worktree`, the plugin's copy, before and after this record | exit 0 both times; the notices that `broad-gate.md` and `guarantee.md` are behind HEAD and that the sealer's verdict reads withheld stand |

The two probe files, their repositories and the scratch clone were removed
before the hand-back.
