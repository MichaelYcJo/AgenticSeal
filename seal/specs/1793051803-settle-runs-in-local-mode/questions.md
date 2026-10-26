# Questions for the planner: settle runs in local mode (#955)

## Answered by the tree

The ticket left these open, and the tree answers them. Each names where the
answer was read, so a reviewer can overturn it by opening the same place.

1. **A1 What released means for a local work item.** The pull request from
   the branch its `routing.md` names has merged, and its merge commit is
   reachable from `--released-at`. Shared mode's meaning is "present on the
   branch the release merges to" (`settle.py`'s module docstring), and a
   local directory is present at no ref; the merge commit is what reaches
   that ref, and `gh` names it for a squash merge too (executed, `spec.md`
   *Grounding*, last row). `plan.md` *Alternatives considered* weighs the
   other readings.
2. **A2 What `--apply` removes, and how it spares an unshipped work item.**
   Each released local directory whose record holds no open row, and
   nothing else. An unreleased one is untouched, and a `gh` that cannot be
   asked stops the run with exit 2 before anything is read, so a failed
   query never reads as "nothing released" (`settle.py#main`'s
   `--released-at` refusal states that rule for a ref).
3. **A3 Whether a removal no commit can undo is acceptable.** Yes. A work
   item's role ends when its work ships (`skills/implement/SKILL.md`
   *Document layout — two roots, three lifetimes*), and its directory is
   safe to delete once its open rows are moved out (`seal/README.md` lines
   12 to 14); the settling session closes every row before `--apply`. The
   dry run names `seal export` for whoever wants a copy.
4. **A4 Whether the local-mode settle's pull request trips a CI predicate.**
   No. It changes the policy root and nothing under `seal/`.
   `seal pr-checks install` writes the workflow only where the root is in the
   tree (`seal/README.md` lines 26 to 32), and where a copy stays, every step
   examines nothing and passes (`templates/hygiene.yml` lines 13 to 20,
   `unverified_check.py#absent_root`, `chain_check.py#declared_for_this_branch`).
   Its commits carry no trailer (`skills/commit-pr-convention/SKILL.md`).
5. **A5 How a local-mode repository with no `docs/` gets one.** The settling
   session creates the policy root and writes its index with it
   (`skills/settle/SKILL.md` *The index*). The script has written no policy
   document since #1033, so the issue's "created if absent" is the session's
   act, not the script's.
6. **A6 A team's own `docs/`.** Where a local-mode repository's `docs/` holds
   the team's own documents, the `Policy root` row names another directory
   (`templates/config.md`, the `Policy root` row).
7. **A7 The merge order of local specs.** Their merge commits' place in
   `git rev-list --topo-order --reverse <ref>`, with `rule_changes.py#unordered`
   asked of them, since no commit adds a local spec (`rule_changes.py#order`).
8. **A8 A reused branch name, a merge without a pull request, a host `gh`
   cannot ask.** Limit sentences in `skills/settle/SKILL.md`, no guard: the
   owner's standing direction for an edge case the one-issue automation flow
   cannot produce, and the flow cuts one branch per issue and opens its pull
   request on GitHub.

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Is `gh` the one source of released in local mode, or does the commit `guarantee.md` audited, reachable from `--released-at`, count too? The tree cannot answer it: no document says which hosts or which merge methods local mode supports, and local mode has no CI to say it for it. | a person | (a) `gh` alone. A local-mode repository on a host `gh` cannot ask never settles, and `settle` exits 2 there with a sentence saying so; a work item merged without a pull request stays until it is removed by hand. (b) `gh`, and where `gh` lists no merged pull request or cannot be asked, the audited commit's reachability as well; a `gh` that cannot be asked then stops nothing. A merge-commit or fast-forward flow settles without GitHub. It is a second reading of one fact, it covers only work items that reached a sealer, and the audited commit is only reachable where the merge kept it, so a squash still needs `gh` | (a) | open |
