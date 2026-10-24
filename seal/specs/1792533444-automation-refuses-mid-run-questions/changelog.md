### Fixed

- **A run routed `automation` no longer stops to ask (#1002).** A new
  `PreToolUse` gate, `question-gate`, refuses `AskUserQuestion` on every call
  on a branch whose `routing.md` answers `Automation` with `yes`. Its reason
  names the work item's directory once: the session builds on the default
  the question states, writes it as a row of `questions.md` there, and names
  it in the pull request body, where the owner can overturn it. A question
  that states no default, such as another gate's choice, is not answered:
  the session takes none of its ways on and hands that stop back at the end
  of the run. The routing question put alone, single-select and with its
  text, goes through while the session's transcript holds no answer to it
  from that clone, so a resumed run can put it again once. After an answer,
  one given for another work item included, or where no transcript can be
  read, it is refused like any other. Every other branch, and every declaration that cannot be read,
  is left alone. A session in a checkout of another branch is not held, and
  neither is a question asked as plain text.
