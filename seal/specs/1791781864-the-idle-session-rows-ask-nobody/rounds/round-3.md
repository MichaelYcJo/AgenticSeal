# 1791781864-the-idle-session-rows-ask-nobody — review round 3

| Field | Value |
|---|---|
| Target SHA | a2d7b4a25498c479efdfb15e09714e3a4631de35 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #902 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | `ae982e7baf1dcdd01097718f6a97d073a8eafe9b..d40e523fb1c50dbe3db0a15cd3e4dcb53f99d10f`, 2 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 3 of #896, the last round of the run, target a2d7b4a2. Round 2 spent the one reopening and recorded `Fix of a fix | first`. It was asked to verify round 2's fixes (dc3501c4..e88a460c) — that `unattended_text`'s reason names the consent that holds in each case and that every consent sentence in the branch diff says what holds — and to confirm the own-clone text is still #894's `PRESS` byte for byte and S10's transcript-read counts are unchanged.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | three prose lines the run wrote break short: the policy's *Under the press* paragraph at line 624, which round 2's note 4 was answered as rewrapped, the guard's module docstring, and changelog item 1 | `docs/worktree-guard-spec.md:624` | answered | corrected at 65e8479c — rewrapped `docs/worktree-guard-spec.md` §*Choice sites* *Under the press*, the guard's module docstring *Under the press* paragraph and changelog item 1. No word changed, which `git diff -w --word-diff` confirms by printing no changed word. d40e523f re-stamped the two ledger rows the rewrap drifted, S13 and the T2 re-read, after reading them; read; enumerated over the branch's added prose lines; also `hooks/worktree-guard.py:94` and the item's `changelog.md:17` |
| 🟢 | round 2's yellow 1 is closed — the record clone's reason names the record as the consent, and the own clone's names the press | `hooks/worktree-guard.py:3155` | confirmed | executed (probe 1): head against `dc3501c4` identical in four states; in the record clone only the why-sentence differs; the named creations get `allow` naming the record. Both mutations of the why-branch turned cases red |
| 🟢 | round 2's yellow 2 is closed — every consent sentence in the branch diff says what holds | `hooks/worktree-guard.py:27` | confirmed | read: 92 matching added lines in 14 files, enumerated and classed; §*Unknowns* is incomplete but true |
| 🟢 | round 2's note 3 is answered as stated | `hooks/worktree-guard.py:3198` | confirmed | read: the other-clone text hedges and is untouched by the fix range; nobody is asked |
| 🟢 | round 2's note 4 is answered for the attribution — the no-switch clause sits under the split's reason alone | `docs/worktree-guard-spec.md:618` | confirmed | read; the wrap half is ⬜ 1 |
| 🟢 | round 2's note 5 is answered as stated | `seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds/round-2.md` | confirmed | read: `New units` is none for a range that adds only locals in a nested function |
| 🟢 | the own-clone text is byte for byte unchanged and carries #894's `PRESS` | `hooks/worktree-guard.py:3158` | confirmed | executed (probe 1): own clone, linked worktree and own clone with a record identical to `dc3501c4`, both rows, both languages; `ways_on` body AST-identical |
| 🟢 | S10's transcript-read counts are unchanged | `tests/test_the_idle_session_rows_ask_nobody.py#test_the_press_is_read_at_most_once_per_command` | confirmed | executed: source-identical at `57f46c5f`, `dc3501c4` and the head, and passes |
| 🟢 | the ledger rows the fix range wrote or re-stamped resolve | `seal/ledger/1791781864-the-idle-session-rows-ask-nobody.md` | confirmed | executed: `evidence-check --ledger` 27, 39 and 239 ok, 0 drifted or broken, on this item's, #894's and #868's fragments |
| ❓ | on Windows, with nothing stubbed, a switch under the press is row 2's deny (M2) | `tests/test_the_idle_session_rows_ask_nobody.py` | ❓ out of verified scope | skipped off Windows, and this round ran on darwin; the test workflow's Windows legs answer it at the pull request |

## Paste-ready fixes

