# Phase 2: 1793163944-the-issues-were-filed-against-the-old-tree

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | |

## What this phase was asked

Fold the 15 bodies of `release: 0.24.0` that `frame/design.md` *Verdicts*,
*release: 0.24.0* names, through *The name mapping every fold applies* and the
released-records table; retitle #1040; move #920 to `release: 0.24.1` and
comment the reason on it, the default of `frame/questions.md` Q1 as the spawn
prompt gave it. Where a body cites `docs/branch-and-release.md`,
`docs/release-checklist.md`, `docs/the-review-record.md` or
`docs/the-agent-set.md` by line, cite the line at `origin/release/v0.24.0`,
because #1108 changed those four documents after the frame's read.

During the phase the orchestrator relayed the owner's answer to Q1, (b): #920
stays in `release: 0.24.0` among the small fixes, no move comment stands, and
a move already made is undone and recorded here.

## What this phase found

**Every issue edited, with `updatedAt` before and after and the exit code of
each `gh` command (executed; each exit code read directly).** Every
`updatedAt` before was earlier than the frame's read at 2026-10-28T05:24:47Z,
so no body had been edited by anyone after the read (`frame/questions.md` Q2
did not arise). Each body read back with `gh issue view <N> --json body`
equals the file sent (`diff` exit 0).

| Issue | updatedAt before | updatedAt after | `gh` commands and exit codes |
|---|---|---|---|
| #1058 | 2026-10-27T04:03:18Z | 2026-10-28T05:32:13Z | body 0 |
| #913 | 2026-10-22T01:20:38Z | 2026-10-28T05:33:04Z | body 0 |
| #920 | 2026-10-18T13:08:36Z | 2026-10-28T05:42:59Z | body 0; milestone to 0.24.1, 0; comment, 0; milestone back to 0.24.0, 0; comment deleted, 0 |
| #712 | 2026-10-18T13:08:47Z | 2026-10-28T05:35:06Z | body 0 |
| #1039 | 2026-10-27T01:28:15Z | 2026-10-28T05:35:08Z | body 0 |
| #1040 | 2026-10-27T01:28:17Z | 2026-10-28T05:36:47Z | body 0; title 0 |
| #1041 | 2026-10-27T01:28:19Z | 2026-10-28T05:36:48Z | body 0 |
| #1043 | 2026-10-27T01:28:23Z | 2026-10-28T05:38:13Z | body 0 |
| #1042 | 2026-10-27T01:28:21Z | 2026-10-28T05:38:14Z | body 0 |
| #992 | 2026-10-19T06:05:09Z | 2026-10-28T05:39:17Z | body 0 |
| #956 | 2026-10-22T01:50:31Z | 2026-10-28T05:39:18Z | body 0 |
| #1055 | 2026-10-27T02:57:54Z | 2026-10-28T05:41:10Z | body 0 |
| #1056 | 2026-10-27T03:18:53Z | 2026-10-28T05:41:11Z | body 0 |
| #1020 | 2026-10-24T00:19:32Z | 2026-10-28T05:42:37Z | body 0 |
| #951 | 2026-10-27T02:15:08Z | 2026-10-28T05:42:39Z | body 0 |

**#920, moved and put back.** The move to `release: 0.24.1` and the comment
(`issuecomment-6461513788`) were made on the default before the owner's answer
reached this phase. Both were undone: `gh issue edit 920 --milestone
"release: 0.24.0"` exited 0, and `gh api -X DELETE
repos/MichaelYcJo/AgenticSeal/issues/comments/6461513788` exited 0. Read back
(S3, executed): milestone `release: 0.24.0`, one comment, the owner's own of
2026-10-18 about the earlier move from 0.22.4 to 0.22.5, which predates this
work. #920's folded body never named the move, so it stands.

**S2 (executed).** `updatedAt` of #1053 2026-10-27T02:26:00Z, #1096
2026-10-28T04:03:25Z and #1102 2026-10-28T04:05:42Z, each the value the frame
read.

**Old-form hits left in each body, each judged.** The search of `plan.md`
*Technical context* finds:

- #1058, #920, #1041, #1043, #1042, #951: none.
- #913: `seal/specs/` and `spec.md` twice, each inside a `0ed5dd3b:` citation.
- #712: `seal/specs/` inside the `5180b89e:` citation.
- #1039: `seal/specs/` and `spec.md` inside the `0ed5dd3b:` citations;
  `spec.md` in `docs/worktree-guard-spec.md`, a current path; `rules --check`
  as `seal rules --check`, which the row keeps.
