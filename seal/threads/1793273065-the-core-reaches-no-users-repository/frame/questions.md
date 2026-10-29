# Questions for the planner: 1793273065-the-core-reaches-no-users-repository

The judgments the issue left open that the tree, the docs or a probe
answered, so nobody reopens them. Each probe is in `frame/design.md`
*Grounding* with its command.

- **`resume`: does a resumed session still hold the hook's earlier output?**
  Yes. A resumed session answered the startup run's fact, and with no
  matcher it also received a second print (probe R). The hook's matcher is
  `startup|clear|compact`, and the harness applies it: with that matcher a
  resume ran no hook and the session held the startup output once
  (probe M).
- **`compact`: does the output return after a compaction, and what marks
  the boundary?** It returns: the hook fires with `source` `compact` and its
  output reaches the context after the boundary (probe C). The boundary is a
  `type: system` entry with `subtype: compact_boundary` and
  `compactMetadata`, followed by an `isCompactSummary` entry and the
  `SessionStart:compact` attachment. Entries the boundary lists in
  `compactMetadata.preservedMessages.uuids` stay in context word for word.
  23 interactive transcripts on this machine, Claude Code 2.1.283 to
  2.1.312, show the same sequence at every boundary.
- **Scope: every session, or only where a `seal/` root exists?** Every
  session. The session that bootstraps a fresh repository has no root when
  it starts, and the root's opt-in is the convention for gates that judge or
  write (plan B6).
- **Which copy governs in this repository, read once?** The tree's: the hook
  prints `<top>/skills/core/SKILL.md` where the session's repository is a
  clone of the running plugin, and its first line names that path (plan B2).
  `CLAUDE.md` imports nothing and tells a session to open the file only where
  no hook printed it.
- **Is there a limit on the hook's output?** Yes: past a cap between 9,990
  and 10,010 characters the context holds a preview, not the output
  (probe S). The core and its first line are near 6,900 characters, and a
  case holds the output under 10,000.
- **What does `seal core` read?** The entry's `content`, what the model
  received, compared with its `stdout` and with the file the first line
  names (plan B7). The transcript is found by `CLAUDE_CODE_SESSION_ID`
  across the project directories (plan B9).
- **The subcommand's name and place?** `seal core`,
  `skills/verify/scripts/core_check.py` (plan B10).
- **Do `install.sh`, `uninstall.sh` and `preset-setup` stay one release?**
  No; all three retire now. The template keeps its two markers for one
  release, because the update to 0.25.0 runs 0.24.x's step 4 against it
  (plan C1, C2).
- **Does `BASELINE_AGENT` still measure what it measured?** Yes. The hook's
  output reaches no subagent, so it is in neither the baseline's prefix nor
  an agent's (plan D2).
- **Q2's `@` line.** Q2 asked whether the block's import loads from the
  user-scope file. Under A5 nothing imports the core, so that question no
  longer applies; Q2 now asks the same moment's measurement for the hook.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Should the core reach a session through the preset block's one `@` line, or through a `SessionStart` hook in `hooks/hooks.json` that prints `${CLAUDE_PLUGIN_ROOT}/skills/core/SKILL.md`, retiring the block, `install.sh`, `uninstall.sh`, `preset-setup` and `update` step 4? The tree cannot answer it: both shapes satisfy the policy and the issue's constraints, and the choice retires or keeps a user-facing install path. No probe answers it: both mechanisms were shown to put a file in context (probes a and f), and what separates them is what the owner wants a user to see and control. The evidence for each is plan A1 and A5 | a person: the owner | **The block's `@` line (A1):** the core is in the memory section `/memory` lists, a user deletes the block to opt out, the block machinery stays to deliver one line, and a machine with a moved plugins root gets a warning and no core in its sessions. **A `SessionStart` hook (A5):** the core is always the installed version and needs no path or scope, the block machinery retires, every user's old block still has to be removed once by `update`, and a user sees the core only in the transcript and opts out only by disabling the plugin's hooks; the build then replaces phase 2 with the hook, the removals of the five files and their cases, and an `update` step that removes the block | A1, the issue's candidate; the build proceeds on it | answered 2026-10-30 by the owner: A5. A1, built through round 5, makes every agent read the core twice (`gaps.md` *Not done*), and a probe of a plugin `SessionStart` hook showed it reaches the session and not a subagent. The grounds, the probe and what replaces `/memory` as the place to see the core are #1177's body, *Update (owner, 2026-10-30)*. #1183 closes with this answer |
| Q2 | On a machine with 0.25.0 installed from the marketplace, does an interactive session hold the core once, and does `! seal core` pass there; and did `/agentic:update` from 0.24.2 leave an empty marker pair in `~/.claude/CLAUDE.md` with a `CLAUDE.md.bak` beside it? The tree cannot answer it: it holds the hook and the check, not a session that ran them. No probe could run here: every probe ran headless with `--plugin-dir`, a subagent cannot drive an interactive session, and this machine's installed plugin is 0.24.2, which has no core hook until the release. The measurement: after `/agentic:update` to 0.25.0 and a restart, type `! seal core`, then read the marker region of `~/.claude/CLAUDE.md` | a measurement: the owner, once, after `/agentic:update` to 0.25.0 (the issue's *Not verified until the release*) | **It passes and the pair is empty:** nothing to do; the next update takes the pair out. **`seal core` reports no core entry:** the installed hook does not reach an interactive session as the `--plugin-dir` one did, and phase 5's registration is redesigned. **It fails for another reason:** `core_check.py` misreads an interactive transcript, and its reading is fixed against that file. **The block is not an empty pair:** 0.24.2's step 4 read the template otherwise; 0.25.0's step 4 still takes out whatever stands between the markers at the next update, and no core is read twice either way | It passes, and the pair is empty: the orchestrator's probe and probe M put a plugin hook's output in a headless session's context, the 23 interactive transcripts record installed plugins' `SessionStart` entries in the shape the check reads, and 0.24.2's step 4 replaces a differing region with the template's | open |
| Q3 | Does `seal core` fail in a session started with `--bare`, as the issue's *Done when* asks? The tree cannot answer it, and no probe could run here: `--bare` authenticates only through `ANTHROPIC_API_KEY` or an `apiKeyHelper`, and `claude -p --bare` on this machine printed `Not logged in`. Under `--bare` the plugin's `bin/` may not be on the `PATH`, so the measurement runs the script by its path: `claude --bare -p --plugin-dir <clone> --allowedTools Bash "run python3 <clone>/skills/verify/scripts/core_check.py and print its output and exit code"` | a measurement: anyone with an `ANTHROPIC_API_KEY`, such as the owner, or a CI job that has one | **It exits 1 naming no core entry and `--bare`:** nothing to do. **It exits 0:** a bare session ran the hook after all, the help text notwithstanding, and the check is right to pass. **It cannot find the transcript:** a bare session writes none or writes it elsewhere, and the check's message says so already | It exits 1: `claude --help` says `--bare` skips plugin hooks, and the planted-transcript case of S5 with no core entry exits 1 | open |
