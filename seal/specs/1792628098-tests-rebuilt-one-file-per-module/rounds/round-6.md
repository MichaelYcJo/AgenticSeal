# 1792628098-tests-rebuilt-one-file-per-module — review round 6

target: db498230, fixes 854f8ff3..db498230

This round verified round 5's fix pass and its second fix pass, 31cf78dd to db498230. It checked round 5's two closes against the tree. It reviewed the reframe at 31cf78dd, the line and the subject rule at 24cd7813, the records at a1abd6a7 and 0c6d6bba, the reframe at 6a62ce17, the reading of an import inside a body at a29834e3, the row at 412760bd, the records at 1f9cd759, the amendment at c5f9641d, the docstring at caec3f8f, the overview at 40df21c5 and the handoff at db498230. Every run was in a `git clone --shared` of the branch worktree under `scratchpad/942-r6/`, one clone moved between commits for the move checks and one at db498230 for the mutants. The interpreter was the worktree's virtualenv, and `HOME` and `SPECSEAL_ANSWERS` pointed into the scratch area. Both clones were removed after the round. The script at db498230 differs from a29834e3's in its module docstring alone (`git diff a29834e3 db498230` over the script, read). The implementer's account was read as claims, and each claim this round checked is named below with what the tree showed.

Facts carried from earlier rounds and not established again: round 4's re-run lines for the 52 recorded commands, the 49 commands phase 7 records as printing the same lines under 0c6d6bba's and a29834e3's scripts (one of them, group 18's, was re-run here), the file and line of each definition phase 6's table gives for group 34's line, the verdicts of bp1, bt1 and br1, cp1 to cp6 and on1 to on3, and sw1 and sw2.

The code, the rows and the re-runs hold, and both of round 5's closes hold. The one finding is in the frame's foot. The second fix pass's reframe and amendment wrote two `Reframed` lines that do not match the line's shape, and the pull request check then reads `spec.md` as carrying no framer mark. Once the finding is answered, what comes due is the orchestrator's broad run, and the sealer's spawn after it.

## Findings

### 1. `spec.md`'s foot ends in two `Reframed` lines the chain check cannot read, so a ready pull request fails on a missing framer mark

severity: must
location: `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:560-561`
evidence: executed `chain_check.py --baseline release/v0.22.3 --root <branch worktree> --worktree`, `chain_check.py --baseline release/v0.22.3 --root <branch worktree>`, `chain_check.py --baseline origin/release/v0.22.3 --root <clone> --worktree`, `git grep -n "after round [0-9]*'s" db498230 -- 'seal/specs/*/spec.md'`
verdict: open
regression: round-5

The unit is the foot of `spec.md`, the framer's mark and the `Reframed` lines under it. The reframe at 6a62ce17 added line 560, `Reframed 2026-10-24 by framer, after round 5's fix pass.`, and the amendment at c5f9641d added line 561, `Reframed 2026-10-24 by framer, after round 5's second fix pass.`. The frame for that foot is the framer's definition and the record's rule: each reframe adds `Reframed <date> by <who>, after round <N>.` under the mark (`agents/framer.md:178-179`, `docs/the-review-record.md:507`). The two commits wrote a pass's name where the shape has the round's number and a full stop, so the defect came from how the lines were written, not from the frame.

What the check does with them. `chain_check.py#frame_foot` reads the foot from the last line up, takes each line `REFRAME_RE` matches (`^Reframed\s+(.+?)\s+by\s+(.+?),\s+after round\s+(\d+)\.$`, `skills/code-review/scripts/chain_check.py:250`), and stops at the first line it does not match, which must then be the `Framed` mark. Line 561 matches neither, so the check finds no mark. Executed at db498230, over the branch worktree and over HEAD, the check prints `spec.md does not end with Framed <date> by <who>, before the build., with any Reframed <date> by <who>, after round <N>. lines under it`. It exits 0 there only because no pull request exists. At a ready pull request the check is strict (`skills/code-review/scripts/chain_check.py:2067`) and returns 1 on any problem (`skills/code-review/scripts/chain_check.py:2151`), so the pull request fails on this line alone. At 854f8ff3 the foot ended `after round 4.` and read clean. No pull request exists yet, so no run so far has judged the foot strictly.

The class, enumerated. `git grep` over every `spec.md` under `seal/specs/` finds no other `Reframed` line of that spelling; the hits are prose. `plan.md`'s dated lines are prose the check does not read.

Seen fixed. In the scratch clone at db498230, with lines 560 and 561 replaced by one line in the shape, the check no longer prints the refusal. The file was restored after the run.

