# Review round 3: 1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request

```seal
target: 871a937d5, fixes 0fbcf50e7..871a937d5
```

This is a verifying round. Its target is the diff from round 2's record commit 0fbcf50e7 to 871a937d5. The diff holds two commits, c990a5fee and 871a937d5, made after the orchestrator's broad run at 0fbcf50e7 exited 1. It changes `ruff.toml`, `tests/github/test_rules.py` and `tests/skills/test_chain_check.py`. No round has read these units, and round 2 closed no finding, so this round has no close to confirm, and no line here is a `regression:` or a `reopens:` line. No `seal/parity.md` is declared, so the round block holds no `original:` line. `seal/config.md` has no `Record language` row and no `Pact` row, so the record is English and no pact anchor was read.

The account read as claims: the broad run's two failures and their causes, handed over by the orchestrator, and the implementer's report that both fixes were seen red and that the old class name stands only in committed records. Each is checked below. Carried from rounds 1 and 2 and not re-established: `chain_check.py` loads `.github/scripts/rules.py` by path (`skills/code-review/scripts/chain_check.py:131-135`), and the marker `a-check-line-in-a-to-is-read-at-the-pull-request` is what the design's `add` names (`frame/design.md:86`). Every verdict below was reached this round.

## Findings

None. The round opened nothing that holds a defect.

## Confirmations

```seal
confirms: none
```
What matched: `ruff.toml:50` lints `.github/scripts/rules.py` at py39, and that is the whole of what the floor case asked. The orchestrator handed over that `tests/hooks/test_launch.py::Test_module::test_what_runs_before_any_floor_is_linted_at_the_floor` failed at 0fbcf50e7 because `chain_check.py` now loads `rules.py`. The case derives its set from what loads what (`before_any_floor` and `loaded_by`, `tests/hooks/test_launch.py:330-390`, read). It follows each `os.path.join` that ends in a `.py` name, and so it also reaches the three modules `rules.py` loads through `SIBLINGS` (`.github/scripts/rules.py:106-118`, read): `unverified_check.py` and two files under `hooks/lib/`, all already in the table. The list is made by that derivation, not by a search for one wording. The case passes at 871a937d5 (executed). In a scratch clone with the `ruff.toml` line removed, it failed (executed), so the line is what it reads. `uvx ruff check` (ruff 0.17.3) over `rules.py` and the two test files exited 0, and so did `uvx ruff format --check` (executed). The tree's `chain_check.py`, run by the `python3` macOS ships (Python 3.9.6) over the branch checkout with `--worktree`, exited 0 and printed no line for this design. This design holds an `add` whose `to` carries a check line, so that run loaded `rules.py` at 3.9 and read the line (executed). The comment above the table (`ruff.toml:35-42`) states the rule in general terms and names no file, so no sentence there went stale.

```seal
confirms: none
```
What matched: the layout refusals the broad run hit are gone, and the old forms were what it refused. With both test files set back to 0fbcf50e7 in the scratch clone, `bin/seal layout --check` over them exited 1 with three refusals (executed): `Test_refused_lines` has no `test_accepts_` case, it has no `test_refuses_` case, and `Test_check_lines_in_a_to` names no top-level definition of `chain_check.py`. At 871a937d5, `bin/seal layout --check tests` exited 0, with 148 files read and 0 refused (executed). The new class name names a real function: `check_lines_in` is defined at `skills/code-review/scripts/chain_check.py:1081`, and the class at `tests/skills/test_chain_check.py:1816` tests the arm that function holds. The class keeps its eight cases and the `@pytest.mark.rule` marker the design's `add` names, so the rename changes no rule's target. As a rename it owes no new red case. The implementer claimed the old name stands only in committed records. `git grep -n Test_check_lines_in_a_to` lists `trail/phases/phase-1.md:21`, `trail/rounds/round-1.md:21,29,50` and `trail/rounds/round-2.md:20,25,65`, and nothing else (executed). Each describes the commit it was written at. Round 2's probe `-k Test_check_lines_in_a_to` now selects nothing, and a later round that re-runs it should spell the new name.

