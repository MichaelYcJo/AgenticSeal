"""The one reader and the one spelling of the `seal` blocks a work item's
records hold their fields in (#1198).

A field a script reads in a round record, in `guarantee.md` or in
`trail/gate.md` stands inside a `seal` block and nowhere else. A block is a
fenced code block, by `hooks/lib/blocks.py#walk`, outside every other fence
and every HTML comment block, whose opener is a line of three backticks then
`seal`, with nothing before it and nothing after it. It closes where
CommonMark closes it. Each line inside it is `<key>: <value>`, or `<key>:`
where the value's shape takes nothing, with the key spelt as `Kind` below
spells it; the first line's key names the block's kind among the kinds the
record holds. This module is the one statement of that grammar, as #1198
drew it, and a change to it is an edit here.

`read` returns each block whose every line parses, each refusal and each
notice, each refusal and notice at its 1-based line:

  refused   a line of a block that is not a field of its kind, a key over
            its count, a second key of a pair the kind holds one of, a
            value that does not match its key's shape whole, a blank line,
            and a block lacking a key it holds one of (at its opener) or
            opening with no kind's key: the block is read no further and
            is not returned. Outside every block: a fence that never closes,
            at its opener, since a renderer hides every line after it; a
            line that begins `<!--`, since a record carries no HTML comment
            (#1012); and a fence line the walk cannot place, because a line
            above it opens an HTML block or a fence stands in a list item, a
            block quote or an indent, so no block from there on is read
  named     a fence outside every fence whose info string's first word,
            case folded, is `seal`, and whose line is not exactly the
            opener: no block, and its lines are no fields. A notice changes
            no exit code

Nothing outside a block is a field, so no line of prose is classified, and
where a field is owed, its reader refuses its absence. Where a block stands
in a record and how many a record holds are its reader's rules
(`skills/code-review/scripts/chain_check.py`), since they turn on headings
this module does not read.

`assemble` is the one way a command writes a block: it builds the block from
`(key, value)` pairs and refuses pairs this reader would refuse.

Standard library only; it imports `blocks` beside it. `chain_check.py`,
`broad_gate.py` and `unverified_check.py` load it by path, as they load
`hooks/lib/routing.py`; `seal_stamp.py`, which the stamp hooks load, and
`pr_body.py` reach it through `chain_check.FIELDS`.
"""

import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import blocks
except ImportError as missing:
    raise ImportError(
        "cannot read "
        + os.path.join(os.path.dirname(os.path.abspath(__file__)), "blocks.py")
        + ", and it is the walk this reader reads a record's fences through. "
        "This file ships beside it under `hooks/`; a copy of one taken on its "
        "own is not a plugin"
    ) from missing

# The info string, and the one line that opens a block.
INFO = "seal"
FENCE = "`" * 3
OPENER = FENCE + INFO
# A fence run, once a line's container markers are taken off.
FENCE_RUN = re.compile(r"`{3,}|~{3,}")
COMMENT_OPENER = "<" + "!--"

ONE, AT_MOST_ONE = "one", "at most one"

# The keys, each spelt as a line opens with it.
TARGET = "target:"
ORIGINAL = "original:"
SEVERITY = "severity:"
LOCATION = "location:"
EVIDENCE = "evidence:"
REGRESSION = "regression:"
REOPENS = "reopens:"
VERDICT = "verdict:"
ANSWER = "answer:"
CONFIRMS = "confirms:"
SEALER_VERDICT = "Verdict:"
RUN = "run:"

# The sealer's three verdict words.
SEALED = "sealed"
WITHHELD = "withheld"
UNDECIDED = "undecided"

COMMIT = r"[0-9a-f]{7,40}"
PATH = r"`[^`\s:/#][^`\s:#]*"
SPAN = r"(?::[0-9]+(?:-[0-9]+)?)?"
LINES = r":[0-9]+(?:-[0-9]+)?"


class Spec:
    """One key of a kind: the shape its value matches whole, how many a
    block holds, and what a refusal of its value says."""

    def __init__(self, shape, many, says):
        self.shape = re.compile(shape)
        self.many = many
        self.says = says


class Kind:
    """A block's kind: its name, its keys in order, the first opening it,
    and the pairs of keys a block holds one of at most."""

    def __init__(self, name, keys, one_of=()):
        self.name = name
        self.keys = keys
        self.one_of = one_of
        self.opener = next(iter(keys))

    def __repr__(self):
        return f"Kind({self.name!r})"


