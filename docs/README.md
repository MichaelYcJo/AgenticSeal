# docs/

The standing policy, one row per topic. A `docs/` document outranks the work
items' specs, and a spec that finds one wrong states the correction in its
`## Rule changes` (`skills/settle/SKILL.md` *Rule changes*).

| File | The question it answers |
|---|---|
| `docs/branch-and-release.md` | where a branch is cut from, how it merges back, and what carries the version |
| `docs/commit-review-gate-spec.md` | how the gates are registered, what the PreToolUse reading of a commit decides where git cannot, and what the implementer mark says |
| `docs/issues-and-milestones.md` | what the issue tracker's fields mean here, and which of them anything reads |
| `docs/measuring-a-run.md` | what a segment of a run measures, and where the reading goes |
| `docs/one-root-by-lifetime.md` and `docs/one-root-by-lifetime.ko.md` | where the plugin's one root is, what opts a repository in, what first setup asks, and what the repository's config rows decide |
| `docs/release-checklist.md` | what to type on the day of a release, in order |
| `docs/the-agent-set.md` | how the rules are split between the agents a work item spawns |
| `docs/the-broad-gate.md` | who takes the one broad run, what it runs, and what it may say |
| `docs/the-commit-gate-inside-git.md` | what git decides inside a commit, what its hooks cannot see, and which reading judges each state of a repository |
| `docs/the-pact.md` | where a contract several repositories keep together lives, how each knows about it, and what checks it |
| `docs/the-reader-registry.md` | how a frame names what its work removes |
| `docs/the-record-layout.md` | where each kind of record lives, which file a change writes, when a later commit brings the changelog fragment along, and what tells a settle from a deletion |
| `docs/the-review-and-parity-arms.md` | what each opt-in arm of the commit gate wants, and the routing declaration that moves the review arm's check to the pull request |
| `docs/the-review-record.md` | what a review round leaves in the tree, what the pull-request check reads of it, the run's bound and end, and how work is handed to an agent |
| `docs/worktree-guard-spec.md` | what the worktree guard refuses, and why |

`docs/experiments/` holds dated scratch documents and is no policy; `settle`
never writes there.
