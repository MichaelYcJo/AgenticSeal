# 1791781864-the-idle-session-rows-ask-nobody — round 1's fix pass

## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| 🔴 1 | fixed | fbf7554f |
| 🟡 2 | fixed | a6313eb5 |
| 🟡 3 | fixed | a6313eb5 |
| ⬜ 4 | answered | the placeholder now names the path either creation form makes, `{wt_root}/<branch>` or `{wt_root}/<name>`, in both languages, at fbf7554f. The path stays unquoted, as `split` prints it on the lines just above: the model copies one spelling from one reason, and S5 holds `split` byte for byte. Quoting both is the predating `{wt_root}` limit `overview.md` §*Not done* already names |
| ⬜ 5 | answered | corrected at a6313eb5: `handoff.md` names PR #902, phases 1–3 with their commits, round 1 at c7860bfe, and the verifying round as the next act |
| ⬜ 6 | answered | corrected at e95a40ec: #894's restated S2 Proof cell names #894's one branch and #896's two `pressed=` reads. a6313eb5 had already restated it; e95a40ec qualified S2's and S9's claims after 🔴 1 |

## What the fix range changes

The range is fbf7554f..5652b6be.

- **🔴 1.** `main` composes the press deny in a nested `unattended_text()`,
  called only where the press was read. It names the split where the
  switch's tree is in the session's own clone (`worktree_consent._clone_of`)
  or this session holds a creation record there (`worktree_consent.granted`).
  Anywhere else it says the answer consents only in the clone it was given
  in, names no split, no question tool and no token, and carries the
  re-issue sentence. The text in the press's own clone is unchanged except
  ⬜ 4's sentence. Neither check reads the transcript, so S10's counts stand.
  The press sentence is still #894's `PRESS`, byte for byte. The same
  qualifier is in the module docstring (the row and the CHOICE paragraph),
  `docs/worktree-guard-spec.md` §*Choice sites* *Under the press* (two
  sentences) and §A's only-IDLE row, §*Unknowns resolve conservatively*,
  changelog item 1, both READMEs, the case module's docstring, and the
  ledger's S3·S4, S11, R1 and #894's S2 and S9.
- **🟡 2.** `choose` declares `Reads: observed`, a marker presence test
  through `already_asked`. The direction stays `refused`.
- **🟡 3.** The Windows bullet of §*Known limits*, §*Unknowns resolve
  conservatively* and changelog item 3 say that a switch carrying
  `[shared-tree-ok]` is not this deny.
- **Contract changes:** none. `choose` keeps its parameters, and `main` is
  the hook's entry point.
- **New units:** `main`'s nested `unattended_text`, and two cases in
  `tests/test_the_idle_session_rows_ask_nobody.py`:
  `test_a_switch_into_another_clone_names_no_split_it_cannot_consent` (the
  report's case, widened to both rows and both languages, with the whole
  text pinned) and `test_a_clone_this_session_already_split_is_named_the_split`
  (the report's second regression, the `granted` branch). S11's first half
  now pins the text for another clone.
- **Removed:** nothing.

## Seen red

- The two new cases and S11 ran against the guard as it stood at
  c7860bfe, before fbf7554f: 7 failed. The another-clone case and S11
  failed on *pass as written*, and the rest on ⬜ 4's sentence.
- Through `bin/mutation-check`, each `red`:
  - the clone test made `True` turned the another-clone case and S11 red;
  - the record's branch made `False` turned the `granted` case red;
  - the session root swapped for the switch's tree turned the another-clone
    case and S11 red.
