### Changed

- **The hooks read the session, a waiver and a creation one way each
  (#868), and the worktree guard names a word the shell builds before git
  runs as a limit (#856).** Four facts every gate depends on were read in
  more than one place, and the readings disagreed. Each now has one reader.

  1. Where a worktree creation lands. The consent writer files a creation
     under the clone the worktree guard judged, by the guard's own
     placement. It used to take the first directory it could compute, so
     `eval x ; cd A || git worktree add …` was filed under `A`, the branch
     bash skips, and `cd <missing> ; git worktree add …` filed nothing.
  2. Which process is the session. The lease writer, the commit gate's
     lease route and the guard's count of other sessions test a process by
     one rule, its basename is `claude`, and read `CLAUDE_PID` first where
     the harness exports it. The lease writer reads it only beside its own
     session's `CLAUDE_CODE_SESSION_ID`, so a session started from another
     session's Bash, which inherits the outer pid, records its own process
     instead. The lease writer used to accept any name
     holding `claude`, so it could record a lease no reader matched. The
     git hook stubs test one session variable, `CLAUDE_CODE_SESSION_ID`;
     they also tested `CLAUDECODE`, which nothing behind them read.
  3. Whether a waiver token was typed. The commit gate, the worktree guard
     and the old spelling handed to the git hooks read `[no-review]`,
     `[no-parity]`, `[worktree-ok]` and `[shared-tree-ok]` through one
     reader, which reads the words before a quote that never closes and
     none inside it.
  4. What a failed git call means. The commit gate's two readings run git
     through one runner, which tells an empty answer from a failure.

  What a person meets:

  - A `[no-review]` inside a quote that never closes, or after an
    apostrophe in its comment (`# don't [no-review]`), waives nothing. The
    commit gate used to read it as a substring. The stop names the waiver
    typed in front, `: '[no-review]'; git commit …`. Over the 32,431
    recorded command and directory pairs, one pair's waiver moves.
  - A token written before an apostrophe in its comment (`# [shared-tree-ok]
    the release's own tree`) is still read, by every gate.
  - In a repository declaring `seal/parity.md`, a commit whose `git diff`
    fails meets the parity question, where it was let through as a change
    confined to `docs/` and `seal/`. That includes `git commit -a` or a
    pathspec on a branch with no commit yet.
  - A brace expansion changes nothing the worktree guard says, as at
    0.20.0. `git rebase {main,feature/x}`, `git rebase --ro{,} feature/x`,
    `git stash {branch,} y` and `git worktree {add,} ../wt f` are listed and
    silent in every tree, though bash makes the first three switch HEAD and
    the fourth add a worktree. A reader for them was built and taken out
    inside this release: every reading of it imitated bash, and five review
    rounds each found the next spelling it missed. The guard's policy names
    the brace as a limit beside the other words the shell builds before git
    runs (a substitution that spells `git`, a here-string handed to a shell,
    a git spelled past the splitter), and #886 decides them together.
  - The git hook stubs' bytes change by one variable name, so the installer
    rewrites every opted-in clone's three stubs at the next session, as it
    does when the plugin moves.
