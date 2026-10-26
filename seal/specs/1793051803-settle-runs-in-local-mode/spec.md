# Feature Specification: settle runs in local mode

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | The local-mode settle asks nobody, as the shared one does. The settling session decides from the tree and the owner reviews the settle's pull request |
| `skills/settle/SKILL.md` *settle — write each section's latest decision*, the paragraph "It refuses to run in local mode", and `skills/settle/scripts/settle.py#main` (the branch printing "which is local mode") | The refusal this work removes. It stands on two reasons: no ref holds a local work item's directory, so nothing can be called released, and nothing removed can be recovered from git |
| `skills/settle/scripts/settle.py#released` | Shared mode's reading of released: a work item whose directory is present at `--released-at` (`git ls-tree`). A local directory is under the git directory and is present at no ref, so this reading returns nothing for it. Kept for shared mode |
| `skills/settle/scripts/settle.py#main`, the `--released-at` refusal | "Without it every work item reads as unreleased and this would report nothing to settle, which is the one answer it must not give by accident." A local-mode reading that cannot ask its source exits 2 for the same reason |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, the `seal/specs/<work-item-id>/` row, and `seal/README.md` lines 12 to 14 | A work item's role "ends when this work ships", and its directory "is safe to delete wholesale once its open rows have been moved out". So a removal that no commit can undo loses nothing that has to survive, once the settling session has closed every row. This answers the refusal's second reason |
| `skills/settle/SKILL.md` *The index* | "A settling session that creates the policy root writes the index with it." The script has written no policy document since #1033, so a local-mode repository with no `docs/` gets one from the settling session |
| `skills/settle/SKILL.md` *The settling session's procedure* and *A settle is not a work item* | Kept whole for local mode. The settle edits under `seal no-work-item`, and its trailer is owed only where the root is shared |
| `skills/commit-pr-convention/SKILL.md`, the paragraph opening "A session's commit in a repository whose root is shared" | "In local mode a commit carries none." The local-mode settle's commits carry no `SpecSeal-Routing:` trailer |
| `seal/README.md` lines 26 to 32 and `templates/hygiene.yml` lines 13 to 20 | `seal pr-checks install` writes the workflow only where the root is in the tree. Where a copy stays after a switch to local mode, every step examines nothing and passes. So the local-mode settle's pull request, which changes the policy root alone, meets no predicate that reads a removal |
| `skills/verify/scripts/unverified_check.py#absent_root` and `skills/code-review/scripts/chain_check.py#declared_for_this_branch` | The two pull-request readers over a tree with no `seal/`: the first prints that nothing is declared, the second that the pull request declared neither way. Neither fails |
| `skills/settle/scripts/rule_changes.py#order` and `rule_changes.py#unordered` | Shared mode's merge order is the first commit on `--released-at` that adds a spec. An id no commit adds gets commit None, and every pair holding a None is marked unordered. A local spec is added by no commit, so the build needs another source of order |
| `docs/the-review-record.md` *The stamp*, the sentence "That last keeps a `sealed` written long ago quiet, since `settle` retires no local-mode work item", and `skills/verify/scripts/seal_stamp.py#queue_for_written_guarantee`'s docstring, which says the same | Both stand on the refusal. The policy sentence changes through `## Rule changes` below. The docstring is rewritten in place by the build |
| `tests/conftest.py#gh_answers` and `CONTRIBUTING.md` *Running the checks*, "A case that needs `gh` stubs it." | The suite runs with `gh` logged out, so every case of this work that reaches `gh` stubs it |
| `seal/specs/1792993972-settle-writes-each-sections-latest-decision/spec.md` *Scope*, *Out*, the bullet "Local mode (#955)" | #1033's frame named this work's coordinates: `settle.py#main`, `settle.py#released`, the SKILL paragraph, *The stamp*, the `settle` rows of both READMEs and two test cases. Each is answered in *Scope* below; the README rows state nothing about local mode (read: `README.md` line 262, `README.ko.md` line 252), so they do not change |
| executed: `gh pr list --head feat/1033-settle-writes-each-sections-latest-decision --state merged --json number,mergeCommit` in this repository | It returned `[{"mergeCommit":{"oid":"91d570289b8a0770a130978a96e84d69ba2aaee4"},"number":1035}]` for a pull request that was squashed into `release/v0.22.4`. `git merge-base --is-ancestor` of that commit exits 0 against `HEAD` and 1 against `origin/main`. So the merge commit names a squash merge, and its reachability says released at one ref and not at another, which is the shared reading's meaning of `--released-at` |

## Scope

