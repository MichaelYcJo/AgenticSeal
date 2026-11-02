# Review round 5: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

```seal
target: a83d8c19c, fixes 879fc39ae..a83d8c19c
```

This verifying round read the diff `879fc39ae..a83d8c19c` in the main clone at `a83d8c19c`. The diff is one commit, the crafter's repair of two test cases after the sealer withheld at `053e83510` (`guarantee.md`, committed at `879fc39ae`). Round 4 opened no finding and closed none, so no close is owed an answer here. The sealer's withheld reason is the claim this round answers. Probes that changed a file ran in a `git clone --no-local` of the main clone at `a83d8c19c`, in the round's scratch directory, each edit restored with `git checkout` before the next and the clone removed before hand-back. Carried as coordinates and not re-established: where the corpus guard, the window and the take-out live (`skills/settle/scripts/passages.py#in_corpus`, `#WINDOW`, `#words`; `skills/settle/scripts/rule_changes.py#literals`, `#copies`), and round 4's `bin/seal layout --pairs` result that no duplicate pair names either changed module (the diff adds no test, so the pairs were not printed again). The sealer's re-run of `test_accepts_a_to_that_keeps_the_literal_naming_nothing` under `pins` reading no `to` is carried and was not repeated. The handoff's account of the repair, and its statement that the crafter searched the whole class, were read as claims. The crafter's list of the cases it searched was not in this round's prompt, so the sample below is this round's own, built by the method its confirmation names. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English.

This round opens one finding, a `should`. It opens no `must`. Both repaired cases now fail with only the guard each names removed, on a line naming the planted file.

## Findings

### 1. The `README.ko.md` parameter of the corpus refusal fails under no single guard, and the `TOP_FILES` membership it stands beside is pinned by no case

```seal
severity: should
location: `tests/skills/test_passages.py:49-62`
evidence: executed `python -m pytest -q -p no:cacheprovider -p no:xdist tests/skills/test_passages.py`, `python -m pytest -q -p no:cacheprovider -p no:xdist tests/skills/test_passages.py tests/skills/test_rule_changes.py tests/skills/test_chain_check.py::Test_pins_and_copies_in tests/text/test_no_passage_is_pasted_into_a_second_file.py`
```

Why it matters: `Test_in_corpus::test_refuses_an_edition_a_record_and_a_file_outside_the_corpus` is a case of the class the sealer withheld on, one that asserts something is not counted. Its parameter `README.ko.md` (`tests/skills/test_passages.py:53`) is refused twice over by `passages.py:57-61`: it ends in `.ko.md`, and it is not one of `TOP_FILES` (`passages.py:29`). So it goes red under neither guard removed alone. Executed: with only `and not rel.endswith(".ko.md")` removed, the module gives 1 failed and 18 passed, and the one failure is the `docs/the-review-record.ko.md` parameter. `README.ko.md` passes. So the edition guard is pinned by `docs/the-review-record.ko.md` alone, and `README.ko.md` covers nothing that parameter does not.

The guard the parameter would naturally pin is left open. Design G8 (`frame/design.md:14`) states the corpus as the four directories "with `CLAUDE.md`, `CONTRIBUTING.md` and `README.md`". Executed: with `rel in TOP_FILES` replaced by `"/" not in rel`, so that any top-level `.md` is a rule document, `tests/skills/test_passages.py`, `tests/skills/test_rule_changes.py`, `Test_pins_and_copies_in` and the paste test all pass, 122 passed. The tree holds two such files, `SECURITY.md` and `TRADEMARKS.md` (`git ls-files`), so that mutant would widen the paste test's corpus and the copy notice's on this tree, and no case would say so.

The parameter dates from phase 1 (`29ce13483`), and phase 1's seen-red for `tests/skills/test_passages.py` is the collection error against the base (`trail/phases/phase-1.md:23`), which shows every parameter red at once and pins no guard. It is no `must`: S5 and *Scope* item 5 name the chain-check case, which now holds (below), and `passages.py`'s units moved with their bodies, so `Test_in_corpus` is beyond what the design owes. It is a `should` because the release would ship a refusal case one of whose parameters pins nothing, the defect the sealer withheld on, and a corpus boundary of G8 that no case keeps.

The fix replaces the parameter with a top-level `.md` outside `TOP_FILES` and not an edition, so `rel in TOP_FILES` alone refuses it. It goes red under the mutant above, since `in_corpus("SECURITY.md")` is then true (read, `passages.py:57-61` is a pure function of its argument).

