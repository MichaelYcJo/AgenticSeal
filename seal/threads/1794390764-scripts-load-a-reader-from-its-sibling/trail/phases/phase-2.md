# Phase 2: 1794390764-scripts-load-a-reader-from-its-sibling

## What this phase found

**The merge of `origin/release/v0.37.4` turned the floor case red through
phase 1's `loaded_by` arm, and `ruff.toml` now names the eight files the
walk derives.** At `48a7009eb`,
`test_every_entry_point_runs_at_the_floor.py::test_what_runs_before_any_floor_is_linted_at_the_floor`
listed eight files as run before any floor is checked and absent from
`ruff.toml`'s `per-file-target-version` (executed: that case at
`48a7009eb`, and red again under `seal mutate` with one of the eight lines
removed from `ruff.toml`). Neither side causes it alone. #1486 gave each row
of `.github/scripts/run_tests.py#PINS` the module that imports the pin as a
tracked path: `"tests/commonmark_oracle.py"`, `"tests/gfm_table_oracle.py"`
and `"tests/workflows.py"` (read: `git show bdc856cd9:.github/scripts/run_tests.py`
holds none of the three strings). Phase 1's arm reads every string constant
that is a tracked path in full as a load. The walk starts at `run_tests.py`,
because `bin/test` hands it to the interpreter, so it reached the three test
modules. From there it reached `tests/conftest.py`, `tests/censuses.py` and
`tests/block_shapes.py` by their imports, and
`skills/verify/scripts/coordinates.py` and `pact_check.py` through strings
and joins in those helpers. Not one of the eight runs in `run_tests.py`'s
process: `main` starts pytest as a subprocess under the virtualenv's
interpreter, which is at the floor (read: `run_tests.py#main`).
`frame/design.md` *Scope* item 10 says the arm reads every such string and
that `ruff.toml`'s table follows what the walk derives. So the fix adds the
eight paths to the table, with a comment that says why they stand there
(commit `18bd8df9e`). Before that, each of the eight passed
`tests/censuses.py#newer_than` at 3.9 and `ruff check --target-version
py39` (executed). The cost is that the eight files are now linted at 3.9 and
held by `floor_syntax` to 3.9 syntax, though they never run below the
floor. A narrower arm, one that reads a tracked path only where it is handed
to `sibling.load`, directly or through a name, would keep them out. That
changes what *Scope* item 10 states, so it is a frame decision, and this
phase did not take it. Judged against `frame/design.md` *Scope* item 10 and
S9.

**The frame holds for the files of this phase, with three exceptions below.**
Each loader that `frame/design.md` *Removes* rows 1 to 3 names for
`.github/scripts/` and `evals/scripts/rule_cases.py` stood where the row
says, at `48a7009eb`. #1486 rewrote `run_tests.py`, so the by-path load of
`lib/launch.py` that the row places at `:82-90` stood at `:84-91` (read).
`.github/scripts/durations_union.py`, which #1486 also changed, holds no
loader form (executed: the two `git grep` commands of G5 at `48a7009eb`).

**Exception: `rules.py` and `release_report.py` never turned a module that
raises into `Unreadable`.** `frame/design.md` *Scope* item 4 and S7 say
both "still end in their `Unreadable`", and G15 says they raise their own
`Unreadable`. At `48a7009eb`, `rules.py#sibling` and
`release_report.py#script` each raised `Unreadable` only where the file was
absent. A module that raised while it executed went through both as a
traceback (read: both functions, and `main`, which catches `Unreadable`
alone). Item 4's rule is "each catches what it caught in its loader". Both
caught nothing, so both still catch nothing, and a module that raises is
still a traceback. An absent module is now `lib/sibling.py`'s sentence at
exit 2, where it was the script's own `Unreadable` sentence at exit 2. No
case at the base plants a raising module for either script. So S7 for these
two has no case to keep, and this phase wrote none, because the behaviour
did not change.

**Exception: a lone copy of `rules.py` or `release_report.py` that is run
with arguments reaching a load now ends in a traceback at exit 1.** S6
compares runs with no argument, and those rows hold (below). With arguments,
the two scripts differ from the base:

