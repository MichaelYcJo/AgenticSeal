# 1791781864-the-idle-session-rows-ask-nobody — round 2's fix pass

## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| 🟡 1 | fixed | f655e31f |
| 🟡 2 | fixed | e78b8de8 |
| ⬜ 3 | answered | No person is asked in that state. The guard withholds a way on that exists, and the other-clone text hedges (*may be put to a person*). Telling a press given in both clones from a press given in the session's clone alone costs a second transcript read, which S10 forbids, or a reader returning every clone with a press, which is mechanism a fix pass does not add. If #903 makes §B's rows deny under the press read from the session's root, the difference stops mattering |
| ⬜ 4 | answered | corrected at e78b8de8. The policy paragraph is rewrapped, and *a branch already checked out in a worktree needs no switch* now sits under the split's reason alone. The sentence that follows the other-clone sentence says what both reasons share |
| ⬜ 5 | answered | `round_record.py close` measures `New units` from the fix range's top-level names. `unattended_text` is nested inside `main`, so the generator does not bound it, and the test helper `elsewhere` is the top-level name it found. Round 1's fix table names `unattended_text`, and that table is the hand-written account. The record is generated, so it is not hand-edited |

## What the fix range changes

The range is f655e31f..e88a460c.

- **🟡 1.** `unattended_text` picks the sentence that says why the split
  passes from the consent that holds. In the session's own clone the
  sentence is the press's, unchanged byte for byte, so S3, S4 and S7–S11 are
  untouched. In a clone holding this session's creation record it is the
  record's: *This session already created a worktree in this clone, and that
  creation consents to the next one here*. The Korean half says the same.
  `test_a_clone_this_session_already_split_is_named_the_split` now pins the
  record's sentence in both languages, using the reviewer's case.
- **🟡 2 and the class.** I searched every added line of `git diff
  origin/release/v0.21.0...HEAD` for `consent`, `동의`, `pass as written`
  and `그대로 통과`. Every live copy now names the consent that holds in its
  case:
  - **Misattributed, corrected:** the guard's module docstring (the
    only-IDLE row and the *Under the press* paragraph), the case module's
    docstring, the `ways_on` docstring, and changelog item 1.
  - **Incomplete, now name the record clone too:** the policy's §A
    only-IDLE row, both READMEs, and #894's restated S2 and S9.
  - **Already right:** the policy's *Under the press* paragraph, ledger R1
    (it now also names which sentence each clone gets), the code comments
    above `press` and in `unattended_text`, the other-clone text, and
    §*Unknowns resolve conservatively*, which names the press in its own
    clone.
  - **Records left as written:** the round reports and fix tables,
    `phases/phase-2.md`, and the frame's `spec.md` In 2, whose divergence is
    already a row in `overview.md`.
- **Contract changes:** none.
- **New units:** none at the top level. `unattended_text` gained the local
  `here` and `why`. The case was replaced, not added.
- **Removed:** nothing.
- **Survivors:** `survivor-check` named one, changelog item 1's
  no-question sentence. It holds for both reasons and is now a row in
  `survivors.md`.

## Seen red

- **The replaced case** failed against the guard at dc3501c4 (`1 failed, 9
  passed, 1 skipped`) and passes at the head.
- **Through `bin/mutation-check`**, both breaks came back `red`:
  - the why-branch made `if True` turned the record-clone case red;
  - `here` reduced to `bool(own)` turned the another-clone case, S11 and the
    record-clone case red.
