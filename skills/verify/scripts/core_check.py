#!/usr/bin/env python3
"""seal core: whether this session's context holds the core, read from its transcript.

  seal core                      the session CLAUDE_CODE_SESSION_ID names
  seal core --transcript PATH    the transcript at PATH

A session receives the core, `skills/core/SKILL.md`, from the plugin's
`SessionStart` hook, `hooks/core-start.py`, under one first line naming the
file printed, the plugin's version and the file's SHA-256 (#1177). The hook's
output is not a memory file, so `/memory` does not list it; this command is
where a person or a session sees which core it holds. `hooks/lib/core.py#parse`
is the one reader of that first line.

**Which transcript.** The one `--transcript` names, or else
`<config>/projects/*/<id>.jsonl`, where `<config>` is `$CLAUDE_CONFIG_DIR` or
`~/.claude` and `<id>` is `$CLAUDE_CODE_SESSION_ID`. Every project directory
is searched, because its name encodes the directory the session started in,
which a worktree changes; where two hold the id, the newest is read. Run from
an agent's Bash, the variable names the session that spawned the agent, so
the check reads the orchestrating session's transcript, never the agent's.

**What is in context.** Every entry after the last `type: system`,
`subtype: compact_boundary` entry, and every earlier entry whose `uuid` that
boundary's `compactMetadata.preservedMessages.uuids` lists. With no boundary,
every entry is.

**A core entry** is an in-context `type: attachment` entry whose
`attachment.type` is `hook_success`, whose `attachment.hookEvent` is
`SessionStart`, and whose `attachment.stdout` opens with a first line `parse`
reads. A transcript whose shape this does not recognise has no core entry,
so a Claude Code release that changes the shape fails the check rather than
passing it.

**It passes, exit 0,** where exactly one core entry is in context, its
`attachment.content`, what the model received, is its `stdout`, the file its
first line names is there, that file's SHA-256 is the line's, and the body is
the file's text below its frontmatter, which is what the hook prints
(`hooks/lib/core.py#without_frontmatter`). Text is compared with each line
ending, a `\\n` and any `\\r` before it, as `\\n`, and the trailing line
endings removed, a `\\r` left at the end among them: the harness drops the
trailing newlines of what it hands the model, and a Windows stream writes
each `\\n` as `\\r\\n`, over a core whose own lines may end `\\r\\n`. It prints
one line naming the file, the version, the digest and the hook.

**It fails, exit 1,** with one line naming the reason: no session id and no
`--transcript`; no transcript; no core entry in context, which names
`--bare` where `CLAUDE_CODE_SIMPLE` is `1`, and names the core this plugin's
hook prints for the working directory, which the session opens once instead;
more than one core entry; `content` that is not `stdout`, which is the
harness's preview past `core.CAP`; a named file that is not there; a digest or
a body that differs from the file.

Exit 2 is an unusable argument, or `hooks/lib/core.py` or
`hooks/lib/hooksession.py` absent from the plugin around this script, so
nothing was read.
"""

import argparse
import glob
import hashlib
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
HOOKS = os.path.join(PLUGIN, "hooks", "lib")

# What `--bare` sets, and so the one sign of a session that runs no plugin hook.
BARE_VARIABLE = "CLAUDE_CODE_SIMPLE"

PREFIX = "seal core: "

# A line ending as the comparison reads it: a `\n` and every `\r` before it.
LINE_END = re.compile(r"\r*\n")


