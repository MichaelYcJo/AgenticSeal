# Phase 6: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | 84cf2dd3 |

## What this phase was asked

Phase 6 of `frame/plan.md`, with `frame/design.md` *Scope* item 3 and
scenario S5: `seal core`. The phase was to build
`skills/verify/scripts/core_check.py`, `seal.py#TOOLS["core"]` and
`#HOOK_PURPOSES["core.py"]`, the cheat-sheet row in `README.md` and
`README.ko.md` with a sentence on seeing the core with `! seal core` in
place of `/memory`, and the sentence in `skills/implement/orchestration.md`
*Orchestrator: the order inside a ticket* step 1. The check reads the
session's transcript and exits 0 only where the hook's core is in context
exactly once, whole, and matching the file its first line names. The
handoff carried three facts. The framer had executed the transcript's
compaction shape, the preview past the cap and `CLAUDE_CODE_SESSION_ID` in
an agent's Bash. Phase 5's crafter had measured the hook's output at 6,909
characters. The orchestrator had read that its own session started on the
installed 0.24.2 plugin, so the by-hand run had to exit 1 naming no core
entry. Phase 8 owns the core's prose, so this phase left
`skills/core/SKILL.md` alone.

## What this phase found

**The frame held at every coordinate the row names.** `seal.py#TOOLS` and
`#HOOK_PURPOSES` stood where the plan's *Technical context* says. The
orchestrating session's transcript held `hook_success` attachments in the
shape *Data & interfaces* gives: `hookEvent`, `hookName`, `stdout` and
`content`. `hooks/lib/core.py#parse` read the header as phase 5 built it.

**The harness drops the trailing newlines of `content`, so `content` and
`stdout` are compared after the same normalising as the bodies.** *Scope*
item 3 says the entry passes where `content` equals `stdout`. A survey of
this machine's transcripts found six `SessionStart` entries with a
non-empty `content`. In three, `content` equalled `stdout`. In the other
three, `content` was `stdout` with its trailing newlines removed. The hook
prints the core, which ends with a newline, and `print` adds one more. A
check comparing the raw strings should therefore fail every real session;
no real core entry exists on this machine to show it.
Both comparisons now treat `\r\n` as `\n` and drop trailing newlines, and a
case plants a `stdout` with carriage returns beside a `content` with extra
newlines.

**The no-entry line names the file to open, decided here.** *Scope* item 3
says the orchestrator opens "the file the output names" where `seal core`
reports no core entry. The frame does not say which file the line names.
It names `hooks/lib/core.py#origin` for the working directory and the
plugin around the script. That is the file the hook would have printed: the
clone's core in a clone of the plugin, and the plugin's own elsewhere. A
case holds both.

**Three behaviours the frame left open were decided here, and a case holds
each.** Where two project directories hold the session's file, the newest
by modification time is read. A boundary with no
`compactMetadata.preservedMessages.uuids`, or one holding something other
than a list, keeps nothing, so a shape change fails toward red. An entry
that names no `hookName` is named `SessionStart` in the line.

**The variable's name is read from `hooks/lib/hooksession.py`, not spelled
again.** The script loads `core.py` and `hooksession.py` by path, and
either one missing exits 2 with a sentence naming it.
`seal.py#HOOK_PURPOSES` gained `core.py` as the row asks, with a comment
saying `seal core` reads it; `seal.py` itself does not import it.

**Each new case was seen red first, in two ways.** Against the tree at
`4d436388`, 27 cases failed: the 24 of the new module, census included, the
`core` rows of `tests/skills/test_seal.py`'s tool and missing-module cases,
and `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`'s
classification. The cases written after the code went red under the
mutation runs below.

**One mutant survived the first cases, and a case was added for it.** In
`in_context`, replacing the list guard with `set(kept or ())` survived. A
boundary whose `uuids` field is a mapping now keeps nothing (`cf60f834`),
and the mutant went red.

**`seal mutate` ran once per unit, and every mutant went red in the end.**
The runs were `find` (5 mutants), `entries` (2), `in_context` (7, then the
survivor again), `core_entries` (6), `_normal` (2), `judge` (10), `main`
(7, the `--bare` variable's name among them), `_load` with the session
variable (3), and `seal.py`'s two table entries (3). `seal.py`'s run went
over `tests/skills/test_seal.py`, this module and the classification case
with `-k core`; every other run went over `tests/skills/test_core_check.py`.
After `84cf2dd3` changed the helper the file-change cases write through,
four mutants of `find` and `judge` ran again and went red.

**The test layout refused a twin helper.** `seal layout --check` found the
module's `write` byte-identical to `tests/hooks/test_core.py`'s. The module
now writes through `tests/conftest.py#write` (`84cf2dd3`).
`seal layout --pairs` over the module found 0 pairs.

**The hand run exited 1 naming no core entry, as the handoff said it
would.** `python3 skills/verify/scripts/core_check.py` in this crafter's
Bash read the orchestrating session's transcript. It printed one line: no
core entry in this session's context, because the installed plugin
predates the hook or its hooks are off. The line named
`<clone>/skills/core/SKILL.md` as the file to open once. `bin/seal core
--help` printed the sentence on an agent's Bash.

**No transcript on this machine holds a core entry, so the passing path ran
only over planted transcripts.** The installed plugin is 0.24.2, which has
no core hook. `questions.md` Q2 is the measurement for a real session.

**The phase-boundary set failed one case, and the failure predates this
phase.** The set was one `bin/test -q` command over 122 modules: the named
modules, and every test module that names `seal.py`, `TOOLS`,
`HOOK_PURPOSES`, a README, `orchestration.md` or `verify/scripts`, or globs
`skills/`. It passed 5,367 cases, skipped 11 and failed 1:
`tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census`.
The census `real_identifiers` refuses a real user path at
`trail/phases/phase-5.md:84`, phase 5's hand-run line. That line stood at
`4d436388`, before this phase's first commit, and no file this phase changed
holds it.
