# Phase 1: 1794390764-scripts-load-a-reader-from-its-sibling

## What this phase found

**The frame holds against the tree at `333fb9def`, with one placement this
phase built differently.** The loaders `frame/design.md` *Removes* names
for the fourteen scripts under `skills/` stood where it says. The
copied-alone case *Removes* names stood in five files,
`test_chain_check.py`, `test_fold_check.py`, `test_payload_meter.py`,
`test_seal.py` and `test_settle.py` (read: `git grep` at `333fb9def`). G10 names eight guarded
commands. `pr_body.py`, `broad_gate.py` and `pact_check.py` had no
copied-alone case at the base, so S4's "a case per command" adds three
(`test_pr_body.py#Test_main`, `test_broad_gate.py#Test_module`,
`test_pact_check.py#Test_module`).

**Departure: the guarded stanza stands at import in all eight guarded
commands.** *Scope* item 2 places the stanza where the script's first load
stood at the base, and a function's first load is lazy in `settle.py`,
`fold_check.py`, `pact_check.py` and `payload_meter.py`. The guard catches
the failed `import sibling` and prints the sentence; inside a function it
would be spelt once for each getter that reaches a module, or behind one
more getter that every call goes through. The reason item 2 gives for the
lazy placement is G10: a script that reaches no load with no argument
still reaches none. Each of these four reaches a load with no argument, so
that reason holds at import (executed: the copied-alone probe of S6 below,
where each prints the sentence at exit 2 at base and at HEAD). The cost is
one case this phase measured. Copied alone and given `--help`, these four
exit 2 with the sentence where the base printed their help at exit 0
(executed: each file at `333fb9def` and at HEAD, copied into an empty
directory and run with `--help`; `broad_gate.py` exits 2 at both). This
contradicts `frame/plan.md` *Operational impact* ("no exit code changes")
and `frame/design.md` *Data & interfaces* ("The exit codes of every command
are unchanged") for that one invocation. Judged against `frame/design.md`
*Scope* item 2, G10 and *Alternatives considered* A9.

**The unguarded scripts split the stanza.** `passages.py`,
`rule_changes.py`, `coordinates.py`, `seal_stamp.py` and `session_cost.py`
put `lib/` on `sys.path` at import, which reads no file, and run
`import sibling` inside the getter at first use. A load that was lazy at
the base stays lazy, and none gains a guard (*Scope* items 2 and 3,
*Alternatives considered* A10). `unverified_check.py` loaded `lib/` at
import at the base and imports `sibling` at import, unguarded, as A10
asks. Its row of S6 still ends in a traceback at exit 1, now
`ModuleNotFoundError: No module named 'sibling'`.

**A getter that only names its module stays, as one line.** *Removes* row
2 allows it. `fold_check.py#reader`, `#optin` and `#config_reader`,
`payload_meter.py#_session_cost`, `#_fence_rule` and `#_core`,
`seal_stamp.py#_gitcmd`, `#_chain_check` and `#_optin`,
`rule_changes.py`'s four getters, `coordinates.py#shared_reader`,
`session_cost.py#lib_module` and `unverified_check.py#rule_changes` now
each return `sibling.load(...)`. Their caches go, since `load` returns the
module `sys.modules` holds. `tests/skills/test_seal_stamp.py` still patches
`stamp._optin`, which is where the script reaches `lib/optin.py`, so that
case needed no rewrite.

**`broad_gate.py` converts at its calls through one helper.**
`broad_gate.py#sibling_module(rel)` calls `sibling.load` and turns an
exception into `Refused("seal gate: <path> will not load, so nothing ran:
<what it said>")`, which is #869's contract (*Scope* item 4).
`stamp_module` and `gitcmd_module` call it. Its round label site catches
`SystemExit` beside `Refused`: an absent `lib/gitcmd.py` or
`seal_stamp.py` there is the loader's `SystemExit(2)`, and a label never
stops a run (`test_broad_gate.py#Test_rounds_rows::test_refuses_to_stop_a_run_where_the_check_will_not_load`).
The cases of `Test_load` that tested the old loader became
`Test_sibling_module`, which point `sibling.ROOT` at a tree under
`tmp_path`. That is more than "only the loader's name changed" that S7
states, and it is the least that lets a case put a raising module where
`load` looks.

**`seal.py` loads `lib/blocks.py` before `lib/tables.py`.** `lib/tables.py`
imports `blocks` by its plain name. Where `lib/blocks.py` is absent, a
load of `lib/tables.py` alone ends in `ModuleNotFoundError` at exit 1,
which is #610's traceback. Loading `lib/blocks.py` first makes that the
loader's sentence at exit 2 (S5), and `tables`' own import then finds it in
`sys.modules` (G14). `test_seal.py#Test_module::test_a_lib_without_the_table_walks_reader_exits_2_in_one_sentence`
holds it, seen red with the preload removed (executed: `seal mutate`, red
on a traceback at exit 1).

**`chain_check.py` and `pr_body.py` no longer catch `SystemExit` at
import.** The loader has already written the sentence and raised
`SystemExit(2)` for an absent file. Catching it there printed a second
line, `chain-check: the shared reader would not load (2)`, below the
sentence. Their own line stays for a module that raises, which is *Scope*
item 4's contract, so the line `frame/design.md` *Removes* row 3 names at
`chain_check.py:290-292` is kept for that case alone.
`test_chain_check.py#Test_module::test_an_absent_reader_is_the_loaders_sentence_alone`
holds it, seen red with `SystemExit` back in the catch (executed:
`seal mutate`). The lazy readers in `chain_check.py`
(`check_lines_reader`, `rule_changes_of`, `originals_of` and
`pr_body_reader`) still catch `SystemExit` and end in their own result, as
they did at the base.

**`unverified_check.py#references_at` no longer turns an absent
`lib/config.py` into `None`.** It now meets the loader's sentence at exit 2,
which is S5 for every script. A module that raises still gives `None`.
`test_unverified_check.py`'s two cases that deleted `lib/config.py` now
make `UC.sibling.load` raise `ImportError` for it, and are renamed
`test_refuses_to_fail_where_lib_will_not_load` and
`test_refuses_nothing_less_where_lib_will_not_load`.

**`seal_stamp.py`'s standard-library case allows `sibling`.**
`test_seal_stamp.py#Test_module::test_imports_nothing_outside_the_standard_library`
holds the file the `Stop` hook and the gate load to the standard library
(#832). `lib/sibling.py` imports only `importlib.util`, `os` and `sys`,
and `ruff.toml` lints `lib/*.py` at `py39`.

**`loaded_by` reads a string that is a tracked path in full.** The scripts
name a module in a constant (`READER = "skills/verify/scripts/unverified_check.py"`)
and hand the constant to `load`, so an arm that read only the call
`sibling.load("<rel>")` would miss most loads. The arm reads any string
constant that equals a tracked path. S9 is held by
`test_every_entry_point_runs_at_the_floor.py#test_a_script_reaches_what_it_hands_the_loader`,
seen red with the arm removed, as was
`test_what_runs_before_any_floor_is_linted_at_the_floor` (executed:
`seal mutate`). The set the walk derives at HEAD equals `ruff.toml`'s
`per-file-target-version` table (executed: that case passes, and the table
is unchanged).

**What was renamed, and its census.** No unit moves in this phase; the
moves are phase 3's. The removed names are `seal.py#LIB_PURPOSES` and
`#refuse_without_lib`, `settle.py#PURPOSES` and `#load`,
`fold_check.py#load` and `#_loaded`, `chain_check.py#load`,
`pr_body.py#_load`, `broad_gate.py#load`, `pact_check.py#load` and
`unverified_check.py#_load_lib`. `git grep` on each, outside
`seal/threads/`, prints only `.test_durations`, which this phase does not
commit (executed). `tests/skills/test_seal.py#Test_refuse_without_lib` and
`tests/skills/test_pact_check.py#Test_load` go with their units;
`tests/lib/test_sibling.py#Test_load` holds what they held of loading.

**The sentences on loading, item 11 for this phase.** Rewritten in place:
`lib/console.py`'s paragraph on how a script reaches `lib/`, the
docstrings of `lib/fields.py` and `lib/gate.py`, a comment in
`lib/routing.py`, two comments in `lib/tables.py` (one cited
`seal.py#LIB_PURPOSES`), the `rule_changes.py` docstrings that said a
module is "loaded by path", and the `NO_SUBCOMMAND` entry for
`rule_changes.py` in
`tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`.
The list was built with `git grep` on `by path`, `importlib`,
`spec_from_file_location`, the private names the old loaders gave
(`agentic_..._for_...`) and each removed name, over `skills/`, `lib/`,
`docs/`, `agents/` and `CONTRIBUTING.md`. It is a sample. `lib/console.py`
still says that some scripts under `.github/scripts/` load by path, which
is true at HEAD until phase 2.

**The scenarios this phase owes.**

- S1 (executed: `settle.py` run as `__main__` over a clone of HEAD with
  `SourceFileLoader.exec_module` counted by file). With no argument, HEAD
  executes 10 files once each, `lib/sibling.py` among them, where the base
  executed 9 files 165 times (`lib/blocks.py` 32 times). With
  `--all-earlier`, HEAD executes the same 10 once each, where the base
  executed 760 (`lib/blocks.py` 151 times). Stdout is byte-identical to the
  base's by `cmp`, 108,756 bytes and 308,213 bytes.
- S4 (executed): the eight copied-alone cases pass, each pinning the exact
  stderr. Each went red with the guard's sentence changed in its command
  (executed: `seal mutate`, eight runs).
- S5 (executed): `tests/lib/test_sibling.py#Test_load`, six cases. Seven
  mutants of `lib/sibling.py` went red, 7 of 7.
- S6 (executed: each script under `skills/*/scripts/` copied alone into an
  empty directory and run with no argument, at HEAD, row against the base).
  Every row holds its exit code and its traceback-or-not, but two kinds of
  change. `chain_check.py`, `pr_body.py` and `broad_gate.py` print the
  sentence where they printed their own line, still at exit 2, which is S4.
  `pytest_record/agentic_pytest_record.py` exits 0 at HEAD, where the base
  row ends in a traceback at exit 1. The file is unchanged in this range.
  The probe ran it under the virtualenv's interpreter, which has `pytest`.
  Run at `333fb9def` under `/opt/homebrew/bin/python3`, which has no
  `pytest`, it ends in `ModuleNotFoundError: No module named 'pytest'`. The
  row differs by interpreter, not by this work.
- S7 for `broad_gate.py` (executed): `Test_sibling_module` and the
  label case pass; three mutants of `sibling_module` and the label site went
  red, 3 of 3.
- S9: above.

**Q1 is answered only as far as the narrow runs go.** No case in the
phase-boundary set failed from one `lib/` module instance being shared by
every script in one `pytest` process (executed). Whether a test file
outside that set meets it is the broad gate's to show.