| Run of the lone copy | At `48a7009eb` | At HEAD |
|---|---|---|
| `rules.py --check` | exit 2, `seal rules: cannot read lib/optin.py, and it is what finds the repository the command is typed in.` | exit 1, `ModuleNotFoundError: No module named 'sibling'` |
| `rules.py --root . x.md` | exit 2, `seal rules: cannot read skills/verify/scripts/unverified_check.py, and …` | exit 1, the same traceback |
| `release_report.py --against v1 --at .` | exit 2, `release-report: cannot read skills/verify/scripts/payload_meter.py, which …` | exit 1, the same traceback |

(executed: `test_tmp_alone_args.py` under this phase's scratch directory.)
*Scope* item 2 leaves these two unguarded, because G10 names neither of
them among the commands that exit 2. G10 measured only runs with no
argument. `frame/design.md` *Data & interfaces* and `frame/plan.md`
*Operational impact* list two changes for a command copied alone, and this
is a third. A guard on the lazy `import sibling` in each script would keep
exit 2. That is the trade *Alternatives considered* A9 and A10 weigh, so
the choice is the framer's, and this phase built to *Scope* item 2 as it
stands. In a whole plugin, where `lib/sibling.py` is present, neither
script changes its exit.

**Departure: `release_seal.py#chain_counts` catches the loader's
`SystemExit`.** Its docstring and S10 of its own work item say that a
reader that will not load leaves the three tree rows unread, and the seal
goes on. At the base an absent `chain_check.py` raised `FileNotFoundError`
inside `exec_module`, which the function's `except Exception` caught. Under
the loader, an absent file is `SystemExit(2)`, which is no `Exception`. Left
uncaught, it would end the whole seal in `main`'s "no seal" line, where the
base drew the seal with three rows unread. The function now catches
`(Exception, SystemExit)`. It keeps its own line, `the chain rows are not
read: …`, which says what the absence costs and does not restate the
absent file. *Scope* item 4 says no caller catches the loader's `SystemExit`
"to add a line of its own under the sentence". This line names the rows
that go unread, which no other line says, and phase 1 caught the same exit
at `broad_gate.py`'s label site for the same reason, that a label never
stops a run. `test_release_seal.py#Test_chain_counts::test_refuses_to_end_the_seal_where_a_reader_is_absent`
points `sibling.ROOT` at an empty directory and holds the three rows at
None with the sentence on stderr. Judged against `release_seal.py#chain_counts`'s
docstring and `frame/design.md` *Scope* item 4.

**Where the stanza stands follows G10, as *Scope* item 2 says.**
`release_report.py`, `release_seal.py` and `rules.py` reach no load with
no argument, so each puts `lib/` on `sys.path` at import and imports
`sibling` at the first load. In `release_report.py` that is inside `meter`,
`floor` and `documents`. In `release_seal.py` it is inside `module`. In
`rules.py` it is inside `sibling`. The eleven other scripts and
`rule_cases.py` loaded at import at the base, so each imports `sibling` at
import, unguarded. A `from <module> import <names>` became attribute reads
of the loaded module under the same module-level names, because cases read
them: `test_issue_claims_check.py` holds `check.KEYWORDS is
closer.KEYWORDS`.

**Two getters stay, each as a call of the loader.** `rules.py#sibling(key)`
stays because `tests/behaviour/test_this_repository_passes_its_own_checks.py`
asks it for `config` and `rule_changes`. Its `SIBLINGS` now maps each key to
a path alone, the purposes and the `_loaded` cache gone, as *Removes* rows 2
and 3 say. The function shares its name with the module it imports, so it
imports the loader as `import sibling as loader`. `release_seal.py#module`
stays, now `module(rel)` in place of `module(name, *parts)`, and its
`functools.cache` goes, because `lib/sibling.py#load` returns the module
`sys.modules` holds. Both getters are what *Removes* row 2 allows.

**One instance per stem reaches these scripts too.** `label_merged_on_release_branch.py#closer`,
`tracker_labels.py#signal`, `release_completeness_check.py#signal` and
`publish_release_note.py#settle` are now the one module `sys.modules` holds
under each stem. A test file still loads the script it tests under a name
of its own, which `load` never sees. `tests/github/` and
`tests/evals/test_rule_cases.py`, run serially in one process, pass, 576
cases (executed: `bin/test tests/github tests/evals/test_rule_cases.py -q
-p no:xdist`). That answers `frame/questions.md` Q1 for these files only.

**`finding_counts.py` exits 2 for an absent reader in the loader's sentence.**
Its `main` catches `Exception` around `readers()` and prints `a reader did
not load`. An absent file is now the loader's `SystemExit(2)`, which that
catch does not take, so the run exits 2 in the loader's sentence alone.
The docstring's exit code 2 stands.

**What was removed, and its census.** `finding_counts.py#load`,
`issue_claims_check.py#load_reader`,
`label_merged_on_release_branch.py#_load`,
`release_completeness_check.py#_load`, `tracker_labels.py#_load` and its
`HERE`, `release_report.py#script`, `release_seal.py#_module`,
`rules.py#_loaded`, `rule_cases.py#load` and `#PR_BODY_MODULE`, and
`run_tests.py`'s `_LAUNCH` and `_launch`. `git grep` on each name, and on
the private module names those loaders gave (`agentic_…_for_counts`,
`agentic_rules_<key>`, `agentic_unverified_reader` and the others), outside
`seal/threads/`, prints only the names tests give their own loads, which
*Out of scope* item 3 keeps (executed). `tests/github/test_rules.py#Test_sibling`
goes, as *Removes* row 8 names it. `seal layout --check` now reports that
`rules.py#sibling` has no class, which is a report and not a refusal
(executed).

**The sentences on loading, *Scope* item 11 for this phase.** The comment
above each stanza, `lib/console.py`'s paragraph on how a script reaches
`lib/` and which scripts load on first ask, the `__main__` comments of
`release_report.py` and `rules.py`, the comments in
`label_merged_on_release_branch.py` and `tracker_labels.py` that said
"imported by path", and three sentences that said a script imports what it
now loads (commit `1ff07b7cd`). The list was built with `git grep` on `by
path`, `importlib`, `loaded by`, `_load`, `load_reader`, the removed
names, and `imports` followed by `it`, `them` or a `lib/` module's name,
over `.github/scripts/`, `evals/scripts/`, `tests/github/`, `tests/evals/`,
`docs/`, `skills/**/*.md`, `agents/`, `templates/`, `CONTRIBUTING.md` and
`README.md`. It is a sample: a sentence that says how a script reaches a
module in other words is not reached by it.

**The scenarios this phase owes.**

- S3 (executed at HEAD): `git grep -n spec_from_file_location -- '*.py'
  ':!tests'` prints `lib/sibling.py:86` alone, and `git grep -nE
  '^\s*def _?load\('` over the same files prints `lib/sibling.py#load` and
  `session_cost.py#load` alone.
- S6 (executed: `test_tmp_alone.py`, each of the fifteen scripts copied
  into an empty directory and run with no argument and with `--help`, the
  file at `48a7009eb` against the file at HEAD, under
  `/opt/homebrew/bin/python3`). Every row keeps its exit code and its
  traceback-or-not. The twelve that loaded at import end in a traceback at
  exit 1 at both commits. The cause moves from `No module named 'console'`,
  `'behaviour'` or a `FileNotFoundError` to `No module named 'sibling'`.
  `release_report.py` exits 2 on its usage and 0 on `--help`, `rules.py` 2
  and 0, and `release_seal.py` 0 and 0, at both commits.
- S7 for `release_seal.py` (executed): the `a module will not load` case of
  `Test_main` and the S10 case of `Test_chain_counts` pass unchanged. The
  new case is described above. It went red with `SystemExit` taken out of
  the catch, failing on `SystemExit: 2` raised at `lib/sibling.py:82`
  (executed: `seal mutate`). For `rules.py` and `release_report.py`, see
  the first exception above.
- The units this phase only moved or renamed, the loads of every other
  script, owe no new case. The test module of each script passes at the new
  call (the phase-boundary run).
