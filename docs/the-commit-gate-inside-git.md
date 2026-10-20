# The commit gate inside git

Authority for the `pre-commit`, `reference-transaction` and `post-commit`
stubs `hooks/hook-install.py` writes: which commits they judge and which they
leave to a person or to git, what they cannot see, and which reading judges a
commit in each state of a repository. What a stop asks about, the two arms
and the routing declaration, is `docs/the-review-and-parity-arms.md`. The
PreToolUse reading that judges where git cannot is
`docs/commit-review-gate-spec.md`. The stamp `post-commit` queues when a
commit carries a `guarantee.md` reading `sealed` is `docs/the-review-record.md`
*The stamp*. Update spec and code together.

## The commit gate inside git

**In a clone carrying this plugin's git hooks, a commit is judged inside the
commit, in the worktree it lands in, and the command's text is an input to
nothing.** `pre-commit` runs in the git process making the commit, with its
working directory at the root of the worktree whose index becomes the commit
and the branch `HEAD` names there. So no shell construct routes a commit
around the decision: a command that commits reaches git, and one that does not
needs no decision.
check: judged-inside-the-commit

**The hooks are stubs that `hooks/hook-install.py` writes, and a hooks slot
somebody else holds is never written over.** The installer runs at session
start and first in every Bash call's `pre-bash` group, for the clone the
payload's `cwd` is in, and writes the three stubs into that clone's common
`hooks/` directory, which every worktree of it shares. Each stub carries the
marker line `# specseal-git-hook <version>` and the installed plugin's
absolute path, which it tests before running anything, so removing the plugin
leaves stubs that do nothing. A stub whose bytes differ from what the running
plugin would write, or that git cannot execute, is rewritten, and until it is
the clone is not one where git decides. `core.hooksPath` set at any level, or
a hook file without the marker, makes the clone foreign: nothing is written,
the plugin's own stubs there are taken out, and the session is told once. A
clone that does not opt in gets nothing and loses the stubs it had.
check: tests/test_the_hooks_are_installed_where_git_runs_them.py

**A commit with no Claude session behind it is a person's own, and is not
judged.** The session comes from `CLAUDE_CODE_SESSION_ID`, the one session
variable the harness exports to every Bash child, which git hands to its
hooks; the stub's short-cut tests that name and no other. Where it is absent,
as under `env -i`, the hook takes the lease (`hooks/session-lease.py`) whose
recorded pid is the session's `claude` process: `CLAUDE_PID` where the
environment carries it, an observed value, and else its nearest ancestor whose
name is `claude`. The lease writer records its pid by the same reader, so the
lease it writes is the one the hook finds, and it reads `CLAUDE_PID` only
where the hook's own `CLAUDE_CODE_SESSION_ID` is the session it records: a
`claude` started from another session's Bash inherits that session's pid, so
elsewhere the writer walks. A process is a Claude session by one test, its
executable's basename is `claude` (`hooks/hooksession.py#is_claude`), which
the worktree guard's count of other sessions uses too. Two leases naming one
pid are no session. With neither, the commit is the person's, and the stub
leaves before Python starts wherever no lease file stands in the clone.
`hooks/hooksession.py` holds the two routes and the names they read.
check: a-persons-own-commit

**The arms, the marks and the declaration are the ones
`docs/the-review-and-parity-arms.md` states, asked of
`hooks/gate.py#arms_missing`; what changes is how a stop is put.** A git hook
cannot render two buttons, so every stop is the hook's exit status and its
text on stderr, which git prints into the command's output and the model
reads. The text is the same on every attempt. Attended, it tells the model to
put the arm's options to the person with AskUserQuestion; under the
`automation` press it names no question tool. Every option names a command
that runs, the git-native waiver first: `git -c specseal.waive=review commit
…` (and `=parity`), which git hands the hook through `GIT_CONFIG_PARAMETERS`
and which inside a message is prose. The older `: '[no-review]'; git commit …`
keeps working: `hooks/answer-write.py` reads the bare word out of the Bash
call, outside every heredoc body, through `hooks/tokens.py#given`, the one
reader of a consent token, and `hooks/answers.py` carries it to the hook for
that call alone. The parent and every subagent share one session id, so the
answer is kept per call, under the payload's `tool_use_id` with the command
beside it, and given only to a commit whose ancestry up to the `claude`
process carries that command, because the Bash tool's shell holds it in its
argv. Another agent's commit in the same moment is its own command and is
judged, and another agent's call starting or ending leaves the answer alone.
check: how-a-stop-is-put

