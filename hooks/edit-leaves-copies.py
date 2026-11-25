#!/usr/bin/env python3
"""PostToolUse on `Edit`: name to the party that edited a work item's
record each place in the item's other records that still holds the words
the edit replaced.

A work item's records restate one fact in several files, and a fix that
changes the fact in one of them leaves the others for the next round to
find (#1612). Contract rule 19 asks the writer to look for what stood on
the old fact; this hook runs that look on the records at the edit, and
leaves the judgment of each place to the writer.

The hook reads the call's `tool_name`, which is `Edit`, and of its
`tool_input` the strings `file_path`, `old_string` and `new_string`. It
reads on where `file_path` is absolute and stands at
`<root>/threads/<id>/<file>`, where `<root>/README.md` opens with
`lib/optin.py#MARKER`, and `<file>` ends in `.md`, stands outside `trail/`
and is not `guarantee.md`. The records it then searches are the `.md` files
of `<root>/threads/<id>/` outside `trail/` and other than `guarantee.md`,
the edited file among them, as they stand after the edit: `trail/` and
`guarantee.md` are records of what a party read and did, and quote what
they read.

The words the edit replaced are each span of `old_string` that differs from
`new_string`, compared word by word, with `AROUND` words of `old_string` on
each side; an insertion's span is the `AROUND` words on each side of the
point. A span is kept where it holds `MIN_WORDS` words and `MIN_CHARS`
characters or more, the floor #1612's frame measured its replay at, so a
short edit, or an `old_string` that holds few words beyond the change,
prints nothing. A place is a record whose text, each run of whitespace
made one space, holds a kept span, and its line is the one where the span
opens. The text names each place by its path under the work item's
directory and its line, with the words that stand there, and says what the
writer does with it. It stays under `LIMIT` characters, the length past
which the harness moves a hook's context to a file behind a preview: the
places that do not fit are counted and not listed.

It reads words, so a copy in other words is not found, and a place that
holds the same words for another fact is named; the text says such a place
stays. A wrong silence costs a copy the next round finds, and a wrong print
costs the writer one look.

**It fails toward printing nothing.** A payload that is not a JSON object,
a call of another tool, a field that is missing or not a string, a relative
path, a path outside a marked root's work item, a `Write` call, which
`hooks/hooks.json` does not match, and a record that cannot be read as
UTF-8 text each print nothing, and so does anything that raises: the
`__main__` block turns every raise into exit 0. The hook writes nothing,
starts no process and reaches no network. Its command in `hooks/hooks.json`
ends with ` || exit 0`, so the command exits 0 whatever happens, a file its
interpreter cannot load among them.
"""

import difflib
import json
import os
import sys

LIB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib")

# The words of `old_string` taken on each side of a changed span.
AROUND = 3

# The floor a span is kept at: this many words, and this many characters
# with its words joined by one space.
MIN_WORDS = 6
MIN_CHARS = 30

# The length the context stays under, and the characters of one span shown
# beside its place before the rest is cut.
LIMIT = 10_000
SHOWN = 240

# The directory of a work item that holds what passed between the parties,
# and the sealer's record: neither is read or searched.
TRAIL = "trail"
GUARANTEE = "guarantee.md"

# The rule the text cites for what the writer does with a place.
RULE = "`skills/agent-contract/SKILL.md` rule 19"


def _located(path, optin):
    """`(item, rel)` for the absolute PATH of a record this hook reads: the
    work item's directory and the record's `/`-joined path under it; None
    where PATH is another file."""
    if not os.path.isabs(path):
        return None
    path = os.path.normpath(path)
    rel = []
    here = path
    while True:
        parent = os.path.dirname(here)
        if parent == here:
            return None
        rel.insert(0, os.path.basename(here))
        if (
            len(rel) >= 2
            and os.path.basename(parent) == optin.WORK_ITEMS
            and optin.marked(os.path.dirname(parent))
        ):
            inner = "/".join(rel[1:])
            if inner.endswith(".md") and _read(inner):
                return os.path.join(parent, rel[0]), inner
            return None
        here = parent


def _read(rel):
    """True where the `/`-joined REL under a work item's directory is a
    record this hook reads and searches: outside `TRAIL` and not
    `GUARANTEE`."""
    return rel.split("/", 1)[0] != TRAIL and rel != GUARANTEE


