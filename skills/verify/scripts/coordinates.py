#!/usr/bin/env python3
"""coordinates — where a unit of a file begins and ends, and the hash of what
it holds.

The coordinate kernel: it resolves a `path#unit` coordinate. No command runs
it: the readers that name a place in a file by its content load this module
by path and call it. They are `pact_check.py` and `chain_check.py`, which
read pact anchors.

A place is named by content, never by position. The locator is a **symbol
name** where the language offers one, `.py` read with the stdlib `ast`, and
otherwise a **quoted line of text** or a markdown heading path. The hash
covers the region with trailing whitespace and blank lines removed, so
reformatting is not a change and reindenting is: in Python indentation
carries meaning.
"""

import ast
import functools
import hashlib
import importlib.util
import os
import re
import sys

HASH_LEN = 8
# A clause of a pact held in another repository, cited from a signer
# (#647, `docs/the-pact.md`): `pact:<name>/"<heading path>"@<hash>`. The name
# is the last path segment of the pact's repository's normalised origin URL
# (`hooks/config.py#pact_name`), the locator is this module's quoted heading
# path with its `\|` and `\"` escapes, and the hash is `content_hash` of the
# clause's region in `seal/pact.md`. `pact_check.py` grades these.
PACT_NAME = r"[A-Za-z0-9_.-]+"
PACT_ANCHOR_RE = re.compile(
    r"(?<![A-Za-z0-9_.@/-])pact:(?P<name>" + PACT_NAME + r")/"
    r"(?P<locator>\"(?:[^\"\n]|\\\")+\")"
    r"@(?P<hash>[0-9a-f]{6,12})"
)

# The fence, heading and line rules are the shared reader's,
# `unverified_check.py` beside this file, which every reader of markdown and
# record text asks.
HERE = os.path.dirname(os.path.abspath(__file__))
READER = os.path.join(HERE, "unverified_check.py")


@functools.cache
def shared_reader():
    """The shared reader's module, loaded once by path.

    A reader that is not there, or will not load, raises: a plugin whose
    shared reader is broken has every other gate broken too, and a fallback
    would hide that here alone.
    """
    spec = importlib.util.spec_from_file_location("specseal_unverified_reader", READER)
    reader = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reader)
    return reader


def quoted_lines(lines):
    """The indices of LINES inside a fenced block that CLOSES, delimiters
    included — the lines `unquoted` blanks.

    A line that holds a claim is read on doubt, the first of the three
    answers `docs/the-record-layout.md` *The fold, and what tells it from
    a deletion* gives to whether a line is live: the wrong answer is a
    parked or malformed line read, never one dropped.

    **Only a block that closes is a quotation.** An unclosed fence runs to
    the end of the file, and reading nothing from there on is the silent
    direction on a file whose author made a mistake, so an unclosed block's
    lines are read. An HTML comment is read too: a commented-out line is a
    claim somebody parked, and dropping it is silent.
    """
    reader = shared_reader()
    out, opener, first = set(), None, None
    for n, line in enumerate(lines):
        if opener is None:
            opener, first = reader.fence_opener(line), n
        elif reader.fence_closes(line, opener):
            out.update(range(first, n + 1))
            opener = None
    return out


BLANK_RE = re.compile(r"[^\r\n]")


def gfm_lines(text, keepends=False):
    """TEXT's lines as GFM reads them, the way `str.splitlines` returns them
    otherwise: no trailing empty line, and each line's end kept only when
    KEEPENDS asks.

    `ast` numbers a `.py` file's lines at LF, CR and CRLF alone, and so does
    GFM, while `str.splitlines` also ends a line at a form feed, NEL, U+2028
    and five more characters. So every walk of lines here, the lines a hash
    covers and a locator spans included, reads these.
    """
    return shared_reader().gfm_lines(text, keepends)


def unquoted(text):
    """TEXT with every line inside a closed fence blanked to spaces.

    **Every character offset is kept**: a blanked line is the same length,
    so a position found in this text is the same position in TEXT.
    """
    lines = gfm_lines(text, keepends=True)
    quoted = quoted_lines([line.rstrip("\r\n") for line in lines])
    if not quoted:
        return text
    return "".join(
        BLANK_RE.sub(" ", line) if n in quoted else line for n, line in enumerate(lines)
    )


