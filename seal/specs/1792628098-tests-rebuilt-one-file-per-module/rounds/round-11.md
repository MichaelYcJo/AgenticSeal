# 1792628098-tests-rebuilt-one-file-per-module — review round 11

target: 600cc01e, fixes 0775ccb8..600cc01e

This round reviewed the six commits after round 10's record. fff64113 splits the planted-team case into one case per check in `tests/test_chain_check.py`, `tests/test_unverified_check.py` and `tests/test_settle.py`, moves `planted`, `SERVICE`, `OURS` and `TEAM` to `tests/conftest.py`, and rewrites the `check:` line at `agents/warden.md:99`. 7d0b36b3 rewrites the class table's test in `phases/phase-7.md` to `spec.md` line 97's, judges the rows kept on the old first branch again, and rewrites `overview.md` line 55. 9ca0867e answers round 10's three findings. cfd345be sets the changelog's count of old gaps to 178. 8516257d is the framer's restatement of `spec.md` line 109, with no foot line. 600cc01e removes the `overview.md` divergence row that 8516257d answers. The round asked five things. Do round 10's three findings close? Does the move check at fff64113 print what the record says, and are the moved cases red on their modules' mutants at the head and at 0775ccb8? Do the re-judged rows hold against line 97's test as now stated? Is the change to line 109 an amendment and no reframe? And does anything else in the diff break a rule? While this round ran, the orchestrator reported that CI run 40031623825 at 9ca0867e failed two cases on three legs. That report is a claim. This round reproduced the failure in its clone, and it is finding 1.

Every command ran in a `git clone --shared` of the branch worktree under the round's scratch directory, at fff64113, 600cc01e and 0775ccb8. `HOME`, `SPECSEAL_ANSWERS` and `TMPDIR` pointed into that directory, and the worktree's `.venv` interpreter ran pytest. The clone was removed before hand-back. The implementer's account was read as claims: the six commit messages, the new section of `phases/phase-7.md`, the rewritten lines of `overview.md`, `spec.md` and `changelog.md`, and the three `answer:` lines of `rounds/round-10.md`. Each claim is named below with what the tree showed.

Some facts were carried from earlier rounds and not established again. Rounds 3 to 10 reviewed what the move check's four conditions are, and that `skills/verify/scripts/test_layout.py` implements them. The texts of the mutants c3, c6, u1 to u5, s1 and s2 were taken from the fix pass's scratch script and matched against the rows of `phases/phase-7.md` lines 554 to 569. This round applied each one itself, through `mutation-check`. Every verdict below was reached on the tree as it stands.

## Findings

### 1. The check line fff64113 wrote turns CI red: a document case reads tests/test_settle.py and tests/test_unverified_check.py as mentions of settle.py and unverified_check.py

severity: must
location: `agents/warden.md:99`, `tests/test_a_document_that_names_a_script_says_how_to_reach_it.py:124-126`, `tests/test_a_document_that_names_a_script_says_how_to_reach_it.py:166`
evidence: executed `python -m pytest -q -p no:xdist tests/test_a_document_that_names_a_script_says_how_to_reach_it.py at 600cc01e`, `a script over every .md under agents, skills and templates at 600cc01e, setting names' substring reading against a bounded one`, `python -m pytest -q -p no:xdist tests/test_a_document_that_names_a_script_says_how_to_reach_it.py with names bounded`
verdict: open
regression: round-10#1

The unit is the `check:` line at `agents/warden.md:99`. fff64113 rewrote it in place for round 10's finding 1, and in the same commit added the files of finding 2's three landings. The frame has the commit that moves a case rewrite a `check:` line outside `docs/` in place, so that it names each file that holds its rule (`questions.md:29`, `spec.md:109`). fff64113 did that, and the line says what the frame says. The defect came from how the fix was checked. Its boundary ran eight files (`phases/phase-7.md:579`), and none of them is the module that reads every shipped document for script names. That module's reader takes a script's filename where it stands inside a longer filename. So the frame is not wrong, and the round gets an ordinary fix pass. This unit is not round 10's finding 1's unit, which was the pinned case, so this is not a second regression on one unit.

