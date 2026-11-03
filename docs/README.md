# docs/

The standing policy, one directory per group of documents and one table per
group, each group holding what one kind of reader opens at one kind of step.
A `docs/` document outranks the work items' designs. A design that finds one
wrong states the correction in its `## Rule changes`
(`skills/settle/rule-changes.md` *Rule changes*), unless its work item's
subject is the policy root itself; which kind of work item edits a document
directly and which states the correction is in `skills/implement/SKILL.md`
*Document layout — two roots, three lifetimes*.

## docs/forms/

Two parties that exchange a record open these: the one that writes it and the
one that reads it.

| File | The question it answers |
|---|---|
| `docs/forms/the-round-record.md` | what a review round leaves in the tree: the proofer writes it, the crafter closes its findings, and `chain_check.py` reads it at the pull request |
| `docs/forms/the-guarantee.md` | what the sealer's verdict holds: the sealer writes it, and the orchestrator and the pull request check read it |
| `docs/forms/the-reader-registry.md` | how a frame names what its work removes |

## docs/running/

The orchestrator opens these while it runs a work item, and an agent opens
the one section its definition, the contract or a skill it opens sends it to.

| File | The question it answers |
|---|---|
| `docs/running/the-run.md` | the orchestrator's rules for the review chain's run, its bound and end, and for what it hands each agent |
| `docs/running/the-agent-set.md` | how the rules are split between the agents a work item spawns |
| `docs/running/the-review-and-parity-arms.md` | what each routing answer owes at the pull request, and what the parity arm wants of a change in a migration |
| `docs/running/the-broad-gate.md` | who takes the one broad run, what it runs, and what it may say |
| `docs/running/what-a-script-gates.md` | which gates a script holds and which an agent holds, what each script reads, and what it does with what it did not read |
| `docs/running/measuring-a-run.md` | what a segment of a run measures, how a reading that moved is judged, and where the reading goes |

## docs/releasing/

The orchestrator and the owner open these at a release and its settle.

| File | The question it answers |
|---|---|
| `docs/releasing/branch-and-release.md` | where a branch is cut from, how it merges back, and what carries the version |
| `docs/releasing/issues-and-milestones.md` | what the issue tracker's fields mean here, and which of them anything reads |
| `docs/releasing/release-checklist.md` | what to type on the day of a release, in order |

## docs/checks/

A person who changes a hook or a script opens these, and so does the
settling session. No agent acts on them: where the contract or a skill an
agent opens cites one, the citing text already states what the agent does,
and the citation gives the reason.

| File | The question it answers |
|---|---|
| `docs/checks/the-pull-request-check.md` | what `chain_check.py` reads at a pull request, for a person who changes it |
| `docs/checks/the-stamp.md` | what the stamp hooks and `seal_stamp.py` draw, for a person who changes them |
| `docs/checks/the-fold.md` | what `seal settle` and `seal fold` read to tell a settle from a deletion |
| `docs/checks/the-unverified-record.md` | what `unverified_check.py` reads, and the baseline it reads against |
| `docs/checks/the-routing-check.md` | where a session's routing is checked: at its edit tools before the first edit, and at the pull request |
| `docs/checks/the-session-hooks.md` | how the hooks are registered, and what the implementer mark says |

## docs/layout/

Whoever sets a repository up opens these, and so do the framer, the crafter
and the orchestrator where they place or write a record.

| File | The question it answers |
|---|---|
| `docs/layout/one-root-by-lifetime.md` and `docs/layout/one-root-by-lifetime.ko.md` | where the plugin's one root is, what opts a repository in, what first setup asks, and what the repository's config rows decide |
| `docs/layout/the-record-layout.md` | where each kind of record lives, which file a change writes, and when a later commit brings the changelog fragment along |
| `docs/layout/the-pact.md` | where a contract several repositories keep together lives, how each knows about it, and what checks it |

`docs/experiments/` holds dated scratch documents and is no policy; `settle`
never writes there.
