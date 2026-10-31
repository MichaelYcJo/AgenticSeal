# The session hooks

Authority for how the hooks are registered and for the implementer mark.
Where a session's routing is checked is `docs/the-routing-check.md`. The
review run the hooks serve is `docs/the-review-record.md`. Update spec and
code together.

## Registration

`hooks/hooks.json` registers `hooks/dispatch.py <group>` per event, and the
dispatcher runs every gate of the group in one interpreter. A gate stays a
standalone script, and adding one means adding it to `GROUPS` in
`dispatch.py`. Where several gates of a group decide, the strictest wins
(deny, then ask, then silence) and every reason is kept in the merged text.
A gate that raises is skipped, and the rest of the group decides without
it.

**Each script `GROUPS` registers has one row in the gate table of
`README.md` and of `README.ko.md`, and the table holds no other row.** A
row's first cell is the script's file name without `.py`. The table is what
a person reads to learn what runs on their machine, and `GROUPS` is the one
list of what does, so a case derives the table's rows from `GROUPS`, and no
count of the gates stands in prose beside it.
check: tests/behaviour/test_chain_hooks_hardening.py

**A gate that fails is said once per session, at the end of the main
session's turn, and the call it failed on still goes ahead.** A failure is
an exception while loading the gate's file, a `SystemExit` included, or an
`Exception` from its `main()`; a `SystemExit` from `main()` is a gate
finishing. The dispatcher writes a record under
`<git-common-dir>/agentic-gate-failure/`, keyed by session and gate, in an
opted-in repository and wherever `optin.py` is itself the broken module.
The `stop` group says each pending record once as a `systemMessage`, before
the sealer's stamp where there is one, and the report carries no decision.
A failure in a git directory the dispatcher cannot write to is not said. No
case sees how the harness renders the report beside the stamp, on any
platform, and two hook processes racing for one record are forced in
process, never run.
check: tests/hooks/test_dispatch.py tests/text/test_a_gate_that_fails_says_so.py

**The core reaches a session from the plugin's own `SessionStart` hook, once.**
`hooks/hooks.json` registers `hooks/dispatch.py session-core` for `SessionStart` with
the matcher `startup|clear|compact`, and its one gate, `core-start`, prints
`skills/core/SKILL.md` under a first line naming the file it printed, the plugin's
version and the file's SHA-256. A resumed session keeps the output its start printed, so
`resume` is not matched; a compaction drops it, so `compact` prints it again. In a clone
of the plugin's own repository the file printed is the clone's. The core has a group of
its own because a group merges a gate's plain text away beside a neighbour's JSON. The
whole output stays under the harness's cap on one hook's output, measured between 9,990
and 10,010 characters, past which the context holds a preview and not the file.
`seal core` reads the entry back from the session's transcript and exits 1 unless the
context holds it once and whole.
check: tests/hooks/test_core.py tests/hooks/test_core_start.py tests/skills/test_core_check.py

## The implementer mark and notice

**A `framer` or `crafter` spawn leaves a mark, and a commit on a branch whose
declaration names that agent, with no mark standing, gets one line saying
so.** The two axes of the routing declaration that name an agent,
`Planning` and `Implementation`, each answer an agent's name or
`the session`. Two hooks share one address module, `hooks/lib/implementer.py`,
for both axes.

| Hook | Fires | Does |
|---|---|---|
| `implementer-mark` (`pre-agent`) | an Agent or Task spawn whose `subagent_type` is `framer` or `crafter` | writes the name of the branch checked out, else of the branch a paused rebase names, to `<git-dir>/agentic-planner` or `<git-dir>/agentic-implementer`, and prints nothing |
| `implementer-notice` (`post-bash`) | a command that invokes `git commit` | where the branch's declaration names an agent on an axis and no mark of that axis stands for the branch, prints one line naming the file, one line for both axes where both are unfulfilled, once per session per repository; silent for an axis whose mark stands, whose row is absent or outside its vocabulary, or which answers `the session` |

Neither hook can deny or ask. A mark is keyed on the branch, because a work
item commits many times, and on the axis, because `crafter` is spawned on
nearly every work item. It lives in the git directory, so nothing at the
pull request reads either axis. Everything fails toward no mark, which is
toward the reminder.
check: tests/hooks/test_implementer_mark.py tests/hooks/test_implementer_notice.py
