# Phase 2: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | d58605ee |

## What this phase was asked

Phase 2 of `frame/plan.md`, and only that phase. The block becomes the two
markers and the `@` line. Each rule the block held stands in the home that
`frame/design.md` *Removes* row 1 names. `install.sh` loses `--project`, the
scope prompt and the overlap loop, and gains a warning for a missing import
target. `preset-setup` and `update` step 4 change as *Scope* item 4 says. The
README rows, the reworded docstrings and the `orchestration.md:458` row
follow. The cases that pinned rules to the block are replaced by cases that
read the homes, and S7's two installer cases are added. `frame/questions.md`
Q1 was answered A1 by the owner, so A1 alone was built; the hook shape is
#1183's. Q2 stays open on its default. The line coordinates were the
framer's at `7280a7cc`, to be opened again before editing. Phase 3's
`payload_meter.py` work was not started. Done when: the commits are on the
branch, row 2's *Verified by* modules pass, `bash install.sh` has been run by
hand against a scratch target and its warning read, this record is written,
and the plan's Status cell holds the closing commit.

## What this phase found

**The frame held at every coordinate it named.** Each line stood where the
frame said, or moved by phase 1's edits only: `install.sh:22-42`, `:106-116`
and `:123-125`; `hooks/mode-gate.py:16-19`;
`skills/verify/scripts/broad_gate.py:4-5`; the `orchestration.md` row, now
at line 460; and `skills/verify/orchestration.md:146`.

**Three places diverge from the frame, each recorded in `gaps.md`.**

- `uninstall.sh` now takes the installer's default. The design gives
  `install.sh` the default `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md`
  and says `uninstall.sh` is unchanged. Unchanged, the uninstaller would
  remove nothing from the file the installer wrote under `CLAUDE_CONFIG_DIR`.
  `test_both_scripts_default_to_the_config_directorys_file` runs both scripts
  with no argument. It sets `HOME` to a scratch directory too, so a script
  that ignores the variable writes there and not into the machine's file.
- `install.sh` refuses an argument that starts with `-`, printing `Unknown
  option <arg>`, and writes nothing. Without that, `bash install.sh
  --project`, which the README taught until this release, would treat
  `--project` as the target path.
- Two of the cases the design removes keep their home half. Their home-side
  assertions were pinned by no other case. `grep` over `tests/` found "What
  is checked is the answer", "each box is a row of" and "in a command of its
  own" pinned only by `test_implement_and_the_preset_block_do_not_drift`. It
  is now `test_the_routing_section_holds_the_answers_and_the_shape`, and
  reads `skills/implement/orchestration.md` alone. It also took the
  `seal no-work-item` and `Seal-Routing: no work item` assertions from the
  removed block case. "Creating the root is what opts the repository in" was
  pinned only by `test_the_preset_says_whose_decision_the_place_is`. It is
  now `test_the_bootstrap_says_whose_decision_the_place_is`, and reads the
  Bootstrap's own sentence, "is the person's decision and not the
  orchestrator's".

**The homes are pinned in the one-home module, and the block is one of its
carriers.** `tests/text/test_the_rules_claude_md_names_have_one_home.py`
already held one home per rule and already listed the block's template
among the carriers. Its `RULES` gained `lint`, `tooling` and `worktree`, with
needles from the new sentences in `skills/implement/SKILL.md` step 2 and
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket*. A copy of a needle in any carrier, the block included, is now
named. The three-fix, verification and batch rules were already stated in
their homes and pinned there. That is `agents/crafter.md`, contract rules 2,
4 and 10, and `skills/verify/SKILL.md`, as *Removes* row 1 says. They needed
no new case.

**The removed cases.** `test_the_preset_block_states_the_rule_the_loaded_files_assume`
(`tests/text/test_broad_gate_rule.py`); `test_the_preset_block_carries_the_routing_decision`
(`tests/text/test_review_axes.py`), whose replacement is phase 1's
`test_the_core_names_where_the_routing_question_is`; in
`tests/behaviour/test_first_setup_asks_once.py`, the four block cases, the
`preset()` and `routing_rule()` helpers and the comment above them, which
now names the files that hold the rule; and
`test_the_preset_block_carries_it_too` in
`tests/behaviour/test_waiver_decided_at_start.py`, whose `STALE` and `SHAPE`
assertions `test_question_1_is_asked_alone_and_the_boxes_only_under_per_axis`
already makes against the orchestrator's section. Two comments there said
the shape sentence is shared with the block. They now say the shape sentence
stands in the orchestrator's section alone.

**New cases, each seen red against the tree before the code.** In
`tests/behaviour/test_the_installer_writes_the_block_from_its_template.py`:
`test_the_block_is_one_import_of_the_core_and_no_rule` (S2, S4),
`test_install_sh_warns_when_the_core_it_imports_is_not_there` and
`test_install_sh_says_nothing_when_the_core_is_there` (S7; the second's
target holds the old loop's keywords, so the loop's removal is pinned too),
`test_both_scripts_default_to_the_config_directorys_file`, and
`test_install_sh_has_no_project_scope`. The `RULES` entries above were red
in `test_each_home_states_its_rule_under_its_section`. The `the core
arrived` assertion in `tests/behaviour/test_release_hygiene.py#test_update_tells_the_user_when_the_preset_block_changed`
was red against the old step. The red run had the old `install.sh`,
template and skills, with only the cases edited. Eight cases failed, each on
its own assertion: these seven, and
`test_install_sh_replaces_an_older_block_from_the_template`, whose stale
block is now made from the `@` line.

**`seal mutate`, one run per unit, each red in the end.** The runs broke the
warning's `warn`, the option `case`, each script's default, the template's
`@` line, the lint, tooling and worktree sentences, update step 4's "the
core arrived", and the Bootstrap's "person's decision". Two survived at
first, and each was fixed in a commit of its own:

- The option refusal survived because, with the `case` broken, `dirname
  --project` fails under `set -e`, so the exit code stayed non-zero. The
  case now reads `Unknown option --project` (`df033453`).
- "the core arrived" survived because two rows of update step 4 said it. The
  old-markers row now says "what the row above does", so the phrase stands
  once (`d58605ee`).

**`bash install.sh` by hand.** It ran against a scratch `CLAUDE.md` under
the session's scratchpad, with nothing beside it. It exited 0, wrote the
three-line block, and printed `[warn] The block imports
<scratch>/plugins/marketplaces/agenticseal/skills/core/SKILL.md, which is not
a file, so no session reads the core yet.`, followed by where to install the
plugin. `bash install.sh --project` printed `[error] Unknown option
--project. Usage: bash install.sh [<target-CLAUDE.md>]` and exited 1. The
scratch directory was removed afterwards.

**The phase-boundary set was green.** It was one `bin/test` command over 97
modules: row 2's *Verified by* modules, and every module that names,
imports or globs a path this phase changed. It passed 4,800 cases and
skipped 10. None of the skips is in this phase's cases. The two reds phase 1
recorded as older than its own diff passed in this run too.

**Left for others.** `skills/update/SKILL.md` step 4's `diff` reads
`~/.claude/CLAUDE.md` and the clone under `~/.claude/plugins`, not under
`CLAUDE_CONFIG_DIR`. That was true before this phase and this phase did not
touch it.
