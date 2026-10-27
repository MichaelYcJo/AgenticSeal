# Overview: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

## Why this work exists

The plugin is renamed to AgenticSeal, a `seal/` is its root only with the marker, and each record sits where its name says what it is, so a reader meets one set of names and no code reads a directory another tool may own.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The marker reached every fixture that builds a root | `plan.md` row 1 names `tests/test_optin.py`, `tests/test_root_migrate.py`, `tests/test_first_setup_asks_once.py` and `tests/test_no_document_names_the_old_roots.py`; 18 more modules failed, because each built a `seal/` with no `README.md` | `tests/conftest.py#mark_root` writes the marker README, and every builder of a root calls it | `spec.md` *Data & interfaces*, *The marker*: `every other state answers ""`; a fixture without the marker tests a repository that is not opted in |
| Four readers outside `optin` told a root by a directory test | `spec.md` *The marker*: "The one reader of the question stays `home_at`"; `broad_gate.seal_home` and `seal.py`'s `destination_root`, `install_workflow` and `refusals` tested a directory | each reads `optin.marked` | the same sentence: a second reader that answers differently is the defect the marker removes |
| The migration's helpers named the old roots | `plan.md` *Alternatives considered*: `dirty`, `git_mv`, `taken`, `move`, `run_moves` and `stamp` "take paths as arguments and name no old root"; `dirty` and `run_moves` named `OLD_HOME` and `OLD_ITEMS` | both take the units and read their source directories from `sources(units)` | the premise the plan kept the hook on, made true so phase 2's units pass through unchanged |
| Where phase 1's record stands | `plan.md` row 2 moves this work item into the thread layout | phase 1's record is `trail/phases/phase-1.md` after the move | `spec.md` *Scope*: `phases/` goes into `trail/` |
| How the migration tells a 0.22.x root from a project's own `seal/` | `frame/design.md` *The migration* lists the units and says nothing about a `seal/` whose README lacks the marker | `hooks/root-migrate.py#ours` moves only a `seal/` whose README opens with the marker or with one of the two headings `templates/seal-README.md` opened with in an earlier release (`OLD_HEADINGS`) | design silent; `frame/design.md` *The marker*: a `seal/` without the marker "is a project's own directory", and nothing may be written into one |
| When the state files are renamed | `frame/design.md` *The migration*: "each state file beside the root renamed from `specseal-` to `agentic-`", and `~/.claude/specseal/` renamed | `rename_state` runs only as part of a move that has units, shared or local, and merges `~/.claude/specseal/` into `~/.claude/agentic/` entry by entry, each entry moved where the new directory does not hold it and the old directory removed once empty | the suite runs the real session-start group with the machine's own `HOME` (`tests/test_stub_remove.py#test_the_dispatcher_carries_the_message`); a rename at every session start would move the installed 0.22.4 plugin's `~/.claude/specseal/` while this run uses it. The merge is fixed at the migration rather than in the suite: a session start of this release writes `version-check` into `~/.claude/agentic/` before any move on every machine, not only under the suite, so a rename of the whole directory would skip the old state wherever the new directory already stood |
| A docs rule-change row applied in phase 2 | `plan.md` row 3 applies `## Rule changes` to `docs/` | the row for `.git/agentic-scratch` in `docs/one-root-by-lifetime.md` and its Korean twin is applied here; every other row is left to phase 3 | `tests/test_first_setup_asks_once.py` holds that section to the reader's name, and phase 2 renames the reader |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through `broad-gate` after the review rounds settle |
| that the three lines README.md prints carry a user from `specseal@specseal` to `agentic@agenticseal` | the owner, on a machine installed at 0.22.4 after the release (`questions.md` Q4) |
| the merge order `skills/settle/scripts/rule_changes.py#order` gives threads whose `frame/design.md` the migration commit added: every such design is first added by that one commit, so their order is that commit's path order and no longer their own pull requests' | the session that runs the 0.23.0 settle, reading its `groups:` against the merge history |

## Not done

nothing

## Fed back into the spec

none
