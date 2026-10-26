# Implementation Plan: settle runs in local mode (#955)

Approved 2026-10-27 by the orchestrator, when `smith` was spawned.

## Summary

`settle` stops refusing a `seal/` root under the common git directory. It
reads the local work items there, calls one released when the pull request
from its `routing.md`'s branch merged with a merge commit `--released-at`
reaches, orders the released specs by those merge commits, and removes the
released local directories whose records hold no open row. The settling
session's procedure does not change: it writes the committed policy root and
closes the rows, asking nobody. The skill, the script's docstring and the
stamp's docstring stop stating the refusal, and `spec.md` *Rule changes*
carries the two policy sentences the settle will write.

## Technical context

- **Where the root is resolved.** `settle.py#main` already resolves the root
  through `hooks/optin.py#home_at(root, common)` and then refuses where
  `home` is not `<root>/seal`. Removing that branch leaves `home` in hand, and
  `os.path.dirname(home)` is the records root of `spec.md` *In* item 2. The
  paths that change their base are every read of a work item's directory:
  `work_items`, `has_spec`, `open_rows`
  (`unverified_check.py#open_record_rows(records, None, "seal/specs/<id>")`,
  which joins its argument under the root it is handed, so handing it the
  common git directory lands on `<common>/seal/specs/<id>`), `closed_rows`,
  `apply`'s `shutil.rmtree`, and `timeline`'s spec read. The policy root,
  `facts`, `citations` and `write_after` keep `root`. `policy_root(root)`
  already resolves `seal/config.md` through the same `home_at`, so it reads a
  local config without a change (`unverified_check.py#config_at`).
- **Where released is read.** `settle.py#released` reads `git ls-tree` at the
  ref and is shared mode's. Local mode's reader sits beside it and is asked
  only where `home` is not `<root>/seal`. It loads `hooks/routing.py` by path,
  as `settle.py#load` loads every sibling, and reads each local
  `routing.md`'s `branch` with `routing.parse`. The `gh` query and its JSON
  shape were executed against this repository (`spec.md` *Grounding*, last
  row). The reachability test is the `git merge-base --is-ancestor` call
  `rule_changes.py#_ancestor` makes; the build may share it.
- **Where the order is read.** `rule_changes.py#order` reads the commits that
  add each `spec.md` and is untouched. The new function takes the
  `(id, merge commit)` pairs and sorts them by the commits' index in one
  `git rev-list --topo-order --reverse <ref>` run. `rule_changes.py#unordered`
  then takes those pairs as it takes `order`'s.
- **What `survey` hands `apply`.** `apply` reads the candidates from the tree
  again and takes only `found["released"]` from `survey` (`settle.py#survey`
  docstring), which is still the one fact only git, and here `gh` with git,
  answers.
- **How the cases reach `gh`.** The suite takes `gh`'s login away at import
  (`tests/conftest.py`, `gh_answers`), so every local-mode case stubs `gh`:
  a stub directory on `PATH` for a subprocess run, or a replaced function for
  an in-process one. Which is the build's.
- **The failure scenario of the chosen approach, six months on.** A
  local-mode repository that squashes, as most GitHub repositories do,
  reuses a short branch name such as `fix/typo` for a second work item after
  the first one's pull request merged and before a settle removed the first.
  The second work item reads as released, and `--apply` removes its
  directory from the git directory, where no commit holds it. The one-issue
  flow cuts `feat/<issue>-<slug>` once per issue, so the shape needs a branch
  named by hand; `spec.md` *In* item 11 states it as a limit, and
  *Alternatives considered* holds the guard that was not built.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the refusal. The premise that would keep it is the refusal's two reasons: no ref holds a local directory, and nothing removed can be recovered | The first premise is true, and it stops only the shared reading of released: the pull request's merge commit does reach the ref (executed, `spec.md` *Grounding*). The second is true and does not matter: a work item's role ends when it ships and its directory is safe to delete once its rows are moved out (`skills/implement/SKILL.md` *Document layout*, `seal/README.md` lines 12 to 14). Kept, a local-mode repository's policy root never changes, which is #955's own problem | rejected: the premise checked does not hold the structure |
