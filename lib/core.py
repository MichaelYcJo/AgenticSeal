"""What the core hook prints into a session.

**This module is the one definition of the core hook's output.** The core is
`skills/core/SKILL.md`. A session in a repository that holds an `agentory/` root
receives it from the plugin's `SessionStart` hook, `hooks/core-start.py`,
which prints `output`: the file's text below its frontmatter, under one
first line naming the file printed and the running plugin's version, and
above one closing line, `closing`, naming where work starts by two paths
relative to the plugin's root. The frontmatter stays out because its
`description:` already reaches every session in the harness's skill
listing. `agentic payload` counts `rendered`'s bytes, so the hook and the meter
cannot disagree about what a session received.

**Where the core is printed, the plugin's root stands once in the
output.** Where the core printed is the plugin's own, the first line names
it under that root and the closing line says its paths are relative to it.
Where the core is a clone's, the closing line names the running plugin's
root. **An output that would reach the harness's cap is not printed**: one
line names the core's file for the session to open, above the closing line
naming the running plugin's root whichever core it is, because past the
cap the harness keeps only a preview and the closing line would be lost.

**A session in a repository with no `agentory/` root receives nothing**: the
root is what says the repository runs the IADD process
(`optin.opted_in`), and a session doing other work pays for no core.

**Where the session's repository is a clone of the running plugin, the file
printed is the clone's** (`origin`), so the tree's core governs a session
there and the session reads it once. A clone is a repository whose top level
holds `.claude-plugin/plugin.json` naming the running plugin, and a core.

Python 3.9 syntax: a hook runs under whatever `python3` the harness finds,
3.9 on a stock macOS.
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import optin

# Where the core and the manifest stand under a plugin root or a clone of one.
CORE = ("skills", "core", "SKILL.md")
MANIFEST = (".claude-plugin", "plugin.json")
# The two files the closing line sends a session to, under the plugin root
# the hook ran from.
ORCHESTRATION = ("skills", "implement", "orchestration.md")
REVIEW = ("skills", "code-review", "SKILL.md")

# The harness's cap on one hook's output, in characters: past it the context
# holds a preview naming a file rather than the output. Measured between
# 9,990 and 10,010 on Claude Code 2.1.312, and a case holds the tree's whole
# output under it at a plugin root of `ROOT_ROOM` characters.
CAP = 10_000
# The length of plugin root at which the tree's whole output is held under
# `CAP`. The default plugin root is the home directory followed by
# `.claude/plugins/cache/<marketplace>/<plugin>/<version>`, and a longer root
# than this receives `TOO_LONG` once the output reaches `CAP`.
ROOT_ROOM = 100

HEADER = "IADD core from {path}, plugin {version}."
MISSING = "IADD core: {path} is not a file, so no core was printed."
# What the hook prints in place of a core whose whole output would reach
# `CAP`. It opens as `MISSING` does and not as `HEADER` does, so a session
# reads it as no core printed.
TOO_LONG = (
    "IADD core: printing {path} here would pass the harness's cap of "
    "{cap:,} characters on a hook's output, so no core was printed. Open that "
    "file whole before anything else."
)
# The output's last line: where work starts in this session. It stands here
# and not in the core's text, because every agent receives the core through
# `skills:` and none starts work (`skills/core/SKILL.md` *A document is cut
# by who opens it and at which step*). Its two paths are relative to the
# plugin's root, joined with `/` on every platform, and one of the two
# sentences below follows it.
START = (
    "Where a request to change code or to work an issue arrives in this "
    "session, this session is the orchestrator and opens `{orchestration}` "
    "*Orchestrator: the order inside a ticket* before its first edit. Where a "
    "request to review a pull request, a diff or a branch arrives, it opens "
    "`{review}`."
).format(orchestration="/".join(ORCHESTRATION), review="/".join(REVIEW))
# Where the core printed is the plugin's own, whose path the first line
# names under the plugin's root.
OWN_ROOT = "Both paths are relative to the plugin's root."
# Where the core printed is another file, a clone's.
RUNNING_ROOT = "Both paths are relative to the running plugin's root, `{root}`."
# A frontmatter: an opening `---` line, then everything up to the first
# closing `---` line, and the blank lines after it.
FRONTMATTER = re.compile(r"---\r?\n(?:.*?\n)??---\r?(?:\n|\Z)[\r\n]*", re.S)
# The version said where the running plugin's manifest names none.
UNKNOWN = "unknown"


def manifest(root):
    """The object `<root>/.claude-plugin/plugin.json` holds, or {} where it
    cannot be read as one."""
    try:
        with open(os.path.join(root, *MANIFEST), encoding="utf-8") as f:
            found = json.load(f)
    except (OSError, ValueError):
        return {}
    return found if isinstance(found, dict) else {}


def origin(cwd, plugin_root):
    """The core to print for a session in CWD: the clone's where CWD is in a
    clone of the plugin at PLUGIN_ROOT, and the plugin's own otherwise."""
    plugin_root = os.path.abspath(plugin_root)
    own = os.path.join(plugin_root, *CORE)
    top = optin.repo_root(cwd)
    if not top:
        return own
    name = manifest(plugin_root).get("name")
    tree = os.path.join(top, *CORE)
    if name and manifest(top).get("name") == name and os.path.isfile(tree):
        return tree
    return own


