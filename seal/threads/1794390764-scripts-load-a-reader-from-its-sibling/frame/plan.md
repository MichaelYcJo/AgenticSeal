# Implementation Plan: 1794390764-scripts-load-a-reader-from-its-sibling (#1482)

## Technical context

The tree as read at `333fb9def`.

**What stands.** A script reaches another module in one of two ways, counted
in `frame/design.md` *Grounding* G5. Either it builds a spec with
`importlib.util.spec_from_file_location` under a name of its own, such as
`agentic_optin_for_broad_gate`, and executes it
(`skills/settle/scripts/settle.py:252-271` is the fullest form). Or it puts
a directory on `sys.path` and imports by a plain name
(`skills/implement/scripts/seal.py:220-225`, `lib/fields.py:54-57`). The
first way keeps nothing between calls unless the file adds a cache of its
own (G17). The two ways do not
share a record of what is loaded: `lib/tables.py` imports `blocks` as
`blocks`, and `unverified_check.py:76` loads the same file as
`agentic_blocks_for_unverified`, so one process runs it under several names
(G6).

**What is absent is said per file.** The commands of G10 that exit 2 where
a sibling is missing each say so in their own words, some with a table or
an argument that says what the file is for (`settle.py:202-217`,
`seal.py:182-217`). The other scripts that lack a module end in a
traceback.

**`unverified_check.py` is three things.** It is the `seal unverified`
command, the markdown line reader of the scripts of G8, and the home of the
predicates of G9, which only `chain_check.py` or `settle.py` call. It
loads `rule_changes.py` at `:1151-1162` for `chain_check.py`, and
`rule_changes.py:87-93` loads it back.

**Constraints.**

- A script cannot read anything from a file it has not located, so each
  script keeps the step that locates `lib/`. That step is the stanza of
  `frame/design.md` *Data & interfaces*, and it is the same plain import
  `lib/` already uses for its neighbours (G14).
- The walk that decides which files are linted at the Python floor reads
  loads statically (G12). A load it cannot read drops a file from that set
  in silence.
- The test layout ties a test class to a function of one module (G13), so
  moving a unit moves its class.
- A hook's script must not turn a missing file into a session's problem
  (G11). Both hook commands end `|| exit 0`.

**The failure scenario of the chosen approach, six months on.**

- **Stems are one namespace per process.** `load` names a module by its
  file's stem. A new script named like an existing module is refused by
  `load` with both paths, which is loud. A third-party module that some
  other code in the process imports by a plain name the plugin also uses is
  shadowed in silence, because `lib/` stands first on `sys.path`. A
  script's process runs no such code. A `pytest` process could, through a
  plugin that imports `lines`, `items` or `gaps`. The same exposure stands
  today for `config`, `tables` and `console`.
- **An entry script loaded by its sibling runs twice**, once as `__main__`
  and once under its stem, as `pr_body.py` and `chain_check.py` do to each
  other today. S1 is stated of `seal settle`, where no sibling loads
  `settle.py` back.
- **A test's instance is not the script's.** A test file loads its `TARGET`
  under a name of its own, and a sibling that asks `load` for the same file
  gets the instance under the stem. A case that patches a module through a
  script's own loader, such as `tests/skills/test_settle.py:2045` on
  `settle.load`, is rewritten against the place the script now reaches
  the module. Where a getter that names its module stays, as
  `seal_stamp.py#_optin` does, a case that patches the getter stands
  unchanged.
- **One instance is shared by every script in a `pytest` process.** A
  module under `lib/` that kept state at module level would carry it from
  one test file to the next. G7 shows the modules a settle loads keep
  none that changes its output; `frame/questions.md` Q1 holds the rest.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. One loader, `lib/sibling.py#load`, that executes a file under its stem in `sys.modules`; each script reaches it by the stanza | The scenarios of *Technical context*. The stanza repeats in every script, and its guard repeats the sentence in each command of *Scope* item 2. | **Chosen.** G7 ran it: each file once, the output byte-identical. `sys.modules` is the record `lib/`'s own imports already write (G14), so the loader adds no second table. |
