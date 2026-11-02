# Review round 7: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

```seal
target: 96f432ef5, fixes 2f5d5f060..96f432ef5
```

This verifying round read the diff `2f5d5f060..96f432ef5`, the run's last by the orchestrator's judgment row (`frame/plan.md:61`). The diff holds the fix pass over round 6: one test commit (`16e94d923`, `tests/skills/test_passages.py`), that judgment row (`bcd6284fd`), round 6's record (`45b528a25`) and its close block (`96f432ef5`). Round 6 closed its one finding `fixed 16e94d923`, and this round answers it below. Probes ran in a `git clone --no-local` of the main clone at `96f432ef5`, under the round's scratch directory; each mutation went through `bin/seal mutate`, which writes the mutant and restores the file from held bytes. The clone and every output file were removed before hand-back.

Carried as coordinates and not re-established: where the corpus guard lives (`skills/settle/scripts/passages.py#in_corpus`, with `TOP_FILES` and `TOP_DIRS` at `passages.py:29-30`); round 6's `git ls-files` result that no tracked path begins with `docs`, `skills`, `agents` or `templates` followed by a character other than `/`; and round 4's `bin/seal layout --pairs` result that no duplicate pair names `tests/skills/test_passages.py`. The diff renames one case and changes its parameters and adds no test module, so the pairs were not printed again. The handover's account of the four guards, the close's account of its `seal mutate` runs, and the comment above the case were read as claims. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English.

This round confirms round 6's close: each of the four guards has a parameter that goes red under that guard alone widened. It also opens one finding, a `should`, on a `regression:` line. It opens no `must`. The fix pass removed three parameters along with `"docs"`. Those three were what pinned which directories `TOP_DIRS` lists, and two of the three directory additions they held now survive every module that reads the corpus.

## Findings

### 1. The fix dropped the parameters that held `TOP_DIRS`'s list, so a directory added to it survives, and the comment says every widening fails a path

