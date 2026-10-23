# 1792628098-tests-rebuilt-one-file-per-module — review round 8

target: fb455bee, fixes 7891de9e..fb455bee

This round reviewed the seven commits after round 7's record, from 7891de9e to fb455bee. They are ca66eca5, which writes `broad-gate.md` and `changelog.md`; 62089da5, 28433aef, 46dec486 and 95f139e1, the sealer's four readings of `guarantee.md`, with 46dec486 also rewriting `overview.md` line 5 and `changelog.md` line 3; 264b37cf, which moves two cases into their modules' files; and fb455bee, which records that move in `phases/phase-7.md`, `phases/phase-6.md` line 1004 and `overview.md` line 19. The sealer's fourth reading at 95f139e1 withheld because two cases stood in another module's file after the group that placed their module (`guarantee.md` lines 39, 60 and 64 at 95f139e1). This round asked whether 264b37cf answers that, and whether the records now say what the tree holds. Every command ran in a `git clone --shared` of the branch worktree under the round's scratch directory, with `HOME` and `SPECSEAL_ANSWERS` pointed into that directory, and the clone was removed before hand-back. The implementer's account, meaning the commit messages, `phases/phase-7.md` *Two left cases placed, after the sealer's fourth reading* and the overview rows, was read as claims. Each claim is named below with what the tree showed.

Facts carried from earlier rounds and not established again: what the move check's four conditions are and that `skills/verify/scripts/test_layout.py` implements them, as rounds 3 to 7 reviewed it; and that the cases `phases/phase-6.md` lines 589, 765 and 1603 keep in place stand where they are for the reasons those lines give, which rounds 2 to 6 read. This round did not re-judge either.

## Findings

### 1. The retirement-predicate case is kept in place on spec.md line 97, but each of its rows judges one file alone, so line 97 does not keep it

severity: should
location: `tests/test_unverified_rows_close.py:1-13`, `tests/test_unverified_rows_close.py:279-302`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:337`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:19-21`
evidence: read `tests/test_unverified_rows_close.py:279-302`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:57`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:97`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-5.md:902`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:589`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:337`
verdict: open

This matters because it leaves the same kind of gap the sealer's fourth reading withheld on, now with a reason written down that does not fit the case. `overview.md:5` and `changelog.md:3` say that a rebuilt module's tests stand in one file that declares it as `TARGET`. The sealer's condition for that sentence to hold was that every case standing outside its module's file is either moved or named in the records with grounds (`guarantee.md` line 60 at 95f139e1). The next agent to read the file is #923's, or the settle that closes S10. That agent reads the new docstring, takes the case for a check across files, and leaves it out of the modules phase 5 assigned it to.

The grounds. Phase 5 classified `test_every_reader_of_a_retirement_calls_the_one_predicate` as left for its module, for `skills/settle/scripts/settle.py` and `skills/code-review/scripts/chain_check.py` (`phases/phase-5.md:902`). Rule 2 keeps such a case in its old file "until the phase that rebuilds the module it pins" (`spec.md:57`). Groups 36 and 37 placed those two modules without it. The smith found this, and the account says why the case stays: "So it holds two modules to a third module's predicate, a check that compares files with each other, which `spec.md` *What the frame decided* keeps where it is (`spec.md` line 97). It stays" (`phases/phase-7.md:337`). The docstring at 264b37cf repeats this: "Two cases hold other modules to this one, and each is a check across files, which stays where it is" (`tests/test_unverified_rows_close.py:6-7`).

The code does not do what that ground says. The case is parametrized over `script`. Each row opens one file, `chain_check.py` or `settle.py`, parses it, asserts that it holds an attribute call named `settled`, and asserts that it defines no function named `settled` (`tests/test_unverified_rows_close.py:288-302`). No row opens `unverified_check.py`, and no row compares one file with another. Each row's verdict depends on its one file alone. `spec.md:97` keeps in place a check that "reads a document's prose, compares files with each other, derives a set across files, or judges records or markdown against an oracle". The sentence before it in the same item describes what this case does: a check that "judges one file by reading that file alone". That item sends such a check to `tests/censuses.py`, not to staying where it is. This case is not a census either, because a census is a rule every file of a kind keeps (`tests/censuses.py:1-2`), and this rule binds two named files. So line 97 keeps the case on neither branch, and rule 2 is the rule that governs it.

The fence-walk case, which the same docstring pairs with it, is a different shape. It runs `hooks/blocks.py`'s walks, `hooks/config.py#fence_map` and `unverified_check.py`'s walk on the same shapes and compares their answers (`phases/phase-6.md:589`). That is a comparison of files with each other, and that sentence holds.

