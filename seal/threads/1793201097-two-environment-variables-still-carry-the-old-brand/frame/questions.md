# Questions for the planner: 1793201097-two-environment-variables-still-carry-the-old-brand

## Answered by the tree, not to be reopened

- **The option's form is a `userConfig` entry of type `string` named
  `worktree_guard_language`, with no `default`, no `options` and no
  `required`.** The issue left the form to the manifest reference, read
  2026-10-29. `plan.md` alternatives B and C give why `options` and `default`
  are left out.
- **The guard reads the option, then `SPECSEAL_LANG`, then the locale, and an
  empty value counts as unset at each step.** So whether Claude Code exports
  an empty variable or none for an option nobody set does not change what is
  built.
- **This work changes no rule.** No document under `docs/` names either
  variable or the language of the guard's prompts (executed, `git grep`), so
  `frame/design.md` holds the no-change block.
- **#1096 stays in 0.24.0 although #1049 may remove the guard in 0.24.1.** The
  owner decided it on 2026-10-28
  (`seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/questions.md`,
  the bullet *#1096 stays in 0.24.0*, read). S5's case makes the option leave
  with the guard if #1049 removes it.
- **No file on #1053's list is edited.** The work touches
  `hooks/lint-python.py`, `hooks/worktree-guard.py`,
  `.claude-plugin/plugin.json`, `README.md`, `README.ko.md`,
  `tests/censuses.py`, `tests/conftest.py`, `tests/hooks/test_lint_python.py`,
  `tests/hooks/test_worktree_guard.py`, one new test file or case for S5, and
  this work item's own records. `templates/setup/config.md` is read for its
  bullet *The response language* and not edited.
- **`WORKTREE_GUARD_IDLE_MIN` stays as it is.** It carries no old name, and the
  issue names two variables.
- **The crafter writes the changelog fragment in phase 2**, as
  `agents/crafter.md` names `changelog.md` among its writes (read, line 19).

## Assumed, because no answer changes what is built

- **Nothing in this work schedules the removal of the `SPECSEAL_LANG` read in
  the next minor release beyond a comment at the read and the census
  comment**, the shape of `chain_check.py#OLD_TRAILER`. That shape has
  already failed once: `OLD_TRAILER` is due out in 0.24.0 and no issue
  schedules it (executed, `gh search issues`). Filing a tracker issue in the
  next minor release's milestone would change nothing this build writes, and
  filing it is the orchestrator's or the owner's act, not the crafter's.
- **Whether Claude Code opens a dialog for the new option when the updated
  plugin is enabled is not read.** The changelog fragment tells a person to
  set the option in `/config`, which is true either way.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does this work also remove `chain_check.py#OLD_TRAILER` and `hooks/lib/routing.py#OLD_BY_CRAFTER`, whose own comments say the minor release after the rename removes them, which is 0.24.0? The tree cannot answer it: the issue scopes this work to two environment variables, the two readings are old names of the same brand that the issue calls *the last names of the old brand the plugin reads*, and no issue in 0.24.0 schedules them (executed, `gh search issues` for `OLD_TRAILER` and `SpecSeal-Routing`) | a person | (a) Leave them out: this work stays on the two variables, and the two readings stay past the release their comments name until someone files them. (b) Fold them in as a third phase: removes the readings and their two `KEPT_OLD_NAMES` items, edits `chain_check.py`, which #1020 and #951 also edit before this work in the milestone's order, and widens what the review reads. (c) File a separate issue in 0.24.0 for them: the release keeps its word without widening this work | (a): the build does not touch `chain_check.py` or `hooks/lib/routing.py`, and the hand-back names the two overdue readings | open |
| Q2 | If #1053 merges into the release branch before phase 2 and changes where or how a work item's changelog fragment is written, which form does the fragment take? | the work | The crafter writes the fragment in the form the tree asks for when phase 2 runs, and records the change in the phase record. Before #1053 merges, that is `seal/threads/1793201097-two-environment-variables-still-carry-the-old-brand/changelog.md` | The form the tree asks for when phase 2 runs | open |