def normalise(lines):
    """The region as the hash sees it.

    Trailing whitespace goes and blank lines go, so a reformat that only moves
    those is not a change. **Leading whitespace stays**: in Python indentation
    decides what a statement belongs to, and a hash that ignored it would call
    a dedent no change at all — a checker going quiet exactly where the edit
    matters most.
    """
    return "\n".join(line.rstrip() for line in lines if line.strip())


def content_hash(lines):
    return hashlib.sha256(normalise(lines).encode("utf-8")).hexdigest()[:HASH_LEN]


def py_spans(text):
    """{qualified name: [(start, end)]} for defs, classes and constants — or
    None for a file that will not parse.

    Decorators are part of the span: a decorator carries behaviour, and a
    locator naming the function it decorates should notice one being added
    or removed. A module- or class-level assignment is a unit too, and its
    span is the whole statement, multi-line value included. An assignment
    inside a function is a local, not a unit, and is not collected.

    None rather than `{}` for a SyntaxError, because the two mean different
    things to `resolve_unit`: a file that cannot be parsed is refused with
    the interpreter's version and the error's line on it (#870), while a
    file that parses and lacks the symbol has no place for it.

    **One parse per distinct text, for the life of the process** (#519). A
    caller asks for many units of one file, and parsing it once per unit was
    1,328 parses of 126 files in one caller's run (`cProfile`, 2026-09-23).
    The memo is keyed on the TEXT and never on the path: one path
    read twice with different content in one process would otherwise be
    handed the first read's spans, a silent wrong answer. Each caller gets a
    fresh dict of fresh lists, so none can change the stored answer for the
    next one.
    """
    spans = parsed_spans(text)
    if spans is None:
        return None
    return {name: list(places) for name, places in spans.items()}


@functools.cache
def parsed_spans(text):
    """`py_spans`'s answer, stored once per distinct text, or None.

    Call `py_spans`, which hands each caller a copy; this is its memo and
    nothing else's, and a caller holding this dict could change the answer
    every later call gets.
    """
    out = {}
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return None

    def walk(node, prefix, in_function):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                name = prefix + child.name
                start = min([child.lineno] + [d.lineno for d in child.decorator_list])
                out.setdefault(name, []).append((start, child.end_lineno))
                walk(child, name + ".", not isinstance(child, ast.ClassDef))
            elif isinstance(child, (ast.Assign, ast.AnnAssign)) and not in_function:
                targets = (
                    child.targets if isinstance(child, ast.Assign) else [child.target]
                )
                for t in targets:
                    elts = t.elts if isinstance(t, (ast.Tuple, ast.List)) else [t]
                    for n in elts:
                        if isinstance(n, ast.Name):
                            out.setdefault(prefix + n.id, []).append(
                                (child.lineno, child.end_lineno)
                            )
            else:
                walk(child, prefix, in_function)

    walk(tree, "", False)
    return out


def heading_level(line):
    """The level of the markdown heading LINE is, or None: CommonMark 4.2's
    ATX heading, by `unverified_check.py#heading_level` (#867).
    """
    return shared_reader().heading_level(line)


def markdown_lines(text):
    """TEXT's lines as GFM ends them, with every line inside a closed fence
    blanked (`unquoted`) — the lines a renderer shows a heading on (#867).
    The count and the line numbers are `gfm_lines(text)`'s, so a region found
    here is the same region there, and its hash is taken over the lines as
    written: where a region ENDS moves, its bytes do not.

    **Computed once per distinct text** (round 1 of #867, ⬜ 11): every
    quoted `.md` anchor asks for its file's shown lines, and recomputing
    them per anchor took a `--strict` run over this repository from 13.2 s
    to 15.4 s. The memo is keyed on the TEXT, as `parsed_spans`' is, and
    each caller gets a fresh list."""
    return list(_shown_lines(text))