| Released means the pull request from the `Branch` row merged, its merge commit reachable from `--released-at`, asked of `gh` | A host `gh` cannot ask, or a branch reached without a pull request, never settles in local mode; a reused branch name releases the later work item early (*Technical context*) | **chosen**: one fact, read the same way whatever the merge method, and its limits are shapes the one-issue flow does not make |
| Released means the branch tip, or the commit `guarantee.md` audited, is reachable from `--released-at` | A squash merge leaves neither reachable, so a squashing repository never settles. Worse, a branch cut a minute ago with no commits of its own is an ancestor of the ref, so its new work item reads as released and `--apply` removes it, with no commit to bring it back | rejected; Q1 asks whether the audited commit should be a second source beside `gh` |
| The settling session names the work items to remove (`--work-item ID`) | The one destructive act is guarded by no fact the script reads; a mistyped id removes an unshipped record, and no commit holds it | rejected |
| Move the root into the tree for the settle (`seal mode shared`, settle, `seal mode local`) | The records enter the repository's history, which is the one direction local mode exists to prevent (`docs/one-root-by-lifetime.md` *Shared or local*) | rejected |
| Order local specs by work item id, the creation order, and mark every pair unordered | A work item created later and merged first is listed first, and every group prints one unordered line for each pair of its specs, for the settling session to resolve by content | rejected: the merge commits are already in hand and give the merge order itself |
| One `gh pr list --state merged --limit <n>` call matched by head branch, in place of one call per branch | A work item whose pull request is older than the newest n merged ones reads as unreleased for good | rejected: one exact query per local branch; a local root holds tens of work items |
| Guard a reused branch name: a pull request merged before the work item's id, its creation time in epoch seconds, is not its pull request | none found; it costs one comparison | rejected under the owner's standing direction that an edge case the one-issue flow cannot produce gets a limit sentence, not a guard |
| Take a `seal export` copy before `--apply` in local mode, as a procedure step | A step that protects nothing the tree says must survive, and a zip for the person to manage at every settle | rejected: the dry run names `seal export` for whoever wants a copy |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `settle` and `settle --apply` run in local mode: the refusal goes, the records root, released through `gh` with the three unreleased states and the `gh` refusal, the spec read from disk, the merge-commit order in `rule_changes.py`, the dry run's local lines and the settled local root (`spec.md` *In* items 1 to 9). In the same commits, `settle.py`'s docstring and `skills/settle/SKILL.md` state it, with the three limits (*In* items 10 and 11) | S1 to S10, each case seen red first; the modules `tests/test_settle.py`, `tests/test_rule_changes.py` and `tests/test_settle_reads_before_it_removes.py` run green | e1815c53 |
| 2 | What else stood on the refusal: `seal_stamp.py#queue_for_written_guarantee`'s docstring rewritten (*In* item 10), and a `git grep` for every remaining statement that `settle` refuses or retires no local-mode work item, outside `docs/` and `seal/specs/`, each rewritten or named in the phase record. S12 run over this `spec.md` | S11 and S12; `tests/test_seal_stamp.py` runs green | |

## Operational impact

- **A local-mode settle needs `gh`**, on `PATH` and logged in to the
  repository's GitHub host. Without it `settle` exits 2 in local mode and
  says so. Shared mode never asks `gh`.
- **No migration, no new configuration row, no new dependency.** The flags
  and the exit codes keep their meanings.
- **What `--apply` removes in local mode is under the git directory**, and no
  commit holds it. The dry run says so and names `seal export`.
- **The policy sentences change at a settle, not here.** `docs/` is the
  policy root and this pull request does not edit it: `spec.md` *Rule
  changes* carries the new paragraph of `docs/the-record-layout.md` and the
  corrected reason in `docs/the-review-record.md` *The stamp*, and the next
  release's settle writes both, changing the pin in
  `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` with it.
