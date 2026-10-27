# Phase 2: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 45c25f35 |

## What this phase was asked

Build `plan.md`'s row 2 in its order, and nothing of phases 3 to 5. First,
open this work item's `overview.md` from `templates/sdd-overview.md` with
phase 1's departures from the frame, which clears
`tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`.
Then the thread layout: `WORK_ITEMS` `threads`, every reader of a work item
file at its new path, the two templates renamed, the migration's new units
for shared and local mode listing through `entries`, the symbolic-link
refusal pointed at `seal/specs/`, the README rewrite to the marker as a
unit, the state-file renames and the new stamp, the paths in skills,
templates, workflows and `docs/`. Last, this work item's own directory moved
to `seal/threads/<id>/`, `overview.md` renamed to `gaps.md`. Phase 3's names
and phase 4's command line stay untouched where a file edited here holds
them.

The owner narrowed the verification mid-phase, through the orchestrator. A
path or a name that moves is proved by the existing tests passing at the new
path, with no new case, no red run and no `mutation-check`. A new case, seen
red once, is written only for behaviour that did not exist before: the
migration's new units and the README rewrite. The tests the row names and
the modules `git grep -l` finds reading a changed path run in one command.

## What this phase found

**The cases written new, and the old cases relied on.** New, in
`tests/test_root_migrate.py`: `Test_moves` (the README unit and every
0.22.x name at its thread path, a `seal/` whose README no release wrote, a
marked root with no README unit), `Test_main`'s end-to-end shared-mode move
and its linked `seal/specs/` refusal, `Test_migrate_local` (the local root
moved by rename, a local `seal/` of the person's own left alone), and
`Test_rename_state` (each old state file renamed where the new name is
free, and nothing invented where no old file stands). They were seen red
once: the first run of the module, before the hook changed, errored at the
`hook` fixture on the missing `OLD_STATE_DIR`. Relied on unchanged in what
they assert, with their paths moved: the `chain_check`, `settle`,
`unverified_check`, `broad_gate`, `seal`, `gather_changelog`, stamp,
`routing` and gate modules, and every boundary case of
`tests/test_root_migrate.py` that drives the move through `UNITS`.

**A 0.22.x root is told from a project's own `seal/` by its README's first
line.** The frame lists the units and does not say how the migration knows
a root an earlier release wrote. `hooks/root-migrate.py#ours` accepts the
marker or one of the two headings the template opened with before 0.23.0,
read from the template's history. A 0.22.x root whose README a person
edited at its first line reads as a project's own and is not moved.

**The state renames run only with a move.** The suite runs the real
session-start group with the machine's own `HOME`, so a rename at every
session start would have moved the installed plugin's `~/.claude/specseal/`
during this run. `rename_state` runs inside a move that has units. The same
runs already write the once-per-repository stamp into the real state
directory, now `~/.claude/agentic/`, and a directory that exists there
before a real migration keeps `~/.claude/specseal/` from being renamed on a
developer's machine. That is a leftover for `seal/follow-up.md`.

**Where the readers stopped matching once the names moved.** `settle`'s
citation pattern read `specs/<id>/` and now reads `threads/<id>/`; a
citation into a settled 0.22.x directory no longer counts, and none of those
directories exists after the move. `rule_changes.order` reads the first
commit that adds `frame/design.md`, which for every migrated thread is the
migration commit, so their merge order is that commit's path order;
`gaps.md` *Not verified* holds it. `broad-gate --record` makes `trail/` in
a thread that has none, and still refuses an item directory that does not
exist.

**What is left for phase 3 and phase 5.** The `## Rule changes` rows in
`docs/` stay unapplied except the scratch file's, because a case holds that
section to the reader phase 2 renamed. The prose that names `spec.md`,
`plan.md`, `overview.md`, `rounds/` or `phases/` as a concept, in skills,
agents, docs and docstrings, is phase 5's sweep. Comments that cite a
settled work item at `seal/specs/<id>/` (`.github/workflows/test.yml`,
`hooks/cmdline_base.py`, `skills/writing-style/SKILL.md`,
`seal/follow-up.md`, the eval prompts and scaffolds) name history, not a
path a reader opens, and phase 5's census meets them. README.md's 0.3.x
commands still move work items into `seal/specs/`, and the session start
then moves them on; `tests/test_the_root_migrates_itself.py` refuses a
sentence in that section naming a session start, so the section does not
say so.

**A module that fails at the base too.** Three cases of
`tests/test_a_shrunken_corpus_declines_to_judge.py` fail at `2b0c162f` as
they do here, over `tests/test_the_root_migrates_itself.py`, which this
phase did not change.

**This work item is read at its new place.** After the move, the tree's
`chain_check.py --baseline main` reads the declaration at
`seal/threads/<id>/routing.md` and names the records a branch before review
lacks; the installed 0.22.4 edit gate no longer finds it, as Q3 states.
