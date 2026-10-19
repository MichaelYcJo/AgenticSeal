---
name: legacy-parity
description: |
  Behavior-equivalence methodology for legacy migrations: three-way judgment
  (policy ↔ original code ↔ new code) with original-preservation as the default.
  Use when: a project declares a migration config (seal/parity.md), porting or
  reviewing ported behavior, judging divergence from a legacy original.
  NOT for: greenfield work — implement/code-review alone cover that.
---

# legacy-parity — the original is the fallback spec

Extends `implement` and `code-review` when the work is a migration, the same
behavior rebuilt on different technology, in a repository that declares
`seal/parity.md`. A scribe reads the sections that find and trace the
original: *The migration config*, *What the original sends* and *The
original's coordinates*. The sections that judge and record are its caller's.

## Premise

**Preserve the original's behavior.** A migration is not a redesign: a safer
design or a more consistent API is never grounds to diverge. An original that
looks wrong is reported, and changing it is the planner's call.
Enforced by: nothing — a judgment the parity review reads

## The migration config

A migrating repository commits `seal/parity.md`, written from
`templates/parity.md`, which holds its fields. A machine-local checkout path
never goes in it: it lives in `~/.claude/specseal/parity-paths.md`, keyed by
the origin remote URL, so worktrees and second checkouts resolve to one entry.

The original resolves in this order: the recorded path, a sibling directory of
the current repository, then a check by `git remote -v` against the declared
original. Where none resolves, the caller asks the user and records the
answer, and a reader that cannot ask returns `original not found` with what it
tried. A comparison against a guessed original proves nothing.
Enforced by: tests/test_review_axes.py::test_the_resolution_order_ends_with_the_caller_asking

## Three-way judgment

Where policy, the original and the new code diverge:

| Situation | Follow |
|---|---|
| Policy explicitly covers the divergence, and it holds up | **Policy** — grounds means a quotable sentence with its source; "the document probably said so" is not grounds |
| Policy silent | **The original**, exactly |
| Grounds exist but look wrong | Neither silently — record both texts side by side and escalate |

Inherit before raising a product decision: where policy is silent and the
original already does the thing, follow it and mark it decided, since only a
rule in neither place needs a planner.
Enforced by: nothing — a judgment the parity review reads

## What the original sends

Where storage, query conditions and response assembly disagree inside the
original, its behavior is what it sends the client. Trace from the endpoint to
the finished response; a mid-layer condition that never changes the response
is reported as such and needs no reproduction. Read the original's history: a
later fix is its intent, and cloning the version before it preserves nothing.
Enforced by: nothing — no case declares `seal/parity.md`

## The original's coordinates

A spec's Grounding cites the original's coordinates for the clauses in scope.
Start every comparison there instead of searching the original; the caller
pins what it settles with a test. A suspect coordinate is opened at the
baseline: `git show <baseline>:<path>`.
Enforced by: nothing — no case declares `seal/parity.md`

## Replacement annotation

Every ported entry point states, where its API docs render (the handler
docstring, say), **what it replaces**: the original's method, path and
function. That line declares the default, the original's business logic, so a
divergence grounded in policy is listed right below it. A 1:N split names the
branch each new handler took, an N:1 merge lists every original, a partial
port states what it left behind, and an addition reads `none (new)` with its
grounding clause.
Enforced by: nothing — a reviewer reads it in the parity review

## Parity review

`code-review` runs as usual with one change of frame: stage 1 compares against
the original, through the spec's coordinates, and not only the written spec,
across the same comparison axes. A verdict is one of four words, lowercase, at
the start of its line, and no other label is written:

```
differs     no grounds: align with the original
grounded    differs with grounds: quote them and confirm intent
equivalent  a different implementation, the same observable behavior
unread      the original or the policy was not found: never a pass
```

Enforced by: tests/test_the_record_is_written_in_words.py::test_the_parity_verdicts_are_four_words, tests/test_review_axes.py::test_legacy_parity_still_points_at_that_table

## Recording the comparison

The mark is written by the party that compared and whose definition names the
write: the warden in a review round, and a session where it compared without
one. The scribe and the smith write none. It is written only once
coordinates were opened, behavior read and verdicts given, so the commit gate
can recognize the cycle:

```bash
git rev-parse HEAD > "$(git rev-parse --git-dir)/specseal-parity"
```

A commit closes the cycle, and the next change to code starts an uncompared
one. Committing code with no such record makes the gate ask: approving is the
waiver, and `[no-parity]` skips it visibly, typed in front of the command with
its quotes, `: '[no-parity]'; git commit …`, because after `git commit` a bare
word is a pathspec. A mark for work nobody compared turns *nobody checked*
into *someone checked and it was fine*.
Enforced by: tests/test_review_axes.py::test_the_record_of_a_comparison_names_its_writer
