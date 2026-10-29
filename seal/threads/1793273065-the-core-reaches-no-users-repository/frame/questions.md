# Questions for the planner: 1793273065-the-core-reaches-no-users-repository

The judgments the issue left open that the tree, the docs or a probe
answered, so nobody reopens them:

- **Is a file read once when two `CLAUDE.md` files import it by one path?**
  Yes, for two memory files inside the working directory (`CLAUDE.md` and
  `CLAUDE.local.md`, probe c in `frame/design.md` *Grounding*, run twice).
  The design never imports the core twice, so a different answer would not
  change the build.
- **Does an `@` import follow a symlink and a `~` path?** A symlink, yes
  (probe b, inside the project). A `~` path is the docs' own example and
  could not be executed from a user-scope file here. The block uses a path
  relative to the file that holds it and needs neither.
- **Which shape for the link?** A relative path from the user-scope file
  (plan A1), over `~` (A2) and the per-machine symlink (A3); the grounds are
  the plan's rows.
- **Which copy governs in this repository?** The tree's, where the branch
  changes `skills/core/SKILL.md`; `CLAUDE.md` says so and imports nothing.
- **Does the project-scope install stay?** No: from a project-level file the
  import is external, gated by an interactive approval and never loaded
  headless (probe d, docs).
- **The skill's name?** `core`, the word the issue, milestone 69 and
  `routing.md` use.
- **Where each block rule lands?** `frame/design.md` *Removes* row 1 names
  the home of each of the eight.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Should the core reach a session through the preset block's one `@` line, or through a `SessionStart` hook in `hooks/hooks.json` that prints `${CLAUDE_PLUGIN_ROOT}/skills/core/SKILL.md`, retiring the block, `install.sh`, `uninstall.sh`, `preset-setup` and `update` step 4? The tree cannot answer it: both shapes satisfy the policy and the issue's constraints, and the choice retires or keeps a user-facing install path. No probe answers it: both mechanisms were shown to put a file in context (probes a and f), and what separates them is what the owner wants a user to see and control. The evidence for each is plan A1 and A5 | a person: the owner | **The block's `@` line (A1):** the core is in the memory section `/memory` lists, a user deletes the block to opt out, the block machinery stays to deliver one line, and a machine with a moved plugins root gets a warning and no core in its sessions. **A `SessionStart` hook (A5):** the core is always the installed version and needs no path or scope, the block machinery retires, every user's old block still has to be removed once by `update`, and a user sees the core only in the transcript and opts out only by disabling the plugin's hooks; the build then replaces phase 2 with the hook, the removals of the five files and their cases, and an `update` step that removes the block | A1, the issue's candidate; the build proceeds on it | open |
| Q2 | Does the one-line block, installed in `~/.claude/CLAUDE.md` on a machine with the 0.25.0 plugin, put `skills/core/SKILL.md` in the context of an interactive session and of a headless one, with no approval dialog? The tree cannot answer it, and no probe could run here: the only user-scope memory file on this machine is the owner's, and a scratch `CLAUDE_CONFIG_DIR` has no login (`Not logged in`). The measurement: after `/agentic:update` to 0.25.0, `/memory` in an interactive session lists the import under `~/.claude/CLAUDE.md`; headless, `claude -p --tools "" "Without using any tool, list each CLAUDE.md or imported file your context shows, by path"` names it | a measurement: the first session on an installed machine after the release; the orchestrator can run it on this machine once the owner's block is the 0.25.0 one | **It loads:** nothing to do. **It does not load:** the block cannot carry the link from the user-scope file either, and the `SessionStart` hook of Q1 becomes the only shape that reaches a session; that is a redesign of phase 2 as Q1's second option describes | It loads, on the docs' two sentences (read): relative paths resolve against the importing file, and user-scope imports load without the dialog | open |
