# Review round 8: 1792976216-the-records-and-the-pr-checks-are-two-answers

target: e2b1e994, fixes 352fc126..e2b1e994

## Findings

### 1. The unmerged-entry case fails on the Windows leg, because its fixture feeds `update-index --index-info` in text mode and every path it writes ends in a carriage return

severity: must
location: `tests/test_seal.py:3420-3425`, `tests/test_seal.py:3427`
evidence: executed `gh -R MichaelYcJo/SpecSeal run view 40269788492 --log-failed`, `python3 -I test_tmp_crlf_index_info.py`, `bin/mutation-check tests/test_seal.py --replace <the two lines at 3421-3422> <the two lines below>`
verdict: fixed 24fe948a
regression: round-6#1

The unit is `Test_pr_checks.test_refuses_an_index_entry_it_cannot_read_deleted_by_hand`, which `1fb674c7` added for round 6's finding 1. The frame, `spec.md` *In* item 3 and the phase 2 row of `plan.md`, asks that `seal pr-checks remove` refuse and name an index entry it cannot read, such as an unmerged path, and names no fixture. The fix built that state by writing three stage lines to `git update-index --index-info` through `subprocess.run(..., input=..., encoding="utf-8")`. The defect came from how that fixture was written, not from the frame.

Why it matters: the branch's `tests` workflow fails on its Windows leg at every commit that carries `1fb674c7`, `e2b1e994` included, and this round's broad run on macOS cannot show it.

The grounds. Run 40269788492 at `c3b9895e` failed three distinct cases, not two (executed, `gh run view --log-failed`). Two are the census cases `e2b1e994` answers, on the ubuntu, macOS and Windows legs. The third is this case on `windows-latest, 3.12, --splits 4 --group 3`, at `tests/test_seal.py:3427`, with `assert 0 == 3`: `update-index` exited 0, and `ls-files --unmerged -- .github/workflows/hygiene.yml` then listed nothing. The smith's commit message for `e2b1e994` says the run "found unaccounted" the census row, which holds. The orchestrator's spawn prompt says the run failed "on the same cases" as the broad run, which does not: the third failure stands unanswered.

The cause. With `encoding` given, `subprocess.Popen` wraps stdin in an `io.TextIOWrapper` with no `newline` argument (read, `subprocess.Popen.__init__` in the local CPython). Such a wrapper writes each `\n` as `os.linesep`, which is `\r\n` on Windows. `update-index --index-info` ends a line at the line feed only, so the carriage return stays in the path. The probe fed the same three lines as bytes on macOS (executed, git 2.50.1). With `\n` endings, `update-index` exited 0 and the scoped `ls-files --unmerged` gave 3 lines. With `\r\n` endings, `update-index` also exited 0, but the scoped listing gave 0 lines. The unscoped listing showed the entry under the path `".github/workflows/hygiene.yml\r"`. With `-z` and NUL endings, it gave 3 lines. That is the Windows symptom exactly, reproduced on POSIX bytes. The step from `\n` to `\r\n` on Windows is read from CPython, not run here.

Only one stdin feed in this branch's tests has the problem. The branch adds one `input=` to `tests/`, `skills/` and `hooks/`, and it is this one (executed, `git diff 02ee12de..e2b1e994` searched for `input=`). The two in `tests/conftest.py` are `json.dumps` payloads that the branch did not add, and they carry no line feed.

The fix below, applied as a mutant in the round's clone, left the case and the census cases passing on macOS: 12 passed, so `bin/mutation-check` printed SURVIVED, which here means the fix keeps the cases green (executed). It holds only on the Windows leg, and the tests workflow is the check for that. The fix keeps both `ls-files` calls, so the census row `e2b1e994` added stays true at 2. Precondition: git's `-z` with `--index-info` reads NUL-terminated records, and a NUL written through the text wrapper is not translated on any platform.

```python
        done = subprocess.run(
            ["git", "-C", str(repo), "update-index", "-z", "--index-info"],
            # NUL-terminated: in text mode Python writes "\n" as os.linesep,
            # so on Windows each path would end in a carriage return.
            input="".join(f"100644 {blob} {n}\t{rel}\0" for n in (1, 2, 3)),
            capture_output=True,
            encoding="utf-8",
        )
```

answer: The finding holds. Counted from the reframe after round 3, this is the third finding round, so the finding takes the filing ladder's first rung: the branch owns the unit, and the fix goes in the diff. The unit is the case `1fb674c7` added, not the hand-deleted branch round 6 found, so it is that case's first regression. The smith fixed it in 24fe948a: the case feeds `git update-index -z --index-info` three NUL-terminated records, so text-mode stdin has no newline to translate. It was shown red on macOS with the old lines written as Windows writes them (`assert 0 == 3` at `tests/test_seal.py:3427`), green after, and mutants dropping `-z` or changing the terminator are red. The branch's other stdin writes were searched and none is in the same shape (executed by the smith). The Windows leg is read by the orchestrator from the branch's `tests` run after this commit.

