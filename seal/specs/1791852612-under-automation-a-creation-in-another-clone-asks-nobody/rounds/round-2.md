# 1791852612-under-automation-a-creation-in-another-clone-asks-nobody — review round 2

| Field | Value |
|---|---|
| Target SHA | d71acaf994b57fd23c917b2d2fa0accfe994983a |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #916 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | none |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 2 of #903, the verifying round, target d71acaf9: the diff of round 1's fixes, `6528e2eb..462e6dd5`. The reviewer was asked whether 🟡 1, 🟡 2 and 🟡 3 are closed; to treat the new case and the `plain_origin` argument `guard_worktree_creation` passes `judge_creation` as a finding surface; and to judge `judge_creation`'s new `Reads:` line against its code. Row 5's hints (#920) were out of scope.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's finding 1 is closed — under the press an unbalanced quote no longer puts `[worktree-ok]` into rows 3 and 4's deny | `hooks/worktree-guard.py:1870` | confirmed | executed (probes 1, 2): the new case passes at `d71acaf9` and fails both parameters with the two `lead` lines put back to `origin` |
| 🟢 | round 1's finding 2 is closed — the tracked-changes row says the shared press and re-issue strings | `hooks/worktree-guard.py:3585` | confirmed | read: the strings are byte for byte the copies they replace; executed (probe 5): a reword of `press_sentence` now fails cases in `tests/test_the_guard_asks_once_per_session.py`, which passed 101 under round 1's reword |
| 🟢 | round 1's finding 3 is closed — both READMEs scope the press's no-question creation to its own clone | `README.md:201` | confirmed | read: row 0 answers every creation in the press's clone; `README.ko.md:198` says the same; no other tracked `.md` carries the old claim |
| 🟢 | `judge_creation`'s `Reads: guess … unknown mixed` is the right class and direction | `hooks/worktree-guard.py:1963` | confirmed | read: it parses the model's command; an untokenizable command is stopped without consent and left silent under it; executed (probe 1): the declaration check passes |
| 🟢 | the `plain_origin` argument breaks no call site | `hooks/worktree-guard.py:1607` | confirmed | read: `judge_creation` is the only caller of `guard_worktree_creation` in hooks and tests |
| ⬜ 5 | the `lead` line's `or origin` fallback is unreachable, and its attended arm survives deletion with every case green | `hooks/worktree-guard.py:1870` | open | executed (probes 3, 4): both mutations leave 268 cases green; behaviour is right in both arms today |
| ⬜ 6 | the policy subsection's `Enforced by:` line does not name the case that holds *names no `[worktree-ok]`* for a command with an unbalanced quote | `docs/worktree-guard-spec.md:558` | open | read: the ledger's S1 row names the case; the subsection's line does not |

## Paste-ready fixes

no paste-ready fix in the report

## Executed probes

| What was run | Result |
|---|---|
| 1. `bin/test` on `tests/test_a_creation_in_another_clone_asks_nobody.py` and `tests/test_a_reader_declares_its_input_class.py`, at `d71acaf9` | exit 0 |
| 2. a `test_tmp_*` probe: both `lead` lines replaced by `lead = origin`, then `test_an_unbalanced_quote_under_the_press_names_no_token`; file restored and its hash checked | exit 1, both parameters failed |
| 3. the same probe: both `lead` lines replaced by `lead = plain_origin or origin` (attended arm dropped), then the new module, `tests/test_worktree_guard.py`, `tests/test_the_guard_asks_once_per_session.py` and `tests/test_the_idle_session_rows_ask_nobody.py` | exit 0, 268 passed, 2 skipped (Windows-only) |
| 4. the same probe: both `lead` lines replaced by `lead = plain_origin if pressed else origin` (fallback dropped), the same four modules | exit 0, 268 passed, 2 skipped |
| 5. the same probe: `press_sentence`'s English reworded, then `tests/test_the_guard_asks_once_per_session.py` and `tests/test_the_idle_session_rows_ask_nobody.py` | exit 1, 30 failed across both, including `test_the_plain_retry_meets_todays_rows` in the first |
| 6. `skills/code-review/scripts/survivor_check.py --range 321e9de1...d71acaf9` with every `seal/specs/*/survivors.md` as `--exempt`, as the broad gate runs it | exit 0, no removed wording standing. Over the fix range alone it lists three press sentences in other hooks; they are those hooks' own strings, and the broad gate does not read that range |
| 7. `bin/test` on `tests/test_a_corrected_sentence_survives_elsewhere.py` | exit 0, 173 passed |
| The broad gate: full suite, repository-wide lint, typecheck | not yet. It is the sealer's. This report leaves nothing needing a fix, so it has come due: the sealer's spawn is next |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `hooks/worktree-guard.py:2008` | round 1's 🟡 1 — fixed |
| round-1 | `hooks/worktree-guard.py:3555` | round 1's 🟡 2 — fixed |
| round-1 | `README.md:201` | round 1's 🟡 3 — fixed |
| round-1 | `seal/ledger/1791852612-under-automation-a-creation-in-another-clone-asks-nobody.md:30` | round 1's ⬜ 4 — open |
| round-1 | `hooks/worktree-guard.py:1892` | round 1's 🟢 — confirmed |
| round-1 | `tests/test_a_creation_in_another_clone_asks_nobody.py` | round 1's 🟢 — confirmed |
| round-1 | `tests/test_a_creation_in_another_clone_asks_nobody.py#test_the_transcript_is_read_at_most_twice_per_creation` | round 1's 🟢 — confirmed |
| round-1 | `tests/test_a_creation_in_another_clone_asks_nobody.py#test_under_the_press_a_creation_row_denies_every_attempt` | round 1's 🟢 — confirmed |
| round-1 | `docs/worktree-guard-spec.md:522` | round 1's 🟢 — confirmed |
| round-1 | `seal/releases/0.21.0.md:748` | round 1's 🟢 — confirmed |
| round-1 | `hooks/worktree-guard.py:95` | round 1's 🟢 — confirmed |
| round-1 | `hooks/worktree-guard.py:1610` | round 1's 🟢 — confirmed |
| round-1 | `hooks/worktree_consent.py` | round 1's 🟢 — confirmed |
| round-1 | `tests/test_a_creation_in_another_clone_asks_nobody.py#test_on_windows_a_creation_in_another_clone_is_row_fours_deny` | round 1's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| under the press in another clone, row 5's hints still name `[worktree-ok]` | issue #920, already deferred before this round; the fix diff did not touch row 5 | the owner, through #920 |
