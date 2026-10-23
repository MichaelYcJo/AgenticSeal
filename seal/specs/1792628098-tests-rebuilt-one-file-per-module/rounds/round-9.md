# 1792628098-tests-rebuilt-one-file-per-module — review round 9

target: 1c43f6a4, fixes c3028ee1..1c43f6a4

This round reviewed the two commits after round 8's record: ed3f25a8, which moves the two rows of `test_every_reader_of_a_retirement_calls_the_one_predicate` from `tests/test_unverified_rows_close.py` into `Test_module` of `tests/test_chain_check.py` and `tests/test_settle.py`, and 1c43f6a4, which writes `phases/phase-7.md` *The retirement-predicate case placed, in round 8's fix pass*, rewrites `phases/phase-7.md` line 337 and answers round 8's finding 1. It asked three things. Does ed3f25a8 answer that finding? Do the placement, the body change and the `.test_durations` change hold? And do the two cases of `tests/test_a_script_copied_alone_exits_2.py`, which the fix pass named and did not move, stand where they are on grounds the frame gives? Every command ran in a `git clone --shared` of the branch worktree under the round's scratch directory, first at ed3f25a8 and then at 1c43f6a4. `HOME`, `SPECSEAL_ANSWERS` and `TMPDIR` pointed into that directory, and the worktree's `.venv` stood first on `PATH`. The clone was removed before hand-back. The implementer's account was read as claims: the two commit messages, the new section of `phases/phase-7.md` and the `answer:` line of round 8's finding 1. Each claim is named below with what the tree showed.

Facts carried from earlier rounds and not established again: what the move check's four conditions are and that `skills/verify/scripts/test_layout.py` implements them, as rounds 3 to 8 reviewed it; and that the cases `phases/phase-6.md` lines 589 and 1603 keep in place stand where they are for the reasons those lines give, which rounds 2 to 6 read. This round did re-judge the grounds that `phases/phase-6.md` lines 765 and 1064 give for the two cases of `tests/test_a_script_copied_alone_exits_2.py`, because the fix pass's own record now names those cases as having round 8's finding's shape (`phases/phase-7.md:372`).

## Findings

### 1. The two cases of tests/test_a_script_copied_alone_exits_2.py are kept as checks across files, but each row runs one module alone, so rule 2 sends them to their modules' files

severity: should
location: `tests/test_a_script_copied_alone_exits_2.py:1-35`, `tests/test_a_script_copied_alone_exits_2.py:135-202`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:54`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:765`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:1064`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:372`, `tests/test_config.py`, `tests/test_routing.py`, `tests/test_fold_check.py`, `tests/test_settle.py`, `tests/test_chain_check.py`, `tests/test_seal.py`, `tests/test_payload_meter.py`, `tests/conftest.py`, `tests/test_conftest.py`
evidence: read `tests/test_a_script_copied_alone_exits_2.py:135-202`, `hooks/config.py:50-66`, `hooks/routing.py:40-56`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:57`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:97`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:129`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/questions.md:28`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:765`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:1064`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:54`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:372`
verdict: open

This matters for the reason round 8's finding 1 gave, and the records now also contradict each other. `overview.md:5` says that a rebuilt module's tests stand in one file that declares it as `TARGET`. Round 8 quoted the sealer's condition for that sentence to hold: every case standing outside its module's file is either moved or named in the records with grounds (`guarantee.md` line 60 at 95f139e1, a carried coordinate). These two cases are named, but on a ground the code does not meet. The fix pass's new paragraph says of both cases "No row of either case compares one module with another" (`phases/phase-7.md:372`). `overview.md:54` still counts the file among the checks of which "each compares files with each other, derives a set across files, or holds a reader to an oracle, a renderer, bash, git or the committed records", and `phases/phase-6.md:765` and `:1064` keep each case as "a check across files". The next agent to read the records is #923's, or the settle that closes S10. It reads `overview.md:54`, takes the file for a check across files, and leaves the cases of seven rebuilt modules out of those modules' files.

The grounds, case by case.

`test_a_hook_reader_copied_without_the_walk_names_it` has two rows (`tests/test_a_script_copied_alone_exits_2.py:174-202`). The `config.py` row copies `hooks/config.py` alone. The `routing.py` row copies `hooks/routing.py` together with `hooks/optin.py`, because `routing.py` runs `import optin` before it imports `blocks` (`hooks/routing.py:41`). Each row then imports its one module and asserts that the import fails with an `ImportError` naming `blocks.py` and ending in a fixed sentence. Each module raises that sentence from its own guard, as its own literal: `hooks/config.py:50-66` and `hooks/routing.py:43-56`, which differ in the file each walks (`config.md`, `routing.md`). No row loads the other module, and no row compares the two. `phases/phase-6.md:765` says the case "holds `hooks/config.py` and `hooks/routing.py` to one sentence in one parametrized body, a check across files that stays". The body does hold each module to a sentence the test writes, but it never holds one module to the other.

