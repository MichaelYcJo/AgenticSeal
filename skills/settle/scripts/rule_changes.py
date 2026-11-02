#!/usr/bin/env python3
"""rule_changes — the one reader of a design's `## Rule changes` section.

The grammar is `skills/settle/SKILL.md` *Rule changes*. `GRAMMAR` below is
the one spelling of its operations in code; the item lines, their fields and
the no-change block are spelt once in `unverified_check.py`, which reads
`## Not verified` with the same block. `parse` reads a section into operations,
refusing at its line any block that does not match whole, and names, without
refusing it, a line that opens like one of the section's forms and is not it.
Each operation carries its fields' lines at their lines in the design
(`Op.lines`), by which `skills/code-review/scripts/chain_check.py` names a
check line inside a `to` at its line. `order` reads merge
order from git, `merge_order` reads it in local mode from the merge commits
`settle` hands it, `group` joins the released designs whose operations name one
place into one group, `unordered` names the pairs inside a group that no
ancestry orders, and `section_lines` finds a section's lines in a document.
`pending` reads the designs not yet settled, and `removed_by` says which of
their `remove` items with no `from` takes a line's section out, for the two
readers that excuse such a line: `.github/scripts/rules.py` and
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`.
`literals`, `pins` and `copies` say what an operation takes out of a test
and what its `to` repeats of another rule document, over texts their caller
hands them, for `chain_check.py` to name as notices (#1216); a copy is read
through `passages.py`, the paste check's reader, loaded by path.
`settle` prints what they read; nothing here writes a file.

Headings and fences are read through
`skills/verify/scripts/unverified_check.py` (`live_lines`, `heading_level`,
`liveness`, `gfm_lines`, `blank_fences`, `comment_lines`), loaded by path,
so this module spells no fence or heading rule of its own. A design is a
record and carries no HTML comment, so `parse` reads it with no comment
state and refuses a section line that begins with `<!--` (#1012); `headings`
keeps the comment state for `section_lines` and `overlapping`, which read the
policy documents.
"""

import ast
import collections
import glob
import importlib.util
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
READER = os.path.join(HERE, "..", "..", "verify", "scripts", "unverified_check.py")
PASSAGES = os.path.join(HERE, "passages.py")

HEADING = "Rule changes"
# Each operation's fields: (required, optional). The item lines, their fields
# and the no-change block are `unverified_check.py`'s (`items`,
# `field_values`, `nothing_block`).
GRAMMAR = {
    "add": (("file", "to"), ("section",)),
    "change": (("file", "section", "from", "to"), ()),
    "remove": (("file", "section"), ("from",)),
}

# `lines` maps each field's name to its value's lines as they land, each
# with its line in the design: `[(line number, text)]`, whose texts joined
# with `\n` are the value `old`, `new`, `file` or `section` holds.
Op = collections.namedtuple("Op", "kind file section old new line lines")
# `ops` is None where the design has no section; `nothing` is the `why` of a
# section holding the no-change block; `errors` is `[(line, reason)]`;
# `unread` is `[(line, why)]` for each line that opens like one of the
# section's forms and is not it, which decides nothing (`parse`).
Parsed = collections.namedtuple("Parsed", "ops nothing errors unread")
# What `parse` says of a heading near `## Rule changes`, at its line.
NEAR_HEADING = (
    "`{written}` opens like `## {heading}` and is not it, so it is another "
    "section and none of its lines were read; the one heading read is "
    "`## {heading}`, spelt exactly so"
)

_reader = None
_passages = None


def reader():
    global _reader
    if _reader is None:
        spec = importlib.util.spec_from_file_location("agentic_rules_reader", READER)
        _reader = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_reader)
    return _reader


def passages():
    """`passages.py`, the paste check's reader, loaded by path once."""
    global _passages
    if _passages is None:
        spec = importlib.util.spec_from_file_location("agentic_passages", PASSAGES)
        _passages = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_passages)
    return _passages


def heading_text(line):
    """A heading line's text, without its `#` runs, trimmed."""
    text = line.strip().lstrip("#").strip()
    return re.sub(r"(^|\s+)#+\s*$", "", text).strip()


