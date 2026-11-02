# Review round 6: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

```seal
target: 2f5d5f060, fixes a83d8c19c..2f5d5f060
```

This verifying round read the diff `a83d8c19c..2f5d5f060` in the main clone at `2f5d5f060`. The diff holds the fix pass over round 5: one test commit (`19004e9a7`, `tests/skills/test_passages.py`), the orchestrator's judgment row (`df25823a9`, `frame/plan.md:60`) and round 5's close block (`2f5d5f060`). Round 5 closed its one finding `fixed 19004e9a7`, and this round answers it below. Probes that changed a file ran in a `git clone --no-local` of the main clone at `2f5d5f060`, in the round's scratch directory, each edit made with the `Edit` tool or `bin/seal mutate` and restored before the next, and the clone was removed before hand-back. Carried as coordinates and not re-established: where the corpus guard lives (`skills/settle/scripts/passages.py#in_corpus`, `TOP_FILES` and `TOP_DIRS` at `passages.py:29-30`), round 5's reading that the tree tracks two top-level `.md` files outside `TOP_FILES`, and round 4's `bin/seal layout --pairs` result that no duplicate pair names `tests/skills/test_passages.py` (the diff changes a parameter and adds no test, so the pairs were not printed again). The handover's statement that each guard widened alone fails exactly one parameter, and the close's account of its own `seal mutate` runs, were read as claims. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English.

This round confirms round 5's close and opens one finding, a `should`. It opens no `must`. The new finding is another parameter of the same refusal case, of the same kind as round 5's: a path two guards refuse, so it goes red under neither removed alone.

## Findings

### 1. The `docs` parameter of the corpus refusal fails under no single guard, and the slash that ends each `TOP_DIRS` prefix is pinned by no case

```seal
severity: should
location: `tests/skills/test_passages.py:61`
evidence: executed `bin/test tests/skills/test_passages.py -q -p no:xdist -p no:cacheprovider -rf`, `bin/test tests/skills/test_passages.py tests/skills/test_rule_changes.py tests/skills/test_chain_check.py::Test_pins_and_copies_in tests/text/test_no_passage_is_pasted_into_a_second_file.py -q -p no:xdist -p no:cacheprovider -rf`, `bin/seal mutate skills/settle/scripts/passages.py --replace ... --tests "bin/test tests/skills/test_passages.py -q -p no:xdist -p no:cacheprovider"`, `git ls-files`
```

Why it matters: the handover claimed that each guard of `in_corpus`, widened alone, fails exactly one parameter of `Test_in_corpus::test_refuses_an_edition_a_record_and_a_file_outside_the_corpus`. The close names two guards, and `passages.py:57-61` holds four: the `.md` suffix, the `.ko.md` exclusion, the `TOP_FILES` membership and the `TOP_DIRS` prefix. Executed, one guard at a time in the scratch clone:

- `rel in TOP_FILES` replaced by `"/" not in rel`: 1 failed, 18 passed, the failure `[SECURITY.md]`.
- the `.ko.md` exclusion removed: 1 failed, 18 passed, the failure `[docs/the-review-record.ko.md]`.
- `rel.endswith(".md")` replaced by `True`: 1 failed, 18 passed, the failure `[skills/README.txt]`.
- `rel.startswith(TOP_DIRS)` replaced by `True`: red (`seal mutate` gives the verdict, not the parameter list).
- `TOP_DIRS` written with no trailing slashes, `("docs", "skills", "agents", "templates")`: `tests/skills/test_passages.py` passes, and so do the four modules round 5 ran its corpus mutant over (122 passed). The mutant survives.

The parameter `"docs"` (`:61`) is refused twice over. It does not end in `.md`, and `"docs".startswith("docs/")` is false (read, `passages.py:58,60`). So it goes red neither with the suffix guard removed nor with the slash dropped. For the suffix, `skills/README.txt` already holds the guard alone, so `"docs"` covers nothing that parameter does not. The slash is the boundary the parameter would naturally pin, and no case pins it. With it dropped, a tracked `.md` under a sibling directory such as `docs-old/` would enter the corpus of the paste test and of the copy notice, and no case would say so.

This is the defect round 5 found in `README.ko.md`, at another parameter of the same list. Round 5 ran the `.ko.md` and `TOP_FILES` mutants and not the suffix or slash ones, so neither round 5 nor the fix pass listed this instance. It takes no `reopens:` line: round 5's finding named `README.ko.md` and the `TOP_FILES` boundary, and both now hold (`## Confirmations`). It takes no `regression:` line: the parameter dates from phase 1 (`29ce13483`, `git blame -L 49,66`), a unit a build phase made.