```seal
severity: should
location: `tests/skills/test_passages.py:49-69`
evidence: executed `bin/seal mutate skills/settle/scripts/passages.py --replace ... --tests "bin/test tests/skills/test_passages.py -q -p no:xdist -p no:cacheprovider"`, `bin/seal mutate skills/settle/scripts/passages.py --replace ... --tests "bin/test tests/skills/test_passages.py tests/skills/test_rule_changes.py tests/skills/test_chain_check.py::Test_pins_and_copies_in tests/text/test_no_passage_is_pasted_into_a_second_file.py -q -p no:xdist -p no:cacheprovider"`, `git ls-files tests/*.md hooks/*.md seal/*.md`
regression: round-6#1
```

Why it matters: the unit is `Test_in_corpus::test_refuses_a_path_one_guard_alone_refuses` (`tests/skills/test_passages.py:49-69`), which fix commit `16e94d923` rewrote. The frame's row (`frame/plan.md:61`) asks that each of the four guards get one parameter that guard alone refuses, shown red with that guard alone widened. The fix did that, and it also deleted `"seal/threads/1-x/frame/design.md"`, `"tests/README.md"` and `"hooks/notes.md"`. The defect came from reading "one parameter per guard" as "only one per guard", with the prefix guard widened at one boundary when it has two. The prefix `rel.startswith(TOP_DIRS)` (`passages.py:60`) can widen by losing its slash, which `docs-old/notes.md` now pins. It can also widen by naming one more directory, and design G8 (`frame/design.md:14`) fixes that list as four directories.

Executed in the scratch clone, each mutation alone, over `tests/skills/test_passages.py` at `96f432ef5`:

- `TOP_DIRS` with `"seal/"` added: survived.
- `TOP_DIRS` with `"tests/"` and `"hooks/"` added: survived.

The same two mutants with the test file put back to its `2f5d5f060` version: 2 mutants, 2 red. So the three deleted parameters were not redundant. Each sat outside both sides of the `or`, as `SECURITY.md` and `docs-old/notes.md` do, and each failed under a directory added to the list.

Over the four modules round 6 ran its corpus mutants over, at `96f432ef5`, the `seal/` mutant goes red: six cases of `Test_copies`, `Test_pins_and_copies_in` and the paste test fail, because their planted designs under `seal/threads/` become corpus files. The `tests/` and `hooks/` mutant survives all four modules. Under it, a tracked `.md` under `tests/` or `hooks/` would enter the corpus of the paste test and of the copy notice, and no case would say so.

The comment above the case (`:49-53`) says "widening any one guard fails exactly its path". For the prefix guard, widened by a directory the list does not hold, it fails none. That is a wrong sentence the next fix pass or round reads and acts on. Round 5 and round 6 each acted on the same comment's earlier claim.

It is no `must`. The base had no `Test_in_corpus`, so against the base no pin is lost. The paste test's selection is unchanged (read, `passages.py:52-61`). On this tree the surviving mutant widens nothing: `git ls-files` lists no tracked `.md` under `tests/` or `hooks/` (executed, 0 lines). Which directory gets added is an unbounded domain, so no finite list of parameters closes it. Each parameter pins the one directory it names, and the fix below says so in its comment rather than claim the list whole.

The fix restores the three paths, each with an id, and narrows the header's claim. Read against the guards (`passages.py:57-61`): none of the three is top-level, so the membership mutant (`"/" not in rel`) leaves them refused, and none begins with a listed name, so the slashless mutant does too. Each fails only under its own directory added.

```python
    # One path per guard of `in_corpus`, each refused by that guard alone, so
    # widening a guard at a boundary named here fails exactly its paths.
    # Membership in `TOP_FILES` and the `TOP_DIRS` prefix are the two sides
    # of one `or`, so each is widened at its boundary: membership to every
    # top-level path, the prefix to its directory names without their slash
    # and to a directory it does not list.
    @pytest.mark.parametrize(
        "rel",
        [
            # Under `skills/` and no edition: the `.md` suffix alone.
            "skills/README.txt",
            # Under `docs/`: the `.ko.md` exclusion alone.
            "docs/the-review-record.ko.md",
            # A tracked top-level `.md` outside `TOP_FILES`: membership alone.
            "SECURITY.md",
            # A directory whose name `docs` begins: the prefix's slash alone.
            "docs-old/notes.md",
            # Directories `TOP_DIRS` does not list, one path each: the
            # prefix's list. A directory added to it fails its path; a
            # directory these paths do not name fails none, so they are a
            # sample of the directories outside the list.
            "tests/README.md",
            "hooks/notes.md",
            "seal/threads/1-x/frame/design.md",
        ],
        ids=[
            "the-md-suffix",
            "the-ko-exclusion",
            "top-files",
            "top-dirs-slash",
            "top-dirs-not-tests",
            "top-dirs-not-hooks",
            "top-dirs-not-records",
        ],
    )
    def test_refuses_a_path_one_guard_alone_refuses(self, rel):
        assert not passages.in_corpus(rel)
```

## Confirmations

```seal
confirms: round-6#1
```
What holds: the close `fixed 16e94d923`, on the defect round 6 named. Claimed: the four guards are the `.md` suffix, the `.ko.md` exclusion, `TOP_FILES` membership and the `TOP_DIRS` prefix with its slash, and each guard widened alone fails only its own id. Read off `passages.py:57-61`: the predicate is `rel.endswith(".md")`, then `not rel.endswith(".ko.md")`, then `rel in TOP_FILES or rel.startswith(TOP_DIRS)`, with the tuples at `:29-30`. Those are four guards, and the close names them all. Executed in the scratch clone at `96f432ef5`, one `seal mutate` run per guard over `tests/skills/test_passages.py` with `-rf`:

- `rel.endswith(".md")` replaced by `True`: 1 failed and 15 passed, the failure `[the-md-suffix]`.
- `and not rel.endswith(".ko.md")` removed: 1 failed and 15 passed, the failure `[the-ko-exclusion]`.
- `rel in TOP_FILES` replaced by `"/" not in rel`: 1 failed and 15 passed, the failure `[top-files]`.
- `TOP_DIRS` written without trailing slashes: 1 failed and 15 passed, the failure `[top-dirs-slash]`.

The slash round 6 found unpinned is now held by `docs-old/notes.md` alone, and `"docs"` is gone. The regression the same commit made is finding 1.

```seal
confirms: none
```
What matched: the boundary widening of the two `or` sides is a fair stand-in for removing the guard. For an `or`, removing a side means making it `True`, and with either side `True` the whole `or` is `True`. Both removals then give one function, which admits every `.md` that is no edition, so no parameter can fail under one removal and not the other. Executed in the same batch: `rel in TOP_FILES` replaced by `True` goes red, and `rel.startswith(TOP_DIRS)` replaced by `True` goes red, so a removal is still caught. Narrowing a side to `False` is caught by `test_accepts_a_rule_document` (`:33-47`, read), whose seven paths each need one side. A boundary of each side is therefore the most a refusal case can tell the two sides apart by. The comment at `:49-53` states that reading. Its one overstatement is finding 1, where the prefix has a second boundary.

```seal
confirms: none
```
What matched: the change as code. The ids are four, one per parameter, in the parameters' order (read, `:54-67`). The new name, `test_refuses_a_path_one_guard_alone_refuses`, is cited nowhere in the tree but the case. The old name stands only in the round 5 and round 6 records, which are history (executed, `git grep`). The unmutated module passes, 16 cases, as each `seal mutate` baseline shows (executed). `uvx ruff check` and `uvx ruff format --check` over the file each exit 0 (executed). The judgment row (`frame/plan.md:61`) cites `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, which round 6 found at `:102` (carried).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `96f432ef5`. This round ran one module, the four modules of the corpus mutants and the changed file's lint, so the suite is `unverified`. Finding 1 is open, so its route, which the orchestrator's judgment row sets as `deferred seal/follow-up.md`, comes before the broad run. | the branch at `96f432ef5` | the orchestrator, at `seal gate` after the rounds settle |
| The changed case on the Windows leg | `tests/skills/test_passages.py:49-69` | the pull request's `.github/workflows/test.yml` run |

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate skills/settle/scripts/passages.py` over `tests/skills/test_passages.py -rf`, one run per guard: the suffix to `True`, the edition exclusion removed, `rel in TOP_FILES` to `"/" not in rel`, `TOP_DIRS` without slashes | each run: 1 failed and 15 passed, the failures `[the-md-suffix]`, `[the-ko-exclusion]`, `[top-files]` and `[top-dirs-slash]` in that order |
| `bin/seal mutate` over `tests/skills/test_passages.py`, eight mutants: the four above, `rel in TOP_FILES` to `True`, `rel.startswith(TOP_DIRS)` to `True`, `TOP_DIRS` plus `"seal/"`, `TOP_DIRS` plus `"tests/"` and `"hooks/"` | exit 1: baseline passes; mutants 1 to 6 red, mutants 7 and 8 survived |
| `bin/seal mutate` with mutants 7 and 8 over `tests/skills/test_passages.py`, `tests/skills/test_rule_changes.py`, `tests/skills/test_chain_check.py::Test_pins_and_copies_in` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` | exit 1: baseline passes; mutant 7 (`seal/`) red, mutant 8 (`tests/`, `hooks/`) survived |
| the same, mutant 7 alone with `-rf --tb=no` | 6 failed and 113 passed: `Test_copies::test_accepts_a_run_the_to_shares_with_another_rule_document`, four cases of `Test_pins_and_copies_in`, and `test_no_pair_shares_more_than_it_was_measured_at` |
| `git checkout 2f5d5f060 -- tests/skills/test_passages.py` in the scratch clone, then `bin/seal mutate` with mutants 7 and 8 over that module, then `git checkout HEAD -- tests/skills/test_passages.py` | exit 0: baseline passes; 2 mutants, 2 red. The file swap went through git rather than the `Edit` tool. It restored committed bytes, and `git status --short` was empty after it. |
| `git ls-files 'tests/*.md' 'hooks/*.md' 'seal/*.md'`, counted by top directory | 143 under `seal/`, none under `tests/` or `hooks/` |
| `uvx ruff check` and `uvx ruff format --check` over `tests/skills/test_passages.py`, in the scratch clone | exit 0 both |