The class, enumerated. In this diff, two places state the line 97 ground: the docstring at 264b37cf and `phases/phase-7.md:337` at fb455bee. The other cases that paragraph lists as kept in place cite records that earlier rounds read, and this round did not re-judge them. No `check:` line names the case (`executed`, `git grep` over the tree at fb455bee).

The fix has two paths, and the fix pass chooses one and says why. The first is the path rule 2 states. Move each row into `Test_module` of its module's file, `tests/test_chain_check.py` and `tests/test_settle.py`, as module-wide behaviour, the way 264b37cf placed the session-start case. One old case would then land in two new files, which the move check's second condition fails, so this path runs the proof for both modules. The second path keeps the case where it stands and records it the way `overview.md:20` and `:21` record the other cases that stand outside their module's file, with grounds that are true of the code. On that path the docstring and `phases/phase-7.md:337` stop citing line 97 for this case. Below is the text for the second path. The bracketed grounds are the fix pass's to state, because this round found no sentence in the frame that keeps the case.

```text
tests/test_unverified_rows_close.py, the docstring's last sentence, replacing "Two cases hold other modules to this one, ..." to the closing quotes:

`test_the_fence_walks_agree_shape_by_shape` holds `hooks/blocks.py` and
`hooks/config.py#fence_map` to this module's fence walk, a check across
files, which stays where it is. `test_every_reader_of_a_retirement_calls_the_one_predicate`
reads `skills/code-review/scripts/chain_check.py` and
`skills/settle/scripts/settle.py`, one file per row, for a call of
`settled` and no second definition of it; it stays here as `overview.md`
*Where spec and implementation diverged* records.

overview.md, a row after line 21:

| Where a case that reads two modules' source for a third module's predicate stands | `spec.md` rule 2: "the case stays in its old file ... until the phase that rebuilds the module it pins"; phase 5 left `test_every_reader_of_a_retirement_calls_the_one_predicate` for `settle.py` and `chain_check.py` (`phases/phase-5.md` line 902) | it stays in `tests/test_unverified_rows_close.py` as one parametrized case over both modules; groups 36 and 37 placed the two modules without it | [the grounds: why one body over two modules stays whole rather than splitting into the two modules' files] (`phases/phase-7.md` *Two left cases placed, after the sealer's fourth reading*) |

phases/phase-7.md:337, the sentences from "Its two rows read" to "It stays.":

