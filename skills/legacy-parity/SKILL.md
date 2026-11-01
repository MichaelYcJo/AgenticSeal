---
name: legacy-parity
description: |
  Behavior-equivalence methodology for legacy migrations: a three-way judgment
  between policy, the original code and the new code, with the original's
  behavior preserved by default.
  Use when: a project declares a migration config (seal/parity.md), porting or
  reviewing ported behavior, judging divergence from a legacy original.
  NOT for: greenfield work, which implement and code-review cover alone.
---

# legacy-parity, the original is the fallback authority

Extends `implement` and `code-review` when the work is a migration, the same
behavior rebuilt on different technology, in a repository that declares
`seal/parity.md`. A tracer reads the sections that find and trace the
original: *The migration config*, *What the original sends* and *The
original's coordinates*. The sections that judge and record are its caller's.

## Premise

**Preserve the original's behavior.** A migration is not a redesign: a safer
design or a more consistent API is never grounds to diverge. An original that
looks wrong is reported, and changing it is the planner's call.
check: none reader: the parity review

## The migration config

A migrating repository declares itself in `seal/parity.md`, written from
`templates/setup/parity.md`, which holds its fields, and commits it where the
root is `<repo>/seal/`; in local mode nothing under the root is committed.
A machine-local checkout path
never goes in it: it lives in `~/.claude/agentic/parity-paths.md`, keyed by
the origin remote URL, so worktrees and second checkouts resolve to one entry.

The original resolves in this order: the recorded path, a sibling directory of
the current repository, then a check by `git remote -v` against the declared
original. Where none resolves, the caller asks the user and records the
answer, and a reader that cannot ask returns `original not found` with what it
tried. A comparison against a guessed original proves nothing.
check: tests/text/test_review_axes.py

## Three-way judgment

Where policy, the original and the new code diverge:

| Situation | Follow |
|---|---|
| Policy explicitly covers the divergence, and it holds up | **Policy**. Grounds means a quotable sentence with its source; "the document probably said so" is not grounds |
| Policy silent | **The original**, exactly |
| Grounds exist but look wrong | Neither silently: record both texts side by side and escalate |

Inherit before raising a product decision: where policy is silent and the
original already does the thing, follow it and mark it decided, since only a
rule in neither place needs a planner.
check: none reader: the parity review

## What the original sends

Where storage, query conditions and response assembly disagree inside the
original, its behavior is what it sends the client. Trace from the endpoint to
the finished response; a mid-layer condition that never changes the response
is reported as such and needs no reproduction. Read the original's history: a
later fix is its intent, and cloning the version before it preserves nothing.
check: none reader: the parity review

## The original's coordinates

A work item's design cites, in its Grounding, the original's coordinates for
the clauses in scope. Start every comparison there instead of searching the
original; the caller pins what it settles with a test. A suspect coordinate
is opened at the baseline: `git show <baseline>:<path>`.
check: none reader: the parity review

## Replacement annotation

Every ported entry point states, where its API docs render (the handler
docstring, say), **what it replaces**: the original's method, path and
function. That line declares the default, the original's business logic, so a
divergence grounded in policy is listed right below it. A 1:N split names the
branch each new handler took, an N:1 merge lists every original, a partial
port states what it left behind, and an addition reads `none (new)` with its
grounding clause.
check: none reader: the parity review

## Parity review

`code-review` runs as usual with one change of frame: stage 1 compares against
the original, through the coordinates the design cites, and not only the
written design, across the same comparison axes. A verdict is one of four
words, lowercase, at the start of its line, and no other label is written:

```
differs     no grounds: align with the original
grounded    differs with grounds: quote them and confirm intent
equivalent  a different implementation, the same observable behavior
unread      the original or the policy was not found: never a pass
```

check: tests/text/test_the_record_is_written_in_words.py

## Recording the comparison

The comparison is recorded in the tree, by the party that compared, once
coordinates were opened, behavior read and verdicts given; the tracer and
the crafter record none. Where the pull request changes a path outside `docs/`
and `seal/`, the record is an `original:` line naming the migration config's
`Baseline commit`, and where it lands follows the routing answer:

| The declaration says | Who writes the `original:` line, and where |
|---|---|
| through the review chain | the proofer, in the round block of each round record |
| straight to the PR | the sealer, in the verdict block each of its runs appends to `guarantee.md` |

The pull-request check reads that line (`docs/the-review-record.md` *The
round record*). A proofer that could not resolve the original writes no line
and raises an `unread` finding, and a sealer that could not compare writes a
`withheld` verdict naming it (`agents/sealer.md`). A line for work nobody
compared turns
*nobody checked* into *someone checked and it was fine*.
check: tests/text/test_review_axes.py
