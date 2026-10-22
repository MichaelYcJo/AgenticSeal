#!/usr/bin/env python3
"""rule_changes — the one reader of a spec's `## Rule changes` section.

The grammar is `skills/settle/SKILL.md` §*Rule changes*. `GRAMMAR` below is
the one spelling of its operations in code; the item lines, their fields and
the no-change block are spelt once in `unverified_check.py`, which reads
`## Not verified` with the same block. `parse` reads a section into operations,
refusing at its line any block that does not match whole. `replay` applies
specs to the policy root's documents in memory, in the order it is handed,
each spec whole or not at all. `order` and `conflicts` read merge order from
git. `settle` writes what `replay` returns; nothing here writes a file.

Headings, fences and comments are read through
`skills/verify/scripts/unverified_check.py` (`live_lines`, `heading_level`,
`closed_fence_lines`, `liveness`, `gfm_lines`), loaded by path, so this
module spells no fence or heading rule of its own.
"""

import collections
import importlib.util
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
READER = os.path.join(HERE, "..", "..", "verify", "scripts", "unverified_check.py")

HEADING = "Rule changes"
# Each operation's fields: (required, optional). The item lines, their fields
# and the no-change block are `unverified_check.py`'s (`items`,
# `field_values`, `nothing_block`).
GRAMMAR = {
    "add": (("file", "to"), ("section",)),
    "change": (("file", "section", "from", "to"), ()),
    "remove": (("file", "section"), ("from",)),
}

Op = collections.namedtuple("Op", "kind file section old new line")
# `ops` is None where the spec has no section; `nothing` is the `why` of a
# section holding the no-change block; `errors` is `[(line, reason)]`.
Parsed = collections.namedtuple("Parsed", "ops nothing errors")

_reader = None


def reader():
    global _reader
    if _reader is None:
        spec = importlib.util.spec_from_file_location("specseal_rules_reader", READER)
        _reader = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_reader)
    return _reader


def heading_text(line):
    """A heading line's text, without its `#` runs, trimmed."""
    text = line.strip().lstrip("#").strip()
    return re.sub(r"(^|\s+)#+\s*$", "", text).strip()


def headings(lines):
    """`[(index, level, text)]` for every live heading in LINES."""
    r = reader()
    out = []
    for n, (line, live) in enumerate(r.live_lines(lines)):
        level = r.heading_level(line) if live else None
        if level is not None:
            out.append((n, level, heading_text(line)))
    return out


def letters(text):
    """TEXT's letters, case folded. A heading whose letters are those of
    `HEADING` and that is not `## HEADING` is a near miss of it."""
    return re.sub(r"[^a-z]", "", text.casefold())


def parse(text, policy_root):
    """The `## Rule changes` section of a spec's TEXT, as a `Parsed`; each
    `file` is a top-level `.md` of the directory POLICY_ROOT. A near miss of
    the heading, at any level, is refused at its line."""
    r = reader()
    lines = r.gfm_lines(text)
    marks = headings(lines)
    found = [(n, lv) for n, lv, t in marks if lv == 2 and t == HEADING]
    near = [
        n
        for n, lv, t in marks
        if letters(t) == letters(HEADING) and (n, lv) not in found
    ]
    if near:
        written = lines[near[0]].strip()
        why = f"`{written}` is a near miss of `## {HEADING}`, the one heading read"
        return Parsed([], None, [(near[0] + 1, why)])
    if not found:
        return Parsed(None, None, [])
    if len(found) > 1:
        return Parsed([], None, [(found[1][0] + 1, "a second `## Rule changes`")])
    start = found[0][0]
    end = next((n for n, lv, _ in marks if n > start and lv <= 2), len(lines))
    live = [flag for _, flag in r.live_lines(lines)]
    fenced = r.closed_fence_lines(lines)
    # `live_lines` ANDs two readings. In this one a code span never leaves
    # its line, so a line dead here is in a comment or a fence, read fence
    # first as `live_lines` reads it, and is skipped. A line live here and
    # dead in `live` begins inside a code span an earlier line opened, and
    # is refused (#988).
    literal = r.liveness(lines, spans_cross_lines=False)

    body = []
    for n in range(start + 1, end):
        line = lines[n]
        outside = live[n] or n in fenced
        if line.lstrip().startswith("<!--") or not (outside or literal[n]):
            continue
        if not outside:
            why = (
                "this line begins inside a code span an earlier line opened, "
                "and settle would drop it: close each span on the line that "
                "opens it"
            )
            return Parsed([], None, [(n + 1, why)])
        body.append((n + 1, line))
    while body and not body[-1][1].strip():
        body.pop()
    while body and not body[0][1].strip():
        body.pop(0)
    if not body:
        return Parsed([], None, [(start + 1, "the section is empty")])

    block = r.nothing_block(body)
    if block is not None:
        why, error = block
        return Parsed([], None, [error]) if error else Parsed([], why, [])

    ops, error = r.items(body)
    # An item's kind is judged before a later line's error, in line order.
    for item in ops:
        if item["kind"] == r.NOTHING:
            error = (item["line"], f"`- {r.NOTHING}` is the section's one item")
        elif item["kind"] not in GRAMMAR:
            kinds = ", ".join([*GRAMMAR, r.NOTHING])
            error = (item["line"], f"`{item['kind']}` is not one of {kinds}")
        else:
            continue
        break
    if error:
        return Parsed([], None, [error])

    out = []
    for item in ops:
        values, error = r.field_values(item, *GRAMMAR[item["kind"]])
        file = (values or {}).get("file", "")
        # No separator of either system and no drive colon in the name, so a
        # value joins to one file at the top level on every platform.
        if not error and not re.fullmatch(
            re.escape(policy_root) + r"/[^/\\:]+\.md", file
        ):
            error = (item["line"], f"`{file}` is not a top-level {policy_root}/ file")
        if error:
            return Parsed([], None, [error])
        out.append(
            Op(
                item["kind"],
                file,
                values.get("section"),
                values.get("from"),
                values.get("to"),
                item["line"],
            )
        )
    return Parsed(out, None, [])


