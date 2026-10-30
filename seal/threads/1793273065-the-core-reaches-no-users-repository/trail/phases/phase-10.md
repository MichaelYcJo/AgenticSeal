# Phase 10: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Phase | 10 |
| Commit | 3f458f83 |

## What this phase was asked

Phase 10 of `frame/plan.md`, with `frame/design.md` *Scope* item 7 and
scenario S10. `changelog.md` was to be rewritten. Its `### Fixed` entry was
to say six things: how the core reaches every session and every agent; how
to see it (`! seal core`); that `/memory` no longer lists it; how to turn it
off; that the preset block, `install.sh`, `uninstall.sh` and
`/agentic:preset-setup` are gone; and that `/agentic:update` empties the old
block on the way to 0.25.0 and takes it out at the next update. Its
`### Process changes` row was to be rewritten. `gaps.md` *Not done* was to
lose the double read. `frame/questions.md` Q2 and Q3 were to stand under
*Not verified*. The handoff named three more places in `gaps.md` that still
described A1: the *Not verified* row for `/agentic:preset-setup`, the
*Why this work exists* line, and *Not done*. The fragment was to be read
against S10. The pull request body's `Closes #1183` is the orchestrator's,
written through `seal pr-body` after the rounds, so this phase wrote no
body.

## What this phase found

**The frame held.** The fragment and `gaps.md` stood as the handoff
described them, and `frame/design.md` *Data & interfaces* gives the process
row's date, change, why and source. The row is that text, opening with a
capital letter as the earlier row did.

**The fragment read against S10 holds, and the reading added one clause.**
S10 asks that the fragment say how the core arrives, how to see it and how
to turn it off, and end with its process table. The entry says that every
agent receives the core through `skills:`, and every session from the
plugin's `SessionStart` hook at a start, a `/clear` and a compaction. It
names `! seal core` as the way to see it, and says that disabling the
plugin's hooks turns it off. The process table is the last section. The
reading found one gap a user would act on: disabling the plugin's hooks
turns off every hook the plugin runs, not only the core's. The fragment now
says so. `README.md:45` and `README.ko.md:45` gave the same instruction
with the same gap, and each now says it in `3f458f83`. *Scope* item 7's
other three points are in the entry: `/memory`, the four retired files and
commands, and what `/agentic:update` does in two steps. The entry also says
that an update names a project `CLAUDE.md` holding a block and does not
edit it, as `skills/update/SKILL.md` step 4 does. It gives the hook's
output as about 1,950 tokens. That is phase 9's 6,226 B at the assumed 3.2
B/token; the exact bytes stay in `trail/phases/phase-9.md`, as the
issue's comment of 2026-10-29 asks.

**The fragment splits as the release note reads it.**
`publish_release_note.py#split_process`, run over the fragment with
`process_shape()`'s heading, returned one process row and left a body that
opens with `### Fixed` and holds no other `###` heading (`python3 -c`,
exit 0). No case in the suite reads this work item's fragment:
`tests/github/test_publish_release_note.py` builds its own fragments in a
scratch repository.

**Every place in `gaps.md` that stated A1, found by reading the file
whole.**

- *Why this work exists* said the preset block imports the core. It now
  says the plugin's `SessionStart` hook prints it into every session.
- *Not done* held the double read. Phase 9 left one thing within reach and
  not taken, a session delta under `seal payload --baseline`, and *Not
  done* now holds that alone.
- The `/agentic:preset-setup` row of *Not verified* was marked `closed`,
  with what closed it: `3a24c9c0` deleted `skills/preset-setup/`
  (`git show --stat`, read). It was not deleted, because
  `skills/implement/SKILL.md` *4. The closing memo* closes an item by
  marking it.
- The Q2 row asked whether the one-line block puts the core in a session.
  It now states Q2 as `frame/questions.md` asks it, for the hook, `seal
  core` and the emptied marker pair, with the owner as its answerer. The Q3
  row is new, with the answerer Q3 names. `seal unverified` read the file
  as one closing memo, 5 open and 1 closed (exit 0).
- Two divergence rows from phase 2 chose defaults and an option refusal
  for `uninstall.sh` and `install.sh`. They stay as the record of what was
  decided, and each now ends by saying that phase 7 deleted the script.
- The other divergence rows name the block's cases, `.gitignore` and the
  core's prose. Each describes a file that still stands, so none changed.

**No case was added.** The phase changed prose only: the fragment, the
closing memo and two README cells. Per `skills/verify/SKILL.md` *The narrow
command still has to be able to fail*, what can fail there is whatever
parses those files, so no `seal mutate` run is owed.

**The phase-boundary sets passed.** At `2a47cb82`, one `bin/test -q`
command ran 66 modules: `tests/github/test_publish_release_note.py`,
`tests/behaviour/test_release_hygiene.py`, and every test module that names
`seal/threads`, a changelog, `gaps.md`, `trail/phases`, `plan.md`, *Not
verified* or `unverified_check`. It passed 4,233 cases and skipped 11 (exit
0). At `3f458f83`, after the README cells changed, one command ran 48
modules: the same two and every test module that names a README. It passed
2,612 and skipped 1 (exit 0).