# The kinds. Each value's shape is the `Shape` cell the round record's
# grammar table in `docs/the-review-record.md` gave its label before #1198,
# and `verdict:` takes no `open`: a finding with no close block is open.
ORIGINAL_SPEC = Spec(
    rf"(?P<commit>{COMMIT})",
    AT_MOST_ONE,
    "it names the migration config's baseline commit, as 7 to 40 hex digits",
)
ROUND_BLOCK = Kind(
    "round",
    {
        TARGET: Spec(
            rf"(?P<commit>{COMMIT})(?: against [\w./-]*\w|, fixes {COMMIT}\.\.{COMMIT})",
            ONE,
            "it names the reviewed commit as `<sha> against <base>`, or `<sha>, "
            "fixes <a>..<b>` for a verifying round",
        ),
        ORIGINAL: ORIGINAL_SPEC,
    },
)
FINDING_BLOCK = Kind(
    "finding",
    {
        SEVERITY: Spec(r"must|should", ONE, "a severity is `must` or `should`"),
        LOCATION: Spec(
            rf"{PATH}{SPAN}`(?:, {PATH}{SPAN}`)*",
            ONE,
            "a location is one or more of `path`, `path:line` or "
            "`path:first-last`, each backticked, joined by `, `",
        ),
        EVIDENCE: Spec(
            rf"executed `[^`]+`(?:, `[^`]+`)*|read {PATH}{LINES}`(?:, {PATH}{LINES}`)*",
            ONE,
            "evidence is `executed` and each command run, or `read` and each "
            "`path:line` or `path:first-last` opened, each backticked, joined "
            "by `, `",
        ),
        REGRESSION: Spec(
            r"round-(?P<round>[1-9][0-9]*)(?:#(?P<finding>[1-9][0-9]*))?",
            AT_MOST_ONE,
            "a reference is `round-<N>#<n>` or `round-<N>`",
        ),
        REOPENS: Spec(
            r"round-(?P<round>[1-9][0-9]*)#(?P<finding>[1-9][0-9]*)",
            AT_MOST_ONE,
            "a reopened close is a finding's, so the reference is `round-<N>#<n>`",
        ),
    },
    one_of=((REGRESSION, REOPENS),),
)
CLOSE_BLOCK = Kind(
    "close",
    {
        VERDICT: Spec(
            rf"rejected|fixed (?P<commit>{COMMIT})|deferred (?P<home>\S(?:.*\S)?)",
            ONE,
            "a verdict is `fixed <commit>`, `rejected` or `deferred <home>`",
        ),
        ANSWER: Spec(r".*", ONE, "an answer is prose after the key"),
        LOCATION: Spec(
            rf"{PATH}{SPAN}`(?:, {PATH}{SPAN}`)*",
            AT_MOST_ONE,
            "a location is one or more of `path`, `path:line` or "
            "`path:first-last`, each backticked, joined by `, `",
        ),
    },
)
CONFIRMATION_BLOCK = Kind(
    "confirmation",
    {
        CONFIRMS: Spec(
            r"none|round-(?P<round>[1-9][0-9]*)#(?P<finding>[1-9][0-9]*)",
            ONE,
            "it is `round-<N>#<n>` or `none`",
        ),
    },
)
VERDICT_BLOCK = Kind(
    "verdict",
    {
        TARGET: Spec(
            rf"(?P<commit>{COMMIT}) against (?P<base>\S+)",
            ONE,
            "it names the audited commit as `<sha> against <base>`, each one word",
        ),
        ORIGINAL: ORIGINAL_SPEC,
        SEALER_VERDICT: Spec(
            rf"{SEALED}|{WITHHELD} reason: \S.*|{UNDECIDED} question: \S.*",
            ONE,
            f"the verdict reads `{SEALER_VERDICT} {SEALED}`, `{SEALER_VERDICT} "
            f"{WITHHELD} reason: <reason>` or `{SEALER_VERDICT} {UNDECIDED} "
            "question: <question>`, written exactly so",
        ),
    },
)
RUN_BLOCK = Kind(
    "run",
    {
        RUN: Spec(
            rf"(?P<commit>{COMMIT}) against (?P<base>{COMMIT})",
            ONE,
            "a run is `<tree> against <base commit>`, each a commit's SHA",
        ),
    },
)

# The kinds each record holds; within one record, a first key names one kind.
ROUND_RECORD = (ROUND_BLOCK, FINDING_BLOCK, CLOSE_BLOCK, CONFIRMATION_BLOCK)
GUARANTEE = (VERDICT_BLOCK,)
GATE = (RUN_BLOCK,)

# What each refusal and notice says.
UNCLOSED = (
    "a fence opened here never closes, so every line after it is hidden from the reader"
)
# `skills/verify/scripts/unverified_check.py#COMMENT_LINE` is this sentence,
# for every other reader of a record.
COMMENT_LINE = (
    "the line begins with `<!--`, and a record carries no HTML comment: the "
    "check reads one as text, so delete the comment"
)
UNSURE = (
    "the walk cannot place this fence line: a line above it opens an HTML "
    "block, or a fence stands in a list item, a block quote or an indent, so "
    "no `seal` block from there on is read; write each fence at the start of "
    "its line"
)
EMPTY = "an empty `seal` block: its first line opens with {openers}"
NO_KIND = (
    "`{line}` opens no `seal` block this record holds: a block's first line "
    "opens with {openers}"
)
BLANK = (
    "a blank line inside a `seal` block: its lines are fields, one after "
    "another, and the block is not read past it"
)
NOT_A_FIELD = (
    "`{line}` is no field of a {kind} block, which takes {keys}, each "
    "written `<key>: <value>`"
)
TWICE = "a second `{key}` line: a {kind} block holds one"
ONE_OF = "`{key}` beside `{other}`: a {kind} block holds one of the two"
SHAPE = "`{line}` does not read whole as `{key} <value>`: {says}"
MISSING = "the {kind} block holds no `{key}` line, and it holds one"
NEAR = (
    "not read: `{line}` opens a fence like a `seal` block and is not one, so "
    "its lines are no fields; a `seal` block opens with three backticks and "
    "`seal` alone on the line"
)

