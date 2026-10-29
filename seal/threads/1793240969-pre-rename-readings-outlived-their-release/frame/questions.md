# Questions for the planner: 1793240969-pre-rename-readings-outlived-their-release

## Judgments the ticket left open that the tree answered

- **Whether anything still holds the old inputs.** The issue asks for this to
  be measured first. Measured on 2026-10-29 after `git fetch origin`
  (executed): no commit outside `origin/main` on the two remote branches or
  the seven local ones carries `SpecSeal-Routing`, and no `routing.md` on any
  of them answers `Implementation` with `smith`. Both readings go.
- **The census item for the old key stays, against the issue's first
  acceptance line.** `docs/the-routing-check.md:101` spells the key, a pull
  request does not edit the policy root (`skills/implement/SKILL.md`
  *Document layout — two roots, three lifetimes*), and `old_names` would flag
  that line on this pull request's own run without the item. S1's case
  spells the key too. The item's comment is rewritten to name those two
  readers (`frame/plan.md` Alternatives D).
- **The pinning cases are rewritten into their opposites, not deleted.** The
  issue's second acceptance line asks for a case. The run's rule allows a
  red-first case for new behaviour only, and `routing.md` *Why this way*
  calls this a change to what the two readers accept. Both point at the same
  case, so the old case is rewritten in place (`frame/plan.md`
  Alternatives B and C).
- **The policy sentence on the old key is not edited by this pull request.**
  It is a `remove` in `frame/design.md` `## Rule changes`, which the settle
  after this release writes.
- **Who notices the `smith` reading's removal.** The only consumer of the
  parsed `implementation` is `hooks/implementer-notice.py#AXES`, so the
  removal costs a `smith` declaration its crafter reminder and nothing else
  (read).

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does this work also remove the other readings that a comment promised to drop in the minor release after the rename? They are the CLAUDE.md block markers that a release before the rename wrote (`install.sh` and `uninstall.sh` `OLD_START` and `OLD_END`, the old-marker row of `skills/update/SKILL.md`, pinned by `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py`), and the old clone line of a workflow (`skills/implement/scripts/seal.py#OLD_PLUGIN_CLONE`, described in `templates/setup/hygiene.yml` and `README.md`, pinned by two cases of `tests/skills/test_seal.py`). No issue schedules them (executed, `gh search issues`). The tree cannot answer it: unlike the two readings in scope, these read files in a person's own install, which stay as written until that person reruns the installer, so how long a straight upgrade from a release before 0.23.0 is supported is a product decision | a person | (a) Leave them out of this work. The build touches none of those files, `gaps.md` *Not done* names each with its coordinate, and the orchestrator files one issue for them, since an agent posts nothing. (b) Fold them in as a third phase. That removes the readings, their cases and their `KEPT_OLD_NAMES` items, and edits `install.sh`, `uninstall.sh`, `skills/update/SKILL.md`, `seal.py`, `templates/setup/hygiene.yml` and `README.md`, which widens where this work meets its siblings. A person upgrading from before 0.23.0 then gets a second CLAUDE.md block appended. (c) Keep them, and rewrite each comment to name a release the owner picks. The readings stay, and the comment shape that already failed once is repeated | (a): the build does not touch those files, `gaps.md` *Not done* names them, and the orchestrator files the issue | open |