def headings(lines, comments=True):
    """`[(index, level, text)]` for every live heading in LINES. `comments`
    is `live_lines`'s: `parse` reads a design with none."""
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
    """The `## Rule changes` section of a design's TEXT, as a `Parsed`; each
    `file` is a top-level `.md` of the directory POLICY_ROOT.

    The section is read under `## Rule changes` alone. A heading at any
    level whose letters, case folded, are that heading's, that is not it and
    that stands outside the section is another section: none of its lines
    is read, nothing is refused for it, and it goes to `unread` at its line
    (`NEAR_HEADING`), so the settle reads the design whole. Such a heading
    below level 2 inside the section is a line of the section, refused as
    the items refuse a line outside them, and is not named. A first
    line of the section that opens like the no-change block and is not it
    goes there too (`unverified_check.py#unread_block`), beside the refusal
    the items give it. Whether either meant the form is the judgment of the
    agent that reads the design."""
    r = reader()
    lines = r.gfm_lines(text)
    marks = headings(lines, comments=False)
    found = [(n, lv) for n, lv, t in marks if lv == 2 and t == HEADING]
    # A section runs to the next heading of level 2 or higher, so a heading
    # below level 2 inside one is a line of it, read and refused as the
    # items refuse a line outside them, and not named.
    inside = set()
    for start, _ in found:
        end = next((n for n, lv, _ in marks if n > start and lv <= 2), len(lines))
        inside.update(range(start + 1, end))
    unread = [
        (n + 1, NEAR_HEADING.format(written=lines[n].strip(), heading=HEADING))
        for n, lv, t in marks
        if letters(t) == letters(HEADING) and (n, lv) not in found and n not in inside
    ]

    def done(ops, nothing, errors):
        return Parsed(ops, nothing, errors, unread)

    if not found:
        return done(None, None, [])
    if len(found) > 1:
        return done([], None, [(found[1][0] + 1, "a second `## Rule changes`")])
    start = found[0][0]
    end = next((n for n, lv, _ in marks if n > start and lv <= 2), len(lines))
    live = [flag for _, flag in r.live_lines(lines, comments=False)]
    # `live_lines` ANDs two readings, here with no comment state, since a
    # design carries no comment (#1012). In this one a code span never leaves
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
            return done([], None, [(n + 1, why)])
        if n in commented:
            return done([], None, [(n + 1, r.COMMENT_LINE)])
        if not literal[n]:
            continue
        body.append((n + 1, line))
    while body and not body[-1][1].strip():
        body.pop()
    while body and not body[0][1].strip():
        body.pop(0)
    if not body:
        return done([], None, [(start + 1, "the section is empty")])

    block = r.nothing_block(body)
    if block is not None:
        why, error = block
        return done([], None, [error]) if error else done([], why, [])
    # A first line that opens like the block and is not it is read as the
    # items read it, and named.
    near = r.unread_block(body)
    if near is not None:
        unread.append(near)

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
        return done([], None, [error])

    out = []
    numbers = [no for no, _ in body]
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
            return done([], None, [error])
        out.append(
            Op(
                item["kind"],
                file,
                values.get("section"),
                values.get("from"),
                values.get("to"),
                item["line"],
                {
                    name: value_lines(numbers, first, parts)
                    for name, (first, parts) in item["fields"].items()
                },
            )
        )
    return done(out, None, [])


def value_lines(numbers, first, parts):
    """`[(line number, text)]` for one field whose value lines are PARTS, the
    first at line FIRST, NUMBERS being the line numbers of the section's body
    in order: each part takes the number of its body line, and the leading
    empty parts and the trailing blank ones are dropped and the last part's
    end trimmed, as `unverified_check.py#field_values` strips its value."""
    at = numbers.index(first)
    lines = list(zip(numbers[at : at + len(parts)], parts))
    while lines and lines[0][1] == "":
        lines.pop(0)
    while lines and not lines[-1][1].strip():
        lines.pop()
    if lines:
        lines[-1] = (lines[-1][0], lines[-1][1].rstrip())
    return lines


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


# --- what an operation takes out of a test and repeats of a document ----------

# A string constant of a test reads as a pin of a rule's text from this many
# words: the floor #1278's lister used. At three words the 0.27.1 settle's
# record names 44 pins against 26 and none more of the literals that failed
# (#1216 design G10).
LITERAL_WORDS = 4