Field = collections.namedtuple("Field", "value line match")
Block = collections.namedtuple("Block", "kind line end fields")
Read = collections.namedtuple("Read", "blocks refusals notices")


def _listed(words, last="and"):
    quoted = [f"`{w}`" for w in words]
    if len(quoted) < 2:
        return "".join(quoted)
    return f"{', '.join(quoted[:-1])} {last} {quoted[-1]}"


def _key_of(line, keys):
    """The key of KEYS that LINE is written with, or None."""
    return next((k for k in keys if line == k or line.startswith(k + " ")), None)


def _block(lines, first, last, kinds):
    """`(Block, None)` for the block whose opener is FIRST and closer LAST,
    or `(None, (line, why))` at its first refusal."""
    openers = _listed([kind.opener for kind in kinds], "or")
    if last == first + 1:
        return None, (first + 1, EMPTY.format(openers=openers))
    head = lines[first + 1]
    kind = next((k for k in kinds if _key_of(head, [k.opener])), None)
    if kind is None:
        return None, (first + 2, NO_KIND.format(line=head, openers=openers))
    got = {}
    for index in range(first + 1, last):
        line, number = lines[index], index + 1
        if not line.strip():
            return None, (number, BLANK)
        key = _key_of(line, kind.keys)
        if key is None:
            keys = _listed(kind.keys)
            return None, (
                number,
                NOT_A_FIELD.format(line=line, kind=kind.name, keys=keys),
            )
        if key in got:
            return None, (number, TWICE.format(key=key, kind=kind.name))
        for pair in kind.one_of:
            other = next((k for k in pair if k != key and k in got), None)
            if key in pair and other:
                said = ONE_OF.format(key=key, other=other, kind=kind.name)
                return None, (number, said)
        spec = kind.keys[key]
        value = line[len(key) + 1 :]
        match = spec.shape.fullmatch(value)
        if match is None:
            said = SHAPE.format(line=line, key=key, says=spec.says)
            return None, (number, said)
        got[key] = Field(value, number, match)
    for key, spec in kind.keys.items():
        if spec.many == ONE and key not in got:
            return None, (first + 1, MISSING.format(kind=kind.name, key=key))
    return Block(kind, first + 1, last + 1, got), None


def read(text, kinds):
    """`Read(blocks, refusals, notices)` of TEXT, a record holding KINDS:
    every block whose lines all parse, in order, and each refusal and notice
    as `(line, why)`, in line order."""
    lines = blocks.gfm_lines(text or "")
    walked = blocks.walk(lines)
    found, refusals, notices = [], [], []
    inside = set()
    for first in sorted(walked.opens):
        last = first + 1
        while last + 1 < len(lines) and (
            walked.kinds[last + 1] == blocks.FENCED and last + 1 not in walked.opens
        ):
            last += 1
        inside.update(range(first, last + 1))
        if lines[first] == OPENER:
            block, refused = _block(lines, first, last, kinds)
            if block is None:
                refusals.append(refused)
            else:
                found.append(block)
            continue
        words = walked.opens[first].split()
        if words and words[0].casefold() == INFO:
            notices.append((first + 1, NEAR.format(line=lines[first])))
    refusals.extend((index + 1, UNCLOSED) for index in walked.unclosed)
    for index, line in enumerate(lines):
        if index in inside or index in walked.unclosed:
            continue
        if line.lstrip().startswith(COMMENT_OPENER):
            refusals.append((index + 1, COMMENT_LINE))
        elif walked.uncertain[index]:
            rest = line[len(blocks.CONTAINER.match(line).group(0)) :]
            if FENCE_RUN.match(rest):
                refusals.append((index + 1, UNSURE))
    return Read(found, sorted(refusals), notices)


def assemble(pairs, kinds):
    """The text of the block holding PAIRS, `(key, value)` each in order, as
    a record holding KINDS reads it. Raises ValueError with the first
    refusal's sentence where the reader would refuse it."""
    body = [f"{key} {value}" if value else key for key, value in pairs]
    text = "\n".join([OPENER, *body, FENCE]) + "\n"
    refused = read(text, kinds).refusals
    if refused:
        raise ValueError(refused[0][1])
    return text


def verdict_word(block):
    """`sealed`, `withheld` or `undecided` for a verdict block, the first
    word of its `Verdict:` value; None for a block of another kind."""
    said = block.fields.get(SEALER_VERDICT)
    return said.value.split(" ", 1)[0] if said else None