def _records(item):
    """The `/`-joined paths of the `.md` files under ITEM this hook
    searches, in path order."""
    found = []
    for at, dirs, files in os.walk(item):
        under = os.path.relpath(at, item)
        prefix = "" if under == os.curdir else "/".join(under.split(os.sep)) + "/"
        dirs[:] = [d for d in dirs if _read(prefix + d)]
        for name in files:
            if name.endswith(".md") and _read(prefix + name):
                found.append(prefix + name)
    return sorted(found)


def _spans(old, new):
    """Each span of OLD's words that the edit to NEW replaced, with
    `AROUND` words on each side, as one space-joined string, where it holds
    `MIN_WORDS` words and `MIN_CHARS` characters or more; each once, in
    the order they stand in OLD."""
    words = old.split()
    matcher = difflib.SequenceMatcher(None, words, new.split(), autojunk=False)
    kept = []
    for tag, start, end, _, _ in matcher.get_opcodes():
        if tag == "equal":
            continue
        span = words[max(0, start - AROUND) : end + AROUND]
        joined = " ".join(span)
        if len(span) >= MIN_WORDS and len(joined) >= MIN_CHARS and joined not in kept:
            kept.append(joined)
    return kept


def _places(item, records, spans):
    """`(rel, line, span)` for each place in RECORDS under ITEM whose text,
    whitespace collapsed, holds one of SPANS, the line being the one where
    the span opens. A record that cannot be read as UTF-8 raises."""
    places = []
    for rel in records:
        with open(os.path.join(item, *rel.split("/")), encoding="utf-8") as f:
            text = f.read()
        # The line each word of the text stands on, in the order the
        # collapsed text holds them.
        lines = []
        for number, line in enumerate(text.split("\n"), 1):
            lines.extend([number] * len(line.split()))
        collapsed = " ".join(text.split())
        for span in spans:
            at = collapsed.find(span)
            while at != -1:
                places.append((rel, lines[collapsed.count(" ", 0, at)], span))
                at = collapsed.find(span, at + 1)
    return sorted(set(places))


def _context(item, rel, places):
    """The text that names PLACES to the writer of the edit of REL in the
    work item at ITEM, under `LIMIT` characters."""
    head = (
        "hooks/edit-leaves-copies.py: words this Edit replaced in `"
        + rel
        + "` still stand in the records of work item "
        + os.path.basename(item)
        + ", outside `trail/` and `guarantee.md`:"
    )
    tail = (
        "A place that states the fact this edit changed is rewritten in place, "
        "or cites the record that holds the fact (" + RULE + "). A place that "
        "states another fact in the same words stays as it is."
    )
    listed = []
    # The room the places have: the limit, less the head, the tail, the
    # line that counts what was left and the blank lines between them.
    room = LIMIT - len(head) - len(tail) - 100
    for at, (where, line, span) in enumerate(places):
        shown = span if len(span) <= SHOWN else span[:SHOWN] + " ..."
        entry = "- `" + where + "` line " + str(line) + ': "' + shown + '"'
        if len(entry) + 1 > room:
            listed.append("- and " + str(len(places) - at) + " more places, not listed")
            break
        room -= len(entry) + 1
        listed.append(entry)
    return head + "\n\n" + "\n".join(listed) + "\n\n" + tail


def main():
    """Print the `PostToolUse` object for the payload on stdin where an
    edit left places, and nothing otherwise. A payload that is not a JSON
    object raises here, and the `__main__` block turns every raise into
    exit 0."""
    sys.path.insert(0, LIB)
    import optin

    payload = json.load(sys.stdin)
    if payload.get("tool_name") != "Edit":
        return
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        return
    path, old, new = (
        tool_input.get(k) for k in ("file_path", "old_string", "new_string")
    )
    if not all(isinstance(v, str) for v in (path, old, new)):
        return
    located = _located(path, optin)
    if located is None:
        return
    item, rel = located
    if not os.path.isfile(os.path.join(item, *rel.split("/"))):
        return
    spans = _spans(old, new)
    if not spans:
        return
    places = _places(item, _records(item), spans)
    if not places:
        return
    said = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": _context(item, rel, places),
        }
    }
    sys.stdout.write(json.dumps(said) + "\n")
    sys.stdout.flush()


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a hook says "nothing to see here". `lib/console.py`
    # owns the reasoning and the three decisions behind these lines. They are
    # its loop rather than its `to_utf8()`, because they run before `lib/` is
    # imported, which this script survives the absence of.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    try:
        main()
    except BaseException:
        pass
    sys.exit(0)