Its two rows each read one file, `chain_check.py`'s source or `settle.py`'s, for a call of `settled` and for no second definition of it. `spec.md` line 97 does not keep it, because each row judges one file alone, so rule 2 sent it to groups 36 and 37. It stays, as `overview.md` records with its grounds.
```

answer:

## Confirmations

confirms: none
The move check holds as recorded. Executed in the clone at 264b37cf: `bin/test-layout --moved 95f139e1 --from tests/test_question_gate.py tests/test_worktree_consent.py tests/test_the_root_migrates_itself.py tests/test_dispatch.py --to` the same four files. It ends `test-layout: moved: 116 old cases, 126 items against 126 at 95f139e1ace1, 0 failed` and exits 0. That is the line and exit `phases/phase-7.md:333` records. The detached worktree of the base that the check adds was gone from `git worktree list` after the run. The two moved cases pass where they now stand: 2 passed, executed with pytest on the two node ids.

confirms: none
Both cases belong in `Test_module`, as the smith placed them, and the smith's reason holds. The account claims that neither case calls a function that has a class. Executed: `bin/test-layout --check` over the four files exits 0 and reports `hooks/worktree_consent.py: function last_routing_answer has no class Test_last_routing_answer`. `git grep` at fb455bee finds `last_routing_answer` called in `tests/` only by the moved case at `tests/test_worktree_consent.py:806`. A `Test_last_routing_answer` would therefore hold one refusing case and no accepting one, and `--check` refuses a function class without both (`spec.md` rule 1). The session-start case reads `GROUPS`, a constant of the module (`hooks/dispatch.py:80` and `:114-118`, read), which is behaviour of the module as a whole and is what rule 1 puts in `Test_module`. The tree already handles a function's single case this way: 099cd54d placed three single-case functions in `tests/test_conftest.py::Test_module` for the same reason (`phases/phase-7.md:70`, read), and `tests/test_dispatch.py::Test_module` already held `test_a_message_is_its_first_line_and_capped` for `first_line` and `capped`. Each moved case was also read against its new class. `test_the_installer_runs_before_the_gates_it_serves` pins `hook-install.py` last in `session-start` (`tests/test_dispatch.py:1159-1164`), and nothing in `Test_module` pins that `root-migrate.py` is in the group, so the verdict is place and not merge. `--pairs` over both receiving files names 0 pairs (executed).

confirms: none
`tests/test_worktree_consent.py` imports `SESSION`, `payload` and `write_the_transcript` from `tests/test_question_gate.py` (`tests/test_worktree_consent.py:41`). That import is not a twin. `--check` refuses a top-level function whose source is byte-identical to one in another test file, and an import defines nothing. Executed: `--check` over the four files exits 0 with 0 refused, and `--check` over the whole of `tests/` at 264b37cf exits 0 with `184 files read, 0 refused, 115 declare no TARGET`. Importing a helper from another test file is a reading the frame states and the move check follows (`spec.md` *The proof of equal protection*, fourth condition). `git grep` finds 33 such imports under `tests/` at fb455bee, this one among them, so it adds no new pattern.

confirms: none
The `.test_durations` rename holds. Executed, `json.load` of the file at 95f139e1 and at 264b37cf: 7,726 ids each time. Each of the two ids appears once, under its old file at 95f139e1 and under its new file at 264b37cf, with the seconds unchanged, 0.08136589999998023 and 0.004409500000008393 (read in the diff). Each new id sorts beside the other ids of its class.

confirms: none
The record rewrites hold against the tree. `phases/phase-6.md:1004` says both cases still stood in another module's file at da3eae09. Executed: `git grep` at da3eae09 finds them in `tests/test_question_gate.py` and `tests/test_the_root_migrates_itself.py`. The coordinates `phases/phase-7.md:327` cites were all read: `phases/phase-6.md:121` (group 1 leaves the press reader's case), `:362` (group 11 places `hooks/worktree_consent.py` without it), `phases/phase-5.md:671` (phase 5 leaves the session-start case) and `phases/phase-6.md:249` (group 7 places `hooks/dispatch.py` without it). Each says what the record says. `overview.md:19` names the same four facts and 264b37cf. At 6046f062, the session-start case already stood in `tests/test_the_root_migrates_itself.py`, a file the work did not remove. So that clause of the row describes the normal path of rule 2 rather than the row's subject, a removed old file. The clause is still true. The claim that `tests/test_the_root_migrates_itself.py` lost its only reader of `load_hook_module` holds (executed, `git grep -c` at 264b37cf: 0). No `check:` line names either case's old node id (executed, `git grep` at fb455bee). `bin/rules --check` exits 0: all 249 check lines in 62 rule files hold (executed).

confirms: none
The class of left cases was enumerated again, apart from the smith's scripts, and agrees with the account except for finding 1. Executed: a probe read every backticked case name on the lines of phases 5 to 7 that leave a case in place, and found which file defines it at fb455bee and that file's `TARGET`. For each of the 112 names that no file defines, a second probe found the commit that removed the name and searched the tree for a case with an equal body. Each case found under its name, apart from the prose and cross-file cases the records keep, stands in its module's file. Every body found under a new name stands in its module's file too: `hooks/worktree_consent.py`, `chain_check.py`, `hooks/cmdline.py`, `hooks/config.py`, `hooks/hooksession.py`, the commit flow, or `evals/scripts/replay_targets.py`. None stands in another module's file. The names with no equal body anywhere were rewritten or cut under rule 3, as the phase records say.

confirms: none
`overview.md:5` and `changelog.md:3`, as 46dec486 rewrote them, hold against the tree at fb455bee, apart from finding 1's case. Executed, a probe over `git ls-tree` at fb455bee: 184 test files, 69 declaring a `TARGET` and 115 none; 73 shipped Python modules, 68 named by a `TARGET` and seven named by none. The seven are `evals/scripts/behaviour.py`, `hooks/cmdline_base.py`, `hooks/git/post-commit.py`, `hooks/git/reference-transaction.py`, `hooks/githooks.py`, `hooks/hook-install.py` and `hooks/implementer.py`. 264b37cf added and removed no test file, so the counts did not move. The two cases the sealer named now stand in their modules' files. The other cases it named stand outside their module's file as `overview.md:20` and `:21` record. The sentence is therefore as true as the records make it, and finding 1 names the one case they do not yet answer for.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at fb455bee, unverified. The broad gate's record names 7891de9e, and 264b37cf changed tests after it. This round declined none of the three, because the prompt ordered none | the whole tree | the orchestrator, at the broad gate after this round's finding is answered |
| CI run 40018644093 at fb455bee, unverified, not read | the run | the orchestrator |
| `ruff check` and `ruff format --check` over the five Python files 264b37cf changed, unverified, not run this round | `tests/test_dispatch.py`, `tests/test_question_gate.py`, `tests/test_the_root_migrates_itself.py`, `tests/test_unverified_rows_close.py`, `tests/test_worktree_consent.py` | the orchestrator, at the broad gate |
| Whether each rewritten case that the second probe found no equal body for is accounted for in its phase record, one by one. This round traced bodies, not record sentences | `phases/phase-5.md`, `phases/phase-6.md` | the sealer, where its next reading weighs the class |
| The sealer's readings in `guarantee.md`, read for their coordinates and not judged, since the file is the sealer's own | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/guarantee.md` | the sealer |
| Round 6's other rows of `## Not judged`, carried as round 7 carried them. This diff answers none of them | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/rounds/round-6.md` | as round 6 names them |

