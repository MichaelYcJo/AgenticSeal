# Questions for the planner: 1794142458-config-dir-readers

The judgments the ticket left open that the tree answered, so nobody reopens them:

- What "the Python equivalent `core_check.py` uses" is, now that the file is gone: `frame/design.md` G3.
- Whether the README's history line about `~/.claude/settings.json` is in the class: `frame/design.md` G2.
- Whether `payload_meter.py` replaces `home` or keeps it beside the config directory: `frame/plan.md` *Alternatives considered* row 8.
- How a row read under a set variable is labelled: `frame/plan.md` *Alternatives considered* rows 6 and 7.
- Where the suite drops the variable: `frame/plan.md` *Alternatives considered* row 9.
- Whether a text case guards the class: `frame/plan.md` *Alternatives considered* row 5.
- An empty or relative variable: `frame/design.md` G5.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does a Claude Code 2.1.319 session started with `CLAUDE_CONFIG_DIR` set load the user's `CLAUDE.md` and user skills from that directory, and not from `~/.claude`? `frame/design.md` G4 reads this from the binary's strings. No subagent can measure it. The measurement needs a signed-in session under a scratch config directory, and G4's search printed a line where the binary reads its credentials from `<config>/.credentials.json`, which a scratch directory does not hold. A subagent cannot sign in, and spending a model call to start a session is not a read-only probe | a measurement | Yes: the build stands as framed. No: `payload_meter.py`'s pair row and shadow follow wherever Claude Code does read, and S3 and S4 change with them | Yes, as the issue states and G4 reads | open |
