# The routing check

Authority for where a session's routing is checked: at the pull request.
What each routing answer owes there is
`docs/running/the-review-and-parity-arms.md`. Update spec and code together.

**A session's routing is checked at the pull request alone, and this plugin
writes nothing into a clone's git hooks.** The routing governs a session,
and git's hooks run for every commit made in the clone, a person's own from
a terminal included. The hooks slot is also where husky, the pre-commit
framework and lefthook live, and a line or an entry in their committed
configuration reaches every teammate. A check at git's level reaches people
who do not use this plugin, with an experience they did not ask for. The
declaration is written before the first edit because the orchestrator
writes and commits `routing.md` before it edits anything else
(`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket*), and no check stands between a session and its first edit.
check: tests/behaviour/test_chain_hooks_hardening.py

**A session that declares nothing is not caught, in shared mode as in
local.** A session that never opened `skills/implement/orchestration.md`
edits and commits as it would without the plugin. At a shared root its
commits carry no `Seal-Routing` trailer, so *At the pull request* below
judges none of them;
at a local root no declaration is committed for anything to read. That is a
limit, and no mechanism is kept against it: what the pull request's check
judges is a work item that was declared.

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
