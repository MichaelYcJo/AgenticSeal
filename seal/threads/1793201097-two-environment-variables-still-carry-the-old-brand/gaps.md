# Overview: 1793201097-two-environment-variables-still-carry-the-old-brand

## Why this work exists

The plugin read two environment variables named for the old brand; it stops reading `SPECSEAL_LINT`, and the guard's prompt language becomes the plugin option `worktree_guard_language`, with `SPECSEAL_LANG` read where the option is empty through 0.24.x.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Which scripts S5's case reads for an undeclared option | `frame/design.md` S5: "`hooks/worktree-guard.py` reads no `CLAUDE_PLUGIN_OPTION_` variable the manifest does not declare". The case reads every `.py` file under `hooks/`, `hooks/lib/` among them | Every script under `hooks/` | The same S5 row reads every declared option "under `hooks/`", and an option read by any hook script reaches a person the same way the guard's does. The wider reading holds the guard too, so nothing the row asks for is lost |
| What `claude plugin validate .` prints | `frame/design.md` S5 and `frame/plan.md` phase 2: "prints `Validation passed`". It exits 0 and prints `Validation passed with warnings`, with one warning: `CLAUDE.md at the plugin root is not loaded as project context` | The run is read as passing on the manifest | The same warning, and the same last line, print at `0c451b8c`, before the manifest changed (executed, over a `git archive` extract of that commit). The warning names `CLAUDE.md`, not `.claude-plugin/plugin.json` |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over the branch | the orchestrator, at its one `seal gate` run (contract rule 2) |
| That Claude Code hands the option to the guard's process as `CLAUDE_PLUGIN_OPTION_WORKTREE_GUARD_LANGUAGE`, and whether it exports an option nobody set as empty or not at all. The name is read from the manifest reference that `frame/design.md` *Grounding* cites, and the cases set the variable themselves | the owner, in the first session after updating with the option set to `ko`, where the guard's prompts read Korean with `SPECSEAL_LANG` removed from their settings |
| Whether Claude Code opens a dialog for the option when the updated plugin is enabled (`frame/plan.md` *Operational impact*); the changelog fragment claims neither way | the owner, at the first update to 0.24.0 |

## Not done

The two old-name readings past their release. `skills/code-review/scripts/chain_check.py#OLD_TRAILER`
and `hooks/lib/routing.py#OLD_BY_CRAFTER` each say the next minor release
after the rename removes them, and 0.24.0 is that release. This work leaves
them, on `frame/questions.md` Q1's default (a), because the issue scopes it
to the two variables. No issue schedules their removal, and filing one is
the orchestrator's or the owner's act.

The `SPECSEAL_LANG` read's own removal is asked for by a comment at the read
and the census comment, the shape `OLD_TRAILER` has. The plan's failure
scenario names that shape as one that has already failed once.

## Fed back into the spec

none
