# The session hooks

Authority for how the hooks are registered. Where a session's routing is
checked is `docs/checks/the-routing-check.md`. The review run the hooks
serve is `docs/running/the-run.md`. Update spec and code together.

## Registration

`hooks/hooks.json` registers `hooks/dispatch.py <group>` per event, and the
dispatcher runs every gate of the group in one interpreter. A gate stays a
standalone script, and adding one means adding it to `GROUPS` in
`dispatch.py`.
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
check: tests/hooks/test_dispatch.py

**A `PreToolUse` group passes on `deny` and `ask` alone, so no gate's
output can approve a call or change its input.** Where several gates
decide, the stricter of the two wins, and every reason is kept in the
merged text. A gate's `allow`, or any other decision, counts as no
decision, and its reason is kept as the gate's text. A gate's JSON
without a decision reaches Claude Code without its `updatedInput`, and
without a top-level `decision` other than `block`, which are the two
fields of it Claude Code reads as an input change or an approval. The plugin
directory holds back a plugin whose hook can approve a call or change its
input, and no gate here needs to do either: a gate that has nothing to
refuse prints nothing, and Claude Code's own permission flow decides.
check: tests/hooks/test_dispatch.py
