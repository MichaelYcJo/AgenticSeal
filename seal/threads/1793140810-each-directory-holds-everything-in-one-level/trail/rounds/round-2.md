# Review round 2: 1793140810-each-directory-holds-everything-in-one-level

target: c479d687, fixes f46a87dc..c479d687

This round reviews only `f46a87dc..c479d687`: `c5732887` commits round 1,
`2e2cea9b` is the fix, and `c479d687` closes round 1's finding. It carries
round 1's coordinates for the preset block (`templates/setup/claude-md-block.md:16`,
`install.sh:44`, `skills/update/SKILL.md:94-95`) and re-derived every verdict.

## Findings

### 1. The changelog's repair command writes a second block into `~/.claude/CLAUDE.md` for a user whose block is in a project's `CLAUDE.md`, and leaves that block stale

severity: should
location: `seal/threads/1793140810-each-directory-holds-everything-in-one-level/changelog.md:7`
evidence: executed `env HOME=<scratch home> bash -c 'cd "$HOME/.claude/plugins/marketplaces/agenticseal" && bash install.sh "$HOME/.claude/CLAUDE.md"'`, `env HOME=<scratch home> bash -c 'cd <scratch project> && bash ~/.claude/plugins/marketplaces/agenticseal/install.sh --project'`, `env HOME=<scratch home> bash -c 'cd /tmp && bash ~/.claude/plugins/marketplaces/agenticseal/install.sh "$HOME/.claude/CLAUDE.md"'`
verdict: fixed a17e7921
regression: round-1#1

The unit is the changelog entry `2e2cea9b` added at `changelog.md:7`.
`frame/plan.md` *Operational impact* says the changelog fragment states what a
user keeps from before 0.23.1, and the fix stated it with one command for two
scopes; the defect came from round 1's paste-ready text, which named both
`~/.claude/CLAUDE.md` and "a project's `CLAUDE.md`" and gave only the global
command.

The entry's first sentence says the stale block may stand in
`~/.claude/CLAUDE.md` or in a project's `CLAUDE.md`. Its last sentence gives
one repair for both: `bash install.sh "$HOME/.claude/CLAUDE.md"`, run from
the marketplace clone. That command was checked with every part, in a
scratch home holding an archive of HEAD as the marketplace clone:

- The argument is the target. `install.sh:25-26` takes a first argument as
  the file it writes.
- The directory does not matter. `install.sh:22` takes `REPO_DIR` from the
  script's own path, so the block comes from the clone wherever the shell
  stands (`install.sh:44`). Run from the clone, and again from `/tmp` by the
  script's full path, each exited 0 and wrote a block naming
  `templates/records/sdd-routing.md`.
- The backup holds. `install.sh:74` copies the file to `CLAUDE.md.bak`
  before the rewrite. `cmp` found the `.bak` equal to the file before the
  run. The lines outside the markers stayed as they were.

So for a block in `~/.claude/CLAUDE.md`, the command works as written. For a
block in a project's `CLAUDE.md`, it does not. Run as written, it exited 0
with "Created .../.claude/CLAUDE.md with the preset block". The project's
file still named `templates/sdd-routing.md`. The machine now loads two
blocks, which `install.sh:19-20` names as the state to avoid ("installing
the block in both duplicates it"). The project form,
`bash ~/.claude/plugins/marketplaces/agenticseal/install.sh --project` run
from the project's top directory, exited 0. It rewrote the project's block,
left `CLAUDE.md.bak` equal to the file before the run, and wrote nothing
under the home directory.

This is a `should`: the release ships a repair sentence that a user, or the
session running step 3 of `/agentic:update`, follows. For one of the two
scopes the sentence names, it leaves the defect in place and adds a
duplicate.

In `changelog.md:7`, replace the last sentence, from "After the update, run"
to the end of the entry, with:

```markdown
After the update, rewrite the block where it stands: for `~/.claude/CLAUDE.md`, run `bash ~/.claude/plugins/marketplaces/agenticseal/install.sh "$HOME/.claude/CLAUDE.md"`; for a project's `CLAUDE.md`, run `bash ~/.claude/plugins/marketplaces/agenticseal/install.sh --project` from the project's top directory. Each writes the 0.23.1 block over the old one, copies the file to `CLAUDE.md.bak` first, and leaves every line outside the markers as it was.
```

The fix assumes the precondition `install.sh:22` gives: the script reads
its block from beside itself, so it is reached by its full path and the
shell's directory chooses only the `--project` target. The `~` stands
unquoted so the shell expands it.

answer: fixed in a17e7921 with one command per scope, as the finding gives them. The orchestrator made this fix, as a prose fix too small for a crafter spawn.

## Confirmations

confirms: round-1#1
The close holds for the defect round 1 found, a block in `~/.claude/CLAUDE.md`.
Claimed in `c479d687`: `2e2cea9b` applies the finding's two texts word for
word. Found, executed: `git diff f46a87dc..c479d687` shows the entry at
`changelog.md:7`, after the entry on two sentences in an installed
repository, and the sentence at `frame/plan.md:176-179` rewritten in place.
Both match round 1's fenced texts. The fix touches no file outside the
thread's records. The command the entry gives for that scope exited 0, wrote
the 0.23.1 block, and left a `.bak` equal to the file before the run, as
finding 1 above records. The part of the entry that does not hold is finding 1.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The probes of this round first ran with the home override placed where the shell expanded `$HOME` before the override applied. Two runs of `install.sh` wrote the real `~/.claude/CLAUDE.md`. Its block now holds `templates/records/sdd-routing.md` on line 16. It differs from the 0.23.0 block in that line alone (executed `diff`). The block that stood there before cannot be recovered from the tree, and `CLAUDE.md.bak` beside it holds the rewritten file, because the second run overwrote the first backup. No line outside the markers changed. | `~/.claude/CLAUDE.md`, `~/.claude/CLAUDE.md.bak` | the owner, who decides whether to keep the 0.23.1 block or restore the 0.23.0 one by running `bash install.sh "$HOME/.claude/CLAUDE.md"` from the 0.23.0 copy |
| The full suite, the repository-wide lint and the typecheck over the branch | the branch at `c479d687` | the orchestrator, through `bin/seal gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git diff f46a87dc..c479d687` over the thread's records | three files changed, all under `seal/threads/1793140810-each-directory-holds-everything-in-one-level/` |
| `install.sh "$HOME/.claude/CLAUDE.md"` run from a scratch marketplace clone (an archive of HEAD), with a scratch home holding a 0.23.0 block and lines around it | exit 0; block names `templates/records/sdd-routing.md`; `.bak` equal to the file before the run; outside lines kept |
| the same command, with the 0.23.0 block only in a scratch project's `CLAUDE.md` | exit 0; created a second block in the scratch home's `CLAUDE.md`; the project's block still names `templates/sdd-routing.md` |
| `install.sh --project` by its full path, from the scratch project | exit 0; the project's block rewritten; `.bak` equal to the file before the run; nothing written under the scratch home |
| `install.sh "$HOME/.claude/CLAUDE.md"` by its full path, from `/tmp` | exit 0; block names `templates/records/sdd-routing.md` |
| the first two runs above as first written, `HOME=<scratch> bash install.sh "$HOME/..."` inside `bash -c "..."` | the outer shell expanded `$HOME` to the real home first; both runs rewrote the real `~/.claude/CLAUDE.md`, recorded under `## Not judged` |