```seal
confirms: none
```
What matched: the split of `Test_refused_lines` (`tests/github/test_rules.py:700-722`) adds a case that covers what its sibling does not. Read against its group: the refuses case asserts the exact list, lines 4 and 6, so it already shows that the held line `check: held.py` and the near line `Check: x` give no refusal. What the accepts case adds is a held no-target line, `check: none reader: review`, through `refused_lines`. The refuses case has no such line: its no-target line is refused for its comma before the reader is read. A probe settled it (executed). In the scratch clone, `parse` was set to refuse every well-formed `none reader:` line (`.github/scripts/rules.py:204`). The accepts case then failed and the refuses case passed. So the new case pins an edge its group did not pin, and it was seen red, as the implementer claimed. `seal layout --pairs` over the two files named no pair in `Test_refused_lines` or `Test_check_lines_in` (executed). The one pair it named stands in `Test_main` of `tests/github/test_rules.py`, which this diff does not touch, and `git log -S` over `origin/release/v0.28.0..HEAD` shows no commit of this branch adding it (executed). The accepts docstring says `unread_lines` names the last line. Run over the same text, `unread_lines` returned one entry, line 5, `Check: x` (executed). Design *Scope* item 2 (`frame/design.md:38`) says the module "gains one" case for `refused_lines`. It now holds two, and the refuses case still holds the held, refused and near lines the item names. The second case is the pair `CONTRIBUTING.md:244-245` requires of each class, and that document outranks the frame.

```seal
confirms: none
```
What matched: one sentence in the refuses case's docstring reads wrong, and the round judges it no finding. It says "the held line between them and the near line give none" (`tests/github/test_rules.py:710-713`). The held line is line 3, before both refusals at lines 4 and 6, so it is not between them; only the near line, line 5, is. The case asserts the exact list, so the sentence changes nothing a reader would act on. It only reads badly, which by `skills/code-review/SKILL.md` *The record* is no finding.

```seal
confirms: none
```
What matched: the four test modules this diff and its causes touch pass at 871a937d5. `bin/test tests/hooks/test_launch.py tests/skills/test_test_layout.py tests/github/test_rules.py tests/skills/test_chain_check.py -q` gave 333 passed, exit 0 (executed). The two cases that failed in the broad run are among them, and so are `Test_refused_lines` and `Test_check_lines_in`. This is a narrow run, not a seal of the suite.

This round leaves nothing open. What comes due is the orchestrator's broad run, and the sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite beyond the narrow runs above, the repository-wide lint and the format check: `unverified` | the whole tree at 871a937d5 | the orchestrator's broad gate, `seal gate --base origin/release/v0.28.0 --record seal/threads/1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request` |
| That the release note shows this fragment under its `<!-- specs/... -->` marker once, still open in `gaps.md` | `.github/scripts/publish_release_note.py:292` | the tag's workflow at the 0.28.0 release, and the orchestrator reading the published note |

## Probes

The narrow run, the lint and the layout check at the target ran in the main clone at 871a937d5, which the prompt names. Every mutant ran in a `git clone --no-local` of the repository at 871a937d5, under the round's scratch directory at `<work item>/round-3/`. Each mutant was set with the `Edit` tool and undone with `git checkout` of its file. The clone is removed before the hand-back.

| Command | Result |
|---|---|
| `bin/test tests/hooks/test_launch.py tests/skills/test_test_layout.py tests/github/test_rules.py tests/skills/test_chain_check.py -q` | 333 passed, exit 0 |
| `bin/seal layout --check tests` | exit 0; 148 files read, 0 refused |
| `bin/seal layout --pairs tests/github/test_rules.py tests/skills/test_chain_check.py` | one pair, in `Test_main` of `test_rules.py`, which this branch did not add |
| `uvx ruff check` and `uvx ruff format --check` over `.github/scripts/rules.py` and the two test files | exit 0 each |
| the macOS system `python3 -I skills/code-review/scripts/chain_check.py --baseline origin/release/v0.28.0 --root` the main clone `--worktree`, Python 3.9.6 | exit 0; no line for this design; notices for the verifying round, the gate record and the guarantee the chain still owes |
| the `ruff.toml:50` line removed, and `parse` returning a refusal for a well-formed `none reader:` line; `bin/test tests/github/test_rules.py tests/hooks/test_launch.py -q -p no:xdist -k "Test_refused_lines or test_what_runs_before_any_floor_is_linted_at_the_floor"` | 2 failed, 1 passed; the failures are the accepts case of `Test_refused_lines` and the floor case, and the refuses case passed |
| both test files set back to 0fbcf50e7; `bin/seal layout --check tests/github/test_rules.py tests/skills/test_chain_check.py` | exit 1; the three refusals named in the second confirmation |
| `unread_lines` over the accepts case's text, under Python 3.9.6 | one entry, line 5, `Check: x` |
| `git grep -n Test_check_lines_in_a_to`, and `git log -S` for the reported pair over `origin/release/v0.28.0..HEAD` | the seven record lines listed in the second confirmation; no commit |
