#!/usr/bin/env python3
"""passages — the one reader of a passage two rule documents share.

`tests/text/test_no_passage_is_pasted_into_a_second_file.py` holds the method
and why it is verbatim: which files are rule documents (`in_corpus`), how a
file is normalised into words (`words`), and the runs of `WINDOW` words two
files are compared by (`windows`). `skills/code-review/scripts/chain_check.py`
reads a design's `to` through the same functions, through
`skills/settle/scripts/rule_changes.py#copies`, so the notice and the test
agree on what a copy is. A file's lines and the fenced blocks among them
are `lib/lines.py#readable`'s, and a heading line is told by
`lib/lines.py#heading_level`, loaded through `lib/sibling.py`, so this
module spells no line split, fence rule or heading rule of its own.
Nothing here reads a document or runs a command: each caller lists and
reads its own files.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# `lib/` first on `sys.path`, where `lib/sibling.py` is imported from; the
# import stands at the first read of a text, so a copy of this module taken
# on its own loads nothing until it reads one.
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "lib"))
READER = "lib/lines.py"

# A run of this many consecutive words is longer than any phrase two rule
# documents share by writing about the same mechanism, and shorter than the
# smallest real copy measured. The measurement and the case that keeps both
# ends of its margin are `tests/text/test_a_moved_rule_leaves_its_definition.py`'s.
WINDOW = 15

TOP_FILES = ("CLAUDE.md", "CONTRIBUTING.md", "README.md")
TOP_DIRS = ("docs/", "skills/", "agents/", "templates/")

# A section quoted by name after a `.md` path (with or without its
# possessive), with the italic name of a row or paragraph of it where one
# comes first, as "*<name>* of <path> *<section>*", so a link to one row is
# one token. `[^*]` crosses a line break, so a wrapped name is one name.
SECTION = re.compile(
    r"(?:\*[^*]{1,200}\*\s+of\s+)?`?[\w./-]+\.md`?(?:'s)?\s+\*[^*]{1,200}\*"
)
SECTION_TOKEN = " section-citation "
STRIP = str.maketrans("", "", "`*|>#")


def _reader():
    """`lib/lines.py`, loaded once."""
    import sibling

    return sibling.load(READER)


def in_corpus(rel):
    """Whether the repository path REL is a rule document: a `*.md` under
    `docs/`, `skills/`, `agents/` or `templates/`, or one of `TOP_FILES`, and
    no `*.ko.md`, whose Korean edition mirrors its English one in other
    words."""
    return (
        rel.endswith(".md")
        and not rel.endswith(".ko.md")
        and (rel in TOP_FILES or rel.startswith(TOP_DIRS))
    )


def words(text):
    """TEXT as a list of words: its lines as `lib/lines.py#readable` gives
    them, fenced blocks blanked, with heading lines dropped; a quoted
    section name made one token with the italic row name a link puts before
    it (`SECTION`); then lowercased and stripped of `` ` ``, `*`, `|`, `>`
    and `#`."""
    reader = _reader()
    kept = [
        line for line in reader.readable(text) if reader.heading_level(line) is None
    ]
    text = SECTION.sub(SECTION_TOKEN, "\n".join(kept))
    return text.lower().translate(STRIP).split()


def windows(word_list):
    """The distinct runs of `WINDOW` consecutive words of WORD_LIST, each
    joined by one space."""
    return {
        " ".join(word_list[i : i + WINDOW]) for i in range(len(word_list) - WINDOW + 1)
    }
