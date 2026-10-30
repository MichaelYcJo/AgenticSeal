# Phase 5: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 36b6b2b6 |

## What this phase was asked

Phase 5 of `frame/plan.md` and `frame/design.md` *Scope* item 2: the core
reaches a session through a plugin `SessionStart` hook. The phase was to
build `hooks/lib/core.py` (`origin`, `header`, `output`, `parse`, `CAP`),
`hooks/core-start.py`, `dispatch.py#GROUPS["session-core"]`, the
`hooks.json` entry with the matcher `startup|clear|compact`, and the
`core-start` row of the gate table in `README.md` and `README.ko.md`. The
same commit was to correct the sentences that stood on "a session receives
the core through the preset block's `@` line": the core's `description:`,
`CLAUDE.md` *The core* as *Scope* item 5 states, and
`skills/implement/orchestration.md:460`. It was the first phase of the A5
redesign. Phase 7 retires the block machinery, so phase 5 left it in place.
The handoff carried two facts. The framer had executed the hook's reach,
resume and cap probes, and had read that `dispatch.py#merge` drops plain
text beside a neighbour's JSON.

## What this phase found

**The frame held at every coordinate the row names.** `hooks/hooks.json`
had one `SessionStart` entry at lines 70 to 79. `GROUPS["session-start"]`
held the three gates the plan names. `merge` keeps only the first JSON
object where any gate prints one. The routing row stood at
`skills/implement/orchestration.md:460`. Each README edition had its gate
table.

**`output` reads the version itself.** *Scope* item 2 gives
`output(cwd, plugin_root)` no version argument, and it says `core-start.py`
takes the version from the plugin root's `plugin.json`. So `output` reads
the version from the manifest at `plugin_root`. `core-start.py` passes only
the payload's `cwd` and the root. Phase 8's meter then calls
`output(root, root)` and gets the version from the same file. Where the
manifest names no version, the header says `plugin unknown`, which still
parses.

**Three behaviours the frame left open were decided here, and a case holds
each.** Where `CLAUDE_PLUGIN_ROOT` is unset, the plugin root is the
directory above the hook's own `hooks/`. A payload that is not a JSON
object, or whose `cwd` is not a string, prints the plugin's core. In both
cases the core still reaches the session, which *Scope* item 2 asks for in
every session. A plugin whose manifest names nothing is a clone of no tree.

**Two mutants survived the first cases, and both were blind spots in the
cases.** In `core-start.py#main`, `or OWN_ROOT` changed to `or ""` survived.
The case ran from this clone, where `os.path.abspath("")` is the same plugin
root. The string guard on `cwd` survived because a `cwd` of `7` never
reaches a type error. The case now starts its process outside the clone and
plants a list-valued `cwd`, and both mutants went red (`36b6b2b6`). The
simplification at `f6a82328` removed a test in `origin` that no case could
tell apart, an empty-string plugin name. The same commit added a refused
header with text after its period, which the `fullmatch` mutant needed.

**`seal mutate` ran once per unit, and every mutant went red.** The runs
were `manifest` (2 mutants), `origin` (4), `header` (2), `output` (5),
`parse` (3), `CAP` (1), `core-start.py#main` (5), `GROUPS["session-core"]`
(2) and the `hooks.json` matcher (1). Each ran over
`tests/hooks/test_core.py` and `tests/hooks/test_core_start.py`.

**Each new case was seen red first, in two ways.** The 16 cases of the
first draft failed against the tree at `ad8f09df` with no `core.py`, no
`core-start.py` and no group. The cases written after the code went red
under the mutation runs above: `Test_manifest`, the refused header with
trailing text, and the two fallback cases as strengthened.

**The test layout reshaped the two modules.** `seal layout --check` refuses
a class that names no top-level definition, and one with no
`test_accepts_` or `test_refuses_` case. The cases now sit in
`Test_manifest`, `Test_header`, `Test_parse`, `Test_origin`, `Test_output`
and `Test_module` for `hooks/lib/core.py`, and in `Test_main` and
`Test_module` for `hooks/core-start.py`. `seal layout --pairs` over the two
files found 0 pairs.

**The hand run printed the expected first line both times.** A `startup`
payload went to `python3 hooks/dispatch.py session-core` with
`CLAUDE_PLUGIN_ROOT` set to a scratch copy of `.claude-plugin/` and the
core. With `cwd` in this clone, the first line named
`<clone>/skills/core/SKILL.md` and 6,909
characters were printed. With `cwd` outside any repository, it named the
scratch copy's core and 6,993 characters were printed. Both exited 0, both
said `plugin 0.25.0`, and both digests equalled `shasum -a 256` of the
tree's core,
`b4cce406e1b3d273953bb629f8e38596e1856f9a6136f29e360d6e7eef8acd00`.

**A docstring outside the row stood on the old fact, and was corrected in
the same commit.**
`tests/behaviour/test_the_installer_writes_the_block_from_its_template.py#test_this_repository_imports_no_core_and_names_the_tree_copy`
said a session here reads the installed core through the block. It now
says a session reads the tree's core from the hook. Phase 7 deletes that
module whole. The other sentences `git grep` finds on "`@` line" and
"preset block" describe the block itself, which stands until phase 7, and
*Removes* names each of them for that phase.

**Until phase 7, a session on a machine whose block holds the template's
`@` line at this commit reads the core twice.** It gets one copy from this
hook and one from the block's import. Both phases land on this branch, so
no release ships between them.

**The phase-boundary set passed.** It was one `bin/test -q` command over
121 modules. They were the named modules, every test module that names
`hooks.json`, a README, `CLAUDE.md`, `dispatch`, the core's path,
`orchestration.md` or `hooks/`, and every module that globs `skills/`. It
passed 5,409 cases and skipped 12.
