# 1792628098-tests-rebuilt-one-file-per-module — review round 10

target: 86661b67, fixes faa7f091..86661b67

This round reviewed the two commits after round 9's record. 18349051 moves 18 cases out of the files `overview.md` counted among the checks across files, removes `tests/test_a_script_copied_alone_exits_2.py`, puts `names_path`, `LS` and `FF` in `tests/conftest.py`, and renames the `.test_durations` ids. 86661b67 writes `phases/phase-7.md` *The class enumerated, in round 9's fix pass*, rewrites `overview.md` lines 12, 29, 51 and 55 and `changelog.md` line 3, and answers round 9's finding 1. The round asked four things. Does 18349051 answer round 9's finding 1, and does the class table close its class? Does the move check print what the record says, and are the moved cases red on their modules' mutants? Do sampled rows of the table hold against the test the record states and `spec.md` line 97? And is holding the liveness file's 40 cells consistent with how the frame treats Q10's installer file? Every command ran in a `git clone --shared` of the branch worktree under the round's scratch directory, first at 18349051 and then at 86661b67. `HOME`, `SPECSEAL_ANSWERS` and `TMPDIR` pointed into that directory, and the worktree's `.venv` stood first on `PATH`. The clone was removed before hand-back. The implementer's account was read as claims: the two commit messages, the new section of `phases/phase-7.md`, the rewritten lines of `overview.md` and the `answer:` line of round 9's finding 1. Each claim is named below with what the tree showed.

Facts carried from earlier rounds and not established again: what the move check's four conditions are and that `skills/verify/scripts/test_layout.py` implements them, as rounds 3 to 9 reviewed it; and that the cases `phases/phase-6.md` lines 589 and 1603 keep compare files with each other, which rounds 2 to 6 and round 8 read. Every verdict below was reached on the tree as it stands.

## Findings

### 1. The pinned case moved into tests/test_settle.py and tests/test_routing.py with no judgment of agents/warden.md line 99, the check line that names the file it left

severity: should
location: `agents/warden.md:99`, `tests/test_settle.py:1288-1296`, `tests/test_routing.py:568-575`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:500`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:505`
evidence: executed `grep -n warden.md seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md`, `git grep -n test_a_reference_root_is_read_and_never_taken 86661b67 -- docs agents skills templates CONTRIBUTING.md CLAUDE.md .github`, `pytest tests/test_settle.py::Test_module::test_the_pinned_checks_read_under_the_root_alone with settle.py's SPECS set to "specs"`
verdict: fixed fff64113
regression: round-9#1

The unit is `Test_module::test_the_pinned_checks_read_under_the_root_alone`, which 18349051 made twice, at `tests/test_settle.py:1288` and `tests/test_routing.py:568`, by splitting the one case of `tests/test_a_reference_root_is_read_and_never_taken.py`. The frame lets a case move only once every `check:` line naming a rule the case holds has its item, and a line outside `docs/` is rewritten by the commit that moves the case (`plan.md:106`, `questions.md:26`, `questions.md:29`); 18349051 moved this case, left `agents/warden.md:99` as it was, and its record does not say why, so the defect came from the fix pass applying that condition to the `docs/` lines that held the liveness cells and not to the one line outside `docs/` that names a file the pass drew from.

This matters because round 9 named this exact line as the open part of the case's placement. Its `## Not judged` row says `agents/warden.md:99`'s `check:` line names the file, "so whether it is part of a set across files is the frame's to say" (`rounds/round-9.md:97`). The fix pass answered the placement and not the line.