## Probes

| Command | Result |
|---|---|
| `git clone --shared --no-checkout` of the branch worktree into the round's scratch directory, then `git checkout --detach 264b37cf` | clone at 264b37cf; 95f139e1 present; removed before hand-back |
| `bin/test-layout --moved 95f139e1 --from <the four files> --to <the four files>`, with the worktree's `.venv` first on `PATH` and `HOME`, `SPECSEAL_ANSWERS` and `TMPDIR` in the scratch directory | exit 0; `test-layout: moved: 116 old cases, 126 items against 126 at 95f139e1ace1, 0 failed`; `git worktree list` afterwards shows the clone alone |
| `bin/test-layout --check` over the four files; `bin/test-layout --pairs tests/test_worktree_consent.py tests/test_dispatch.py`; `bin/test-layout --check` over `tests/` | exit 0, 4 read, 0 refused; exit 0, 0 pairs; exit 0, 184 read, 0 refused, 115 declare no TARGET |
| `python -m pytest -q -p no:xdist -p no:cacheprovider` on the two moved node ids, at 264b37cf | 2 passed, exit 0 |
| `bin/rules --check` at 264b37cf | exit 0, all 249 check lines in 62 rule files hold |
| `json.load` of `.test_durations` at 95f139e1 and 264b37cf, counting all ids and the two moved ids | 7726 and 2 at each; old files at 95f139e1, new files at 264b37cf |
| `git grep` at da3eae09 and 6046f062 for the two cases' definitions; `git grep -c load_hook_module` at 264b37cf over `tests/test_the_root_migrates_itself.py`; `git grep` at fb455bee for `last_routing_answer`, for `from test_` imports under `tests/`, for the retirement case's name and for both moved cases' names | as stated in the confirmations and finding 1 |
| Probe script one, over phases 5 to 7 at fb455bee: each backticked case name on a line that leaves a case in place, the file defining it and that file's `TARGET` | 243 names; the cases found under their names stand in their modules' files, apart from the prose and cross-file cases the records keep |
| Probe script two, over the 112 names no file defines: the commit that removed each name, and a case at fb455bee with an equal body, docstring dropped | every equal body found stands in its module's file; the rest have no equal body |
| Probe script three, over `git ls-tree` at fb455bee: test files declaring a `TARGET`, and shipped modules named by none | 184, 69, 115; 73 shipped, 68 named, seven unnamed |
| `chain_check.py --baseline release/v0.22.3 --root <branch worktree> --worktree`, after this record, with the branch's copy and the installed plugin's copy | each exit 0, no pull request found; four lines each: this record's finding 1 reading `open`, the broad-gate record and the guarantee behind HEAD since 264b37cf, and the guarantee's `withheld` verdict |
