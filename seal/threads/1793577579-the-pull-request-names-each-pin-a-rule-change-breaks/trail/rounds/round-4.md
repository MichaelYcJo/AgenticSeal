# Review round 4: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

```seal
target: 8106c68b1, fixes a0dc967db..8106c68b1
```

This verifying round read the diff `a0dc967db..8106c68b1` in the main clone at `8106c68b1`. That diff holds the orchestrator's fold and judgment row (`a10750aea`), the fix commit (`225bd1c6c`) and the fix pass's close blocks (`8106c68b1`). Probes that changed a file ran in a scratch clone made with `git clone --no-local` at `8106c68b1`, removed before hand-back. Carried from rounds 1 to 3 as coordinates and not re-established: the load chain against `ruff.toml` `[per-file-target-version]` (the fix adds no load), the pin half of the S7 replay in `trail/phases/phase-1.md` (the fix touches only the copy reading), and where the reading lives (`chain_check.py#_read_tree`, `#_section_text`, `#pins_and_copies_in`, `rule_changes.py#copies`). The handoff and the fix pass's close blocks were read as claims and checked against the tree below. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English.

This round opens no finding, so it opens no `must`. Each of round 3's two closes holds.

## Findings

None. Each unit the fix pass added or changed was read as code, and each claim of its close was checked; nothing below is a defect.

## Confirmations

```seal
confirms: round-3#1
```
What holds: two `add`s of one passage into two documents are named, one notice at each `to`. Claimed: `pins_and_copies_in` records an `add`'s `to` as `(None, to)`, and `copies` applies all three kinds the parser reads. Found: `chain_check.py:1282-1284` appends `(None, op.new)` for an `add` with a `to`, after the `if taken:` branch at `:1278` that records a `change` and a `remove`. `rule_changes.py:390-397` replaces a found `from` through `subn` and puts a `to` at the document's end where nothing was found to replace, so an `add`'s `to` (no text taken) lands at the end and a `remove` (no `to`) adds nothing. That is the orchestrator's decided answer in `frame/plan.md` *Judgments of the run*, last row. Executed: the three new cases, `Test_copies::test_names_a_run_another_add_of_the_design_puts_in` (`tests/skills/test_rule_changes.py:691`), `Test_copies::test_names_a_run_a_change_puts_in_where_its_from_is_not_yet_there` (`:701`) and `Test_pins_and_copies_in::test_names_a_passage_two_adds_of_one_design_put_in_two_documents` (`tests/skills/test_chain_check.py:2165`), fail with `a10750aea`'s two scripts checked out in the scratch clone (3 failed) and pass at `8106c68b1`. The chain-check case pins both notices whole, each naming the other document with 4 runs. The `seal mutate` count of the close (3 of 3 red) was read, not re-run. Read: the sentences round 3 named now name the `add`: the module docstring (`chain_check.py:96-97`), `pins_and_copies_in`'s docstring, `copies`' docstring, the changelog fragment and design *Scope* item 3 (`frame/design.md:45`, the orchestrator's fold at `a10750aea`). Executed: the copy half of S7, replayed over a worktree at `a92c358b^` once with `a10750aea`'s scripts and once with `8106c68b1`'s, reads the 9 designs of that tree that hold operations and prints the same 5 copy notices under both, from `to` values of three designs, two of them naming `skills/core/SKILL.md`. So the fix changes no pair of the replay, as the close and the handoff claim, and round 3's `## Not judged` row on the replay is answered.

```seal
confirms: round-3#2
```
What holds: this design's own `add` and its `change` of `docs/what-a-script-gates.md` *The checks* no longer share a run. Found: the `change`'s `to` at `frame/design.md:121` now points at `docs/the-review-record.md` *What the check reads at the pull request*, and the `add` that lands there (`:102-104`) lists the four sources not read, so the pointer names a section that holds the list. Executed: the fixed reader over the design as it stood at `a0dc967db` names the copy at `:88` (naming `docs/what-a-script-gates.md`) and at `:121` (naming `docs/the-review-record.md`), 2 runs each. Over the design at `8106c68b1` it prints no line for the design, both in the main clone against `origin/release/v0.28.0` and in the scratch clone against `8d39d6f80`, exit 0 each. So the silence is the fold's and not the reader's, and design S8 (`:73`) holds.

