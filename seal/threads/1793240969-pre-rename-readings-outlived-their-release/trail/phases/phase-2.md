# Phase 2: 1793240969-pre-rename-readings-outlived-their-release

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | f4d3d4a3 |

## What this phase was asked

Build phase 2 of `frame/plan.md` in the same spawn as phase 1. In
`skills/implement/orchestration.md`, edit only the `Implementation` row of
*What the answer writes*, because sibling #1046 edits other sections of
that file. The rewritten case is seen red against the parser as it stood
at `1e82fd0a`, and the hand-back says how.

## What this phase found

- **The frame held.** `hooks/lib/routing.py:72-78` held `BY_CRAFTER`, the
  comment, the exemption line and `OLD_BY_CRAFTER`, and `:258-259` held the
  two lines in `parse` (read, at `1e82fd0a`). The return dict's
  `implementation if implementation in IMPLEMENTATION_ANSWERS else None`
  is what reads the old answer once those lines go, as the plan says.
- **How the case was seen red (executed).** The case was rewritten first,
  with `hooks/lib/routing.py` byte for byte the file at `1e82fd0a`
  (`git diff --quiet 1e82fd0a -- <path>` exit 0). Run alone, it failed with
  `assert 'crafter' is None`. With the two lines of `parse` removed it
  passed.
- **The case also asserts the declaration's review answer.** It follows
  `test_refuses_an_unreadable_third_axis_as_an_answer_and_keeps_the_declaration`,
  the group's case for an answer outside the vocabulary, so it shows the
  declaration still parses whole and not only that the axis is None.
- **The exemption sits inside the call's arguments.** The line that spells
  the old answer is the `replace` call's second argument, and its
  `# exempt from old_names:` comment stands on its own line above it.
  `ruff format --check` keeps it there (executed, exit 0), and
  `tests/test_censuses.py` passes over the tree (executed, exit 0).
- **No other living line states the reading (rule 12, executed).**
  `git grep` for `OLD_TRAILER`, `OLD_BY_CRAFTER`, *renamed AgenticSeal*,
  *before the rename*, *minor release of the rename* and *under either key*
  outside `seal/threads/` and `evals/` finds the policy sentence in
  `docs/the-routing-check.md:101-102`, which the settle removes, and lines
  about the other readings Q1 keeps out. None states either reading this
  work removes.
- **No unit was added, so the mutation was the removed reading put back.**
  `seal mutate` added the two lines that turn the old answer into
  `BY_CRAFTER` back into `parse`, ran the S2 case, and reported `red`
  (exit 0); the file came back to its committed bytes.
- **`.test_durations` still prices both cases under their old ids.** The
  two entries are left; `gaps.md` *Not done* says why.
