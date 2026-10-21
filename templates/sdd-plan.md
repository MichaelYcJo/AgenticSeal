# Implementation Plan: <work item>

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md holds HOW, in phases. It
is the Design Gate's artifact: where the work alters observable behaviour,
approval of this plan is the gate. -->

Approved <date> by <who>, when `smith` was spawned.

<!-- The line above is the record that the gate happened. The orchestrator
writes it when it spawns the build, in the shape and on the terms
`skills/implement/orchestration.md` *The plan is approved at the spawn*
states, including the shape where `routing.md` answers `Implementation`
with `the session`. A later session, a reviewer and CI all read the tree,
and a plan with nobody's name on it cannot be told from one nobody approved.
The line shares its shape with `templates/sdd-routing.md`'s `Answered <date>
by <who>, before the first edit.`: the verb, the date, who, and the moment.
The two are pinned against each other, so neither spelling can drift into a
second convention for one kind of fact. -->

## Summary

## Technical context

Existing code this builds on (file:line coordinates), constraints, and the
failure scenario of the chosen approach ("what breaks in 6 months").

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| | | |

## Phases

Vertical slices: each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | | | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past
one, which someone can open.

The party that builds a phase fills its cell as the phase closes, not at the
end. A phase reconstructed afterwards is reconstructed from the diff, which is
where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. The party that builds the phase
writes it to `seal/specs/<work-item-id>/phases/phase-N.md`, from
`templates/sdd-phase.md`, when the phase closes.

Where feature branches squash, these commits stop resolving at the merge, and
**a rebase during the work does the same thing earlier and more quietly**,
because the orphaned object still answers `git cat-file` in the worktree that
wrote it. **The party that rebases the branch re-reads this column after the
rebase**, or the column names commits that resolve in one clone and nowhere
else. Nothing measures from this column, which is why that is tolerable.

## Operational impact

Migrations, new environment variables, new dependencies and compatibility
breaks: the items a deployer must not miss.
