# Questions for the planner: 1795499830-the-orchestrator-asks-under-automation-yes

The issue left these judgments open, and the tree answered each:

- The form the hook reads exactly: `frame/plan.md` *Alternatives considered*, the rows on the form.
- How a work item counts as still open: `frame/plan.md` *Alternatives considered*, the rows on what counts as open.
- How the session's worktrees are found: `frame/design.md` *Grounding*, the paragraphs on the reading this design takes and on how the tree lists worktrees.
- How the sentence that no script decides on `Automation`, and every other statement of it, changes: `frame/design.md` *Grounding*, the paragraph on every statement that no script decides on `Automation`, and `## Removes`.
- Whether the policy documents change in this pull request: `frame/plan.md` *Alternatives considered*, the row on editing the three documents under `docs/running/`.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does Claude Code 2.1.331 honour this plugin's `PreToolUse` deny on `AskUserQuestion` in the main session: is the question not shown to the person, and does the session read `permissionDecisionReason`? The tree cannot answer it, since the hook runs from the installed plugin copy, which gains it only after the release, and no probe can, since a subagent has no `AskUserQuestion` to call | a measurement | Honoured: the work holds as framed. Not honoured: the hook prints nothing a session acts on, and the work item that finds it reopens the carrier | Honoured, as the binary's `PreToolUse` branch reads `permissionDecision` `deny` with its reason (`frame/design.md` *Grounding*, executed). The orchestrator's first session on 0.38.8 that calls `AskUserQuestion` while an open work item reads `yes` answers it | answered 2026-11-24 by the orchestrator, by measurement (executed): honoured. An interactive Claude Code 2.1.331 session, started through a pseudo-terminal with a `--settings` file whose `PreToolUse` hook on `AskUserQuestion` printed the deny object of `frame/design.md` *Data & interfaces*, called the tool once. The hook received `tool_name` `AskUserQuestion` with the one input key `questions`; no question was shown; the session received `PreToolUse:AskUserQuestion hook error: <the reason>`, quoted the reason and did not call again. A `claude -p` session cannot answer it, since it offers no `AskUserQuestion` |
