"""Shared reader: a closing memo's `## Not verified` section.

`verify` condition 4 lets a claim go out unproven as long as the row names
who answers it, and this module reads those rows: `check_text` reads one
memo's text into its open rows, its closed rows and what it could not
read, `check_file` reads one memo on disk, and `open_record_rows` lists a
work item's open rows. `skills/verify/scripts/unverified_check.py`, the
`seal unverified` command, reports them over a tree, and
`skills/settle/scripts/settle.py` refuses to take a directory that still
holds one.

**The format is strict on purpose.** A tolerant parser reports zero for a
section it cannot read, and zero reads as "everything has been closed".
Exactly one section is read, headed exactly `HEADING`, and it holds a
`| Item | Who must answer |` table or, alone, the no-change block of
`lib/items.py`. An item is closed by marking it, never by deleting it: the
Item cell opens with the word `closed`, and the second cell says what closed
it. Anything unmarked counts open, so the silent direction is "still open",
except for an open item whose own text begins with the word `closed`, which
reads as closed and which only a reader catches.

Deliberately a text scan of markdown, not a parser library: its lines are
`lib/lines.py`'s, its items `lib/items.py`'s, and the sentence a comment
line is refused with `lib/fields.py`'s, each imported beside it. Standard
library only, and Python 3.9 syntax, as every module under `lib/`.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fields import COMMENT_LINE
from gitcmd import under_root
from items import NOTHING_WRITTEN, nothing_block, unread_block
from lines import (
    comment_lines,
    heading_level,
    headings,
    is_separator,
    readable,
    sections,
    split_row,
    visible,
)

# A thread's closing memo, at the thread's top: `lib/optin.py#GAPS`, which a
# case holds this to.
OVERVIEW = "gaps.md"
HEADING = "## Not verified"
HEADER = ("Item", "Who must answer")
CLOSED = "closed"
# The emoji a closed row opened with before the word, U+2705, spelt by its code
# point so no emoji stands in this file. `parse_section` refuses a row opening
# with it, naming the edit.
OLD_MARK = chr(0x2705)
# What `parse_section` says of a section whose first line is neither the
# table's header nor the block.
FOUND_PROSE = (
    "expected `| Item | Who must answer |`, found prose. Prose belongs under "
    "`## Not done`; this section is read by a machine"
)
PLACEHOLDER = re.compile(r"^<[^>]*>$")


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


def is_header(cells):
    return bool(cells) and cells[0].strip().lower() == "item"


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


def check_text(text):
    """The reader of one closing memo's text: `(open, closed, errors)`.

    There is one reading, whoever asks: `unverified_check.py#main` through
    `check_file`, and `settle.py` through `open_record_rows` and for the
    closed rows it lists.
    The section is the one headed exactly `HEADING`, and `parse_section`
    reads its body. Where no such heading stands, the refusal names the
    first heading near it (`LOOSE_HEADING`), so the author finds the
    spelling to fix.

    **A comment line is refused before any section is looked for.** The
    first line that begins with `lib/lines.py#OPENER` is refused at its line
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
