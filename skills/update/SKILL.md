---
name: update
description: Update the plugin to the newest release and say what changed. Runs both commands in the right order, then names the entries the user is getting.
disable-model-invocation: true
---

# /agentic:update, take the release and see what is in it

The user runs this command; the session running it follows the procedure
below and reports to the user. Two commands run in a fixed order, and neither
of them says what the user is getting: run by hand they answer "you are now
on <version>", which is a number, not a reason to reload or restart.

## Procedure

**1. Record what is running.** Read the `version` from
`$CLAUDE_PLUGIN_ROOT/.claude-plugin/plugin.json`. This is the version this
session actually loaded, which is the one the user is comparing against.

**2. Refresh the marketplace, then install.**

```bash
claude plugin marketplace update agenticseal
claude plugin update agentic@agenticseal
```

Both, in that order. The first pulls the marketplace clone; the second
installs from it. Run alone, the second reports *already at the latest
version* against whatever the clone last knew: the failure is silent and
looks like success.

If the second command reports it is already current, say so and stop. Nothing
arrived, so there is nothing to load and neither move below is needed.

**2b. Read the installed copy before believing the installer.** The install
path is keyed by the version string, and extraction is skipped when a
directory by that name already exists. So on a machine that had one from an
earlier numbering, the installer reports success, writes the right commit
SHA beside it, and the copy that loads is whatever was already there. The
summary in step 3 cannot see that, because it reads the published release
notes, which are correct; it is the installed copy that is stale. Read the
one path the installer records, then the `version` of the
`.claude-plugin/plugin.json` in it, and compare:

```bash
p=$(python3 -c "import json,os;d=json.load(open(os.path.expanduser('~/.claude/plugins/installed_plugins.json'),encoding='utf-8'));print(d['plugins']['agentic@agenticseal'][0]['installPath'])")
python3 -c "import json,sys;print(json.load(open(sys.argv[1]+'/.claude-plugin/plugin.json',encoding='utf-8'))['version'])" "$p"   # must be the version step 2 reported
```

| Result | What happens |
|---|---|
| the `version` is the one the installer reported | go on to step 3 |
| a mismatch | **stop before step 3.** The update did not land. Say so, name both versions (the one the installer reported and the one the installed `plugin.json` names), and print the repair below for the user to type. Give no summary: a summary of what the user should be getting is exactly what makes this failure invisible |

The repair replaces the stale directory from the marketplace clone, and it is
the user's to type rather than this procedure's to run, because it deletes a
directory a session may be holding:

```bash
mv "$p" "$p.stale.bak"
rsync -a --exclude '.git' ~/.claude/plugins/marketplaces/agenticseal/ "$p/"
mkdir -p "$p/.in_use"
```

Two cautions. `.in_use/` under a version directory holds PID files, because a
running session pins its own version, so a directory whose `.in_use/` names a
live PID is never deleted; the `mv` above leaves the stale copy in place under
another name for that reason. And `installed_plugins.json` names exactly one
`installPath`: deleting that directory breaks the install, while any other
version directory is free to remove.

**3. Name what changed.** Each release's notes are its GitHub Release, the
note published at its `vX.Y.Z` tag. Read them from GitHub's public API, with
no token: `gh` is not used, because it needs a login. The repository is the
one the refreshed marketplace clone was cloned from, its `origin`. The list
holds every release's whole note, close to a megabyte, so it goes to a file
and only the span is printed. Set `old` to the version step 1 recorded and
`new` to the one step 2 reported, then run:

```bash
repo=$(git -C ~/.claude/plugins/marketplaces/agenticseal remote get-url origin | sed -E 's#^.*github\.com[:/]##; s#\.git$##')
f=$(mktemp)
curl -fsS "https://api.github.com/repos/$repo/releases?per_page=100" -o "$f"; echo "curl exit $?"
python3 -c '
import json, sys

def key(name):
    try:
        return tuple(int(n) for n in name.lstrip("v").split("."))
    except ValueError:
        return None

old, new = key(sys.argv[2]), key(sys.argv[3])
with open(sys.argv[1], encoding="utf-8") as handle:
    releases = json.load(handle)
for release in reversed(releases):
    at = key(release["tag_name"])
    if at and old < at <= new:
        print("## " + release["tag_name"])
        print(release["body"])
' "$f" "$old" "$new"
rm -f "$f"
```

It prints the `body` of every release after the old version up to the new
one, oldest first, each under its tag. Summarize every entry in them. Lead
each with what it changes for the user, not with the release number.

Where `curl` exits non-zero, or the list holds no release in that span, say
that what changed could not be read, name the releases page,
`https://github.com/<repo>/releases` with `<repo>` as read above, and go on
to step 4. The update has already landed, so nothing here stops it.

Two kinds get a line of their own, because a user who skips them is
surprised later:

- **behavior that changes without being asked for**: a new gate, a gate that
  fires where it did not, anything that writes to the user's tree;
- **anything the user has to do**: a path that moved, a setting that was
  renamed, a compatibility fallback with an expiry.

**4. Take out the preset block.** Earlier releases wrote a preset block
into the user's `CLAUDE.md`, between `<!-- agentic:start -->` and
`<!-- agentic:end -->`, or between the older `<!-- specseal:start -->` and
`<!-- specseal:end -->`. The core now reaches every session from the
plugin's own `SessionStart` hook, and the rules an older block stated stand
in the skills and definitions the plugin installs, so the block carries
nothing a session needs. `claude plugin update` never opens `CLAUDE.md`, so
without this step the block stays. Everything between the markers was
written by the plugin and everything outside them is the user's, so taking
the region out cannot touch a line the user wrote. No question is asked.