**The design in one paragraph.** In local mode the work items sit under
`$(git rev-parse --git-common-dir)/seal/specs/`, and no commit holds them.
`settle` reads them there. A local work item is released when the pull
request from the branch its `routing.md` names merged, and that pull
request's merge commit is reachable from `--released-at`. The GitHub
command-line tool, `gh`, names the merge commit whatever the merge method
was, and git says whether `--released-at` reaches it. The merge commits also
give the merge order the groups are listed in. The settling session then
follows *The settling session's procedure* unchanged: it writes the
repository's committed policy root (`docs/` unless `Policy root` names
another), creating it with its index where it is absent, and closes every
open row. `settle --apply` removes each released local directory whose
record holds no open row, from the git directory. Nothing else about local
mode changes: the settle's pull request is an ordinary one, and its commits
carry no trailer, as no local-mode commit does.

### In

1. **The refusal goes.** `settle.py#main` loses the branch that exits 2 for a
   root in local mode. The no-root and opt-out refusals stay as they are.
2. **One records root.** `settle.py` reads and removes every
   `seal/specs/<id>/` path under the directory that holds the resolved
   `seal/` root, `os.path.dirname(home)`: the repository's top in shared
   mode, the common git directory in local mode. Every other read stays on
   the repository's top: the policy root, the tracked files `citations`
   scans, and `tests/`. The printed coordinates keep the form
   `seal/specs/<id>/...`, which the agent contract's rule 11 resolves by
   mode.
3. **Released, in local mode.** For each local work item, `settle` reads the
   `Branch` row of its `routing.md` with `hooks/routing.py#parse`, then asks
   `gh pr list --head <branch> --state merged --json number,mergeCommit`
   from the repository's top, once per branch. The work item is released
   when a listed pull request's `mergeCommit` is reachable from
   `--released-at` (`git merge-base --is-ancestor <oid> <ref>`). Three
   states read as unreleased, and the dry run names which: no `routing.md`
   or no `Branch` row; no merged pull request from that branch; and no
   listed merge commit reachable from `--released-at`. An unreleased work
   item is untouched, as in shared mode. Shared mode never asks `gh`.
4. **`gh` that cannot be asked is a refusal.** Where `gh` is not on `PATH`,
   or a query exits non-zero, `settle` exits 2 in local mode with one
   sentence naming `gh` and its message, and reads and removes nothing.
   Every local work item reading as unreleased would be the quiet zero the
   `--released-at` refusal is written against.
5. **The spec read.** In local mode each `spec.md` is read from its
   directory, since no ref holds it. In shared mode it is still read as
   `--released-at` holds it.
6. **The merge order, in local mode.** The released local specs are ordered
   by their merge commits' place in
   `git rev-list --topo-order --reverse <ref>`, and `rule_changes.py#unordered`
   is asked of those merge commits, so two merges no ancestry orders are
   marked as they are in shared mode. `rule_changes.py` gains the one
   function that sorts `(id, commit)` pairs this way, beside `order`, which
   keeps shared mode's reading.
7. **What the dry run adds in local mode.** Its first line names the root's
   path and says it is local mode. Each released local work item is listed
   with its pull request's number and its merge commit, so the settle's pull
   request body can cite them. Each unreleased one is listed with which of
   the three states of *In* item 3 holds. The heading of what `--apply`
   removes says, in local mode, that no commit holds those directories and
   that `seal export` takes a copy for whoever wants one. Everything else
   the dry run prints is as in shared mode.
8. **`--apply` in local mode.** It removes each released local directory
   whose record holds no open row in the working tree, keeps and names one
   that holds a row, and exits as in shared mode: 0 when it kept nothing, 1
   when it kept a directory, 2 when the arguments or the tree are unusable.
   It writes no policy document. It prints `fold-check`'s lines after the
   removals where the policy root exists, as today.
9. **The settled root, in local mode.** `settle.py#SETTLED`, printed where
   the root holds no work item, names the local root's path in local mode.
   Its clause about a fresh checkout holding no `seal/specs/` is said in
   shared mode only, since a checkout carries no local root.
10. **The text that states the present behaviour is rewritten in the same
    commit as the code**: `settle.py`'s module docstring (the paragraph
    "Local mode is refused rather than reported on", the opening "Released
    means present on the branch the release merges to", and the exit-2 list,
    which drops "a root in local mode" and gains a `gh` that cannot be
    asked); `skills/settle/SKILL.md`, whose paragraph "It refuses to run in
    local mode" becomes a section stating *In* items 2 to 8 and the limits
    below, and whose *What the dry run shows* sentence on a spec's place in
    the order names the local source; and
    `skills/verify/scripts/seal_stamp.py#queue_for_written_guarantee`'s
    docstring sentence "since `settle` retires no local-mode work item".
