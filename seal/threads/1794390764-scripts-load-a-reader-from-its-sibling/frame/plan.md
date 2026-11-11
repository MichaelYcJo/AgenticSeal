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
  `settle.load` and `tests/skills/test_seal_stamp.py:2105` on
  `stamp._optin`, is rewritten against the place the script now reaches
  the module.
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

## Phases

Each phase leaves every command working. Phase 3 can be handed to an issue
without undoing phases 1 and 2, which deliver the second and third *Done
when* of the issue on their own.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1 and 2; item 3 for the scripts under `skills/`; item 4 for `broad_gate.py`, `chain_check.py` and `pr_body.py`; of item 10, `tests/lib/test_sibling.py`, the `loaded_by` arm and the pins of these scripts' loaders; item 11 for the sentences on loading in the files it edits and in `lib/console.py`. `unverified_check.py` is still the reader, loaded through `load`. | S1, S4, S5 and S9; S6 for the rows under `skills/`; S7 for `broad_gate.py`. The narrow run is `tests/lib/test_sibling.py`, the test module of each script edited, and `tests/behaviour/test_every_entry_point_runs_at_the_floor.py`. | 2418ece65 |
| 2 | *Scope* item 3 for the scripts under `.github/scripts/` and for `evals/scripts/rule_cases.py`; item 4 for `release_seal.py`, `rules.py` and `release_report.py`; items 10 and 11 for those files. | S3; S6 for the remaining rows; S7 for the three scripts. The narrow run is the test module of each script edited. | |
| 3 | *Scope* items 5 to 9; item 10 for the moved classes and for each test file that loads `unverified_check.py` for a moved name; item 11 for every citation of a moved unit; item 12. | S2 and S8; S1 again, its count holding no run of `unverified_check.py`. The narrow run is `tests/lib/test_lines.py`, `test_items.py`, `test_gaps.py`, `test_console.py` and `test_gitcmd.py`, the test module of each script of G8, `tests/skills/test_unverified_check.py`, and each `tests/behaviour/` file edited. | |

## Overlap with the release

The spawn names #1486, #1488, #1484, #1489 and #1485. #1483, #1487 and
#1498 have merged and are part of this base (read: `git log` at
`333fb9def`, #1524, #1525 and #1523).

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1486 (`refactor/1486-a-committed-durations-file-turns-ci-red`, under review; executed: `git diff --name-only origin/release/v0.37.4...origin/<branch>`) | `.github/scripts/release_report.py`, whose `script` loader this work removes and which #1486 rewrites in part; `.github/scripts/run_tests.py`, whose by-path load of `lib/launch.py` at `:82-90` this work replaces and which #1486 rewrites in part; their test modules `tests/github/test_release_report.py` and `tests/github/test_run_tests.py`; `tests/conftest.py` and `tests/censuses.py`, where this work touches them for the new spelling of a load; `CONTRIBUTING.md`, where *Scope* item 11 finds a sentence; and `.test_durations`, which lists test ids this work moves and which #1486 changes | #1486 | It is under review and likelier to be sealed first. Its diff of the two scripts is larger than this work's few lines in each, and both stand in phase 2, so this work integrates inside a phase it spends anyway. Phase 2 builds on the release branch as #1486 leaves it where #1486 has merged by then. |
| #1488 (`test/1488-asserts-pin-literal-phrases`, built, waiting for #1486; executed: `git diff --name-only origin/release/v0.37.4...test/1488-asserts-pin-literal-phrases` on the local branch, which is not pushed) | `.github/scripts/release_completeness_check.py`, whose `_load` this work removes; and the `tests/behaviour/` files that name `unverified_check.py`: `test_a_phase_hands_the_next_one_a_record.py`, `test_both_editions_carry_the_same_folds.py`, `test_the_pull_request_language_is_the_repositorys.py` and `test_the_sealer_guarantees.py`, which load it by path, and `test_a_reference_root_is_read_and_never_taken.py`, `test_first_setup_asks_once.py` and `test_release_hygiene.py`, which name it in a comment or an assert | #1488 | Its phases are built and it waits only on #1486, so it is sealed before this work's phase 3. This work changes a load line or a citation in each file, which rebases onto #1488's edits at lower cost than the reverse. |
| #1484 (no frame; executed: `gh issue view 1484`) | `skills/verify/scripts/payload_meter.py`, whose three loaders this work replaces and whose `--sections` and calibration paths #1484 removes; `closed_fence_lines`, which this work moves to `lib/lines.py` and #1484 removes; `skills/verify/scripts/seal_stamp.py`; and `tests/skills/test_payload_meter.py` | #1482 | The release's plan and #1484's own body put it after this work. #1484 then removes units at the homes this work gives them, and frames against the tree this work leaves. |
| #1489 (no frame; executed: `gh issue view 1489`) | The test files this work writes and splits: `tests/skills/test_unverified_check.py` and the new files under `tests/lib/`. #1489 moves cases into module test files and reads the layout whole | #1482 | #1489 builds after #1488 and has no frame. It moves cases to the homes this work leaves. |
| #1485 (no frame; executed: `gh issue view 1485`) | The docstrings and comments of every script this work edits | #1482 | #1485's body says it builds last of the code items. This work moves a docstring as it reads (`frame/design.md` *Scope*, out of scope item 6). |

## Operational impact

No migration, environment variable or dependency. No command gains or loses
an argument, and no exit code changes.

A deployer sees one change: a command of the plugin copied out and run
alone prints one sentence in place of its own, and `chain_check.py`,
`pr_body.py` and `broad_gate.py` print that sentence where they printed a
line of their own. The exit is 2 as before.

`lib/` gains `sibling.py`, `lines.py`, `items.py` and `gaps.py`.
`ruff.toml` already lints `lib/*.py` at the floor. No tracked list names the
files `lib/` ships (executed: `git grep -n 'blocks.py\|gitcmd.py' -- '*.yml'
'*.json' '*.toml' bin` prints nothing).

The version stays `0.37.4`, which #1523 set for this release. Phase 3's
commit adds `changelog.md`.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
