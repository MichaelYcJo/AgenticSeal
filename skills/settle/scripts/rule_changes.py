#!/usr/bin/env python3
"""rule_changes — the one reader of a spec's `## Rule changes` section.

The grammar is `skills/settle/SKILL.md` *Rule changes*. `GRAMMAR` below is
the one spelling of its operations in code; the item lines, their fields and
the no-change block are spelt once in `unverified_check.py`, which reads
`## Not verified` with the same block. `parse` reads a section into operations,
refusing at its line any block that does not match whole. `order` reads merge
order from git, `merge_order` reads it in local mode from the merge commits
`settle` hands it, `group` joins the released specs whose operations name one
place into one group, `unordered` names the pairs inside a group that no
ancestry orders, and `section_lines` finds a section's lines in a document.
`settle` prints what they read; nothing here writes a file.

Headings and fences are read through
`skills/verify/scripts/unverified_check.py` (`live_lines`, `heading_level`,
`liveness`, `gfm_lines`, `blank_fences`, `comment_lines`), loaded by path,
so this module spells no fence or heading rule of its own. A spec is a
record and carries no HTML comment, so `parse` reads it with no comment
state and refuses a section line that begins with `<!--` (#1012); `headings`
keeps the comment state for `section_lines` and `overlapping`, which read the
policy documents.
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
        spec = importlib.util.spec_from_file_location("agentic_rules_reader", READER)
        _reader = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_reader)
    return _reader


def heading_text(line):
    """A heading line's text, without its `#` runs, trimmed."""
    text = line.strip().lstrip("#").strip()
    return re.sub(r"(^|\s+)#+\s*$", "", text).strip()


def headings(lines, comments=True):
    """`[(index, level, text)]` for every live heading in LINES. `comments`
    is `live_lines`'s: `parse` reads a spec with none."""
    r = reader()
    out = []
    for n, (line, live) in enumerate(r.live_lines(lines, comments=comments)):
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
    marks = headings(lines, comments=False)
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
    live = [flag for _, flag in r.live_lines(lines, comments=False)]
    # `live_lines` ANDs two readings, here with no comment state, since a
    # spec carries no comment (#1012). In this one a code span never leaves
    # its line, so a line dead here is in a fence and is skipped. A fence's
    # opener is live, so a fence inside the section is refused at that line
    # as no field. A line live here and dead in `live` begins inside a code
    # span an earlier line opened, and is refused (#988), before a line
    # beginning with `<!--` is, since an opener inside a span is text.
    literal = r.liveness(lines, spans_cross_lines=False, comments=False)
    commented = set(r.comment_lines(r.blank_fences(lines)))

    body = []
    for n in range(start + 1, end):
        line = lines[n]
        if literal[n] and not live[n]:
            why = (
                "this line begins inside a code span an earlier line opened, "
                "and settle would drop it: close each span on the line that "
                "opens it"
            )
            return Parsed([], None, [(n + 1, why)])
        if n in commented:
            return Parsed([], None, [(n + 1, r.COMMENT_LINE)])
        if not literal[n]:
            continue
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


# --- where an operation's text stands in a document ---------------------------


def pattern(old):
    """OLD as a pattern: whitespace runs collapsed, and no match inside a word.
    `settle`'s dry run finds an operation's `from` and `to` with it."""
    words = old.split()
    pat = r"\s+".join(re.escape(w) for w in words)
    if re.match(r"\w", words[0]):
        pat = r"(?<!\w)" + pat
    if re.search(r"\w$", words[-1]):
        pat += r"(?!\w)"
    return re.compile(pat)


def section_lines(text, section):
    """`((first, last), None)`: the lines, counted from 1, that SECTION spans
    in TEXT, from its heading to its last line of text before the next
    heading of its level or higher, and the whole document where SECTION is
    None; or `(None, why)` where the document is absent or the heading is not
    there once. Headings are read through `headings`, with the comment state
    a policy document keeps."""
    if text is None:
        return None, "the document is not in the tree"
    lines = reader().gfm_lines(text)
    if section is None:
        return (1, len(lines)), None
    marks = headings(lines)
    at = [(n, lv) for n, lv, t in marks if t == section]
    if not at:
        return None, f"no heading `{section}`"
    if len(at) > 1:
        return None, f"heading `{section}` appears {len(at)} times"
    h, level = at[0]
    end = next((n for n, lv, _ in marks if n > h and lv <= level), len(lines))
    while end > h + 1 and not lines[end - 1].strip():
        end -= 1
    return (h + 1, end), None


# --- the released specs, by place and in merge order --------------------------


def place(op):
    return (op.file, op.section)


