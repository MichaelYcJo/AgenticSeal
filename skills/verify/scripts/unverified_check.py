#!/usr/bin/env python3
"""seal unverified — read what a closing memo recorded as unverified, and fail
on a record that cannot be read.

`verify` condition 4 lets a claim go out unproven as long as the row names who
answers it. Nothing ever read those rows again. The measured failure: a row in
the closing memo of work item 1787495842 (verify-the-unverified), a record
older than this repository's first commit, said nobody had seen the
gates render in an interactive TUI and named the user as the answerer. Months
later the user hit exactly that, from the other side, and asked why every gate
renders as yes/no. The record was accurate and no procedure ever closed it.

So this reads every `## Not verified` section and reports what is still open.
It does **not** fail because items are open. Dozens were open the day it was
written, and a build that goes red for an honest `unverified` row teaches
people to write none, which voids the condition it is defending. Counting them
is what `seal unverified seal/threads/` is for; no number is repeated in prose here,
because a number in a comment is right for one commit and nobody recounts it.

It fails for what the author can always fix: a section that cannot be read.
A tolerant parser reports zero there, and zero reads as "everything has been
closed", the worst available failure, because it is indistinguishable from
success.

A row or a closing memo deleted rather than closed is read by nobody here:
the proofer reads it in the closing memo's diff (`skills/implement/SKILL.md`
*4. The closing memo*).

An item is closed by marking it, never by deleting it: the Item cell opens
with the word `closed`, and the second cell says what closed it. Anything
unmarked counts open, so the silent direction is "still open", except for an
open item whose own text begins with the word `closed`, which reads as closed
and which only a reader catches.

Deliberately a text scan of markdown, not a parser library: the gates here are
stdlib-only, and the format it accepts is one line long. That format is strict
on purpose — see `check_file`.

Exit codes: 0 the record is readable (open items are reported, not punished) ·
1 a section could not be read · 2 the path or arguments were unusable, which
includes a scan that found no closing memo at all. Three states of a `seal/`
root's own `threads` path are exit 0 instead, each saying which it is,
because a pull request in any of them declares nothing and owes nothing: the
path holding no work item, empty or absent, which is the state a complete
settle ends in (`settled_root`); no `seal/` directory at the working tree's
top level (`absent_root`); and work items none of which carries a `gaps.md`
(`unwritten_root`).
"""

import argparse
import importlib.util
import os
import re
import subprocess
import sys

# `lib/` beside this script, from which the fence rule, the line split,
# the `Reference specs` row's reader and the root's resolver are loaded by
# path (#688, #1005).
HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, "..", "..", "..", "lib")


def _load_lib(name, as_name):
    """`lib/<name>`, run as module AS_NAME. A module under `lib/` imports
    nothing from `skills/`, so this module asks `lib/`'s copy rather than the
    other way round: `blocks.py`, the one place the fence delimiter rule and
    the GFM line split are written, and `fields.py`, the one place a record's
    comment line is said."""
    spec = importlib.util.spec_from_file_location(as_name, os.path.join(LIB, name))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_BLOCKS = _load_lib("blocks.py", "agentic_blocks_for_unverified")
# The fence delimiter rule, CommonMark 4.5 (#491, #444, #584): `fence_opener`
# says which fence a line opens and `fence_closes` whether a line closes it.
# The readers of this module ask them, `fence_spans` and through it
# `blank_fences` and `closed_fence_lines`, `_scan` and through it `liveness`
# and `live_pieces`, and `_paragraph_ends_at`; so do
# `coordinates.py#quoted_lines`, `payload_meter.py#heading_starts`,
# `payload_meter.py#imports_of` through `live_pieces`
# and `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py`;
# and `lib/blocks.py#walk` adds a line-start HTML comment block to it for
# `lib/config.py`, `lib/routing.py` and `lib/fields.py`, apart
# from `live_lines` on purpose, since a row they read is safe at its old reading
# where the walk is unsure, and `fields.py` refuses a fence line the walk cannot
# place. Readers that keep a rule of their own, each on purpose: the pull request
# body readers through `close_issues_on_release.py#FENCE`, which open a fence
# at any indentation as GitHub does, so a fence under a list item masks a
# closing keyword (`docs/releasing/issues-and-milestones.md` *A keyword claims the
# one number after it*); `tests/behaviour/test_docs_line_wrap.py#fenced_numbers`,
# which strips a line's indentation first; and the oracle walk in
# `tests/skills/test_unverified_check.py`. A new reader
# that decides by line whether it stands inside a fence belongs in one of
# these two lists.
fence_opener = _BLOCKS.fence_opener
fence_closes = _BLOCKS.fence_closes
# Where GFM ends a line: LF, CR or CRLF, and nowhere else (#664). Every reader
# of markdown or record text reads its lines through `gfm_lines`, this
# module's callers and the scripts that load it among them, because two
# readers of one text that split it two ways disagree about which line an
# index names; the `splitlines` census in `tests/censuses.py` holds the
# remaining splitters to it.
GFM_LINE_RE = _BLOCKS.GFM_LINE_RE
gfm_lines = _BLOCKS.gfm_lines

# A thread's closing memo, at the thread's top, and the directory under a
# `seal/` root that holds the threads: `lib/optin.py#GAPS` and
# `#WORK_ITEMS`, which a case holds these two to.
OVERVIEW = "gaps.md"
ITEMS = "threads"
HEADING = "## Not verified"
HEADER = ("Item", "Who must answer")
CLOSED = "closed"
# The emoji a closed row opened with before the word, U+2705, spelt by its code
# point so no emoji stands in this file. `parse_section` refuses a row opening
# with it, naming the edit.
OLD_MARK = chr(0x2705)
# A design section's items, `skills/settle/rule-changes.md` *Rule changes*: the
# item's line, then one field per line indented two spaces, a value continuing
# on the lines below it indented four.
ITEM_RE = re.compile(r"^- (\S+)\s*$")
FIELD_RE = re.compile(r"^  ([a-z]+):(?: (.*))?$")
CONTINUED = " " * 4
# The item a section that holds nothing writes alone, and its one field.
# `## Not verified` and `## Rule changes` read it through `nothing_block`.
NOTHING = "nothing"
WHY = "why"
NOTHING_WRITTEN = f"the block `- {NOTHING}` with `  {WHY}: <reason>`"
# A first line that opens like the block and is not it: `none` or `nothing`
# in any case, behind any list marker. The old `none — <why>` line is one.
# Such a line is no block, and its reader names it (`unread_block`).
NEAR_NOTHING = re.compile(r"[-*+\s]*(?:none|nothing)\b", re.IGNORECASE)
UNREAD_BLOCK = (
    f"`{{said}}` opens like {NOTHING_WRITTEN} and is not it, so it was read as prose"
)
# What `parse_section` says of a section whose first line is neither the
# table's header nor the block.
FOUND_PROSE = (
    "expected `| Item | Who must answer |`, found prose. Prose belongs under "
    "`## Not done`; this section is read by a machine"
)
PLACEHOLDER = re.compile(r"^<[^>]*>$")
# Characters that occupy no width: the two variation selectors, the zero-width
# family, and the byte-order mark. None of them make a marker into a claim.
INVISIBLE = "\ufe0f\ufe0e\u200b\u200c\u200d\u2060\ufeff"
SEPARATOR = re.compile(r"^:?-+:?$")
# The two delimiters of an HTML comment. `live_lines` scans for them directly
# for the callers that read files other than records: it holds the comment
# state itself, so neither is looked for while it is inside a fence or a code
# span. A record carries no comment, and `comment_lines` finds a record line
# that begins with OPENER for the reader that refuses it (#1012).
OPENER = "<!--"
CLOSER = "-->"
# What each reader of a record says of a line `comment_lines` finds, spelt
# once, in `lib/fields.py`, whose `read` says it of a `guarantee.md` and a
# `trail/gate.md`: `check_text` here, `chain_check.py` for a round record, and
# `rule_changes.py#parse` for a design's `## Rule changes` say it from here.
COMMENT_LINE = _load_lib("fields.py", "agentic_fields_for_unverified").COMMENT_LINE
# A run of backticks. `live_lines` needs it as it scans for code spans.
BACKTICKS = re.compile(r"`+")
SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "venv",
}