**Beside the arms, `pre-commit` refuses a commit that stages a work item's
`sealed` over a commit its own history does not hold, and records the
refusal; it is no arm.** Where no arm is missing,
`hooks/commitgate.py#guarantee_off_history` reads each staged
`seal/specs/<item>/guarantee.md` and that item's `routing.md` from the index,
with `git show :<path>`, so a `commit -a` and a pathspec commit are read as
git will commit them. It refuses where the guarantee reads one `Verdict:` of
`sealed`, the `Branch` row names the branch being committed on, and
`git merge-base --is-ancestor <target> HEAD` does not exit 0, which covers a
target that does not resolve and one off the history alike. A commit that
concludes a conflicted merge is judged against `HEAD` alone, so a `sealed`
the merged side brings in over that side's own commit is refused, and the way
on is `git commit --no-verify`; in this plugin's flow a conflict with the base
is resolved before the broad run and the sealer, so a sealed guarantee is
never what such a merge brings in. The text names the file, the commit the
row names, the branch and HEAD, and one way on: a new audit of the sealer at
HEAD, whose `Target SHA` row keeps the refused verdict as
`; earlier run: <sha> sealed`, and never a row edited by hand. Before it
prints, the hook writes the refusal record
`<git-common-dir>/specseal-stamp-refused/<id>-<target>`, so that the new
audit draws the work item's stamp. It does not read the `; earlier run:`
chain, judge a commit on any other branch, or judge a commit git makes for its
own rebase or cherry-pick. It has no opt-in beyond `seal/`, no mark, no waiver
and no question, because the pull request's check refuses the same file. A
commit that stages no guarantee loads nothing for it, and a reading that fails
stops nothing. Where the stub does not run, as under `--no-verify` or in a
foreign hooks slot, the row lands, and its work item draws no stamp. So does a
row an amend folds into the very commit it audited: `pre-commit` runs with
HEAD still at that commit and cannot tell an amend from a plain commit, and
the pull request's check refuses the landed row as stale.
check: sealed-off-the-branch-refused

**`--no-verify` is met where the branch moves, and nothing else that moves a
branch is.** `--no-verify` skips `pre-commit` and nothing after it, so
`reference-transaction` refuses, at `prepared`, a commit that `pre-commit`
never judged: HEAD, the index and the working tree stay as they were, with one
unreachable commit object left. What tells a commit from a merge, a reset, a
clean cherry-pick or revert, a rebase or a pull is `GIT_AUTHOR_DATE`, which
every `git commit` exports to its hooks and none of those does, measured on
git 2.34.1, 2.39.5, 2.43.0 and 2.50.1. A commit `pre-commit` let through
carries a one-shot mark keyed by the old HEAD, the tree, that date and the
`git commit` process both hooks run under, and passes; a mark a commit left
when it aborted after `pre-commit` is another process's, and passes nothing.
A person who exports `GIT_AUTHOR_DATE` around a rebase makes it look like a
commit, and it meets the refusal: the fail direction is a stop.
check: no-verify-met-where-the-branch-moves

