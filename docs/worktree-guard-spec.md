# The worktree guard

Authority for `hooks/worktree-guard.py` and for the consent record
`hooks/worktree_consent.py` writes: what the guard refuses, asks or allows
before a branch switch or a worktree creation runs, and why. Update spec and
code together.

## Premise

Worktrees exist to keep concurrent work from mixing in one folder.
Single-stream work uses plain `git switch` on the shared tree. The guard
enforces both directions of that rule from one signal: how many work streams
are live on the tree.

## Decision matrix

### A. Branch switch

| Tree state | Decision |
|---|---|
| ACTIVE session present | deny, steering to a worktree. One destination, so no choice to offer |
| only IDLE sessions | **choice**: switch here, or split into a worktree, each session listed with its last-activity age, because a forgotten tab is the user's call. Under the `automation` press, a deny to the model on every attempt instead (*Choice sites*, *Under the press*) |
| detection unusable (the guard cannot see even its own process) | **choice**, the same two, because a blanket deny locks some hosts out entirely. Under the press, the same deny as the row above |
| single stream, tracked changes present | ask: the destination is the same either way, and what is asked is whether the uncommitted changes ride along. Under the press, a deny to the model instead |
| single stream, clean | allow silently |

`[shared-tree-ok]` in the command turns the two **choice** rows silent
(*Choice sites*). A dirty tree then reaches the tracked-changes row from those
two states as well, and its reason opens with the token carrying the user's
answer rather than with *Single-stream tree*.

**The tracked-changes row has two readers.** Where the session's person
pressed `automation` on the routing question, the row is a `deny` to the
model, because nobody is at the keyboard and the answer the person would give,
commit first, is not one of its two buttons. The press is read by the reader
the unrecognised-shape stop uses, against the root of the session's own
directory, never against the tree the switch names. The reason opens with the
`ask`'s lead, lists the changes as the `ask` does, carries the press
sentence, and says the row stops a switch while uncommitted tracked changes
are present and says nothing once none are. It names `git commit` and
`git stash` as commands on `LEAVES_THE_TREE`, each passing the guard when
issued alone, and leaves to the model which fits the switch. Each is a command
of its own, because the guard reads the tree before a line runs, so
`git stash && git switch x` meets this same row. It names no question tool,
and says re-issuing the command unchanged meets the same refusal. Without the
press the row is the `ask`, and `[shared-tree-ok]` reaches neither reader.

The row's text predicts nothing about what git does with the changes: one
string serves every switch form, from a branch or a detached HEAD, and names
no switch option. Its one sentence about git is the index-residue note it
shares with the `ask`. The guard reads the changes, that a switch is asked
for, and the press; where a commit lands or whether a stash restores cleanly
is not among them, and a sentence predicting either was wrong for some form
in every version written. A form found later is a row in the case that pins
one text for every form, never a sentence here.

**The failure direction.** A verdict moves from `ask` to `deny` in one state
and nowhere else, and the reader that decides it is the stop's. A wrong deny
costs the model a turn.
check: tests/test_worktree_consent.py tests/test_worktree_guard.py