def where(p):
    """A place as a person reads it."""
    return f"{p[0]} section `{p[1]}`" if p[1] else p[0]


def overlapping(read):
    """`same(p, q)`: whether two places can name one text. They do when they
    are one file and one section holds the other, a section's range holding
    its sub-sections, or either is the whole document. READ(path) is the
    document as it stands, whose headings decide what holds what."""
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


# A thread's design, relative to its directory: `hooks/lib/optin.py#DESIGN`.
DESIGN = "frame/design.md"
# Where a thread's design stood before the session-start move brought it into
# `seal/threads/`, as (directory, name): read from history only, so a moved
# thread is placed where its design was first added and not at the move's one
# commit, which adds every moved design at once.
# exempt from old_names: the 0.22.x path of a design, read from history
EARLIER = ("seal/specs", "spec.md")


def order(root, ref, ids, specs="seal/threads"):
    """`[(id, commit)]` for IDS in merge order: the first commit reachable from
    REF that adds the id's `frame/design.md`, or its design at the earlier path
    (`EARLIER`), in `git log --topo-order --reverse` order, a directory moved
    under a new id counting as added where it lands. An id no such commit adds
    comes last, with commit None."""
    r = subprocess.run(
        [
            "git", "-C", root, "log", "--full-history", "--topo-order",
            "--reverse", "--no-renames", "--diff-filter=A", "--name-only",
            "--format=%x00%H",
            ref, "--", specs, EARLIER[0],
        ],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )  # fmt: skip
    first, commit = {}, None
    # exempt from splitlines: git output
    for line in r.stdout.splitlines():
        if line.startswith("\0"):
            commit = line[1:]
            continue
        for base, name in ((specs, DESIGN), EARLIER):
            parts = line[len(base) + 1 :].split("/", 1)
            if line.startswith(base + "/") and len(parts) == 2 and parts[1] == name:
                first.setdefault(parts[0], commit)
    known = [i for i in first if i in ids]
    return [(i, first[i]) for i in known] + [(i, None) for i in ids if i not in first]


def merge_order(root, ref, pairs):
    """PAIRS, `[(id, commit)]`, sorted by each commit's place in `git rev-list
    --topo-order --reverse REF`: the merge order of local-mode specs, which
    no commit adds, read from their pull requests' merge commits. A pair
    whose commit REF does not reach comes last, in the order handed."""
    r = subprocess.run(
        ["git", "-C", root, "rev-list", "--topo-order", "--reverse", ref],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    place = {commit: n for n, commit in enumerate(r.stdout.split())}
    return sorted(pairs, key=lambda pair: place.get(pair[1], len(place)))


def _ancestor(root, a, b):
    return (
        a != b
        and subprocess.run(
            ["git", "-C", root, "merge-base", "--is-ancestor", a, b],
            capture_output=True,
        ).returncode
        == 0
    )


def group(specs, same):
    """`[(places, [(id, Op)])]` for SPECS, `[(id, [Op])]` in merge order.

    Two places are one group where SAME (`overlapping`) says they can name
    one text, and a place joins every group it overlaps, so a group is the
    history of one rule. Each group lists its places and its operations in
    the order SPECS hands them, and the groups come in the order of their
    first operation. A spec with operations at two places that cannot name
    one text is in two groups."""
    places = []
    for _, ops in specs:
        for o in ops:
            if place(o) not in places:
                places.append(place(o))
    parent = list(range(len(places)))

    def find(n):
        while parent[n] != n:
            parent[n] = parent[parent[n]]
            n = parent[n]
        return n

    for n, p in enumerate(places):
        for m in range(n):
            if same(p, places[m]):
                parent[find(n)] = find(m)
    # A group is first met at its first place, and places are in the order
    # of the operations that name them, so the dict keeps the groups' order.
    out = {}
    for n, p in enumerate(places):
        out.setdefault(find(n), ([], []))[0].append(p)
    for work_item, ops in specs:
        for o in ops:
            out[find(places.index(place(o)))][1].append((work_item, o))
    return list(out.values())


def unordered(root, commits):
    """`[(a, b)]` for the ids of COMMITS, `[(id, commit)]` in merge order,
    whose commits no ancestry orders: commits on two branches, or a commit
    None, which `order` hands an id no commit adds. The commits are the ones
    that add each spec, or in local mode its pull request's merge commit."""
    out = []
    for n, (a, ca) in enumerate(commits):
        for b, cb in commits[n + 1 :]:
            if a == b:
                continue
            if None in (ca, cb) or not (
                ca == cb or _ancestor(root, ca, cb) or _ancestor(root, cb, ca)
            ):
                out.append((a, b))
    return out
