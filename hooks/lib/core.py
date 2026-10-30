"""What the core hook prints into a session, and how its first line is read.

**This module is the one definition of the core hook's output.** The core is
`skills/core/SKILL.md`. A session receives it from the plugin's
`SessionStart` hook, `hooks/core-start.py`, which prints `output`: the file
under one first line naming the file printed, the running plugin's version
and the file's SHA-256. `seal core` reads that line back from a session's
transcript with `parse`, and `seal payload` counts `output`'s bytes, so the
hook, the check and the meter cannot disagree about what a session received.

**Where the session's repository is a clone of the running plugin, the file
printed is the clone's** (`origin`), so the tree's core governs a session
there and the session reads it once. A clone is a repository whose top level
holds `.claude-plugin/plugin.json` naming the running plugin, and a core.

Python 3.9 syntax: a hook runs under whatever `python3` the harness finds,
3.9 on a stock macOS.
"""

import hashlib
import json
import os
import re
import sys
from collections import namedtuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import optin

# Where the core and the manifest stand under a plugin root or a clone of one.
CORE = ("skills", "core", "SKILL.md")
MANIFEST = (".claude-plugin", "plugin.json")

# The harness's cap on one hook's output, in characters: past it the context
# holds a preview naming a file rather than the output. Measured between
# 9,990 and 10,010 on Claude Code 2.1.312 (#1177), and a case holds the
# tree's whole output under it.
CAP = 10_000

HEADER = "AgenticSeal core from {path}, plugin {version}, sha256 {digest}."
# Anchored at both ends, so a path that holds a comma, or the header's own
# words, still parses: the path takes everything the last two fields leave.
PATTERN = re.compile(
    r"AgenticSeal core from (?P<path>.+), plugin (?P<version>\S+), "
    r"sha256 (?P<digest>[0-9a-f]{64})\."
)
MISSING = "AgenticSeal core: {path} is not a file, so no core was printed."
# The version said where the running plugin's manifest names none.
UNKNOWN = "unknown"

Core = namedtuple("Core", "path version digest body")


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


def header(path, version, digest):
    """The first line of the output, naming PATH, VERSION and DIGEST."""
    return HEADER.format(path=path, version=version, digest=digest)


def output(cwd, plugin_root):
    """What the hook prints for a session in CWD: the header, a newline, then
    the core's text, its digest over the bytes as read. Where the core is not
    a file, the one line `MISSING` says so."""
    path = origin(cwd, plugin_root)
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError:
        return MISSING.format(path=path)
    version = manifest(os.path.abspath(plugin_root)).get("version") or UNKNOWN
    digest = hashlib.sha256(data).hexdigest()
    return header(path, version, digest) + "\n" + data.decode("utf-8", "replace")


def parse(text):
    """`Core(path, version, digest, body)` read from TEXT, or None where its
    first line is not a header. The first line ends at the first newline, and
    a carriage return before it is not part of the line."""
    first, _, body = text.partition("\n")
    found = PATTERN.fullmatch(first[:-1] if first.endswith("\r") else first)
    if not found:
        return None
    return Core(found["path"], found["version"], found["digest"], body)