| A2. Keep every script's by-path loader and add a cache to each. This is the alternative that keeps the structure | Each cache is keyed by that script's own name for the file. `lib/blocks.py` still runs once for each script and each `lib/` module that loads it, so S1 fails. The sentence for an absent file stays in every loader. | Rejected. The premise that keeps the structure is that a script needs an instance of its own. G7 checked it for a settle and found no output that depends on it. |
| A3. Plain `import` everywhere, with every script directory on `sys.path`, and no loader | An absent module is a `ModuleNotFoundError` traceback at exit 1 (#610), so each command keeps a refusal that lists its modules, as `seal.py#refuse_without_lib` does. Python also returns the first file of a stem on `sys.path`, which is not always the one the script meant. | Rejected. It leaves the sentence in every command, and it loads by search where `load` loads the file named. |
| A4. One loader with a table of its own, keyed by path, under private names | `lib/tables.py`'s `import blocks` and the loader's `blocks.py` are two instances, so S1 fails unless `lib/` goes through the loader too. A `lib/` module cannot reach the loader without the plain import this alternative set out to drop. | Rejected. |
| A5. The line readers move into `lib/blocks.py`, the issue's first candidate | `lib/tables.py`, `lib/fields.py` and `lib/routing.py` import `blocks`, and through them nearly every command and the `Stop` hook. Each would parse about 450 more lines for readers it never calls. `blocks.py#walk` and `live_lines` are two walks kept apart on purpose (`unverified_check.py:85-88`); one file invites the next reader to mix them. | Rejected for `lib/lines.py`, which only the readers of lines open (G2). |
| A6. Move the line readers alone, and let `chain_check.py` and `settle.py` load `unverified_check.py` through the loader for the predicates | The issue's first *Done when* fails as written. `unverified_check.py` and `rule_changes.py` keep loading each other, which under one instance per stem is an import cycle that holds only while both loads stay inside functions. | Rejected. G9 shows each predicate has one reader, so each has a home that is not this file. |
| A7. One new `lib/` module for the line readers, the item grammar and the `## Not verified` reader together | The scripts that read lines alone (G8) load the memo reader and the grammar with them. `rule_changes.py` loads the memo reader to parse an item. | Rejected. The three have three sets of readers. |
| A8. The predicates of G9 move to a `lib/` module | A `lib/` module with one caller is a file one party opens, standing apart from the code that decides with it. The case in `test_chain_check.py#Test_module` that keeps a second `settled` out exists because the predicate stood away from its reader. | Rejected. Each moves to its one reader. |
| A9. No guard on the stanza | A command copied alone ends in `ModuleNotFoundError` at exit 1. That takes back #590 and #610, which the `test_a_script_copied_alone_exits_2_and_names_what_it_misses` cases pin, and it is a change a person sees beyond the wording the issue agreed to lose. | Rejected. |
| A10. A guard on the stanza of every script | The scripts that end in a traceback today for a missing module (G10) would gain a refusal nobody asked for, and the sentence would stand in every script of *Scope* item 3. | Rejected. The guard stands where the behaviour stands today. |
| A11. A census that refuses `spec_from_file_location` outside `lib/sibling.py` | It is a mechanism with no catch on the day it is added (`skills/core/SKILL.md` *The rule a mechanism is kept against*). A new by-path load shows in the diff that adds it, where the proofer reads it. | Rejected. S3 is a command a reviewer runs, not a gate. |
| A12. `lib/`'s own imports and `hooks/core-start.py` go through the loader too | A `lib/` module reaches `sibling` only by the plain import it would be replacing. The hook would need a guard to stay silent where today it needs none. | Rejected (`frame/design.md` *Scope*, out of scope item 2). |
| A13. The guard stands inside the function that first loads, in `settle.py`, `fold_check.py`, `pact_check.py` and `payload_meter.py`, so a lone copy still prints its help at exit 0 | The guard is spelt once in each getter that reaches a module, or behind one more getter every call goes through, and the sentence then stands more often than once per command. What it buys is the help text of a copy that can run none of what the help lists. | Rejected after phase 1 built the guard at import and measured the one invocation that changes (`trail/phases/phase-1.md` *What this phase found*). Each of the four reaches a load with no argument at the base (G10), so a bare run of the copy already ended in the sentence at exit 2. `frame/design.md` *Data & interfaces* states the changed exit code. |
| A14. `loaded_by` reads a tracked path only where it is handed to `sibling.load`, in the call or through a module-level name | It reads under. `rules.py#SIBLINGS` holds its paths in a table, and `release_seal.py#module` and `broad_gate.py#sibling_module` take theirs as a helper's argument. Tried at `d50d63e9d` (executed: `test_tmp_arm.py`, the walk run with that arm), it drops the eight files and also `skills/settle/scripts/fold_check.py`, which `chain_check.py` reaches through `rules.py` before any floor is checked. A file dropped from the floor table is linted at 3.12 while the `Stop` hook may run it at 3.9. | Rejected. Following a table and a helper's argument is a data flow the walk would have to guess. |
| A15. `loaded_by` keeps reading every tracked-path string, and `ruff.toml` names the eight files, as phase 2 built it | Six test helpers, `tests/conftest.py` and `tests/censuses.py` among them, and two scripts are held to 3.9 syntax, though pytest runs them at the floor, 3.12. Each later string that names a test file in `run_tests.py`, or in a file it reaches, adds lines to the table for a load that never happens. | Rejected for the arm that leaves `tests/` out. Tried at `d50d63e9d` (executed: the same probe), that arm drops the eight and nothing else, so no script before the floor hands `load` a path under `tests/`. |
| A16. `rules.py` and `release_report.py` stay unguarded, and the frame states a third change for a lone copy | A lone copy run with arguments ends in `ModuleNotFoundError` at exit 1 where it exited 2 in a sentence. That is A9's failure for two scripts, and `rules.py` is `seal rules`, which a user's CI runs. | Rejected by A10's own rule, that the guard stands where the behaviour stood. The behaviour stood for these two, and G10 missed it because it ran each script with no argument. One guard in each script's one loading function keeps it. |
| A17. The moved cases keep the module name they read, so that `seal layout --moved` passes, and *Scope* item 10 changes in place of S8 | The check compares the definition of each name a case reads, and a name that binds `lib/gaps.py` is defined differently from one that binds `unverified_check.py` whatever it is called (G13). The only tree that passes leaves each moved case reading its unit through `unverified_check.py`, which is the load the issue's first *Done when* removes. | Rejected. S8 changes: its check is the comparison with module names read as one, and `--moved` is stated as failing by rule. The cost is that the moved cases have no `--moved` exemption from mutants, and the proofer weighs the nine cases that differ. |

## Phases

Each phase leaves every command working. Phase 3 can be handed to an issue
without undoing phases 1 and 2, which deliver the second and third *Done
when* of the issue on their own.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1 and 2; item 3 for the scripts under `skills/`; item 4 for `broad_gate.py`, `chain_check.py` and `pr_body.py`; of item 10, `tests/lib/test_sibling.py`, the `loaded_by` arm and the pins of these scripts' loaders; item 11 for the sentences on loading in the files it edits and in `lib/console.py`. `unverified_check.py` is still the reader, loaded through `load`. | S1, S4, S5 and S9; S6 for the rows under `skills/`; S7 for `broad_gate.py`. The narrow run is `tests/lib/test_sibling.py`, the test module of each script edited, and `tests/behaviour/test_every_entry_point_runs_at_the_floor.py`. | bdc856cd9 |
| 2 | *Scope* item 3 for the scripts under `.github/scripts/` and for `evals/scripts/rule_cases.py`; item 4 for `release_seal.py`, `rules.py` and `release_report.py`; items 10 and 11 for those files. | S3; S6 for the remaining rows; S7 for `release_seal.py`. The narrow run is the test module of each script edited. | 1ff07b7cd |
| 3 | Two items the fold after phase 2 decided, built first: the guard of *Scope* item 2 on `rules.py` and `release_report.py`, with a copied-alone case for each; and the `tests/` half of *Scope* item 10's `loaded_by` arm, with the eight lines and their comment out of `ruff.toml`. Then *Scope* items 5 to 9; item 10 for the moved classes and for each test file that loads `unverified_check.py` for a moved name; item 11 for every citation of a moved unit; item 12. | S4 for the two scripts and S9's second half; S2, and S8 by its comparison; S1 again, its count holding no run of `unverified_check.py`. The narrow run is `tests/github/test_rules.py`, `tests/github/test_release_report.py`, `tests/behaviour/test_every_entry_point_runs_at_the_floor.py`, `tests/lib/test_lines.py`, `test_items.py`, `test_gaps.py`, `test_console.py` and `test_gitcmd.py`, the test module of each script of G8, `tests/skills/test_unverified_check.py`, and each `tests/behaviour/` file edited. | 2d46c5d34 |

## Overlap with the release

The spawn names #1486, #1488, #1484, #1489 and #1485. #1483, #1487 and
#1498 have merged and are part of this base (read: `git log` at
`333fb9def`, #1524, #1525 and #1523).

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1486 (merged into `release/v0.37.4`, and into this branch at `48a7009eb`; read: `git log`) | `.github/scripts/release_report.py`, whose `script` loader this work removes and which #1486 rewrites in part; `.github/scripts/run_tests.py`, whose by-path load of `lib/launch.py` at `:82-90` this work replaces and which #1486 rewrites in part; their test modules `tests/github/test_release_report.py` and `tests/github/test_run_tests.py`; `tests/conftest.py` and `tests/censuses.py`, where this work touches them for the new spelling of a load; and `CONTRIBUTING.md`, where *Scope* item 11 finds a sentence. #1486 removed `.test_durations`, so the test ids this work moves stand in no tracked list. Its `run_tests.py#PINS` names three test modules by tracked path, which is what *Scope* item 10's `tests/` half answers | #1486 | It merged first, and phase 2 built on its text. The orchestrator reports the merge at `48a7009eb` took no conflict. |
| #1488 (merged into `release/v0.37.4` as #1528, and into this branch at `f55d551de`; executed: `gh pr view 1528`, read: `git log`) | `.github/scripts/release_completeness_check.py`, whose `_load` this work removed; the `tests/behaviour/` files that named `unverified_check.py` and now load the home of what they read (`trail/phases/phase-3.md` lists them); and `tests/behaviour/test_release_hygiene.py::test_the_chain_check_loads_the_one_reader`, #1488's name for the case that asserts the reader's path and `"reader.readable("` against `chain_check.py`'s text | #1488 | It merged first. The one conflict was that case: #1488 kept the assert as a fact a reader acts on, with a comment that says so, and this work moved the fact, so the merge keeps #1488's comment over this branch's `"lib/lines.py"`, the path `chain_check.py:167` holds at HEAD (read: `tests/behaviour/test_release_hygiene.py:1305-1318`). The orchestrator reports no other conflict, and its narrow run after the merge. |
| #1484 (no frame; executed: `gh issue view 1484`) | `skills/verify/scripts/payload_meter.py`, whose three loaders this work replaces and whose `--sections` and calibration paths #1484 removes; `closed_fence_lines`, which this work moves to `lib/lines.py` and #1484 removes; `skills/verify/scripts/seal_stamp.py`; and `tests/skills/test_payload_meter.py` | #1482 | The release's plan and #1484's own body put it after this work. #1484 then removes units at the homes this work gives them, and frames against the tree this work leaves. |
| #1489 (no frame; executed: `gh issue view 1489`) | The test files this work writes and splits: `tests/skills/test_unverified_check.py` and the new files under `tests/lib/`. #1489 moves cases into module test files and reads the layout whole | #1482 | #1489 builds after #1488 and has no frame. It moves cases to the homes this work leaves. It also finds that `tests/lib/test_gaps.py`, `tests/skills/test_chain_check.py` and `tests/skills/test_settle.py` bind the fixtures of `tests/skills/test_unverified_check.py` by import, so the moved cases read the worlds they read before; a home of their own for those worlds is #1489's to give. |
| #1485 (no frame; executed: `gh issue view 1485`) | The docstrings and comments of every script this work edits | #1482 | #1485's body says it builds last of the code items. This work moves a docstring as it reads (`frame/design.md` *Scope*, out of scope item 6). |

## Operational impact

No migration, environment variable or dependency. No command gains or loses
an argument, and no exit code of a command in a whole plugin changes.

A deployer sees a change only in a command of the plugin copied out and run
alone. It prints one sentence in place of its own, and `chain_check.py`,
`pr_body.py` and `broad_gate.py` print that sentence where they printed a
line of their own, at exit 2 as before. One exit code changes: a lone copy
of `settle.py`, `fold_check.py`, `pact_check.py` or `payload_meter.py` run
with `--help` exits 2 in that sentence, where it printed its help at exit 0
(`frame/design.md` *Data & interfaces*).

`lib/` gains `sibling.py`, `lines.py`, `items.py` and `gaps.py`.
`ruff.toml` already lints `lib/*.py` at the floor. No tracked list names the
files `lib/` ships (executed: `git grep -n 'blocks.py\|gitcmd.py' -- '*.yml'
'*.json' '*.toml' bin` prints nothing).

The version stays `0.37.4`, which #1523 set for this release. Phase 3's
commit adds `changelog.md`.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-11 | The seven frame statements phase 1's hand-back names, among them the exit code of a lone copy run with `--help` and *Scope* item 2's placement of the guard, went to the framer as one fold before phase 2 | One of them changes a stated interface, the exit codes design *Data & interfaces* holds unchanged, so it is a design decision and not a restatement; phase 2 applies item 2 and item 10 to `.github/scripts/`, so it should read the frame that states what phase 1 built | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-11 | The two choices phase 2's hand-back leaves open, whether `loaded_by` reads every tracked-path string or only one handed to `sibling.load`, and whether `rules.py` and `release_report.py` guard their lazy `import sibling`, went to the framer with its two restatements in one fold before phase 3 | Each changes what *Scope* items 2 and 10 state: the first decides which eight files the floor table names, the second whether a lone copy of the two scripts keeps exit 2. Phase 3 moves classes the `loaded_by` arm traces, so it should start from the frame's answer | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-11 | The merge `f55d551de` took #1488, whose `test_release_hygiene.py` case kept the chain check's reader-path assert with a comment; the resolution keeps that comment over this branch's `lib/lines.py` | #1488 ruled the assert a fact a reader acts on and this branch moved the fact; the *Overlap with the release* #1488 row has whichever merges second rule it on the other's text | `frame/plan.md` *Overlap with the release* |
| 2026-11-11 | Phase 3's three frame statements, S8's `seal layout --moved` against *Scope* item 10 among them, went to the framer as one fold before the first round | S8 states a check that cannot pass under item 10, so one of the two is a design decision; a round read before it would judge the moved cases against a scenario the frame has not settled | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