class _LooseHeading:
    """The matcher behind the one hint `check_text` gives where a memo holds
    no `## Not verified` section: the first heading near it, named in the
    refusal so the author finds the spelling to fix. It decides nothing, and
    no section is read under it.

    **Whether the line is a heading is the one rule's**, `heading_level`, at
    level 2 or 3; this decides the wording alone, a heading that mentions
    `not verified` in any case. It was a pattern of its own, a sixth
    spelling of the heading rule beside the one in this file (#867 round 1,
    🟡 6). `.match` is the name `check_text` calls."""

    def match(self, text):
        return heading_level(text) in (2, 3) and "not verified" in text.lower()


LOOSE_HEADING = _LooseHeading()


def split_row(line):
    """Cells of one markdown table row, or None if the line is not a row.

    `\\|` inside a cell is an escaped pipe, not a column break."""
    s = line.strip()
    if not s.startswith("|"):
        return None
    s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]


def is_separator(cells):
    return bool(cells) and all(SEPARATOR.match(c) for c in cells)


def is_header(cells):
    return bool(cells) and cells[0].strip().lower() == "item"


def visible(s):
    """`s` without characters that take no space on screen.

    A zero-width space pastes in from anywhere, and many keyboards emit the
    old mark followed by U+FE0F. Either one makes `| closed\\u200b | done |`
    survive a plain `.strip()` while looking exactly like a bare `closed`,
    which is the one row shape this refuses."""
    return s.translate({ord(c): None for c in INVISIBLE}).strip()


def fence_spans(lines):
    """`[(first, last)]` for each fenced block in `lines`, delimiters
    included, with `last` None for a block that is never closed.

    The walk where only the fence delimiter rule decides where a fence
    opens: no comment state and no code-span state is kept (#1012). In this
    module `closed_fence_lines` and `blank_fences` walk it, and `readable`
    through `blank_fences`. Callers in other scripts are found with
    `git grep`, and no list of them is kept here to go stale. A walk that
    keeps a comment or a code-span state, `_scan`, which `liveness` and
    `live_pieces` read, asks `fence_opener` and `fence_closes` directly
    instead, because there whether a line can
    open a fence at all depends on the state it began in.

    **An unclosed block is reported, not decided.** `blank_fences` blanks it
    to the end, because a gate reading a record treats it as quoted. A reader of a
    line that HOLDS something — an open row — reads it,
    because only a block that closes is certainly a quotation
    (`docs/checks/the-fold.md`'s *Whether a line is live is asked by what
    the line does*).
    """
    spans, opener, first = [], None, None
    for n, line in enumerate(lines):
        if opener is None:
            opener = fence_opener(line)
            if opener is not None:
                first = n
        elif fence_closes(line, opener):
            spans.append((first, n))
            opener = None
    if opener is not None:
        spans.append((first, None))
    return spans


def closed_fence_lines(lines):
    """The indices of `lines` inside a fenced block that CLOSES, delimiters
    included — the lines a reader of something a line holds may skip."""
    lines = list(lines)
    return {
        n
        for first, last in fence_spans(lines)
        if last is not None
        for n in range(first, last + 1)
    }


def blank_fences(lines):
    """The same lines with fenced blocks blanked out, indices intact.

    A skill or a closing memo quoting this very format must not read as rows or
    as a second section. Blanking rather than truncating matters: truncated,
    the rows after an example would read as absent. A block that is never
    closed is blanked to the end, and the delimiter rule is `fence_opener`'s."""
    lines = list(lines)
    out = list(lines)
    for first, last in fence_spans(lines):
        for n in range(first, len(lines) if last is None else last + 1):
            out[n] = ""
    return out


def comment_lines(lines):
    """The indices of LINES whose text, leading whitespace removed, begins
    with `OPENER` — the lines a reader of a record refuses with
    `COMMENT_LINE` (#1012).

    LINES are `readable`'s, so a line inside a fence is blank and never
    found. A record carries no HTML comment, and its readers keep no comment
    state, so a comment they met would read as text; this is where they
    find one instead. An `OPENER` anywhere later in a line is text, in a code
    span or not, and is not found: refusing it would need a code-span state
    in `readable` and every reader of a record through it, the state #1000
    broke."""
    return [n for n, line in enumerate(lines) if line.lstrip().startswith(OPENER)]


def liveness(lines, spans_cross_lines, comments=True):
    """Whether each line BEGINS live, under one of the two span readings.

    `spans_cross_lines` is the only thing that differs between them, and it is
    the one question markdown cannot answer without a block model: a backtick
    run with no partner on its own line is literal text if the paragraph ends
    before its partner, and a code span if it does not. `live_lines` runs this
    twice rather than deciding. `rule_changes.py#parse` reads the reading
    with `spans_cross_lines=False` as well: a line dead there is in a fence,
    and a line live there and dead in `live_lines` begins inside a code span
    an earlier line opened.

    `comments` False keeps no comment state, so `OPENER` is text: the
    reading of a record, which carries no comment, for
    `rule_changes.py#parse` (#1012). Every caller that reads a file other
    than a record keeps the default.

    The flags are read from `_scan`, the one walk of fences, comments and
    code spans, which `live_pieces` reads too (#1185).
    """
    return [begins for begins, _pieces in _scan(lines, spans_cross_lines, comments)]