```markdown
seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md, lines 560 and 561,
in place of

Reframed 2026-10-24 by framer, after round 5's fix pass.
Reframed 2026-10-24 by framer, after round 5's second fix pass.

write

Reframed 2026-10-24 by framer, after round 5.
```

One line stands for 6a62ce17's reframe. `plan.md:19` records c5f9641d as an amendment, and the foot carries no line for the framer's earlier amendments (`plan.md:9-14`), so it takes none. If the framer counts c5f9641d as a reframe, a second `Reframed 2026-10-24 by framer, after round 5.` reads clean as well; the check accepts repeated rounds. Which pass each reframe followed is already stated in `spec.md:76` and `plan.md:17-19`.

answer:

## Confirmations

confirms: round-5#1
The close holds. The line names every name apart. Executed: group 15's command at f1d13be0, with the script at db498230, prints `names reader, HOOKS, READER, ROOT, _load, blocks, load_hook_module` for two cases, the name both readings find apart first and the names one reading alone reaches after it, each run in alphabetical order. The rows `two-changed-names` and `a-changed-name-beside-one-reached-once` pass at db498230 (`tests/test_test_layout.py`, 119 passed). The first row pins a line with two names apart, which `a-changed-name-beside-one-reached-once` cannot, since it has one name apart; the second pins the order of the two runs, which the first cannot, since both its names are apart. So each row covers something the other does not (read, `tests/test_test_layout.py:942-961`). The subject rule is stated in one set of words in `spec.md:78` and `CONTRIBUTING.md:302-310`. The module docstring states the line the rule reads (`skills/verify/scripts/test_layout.py:119-124`, read). Claimed: group 34's case is proved at `tests/test_broad_gate.py`'s `import pathlib`, `TARGET`, `ROOT` and `gate`, by five mutants red against the case alone. Executed: bg1 (`gate` bound to `chain_check.py`) and bg2 (`gate` with every reason of `PARTITION` emptied) are red at db498230 against that case alone. bg2 is red on the case's own assertion, whose sentence opens "No steps", as `phases/phase-6.md` records. The finding's sketch placed the mutants of a name only the base's reading reaches at the base. The framer refused that (`plan.md:81`), on the grounds that such a name is reached only through a name both readings reach whose definitions differ. Read against `_Names.forms` and `_Names.items` (`skills/verify/scripts/test_layout.py:801-857`), the argument holds. Both readings start from one body and one set of fixtures, so a name one side reaches alone hangs from a definition both sides reach that reads it on one side only, and that definition differs. The one other path is an import inside the case's own body of a module that one tree's module map lacks, and the moved case then fails at import in that tree. The answer's open sentence about `TOKEN_CASES` is answered by the second pass. Executed: group 19's command at e1e39bf7 prints `name _corpora` for `test_the_three_token_reads_answer_as_one`.

confirms: round-5#2
The close holds. Executed, one `mutation_check.py` batch over the script at db498230 against `Test_moved`: u2 (the guard `if source is not None:` dropped) and v1 (the `<module>.<name>` reading stopped at test files) are both red. The rows `a-directory-named-like-a-module` and `a-changed-attribute-of-another-test-file` stand at `tests/test_test_layout.py:753` and `tests/test_test_layout.py:1010`. `phases/phase-7.md`'s paragraph under *A test file's import followed, at 32cd06c7* now points at the row and no longer gives a reason (read). This round did not run either mutant with its row left out. That claim is carried from the fix pass's record.

confirms: none
The whole re-runs reproduce. Claimed: groups 15, 19 and 22 print fewer names on the same cases and keep their last lines and exits, and every other command prints what it printed. Executed, each command at its commit with the script at db498230 copied over the clone's and restored after. Group 15 at f1d13be0 ends `31 old cases, 142 items against 142 at 06d0f55453fc, 6 failed`, exit 1, and its four cases of `tests/test_the_hooks_hide_what_a_renderer_hides.py` print `names blocks, load_hook`. Group 19 at e1e39bf7 ends `2 old cases, 19 items against 19 at 95991e42b3d5, 2 failed`, exit 1. Group 22 at 10f6ad94 ends `65 old cases, 190 items against 190 at 92add28be86b, 5 failed`, exit 1, each of its five lines `name shape_text`. Group 18 at 95991e42 is one of the 49 unchanged commands: it ends `27 old cases, 27 items against 27 at 67a86c5730f0, 1 failed`, exit 1, its line `name git`, as round 4's re-run recorded. Each line matches the table in `phases/phase-7.md` *The import inside a function body, in round 5's second fix pass*. Group 15's two other lines name cases that stand at f1d13be0 in `tests/test_blocks.py`, which declares `TARGET = "hooks/blocks.py"`, so they count for that module's table (read, `git show f1d13be0:tests/test_blocks.py`).