**A commit git makes for its own rebase, cherry-pick or revert is not judged;
a commit a shell starts while one is paused is.** A rebase, cherry-pick or
revert that stopped on a conflict, and a reword, finish through a child
`git commit` that hands both hooks the date and runs `pre-commit` for all but
`rebase --continue`. What tells that child from a person's commit, on all four
gits, is two facts together: a sequencer state under the worktree's git
directory (`rebase-merge`, `rebase-apply`, `sequencer`, `CHERRY_PICK_HEAD`,
`REVERT_HEAD`), and the `git commit` having been started by another `git`
process rather than a shell. So `git commit --no-verify` or `--amend` typed at
a paused rebase is judged, and so is an alias's commit outside a sequencer.
Where `ps` cannot answer, as on Windows, the commit is judged, and the fail
direction is a stop. `GIT_REFLOG_ACTION` is no criterion: only a rebase's
children carry it. A conflicted merge is not one of them: `MERGE_HEAD` is no
sequencer state here, and `git merge --continue` runs its commit in the
process the shell started, so concluding a conflicted merge is judged whether
it is typed as `git commit` or as `git merge --continue`. A merge with no
conflict makes its commit without `pre-commit` or the author date, and is not
judged.
check: gits-own-commits-not-judged

**Where git decides, the PreToolUse reading of
`docs/commit-review-gate-spec.md` stands aside; in a clone where git cannot,
that reading judges the commit.** Each target the reading names is asked
`hooks/githooks.py#decides` first and left to git where the stubs run. A
target the reading cannot place is left to git when the session's own clone is
git-decided, because the session's directory is the stand-in it would have
been judged against. **Only a command whose shape is known plain is left to
git at all** (`hooks/tokens.py#is_plain`); every other command is judged by
the reading wherever it lands. Plain is a positive rule rather than a list of
words that step around the hooks, because such a list is never finished. A
command is plain when it splits; every simple command's program is one of a
few words measured from the commit commands agents type (`git`, `cd`, `true`,
`:`, `echo`, `printf` with no option, `test`, `[`, and `cat`, `head`, `tail`,
`grep`, `wc`, `cut` reading output); each `git` passes only `-C` and a `-c` of
`commit.gpgsign`, `user.name`, `user.email` or `specseal.*` before `commit`,
`add`, `status`, `log`, `diff`, `show` or `rev-parse`; no assignment stands in
a command's place; output goes only to `/dev/null` or another descriptor;
nothing is parsed again (no `$( … )`, backtick, `( … )` or `{ … }`, and no
heredoc body holding a substitution behind an unquoted delimiter); and none of
the words `hooks/tokens.py#steps_around_hooks` reads appears. A misread costs
the one judgment the PreToolUse reading makes.
check: text-reading-stands-aside

**The convergence argument is claimed for commits alone.** No git refuses a
branch switch before its tree has moved: on 2.34 to 2.43 a switch reaches
`reference-transaction` with no line at all, and on 2.50.1 the line arrives
after the tree and index already hold the new branch. A branch-naming rebase
reaches `reference-transaction` the same way a switch does: on 2.50.1 its line
names the branch after the tree already holds it. A worktree creation can be
judged after git made it, in `post-checkout`, but only taken back there, and a
take-back cannot undo all of it: `worktree add -B` resets an existing branch
first, `--no-checkout` and `--orphan` run no `post-checkout`, and a `--lock`ed
tree survives one `--force`. So the worktree guard's switch and creation arms
read the command through the frozen reader `hooks/cmdline_base.py` on every
git, pinned so it cannot gain a rule (`docs/worktree-guard-spec.md`
*Which tree*). Those arms predict from text, and do not converge.
check: tests/test_the_hook_surface_git_offers.py tests/test_the_frozen_reading_never_grows.py

### Known limits of the commit gate inside git

- **A clone no session has reached carries no stubs.** The installer writes
  them for the clone a session starts in or a Bash call's `cwd` is in, so a
  commit by `git -C` into a clone neither ever was is judged by the PreToolUse
  reading instead. A person's global `init.templateDir` or `core.hooksPath`
  would close it, and writing either is outside what this plugin writes.
- **A commit through a construct the reading cannot place, into a clone that
  carries no stubs, from a session whose own clone does, is judged by
  nobody.** The reading stands aside on the session's clone, and git has no
  hook to run in the other one.
- **A command that removes the stubs, or takes their execute bit, before it
  commits steps around both hooks.** Neither `rm` nor `chmod` is a plain
  program, so the PreToolUse reading judges such a command before it runs, and
  the installer puts the stubs and their mode back at the next Bash call.
