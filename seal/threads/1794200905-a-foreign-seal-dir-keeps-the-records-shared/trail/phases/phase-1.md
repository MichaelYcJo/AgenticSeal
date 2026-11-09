# Phase 1: 1794200905-a-foreign-seal-dir-keeps-the-records-shared

## What this phase found

**The frame holds for this phase, with one statement the tree contradicts
and one case it did not place.** `bc3cb015` differs from `872ff59c`, the
commit the frame read, only by the three frame files (executed: `git diff
--stat 872ff59c bc3cb015`). The coordinates *Technical context* and G7, G9
give for `lib/optin.py` and `skills/implement/scripts/seal.py` stood where
they say at `bc3cb015` (read). Two things in the frame did not hold:

- `frame/design.md` S7 says every existing case passes "with no edit except
  a changed signature". The case
  `tests/skills/test_seal.py::Test_refusals::test_refuses_a_projects_own_seal_as_a_destination_not_as_two_roots`
  stated the old rule: a project's own `seal/` refuses a switch to shared.
  S6 states the new one, so the case failed against the new resolver. The
  phase rewrote it to the state where the rule still holds, both `seal/` and
  `agentic-seal/` the project's own, which is the *Out* item on both names.
  Its guard, a directory in the way and not two roots, is the same. Judged
  against `frame/design.md` S6 and *Scope* item 1, which outrank S7's
  description of the existing cases.
- `frame/design.md` *Scope* item 6 names a case for `seal pr-checks
  install`, and no *Phases* row places one. Phase 1 builds `seal.py`, so the
  case is here: `test_pr_checks_install_writes_the_workflow_beside_a_shared_agentic_seal`.
  It needed no code change, because `install_workflow` already took the
  shared place from `optin.home_paths`.

**Seen red at the phase's parent.** The new cases ran against `bc3cb015`'s
code, with only the test files changed (executed: `bin/test
tests/lib/test_optin.py
tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py -q -p
no:xdist -k "shared_place or three_places or home_name or s1_ or s6_"`, 17
failed, 5 passed). S2's `home_paths` cases failed on the shared entry (`repo/seal`
where `repo/agentic-seal` was expected). S2's `home_at` case for a marked
`agentic-seal/` returned the local root. The `home_name_in` and `home_name`
cases failed on the missing names. S1 failed on the printed shared place,
`<repo>/seal`. S6's mode case failed on `seal mode local` exiting 1 with no
root found. S6's import case failed because `--into shared` wrote into the
project's own `seal/` and nothing under `agentic-seal/`, the defect itself.
The `pr-checks install` case, added later, failed with `bc3cb015`'s
`lib/optin.py` swapped in, on "seal/ is not in this tree" (executed).

**Every unit that adds behaviour went red under `seal mutate`** (executed,
one command per unit, 0 survived):

| Unit | Mutants | Cases run |
|---|---|---|
| `lib/optin.py#home_paths`, the shared entry and its fallback | 2 | `tests/lib/test_optin.py -k shared_place` |
| `lib/optin.py#home_name_in`, the order | 1 | `-k home_name_in` |
| `lib/optin.py#home_name`, the opt-out guard | 1 | `-k Test_home_name` |
| `lib/optin.py#_opens_with_marker`, the CR strip | 1 | `-k home_name_in` |
| `seal.py#refusals`, the name and each message using it | 5 | the behaviour module |
| `seal.py#gitlinks_under_root`, the pathspec | 1 | the behaviour module |
| `seal.py#indexed`, the config row's path | 1 | the behaviour module |
| `seal.py#switch`, the name, each pathspec and each message | 13 | the behaviour module |
| `seal.py#import_`, the root's name in both messages | 2 | the behaviour module |
| `seal.py#export`, the shared-mode message | 1 | the behaviour module |

