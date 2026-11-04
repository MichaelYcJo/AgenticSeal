# Review round 3: 1793769283-each-form-a-script-does-not-decide-on-goes-to-plain-words

```seal
target: c8239c559, fixes ec376aa0c..c8239c559
```

This verifying round read `git diff ec376aa0c..c8239c559` in a `git clone --no-local` checked out at `c8239c559`. That diff holds two commits. `0d84a120b` changes `tests/conftest.py#guarantee_record` and `tests/skills/test_seal_stamp.py#guarantee_text`, and `c8239c559` corrects the rule-19 list of `trail/phases/phase-4.md`. The branch's base is `origin/release/v0.31.1`, which names `c186a59ac`. The `target:` line takes the verifying round's form, as round 2's did. No `seal/parity.md` is declared, and `seal/config.md` holds no `Record language` row, so this record is English.

The repair answers the sealer's withheld verdict in `guarantee.md` at `ec376aa0c`, its ground (1), and no round finding. Round 2 opened no finding and closed none `fixed` or `rejected`, so no `confirms:` line is owed. The two fixtures are units a fix pass changed, so this round read them as code. A defect introduced there would take a `regression: round-2` line, since no finding named the pass. None was found. The round stayed inside the diff. Outside it, it opened every reader of the two fixtures, the guarantee reader they reach (`skills/verify/scripts/seal_stamp.py#_guarantee_read`), the template at HEAD and at `c186a59ac`, and the sibling fixture `tests/skills/test_chain_check.py#guarantee`.

Carried from the sealer's verdict as coordinates and not re-established: where the two fixtures stand (`tests/conftest.py:1562-1568`, `tests/skills/test_seal_stamp.py:1268-1277`), and that phase 4 dropped the same lines from `tests/skills/test_chain_check.py#guarantee` (`trail/phases/phase-4.md:82`). Each was opened again at the target and still stands where the verdict put it. The sealer's verdict and the earlier rounds' verdicts are not carried. No earlier finding is closed `deferred`.

The implementer's account was read as a claim and checked against the tree:

- The account claimed that the three modules using the fixtures pass narrow, 241 passed. `bin/test tests/hooks/test_sealer_stamp_queue.py tests/skills/test_seal_stamp.py tests/test_conftest.py -q` gave 241 passed, exit 0 (executed).
- The account claimed that ruff passes on both files. `uvx ruff check` and `uvx ruff format --check` over the two files each exited 0 (executed).
- `trail/phases/phase-4.md:104` claims that its `git grep -n -E '\| Broad gate \|.*against|Field \| Value'` lists every other hit as a record of the shape before the blocks (C1), `seal/parity.md`'s table, or `noninferiority.py`'s own output. The same grep at the target lists 16 hits (executed). Six are C1 records: `tests/skills/test_broad_gate.py:2005`, `tests/skills/test_chain_check.py:160`, `:559`, `:2863`, `:3079` and `tests/skills/test_seal_stamp.py:1688`. A seventh, `tests/skills/test_seal_stamp.py:1512`, is a gate line of the shape before the blocks that `_newest_run` is shown refusing. Seven are the parity table: `hooks/lib/config.py:1368`, `templates/setup/parity.md:12` and `tests/hooks/test_config.py:493-494`, `:1923`, `:1933`, `:2008`. A fifteenth, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:484`, is "a file whose table is another one" for the language reader. It is the same text that `tests/hooks/test_config.py:493-494` names as `parity.md`'s header, so the parity class covers it. The last is `evals/scripts/noninferiority.py:1014`. The claim holds.
- `trail/phases/phase-4.md:103` now says that `tests/conftest.py:1051-1095` names the `config.md` row. The paragraph's grep includes `Broad gate |`. At the target its hits in `tests/conftest.py` are lines 1051, 1067, 1072, 1081, 1084 and 1095, each a `config.md` row (executed). The claim holds. `tests/conftest.py:681` names "a `Broad gate` row's fixture" without the pipe. It is also the config row, and that grep does not reach it.

## Findings

This round opens no finding.

## Confirmations

What matched: neither fixture now states the guarantee template's removed form. `templates/records/sdd-guarantee.md` at HEAD has no `| Field | Value |` table, and `3114868c1` removed it with its `| Broad gate |` row (read, against `c186a59ac`). `tests/conftest.py:1566-1567` and `tests/skills/test_seal_stamp.py:1275-1276` now write `## Claims re-run` with the template's four column headers, `| Claim | Source | Command | Result |`, and its separator row, and then the verdict blocks. The headers match the template's `:3-6` character for character (read). Neither writes `Broad gate` or `Field | Value` (executed, by the grep above). The changed docstring at `tests/skills/test_seal_stamp.py:1269-1271` describes what the function writes. The unchanged one at `tests/conftest.py:1563-1564`, "its table for people and one verdict block", now describes its one table and one block.

