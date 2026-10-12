# 1791781864-the-idle-session-rows-ask-nobody — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | abe3dc3e |
| Ran by | specseal:smith on claude-opus-5-5 |

## What this phase was asked

`spec.md` In 2, built in the same segment as phase 1: `choose` takes
`pressed` and the way-on text and denies before the marker where it is set.
`main` passes it at rows 1-b and 2, read lazily (W2), with W1's text in both
languages. `tests/test_the_idle_session_rows_ask_nobody.py` holds S3, S4 and
S6–S11, each new case seen red at `c38f97d7`, S5's assertion goes into the
three existing cases, and S12 is checked. W1–W3 are this phase's to decide
and record here. The P-rows stand at P1 (b) and P2 (a). Stop after this
phase: phase 3 waits for #894 to land on `origin/release/v0.21.0`.

## What this phase found

**The frame holds, with two corrections to the scenario table.**

1. **S6's dirty half cannot be built as written before #894 lands.**
   `spec.md` S6 says a dirty tree under the press with the token meets
   *#894's deny with the token lead*. On this branch the tracked-changes row
   is still the base's `ask`, because #894 is not merged. The case pins the
   part this work owns: the token stands both rows aside, so the first line
   is the token's lead, `f.txt` is listed, and In 2's text is absent. The
   decision is not asserted. **Phase 3 adds `decision == "deny"` to that
   half once #894 is merged.** It can compare against #894's `dirty_deny`
   in the same way #894's own S3 case does. Nothing goes red at the merge,
   so nothing is left red for the merge to inherit.
2. **S7's `git worktree add ../wt -b feature/x` fails in git**, because
   the `repo` fixture already holds `feature/x` (`tests/conftest.py#_build_repo`).
   The case creates `feature/y` instead.

**W1, the text and where it is composed.** It is composed in `main` and
handed to `choose` as `unattended`. `main` holds what the text needs: the
command word from `git_at` and `wt_root` from `repo_paths`. `choose` stays
generic. It does `respond("deny", situation.rstrip("\n") + "\n\n" +
unattended)` before `already_asked`, so no marker is written and
`before_ask` is not run. The commands are one string, `split`, factored
out of `steer`. The attended steer is `split` plus its old last sentence,
byte for byte (S5 pins it), and the deny uses the same `split`, so the two
cannot drift apart. The text is, in order: the press sentence, word for word
#894's; that the split needs nobody because the answer already consents to
the creation; `split`; working there by path with `git -C
<wt_root>/<name> …` and an absolute path for edits; the sentence that a
branch already checked out in a worktree needs no switch (the bound
`plan.md` puts on its six-months failure scenario); and the re-issue
sentence. It names no question tool, no `[shared-tree-ok]` (P1 (b)) and no
`[worktree-ok]`. The Korean half follows #894's register. S3 and S4 pin
both languages whole.

**W2, the lazy read.** `pressed=automation_pressed(repo_paths(cwd)[0],
session_id, transcript_path)` is an argument inside each row's `if`, with
no closure and no value computed above the rows. `choose` ends the command
on every path, so at most one of the two arguments is ever evaluated. S10
counts 0, 1, 1 and 1.

**W3, S7's fixture.** The case gives `repo` a bare `origin` and pushes
`HEAD` to `main`, so the deny's commands run as written. `git fetch origin`
and `git worktree add <wt_root>/y -b feature/y origin/main` each pass the
guard, the first silent and the second `allow`, and then run in git. `git
-C <wt_root>/y status` is silent. The judged creation quotes the path with
`shlex.quote`. On POSIX that leaves the deny's bytes unchanged, and on
Windows it keeps the backslashes, the same choice as #894's S11-shaped case.

**M2 has a case now.** `test_on_windows_a_switch_under_the_press_is_row_twos_deny`
runs only on `win32`, with nothing stubbed, so the Windows shards measure
the claim at the pull request. Off Windows it was seen red against the
pre-change hook by a deleted probe, `tests/test_tmp_896_m2.py`, in which
`hooksession.is_claude` answered False. That is the branch Windows takes
when `ps -axo` yields nothing: `sessions_in_tree` returns `[], [], False`.
The same probe was green after the change. `questions.md` M2 stays open
until the Windows shards run.

**How each case was seen red.** The hook stood at `79a0577a`, whose diff
from `c38f97d7` is `fmt_sessions`'s unidentified branch alone, which no
phase-2 case prints. S3 (idle), S4 (unusable), S7, S8, S9, S10 and S11 each
failed on the attended text: the deny naming `AskUserQuestion`, or for S10
the counts 0, 0, 0, 1. S6 was green there, by design, and S5's four English
and four Korean texts were green there, because they are the base's. Both
were then shown to catch a change by mutation.

**Mutations, one break each through `mutation-check`, all `red`:** the
press branch removed from `choose` (S3, S4); row 1-b passed `False` (S3);
row 2 passed `False` (S4); the press read against the switch's `top`
instead of the session's root (S11); the press read ahead of the token at
row 1-b (S6); the marker written before the deny (S3, S4); the re-issue
sentence dropped (S3, S4); the situation dropped from the deny (S3, S4,
S9); the press read eagerly above the rows (S10); and one newline dropped
from `split` (S5).

**The environment moves `IDLE_MIN`.** The owner's shell exports
`WORKTREE_GUARD_IDLE_MIN=3`, and CI reads the default 5, so every pinned
text formats `module.IDLE_MIN` in rather than a number.

**A comment in `main` was made true again.** The comment above
`judge_creation`, *Only one of those three denies unconditionally*, now
says that under the press rows 1-b and 2 deny on every attempt too.

**Seen and left as it was.** The steer has always printed `{wt_root}`
unquoted, and the new deny does the same. On a path holding a space, or a
Windows path in a POSIX shell, the printed command is not safe to copy.
This predates the work item, and the attended text is held byte for byte
(S5). Nobody is named for it, so it stays in this record.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| none — `steer`'s commands moved into `split`, and `steer` is `split` plus its old last sentence, byte for byte | none |