Why it matters. A ready pull request needs CI green. The orchestrator read CI run 40031623825 at 9ca0867e and reported the same two cases failing on ubuntu, macOS split 1 and Windows split 1. The two cases are `test_a_document_naming_a_wrapped_script_says_how_to_reach_it[agents/warden.md::settle.py]` and `[agents/warden.md::unverified_check.py]` (read, the orchestrator's message). This round ran the module in the clone at 600cc01e: the same two cases failed and nothing else failed (executed). The first message is "agents/warden.md names settle.py and never says where it is ... Add the path `skills/settle/scripts/settle.py`", and the second offers `unverified-check` or the path.

The grounds. `names` (`tests/test_a_document_that_names_a_script_says_how_to_reach_it.py:124-126`) returns `os.path.basename(script) in text`. `settle.py` is a substring of `tests/test_settle.py`, and `unverified_check.py` of `tests/test_unverified_check.py`. So line 99 puts `agents/warden.md` into `named_pairs` for two scripts. The document never mentions either script, and `reachable` then finds no locator. Before fff64113 the line named `tests/test_config.py`, and `hooks/config.py` is not under `skills/*/scripts/`, so the reader never met it.

The class, enumerated. A script over every `.md` under `agents/`, `skills/` and `templates/` at 600cc01e listed each document that the substring reading counts as naming a script while a reading bounded by `(?<![\w-])` does not (executed). It found five pairs:

- `agents/warden.md` with `settle.py` and `unverified_check.py`: the two red cases.
- `agents/smith.md` with `mutation_check.py`: from its `check:` lines at 109 and 123, which name `tests/test_mutation_check.py`. This pair passes only because the document carries the command `mutation-check` elsewhere.
- `skills/code-review/SKILL.md` with `chain_check.py`, and `skills/writing-style/SKILL.md` with `rule_changes.py`: both scripts are unwrapped, so these pairs reach the command-form case, which they pass.

`command_forms` (line 166) has the same missing bound. A line like `tests/test_chain_check.py -q` would read as `chain_check.py` being invoked. The same script found no such line today (executed).

Which repair. The reader, not the line. Spec rule 1 names a module's test file `tests/test_<module>.py`, so the test file of every rebuilt script contains that script's filename. A `check:` line can name its files only by path. Every shipped document whose `check:` line names a rebuilt script's test file meets this reader. Writing a locator for `settle.py` and `unverified_check.py` into `agents/warden.md` would satisfy a wrong reading with a sentence the document has no use for. Contract rule 18 forbids that. With `names` bounded in the clone, the module passed whole, with this round's own case among the passed: 34 passed, 8 skipped (executed). The file was then restored. The smith fixes it in this round's fix pass. The file is one `overview.md:56` leaves to #923, but the defect arose on this branch.

```python
# tests/test_a_document_that_names_a_script_says_how_to_reach_it.py

def names(text, script):
    """Whether `text` mentions the script by filename at all. A filename
    standing inside a longer one is another file's name: `tests/test_settle.py`
    on a `check:` line is not a mention of `settle.py`."""
    base = re.escape(os.path.basename(script))
    return re.search(rf"(?<![\w-]){base}", text) is not None


# in command_forms, the same bound:
    pattern = re.compile(rf"(?<![\w-]){re.escape(os.path.basename(script))}\s+-")


def test_a_test_file_named_for_a_script_does_not_name_it():
    """A `check:` line names test files, and rule 1 names each module's file
    for its module, so `tests/test_round_record.py` holds the script's
    filename without mentioning the script. Read as a mention, it asked
    `agents/warden.md` for locators of two scripts it never names."""
    script = "skills/x/scripts/round_record.py"
    assert not names("check: tests/test_round_record.py", script)
    assert names("`round_record.py` writes the record.", script)
    assert names("It lives at `skills/x/scripts/round_record.py`.", script)
    assert not command_forms("bin/test tests/test_round_record.py -q\n", script)
```

The case is seen red against the reader as it stands: its first assertion fails on the substring reading. No OS boundary is touched.

answer:

### 2. The three cases fff64113 placed cover nothing their files do not already cover: every mutant red on each is red on the rest of its file

severity: should
location: `tests/test_chain_check.py:3116-3154`, `tests/test_unverified_check.py:2398-2436`, `tests/test_settle.py:1312-1350`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:538`
evidence: executed `mutation-check skills/code-review/scripts/chain_check.py with c6 --tests "pytest -x tests/test_chain_check.py -k 'not test_a_planted_team_specs_changes_no_checks_verdict'"`, `mutation-check skills/verify/scripts/unverified_check.py with u1 to u5 --tests "pytest -x tests/test_unverified_check.py -k 'not test_a_planted_team_specs_changes_no_checks_verdict'"`, `mutation-check skills/settle/scripts/settle.py with s1 and s2 --tests "pytest -x tests/test_settle.py -k 'not test_a_planted_team_specs_changes_no_checks_verdict'"`
verdict: open
regression: round-10#2

The unit is the three cases named `test_a_planted_team_specs_changes_no_checks_verdict` that fff64113 added to `Test_module` of the three receiving files. The frame gives every old case that exercises a target one verdict. That verdict is merge where a case of the class already covers it, and cut where the mutation table shows that another case kills every mutation it kills (`spec.md:48-56`). This round's rule reads each test the diff adds against its group. The fix took round 10's paste-ready fix, which placed each pass of the loop in `Test_module` and asked neither question. Neither did the fix pass's record (`phases/phase-7.md:538`): it says "No new case was written" and gives each case no rule 2 verdict. The defect came from a paste-ready fix taken from a review record, so the round gets an ordinary fix pass.

Why it matters. Each case builds two git repositories and runs a script twice, 1.6 s each by `.test_durations`, and its body stands three times nearly word for word. Each copy can be red only where another case of its file is red too. Round 9's fix pass asked rule 2's question of its moves and merged one, the line-separator case of `hooks/worktree-guard.py` (`phases/phase-7.md:384`), so the question was owed to these moves as well.

The grounds (executed). The mutants that the moved cases kill alone are c6, u1 to u5, s1 and s2 (`phases/phase-7.md:554-569`, re-run by this round for c6, u1 and s1). Each was run against its receiving file with the moved case deselected, and each is red there. The other mutants of the table are c1, c2, c5 and s3, which the moved cases do not kill and the group's other files do (read, not re-run), and c3, c4, s4 and s5, which nothing kills. So no mutant of the table is killed by a moved case alone. In `tests/test_unverified_check.py` the covering case can be named by reading. `Test_main::test_accepts_a_walk_from_the_root_leaving_a_team_specs_out` (line 2335) runs the command over a `seal/` root beside a team's unreadable `specs/` overview. It asserts exit 0, the own work item named and `team-thing` not named, which is the moved case's second assertion. Beyond that, the moved cases assert that the whole output equals a team-less repository's, and that the team's bytes are unchanged after the run. No mutant of the table tells those two assertions apart, and a mutation score licenses *tested*, not *safe*. So whether one of them is a property no case of its class holds is the fix pass's reading. This round did not name the covering cases in `tests/test_chain_check.py` and `tests/test_settle.py`, because `-x` stops at the first red case.

```text
For each of the three cases, in the commit that answers this finding:
1. Read the receiving file's cases of the function the case runs (the
   command's main) for one that covers it, as spec.md rule 2's merge row
   asks.
2. Where one covers it: merge, folding in any assertion the survivor lacks
   (the whole-output equality against a team-less repository, or the team's
   bytes unchanged, where the fix pass finds no case holding it), and record
   the surviving case. Where none covers it: keep it, and record which
   assertion no case of the class holds, as rule 2's pair sentence asks.
   A merge that leaves `tests/conftest.py#planted` read by one file moves it
   back into that file (rule 1).
3. agents/warden.md:99 keeps a file only while a case of it still holds the
   rule (questions.md:26), in the same commit.
4. phases/phase-7.md, section "The planted team's case split, in round 10's
   fix pass": one line per case with its rule 2 verdict and the surviving
   case; .test_durations follows any id that goes.
```

answer:

## Confirmations

confirms: round-10#1
The close holds for its defect. `agents/warden.md:99` names `tests/test_settle.py`, whose settle half of the pinned case holds the rule "The plugin never writes there". s1, `SPECS` widened to `specs`, is red on the receiving file with the planted case deselected (executed), and the pinned case asserts `settle.SPECS == "seal/specs"` (read). The routing half stays off the line on grounds the tree shows. A search of `hooks/routing.py` for writes, removals, renames and directory creation finds only comments and docstrings (read). The line's new names break a document case, and that is finding 1, a regression on the line and not a failure of this close.

confirms: round-10#2
The close holds for its defect. The loop is gone from `tests/test_a_reference_root_is_read_and_never_taken.py`, which keeps three cases, and each script's pass is one case in its module's file. `planted`, `SERVICE`, `OURS` and `TEAM` stand once in `tests/conftest.py`, and `tests/test_unverified_check.py` imports the two values it had copies of, which were the same values (read, the diff). The move check at fff64113 prints the five lines `phases/phase-7.md:540-546` records, word for word, and ends `test-layout: moved: 336 old cases, 638 items against 636 at 0775ccb8db03, 5 failed`, exit 1; `git worktree list` afterwards shows the clone alone (executed). At 600cc01e, c6, u1 and s1 are red and c3 survives against the moved case of each module alone. At 0775ccb8 the same four give the same verdicts against the old case alone, so c3 is an old gap, as the record says (executed). `.test_durations` holds 7,728 ids, three of them the new ids, each at 1.6398620 s, a third of the old 4.919586 s (executed). `ruff check` and `ruff format --check` pass each of the five changed Python files (executed). The class test and the rows are the next entry. Whether the three cases cover anything their files do not is finding 2, which is a question rule 2 asks of the placement and not of the split.

confirms: round-10#3
`overview.md:55` holds the liveness cells until `spec.md` *Rule changes* carries items for `docs/the-record-layout.md` lines 141, 150, 170 and 177. The same four lines stand in `phases/phase-7.md:380` and in the held row at line 496, and `overview.md:29` asks the framer for an item for each of the four (read).

confirms: none
The class table states line 97's test, and no row's ground departs from it. A count over the table's 116 rows gives 16 placed, 1 merged and 2 split, so 19 moved; 1 held; and 96 stay. The stays are 40 oracle, 22 no module, 19 set across files, 5 compare, 5 workflow, 4 prose and 1 Q10, as `phases/phase-7.md:384` says (executed). The six re-judged rows were read against their bodies at 600cc01e. `test_every_copy_of_the_splitter_is_the_readers` holds `coordinates.py#gfm_lines`'s and `arm_check.py#_lines`'s answers equal to the reader's on each text. `test_the_three_token_reads_answer_as_one` collects every command and token on which `tokens.given`, `has_marker` and `has_token` disagree. `test_the_config_reader_never_leaves_both_readings` sets `config.unfenced` against `config_base`, built from `unverified_check.py#fence_spans`, and against markdown-it's hidden lines. Each of these three compares modules' answers. `test_the_walk_is_exact_somewhere` and `test_the_routing_reader_hides_something` assert a reader against `RENDERER` on the shapes the oracle case reads, and so keep that case from passing empty. The S10 case's assertions read `install`, `githooks.decides` and the guard one at a time, and its row now says so. Two branches of the stated test are not line 97's words: a workflow under `.github/workflows/`, and a case that calls no shipped module. They come from elsewhere in the frame. The first is the line of `spec.md:169` that lands a workflow-reading case beside the cases reading the same workflow, together with *Out*'s #923. The second is rule 2, which gives a verdict only to a case that exercises a target (`spec.md:48`). Both exceptions are stated with their answerers. The 40 cells are held for the framer's four items (`overview.md:29`, `phases/phase-7.md:496`). The S10 case waits on Q10 under `spec.md:129`, and Q10's row names a person as its answerer, with the default `wait` (`questions.md:77`) (read).

confirms: none
The change to `spec.md:109` is an amendment and no reframe. The `Reframed` foot line belongs to one route: a regression whose fix built what the frame says is sent back to the framer for a redesign (`docs/the-review-record.md:507`, `agents/framer.md:178`). Round 10's regressions took fix passes, and the frame's rule did not move. The rule is that a line outside `docs/` names each file where a moving case of its rule lands, and that the moving commit rewrites it (`questions.md:26`, `questions.md:29`). The row states what that rule now gives, in place, as contract rule 19 asks. Its claims hold. The line names the five files the row lists (read). `tests/test_config.py`'s cases came at 1b3e6978, whose subject says so (executed, `git show --stat`). The settle half and the three landings are red on s1, c6 and u1 (executed, above). `hooks/routing.py` writes nothing (read, above). The old file keeps `test_every_shipped_command_is_classified` and `test_each_reader_says_when_it_reads_a_reference_root_and_where_it_cites_it`, beside a third case the row does not name and need not (read). No other statement of the old two-file line stands outside group records. `phases/phase-6.md:773` is group 22's record of what it wrote then (executed, `git grep`). 600cc01e drops the divergence row 7d0b36b3 added, so `overview.md` carries no row the amendment answers (read, the diff).

confirms: none
The changelog's 178 is 174 and the four old gaps of round 10's fix pass. The last comment on #1017 lists c3, c4, s4 and s5 with their record lines at 9ca0867e (executed, `gh issue view 1017`).

confirms: none
The tree checks hold at 600cc01e: `test-layout --check` exits 0, 183 files read, 0 refused, 114 declaring no `TARGET`; `rules --check` exits 0, all 249 check lines in 62 rule files holding; `unverified-check seal/specs/` exits 0 (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 600cc01e, unverified. The prompt ordered none of the three, so none was declined. What comes due after this round's two findings are answered is a verifying round, then the orchestrator's broad run and the sealer's spawn | the whole tree | the orchestrator, at the broad gate |
| CI run 40031623825 beyond the two cases the orchestrator reported: read from its message, not opened by this round | the run | the orchestrator |
| Which cases of `tests/test_chain_check.py` and `tests/test_settle.py` kill c6, s1 and s2 besides the moved ones; `-x` stopped each run at the first red case | `tests/test_chain_check.py`, `tests/test_settle.py` | finding 2's fix pass |
| c1, c2, c5 and s3 red on the group's other files, and c4, s4 and s5 surviving the old files, as `phases/phase-7.md:554-569` records: read, not re-run | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md` | the sealer, where it samples the smith's claims |
| The 110 rows of the class table this round did not read against their bodies | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:386-503` | the sealer, where it samples the smith's claims |
| Round 6's other rows of `## Not judged`, carried as rounds 7 to 10 carried them. This diff answers none of them | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/rounds/round-6.md` | as round 6 names them |

## Probes

| Command | Result |
|---|---|
| `git clone --shared --no-checkout` of the branch worktree into the round's scratch directory, then `git checkout --detach` at 600cc01e, fff64113 and 0775ccb8 in turn | the clone alone in `git worktree list`; removed before hand-back |
| `pytest -q -p no:xdist` over `tests/test_a_document_that_names_a_script_says_how_to_reach_it.py`, the three moved cases and `tests/test_a_reference_root_is_read_and_never_taken.py`, at 600cc01e | exit 1; 2 failed, the two `agents/warden.md` cases of finding 1; 43 passed, 7 skipped |
| `test_layout.py --moved 0775ccb8 --from` the four files `--to` the same four, at fff64113 | exit 1; the five lines of `phases/phase-7.md:540-546`; `test-layout: moved: 336 old cases, 638 items against 636 at 0775ccb8db03, 5 failed` |
| `mutation-check` with c6, c3, u1 and s1 one at a time, against the moved case of each module alone at 600cc01e and against the old case alone at 0775ccb8 | c6, u1, s1 red at both; c3 SURVIVED at both; `git status --short` empty after each revision |
| `mutation-check` with c6, with u1 to u5 and with s1 and s2, one batch per module, against each receiving file with the moved case deselected, at 600cc01e | all eight red; baselines passed; `git status --short` empty |
| A script over every `.md` under `agents/`, `skills/` and `templates/` at 600cc01e, setting `names`' substring reading against one bounded by `(?<![\w-])`, and `command_forms` likewise | five pairs differ, as finding 1 lists; no command-form line differs |
| `names` bounded in the clone with the `Edit` tool, with a `test_tmp_` case beside it, then the module run with pytest; the file restored with `git restore` | 34 passed, 8 skipped, exit 0; `git status --short` empty after the restore |
| `test-layout --check`, `rules --check`, `unverified-check seal/specs/`, `uvx ruff check` and `uvx ruff format --check` over the five changed Python files, and `json.load` of `.test_durations`, at 600cc01e | exit 0, 183 read, 0 refused, 114 undeclared; exit 0, 249 lines in 62 files hold; exit 0; every ruff run exit 0; 7,728 ids, 3 of the case's name |
| `gh issue view 1017`; `git show --stat 1b3e6978`; `git grep` at 600cc01e for the old two-file line and for `agents/warden.md` line 99 | the last comment lists c3, c4, s4 and s5; 1b3e6978 moves `hooks/config.py`'s reference root cases into `tests/test_config.py`; the old line stands only in `phases/phase-6.md:773`, a group record |
| `chain_check.py --baseline release/v0.22.3 --root <branch worktree> --worktree`, after this record, with the branch's copy and the installed plugin's copy | each exit 0, no pull request found; five lines: this record's two findings reading `open`, the broad-gate record and the guarantee behind HEAD since 264b37cf, and the guarantee's `withheld` verdict |
