### Changed

- **The bootstrap has a file of its own, read only where a repository has no root yet (#1046).** *Orchestrator: Bootstrap* moves unchanged from `skills/implement/orchestration.md` to `skills/implement/bootstrap.md`. Every orchestrating session reads `orchestration.md` before its first edit, and it is down from 7,835 words to 5,839. Its opening paragraph says that where no `seal/` whose `README.md` opens with the marker exists at `<repo>/seal/` or at `$(git rev-parse --git-common-dir)/seal/`, the orchestrator reads `skills/implement/bootstrap.md` first. The preset block in `templates/setup/claude-md-block.md` sends a fresh repository to the new file. A block copied into `~/.claude/CLAUDE.md` before this release still names `orchestration.md`, whose opening paragraph sends the session on, until `/agentic:update` copies the block again.
- **A yes to the parity question follows the parity-setup procedure (#1046).** The bootstrap's step 3 sends the orchestrator to `skills/parity-setup/SKILL.md` *Procedure*, which it reads rather than invokes. That procedure also confirms the original's module, which the removed restatement did not.
- **The parity-setup procedure says which mode commits the declaration and which setup refuses a pull request without an `original:` line (#1046).** Step 6 commits `seal/parity.md` only where the root is `<repo>/seal/`, and in local mode commits nothing. Step 7 promises the refusal only where the root is `<repo>/seal/` and `seal pr-checks` reports the checks installed. In local mode and under shared, records only, it says that the line is still written and that nothing refuses a record without it. `skills/legacy-parity/SKILL.md` *The migration config* says the same about committing the file.

### Removed

- **`skills/implement/orchestration.md` *Orchestrator: Parity setup* (#1046).** It restated four steps of `skills/parity-setup/SKILL.md` *Procedure*, and the two had drifted apart. The acts table's row for it goes, and its grounds join the Bootstrap row.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-10-29 | The bootstrap is `skills/implement/bootstrap.md`, which the orchestrator reads only where no root carrying the marker exists, and a yes to its parity question follows `skills/parity-setup/SKILL.md` *Procedure*; `skills/implement/orchestration.md` holds neither | Every orchestrating session read about 2,000 words of first-setup text before its first edit, and the parity setup was a second statement of a procedure that had moved on | https://github.com/MichaelYcJo/AgenticSeal/issues/1046 |
