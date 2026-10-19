#!/usr/bin/env python3
"""rule_changes — the one reader of a spec's `## Rule changes` section.

The grammar is `skills/settle/SKILL.md` §*Rule changes*, and `GRAMMAR` below
is its one spelling in code. `parse` reads a section into operations,
refusing at its line any block that does not match whole. `replay` applies
specs to the policy root's documents in memory, in the order it is handed,
each spec whole or not at all. `order` and `conflicts` read merge order from
git. `settle` writes what `replay` returns; nothing here writes a file.

Headings, fences and comments are read through
`skills/verify/scripts/unverified_check.py` (`live_lines`, `heading_level`,
`closed_fence_lines`, `gfm_lines`), loaded by path, so this module spells no
fence or heading rule of its own.
"""

import collections
import importlib.util
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
READER = os.path.join(HERE, "..", "..", "verify", "scripts", "unverified_check.py")

HEADING = "Rule changes"
NOTHING = "nothing — "
# Each operation's fields: (required, optional).
GRAMMAR = {
    "add": (("file", "to"), ("section",)),
    "change": (("file", "section", "from", "to"), ()),
    "remove": (("file", "section"), ("from",)),
}

ITEM_RE = re.compile(r"^- (\S+)\s*$")
FIELD_RE = re.compile(r"^  ([a-z]+):(?: (.*))?$")

Op = collections.namedtuple("Op", "kind file section old new line")
# `ops` is None where the spec has no section; `nothing` is the reason of a
# `nothing — <why>` section; `errors` is `[(line, reason)]`.
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


def parse(text, policy_root="docs"):
    """The `## Rule changes` section of a spec's TEXT, as a `Parsed`."""
    r = reader()
    lines = r.gfm_lines(text)
    marks = headings(lines)
    found = [(n, lv) for n, lv, t in marks if lv == 2 and t == HEADING]
    if not found:
        return Parsed(None, None, [])
    if len(found) > 1:
        return Parsed([], None, [(found[1][0] + 1, "a second `## Rule changes`")])
    start = found[0][0]
    end = next((n for n, lv, _ in marks if n > start and lv <= 2), len(lines))
    live = [flag for _, flag in r.live_lines(lines)]
    fenced = r.closed_fence_lines(lines)

    body = []
    for n in range(start + 1, end):
        line = lines[n]
        if (not live[n] and n not in fenced) or line.lstrip().startswith("<!--"):
            continue
        body.append((n + 1, line))
    while body and not body[-1][1].strip():
        body.pop()
    while body and not body[0][1].strip():
        body.pop(0)
    if not body:
        return Parsed([], None, [(start + 1, "the section is empty")])

    first_no, first = body[0]
    if first.startswith(NOTHING.strip()):
        why = " ".join(
            [first[len(NOTHING.strip()) :].strip()] + [t.strip() for _, t in body[1:]]
        ).strip()
        if not why or any(ITEM_RE.match(t) for _, t in body[1:]):
            return Parsed(
                [], None, [(first_no, "`nothing — ` needs a reason and no item")]
            )
        return Parsed([], why, [])

    ops, errors, item = [], [], None
    for no, line in body:
        m = ITEM_RE.match(line)
        if m:
            item = {"kind": m.group(1), "line": no, "fields": {}, "last": None}
            ops.append(item)
            if item["kind"] not in GRAMMAR:
                errors.append(
                    (no, f"`{item['kind']}` is not one of add, change, remove")
                )
            continue
        if item is None:
            errors.append((no, "a line outside an item"))
            break
        m = FIELD_RE.match(line)
        if m:
            name = m.group(1)
            if name in item["fields"]:
                errors.append((no, f"`{name}` given twice"))
            item["fields"][name] = [no, [m.group(2) or ""]]
            item["last"] = name
            continue
        if item["last"] and (not line.strip() or line.startswith("    ")):
            item["fields"][item["last"]][1].append(line[4:])
            continue
        errors.append((no, "a line that is not a field of the item above"))
    if errors:
        return Parsed([], None, errors[:1])

    out = []
    for item in ops:
        need, may = GRAMMAR[item["kind"]]
        fields = item["fields"]
        for name, (no, _) in fields.items():
            if name not in need + may:
                errors.append((no, f"`{name}` is not a field of `{item['kind']}`"))
        for name in need:
            if name not in fields:
                errors.append((item["line"], f"`{item['kind']}` needs `{name}`"))
        values = {}
        for name, (no, parts) in fields.items():
            value = "\n".join(parts).strip("\n").rstrip()
            if not value.strip():
                errors.append((no, f"`{name}` is empty"))
            values[name] = value
        file = values.get("file", "")
        if not re.fullmatch(re.escape(policy_root) + r"/[^/]+\.md", file):
            errors.append(
                (item["line"], f"`{file}` is not a top-level {policy_root}/ file")
            )
        if errors:
            return Parsed([], None, errors[:1])
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


def _pattern(old):
    """OLD as a pattern: whitespace runs collapsed, and no match inside a word."""
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
        return "".join(head + [nl, rule] + gap + tail), None

    offset = len("".join(lines[: h + 1]))
    region = "".join(lines[h + 1 : end])
    hits = list(_pattern(op.old).finditer(region))
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


def replay(read, specs, held):
    """`(documents, applied, refused)` for SPECS, `[(id, [Op])]` in merge order.

    READ(path) is a document's text before the replay, or None. HELD maps an
    id to `[(line, reason)]` refused before the replay (a parse error, an open
    record, a conflict). A spec applies all of its operations or none, and a
    spec after a refused one at one of its places waits, so a later spec never
    applies under an earlier one. `documents` holds every changed text."""
    documents, applied, refused, blocked = {}, [], [], {}
    for work_item, ops in specs:
        places = [place(o) for o in ops or []]
        why = list(held.get(work_item, []))
        if not why:
            waits = [blocked[p] for p in places if p in blocked]
            if waits:
                file, section = next(p for p in places if p in blocked)
                where = f"{file} section `{section}`" if section else file
                why = [(0, f"waits on {waits[0]}, refused earlier at {where}")]
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
    order. An id no such commit adds comes last, with commit None."""
    r = subprocess.run(
        [
            "git", "-C", root, "log", "--full-history", "--topo-order",
            "--reverse", "--diff-filter=A", "--name-only", "--format=%x00%H",
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
        parts = line.split("/")
        if len(parts) == 4 and "/".join(parts[:2]) == specs and parts[3] == "spec.md":
            first.setdefault(parts[2], commit)
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


def conflicts(root, entries):
    """`{id: (other id, place)}` for specs that name one place where ancestry
    cannot order their adding commits. ENTRIES is `[(id, commit, [Op])]`."""
    out = {}
    for n, (a, ca, ops_a) in enumerate(entries):
        for b, cb, ops_b in entries[n + 1 :]:
            shared = set(map(place, ops_a)) & set(map(place, ops_b))
            if not shared or _ancestor(root, ca, cb) or _ancestor(root, cb, ca):
                continue
            where = sorted(shared, key=str)[0]
            out.setdefault(a, (b, where))
            out.setdefault(b, (a, where))
    return out