The grounds. `agents/warden.md:99` reads `check: tests/test_a_reference_root_is_read_and_never_taken.py tests/test_config.py`, under a rule that ends "The plugin never writes there". The `git grep` above finds it the one `check:` line, in any root `rules.py` reads, that names a file this pass drew cases from (executed). `questions.md:26` says a case holds a rule "where breaking what the rule states turns it red", and that a line names the rule 1 file each moving case of its rule lands in. The settle half meets that test. With `SPECS` widened to `specs`, `settle.py#work_items` lists a team's `specs/` directories (`skills/settle/scripts/settle.py:119-125`), and the retire step removes a listed directory with `shutil.rmtree` (`skills/settle/scripts/settle.py:596`): the plugin writing in a reference root. This round set `SPECS` to `"specs"` in the clone and ran the moved case alone: it failed on `assert 'specs' == 'seal/specs'` (executed). The frame read the same line this way once already: `spec.md:109` adds `tests/test_config.py` to it because the resolver's cases moved there. The new section of `phases/phase-7.md` gives the split a row (line 500) and a sentence (line 505) and names no `check:` line for it; the `grep` for `warden.md` over the section and `overview.md` finds no line (executed). This round did not read whether `hooks/routing.py` writes anything under `WORK_ITEMS`, so whether the routing half holds the rule is a row of `## Not judged`.

The fix, on the path `questions.md:29` states for a line outside `docs/`:

```text
agents/warden.md:99, rewritten in place in the fix pass's own commit:
check: tests/test_a_reference_root_is_read_and_never_taken.py tests/test_config.py tests/test_settle.py
(tests/test_routing.py added too if hooks/routing.py writes under WORK_ITEMS,
which the fix pass reads and states.)

seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md,
section "The class enumerated, in round 9's fix pass", after the sentence on
the pinned case's two assertions (line 505):
  The split case holds the rule of agents/warden.md:99 in its settle half:
  with SPECS widened, settle lists and removes a team's specs/ directories.
  The line now names tests/test_settle.py beside its two files.

seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md,
"Where spec and implementation diverged", one row: spec.md:109 states what
agents/warden.md:99 names once hooks/config.py's group moved, and round 9's
fix pass added the settle half's landing; the framer restates the row.
```

If the fix pass finds that neither half holds the rule, the other path is one sentence at `phases/phase-7.md:505` saying why, and the line stays.

answer: The finding holds for the settle half, and the routing half holds no rule of the line. fff64113 rewrites `agents/warden.md:99` in place to `check: tests/test_a_reference_root_is_read_and_never_taken.py tests/test_config.py tests/test_settle.py tests/test_chain_check.py tests/test_unverified_check.py`, which adds finding 2's three landings in the same commit. The routing half stays off the line because `hooks/routing.py` writes nothing, and every module that reads `routing.WORK_ITEMS` only lists, matches or names paths under it: `chain_check.py`, `hooks/commitgate.py`, `hooks/gate.py` and `hooks/commit-review-gate.py` (read). 7d0b36b3 writes both halves' grounds into the sentence on the pinned case in `phases/phase-7.md` *The class enumerated, in round 9's fix pass*. It also adds the row on what `agents/warden.md:99` names against `spec.md:109` to `overview.md` *Where spec and implementation diverged*, for the framer to restate. `bin/rules --check` exits 0 at fff64113, with all 249 check lines in 62 rule files holding (executed).

### 2. test_a_planted_team_specs_changes_no_checks_verdict stays on a ground spec.md line 97 does not give: its loop runs each of three hand-written checks alone

severity: should
location: `tests/test_a_reference_root_is_read_and_never_taken.py:76-174`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:382`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:501`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:55`, `agents/warden.md:99`, `tests/conftest.py`, `tests/test_chain_check.py`, `tests/test_unverified_check.py`, `tests/test_settle.py`
evidence: read `tests/test_a_reference_root_is_read_and_never_taken.py:126-174`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:97`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:129`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/questions.md:28`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:382`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:501`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:55`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/rounds/round-9.md:24`
verdict: fixed fff64113
reopens: round-9#1

Why the close does not hold. Round 9's finding 1 was closed `fixed 18349051` with its class enumerated by one test, and the answer says the test closed the class. The test as the record states it keeps a member of that class: a case whose subjects each run alone, one per pass of a loop over a list written by hand.

The test (`phases/phase-7.md:382`, restated at `overview.md:55`) keeps a case "where one of its assertions depends on more than one shipped module". `spec.md:97` keeps a check that "compares files with each other". These differ. A comparison sets one module's answer against another's. Dependence also covers a conjunction: one property asserted once after several modules each ran alone.