## Confirmations

confirms: none
The census row `e2b1e994` adds is honest by the census's own grounds and is not a weakening (read, `tests/test_a_shrunken_corpus_declines_to_judge.py:126-144`, `tests/test_seal.py:3411-3438`). The case works in a copy of a world that the `take` fixture makes under the case's own `tmp_path` (`tests/test_seal.py:179-189`). Table 6, `LISTS_A_FIXTURE`, says its scope lists a repository the case built, and that holds. The scope's two `ls-files --unmerged` calls count lines and open no listed path. The listed path is gone from disk on purpose, so `on_disk` would be asserting the fixture against itself. Table 5, `OPENS_NOTHING`, also fits by its words. But `dict.fromkeys` fixes its count at 1 (line 154), so only tables 1 and 6 can carry a count of 2. Table 6 already holds the nearest precedent, `tests/conftest.py#staged`. The repository spelled the same choice in an earlier work item's `overview.md:32`, two `--name-only` fixture scopes put in `LISTS_A_FIXTURE`. Three mutants of the census were all red (executed, `bin/mutation-check`). The count 2 made 1 gave a miscount. The row removed reproduced the two cases run 40269788492 failed. `**LISTS_A_FIXTURE` made `dict.fromkeys(LISTS_A_FIXTURE, 1)` showed that the map's counts carry. A third `ls-files` call planted in the case's scope was red with `(3, 2)` (executed). So a further call is still caught, and the row widens nothing beyond the two calls it counts.