11. **The limits, stated in `skills/settle/SKILL.md` as sentences, with no
    guard.** A work item whose branch reached `--released-at` without a pull
    request reads as unreleased, and its directory is removed by hand. A
    repository on a host `gh` cannot ask cannot settle in local mode, and
    the exit-2 sentence says so. A branch name a later work item reuses
    after an earlier pull request from it merged reads that later work item
    as released; the one-issue flow cuts one branch per issue, so it never
    produces this.

### Out

- **Running a settle**, in this repository or in a local-mode one. A settle
  is not a work item (`skills/settle/SKILL.md` *A settle is not a work
  item*).
- **A second source of released**, such as git ancestry of the branch tip or
  of the commit `guarantee.md` audited. `plan.md` *Alternatives considered*
  weighs it, and `questions.md` Q1 holds the person's answer.
- **A guard for a reused branch name.** The one-issue automation flow cannot
  produce it, so it is a limit sentence (*In* item 11).
- **A copy taken before `--apply`.** The tree says the records end their role
  when the work ships (*Grounding*), so the procedure gains no export step;
  the dry run names `seal export` for whoever wants a copy.
- **`README.md` and `README.ko.md`.** Their `settle` rows state nothing about
  local mode, and the skill is the one place the command's local-mode
  behaviour is stated.
- **`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`'s pin of
  "`settle` retires no local-mode work item".** It reads
  `docs/the-review-record.md`, which this pull request does not edit. The
  settle that writes the *The stamp* section changes that pin, as step 8 of
  the settling session's procedure says.
- **Shared mode.** Every shared-mode behaviour of both commands stays as
  #1033 left it.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a released and an unreleased local item | Given a repository whose root is local, holding two work items, each with a `routing.md` naming its branch and a `spec.md` with one `change`, and a `gh` stub answering a merged pull request with a merge commit reachable from `--released-at` for the first branch and none for the second. When `settle` runs, then it exits 0, its first line names the local root, the first item is listed released with its pull request number and merge commit and its operation appears in a group, the second is listed unreleased because no merged pull request came from its branch, and nothing is written or removed | a case in `tests/test_settle.py`, seen red against the current refusal |
| S2 the merge order | Given two released local items whose operations name one section, their merge commits on one line of history with the later-created item merged first. When `settle` runs, then the group lists the earlier-merged item first and marks no pair unordered; when the two merge commits sit on two branches no ancestry orders, the pair is marked unordered | cases in `tests/test_settle.py`, and a case in `tests/test_rule_changes.py` for the new ordering function, each seen red |
| S3 a merge commit the ref does not reach | Given a local item whose branch's pull request merged into a branch `--released-at` does not reach. When `settle` runs, then the item is unreleased with that reason, and `--apply` keeps it | a case in `tests/test_settle.py`, seen red |
| S4 `--apply` in local mode | Given S1's repository, the released item's record holding no open row, and a third released item whose `overview.md` holds an open row. When `settle --apply` runs, then the first item's directory under the common git directory is gone, the third is kept with its row named, the unreleased one is untouched, nothing under the repository's top is removed or written, and the exit is 1; once the row is closed on disk, a second run removes the third and exits 0 | cases in `tests/test_settle.py`, seen red |
| S5 `gh` that cannot be asked | Given a local root with a work item, and a `gh` that is absent from `PATH` or exits non-zero. When `settle` or `settle --apply` runs, then it exits 2, its sentence names `gh` and its message, and nothing is removed | cases in `tests/test_settle.py`, seen red |
| S6 shared mode is untouched | Given a shared root. When either command runs, then `gh` is never asked and every existing shared-mode case passes unchanged | the existing cases of `tests/test_settle.py`, passing unchanged, and a case asserting no `gh` call in shared mode |
| S7 an item with no branch | Given a local item with no `routing.md`, and one whose `routing.md` has no `Branch` row. When `settle` runs, then both are unreleased with that reason, and `gh` is not asked for them | a case in `tests/test_settle.py`, seen red |
| S8 the settled local root | Given a local root whose `seal/specs/` holds no work item. When either command runs, then it exits 0 and names the local root, and says nothing about a fresh checkout | a case beside the `an-empty-root-is-settled` cases, seen red |
| S9 no policy root | Given a local-mode repository with no `docs/` and one released local item whose spec `add`s a new document. When `settle` runs, then it exits 0 and the group's place says the heading is not in the working tree; `settle --apply` removes the item and prints no `fold-check` lines | a case in `tests/test_settle.py`, seen red against the current refusal |
| S10 the documents say the new fact | Given `skills/settle/SKILL.md` and `settle.py`'s docstring. Then neither says settle refuses local mode; the skill states *In* items 2 to 8 and the three limits of *In* item 11; the docstring's exit-2 list names a `gh` that cannot be asked and no longer names a root in local mode | `tests/test_settle_reads_before_it_removes.py::test_the_module_and_the_skill_both_say_local_mode_is_refused`, rewritten to these assertions and seen red against the current text |
| S11 the stamp's docstring | Given `skills/verify/scripts/seal_stamp.py#queue_for_written_guarantee`. Then its docstring no longer says `settle` retires no local-mode work item, and gives the reason the branch keeps an old `sealed` quiet as the rule change below states it | read by the warden; `git grep -n "retires no local-mode"` outside `docs/`, `tests/` and `seal/specs/` returns nothing |
| S12 the rule changes parse | Given this `spec.md`. When `rule_changes.py#parse` reads it, then its `## Rule changes` parses, and each `from` is found in its section of the policy root | run by the smith |