The case is that conjunction. `CHECKS` (`tests/test_a_reference_root_is_read_and_never_taken.py:126-136`) is a dict of three scripts written by hand: `chain_check.py`, `unverified_check.py` and `settle.py`. Each pass of the loop (lines 150-172) runs one script over the two repositories `planted` builds. It asserts that script's two outputs equal and that the joined output does not name the team's directory. Both assertions hold one module. The last assertion (lines 173-174) holds the team's three files unchanged after all three scripts ran. That is a property of each script, checked once after the loop. No assertion sets one script's answer against another's. Round 9 said of the copied-alone case, "Running several scripts, one per row, is not a comparison of files" (`rounds/round-9.md:24`). A loop over a hand-written dict is that shape, and the check after the loop is its conjunction. Split per script, each case checks the team's files after its own script ran. That holds what the old case held, and the failure names the script that wrote. The row at `phases/phase-7.md:501` keeps the case as "compares modules", which is the frame's ground in name only.

On the smith's reading of the first branch per assertion rather than per row. Where it splits a case, the reading follows the frame: `questions.md:28` lands a case by the module it calls as its subject, and the pinned case's two assertions had one subject each, so each half has a module file. Where it keeps a case, the branch has to be one `spec.md:97` gives, and "depends on more than one" is wider than "compares". The 116 rows give "compares modules" as the whole reason four times. Two set answers across modules against each other: `test_every_copy_of_the_splitter_is_the_readers` holds two copies of the splitter equal to the reader's, and `test_the_three_token_reads_answer_as_one` holds three readers to one answer. One, the S10 case of `tests/test_the_frozen_reading_never_grows.py`, stays on `spec.md:129`'s Q10 ground (see the confirmations). This case is the fourth.

The fix, on the path rule 2 states, in the shape 18349051 gave the copied-alone rows:

```text
1. tests/conftest.py: `planted(where, team)` and the three constants it reads,
   SERVICE, OURS and TEAM, defined once, with the bodies of
   tests/test_a_reference_root_is_read_and_never_taken.py:79-124 unchanged,
   because three test files will read them (spec.md rule 1).

2. Each script's file takes one case in Test_module: the body of one pass of
   the loop, followed by the check of the team's three files, with the
   script bound from TARGET and its arguments as CHECKS gives them:
   tests/test_chain_check.py       ["--baseline", "HEAD~1", "--root", "{r}"]
   tests/test_unverified_check.py  ["{r}"]
   tests/test_settle.py            ["--root", "{r}", "--released-at", "HEAD"]
   Each receiving file's docstring names the case and the file it came from.

3. agents/warden.md:99 names the three receiving files beside its two, in
   the same commit (questions.md:29), with finding 1's change.

4. The move check over the old file and the three receiving files, and
   decision-point mutants for each module its lines send, against the moved
   cases alone.

5. Records: phases/phase-7.md:382 and overview.md:55 state the first branch
   as spec.md:97 states it, "where one of its assertions compares one shipped
   module's answer with another's"; row 501 says where the case went.
```

If the fix pass finds a sentence of the frame that keeps a conjunction over modules each run alone, the other path is to keep the case, state that sentence in `overview.md` *Where spec and implementation diverged*, and rewrite `phases/phase-7.md:382` and `overview.md:55` to it. This round found no such sentence.

