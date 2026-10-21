# 1792619289-the-pull-request-check-parses-rule-changes — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 2a3ea1a2 |

## What this phase was asked

The reframe after round 1, approved at 81f607c0. In `main`, the edited
set: every `seal/specs/<id>/spec.md` the pull request adds or changes,
filtered by `carried_by`, less an exact move, on a pull request that
declares at least one work item, and its read after the per-declaration
loop under the same exit-2 guard. Cases S12 to S16 and S6's second half,
each with the `rule-changes-read-at-the-pull-request` marker, and S12 to
S14 seen red against `chain_check.py` at 22bfec31. Rewritten in place: the
docstring's `rule changes` arm, both hygiene comments, the `settle` pointer
sentence and the changelog's broad-gate sentence.

In the same pass, round 1's findings closed in `rounds/round-1.md`: 1 and 2
deferred to the frame, 3 and 4 fixed. Finding 4's comment fix came before
this phase's comment edits, so they rest on it. Finding 3 is decided once
in the one reader, as a class and not a list of spellings, and stated once
in `skills/settle/SKILL.md` *Rule changes*, with no spec in the tree newly
refused.

The owner's direction binds as in phase 1. The boundary runs are phase 1's,
plus `rule_changes.parse` over every spec and `chain_check.py --baseline
release/v0.22.3 --worktree`.

## What this phase found

- **Red against 22bfec31.** `chain_check.py` was unchanged from 22bfec31
  until this phase's commit, so the run before the build is that file. S12,
  S13 and S14 failed on `assert 0 == 1`. S15, S16 and S6's second half
  passed there, because each pins what the check already did.
- **The filters needed cases of their own.** The first mutation run left
  four units green: the `carried_by` filter, the depth filter, the
  `spec.md` name filter, and the exit 2 for an edited spec. S8 never
  reached the edited set, because a release pull request that declares
  nothing returns before it. Three cases now hold them:
  - a release pull request that declares a work item of its own leaves a
    carried spec unread;
  - a `plan.md` changed beside a spec the branch leaves alone, and a
    `spec.md` one directory down, are not read;
  - a reader that will not load for an edited spec is exit 2.
- **One guard, two callers.** `rule_changes_of` holds the exit-2 guard and
  the stderr line, and the per-declaration loop and the edited set both call
  it. The two spellings of the guard phase 1 would otherwise have needed are
  one. `edited_work_items` holds the set, so `main` keeps only its
  subtraction of the judged work items.
- **The near-miss class is the heading's letters.** A heading at any level
  whose letters, case folded, are `rulechanges`, and that is not
  `## Rule changes`, is refused at its line. That covers case, level and
  punctuation. A heading with other letters, such as `## Rules changes`, is
  another section, and a case pins that boundary. The refusal also stands
  where the right heading is present too. Over the 119 specs in the tree, no
  spec is refused (executed, in memory).
- **The two hygiene comments carry one list in the same words.** Each
  comment wraps it to its own indent.
