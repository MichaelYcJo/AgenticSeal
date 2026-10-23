# 1792628098-tests-rebuilt-one-file-per-module — review round 5

target: c97b5f91, fixes a1047bfe..c97b5f91

This round verified round 4's fix pass, b120e598 to c97b5f91. It checked round 4's two closes against the tree. It reviewed the reframe at b120e598, the change to `skills/verify/scripts/test_layout.py#_test_modules` and its `Test_moved` rows at 32cd06c7, the statements in the script's docstrings and in `CONTRIBUTING.md` *The test layout*, the records at f9031b38 and cc420aa0, and the framer's count correction at c97b5f91. Every run was in a `git clone --shared` of the branch worktree, in `scratchpad/942-r5/clone`, moved between the commits the records name, with the worktree's virtualenv as the interpreter and `HOME` and `SPECSEAL_ANSWERS` in the scratch area. The clone was removed after the round. The script at c97b5f91 is the script at 32cd06c7 (`git diff --stat` empty). Facts carried from rounds 3 and 4 and not established again: each recorded last line reproducing under its own commit's script, and the group tables of phase 6 that the subject table stands on (groups 16, 17, 23, 35 and 37), read as recorded. The implementer's account was read as claims, and each claim this round checked is named below with what the tree showed.

The two findings are both in the unit 32cd06c7 and b120e598 made. Finding 1 is about the rule that sends a failing case of an undeclared file to a definition: the line it keys on names one name, and for group 34 that name's mutant sat on a definition that did not change. Finding 2 is about two readings of the changed module map that no row pins.

## Findings

### 1. Group 34's case is proved at a `ROOT` that did not change, and the definitions that did change behind it carry no mutant

severity: should
location: `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:78`, `CONTRIBUTING.md:300-306`, `skills/verify/scripts/test_layout.py:104-108`, `skills/verify/scripts/test_layout.py:813-819`, `skills/verify/scripts/test_layout.py:909-913`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:1827`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:1845`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:1851`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:35`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:45`
evidence: executed `python3 lines.py`, `python3 show.py undeclared`, `python3 mutants.py`, `git show 5966150b:tests/test_broad_gate.py`, `git show 10667b32:tests/test_the_gate_names_every_step_ci_runs.py`, `git show 5966150b:tests/test_the_gate_names_every_step_ci_runs.py`
verdict: open
regression: round-4#1

The unit is the rule for a failing case that stands in a file declaring no `TARGET` and calls no shipped module, which the reframe at b120e598 wrote into `spec.md:78` and 32cd06c7 into `CONTRIBUTING.md:302-306`, as f9031b38 applied it to group 34. The frame sends such a case to "the definition its line names, in the file that defines it in the working tree" (`plan.md:114`, step 4, and `spec.md:78`); the fix ran one mutant, ro1, at the `ROOT` of the case's own file; the defect comes from the rule, which takes the line's one name for every changed definition and one file for its place, while the line names only the first name in alphabetical order and the condition compares each name as the set of its definitions across files.

What the trees show. The case is `tests/test_the_gate_names_every_step_ci_runs.py::test_the_skill_counts_the_steps_with_a_local_answer_and_no_arm`. It reads `reasons()`, which group 34 moved into `tests/test_broad_gate.py`. With the import followed, the case's reading at 5966150b reaches two definitions of `ROOT`. Its own file holds `ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))`, the same text as at the base 10667b32 (line 43 there, line 48 at 5966150b). `tests/test_broad_gate.py` holds `ROOT = pathlib.Path(__file__).resolve().parent.parent` (line 45 at 5966150b). The key `ROOT` differs only because the second joined the set. The condition also finds `gate` apart: `gate = gate_module()` in the case's file at the base (line 53), against `gate = load_module(ROOT / TARGET, "broad_gate_under_test")` in `tests/test_broad_gate.py` (line 54 at 5966150b). It finds `GATE`, `TARGET`, `gate_module` and `pathlib` reached by one tree's reading alone. The line prints `ROOT` and nothing else, because `_name_change` returns the first key in alphabetical order, and a capital letter sorts before a small one.

What ran. The record claims ro1, "`ROOT` names `tests/`, not the repository", red at collection (`phases/phase-6.md:1845`). The fix pass's batch input, left in the session's scratch area as `scratchpad/942-r4fix/specs/root.json`, puts it on the case file's own line, the one that did not change. Rebuilt there, ro1 is red with `1 error during collection`, so the case never ran. No mutant sits at `tests/test_broad_gate.py`'s `ROOT` or at `gate`. The proof for this case rests on a definition the move did not change, and the two definitions it did change are unproved. `overview.md:35` and `phases/phase-6.md:1851` count this case where they say no protection was lost.

Why it matters past this case. `CONTRIBUTING.md` carries the rule past this work item, and every later move that leaves a check across files or a prose case behind meets it. A contributor who follows it proves the first name in alphabetical order and ships the others unproved. Where the reading reaches the name in two files, the rule names no file.

The class, enumerated. `lines.py` read all 52 recorded commands with the script at c97b5f91, instrumented to report every name apart for each failing case and where the case stands. Three commands send a line to a definition. 4e987021's five lines find `OPENS_NOTHING` alone apart. Group 19's line finds `_corpora` apart and `TOKEN_CASES` reached by the base's reading alone; cp2, which drops `TOKEN_CASES`'s commands from `_corpora`, survives at the head and at 95991e42, so that collection is measured in substance, though the record does not say so. Group 34's line is the one that escapes. Lines of groups 7, 9, 22, 23, 35 and 37 also find more than one name apart, but their subject is the shipped module the case calls, so the extra names change nothing they send.

```python
# skills/verify/scripts/test_layout.py, `_name_change`, in place of lines 813 to 819:
def _name_change(before, after):
    """Every key whose definitions BEFORE and AFTER, `{key: forms}`, read
    apart where both reached it, then every key one side reached and the
    other did not, each run in alphabetical order; empty where every one
    reads alike."""
    apart = sorted(k for k in before.keys() & after.keys() if before[k] != after[k])
    return apart + sorted(before.keys() ^ after.keys())


