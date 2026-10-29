# Phase 1: 1793240969-pre-rename-readings-outlived-their-release

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | e1fc252d |

## What this phase was asked

Build phase 1 of `frame/plan.md`, with phase 2 in the same spawn, against
the frame committed at `4b6e8fbe` and approved at `8380774e`. Routing is
automation, so nobody is asked anything mid-run. `frame/questions.md` Q1
stands on its default (a): the other readings of the same promise stay out,
and `gaps.md` *Not done* names each with its coordinate. Sibling #1046 edits
other sections of `skills/implement/orchestration.md`, so only the
`Implementation` row the plan names is edited there. The rewritten case is
seen red against the reader as it stood at `1e82fd0a`, read through
`git show` rather than a checkout, and the hand-back says how.

## What this phase found

- **The frame held.** Every coordinate the phase-1 row and *Technical
  context* give stood where they say at `1e82fd0a` (read):
  `chain_check.py:2076-2082` for `TRAILER` and `OLD_TRAILER`, `:2101` and
  `:2121` for `routing_trailers` and its format line, `:12-16` for the
  module docstring's `trailer` arm, `tests/skills/test_chain_check.py:2965-2981`
  for the pinning case, and `tests/censuses.py:1006-1009` for the census
  item.
- **How the case was seen red (executed).** The case was rewritten first,
  with `skills/code-review/scripts/chain_check.py` byte for byte the file at
  `1e82fd0a` (`git diff --quiet 1e82fd0a -- <path>` exit 0). Run alone, it
  failed at `assert code == 0`: the old reader judged the commit carrying
  `SpecSeal-Routing: 1792000000-a-routed-item` as naming an undeclared work
  item and exited 1. With the reader changed it passed.
- **The rewritten case drops the old case's third commit.** That commit
  carried `Seal-Routing: no work item` and showed the new key read beside
  the old one. S3 already holds the new key through
  `test_refuses_a_commit_naming_a_work_item_no_declaration_names`, which
  stands unchanged, so S1's case carries only the two commits S1 names.
- **The census comment names the case by its class.** It cites
  `tests/skills/test_chain_check.py#Test_routing_trailers`, the group the
  case belongs to, so the case's name is not stated a second time.
- **No unit was added, so the mutation was the removed reading put back.**
  `seal mutate` put the old key back into the format line as a second
  `key=`, ran the S1 case, and reported `red` (exit 0); the
  file came back to its committed bytes.