def _collapsed(text):
    return " ".join(text.split())


def literals(source):
    """`[(line, text)]` for each string constant of the Python SOURCE that is
    no docstring and holds at least `LITERAL_WORDS` words, its whitespace runs
    collapsed to one space, at the line it starts on. An implicit
    concatenation is one constant, as the parser joins it. Raises the
    parser's SyntaxError or ValueError where SOURCE does not parse; naming
    that file is the caller's."""
    tree = ast.parse(source)
    docstrings = set()
    for node in ast.walk(tree):
        if isinstance(
            node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
        ):
            first = node.body[0] if node.body else None
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant):
                docstrings.add(id(first.value))
    found = set()
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Constant)
            and isinstance(node.value, str)
            and id(node) not in docstrings
        ):
            text = _collapsed(node.value)
            if len(text.split()) >= LITERAL_WORDS:
                found.add((node.lineno, text))
    return sorted(found)


def pins(op, taken, found):
    """The entries of FOUND, `[(path, line, text)]` as `literals` gives a
    test file's, whose text stands in TAKEN and not in OP's `to`, both with
    their whitespace runs collapsed. TAKEN is what OP takes out of the policy
    root: its `from`, or for a `remove` with no `from` its section's text;
    None where it takes out nothing."""
    if not taken:
        return []
    taken, kept = _collapsed(taken), _collapsed(op.new or "")
    return [f for f in found if f[2] in taken and f[2] not in kept]


def copies(op, texts, gone=None):
    """`[(path, count, run)]` for each rule document of TEXTS, `{path: text}`,
    other than OP's file, that shares a run of `passages.py#WINDOW` words with
    OP's `to`, read as `passages.py#words` reads both: the number of distinct
    runs shared and the first of them in the `to`'s order. GONE, `{path:
    [text]}`, is what the same design's operations take out of each document:
    each such text is taken out of the document once, found by `pattern`
    across any wrapping, before the runs are counted, so a design that moves a
    passage from one document to another leaves no copy where it took it
    from. [] for an operation with no `to`, or whose file
    `passages.py#in_corpus` leaves out."""
    p = passages()
    if op.new is None or not p.in_corpus(op.file):
        return []
    said = p.words(op.new)
    order = [" ".join(said[i : i + p.WINDOW]) for i in range(len(said) - p.WINDOW + 1)]
    out = []
    for path in sorted(texts):
        if path == op.file or not p.in_corpus(path):
            continue
        text = texts[path]
        for taken in (gone or {}).get(path, ()):
            if taken and taken.split():
                text = pattern(taken).sub("\n", text, count=1)
        shared = p.windows(p.words(text)).intersection(order)
        if shared:
            out.append((path, len(shared), next(r for r in order if r in shared)))
    return out


# --- the pending designs, not yet settled -------------------------------------


def pending(root, policy_root):
    """`[(Op, work item directory)]` for every item of a pending `## Rule
    changes`: each `frame/design.md` under `<root>/seal/threads/`, read
    through `parse` against POLICY_ROOT. A design that cannot be read as
    UTF-8, or a section `parse` refuses, gives no item."""
    found = []
    pattern = os.path.join(glob.escape(root), "seal", "threads", "*", DESIGN)
    for path in sorted(glob.glob(pattern)):
        try:
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError):
            continue
        item = (
            f"seal/threads/{os.path.basename(os.path.dirname(os.path.dirname(path)))}/"
        )
        found += [(o, item) for o in parse(text, policy_root).ops or []]
    return found


def removed_by(items, rel, text, line):
    """The work item directory of the first of ITEMS, as `pending` gives
    them, that is a `remove` with no `from` whose section of REL holds LINE,
    REL's text being TEXT; or None. That section leaves at the settle. An
    item whose `from` holds the line is not read here."""
    for o, item in items:
        if o.file != rel or o.kind != "remove" or o.old is not None:
            continue
        span, _ = section_lines(text, o.section)
        if span and span[0] <= line <= span[1]:
            return item
    return None


# --- the released designs, by place and in merge order ------------------------


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
    --topo-order --reverse REF`: the merge order of local-mode designs, which
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
    first operation. A design with operations at two places that cannot name
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
    that add each design, or in local mode its pull request's merge commit."""
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
