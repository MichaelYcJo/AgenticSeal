# Overview: 1793201097-two-environment-variables-still-carry-the-old-brand

## Why this work exists

The plugin read two environment variables named for the old brand; it stops reading `SPECSEAL_LINT`, and the guard's prompt language becomes the plugin option `worktree_guard_language`, with `SPECSEAL_LANG` read where the option is empty through 0.24.x.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Which scripts S5's case reads for an undeclared option | `frame/design.md` S5: "`hooks/worktree-guard.py` reads no `CLAUDE_PLUGIN_OPTION_` variable the manifest does not declare". The case reads every `.py` file under `hooks/`, `hooks/lib/` among them | Every script under `hooks/` | The same S5 row reads every declared option "under `hooks/`", and an option read by any hook script reaches a person the same way the guard's does. The wider reading holds the guard too, so nothing the row asks for is lost |
| What `claude plugin validate .` prints | `frame/design.md` S5 and `frame/plan.md` phase 2: "prints `Validation passed`". It exits 0 and prints `Validation passed with warnings`, with one warning: `CLAUDE.md at the plugin root is not loaded as project context` | The run is read as passing on the manifest | The same warning, and the same last line, print at `0c451b8c`, before the manifest changed (executed, over a `git archive` extract of that commit). The warning names `CLAUDE.md`, not `.claude-plugin/plugin.json` |
| The option's description | `frame/design.md` *Data and interfaces*: "Left empty, the system locale decides." The manifest says "Left empty, the variable SPECSEAL_LANG decides through 0.24.x, then the system locale.", and S5's case asserts the description names `SPECSEAL_LANG` | The manifest's text, from `trail/rounds/round-1.md` finding 1 | `hooks/worktree-guard.py#_lang` reads `SPECSEAL_LANG` before the locale wherever the option is empty. The description is the help text Claude Code shows where a person sets the option, in its dialog and in `/config`, and the README that states the fallback is not shown there. The frame's text told the person the fallback exists for, the owner with `SPECSEAL_LANG=ko` and an `en_US.UTF-8` locale, that an empty option gives English. The next minor release removes the clause and its assertion with the read |
| Where S5's case checks the option's fields | `frame/design.md` S5: the manifest "declares `worktree_guard_language` with `type`, `title` and `description` and no other field". The case checks those fields only where the option is declared | The check runs only where the option is declared, from `trail/rounds/round-1.md` finding 2 | `frame/plan.md` *Technical context* asks that the case go red if the guard leaves and pass again once the option leaves with it. A field check that also ran with no declaration failed on an empty mapping whatever `hooks/` held, so the case could not pass again (executed, over an extract of `99c1649a` with the declaration and the guard's read removed). While the guard reads the option, the comparison of declared and read names still fails a missing or misspelt declaration |

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
