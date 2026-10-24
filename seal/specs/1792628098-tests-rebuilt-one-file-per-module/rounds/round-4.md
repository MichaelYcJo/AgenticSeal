# 1792628098-tests-rebuilt-one-file-per-module — review round 4

target: fc4f81ae, fixes 76551ca7..fc4f81ae

This round verified round 3's fix pass, 79f9c3fd to fc4f81ae. It checked round 3's two closes against the tree. It reviewed S15's name condition in `skills/verify/scripts/test_layout.py#moved` with its rows in `tests/test_test_layout.py`, the three false-refusal fixes at 79af3fcc, the pact ids and the `.test_durations` rename at 208803e6, the a17 case at 56d2f856, the conftest helper move at 4e987021, and the records at 724b3831 and fc4f81ae. Every run was in a `git clone --shared` of the branch worktree at fc4f81ae, in `scratchpad/942-r4/clone`, or in a second clone moved to the commits the records name. Both clones were removed after the round. Facts carried from round 3 and not established again: the 52 recorded move checks reproducing under their own commits' scripts (this round re-ran 8 of them), phase 6's recorded mutant tables, and the shipped scripts' AST equality up to 425d052a. The fix range changes no shipped file but `skills/verify/scripts/test_layout.py`. The implementer's account was read as claims, and each claim this round checked is named below with what the tree showed.

The two findings share one cause. The name condition now refuses moves the three-condition check passed, which is what round 3's finding 1 asked for. Finding 1 is about the cases it refuses that the fix pass's rule then sends to no proof. Finding 2 is about the condition's own statements, which say less than the code does and miss one way a changed definition passes.

## Findings

### 1. Twenty-five cases the name condition refuses stand in files with no TARGET, so four groups exit 1 and nothing proves them

severity: should
location: `seal/specs/1792628098-tests-rebuilt-one-file-per-module/plan.md:94`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/questions.md:46`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:35`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:1693`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:160`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:168`
evidence: executed `python3 moves.py`, `git show 7cd34d46:tests/test_a_unit_is_bounded_where_a_parser_decides.py`, `git show 31aed13b:tests/test_coordinates.py`, `git show f7ef43cc:tests/test_the_suite_has_a_command_that_is_cheap_twice.py`, `git show a4a113f6:tests/test_run_tests.py`, `git show 56d2f856:tests/test_a_shrunken_corpus_declines_to_judge.py`
verdict: fixed f9031b38
regression: round-3#1

The unit is `plan.md` *Round 3's fix pass* step 3, the rule for which modules a re-run that now fails sends to the mutants, as the re-run records at 724b3831 apply it. `spec.md:78` ends "A group whose check exits 1 runs the mutants for each of its modules". Step 3 narrows that, for a re-run whose lines are all on the name condition, to "those whose new file, by its `TARGET`, holds a case a line names". The fix followed step 3 as written. The defect comes from step 3 itself: it keys on a `TARGET` that the file holding a named case need not declare.

The re-run's lines name 25 such cases. The new case standing for each one is in a file that declares no `TARGET`. Phase 6 has 17 of them (`phases/phase-6.md:1693`). Phase 7 has group 44's 2 and 099cd54d's 1 (`phases/phase-7.md:160`). The other 5 are the five sweep cases of `tests/test_a_shrunken_corpus_declines_to_judge.py` that 4e987021's move check names on `OPENS_NOTHING` (`phases/phase-7.md:168`). The overview's *Not verified* row counts 20 (`overview.md:35`) and leaves those five out. They are the same kind of case: a case that stayed in an undeclared file while the group changed a name it reads. The four helpers' mutants that 4e987021 ran do not reach them.

Groups 29, 41, 48 and 49 have no other line. Re-run with the script at fc4f81ae, each exits 1. For each of them the records send no module, and no mutant ran. Of the four, the spec's own rule would have sent `skills/verify/scripts/coordinates.py`, `.github/scripts/rules.py`, `publish_release_note.py` with `release_seal.py`, and `run_tests.py`. For these four groups, the proof of equal protection now rests on neither the check nor the mutants. `spec.md:76` gives the move check, not anybody's record, the decision on whether a group was only moved. The account does not hide the gap: `overview.md:35` asks the framer. Under `Automation`, though, an open question to the framer ships unless a round holds it, and that is why this is a finding and not a row of *Not judged*.

What the names are, read at the two trees. Most of the 25 are a name the file now imports from another test file. Group 29's `RUBY` was `"def render\n  1\nend\n"` in the old file at 7cd34d46. At 31aed13b it is `from test_coordinates import RUBY`, and `tests/test_coordinates.py:96` holds the same assignment. Group 49's `rt` was `_load_runner()` in the old file at f7ef43cc. At a4a113f6 it is `from test_run_tests import rt`, and `tests/test_run_tests.py:53` holds `rt = _load_runner()` again. The condition reads an import from a test file as the import, by design: the row `a-name-imported-from-another-test-file` pins that. So these cases fail because the condition does not follow such an import, not because a definition is known to have changed. The other lines name real changes: group 16's `a_git_whose_diff_fails` and group 22's `shape_text` changed as they moved into `tests/conftest.py`, and the `OPENS_NOTHING` key now names `tests/test_conftest.py`. This round judged none of them harmless. That judgment is the one the owner refused to a record.

The framer has two ways to close it. Each one leaves the move check, not a record, as the decider. The first applies the spec's rule to these lines and needs no change to the check. The second makes the check follow the import that most of these lines are about. The frame then re-runs the commands, and whatever still fails goes to the first.

```markdown
plan.md, Round 3's fix pass, step 3, after "where any line is on another
condition, every module of the group goes.":

