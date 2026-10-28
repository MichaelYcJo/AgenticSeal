# Implementation Plan: 1793169129-the-creation-row-still-says-retry-with-worktree-ok

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned.

## Summary

Under the `automation` press, the creation ladder's row 5 (single stream) in
another clone keeps its `deny` and its steer to `git switch`, opens with
`plain_origin`, and ends with `press_sentence()` and `reissue_sentence()` in
place of the sentence that asks for the user's confirmation and names
`[worktree-ok]`. Attended, nothing changes. One phase builds it, test first.

## Technical context

- `hooks/worktree-guard.py#guard_worktree_creation` (`:1590-1944` at
  `977b6613`, read). Row 0 reads consent first (`:1691`), so under the press
  rows 1 to 5 are reached only in a clone the press was not given in and this
  session holds no record in. Rows 3 and 4 read the press inside their `if`
  (`:1858`, `:1896`) and open with `plain_origin`; row 5 (`:1928-1944`) reads
  neither and ends with `steer_to_switch(git)`.
- `hooks/worktree-guard.py#steer_to_switch` (`:1382-1395`) returns the three
  switch command lines and the confirmation sentence in one `tr`. Its callers
  are row 2's `ask` (`:1815`), row 3's attended fallback (`:1889`) and row 5
  (`:1942`) (read; `grep -n steer_to_switch`, executed).
- `hooks/worktree-guard.py#judge_creation` (`:1947-2052`) builds `origin`
  with the quote note where the command does not parse cleanly and passes
  `plain_origin` beside it (`:2016`, `:2051`). Every creation in `main`
  reaches the ladder through it (`:3123`, `:3163`, `:3169`, `:3340`,
  `:3488`; executed `git grep`).
- `press_sentence` (`:1469-1483`) and `reissue_sentence` (`:1486-1493`) are
  module-level functions returning `tr(en, ko)`, shared by both ladders
  since #903; this work reuses them and adds no string.
- The cases: `tests/hooks/test_worktree_guard.py`, #903's section from
  `:4190` (read), with its helpers `creation_situation`, `creation_elsewhere`
  and `creation_unattended` (`:546-618`). Those helpers build rows 3 and 4's
  texts; row 5's expected texts are new helpers or literals beside them.
- **The failure scenario of the chosen approach.** In six months #1049 has
  narrowed or removed the guard, and this arm went with it: one chain run
  spent on text that no longer exists. The owner accepted that cost on
  2026-10-28 (`seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/questions.md`
  Q1, answer (b)). A second scenario: a model under the press, steered to
  `git -C <other> switch`, switches a branch in a clone it was not asked to
  touch. That steer stands at the base and #903's frame relied on it (*The
  class*, row 5); the switch there meets *A. Branch switch*'s rows, which
  pass a clean single-stream tree and deny a dirty one, so it reaches no
  person either way.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Under the press, row 5 keeps its verdict, its situation and its switch command lines, opens with `plain_origin`, and ends with `press_sentence()` and `reissue_sentence()` | The steer to `git switch` in another clone outlives a later decision that the model should leave other clones alone; the next frame then rewrites one arm. Reuses two shared strings, so a reword of either reaches every deny under the press at once | **chosen**: no new sentence in either language, the same register as every other deny under the press, and attended byte-identical |
| B. Under the press, drop only the parenthesis *(if the user already asked for a worktree, retry with [worktree-ok] in the command)* | *State why and get the user's confirmation first* still sends the model to a person; under `Automation` `yes` `hooks/question-gate.py` holds `AskUserQuestion`, so the model meets a refusal at the next step instead of an `ask` | rejected: it removes the token and keeps the question |
| C. Remove the confirmation sentence from `steer_to_switch` for every session | Attended, the single-stream deny loses its documented way past (`README.md:282`, `docs/worktree-guard-spec.md` *B. Worktree creation*), and a user who did ask for a worktree has no path but rewording the command | rejected: changes attended behaviour #920 does not ask about |
| D. Under the press, row 5 says rows 3 and 4's `elsewhere`, naming no way on | Drops the steer to `git switch` that #903's frame relied on, in a tree the guard has judged single-stream, where a switch needs nobody; and `elsewhere` says *nobody is at the keyboard to choose between splitting it and switching*, which row 5 does not ask | rejected |
| E. Replace the structure: under the press row 2 denies too, so a token the model writes reaches no person | A verdict change: #903 kept row 2's `ask` under the press on purpose (its S6, `test_the_token_still_reaches_its_own_row`), and the spec says *`[worktree-ok]` still reaches its `ask`*. The owner scoped #920 to the hint | not chosen; P1 of `questions.md`, default unchanged |
| F. Replace the structure: remove `[worktree-ok]` and the single-stream deny, or the guard | The premise that keeps the structure for now is the owner's answer (b) to `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/questions.md` Q1: fix the hint in 0.24.0, before #1049 weighs the guard in 0.24.1 (read, `:30`). Checked: #1049 stands in the milestone `release: 0.24.1` (executed, `gh issue view 1049`) | not chosen; #1049 decides it |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Under the press, row 5's deny names no `[worktree-ok]` and asks for no confirmation, on every attempt, in both languages, with and without an unbalanced quote; attended byte-identical; S5's pin `[1, 2, 2, 2]`; every comment and docstring in `frame/design.md` *In* rewritten in place | S1, S2, S3 and S5 seen red at `977b6613` as `frame/design.md` says for each, then green; S4 and S6 green unchanged; `bin/test tests/hooks/test_worktree_guard.py`, the crafter's narrow run | |

## Operational impact

None. No migration, no environment variable, no dependency and no
compatibility break. A reader outside this repository sees one change: under
the press, the single-stream creation deny in another clone stops naming
`[worktree-ok]`. The changelog fragment says so.