```seal
confirms: none
```
What matched: the fix pass's step past the decided answer, judged against the frame and the settle. Claimed: where a `change`'s `from` is not in the document yet, because another pending design's `to` holds it, its `to` is still put at the end. Found: the step stays inside the `change` kind of the decided answer. After the settle a `change` leaves its `to` in its document whether its `from` stood in the tree or in a pending design's `to`. The design itself records the second case: G3 (`frame/design.md:9`) and S8 (`:73`) say two of its five `from` values stand in #1215's pending `to` values. The step reads no other design's text, so *Scope* Out's item on a `to` sharing a run with another pending design's `to` (`:57`) is not crossed. The settle's behaviour agrees (read): `settle.py`'s dry run reports each operation's `from` as found or not found in the working tree (`skills/settle/scripts/settle.py:37-38`, `#op_line`), and the settling session writes each section as its group's latest decision, so a `from` absent from the tree is a state the settle meets and the `to` still lands. Executed: with the step removed in the scratch clone (round 3's paste-ready `elif put:`, written as `if not taken and put:`), `Test_copies::test_names_a_run_a_change_puts_in_where_its_from_is_not_yet_there` alone fails (1 failed, 23 passed), and the reader over the pre-fold design names only `:121`, so without the step the `add` side of round 3's finding 2 is silent. The code puts the `to` at the end for every `from` it does not find, a stale one included, where `copies`' docstring names the pending-design case it is for. A stale `from` is reported not found by the settle's dry run as well, and a copy notice refuses nothing, so no finding stands on it. *Scope* item 3 and the changelog fragment state the `change` as its `from` replaced by its `to` and do not name this case; `copies`' docstring does.

```seal
confirms: none
```
What matched: each new case against its group. `bin/seal layout --pairs` (exit 0, 129 lines) names no pair in `tests/skills/test_rule_changes.py` or `tests/skills/test_chain_check.py`. The two `Test_copies` cases reach the end-put branch with nothing taken and with a text taken and not found; the mutation above separates them, since only the second goes red. The chain-check case is the only one that reaches `chain_check.py:1282-1284`, which no unit case reaches. No new case covers nothing its group did not already cover.

```seal
confirms: none
```
What matched: the narrow modules and the changed files' lint at `8106c68b1`. Executed: `bin/test -q -p no:xdist tests/skills/test_rule_changes.py tests/skills/test_chain_check.py::Test_pins_and_copies_in tests/skills/test_passages.py` exits 0, 115 passed. `uvx ruff check` and `uvx ruff format --check` over the four changed Python files exit 0.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `8106c68b1`. This round ran narrow modules and the changed files' lint only, so the suite is `unverified`. With this round nothing is open: the orchestrator's broad run comes due, then the sealer's spawn. | the branch at `8106c68b1` | the orchestrator, at `seal gate` after the rounds settle |
| The new cases on the Windows leg | `tests/skills/test_chain_check.py:2165`, `tests/skills/test_rule_changes.py:691`, `tests/skills/test_rule_changes.py:701` | the pull request's `.github/workflows/test.yml` run |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist tests/skills/test_rule_changes.py tests/skills/test_chain_check.py::Test_pins_and_copies_in tests/skills/test_passages.py`, in the main clone | exit 0, 115 passed |
| `.venv/bin/python -m pytest -q -p no:cacheprovider -p no:xdist` over the three new cases, in the scratch clone with `git checkout a10750aea -- skills/code-review/scripts/chain_check.py skills/settle/scripts/rule_changes.py` | 3 failed |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.28.0 --root . --worktree`, in the main clone | exit 0; no line for this design; the owed verifying round, the missing gate record and the missing guarantee named |
| `python3 skills/code-review/scripts/chain_check.py --baseline 8d39d6f80 --root . --worktree`, in the scratch clone with `git checkout a0dc967db --` the design, then with the design at `8106c68b1` | two copy notices for the design, at `:88` and `:121`; then no line for the design |
| `.venv/bin/python -m pytest -q -p no:cacheprovider -p no:xdist tests/skills/test_rule_changes.py::Test_copies tests/skills/test_chain_check.py::Test_pins_and_copies_in`, then the same `chain_check.py` run over the pre-fold design, in the scratch clone with `rule_changes.py:396` edited to `if not taken and put:` | 1 failed, 23 passed (the not-found case); one copy notice, at `:121` only |
| `python3 -I test_tmp_replay.py <code> <worktree at a92c358b^>`, one file in the round's scratch directory, run once with `a10750aea`'s tree from `git archive` and once with the scratch clone at `8106c68b1`, then deleted | 9 designs with operations under both; the same 5 copy notices under both (`diff` empty) |
| `bin/seal layout --pairs`, in the main clone | exit 0; no pair in either changed test module |
| `uvx ruff check` and `uvx ruff format --check` over the four changed Python files | exit 0 both |
