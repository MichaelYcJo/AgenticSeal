---
name: preset-setup
description: Merge the AgenticSeal CLAUDE.md block into the user's CLAUDE.md with semantic dedup. Propose, get approval, then apply.
disable-model-invocation: true
---

# /agentic:preset-setup, a reviewed CLAUDE.md merge

The user runs this command, and the session running it merges the preset's
CLAUDE.md block into the user's global `~/.claude/CLAUDE.md`, or into the
target the user names. `install.sh` only inserts the marker block; this
command also removes what the block duplicates, and every deletion goes
through the user first.

## Procedure

0. **Ask the scope first**, unless the user already said: global
   (`~/.claude/CLAUDE.md`, every project on this machine) or this project
   (`./CLAUDE.md`, committed, so teammates receive it through git). Recommend
   project scope for team repositories and global for a personal machine.
   Warn where the preset block already exists in the *other* scope: both
   files load, so the block lives in exactly one.

1. **Back up.** Copy the target file to `CLAUDE.md.bak` before touching
   anything. Where the target does not exist, write the preset block and stop.

2. **Read both.** The preset block is the content between
   `<!-- agentic:start -->` and `<!-- agentic:end -->` in this plugin's
   `templates/claude-md-block.md` (`$CLAUDE_PLUGIN_ROOT/templates/claude-md-block.md`),
   the block's one source. Read the user's file in full.

3. **Classify each overlap** between the user's existing content (outside any
   preset markers) and the preset block:

   | Finding | Proposal |
   |---|---|
   | Exact duplicate: same rule, same meaning | Propose removing the user's copy (the block now owns it) |
   | Partial overlap: the user's rule is more specific | Propose **keeping the user's rule** and note it overrides the block's general form |
   | Conflict: different values for the same concern (for example the response language) | Ask which side wins. Never decide silently |

4. **Present the result as a diff**: the full proposed file, with each change
   annotated by its classification above. Apply nothing yet.

5. **Apply only after approval.** Where the user amends the proposal, present
   the diff again. After applying, confirm the marker block is intact and
   nothing outside it changed except approved deletions.

## Rules

- Never delete or rewrite user content without an approved diff line covering it.
- Never modify anything when the user rejects the proposal: the `.bak` and the
  untouched original both survive.
- Where the user's file already has a preset marker block from an older
  version, its contents are preset-owned: replace it without asking, and diff
  only the user-owned remainder. A block between `<!-- specseal:start -->`
  and `<!-- specseal:end -->` is such a block (`skills/update/SKILL.md`
  step 4 names those markers), and the block under the new markers takes its
  place.