```python
        [
            "docs/the-review-record.ko.md",
            # A top-level `.md` outside `TOP_FILES` and no edition, so the
            # membership alone refuses it.
            "SECURITY.md",
            "seal/threads/1-x/frame/design.md",
            "tests/README.md",
            "skills/README.txt",
            "hooks/notes.md",
            "docs",
        ],
```

```seal
verdict: fixed 19004e9a7
answer: Held; the paste-ready fix applied. `README.ko.md` gives its place to `SECURITY.md`, a tracked top-level file outside `TOP_FILES`, and `docs/the-review-record.ko.md` stays as the parameter only the `.ko.md` exclusion refuses, each with a comment saying which guard holds it. Executed with `seal mutate` on `passages.py#in_corpus`: with `rel in TOP_FILES` widened to `"/" not in rel`, only `[SECURITY.md]` failed; with the `.ko.md` exclusion dropped, only `[docs/the-review-record.ko.md]` failed. `tests/skills/test_passages.py` passed (19), and `bin/seal layout --check tests`, `uvx ruff check` and `uvx ruff format --check` each exited 0.
```

## Confirmations

```seal
confirms: none
```
What matched: the repaired Korean-edition case pins design S5. Claimed: the case's `to` is now `New {run} rule.`, red with only the `.ko.md` exclusion removed, failing at the design's `add` into `docs/policy.ko.md`. Found: `tests/skills/test_chain_check.py:2093-2098` plants `skills/planted/SKILL.md` holding `then w0 ... w14 and on.` and an `add` into `docs/policy.ko.md` whose `to` is `New w0 ... w14 rule.`, so the 15 words `w0` to `w14` stand in both as `passages.py#words` reads them (read). `rule_changes.py:380` returns nothing for an operation whose file `in_corpus` leaves out, which is the only guard between that `to` and a notice. Executed: with only `and not rel.endswith(".ko.md")` removed from `passages.py#in_corpus` in the scratch clone, the case fails, and its one extra line is `seal/threads/1791999999-a-work-item/frame/design.md:9`, a copy notice naming `skills/planted/SKILL.md` with 1 run of 15 words. Under the same mutation the case as it stood at `879fc39ae` passes (1 passed), so the sealer's withheld reason held, and the repair is what turns the case red. The docstring's account (`:2088-2091`) matches the run. `trail/phases/phase-1.md:25` still records phase 1's red under "admitting every `.md`". That line is phase 1's history, and the guarantee at `879fc39ae` records why that red was another file's. The red that pins the guard is in the case's docstring and in this record.

```seal
confirms: none
```
What matched: the repaired fourteen-word case pins the window length. Claimed: the parameter built its run from `WINDOW - 1` and now uses 14. Found: `tests/skills/test_rule_changes.py:651-653` gives `("docs/a.md", 14)`, with a comment saying why the number is written out, and the case asserts `copies` names nothing (read). Executed: with `WINDOW = 14` at `passages.py:27` in the scratch clone, `Test_copies` gives 1 failed and 7 passed, the failure being `[fourteen-words]` with the line `('skills/b/SKILL.md', 1, 'w0 w1 ... w13')`. Under the same mutation the parameter list as it stood at `879fc39ae` passes (2 passed). The `[a-korean-edition]` parameter still reads `WINDOW`, which is right for it: it pins the edition guard and needs a run of exactly the window. It failed with only the `.ko.md` exclusion removed (executed, the run in the first confirmation), its line naming `skills/b/SKILL.md`. Under `WINDOW = 14` the chain-check case `test_names_a_copy_at_the_tos_line_and_no_run_of_fourteen` also fails (executed), so the length is now pinned at the unit and at the arm.

```seal
confirms: none
```
What matched: a sample of the class the repair names, cases this branch added that assert something is not named, counted or read, each run with one guard removed and its failing line read. The method: `git diff 405109767..HEAD` over the three modules the work item added cases to, listing every added `def test_`, and keeping those whose assertion is an absence (executed). That lists 13 cases with an absence half: six in `Test_pins_and_copies_in`, four in `tests/skills/test_rule_changes.py`, three in `tests/skills/test_passages.py`. Each run below was one edit in the scratch clone, restored before the next (executed).
- The docstring exclusion of `rule_changes.py#literals` removed: `test_names_a_pin_at_the_froms_line_and_no_docstring_or_three_words` fails on a notice for `tests/test_pinning.py:2`, the docstring; `Test_literals` and the `remove` case fail too (3 failed).
- `LITERAL_WORDS = 3`: the same chain-check case fails on a notice for `tests/test_pinning.py:4`, "the old rule" (3 failed, 112 passed).
- The take-out of `copies`' `gone` ignored for every `from` and `remove`: `test_accepts_a_passage_the_design_moves_naming_no_copy` fails on a notice naming `docs/policy.md`, and `Test_copies::test_refuses_a_run_that_stands_only_in_text_the_design_takes_out` on `('docs/a.md', 4, ...)` (5 failed, 110 passed).
- The heading skip of `passages.py#words` removed: `Test_words::test_refuses_fences_and_headings_and_reads_case_and_backticks_as_no_words` fails on the heading input (1 failed, 26 passed).
- The `.ko.md` exclusion removed, over `tests/skills/test_passages.py`: the `docs/the-review-record.ko.md` parameter fails and `README.ko.md` passes (finding 1).
- The two repaired cases, in the confirmations above.
Of the 13, 9 were run this way. Each failed on a line naming the guard's own input, except the `README.ko.md` parameter. The 4 not run are in `## Not judged`.