- #1040: `broad-gate` in "beside a broad-gate failure", the body's own
  adjective for a failure of the broad gate, not the retired command name. The
  sentence is otherwise unchanged, so it was left.
- #992: `smith`, `seal/specs/` and `overview.md` inside the `0ed5dd3b:`
  citation of `1792251842-the-smith-is-written-anew-from-its-job`; `warden` in
  "recorded as the warden's", which the row keeps, and in `warden-phase-3.md`
  inside the `0ed5dd3b:` citation.
- #956: `seal/specs/` inside the `0ed5dd3b:` citation.
- #1055, #1056: none outside `0ed5dd3b:` citations (#1056's closing memo).
- #1020: `warden` at five lines and `overview.md`, `spec.md` and
  `seal/specs/` in the `6fb3b2fd:` citation and in the two tables of #942's
  history. The body now says the tables name paths as #942's records do at
  `6fb3b2fd`, which the row keeps.

**Coordinates that differ from the frame's (executed or read at the tree of
`c1b79d40`, equal to `0b75346f` outside this directory).** The bodies carry
the coordinates as found:

- #1040: `agents/sealer.md`'s *Rules* paragraph is `:125-127`, not
  `:124-126`; `agents/proofer.md`'s rule 2 sentence is `:138-140`, not
  `:138-139`. The crafter's paste-check reader is named by its function,
  `test_the_crafter_puts_both_answers_in_the_hand_back`, since the row drops
  the line.
- #1041: the crafter's quoted sentence runs to `:156` (`:153-156`), and the
  orchestration quote is `:54-55`.
- #1043: the corrected citation is `docs/the-review-record.md:682-683` at
  `origin/release/v0.24.0` (`:670-671` at `0b75346f`), as the spawn prompt
  asks for the four documents #1108 changed. `docs/the-review-record.md:135-136`
  in #1041 is the same at both.
- #1055: the Korean README's gate count is `README.ko.md:408`, beside the
  frame's `README.md:417`. The passage-pair item cites `BASELINE` for both
  pairs and drops the old line numbers of the 34-word sentence.
- #1056: `LABEL_DESCRIPTION_LIMIT` is read by two test modules, not one:
  `tests/github/test_label_merged_on_release_branch.py:383` and
  `tests/github/test_tracker_labels.py:146`, through
  `.github/scripts/tracker_labels.py`'s `signal` (executed, `git grep`). The
  body names both. `gaps.md` holds the divergence.

**The mapping applied where the row did not list the instance (rule 12 of the
contract, the class of each mapping row).** Each is in `gaps.md`:

- #913: "#871's `plan.md` *Operational impact*" became
  `0ed5dd3b:seal/specs/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker/plan.md`
  *Operational impact*; the record was removed by `de11df75` (executed, `git
  log --diff-filter=D`) and the heading stands at that commit.
- #951: `arm-check` became `seal arms` (`skills/implement/scripts/seal.py:148`).
- #1042: "SpecSeal's own record shapes" became "AgenticSeal's".
- #992: "the warden's recall" became "the proofer's recall", beside the row's
  "recorded as the warden's".
- #1055: `templates/seal-README.md` became `templates/setup/seal-README.md`.
- #1058: "with `monkeypatch.delenv` in others" became "with
  `monkeypatch.delenv` or `env.pop` in others", because `:2785` is an
  `env.pop`.

**Done since filing, as the rows say.** #1039: the settle it waited for is
`de11df75`; its first *Done when* bullet no longer waits for one. #1043: the
`docs/` citation was corrected by `de11df75`; the body says so and keeps the
script's citation and the resolver case. #1055: items 1 and 2 keep only what
is left.

**Titles left as the frame scopes them.** The frame changes only #1040's
title. Four other titles of this milestone still carry an old form or a
figure the fold corrected: #712 "session-cost's spawn rows"; #1039
"tests/test_the_hook_surface_git_offers.py" and "19.5 s" (16.3 s at
`0b75346f`); #1043 names the citation the settle already corrected. They are
named in the hand-back for the orchestrator.

The 16 body and comment files were written to the crafter's scratch directory
outside the tree and removed by their paths when this phase closed.