- **`git commit-tree` with `update-ref`, and `git am`, are not commits to
  either reading.** Neither meets `pre-commit`.
- **A commit git starts while a sequencer state is on disk is not judged,
  whoever asked for it.** An alias (`git -c alias.ci=commit ci`) and, where
  `/bin/sh` hands its last command straight to git as macOS's does, a
  `rebase --exec 'git commit …'` both run `git commit` under a `git` parent,
  and during a paused rebase, cherry-pick or revert those commits pass as the
  sequencer's own.
- **On Windows** the stubs run through git's bundled `sh`, whose `ps` takes no
  `-o`, so a hook finds no `claude` ancestor, and `env -i` empties
  `CLAUDE_PID` as it empties the session variable: a commit under `env -i`,
  which the lease names on POSIX, is a person's there. The backstop's mark is
  keyed without the `git commit` process, because each hook runs under its own
  `sh.exe`, so a mark an aborted commit left can pass a later `--no-verify`
  commit with the same HEAD, tree and date. No commit counts as the
  sequencer's, so a `rebase --continue` into an undeclared repository is
  refused. A command that exports `LD_PRELOAD` runs no hook at all, because
  the bundled `sh` dies loading the MSYS path `stdbuf` exports, and git
  commits as if every hook had passed. Neither command is plain, so the
  PreToolUse reading judges both before they run.
- **The old spelling waives only where the hook can find the call's shell.**
  It needs `ps`, a `claude` process above the commit, and a shell whose argv
  carries the command, which is how the Bash tool runs one. Where any of the
  three is missing, the bare word waives nothing and the refusal names
  `git -c specseal.waive=…`, the spelling that belongs to its own command.
  The match drops everything but letters and digits, `\NNN` escapes included,
  and looks for the carried command inside the shell's argv, so two agents
  running the same command are both waived, and so is a command carrying no
  token that contains another open call's whole command that way.
- **No case runs the stubs under a live Claude Code session.** The cases run
  git below a process named `claude` with the session variable set. Which
  harness version first exports `CLAUDE_CODE_SESSION_ID` and `CLAUDE_PID`,
  what a headless run exports, whether every payload carries `tool_use_id`
  (the answer store keys by the command's hash where one does not), and
  whether every harness keeps the command in the Bash shell's argv were read
  from one harness and are not pinned.
- **Latency.** A judged commit starts one interpreter in `pre-commit`, one in
  `reference-transaction` at `prepared`, and one in `post-commit`, which lists
  the paths the commit touched for the stamp. `pre-commit` lists the staged
  paths once for the arms and the guarantee refusal together. Measured on one
  machine as medians of 11 commits: 268 ms an ordinary judged commit against
  260 ms without it, and 310 ms against 283 ms for one that stages a `sealed`
  guarantee. A ref update that is not a commit, a fetch's among them, starts
  none, and so does a person's own commit where no lease file stands in the
  clone. A lease stands for up to a day after its session's last tool call,
  and while one does a person's commit pays the three interpreter starts so
  the stub can look for a `claude` ancestor, about 400 ms against 125 ms with
  no lease and 50 ms with no stubs. The installer, first in every Bash call's
  `pre-bash` group, starts two `git` processes and reads each stub, a median
  113 ms on every Bash call in an opted-in clone, a commit or not.

### Where each state of a repository stands

| State | What judges a commit |
|---|---|
| a clone carrying the stubs | `pre-commit`, then `reference-transaction` for one that skipped it; the PreToolUse reading as well for every command `hooks/tokens.py#is_plain` does not call plain |
| a clone whose hooks slot is foreign | the PreToolUse reading, said once per session |
| an opted-in clone no session has reached | the PreToolUse reading, until a session or a Bash call reaches it |
| a clone that opted out after the stubs arrived | nothing: each stub reads the opt-in when it runs, and the installer takes them out |
| a person's own commit, with no session behind it | nothing |