A command that also creates a worktree is judged by this table whichever of
the two is written first, with the creation judged inside it (*Creation
consent*, *So the creation is judged between the ladder's two halves*).

**Which commands reach these rows.** The guard does not predict whether a
command switches a branch. It reads each git segment the frozen reading
yields (*Which tree*) as one of three shapes, from its words alone:

- **listed**: its subcommand is in `LEAVES_THE_TREE`, the git subcommands this
  repository's recorded runs hold whose plain invocation leaves HEAD's branch
  where it was, each beside its count, or it is a `checkout` with a path after
  its `--` (`git checkout -- f`, `git checkout x -- f`). A listed shape is
  silent in every tree state and spawns no git. `worktree` and `stash` are
  listed unless the first word bash hands git after them is `add` or
  `branch`, so a redirection in front of that word hides nothing. A `rebase`
  is listed unless it has two words that are not options, or `--root` and
  one: those name the branch git switches to before it rebases
  (`git rebase main feature/x`). A lone `-` is a word, since git reads it as
  `@{-1}`, and so is every word after a `--` or an `--end-of-options`: `git
  rebase - feature/x` switches too. git takes an unambiguous prefix of
  `--root` (`--ro`) as `--root`, and so does the guard.
- **a switch** — `git switch`, whatever its words. It takes the rows above, in
  the tree its segment names.
- **unrecognised**: every other git. That is a `checkout` with no path after a
  `--`, a subcommand the list does not hold (`update-ref`, `symbolic-ref`,
  `stash branch`, or one this repository never ran), and a git the frozen
  reading does not read as one: in a string handed to a shell (`sh -c`,
  `bash -c`, `eval`, `env -S`), in a `$( … )`, backtick or `<( … )` body whose
  git is not all listed, behind a redirection or a zsh precommand word, or in
  a command that would not split into words.

A creation is *B*'s and is read as *B* says.

**The stop for an unrecognised shape.** It is taken only where one of the
first four rows above would speak about a switch in the tree the shape's
segment names: another session ACTIVE or IDLE there, detection unusable, or
tracked changes. In a clean tree nobody else is in, row 5 says nothing of a
switch, and nothing is said of a shape that might be one. Where the tree
matters the guard stops before the rows, with one reason that quotes every
unrecognised shape on the line and its plain spelling: `git switch <branch>`
or `git switch --detach <rev>` for a switch, `git checkout -- <path>` or
`git restore <path>` for a restore, the git command run on its own for a
string or a body, `git` first and the redirection last, `git commit -F <file>`
for a command that would not split, and `git -C <dir>` for another tree. A
subcommand the list does not hold is its own plain spelling, so the reason
names running it in a scratch clone with `git -C <scratch clone>`, or after
the other session ends.

The stop has two readers. Where the session's person pressed `automation` on
the routing question, it is a `deny` to the model, which rewrites in the plain
spelling and meets the rows above on the retry, and no person is asked. In a
dirty tree that retry meets the tracked-changes row's deny, and with only IDLE
sessions or detection unusable the choice rows' deny, so no issue reaches a
person. Otherwise it is an `ask` with the same text, except in a tree another
session is ACTIVE in: row 1 denies a switch there with nobody asked, so the
stop is a `deny` whoever is at the keyboard. On the `ask` path a creation on
the same line is judged first, because approving runs every segment. A `git
switch` on the same line makes the stop a `deny` whoever is at the keyboard,
for the same reason: approving would run the switch past the rows above, in a
tree the stop's reason does not describe, so the reason says to run the switch
on its own. The consent record is never read for the stop: a creation having
run says nothing about whether anybody is at the keyboard.

Each unrecognised shape is judged in the tree its own segment names, first one
first, and each tree is looked up once, so a shape in a clean tree takes no
stop away from one behind it in a dirty tree. Every tree on the line is read
before the stop is taken, so a shape in a tree another session is ACTIVE in
makes it a `deny` even where an earlier tree only matters for its changes. The
reason names each tree that matters and why, because approving the `ask` runs
the line in every one of them; where one is ACTIVE, it describes the ACTIVE
trees alone. A reason that describes one tree calls it "this tree", whichever
tree it is: with the session's own tree clean and `W` dirty,
`git -C W checkout x` asks about "this tree" and means `W`. A git the wider
reading of `hooks/cmdline.py` (*Which tree*) reads as a segment of its own
(behind a redirection or a zsh precommand word) is judged in the tree its own
`-C` names, and so is a git
an `&` cut apart (`2>&1 git -C W switch x`), from the directory its first part
runs in. A body and a command that would not split belong to no one segment
and are judged in the session's own tree.

**The failure direction.** The stop adds a stop for every unrecognised shape
where the tree matters, and allows one thing more: a creation only a hidden
spelling holds, in a clean tree nobody else is in, where nothing the Premise
protects is at stake. Under the press the stops ask no person anything;
without it each is one `ask`.
check: tests/test_worktree_guard.py tests/test_worktree_consent.py

### B. Worktree creation

A creation is a `git worktree add`, or an Agent or Task call with
`isolation: "worktree"`.

| Tree state | Decision |
|---|---|
| **consent**: this session already created a worktree in this clone, or its person pressed `automation` on the routing question | **allow** where the tool call is worktree creation and nothing else; **silent** where the command does more, and on the Agent or Task path. Read before every row below it (*Creation consent*) |
| ACTIVE session present | ask: separation is justified, and creation still needs a person. Declining leaves nothing this session could issue instead |
| only IDLE sessions | **choice**: create it, or switch in the shared tree. Under the press this row is reached only in a clone the press was not given in and this session has created no worktree in, and there it is a deny to the model on every attempt, naming no way on (*Choice sites*, *Under the press*) |
| detection unusable | **choice**, the same two, and under the press the same deny |
| `[worktree-ok]` given (Bash only) | ask: the token is a completed confirmation coming back, and declining withdraws it |
| single stream, **Bash** | deny, steering to `git switch`; `[worktree-ok]` in a retry reaches the row above |
| **Agent or Task**, no consent, any tree state | ask: the agent runs beside this session, so the call is concurrent by construction. No session is counted, no choice site is reached, and declining cancels the spawn |

Every row between the consent row and the Agent or Task row is the Bash
path's, decided before the command runs in every clone (*Decided before git
runs*).