# `moved`, in place of lines 909 to 913:
            names = _name_change(*reached)
            if len(names) == 1:
                lines.append(
                    f"{where}: name {names[0]}: its definition differs from the base's"
                )
            elif names:
                lines.append(
                    f"{where}: names {', '.join(names)}: their definitions differ "
                    "from the base's"
                )
```

```markdown
spec.md, The proof of equal protection, the fourth condition, in place of
"a case that fails the fourth prints one line, `moved: <old file>::<case>:
name <name>: its definition differs from the base's`, where `<name>` is the
first name in alphabetical order whose own definition differs, so a changed
name reached through a helper is named itself and the helper is not.":

a case that fails the fourth prints one line naming every name whose own
definition differs, those both trees reach first and then those one tree's
reading reaches alone, each run in alphabetical order: `moved: <old
file>::<case>: name <name>: its definition differs from the base's` for one
name, and `moved: <old file>::<case>: names <name>, <name>: their
definitions differ from the base's` for more. A helper that reads a changed
name is not named, because its own definition did not change.

spec.md, the same bullet, and CONTRIBUTING.md, The test layout, the move
check bullet, in place of "it counts for the definition its line names, in
the file that defines it in the working tree, and that definition's
decision points carry the mutants":

it counts for each definition its line names, at the place the working
tree's reading reaches with a form the base's reading does not reach, or,
for a name only the base's reading reaches, at the base, and those
definitions' decision points carry the mutants

skills/verify/scripts/test_layout.py, the module docstring, the `names`
entry, in place of "its line names the first name, in alphabetical order,
whose own definition differs":

its line names every name whose own definition differs, those both trees
reach first, each run in alphabetical order

phases/phase-6.md, The move checks re-run with a test file's import
followed: group 34's row names as its subject the definitions its re-run
line names at 5966150b, `ROOT` and `gate` of tests/test_broad_gate.py among
them, each with its mutants run against the case's file at the head and the
old column for a survivor over group 34's old files at 10667b32. Group 19's
row says that cp2 stands for `TOKEN_CASES`. A row of
tests/test_test_layout.py::Test_moved with two names apart, seen red
against the script at c97b5f91, pins the new line.
```

answer:

### 2. Two readings of the changed module map pass `Test_moved` broken: `<module>.<name>` into a test file, and u2

severity: should
location: `tests/test_test_layout.py:633`, `tests/test_test_layout.py:661-702`, `tests/test_test_layout.py:845-913`, `skills/verify/scripts/test_layout.py:778`, `skills/verify/scripts/test_layout.py:991`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md:190-199`
evidence: executed `python3 mutants2.py`, `git ls-tree c97b5f91 tests/`
verdict: open
regression: round-4#1

The unit is 32cd06c7's change to `_test_modules`, with the rows and the mutant batch that `plan.md` *Round 4's fix pass* step 1 asks for. The frame has the changed code's mutants run over `Test_moved`, "each survivor is answered by a row seen red on it" (`plan.md:111`), and the condition reads `<module>.<name>` into any module directly under `tests/` (`spec.md:78`); the fix wrote two rows for `from <module> import`, ran 31 mutants and answered its one survivor, u2, by a reason (`phases/phase-7.md:199`); the defect comes from the batch, which carried no mutant for the attribute reading the same change opened, and from the answer, which leaves u2 standing where the plan asks for a row.

