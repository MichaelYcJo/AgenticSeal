# Design: update reads the config dir in use (#1184)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| G1 The paths `skills/update/SKILL.md` fixes at `~/.claude` (executed: `git grep -n -E '~/\.claude\|HOME/\.claude\|expanduser' -- skills/update`) | Four coordinates name the directory as a fixed path: `:46` (step 2b reads `~/.claude/plugins/installed_plugins.json` through `os.path.expanduser`), `:61` (step 2b's repair copies from `~/.claude/plugins/marketplaces/agenticseal/`), `:81` (step 3 reads the clone's `origin` with `git -C ~/.claude/plugins/marketplaces/agenticseal`) and `:223` (step 5's sentinel method names `~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/`). Step 4 already resolves the directory: its command is given `"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md"` at `:190`. The issue's `:135-136` is that command, and it stood at `:135` before #1177's phase 7 rewrote step 4. |
| G2 The installer the issue cites is gone (executed: `git show --stat 334189fd` lists `install.sh` and `uninstall.sh` as deleted; `git ls-files` lists no `install.sh`) | #1177's phase 2 gave `install.sh` the default `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md` (read: `git show 334189fd:seal/threads/1793273065-the-core-reaches-no-users-repository/trail/phases/phase-2.md`, lines 36-42). Its phase 7, in the same pull request, deleted the installer, so nothing writes a block any more. `tests/behaviour/test_the_old_block_leaves_through_update.py#test_the_installer_the_uninstaller_and_preset_setup_are_gone` refuses any shipped `.md` that names `install.sh`. So the rule this work takes from the installer is its spelling of the directory, and no shipped text names the installer. |
| G3 Claude Code keeps its plugins under the config directory (executed, this frame: `CLAUDE_CONFIG_DIR=<scratch>/cfg claude plugin marketplace list` lists only the built-in Anthropic directory, while the same command with the variable unset lists `agenticseal`; `ls ~/.claude/plugins` lists `installed_plugins.json`, `marketplaces` and `cache`) | The issue's premise holds. A session started under `CLAUDE_CONFIG_DIR` reads `installed_plugins.json`, the marketplace clone and the version cache under that directory, so step 2b and step 3 read files that are not the ones in use. `installed_plugins.json` records an absolute `installPath` (executed: it reads `.../.claude/plugins/cache/agenticseal/agentic/0.32.1` on this machine), so `"$p"` in step 2b and its repair needs no change. |
| G4 The shell spelling (executed, this frame: `printf` of `"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/installed_plugins.json"` under `bash -c` and `zsh -c`, with the variable unset, set empty and set to a path holding a space) | Both shells print `$HOME/.claude/...` where the variable is unset or empty, and keep the spaced path whole where it is quoted. `skills/verify/scripts/core_check.py:117` reads the variable with `or`, so an empty value falls back there too (read). |
| G5 Claude Code under an empty `CLAUDE_CONFIG_DIR` (executed, this frame: `CLAUDE_CONFIG_DIR= claude plugin marketplace list`, run from an empty scratch directory, lists only the built-in directory and writes nothing there) | Claude Code does not read `~/.claude` when the variable is set empty, and where it does read is not known. The `:-` spelling falls back to `~/.claude` there, as step 4 and `core_check.py` already do. A variable set to the empty string is outside the flow this command serves, so it stays a limit, named in *Scope*, and no guard is built for it. |
| G6 #1177's decision for step 4 (read: `git show 334189fd:seal/threads/1793273065-the-core-reaches-no-users-repository/frame/design.md`, lines 138-142) | #1177 put step 4 on `${CLAUDE_CONFIG_DIR:-~/.claude}/CLAUDE.md`, and its build wrote `$HOME` in place of `~` at `:190`. This work gives the other four coordinates the same spelling and departs from nothing #1177 decided. #1177's phase 2 *Left for others* and its round 1 *Not judged*, the second row, both named `:46`, `:61`, `:81` and `:135` and left them to the orchestrator for an issue (read at 334189fd). #1184 is that issue. |
| G7 What the issue's second *Done when* now asks for (read: `tests/behaviour/test_the_old_block_leaves_through_update.py`, `:31`, `:52-62` and `:149-155`) | Step 4 no longer diffs a template against the file. Since #1177's phase 7 it backs the file up and takes the marker region out. The module runs step 4's program with the target passed as an argument (`take_out`), and `test_step_4_works_on_the_config_directorys_file_and_writes_no_block` compares the shell line's argument to the literal `USER_FILE`. No case lets a shell expand the line, so no case shows that the step works on the file under a set `CLAUDE_CONFIG_DIR`. The case the issue asks for runs step 4's shell line under a scratch config directory that holds a block, and reads that file afterwards. |
| G8 The pins that stand on the text this work edits (read: `tests/behaviour/test_release_hygiene.py#test_update_reads_the_installed_copy_before_it_summarises` and `#test_update_shows_what_changed_from_the_github_releases`) | Step 2b must still carry `installed_plugins.json`, `installPath`, `/.claude-plugin/plugin.json'`, `['version']`, `rsync` and no `/Users/`. Step 3 must still carry `remote get-url origin` and `marketplaces/agenticseal`. The spelling of *Data & interfaces* keeps each of them. |
| G9 The policy in force (executed: `git grep -n CLAUDE_CONFIG_DIR -- docs` and `git grep -n -E 'agentic:update\|skills/update' -- docs`, no hit; a loop over every `seal/threads/*/frame/design.md` *Rule changes* for `update/SKILL`, `CLAUDE_CONFIG` or `/agentic:update`, no hit) | No document of the policy root states where `update` reads, and no unsettled design changes such a rule. The work's subject is a shipped skill's commands, so `## Rule changes` holds the no-change block (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). |
| G10 What runs beside this work (executed: `gh api repos/MichaelYcJo/AgenticSeal/milestones`, the 0.32.2 description; read: `routing.md`; read: `seal/follow-up.md`; executed: `gh release view --json tagName,body`, v0.32.1, no `### Process changes` heading; executed: a loop over the fragments' `### Process changes` rows under `seal/threads/`, none naming `update` or the config directory) | #1190 holds `skills/verify/scripts/core_check.py` and #1185 holds `skills/verify/scripts/payload_meter.py`, and this work edits neither. No follow-up row waits on this work. This work item carries the version move to 0.32.2 (`skills/implement/orchestration.md` *Which branch the pull request lands on is decided with the routing question*). The ticket was read with `gh issue view 1184 --json title,comments` on 2026-11-05 (executed): no comments. |
| G11 How a case runs a shell line here (read: `tests/conftest.py#shell_probe`, `tests/behaviour/test_first_setup_asks_once.py:505-527`, `tests/behaviour/test_release_hygiene.py:1230-1245`; read: `.github/workflows/test.yml:104-110`, macOS and Windows legs) | A case that runs a bash block calls `shell_probe("bash")` first and skips where `bash` is not a usable shell, as on a `windows-latest` runner whose `bash` is the WSL launcher. A case substitutes `sys.executable` for the command it runs, as `test_release_hygiene.py` does for `rules.py`. |

## Scope

In:

1. **Step 2b reads `installed_plugins.json` in the config directory in use.** The first command of step 2b's block passes `"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/installed_plugins.json"` to its program as an argument, which opens `sys.argv[1]`. This replaces `os.path.expanduser('~/.claude/...')`, and the program imports `sys` in place of `os`. The second command of the block is unchanged.
2. **Step 2b's repair copies from the marketplace clone in the config directory in use.** The `rsync` source becomes `"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/marketplaces/agenticseal/"`, quoted.
3. **Step 3 reads the `origin` of the clone in the config directory in use.** The `repo=` line runs `git -C "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/marketplaces/agenticseal"`, quoted, and the rest of the line is unchanged.
4. **Step 5's sentinel method names the version cache in the config directory in use**: `` `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/cache/<marketplace>/<plugin>/<version>/` `` in place of `~/.claude/...` at `:223`.
5. **The procedure says once where these paths stand.** One or two sentences under `## Procedure`, before step 1, say that the plugins and the user's `CLAUDE.md` stand in the directory Claude Code is configured to use, which the shell spells `${CLAUDE_CONFIG_DIR:-$HOME/.claude}`. They say that each command carries that spelling on its own, because the steps' commands do not share a shell. The sentences name the directory in that spelling alone, so *Scope* 6d holds for them too. Step 4's own sentence ("in the `CLAUDE.md` the harness reads as the user's") stays.
6. **Cases run each command under a scratch config directory** (test-first; contract rules 14 and 15). Each case calls `shell_probe("bash")` and runs the command's line from the skill's text under `bash -c`, with `HOME` set to one scratch directory and `CLAUDE_CONFIG_DIR` to another, and `python3` replaced by `sys.executable`:
   - a. **Step 4** (in `tests/behaviour/test_the_old_block_leaves_through_update.py`, which owns step 4): each of the two directories holds a `CLAUDE.md` with a block. With `CLAUDE_CONFIG_DIR` set, the config directory's block is taken out after a backup, and the file under `HOME` is byte for byte as it was. With the variable unset, and again set empty, the file under `HOME` is the one taken out.
   - b. **Step 2b's first two commands** (in a new module, `tests/behaviour/test_update_reads_the_config_directory_in_use.py`): the config directory holds an `installed_plugins.json` whose `installPath` names a scratch copy with a `.claude-plugin/plugin.json`, and `HOME` holds a second set naming a different version. The block prints the config directory's version.
   - c. **Step 3's `repo=` line** (same module): the config directory holds a git repository at `plugins/marketplaces/agenticseal` whose `origin` is a GitHub URL, and `HOME` holds one with another `origin`. The line yields the config directory's `owner/repo`. Nothing reaches the network.
   - d. **No fixed path is left** (same module): `skills/update/SKILL.md` names `~/.claude` or `$HOME/.claude` nowhere except inside the spelling `${CLAUDE_CONFIG_DIR:-$HOME/.claude}`. This covers the repair's `rsync` and step 5's prose, which no case runs.

Out:

- **Other readers of a file Claude Code keeps, outside `update`.** `hooks/lib/press.py:30` (`PROJECTS_ROOT`) and `skills/verify/scripts/session_cost.py:83` (`PROJECTS`) read transcripts under `~/.claude/projects`. The prose of `docs/checks/the-routing-check.md:86` and `skills/verify/orchestration.md:241` names the same directory. `skills/verify/scripts/payload_meter.py:405` and `:424` read `~/.claude/skills` and `~/.claude/CLAUDE.md`. Each has the same cause, a fixed `~/.claude`, outside the issue's subject. `payload_meter.py` is #1185's file in this release. The list is a sample by spelling (contract rule 12), made by `git grep -n -E '~/\.claude|HOME/\.claude|expanduser|Path\.home\(\)|"\.claude"'` over the shipped files; a path built another way is out of its reach. `frame/questions.md` Q1 holds whether they get their own issue.
- **The plugin's own machine-local state under `~/.claude/agentic/`**: `hooks/version-check.py:55`, `skills/verify/scripts/pact_check.py`, and the parity paths in `skills/legacy-parity/SKILL.md`, `skills/parity-setup/SKILL.md` and `templates/setup/parity.md`. These are files the plugin chose to keep there, not files Claude Code keeps, so a set `CLAUDE_CONFIG_DIR` does not make them stale.
- **`skills/verify/scripts/core_check.py`**: #1190's file, and it already resolves the directory (G4).
- **`docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md` and its Korean copy**: a dated record of what was measured on one machine, which names that machine's paths.
- **A `CLAUDE_CONFIG_DIR` set to the empty string** (G5): the spelling falls back to `~/.claude`, where Claude Code does not. This is a limit, and nothing is built for it.
- **Windows**: the skill's commands are bash, and the cases skip where `shell_probe` finds no usable `bash`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 Step 4 under a set config directory | Given `CLAUDE_CONFIG_DIR` names a directory whose `CLAUDE.md` holds a block, and `~/.claude/CLAUDE.md` holds another. When step 4's shell line runs. Then the config directory's block is taken out with its markers, `CLAUDE.md.bak` stands beside that file with the text as it was, and `~/.claude/CLAUDE.md` is unchanged. | *Scope* 6a, seen red with `:190`'s argument rewritten to `"$HOME/.claude/CLAUDE.md"` |
| S2 Step 4 with the variable unset or empty | Given the same two files. When step 4's shell line runs with `CLAUDE_CONFIG_DIR` unset, and again set empty. Then `~/.claude/CLAUDE.md` is the file taken out. | *Scope* 6a |
| S3 Step 2b reads the copy installed in the config directory | Given the config directory and `~/.claude` each hold an `installed_plugins.json` naming a copy of a different version. When step 2b's two commands run. Then they print the version of the copy the config directory names. | *Scope* 6b, seen red against `:46` as it stands |
| S4 Step 3 reads the clone in the config directory | Given each directory holds a marketplace clone with a different `origin`. When step 3's `repo=` line runs. Then `repo` is the config directory's `owner/repo`. | *Scope* 6c, seen red against `:81` as it stands |
| S5 No fixed `~/.claude` stays in the skill | Given the skill after the build. When it is searched for `~/.claude` and `$HOME/.claude`. Then each hit lies inside `${CLAUDE_CONFIG_DIR:-$HOME/.claude}`. | *Scope* 6d, seen red against the skill as it stands, which holds four hits |
| S6 The pins on steps 2b and 3 hold | Given the edited skill. When `tests/behaviour/test_release_hygiene.py`'s two update cases run. Then both pass with no needle changed. | The narrow run of those two cases (G8) |

## Data & interfaces

The command lines after the build, in the skill's bash fences. Step 2b, first command:

```bash
p=$(python3 -c "import json,sys;d=json.load(open(sys.argv[1],encoding='utf-8'));print(d['plugins']['agentic@agenticseal'][0]['installPath'])" "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/installed_plugins.json")
```

Step 2b's repair, second line:

```bash
rsync -a --exclude '.git' "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/marketplaces/agenticseal/" "$p/"
```

Step 3, first line:

```bash
repo=$(git -C "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/marketplaces/agenticseal" remote get-url origin | sed -E 's#^.*github\.com[:/]##; s#\.git$##')
```

Step 4's command and its argument at `:190` are unchanged. The skill has no other interface, and no script, hook or form changes.

## Rule changes

- nothing
  why: The policy root states no rule about where `/agentic:update` reads (G9). The work changes a shipped skill's commands, and no document of `docs/` stands on them.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The fixed `~/.claude` as the home of Claude Code's plugins, stated four times | `skills/update/SKILL.md` *Procedure*, steps 2b, 3 and 5 (`:46`, `:61`, `:81`, `:223`) | The one spelling `${CLAUDE_CONFIG_DIR:-$HOME/.claude}` that step 4 already uses (`:190`), and the sentence of *Scope* 5 that says why each command carries it |
| `os.path.expanduser` and the `os` import in step 2b's first program | `skills/update/SKILL.md` *Procedure*, step 2b (`:46`) | The shell expands the path and hands it over as `sys.argv[1]`, as step 2b's second program and step 4's program already take theirs |
| The literal comparison of step 4's argument, `assert args == USER_FILE`, and the constant `USER_FILE` | `tests/behaviour/test_the_old_block_leaves_through_update.py#test_step_4_works_on_the_config_directorys_file_and_writes_no_block` and `:31` | *Scope* 6a runs the line under a shell with the variable set, unset and empty, which shows what the literal only spelled. The rest of that case, the sentences step 4 says and the words it no longer carries, stays. The new cases are the check this work adds, and this assertion is what goes in return. |

Framed 2026-11-05 by framer, before the build.