**An isolated agent is concurrent work by construction, so the Agent path
counts no session, asks once, and reads no token.** The agent runs beside the
session that spawned it, in a tree that is not switched: two work streams. The
session count cannot see it, because a subagent's call renews its parent's
lease and has no id of its own, so a count would read the spawn as
single-stream and steer it into the parent's tree. Consent is silence, for
the reason *Creation consent* gives; otherwise the path asks, once per
session, because a spawn that ran writes the record. An Agent call carries
prose, not a command line, and the model writes that prose, so a token in a
prompt could not tell a person's answer from a sentence about the token; the
path asks outright and the verdict does not depend on the prompt.
check: tests/test_worktree_guard.py

## Creation consent

**The first worktree creation in a session is the question, and a later one
in the same session is allowed; where the person pressed `automation`, not
even the first is asked.** A guard that asked at every creation held a run of
six work items at six `git worktree add` calls, and an unattended run stops
at the first.

`[worktree-ok]` is no consent: the token is written by whoever issues the
command, so the model can write it on the first attempt. What separates the
first creation from the sixth is available without trusting any token. The
harness runs only a `git worktree add` that was permitted, so a `PostToolUse`
observation of one that ran is written after the answer, which a command's
text cannot forge.

The routing answer is the second consent, and it covers the creation the
record cannot: the first. An automation run creates its worktrees before any
of them has run, and the answer is on disk when the first creation arrives,
written by the harness into the session's transcript from the person's click.
The model writes the question and its options, never which one was pressed.

| | `[worktree-ok]` | a `routing.md` reading `Automation` `yes` | the consent record | the routing answer in the transcript |
|---|---|---|---|---|
| written by | whoever issues the command | the model, with `Write` | the `PostToolUse` hook | the harness, from the person's click |
| written when | before the question | after the answer, as the model's account of it | after a creation ran | when the person answers |
| present at the first creation of an automation run | yes | no: the worktrees come first so each branch can carry its own | no | **yes** |
| forgeable by the model by habit | yes | yes | no | no |
| forgeable by editing a file on purpose | n/a | n/a | yes (`touch`) | yes (an appended line) |

A `routing.md` is not read, not even as a fallback: a fallback the model can
satisfy by writing a file is `[worktree-ok]`'s standing under another name.

**What is read**, and every way of failing it is *no consent*:

1. **This session's own main transcript**: the payload's `transcript_path`
   where its basename is `<session-id>.jsonl`, otherwise the one file matching
   `~/.claude/projects/*/<session-id>.jsonl`. A subagent's call carries its
   parent's session id, so it reaches the parent's answer through the second
   form. No other session's file is read, and no `subagents/` file.
2. **A harness-written `AskUserQuestion` result**: a `user` entry whose
   `tool_result` names, by `tool_use_id`, an earlier `AskUserQuestion` call,
   read from its structured `toolUseResult.answers`, and carrying
   `isSidechain: false`. A Bash result echoing the answer has no such link,
   and `true`, an absent field or a value that is not a bool is refused.
3. **The routing question**: one single-select question whose options'
   leading phrases are exactly `automation`, `per axis` and `no work item`
   (`skills/implement/orchestration.md` *Question 1*),
   answered with the option labelled `automation`. A `multiSelect` question is
   skipped, so the boxes neither give nor take back the press. The answer must
   equal one of the option labels verbatim; a typed `Other` answer is the
   person's own text and is not read. A leading phrase is the label casefolded
   and cut at the first ` (`, ` —` or ` -`, so `automation (Recommended)`
   counts.
4. **The same clone**: the result entry's own `cwd` resolves to the same
   common git directory as the creation's repository.
5. **The last answer stands**: of every answer to the routing question from
   that clone, the latest is read, so a later `per axis` or `no work item`
   takes the press back and a later press gives it back. A record already
   written stands: it is read first, and a creation that ran under the press
   was consented to.

A `per axis` answer is not read, even with its first box ticked: the box label
is reworded or translated often enough that a rule matching the prescribed
label would never fire. A read that raises is no consent, because a gate that
raises is skipped. The record is read first, because it is one `stat`, and
the transcript only while there is no record.

**The record** is an empty file at
`<git-common-dir>/agentic-worktree-consent/<session-id>`, whose existence is
the whole fact.

- **A directory of its own.** The choice marker is written before the answer
  and means the question was put, so one shared file would let the guard read
  its own question back as consent; and the two fail in opposite directions,
  an unwritable marker counting as already asked and an unwritable record as
  no consent.
- **The common git directory.** The record stands for *this session may split
  this clone*, and a linked worktree is the same clone.
- **The clone the guard judged.** The writer places a creation by the guard's
  own placement, `hooks/worktree_consent.py#place`, through the same
  tokenizing adapter, so the record lands under the clone whose tree the guard
  judged.
- **No expiry.** A session id is already scoped to a session.
- **A failed `git worktree add` records too.** The approval happened, and the
  retry after a failure is the worst moment to ask again.
- **An unwritable record leaves none**, silently, and the next creation asks.

