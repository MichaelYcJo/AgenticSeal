# Phase 1: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | dfae7be9 |

## What this phase was asked

Build `plan.md`'s row 1 and nothing of phases 2 to 5. The marker:
`optin.MARKER`, `home_at` answering only a root whose `README.md` opens with
it, `templates/seal-README.md` and `seal/README.md` opening with it, and the
bootstrap's sentence for a foreign `seal/`. The arm reading `.specseal/` and a
top-level `specs/` removed from `hooks/root-migrate.py` with its cases.
README.md and README.ko.md *Coming up from 0.3.x* reduced to the by-hand
path. Each new case seen red before the code that makes it green. The gates
of the run are the installed 0.22.4 plugin, so the tree's scripts run by
path, and phase 2's thread layout, phase 3's names and phase 4's command line
stay untouched where a file edited here also holds them.

## What this phase found

**The marker reaches every fixture that builds a root, not the four modules
the row names.** Before the fixtures changed, 18 more modules failed, because
each built a `seal/` with no `README.md` and every gate then read it as not
opted in. `tests/conftest.py#mark_root` now writes the marker README, every
conftest helper that builds a root calls it, and the modules with builders of
their own call it too. A fixture a later phase adds that builds a root calls
`mark_root`, or its gate stays silent and the case passes for the wrong
reason. One of those failures wrote outside its fixture: with the root
unread, `tests/test_seal.py`'s `home` was "", and a run wrote `config.md` and
`untracked.md` into the repository root. They were removed, and
`optin.marked("")` now answers False.

**The plan's premise for keeping the migration hook held only in part.**
*Alternatives considered* says `dirty`, `git_mv`, `taken`, `move`, `run_moves`
and `stamp` take paths as arguments and name no old root. `dirty` and
`run_moves` named `OLD_HOME` and `OLD_ITEMS`. Both now take the units and
read their source directories from `sources(units)`, so phase 2 hands
`moves` its units under `seal/specs/` and the never-over-uncommitted-work
check and the cleanup follow them.

**What phase 2 meets in `hooks/root-migrate.py`.** `moves` returns an empty
list, `entries` has no caller until phase 2's units list through it, and the
boundary cases drive `main` through the `moving` fixture of
`tests/test_root_migrate.py`. Two refusals left with the arm because each
named an old root: the symbolic-link refusal, which `spec.md` *The migration*
keeps as a boundary and phase 2 points at `seal/specs/`, and the
`.specseal/scratch` refusal. `main` does not read `optin.SCRATCH`. The
rewrite of `seal/README.md` to the marker is a phase 2 unit, and until it
lands a root an earlier release wrote reads as not opted in.

**Four more readers told a root by a directory test.** `broad_gate.seal_home`
read the two places itself, and `seal.py` tested a directory in
`destination_root`, `install_workflow` and `refusals`. A project's own
`seal/` beside a local root read as a second root to all four, and
`broad-gate` would have read its `config.md`. Each reads `optin.marked` now,
with a case seen red against the directory test. `broad-gate` still does not
read the scratch opt-out, as before.

**The sentences that stated the old opt-in, outside the policy root.** Rule
19's class was enumerated with `git grep` on *presence*, *exists* and *at
either place*. These were corrected: README.md and README.ko.md *Where the
records live* and *First run*, both copies of the seal README,
`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, the bootstrap in three places,
contract rule 11, `skills/commit-pr-convention/SKILL.md`,
`skills/config/SKILL.md`, and the routing rule in
`templates/claude-md-block.md`, which a session follows before the
bootstrap. Left as they stand: `docs/`, where phase 3 applies `spec.md`'s
rule-change rows, and the gates tables' *Where* cells with README.md lines
178, 223 and 425 and their Korean twins, which name the place a root sits
and not the rule that makes it one.

**A case that fails at the base too.**
`tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
fails because this work item holds `spec.md` and no `overview.md`, which
holds at `ace7601a` as well. The work item's `overview.md` clears it.
