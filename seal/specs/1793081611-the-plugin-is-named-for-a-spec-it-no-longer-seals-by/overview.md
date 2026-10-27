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

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through `broad-gate` after the review rounds settle |
| that the three lines README.md prints carry a user from `specseal@specseal` to `agentic@agenticseal` | the owner, on a machine installed at 0.22.4 after the release (`questions.md` Q4) |

## Not done

nothing

## Fed back into the spec

none
