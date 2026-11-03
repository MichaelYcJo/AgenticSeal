# settle, in local mode

The settling session opens this file before the dry run, step 2 of
`skills/settle/SKILL.md` *The settling session's procedure*, where the
`seal/` root is under the common git directory.

## In local mode

**In local mode `seal settle` reads the work items under the common git
directory, and a work item is released when the pull request from the
branch its `routing.md` names has merged, its merge commit reachable from
`--released-at`.** No ref holds a local work item's directory, so presence
at a ref cannot say that it shipped. What reaches the ref is its pull
request's merge commit, whatever the merge method was.

- **Where it reads.** Every `seal/threads/<id>/` path is read and removed
  under `$(git rev-parse --git-common-dir)`, so a work item's directory is
  `<git-common-dir>/seal/threads/<id>/`, and it is printed as
  `seal/threads/<id>/`. The policy root, the tracked files the citations are
  read from, and `tests/` are read from the repository's top.
- **What released means.** `seal settle` reads the `Branch` row of each work
  item's `routing.md` and asks
  `gh pr list --head <branch> --state merged --json number,mergeCommit`
  from the repository's top, once per branch. A work item is unreleased,
  and untouched, in three states: no `routing.md` that `hooks/lib/routing.py`
  reads as a declaration naming a branch, no merged pull request from that
  branch, or no listed merge commit reachable from `--released-at`, a pull
  request listed with no merge commit among them. Shared mode asks `gh`
  only in `--apply`, for the release list, and only where a directory it
  would remove gets as far as a version tag (`skills/settle/SKILL.md` *What
  `--apply` does*).
- **A `gh` that cannot be asked stops the run.** Where `gh` is not on
  `PATH` or its query fails, `seal settle` exits 2 with one sentence naming `gh`
  and what it said, and reads and removes nothing. Every work item would
  otherwise read as unreleased, and the run would say there is nothing to
  settle.
- **The design and the order.** Each `frame/design.md` is read from its directory,
  since no ref holds it. The released designs are listed by their merge
  commits' place in `git rev-list --topo-order --reverse` of
  `--released-at`, and two whose merge commits no ancestry orders are marked
  `unordered`.
- **The judgments earlier settles removed.** `--apply` removes a local
  directory from the git directory, and no commit holds it, so the history
  holds an earlier plan only where the repository once committed its
  `seal/` root. Where none did, the section is not printed.
- **What the dry run adds.** Its first line names the root's path and says
  it is local mode. Each released work item is listed with its pull
  request's number and its merge commit, for the settle's pull request body
  to cite, and each unreleased one with which of the three states holds.
  The heading of what `--apply` removes says that no commit holds those
  directories, and that `seal export` takes a copy for whoever wants one.
- **What `--apply` does.** It removes each released local directory whose
  record holds no open row, from the git directory, and keeps and names one
  that holds a row, with the exit codes `skills/settle/SKILL.md` *What
  `--apply` does* states. It
  reads no published note: no fragment is committed in local mode, so no
  note is built from the history. No
  commit holds what it removes, and none needs to: a work item's records
  end their role when it ships, and the settling session closes its rows
  first.
- **The settling session's procedure is the same.** It writes the
  repository's committed policy root, and creates it with its index where
  it is absent (`skills/settle/rule-changes.md` *The index*).

**The limits, which no guard covers.** A work item whose branch reached
`--released-at` without a pull request reads as unreleased, and its
directory is removed by hand. A repository on a host `gh` cannot ask cannot
settle in local mode, and the exit-2 sentence says so. A branch name that a
later work item reuses, after an earlier pull request from it merged, reads
that later work item as released. So does a merged pull request from a fork
whose branch has the same name, since `gh pr list --head` matches a branch's
name and not its owner. The one-issue flow names each branch after its
issue, which makes either match unlikely; it does not rule out the second,
because the flow does not name a fork's branches.
