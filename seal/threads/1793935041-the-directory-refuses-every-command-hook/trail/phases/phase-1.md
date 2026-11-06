# Phase 1: 1793935041-the-directory-refuses-every-command-hook

## What this phase found

**The frame holds for this phase.** Every coordinate phase 1's row names
stood at `0393a057`: `hooks/core-start.py`, `hooks/lib/core.py`,
`skills/verify/scripts/core_check.py`, their three test modules, the
`session-core` entry of `hooks/hooks.json` and `hooks/dispatch.py#GROUPS`,
`skills/verify/scripts/payload_meter.py`'s session row, and the `core`
entry of `seal.py#TOOLS`. The build follows `frame/design.md` *Scope*
items 1 and 2.

**The closed set of statements on the removed units reached past the
Delivers cell, and each was edited in this phase.** The method was
`git grep -n -E` for `core-start`, `seal core`, `hooks/lib/core`,
`core_check`, `session-core`, `SessionStart hook` and `AgenticSeal core
from` over the tree, then a second grep for sentences that tie the core to
a hook or say every session holds it. Each edit below is a departure from
the Delivers cell, made on the grounds given:

- `docs/checks/the-session-hooks.md`, the paragraph opening **The core
  reaches a session from the plugin's own `SessionStart` hook, once.**,
  is removed now and not with the document in phase 5. Its `check:` line
  named the three removed test modules, and `seal rules --check` refuses a
  target that is gone (`frame/plan.md` *Technical context* *Constraints*).
- `docs/running/what-a-script-gates.md`'s `seal fold`, `seal core` row now
  names `seal fold` alone. The frame's `## Removes` places that change with
  the gates' rows, but `seal core` is this phase's removal.
- `skills/implement/orchestration.md` *Orchestrator: the order inside a
  ticket* step 1 told the orchestrator to run `seal core` before the first
  edit. It now says the orchestrator has read the core once, which
  `/agentic:start` does at its first step. The plan's technical context did
  not list this line.
- `skills/core/SKILL.md`'s `description:` said a session receives the core
  from the `SessionStart` hook; it now says the entry opens it. The frame
  names the core's lines 101 and 107 to 111 for phase 2 and not the
  description.
- `docs/layout/the-record-layout.md` *The root records*, the `CLAUDE.md`
  row, and `CONTRIBUTING.md` *Proposing a new gate or skill*, "which every
  session loads", stated the hook's delivery and now state the entry's.
- Both READMEs' *How it works* opening sentence said every session starts
  with the core; it now names the session started with `/agentic:start`.
- Both READMEs' gate table loses its `core-start` row in this commit,
  because `tests/behaviour/test_chain_hooks_hardening.py#test_the_gate_table_has_one_row_for_each_script_groups_registers`
  derives the table from `GROUPS`.
- Both READMEs' *Commands* table gains a `/agentic:start` row.
  `#test_every_shipped_skill_is_named_in_both_readmes` asks a user-invoked
  skill to be shown in the form a person types.
- `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py#SHIPPED`
  loses `seal core`, since the case derives the shipped commands from
  `seal.py#TOOLS`.
- `tests/behaviour/test_the_old_block_leaves_through_update.py` pinned the
  update's step 4 with the needle "`SessionStart` hook"; the needle is now
  "`/agentic:start` opens it". Docstrings and comments in that module,
  `tests/behaviour/test_first_setup_asks_once.py`,
  `tests/text/test_broad_gate_rule.py`,
  `tests/text/test_the_rules_claude_md_names_have_one_home.py` and
  `tests/text/test_a_language_section_of_writing_style_opens_alone.py`
  stated the hook's delivery and now state the entry's.
- `CLAUDE.md`'s second paragraph told a session with no hook message in
  its context to open the core itself. With no hook there is no message to
  look for, so the paragraph goes, and its last sentence, on the copy an
  agent spawned here receives, stays as a paragraph of its own.