# --- applying one operation to one document ------------------------------------


def pattern(old):
    """OLD as a pattern: whitespace runs collapsed, and no match inside a word.
    `unverified_check.py#settled` counts texts with it too."""
    words = old.split()
    pat = r"\s+".join(re.escape(w) for w in words)
    if re.match(r"\w", words[0]):
        pat = r"(?<!\w)" + pat
    if re.search(r"\w$", words[-1]):
        pat += r"(?!\w)"
    return re.compile(pat)


def _cut(text, s, e):
    """TEXT with [s, e) removed, and the line or blank line it leaves tidied."""
    if e < len(text) and text[e] in " \t":
        while e < len(text) and text[e] in " \t":
            e += 1
    else:
        while s > 0 and text[s - 1] in " \t":
            s -= 1
    out = text[:s] + text[e:]
    start = out.rfind("\n", 0, s) + 1
    stop = out.find("\n", s)
    if out[start : stop if stop >= 0 else len(out)].strip():
        return out
    out = out[:start] + (out[stop + 1 :] if stop >= 0 else "")
    if out[max(0, start - 2) : start] == "\n\n" and out[start : start + 1] == "\n":
        out = out[:start] + out[start + 1 :]
    return out


def apply_op(text, op):
    """`(new text, None)`, or `(None, why)` where OP cannot be placed in TEXT."""
    if op.kind == "add" and op.section is None:
        if text is not None:
            return None, f"{op.file} exists, and an add with no section creates one"
        return op.new + "\n", None
    if text is None:
        return None, f"{op.file} does not exist"
    lines = reader().gfm_lines(text, keepends=True)
    marks = headings([line.rstrip("\r\n") for line in lines])
    at = [(n, lv) for n, lv, t in marks if t == op.section]
    if not at:
        return None, f"no heading `{op.section}` in {op.file}"
    if len(at) > 1:
        return None, f"heading `{op.section}` appears {len(at)} times in {op.file}"
    h, level = at[0]
    end = next((n for n, lv, _ in marks if n > h and lv <= level), len(lines))
    nl = "\r\n" if "\r\n" in text else "\n"

    if op.kind == "remove" and op.old is None:
        out = "".join(lines[:h] + lines[end:])
        if end == len(lines):
            out = out.rstrip("\r\n") + nl if out.strip() else ""
        return out, None

    if op.kind == "add":
        own = next((n for n, _, _ in marks if n > h), len(lines))
        q = own
        while q > h + 1 and not lines[q - 1].strip():
            q -= 1
        head = lines[:q]
        if not head[-1].endswith(("\n", "\r")):
            head[-1] += nl
        tail = lines[q:own] + lines[own:]
        rule = nl.join(op.new.split("\n")) + nl
        gap = [nl] if own < len(lines) and not lines[q:own] else []
        return "".join([*head, nl, rule, *gap, *tail]), None

    offset = len("".join(lines[: h + 1]))
    region = "".join(lines[h + 1 : end])
    hits = list(pattern(op.old).finditer(region))
    if not hits:
        return None, f"the `from` text is not in section `{op.section}` of {op.file}"
    if len(hits) > 1:
        return None, (
            f"the `from` text appears {len(hits)} times in section `{op.section}` "
            f"of {op.file}"
        )
    s, e = offset + hits[0].start(), offset + hits[0].end()
    if op.kind == "change":
        return text[:s] + nl.join(op.new.split("\n")) + text[e:], None
    return _cut(text, s, e), None


