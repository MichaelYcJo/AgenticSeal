"""Which variable names a Claude Code session.

**This module is the one reader of which variable is the session's.**
`skills/implement/scripts/seal.py` reads the session's id from it.

The commit gate's route from a git hook back to its session lived here until
#1027 removed every hook of this plugin that ran inside git.
"""

# The one variable the harness exports that names the session.
SESSION_VARIABLE = "CLAUDE_CODE_SESSION_ID"