confirms: none
The rewritten comment above `PATH_LIST_CALLS` states the tree truly (read, `tests/test_a_shrunken_corpus_declines_to_judge.py:146-156`). The old first sentence, "One call per scope everywhere today", became false with the new row, and the commit removed it. The new sentence says the map holds call counts so that a further call inside a classified scope goes red. Tables 2 to 5 enter the map at 1 and tables 1 and 6 at their own counts, and the planted third call above went red. The old sentence stands nowhere else in the tree (executed, `git grep -n -i "one call per"` at `e2b1e994`, whose one match is an unrelated row of another work item's `plan.md`). The new row's comment holds too. The case writes stages 1 to 3 of one path into the index through `update-index --index-info`, and counts that path's unmerged entries once before and once after `remove`.

confirms: none
No other scope this branch added to `tests/` derives a path list from git unclassified. The census module passes at `e2b1e994`, 9 passed (executed, `bin/test tests/test_a_shrunken_corpus_declines_to_judge.py -q -p no:randomly` in the clone). Its reader reads literal words only, so the branch's test diff was searched for the listing words and for `LS_FILES` too (executed, `git diff 02ee12de..e2b1e994 -- tests` searched for `ls-files`, `ls-tree`, `name-only`, `LS_FILES` and `git_listing`). It added three spellings. Two are this case's calls. The third is `unanswered = ("ls-tree", "HEAD", "--", "seal")` at `tests/test_chain_check.py:3410`, the argument tuple a monkeypatched `chain.git` answers `None` for, which lists nothing. The census reads only `tests/*.py`, so the listing calls the branch added to `skills/implement/scripts/seal.py` are outside it, as before.

confirms: none
This branch made neither of the smith's two older mismatches worse (executed, `git grep` at `02ee12de` and `e2b1e994`). `LS_FILES = "ls-files"` is defined and used nowhere in `tests/test_seal.py` at both commits. It sits at line 111 at the base and line 112 now, and a line the branch added above it moved it. The census's two messages say "one of the five tables above" while the comment at line 63 says six. The text is the same at the base, and `git diff 02ee12de..e2b1e994` of the module holds only `e2b1e994`'s two hunks, which touch neither message. Run 40269788492 printed "five tables", and the smith still chose among the six.

confirms: none
`e2b1e994` passes its own narrow checks (executed). `uvx ruff check` and `uvx ruff format --check` over the changed module exit 0. The commit carries the work item's `SpecSeal-Routing` trailer, and the repository's identity is both author and committer (`git log -1 e2b1e994`). The fix adds no test function, so no new test is read against its group.

Two facts were carried from round 7 and not re-established: the range `dc07a4ea..352fc126` reviewed there, and the `remove_workflow` states its probe measured. This range changes only the census module and round 7's record. Round 7 opened no finding, so no close of it is owed an answer here. Every verdict above was reached this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `e2b1e994`, not run because contract rule 2 gives them to the broad gate. `broad-gate.md` still holds the run at `4b63982f`. The orchestrator's run at `c3b9895e` is a claim of the spawn prompt, and this round read only CI run 40269788492 at that commit. The smith's suite stays `unverified`. This round leaves finding 1 open, so the fix pass comes before the broad run | the branch | the orchestrator, by `broad-gate` after the fix pass |
| Whether finding 1's fix passes on Windows. It was executed on macOS only, and a broad run on macOS cannot show it | `tests/test_seal.py:3420-3425` | the orchestrator, by the branch's `tests` workflow on its Windows legs |
| Whether, on Windows with `core.autocrlf` off, the index copy `install` stages compares equal to `plugin_workflow()` in the hand-deleted arm. Carried from round 7, and it belongs to the same class as finding 1: text-mode newline translation on Windows | `skills/implement/scripts/seal.py:2040` | the orchestrator, who decides whether a Windows case is owed |
| `questions.md` Q1 and Q4 stay open for the owner, built on their defaults (a). Carried from round 6 | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/questions.md` | the owner, relayed by the orchestrator in the pull request body |
| The settle holds this spec behind specs refused for reasons outside this branch. Carried from round 2, and not replayed | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/overview.md:25` | #1033, and the orchestrator at the settle that applies this release's specs |
| `guarantee.md` is behind HEAD, and its verdict reads withheld on the defect `83ccc9ae` answered | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/guarantee.md:36` | the sealer, at its next run after the broad gate |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the repository into the round's scratch directory, checked out at `e2b1e994` | clone at `e2b1e99`; `git status` stayed empty after every probe below |
| `bin/test tests/test_a_shrunken_corpus_declines_to_judge.py -q -p no:randomly` in the clone | 9 passed, exit 0 |
| `bin/mutation-check tests/test_a_shrunken_corpus_declines_to_judge.py` with three `--replace` pairs: the new row's count 2 made 1, the row removed, `**LISTS_A_FIXTURE,` made `**dict.fromkeys(LISTS_A_FIXTURE, 1),`; `--tests "bin/test tests/test_a_shrunken_corpus_declines_to_judge.py -q -p no:xdist -p no:randomly"` | baseline passed; 3 mutants, 3 red, 0 survived |
| `bin/mutation-check tests/test_seal.py --replace 'it never read."""' 'it never read."""; git_out(take, "ls-files")'` with the census module as its tests | red: `test_no_scope_in_the_suite_lists_paths_from_git_without_a_guard` reported `{'tests/test_seal.py#test_refuses_an_index_entry_it_cannot_read_deleted_by_hand': (3, 2)}`, and `test_an_unguarded_scope_is_named_although_a_module_is_mid_edit` failed as well |
| `gh -R MichaelYcJo/SpecSeal run view 40269788492 --log-failed`, and `--json headSha,conclusion` | head `c3b9895e`, failure. The census case and the mid-edit case failed on the ubuntu, macOS and Windows group 1 legs. `Test_pr_checks::test_refuses_an_index_entry_it_cannot_read_deleted_by_hand` failed on Windows group 3 at `tests\test_seal.py:3427` with `assert 0 == 3` |
| `gh run view` of runs 40266182294 and 40264357704 for their head commits, and `git merge-base --is-ancestor 1fb674c7` against each | the two green runs are at `2cf62b72` and `895db45e`, and both ancestry checks exit 1: neither carries `1fb674c7` |
| `python3 -I test_tmp_crlf_index_info.py`: three `git init` repositories in the round's scratch directory, one blob, three stage lines fed as bytes to `update-index --index-info` with `\n`, with `\r\n`, and with `-z` and `\0` | exit 0 in all three. The scoped `ls-files --unmerged` listing gave 3, 0 and 3 lines. With `\r\n` the unscoped listing names `".github/workflows/hygiene.yml\r"` |
| `bin/mutation-check tests/test_seal.py` with finding 1's fix as its one `--replace` pair; `--tests "bin/test tests/test_seal.py tests/test_a_shrunken_corpus_declines_to_judge.py -q -p no:xdist -p no:randomly -k 'deleted_by_hand or path_list or unguarded or helpers'"` | SURVIVED, 12 passed: the fix keeps the case and the census green on macOS |
| `uvx ruff check` and `uvx ruff format --check` over `tests/test_a_shrunken_corpus_declines_to_judge.py` | both exit 0 |
| `git diff 02ee12de..e2b1e994` of `tests`, `skills` and `hooks`, searched for `input=` and for the listing words; `git grep` for `LS_FILES`, "five tables", "six tables" and "one call per" at `02ee12de` and `e2b1e994` | one new `input=`, this case's; three new listing spellings, as the confirmations give them; the two older mismatches read the same at both commits; the old comment sentence stands nowhere |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.4 --root <the branch worktree> --worktree`, the plugin's copy, after this record | exit 0; it names finding 1 as reading `verdict: open`, and repeats the notices that `broad-gate.md` and `guarantee.md` are behind HEAD and that the sealer's verdict reads withheld |

The probe file, its three repositories, the clone and its virtual environment, and the saved outputs were removed before the hand-back.
