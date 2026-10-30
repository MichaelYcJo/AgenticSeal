# Implementation Plan: 1793273065-the-core-reaches-no-users-repository

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phase 1.
Approved 2026-10-30 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phase 5.

## Summary

The core moves from `CLAUDE.md` into `skills/core/SKILL.md`, and every agent
definition preloads it before `agent-contract` (phase 1, built). A session
receives it from a plugin `SessionStart` hook that prints the file under a
first line naming the file, the plugin's version and its SHA-256, on
`startup`, `clear` and `compact` and never on `resume`; in this repository
the hook prints the tree's copy. `seal core` reads that entry back from the
session's transcript and fails unless the context holds the core once and
whole. The preset block's `@` line, `install.sh`, `uninstall.sh` and
`/agentic:preset-setup` retire; the template keeps its two markers for one
release so that 0.24.x's update empties an installed block, and 0.25.0's
update step takes the markers out. `seal payload` gains a session table that
counts the hook's output. Phases 1 to 4 built A1 and closed; phases 5 to 10
deliver A5 and the core's refactor, which the owner chose on 2026-10-30 (`questions.md` Q1).

## Technical context

- `hooks/hooks.json:70-79` registers one `SessionStart` entry with no
  matcher, running `dispatch.py session-start`;
  `hooks/dispatch.py#GROUPS` gives that group `version-check.py`,
  `root-migrate.py` and `stub-remove.py`. `hooks/dispatch.py#merge` keeps the
  first JSON object a group prints and drops its gates' plain text, and
  `version-check.py` prints JSON when a release is behind.
- `hooks/lib/hooksession.py#SESSION_VARIABLE` is `CLAUDE_CODE_SESSION_ID`;
  `skills/implement/scripts/seal.py#TOOLS` maps a subcommand to a script and
  `#HOOK_PURPOSES` names each `hooks/lib/` module it needs.
  `skills/verify/scripts/session_cost.py#newest` finds a transcript by the
  working directory's slug and mtime, which is not one session's;
  `#subagent_transcripts` finds a session's subagents beside it.
- `skills/verify/scripts/payload_meter.py#composition` (lines 340-384) lists
  one agent's rows and the `CLAUDE.md` pair with `imports_of`'s rows;
  `#calibration_of` reads only subagent transcripts; `BASELINE_AGENT`
  (line 93) is `general-purpose`.
- `templates/setup/claude-md-block.md` holds the A1 line; `install.sh`,
  `uninstall.sh`, `skills/preset-setup/SKILL.md` and
  `skills/update/SKILL.md` step 4 write, remove or compare it, and
  `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py`
  holds them.
- `skills/core/SKILL.md` is 6,705 characters (executed, *Grounding*); the
  harness keeps a hook's output whole up to a cap between 9,990 and 10,010
  characters (probe S).