def live_pieces(lines, spans_cross_lines, comments=True):
    """For each line, the `(start, end)` offsets into it of every piece of
    live text: text outside a fenced block, an HTML comment and a code span,
    under the span reading `spans_cross_lines` names, as `liveness` takes
    it. The pieces of a line are in order, and a piece may be empty.

    A fence's lines, its opener and its closer among them, hold no piece. A
    backtick run that opens no span is live text and stays inside its
    piece; a span's backticks and a comment's delimiters stand in none.
    `payload_meter.py#imports_of` reads a `CLAUDE.md`'s imports here, with
    `spans_cross_lines=True` (#1185). It reads from `_scan`, the walk
    `liveness` reads, so the two never disagree about where a line stands.
    """
    return [pieces for _begins, pieces in _scan(lines, spans_cross_lines, comments)]


def _scan(lines, spans_cross_lines, comments):
    """`[(begins_live, pieces)]` for each line: whether the line begins
    live, `liveness`'s answer, and its live pieces, `live_pieces`'s. The
    arguments are theirs.

    Everything but `spans_cross_lines` is shared and is not a guess. Inside
    a fence nothing is read but the closing fence; inside a comment nothing
    is markdown, so backticks there are ordinary characters; inside a code
    span no comment delimiter is a delimiter. A fence is decided before the
    rest of its line because a fence opener owns the whole line, and after
    that whichever of a comment opener and a backtick run comes first in the
    text wins.
    """
    fence, comment, span = None, False, None
    out = []
    for n, line in enumerate(lines):
        pieces = []
        out.append((fence is None and not comment and span is None, pieces))

        if fence is not None:
            if fence_closes(line, fence):
                fence = None
            continue
        if not comment and span is None:
            fence = fence_opener(line)
            if fence is not None:
                continue

        # Where the live piece being read began, or None outside live text.
        start = None if comment or span is not None else 0
        pos = 0
        while pos < len(line):
            if comment:
                at = line.find(CLOSER, pos)
                if at == -1:
                    break
                pos, comment = at + len(CLOSER), False
                start = pos
            elif span is not None:
                closer = next(
                    (
                        m
                        for m in BACKTICKS.finditer(line, pos)
                        if m.end() - m.start() == span
                    ),
                    None,
                )
                if closer is None:
                    break
                pos, span = closer.end(), None
                start = pos
            else:
                opener = line.find(OPENER, pos) if comments else -1
                run = BACKTICKS.search(line, pos)
                if opener != -1 and (run is None or opener < run.start()):
                    pieces.append((start, opener))
                    pos, comment, start = opener + len(OPENER), True, None
                elif run is None:
                    break
                else:
                    width = run.end() - run.start()
                    closer = next(
                        (
                            m
                            for m in BACKTICKS.finditer(line, run.end())
                            if m.end() - m.start() == width
                        ),
                        None,
                    )
                    if closer is not None:
                        pieces.append((start, run.start()))
                        pos = start = closer.end()
                    elif spans_cross_lines and _partner_ahead(lines, n + 1, width):
                        pieces.append((start, run.start()))
                        span, start = width, None
                        break
                    else:
                        pos = run.end()
        if start is not None:
            pieces.append((start, len(line)))
    return out


def heading_level(line):
    """The level of the ATX heading LINE is, 1 to 6, or None where it is
    not one — **the one spelling of a markdown heading in this plugin**
    (#867).

    CommonMark 4.2: at most three spaces of indentation, then one to six
    `#`, then a space, a tab or the end of the line. So `#hello`, `#######
    seven`, an issue reference that begins a wrapped line (`#120) was …`) and
    a `#` run four spaces in are not headings, and `   ## B` is. A tab
    before the run is four columns, an indented code block, and not a
    heading either.

    **It reads one line, so the lines it is asked of are the caller's
    business.** A renderer shows a heading only where the line is shown, so
    every reader asks it of lines with fenced blocks blanked — `readable`'s
    here, `coordinates.py#unquoted`'s in the kernel — and a `## B`
    quoted in a closed fence is never asked. Setext headings are not read:
    every one markdown-it finds in this repository is a front-matter line
    under its `---` closer, which GitHub renders as a table.
    `tests/skills/test_unverified_check.py`'s `Test_heading_level` holds this to
    markdown-it's ATX headings, through `tests/commonmark_oracle.py`, over
    the frame's shapes and a generated corpus;
    `tests/behaviour/test_one_heading_rule_holds_to_commonmark.py` holds every tracked
    `.md` file to them, and says so the day a setext heading appears in a
    body.

    It used to be spelled in five places: here inline in
    `_paragraph_ends_at`, as `startswith("#")` in `headings` and in
    `chain_check.py`, as `^#{1,6}\\s` in the checker and the payload meter,
    and as a pattern in `fold_check.py`; the first two read a `#NNN`-led
    line as a heading and ended a `## Not verified` or `## Verdicts` section
    there.
    """
    indent = len(line) - len(line.lstrip(" "))
    if indent > 3:
        return None
    s = line[indent:]
    n = len(s) - len(s.lstrip("#"))
    if 1 <= n <= 6 and (len(s) == n or s[n] in " \t\r\n"):
        return n
    return None


def _paragraph_ends_at(line):
    """Whether this line ends the paragraph above it.

    Each rule is the format's own: a blank line (CommonMark 4.8), an ATX
    heading (4.2), a fence delimiter (4.5), a thematic break (4.1), a block
    quote marker (5.1), a bullet or an ordered list that may interrupt a
    paragraph (5.2, 5.3), a setext underline (4.3), and a table row, which
    GFM parses cell by cell.

    **Being incomplete here is CHEAP, not safe, and the difference is a line
    the format parks.** This bounds one half of a disagreement rather than
    the answer, and a missing stop USUALLY only lets `_partner_ahead` reach
    further, which makes the crossing reading believe in a span the format
    would not, which parks a line — a marker or a heading not read,
    which a person sees. Usually, not always: reaching further also changes
    which runs pair with which, and a run that consumes a partner early
    leaves a later run with none, so a later line goes live rather than
    parked. Measured 2026-09-22 with the setext underline missing, which it
    was until round 6: `["text `", "===", "text `", "plain prose", "text `"]`
    read its last two lines live where the format parks them. The rule round
    5 removed decided the answer by itself, so its missing stops removed a
    directory; this one only leans, but it leans in both directions. **Add a
    stop when the format has one, and stop nowhere the format does not** — an
    over-stop shortens the reach, which is the direction that goes live.
    """
    s = line.strip()
    if not s:
        return True
    # `|` is a deliberate over-stop — GFM parses a table row's cells
    # independently and it is what keeps three work items' coordinates.
    # `>` is the format's own rule (CommonMark 5.1).
    if s.startswith(("|", ">")):
        return True
    # CommonMark 4.2, asked of the one spelling, `heading_level` (#867).
    # `s.startswith("#")` alone stopped on `#hello` and on `####### seven`,
    # which are paragraph text — and on the issue references this repository
    # writes constantly, 944 lines of them (round 6, finding 4). Four spaces
    # is paragraph text too, a lazy continuation line, and the oracle
    # `tests/skills/test_unverified_check.py#block_ends_at` has bounded it all
    # along (#491's round-7 comment).
    if heading_level(line) is not None:
        return True
    # Only an OPENER interrupts a paragraph, and `fence_opener` is the rule.
    if fence_opener(line) is not None:
        return True
    if s[0] in "*-_" and len(s) >= 3 and set(s.replace(" ", "")) == {s[0]}:
        return True
    if s[:2] in ("- ", "* ", "+ "):
        return True
    # CommonMark 4.3: a setext underline is a run of `=` under a paragraph.
    # The `-` form is already a thematic break above.
    if set(s) == {"="}:
        return True
    # CommonMark 5.3: an ordered list interrupts a paragraph only when it
    # starts with 1. `3. an item` inside a paragraph is paragraph text, and
    # stopping there shortens the crossing reading's reach.
    return s[:2] in ("1.", "1)") and len(s) > 2 and s[2] in " \t"


