#!/usr/bin/env python3
"""passages — the one reader of a passage two rule documents share.

`tests/text/test_no_passage_is_pasted_into_a_second_file.py` holds the method
and why it is verbatim: which files are rule documents (`in_corpus`), how a
file is normalised into words (`words`), and the runs of `WINDOW` words two
files are compared by (`windows`). `skills/code-review/scripts/chain_check.py`
reads a design's `to` through the same functions, through
`skills/settle/scripts/rule_changes.py#copies`, so the notice and the test
agree on what a copy is. A heading line is told by
`skills/verify/scripts/unverified_check.py#heading_level`, loaded by path,
so this module spells no heading rule of its own. Nothing here reads a
document or runs a command: each caller lists and reads its own files.
"""

import importlib.util
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
READER = os.path.join(HERE, "..", "..", "verify", "scripts", "unverified_check.py")

# A run of this many consecutive words is longer than any phrase two rule
# documents share by writing about the same mechanism, and shorter than the
# smallest real copy measured. The measurement and the case that keeps both
# ends of its margin are `tests/text/test_a_moved_rule_leaves_its_definition.py`'s.
WINDOW = 15

TOP_FILES = ("CLAUDE.md", "CONTRIBUTING.md", "README.md")
TOP_DIRS = ("docs/", "skills/", "agents/", "templates/")

FENCE = re.compile(r"^ *(`{3,}|~{3,})")
# A section quoted by name after a `.md` path (with or without its
# possessive). `[^*]` crosses a line break, so a wrapped name is one name.
SECTION = re.compile(r"`?[\w./-]+\.md`?(?:'s)?\s+\*[^*]{1,200}\*")
SECTION_TOKEN = " section-citation "
STRIP = str.maketrans("", "", "`*|>#")

_reader = None


def _heading_level(line):
    """`unverified_check.py#heading_level` of LINE, its module loaded once."""
    global _reader
    if _reader is None:
        spec = importlib.util.spec_from_file_location("agentic_passages_reader", READER)
        _reader = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_reader)
    return _reader.heading_level(line)


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


def _lines(text):
    """TEXT's lines, ended where GFM ends one: LF, CR or CRLF alone."""
    return text.replace("\r\n", "\n").replace("\r", "\n").split("\n")


def words(text):
    """TEXT as a list of words: fenced blocks and heading lines dropped, a
    quoted section name made one token, then lowercased and stripped of
    `` ` ``, `*`, `|`, `>` and `#`."""
    kept, fence = [], None
    for line in _lines(text):
        opened = FENCE.match(line)
        if fence:
            if (
                opened
                and opened.group(1)[0] == fence[0]
                and len(opened.group(1)) >= len(fence)
                and not line.strip().strip(fence[0])
            ):
                fence = None
            continue
        if opened:
            fence = opened.group(1)
            continue
        if _heading_level(line) is not None:
            continue
        kept.append(line)
    text = SECTION.sub(SECTION_TOKEN, "\n".join(kept))
    return text.lower().translate(STRIP).split()


def windows(word_list):
    """The distinct runs of `WINDOW` consecutive words of WORD_LIST, each
    joined by one space."""
    return {
        " ".join(word_list[i : i + WINDOW]) for i in range(len(word_list) - WINDOW + 1)
    }