@functools.cache
def _shown_lines(text):
    """`markdown_lines`' answer, stored once per distinct text, as a tuple
    no caller can change."""
    return tuple(gfm_lines(unquoted(text)))


def text_regions(lines, anchor, markdown=False, shown=None):
    """Every region a text anchor matches, 1-based and inclusive.

    A markdown heading owns everything down to the next heading at its level or
    above, which is what a reader means by a section. Anything else owns the
    contiguous run of non-blank lines it sits in — a paragraph, a table, a
    block of code. **A quoted line is a paragraph and never a function** (#870):
    nothing here reads the language, so a unit with no blank line inside it
    is hashed whole by one quote, and a unit with blank lines is cited one
    quote per paragraph.

    **The heading rule is markdown-only.** `#` opens a comment in Python, shell
    and YAML, and reading one as a heading made a 23-line comment block resolve
    to its first line alone.

    **A heading is read on SHOWN, the lines a renderer shows** (#867):
    `markdown_lines` of the same text, which the caller passes for a markdown
    file. A `## B` quoted in a closed fence opens no section and ends none.
    The text is still matched on LINES as written, so an anchor on a line
    inside a fence finds its paragraph as it did.
    """
    shown = lines if shown is None else shown
    want = " ".join(anchor.split())
    out = []
    for i, line in enumerate(lines):
        if " ".join(line.split()) != want:
            continue
        level = heading_level(shown[i]) if markdown else None
        if level is not None:
            j = i + 1
            while j < len(lines):
                k = heading_level(shown[j])
                if k is not None and k <= level:
                    break
                j += 1
            out.append((i + 1, j))
        else:
            a = b = i
            while a > 0 and lines[a - 1].strip():
                a -= 1
            while b + 1 < len(lines) and lines[b + 1].strip():
                b += 1
            out.append((a + 1, b + 1))
    return out


def unescape(anchor):
    """The anchor as written in the file it points at."""
    return anchor.replace("\\|", "|").replace('\\"', '"')


HEADING_SEP = " / "


def heading_path(lines, parts):
    """[(start, end)] for a `## A / ### B` heading path in a markdown file.

    Each part narrows inside the section the previous one opened, so a heading
    that repeats across a document is disambiguated by its parent rather than
    by a line number. Zero matches or several is the caller's BROKEN.

    LINES are `markdown_lines` (#867): a heading quoted in a closed fence is a
    blank line there, so it is no part of any path and ends no section.
    """
    regions = [(1, len(lines))]
    for part in parts:
        want = " ".join(part.split())
        found = []
        for lo, hi in regions:
            for i in range(lo - 1, hi):
                if " ".join(lines[i].split()) != want:
                    continue
                level = heading_level(lines[i])
                if level is None:
                    continue
                j = i + 1
                while j < hi:
                    k = heading_level(lines[j])
                    if k is not None and k <= level:
                        break
                    j += 1
                found.append((i + 1, j))
        regions = found
        if not regions:
            return []
    return regions


# The suffixes each bounding rule reads (#870). `bounding_rule` is the one
# place a path's suffix decides how a unit in it is bounded.
AST_SUFFIXES = frozenset([".py", ".pyi"])
HEADING_SUFFIXES = frozenset([".md"])


def bounding_rule(path):
    """The rule that bounds a unit in PATH: "ast", "heading", or None where
    no rule does (#870).

    A unit is bounded only where a real parser decides its extent. "ast" is
    the running interpreter's own parse, and "heading" is a locator over a
    person's document, read by CommonMark's heading rule (#867). None is the
    refusal: a bare symbol in any other file is BROKEN with the quoted-line
    anchor's shape on its line, never read through a rule that imitates a
    language's grammar without its parser. A quoted locator needs no rule — the run of non-blank lines it
    sits in is a structure the file itself shows.
    """
    suffix = os.path.splitext(path)[1]
    if suffix in AST_SUFFIXES:
        return "ast"
    if suffix in HEADING_SUFFIXES:
        return "heading"
    return None