def _partner_ahead(lines, start_line, width):
    """Whether a backtick run of exactly `width` arrives before the paragraph
    the run opened in has ended.

    This is one half of a disagreement, not an answer: it asks how far a span
    COULD reach, and `live_lines` pairs it with the reading where an unclosed
    run reaches nowhere at all. A true span's partner lies inside its own
    paragraph, so this finds the very same partner; everywhere the two differ
    this reading parks a line the format would have read live, which is the
    direction that keeps a work item's directory.
    """
    for i in range(start_line, len(lines)):
        if _paragraph_ends_at(lines[i]):
            return False
        for m in BACKTICKS.finditer(lines[i]):
            if m.end() - m.start() == width:
                return True
    return False


def live_lines(lines, comments=True):
    """`(the line, it begins live)` for each line — both readings, ANDed.
    `comments` is `liveness`'s, handed to both.

    A line that excuses or declares something is not taken on doubt, the
    second of the three answers `docs/checks/the-fold.md` *The fold, and
    what tells it from a deletion* gives: what this parks, `rule_changes.py`
    reads as no heading.

    **The one rule for whether a line is live, and every reader of a marker
    or a policy heading asks it here.** A line
    begins live when it begins outside a fenced block, outside an HTML
    comment and outside a code span. The line is handed back unchanged; what
    a caller reads out of it — a marker, a coordinate — lives inside
    backticks, and the flag beside it is the whole of the judgment.

    **The one question markdown will not answer without a block model, and
    what is done about it.** A backtick run with no partner on its own line
    is literal text if the paragraph ends before its partner arrives, and a
    code span if it does not. Knowing which needs to know where the block
    ends, and every rule this reader has had for that was a guess:

    - Reading A: the run is **not** a span. It is literal, and comment
      delimiters after it on later lines are real delimiters.
    - Reading B: the run **is** a span, reaching to the next run of equal
      length wherever that falls.

    **A line is live only where both readings call it live.** Nothing decides
    where a block ends, because neither reading is chosen — both are computed
    and the disagreement is resolved toward reading less. Where the two
    agree, that is the answer; where they differ, the line is read as quoted.
    The cost is a marker or a heading not read, which a person sees as a
    refusal and can act on.

    **This is what five review rounds cost.** Rounds 1 to 4 each guessed at
    the comment state from a stateless pass; the scan that replaced them
    guessed instead at markdown's block structure, and round 5 found the
    shape that guess got wrong — a paragraph carrying an unclosed backtick,
    a draft opener on the next line, the closing backtick after it, and a
    marker below, which read live. A guess at a block model fails for the same reason
    a guess at the comment state did, one level down. Computing both readings
    is what ends the class: there is no third thing to be wrong about.
    `plan.md` *Alternatives considered* carries the four formulations of the
    pre-pass and this one's own predecessor.

    **What it reads, and what it does not model.** Inside a fence nothing is
    read but the closing fence; inside a comment nothing is markdown, so
    backticks there are ordinary characters; inside a code span no comment
    delimiter is a delimiter. A fence is decided before the rest of its line,
    then whichever of a comment opener and a backtick run comes first wins.
    Reference definitions, link destinations, raw HTML blocks and entity
    references are not modelled and none can hold a declaring line, such as
    a `seal/config.md` row, on a line of its own. Markdown's indented code
    block is the one deliberate omission with a shape that could.

    **What this may not touch.** `blank_fences` and `readable` keep no
    comment state, because a record carries no comment, and they serve the
    readers of a record (#1012). Neither is on this path. What this scan and
    `blank_fences` DO share is the fence delimiter, `fence_opener` and
    `fence_closes`, because two spellings of it is what #491 found: the
    three-space bound had landed here and not one function over. They share
    the line split too: `readable` and every caller that hands this lines
    split the text with `gfm_lines` (#664).
    """
    lines = list(lines)
    literal = liveness(lines, spans_cross_lines=False, comments=comments)
    crossing = liveness(lines, spans_cross_lines=True, comments=comments)
    for n, line in enumerate(lines):
        yield line, literal[n] and crossing[n]


def readable(text):
    """The lines a reader of a record should judge: no fenced blocks.

    A line a record's rows are counted on is blanked, the third of the three
    answers `docs/checks/the-fold.md` *The fold, and what tells it from a
    deletion* gives: a fence nobody closed is blanked to the end, and the
    readers that judge a record refuse the table it hid as absent, while
    `broad_gate.py`'s label, which never stops a run that passed, is
    printed without it.

    **A comment is text here.** A record carries no HTML comment, so this
    keeps no comment state, and the reader of a record refuses a line that
    begins with `OPENER` at its line (`comment_lines`, #1012).

    Every read of a record starts here, on disk and at a ref alike, so every
    reader counts the same table. Its lines are `gfm_lines(text)`, so an
    index into what this returns is an index into `gfm_lines(text)` and into
    no other split."""
    return blank_fences(gfm_lines(text))


def headings(lines):
    """(index, text) for every heading in already-`readable` lines, by the
    one rule, `heading_level` (#867). `startswith("#")` read a wrapped line
    beginning `#120)` as a heading, so a `## Not verified` section ended
    there and the rows below it went uncounted — the permissive direction."""
    return [
        (i, line.rstrip())
        for i, line in enumerate(lines)
        if heading_level(line) is not None
    ]


