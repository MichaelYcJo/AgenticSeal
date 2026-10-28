#!/usr/bin/env python3
"""coordinates — where a clause of a markdown file begins and ends, and the
hash of what it holds.

No command runs it. Its one reader, `pact_check.py`, loads it by path to
grade a pact anchor: the anchor's `Clause` cell is a heading path, which
`heading_path` resolves over the lines `markdown_lines` shows, and its
`Hash` cell is `content_hash` of that region, `HASH_LEN` hex digits long.

A clause is named by its headings, never by position. The hash covers the
region with trailing whitespace and blank lines removed, so reformatting is
not a change and reindenting is.
"""

import functools
import hashlib
import importlib.util
import os
import re

HASH_LEN = 8

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
    spec = importlib.util.spec_from_file_location("agentic_unverified_reader", READER)
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

    GFM ends a line at LF, CR and CRLF alone, while `str.splitlines` also
    ends one at a form feed, NEL, U+2028 and five more characters. So every
    walk of lines here, the lines a hash covers and a clause spans included,
    reads these.
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

    **Computed once per distinct text** (round 1 of #867, white 11): every
    anchor graded against one version of the pact asks for its shown lines.
    The memo is keyed on the TEXT, never on a path, and each caller gets a
    fresh list."""
    return list(_shown_lines(text))


@functools.cache
def _shown_lines(text):
    """`markdown_lines`' answer, stored once per distinct text, as a tuple
    no caller can change."""
    return tuple(gfm_lines(unquoted(text)))


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
