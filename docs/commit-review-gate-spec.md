# The commit gate's PreToolUse reading

Authority for how the hooks are registered, for `hooks/commit-review-gate.py`,
which reads a commit from the command's text where git cannot judge it, and
for the implementer mark. What git decides inside a commit, and which reading
judges each state of a repository, is `docs/the-commit-gate-inside-git.md`.
What each arm wants is `docs/the-review-and-parity-arms.md`. The review run
the hooks serve is `docs/the-review-record.md`. Update spec and code
together.

## Registration

`hooks/hooks.json` registers `hooks/dispatch.py <group>` per event, and the
dispatcher runs every gate of the group in one interpreter. A gate stays a
standalone script, and adding one means adding it to `GROUPS` in
`dispatch.py`. Where several gates of a group decide, the strictest wins
(deny, then ask, then silence) and every reason is kept in the merged text. A
gate that raises is skipped, and the rest of the group decides without it.

**A gate that fails is said once per session, at the end of the main
session's turn, and the call it failed on still goes ahead.** A failure is an
exception while loading the gate's file, a `SystemExit` included, or an
`Exception` from its `main()`; a `SystemExit` from `main()` is a gate
finishing. The dispatcher writes a record under
`<git-common-dir>/specseal-gate-failure/`, keyed by session and gate, in an
opted-in repository and wherever `optin.py` is itself the broken module. The
`stop` group says each pending record once as a `systemMessage`, before the
sealer's stamp where there is one, and the report carries no decision. A
failure in a git directory the dispatcher cannot write to is not said. No case
sees how the harness renders the report beside the stamp, on any platform, and
two hook processes racing for one record are forced in process, never run.
check: tests/test_a_gate_that_fails_says_so.py

## The PreToolUse reading of a commit

**The reading judges a commit only where git cannot:** a target in a clone
without this plugin's git hooks, a target it cannot place from a session whose
own clone has none, and a command whose shape is not known plain.
`docs/the-commit-gate-inside-git.md` *Where each state of a repository stands*
says which reading judges each state. It asks both arms
`docs/the-review-and-parity-arms.md` states, each with its own mark, waiver
and silence, and one arm satisfied never quiets the other.

| Condition | Decision |
|---|---|
| not a `git commit` command | silent |
| neither opt-in applies | silent, so a globally installed plugin does not nag unrelated repositories |
| a target the reading cannot resolve | stopped, as *Which repository* below says |
| every applicable mark equals current HEAD | allow |
| no session id in the payload | **ask**: nowhere records that the choice was put up, and a deny would repeat forever |
| this session's person pressed `automation` on the routing question | **deny**, every time, naming the ways on that need nobody |
| otherwise, the first stop this session meets in this repository | **deny**, whose reason instructs the model to put the choice up with AskUserQuestion, naming both ways on for every arm that fired |
| otherwise | **ask**, the harness putting two buttons to the user, every missing mark named at once; approving is the waiver |

A `deny` addresses the **model**: a hook cannot render a dialog, so it spends
its reason on instructions and hands the turn back. An `ask` addresses the
**user**: the harness renders two buttons the model never sees, and
declining is a bare "No". The word *asks* is used for neither alone.

**The first stop is a deny, and every later one in the same session and
repository an ask.** A declined `ask` leaves the user retyping the command for
the other way on, and a deny gives the model the turn to put both. The record
is `<git-dir>/specseal-commit-choice/<session-id>`, the id reduced to its
basename, and an unwritable record counts as already asked, because one
missed question beats a deny nothing gets past.