The first mutants of `seal.py` met no case on the `agentic-seal/` fixture:
the config-row exemption, the staged-edit and submodule guards, the
untracked note, both `git reset` lines, both could-not-stage commands, and
the not-a-directory line. The phase added a case or a parameter for each
before running them (`632b9b3b`, `f16928fc`). Those cases, and the
export case of `b41ce59e`, were not run at the parent: each was seen red by
the mutant of its own line above, with that one guard removed. For the
three units run as a single mutant, the failing line was read and names
the guard: `gitlinks_under_root`'s mutant failed the submodule case with no
submodule line in the output, `indexed`'s failed on ` M
agentic-seal/config.md` refused, and `export`'s on the old `/seal` path in
the commands. For the batched runs of `refusals`, `switch` and `import_`,
only each mutant's red verdict was read, not its failing line.

**Departures from the frame, among them a removal `## Removes` did not name
and one it named for no phase.** Judged against `skills/core/SKILL.md` *The rule a mechanism is kept
against*: a change removes in the same commit what stood on the old fact.

- `seal.py#CONFIG_PATHSPEC` and its comment are removed. It spelled
  `seal/config.md` as the row's pathspec. `indexed(line, name, moved)` now
  takes the root's name, and `gitlinks_under_root(repo, name)` does too. The
  existing cases of both pass `"seal"`, which is the changed-signature edit
  S7 allows.
- `frame/design.md` *Removes* row 1, the comment above `WORK_ITEMS` in
  `lib/optin.py`, went in this phase, because its premise became false here.
  Its first sentence, what `WORK_ITEMS` is, stays.
- The two `seal import` lines that name a path in this clone ("is a symbolic
  link", "is not a directory") print the root's own name, `agentic-seal/…`,
  where they printed `seal/…`. The line naming a zip member keeps
  `optin.HOME`, the archive's prefix (G9). `seal export`'s shared-mode
  commands name the shared root by its name. Each is a path a person reads,
  as *Scope* item 3 asks, and each has a case.
- Two docstrings outside `seal.py` stated the old two-place order and were
  corrected: `skills/verify/scripts/broad_gate.py#seal_home` and
  `skills/settle/scripts/fold_check.py#located`. Phase 3 owns
  `broad_gate.py`'s message at `:2984`, which still lists the literal
  places.

**Decisions made while building.**

- The names are `optin.SECOND_HOME`, `optin.home_name(root, common=None)`
  and `optin.home_name_in(read)`, as *Data & interfaces* leaves to the
  crafter. The first-line read and the marker comparison moved out of
  `marked` into `_first_line` and `_opens_with_marker`, so `marked` and
  `home_name_in` compare one way. They are private because no other module
  calls them, and `seal layout --check` reports a public function without
  its class.
- `home_paths`'s fallback asks `os.path.lexists`, so a file or a broken link
  named `seal` counts as standing and the shared place becomes
  `agentic-seal`. *Scope* item 1 says "where nothing stands at that path".
- `seal.py` takes the shared root's name in the tree from
  `display(repo, shared)`, the shared place `home_paths` gives, and not
  from `optin.home_name`. A switch to shared starts from a local root, and
  `home_name` answers "" there by design (*Data & interfaces*).
- S6's import case exports from a local root beside the package, because
  `seal export` refuses in shared mode. The fresh clone imports with
  `--into shared`. With no `--into` and no root in force,
  `destination_root` picks local, the safe guess its docstring states, so
  the clone would not write under `agentic-seal/` unasked.

**For the next phases.** `chain_check.py` reads a commit through
`optin.home_name_in(read)` with its own `read(relpath)`. The behaviour
module imports `status` and `unanswered` from `tests/skills/test_seal.py`,
because `seal layout --check` refuses a helper defined byte-identically in
two test files. The `shared` fixture commits `agentic-seal/` with a work item
under `threads/`.

**The phase boundary.** The set the *Phase boundary* row names ran as one
command over the plan row's files, `tests/text`, `tests/behaviour`, and the
test files that load a module calling the resolver: `tests/lib/` for
`config`, `routing` and `core`, and `tests/skills/` for `chain_check`,
`broad_gate`, `pact_check`, `seal_stamp`, `settle`, `fold_check`,
`unverified_check`, `deferral_check`, `mutation_check`, `payload_meter` and
`pr_body`, with `tests/e2e/teammate/` and `tests/github/test_release_seal.py`.
`tests/conftest.py` loads `lib/optin.py` for `MARKER` alone, which this
phase did not change, so the files that load it only through the conftest
were not taken as readers. The first run, before this record, failed one
case:
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which asks for this work item's `gaps.md`. With `gaps.md` and this record
written, the same command passed (executed: 4208 passed, 9 skipped).
