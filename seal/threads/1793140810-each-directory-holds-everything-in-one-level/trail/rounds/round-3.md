# Review round 3: 1793140810-each-directory-holds-everything-in-one-level

target: 4f7764b3, fixes c479d687..4f7764b3

This round reviews only `c479d687..4f7764b3`. In that range, `3889f13d`
commits round 2, `a17e7921` is the fix, and `4f7764b3` closes round 2's
finding. It carries round 2's runs of the two commands as executed facts
and re-ran neither. The orchestrator ruled out any command that can write
under the real home directory. The script's behaviour is read from
`install.sh`.

## Findings

None.

## Confirmations

confirms: round-2#1
The close holds. Claimed in `4f7764b3`: `a17e7921` gives one command for
each scope. Found, executed (`git diff c479d687..4f7764b3`): the fix changes
only the entry at `seal/threads/1793140810-each-directory-holds-everything-in-one-level/changelog.md:7`,
and round 2's `verdict:` and `answer:` lines. The entry now names
`bash ~/.claude/plugins/marketplaces/agenticseal/install.sh "$HOME/.claude/CLAUDE.md"`
for the block in `~/.claude/CLAUDE.md`. For a block in a project's
`CLAUDE.md`, it names `bash ~/.claude/plugins/marketplaces/agenticseal/install.sh --project`,
run from the project's top directory.

Each command is the form round 2 executed in a scratch home and recorded in
its `## Probes`. The by-path global form exited 0 from `/tmp`, and its block
named `templates/records/sdd-routing.md`. The `--project` form exited 0 from
the scratch project. It rewrote that project's block, left `CLAUDE.md.bak`
equal to the file before the run, and wrote nothing under the home.

Read: `install.sh:22` takes the block's source from the script's own
directory, so the full path reaches the 0.23.1 block from any directory.
`install.sh:23-24` sets the target to `$(pwd)/CLAUDE.md` for `--project`, so
the project's top directory is the right place to run it. `install.sh:25-26`
takes the quoted argument as the target. `install.sh:74` copies the file to
`CLAUDE.md.bak` before the rewrite, which is the entry's "backs the file up
first". The `~` stands unquoted, so the shell expands it. No command in the
entry writes the scope it does not name.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the owner's `~/.claude/CLAUDE.md`, which round 2's first probes rewrote and the orchestrator restored, now holds the block the owner wants; this round read only its size and time with `stat` and wrote nothing there | `~/.claude/CLAUDE.md` | the owner |
| The full suite, the repository-wide lint and the typecheck over the branch | the branch at `4f7764b3` | the orchestrator, through `bin/seal gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git diff c479d687..4f7764b3` | two files changed under the thread: `changelog.md` one line, `trail/rounds/round-2.md` its committed record and its two closing lines |
| `stat` of `~/.claude/CLAUDE.md` and `~/.claude/CLAUDE.md.bak`, before writing this record and after the censuses ran | the same size and time both times; this round wrote nothing under the home directory |
