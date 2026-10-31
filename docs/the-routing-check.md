# The routing check

Authority for where a session's routing is checked: at its edit tools,
before the first edit, and at the pull request. What each routing answer
owes at the pull request is `docs/the-review-and-parity-arms.md`. How the
hooks are registered is `docs/the-session-hooks.md`. Update spec and code
together.

**A session's routing is checked where the session acts, at its edit tools
before the first edit, and again at the pull request; this plugin writes
nothing into a clone's git hooks.** The routing governs a session, and
git's hooks run for every commit made in the clone, a person's own from a
terminal included. The hooks slot is also where husky, the pre-commit
framework and lefthook live, and a line or an entry in their committed
configuration reaches every teammate. A check at git's level reaches people
who do not use this plugin, with an experience they did not ask for (the
owner, 2026-10-25).
check: tests/hooks/test_routing_edit_gate.py tests/hooks/test_dispatch.py

## The edit check

**`hooks/routing-edit-gate.py` refuses a `Write`, `Edit` or `NotebookEdit`
of a file in an opted-in repository's worktree while no routing declaration
names the branch checked out there and the session has not recorded that
its change belongs to no work item.** The repository and the branch are the
edited file's: its path is resolved to a worktree, never the payload's
`cwd`, because a session can edit a tree its working directory is not in. A
detached HEAD names no branch, with two exceptions. During a paused rebase
the branch the rebase names stands for it. And a detached HEAD whose commit
a branch some declaration names already holds, under `refs/heads/<branch>`
or a remote-tracking `refs/remotes/<remote>/<branch>`, is allowed, because
commits made there reach a pull request only through a branch, which this
gate and the trailer arm judge. The tool input is a path, so no command is
read. Every way the declaration cannot be read is no declaration, as
`docs/the-review-and-parity-arms.md` states.
check: tests/hooks/test_routing_edit_gate.py

**Three kinds of file are not judged: one under the repository's `seal/`
root, one git ignores, and one outside every opted-in repository.** The
root holds the routing record and the records that follow it, so writing
the declaration is never refused for the want of one. An ignored file never
lands in a commit. Anything else belongs to nothing this plugin governs.
check: tests/hooks/test_routing_edit_gate.py

**A change that belongs to no work item is recorded per session and per
branch by `seal no-work-item`, and the record lets that session edit on that
branch only.** It is `<git-common-dir>/agentic-no-work-item/<session-id>`,
one line per branch, the session read from `CLAUDE_CODE_SESSION_ID` and the
branch from the worktree it ran in: the branch checked out there, or the
branch a paused rebase there names. A run on a second branch adds a line.
On a detached HEAD outside a paused rebase no branch is named, so nothing
is recorded and `seal no-work-item` exits 1. The session's edits on a
branch its record does not name are judged as if it had no record, so a
session that recorded a change of no work item and then starts a work item
on a new branch meets the refusal there. Nothing verifies who ran it: the
record is an audit trail, in the transcript and, at a shared root, in each
commit's trailer at the pull request, not an authorization. A record that
cannot be read is no record.
check: tests/hooks/test_routing_edit_gate.py tests/skills/test_seal.py

**A refusal is a deny addressed to the model, with the same text every
time.** It names the declaration to write, at the path `routing.md` takes
under the repository's root, and `seal no-work-item`. Where HEAD is
detached, its ways on start by checking out a branch, and they name
`seal no-work-item` only as a run on that branch, because on a detached
HEAD it records nothing. Where the person pressed `automation` on the
routing question, read through `hooks/lib/press.py#automation_answered`, it
names no question tool; otherwise it tells the model to put the routing
question to the person with `AskUserQuestion`. Re-issuing the edit
unchanged meets the same refusal.
check: tests/hooks/test_routing_edit_gate.py

**The check reaches a subagent's edits as it reaches the main session's,
and an edit made through the shell reaches neither.** A subagent's tool
call runs the same hooks and carries the main session's id. A shell write
calls no edit tool, which is why every agent edits through the `Edit` tool
(`skills/agent-contract/SKILL.md` rule 9), and at a shared root the pull
request's trailer arm, as *At the pull request* below states, is what
remains for such a change.
check: none reader: the orchestrator on the first live run after a change here

**The `automation` press is the person's own click on the routing question,
read from the session's main transcript, and nothing the model writes
stands in for it.** `hooks/lib/press.py` is its one reader, and the edit
check and `hooks/question-gate.py` both ask it. The transcript is the
payload's `transcript_path` where its file name is the session id followed
by `.jsonl`, and otherwise the one file of that name under
`~/.claude/projects/`, so a subagent reaches its parent's answer; no other
session's file and no `subagents/` file is read. The answer is read only
from a harness-written `AskUserQuestion` result: a `user` entry that names
an earlier `AskUserQuestion` call by `tool_use_id`, carries `isSidechain`
set to `false`, and holds a structured `toolUseResult`. The routing
question is the one single-select question whose three options lead with
`automation`, `per axis` and `no work item`, a label's lead being its text
folded to lower case and cut where a space is followed by an opening
parenthesis, an em dash or a hyphen. The answer counts only where it equals
one of the option labels exactly, so a typed answer is not read. The result
entry's own `cwd` must lie in the same clone as the repository the gate
judges. Of every answer to the routing question from that clone, the latest
stands, so a later `per axis` or `no work item` takes the press back. A
`routing.md` is never read for it, and every way a read fails is no press.
A run resumed in a new session, by `/clear`, a new `claude` start or another
machine, has no press until question 1 is put again; `claude --resume` and
compaction keep the transcript, so the press survives them.
check: tests/hooks/test_press.py tests/hooks/test_question_gate.py

## At the pull request

**A session's commit in a repository whose root is shared ends with one
trailer, `Seal-Routing:`, naming its work item or reading
`no work item`; at a local root a commit carries none.** It tells a
session's commit from a person's: the harness's co-author trailer is
carried by any Claude Code session, a teammate's who does not use this
plugin included, and a person's own commit carries neither. At a local root
no declaration is ever committed for a trailer to name, and the history
belongs to a team that does not run this plugin.
`skills/commit-pr-convention/SKILL.md` is where a session reads it.
check: skills/commit-pr-convention/SKILL.md

**At a shared root, `chain-check` fails a ready pull request where one of
its own commits, committed by its author, carries a `Seal-Routing`
trailer naming a work item that no declaration it judges names, and prints
each commit whose trailer reads `no work item`.** A commit with no such
trailer is not judged, so a teammate's never is, and neither is a
session's that dropped the trailer: that is what judging no teammate costs.
A commit whose committer email differs from its author email, compared
case-folded, is not judged either, because its committer did not write the
trailer: GitHub's squash is one such commit, and a person's cherry-pick or
rebase under another identity is another. The cost is that a person's
cherry-pick of their own session's commit under the same identity is still
judged. At a local root a work item's trailer is printed as a notice and
never refused. The commits are the pull request's own, merges left out, and
the trailer is read by git's own trailer parser.
check: routing-trailer-at-the-pull-request