**Why the allow is bounded.** `permissionDecision: "allow"` bypasses the
user's own permission settings for the whole tool call, so the guard allows
only a command that is worktree creation and nothing else. For anything more
it stays **silent**: it withdraws its objection, and the rest of the command
meets the harness's own permission flow. A command the lexer gave up on is
not vouched for. Within a segment, two tests bound the allow: **the segment's
command word is the word `git`**, compared exactly, because a basename is no
identity (`./git`, `/tmp/x/git` name files this hook cannot identify); and
**no token carries an expansion or a redirection** (`$`, a backtick, `<` or
`>`). Every quoting of the word `git` runs what `git` runs and is vouched for.
A glob or `~` in an argument, and a trailing `&`, run nothing else and are
left alone.

Without consent a command word outside that class splits two ways. One that
`cmdline.parse_git` reads as a git invocation (a path, a runner it reads past
such as `sudo` or `nice`, a leading assignment) is a creation and meets the
ladder. One it does not (`$GIT`, `gi*`, a substitution, a different case, a
trailing slash, a program outside the runners such as `uv run`) is no git to
this guard, and it says nothing. A git behind a redirection or a zsh
precommand word, or after a spaced `--config-env`, is no git to the frozen
reading either, and is an unrecognised shape (*A*): it stops where its tree
matters, under consent too, and in a clean tree nobody else is in it says
nothing. What the class costs is the allow on `/usr/bin/git worktree add …`:
a wrong silence leaves the call to the user's own settings, and a wrong allow
signs for a binary nobody identified.
`Test_only_creates_a_worktree` in `tests/test_worktree_guard.py` pins
members of each group in the rows of its two cases, and is where a new
spelling is checked.

**So the creation is judged between the ladder's two halves**, whichever of
the switch and the creation is written first, because the consent writer
records for a creation anywhere in a command that ran, and a creation the
guard never judged would mint consent.

| Switch-ladder row | Order | Why |
|---|---|---|
| ACTIVE session | above the creation | the one row that denies unconditionally; its deny stops the creation with the rest of the command |
| only IDLE, detection unusable | **both**, and the branch decides | these are choice sites: the deny keeps its precedence, because it stops the whole command line, while the fallback `ask` runs every segment, so that branch hands the creation its verdict first, through `choose`'s `before_ask` |
| **the creation** | | |
| tracked changes present | below | it asks whether the changes ride along and protects no tree, so the creation is questioned whether or not the tree is dirty |
| single stream, clean | below | it says nothing at all |

The walk keeps the first switch and the first creation in either order and
hands both to this table; an unrecognised shape on the same line is stopped
before either where its tree matters (*A*). Both orders get the same decision
and reason in every tree state, consent state and attempt, and the combined
verdict is never weaker than the switch's alone or the creation's alone. The
guard's other silent exit, at `if not top`, falls through the same way when a
`git -C <repo> worktree add` is in a command whose shell is outside any
repository.

**The property.** For a session with no consent, whatever the writer would
record for, the guard has either denied it or put the creation question in
the text of its `ask`.
`Test_main::test_refuses_to_be_silent_where_the_writer_records` in
`tests/test_worktree_guard.py` walks every shape `CREATIONS` lists in four
session states, from two shell directories, three attempts in the two
states whose budget the attempts spend, and
`Test_main::test_refuses_a_line_weaker_than_its_switch_or_its_creation`
holds the fifth state, the dirty tree. With consent, silence for a compound
is the designed answer.

**The Agent or Task path is silent rather than an allow**, because the call
is a creation plus an agent with a prompt, and the record answers the first
half only.

**What does not change.** A session with neither the record nor the routing
answer asks at every site, and the single-stream row denies and steers to
`git switch`. The switch direction reads neither: a creation the user agreed
to, or a run the user said should not stop, says nothing about taking another
session's branch out from under it.

**The prompt budget.** Zero for a session whose person pressed `automation`,
in the clone it was given in (another clone: *Choice sites*, *Under the
press*). One per session otherwise, for a creation written on its own: six
creations in one session on a clean single-stream tree answer deny, then
allow five times. With consent, a creation written as one segment of a
compound, or carrying an expansion, a redirection, a wrapper or a
path-qualified command word, gets no allow; the guard is silent, and what each
costs is whatever the user's own settings ask.
check: tests/test_worktree_consent.py tests/test_worktree_guard.py

### Decided before git runs

**A worktree creation is decided before git runs, in every clone.** A hook
after git made a creation
can only take it back, and a take-back cannot undo all of it: `git worktree
add -B <existing>` resets that branch before any hook runs, `--no-checkout`
and `--orphan` run no `post-checkout`, and a `--lock`ed tree survives one
`git worktree remove --force`. So the rows of *B* decide before the command
runs, through the frozen reading *Which tree* describes, and this plugin
installs no `post-checkout`.
check: tests/e2e/creation/test_creation_flow.py tests/test_the_hook_surface_git_offers.py