- The attribute reading. `_test_modules` now puts every test file in the module map, so `_Names.items` follows `test_x.<name>` after `import test_x` (`test_layout.py:778`). The docstring states it, "or that `<module>.<name>` reads after `import <module>`, where the module is any module directly under `tests/`, a test file among them", and so does `spec.md:78`. v1 adds `and not alias.name.startswith("test_")` to line 778, so the reading stops at test files. It survives `Test_moved`. No row reads an attribute of a test file: the world's one test file beside the old files, `tests/test_e.py`, is reached through `from test_e import V` alone.
- u2. Rebuilt from its record, with the guard `if source is not None:` at `test_layout.py:991` dropped, it survives `Test_moved`, as the record says. The reason's facts hold. No `.py` entry directly under `tests/` at c97b5f91 is anything but a file. Under u2 such an entry reaches `ast.parse(None)` at line 864 and stops the check with a traceback, exit 1, so it passes no group. But the plan asks for a row, and the overview's divergence table has none for this departure. A row is cheap: a directory named like a module, written only in the working tree, makes `_read` return None through `IsADirectoryError`.

Why it matters: the statements now promise both readings and nothing pins either. A later edit that narrows line 778 or drops line 991 passes the suite. The record's table says the batch left one survivor, and a mutant it never carried survives too.

```python
# tests/test_test_layout.py

OLD_G, G = "tests/test_old_g.py", "tests/test_g.py"  # NAMES NOT IN TREE, added with these rows

# _moved_world, after the line that writes tests/test_e.py:
    write(repo, OLD_G, "import test_e\n\n\ndef test_attribute():\n    assert test_e.V\n")

# Test_moved::test_accepts_a_pure_move, one more entry in the list of
# `(new, beside)` pairs, with the id "a-directory-named-like-a-module"
# after the last id:
                (NAMED_NEW, {"tests/held.py/rows.txt": "a 1\n"}),

# Test_moved::test_refuses_a_cut_a_merge_an_edited_body_and_a_changed_fixture,
# one more row after the last, with the id
# "a-changed-attribute-of-another-test-file" after the last id:
        + [
            (
                {
                    G: "import test_e\n\n\nclass Test_module:\n"
                    "    def test_attribute(self):\n        assert test_e.V\n"
                },
                {"tests/test_e.py": "V = 2\n"},
                [f"moved: {OLD_G}::test_attribute: name test_e.V: {DIFFERS}"],
                (OLD_G,),
            )
        ]
```

The first row is seen red on u2 and the second on v1, as step 1 asks. `phases/phase-7.md`'s table then lists u2 and v1 red and drops the reason.

answer:

## Confirmations

confirms: round-4#1
The close holds for what the finding named. Executed, with the script at c97b5f91: groups 29 and 49, run whole at 31aed13b and a4a113f6, end `0 failed` and exit 0 as recorded, and groups 41 and 48 print no line through `moved`. Claimed: 34 lines name a case in a file that declares no `TARGET`, 29 in phase 6's commands and 5 in 4e987021's. `lines.py` finds 34 over all 52 commands: groups 1 (5), 7, 8, 9, 14 (12), 16 (2), 19, 22, 23, 34, 35 and 37 (2), and 4e987021 (5), every one on the name condition and none on a body or fixture line. Each has its row in `phases/phase-6.md:1812-1830` or its section in `phases/phase-7.md:213-221`. Read: `plan.md:99` now sends such a line to step 4, `questions.md:46` gives the subject, and `overview.md:35` closes the row with the count. The defect this round found in the subject rule as applied is finding 1.

confirms: round-4#2
The close holds. Read: the script's docstring says "for each failure of the conditions below" (`test_layout.py:61`), its `names` entry states the `self.<name>` and `<module>.<name>` readings, the change one tree's reading alone reaches, the set of distinct definitions and the two limits, and it says "passed the body and fixture conditions". `spec.md:78` states the same readings and limits. `CONTRIBUTING.md:295-297` points at the docstring for the conditions and lists none. Executed: `git grep -n "four conditions\|the other two"` at c97b5f91 over `CONTRIBUTING.md`, `skills`, `agents`, `docs`, `tests` and `bin` finds the verify skill's own term (`skills/verify/SKILL.md:28-30`, `skills/verify/orchestration.md`, `broad_gate.py:2954`) and prose unrelated to the move check, so the collision is gone. `overview.md:69` names the reframe and the two limits. The pinning gap in the new reading is finding 2.

