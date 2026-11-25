# Mechanisms a plugin can ship, beside instruction text

Read by a claude-code-guide agent from the official Claude Code docs on 2026-11-25
(code.claude.com/docs/en/hooks.md, sub-agents.md, plugins/components.md,
plugins/manifest-reference.md, plugins/loading.md). The settings, agent-view,
output-style and status-line pages were not read in full. Each line is the
agent's reading of the docs, a claim, not a probe of this harness: anything a
design rests on is probed before it is relied on.

## Hooks (plugin `hooks/hooks.json`; fire from session load, not gated by a skill)

- Events include SessionStart, UserPromptSubmit, PreToolUse, PermissionRequest,
  PostToolUse, PostToolUseFailure, PostToolBatch, SubagentStart, SubagentStop,
  TaskCreated, TaskCompleted, Stop, PreCompact, PostCompact, FileChanged,
  WorktreeCreate/Remove, SessionEnd and others (33 in the docs' table).
- `additionalContext` reaches the model as a system reminder for SessionStart,
  UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PostToolBatch,
  SubagentStart, SubagentStop, Stop. For Pre/PostToolUse it appears next to the
  tool result. Over 10,000 chars it goes to a file with a 2,000-char preview.
- Blocking (exit 2 or a decision): PreToolUse blocks the call (stderr to the
  model as the tool error; `permissionDecision` deny/ask/allow/defer,
  `permissionDecisionReason`, `updatedInput`); Stop and SubagentStop keep the
  session or the subagent working; PostToolBatch stops the loop; TaskCreated,
  TaskCompleted, PreCompact, UserPromptSubmit. PostToolUse cannot undo the tool;
  `decision: "block"` adds a reason beside the result.
- Matchers: tool name (`Write|Edit`), and an `if` field in permission-rule
  syntax filters by arguments, e.g. a path glob. Edit input carries
  `file_path`, `old_string`, `new_string`, `replace_all`; Write carries
  `file_path`, `content`; PostToolUse adds `tool_response`.
- Common input fields: `agent_type` (the agent's name, inside a subagent or
  under `--agent`) and `agent_id`. SubagentStart/SubagentStop match by agent
  name. Unconfirmed: that a plugin's `hooks/hooks.json` hook fires inside a
  subagent with these fields set; probe before relying on it.

## Hook types

- `command` (stdin JSON, default timeout 600 s), `http`, `mcp_tool`.
- `prompt`: a single-turn LLM evaluation of the hook input (`$ARGUMENTS`),
  returning `{ok: true}` or `{ok: false, reason}`; optional `model`; default
  timeout 30 s. The default model is "the model Claude Code uses for background
  functionality", unnamed. `continueOnBlock: true` feeds the reason back as a
  tool error or a continuation instead of ending the turn.
- `agent` (experimental): a subagent with Read, Grep and Glob, up to 50 turns,
  the same `{ok, reason}` reply, default timeout 60 s.
- Up to 12 prompt/agent hooks run concurrently. Whether a prompt hook reads the
  transcript at `transcript_path` is unconfirmed.

## Agent definitions shipped in a plugin

- Honoured: name, description, model, effort, maxTurns, autoCompactWindow,
  tools, disallowedTools, skills, memory, background, omitClaudeMd,
  isolation (`worktree` only), color, experimental.cacheTtl.
- Ignored for plugin agents: `hooks`, `mcpServers`, `permissionMode`,
  `initialPrompt` ("For security reasons, plugin subagents don't support the
  hooks, mcpServers, or permissionMode frontmatter fields", sub-agents.md).
  A per-agent hook is a plugin-level hook that reads `agent_type`.

## Other plugin components

- Skills, commands, agents, hooks, `.mcp.json` MCP servers, `.lsp.json`,
  output styles, themes, `monitors/monitors.json` (background commands started
  at session start or on a named skill's first run; stdout reaches Claude as
  notifications; not under `-p`; not for repository-scope plugins),
  `workflows/*.js` (scripts that orchestrate subagents), `bin/` on the Bash
  tool's PATH, `userConfig`.
- A `CLAUDE.md` at the plugin root is not loaded. Whether a plugin can ship
  `settings.json` keys such as `statusLine` or `agent` is unconfirmed.

## What this repository already ships

`hooks/hooks.json`: SessionStart (`hooks/core-start.py`), Stop, PreToolUse on
AskUserQuestion (`hooks/ask-under-automation.py`, 0.38.8). `bin/seal`, `bin/test`.
The plugin-directory listing has been on hold since 2026-11-08 (milestone 93), so
its file limits do not bind a design.