def items(body):
    """`(items, error)` for BODY, `[(line number, line)]`, read as a design
    section's items. Each item is `{"kind", "line", "fields"}`, `fields`
    mapping a name to `[line number, [value lines]]`; ERROR is the first line
    that is no part of an item, as `(line number, why)`, or None."""
    found, item, last = [], None, None
    for no, line in body:
        m = ITEM_RE.match(line)
        if m:
            item, last = {"kind": m.group(1), "line": no, "fields": {}}, None
            found.append(item)
            continue
        if item is None:
            return found, (no, "a line outside an item")
        m = FIELD_RE.match(line)
        if m:
            last = m.group(1)
            if last in item["fields"]:
                return found, (no, f"`{last}` given twice")
            item["fields"][last] = [no, [m.group(2) or ""]]
            continue
        if last and (not line.strip() or line.startswith(CONTINUED)):
            item["fields"][last][1].append(line[len(CONTINUED) :])
            continue
        return found, (no, "a line that is not a field of the item above")
    return found, None


def field_values(item, need, may):
    """`(values, error)`: ITEM's fields as `{name: value}`, or ERROR, the
    first field outside NEED and MAY, missing from NEED, or empty."""
    fields, values = item["fields"], {}
    for name, (no, _) in fields.items():
        if name not in need + may:
            return None, (no, f"`{name}` is not a field of `{item['kind']}`")
    for name in need:
        if name not in fields:
            return None, (item["line"], f"`{item['kind']}` needs `{name}`")
    for name, (no, parts) in fields.items():
        values[name] = "\n".join(parts).strip("\n").rstrip()
        if not values[name].strip():
            return None, (no, f"`{name}` is empty")
    return values, None


def opens_the_block(line):
    m = ITEM_RE.match(line)
    return bool(m) and m.group(1) == NOTHING


def unread_block(body):
    """`(line number, why)` where BODY, a section's non-blank `[(line number,
    line)]`, opens with a line that opens like the no-change block and is
    not it (`NEAR_NOTHING`, `UNREAD_BLOCK`); else None. The line decides
    nothing: `nothing_block` passes it on as any other line, and its reader
    refuses the section for what it lacks and names the line. Whether it
    meant the block is the judgment of the agent that reads the record."""
    first_no, first = body[0]
    if opens_the_block(first) or not NEAR_NOTHING.match(first):
        return None
    return first_no, UNREAD_BLOCK.format(said=first.strip())


def nothing_block(body):
    """None where BODY, a section's non-blank `[(line number, line)]`, does
    not open with the no-change block; else its errors, `[(line number,
    reason)]`, empty where the block reads. The block is read in its one
    spelling, and a line that opens like it is passed on (`unread_block`).
    Its field `why` is optional and its value is returned to nobody: the
    readers use only that the section holds no row or no operation, and the
    reason is the agents' to read (#1319)."""
    if not opens_the_block(body[0][1]):
        return None
    found, error = items(body)
    if error:
        return [error]
    if len(found) > 1:
        return [(found[1]["line"], f"`- {NOTHING}` is the section's one item")]
    _, error = field_values(found[0], (), (WHY,))
    return [error] if error else []


def parse_section(body, offset):
    """(open, closed, errors) for the body lines of one section.

    `offset` is the file line number of body[0], so every error carries a
    coordinate the author can open. The header is exactly `HEADER`, a row
    opening with `OLD_MARK` is refused naming the edit, and a first line
    that opens like the no-change block and is not it is prose, which
    `unread_block` names."""
    errors, open_rows, closed_rows = [], [], []
    content = [(offset + i, ln) for i, ln in enumerate(body) if ln.strip()]

    if not content:
        errors.append(
            (offset, f"the section is empty: write the table, or {NOTHING_WRITTEN}")
        )
        return open_rows, closed_rows, errors

    first_no, first = content[0]
    block = nothing_block(content)
    if block is not None:
        errors.extend(block)
        return open_rows, closed_rows, errors

    cells = split_row(first)
    if cells is None:
        unread = unread_block(content)
        errors.append(
            (
                first_no,
                f"{FOUND_PROSE}. Not read: {unread[1]}" if unread else FOUND_PROSE,
            )
        )
        return open_rows, closed_rows, errors
    if tuple(cells) != HEADER:
        errors.append(
            (
                first_no,
                f"header is |{'|'.join(cells)}|, and the one this reads is "
                f"|{'|'.join(HEADER)}|",
            )
        )
        return open_rows, closed_rows, errors
    if len(content) < 2 or not is_separator(split_row(content[1][1]) or []):
        errors.append((first_no, "the header row is not followed by a separator row"))
        return open_rows, closed_rows, errors

    rows = content[2:]
    if not rows:
        errors.append(
            (first_no, f"a table with no rows says nothing: write {NOTHING_WRITTEN}")
        )
    for line_no, line in rows:
        cells = split_row(line)
        if cells is None:
            errors.append((line_no, "a line inside the table that is not a table row"))
            continue
        if len(cells) != 2:
            errors.append((line_no, f"{len(cells)} cells, expected 2"))
            continue
        item, who = cells
        # One normalization for every judgment below. Reading the raw cell in
        # one place and the normalized cell in another is how a zero-width
        # space turned a separator into an unverified item and a blank row
        # into an open one.
        seen = [visible(c) for c in cells]
        if is_separator(seen) or is_header(seen):
            errors.append(
                (
                    line_no,
                    "a second header or separator row inside the section — it "
                    "holds one table, and a repeated one counts `|---|---|` "
                    "as an unverified item",
                )
            )
            continue
        if not seen[0] or not seen[1]:
            errors.append(
                (line_no, "an empty cell — every row names an item and its answerer")
            )
            continue
        if PLACEHOLDER.match(seen[0]) or PLACEHOLDER.match(seen[1]):
            errors.append((line_no, "the template's placeholder is still in the row"))
            continue
        word, rest = closing_word(seen[0])
        if word == OLD_MARK:
            errors.append(
                (
                    line_no,
                    f"the row opens with U+2705, which no longer closes a row: a "
                    f"closed row opens with the word `{CLOSED}`, so write "
                    f"`| {CLOSED} {rest or '<the item>'} | <what closed it> |`",
                )
            )
            continue
        if word == CLOSED:
            if not rest:
                errors.append(
                    (
                        line_no,
                        f"a bare `{CLOSED}` — the row keeps the item's text "
                        "after the word, and the second cell says what closed it",
                    )
                )
                continue
            closed_rows.append((line_no, rest, who))
        else:
            open_rows.append((line_no, item, who))
    return open_rows, closed_rows, errors


def closing_word(cell):
    """`(first word, the rest)` of an Item cell already through `visible`.

    The old mark is its own word whether or not a space follows it, which is
    how it was written; every other word ends at whitespace."""
    if cell.startswith(OLD_MARK):
        return OLD_MARK, visible(cell[len(OLD_MARK) :])
    parts = cell.split(None, 1)
    word = parts[0] if parts else ""
    rest = parts[1].strip() if len(parts) > 1 else ""
    return word, rest