It is no `must`, for round 5's reasons: `passages.py`'s units moved with their bodies (`trail/phases/phase-1.md:36`), the base's paste test used the same slashed prefixes (`405109767:tests/text/test_no_passage_is_pasted_into_a_second_file.py:73,98`, read), and `Test_in_corpus` is beyond what the design owes. On this tree the mutant widens nothing: no tracked path begins with `docs`, `skills`, `agents` or `templates` followed by a character other than `/` (executed, `git ls-files`, 0 lines). What would ship is a refusal case one of whose parameters pins nothing, the class the sealer withheld on and round 5 held to `should`.

The fix replaces the parameter with a `.md` under a directory that shares the `docs` prefix, so only the slash refuses it. Executed in the scratch clone: with this parameter in place of `"docs"`, the module passes, and the slashless `TOP_DIRS` mutant and the suffix mutant each go red (`seal mutate`, 2 mutants, 2 red). The suffix stays held by `skills/README.txt`.

```python
            "hooks/notes.md",
            # A `.md` under a sibling of `docs/` that shares its name, so
            # only the slash ending each `TOP_DIRS` prefix refuses it.
            "docs-old/notes.md",
        ],
```

## Confirmations

```seal
confirms: round-5#1
```
What holds: the close `fixed 19004e9a7`. Claimed: `README.ko.md` gives its place to `SECURITY.md`, `docs/the-review-record.ko.md` stays as the parameter only the `.ko.md` exclusion refuses, and each guard's mutant fails one parameter. Found: `tests/skills/test_passages.py:52-56` holds the two parameters, each under a comment naming the one guard that refuses it (read). Executed in the scratch clone at `2f5d5f060`, each mutation alone: with `rel in TOP_FILES` replaced by `"/" not in rel`, 1 failed and 18 passed, the failure `[SECURITY.md]`; with `and not rel.endswith(".ko.md")` removed, 1 failed and 18 passed, the failure `[docs/the-review-record.ko.md]`. Under the `TOP_FILES` mutant round 5's finding reported 122 passed, so the top-level boundary of design G8 (`frame/design.md:14`) is now held by a case. Both comments state what the runs show. `SECURITY.md` is a tracked file, and the case does not depend on that: `in_corpus` is a pure function of its argument (read, `passages.py:52-61`), so the case holds wherever the file stands.

```seal
confirms: none
```
What matched: the change as code and the close's lint claim. The test's name, `test_refuses_an_edition_a_record_and_a_file_outside_the_corpus`, still describes its parameters, `SECURITY.md` being a file outside the corpus (read). The unmutated module passes, 19 cases, as the `seal mutate` baselines and the runs above show (executed). `uvx ruff check` and `uvx ruff format --check` over `tests/skills/test_passages.py` each exit 0 in the main clone (executed). The judgment row (`frame/plan.md:60`) cites `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, which stands at `:102` (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `2f5d5f060`. This round ran one module, the four modules of round 5's corpus mutant and the changed file's lint, so the suite is `unverified`. Finding 1 is open, so its route comes before the broad run. | the branch at `2f5d5f060` | the orchestrator, at `seal gate` after the rounds settle |
| The changed case on the Windows leg | `tests/skills/test_passages.py:49-65` | the pull request's `.github/workflows/test.yml` run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_passages.py -q -p no:xdist -p no:cacheprovider -rf`, in the scratch clone with `rel in TOP_FILES` replaced by `"/" not in rel` | exit 1: 1 failed, 18 passed, `[SECURITY.md]` |
| the same, with `and not rel.endswith(".ko.md")` removed | exit 1: 1 failed, 18 passed, `[docs/the-review-record.ko.md]` |
| the same, with `rel.endswith(".md")` replaced by `True` | exit 1: 1 failed, 18 passed, `[skills/README.txt]` |
| `bin/test` over `tests/skills/test_passages.py`, `tests/skills/test_rule_changes.py`, `Test_pins_and_copies_in` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, with `TOP_DIRS` written without trailing slashes | exit 0: 122 passed |
| `bin/seal mutate skills/settle/scripts/passages.py` with five single-guard mutants (the four above and `rel.startswith(TOP_DIRS)` replaced by `True`), over `tests/skills/test_passages.py` | baseline passes; mutants 1, 2, 3 and 5 red, mutant 4 (slashless `TOP_DIRS`) survived |
| the same `seal mutate`, with the slashless `TOP_DIRS` and the suffix mutants only, with `"docs"` replaced by `"docs-old/notes.md"` in the test | baseline passes; 2 mutants, 2 red |
| `git ls-files`, filtered to paths beginning with `docs`, `skills`, `agents` or `templates` and a character other than `/` | 0 lines |
| `uvx ruff check` and `uvx ruff format --check` over `tests/skills/test_passages.py`, in the main clone | exit 0 both |