A line naming a case whose new case stands in a file that declares no
`TARGET` sends the modules whose functions that case calls as its subject,
placed as `questions.md` places a moving case; where none is a shipped
module, as for a check across files, the line is listed in `overview.md`
*Not done* with the name it gives, and the framer rules on that list. For
groups 29, 41, 48 and 49 this sends `skills/verify/scripts/coordinates.py`,
`.github/scripts/rules.py`, `.github/scripts/publish_release_note.py` with
`.github/scripts/release_seal.py`, and `.github/scripts/run_tests.py`. For
the groups that already ran their mutants, the functions those cases reach
are among the decision points the module's mutants sit at.

overview.md, Not verified, the row on these cases:

| whether anything proves the 25 cases the name condition's re-run names in
files that declare no `TARGET`: 17 in phase 6's groups, 3 in phase 7's
re-run of group 44 and of 099cd54d, and 5 in 4e987021's move, the sweep
cases of `tests/test_a_shrunken_corpus_declines_to_judge.py` reading
`OPENS_NOTHING` (each phase's *The move checks re-run with the name
condition*, and `phases/phase-7.md` *The shrunken corpus file's helper
cases, at 4e987021*) | the framer |
```

The second way, for the framer to weigh against the first: the name condition follows `from <module> import <name>` into a test file directly under `tests/` too, in the same tree. pytest imports such a file by that name. The row `a-name-imported-from-another-test-file` then passes where `V` is defined alike in both test files and refuses where it is not.

answer: The framer took both ways at b120e598. 32cd06c7 makes the condition follow an import from another test file, with `a-name-imported-from-another-test-file` moved to the accepting case and `a-changed-name-in-another-test-file` refusing, both seen red at a1047bfe. f9031b38 holds the re-run of all 52 recorded commands with it and sends every line naming a case in a file that declares no `TARGET` to its case's subject. The re-run counts 34 such lines, not 25: 13 of the 25 now pass, 12 still fail, and 22 more stand in groups recorded at exit 1, which plan step 4 sends whatever the command was recorded at and the count of 25 left out. Groups 29, 41, 48 and 49 now exit 0. Each subject has a fresh table or names the earlier table it stands on; 19 fresh mutants ran, 12 red and 7 old gaps, and no protection was lost (`phases/phase-6.md` and `phases/phase-7.md`, each *The move checks re-run with a test file's import followed*). `overview.md`'s row is rewritten with these counts and closed.

### 2. The fourth condition's statements say less than the check does, and a swap of two definitions passes the check

severity: should
location: `skills/verify/scripts/test_layout.py:97-99`, `skills/verify/scripts/test_layout.py:801`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:78`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:60`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:67`, `CONTRIBUTING.md:295-299`
evidence: executed `python3 swap_probe.py clone`, `git grep -n "four conditions\|the other two" -- tests skills/verify agents CONTRIBUTING.md docs`, `grep -n "self.<name>\|<module>.<name>\|reaches and the other" spec.md`
verdict: fixed 32cd06c7
regression: round-3#1