def check_file(path):
    """(open, closed, errors) for one closing memo.

    Exactly one `## Not verified` section, spelled that way. Tolerating other
    spellings is what makes an unknown one report zero, and this corpus had
    more than one of them."""
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
    except OSError as exc:
        return [], [], [(0, f"cannot be read: {exc}")]
    return check_text(text)


def sections(lines, heading):
    """The index of each heading in LINES, already `readable`, whose text is
    the string `heading` exactly. `check_text` asks it for `HEADING`, and
    `pr_body.py` for the section of a record it copies."""
    return [i for i, text in headings(lines) if text.strip() == heading]


def check_text(text):
    """The reader of one closing memo's text: `(open, closed, errors)`.

    There is one reading, whoever asks: `main` through `check_file`, and
    `settle.py` through `open_record_rows` and for the closed rows it lists.
    The section is the one headed exactly `HEADING`, and `parse_section`
    reads its body. Where no such heading stands, the refusal names the
    first heading near it (`LOOSE_HEADING`), so the author finds the
    spelling to fix.

    **A comment line is refused before any section is looked for.** The
    first line that begins with `OPENER` is refused at its line
    (`comment_lines`, #1012). `open_record_rows` hands any refusal on as one
    entry saying the record cannot be read, never as zero open rows."""
    lines = readable(text)

    commented = comment_lines(lines)
    if commented:
        return [], [], [(commented[0] + 1, COMMENT_LINE)]

    found = sections(lines, HEADING)
    if not found:
        near = [(i, text) for i, text in headings(lines) if LOOSE_HEADING.match(text)]
        hint = (
            f" (found `{near[0][1].strip()}` at line {near[0][0] + 1})" if near else ""
        )
        return [], [], [(1, f"no `{HEADING}` section{hint}")]
    if len(found) > 1:
        at = ", ".join(str(i + 1) for i in found)
        return (
            [],
            [],
            [(found[1] + 1, f"more than one `{HEADING}` section: lines {at}")],
        )

    start = found[0]
    end = len(lines)
    for i, _ in headings(lines):
        if i > start:
            end = i
            break
    return parse_section(lines[start + 1 : end], start + 2)


def overviews(paths):
    """Every gaps.md under the given paths, in a stable order.

    **A walk leaves the reference roots out** (#688): a project's own
    `specs/` is a team's document, read as history and never as this
    plugin's record, so a malformed `## Not verified` there is not a finding.
    A path NAMED, a file or a directory inside a reference root, is read as
    named — the person asked for it."""
    found = []
    for p in paths:
        # Each argument is read at its real path. `reference_rule` measures
        # the path against the top `git rev-parse --show-toplevel` gives,
        # which has its links resolved, so a tree reached through a link and
        # read as named would leave no team's `specs/` out of the walk.
        p = os.path.realpath(p)
        if os.path.isfile(p):
            found.append(p)
            continue
        skip = reference_rule(p)
        for root, dirs, files in os.walk(p):
            dirs[:] = sorted(
                d
                for d in dirs
                if d not in SKIP_DIRS and not (skip and skip(os.path.join(root, d)))
            )
            if OVERVIEW in files:
                found.append(os.path.join(root, OVERVIEW))
    return sorted(dict.fromkeys(found))


def config_at(top):
    """`(lib/config.py, the seal/ root, its name in the tree)` for the
    repository at `top`: the root as `lib/optin.py#home_at` resolves it, and
    the name `lib/optin.py#home_name` gives, "" where the root is local or
    absent."""
    modules = []
    for name in ("config", "optin"):
        path = os.path.join(LIB, f"{name}.py")
        spec = importlib.util.spec_from_file_location(
            f"agentic_{name}_for_unverified", path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)
    config, resolver = modules
    common = resolver.git_common_dir(top)
    return config, resolver.home_at(top, common), resolver.home_name(top, common)


def references_at(top):
    """`(lib/config.py, roots, name)` for the repository at `top` — the
    module holding `under_reference_root`, what the row names under the root
    `lib/optin.py#home_at` resolves, and that root's name in the tree
    (`config_at`) — or None for a copy of this script with no `lib/` beside
    it.

    None prunes nothing, which reads more and never less: a copy taken alone
    keeps the walk it had before reference roots existed, rather than
    refusing a run that needed none of this. Read once per path a run is
    handed, so nothing is cached."""
    try:
        config, home, name = config_at(top)
        return config, config.reference_roots(home, name), name
    except (OSError, ImportError, AttributeError):
        return None


def policy_root(top):
    """The policy root of the repository at `top`, `lib/config.py#policy_root`'s
    answer for its `seal/` root."""
    config, home, _name = config_at(top)
    return config.policy_root(home)


def reference_rule(start):
    """A predicate on a disk directory — True for one the walk from `start`
    leaves out — or None where nothing is left out: `start` outside a git
    repository, a copy with no `lib/`, or `start` itself inside a
    reference root, which the person named and so asked for. Every
    directory the walk meets is under `start`, so under `top` as well, and
    has a repository-relative form."""
    top = repo_root(start)
    if top is None:
        return None
    loaded = references_at(top)
    if loaded is None:
        return None
    config, roots, name = loaded
    if config.under_reference_root(repo_relative(start, top), roots, name):
        return None

    def skip(directory):
        return config.under_reference_root(repo_relative(directory, top), roots, name)

    return skip


def git_path(path):
    r"""`path` as git spells it: forward slashes, whatever `os.sep` is here.

    Every repo-relative path in this file is built by `os.path.relpath` and
    then read beside what git prints or handed to a reader of git's paths:
    `repo_relative`'s answer is matched against the `Reference specs` row,
    `tree_at` lists a directory on disk in the form `ls-tree` lists it at a
    ref, and `annotate` names a file to GitHub. git answers and accepts `/`
    on every platform, so on Windows a path built by `os.sep` would match
    none of them: `threads\x\gaps.md` against `threads/x/gaps.md`.

    A no-op where `os.sep` already is `/`, rather than branching on `os.name`:
    the substitution has to be on the path Linux CI runs, or the Windows half
    is proven by nothing. It also must not run there — a backslash is a legal
    character in a POSIX filename, and rewriting it would corrupt a real name.
    """
    return path if os.sep == "/" else path.replace(os.sep, "/")


def repo_relative(path, root):
    r"""`path` as a repo-relative git path, or None when it has no relative form.

    The composition `git_path(os.path.relpath(...))` is not safe on its own:
    `relpath` raises across drives, and a `ValueError` raised mid-report
    kills a run that has already printed part of its rows, which
    `display_path` beside this one exists to prevent.

    None rather than a fallback, because the question is about a path INSIDE
    a repository. A path on another volume is not inside this one -- a
    working tree cannot span drives -- so there is no answer to degrade to,
    and inventing one is the quiet zero this tool refuses. `reference_rule`
    asks it only of paths under the top `repo_root` found for them.
    """
    try:
        return git_path(os.path.relpath(path, root))
    except ValueError:
        return None


