# Round 3 report — 1791781864-the-idle-session-rows-ask-nobody (#896)

| Field | Value |
|---|---|
| Target | `fix/896-the-idle-session-rows-ask-nobody` at `a2d7b4a2`; fix range `dc3501c4..e88a460c`; base `origin/release/v0.21.0` at `34fc36e9` |
| Kind | verifying round over round 2's fixes, the last round of the run (round 2 spent the reopening) |
| Where it ran | a `git clone --no-local` of the worktree at `a2d7b4a2`, under `<scratchpad>/1791781864-the-idle-session-rows-ask-nobody/round-3/clone`, removed at handover |
| Ran by | specseal:warden on claude-opus-5-5 |

Carried from rounds 1 and 2 as coordinates, not verdicts: the press is read
at the session's own root (`hooks/worktree-guard.py#automation_pressed`) and
is consent only in the clone it was given in
(`hooks/worktree_consent.py#automation_answered`, condition 4); this
session's creation record is consent in the clone it sits in
(`hooks/worktree_consent.py#granted`). `hooks/worktree_consent.py` and
`tests/test_the_guard_asks_once_per_session.py` are untouched by the fix
range (`git diff --stat` empty), so those coordinates still hold.

## Round 2's findings, each answered

- **Round 2's yellow 1 is closed.** The fix pass claimed `unattended_text`
  now picks the why-sentence by the consent that holds: the press's
  sentence where the switch's tree is in the session's own clone, and the
  record's sentence where only this session's record consents. The code at
  `hooks/worktree-guard.py:3155` does that. `here` is the old clone test,
  and `why` is the press's sentence when `here` is true and the record's
  otherwise. I compared the head guard with the guard at `dc3501c4`, loaded
  side by side, in both rows and both languages (executed, probe 1). Four
  states gave identical decisions and reasons: the session's own clone, a
  linked worktree of it, the own clone with this session's record in it, and
  another clone without a record. In another clone holding the record, the
  head's reason equals the base's with the press's why-sentence replaced by
  the record's, and nothing else differs. The creation that reason names in
  that clone, in both forms, gets `allow`, and its reason says *A worktree
  creation already ran in this repository this session*. So the new
  sentence and the creation's own reason now agree.
  `test_a_clone_this_session_already_split_is_named_the_split` pins the
  record's sentence in both languages. I mutated the branch both ways.
  `if True` (always the press's sentence) turned that case red.
  `if False` (always the record's sentence) turned four own-clone cases red
  (executed).
- **Round 2's yellow 2 is closed.** I enumerated the class by construction.
  I took every added line of `git diff 34fc36e9...HEAD`, outside this
  item's `rounds/`, that matches `consent`, `동의`, `pass as written`,
  `그대로 통과`, `that answer` or `그 답`. There were 92 lines in 14 files.
  I read each line that states which consent holds where:
  - **Names what holds:** the guard's module docstring (the only-IDLE row,
    lines 27–29, and the *Under the press* paragraph, lines 90–92), the
    code comments above `press` and in `unattended_text`, the case module's
    docstring (lines 11–14), the `ways_on` docstring, policy §A's IDLE row
    (`docs/worktree-guard-spec.md:20`), the *Under the press* paragraph
    (lines 614–618), changelog item 1, #894's S2 and S9, and ledger R1.
  - **Incomplete but true:** §*Unknowns resolve conservatively*
    (`docs/worktree-guard-spec.md:779`) names only the press in its own
    clone. It is about Windows switches in the session's own clone, so
    nothing in it is false.
  - **Not about this attribution:** `hooks/worktree-guard.py:1527` (the
    creation ladder), ledger S8 and S12, #868's re-stamped rows, the other
    clone's text and the case docstrings that describe it.
  - **Records left as written:** `spec.md`, `plan.md`, `questions.md` and
    `phases/phase-2.md`. Their divergence is the row *the split's consent in
    another clone* in `overview.md`, which names both consents correctly.

  Both READMEs now say the way on is named in the clone the answer was given
  in, or in one this session already created a worktree in. Neither says
  which consent makes the commands pass, so neither misattributes it (read).
- **Round 2's note 3 is answered as stated.** The other-clone text still
  hedges (*a split of it may be put to a person*), the fix range does not
  touch it, and nobody is asked in that state. The grounds about a second
  transcript read hold: `unattended_text` reads no transcript, and S10
  counts the reads (read).
- **Round 2's note 4 is answered in part.** The attribution half is done.
  *A branch already checked out in a worktree needs no switch* now sits
  under the split's reason alone (`docs/worktree-guard-spec.md:618–619`).
  The other-clone text does not carry that clause, and the sentence after it
  says what both reasons share (read; probe 1 showed the other-clone text).
  The claim that the paragraph was *rewrapped* is not quite true:
  line 624 still breaks after 29 characters. That is ⬜ 1 below.
- **Round 2's note 5 is answered as stated.** `unattended_text` is nested in
  `main`. Round 2's record writes `New units | none` for a fix range that
  added only locals inside it, which is consistent with the fix pass's
  account of the generator (read).

## What the prompt asked to confirm

- **The own-clone text is byte for byte unchanged, and it is still #894's
  `PRESS`.** Probe 1 compared the head guard with `dc3501c4`'s in the own
  clone, in a linked worktree of it, and in the own clone with a record
  present. The reasons were identical in both rows and both languages, and
  each carries `PRESS[lang]` between blank lines (executed). The `ways_on`
  body is AST-identical at `dc3501c4` and at the head. Only its docstring
  changed (executed). The `if False` mutation above shows the own-clone
  cases pin the press's sentence.
- **S10's transcript-read counts are unchanged.**
  `test_the_press_is_read_at_most_once_per_command` is source-identical at
  `57f46c5f`, `dc3501c4` and the head (executed: AST segment compare). It
  passes at the head (executed). The fix adds `here` and `why`, which call
  `_clone_of` and `granted`. Neither calls `automation_answered` (read).
- **#903 is not re-raised.**

## Findings

### ⬜ 1 — three prose lines the run wrote still break short, one of them in the paragraph round 2 said was rewrapped

`docs/worktree-guard-spec.md:624` (*refusal. The press is read by*, 29
characters, followed by a full line), `hooks/worktree-guard.py:94` (*work
there by path. A switch into*, 33 characters, in the module docstring's
*Under the press* paragraph), and
`seal/specs/1791781864-the-idle-session-rows-ask-nobody/changelog.md:17`
(*person. It names no question tool and*, 42 characters with its indent).

I found them by construction. I searched every added line of the branch
diff in the guard, the case module, the policy and the changelog for a prose
line under 45 characters that is followed by a full prose line. Those three
are the only hits. The rest are code. The behaviour and every stated fact
are right. Each is a sentence that reads badly, so ⬜, and
`tests/test_docs_line_wrap.py` does not read these widths. The changelog's
line is the one that reaches the release note. Rewrapping line 17 leaves
the words of the sentence `survivors.md` quotes unchanged, but
`survivor-check` should be run again after it.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | three prose lines the run wrote break short: the policy's *Under the press* paragraph at line 624, which round 2's note 4 was answered as rewrapped, the guard's module docstring, and changelog item 1 | `docs/worktree-guard-spec.md:624` | open | read; enumerated over the branch's added prose lines; also `hooks/worktree-guard.py:94` and the item's `changelog.md:17` |
| 🟢 | round 2's yellow 1 is closed — the record clone's reason names the record as the consent, and the own clone's names the press | `hooks/worktree-guard.py:3155` | confirmed | executed (probe 1): head against `dc3501c4` identical in four states; in the record clone only the why-sentence differs; the named creations get `allow` naming the record. Both mutations of the why-branch turned cases red |
| 🟢 | round 2's yellow 2 is closed — every consent sentence in the branch diff says what holds | `hooks/worktree-guard.py:27` | confirmed | read: 92 matching added lines in 14 files, enumerated and classed; §*Unknowns* is incomplete but true |
| 🟢 | round 2's note 3 is answered as stated | `hooks/worktree-guard.py:3198` | confirmed | read: the other-clone text hedges and is untouched by the fix range; nobody is asked |
| 🟢 | round 2's note 4 is answered for the attribution — the no-switch clause sits under the split's reason alone | `docs/worktree-guard-spec.md:618` | confirmed | read; the wrap half is ⬜ 1 |
| 🟢 | round 2's note 5 is answered as stated | `seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds/round-2.md` | confirmed | read: `New units` is none for a range that adds only locals in a nested function |
| 🟢 | the own-clone text is byte for byte unchanged and carries #894's `PRESS` | `hooks/worktree-guard.py:3158` | confirmed | executed (probe 1): own clone, linked worktree and own clone with a record identical to `dc3501c4`, both rows, both languages; `ways_on` body AST-identical |
| 🟢 | S10's transcript-read counts are unchanged | `tests/test_the_idle_session_rows_ask_nobody.py#test_the_press_is_read_at_most_once_per_command` | confirmed | executed: source-identical at `57f46c5f`, `dc3501c4` and the head, and passes |
| 🟢 | the ledger rows the fix range wrote or re-stamped resolve | `seal/ledger/1791781864-the-idle-session-rows-ask-nobody.md` | confirmed | executed: `evidence-check --ledger` 27, 39 and 239 ok, 0 drifted or broken, on this item's, #894's and #868's fragments |
| ❓ | on Windows, with nothing stubbed, a switch under the press is row 2's deny (M2) | `tests/test_the_idle_session_rows_ask_nobody.py` | ❓ out of verified scope | skipped off Windows, and this round ran on darwin; the test workflow's Windows legs answer it at the pull request |

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

Nothing new is deferred. #903 still holds §B's creation rows under a press
read from the session's root, and this round does not re-raise it.

## Paste-ready fixes

### ⬜ 1

`docs/worktree-guard-spec.md`, replace lines 620–634 (from *A switch into
another clone* to *word for word.*). The `Enforced by:` line below is
unchanged.

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

`hooks/worktree-guard.py`, module docstring, the *Under the press*
paragraph (lines 88–99):

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

`seal/specs/1791781864-the-idle-session-rows-ask-nobody/changelog.md`,
lines 16–19:

```
     is refused without one, because a split there would be put to the
     person. It names no question tool and no `[shared-tree-ok]`, and says
     that re-issuing the switch unchanged meets the same refusal.
```

Needs a fix: no

Loses a record or crashes: no

The broad gate has come due. Nothing this round found needs a fix. ⬜ 1
is a correction the smith may take or answer, and it changes no behaviour.
What comes due is the sealer's spawn.

## Proof block

Files opened in this round, at `a2d7b4a2` unless named otherwise:

- `seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds/`: `round-1.md`, `round-1-fixes.md`, `round-2.md`, `round-2-report.md`, `round-2-fixes.md`; `overview.md` (the divergence row), `changelog.md`, `survivors.md` (the fix diff)
- `hooks/worktree-guard.py`: the fix diff whole; module docstring lines 18–32 and 84–104; `main` lines 3100–3260; the same file at `dc3501c4`, loaded in probe 1
- `hooks/worktree_consent.py`: `consent_path` tail, `granted`, `main`
- `tests/test_the_idle_session_rows_ask_nobody.py` lines 25–240 and 360–520; `tests/test_the_guard_asks_once_per_session.py` (`grant`, `ask_entries`, `write_transcript`, `PRESS`); `tests/conftest.py` (`load_hook_module`, `repo`)
- `docs/worktree-guard-spec.md` line 20, lines 600–636, 770–782 and 980–988
- `README.md` and `README.ko.md` (the fix diff)
- `seal/ledger/1791781864-the-idle-session-rows-ask-nobody.md` and `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` (the word diff of the fix range), `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md` (changed tokens: anchor re-stamps only)
- `bin/test`
