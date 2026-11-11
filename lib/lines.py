"""Shared reader: the lines of a markdown text as a renderer shows them.

Every script that reads markdown or a record by line asks this module:
which cells a table row holds (`split_row`, `is_separator`), what a cell
shows (`visible`), which lines a fenced block holds (`fence_spans`,
`blank_fences`), which line of a record opens an HTML comment
(`comment_lines`), whether a line begins live (`liveness`,
`live_pieces`, `live_lines`), which ATX heading a line is
(`heading_level`, `headings`, `sections`), and which lines of a record a
reader judges (`readable`). `lib/gaps.py` reads a closing memo through it,
and the scripts load it through `lib/sibling.py`.

The fence delimiter rule and the GFM line split are `lib/blocks.py`'s,
imported beside it. `lib/blocks.py#walk` is the other walk of a markdown
file, kept apart from `live_lines` on purpose: a row the walk's readers read
is safe at its old reading where the walk is unsure.

Standard library only, and Python 3.9 syntax: `chain_check.py` and the
`Stop` hook's `seal_stamp.py` reach it on whatever `python3` starts them.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# The fence delimiter rule, CommonMark 4.5 (#491, #444, #584): `fence_opener`
# says which fence a line opens and `fence_closes` whether a line closes it.
# The readers of this module ask them, `fence_spans` and through it
# `blank_fences`, `_scan` and through it `liveness`
# and `live_pieces`, and `_paragraph_ends_at`; so do
# `coordinates.py#quoted_lines`, `payload_meter.py#imports_of` through
# `live_pieces`
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
# `tests/lib/test_lines.py`. A new reader
# that decides by line whether it stands inside a fence belongs in one of
# these two lists.
#
# Where GFM ends a line: LF, CR or CRLF, and nowhere else (#664). Every reader
# of markdown or record text reads its lines through `gfm_lines`, because two
# readers of one text that split it two ways disagree about which line an
# index names; the `splitlines` census in `tests/censuses.py` holds the
# remaining splitters to it.
try:
    from blocks import fence_closes, fence_opener, gfm_lines
except ImportError as missing:
    # A sentence rather than a bare `ModuleNotFoundError`, as `lib/tables.py`
    # and `lib/fields.py` raise it: this is a module other code imports.
    raise ImportError(
        "cannot read "
        + os.path.join(os.path.dirname(os.path.abspath(__file__)), "blocks.py")
        + ", and it is the fence rule and the line split this reader reads "
        "markdown through. This file ships beside it under `lib/`; a copy of "
        "one taken on its own is not a plugin"
    ) from missing

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
# A run of backticks. `live_lines` needs it as it scans for code spans.
BACKTICKS = re.compile(r"`+")


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
    module `blank_fences` walks it, and `readable` through `blank_fences`.
    Callers in other scripts are found with `git grep`, and no list of them
    is kept here to go stale. A walk that
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
    `tests/lib/test_lines.py`'s `Test_heading_level` holds this to
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
    # `tests/lib/test_lines.py#block_ends_at` has bounded it all
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
    a `routing.md` row, on a line of its own. Markdown's indented code
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


def sections(lines, heading):
    """The index of each heading in LINES, already `readable`, whose text is
    the string `heading` exactly. `lib/gaps.py#check_text` asks it for
    `HEADING`, and `pr_body.py` for the section of a record it copies."""
    return [i for i, text in headings(lines) if text.strip() == heading]
