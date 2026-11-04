# Closing memo: 1793833679-update-reads-the-config-dir-in-use

## Not verified

| Item | Who must answer |
|---|---|
| The new cases on the ubuntu and Windows legs of the test workflow (`frame/questions.md` Q2). Phase 1 ran them on macOS alone | the orchestrator, by a run of the `tests` workflow on the branch |
| That the shell a session's Bash call runs in inherits `CLAUDE_CONFIG_DIR` from the Claude Code process that started it (`frame/questions.md`, the paragraph above its table). The cases set the variable themselves, so none of them shows it | the orchestrator, by a measurement: a session started under a scratch `CLAUDE_CONFIG_DIR` prints the variable from its Bash tool |
| The full suite, the repository-wide lint and the format check at the branch's HEAD | the orchestrator's broad run of the `Broad gate` row in `seal/config.md` |

## Not done

`test_the_skill_names_no_fixed_claude_directory` searches for two spellings, `~/.claude` and `$HOME/.claude`, as `frame/design.md` *Scope* 6d fixes them. A third spelling such as `${HOME}/.claude` passes it. For step 2b and step 3, the cases that run the command catch that spelling, and the mutation runs in `trail/phases/phase-1.md` show it. For the repair's `rsync` source and step 5's prose, no case does. Widening the search was within reach and was not taken. The spellings of a path form an open class, and the core says no script carries a list of the spellings a label is written in (`skills/core/SKILL.md` *The rule a mechanism is kept against*). So that reading stays with review.
