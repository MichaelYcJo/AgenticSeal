# Phase 3: 1793163944-the-issues-were-filed-against-the-old-tree

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | |

## What this phase was asked

Fold the 7 bodies of `release: 0.24.1` that `frame/design.md` *Verdicts*,
*release: 0.24.1* names, including #947's *After* row and #1044's count, and
post one comment on #1044 saying its count now lives in #947. By the owner's
answer to Q1, relayed by the orchestrator during phase 2, #1049's folded body
does not gain #920 in its list of guard issues.

## What this phase found

**Every issue edited, with `updatedAt` before and after and the exit code of
each `gh` command (executed; each exit code read directly).** Every
`updatedAt` before was earlier than the frame's read, so `frame/questions.md`
Q2 did not arise. Each body read back equals the file sent (`diff` exit 0).

| Issue | updatedAt before | updatedAt after | `gh` commands and exit codes |
|---|---|---|---|
| #947 | 2026-10-27T01:28:58Z | 2026-10-28T05:45:25Z | body 0 |
| #1045 | 2026-10-27T05:24:27Z | 2026-10-28T05:45:58Z | body 0 |
| #1046 | 2026-10-27T01:28:37Z | 2026-10-28T05:47:21Z | body 0 |
| #1047 | 2026-10-27T01:28:39Z | 2026-10-28T05:47:22Z | body 0 |
| #1048 | 2026-10-27T01:28:41Z | 2026-10-28T05:49:15Z | body 0 |
| #1049 | 2026-10-27T01:28:54Z | 2026-10-28T05:49:17Z | body 0 |
| #1091 | 2026-10-27T07:37:50Z | 2026-10-28T05:49:18Z | body 0 |
| #1044 | 2026-10-28T04:50:12Z | 2026-10-28T05:49:35Z | comment 0 (`issuecomment-6461767960`); body not edited |

**S6 (executed).** `gh issue view 1044 --json comments` reads two comments,
the second this phase's, saying the count now lives in #947. #1044 stays
closed.

**#947's reading was taken again before it was written (executed at
`c1b79d40`, `wc -c`).** Each definition plus `skills/agent-contract/SKILL.md`
(12,233 B): framer 22,513, crafter 21,461, proofer 21,898, sealer 21,386,
tracer 15,236; `CLAUDE.md` 3,425, the same at `origin/release/v0.24.0`. Each
definition's `skills:` lists only `agent-contract`. The figures equal the
frame's.

**#1049's cost table was measured again (executed at `c1b79d40`, `wc -l`,
`wc -w`, sums from `.test_durations`).** Every figure equals the frame's:
the guard's cases come to 105.9 s of 1,252.4 s.

**#1049's importers of `hooks/lib/cmdline.py` differ from the frame's
(executed, `git grep -w cmdline -- hooks` and each import line read).** The
frame lists `hooks/lib/tokens.py`, `hooks/lib/one_heredoc.py`,
`hooks/worktree-guard.py` and `hooks/worktree_consent.py`, and drops
`hooks/implementer-notice.py`. In the tree, `hooks/worktree-guard.py:197`
(`import cmdline as wide`), `hooks/implementer-notice.py:47` and
`hooks/lib/tokens.py:71` import it; `hooks/worktree_consent.py:94` imports
`cmdline_base as cmdline`, and `hooks/lib/one_heredoc.py` names the file only
in its docstring (`:10`). The body keeps its original three importers at
their new paths, with the line of each, and its *Done when* names
`hooks/implementer-notice.py` and `hooks/lib/tokens.py`. `gaps.md` holds the
divergence.

**#1049 holds no line about #920.** It gains only the #1096 sentence the
frame names. #920 also edits `hooks/worktree-guard.py` in 0.24.0; a sentence
saying so was not added, because the owner's answer names #920 only as
staying out of #1049's list.

**Old-form hits left in each body, each judged.**

- #947: `smith`, `warden` and `scribe` in the *Before* heading, "as the
  framer, smith, warden, sealer and scribe, the names the agents had then",
  which the row keeps so the old figures keep their meaning.
- #1045: `overview.md` four times, in the count table's row "(then
  `overview.md`, now `gaps.md`)" and in #1016's history, its `location:` lines
  `overview.md:17` and `:13-18` and "the file then named `overview.md`".
- #1046: none.
- #1047: `seal/specs/` and `spec.md` inside the `0ed5dd3b:` citations;
  `warden` in "(then the warden's)" and in the cited directory name
  `1792366315-the-wardens-real-false-finding-rate-is-unknown`.
- #1048: `smith` in "written when the agent was named the smith";
  `seal/specs/` inside the `fa7d1374:` citations.
- #1049: `spec.md` in `docs/worktree-guard-spec.md`, a current path, three
  times.
- #1091: `smith` and `mutation-check` in "then named the smith, ran nine
  mutation runs (`mutation-check`, now `seal mutate`)", history of #1051's
  phase.

**Instances folded beyond the rows (the mapping's classes, contract rule
12).** #1047: #971's phase record became
`0ed5dd3b:seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/phases/phase-3.md`
(executed, `git cat-file -e`), and the "nine warden cases" became "nine
proofer cases (then the warden's)". #1048: #955's phase record became
`fa7d1374:seal/specs/1793051803-settle-runs-in-local-mode/phases/phase-1.md`
(executed, `git cat-file -e`). #1046: "outside `seal/specs/` and
`changelog/`" became "outside `seal/threads/`, `seal/process/`, `changelog/`
and `CHANGELOG.md`", as the frame does for #1043 and #1056. #1047's
`questions.md` in three sentences about 0.22.x records stays, because those
records carried that name.

**#1046's word count.** The two sections are 1,847 and 146 words, 1,993
together, of 7,649 (executed, `wc -w`). The body states the sum, which the
frame does not.

**Titles left as the frame scopes them.** #1048's title names "the smith's
claims", #1045's names `overview.md`'s divergence table, and #1046's names
"1,836 of the 7,047 words". They are named in the hand-back.

The 8 body and comment files were written to the crafter's scratch directory
outside the tree and removed by their paths when this phase closed.