## Data & interfaces

- **`bin/settle`'s flags do not change**: `settle`, `settle --apply`,
  `--released-at REF` (default `origin/main`), `--root DIR`. In local mode
  `--released-at` names the ref the merge commits must be reachable from.
- **`settle.py`** gains: the records root of *In* item 2; a reader of
  released for local mode returning, for each local id, its pull request's
  number and merge commit, or which unreleased state holds; the `gh` refusal
  of *In* item 4; `hooks/routing.py` in `PURPOSES`, for the sentence `load`
  prints when it is missing. It loses the local-mode branch of `main`.
  `released` keeps its shared-mode reading. The dry run's new lines are the
  build's to word and the cases' to pin; *In* item 7 names what each holds.
- **`rule_changes.py`** gains one function, beside `order`, that sorts
  `(id, commit)` pairs by the commits' place in
  `git rev-list --topo-order --reverse REF`. `order`, `unordered`, `group`
  and the grammar do not change.
- **The `gh` query** is
  `gh pr list --head <branch> --state merged --json number,mergeCommit`,
  run from the repository's top, which yields a list of
  objects holding `number` and `mergeCommit.oid` (executed against this
  repository, *Grounding*).

## Rule changes

- add
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  to: **In local mode the settle reads the work items under the common git
    directory, and a work item is released when the pull request from the
    branch its `routing.md` names has merged, its merge commit reachable
    from `--released-at`.** No ref holds a local work item's directory, so
    presence at `--released-at` cannot say that it shipped. What reaches
    that ref is its pull request's merge commit, which the GitHub
    command-line tool names whatever the merge method was, and the merge
    commits give the merge order. A work item with no `Branch` row, no
    merged pull request from its branch, or a merge commit `--released-at`
    does not reach is unreleased and stays. The settling session writes the
    committed policy root as in shared mode, creating it with its index
    where it is absent, and `settle --apply` removes each released local
    directory whose record holds no open row. No commit holds what it
    removes, and none needs to: a work item's records end their role when
    it ships, and the settling session closes its rows first. The settle's
    pull request changes the policy root alone, so no check reads a removal
    there, and its commits carry no trailer, as no local-mode commit does.
    check: tests/test_settle.py
- change
  file: docs/the-review-record.md
  section: The stamp
  from: since `settle` retires no local-mode work item
  to: since a local-mode work item stays under the root until the settle
    after its release removes it

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The local-mode refusal | `skills/settle/scripts/settle.py#main`, the branch whose message says "which is local mode" | `settle` reads the local root (*In* items 1 to 8) |
| The refusal's statements in the module and the skill | `settle.py`'s module docstring, the paragraph "Local mode is refused rather than reported on" and "a root in local mode" in its exit-2 list; `skills/settle/SKILL.md`, the paragraph "It refuses to run in local mode" | rewritten in place to the local-mode section of *In* item 10 |
| The case pinning the refusal | `tests/test_settle.py::Test_main::test_refuses_local_mode_rather_than_reading_an_empty_repository` | replaced by S1 and S5; its half that guards against telling a repository holding work items that it has none is kept in S1's assertions |
| The pin on the skill's refusal sentence | `tests/test_settle_reads_before_it_removes.py::test_the_module_and_the_skill_both_say_local_mode_is_refused`, its assertions "refuses to run in local mode", "seal mode shared" and "local mode" in the exit-code list | rewritten to S10 |
| The stamp docstring's reason | `skills/verify/scripts/seal_stamp.py#queue_for_written_guarantee`, the clause "since `settle` retires no local-mode work item" | rewritten in place to the reason the `## Rule changes` item for *The stamp* states |
| The stamp policy sentence's reason | `docs/the-review-record.md` *The stamp*, "since `settle` retires no local-mode work item" | the `## Rule changes` item above; the settle writes it, and changes the pin in `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` then |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-27 by framer, before the build.
