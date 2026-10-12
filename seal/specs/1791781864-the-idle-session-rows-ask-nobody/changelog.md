### Changed

- **Under `automation`, a branch switch in a tree holding only idle sessions,
  or where sessions cannot be counted, no longer reaches the person (#896).**
  In the 0.21.0 run the worktree guard met a `git switch` beside a lease
  4.7 hours old, told the model to put two options to the owner with
  `AskUserQuestion`, and asked the owner directly on every attempt after, in
  a run routed `automation`.

  1. Where the person pressed `automation`, both rows now refuse the switch
     to the model on every attempt. The refusal names the way on that needs
     nobody: split into a worktree with `git worktree add`, which that answer
     already consents to, and work there by path with `git -C`. It names no
     question tool and no `[shared-tree-ok]`, and says that re-issuing the
     switch unchanged meets the same refusal.
  2. Without the press nothing changes: the person sees the same two
     options and the same prompt after them, word for word.
  3. On Windows, where sessions can never be counted, every `git switch`
     under the press is this refusal, so an `automation` run there works in
     a worktree per branch.

- **A session the guard cannot tie to a process no longer reads as working
  right now (#896).** Its line under a guard prompt used to end with a clause
  saying it was working on the tree at that moment, at any age, under a
  header saying none of the sessions could be shown to be working. The line
  now prints the kind of signal and its age and stops there, for example
  `lease declaration 4.7h ago`, in both languages.
