# 1791852612-under-automation-a-creation-in-another-clone-asks-nobody — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 7fd83e55 |
| Ran by | unknown — the spawn prompt named the agent (`smith`) and no model, and this record transcribes only what it was given |

## What this phase was asked

Build `plan.md` phase 1: `guard_worktree_creation`'s rows 3 and 4 pass
`choose` the press, read lazily inside each row's `if` from the session's
own root, and the unattended text; the other-clone sentence in both
languages, the press and re-issue sentences shared per W1 (default (a),
module level); `choose`'s docstring sentence replaced (`spec.md`
§*Removes*); a `Reads:` line on `guard_worktree_creation` and its census
line removed (S13, W2); `tests/test_a_creation_in_another_clone_asks_nobody.py`
with S1, S2, S5–S8, S10 and the Windows-only S11, each case seen red at
`321e9de1` where the scenario says red; S3's assertion beside the existing
creation cases; S9 and S12 checked. P1 at its default (a), row 1 unchanged,
on the owner's decision. Also, from the orchestrator mid-phase: a
`### Why these rows` sub-heading above the prose under `spec.md`'s
`## Removes` table, words unchanged, for #905's reader.

## What this phase found

**The frame does not hold in two places, both in its scenarios, and the
build follows the code rather than the sentence.**

1. **S10's fourth count is 2, not 1.** The frame wrote *1, 2, 1, 1 —
   `consent` once each, and the rows' read only where a row fires under the
   press*. Attended in the other clone's idle state, row 3 still fires, and
   whether the press is there is exactly what its read finds out, so the
   transcript is read twice: once by `consent` for the creation's clone, once
   by `automation_pressed` for the session's own root. No reading of the
   rows can know the press is absent without that read. The case pins
   `[1, 2, 1, 2]`, and the bound the frame argued for — at most twice per
   creation — holds in all four states. `overview.md` records the divergence.
2. **S1's *no `worktree add` in the reason* cannot hold as written.** Every
   creation row opens with `origin`, *Attempting to create a worktree with
   `git worktree add`.*, which names the command being judged. The case
   asserts no `worktree add` after that first line — no command to run is
   named — which is what the frame's sentence was for (#896's switch-side
   case asserts the whole reason because its situation names none).

**W1, answered (a).** `press_sentence()` and `reissue_sentence()` are
module-level functions returning `tr(en, ko)`; `main` assigns its two
locals from them and `guard_worktree_creation` composes its deny from them.
Byte-identical output on the switch side:
`tests/test_the_idle_session_rows_ask_nobody.py` passes unchanged, and a
mutation of either sentence turns both ladders' cases red at once
(`mutation-check`, mutations E and F below).

**A third copy of both sentences, outside W1's frame.** The tracked-changes
row's deny under the press (`main`, the `automation_pressed` branch above
the dirty-tree `ask`, #894) carries both sentences inlined inside one
`tr(...)` pair, in both languages. It was there at `321e9de1` and the frame
named only `main`'s two locals. It is left as it was: folding it would
change the code of a row this work item does not touch, and its text is
pinned by `tests/test_the_guard_asks_once_per_session.py`'s `dirty_deny`
cases, so a reword of `press_sentence` that misses it fails there rather
than drifting silently. Named for review rather than built.

**W2, answered.** `Reads: observed` with direction `refused`: the unit's
own reads are the consent (a record's presence and a harness-written
transcript), the process-scan session count, and the press — facts asked
of the system. The token and the allow's bound are its caller's, read from
the command, so they do not lower its class. Every way of not reading one
of its own inputs lands on a row that stops the command (no consent → the
rows; an unreadable count → row 4; an unreadable press → the attended
deny/ask), so `refused`. The wording is the warden's to argue.

**The two new functions declare `Reads: nothing`**, as text formatters of
this guard's own output.

**Where the press is not read.** `judge_creation` is also reached from
`main`'s `if not top:` exit, where the shell stands outside any
repository; `repo_paths(cwd)[0]` is `""` there, `automation_pressed`
answers False, and the rows give the attended verdict, as at the base.
There is no session root to read a press from, which is the switch rows'
reading too.