**A creation the guard lets through is recorded from the command that ran.**
The `PostToolUse` writer files the record in every clone, and `[worktree-ok]`
is read from the command by the guard itself, never carried to a git hook.
check: tests/e2e/creation/test_creation_flow.py

## Choice sites

A hook decision renders as approve or decline, and the model never gets the
turn, so at a site where declining has two destinations the user sees neither
and has to retype the command they wanted. Those sites deny instead, and spend
the reason on an AskUserQuestion instruction naming both. A site qualifies
when, after declining, more than one command is left that this session could
issue; the rows that stay `ask` or `deny` fail that test. A choice deny and
the ACTIVE-session block are both `deny`, and the reason tells them apart.

**The two branches have opposite standing for whatever else is on the
command line.** The deny stops the whole command, so anything written beside
what the site asks about is stopped too. The fallback `ask` does not:
approving runs every segment while its text asks about one of them. So
`choose` takes a `before_ask`, a judgment the fallback yields to, which is how
the switch ladder's two choice rows keep their deny and still question a
creation on the same line.

**Once per session per direction**, not per site. The marker is
`<git-dir>/agentic-worktree-choice/{create,switch}/<session-id>`, with the
session id reduced to its basename, because it names a file. One budget for
the whole guard let a creation question spend the answer a later switch
needed; within a direction the sites are mutually exclusive on tree state, so
a budget per site would buy nothing and cost a second question when a retry
with a token lands on a neighbouring site. The marker means the question was
put, and the consent record means a creation ran; they are different records.

An unwritable marker counts as already asked: one missed question beats a
deny nothing can get past. Every attempt after the first gets the site's
fallback decision, which is also the answer for an environment with nobody to
ask. With no session id there is no marker, and the fallback stands from the
start.

**Under the press** all four choice sites deny on every attempt; the switch's
two name the split into a worktree as the way on where its creation is
consented, and the creation's two name none. Nobody is at the keyboard to put
the two options to. The reason opens with the row's situation and the
tracked-changes row's press sentence. Where a creation in the switch's clone
is consented, by the press in the clone it was given in or by this session's
record in a clone it already split, the switch reason names which of the two
consents and the split as commands that pass as written with no
`[worktree-ok]`: `git worktree add <wt_root>/<branch> <branch>`, or
`git worktree add <wt_root>/<name> -b <branch> origin/main`, then `git -C` on
that path; a branch already in a worktree needs no switch. Elsewhere it names
no split, because a creation there is not consented. The creation rows are
reached under the press only there; their reason says the press consents to a
creation only in its own clone and nobody is at the keyboard to choose. No
reason names a question tool, `[worktree-ok]` or `[shared-tree-ok]`, and each
says re-issuing the command unchanged meets the same refusal. The press is
read by the stop's reader at the session's own root, only where a choice row
fires. No marker is written, because none was asked, so a later `per axis` in
the same clone meets the attended first attempt. `[shared-tree-ok]` still
turns the switch rows silent and `[worktree-ok]` still reaches its `ask`
above the creation rows. Without the press all four rows are as above.
check: tests/test_worktree_guard.py

**Retry tokens, one per direction**, matched as bare words of the command,
never as substrings, so a quoted sentence about a token answers nothing. The
whole command is tokenized first, and only when that fails does the check
drop to per-segment scanning. Unquoted prose still passes:
`git switch x && echo the [shared-tree-ok] token is documented` goes silent.

**A token counts only where it is typed outside every here-document body,
and a command that does not split carries none from where its split
fails.** The token is read from the command, and only the command:
`hooks/tokens.py#given` takes it only where the command as written and the
command with its here-document bodies taken out
(`hooks/tokens.py#without_bodies`) both carry it, a body a shell runs
included. It keeps comments, because a token may be written in one. Where
`hooks/cmdline.py` cannot load, the frozen reader finds the bodies. A token
inside a quote that never closes, or after an apostrophe in a comment
(`# don't [worktree-ok]`), is read as nothing. The Agent or Task path has no
command line and reads no token.
check: executed-text-is-read

| Token | Answer it carries | Effect |
|---|---|---|
| `[worktree-ok]` | create the worktree | the site asks: creating one always takes a confirmation, so no token lowers this direction below `ask` |
| `[shared-tree-ok]` | switch in the shared tree | the two switch **choice** rows go silent: the guard's own verdict there is *cannot tell*, so the token settles it |

