#!/usr/bin/env bash
set -euo pipefail

# AgenticSeal installer — the CLAUDE.md marker block, and nothing else.
#
# Skills / agents / hooks / commands are distributed as a Claude Code plugin
# (see README: /plugin install), and every agent receives the core,
# skills/core/SKILL.md, through its definition. A plugin hook could print the
# core into a session too; the block is the harness's own memory mechanism
# instead, which the user sees in /memory and can delete. It is one `@` line
# importing the core from the plugin's marketplace clone, by a path relative
# to the CLAUDE.md that holds it, so this script manages exactly that block:
#
#   1. Back up the existing CLAUDE.md to CLAUDE.md.bak
#   2. Insert or update the <!-- agentic:start/end --> block
#   3. NEVER touch content outside the markers
#   4. Warn when the file the block imports is not there: a dangling import
#      loads nothing and says nothing
#
# Usage: bash install.sh                      → ${CLAUDE_CONFIG_DIR:-~/.claude}/CLAUDE.md
#        bash install.sh <target-CLAUDE.md>   → explicit path
# There is no project scope: from a project's CLAUDE.md the import resolves
# outside the working directory, which an approval dialog gates and a
# headless session never loads.

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$REPO_DIR/templates/setup/claude-md-block.md"
START='<!-- agentic:start -->'
END='<!-- agentic:end -->'
# The markers every release before the rename to AgenticSeal wrote. A
# CLAUDE.md holding a block between them gets the block above in its place,
# once; the minor release after the rename removes this.
OLD_START='<!-- specseal:start -->'
OLD_END='<!-- specseal:end -->'

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'
info()  { echo -e "${GREEN}[info]${NC} $1"; }
warn()  { echo -e "${YELLOW}[warn]${NC} $1"; }
error() { echo -e "${RED}[error]${NC} $1"; exit 1; }

case "${1:-}" in
    -*) error "Unknown option $1. Usage: bash install.sh [<target-CLAUDE.md>]" ;;
esac
TARGET="${1:-${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md}"

[ -f "$SOURCE" ] || error "Run this script from the AgenticSeal directory (templates/setup/claude-md-block.md not found)."
grep -qF "$START" "$SOURCE" || error "templates/setup/claude-md-block.md has no preset markers."

# Extract the managed block (markers included) from the repo file.
BLOCK="$(awk -v s="$START" -v e="$END" '
  index($0, s) { in_block = 1 }
  in_block     { print }
  index($0, e) { exit }
' "$SOURCE")"

mkdir -p "$(dirname "$TARGET")"

if [ ! -f "$TARGET" ]; then
    printf '%s\n' "$BLOCK" > "$TARGET"
    info "Created $TARGET with the preset block."
else
    cp "$TARGET" "$TARGET.bak"
    info "Backed up existing file to $TARGET.bak"

    # The markers the target's block stands between: this release's, else the
    # ones a release before the rename wrote, else none.
    FOUND_START=""; FOUND_END=""
    if grep -qF "$START" "$TARGET"; then
        FOUND_START="$START"; FOUND_END="$END"
    elif grep -qF "$OLD_START" "$TARGET"; then
        FOUND_START="$OLD_START"; FOUND_END="$OLD_END"
    fi

    if [ -n "$FOUND_START" ]; then
        # A start marker without its end marker means the block is damaged;
        # the update below would silently drop everything after START.
        grep -qF "$FOUND_END" "$TARGET" || error \
            "Found the start marker but no end marker in $TARGET — refusing to edit. Repair the block (or delete it) and rerun."
        # Replace everything between the markers (inclusive) with the new block.
        # BSD awk rejects multi-line -v strings, so assemble in three parts.
        awk -v s="$FOUND_START" 'index($0, s) { exit } { print }' "$TARGET.bak" > "$TARGET"
        printf '%s\n' "$BLOCK" >> "$TARGET"
        awk -v e="$FOUND_END" 'after { print } index($0, e) { after = 1 }' "$TARGET.bak" >> "$TARGET"
        if [ "$FOUND_START" = "$OLD_START" ]; then
            info "Replaced the block a release before the rename to AgenticSeal wrote with the preset block in $TARGET"
        else
            info "Updated the preset block in $TARGET"
        fi
    else
        { cat "$TARGET.bak"; echo ""; printf '%s\n' "$BLOCK"; } > "$TARGET"
        info "Appended the preset block to $TARGET"
    fi
fi

# The block's `@` line resolves against the directory of the file holding it.
# A file that is not there loads nothing and nobody is told, so say it here,
# the one moment anybody is looking.
IMPORT="$(printf '%s\n' "$BLOCK" | sed -n 's/^@//p')"
CORE="$(dirname "$TARGET")/$IMPORT"
if [ -n "$IMPORT" ] && [ ! -f "$CORE" ]; then
    warn "The block imports $CORE, which is not a file, so no session reads the core yet. Install the plugin (below); where its plugins directory is not beside $TARGET, the import cannot load."
fi

echo ""
info "CLAUDE.md done. Remaining components install as a plugin:"
echo "       claude → /plugin marketplace add MichaelYcJo/AgenticSeal"
echo "                /plugin install agentic@agenticseal"