answer: The fix pass took the fenced fix and found no sentence of the frame that keeps the conjunction. fff64113 defines `planted`, `SERVICE`, `OURS` and `TEAM` once in `tests/conftest.py` with their bodies unchanged. `tests/test_unverified_check.py` imports `TEAM` and `OURS` from there in place of its own copies of the same values, which the fix did not name. Each script's pass is a case of `Test_module` in `tests/test_chain_check.py`, `tests/test_unverified_check.py` and `tests/test_settle.py`, followed by the check of the team's three files, with the script bound from `TARGET` and the arguments `CHECKS` gave it. `agents/warden.md:99` names the three files, and `.test_durations` gives each new id a third of the old id's seconds. Executed, the move check over the four files at 0775ccb8: `test-layout: moved: 336 old cases, 638 items against 636 at 0775ccb8db03, 5 failed`, exit 1, sending `chain_check.py`, `unverified_check.py` and `settle.py`. Sixteen decision-point mutants ran, one batch per module, against the moved cases alone with `-x` and the runner copied outside the tree. 8 are red there: u1 to u5, s1, s2, and c6 on the chain check's case. Of the 8 survivors, c1, c2, c5 and s3 are red on the group's other new files at fff64113. c3, c4, s4 and s5 survive the four old files whole at 0775ccb8 too, so they are old gaps: the planted repositories hold no team `routing.md`, no declaration, no citation and no `tests/` directory. No protection was lost, and no case was added. The class closes in 7d0b36b3. The test of `phases/phase-7.md` *The class enumerated, in round 9's fix pass* is now `spec.md:97`'s, worded in the record as it is at `overview.md:55`, and each row kept on the old first branch was judged again. The splitter, token and config-reader cases each set one module's answer against another's, and their rows say so. The S10 case meets none of line 97's branches and stays on `spec.md:129`'s Q10 ground, which its row now states, since the guard imports neither installer module. `test_the_walk_is_exact_somewhere` and `test_the_routing_reader_hides_something` each guard an oracle case, and their rows say so. The table now counts 19 moved, 1 held and 96 stay. The new section *The planted team's case split, in round 10's fix pass* records the pass.

### 3. overview.md line 55 holds the liveness cells until items for three docs lines, where the Not verified row and plan.md's condition ask for four

severity: should
location: `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:55`
evidence: read `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:29`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:55`, `docs/the-record-layout.md:138-141`, `docs/the-record-layout.md:150`, `docs/the-record-layout.md:170`, `docs/the-record-layout.md:177`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/plan.md:106`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/questions.md:26`
verdict: fixed 7d0b36b3

This matters because `overview.md:55` states when the held cells may move, and the next smith acts on it. It says the cells "stay until `spec.md` *Rule changes* carries items for `docs/the-record-layout.md` lines 150, 170 and 177". `plan.md:106` lets a case move only once every `check:` line naming a rule the case holds has its item. `docs/the-record-layout.md:141` names the liveness file, with `tests/test_routing_is_recorded.py`, for the rule the cells state reader by reader: "the four readers that ask it give three answers" (lines 138-140). By `questions.md:26`, a moving cell lands in a file line 141 must then name. So the condition is four items, as the *Not verified* row at `overview.md:29` says ("an item for each of the four lines"). A smith reading line 55 could move the cells once three items land and leave line 141 naming too little.

The rest of what this round was asked about the row holds, and is in the confirmations: the hold is consistent with Q10, the row names its answerer, and line 55 states what stands until the answer.

```text
seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:55, the
clause on the held cells, rewritten in place:
  they stay until `spec.md` *Rule changes* carries items for
  `docs/the-record-layout.md` lines 141, 150, 170 and 177: the last three
  name that file alone for the rules the cells hold, and line 141 names it
  with `tests/test_routing_is_recorded.py` (*Not verified*).