**Where the person pressed `automation`, every stop is a deny.** The run was
promised that nothing stops to ask, and a subagent's call carries its
parent's session id, so one deny per session would be spent by the first
agent to meet it. The reason names the ways on that need nobody: a commit
whose repository the gate can read, an edit through the `Edit` or `Write`
tool, the waiver only for a commit no work item owns, and otherwise handing
the commit back. It names no question tool, and says that re-issuing the
command unchanged meets the same refusal. The press is read through
`hooks/worktree_consent.py#automation_answered`, the reader
`docs/worktree-guard-spec.md` *Creation consent* uses, against the session's
own repository and only once a stop is decided, so what the gate stops does
not move. A `per axis` answer and a `routing.md` `Automation` row are not
read, and the last answer to the routing question from this clone stands.
Every way of not reading the press is the attended answer. This blocks more
and never allows more; what bounds a model that re-issues the same command is
the reason's text alone.
check: tests/test_an_automation_run_meets_no_commit_prompt.py

**Both arms, one call.** When both arms fire, the reason asks for two
questions inside one AskUserQuestion call rather than one question with four
combined options: the arms are waived independently, and one call is one
interruption.

### Which repository

**The repository judged is the one the command commits into, not the one the
shell sits in.** `git -C <path>` moves git without moving the shell, repeated
`-C` compose, and a `cd` moves the shell before git runs, so every directory a
command can commit into is read from the command, with `cwd` the fallback. A
command committing into two repositories is judged for both, and where every
directory it reaches sits in one repository the operators decide nothing.

| The command | What is judged |
|---|---|
| `cd X && git commit` | the repository holding X |
| `cd X ; git commit`, or the two on separate lines | both: a failed `cd` leaves the commit in the session's own repository |
| `cd X \|\| git commit` | both |
| `cd X \| git commit`, `cd X & git commit` | both: the commit runs in a subshell that never left, unless `lastpipe` runs it in X |
| `cd N \|\| cd B && git commit` | N and B |
| `cd X && make \|\| git commit` | X and the session's own repository |

The reading is of `tool_input.command` before the shell expands it.

**A target the reading cannot resolve stops wherever the session's own
repository opted in, and is silent anywhere else.** The session's own
repository decides whether the gate speaks, never what is true of the target.

| The command | Why it cannot be resolved |
|---|---|
| `git -C "$WT" commit`, `cd "$WT"` | a variable is not expanded, and a mistyped path reads the same |
| `cd /tmp/x*`, `cd {a,b}` | it names a set of paths |
| `(cd X && git commit)` | the parenthesis decides where the commit runs |
| `cd -` with nothing behind it | there is no previous directory |
| a function body, a sourced script, an `eval`, a `pushd`, a loop | the reader enumerates the shell's reserved words and simple commands, never the open list of things that move a shell |

The stop is put as the table above puts any stop. Its first way on is to
write the path out, which lets the gate reach a verdict; the waiver is
second.
check: tests/test_gate_judges_the_repo_it_commits_to.py tests/test_what_the_reader_understands.py

**A commit is read wherever the shell would run one.** That is behind a
reserved word that opens a command list (`do`, `then`, `else`, `elif`, `if`,
`while`, `until`, `{`), behind a program that runs its operands (`exec`,
`nice`, `timeout`, `xargs`, `sudo`, `find`, `watch` and the rest of
`cmdline.RUNNERS`), behind a redirection, in a string a shell is handed
(`sh -c`, `bash -c`, `su -c`, `env -S`, the argument of `eval`), and in the
body of `$( … )`, backticks, `<( … )` or `>( … )`. A commit the walk cannot
place, behind a reserved word, a runner's own options, or in a string or a
substitution, is unresolved and stops as above. A body nested past what the
reader reads counts as one that might commit. A program whose operand is a
script or another machine (`bash run.sh`, `source`, `make`, `uv run`, `npx`,
`ssh`, `docker exec`) is not read.
check: tests/test_a_commit_behind_a_reserved_word_is_judged.py tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py

**A change to the reading adds stops and never removes one.** A `cd` target
is not trusted not to fail, and a heredoc body is read as shell for whether it
commits, but for the one shape below: each narrowing tried read a command
silent that a real bash then committed.
check: tests/test_no_shape_the_base_stops_reads_silent.py

