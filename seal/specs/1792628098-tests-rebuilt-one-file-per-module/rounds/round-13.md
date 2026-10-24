# 1792628098-tests-rebuilt-one-file-per-module — review round 13

target: 1f26ecef, fixes 25285dea..1f26ecef

This round reviewed the three commits after round 12's record. 329619c7 is the framer's amendment: it rewrites `spec.md` line 109 to one criterion and adds an answer to `questions.md` at line 65. 11057142 rewrites `agents/warden.md` line 99 to `check: tests/test_a_reference_root_is_read_and_never_taken.py tests/test_settle.py tests/test_root_migrate.py`. 1f26ecef adds the last section of `phases/phase-7.md` (*Warden line 99 rewritten on a write ground, in round 12's fix pass*) and writes round 12's finding 1 `fixed 11057142`. The round asked two things. Does round 12's close hold? And do line 109's criterion and its file list hold against the rule's words and `questions.md:26`?

Every command ran in a `git clone --shared` of the branch worktree under the round's scratch directory, at 1f26ecef. `HOME`, `SPECSEAL_ANSWERS` and `TMPDIR` pointed into that directory, and the worktree's `.venv` interpreter ran pytest. Each mutant was written into the clone with the `Edit` tool and restored with `git checkout`. The clone was removed before hand-back. The implementer's account was read as claims: the three commit messages, the new section of `phases/phase-7.md`, and the `answer:` line of `rounds/round-12.md`. Each claim is named below with what the tree showed.

Some facts were carried from earlier rounds and not established again. That `chain_check.py` and `unverified_check.py` write nothing is round 12's search, carried. That s1 is red on `Test_apply::test_apply_leaves_a_team_specs_of_the_same_name_on_disk` is round 12's run, carried, because neither `settle.py` nor `tests/test_settle.py` changed in this diff. Every verdict below was reached on the tree as it stands.

## Findings

### 1. questions.md's new answer says lines 96 to 98 of agents/warden.md say nothing of reading a reference root, and line 96 tells the warden to open one

severity: should
location: `seal/specs/1792628098-tests-rebuilt-one-file-per-module/questions.md:65`
evidence: read `agents/warden.md:94-98`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/questions.md:65`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:109`, `tests/test_a_reference_root_is_read_and_never_taken.py:89-127`
verdict: fixed d57ad448
regression: round-12#1

The unit is the answer 329619c7 added at `questions.md:65`, on which files `agents/warden.md` line 99 names. The frame at `spec.md:109` says the rule states two things, that the warden opens a cited reference root in stage 1 and that the plugin never writes there, and that reading one breaks neither; the framer's answer, written in the same commit as that row, says the rule "says nothing of reading one", so the defect came from the answer's wording and not from the row, and it goes back to the framer.

Why it matters. Line 96 reads "open it in stage 1 where the work touches what it describes". That is a read of a reference root, and the rule asks for it. So the answer's premise is false of the lines it cites. The two documents now state the rule's content two ways. A reader of the answer learns that the rule is silent on reads. A reader of the row learns that it asks the warden for one. The file set is the same under both, so nothing on line 99 changes. But the old file stands on the line partly because its case goes red when the paragraph stops saying "stage 1" (`READERS` in `tests/test_a_reference_root_is_read_and_never_taken.py`, the `agents/warden.md` entry). Under the answer's premise, that half of the case pins nothing the rule says. The answer's last part has the same slip. "Rewords lines 96 to 98 to cover reads" means forbidding a check to read a team's `specs/` as the plugin's own record, and the lines already ask for one kind of read.

What the answer means is that the rule forbids no read. The fix says that.

```text
seal/specs/1792628098-tests-rebuilt-one-file-per-module/questions.md, line 65, two phrases rewritten in place:

"says the plugin never writes in a reference root, and says nothing of reading one."
becomes
"says the plugin never writes in a reference root and tells the warden to open a cited one in stage 1, and it forbids no read of one."

"rewords lines 96 to 98 to cover reads"
becomes
"rewords lines 96 to 98 to forbid a check to read a team's `specs/` as the plugin's own record"
```

The fix touches no OS boundary.

answer: d57ad448 rewrites the two phrases of `questions.md` line 65 in place as this finding's fenced block writes them: the rule says the plugin never writes in a reference root and tells the warden to open a cited one in stage 1, and it forbids no read of one; and the other direction rewords lines 96 to 98 to forbid a check to read a team's `specs/` as the plugin's own record. The file list on `agents/warden.md` line 99 does not change.

## Confirmations

confirms: round-12#1
The close holds. `agents/warden.md:99` names the old file, `tests/test_settle.py` and `tests/test_root_migrate.py` at 1f26ecef (read), and 11057142 changes that line alone (executed, `git show --stat`). `spec.md:109` now gives one ground, a case that goes red when what the rule states breaks, and the cell's last sentences keep `tests/test_routing.py`, `tests/test_chain_check.py`, `tests/test_unverified_check.py` and `tests/test_config.py` off the line on that same ground. The two grounds round 12 found in one cell are gone. Claimed: r1 and r2 are red on `Test_main::test_accepts_only_work_items_under_specs_and_names_the_rest` at `tests/test_root_migrate.py:620`, with 3 and 2 work items moved. Found the same (executed). r1 made `ITEM_RE.match(n)` the test in `old_items`: 1 failed, the message reading "moved .specseal/ and 3 work items into seal/". r2 put `True or` before `tracked_marks`'s mark test: 1 failed, "2 work items". Each failed at line 620. Against the whole file, r1 is red on that case alone, 1 failed and 71 passed, so the file holds this half of the rule in one case. Unmutated, the whole file passes, 72 passed. `bin/rules --check` exits 0, all 249 check lines in 62 rule files holding. `tests/test_a_document_that_names_a_script_says_how_to_reach_it.py` and `tests/test_a_reference_root_is_read_and_never_taken.py` pass, 37 passed and 8 skipped (executed). `git status --short` in the clone was empty after each restore.

confirms: none
The file list on `spec.md:109` holds against the rule's words and `questions.md:26`. The old file: `test_each_reader_says_when_it_reads_a_reference_root_and_where_it_cites_it` asserts that the warden's paragraph holds "stage 1", "spec.md" and a match of `never writ` (`tests/test_a_reference_root_is_read_and_never_taken.py:89-127`, read). The case reads the rule's own paragraph in the definition the warden runs on, and not a document's sentence about a rule held elsewhere, so `questions.md:26`'s clause on pinned sentences does not take it off. `tests/test_settle.py`: `settle.py:596` removes with `shutil.rmtree` (executed, `git grep`), and s1 is carried. `tests/test_root_migrate.py`: the hook moves `.specseal/` before any work item (`hooks/root-migrate.py:306-317`, read), so `seal/` exists when r1 moves the team's directory. A top-level `specs/` is then a reference root under `templates/config.md` *Reference specs*, whose table names no reference root only where no `seal/` exists. The four files left off: `hooks/config.py` and `hooks/routing.py` hold no writer, removal, rename or directory creation, the one hit being a comment at `hooks/routing.py:492`, and the one caller of `under_reference_root` outside `tests/`, `seal/` and `docs/` is `unverified_check.py` (executed, `git grep`). The class was enumerated. A `git grep` of `hooks/`, `skills/` and `bin/` for `rmtree`, `shutil.move`, `os.rename`, `os.replace`, `mv`, `os.unlink`, `os.remove` and `os.rmdir` finds two writers that reach a `specs/` directory: `settle.py:596` and `hooks/root-migrate.py`'s `git mv` and `rmdir` (executed). `seal.py:2232` renames the plugin's own root (read). The other hits were read at their grep line only, and name scratch, marker, lease or report paths. The paragraph's first half, the implementer's account as a claim at `agents/warden.md:90-94`, has no case anywhere under `tests/` (executed, `git grep` for "account is a claim", "claimed X" and "implementer's account"), and line 99 named none for it at `release/v0.22.3` either, so the cell's "two things" leaves no file off.

confirms: none
The new section of `phases/phase-7.md` matches the tree where this round re-ran it. Claimed: `has_root` gates only the stamp when nothing is left to move; `hooks/root-migrate.py:479-493` stamps under `has_root` inside the branch for no units, and runs `moves` otherwise (read). Claimed: no place outside `seal/specs/` states line 99's old file set; a `git grep` for the old adjacent pairs finds none (executed). Claimed: the D3 comment names no `check:` line; `tests/test_a_reference_root_is_read_and_never_taken.py:26-41` names the files that hold each check off a team's `specs/` and no line (read). 1f26ecef changes only round 12's `verdict:` and `answer:` lines in `rounds/round-12.md` (executed, `git diff 25285dea..1f26ecef`), and the answer's claims are the ones confirmed above.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 1f26ecef, unverified. The prompt ordered none of the three, so none was declined. The orchestrator runs the broad gate in parallel with this round. What comes due is finding 1's route to the framer, its fix and a verifying round, then the broad run at the head that leaves and the sealer's spawn | the whole tree | the orchestrator, at the broad gate |
| r3 and r4, and the boundary's 1925 passed over the 41 files that name `agents/` and `tests/test_root_migrate.py`, as `phases/phase-7.md` records them: read, not re-run | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md` | the sealer, where it samples the smith's claims |
| Round 12's rows of `## Not judged`, carried. This diff answers none of them | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/rounds/round-12.md` | as round 12 names them |

## Probes

| Command | Result |
|---|---|
| `git clone --shared` of the branch worktree into the round's scratch directory, then `git checkout --detach 1f26ecef` | the clone alone; removed before hand-back |
| `bin/rules --check` at 1f26ecef | exit 0; all 249 check lines in 62 rule files hold |
| `pytest -q -p no:xdist` over `tests/test_a_document_that_names_a_script_says_how_to_reach_it.py` and `tests/test_a_reference_root_is_read_and_never_taken.py` | exit 0; 37 passed, 8 skipped |
| `pytest -q -p no:xdist tests/test_root_migrate.py`, unmutated | exit 0; 72 passed |
| r1 in `old_items`, `n in marks if marks is not None` made `ITEM_RE.match(n) if marks is not None`, against `-k test_accepts_only_work_items_under_specs_and_names_the_rest` and then the whole file | exit 1; 1 failed at line 620, 3 work items moved; whole file 1 failed, 71 passed, that case alone |
| r2 in `tracked_marks`, `True or` put before the mark test, against the same case | exit 1; 1 failed at line 620, 2 work items moved |
| `git checkout -- hooks/root-migrate.py` and `git status --short` in the clone after each mutant | empty each time |
| `git grep` of `hooks/`, `skills/` and `bin/` for removals and renames; of `hooks/config.py` and `hooks/routing.py` for writers; for `under_reference_root` outside `tests/`, `seal/` and `docs/`; for the account half under `tests/`; for line 99's old file pairs outside `seal/specs/` | writers reaching a `specs/` directory in `settle.py` and `hooks/root-migrate.py` alone; one comment hit in `hooks/routing.py`; one caller, `unverified_check.py`; no hit; no hit |
| `chain_check.py --baseline release/v0.22.3 --root <branch worktree> --worktree`, after this record, with the branch's copy and the installed plugin's copy | each exit 0, no pull request found; three lines: this record's finding reading `open`, the guarantee behind HEAD since 264b37cf, and the guarantee's `withheld` verdict |