confirms: none
The re-runs reproduce. Executed, run whole at each commit with the script at c97b5f91 copied over the clone's and restored after: groups 29, 34, 37, 45 and 49, and 4e987021's move. Each last line and exit is the one the new column records: 0, 46, 77, 30 and 0 failed, and 5 failed. Claimed: 39 commands print round 3's re-run lines word for word, eight print fewer, and three print one other name. Executed, `python3 moves.py compare`, all 52 read through `moved` with the scripts at 8dd97a30 and c97b5f91: 39 print the same lines; groups 29, 39, 41, 44, 45, 48, 49 and 50, cc391101's command and 099cd54d's lose lines and add none; groups 34, 35 and 37 swap `reasons` for `ROOT`, `disagreements` for `uc`, and `parse` and `OVERVIEW_OPEN` for `rules` and `git`. Every added line names a case in a file that declares no `TARGET`, so no module goes to the mutants by its `TARGET` that round 3 did not send. The framer's correction at c97b5f91 states these names (`questions.md:53`) and the count step 5 now gives (`plan.md:115`).

confirms: none
A sample of the subject mutants gives the verdicts the record gives. Executed, rebuilt from the record's descriptions: op1 (`optin.repo_root` reading a None stdout as text) is red at c97b5f91 on `tests/test_optin.py`, with `AttributeError` at `hooks/optin.py:85`; cp2 (`_corpora` leaving out `TOKEN_CASES`) survives `tests/test_the_old_spellings_reach_the_hook.py` at c97b5f91 and at 95991e42, an old gap; ro1 is red at collection, as finding 1 says. Read: `OPENS_NOTHING` holds two entries (`tests/test_a_shrunken_corpus_declines_to_judge.py:120-128`), so on1 and on2 with on3 at the rewritten key are Q12's default as written. g12 and g15 are rebuilt from group 14's descriptions (`phases/phase-6.md:553-556`), and the rebuilt g12 is red at the head on a case that stands there, so no old column is owed for it; the text of the g12 that group 17's table left alive is not in the tree.

confirms: none
The new rows are each read against their group. Read: `a-name-imported-from-another-test-file` and `a-changed-name-in-another-test-file` each exercise the test-file reading, which no earlier row reaches; the conftest and `shapes_d` rows exercise the other two kinds of module. Executed: the baseline of the `mutants2.py` batch, `Test_moved` at c97b5f91, passes.

confirms: none
The changed modules and the tree checks pass at c97b5f91. Executed in the clone: `python -m pytest tests/test_test_layout.py tests/test_docs_line_wrap.py -q`, 111 passed. `test_layout.py --check` exits 0 with `184 files read, 0 refused, 115 declare no TARGET`. `rules.py --check` exits 0, with all 249 check lines in 62 rule files holding. `unverified_check.py seal/specs/` exits 0.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The other 46 recorded commands run whole with collection, and the subject mutants other than op1, cp2 and ro1. This round read all 52 through `moved` without collection, ran 6 whole, and rebuilt 3 of the 19 fresh mutants | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md` | the sealer |
| CI run 39992218040 at cc420aa0, in flight when this round ended, unverified | `.github/workflows/test.yml` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at c97b5f91, unverified. Nothing is due from this round until findings 1 and 2 are answered | the whole tree | the orchestrator, at the broad gate |
| The directory `s1` that round 4's fix pass left in the answers store under the home directory. This round did not open or remove it | outside the repository | the owner |

## Probes

| Command | Result |
|---|---|
| `git clone --shared` of the branch worktree into `scratchpad/942-r5/clone`, moved between commits; removed after the round with every script below | every run below ran in it |
| `python3 lines.py`, a script outside the tree reading all 52 recorded commands through `moved` with c97b5f91's script, instrumented to report every name apart and where each failing case stands | 34 lines on cases in files that declare no `TARGET`, all name lines; group 34's case finds `ROOT` and `gate` apart and prints `ROOT` |
| `python3 moves.py compare`, the 52 commands through `moved` with the scripts at 8dd97a30 and c97b5f91 | 39 alike; 13 differ, every added line on a case of an undeclared file |
| `python3 moves.py whole 31aed13b a4a113f6 efc3a79f 809408e5 4e987021 5966150b`, each run whole with c97b5f91's script | 0, 0, 30, 77, 5 and 46 failed, each as recorded |
| `python3 mutants.py`: op1, ro1 and cp2 at c97b5f91, and cp2 at 95991e42, through a copy of `mutation_check.py` outside the tree | red; red at collection; SURVIVED; SURVIVED |
| `python3 mutants2.py`: v1 and u2 over `skills/verify/scripts/test_layout.py` against `Test_moved` at c97b5f91, one batch | baseline passes; SURVIVED; SURVIVED |
| `git ls-tree c97b5f91 tests/`, filtered to `.py` entries that are not files | none |
| `python -m pytest tests/test_test_layout.py tests/test_docs_line_wrap.py -q`, `test_layout.py --check`, `rules.py --check`, `unverified_check.py seal/specs/` | 111 passed; exit 0, 115 undeclared; exit 0, 249 lines; exit 0 |