**Only what the shell would execute is read as a command, and a waiver
counts only where it is typed in front of the call's own command.** A heredoc
body is data for where a commit lands, as a comment is. The waiver read,
`hooks/tokens.py#given`, keeps comments, because the documented form writes
the token in one, and skips every heredoc body, so a token inside a body
waives nothing, a body a shell runs included. A command that does not split
carries no token from where its split fails: a waiver inside a quote that
never closes, or after an apostrophe in a comment (`# don't [no-review]`), is
read as nothing. The worktree guard and the git hooks' old spelling read
through the same reader.
check: executed-text-is-read

**A file edit goes through the `Edit` tool, because a shell command that only
edits a file is still a command line this gate reads.** Whether a command
commits at all is asked of every heredoc body but one shape's, as shell. Two
kinds of segment count. One is a segment whose command word is `git` with the
`commit` subcommand, so what counts is the position and never the presence of
the word: a fixture file of shell commands held in Python strings can read
clean whole while a patch of it trips. A string a shell would run is a
position too, the one `sh -c` is handed or the inside of `$( … )` or a
backtick pair. The other has no commit in it: an `eval` whose argument the
reader cannot expand stops the session. So a session that searched its patch
for a commit and found none has not cleared it, and an `Edit` call leaves no
command line to read.

The one shape is data, and the repository owner made that trade for one shape
alone, the one `hooks/one_heredoc.py` matches byte for byte. Its first line
is, with one space between tokens and nothing before or after: optionally
`cd`, one word and `&&`; then the consumer; then `<<` and, with no space
between them, a delimiter of letters, digits and underscores in single
quotes. The consumer is `cat` with `>` or `>>` and one word, `tee` or `tee -a`
and one word, or `python3 -` and any number of words, where a word is a path
of letters, digits, `_`, `.`, `/` and `-` not starting with `-`, or one
single-quoted word that is not empty and holds no quote or newline. The body
ends at the first line exactly equal to the delimiter, compared on the raw
text. The command holds no carriage return, no NUL, no backslash before a
newline, and no second `<<` outside the body. After `cat` or `tee` nothing
but newlines may follow the terminator, because nothing may run after a file
is written; after `python3 -` anything may, and it is read as shell. The gate
reads such a command with its body and terminator taken out. Every other body
is read as shell: an unquoted, double-quoted or partly quoted delimiter,
`<<-`, an assignment or a substitution on the first line, a parameter as a
target or an argument, a program after a file sink, a second heredoc, and
every body below the top level.
check: one-heredoc-shape-is-data

## The implementer mark and notice

**A `framer` or `smith` spawn leaves a mark, and a commit on a branch whose
declaration names that agent, with no mark standing, gets one line saying
so.** The two axes of the routing declaration that name an agent,
`Planning` and `Implementation`, each answer an agent's name or
`the session`. Two hooks share one address module, `hooks/implementer.py`,
for both axes.

| Hook | Fires | Does |
|---|---|---|
| `implementer-mark` (`pre-agent`) | an Agent or Task spawn whose `subagent_type` is `framer` or `smith` | writes the checked-out branch name to `<git-dir>/specseal-planner` or `<git-dir>/specseal-implementer`, and prints nothing |
| `implementer-notice` (`post-bash`) | a command that invokes `git commit` | where the branch's declaration names an agent on an axis and no mark of that axis stands for the branch, prints one line naming the file, one line for both axes where both are unfulfilled, once per session per repository; silent for an axis whose mark stands, whose row is absent or outside its vocabulary, or which answers `the session` |

Neither hook can deny or ask. A mark is keyed on the branch, because a work
item commits many times, and on the axis, because `smith` is spawned on nearly
every work item. It lives in the git directory, so nothing at the pull request
reads either axis. Everything fails toward no mark, which is toward the
reminder, and the commit gate's decision does not read the mark.
check: tests/test_the_implementer_is_recorded.py