**S9 and S12.** `git diff 321e9de1 -- hooks/worktree_consent.py
hooks/commit-review-gate.py hooks/cmdline_base.py` is empty (exit 0). The
one hunk in `main` replaces the two locals' literals with the function
calls, above `unattended_text`; nothing inside `unattended_text` moved, and
`test_a_switch_into_another_clone_names_no_split_it_cannot_consent` is
green.

**The switch side's other-clone sentence stays true.** It says a split of
another clone *may be put to a person*. After this work rows 3 and 4 put
nothing to a person there under the press, but row 1 (ACTIVE) and row 2
(`[worktree-ok]`) still ask, so *may* still holds — on P1's default (a). If
P1 is ever answered (b), that sentence is the one to re-read.

### How each case was seen red

| Case | How |
|---|---|
| S1, S2 (`test_under_the_press_a_creation_row_denies_every_attempt[idle/unusable]`) | run against the guard while it was byte-identical to `321e9de1` (`git diff --quiet 321e9de1 -- hooks/` exit 0): the first attempt was the attended deny naming `AskUserQuestion` |
| S8 (`test_a_creation_behind_a_cd_meets_the_same_deny`) | the same run: the attended deny naming `AskUserQuestion` |
| S10 (`test_the_transcript_is_read_at_most_twice_per_creation`) | the same run: `[1, 1, 1, 1]` |
| S11 (Windows-only) | a deleted probe, `tests/test_tmp_s11_903.py`, ran its body off Windows with `sessions_in_tree` stubbed unusable: red at the base, green after |
| S5 (`test_a_record_in_the_other_clone_outranks_the_rows`) | green at the base by design; `mutation-check` with row 0's `consent` read replaced by `''`: red |
| S6 (`test_the_token_still_reaches_its_own_row`) | green at the base by design; `mutation-check` with row 2's `if user_ok:` made `if False:`: red |
| S7 (`test_the_press_is_read_from_the_sessions_own_root`) | green at the base by design; `mutation-check` with row 3's `pressed=` made `True`: red |
| S3 (`tests/test_worktree_guard.py::test_the_attended_creation_choice_rows_are_the_bases`) | text captured at the base by a deleted probe; `mutation-check` changing one word of row 3's question: red |

### Mutations of the units this phase added (`bin/mutation-check`)

| # | Mutation | Cases | Verdict |
|---|---|---|---|
| A | row 3 reads the press from `top` (the creation's clone) instead of `repo_paths(cwd)[0]` | the new file, `-k idle` | red |
| B | row 4 the same | the new file, `-k unusable` | red |
| C | row 3 `pressed=False` | `-k 'idle or twice'` | red |
| D | the other-clone sentence's *names no way on* reworded | `-k denies_every` | red |
| E | `press_sentence`'s English reworded | both ladders' `denies_every` cases | red |
| F | `reissue_sentence`'s English reworded | both ladders' `denies_every` cases | red |
| G | row 0's consent read removed | `-k outranks` | red |
| H | row 2 removed | `-k token_still` | red |
| I | row 3 `pressed=True` | `-k own_root` | red |
| J | row 3's attended question reworded | `-k attended_creation` | red |

### What phase 2 needs

- The deny's English and Korean texts as built are in
  `tests/test_a_creation_in_another_clone_asks_nobody.py#elsewhere`; the
  documents quote the policy, not the text.
- `Enforced by:` names for S14: S1/S2 are one parametrized case,
  `test_under_the_press_a_creation_row_denies_every_attempt`; S5
  `test_a_record_in_the_other_clone_outranks_the_rows`; S6
  `test_the_token_still_reaches_its_own_row`; S7
  `test_the_press_is_read_from_the_sessions_own_root`; S8
  `test_a_creation_behind_a_cd_meets_the_same_deny`; S10
  `test_the_transcript_is_read_at_most_twice_per_creation`; S11
  `test_on_windows_a_creation_in_another_clone_is_row_fours_deny`.
- Units whose hash moved, for the `Re-read ·` rows: `guard_worktree_creation`,
  `choose`, `main`; new units `press_sentence`, `reissue_sentence`.