What matched: every case that reads the fixtures still holds what it claims. `guarantee_record` has one reader, `tests/hooks/test_sealer_stamp_queue.py:68`. `guarantee_text` has 21 call sites in `tests/skills/test_seal_stamp.py`, from `:1296` to `:1796` (executed: `git grep -n -E 'guarantee_record|guarantee_text'`). Each reaches the guarantee through `seal_stamp._guarantee_read`, which reads only the `seal` blocks through `hooks/lib/fields.py` (`skills/verify/scripts/seal_stamp.py:1150-1153`, read). It refuses a fence nobody closed and a line opening `<!--`, and a table is prose to it. No case in either module says anything about the table (executed: `grep -n -i -E 'table|Broad gate|for people'` over both modules lists only the fixture's docstring). The case `test_refuses_a_text_the_reader_refuses_or_holding_no_block` (`tests/skills/test_seal_stamp.py:1493-1501`) says that a refused line below reads as no guarantee "though a block above it reads". That still holds, because the fixture still ends with a block that reads, and the case passed in the run above.

What matched: no other statement of the template's old shape stands outside the work item's records. The class was listed by two methods. The first lists every fixture that builds a guarantee's text, found from what writes `guarantee.md` in `tests/` and `evals/scripts/` and from every function named `guarantee*` (executed: `git grep -n -E 'guarantee\.md|GUARANTEE\b'` and `grep -n 'def guarantee'`). That gives `tests/skills/test_chain_check.py:192` (a heading and a block) and `:2684-2697` (both template tables), `tests/hooks/test_fields.py:31-34` (a `| Claim | Result |` table, with no claim to the template's shape), `tests/skills/test_pr_body.py:321` and `:747`, and `tests/evals/test_rule_cases.py:376` and `:385` (a heading and a block), beside the two fixtures repaired here. The pre-block literals `tests/skills/test_seal_stamp.py:1686-1692` and `tests/skills/test_chain_check.py:2862-2865` each say they stand for a record from before #1198 (C1). The second method greps the row's own spellings, `Broad gate` and `Field | Value`, over the tree outside `seal/threads/` and `CHANGELOG.md` (executed). Every `Broad gate` hit is the `config.md` row, the pull request body's `## Broad gate` section (`skills/code-review/scripts/pr_body.py:186`, the sealer scaffolds' bodies, `tests/skills/test_pr_body.py:205`), a C1 gate record, or `tests/behaviour/test_evals_layout.py:130-165`. That last one keeps graders off a `Broad gate` cell the sealer no longer writes, which agrees with the template now. The prose that describes the guarantee's shape, `agents/sealer.md:98-99` and `docs/forms/the-guarantee.md:25`, names "its tables" and "tables for people" and no row (read). A paraphrase in other words, outside both methods, is not reached, so that part is a sample.

One gap is named here and is no finding. Each fixture says it builds a guarantee in the template's shape, but neither writes the template's `## The parties` table or its `# Guarantee: <work-item-id>` heading. The sibling `tests/skills/test_chain_check.py:2684-2697` writes both tables. No reader reads either (the second confirmation above). Neither is a removed form, since D6 kept the parties table (`trail/phases/phase-4.md:35`). So the docstrings at `tests/conftest.py:1563` and `tests/skills/test_seal_stamp.py:1269` claim a little more than the fixture holds, and only the next person to edit the fixture reads them.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD. The account labels them `unverified`, and the label is honest, since it names only the narrow run and the two files' ruff runs, which this round repeated | `gaps.md`, its first row; `trail/gate.md`, whose newest run is `d1642ebe4` and is behind HEAD | the orchestrator, at the broad run after this round |
| The orchestrator's correction to its part of the pull request body, the sealer's ground (2). The body is outside the tree, and this round read no copy of it | the body file | the sealer, at its next run |

This round leaves nothing open. What comes due is the orchestrator's broad run at HEAD, then the sealer's spawn.

## Probes

| Command | Result |
|---|---|
| `bin/test tests/hooks/test_sealer_stamp_queue.py tests/skills/test_seal_stamp.py tests/test_conftest.py -q` at the target | 241 passed, exit 0 |
| `uvx ruff check tests/conftest.py tests/skills/test_seal_stamp.py` and `uvx ruff format --check` over the same two files | exit 0 for each |
| the `git grep -n -E` that `trail/phases/phase-4.md:104` names, over the seven directories it names, at the target | 16 hits, each in the classes listed above |
| `python3 skills/code-review/scripts/chain_check.py --baseline c186a59ac --root <the branch worktree> --worktree` before this record was written | exit 0; the only lines on this work item say that round 2, `trail/gate.md` and `guarantee.md` are behind HEAD, which this round, the broad run and the sealer answer; no notice at `frame/design.md` |