The unit is the name condition as the fix pass built it and stated it: `_Names.forms` at 2f681b9c to 79af3fcc, the script's `names` entry, the `CONTRIBUTING.md` sentence and the fourth condition of `spec.md:78`. The frame says the condition's one limit is a name reached through a string ("and that is the condition's limit"). The fix built a check that also reads `<module>.<name>`, `self.<name>` and a name only one tree reaches, and that keeps one set of forms per name. The defect comes from how those statements describe the code, plus one escape that 79af3fcc's set of forms opens.

Why it matters: the move check is the whole proof for a group it passes. Its statements are what a later contributor, a sealer and the settle that folds this frame into `docs/` read to know what "exit 0" proves. Four parts:

- **A swap passes.** `forms` keys each definition by the name alone and keeps the sorted set of its distinct forms (`test_layout.py:801`). 79af3fcc did this so that one definition reached from two files counts once. The cost: two definitions of one name, in two places one case reaches, compare equal when they swap places between the trees. A probe calling `moved` directly passed it. In the old tree, the case's file defines `b = 1` and a helper that returns `b`, and the conftest defines `b = 2` and a fixture `fx` that returns `b`. In the new tree the two values are swapped. The run printed 0 lines. The control printed 0 lines, and changing only the file's `b` printed `name b`. The normal flow of a move does not produce this shape, so a limit sentence fits it better than a guard. As things stand, `spec.md:78` names the string as the condition's only limit.
- **The frame does not state three readings the code makes.** `spec.md:78` does not say that `<module>.<name>` is read in that module, or that `self.<name>` is read in the case's class. It also does not say that a name bound in both trees but reached in only one is a change, which the row `a-module-reached-another-way` pins. `git grep "self.<name>"` over `spec.md` finds nothing. Even so, `overview.md:60` opens the section holding these three (`overview.md:67`) with "Each clause below was written into the frame because the build had already done it". For these three, that is not true.
- **The docstring says "the other two" of four conditions.** `test_layout.py:99` says a case "is tested on this condition only where it passed the other two". The count is the group's, not a case's, so the reader has to work out which two are meant. `spec.md:78` names them: the second and the third.
- **`CONTRIBUTING.md` states the list a second time.** Its bullet (`CONTRIBUTING.md:295-299`) says "four conditions hold, which ... docstring states" and lists them. The list and the count then stand in two files with no case tying them together. "The four conditions" is also the verify skill's defined term for a claim (`skills/verify/SKILL.md:28-30`).

```markdown
spec.md, The proof of equal protection, the fourth condition: in place of
"A name a case reaches only through a string, such as `globals()["x"]`, is
not read, and that is the condition's limit.":

A name read as `<module>.<name>`, where `import <module>` binds a module
directly under `tests/` that is not a test file, is read where that module
defines it, and a name read as `self.<name>` is read where the case's class
binds it, outside a function or lambda that takes a `self` of its own. A
name one tree's reading reaches and the other's does not is a change. Each
name is compared as the set of its distinct definitions, wherever the
reading reaches them, so one definition reached from two files counts once.
The condition has two limits. A name a case reaches only through a string,
such as `globals()["x"]`, is not read. Two definitions of one name in two
places a case reaches, swapped between the trees, compare equal.
```

```python
# skills/verify/scripts/test_layout.py, module docstring, the `names` entry,
# its last sentences in place of lines 96 to 100:
           reading reaches and the other's does not; a name a case reaches
           only through a string, such as `globals()["x"]`, is not read,
           and two definitions of one name in two places a case reaches,
           swapped between the trees, compare equal, because each name is
           compared as the set of its forms. A case is tested on this
           condition only where it passed the body and fixture conditions,
           and its line names the first name, in alphabetical order, whose
           own definition differs
```