`test_a_script_copied_alone_exits_2_and_names_what_it_misses` has eight rows, one per entry of `CASES` (`tests/test_a_script_copied_alone_exits_2.py:51-105`, `:135-165`). Each row copies one script into an empty directory and runs it there. It then asserts five things about that one run: exit 2, no traceback, the copy's directory named, the purpose phrase present, and the `absent` phrase missing. Each phrase is that script's own loader text. `phases/phase-6.md:1064` keeps the case because it "runs each of several shipped scripts copied alone". Running several scripts, one per row, is not a comparison of files.

What the frame says. `spec.md:97` keeps in place a check that "reads a document's prose, compares files with each other, derives a set across files, or judges records or markdown against an oracle". `spec.md:129` repeats "compare files with each other". Neither case does any of the four: `CASES` and `HOOK_READERS` are written out by hand, not derived from a listing. Rule 2 gives every old case that exercises a target one verdict (`spec.md:48`, `:57`). `questions.md:28` lands a moving case in "the rule 1 file of the module whose function the case calls as its subject", and each row's subject is the one module it copies. All seven of those files exist at 1c43f6a4 (executed, `ls`). So the frame's text decides these cases the way round 8's finding 1 decided the retirement case. No sentence of the frame keeps them.

The fix pass found the shape and recorded it. Its paragraph says it "moved neither, because the spawn asked for finding 1's case" (`phases/phase-7.md:372`). Contract section 12 owes the fix to every instance the same cause produces.

Why this is neither a `regression:` nor a `reopens:`. A build phase made the keep, phase 6 at lines 765 and 1064, and the fix passes since then changed neither case. Round 8's finding 1 enumerated its class as the two places that cite `spec.md` line 97 for the retirement case, and that round did not re-judge line 765. Its close holds for the case it named (see the confirmation below). So this is an ordinary finding.

The class, as far as this round read it. The cases kept by the *Two left cases placed* paragraph compare files with each other, as `phases/phase-7.md:372` describes them; this round did not open their bodies. `tests/test_a_reference_root_is_read_and_never_taken.py::test_the_pinned_checks_read_under_the_root_alone` is kept by the same paragraph at `phases/phase-6.md:765`. It asserts `settle.SPECS` and `routing.WORK_ITEMS` each against a literal, which is the same shape in its assertions. But it stands beside the file's classification of every `bin/` command, and `agents/warden.md:99`'s `check:` line names its file, so the frame does not settle it alone. It is a row of `## Not judged`. This round did not read the other twelve files of `overview.md:54` case by case, which is a row of `## Not judged` too.

The fix, on the path rule 2 states. It is the shape ed3f25a8 gave the retirement case:

```text
1. tests/conftest.py: define `names_path(path, text)` once, with the body of
   tests/test_a_script_copied_alone_exits_2.py:108-115 unchanged, because it
   will be read by seven test files (spec.md rule 1, a helper used by two files).

2. Each module's Test_module takes its rows, with each row's script bound from
   TARGET as ed3f25a8 bound `script`, and the rest of the body unchanged:
   tests/test_config.py        test_a_hook_reader_copied_without_the_walk_names_it, row ("config.py", [])
   tests/test_routing.py       test_a_hook_reader_copied_without_the_walk_names_it, row ("routing.py", ["optin.py"])
   tests/test_fold_check.py    test_a_script_copied_alone_exits_2_and_names_what_it_misses, the fold_check.py row
   tests/test_settle.py        the same case, the settle.py row
   tests/test_chain_check.py   the same case, the chain_check.py row
   tests/test_seal.py          the same case, parametrized over the three seal.py rows
   tests/test_payload_meter.py the same case, parametrized over the two payload_meter.py rows
   Each receiving file's docstring names the case and the file it came from.

3. tests/test_conftest.py: test_the_path_is_found_as_a_windows_oserror_spells_it,
   which then tests a helper of tests/conftest.py, in `Test_module` as 099cd54d
   placed a single-case function, or in a `Test_names_path` that rule 1 accepts.

4. tests/test_a_script_copied_alone_exits_2.py: removed once it holds no case. No
   check: line names it (executed, git grep over docs, agents, skills, templates,
   .github, CONTRIBUTING.md and CLAUDE.md at 1c43f6a4). `.test_durations`: each old
   id replaced by its new id, with its seconds kept.

5. The move check over the old file and the eight receiving files, and
   decision-point mutants for each module its failing lines send, against the
   moved case alone, as phase-7.md *The retirement-predicate case placed* ran them.

6. Records: overview.md:54 drops the file and counts 13 files; every count of the
   files declaring no TARGET that the removal changes, found by git grep on the
   count, is rewritten in place; phases/phase-6.md:765 and :1064 say where each
   case went; phases/phase-7.md:372 records the move in place of "This pass
   moved neither".
```