confirms: none
The reading at a29834e3 and the row at 412760bd hold. Read: `_Names.reads` collects each import inside the node and keeps a name a `from` import binds only where the node loads it, and an `<owner>.<attribute>` only where an inner `import` binds the owner (`skills/verify/scripts/test_layout.py:778-797`). `_Names.items` follows each into a module of the same tree's map (`skills/verify/scripts/test_layout.py:822-826`). Claimed: L5 and L6 survived `Test_moved` until 412760bd's row and are red on it. Executed at db498230: L5 (`if _alias_name(alias) in loaded` dropped) and L6 (`if owner == _alias_name(alias)` dropped) are red against `Test_moved`. With the row `a-changed-name-of-a-local-import-the-case-does-not-read` deselected, both survive. So the row is the case that kills them, and it covers what no other row of its group covers. The three rows a29834e3 adds were each read against the group. Two refusing rows pin a `from` import inside the case and an `import` inside a helper, and no earlier row reaches an import below the top of a file. The accepting row pins the module-map test that keeps `tempfile` out.

confirms: none
The statements agree with each other and with the code. Read: `spec.md:78` and the module docstring (`skills/verify/scripts/test_layout.py:93-124`) name the same four limits in the same order: the string, the star import, the import inside a compound statement at the top of a file, and the swap. Both state the reading of an import inside a case or a definition in the same words. `CONTRIBUTING.md:295-297` sends a reader to the docstring for the conditions, and `CONTRIBUTING.md:302-310` states the subject rule in `spec.md`'s words. Executed: `git grep` at db498230 over `skills`, `agents`, `docs`, `CONTRIBUTING.md`, `tests`, `bin`, `hooks` and `.github` for "three limits", "two limits", "first name, in alphabetical", "definition its line names" and "in the file that defines it in the working" finds the docstring's "four limits" and three unrelated sentences, at `CONTRIBUTING.md:423`, `skills/implement/scripts/seal.py:165` and `tests/test_version_check.py:1`. In the frame, the older counts stand only in dated notes and in the steps of passes already run.

confirms: none
The two open items the orchestrator named are judged no finding.

- `spec.md` S15 does not name 412760bd's row `a-changed-name-of-a-local-import-the-case-does-not-read`. The behaviour the row pins, a name an inner import takes and the body does not read, is stated in `spec.md:78`: the reading follows such a name only where the case or definition "reads" it. The proof that the row is red on L5 and L6 has one source, `phases/phase-7.md`, and this round executed it again. S15 states no sentence the row contradicts, and nothing an agent does differs for the row's absence from S15's list, since the row stands in the suite either way. Adding the id would put a second copy of the suite's contents in the frame.
- `plan.md:18` says the 6a62ce17 reframe states three limits. It is the dated record of that reframe, which did state three, in the column of dated lines that starts at `plan.md:7`. `plan.md:19` records the amendment that made it four. `plan.md:16`, round 4's reframe, says two limits for the same reason. The current rule's one source is `spec.md:78`, which states four. Rewriting line 18 to say four would misstate what 6a62ce17 decided. No step a pass still has to run reads the line.

confirms: none
The CLAUDE.md question, asked of the name condition once more: does the framer's argument hold, that the ways a body reaches a definition in another module under `tests/` can be listed from Python's grammar (`plan.md:88`, `questions.md:60`)? It holds for every shape the suite holds. Executed, a scan with `ast` of every `.py` file directly under `tests/` at db498230 through `git show`: 202 imports of a module under `tests/` at the top of a file, 26 inside functions in 13 files, and none in a compound statement at the top of a file, in a class body or as a star import. That matches `questions.md:57-59`. No inner import binds a name its function never loads, and none binds a module its function reads bare. Executed, `git grep` over `tests/`: no import through `tests.` and no relative import. No loader call loads a file under `tests/`, and `globals()` is read only in `tests/test_release_hygiene.py:794-803`, where the string limit stands as stated. This round looked for shapes outside the framer's list, and found three. None is a regression, because no move this work made reaches one.
- A `self.<name>` that a case's class takes from a base class. `_Names.forms` looks such a name up in the class body alone, so a changed inherited definition would compare equal. Executed, every class under `tests/` with a base: five helper classes, each base read as a name the helper's definition reads. No test class has a base.
- An xunit setup or teardown function, which pytest calls without a case reading it. None stands under `tests/`.
- A pytest hook in `tests/conftest.py`. Three stand, and the branch changed them only in phase 2's planned report: `pytest_collection_modifyitems` and `pytest_configure` read alike at 6046f062 and db498230, and `pytest_runtest_makereport` gave way to `pytest_terminal_summary`.
No file holds the first two shapes, and no group's move changed the third, so each is a limit question. `## Not judged` holds it for the framer.

