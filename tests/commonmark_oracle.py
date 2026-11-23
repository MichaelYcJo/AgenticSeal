"""Which lines of a markdown document a CommonMark renderer hides (#667).

This is the oracle the readers under `lib/` are held to. It answers one question per
line -- does a renderer show this line as markdown text, or does it put it
inside something that is not -- and nothing else. Which lines form a table is
each reader's own grammar and is not asked here.

**It shares nothing with what it checks.** It imports markdown-it-py and the
standard library, and nothing from `lib/`, `skills/` or `.github/scripts/`;
`tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py` reads this file's own
imports to hold that. The work item before this one built its oracle out of
the readers' shared functions, and round 3 of it found the gap that
arrangement cannot see: "The oracle cannot catch this, because it is built
the same way." A parser written by somebody else, from the specification,
is the whole point, so no rule of this repository's is written here.

A line is hidden when the parser puts it in one of four places:

  fence        a fenced code block, its delimiter lines included
               (CommonMark 4.5)
  code         an indented code block (4.4)
  html         an HTML block of any of the seven kinds, a comment among them
               (4.6)
  inline html  inline raw HTML (6.6) that the line BEGINS inside: a comment,
               a CDATA section, a processing instruction, a declaration, an
               open tag or a closing tag -- every token the parser emits as
               `html_inline` (#673). The line where it opens begins outside
               it and is not hidden; every later line up to and including
               the one holding its closer is

All six inline kinds, and not the comment alone, because the block half
already reads that way: an HTML block of every kind is `html`, and CommonMark
6.6 renders raw HTML "without escaping" wherever it stands. Reading only the
comment let this oracle answer "shown" on the other five, which was the
walk's own answer there, so the two agreed by construction (#667 round 3,
🟡 2).

The parser is markdown-it-py's `commonmark` preset with GFM tables switched
on, because the files the readers read are rendered as GFM, and a table changes
which lines a paragraph holds. The version is pinned in
`tests/run_tests.py#MARKDOWN_IT`.

**Where the inline HTML is, the parser says.** A token carries no source
position, so the parser's own `html_inline` rule is wrapped: the wrapper
calls it unchanged and writes down the offset the rule started and ended at,
in the inline source it was reading. Nothing about what is inline HTML is
decided here; only where the tokens the parser found lie. Where a paragraph's
text starts, the parser says too: its own `paragraph` and `lheading` rules
are wrapped the same way, and the wrapper counts the whole lines their strip
dropped from the lines the parser joined behind the markers it consumed
(#677).
"""

from markdown_it import MarkdownIt
from markdown_it.rules_block.lheading import lheading
from markdown_it.rules_block.paragraph import paragraph
from markdown_it.rules_inline.html_inline import html_inline

FENCE, CODE, HTML, INLINE_HTML = "fence", "code", "html", "inline html"

BLOCK_KINDS = {"fence": FENCE, "code_block": CODE, "html_block": HTML}


def _recording_html_inline(state, silent):
    """The parser's own rule, with where its token started and ended kept."""
    start = state.pos
    found = html_inline(state, silent)
    if found and not silent:
        state.tokens[-1].meta = {"start": start, "end": state.pos}
    return found


def _recording_lines(rule):
    """A block rule of the parser's that joins lines into an inline token's
    source, with the number of whole lines its strip dropped from the top
    kept on that token as `meta["dropped"]`.

    The rule is called unchanged. The lines are then joined again with the
    same arguments the rule used, before any container around the paragraph
    restores the line marks it moved, so each line is taken from behind the
    container markers the parser itself consumed and no marker is read here.
    The joined lines end in `\\n` and only there, so every `\\n` inside what
    `lstrip` removes from the top ends a line it removed whole, whichever of
    the characters the strip removes that line held, U+001F among them
    (#677)."""

    def recorded(state, start, end, silent):
        count = len(state.tokens)
        found = rule(state, start, end, silent)
        if found and not silent:
            for token in state.tokens[count:]:
                if token.type == "inline" and token.map:
                    joined = state.getLines(*token.map, state.blkIndent, False)
                    dropped = joined[: len(joined) - len(joined.lstrip())]
                    token.meta = {"dropped": dropped.count("\n")}
        return found

    return recorded


def parser():
    md = MarkdownIt("commonmark").enable("table")
    md.inline.ruler.at("html_inline", _recording_html_inline)
    md.block.ruler.at("paragraph", _recording_lines(paragraph))
    md.block.ruler.at("lheading", _recording_lines(lheading))
    return md


_PARSER = parser()