def unbounded(path, rule, text):
    """The sentence a refused bare-symbol locator in PATH reads, naming why
    no unit can be bounded and the anchor to write instead (#870).
    """
    remedy = "anchor a quoted line instead"
    if rule == "ast":
        try:
            ast.parse(text)
        except SyntaxError as err:
            why = err.msg + (f" at line {err.lineno}" if err.lineno else "")
        else:  # asked only of a text `py_spans` already refused
            why = "it did not parse"
        version = ".".join(str(n) for n in sys.version_info[:3])
        return (
            f"Python {version} cannot parse this file ({why}), so no unit in it "
            "is bounded and none is guessed at — run the checker on the Python "
            f"the file is written for, or {remedy}"
        )
    if rule == "heading":
        return (
            "a markdown unit is a heading, and a bare symbol names none — "
            'anchor its heading path instead, `"## <heading>"`'
        )
    suffix = os.path.splitext(path)[1]
    named = f"`{suffix}`" if suffix else "a file with no suffix"
    return (
        f"no bounding rule for {named}; {remedy}, "
        '`"<a line of the unit>"`, whose region is the paragraph that line '
        "sits in"
    )


class Resolution:
    """`resolve_unit`'s one reading of a coordinate (#870): `places`, the
    `[(start, end)]` the locator resolves to, and `refused`, None or the
    sentence saying why no unit in the file can be bounded.

    A refused reading has no places, so a caller that never asks for the
    reason still reads nothing there rather than a span nobody bounded; one
    that prints a verdict asks for it, and that is one reading of the
    coordinate rather than a second call (#809). It is no tuple: a field
    beside `places` that no code can set would be read by its callers as a
    fact about the place, which is how the resurrection flag outlived the
    rule that set it until #870 took both out.
    """

    __slots__ = ("places", "refused")

    def __init__(self, places, refused=None):
        self.places = places
        self.refused = refused

    def __repr__(self):
        return f"Resolution({self.places!r}, refused={self.refused!r})"


def resolve_unit(path, locator, text, shown=None):
    """`Resolution(places, refused)` — the places the locator resolves to,
    and why no unit could be bounded, or None.

    SHOWN is the path the caller's own record writes, where it differs from
    PATH: the refusal's remedy is the edit to make, so it is written on that
    path (round 2 of #870).

    **A unit no rule can bound is refused, never guessed at** (#870). Which
    rule bounds PATH is `bounding_rule`'s answer and nobody else's. A `.py`
    file the running interpreter cannot parse used to fall through to the
    text rule, which hashed lines 1-3 of a five-line `def f(` whose
    parameters ran over three lines and left the body out; a suffix no rule
    names was read by an indentation rule, and then by a bracket walk over a
    hand-written lexer, each imitating a grammar without its parser. Both
    now come back with no places and the reason, which a caller prints with
    the quoted-line anchor's shape on the line.

    **A locator's job is to put a reader in the right logic, not to pin a
    line.** So the address is the enclosing unit: the function for code, the
    heading for a document. That unit is stable against every edit that does
    not change what the unit IS. A markdown locator is a heading path rather
    than a sentence for the same reason: a sentence breaks on any rewording,
    while a heading is the document's own structure and survives its prose
    being rewritten, and the hash still reports the prose changing.
    """
    lines = gfm_lines(text)
    rule = bounding_rule(path)
    if locator.startswith('"'):
        body = unescape(locator[1:-1])
        if rule == "heading":
            # A heading is read where a renderer shows one (#867).
            shown = markdown_lines(text)
            parts = [p for p in body.split(HEADING_SEP) if p.strip()]
            if parts and heading_level(parts[0].strip()) is not None:
                return Resolution(heading_path(shown, parts))
            return Resolution(text_regions(lines, body, True, shown))
        return Resolution(text_regions(lines, body))
    if rule == "ast":
        spans = py_spans(text)
        if spans is None:
            return Resolution([], unbounded(shown or path, rule, text))
        # The parse succeeded, so ast's answer is the whole answer: a symbol
        # it cannot find is GONE, and a leftover call site is never read as
        # the unit (round 4, 🔴 2).
        return Resolution(spans.get(locator, []))
    return Resolution([], unbounded(shown or path, rule, text))