```markdown
CONTRIBUTING.md, The test layout, the move check bullet, in place of "It
passes where four conditions hold, which
`skills/verify/scripts/test_layout.py`'s docstring states: the count of
items, each case's body, the fixtures it requests, and the names it and
those fixtures read from the module around them.":

It passes where every condition `skills/verify/scripts/test_layout.py`'s
docstring states for `--moved` holds.
```

answer: The framer wrote the three readings and the two limits into `spec.md` at b120e598. 32cd06c7 rewrites the script's `names` entry: it states the `self.<name>` and `<module>.<name>` readings, that a name one tree's reading reaches and the other's does not is a change, that each name is compared as the set of its distinct definitions, and the two limits, the string and the swap. It says "for each failure of the conditions below" and "passed the body and fixture conditions". `CONTRIBUTING.md`'s bullet now points at the docstring for the conditions and lists none, and neither file says "four conditions". The swap gets no guard, as the plan's alternatives weigh it. `overview.md`'s *Fed back into the spec* bullet names the reframe and the two limits at f9031b38.

## Confirmations

confirms: round-3#1
The close holds for what the finding named: the move check now reads the module-level names a moved case and its fixtures read. Executed: with `skills/verify/scripts/test_layout.py` from 76551ca7 copied over the clone's, `bin/test tests/test_test_layout.py -q -p no:xdist -k Test_moved` gives 11 failed and 24 passed, and the 11 are exactly the name rows of the refusing case. As committed, the module passes among the 268 below. Executed: two of the 30 mutants rebuilt from `phases/phase-7.md` *S15*, n2 (a name one tree alone reaches passed) and o1 (`from <module> import` not followed), in one `bin/mutation-check` batch with `-x`: 2 red. Group 15's line on `reader` prints at f1d13be0, as the answer says. The new defects this round found in the units the fix made are findings 1 and 2.

confirms: round-3#2
The close holds. Read: `overview.md:5` and `handoff.md:12` name 6a54be98 as the tree the suite was timed at. `overview.md:62` says `--pairs` named 0 at 00674174 and 210 at 208803e6. Row 16 quotes `spec.md` rule 2 as the reframe wrote it and names the groups whose records give each pair's reason. Group 44's record carries its pair's sentence (`phases/phase-6.md:1429`). The answer's correction holds too: group 45's record at 425d052a, line 1471, already named the `tests/test_tracker_labels.py::Test_main` pair with its reason. Executed: `bin/test-layout --pairs tests/` at fc4f81ae ends `184 files read, 210 pairs`.

confirms: none
The recorded re-runs reproduce. Executed, in a second clone at each record's commit, first with that commit's own script and then with the script at fc4f81ae, which equals 8dd97a30's (`git diff --quiet 8dd97a30 fc4f81ae` on the file): groups 5, 15, 18, 27, 29, 41 and 49, and 4e987021's move. Each own-script last line matches the recorded one, and each fc4f81ae last line matches the re-run table: 15, 6, 1, 0, 1, 1 and 5 failed, and 5 for 4e987021, every line on the name condition. Each group's named cases and names are the ones `phases/phase-6.md:1693` and `phases/phase-7.md:160-168` give.

confirms: none
a17 is the lost protection the record says, and 56d2f856's case answers it. Executed, with `HOME` set to a directory in the scratch area, because under a17 the hooks write to the store under the home directory. At fc4f81ae, a17 (`root_dir` ignoring `SPECSEAL_ANSWERS`) is red against the group's four new files, on `Test_module::test_the_override_names_the_store_where_it_is_set`. With that case deselected, a17 survives the same four files. At 714f2df2, from an empty home directory, a17 is red on the old file's `test_a_payload_with_no_tool_use_id_is_keyed_by_its_command`. Read against its group: the new case's neighbour asserts the store under the home directory where the override is unset, so the two cases cover the two branches of `root_dir` and neither repeats the other.

confirms: none
Group 18's g3 is an old gap. Executed: `gate.lines` keeping a blank line survives `tests/test_gate.py` and `tests/test_chain_hooks_hardening.py` at fc4f81ae, and survives `tests/test_chain_hooks_hardening.py` at 67a86c57.