def display_path(path, start):
    r"""`path` relative to `start`, or absolute when there is no relative form.

    `os.path.relpath` raises `ValueError` on Windows when the two are on
    different drives, and this is the reporting footing for every line the
    tool prints. Running `seal unverified D:\repo\specs` from `C:\` is
    an ordinary thing to do, and it died with a traceback before printing a
    single row. The absolute path is a worse answer than a relative one and a
    far better one than no output at all.
    """
    try:
        return os.path.relpath(path, start)
    except ValueError:
        return os.path.abspath(path)


def unique_by_target(paths):
    """One path per real file, the real file's own, in sort order.

    A tracked symbolic link and the file it points at are one record and two
    paths. Counting both doubles its open items. The path kept is the one
    `os.path.realpath` answers, whichever path the scan reached the file by,
    and it may lie outside the scanned path, or outside the repository."""
    return sorted({os.path.realpath(p) for p in paths})


def repo_root(path):
    here = path if os.path.isdir(path) else (os.path.dirname(path) or ".")
    r = subprocess.run(
        ["git", "-C", here, "rev-parse", "--show-toplevel"],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    return r.stdout.strip() if r.returncode == 0 else None


def commit_of(root, ref):
    """The commit `ref` names in `root`, or None. `resolves` asks it for
    `chain_check.py`."""
    r = subprocess.run(
        ["git", "-C", root, "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    if r.returncode != 0:
        return None
    return r.stdout.strip() or None


def resolves(root, ref):
    """Whether `ref` names a commit in `root`.

    `chain_check.py` loads this module and asks this of its `--baseline`
    before it reads anything at that ref, so a CI checkout too shallow to
    hold the base branch is exit 2 there rather than a diff read against
    nothing. It calls this by name, which is why it stays a predicate rather
    than becoming `commit_of` at its call sites."""
    return commit_of(root, ref) is not None


def merge_base(root, ref):
    """The last commit `ref` and `HEAD` agreed on, or None.

    `chain_check.py` asks `settled` at this commit, and not at `ref`. The ref
    it passes is the branch the pull request merges into, and that branch
    MOVES: the moment one work item squashes into it, every sibling branch
    cut before that squash has the squashed item's files at the ref and never
    had them at all (#272).

    On a branch checkout the merge base is the fork point. In CI, whose
    checkout of a pull request is the head already merged into the base, it is
    the base's tip. Either way a directory present there and absent here was
    removed by THIS branch, and one that arrived on the base after the branch
    was cut is not this branch's business.

    None for two states: unrelated histories (exit 1, empty output) and a
    `HEAD` that names no commit (exit 128). A shallow clone whose base ref
    resolves while their common ancestor sits beyond the graft lands in the
    first."""
    r = subprocess.run(
        ["git", "-C", root, "merge-base", ref, "HEAD"],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    if r.returncode != 0:
        return None
    return r.stdout.strip() or None


_rules = None


def rule_changes():
    """`skills/settle/scripts/rule_changes.py`, the one reader of a design's
    `## Rule changes`, loaded by path once."""
    global _rules
    if _rules is None:
        here = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(here, "..", "..", "settle", "scripts", "rule_changes.py")
        spec = importlib.util.spec_from_file_location("agentic_rule_changes", path)
        _rules = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_rules)
    return _rules


def settled(root, ref, directories):
    """The DIRECTORIES that stood at REF, each a settle where it is gone whole.

    **The one predicate, and its one reader, `chain_check.py`, asks it**, of
    the merge base it already computes, handing it only directories absent
    on its head side. It stands here rather than in `chain_check.py`, where
    `tests/skills/test_chain_check.py`'s `Test_module` keeps a second one
    from being defined. Its rule is `docs/checks/the-fold.md` *The fold, and
    what tells it from a deletion*. A directory is settled when it held a
    file at REF. What its record held there and what the policy root holds
    of its design are not read: the settling session writes each section in
    its own words, and the settle's pull request states each decision for
    review. A directory a pull request empties only in part never reaches
    here, since its caller passes only the directories that are gone."""
    return {d for d in directories if tree_at(root, ref, d)}


def tree_at(root, ref, directory):
    """Repo-relative paths under `directory` at `ref`; the disk when `ref` is
    None. `directory` is `/`-joined, and so is every path returned. At a ref
    the paths come from `-z`, which quotes none, whatever `core.quotePath`
    says."""
    if ref is None:
        top = under_root(root, directory)
        out = []
        for here, dirs, files in os.walk(top):
            dirs.sort()
            for name in sorted(files):
                rel = os.path.relpath(os.path.join(here, name), root)
                out.append(git_path(rel))
        return out
    r = subprocess.run(
        ["git", "-C", root, "ls-tree", "-r", "-z", "--name-only", ref, "--", directory],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    return [rel for rel in r.stdout.split("\0") if rel] if r.returncode == 0 else []


def open_record_rows(root, directory):
    """`[(file, what is open)]` for a work item's record on disk, DIRECTORY
    `/`-joined under ROOT.

    The rows `seal settle --apply` refuses to take with a directory, and its dry
    run lists: every open item in `gaps.md`'s `## Not verified`. Each is a claim with an answerer rather
    than a rule, and #514's frame measured the loss this prevents — the only
    record that a production workflow was red sat in a retiring closing memo (its
    L2).

    The record is read by `check_text`, as `seal unverified` reads it. A
    closing memo whose section cannot be read is one entry saying so, never
    zero rows: a count this cannot read is not a count of nothing, which is
    the rule `check_text` above is written to. A directory with no `gaps.md`
    holds no row."""
    try:
        with open(
            under_root(root, f"{directory}/{OVERVIEW}"),
            encoding="utf-8",
            errors="replace",
        ) as f:
            overview = f.read()
    except OSError:
        return []
    rows, _, errors = check_text(overview)
    found = []
    if errors:
        found.append((OVERVIEW, f"cannot be read ({errors[0][1]})"))
    for _, item, _who in rows:
        found.append((OVERVIEW, item))
    return found


def root_name(top):
    """The name of the `seal/` root of the repository at TOP as the tree
    spells it, `lib/optin.py#home_name`'s answer; `optin.HOME` where TOP is
    None or holds no shared root. That is the name every root had before
    the second one (#1059), the one a local root keeps, and the one each
    fixture that commits a `seal/` with no marker is read under."""
    optin = _load_lib("optin.py", "agentic_optin_for_unverified")
    return (top and optin.home_name(top)) or optin.HOME


def named_root(parent):
    """Whether the directory PARENT carries the name `root_name` gives for
    the repository holding it. Only the name is read, as it was when the
    one name was `seal`: whether PARENT is that root is not asked. PARENT
    is a directory on disk."""
    return os.path.basename(parent) == root_name(repo_root(os.path.dirname(parent)))


def settled_root(path):
    """Whether `path` is a `seal/` root's own `threads` directory with no work
    item under it — empty on disk, or absent while the root is there.

    That is the state a complete settle reaches (#517, `frame/design.md` G7), and it
    is two states: the tree that ran `seal settle --apply` holds an empty
    `seal/threads/`, and a fresh checkout of the commit holds none, because git
    keeps no empty directory. A person who runs `seal unverified seal/threads/`
    after the settle hands this tool that path, and reading it as a typo would
    refuse a finished settle. Only this one path is settled: any other path
    that is missing is still refused, which is what keeps `threads/ thraeds/`
    from passing in silence.
    """
    p = os.path.abspath(path)
    parent = os.path.dirname(p)
    if os.path.basename(p) != ITEMS or not os.path.isdir(parent):
        return False
    if not named_root(parent):
        return False
    if not os.path.isdir(p):
        return True
    return not any(os.path.isdir(os.path.join(p, n)) for n in os.listdir(p))


SETTLED = (
    "seal unverified: {path} holds no work item and its `seal/` root is "
    "there — the state a complete settle ends in, so there is nothing to read"
)


def absent_root(path):
    """Whether `path` is the `seal/threads` path of a working tree's top level
    that holds no `seal/` directory: the `threads` path under the shared
    place `lib/optin.py#home_paths` gives there, under the second name where
    the project's own `seal/` stands.

    That is a repository whose records are in local mode, under the git
    directory, or that never had any, and a teammate's pull request against
    it declares nothing (#952). Read at the top level only, the directory
    `git rev-parse --show-toplevel` names, so a `seal/threads` typed from
    anywhere else is still the mistyped path it always was.
    """
    p = os.path.abspath(path)
    parent = os.path.dirname(p)
    top = os.path.dirname(parent)
    if os.path.basename(p) != ITEMS:
        return False
    if os.path.isdir(parent) or not os.path.isdir(top):
        return False
    found = repo_root(top)
    if found is None or not os.path.samefile(found, top):
        return False
    optin = _load_lib("optin.py", "agentic_optin_for_unverified")
    shared = optin.home_paths(found, optin.git_common_dir(found))[0]
    return os.path.basename(parent) == os.path.basename(shared)


ABSENT = (
    "seal unverified: {path} has no `seal/` root in this tree, so nothing "
    "here is declared: there is no record to read. A root in local mode sits "
    "under the git directory and is never committed"
)


def unwritten_root(path):
    """Whether `path` is a `seal/` root's own `threads` directory holding work
    items, none of which carries an `gaps.md`.

    Every work item that never opened a closing memo is in this state, and a
    pull request against it has no row to read (#952). `main` asks it only
    once the scan found no closing memo.
    """
    p = os.path.abspath(path)
    parent = os.path.dirname(p)
    if os.path.basename(p) != ITEMS or not os.path.isdir(p):
        return False
    if not named_root(parent) or settled_root(p):
        return False
    return not overviews([p])


UNWRITTEN = (
    "seal unverified: {path} holds work items and none of them carries an "
    "`gaps.md`, so no `## Not verified` row exists to read"
)


def under_root(root, rel):
    """The disk path of a `/`-joined repository-relative path."""
    return os.path.join(root, *rel.split("/"))


def show(root, ref, rel):
    r = subprocess.run(
        ["git", "-C", root, "show", f"{ref}:{rel}"],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    return r.stdout if r.returncode == 0 else None


def annotate(kind, path, line, message):
    """A GitHub annotation in CI, a plain line anywhere else."""
    if os.environ.get("GITHUB_ACTIONS"):
        # An annotation is matched against the diff by path, and GitHub spells
        # those the way git does. Every caller passes `display_path` output,
        # which is `os.sep`-spelled on purpose -- right for a line a person
        # reads, wrong for this. Live wherever this tool runs on a Windows
        # runner.
        where = f" file={git_path(path)},line={line}" if path else ""
        return f"::{kind}{where}::{message}"
    return f"{path}:{line}  {message}" if path else message


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="seal unverified",
        description="Report open `## Not verified` items; fail on a record "
        "that cannot be read.",
    )
    ap.add_argument("path", nargs="*", default=["."])
    args = ap.parse_args(argv)

    # The pull request that moves a root to local mode takes every closing
    # memo out of the tree, and with no root in it nothing is declared.
    if all(absent_root(p) for p in args.path):
        for p in args.path:
            print(ABSENT.format(path=p))
        return 0

    missing = [p for p in args.path if not os.path.exists(p) and not settled_root(p)]
    if missing:
        print(f"seal unverified: no such path: {missing[0]}", file=sys.stderr)
        return 2

    files = overviews(args.path)
    cwd = os.getcwd()
    total_open = total_closed = 0
    bad = []
    for path in unique_by_target(files):
        rel = display_path(path, cwd)
        open_rows, closed_rows, errors = check_file(path)
        total_open += len(open_rows)
        total_closed += len(closed_rows)
        for line_no, message in errors:
            bad.append(annotate("error", rel, line_no, message))
        if not errors and (open_rows or closed_rows):
            print(f"  {rel}  {len(open_rows)} open · {len(closed_rows)} closed")
            for _, item, who in open_rows:
                print(f"      open  {item}  —  {who}")

    if not files:
        if all(settled_root(p) for p in args.path):
            print(SETTLED.format(path=", ".join(args.path)))
            return 0
        if all(settled_root(p) or unwritten_root(p) for p in args.path):
            for p in args.path:
                print((SETTLED if settled_root(p) else UNWRITTEN).format(path=p))
            return 0
        print(
            f"seal unverified: no {OVERVIEW} found under "
            f"{', '.join(args.path)} — nothing was checked",
            file=sys.stderr,
        )
        return 2

    print(
        f"\n{len(unique_by_target(files))} closing memos · {total_open} open"
        f" · {total_closed} closed"
        f" · {len(bad)} unreadable"
    )

    if bad:
        print("\nthe record could not be read as it stands:")
        for line in bad:
            print(line)
        print(
            "\nThis is not a report of zero open items. A section this cannot "
            "read is a section whose count is unknown."
        )
        return 1

    if total_open == 0:
        print(
            f"open: 0 — every recorded item opens with `{CLOSED}` and says what "
            "closed it."
        )
    return 0


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a script run for its output says "nothing to see
    # here". `lib/console.py`
    # owns the reasoning and the three decisions behind these lines.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
