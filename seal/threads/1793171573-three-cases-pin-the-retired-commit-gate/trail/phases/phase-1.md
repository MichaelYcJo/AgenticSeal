# Phase 1: 1793171573-three-cases-pin-the-retired-commit-gate

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 5f2efce2 |

## What this phase was asked

Build #1039 with no frame, on the ladder's second rung: the change removes
cases and alters no observable behaviour, so a one-line scope confirmation
in `gaps.md` stands in for the plan, and `gaps.md` is the closing memo.
Delete every case the issue names with its `.test_durations` entry. Leave
nothing in the module or the tree that only those cases needed. Correct every
place that cited them, searched with `git grep` for their names and for the
module's coordinates in `docs/`, `skills/`, `tests/` and `CONTRIBUTING.md`.
Stop and report if the issue's premise no longer holds. Work items #1040,
#1058 and #913 run in parallel, and a change to one of their files is
reported before it is made. Write a `changelog.md` fragment only if a
release note would state the change.

## What this phase found

- **The issue's premise held at `27a6bb6d`.** The three cases stood at
  `tests/behaviour/test_the_hook_surface_git_offers.py:176`, `:274` and
  `:318`, with the markers `no-verify-met-where-the-branch-moves` at `:273`
  and `gits-own-commits-not-judged` at `:317`. `.test_durations` priced them
  at 3.01 s, 7.10 s and 6.19 s, at `:874`, `:880` and `:876`. The
  `check:` lines at `docs/worktree-guard-spec.md:360` and `:587` name the
  module and no case (read).
- **No document, skill, test or contribution guide cites the three cases or
  their markers.** `git grep` found the case names only in the module and
  `.test_durations`. It found the markers only in the module and in
  `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/design.md:172`,
  which is another work item's record of the issue text and is left as
  written (executed).
- **One helper went with the cases.** `AUTHOR_DATE_LOG` and its `M12`
  comment served only the two marked cases. `REFUSING_RT`, `ZERO`, `repo`,
  `hook`, `head`, `POST_CHECKOUT_LOG` and `UNDO` still serve the seven cases
  that stay, and ruff found no import left unused (executed).
- **The docstring now names both rules of the worktree guard and the cases
  that pin each.** It names the three switch cases for *Which tree* and the
  four creation cases for *Decided before git runs*. The `HEAD` sentence for
  git 2.34 to 2.43 is kept as the measurement stated it. The module's own
  comment on the rebase parameter cites one measurement of it, on 2.50.1
  (S28 of work item 1791384157), so the docstring says the checkout and the
  rebase reach the hook "the same way" and claims no more for older gits.
- **No unit was added, so `seal mutate` had nothing to run over.**
