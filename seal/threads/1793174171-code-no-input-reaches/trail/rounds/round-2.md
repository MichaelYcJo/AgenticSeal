# Review round 2: 1793174171-code-no-input-reaches

target: e1c72f88, fixes 34616bd7..e1c72f88

This round verifies the fix pass and stays inside its diff: `c8b5f382`, which changes `skills/code-review/scripts/chain_check.py` and `gaps.md`, and `e1c72f88`, which writes round 1's two lines for finding 1. Round 1's coordinates were carried and opened again rather than searched for: `finding_of`'s whole-row match, the readers of `f.verdict` and `f.paths`, and the direct-call cases. Round 1's `evidence: executed` line for finding 1 was re-run at `e1c72f88`.

## Findings

None.

## Confirmations

confirms: round-1#1
The close `fixed c8b5f382` holds. Both docstrings drop "which the arm refuses by name", and what each now says matches the tree at `e1c72f88` (read `skills/code-review/scripts/chain_check.py:883-899`, `skills/code-review/scripts/chain_check.py:914-930`).

- `location_of`'s one caller in the tree is `finding_of` (`chain_check.py:1171`). `verdict_of` has two callers: `finding_of` (`chain_check.py:1170`) and `deferred_home` (`chain_check.py:904`). The only callers of `deferred_home` are in `tests/skills/test_chain_check.py`, at `Test_deferred_home` and `Test_issue_of` (executed `git grep -n -e "verdict_of(" -e "location_of(" -e "deferred_home(" -- . ':!seal/threads' ':!seal/process'`).
- `finding_of` hands a reader only a line that `row.shape.fullmatch` matched (`chain_check.py:1135`), so no record reaches either None.
- The cases each docstring names do call the function with values the row refuses (read `tests/skills/test_chain_check.py:743`, `tests/skills/test_chain_check.py:752-754`, `tests/skills/test_chain_check.py:805`). `Test_issue_of` passes `deferred_home` only values the `verdict:` row accepts, so leaving it out of `verdict_of`'s docstring is correct.

Round 1's evidence command was re-run at `e1c72f88`. With the direct-call refusing cases deselected, both mutants still SURVIVED (exit 1), so the branches are still reached only by those cases. The nine readers of `f.verdict` and `f.paths` are unchanged, and none of them handles a None.

`gaps.md` *Not done* now names all three readers and their direct-call cases. It also states the owner's question of whether those cases should call `as_row`, which round 1 left under `## Not judged`.

The sweep the fix pass reported holds (executed `git grep -n -e "refuses by name" -e "refused by name" -e "None, which" -- . ':!seal/threads' ':!seal/process' ':!changelog' ':!CHANGELOG.md'`). It found eleven hits. The answer judged five of them, and those five judgments are right. Of the six it did not name:

- `tests/hooks/test_config.py:1460` restates the same claim as `hooks/lib/config.py:855`, which the answer showed is handled.
- `hooks/dispatch.py:643`, `hooks/lib/implementer.py:76`, `tests/hooks/test_one_heredoc.py:8` and `tests/skills/test_broad_gate.py:2768` describe a value being None, not a refusal of it.
- `chain_check.py:768` matches only because a parameter is named `which`.

None of these claims a refusal that no caller makes. The fix pass changed only the two lines of round 1 that the fix pass owns, `verdict:` and `answer:`, and `c8b5f382` touches the path the finding's `location:` names.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the three None branches that only direct-call cases reach stay, or the cases call `as_row` and the branches go. This question is carried from round 1 and is now stated in `gaps.md` *Not done*. | `skills/code-review/scripts/chain_check.py:883-946` | the repository owner |
| The full suite, the repository-wide lint and the typecheck. This round ran none of them, under contract rule 2. | the whole tree | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the 26 files in `tests/` that `git grep -l -e chain_check` finds, plus `tests/github/test_release_seal.py` | 2059 passed, 9 skipped, exit 0 |
| round 1's finding 1 `bin/seal mutate` command, unchanged, at `e1c72f88` | mutant 1 SURVIVED, mutant 2 SURVIVED, exit 1 |
| `uvx ruff check skills/code-review/scripts/chain_check.py` and `uvx ruff format --check skills/code-review/scripts/chain_check.py` | exit 0 and exit 0 |
| `bin/seal layout --check` | exit 0 |
| `bin/seal rules --check` | exit 0 |

Every probe ran in a `git clone --no-local` at `e1c72f88` under the round's scratch directory. The clone was removed before hand-back.
