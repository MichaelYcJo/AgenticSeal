# Implementation Plan: 1793273065-the-core-reaches-no-users-repository

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phase 1.

## Summary

The core moves from `CLAUDE.md` into `skills/core/SKILL.md`, every agent
definition preloads it before `agent-contract`, the preset block becomes one
`@` line that imports it from the marketplace clone, and the rules the block
held go to the one file that applies each. `seal payload` learns to follow
an `@` line so the cost of loading the core is measured, and the first pull
request into `release/v0.25.0` moves the version with its changelog
fragment. Four phases, each a slice the tests can read.

## Technical context

- `CLAUDE.md:3-93` is the core as #1172 left it (`51eca3ac`); nothing else
  in the file. `tests/text/test_the_rules_claude_md_names_have_one_home.py#LINKED`
  requires the file that holds the batch link to name
  `skills/implement/SKILL.md` and its section;
  `tests/text/test_a_language_section_of_writing_style_opens_alone.py:178-187`
  requires `CLAUDE.md` to name the writing rules and the block not to; both
  read the core after phase 1.
- `agents/*.md:7-10`: `skills:` lists `agent-contract` alone;
  `tests/text/test_every_agent_reads_the_contract.py#shape_problems` refuses
  any other list and any other opening sentence.
- `templates/setup/claude-md-block.md`: eight bullets between two markers;
  `install.sh:64-69` cuts the marker region with `awk`; eight cases in
  `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py`
  hold the installed block equal to it. The cases `frame/design.md`
  *Removes* lists read its rules.
- `skills/verify/scripts/payload_meter.py#composition` (lines 297-323)
  appends `CLAUDE.md` and `~/.claude/CLAUDE.md` as two flat rows;
  `tests/skills/test_payload_meter.py#run` sets `HOME` for a run, and
  `#test_the_claude_md_pair_is_marked_as_the_harness_share` pins the pair's
  two paths.
- `~/.claude/plugins/marketplaces/agenticseal/` is the clone
  `claude plugin marketplace update` pulls (`skills/update/SKILL.md` step 2),
  and `~/.claude/plugins/cache/agenticseal/agentic/<version>/` is the copy a
  session runs; the clone's path has no version in it.
- The chosen approach's failure in six months: a machine whose plugins root
  is not under the directory that holds its `CLAUDE.md` (a
  `CLAUDE_CODE_PLUGIN_CACHE_DIR`, or a marketplace registered from a local
  directory) has no file at the imported path, and the import loads nothing
  without a word (probe e). The installer's warning fires once, at install
  time; a plugins root moved afterwards is noticed only when somebody opens
  `/memory`. The agents still carry the core by `skills:`, so the chain's
  parties lose nothing; the orchestrating session on that machine does.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 The block holds one `@` line, a path relative to the file that holds it: `@plugins/marketplaces/agenticseal/skills/core/SKILL.md`; `CLAUDE.md` here links and says the tree's copy governs where the branch changes it | A plugins root elsewhere (above), or a user who runs `claude plugin marketplace update` without the install step and reads a core one release ahead of their skills until they run the second command | **Chosen.** Rests on the docs' resolution rule and the no-dialog rule for user-scope imports (read), on an in-project import loading headless (probe a), and on the block staying a fixed template the eight installer cases already hold |