**The token check runs before the choice sites**, after the ACTIVE-session
row, so a user who answered "split into a worktree" and came back with
`[worktree-ok]` is not asked again. **Each choice hands back the other
direction's token**: the switch options name `git worktree add … #
[worktree-ok]` and the creation options name `git switch … #
[shared-tree-ok]`, so following either answer arrives confirmed.

**What `[shared-tree-ok]` cannot reach.** The ACTIVE-session row is tested
before the token, so a token from this session never crosses the deny that
protects a tree this session does not own; the dirty-tree row asks something
else and is outside it too. The token records an answer in the command and
nothing verifies who wrote it, the standing `[worktree-ok]` has: an audit
trail, not an authorization.

Never guarded: file restores (`checkout -- <path>`, `restore`), every worktree
subcommand but `add`, and sessions living in linked worktrees, which are
already isolated.

## Declared work streams

Liveness is inferred below, and inference has a ceiling: a session hosted
outside a terminal, or working on this tree from another directory, leaves no
process, tty or per-project transcript trace here. So every tool call that
touches a repository also declares: the `session-lease` hook stamps
`<git-dir>/agentic-leases/<session-id>` for the repository touched (a file
edit leases the edited file's repository, a Bash call its `cwd`'s). A lease
fresher than the idle threshold is an active work stream. Leases older than a
day are pruned, and a failure is silent: a lease is a safety net, never a
blocker.

## Activity: what makes a session ACTIVE without a lease

**Active is any signal within `WORKTREE_GUARD_IDLE_MIN` minutes, default 5:**

| Signal | Detects | Grounds |
|---|---|---|
| tty atime (keystrokes) | a person at the keyboard | a forgotten tab is hours stale |
| tty mtime (screen writes) | a session streaming its progress | an idle prompt does not repaint; a working one repaints every second |
| transcript last ACTIVE event | autonomous turns and background agents (`~/.claude/projects/<slug>/<session-id>/subagents/*.jsonl`) | a session long past its last keystroke can be writing its transcript |

Five minutes is safe only because of the second and third signals: keyboard
input alone cannot tell a forgotten tab from an autonomous turn.
check: tests/test_worktree_guard.py

### Passive-event filtering

A transcript's mtime over-reports, because idle sessions receive passive
appends (an `attachment`, such as a file-changed notice another session's edit
fired). So a fresh mtime is confirmed against the last 64 KB: only `user`,
`assistant`, `tool_use`, `tool_result` and `progress` events count, by their
own timestamps. A stale mtime is trusted as it is, because a passive append
only makes a file look fresher.

### What a blocking prompt must show

"Another session is active" cannot be acted on without identity. Every listed
session shows:

- the **host app**, attributed by walking the ancestor process chain, never a
  sibling process;
- the **signals apart**: terminal input and output age and transcript
  active-event age. An unidentified session prints its one signal's kind and
  age and nothing after them, because whether it is working is the header's
  to say;
- the project's newest other transcript's **last user message**, so the
  person can recognise which conversation is being protected.

### Unknowns resolve conservatively

No readable tty and no readable transcript is active. Detection that cannot
find its own process is `reliable=False`, which takes the matrix's
detection-unusable rows. Those rows are a **choice**, a deny that hands the
decision back, so the second attempt is an `ask` and no host is locked out. A
plain deny must not return there: some hosts never satisfy the process
heuristics, and a deny on every switch in an environment is an outage, not a
cost. A wrong deny costs a prompt and a wrong allow breaks another session's
tree. Under the press those rows deny every attempt, on Windows every switch
without `[shared-tree-ok]`; their way on, a worktree per branch made with
`-b`, needs no switch and no person, which keeps that a cost.

### Which tree

The tree judged is the one the command acts on, by every row of *A*, the
tracked-changes row included. `git -C <path>` names it, and a `cd` earlier in
the command moves the shell to it. The whole command is read the way the
frozen reading reads it: which segments are git, the `-C` values each names,
and where every `cd` lands. **Nothing is read past the base's words**: a
segment's shape (*A*) is its subcommand and, for `checkout`, `worktree` and
`stash`, the one word that decides it, and no name is looked up in any tree.
The guard and the consent writer read the command through
`hooks/cmdline_base.py`, a byte-for-byte copy of an earlier
`hooks/cmdline.py` that `tests/test_the_frozen_reading_never_grows.py` pins,
and neither chooses a segment, a slot or a directory through
`hooks/cmdline.py`. The guard asks that module only what the frozen reading
does not read as git (a shell's string, an `eval`'s argument, a substitution
body, a git behind a redirection or a zsh precommand word, a group an `&` cut
apart), and each answer is an unrecognised shape. Where only that module
reads a git, the `-C` it reads is composed onto the directory the frozen walk
placed the segment in.

The guard takes one answer where a reader of every target would take all of
them: the first switch, the first creation, and the first directory in each that names a
tree. A wider reading finds more segments and more directories, and which came
first would then decide the tree; every order tried met a command where the
first was a segment or a directory bash never ran the switch in. The frozen
reading makes the guard's answer the base's by construction, at a stated cost
(*Known limits*): a `cd` with a redirection among its words does not move the
tree judged, and a git behind a redirection or a zsh precommand word is no git
to the frozen reading. Where `hooks/cmdline.py` fails to load, or a reader in
it raises, the bare word `git` in a string, a body, a hidden position, a
command that would not split or either side of an `&` the splitter cut is the
finding, so a broken reader costs a stop where the tree matters and never a
silence. Such a cut is judged in the tree the part before it names, and a
`-C` written after the cut is not read.
check: tests/test_worktree_guard.py tests/test_worktree_consent.py

The advice follows the same tree. A command a reason tells the person to run
(the worktree steer, a choice's option, the switch steer, the tracked-changes
note's `git restore`) carries `git -C <root>` where the shell is not in the
judged tree. The note's `git restore` commands carry it always, because their
paths are relative to the root.

Two kinds of destination fall back to the session's own directory: one that
cannot be computed (a variable, a glob, a subshell, `cd -` with nothing behind
it), and one that reads cleanly and holds no repository, since
`cd /no/such/dir ; git switch x` switches in the session's own tree. A
`git -C` naming no repository stays silent, because git refuses that command
itself.

**No git hook can judge a branch switch or a worktree creation before it
happens, so the guard's switch and creation arms read the command, and
that reading does not converge.** No git refuses a branch switch before its
tree has moved: on 2.34 to 2.43 a switch reaches `reference-transaction`
with no line at all, and on 2.50.1 the line arrives after the tree and index
already hold the new branch. A branch-naming rebase reaches
`reference-transaction` the same way. A worktree creation can be judged
only after git made it, in `post-checkout`, and only taken back there,
which *Decided before git runs* shows cannot undo all of it. This plugin
writes nothing into a clone's git hooks in any case
(`docs/the-routing-check.md`).
check: tests/test_the_hook_surface_git_offers.py tests/test_the_frozen_reading_never_grows.py

## Known limits

- **Neither a switch nor a creation is judged by git**, for the reasons
  *Which tree* gives, so *A* and *B* read the command's text on every git,
  through the frozen reading.
- A word the shell builds before git runs — a brace expansion, a
  substitution that spells `git`, a here-string or heredoc handed to a shell,
  a git spelled past the splitter (`g""it` in a line it cannot close) — is not
  read, so `git rebase {main,feature/x}`, `git rebase --ro{,} feature/x`, `git
  stash {branch,} y` and `git worktree {add,} ../wt f` are listed and silent in
  every tree, though bash makes the first three switch HEAD and the fourth add
  a worktree. A reader imitating bash's expansion was built and taken out,
  because each review found a spelling it missed.
  The braced rows of
  `Test_main::test_accepts_data_no_shell_runs_as_no_command` and the braced
  half of `Test_shape_of::test_accepts_no_listed_form_that_moves_head_under_git`
  in `tests/test_worktree_guard.py` pin the limit.
- A switch into the worktree the same command creates is judged against the
  session's own tree, because `../x` does not exist yet when the guard runs:
  `git worktree add ../x -b x && cd ../x && git switch y` meets that tree's
  switch verdict. `git -C ../x switch y` names no repository yet, so only the
  creation is judged.
- A switch whose tree the guard cannot place is judged against the session's
  own tree, and passes silently where that tree is clean and single-stream:
  each of `builtin cd w`, `command cd w`, `time cd w`, `pushd w`,
  `noglob cd w`, `cd "$W"` with `W` unset, and `2>&1 cd w`, before
  `&& git switch …`. Asking there instead was counted over the recorded runs
  and would have stopped 9 of 395 switches, so the fallback stays. Two more
  spellings reach it. One is `cd w 2>&1` before the switch: the frozen
  splitter cuts it at its `&`, so the walk keeps the directory before the
  `cd` first. The other is an unrecognised shape the walk cannot place: a cut
  git inside an `if` body after `cd w` (`cd w && if …; then 2>&1 git switch x;
  fi`) is judged in the session's own tree. `git -C <dir> switch …`, or a
  plain `cd <dir>` of its own, is the spelling the guard reads.
  `Test_main::test_a_switch_tree_the_guard_cannot_place_is_judged_as_its_own`
  in `tests/test_worktree_guard.py` pins it.
- `LEAVES_THE_TREE` holds the subcommands this repository's recorded runs
  hold, each with its count, and nothing guessed. A git subcommand this
  repository never ran (`git submodule update`, `git notes`) is unrecognised
  in every repository the plugin is installed in, so it stops in a tree that
  matters until a release adds its row; under the press the model cannot
  rewrite it, because it is its own plain spelling. The stop's reason names
  the list. One form of each row is run against git, and a listed form that
  moves HEAD fails
  `Test_shape_of::test_accepts_no_listed_form_that_moves_head_under_git`; a
  form no case runs is still a reading.
- A creation only a hidden spelling holds (`git 2>&1 worktree add …`, `git
  worktree 2>/dev/null add …`) is an unrecognised shape, so in a clean tree
  nobody else is in it says nothing and *B* never reads it. The consent writer
  files nothing for it either.
- A `rebase` is listed, and detaches HEAD while it runs: a session switching in
  the same tree during that window meets a detached HEAD. The guard judges the
  command before it runs and reads no window. A `rebase` naming a branch is
  unrecognised, and its words are read without an option table, so an
  option's value counts as a word: `git rebase --onto main x` stops too.
- A body (`$( … )`, a backtick pair, `<( … )`) and a command that would not
  split belong to no one segment, so each is judged in the session's own
  tree: `cd W && F=$(git checkout x)` with `W` dirty and the session's tree
  clean says nothing.
- A string handed to a shell (`sh -c`, `bash -c`, `eval`) is judged in the
  tree its segment names, the one it was typed from: its own `-C` and `cd` are
  not read, so `sh -c 'git -C W switch x'` with `W` dirty and the session's
  tree clean says nothing. Only a git the wider reading reads as a segment of
  its own has its `-C` composed.
- Where `hooks/cmdline.py` did not load, or the reader that glues an `&` cut
  back raises, a git the cut split is judged in the tree the part before the
  cut names: `git -C W worktree 2>&1 add …` in `W`, and `2>&1 git -C W switch
  x`, whose `-C` comes after the cut, in the tree it was typed from.
- The frozen splitter has taken the quotes off before a word is read, so a
  quoted `<` or `>` reads as a redirection: a path written `"> f"` after a
  `checkout`'s `--` is no path. The same splitter reads a redirection glued to
  the subcommand as the subcommand (`git status>/dev/null`), and a spaced
  `--config-env`'s value as the subcommand (`git --config-env k=v switch x`
  reads `k=v`), so each stops where the tree matters with a plain spelling
  that names the wrong word. None goes silent.
- On Windows the count of other sessions is always unusable, because Git for
  Windows' `ps` takes neither `-o` nor `-axo`, so every tree state there reads
  as detection unusable and takes that row of *A* and *B*. A second Bash
  creation in one session meets the confirmation where a POSIX system's
  single-stream row refuses it, and every unrecognised shape stops there, in
  every tree: a `deny` to the model under the press, an `ask` otherwise.
  Under the press every switch without `[shared-tree-ok]` is row 2's deny, and
  every Bash creation in a clone the press was not given in and this session
  holds no record in is *B*'s detection-unusable deny. Two Windows-only cases
  of `Test_main` in `tests/test_worktree_guard.py`,
  `test_on_windows_a_switch_under_the_press_is_row_twos_deny` and
  `test_on_windows_a_creation_in_another_clone_is_row_fours_deny`, measure
  the two.
- The `automation` press is this session's, on this machine. It is read from
  this session's own main transcript, which the harness writes where the
  session runs, and a subagent reaches it through its parent's id. A run
  resumed in a new session (a `/clear`, a new `claude` start, another
  machine) has no press until question 1 is put through `AskUserQuestion`
  again, and until then every stop that reads it is the person's `ask`
  (`skills/implement/orchestration.md` *Orchestrator: how the work is
  routed*). Nothing that survives a machine move can stand in for it: the
  consent record and the choice markers sit under the git directory, which
  does not travel, and what travels is in the tree, which the model writes.
  `claude --resume` and compaction go on writing the same transcript, so the
  press survives them. That a `/clear` or a new `claude` start issues a new
  session id is not observed by any case. The entry shape the reader requires
  (`toolUseResult` with `questions` and `answers`, and a top-level `cwd`) and
  the transcript's place were read from one harness on one machine, and a
  harness that moves either leaves the press unread, so the guard asks.
  Whether a subagent's payload carries its parent's `transcript_path` or its
  own is not observed; either reaches the parent's file through the glob.
- Under the press a model that does not take the way a deny names may
  re-issue the command, on the choice rows or the tracked-changes row,
  bounded by the reason's text alone. What it does next, a stash it never pops
  or a commit on a detached HEAD, is the model's: the guard reads no later
  command.
- No case runs the switch arm against a live concurrent session; the cases
  stub the session count.
- Every count this document gives, the switches the fallback would have
  stopped and the six creations, is over this repository's recorded runs on
  the maintainer's machine. Another person's sessions are not measured.
- No case observes whether an Agent or Task spawn with
  `isolation: "worktree"` runs `git worktree add`. No git hook judges a
  creation, so the answer moves no verdict, and the PreToolUse arm reads
  `tool_input.isolation`, not a command.
- Transcript activity is per project, not per process: one working session
  marks every session of that project active, which errs conservative.
- tty atime also refreshes on in-turn stdin reads, not only keystrokes, which
  is why the prompt labels it terminal input and output; either cause means
  the session is live.