```

answer: 7d0b36b3 rewrites the clause in place. The held cells now stay until `spec.md` *Rule changes* carries items for `docs/the-record-layout.md` lines 141, 150, 170 and 177; the last three name the liveness file alone, and line 141 names it with `tests/test_routing_is_recorded.py`. That is the count the *Not verified* row and `plan.md:106` ask for. The same clause stood twice more in `phases/phase-7.md` *The class enumerated, in round 9's fix pass*: the paragraph on whether the frame holds and the held row. Both now name the four lines.

## Confirmations

confirms: none
The fixed commit answers the coordinates round 9's finding 1 named, and this is why the finding is reopened and not regressed. 18349051 removes `tests/test_a_script_copied_alone_exits_2.py`. It places each copied-alone row in the file of the module the row copies, with the script bound from `TARGET`, and `names_path` stands once in `tests/conftest.py` (read, the diff). `phases/phase-6.md` lines 765 and 1064 are left as written. `phases/phase-7.md:526` corrects them, on `plan.md:118`'s rule that a group's own record states what its check printed at its commit and is not rewritten (read). `overview.md:54` and `:55` drop the file, and the counts it changed read 114 in `overview.md:12`, `:51` and `changelog.md:3` (read). `bin/test-layout --check --all` at 86661b67 refuses 114 files and nothing else, and those 114 are exactly the files the four lists of `overview.md` lines 53 to 56 name: 19, 1, 13 and 81 (executed, a comparison of the two sets). The other path to a close of the class is open, which is finding 2.

confirms: none
The move check prints what the record says. Executed in the clone at 18349051: `bin/test-layout --moved faa7f091 --from` the removed file, the four other old files and the eleven receiving files `--to` the same less the removed file exits 1 and prints 36 lines. 15 say an old case is `not in the new files unchanged`: the pinned case, the two copied-alone cases and the twelve line-end cases. 20 say a new case `stands for no old case`. One says `name config: its definition differs from the base's` for the walker case. The last line is `test-layout: moved: 826 old cases, 1934 items against 1934 at faa7f09165b4, 36 failed`, word for word as `phases/phase-7.md:507` records it. `git worktree list` afterwards shows the clone alone.

confirms: none
The moved cases are red on their modules' mutants, as `phases/phase-7.md:509-522` records. All 27 new ids and the merge's surviving case pass unmutated at 18349051 (28 passed, executed). Six of the 50 mutants were written again in the clone with the `Edit` tool, each run against one moved case alone, and each restored with `git restore` before the next. In `hooks/worktree-guard.py#last_active_event_epoch`, `tail.split("\n")` became `tail.splitlines()`. The merge's surviving case, `Test_last_active_event_epoch::test_accepts_the_newest_active_event_past_a_line_separator`, is red: the reader returned the older user event, 1680 seconds off. `settle.py`'s `SPECS` became `"specs"`, and the split case in `tests/test_settle.py` is red. `settle.py#load`'s missing-sibling exit became 1, and the copied-alone row in `tests/test_settle.py` is red on the exit code. `hooks/routing.py`'s `WORK_ITEMS` became `optin.WORK_ITEMS`, and the split case in `tests/test_routing.py` is red. `hooks/routing.py`'s guard caught `KeyError` in place of `ImportError`, and the copied-alone row in `tests/test_routing.py` is red, the copy raising `ModuleNotFoundError` with no sentence. `gather_changelog.py#section_lines` split with `splitlines`, and `test_a_section_line_is_a_line_that_starts_one` is red, numbering the form-feed line as a section line. These are four of the ten modules and include the guard's merge and both halves of the split case. A mutation score licenses *tested*, not *safe*.

