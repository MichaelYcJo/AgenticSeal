# Review round 5: 1793437163-fields-stand-in-marked-blocks

```seal
target: 5c48f349, fixes d764ac37..5c48f349
```

This is a verifying round over `d764ac37..5c48f349`, the repairs that followed a failed broad run at `d764ac37`. The range has four commits. `153afb69` moves the `block` helper into `tests/conftest.py#seal_block`. `b14ad020` merges four classes of `tests/skills/test_chain_check.py` into the classes of the functions their cases call. `dfdc921f` splits the two grader cases of `tests/evals/test_rule_cases.py` in two. `5c48f349` replaces `.test_durations`. Round 4's two findings were closed `fixed` by the orchestrator in the records-only commits `40b53b23` and `40c77f52`. The spawn said they need no answer here. This tree's check, run over a draft of this record, refused it for naming neither `round-4#1` nor `round-4#2`, since every `fixed` close is named by the next record. So this round reads both closes and confirms them below. The work was done in a `git clone --no-local` under the session scratchpad at `5c48f349`. The run's artifact was downloaded under the same round directory.

Facts carried from round 4 without searching again: none bear on this range. Every fact below was established this round.

## Findings

No finding: every part of the range holds, as the confirmations below say.

## Confirmations

```seal
confirms: round-4#1
```
What holds: the close holds (read). `40b53b23` adds the round's sentence, word for word, to the **Compatibility** bullet of `seal/threads/1793437163-fields-stand-in-marked-blocks/changelog.md:12`. The sentence says a pin of `v0.26.0` or older refuses the 0.27.0 records until it moves, and that a pin moved first refuses the labelled records. The same fact goes into `frame/plan.md` *Operational impact*, which the close names on its own `location:` line. The sentence's last claim holds: `skills/implement/scripts/seal.py#pinned` reads the release a workflow's clone line pins. `seal pr-checks` with no argument reports it, and names a pin other than the installed release (`seal.py:34-35`, `:1956-1970`).

```seal
confirms: round-4#2
```
What holds: the close holds (read). `40c77f52` rewrites only the answer cell of the row at `seal/threads/1793437163-fields-stand-in-marked-blocks/gaps.md:12`. The cell now cites round 4's confirmation that `aef89462` only adds fences and reads the same on both checks. Round 4's last confirmation block holds exactly that.

```seal
confirms: none
```
What matched: the shared helper behaves as both copies did (read). At `d764ac37`, `tests/hooks/test_fields.py:23-25` and `tests/skills/test_chain_check.py:73-75` each defined `block(*lines, opener=FENCE + "seal")`, where `FENCE` was three backticks in each module. Each returned the lines joined by newlines between the opener and a closing fence, with a newline after it. `tests/conftest.py#seal_block` has the same signature with its default spelt as three backticks and `seal`, and the same body. Both modules import it under the name `block`, so no call site changed. No other module defined or imports a `block` helper.

```seal
confirms: none
```
What matched: the merges keep every case and every assertion (executed). A Python `ast` comparison of `tests/skills/test_chain_check.py` at `d764ac37` and `5c48f349` keyed each function by its class and its name. It found the same functions on both sides, apart from the removed helper. For each test function, the body without its docstring is identical. The three cases named `test_refuses_a_comment_line_at_its_line` stay in `Test_record_findings`, `Test_guarantee` and `Test_broad_gate`, each with the same body. No merged class gained two functions of one name, which would silently drop one case: 191 keyed functions stand where 192 stood less the helper. None of the four removed classes, nor any class that took their cases, held a member other than its test methods, so no case lost a fixture or a helper.

The one case whose decorators differ is `test_accepts_one_or_more_backticked_coordinates`. The class-level `@pytest.mark.rule("location-touched-by-fix")` of the removed `Test_location_paths` now stands on the function itself in `Test_record_findings`. The `round-record-read-by-label` mark moved with its case into `Test_round_of`. `bin/seal rules --check` exits 0. Each moved case now stands in the class of the function it calls: `record_findings` for the finding and location cases, `round_of` for the confirmation cases, and `Test_module` for the loader case.