def _load(name, purpose):
    """`hooks/lib/<name>` by path, or a sentence naming PURPOSE and exit 2."""
    path = os.path.join(HOOKS, name)
    if not os.path.isfile(path):
        sys.stderr.write(
            f"{PREFIX}cannot read {path}, which {purpose}. It ships in the "
            "plugin beside this script; a copy of one script taken on its own "
            "is not a plugin. Nothing was read.\n"
        )
        raise SystemExit(2)
    spec = importlib.util.spec_from_file_location(
        "agentic_seal_core_" + name[:-3], path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CORE = _load("core.py", "reads the core hook's first line")
SESSION_VARIABLE = _load(
    "hooksession.py", "names the variable a session's id is read from"
).SESSION_VARIABLE


def find(environ, given):
    """`(path, None)` for the transcript to read, or `(None, reason)`: the
    path GIVEN, or else the session's file under the config directory."""
    if given:
        if os.path.isfile(given):
            return given, None
        return None, f"no transcript at {given}."
    session = environ.get(SESSION_VARIABLE)
    if not session:
        return None, (
            f"{SESSION_VARIABLE} is not set and no --transcript was given, so "
            "no transcript was read."
        )
    config = environ.get("CLAUDE_CONFIG_DIR") or os.path.expanduser("~/.claude")
    projects = os.path.join(config, "projects")
    pattern = os.path.join(glob.escape(projects), "*", glob.escape(session) + ".jsonl")
    found = glob.glob(pattern)
    if not found:
        return None, f"no transcript for session {session} under {projects}."
    return max(found, key=os.path.getmtime), None


def entries(path):
    """Each line of the transcript at PATH that is a JSON object, in order."""
    out = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            if isinstance(entry, dict):
                out.append(entry)
    return out


def _is_boundary(entry):
    return entry.get("type") == "system" and entry.get("subtype") == "compact_boundary"


def in_context(entries):
    """The ENTRIES the session's context holds: every one after the last
    compaction boundary, and every earlier one that boundary preserves."""
    last = None
    for at, entry in enumerate(entries):
        if _is_boundary(entry):
            last = at
    if last is None:
        return list(entries)
    # A field missing or of another type preserves nothing, so a boundary
    # whose shape moved drops what came before it rather than keeping it.
    kept = entries[last].get("compactMetadata")
    for field in ("preservedMessages", "uuids"):
        kept = kept.get(field) if isinstance(kept, dict) else None
    preserved = set(kept) if isinstance(kept, list) else set()
    return [e for e in entries[:last] if e.get("uuid") in preserved] + entries[last:]


def core_entries(entries):
    """The ENTRIES that are the core hook's output: a `SessionStart`
    `hook_success` attachment whose `stdout` opens with the core's header."""
    out = []
    for entry in entries:
        hook = entry.get("attachment") if entry.get("type") == "attachment" else None
        if not isinstance(hook, dict):
            continue
        if (
            hook.get("type") != "hook_success"
            or hook.get("hookEvent") != "SessionStart"
        ):
            continue
        stdout = hook.get("stdout")
        if isinstance(stdout, str) and CORE.parse(stdout) is not None:
            out.append(entry)
    return out


def _normal(text):
    """TEXT with each line ending as `\\n` and its trailing line endings
    removed. A line ending is a `\\n` and any `\\r` before it, so a stream
    that writes `\\n` as `\\r\\n` over a `\\r\\n` file changes no line; a `\\r`
    left at the end is the rest of a line ending whose `\\n` was dropped."""
    return LINE_END.sub("\n", text).rstrip("\r\n")


def judge(entries, bare, fallback):
    """`(exit code, line)` for a transcript's ENTRIES. BARE says the session
    runs under `--bare`; FALLBACK is the core the session opens where no
    entry holds one."""
    found = core_entries(in_context(entries))
    if not found:
        if bare:
            why = f"the session runs under --bare ({BARE_VARIABLE}=1), which skips"
            why += " plugin hooks"
        else:
            why = "no SessionStart hook printed the core since the last compaction,"
            why += " so the installed plugin predates the hook or its hooks are off"
        return 1, (
            f"{PREFIX}no core entry in this session's context: {why}; open "
            f"{fallback} once."
        )
    names = [e["attachment"].get("hookName") or "SessionStart" for e in found]
    if len(found) > 1:
        return 1, (
            f"{PREFIX}{len(found)} core entries are in this session's context "
            f"({', '.join(names)}), so the core was read more than once."
        )
    hook, name = found[0]["attachment"], names[0]
    stdout, content = hook["stdout"], hook.get("content")
    if not isinstance(content, str) or _normal(content) != _normal(stdout):
        received = len(content) if isinstance(content, str) else 0
        return 1, (
            f"{PREFIX}what the model received from {name} ({received} characters "
            f"of content) is not what the hook printed ({len(stdout)} characters "
            f"of stdout): past about {CORE.CAP:,} characters the context holds a "
            "preview, not the core."
        )
    read = CORE.parse(stdout)
    try:
        with open(read.path, "rb") as f:
            data = f.read()
    except OSError:
        return 1, (
            f"{PREFIX}{read.path}, which the core entry's first line names, is "
            "not a file, so what the session read cannot be compared with it."
        )
    digest = hashlib.sha256(data).hexdigest()
    if digest != read.digest:
        return 1, (
            f"{PREFIX}{read.path} has changed since the session read it: its "
            f"sha256 is {digest}, and the core entry's first line says {read.digest}."
        )
    text = CORE.without_frontmatter(data.decode("utf-8", "replace"))
    if _normal(read.body) != _normal(text):
        return 1, (
            f"{PREFIX}the core entry's body is not the text of {read.path} "
            "below its frontmatter, though the two digests agree."
        )
    return 0, (
        f"{PREFIX}{read.path}, plugin {read.version}, sha256 {read.digest}, "
        f"from {name}, in context once."
    )


def main(argv=None, environ=None, cwd=None):
    environ = os.environ if environ is None else environ
    parser = argparse.ArgumentParser(
        prog="seal core",
        description="Whether this session's context holds the core, "
        "skills/core/SKILL.md, once and whole, read from its transcript. "
        f"Without --transcript it reads the session {SESSION_VARIABLE} names; "
        "run from an agent's Bash, that is the session that spawned it, so "
        "the orchestrating session's transcript is read. Exit 0 where the "
        "core is in context once, 1 with the reason otherwise.",
    )
    parser.add_argument(
        "--transcript", metavar="PATH", help="the transcript to read instead"
    )
    args = parser.parse_args(argv)
    path, reason = find(environ, args.transcript)
    if path is None:
        print(PREFIX + reason)
        return 1
    fallback = CORE.origin(cwd or os.getcwd(), PLUGIN)
    code, line = judge(entries(path), environ.get(BARE_VARIABLE) == "1", fallback)
    print(line)
    return code


if __name__ == "__main__":
    for _name, _errors in (("stdout", "replace"), ("stderr", "backslashreplace")):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