- The chosen approach's failure in six months: a Claude Code release that
  renames the transcript's `compact_boundary` entry, its
  `preservedMessages` field or the attachment's `content` field makes
  `seal core` report no core in a session that holds one. It fails toward
  a red line and an extra read of the file, never toward a silent pass, and
  its cases name the shape it reads. A core grown past the cap is held by
  a case in CI before it ships.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 The block holds one `@` line, relative to the file that holds it, importing the marketplace clone's core | The harness adds the user's `CLAUDE.md` to every spawn, so every agent read the core twice, about 2,100 tokens a spawn (`gaps.md` *Not done*, phase 3's record); a plugins root elsewhere loads nothing without a word | **Rejected 2026-10-30 by the owner** (Q1), after round 5. The issue's update holds the grounds |
| A2 The same line as `@~/.claude/plugins/…` | `~` does not follow `CLAUDE_CONFIG_DIR`, and it double-reads as A1 does | Rejected with A1 |
| A3 A per-machine symlink `~/.claude/agentic-core.md` imported by the block | Every project on the development machine reads an unreleased core; `ln -s` under Git Bash writes a copy; it double-reads as A1 does | Rejected with A1 |
| A4 This repository's `CLAUDE.md` imports `@skills/core/SKILL.md` | A session here reads the hook's copy and this one: twice | Rejected |
| A5 A plugin `SessionStart` hook prints `skills/core/SKILL.md`; the block and its machinery retire | `/memory` does not list the core, and a user turns it off only by disabling the plugin's hooks; `--bare` skips it; a transcript format change breaks the check toward red | **Chosen** by the owner (Q1). The README says what is given up; the first line and `seal core` stand in for `/memory` |
| A6 Keep the block's rules and add the link beside them | Every rule has a second source | Rejected |
| A7 Fold the core into `agent-contract` | The contract binds agents to acts a session must not take (rule 6), and the core would have two sides | Rejected |
| B1 How the tree's core governs here: a sentence in `CLAUDE.md` telling a session to open the tree's copy where the branch changes it (the A1 design) | A session that follows it reads the core twice, the hook's and the tree's; one that does not judges by the installed copy. Whether it follows depends on the model, which is the ground the issue's update gives against a memory line | Rejected |
| B2 How the tree's core governs here: the hook prints `<top>/skills/core/SKILL.md` where the session's repository is a clone of the running plugin, read from `.claude-plugin/plugin.json`'s `name` | A clone of a fork named `agentic` prints its own core, which is the core a person developing that fork means. A branch switched mid-session leaves the context's core stale; `seal core` then fails on the digest and says so | **Chosen**: one mechanism, one read, and the first line names which file it was |
| B3 The installed core always governs, here too | A session working on a branch that changes the core judges by the last release's, which the issue's constraint *In this repository the tree's core governs* refuses | Rejected |
| B4 The hook answers every `source`, or the gate filters `source` itself | Probe R: a resumed session keeps the start's output, so a `resume` print is a second copy. A filter inside the gate still starts an interpreter on every resume and states in code what the harness's matcher states in `hooks.json` | Rejected for the matcher `startup\|clear\|compact`, which probe M shows the harness applies |
| B5 The core as a fourth gate of the existing `session-start` group | `dispatch.py#merge` drops plain text beside a neighbour's JSON, so on a day `version-check` speaks the core is not printed; and the group has no matcher, so it runs on `resume` | Rejected for a group of its own. Replacing the dispatcher for this one hook was weighed too: a separate script would lose the dispatcher's UTF-8 streams, which a core with an em dash needs on a cp949 console, and its failure record |
| B6 Print the core only where a `seal/` root exists, and nothing or a pointer elsewhere | The session that bootstraps a fresh repository has no root when it starts, and it frames and routes that repository's first work item without the core; the root's opt-in is the convention for gates that judge or write, and the core does neither | Rejected; every session, the issue's default |
| B7 `seal core` hashes the entry's `stdout` | Past the cap `stdout` holds the whole output while `content`, what the model received, is a preview (probe S), so a check over `stdout` passes a session that never read the core | Rejected for `content`, compared with `stdout` |
| B8 `seal core` reads only entries after the last boundary | An entry a compaction preserves stays in context (probe C), so a core printed just before a boundary and again after it would read as once | Rejected; the boundary's `preservedMessages.uuids` count too |
| B9 `seal core` finds the transcript by the working directory's slug, as `session_cost.py#newest` does | A session started in one directory and working in a worktree has its transcript under the first directory's slug, and the newest file under a slug may be another session's | Rejected for `CLAUDE_CODE_SESSION_ID` and a glob over the project directories |
| B10 `seal core` in `skills/core/scripts/` beside the file it checks, or in `hooks/lib/` | The core skill is text every agent preloads, and a script beside it is one more path in its directory nothing loads; `hooks/lib/` holds what hooks import, not commands | Rejected for `skills/verify/scripts/core_check.py`, beside the other transcript readers |
| C1 Keep `install.sh`, `uninstall.sh` and `preset-setup` one more release to take old blocks out | `install.sh` and `preset-setup` write a block, and there is nothing left to write. `uninstall.sh` would be a second remover beside update step 4, two sources of one act; the premise that a user needs it, one who uninstalls the plugin without updating, is met by one README sentence: delete the lines between the markers | Rejected; all three retire now |
| C2 Delete `templates/setup/claude-md-block.md` now | The update to 0.25.0 runs 0.24.x's step 4 (update steps 1 and 5 say a session keeps its version), which diffs the clone's template; a missing file leaves that step to guess, and a template holding the A1 line would install a second read | Rejected; the template holds the two markers for one release, so 0.24.x's step empties the block, and 0.25.0's step 4 removes the markers at the next update. #1154 settles when the template goes |
| C3 The core hook warns when `~/.claude/CLAUDE.md` still holds a block | A per-session line for a file only `/agentic:update` may edit, said in every session of every repository until the user acts | Rejected; the update step and the release note say it once |
| D1 Drop `imports_of` from the meter, since the core no longer arrives by import | Any user's `CLAUDE.md` may import a file, and the harness adds the pair to every spawn; without it the pair's bytes are short by whatever a user imports | Rejected; the import rows stay, and the session table is added |
| D2 Change `BASELINE_AGENT` | The baseline exists to subtract what every spawn carries that is not the agent's own: the system prompt, tool schemas and the pair. The hook's output reaches no subagent (the orchestrator's probe), so it is in neither prefix and the subtraction is unchanged | Rejected; the docstring states the premise |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `skills/core/SKILL.md` holds the core with the one added sentence; `CLAUDE.md` holds *The core* and nothing else; every `agents/*.md` lists `core` then `agent-contract` and opens with the new sentence; `CONTRIBUTING.md:368`, `:381`, `:473`, `tests/text/test_a_rider_reaches_its_file.py:66` and `tests/behaviour/test_chain_hooks_hardening.py:773` name the core's path; `.github/scripts/release_report.py#DOCUMENTS` gains the core; the tests that read `CLAUDE.md` for the core read `skills/core/SKILL.md` | `tests/text/test_every_agent_reads_the_contract.py`, `tests/text/test_the_rules_claude_md_names_have_one_home.py`, `tests/text/test_a_language_section_of_writing_style_opens_alone.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py#test_this_repository_carries_no_copy_of_the_block`, `tests/github/test_release_report.py`, `tests/behaviour/test_docs_line_wrap.py`; `bin/seal payload` lists the core for every agent | 5a283bd8 |
| 2 | The block is the markers and the `@` line; each rule it held stands in its home: the tooling and lint sentences in `skills/implement/SKILL.md` step 2, the worktree sentence in `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, `skills/verify/orchestration.md:146` citing the crafter's rule; `install.sh` loses `--project`, the prompt and the overlap loop and gains the exists warning; `preset-setup` and `update` step 4 rewritten for the line; the README rows; `hooks/mode-gate.py`, `skills/verify/scripts/broad_gate.py` and `skills/implement/orchestration.md:458` reworded; the block-pinning cases replaced by cases that read the homes and the core's routing sentence; S7's two installer cases. Phase 7 undoes the line, the installer, `preset-setup` and update step 4; the rules' homes stand | `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py`, `tests/behaviour/test_first_setup_asks_once.py`, `tests/behaviour/test_waiver_decided_at_start.py`, `tests/text/test_review_axes.py`, `tests/text/test_broad_gate_rule.py`, `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`; `bash install.sh <scratch target>` by hand, read for the warning | d58605ee |
| 3 | `payload_meter.py#composition` follows `@` lines; the before and after totals measured against a scratch home, written into this phase's record with the two commands. `imports_of` stands under A5 (D1); phase 9 adds the session table | `tests/skills/test_payload_meter.py`, with new cases for an `@` line in each file of the pair, a `~` path, a relative path, a symlink, a missing target, one real path imported twice, and the fourth hop | a7329570 |
| 4 | `changelog.md` with the `### Fixed` entry and the `### Process changes` row; `.claude-plugin/plugin.json` at `0.25.0` in the same commit. Phase 10 rewrites the fragment; the version stands | `tests/github/test_publish_release_note.py` for the fragment's shape; `tests/behaviour/test_release_hygiene.py`; the commit shows both files | 0c1144ef |
| 5 | The hook, as `frame/design.md` *Scope* item 2 states: `hooks/lib/core.py` (`origin`, `header`, `output`, `parse`, `CAP`), `hooks/core-start.py`, `dispatch.py#GROUPS["session-core"]`, the `hooks.json` entry with the matcher `startup\|clear\|compact`, and the `core-start` row of the gate table in `README.md` and `README.ko.md`. In the same commit, what stood on "a session receives the core through the block": the core's `description:`, `CLAUDE.md` as *Scope* item 5 states, and `skills/implement/orchestration.md:460` | New `tests/hooks/test_core.py` (S3, S4, S7) and `tests/hooks/test_core_start.py` (S2), each case seen red against the tree without the code; `tests/hooks/test_dispatch.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_the_rules_claude_md_names_have_one_home.py`, `tests/text/test_every_agent_reads_the_contract.py`, `tests/behaviour/test_docs_line_wrap.py`, and every module that reads `hooks/hooks.json`, `README.md` or `CLAUDE.md`, found by `git grep -l` on those names under `tests/`; by hand, a `startup` payload piped to `python3 hooks/dispatch.py session-core` with `CLAUDE_PLUGIN_ROOT` set to a scratch copy, once with `cwd` in this clone and once outside it, each output's first line read | 36b6b2b6 |
| 6 | `seal core`, as *Scope* item 3 states: `skills/verify/scripts/core_check.py`, `seal.py#TOOLS["core"]` and `#HOOK_PURPOSES["core.py"]`, the cheat-sheet row in `README.md` and `README.ko.md` with a sentence on seeing the core (`! seal core`) in place of `/memory`, and the sentence in `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* step 1 | New `tests/skills/test_core_check.py` over planted transcripts, every case of S5, each seen red first; `tests/skills/test_seal.py` and every module that reads `seal.py#TOOLS`, `#HOOK_PURPOSES` or the cheat sheet, found by `git grep -l`; by hand, `python3 skills/verify/scripts/core_check.py` in the crafter's own Bash, which reads the orchestrating session's transcript, started on 0.24.2 with no core hook, and must exit 1 naming no core entry | 84cf2dd3 |
| 7 | The block's machinery retires, as *Scope* item 4 and *Removes* state: `install.sh`, `uninstall.sh` and `skills/preset-setup/` deleted; the template at its two markers; update step 4 rewritten to take the block out; the README's install, rename, update and cheat-sheet text in both editions; `.gitignore:14`; `tests/censuses.py:1014-1015`; the installer test module replaced by `tests/behaviour/test_the_old_block_leaves_through_update.py` (S6); every case and docstring *Removes* names | `tests/behaviour/test_the_old_block_leaves_through_update.py`, its cases seen red against the tree before the edit; `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_the_release_check_watches_what_ships.py`, `tests/behaviour/test_no_document_names_the_old_roots.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_a_language_section_of_writing_style_opens_alone.py`, `tests/text/test_the_rules_claude_md_names_have_one_home.py`, `tests/behaviour/test_first_setup_asks_once.py`, `tests/text/test_review_axes.py`, `tests/text/test_broad_gate_rule.py`, `tests/test_censuses.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_docs_line_wrap.py`; `git grep -n` on "preset-setup", "install.sh", "uninstall.sh" and "`@` line", outside `seal/`, printed in the phase record with each remaining hit's reason | 56861925 |
| 8 | The core's prose, as `frame/design.md` *Scope* items 9 to 12 state: `skills/core/SKILL.md` without its repeated sentences and its `#1167` pointer, every directive, citation, invariant and reason sentence kept, the `##` headings and phase 5's `description:` unchanged (item 9); the sentences on where the core applies, whose paths it cites and whose owner it names, and the `CONTRIBUTING.md` sentence moved to `CLAUDE.md` (item 10); one sentence kept where two asked for one thing, and each two-way sentence item 11 lists rewritten (item 11); `hooks/lib/core.py#output` printing the body below the frontmatter and `core_check.py` comparing against that body (item 12); then the four agents' behaviour suites run on both sides and compared | S11: `evals/scripts/noninferiority.py run --agent <agent> --rev 6ebfada5`, the commit before the phase's first, and the same at the phase's last commit for `framer`, `crafter`, `proofer` and `sealer`, then `compare --phase 8`, each record under `seal/threads/1793273065-the-core-reaches-no-users-repository/evals/` and each passing; S12 for the proofer; item 12 test-first in `tests/hooks/test_core.py` and `tests/skills/test_core_check.py`, each new case seen red; phase 5's and phase 6's verified-by sets, every module that cites a bold sentence of the core (`tests/behaviour/test_a_cited_section_stands_in_its_file.py` among them), and S7 green | 72c1a3ee |
| 9 | The meter's session table, as *Scope* item 6 states, and the `BASELINE_AGENT` premise in the module docstring; the README's `seal payload` row in both editions; the before and after numbers from two runs against a scratch home, base `53f21b54` with the 0.24.2 block and HEAD with none, written into this phase's record with both commands | `tests/skills/test_payload_meter.py`, new cases seen red first: the session table carries the hook row at `output`'s bytes, the JSON's `session` object, no agent table carries a hook row | dd6f930a |
| 10 | `changelog.md` rewritten as *Scope* item 7 states; `gaps.md` *Not done* without the double read and with `questions.md` Q2 and Q3 under *Not verified*; the pull request body closes #1183 beside #1177 | `tests/github/test_publish_release_note.py`, `tests/behaviour/test_release_hygiene.py`; the fragment read against S10 | 3f458f83 |

## Operational impact

- A user's sessions receive the core from the plugin's hook from the first
  session on 0.25.0, whether or not they ever ran an installer. Every
  session pays the core's tokens once, about 2,100, and its cache.
- `/agentic:update` from 0.24.x runs 0.24.x's step 4 against the 0.25.0
  template and leaves an empty marker pair in `~/.claude/CLAUDE.md`, with
  `CLAUDE.md.bak` beside it. The next update, run by 0.25.0's step 4, takes
  the pair out. A user who updates only with `claude plugin update` keeps
  the 0.24.x block, eight rules that now stand a second time in the skills,
  and no core twice.
- `bash install.sh`, `bash uninstall.sh` and `/agentic:preset-setup` stop
  existing. A repository that committed a block under 0.24.x's `--project`
  keeps it until somebody deletes the lines between the markers; update
  step 4 names that file.
- `/memory` does not list the core. `! seal core` prints which core loaded;
  disabling the plugin's hooks turns it off.
- New cases need prices: the orchestrator refreshes `.test_durations` from
  the branch's CI `durations` artifact after the phases close, as round 5
  did (`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`
  prints the recipe).
- The review rounds, the broad gate and the seal run again over the
  redesign: `trail/gate.md` and `guarantee.md` name commits before it.
- No new dependency and no environment variable. `seal core` reads
  `CLAUDE_CODE_SESSION_ID` and `CLAUDE_CONFIG_DIR`, both the harness's.