# --- applying specs in order ------------------------------------------------------


def place(op):
    return (op.file, op.section)


def where(p):
    """A place as a person reads it."""
    return f"{p[0]} section `{p[1]}`" if p[1] else p[0]


def overlapping(read):
    """`same(p, q)`: whether two places can name one text. They do when they
    are one file and one section holds the other, a section's range holding
    its sub-sections, or either is the whole document. READ(path) is the
    document before the replay, whose headings decide what holds what."""
    held_by = {}

    def lineage(p):
        if p not in held_by:
            text, found = read(p[0]), {p[1]}
            marks = headings(reader().gfm_lines(text)) if text and p[1] else []
            at = [n for n, (_, _, t) in enumerate(marks) if t == p[1]]
            if len(at) == 1:
                level = marks[at[0]][1]
                for _, lv, t in reversed(marks[: at[0]]):
                    if lv < level:
                        found.add(t)
                        level = lv
            held_by[p] = found
        return held_by[p]

    def same(p, q):
        if p[0] != q[0]:
            return False
        return None in (p[1], q[1]) or p[1] in lineage(q) or q[1] in lineage(p)

    return same


def replay(read, specs, held):
    """`(documents, applied, refused)` for SPECS, `[(id, [Op])]` in merge order.

    READ(path) is a document's text before the replay, or None. HELD maps an
    id to `[(line, reason)]` refused before the replay (a parse error, an open
    record, a conflict). A spec applies all of its operations or none, and a
    spec after a refused one at a place overlapping one of its own
    (`overlapping`) waits, so a later spec never applies under an earlier
    one. `documents` holds every changed text."""
    documents, applied, refused, blocked = {}, [], [], {}
    same = overlapping(read)
    for work_item, ops in specs:
        places = [place(o) for o in ops or []]
        why = list(held.get(work_item, []))
        if not why:
            waits = [(b, w) for p in places for b, w in blocked.items() if same(p, b)]
            if waits:
                at, by = waits[0]
                why = [(0, f"waits on {by}, refused earlier at {where(at)}")]
        trial = dict(documents)
        for o in [] if why else ops:
            current = trial[o.file] if o.file in trial else read(o.file)
            text, reason = apply_op(current, o)
            if reason:
                why = [(o.line, reason)]
                break
            trial[o.file] = text
        if why:
            refused.extend((work_item, line, reason) for line, reason in why)
            for p in places:
                blocked.setdefault(p, work_item)
            continue
        documents = trial
        applied.append(work_item)
    return documents, applied, refused


def order(root, ref, ids, specs="seal/specs"):
    """`[(id, commit)]` for IDS in merge order: the first commit reachable from
    REF that adds the id's `spec.md`, in `git log --topo-order --reverse`
    order, a moved directory counting as added where it lands. An id no such
    commit adds comes last, with commit None."""
    r = subprocess.run(
        [
            "git", "-C", root, "log", "--full-history", "--topo-order",
            "--reverse", "--no-renames", "--diff-filter=A", "--name-only",
            "--format=%x00%H",
            ref, "--", specs,
        ],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )  # fmt: skip
    first, commit = {}, None
    for line in r.stdout.splitlines():
        if line.startswith("\0"):
            commit = line[1:]
            continue
        parts = line[len(specs) + 1 :].split("/")
        if line.startswith(specs + "/") and len(parts) == 2 and parts[1] == "spec.md":
            first.setdefault(parts[0], commit)
    known = [i for i in first if i in ids]
    return [(i, first[i]) for i in known] + [(i, None) for i in ids if i not in first]


def _ancestor(root, a, b):
    return (
        a != b
        and subprocess.run(
            ["git", "-C", root, "merge-base", "--is-ancestor", a, b],
            capture_output=True,
        ).returncode
        == 0
    )


def conflicts(root, entries, read):
    """`{id: (other id, place)}` for specs at overlapping places
    (`overlapping`) where ancestry cannot order their adding commits.
    ENTRIES is `[(id, commit, [Op])]`; READ is `replay`'s."""
    out, same = {}, overlapping(read)
    for n, (a, ca, ops_a) in enumerate(entries):
        for b, cb, ops_b in entries[n + 1 :]:
            shared = sorted(
                {p for p in map(place, ops_a) for q in map(place, ops_b) if same(p, q)},
                key=str,
            )
            if not shared or _ancestor(root, ca, cb) or _ancestor(root, cb, ca):
                continue
            out.setdefault(a, (b, shared[0]))
            out.setdefault(b, (a, shared[0]))
    return out