The command below backs the file up to `CLAUDE.md.bak` and takes each marker
region out with its markers, in the `CLAUDE.md` the harness reads as the
user's. It then looks for a marker in the current repository's `CLAUDE.md`,
which it never edits:

```bash
python3 -c '
import os, shutil, subprocess, sys

PAIRS = (
    ("<!-- agentic:start -->", "<!-- agentic:end -->"),
    ("<!-- specseal:start -->", "<!-- specseal:end -->"),
)


def text_of(path):
    if not os.path.isfile(path):
        return ""
    with open(path, encoding="utf-8", newline="") as handle:
        return handle.read()


def holds_a_block(text):
    return any(start in text for start, _ in PAIRS)


def without_blocks(text):
    kept, inside = [], None
    for line in text.splitlines(keepends=True):
        if inside is None:
            inside = next((end for start, end in PAIRS if start in line), None)
            if inside is None:
                kept.append(line)
        elif inside in line:
            inside = None
    return None if inside else "".join(kept)


user = sys.argv[1]
text = text_of(user)
if holds_a_block(text):
    after = without_blocks(text)
    if after is None:
        print(user + " holds a start marker with no end marker after it, so nothing was changed")
        sys.exit(1)
    shutil.copyfile(user, user + ".bak")
    with open(user, "w", encoding="utf-8", newline="") as handle:
        handle.write(after)
    print("took the preset block out of " + user + ", backed up to " + user + ".bak")
try:
    top = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, encoding="utf-8",
    ).stdout.strip()
except OSError:
    top = ""
project = os.path.join(top, "CLAUDE.md") if top else ""
if project and holds_a_block(text_of(project)):
    print("needs action: " + project + " holds a preset block, the committed text of this repository, so it was not edited")
' "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md"
```

| Output | What happens |
|---|---|
| nothing | no block stood; nothing is said |
| `took the preset block out of <file>, backed up to <file>.bak` | say so, with the two facts this step opens with: where the core now comes from, and where the rules an older block stated stand |
| `<file> holds a start marker with no end marker after it, so nothing was changed`, exit 1 | the block is damaged, and nothing says where it ends. Say so, leave the file to the user, and go on to step 5 |
| `needs action: <file> holds a preset block, …` | an earlier release's installer could write the block into a project's `CLAUDE.md`, which is that project's committed text. Name the file under *Needs action* in the output; the user deletes the lines between its markers |

**5. Name both moves, cheapest first, and say what each one is known to do.**
The user can finish the work in hand either way: the running session keeps
the version it started with, because the old directory stays in the plugin
cache and `$CLAUDE_PLUGIN_ROOT` still resolves to it. Nothing is half-updated
and nothing breaks mid-session.

Then say what loads it. The two moves cost very different things (one ends
the session in progress and the other does not), and the evidence behind them
is not the same either:

| Move | What it is known to do | On what evidence |
|---|---|---|
| `/reload-plugins` | re-reads preloaded skill bodies out of the copy in force, which is what a spawned agent is handed | **measured.** Run 6 of `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md`: a sentinel in the version cache came back PRESENT after a reload, and ABSENT in run 5 without one |
| the same command, for anything else: hooks, agent definitions, or moving a running session onto a newly installed version | unknown | **not measured.** The experiment touched none of the three, and its sentinel sat in the *running* version's own directory, so it shows a re-read of the copy already loaded and nothing about picking up a new one |
| restarting Claude Code | starts a session on the newly installed version, with its skills, hooks and agent definitions | the move with no open question |

Say *not measured* rather than *not needed*. The difference is the whole
value of the row: a user told the reload is insufficient stops using it, and
a user told it covers everything gets a half-loaded plugin with no way to
tell.

What would settle the middle row, for whoever wants it settled: plant a
sentinel in a hook and in an `agents/*.md` under the newly installed version
in `~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/`, type
`/reload-plugins` without restarting, then trigger the hook's event and spawn
the agent. That is run 6's own method, one artifact over.

## What this does not do

**It does not restart or reload anything.** Both are the user's to type.
Ending a session is the user's call and the user's unfinished work is in it,
and a built-in CLI command is not a skill, so `/reload-plugins` is not
something this procedure can invoke on the user's behalf either. Naming the
cheaper move and running it are different acts, and only the first is this
command's job.

**It does not delete anything the user wrote.** The preset block is taken
out with its markers, which is the whole of what the plugin wrote, and no
line outside them is touched; a project's `CLAUDE.md` is named, never
edited.

**It does not decide the update is wanted.** If a release changes behavior the
user relies on, the summary in step 3 is where the user finds that out, which
is why the summary comes with the update rather than after it.

## Output

```
Updated: <old> to <new>           (or: already on <version>, nothing to do)

What you are getting:
- <what changes for the user> (<version>)
- ...

Needs action:                     (omit when there is none)
- <what moved, what to set, what expires when>

To load it: /reload-plugins re-reads the skill bodies a spawned agent is
handed, out of the copy this session is already on. That is what was measured
and it is the whole of it. Nobody has measured whether a reload reaches hooks,
agent definitions, or <new> itself, so restart for those. Either way this
session keeps running <old> until you do, so nothing is half-applied.
```