If the fix pass finds a sentence of the frame that keeps these cases, the other path is to keep them and state that sentence. It goes in `overview.md` *Where spec and implementation diverged*, and `phases/phase-6.md:765`, `:1064` and `overview.md:54` are rewritten to it. This round found no such sentence.

answer:

## Confirmations

confirms: round-8#1
The close holds. ed3f25a8 removes the retirement case from `tests/test_unverified_rows_close.py` and places one row in each module's file, which is the first path the finding gave. Executed in the clone at ed3f25a8: `bin/test-layout --moved c3028ee1 --from tests/test_unverified_rows_close.py tests/test_chain_check.py tests/test_settle.py --to` the same three files exits 1. It prints the three lines `phases/phase-7.md` records, word for word: the old case's body not in the new files unchanged, and each landing standing for no old case. Its last line is `test-layout: moved: 168 old cases, 342 items against 342 at c3028ee1bd51, 3 failed`, and `git worktree list` afterwards shows the clone alone. The two moved cases pass unmutated (2 passed). Two of the smith's six mutants were written again in the clone and run against the moved case alone. rc1 makes `chain_check.py#retired` return `set(gone)` and call no `settled`. It is red with `skills/code-review/scripts/chain_check.py decides a removal without asking the predicate`, from `tests/test_chain_check.py:3039`. rs2 adds a `def settled` at the top of `settle.py` before `rule_arm` and keeps the calls. It is red on the message that `skills/settle/scripts/settle.py` defines a second `settled`, from `tests/test_settle.py:1230`. Each mutant was restored before the clone moved on. The finding's other coordinates are answered too. The old docstring no longer cites a check across files for the case (`tests/test_unverified_rows_close.py:3-13`, read). `phases/phase-7.md:337` no longer cites `spec.md` line 97 for it and now says each row judges one file alone (read). `overview.md:19-21` needed no change, because no row there named the case.

confirms: none
The placement in `Test_module` holds against rule 1. The account claims that the second assertion walks the whole module for a definition of `settled`, so the case holds the module as a whole. The body shows it: `ast.walk(tree)` over the parsed file, for any `FunctionDef` named `settled` (`tests/test_chain_check.py:3042-3046`, read). The two function classes it could have gone to were weighed too. `tests/test_chain_check.py::Test_retired` at line 2988 holds cases that run `retired`. `settle.py#rule_arm` has no class: executed, `bin/test-layout --check` over the three files at 1c43f6a4 reports `function rule_arm has no class Test_rule_arm` and exits 0, with 3 files read and 0 refused. `--pairs` over the two receiving files names 0 pairs (executed). The moved case was also read against its group. A mutant that adds a second `def settled` while the call stays, as rc2, rc3, rs2 and rs3 do, changes no behaviour, so no case that runs `retired` or `rule_arm` can see it. The moved case is the one that does. It covers something its group does not, and the verdict is place, not merge.

confirms: none
The body change holds. Each case binds `script = TARGET.split("/")` and reads `os.path.join(ROOT, *script)`. `TARGET` is `skills/code-review/scripts/chain_check.py` at `tests/test_chain_check.py:29` and `skills/settle/scripts/settle.py` at `tests/test_settle.py:31`, so each case reads the module its file declares (read). `ROOT` is a `pathlib.Path` in the first file and a string in the second, and `os.path.join` takes either; the unmutated run passed in both files (executed). The rest of each body matches the old one, apart from the formatter's parentheses around one assertion message, which the AST does not see (read, the diff of ed3f25a8). `uvx ruff check` and `uvx ruff format --check` pass each of the three changed test files, one file per run (executed).

