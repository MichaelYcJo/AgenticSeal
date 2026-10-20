### Fixed

- **A run routed `automation` no longer stops to ask (#1002).** A new
  `PreToolUse` gate, `question-gate`, refuses `AskUserQuestion` on every call
  on a branch whose `routing.md` answers `Automation` with `yes`. Its reason
  names that declaration and the work item's `questions.md`: the session
  builds on the default the question states, writes it there as a row, and
  names it in the pull request body, where the owner can overturn it. The
  routing question put alone goes through, so a resumed run can put it
  again. Every other branch, and every declaration that cannot be read, is
  left alone. A session in a checkout of another branch is not held, and
  neither is a question asked as plain text.