```
A switch into another clone is refused under the press as well, and its reason
names no split, because a creation there is not consented and §B's rows would
put it to a person. Both reasons name no question tool and no
`[shared-tree-ok]`, and say re-issuing the command unchanged meets the same
refusal. The press is read by the stop's reader, against the session's own
root, and only where one of the two rows fires, so a command reads the
transcript at most once. No marker is written, because the marker means *the
question was put* and none was: a session whose person later answers `per axis`
in the same clone meets the first-attempt deny an attended session meets. The
token reads as it did, so `[shared-tree-ok]` still turns both rows silent under
the press; the reason does not name it, and a model that appends it anyway
leaves that on the command line. In the clone the press was given in, the
creation direction's two sites never run under the press, because consent is
read before them. Without the press both rows are what they were, word for
word.
```
```
Under the press -- this session's person pressed `automation` on the
routing question -- nobody is there to put the two options to, so the switch
direction's two sites deny on every attempt. Where a creation in the
switch's clone is consented -- by that answer in the clone it was given in,
or by this session's record in a clone it already created a worktree in --
the reason names the way on that needs nobody: split into a worktree and
work there by path. A switch into another clone is refused naming no split,
because the creation rows there would put it to a person. The reason names
no question tool and no token, and no marker is written, because no question
was put (#896). In the clone the press was given in, the creation
direction's two sites never run under the press: consent is read first.
```
```
     is refused without one, because a split there would be put to the
     person. It names no question tool and no `[shared-tree-ok]`, and says
     that re-issuing the switch unchanged meets the same refusal.
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test -q -p no:cacheprovider` over `tests/test_the_idle_session_rows_ask_nobody.py`, `tests/test_worktree_guard.py`, `tests/test_the_guard_asks_once_per_session.py`, `tests/test_a_reader_declares_its_input_class.py`, `tests/test_a_folded_statement_names_what_enforces_it.py`, `tests/test_docs_line_wrap.py`, `tests/test_no_real_identifiers.py`, `tests/test_one_word_one_meaning.py`, in the clone at `a2d7b4a2` | 434 passed, 1 skipped (the Windows-only M2 case), exit 0 |
| probe 1, a temporary test file with `dc3501c4`'s guard loaded beside the head's, both rows, both languages: own clone, linked worktree, own clone with a record, another clone without and then with a record, and the two creation forms in the record clone | 4 passed. Head and base are identical in the first four states, and each own-clone reason carries `PRESS[lang]` between blank lines. In the record clone, head equals base with the why-sentence swapped. Both creations `allow`, naming the record. The file, the base copy and pytest's run directory were deleted |
| why-branch mutated to `if True`, then `if False`, in the clone's guard, each restored with `git checkout` | `if True`: `test_a_clone_this_session_already_split_is_named_the_split` red (1 failed). `if False`: both `test_under_the_press_a_choice_row_denies_every_attempt` rows, `test_a_creation_on_the_same_line_is_stopped_with_it` and `test_the_plain_retry_after_the_stop_meets_the_deny` red (4 failed) |
| AST compare of the case module's functions at `57f46c5f`, `dc3501c4` and the head | S10's case, `situation`, `unattended` and the other-clone helper identical; the `ways_on` body identical with its docstring removed |
| `bin/evidence-check --ledger` on this item's fragment, #894's, and #868's | 27 ok, 39 ok, 239 ok; 0 drifted, 0 broken; records arm 13 work items read, 0 refused, 0 drifted |
| the clone's `git status --short` before removal | empty |
| broad gate (full suite, lint, typecheck) | not yet: no run made by anyone; it is the sealer's, and it has come due with this report |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `hooks/worktree-guard.py:3125` | round 1's 🔴 1 — fixed |
| round-1 | `hooks/worktree-guard.py:1474` | round 1's 🟡 2 — fixed |
| round-1 | `docs/worktree-guard-spec.md:974` | round 1's 🟡 3 — fixed |
| round-1 | `hooks/worktree-guard.py:3137` | round 1's ⬜ 4 — answered |
| round-1 | `seal/specs/1791781864-the-idle-session-rows-ask-nobody/handoff.md` | round 1's ⬜ 5 — answered |
| round-1 | `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` | round 1's ⬜ 6 — answered |
| round-1 | `hooks/worktree-guard.py:3122` | round 1's 🟢 — confirmed |
| round-1 | `hooks/worktree-guard.py#choose` | round 1's 🟢 — confirmed |
| round-1 | `hooks/worktree-guard.py#main` | round 1's 🟢 — confirmed |
| round-1 | `seal/specs/1791781864-the-idle-session-rows-ask-nobody/spec.md` | round 1's 🟢 — confirmed |
| round-1 | `docs/worktree-guard-spec.md:769` | round 1's 🟢 — confirmed |
| round-1 | `tests/test_the_idle_session_rows_ask_nobody.py` | round 1's ❓ — out of verified scope |
| round-2 | `hooks/worktree-guard.py:3157` | round 2's 🟡 1 — fixed |
| round-2 | `hooks/worktree-guard.py:27` | round 2's 🟡 2 — fixed |
| round-2 | `hooks/worktree-guard.py:3181` | round 2's ⬜ 3 — answered |
| round-2 | `docs/worktree-guard-spec.md:620` | round 2's ⬜ 4 — answered |
| round-2 | `seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds/round-1.md` | round 2's ⬜ 5 — answered |
| round-2 | `hooks/worktree-guard.py:3149` | round 2's 🟢 — confirmed |
| round-2 | `hooks/worktree-guard.py:1479` | round 2's 🟢 — confirmed |
| round-2 | `docs/worktree-guard-spec.md:981` | round 2's 🟢 — confirmed |
| round-2 | `tests/test_the_idle_session_rows_ask_nobody.py#ways_on` | round 2's 🟢 — confirmed |
| round-2 | `hooks/worktree-guard.py:3135` | round 2's 🟢 — confirmed |
| round-2 | `tests/test_the_idle_session_rows_ask_nobody.py#test_the_press_is_read_at_most_once_per_command` | round 2's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