confirms: none
The `.test_durations` change holds. Executed, a script over `git show <rev>:.test_durations` at c3028ee1, ed3f25a8 and 1c43f6a4. Each holds 7,726 ids. At c3028ee1, the two old ids `[script0]` and `[script1]` price at 0.11326790000003939 s and 0.03778609999994842 s. At ed3f25a8 and 1c43f6a4, the `tests/test_chain_check.py` id carries the first and the `tests/test_settle.py` id carries the second. That matches the parameter order, where `script0` was `chain_check.py`. The file is not in sorted key order at c3028ee1 either, so where the ids stand is no contract, and each new id stands beside its class's other ids (read, the diff). `git grep` at 1c43f6a4 finds the case's name outside `.test_durations` and `seal/specs/` only at its two new definitions, `tests/test_chain_check.py:3019` and `tests/test_settle.py:1207`. Inside `seal/specs/`, it finds the name in the two other work items' records `phases/phase-7.md` names, and in this work item's records (executed). No `check:` line names the case. `bin/rules --check` at 1c43f6a4 exits 0, with all 249 check lines in 62 rule files holding (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 1c43f6a4, unverified. ed3f25a8 changed tests after the broad gate's record. This round declined none of the three, because the prompt ordered none | the whole tree | the orchestrator, at the broad gate after finding 1 is answered |
| CI at 1c43f6a4, unverified, not read | the run | the orchestrator |
| rc2, rc3, rs1 and rs3 of `phases/phase-7.md`'s mutation table, read and not re-run. This round re-ran rc1 and rs2 | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md` | the sealer, where it samples the smith's claims |
| Whether `tests/test_a_reference_root_is_read_and_never_taken.py::test_the_pinned_checks_read_under_the_root_alone` belongs in `tests/test_settle.py` and `tests/test_routing.py`. Each of its two assertions reads one module's constant against a literal, the shape of finding 1. But it stands beside the file's census of every `bin/` command, whose `PINNED` rows name the constants it holds, and `agents/warden.md:99`'s `check:` line names its file, so whether it is part of a set across files is the frame's to say | `tests/test_a_reference_root_is_read_and_never_taken.py:88-95`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:765` | the framer |
| Whether any case of the other twelve files `overview.md:54` names has finding 1's shape, rows that each judge one module alone. This round read the two cases the fix pass named and not the other files case by case | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:54` | round 9's fix pass, as finding 1's class under contract section 12 |
| Round 6's other rows of `## Not judged`, carried as rounds 7 and 8 carried them. This diff answers none of them | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/rounds/round-6.md` | as round 6 names them |

## Probes

| Command | Result |
|---|---|
| `git clone --shared --no-checkout` of the branch worktree into the round's scratch directory, then `git checkout --detach ed3f25a8` | clone at ed3f25a8, c3028ee1 present; later moved with `git switch --detach 1c43f6a4`; removed before hand-back |
| `bin/test-layout --moved c3028ee1 --from tests/test_unverified_rows_close.py tests/test_chain_check.py tests/test_settle.py --to` the same three files, at ed3f25a8, with the worktree's `.venv` first on `PATH` and `HOME`, `SPECSEAL_ANSWERS` and `TMPDIR` in the scratch directory | exit 1; three lines as `phases/phase-7.md` records them; `test-layout: moved: 168 old cases, 342 items against 342 at c3028ee1bd51, 3 failed`; `git worktree list` afterwards shows the clone alone |
| `python -m pytest -q -p no:xdist -p no:cacheprovider` on the two moved node ids, at ed3f25a8 | 2 passed, exit 0 |
| rc1 written with the `Edit` tool into the clone's `chain_check.py#retired`, and rs2 into the clone's `settle.py`, then each moved case run alone with pytest | rc1: 1 failed, exit 1, on the call assertion; rs2: 1 failed, exit 1, on the second-definition assertion; both files restored with `git restore` |
| `bin/test-layout --check` over the three changed test files; `bin/test-layout --pairs tests/test_chain_check.py tests/test_settle.py`; `bin/rules --check`, at 1c43f6a4 | exit 0, 3 read, 0 refused, `rule_arm` reported without a class; exit 0, 0 pairs; exit 0, all 249 check lines in 62 rule files hold |
| `uvx ruff check` and `uvx ruff format --check`, each of the three changed test files, one file per run, at 1c43f6a4 | each exit 0 |
| A script over `git show <rev>:.test_durations` at c3028ee1, ed3f25a8 and 1c43f6a4: id count, sorted order, and the case's ids with their seconds | 7,726 ids at each, unsorted at each; the two seconds carried to the two new ids, `script0` to `tests/test_chain_check.py` |
| `git grep` at 1c43f6a4 for the case's name, for `test_a_script_copied_alone_exits_2` and `test_a_reference_root_is_read_and_never_taken` under the policy and agent roots, and for each blocks guard's `from missing`; `ls` of the seven receiving test files | as stated in the confirmations and finding 1; one `check:` line, `agents/warden.md:99`, names the reference-root file, and none names the copied-alone file; all seven files exist |
| `chain_check.py --baseline release/v0.22.3 --root <branch worktree> --worktree`, after this record, with the branch's copy and the installed plugin's copy | each exit 0, no pull request found; four lines each: this record's finding 1 reading `open`, the broad-gate record and the guarantee behind HEAD since 264b37cf, and the guarantee's `withheld` verdict |