**One file outside `seal/threads/` still names a removed unit, and the
frame says not to edit it.** The plan's
`git grep -n 'core-start\|seal core\|hooks/lib/core'` exits 1 at the build
commit, matching nothing. The wider grep for `core_check` and
`session-core` lists `.test_durations` alone, whose test ids name
`tests/skills/test_core_check.py` and the `core` row of
`tests/skills/test_seal.py`. `frame/design.md` *Grounding* states that
`.test_durations` is rebuilt by `.github/scripts/durations_union.py` from
CI's runs and needs no hand edit, so it was left as it stands.

**The meter's session row is one `file_row`.** `session_composition` now
appends `file_row(root, CORE, ENTRY_ROW, "entry", sections)`: the row is
named `/agentic:start: skills/core/SKILL.md`, its share is `entry`, and its
bytes and characters are the core file's whole, frontmatter included, as
the design's *Scope* item 2 states. `file_row` already marks a missing file
`missing` and splits a file at its headings under `--sections`, so the
row's separate branch went. `_core`, the loader of `hooks/lib/core.py`,
and its exit 2 went with the module. The `core.py` row of
`Test_module#test_a_script_copied_alone_exits_2_and_names_what_it_misses`
went too, and `#test_a_copy_without_the_scan_exits_2_on_a_run_that_reads_a_claude_md`
now copies the script alone, since no sibling module stands before the scan.
The `--calibrate` baseline sentence of the module's docstring now says the
core the entry opens reaches no subagent.

**Seen red, and the mutation runs.** The plan row asks for a new case that
the session row counts the core file whole. The S8 group already held the
hook row's case, so that case was rewritten to the entry row in place of a
case added beside it, as `agents/crafter.md` *A new test starts from its
group* asks. The four rewritten S8 cases of
`tests/skills/test_payload_meter.py` and the copy-alone case were run
against the meter at `0393a057` before it changed: 5 failed, 2 passed.
The main case, `#test_the_session_table_carries_the_entry_row_at_the_core_files_whole_size`,
failed there on the row's share. Its guard on the whole file was shown red
by `seal mutate` with the entry row's bytes set to 1. It failed at the
bytes line with `(1, 67) == (68, 67)`. Four `seal mutate` runs over
`skills/verify/scripts/payload_meter.py`, each with
`-k entry_row` or `-k 'session or entry_row'`, went red: the bytes set to
1 (2 cases), the present row's note emptied (1 case), the missing row's
note emptied (1 case), and the share `entry` read as `harness` (3 cases).
`skills/start/SKILL.md` is prose that no script parses, so no mutation
covers it; the two `test_chain_hooks_hardening.py` cases the design's
scenario names read its frontmatter and the READMEs.

**The entry cites where it could copy.** Step 4 of `skills/start/SKILL.md`
sends a change with no work item to the third answer of
`skills/implement/orchestration.md` *Question 1*, which still names
`seal no-work-item` at this phase. Phase 2's edit of that row then reaches
the entry with no edit to the entry. Step 1 names the plugin root both as
`${CLAUDE_PLUGIN_ROOT}` and as the directory two above the base directory
the harness prints, because the spike in *Grounding* measured the
substitution of `${CLAUDE_PLUGIN_DATA}` in a skill body and not of
`${CLAUDE_PLUGIN_ROOT}`; `gaps.md` holds that as not verified.

**The phase boundary set.** The modules that read a path this phase
changed were listed by `git grep -l` over `tests/` for each changed path's
name and for a glob of `skills/`, with the plan row's three modules and
every changed test module added: 90 modules. One command ran them at the
build's tree. 4,032 passed and 1 failed,
`test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which reads this work item's `gaps.md`. With `gaps.md` written, the plan
row's three modules ran again in one command: 481 passed, exit 0.
`seal rules --check` exited 0, and `seal unverified .` read the memo's one
open row.
