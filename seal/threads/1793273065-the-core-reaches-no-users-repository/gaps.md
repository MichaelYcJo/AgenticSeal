# Closing memo: 1793273065-the-core-reaches-no-users-repository

## Why this work exists

The plugin's core stood only in this repository's `CLAUDE.md`, so no agent or session in a plugin user's repository read it; it becomes `skills/core/SKILL.md`, which every agent preloads and the preset block imports.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The agents' opening sentence wraps | `frame/design.md` gives the sentence on one line of 115 columns; `tests/behaviour/test_docs_line_wrap.py` holds agent definitions to 88 | the design's words, with one fixed break after "and both" | `trail/phases/phase-1.md` *What this phase found* |
| `uninstall.sh` takes the installer's default | `frame/design.md` *Scope* item 4: "`uninstall.sh` is unchanged"; the design gives `install.sh` the default `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md`, and `uninstall.sh` kept `$HOME/.claude/CLAUDE.md` | both scripts default to `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md` | left as it was, under `CLAUDE_CONFIG_DIR` the uninstaller would remove nothing from the file the installer wrote; `trail/phases/phase-2.md` *What this phase found* |
| `install.sh` refuses an option | the design removes `--project` and names no handling for it; after the removal, `bash install.sh --project` would take `--project` as the target path | an argument starting with `-` exits 1 with `Unknown option <arg>` and writes nothing | the README told users to type `--project` until this release; `trail/phases/phase-2.md` |
| Two block cases keep their home half | `frame/design.md` *Removes* row "Cases that pin a rule to the block" removes `test_implement_and_the_preset_block_do_not_drift` and `test_the_preset_says_whose_decision_the_place_is` | the first stays as `test_the_routing_section_holds_the_answers_and_the_shape`, reading `skills/implement/orchestration.md` alone; the second stays as `test_the_bootstrap_says_whose_decision_the_place_is`, reading `skills/implement/bootstrap.md` alone | their home-side assertions were pinned by no other case; `trail/phases/phase-2.md` |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch | the orchestrator, through `seal gate` |
| `frame/questions.md` Q2: the one-line block in `~/.claude/CLAUDE.md` puts the core in an interactive and a headless session with no dialog | the orchestrator, on an installed machine after the 0.25.0 release |
| `/agentic:preset-setup` as rewritten in phase 2 writes the one-line block and names a missing import target when a session runs it; no case runs a skill's procedure | the owner, who types the command (its `disable-model-invocation: true` keeps a session from loading it), on an installed machine after the 0.25.0 release |

## Not done

On a machine with the new block installed, every agent reads the core twice: once through its `skills:` list and once through `~/.claude/CLAUDE.md`'s import, which the harness adds to every spawn (#292). That is the core's 6,711 B a second time, about 2,100 tokens at 3.2 B/token, inside a per-agent growth of 6,796 B (`trail/phases/phase-3.md`). Both paths stay. The issue's Done-when names `skills:` as the agents' path, and that path is the only one that reaches a user who never ran the installer. A user-scope import cannot be made conditional on who reads it. The orchestrator decided this on 2026-10-29 against the issue's constraint *No session reads the core twice*, which names sessions. #1183's review weighs it, because a `SessionStart` hook may not reach a subagent at all (unverified).

## Fed back into the design

none
