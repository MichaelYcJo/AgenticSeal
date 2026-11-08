# Closing memo: 1793935041-the-directory-refuses-every-command-hook

## Not verified

| Item | Who must answer |
|---|---|
| closed whether the harness substitutes `${CLAUDE_PLUGIN_ROOT}` and `$ARGUMENTS` in `skills/start/SKILL.md`'s body, and whether a session the entry reaches opens the core once at step 1; no case can run the harness, and the spike measured `${CLAUDE_PLUGIN_DATA}` alone | moot: `skills/start/SKILL.md` is not in the tree. #1430's squash `591c136cc` removes it (`git show 591c136cc --stat -- skills/start/SKILL.md`, 80 lines deleted), and the core now reaches a session through the `SessionStart` hook of `hooks/hooks.json` (settle of 0.32.6 to 0.34.1) |
| closed whether a plain request to change code, such as `fix #42` or "이 기능 고쳐줘", makes the model invoke `agentic:start` rather than `agentic:implement` or no skill, and whether question 1 then shows the ladder's answer with the ` (Recommended)` mark and the options in the table's order; the description and the orchestration paragraph are the one carrier, and no case can run the model's choice of a skill or read the question it puts | moot: the entry skill `agentic:start`, whose description was the unit measured, left the tree at `591c136cc` (#1430), and `ls skills/` lists no `start`; what a plain request reaches under 0.35.0 is a row of `seal/threads/1794128303-the-plugin-ships-two-hooks-again/gaps.md`, which stays with its work item (settle of 0.32.6 to 0.34.1) |
| closed whether an orchestrator on a run routed `Automation` `yes` follows the paragraph of `docs/running/the-run.md` *The run* that replaced the question gate; the rule is guidance with no check line, and no case can hold an orchestrator's choice to ask | two later runs routed `Automation` `yes`: `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/plan.md:55`, under the installed 0.33.0, whose one blocking act was the removal of a remote branch, which reaches outside the repository, and `seal/threads/1794096494-compare-reads-a-grader-with-a-string-target/frame/questions.md` Q1, proceeded on its default and quoted in that work item's `pr.md` (settle of 0.32.6 to 0.34.1) |
| closed whether a plain request such as "review this PR <url>" opens `agentic:code-review` and a typed `/code-review` runs Claude Code's built-in command, now that no gate asks which review was meant; the description is the one carrier, and no case can run the model's choice of a skill | a measurement no record asks for: no open issue, failed run or other work item's rule or design waits on it, and the answer would decide only whether the skill's description needs rewording; a lapse would show as a built-in `/code-review` run where a review was asked for, which no later record names. Nothing is opened (settle of 0.32.6 to 0.34.1) |
| closed whether the `Stop` entry `seal stamp --install` writes into a person's `settings.json` draws the stamp on the screen once after the sealer queues it, and whether bootstrap's question and `skills/update/SKILL.md` step 4b reach the person with the data directory spelled; `tests/skills/test_seal_stamp.py` runs the launcher as the entry's command runs it, and no case can run the harness that reads the entry | moot: `seal stamp --install` is gone. #1430's squash `591c136cc` cut the install, remove and hook entries from `skills/verify/scripts/seal_stamp.py#main`, whose parser now takes `--from`, `--guarantee` and `--stop` alone, registers the `Stop` hook in `hooks/hooks.json`, and turns `skills/update/SKILL.md` step 4b into the removal of the launcher an earlier release wrote (settle of 0.32.6 to 0.34.1) |
| closed whether the entry's `py -3` half starts the launcher on Windows where `python3` is absent, and whether the drawing reaches a Windows terminal; the cases run on the platform CI and this machine give | moot: the person-side entry whose `py -3` half the row measures left with the launcher at `591c136cc` (#1430); the `py -3` half now in `hooks/hooks.json`'s two commands is a row of `seal/threads/1794128303-the-plugin-ships-two-hooks-again/gaps.md`, which stays with its work item (settle of 0.32.6 to 0.34.1) |

## Not done

`seal payload`'s session table counts the core the entry opens and not the
entry skill's own body, which also reaches every session the entry takes. `frame/design.md` *Scope* item 2 names the core row
alone, and a second row would be a measure the frame did not ask for.

`lib/gate.py` and `tests/lib/test_gate.py`, at `hooks/lib/gate.py` and
`tests/hooks/test_gate.py` until phase 7 moved them, were not removed in
phase 2, though `frame/design.md` *Removes* names them. The module is the
pull request's parity arm's reader, loaded by
`skills/code-review/scripts/chain_check.py#parity_readers`, and
`trail/phases/phase-2.md` gives the grounds.

The plugin's one-line description dropped "without asking anyone" in phase
4, at `README.md:8-9`, `README.ko.md:8-9`, `.claude-plugin/plugin.json` and
both descriptions of `.claude-plugin/marketplace.json`, as the default the
orchestrator's judgment row of 2026-11-06 chose. The owner has not read the
new sentence, and may overturn it in the pull request.

Twelve files `dist` holds still name one of the thirteen release-only
scripts by path, `docs/releasing/` and `lib/console.py` among them,
and a reader of `dist` finds no file there. Phase 6 rewrote the five that
cited a script by `path#name`, which the archive's census reads, and left
the path-only mentions, which name this repository's file and which no
census reads. `trail/phases/phase-6.md` lists the twelve.

The repository's GitHub label `hooks-gates` keeps its name and its
description, "Hooks, the commit gate, the worktree guard". The label lives
outside the tree, so no phase changes it; the owner renames it or leaves it.