```seal
confirms: none
```
What matched: the narrow groups and the changed files' lint at `a83d8c19c`. Executed: `bin/test -q -p no:xdist tests/skills/test_chain_check.py::Test_pins_and_copies_in tests/skills/test_rule_changes.py::Test_copies` exits 0, 24 passed. `uvx ruff check` and `uvx ruff format --check` over the two changed test files exit 0.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The crafter's list of the cases it searched, and whether its method made the class whole (contract rule 12). The list was not in this round's prompt, so this round could not set its sample beside it. | the crafter's hand-back for `a83d8c19c` | the orchestrator, which holds the hand-back |
| The four cases of the class this round did not run with a guard removed: `test_accepts_a_to_that_keeps_the_literal_naming_nothing` (the sealer re-ran it at `053e83510`), the empty-notice half of `test_names_a_test_file_that_does_not_parse_as_not_read`, `Test_pins::test_refuses_a_literal_the_to_keeps_or_nothing_taken` and `Test_windows::test_refuses_a_text_shorter_than_the_window` | `tests/skills/test_chain_check.py`, `tests/skills/test_rule_changes.py:613`, `tests/skills/test_passages.py` | the orchestrator, from the crafter's list, or the sealer's re-run sample |
| The full suite, the repository-wide lint and the typecheck at `a83d8c19c`. This round ran narrow groups and the changed files' lint only, so the suite is `unverified`. Finding 1 is open, so a fix pass and its verifying round come before the broad run. | the branch at `a83d8c19c` | the orchestrator, at `seal gate` after the rounds settle |
| The repaired cases on the Windows leg | `tests/skills/test_chain_check.py:2085`, `tests/skills/test_rule_changes.py:649` | the pull request's `.github/workflows/test.yml` run |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist tests/skills/test_chain_check.py::Test_pins_and_copies_in tests/skills/test_rule_changes.py::Test_copies`, in the main clone | exit 0, 24 passed |
| `.venv/bin/python -m pytest -q -p no:cacheprovider -p no:xdist` over `Test_pins_and_copies_in` and `Test_copies`, in the scratch clone with only `and not rel.endswith(".ko.md")` removed from `passages.py` | 2 failed, 22 passed: the Korean-edition chain-check case (line `design.md:9` naming `skills/planted/SKILL.md`) and `[a-korean-edition]` |
| the same mutation, with `tests/skills/test_chain_check.py` checked out from `879fc39ae`, over the Korean-edition case | 1 passed |
| the same pytest over `Test_copies`, with `WINDOW = 14` | 1 failed, 7 passed: `[fourteen-words]` |
| the same mutation, with `tests/skills/test_rule_changes.py` checked out from `879fc39ae`, over the parametrized case | 2 passed |
| the same pytest over `Test_pins_and_copies_in` and `tests/skills/test_passages.py`, with `WINDOW = 14` | 3 failed, 32 passed |
| the same pytest over `Test_pins_and_copies_in`, `tests/skills/test_rule_changes.py` and `tests/skills/test_passages.py`, once each with: the docstring exclusion of `literals` removed; `LITERAL_WORDS = 3`; `copies` applying only the `gone` entries with no taken text | 3 failed; 3 failed, 112 passed; 5 failed, 110 passed |
| the same pytest over `tests/skills/test_passages.py` and `Test_copies`, with the heading skip of `words` removed | 1 failed, 26 passed |
| the same pytest over `tests/skills/test_passages.py`, with only the `.ko.md` exclusion removed | 1 failed, 18 passed: `[docs/the-review-record.ko.md]`; `[README.ko.md]` passes |
| the same pytest over `tests/skills/test_passages.py`, `tests/skills/test_rule_changes.py`, `Test_pins_and_copies_in` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, with `rel in TOP_FILES` replaced by `"/" not in rel` | 122 passed |
| `uvx ruff check` and `uvx ruff format --check` over the two changed test files | exit 0 both |
