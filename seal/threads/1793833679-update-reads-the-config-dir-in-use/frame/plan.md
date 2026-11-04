# Implementation Plan: update reads the config dir in use (#1184)

## Technical context

`skills/update/SKILL.md` is a procedure a session follows. Each bash fence is a command the session runs, or a repair it prints for the user to type. Step 2b's two commands read `installed_plugins.json` (`:46`) and then the installed copy's `plugin.json` (`:47`). Its repair (`:60-62`) moves the stale copy aside and copies the marketplace clone over it. Step 3 (`:81`) takes the repository from the clone's `origin`. Step 4 (`:137-191`) already works on `"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md"`. Step 5's method for settling the reload question (`:221-225`) names the version cache in prose. `frame/design.md` G1 lists the four fixed coordinates.

The cases stand on two modules. `tests/behaviour/test_the_old_block_leaves_through_update.py` cuts step 4 out of the skill (`step_4`, `command`) and runs its program (`take_out`). `tests/behaviour/test_release_hygiene.py` pins the words of steps 2b and 3 (`frame/design.md` G8). A case that runs a bash line skips through `tests/conftest.py#shell_probe` where `bash` is no usable shell (`frame/design.md` G11).

The constraint is that no two commands of the procedure share a shell. A session runs each fence as a call of its own, and the user types the repair in a terminal of their own. So the directory is spelled at each command, and no variable carries it from one step to the next.

The failure scenario of the chosen approach, six months on, is that Claude Code moves its plugins out of the config directory, or adds a variable of its own for them. Step 2b's program then raises on `open` and prints a traceback, so the step stops loudly before the summary. Step 3's `git -C` then fails, `repo` is empty, the `curl` fails, and the step says what changed could not be read and goes on. That is how both steps behave today on a machine whose clone is missing. Nothing in the tree would notice the move ahead of a user. G3's probe is the one check of the premise, and it is not repeated by any case.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Spell `${CLAUDE_CONFIG_DIR:-$HOME/.claude}` at each command, the way step 4 already does (`frame/design.md` *Data & interfaces*) | Claude Code moves its plugins out of the config directory, and the skill reads a stale path again (*Technical context*) | Chosen. It is the spelling step 4, the deleted installer and #1177's design used (`frame/design.md` G2, G6), and `core_check.py` reads the variable with the same fallback (G4). Each command can be run under a scratch directory in CI, which is what the issue's acceptance asks. Every needle of the hygiene pins survives (G8). |
| Replace the structure: take the paths from Claude Code's own output, `claude plugin list --json` for `installPath` and `claude plugin marketplace list --json` for the clone's `installLocation` (executed, this frame: both commands print those fields on this machine) | The JSON's fields are Claude Code's, and no document this frame read says they are stable (unverified). A marketplace added from a git URL may carry no `repo` field (unverified: only a `github` source was seen). No runner of `.github/workflows/test.yml` has the `claude` CLI, so a case could only stub the command and would test the parsing, not the resolution. Step 3's pin on `marketplaces/agenticseal` would move. | Rejected. It removes the fact from the skill, which is its strength. The premise that keeps the structure, that Claude Code keeps its plugins under the config directory, was checked by running the CLI under a scratch `CLAUDE_CONFIG_DIR` (`frame/design.md` G3). While that premise holds, reading by path is as correct and can be run end to end in CI. |
| One shared resolver: a `seal` subcommand, or a helper that `core_check.py` and the skill both call | The resolver is one more mechanism to keep, for a fact the shell states in one expansion. `core_check.py` is #1190's file in this release (`frame/design.md` G10), so sharing it now puts two work items on one file. | Rejected. A fact with one source is met by one spelling at each site, and the spelling has no logic to drift. |
| Set the directory once in step 1, `config="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"`, and use `$config` after | Each step runs in a fresh shell (*Technical context*). Step 2b then reads `"$config"` as empty and opens `/plugins/installed_plugins.json`, and the repair the user types has no `$config` at all. | Rejected. |
| Write the changelog fragment and the version move as a phase of their own, once the review rounds settle | `.claude-plugin/plugin.json` lies outside the work item's records, so a commit to it after the last round's `target:` commit needs one more verifying round (`skills/core/SKILL.md` *Judgment is not licence to skip a party*, the row "No fix that no round reads"; `skills/code-review/orchestration.md:208-217`) | Rejected, at the orchestrator's reading of the frame. Phase 1's last commit carries both, so round 1 reads them. |
| Leave step 5's prose at `:223`, because no command runs it | The method sends a reader under `CLAUDE_CONFIG_DIR` to plant the sentinel in a directory that is not loaded, and the measurement reads `ABSENT` for the wrong reason. *Scope* 6d's search would also need an exception. | Rejected. The skill is a closed set of four coordinates (contract rule 12), so all four are fixed. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* 1, 2, 3, 4, 5 and 6, test-first. The phase's last commit adds the work item's `changelog.md` fragment, one entry under `### Fixed`, and moves `.claude-plugin/plugin.json`'s `version` from 0.32.1 to 0.32.2. This work item carries the release's version move, and #1190 and #1185 leave the version alone (`skills/implement/orchestration.md` *Which branch the pull request lands on is decided with the routing question*). Round 1 reads both. A fix pass that changes what the work ships updates the fragment in the same range (`docs/layout/the-record-layout.md` *A commit after the build brings its changelog fragment along*). | S1, S3, S4 and S5 as the new cases of *Scope* 6, each seen red against the skill at 5ce47e0d, with how in the phase record. S2 as a case that is green before and after, since `:190` already spells the directory. S6 through the two update cases of `tests/behaviour/test_release_hygiene.py`, unchanged. The narrow run of `tests/behaviour/test_the_old_block_leaves_through_update.py`, the new module and those two cases. `.claude-plugin/plugin.json` parses as JSON and its `version` reads `0.32.2`. `git diff --name-only` against the base lists `skills/update/SKILL.md`, the two test modules, `.claude-plugin/plugin.json` and the work item's records only. The suite stays `unverified` until the orchestrator's broad run. | |

## Operational impact

None for a deployer. `CLAUDE_CONFIG_DIR` is Claude Code's variable, not a new one. Where it is unset, every command reads the path it reads today. Where it is set, `/agentic:update` reads the installed copy, the marketplace clone and the `CLAUDE.md` that Claude Code is using. No dependency is added and nothing is migrated.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
