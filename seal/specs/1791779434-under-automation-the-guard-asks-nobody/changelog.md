### Changed

- **Under `automation`, a branch switch over uncommitted changes no longer
  asks the person (#894).** In the 0.21.0 run the worktree guard put a
  yes/no to the owner when a `smith` switched branches with one modified
  file, in a run routed `automation` on every item. That row of the guard
  read no press at all. It now has two readers, as the guard's stop for an
  unrecognised shape already had.

  1. Where the person pressed `automation`, the switch is refused to the
     model. The refusal lists the changes and says the guard stops a switch
     while they are present. It names `git commit` and `git stash` as
     commands that pass the guard when run on their own, and leaves which
     one fits, and what comes after, to the model and to git's own output.
     It says nothing about what any kind of switch does with the changes,
     and it is the same text for every kind. Re-issuing the switch unchanged
     meets the same refusal, so the model is told to act rather than retry.
  2. Without the press nothing changes: the person sees the same prompt,
     word for word.

  **What an orchestrating session does differently.** The press lives in
  the session that received it, on the machine it ran on. A run resumed in
  a new session (a `/clear`, a new start, another machine) puts the routing
  question's first question through `AskUserQuestion` again before the
  first spawn. A typed "automation, as before" is not the press, and
  `routing.md` is not read in its place, because the model writes that file.
  `claude --resume` and compaction keep the session, so neither needs it.