```seal
confirms: none
```
What matched: the splits keep every assertion and each case still tests one side (read). `Test_proofer_case::test_accepts_an_open_finding_in_its_block` holds the old case's `contains` and positive search. `test_refuses_labelled_lines_a_bare_heading_and_a_close_alone` holds its three negative searches. `Test_sealer_case.shapes` holds the old loop's setup, including the assertion that the cases equal `SEALER_RUNS`, and yields each case's grader and block. pytest does not collect it, since its name has no `test_` prefix. `test_accepts_the_verdict_in_its_block` holds the `contains` assertion and the search that finds the block. `test_refuses_the_line_outside_a_block_or_another_verdict` holds the line outside a block, the other verdict, the three near words, and the line below a closed block. Both sealer cases iterate `shapes()`, so the count assertion runs in each.

```seal
confirms: none
```
What matched: the new `.test_durations` is the run's artifact, byte for byte (executed). `gh run view 41203186159` names `tests` on `feat/1198-fields-stand-in-marked-blocks` at `dfdc921f`, the parent of `5c48f349`, which changes nothing but this file. So the cases it priced are the cases this tree collects. `gh run download 41203186159 -n test-durations` gave a file of 897683 bytes, and `git cat-file -s 5c48f349:.test_durations` gives the same size. Both files' SHA-256 is `6dca2567...4698a8f`. The file holds 6181 entries, the 6181 cases the run collected, where the old file held 6194. It holds the new node ids, such as `Test_record_findings::test_accepts_each_finding_by_its_blocks` and `Test_sealer_case::test_accepts_the_verdict_in_its_block`, and no id under the removed classes or the old split names. `gh run view --log-failed` shows that each failing job of the run failed on `test_the_durations_file_prices_the_suite` alone: 355 unpriced cases and 368 entries no longer collected.

```seal
confirms: none
```
What matched: the range passes its own checks (executed). `bin/test` over `tests/skills/test_chain_check.py`, `tests/hooks/test_fields.py`, `tests/evals/test_rule_cases.py`, `tests/skills/test_test_layout.py` and `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` gave 375 passed and 2 skipped. `bin/seal layout --check tests` exits 0. `uvx ruff check` over the four changed test files exits 0.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `5c48f349`. This round ran five modules and a lint of four files, and the suite stays `unverified` | the branch at `5c48f349` | the orchestrator, by `seal gate --base <base> --record <item>` |
| The crafter's `seal mutate` runs over the four split cases. This round read that the assertions are unchanged and re-ran no mutant | the crafter's hand-back for `dfdc921f` | the sealer, at the guarantee (contract rule 15) |

## Probes

| Command | Result |
|---|---|
| A Python `ast` comparison of `tests/skills/test_chain_check.py`, `tests/hooks/test_fields.py` and `tests/evals/test_rule_cases.py` at `d764ac37` and `5c48f349`, keyed by class and name, bodies compared without docstrings | the same functions less `block`; no body differs; one decorator moved from class to function; the two split cases' assertions read in their new halves |
| `gh run download 41203186159 -n test-durations` into the round directory, then `shasum -a 256` over it and over `git show 5c48f349:.test_durations` | 897683 bytes each, the same SHA-256 |
| `gh run view 41203186159 --json headSha,conclusion,jobs` and `--log-failed` | head `dfdc921f`; each failing job failed only on the durations case |
| `bin/test tests/skills/test_chain_check.py tests/hooks/test_fields.py tests/evals/test_rule_cases.py tests/skills/test_test_layout.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q` | 375 passed, 2 skipped |
| `bin/seal layout --check tests`, `bin/seal rules --check`, `uvx ruff check` over the four changed test files | exit 0 each |