confirms: none
The pact ids, the durations rename and the conftest move hold. Read: 208803e6 changes the parametrize's `ids` alone and one `.test_durations` key with its seconds kept. 4e987021's re-run prints no body or fixture line for the eight moved cases. `spec.md` *Rule changes* carries the item for `docs/release-checklist.md` *3. Verify before committing*, naming `tests/test_conftest.py` beside the old file. Executed: `bin/test tests/test_one_word_one_meaning.py -q -k test_no_live_text_says_the_word_0_19_0_renamed`, 1 passed.

confirms: none
The changed modules and the tree checks pass at fc4f81ae. Executed: `bin/test tests/test_test_layout.py tests/test_answers.py tests/test_conftest.py tests/test_a_shrunken_corpus_declines_to_judge.py tests/test_pact_check.py tests/test_docs_line_wrap.py -q`, 268 passed. `bin/test-layout --check` exits 0 with `184 files read, 0 refused, 115 declare no TARGET`. `bin/rules --check` exits 0, with all 249 check lines holding. `bin/unverified-check seal/specs/` exits 0.

confirms: none
The S15 rows are each read against their group. Read: each new row of `Test_moved` exercises a reading no earlier row reaches. The five refusing rows the spec names, the seven for the build's readings and the mutants, and the four accepting rows each change one name and nothing else. The row `a-changed-fixture-reading-another-name` pins that a case whose fixture differs is reported on the fixture condition alone.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a re-run module's mutants may sit only at the functions the named cases reach, where `spec.md` puts them at every decision point of every public function. The same applies to reusing a table under Q11 by the named cases rather than every case the group moved. The grounds hold as reasoning: a function that only cases passing all four conditions reach cannot have lost a case that killed a mutant there. But the overview is the account, and the set "the named cases reach" is the smith's reading, recorded per module and not per case | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md`, the divergence row on where a re-run module's mutants sit | the framer |
| The other 43 of the 51 re-run commands, and the re-run tables' mutants other than a17 and g3. This round re-ran 8 commands and 2 survivors, and rebuilt 2 of S15's 30 mutants | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md` | the sealer |
| The directory `s1` that the fix pass's a17 runs left in the answers store under the home directory, which its hand-back names. This round saw it there and did not remove it | outside the repository | the orchestrator |
| The CI run at fc4f81ae, in flight when this round ended, unverified | `.github/workflows/test.yml` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at fc4f81ae, unverified. Nothing is due from this round until findings 1 and 2 are answered | the whole tree | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `git clone --shared` of the branch worktree into `scratchpad/942-r4/clone` at fc4f81ae, and a second, `clone2`, moved between commits; both removed after the round | every run below ran in one of the two |
| `bin/test tests/test_test_layout.py tests/test_answers.py tests/test_conftest.py tests/test_a_shrunken_corpus_declines_to_judge.py tests/test_pact_check.py tests/test_docs_line_wrap.py -q` | 268 passed |
| `bin/test-layout --check`, `bin/rules --check`, `bin/unverified-check seal/specs/`, `bin/test-layout --pairs tests/` | exit 0, 115 undeclared; exit 0, 249 lines; exit 0; 210 pairs |
| `python3 moves.py`, a script outside the tree running 8 recorded `--moved` commands at their commits with the commit's script and then with fc4f81ae's | all 16 last lines as recorded |
| `bin/test tests/test_test_layout.py -q -p no:xdist -k Test_moved` with the 76551ca7 script copied in, then restored by `git checkout` | 11 failed, 24 passed |
| `bin/mutation-check skills/verify/scripts/test_layout.py`, n2 and o1 rebuilt, against `Test_moved` with `-x` | 2 red |
| `bin/mutation-check hooks/answers.py`, a17, with `HOME` in the scratch area: against the group's four new files at fc4f81ae, again with the new case deselected, and against the old file at 714f2df2 from an empty home | red; SURVIVED; red |
| `bin/mutation-check hooks/gate.py`, g3, at fc4f81ae and at 67a86c57 | SURVIVED; SURVIVED |
| `python3 swap_probe.py clone`, three calls of `moved` over two definitions of `b`, one in the case's file and one in the conftest | control 0 lines; one changed, `name b`; swapped, 0 lines |
| `bin/test tests/test_one_word_one_meaning.py -q -k test_no_live_text_says_the_word_0_19_0_renamed` | 1 passed |