def _inline_html_lines(inline):
    """Lines of `inline`'s source that begin inside inline raw HTML in it,
    of any of the six kinds.

    Only the inline token's own children are read, not a child's children:
    an offset the wrapper kept is an offset in the source the rule was
    reading, and inside an image description that is the description, not
    the paragraph. A line that begins inside HTML nested there is a line
    after one that left HTML open, which the walk never claims.

    The inline source is the paragraph's lines joined, with Python's
    `str.strip` applied to the whole by the parser. That strip also takes a
    line holding only a no-break space, another Unicode space or U+001F,
    which CommonMark reads as paragraph text, so the lines it dropped from the top
    are counted before an offset is turned into a line. The parser's own
    block rule counts them, from the lines it joined behind the markers it
    consumed (`_recording_lines`): three rounds of #673 read those markers
    here instead, and each found one more marker read wrong (#677). A token
    from any other rule holds one line, which a strip cannot drop whole, and
    carries no count.
    """
    out = set()
    if not inline.map or not inline.children:
        return out
    first = inline.map[0] + (inline.meta or {}).get("dropped", 0)
    src = inline.content
    starts = [0] + [n + 1 for n, ch in enumerate(src) if ch == "\n"]
    for child in inline.children:
        if child.type != "html_inline":
            continue
        span = child.meta or {}
        if "start" not in span:
            continue
        for offset, at in enumerate(starts):
            if span["start"] < at < span["end"]:
                out.add(first + offset)
    return out


def commonmark_lines(text):
    """TEXT's lines as CommonMark ends them, each with its own ending: at LF,
    CR or CRLF, and nowhere else (the specification's section 2.1). Written from the
    specification by a scan, not taken from anything this oracle checks."""
    out, line, index = [], "", 0
    while index < len(text):
        ch = text[index]
        line += ch
        if ch == "\r" and text[index + 1 : index + 2] == "\n":
            line += "\n"
            index += 1
        if ch in "\r\n":
            out.append(line)
            line = ""
        index += 1
    if line:
        out.append(line)
    return out


def _hidden_commonmark(lines):
    """{CommonMark line index: kind} for LINES, CommonMark's own lines."""
    count = len(lines)
    out = {}
    for token in _PARSER.parse("\n".join(lines)):
        kind = BLOCK_KINDS.get(token.type)
        if kind and token.map:
            for index in range(token.map[0], min(token.map[1], count)):
                out.setdefault(index, kind)
        elif token.type == "inline":
            for index in _inline_html_lines(token):
                if index < count:
                    out.setdefault(index, INLINE_HTML)
    return out


def hidden_text(text):
    """{index: kind} for every line of `commonmark_lines(text)` a renderer
    hides.

    **The renderer reads TEXT, not a reader's split of it** (#667 round 1,
    🟡 1). `str.splitlines` also ends a line at U+2028, NEL, a form feed and
    five more characters, and CommonMark does not, so the parser is given
    CommonMark's lines and the answer is keyed by them. The readers this
    oracle holds split their text at the same three endings (#1574), so an
    index here is an index into the lines a reader reads.
    """
    return _hidden_commonmark([line.rstrip("\r\n") for line in commonmark_lines(text)])


def hidden(lines):
    """`hidden_text` of LINES joined with `\\n`, endings removed or not, so
    index N here is index N of that text's CommonMark lines -- LINES' own
    index wherever no line holds a CR inside it."""
    return hidden_text("\n".join(line.rstrip("\r\n") for line in lines))


def hidden_lines(lines):
    """The indices alone."""
    return set(hidden(lines))


def _headings(text, markups):
    """{CommonMark line index: level} for every top-level `heading_open`
    token of TEXT whose markup is one of MARKUPS' characters repeated."""
    lines = [line.rstrip("\r\n") for line in commonmark_lines(text)]
    out = {}
    for token in _PARSER.parse("\n".join(lines)):
        if (
            token.type == "heading_open"
            and token.level == 0
            and token.map
            and token.markup
            and len(set(token.markup)) == 1
            and token.markup[0] in markups
        ):
            out[token.map[0]] = int(token.tag[1:])
    return out


def heading_lines(text):
    """{CommonMark line index: level} for every ATX heading the parser reads
    in TEXT at the top level of the document (#867): a `heading_open` token
    whose markup is a run of `#` (CommonMark 4.2). A heading inside a block
    quote or a list item is that container's, not the document's, and a
    reader of a document's sections reads none of them, so they are left
    out; what the parser hides in a fence or an HTML block it never reads as
    a heading at all."""
    return _headings(text, "#")


def setext_lines(text):
    """{CommonMark line index: level} for every top-level setext heading the
    parser reads in TEXT (CommonMark 4.3), keyed on the heading's first line:
    a `heading_open` token whose markup is a run of `=` or `-`."""
    return _headings(text, "=-")