confirms: none
The changed modules and the tree checks pass at db498230. Executed in the clone: `python -m pytest tests/test_test_layout.py tests/test_docs_line_wrap.py -q -p no:xdist`, 119 passed. `test_layout.py --check` exits 0 with `184 files read, 0 refused, 115 declare no TARGET`. `rules.py --check` exits 0, with all 249 check lines in 62 rule files holding. `unverified_check.py seal/specs/` exits 0.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at db498230, unverified. Nothing is due from this round until finding 1 is answered; then the broad run, and the sealer's spawn after it | the whole tree | the orchestrator, at the broad gate |
| The other 48 recorded commands run whole, the comparison of all 52 through `moved`, and the mutants this round did not rebuild: bp1, bt1, br1, L1 to L4, z1 to z3, p1, p2, on1 to on3, and u2 and v1 with their rows left out. This round ran 4 commands whole and 8 mutant runs | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md` | the sealer |
| Whether `spec.md` *The proof of equal protection* and the script's module docstring state as limits a `self.<name>` that a case's class takes from a base class, and a function pytest calls that no case reads, an xunit setup or a hook in `tests/conftest.py`. Under the owner's direction a shape the flow does not produce gets a limit sentence and not a guard. The sentence "every other way a body reaches a definition in another module under `tests/` is an import that binds the name the body reads" does not hold for the first. No file under `tests/` holds the first two, and no move changed the third | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:78`, `skills/verify/scripts/test_layout.py:108-118` | the framer, through the orchestrator |
| `overview.md`'s *Not verified* row on the files changed after b2c300c9 still reads open. `handoff.md` item 2 names CI run 40007433075 at 1f9cd759 as passing every leg over those files, and the commits after it change a docstring and records. This round did not read the run | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:35` | the orchestrator |
| The directory `s1` that round 4's fix pass left in the answers store under the home directory. This round did not open or remove it | outside the repository | the owner |

## Probes

| Command | Result |
|---|---|
| `git clone --shared` of the branch worktree into `scratchpad/942-r6/clone-moves` and `scratchpad/942-r6/clone-mutants`; both removed after the round with every script below | every run below ran in one of them |
| `python3 moves.py`: groups 15, 18, 19 and 22 run whole at f1d13be0, 95991e42, e1e39bf7 and 10f6ad94, the script at db498230 copied over the clone's and restored after | 6, 1, 2 and 5 failed, each exit 1, each last line as recorded; the clone's status clean after |
| `python3 mutants.py`: bg1 and bg2 over `tests/test_broad_gate.py` against the one case of group 34's line; L5, L6, u2 and v1 over `skills/verify/scripts/test_layout.py` against `Test_moved`; L5 and L6 again with 412760bd's row deselected | 2 red; 4 red; 2 SURVIVED; the clone's status clean after |
| `python3 bg2.py`: bg2 alone, for its output | red on the case's assertion, the sentence opening "No steps" |
| `python3 shapes.py db498230`: each import of a module under `tests/` in each `.py` file directly under `tests/`, by where it stands | 202 at the top of a file, 26 inside functions in 13 files, none in a compound statement, a class body or a star import; none unread, none read bare |
| `python3 implicit.py db498230`: classes with a base, xunit setup and teardown functions, and pytest hooks in every `.py` file under `tests/` | 5 helper classes with a base, no test class; no xunit function; 4 hooks, 3 in `tests/conftest.py` |
| `python3 hooks_diff.py`: `tests/conftest.py`'s hooks at 6046f062 against db498230 | two alike, one at the base only, one at the head only |
| `python -m pytest tests/test_test_layout.py tests/test_docs_line_wrap.py -q -p no:xdist`, `test_layout.py --check`, `rules.py --check`, `unverified_check.py seal/specs/` | 119 passed; exit 0, 115 undeclared; exit 0, 249 lines; exit 0 |
| `chain_check.py --baseline release/v0.22.3` over the branch worktree, once with `--worktree` and once at HEAD, the repository's copy and the plugin's | exit 0, no pull request found; each prints the refusal that `spec.md` carries no framer mark, beside the broad-gate and guarantee files not yet written; at HEAD also round 5's closes awaiting this record |
| the same check in `scratchpad/942-r6/clone-mutants` at db498230, before and after `spec.md` lines 560 and 561 were replaced by one `Reframed 2026-10-24 by framer, after round 5.` through the `Edit` tool; the file restored after | the refusal printed once before, and not after; the clone's status clean after |