confirms: none
The class table covers the class it names. A script over the fifteen files at faa7f091 listed 116 cases, and the table's 116 rows name exactly those (executed). Its verdicts count as `phases/phase-7.md:384` says: 16 placed, 1 merged, 1 split, 1 held and 97 stays, which split 40, 22, 19, 7, 5 and 4 by reason (executed). Sixteen rows were read against the test and against `spec.md:97`, at their bodies at faa7f091. Placed: `test_fold_check_keeps_no_copy_of_its_own` reads two attributes of `fold_check.py`, one module. `test_the_framers_mark_is_the_last_line_a_renderer_shows` calls `chain_check.frame_foot` with the reader the command loads itself, one subject. `test_a_line_directly_above_the_header_is_refused` calls `hooks/config.py#unfenced` and `#gfm_table` and asks no oracle. Merged: the old case and the surviving one each put a raw U+2028 inside the newest active event and assert its time, so the survivor covers it (read against its group, `tests/test_worktree_guard.py:1791-1805`). Split: each of the pinned case's two assertions reads one module's constant, and the halves pass the move (finding 1 is about the line, not the split). Held: each of the 40 cells asks one adapter of `TABLE` for one shape (`tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:219-231`), so the cells are cases of three modules. Stays, oracle: `test_the_walk_is_exact_somewhere` asks no oracle itself. It asserts `blocks.walk` against `RENDERER`, the column `test_the_oracle_gives_the_frames_renderer_column` holds the oracle to, and it exists so that the oracle case above it is not empty. It stays as part of that oracle check, a branch the record's test sentence does not name but `spec.md:97` covers. Stays, no module: `staleness` and `unpriced` are defined in the shard file itself (lines 251 and 285). Stays, set across files: `test_no_scope_in_the_suite_lists_paths_from_git_without_a_guard` derives its scopes from every suite module git lists. Stays, workflow: `test_the_pytest_line_hands_the_split_to_pytest` reads `.github/workflows/test.yml`. Stays, prose: `test_the_recipe_names_the_artifact_and_the_checklist_has_no_box` reads `CONTRIBUTING.md` and `docs/release-checklist.md`. Stays, oracle and compares: `test_the_config_reader_never_leaves_both_readings` holds `hooks/config.py#unfenced` against its base reading and markdown-it's hidden lines. Stays, compares: `test_the_three_token_reads_answer_as_one` sets three readers' answers against each other, and `test_every_copy_of_the_splitter_is_the_readers` holds `unverified_check.py`'s and `arm_check.py`'s splitters equal to the reader's. The S10 case of `tests/test_the_frozen_reading_never_grows.py` stays too, on `spec.md:129`'s last sentence, which waits on Q10 with the installer. Its row's reason does not match the code: the reason says the guard's answer depends on `githooks.py` and `hook-install.py`, and `hooks/worktree-guard.py` imports neither (executed, `grep -n githooks hooks/worktree-guard.py hooks/hooksession.py`; the one hit is a docstring at `hooks/hooksession.py:36`). The verdict holds, so this is no finding. The sixteenth row, the planted-team case, is finding 2.

confirms: none
Holding the liveness cells is consistent with how the frame treats Q10's installer file. Both rest on the condition `plan.md:106` puts on every move: a case moves only once each `check:` line naming a rule it holds has its item. For the installer, `docs/the-commit-gate-inside-git.md:37` names its file, and no item can be written while the heading appears twice, so Q10 asks a person and defaults to wait (`questions.md:77`). For the cells, `docs/the-record-layout.md` lines 150, 170 and 177 name the liveness file alone. The smith cannot write `spec.md` *Rule changes*, so the cells wait on the framer. No heading blocks the framer here, so the row names the framer and not a person, which is right. The row's answerer is stated, the framer, with what the framer would write (`overview.md:29`). What stands until then is stated at `overview.md:55`: the cells stay where they are. So the pull request can carry the row open. Finding 3 is the one defect in it, the count of lines.

confirms: none
The `.test_durations` change holds. Executed, a script over `git show <rev>:.test_durations` at faa7f091 and 18349051: 7,726 ids at each, 27 gone and 27 added, and no kept id changed its seconds. Each moved id carries its old seconds. The merged case's id is gone with 0.0075 s. The split case's 0.0089 s is halved between its two ids. Every one of the 27 new ids is collected by `pytest --collect-only` over the eleven receiving files (executed).