| A2 The same line as `@~/.claude/plugins/…` (the issue's first shape) | Under `CLAUDE_CONFIG_DIR` the plugins move with the config directory and `~` does not, so the import dangles for exactly the users whose setup is not the default | Rejected for A1's relative form, which follows the config directory |
| A3 A per-machine symlink `~/.claude/agentic-core.md`, pointed by the installer at the clone and by the owner at the tree (the issue's second shape) | Symlinks are followed (probe b), and then every project on the development machine reads an unreleased core beside released agents; `ln -s` under Git Bash on Windows writes a copy that never updates; one more file for `uninstall.sh`; and what it buys, the tree's core governing here, a sentence in `CLAUDE.md` and `git diff` give with no mechanism | Rejected |
| A4 This repository's `CLAUDE.md` imports `@skills/core/SKILL.md` as well | The installed copy and the tree's are two files, so the once-only reading (probe c) does not merge them, and every session here reads the core twice, which the issue's first constraint refuses and `test_this_repository_carries_no_copy_of_the_block` exists to stop | Rejected |
| A5 A `SessionStart` hook in `hooks/hooks.json` prints `${CLAUDE_PLUGIN_ROOT}/skills/core/SKILL.md`; the block, `install.sh`, `uninstall.sh`, `preset-setup` and update step 4 retire. The core is then always the installed version, no path is assumed, no scope exists, and the plugin delivers it as it delivers its skills | The core arrives as hook context, not in the memory section `/memory` lists, so a user cannot see what loaded and can opt out only by disabling the plugin's hooks; `--bare` skips it; every installed `~/.claude/CLAUDE.md` still holds the old block, so a removal step survives one release anyway; and it retires five files and about twelve cases in the first item of a release whose next item, #1148, reads every document against the core. The premise that keeps the block, "a plugin cannot carry a CLAUDE.md block" (`install.sh:7`), is false as stated: a hook carries context (probe f, docs). What keeps it is narrower: the `@` import is the harness's own memory mechanism, visible to the user and deletable by them, and the block is on every installed machine already | Not taken by default. Q1 puts it to the owner with this row's evidence |
| A6 Keep the block's rules and add the link beside them | Every rule has a second source, which the core forbids and the issue's Done-when refuses | Rejected |
| A7 Fold the core into `skills/agent-contract/SKILL.md` and import that | The contract holds rules an orchestrating session must not follow (rule 6: open no pull request), and the issue refuses a core with two sides | Rejected |
| A8 Import from the versioned cache path `plugins/cache/agenticseal/agentic/<version>/…` | The template then carries the version, a second copy of `plugin.json`'s that every release bumps by hand | Rejected |
| A9 Keep `install.sh --project` | From a project-level file the import is external: the approval dialog gates it, declining disables it for good, and a headless session never loads it (probe d, docs). A committed block gives a teammate without the plugin nothing, since the path does not exist on their machine | Rejected; the scope goes |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `skills/core/SKILL.md` holds the core with the one added sentence; `CLAUDE.md` holds *The core* and nothing else; every `agents/*.md` lists `core` then `agent-contract` and opens with the new sentence; `CONTRIBUTING.md:368`, `:381`, `:473`, `tests/text/test_a_rider_reaches_its_file.py:66` and `tests/behaviour/test_chain_hooks_hardening.py:773` name the core's path; `.github/scripts/release_report.py#DOCUMENTS` gains the core; the tests that read `CLAUDE.md` for the core read `skills/core/SKILL.md` | `tests/text/test_every_agent_reads_the_contract.py`, `tests/text/test_the_rules_claude_md_names_have_one_home.py`, `tests/text/test_a_language_section_of_writing_style_opens_alone.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py#test_this_repository_carries_no_copy_of_the_block`, `tests/github/test_release_report.py`, `tests/behaviour/test_docs_line_wrap.py`; `bin/seal payload` lists the core for every agent | 5a283bd8 |
| 2 | The block is the markers and the `@` line; each rule it held stands in its home (`frame/design.md` *Removes* row 1): the tooling and lint sentences in `skills/implement/SKILL.md` step 2, the worktree sentence in `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, `skills/verify/orchestration.md:146` citing the crafter's rule; `install.sh` loses `--project`, the prompt and the overlap loop and gains the exists warning; `preset-setup` and `update` step 4 as *Scope* item 4 says; the README rows; `hooks/mode-gate.py`, `skills/verify/scripts/broad_gate.py` and `skills/implement/orchestration.md:458` reworded; the block-pinning cases replaced by cases that read the homes and the core's routing sentence; S7's two installer cases | `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py`, `tests/behaviour/test_first_setup_asks_once.py`, `tests/behaviour/test_waiver_decided_at_start.py`, `tests/text/test_review_axes.py`, `tests/text/test_broad_gate_rule.py`, `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`; `bash install.sh <scratch target>` by hand, read for the warning | d58605ee |
| 3 | `payload_meter.py#composition` follows `@` lines as `frame/design.md` *Scope* item 5 states; the before and after totals measured against a scratch home (today's block; the new block beside a copy of the tree at `plugins/marketplaces/agenticseal`), written into this phase's record with the two commands | `tests/skills/test_payload_meter.py`, with new cases for an `@` line in each file of the pair, a `~` path, a relative path, a symlink, a missing target, one real path imported twice, and the fourth hop; `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` if it reads the meter | a7329570 |
| 4 | `changelog.md` with the `### Fixed` entry and the `### Process changes` row; `.claude-plugin/plugin.json` at `0.25.0` in the same commit | `tests/github/test_publish_release_note.py` for the fragment's shape; `tests/behaviour/test_release_hygiene.py`; the commit shows both files | |

## Operational impact

- Every installed machine takes the one-line block at its next
  `/agentic:update` after 0.25.0 ships; the eight rules leave the user's
  `~/.claude/CLAUDE.md` with it, and each stands in a skill or definition the
  plugin installs. A user who never runs `/agentic:update` keeps the old
  block, the last release's, which is the state every block change leaves.
- `bash install.sh --project` stops existing. A repository that committed a
  block keeps it until somebody removes it; the next `bash install.sh` on
  that machine writes the global file.
- A machine whose plugins root is not beside its `CLAUDE.md` gets a warning
  from the installer and no core in its sessions; its agents still carry
  it.
- No new dependency, no migration, no environment variable.
