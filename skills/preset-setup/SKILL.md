---
name: preset-setup
description: Write or replace the AgenticSeal preset block, the one `@` line that imports the core, in the user's CLAUDE.md from inside Claude Code. Backs up first and touches nothing outside the markers.
disable-model-invocation: true
---

# /agentic:preset-setup, the CLAUDE.md block from inside Claude Code

The user runs this command, and the session running it writes the preset
block into the user's `CLAUDE.md`: `$CLAUDE_CONFIG_DIR/CLAUDE.md` where that
variable is set, `~/.claude/CLAUDE.md` otherwise, or the target the user
names. It does what `install.sh` does, for a user who has no clone to run
the script from. The block is one `@` line that imports the core,
`skills/core/SKILL.md`, from the plugin's marketplace clone, by a path
relative to the file that holds it. It holds no rule, so nothing in the
user's own text can overlap it, and there is nothing to classify or approve.

## Procedure

1. **Back up.** Copy the target file to `CLAUDE.md.bak` before touching
   anything. Where the target does not exist, write the preset block into a
   new file and go to step 3.

2. **Write the block.** The preset block is the content between
   `<!-- agentic:start -->` and `<!-- agentic:end -->` in this plugin's
   `templates/setup/claude-md-block.md` (`$CLAUDE_PLUGIN_ROOT/templates/setup/claude-md-block.md`),
   the block's one source, markers included. Where the target holds a block
   under those markers, replace that region with it. Where it holds one
   under the older markers `skills/update/SKILL.md` step 4 names,
   `<!-- specseal:start -->` and `<!-- specseal:end -->`, put the block in
   that region's place. Where it holds neither, append the block
   after a blank line. A start marker with no end marker is a damaged block:
   stop and say so rather than guess where it ends.

3. **Confirm.** Read the file back: one block stands, between the new
   markers, and every line outside it is the line the `.bak` holds. Then
   check that the file the block's `@` line names, read relative to the
   target's directory, is a file. Where it is not, say so with that path: an
   import of a missing file loads nothing and says nothing, so no session
   reads the core until the plugin's marketplace clone holds it there.

## Rules

- Never delete or rewrite a line outside the markers.
- Where the user's file already has a preset marker block from an older
  version, its contents are preset-owned: replace it without asking.
