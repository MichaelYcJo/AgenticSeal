# 1791779434-under-automation-the-guard-asks-nobody — round 6 fixes

Fix range: `5356b8a6..8141dbee`. It holds the merge of
`origin/release/v0.21.0` at `1762901d`, 35c0cade's `Reads:` line in
`hooks/worktree-guard.py#main`, the handoff, and fc3a107d's re-read of the
33 ledger rows that line drifted, ahead of the four commits below.

## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| 1 | answered | corrected at 0f1f6efb — the policy paragraph is titled *Why the row's own sentences predict nothing*, so the title no longer covers the index-residue note the deny shares with the `ask`. The six ledger rows hashing `## Decision matrix` were read again against the new title and re-stamped; none of their claims rests on it, and S9's claim now names it |
| 2 | answered | corrected at 8141dbee — `spec.md` §Why's last paragraph says the deny drops every sentence of its own about what git will do and keeps the note as the `ask` has it. Its heading and In 2's say *its own sentences*, and the references to it in `spec.md`, `plan.md` and `questions.md` follow. `overview.md` quotes In 2 as it now reads and names the policy paragraph's new title |
| 3 | answered | corrected at e5ea20f2 — `test_the_press_is_read_from_the_sessions_own_root` pins the whole Korean deny issued through `git -C <repo>`, the report's fenced block. A Korean clause appended only where the command word carries `git -C` turned it red through `mutation-check`. Ledger W2 names the Korean half at 0f1f6efb |
| 4 | answered | corrected at e5ea20f2 — `test_the_deny_carries_the_note_the_ask_carries` puts a force-staged ignored file under the press and asserts the deny carries the attended `ask`'s note line for line, the report's fenced case. `{note}` taken out of the deny's English text turned it red through `mutation-check`. Ledger S1 cites it at 0f1f6efb |

## Fix surface

| Field | Value |
|---|---|
| Contract changes | none |
| New units | `test_the_deny_carries_the_note_the_ask_carries` (depth 1), in `tests/test_the_guard_asks_once_per_session.py`; ⬜ 3's half is added inside an existing case |