confirms: none
The tree checks the record cites hold at 86661b67. Executed in the clone: `bin/test-layout --check` exits 0, `183 files read, 0 refused, 114 declare no TARGET`. `bin/test-layout --check --all` exits 1 with `114 refused`. `bin/rules --check` exits 0, `all 249 check lines in 62 rule files hold`. `uvx ruff check` and `uvx ruff format --check` over the sixteen changed Python files that still exist report no error, and 16 files formatted; the one error named is the removed file, which this round passed by mistake.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 86661b67, unverified. 18349051 changed tests after the broad gate's record. The prompt ordered none of the three, so none was declined | the whole tree | the orchestrator, at the broad gate after this round's findings are answered |
| CI run 40026132996 at 86661b67, unverified, not read | the run | the orchestrator |
| 44 of the 50 mutants of `phases/phase-7.md:511-522`, read and not re-run. This round re-ran six, in four modules | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md` | the sealer, where it samples the smith's claims |
| Whether `hooks/routing.py` writes anything under `WORK_ITEMS`, which decides whether finding 1's line also names `tests/test_routing.py` | `hooks/routing.py`, `agents/warden.md:99` | finding 1's fix pass |
| The 100 rows of the class table this round did not sample. Each row whose whole reason is "compares modules" was read; each other reason was sampled at least once | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:386-503` | the sealer, where it samples the smith's claims |
| Round 6's other rows of `## Not judged`, carried as rounds 7 to 9 carried them. This diff answers none of them | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/rounds/round-6.md` | as round 6 names them |

## Probes

| Command | Result |
|---|---|
| `git clone --shared --no-checkout` of the branch worktree into the round's scratch directory, then `git checkout --detach 18349051` | clone at 18349051, faa7f091 present; later moved with `git switch --detach 86661b67`; removed before hand-back |
| `bin/test-layout --moved faa7f091 --from` the five old files and the eleven receiving files `--to` the same less the removed file, at 18349051, from a script in the scratch directory, with the worktree's `.venv` first on `PATH` and `HOME`, `SPECSEAL_ANSWERS` and `TMPDIR` in the scratch directory | exit 1; 36 lines, 15 body, 20 landings, 1 name; `test-layout: moved: 826 old cases, 1934 items against 1934 at faa7f09165b4, 36 failed`; `git worktree list` afterwards shows the clone alone |
| `python -m pytest -q -p no:xdist -p no:cacheprovider` on the 27 new ids and the merge's surviving case, at 18349051 | 28 passed, exit 0 |
| Six mutants written with the `Edit` tool into the clone, in `hooks/worktree-guard.py`, `skills/settle/scripts/settle.py` (two), `hooks/routing.py` (two) and `.github/scripts/gather_changelog.py`, each run with pytest against one moved case alone | each 1 failed, exit 1, on the assertions named in the confirmations; every file restored with `git restore`, `git status --short` empty |
| A script over the fifteen judged files at faa7f091 against the table rows of `phases/phase-7.md`, and an `awk` count of the rows by verdict and reason | 116 cases and 116 rows, none missing on either side; 16 placed, 1 merged, 1 split, 1 held, 97 stays |
| A script printing the sampled cases' source at faa7f091 | as read in the confirmations and finding 2 |
| A script over `git show <rev>:.test_durations` at faa7f091 and 18349051; `pytest --collect-only -q` over the eleven receiving files at 18349051 | 7,726 ids at each; 27 gone, 27 added, 0 kept ids changed; all 27 new ids collected |
| `bin/test-layout --check`, `bin/test-layout --check --all` and `bin/rules --check` at 86661b67; the refused files set against `overview.md` lines 53 to 56 | exit 0, 183 read, 0 refused, 114 undeclared; exit 1, 114 refused; exit 0, 249 lines in 62 files hold; the two sets equal |
| `uvx ruff check` and `uvx ruff format --check` over the changed Python files of faa7f091..86661b67 | one error, E902 on the removed file passed by mistake; 16 files already formatted |
| `git grep` at 86661b67 for each old file's name under the policy and agent roots; `grep -n warden.md` over the new section and `overview.md`; `grep -n githooks` over the guard and `hooks/hooksession.py` | one `check:` line, `agents/warden.md:99`, names an old file of this pass, `tests/test_a_reference_root_is_read_and_never_taken.py`; no line of the section or the overview names `warden.md`; the guard has no `githooks` hit and `hooksession.py` one, in a docstring |
| `chain_check.py --baseline release/v0.22.3 --root <branch worktree> --worktree`, after this record, with the branch's copy and the installed plugin's copy | each exit 0, no pull request found; six lines each: this record's three findings reading `open`, the broad-gate record and the guarantee behind HEAD since 264b37cf, and the guarantee's `withheld` verdict |
