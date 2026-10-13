### Changed

- **The routing question no longer shows the four per-axis boxes to a person
  who pressed `automation` or `no work item` (#911).** The two questions used
  to go in one `AskUserQuestion` call, and the harness shows every question
  of a call at once, so the boxes were on screen at the start of nearly every
  run while meaning nothing under either answer.

  1. Question 1 is now asked alone. `automation` and `no work item` end the
     asking there.
  2. Under `per axis` the four boxes follow at once, in a second call, before
     the first edit. That answer now costs two clicks where it cost one.

  **Nothing that reads the answer changes.** The worktree guard and the
  commit gate read the `automation` press the same way from either shape, so
  a machine whose installed `CLAUDE.md` block is older still asks the old
  shape and still runs unattended. Run `/specseal:update` there to get the
  new block.
