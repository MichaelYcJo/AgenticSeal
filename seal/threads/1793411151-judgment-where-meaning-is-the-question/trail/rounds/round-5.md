# Review round 5: 1793411151-judgment-where-meaning-is-the-question

target: 70a314ec, fixes 228ccb19..70a314ec

This is the verifying round over round 4's fix pass. The range holds
`321c8e58` (finding 1: `chain_check.py` and one case) and `70a314ec` (the
round 4 record's two closing lines). It reads that diff and what the diff
calls. It reads nothing of phases 3 to 5, which are not built.

Carried from round 4, not re-derived: where `unread`, `originals_of`,
`original_of`, `main` and the `item` fixture live, and round 4's grounds for
the class, that a straight-to-the-PR guarantee's `original:` line is owed
only where git carries `seal/parity.md` and the diff leaves `docs/` and
`seal/` (`agents/sealer.md:105-111`). Re-derived this round: the close, by
re-running the new case and its neighbour against three mutants of the fix,
and the fix range's own state, by the three modules round 4 ran. The
repository declares no `seal/parity.md`, so this record holds
no `original:` line.

The round leaves nothing open. What comes due is the orchestrator's: phase
3's build, then the broad run and the sealer's spawn once the rounds
settle.

## Findings

## Confirmations

confirms: round-4#1
The close holds. The fix pass claimed it applied round 4's paste-ready fix
as written. `321c8e58` removes the `if not chained:` block from `unread`
and restores that docstring's text before `b2f0bc30`. It adds
`unread_originals` beside `original_of` and calls it only inside the
`for item in direct:` loop of `originals_of`. That loop runs only after
the config read, the document-roots return and the baseline-SHA return
have each let the read through (`skills/code-review/scripts/chain_check.py:1895-1924`,
read). `main` passes its `notices` list and prints it after the call
(`chain_check.py:2410-2422`, read). The commit touches both paths on
finding 1's location line (executed, `git show --stat`). The round 4 record
changed only in the finding's `verdict:` and `answer:` lines (executed,
`git diff 228ccb19..70a314ec`).

The fix pass's three mutation claims are reproduced in a clone, each by an
`Edit` and restored after (executed). With the code before the fix (the
block back in `unread`, the call in the loop removed), the new case
`test_names_no_original_line_where_none_is_owed` failed at its first
`respelt()` (`tests/skills/test_chain_check.py:2294`), the half with no
migration config. That is the fix pass's seen-red claim. With the naming
placed before the `touches_code` return, the new case failed at its second
`respelt()` (`:2307`), the half with a config and a diff inside the
document roots. With the call in the loop removed,
`test_refuses_a_direct_guarantee_whose_only_original_is_misspelt` failed at
`:2232` with `[] == [...]`. Each mutant failed one of the two cases and
passed the other. So each member of round 4's class has a case that fails
when the naming leaks into it, and the migration case keeps its one
`not read:` line.

confirms: none
The new case is read against its group, `Test_originals_of`. Its neighbour
`test_a_direct_guarantee_owes_nothing_for_the_document_roots_alone` builds
the same docs-only branch and asserts only the exit code. No case of the
group asserted that no `not read:` line is printed, so the new case covers
what its group did not (`tests/skills/test_chain_check.py:2249-2307`,
read). `seal layout --pairs` names no pair in the module (executed).

confirms: none
No other text stands on the old naming. `git grep` for the old docstring's
words ("not chained") finds them only in the round 3 and round 4 records
and in the new case's docstring, which names the old code it was seen red
against (executed). No document under `docs/`, `agents/` or `skills/`
states where the check names a guarantee's near `original:` line
(executed, `git grep` for "opens like" and `Original: <sha>`). The module
docstring's naming paragraph now names `unread_originals`
(`chain_check.py:65-71`, read).

confirms: none
The fix range passes. `bin/test` over `tests/skills/test_chain_check.py`,
`tests/skills/test_seal_stamp.py` and
`tests/behaviour/test_the_sealer_guarantees.py` at `70a314ec` passed, 435
cases, as the fix pass reported. `ruff check` and `ruff format --check`
over the two changed code files exited 0 (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch, labelled `unverified` in `gaps.md` | the branch at `70a314ec` | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the rounds settle |
| How GitHub renders the `::notice` `not read:` lines, carried from round 3 | `skills/code-review/scripts/chain_check.py:2421-2422` | the orchestrator, at the first CI run of the pull request |
| Departure d of phase 2 still says a guarantee's near `original:` line is not named, while the code names it where the original arm reads the guarantee; a fix pass writes no phase record, and phase 3's crafter reads phase records and not round records | `seal/threads/1793411151-judgment-where-meaning-is-the-question/trail/phases/phase-2.md:58-63` | the orchestrator, in the phase 3 spawn prompt |
| Departure e: a near `## Rule Changes` heading has no path into `unread` yet, carried from round 4 | `skills/code-review/scripts/chain_check.py:774` | the round that reads phase 3 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_chain_check.py -q -k Test_originals_of`, in a `git clone --no-local` at `70a314ec` under the scratchpad | 12 passed, exit 0 |
| The new case and the misspelt-original case by `-k`, `-p no:xdist`, with the pre-fix code restored by `Edit` (block back in `unread`, call in the loop removed), then restored | 1 failed, the new case at `test_chain_check.py:2294`; 1 passed (round-4#1) |
| The same two cases with the naming placed before the `touches_code` return in `originals_of`, then restored | 1 failed, the new case at `test_chain_check.py:2307`; 1 passed (round-4#1) |
| The same two cases with the call in the loop removed, then restored | 1 failed, the misspelt-original case at `test_chain_check.py:2232`, `[] == [...]`; 1 passed (round-4#1) |
| `bin/test tests/skills/test_chain_check.py tests/skills/test_seal_stamp.py tests/behaviour/test_the_sealer_guarantees.py -q`, same clone, `git diff --quiet` exit 0 before it | 435 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over `chain_check.py` and `test_chain_check.py`, same clone | exit 0 and exit 0 |
| `bin/seal layout --pairs`, same clone | no pair names a case of `tests/skills/test_chain_check.py` |