def header(path, version):
    """The first line of the output, naming PATH and VERSION."""
    return HEADER.format(path=path, version=version)


def without_frontmatter(text):
    """TEXT below its frontmatter's closing line, from its first line that is
    not blank; TEXT whole where it does not open with a closed frontmatter."""
    found = FRONTMATTER.match(text)
    return text[found.end() :] if found else text


def closing(plugin_root=None):
    """The output's last line: `START`, one space, and `OWN_ROOT` where
    PLUGIN_ROOT is None, or `RUNNING_ROOT` naming PLUGIN_ROOT otherwise."""
    if plugin_root is None:
        return START + " " + OWN_ROOT
    return START + " " + RUNNING_ROOT.format(root=plugin_root)


def whole(text, path, version, plugin_root=None):
    """The whole output for a core whose TEXT stands below its frontmatter:
    the header for PATH and VERSION, a newline, TEXT, a newline, then
    `closing(PLUGIN_ROOT)`. It reads no file."""
    return header(path, version) + "\n" + text + "\n" + closing(plugin_root)


def rendered(path, plugin_root):
    """The core at PATH as the hook prints it: `whole`, whose closing line
    names its two files relative to the plugin's root and names
    PLUGIN_ROOT only where PATH is not the plugin's own core. Where that
    output would reach `CAP`, the line `TOO_LONG` naming PATH, a newline and
    the closing line naming PLUGIN_ROOT. Where PATH is not a file, the one
    line `MISSING` says so."""
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError:
        return MISSING.format(path=path)
    plugin_root = os.path.abspath(plugin_root)
    version = manifest(plugin_root).get("version") or UNKNOWN
    text = without_frontmatter(data.decode("utf-8", "replace"))
    # The plugin's own core is the file under PLUGIN_ROOT, and a path that
    # cannot be compared with it is another file.
    try:
        own = os.path.samefile(path, os.path.join(plugin_root, *CORE))
    except OSError:
        own = False
    out = whole(text, path, version, None if own else plugin_root)
    if len(out) < CAP:
        return out
    return TOO_LONG.format(path=path, cap=CAP) + "\n" + closing(plugin_root)


def output(cwd, plugin_root):
    """What the hook prints for a session in CWD: `rendered` for the core
    `origin` names, where CWD's repository holds an `agentory/` root, and ""
    where it holds none."""
    if not optin.opted_in(cwd):
        return ""
    return rendered(origin(cwd, plugin_root), plugin_root)
