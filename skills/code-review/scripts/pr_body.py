#!/usr/bin/env python3
"""seal pr-body: the part of a pull request body a work item's records hold,
copied from them.

  seal pr-body <item> --body <file>           write the generated part
  seal pr-body <item> --body <file> --check   say whether it is the records'

#1044. A body written by hand restated the records, and most of the sealer's
withheld verdicts were a sentence of it that restated one wrongly. This
writes the part of the body below the line `HEADING` holds from the records
themselves: the changelog fragment, the plan's `## Phases` section and the
phase records' paths, each round record's `target:` line and its findings'
labelled lines, the broad run's record, `gaps.md`'s `## Not verified` and
`## Not done` sections, and every table line of `frame/questions.md`. It
copies lines and composes none: no count, no summary, no rewording. Each
section opens with a line of `FIXED` naming its source, and a record that is
not there is named by its own line of `FIXED`.

The body opens with the orchestrator's part, the summary a reader needs
first, and `HEADING` follows it. The copy stands below that line in one
`<details>` fold, whose `<summary>` names the copy and is followed by a
blank line so the Markdown inside renders, and nothing inside it is folded
again. A rewrite keeps the orchestrator's part byte for byte, and the
squash commit keeps the fold's tags as text. `frame/design.md` *Data &
interfaces* of the work item that last reshaped this lays out the part line
for line. A copied line equal to `HEADING`,
`FOLD` or `FOLD_END` is refused at the record's line, and so is a copied
line where `close_issues_on_release.py#keywords_in` reads a closing
keyword: the `Closes` line is the orchestrator's, written above `HEADING`.

Round records are read through `chain_check.py`'s grammar, the one reader of
a round record, and a record it refuses is refused here with its sentence.
The other records' headings are read through `unverified_check.py`'s
`readable` and `sections`, so a heading inside a fence is no heading. No
record is parsed any other way.

Limits, stated here and not guarded:

- GitHub refuses a pull request body over its length limit, and
  `gh pr create` prints the refusal; nothing here repeats it.
- In local mode the records sit under the git directory, so a reader of the
  pull request cannot open the paths the generated part names. The copied
  text still stands in the body.
- A body edited on GitHub after the pull request opens is read by nobody.
- Exit 2's line names `<item>` as it was given, or the module that would not
  load by its installed path. The normal flow gives neither: the sealer is
  handed a work item's directory that exists, from an installed plugin.

Exit: 0 written, or under `--check` the part below the heading is what the
records give; 1 refused and nothing written, each cause on a line that opens
with `refused:` naming the body file by its name, or a record by its path
under the `seal/` root, and the line; 2 the arguments are unusable,
`<item>` is not a directory, or a module this loads will not load.
"""

import argparse
import difflib
import importlib.util
import os
import re
import sys

if __name__ == "__main__":
    # A record in another language prints through a console's code page.
    for _name, _errors in (("stdout", "replace"), ("stderr", "backslashreplace")):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)

HERE = os.path.dirname(os.path.abspath(__file__))
CHAIN_CHECK = os.path.join(HERE, "chain_check.py")


def _load(path, name):
    """Import a sibling script by path, or raise ImportError naming it."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Loaded once, here: `chain_check.py` with the round record's grammar it
# loads at its import and the shared markdown reader it loads,
# `hooks/lib/routing.py`, whose `round_number` is the one ordering rule of
# round records and whose `optin` names a work item's files, and
# `.github/scripts/close_issues_on_release.py`, whose `keywords_in` is the one
# reader of a closing keyword. The plugin ships from the repository root, so
# `.github/scripts/` stands three levels above HERE in a clone and in an
# installed copy alike. As a command, a module that will not load ends the
# run at exit 2; imported, the error is raised to the importer.
try:
    CHAIN = _load(CHAIN_CHECK, "agentic_chain_check_for_the_pr_body")
    ROUTING = CHAIN.load(CHAIN.ROUTING, "agentic_routing_for_the_pr_body")
    CLOSER = _load(
        os.path.join(
            HERE, "..", "..", "..", ".github", "scripts", "close_issues_on_release.py"
        ),
        "agentic_closer_for_the_pr_body",
    )
except (OSError, SyntaxError, ImportError, SystemExit, ValueError) as _exc:
    if __name__ != "__main__":
        raise
    print(
        f"seal pr-body: a reader of the records would not load ({_exc})",
        file=sys.stderr,
    )
    raise SystemExit(2) from None
READER = CHAIN.SHARED_READER
OPTIN = ROUTING.optin

# The line that ends the orchestrator's part and opens the generated one.
HEADING = "## From the records"
# The fold the generated part's sections stand in, opened under `HEADING`
# and ended on the part's last line.
FOLD = "<details>"
FOLD_END = "</details>"
# The record headings the generator reads, beside `gaps.md`'s
# `## Not verified`, which is `unverified_check.py#HEADING`.
PHASES = "## Phases"
NOT_VERIFIED = READER.HEADING
NOT_DONE = "## Not done"
# The labelled lines of a finding the generator copies beside the
# `verdict:`, `regression:` and `reopens:` lines `chain_check.py` names: rows
# of the grammar table, read through its `label_of`.
SEVERITY = "severity:"
ANSWER = "answer:"

# A work item's records, by their path under its directory.
CHANGELOG = OPTIN.CHANGELOG
PLAN = OPTIN.PLAN
PHASE_DIR = OPTIN.PHASES
ROUND_DIR = OPTIN.ROUNDS
GATE = OPTIN.GATE
GAPS = OPTIN.GAPS
QUESTIONS = OPTIN.QUESTIONS
# The phase records' names, in the shape of `routing.py#ROUND_RE`.
PHASE_RE = re.compile(r"phase-(\d+)\.md")
# What a table line opens with: a line outside a fence whose first
# character is this.
TABLE = "|"

# Every fixed line the generated part can hold. `{name}` is the work item's
# directory name and `{path}` a record's path under it.
SUMMARY = (
    f"<summary>Copied from the records in {OPTIN.HOME}/{OPTIN.WORK_ITEMS}/{{name}}/ "
    "by seal pr-body.</summary>"
)
CHANGED = "## What changed"
BUILT = "## How it was built"
REVIEWED = "## Review rounds"
BROAD = "## Broad gate"
ASKED = "## Questions"
FROM = "From `{path}`."
FROM_PHASES = "From `{path}`, its *" + PHASES.lstrip("# ") + "* section."
PHASE_LIST = "The phase records:"
PHASE_ITEM = "- `{path}`"
ROUND_HEADING = "### `{path}`"
ABSENT = "`{path}` is not in this work item."
NO_PHASE = f"`{PHASE_DIR}/` holds no phase record."
NO_ROUND = f"`{ROUND_DIR}/` holds no round record."
NO_PLAN_PHASES = f"`{PLAN}` has no `{PHASES}` section."
NO_GATE_TABLE = f"`{GATE}` holds no table line."
NO_NOT_VERIFIED = f"`{GAPS}` has no `{NOT_VERIFIED}` section."
NO_NOT_DONE = f"`{GAPS}` has no `{NOT_DONE}` section."
NO_QUESTION_TABLE = f"`{QUESTIONS}` holds no table line."
FIXED = (
    HEADING,
    FOLD,
    SUMMARY,
    FOLD_END,
    CHANGED,
    BUILT,
    REVIEWED,
    BROAD,
    NOT_VERIFIED,
    NOT_DONE,
    ASKED,
    FROM,
    FROM_PHASES,
    PHASE_LIST,
    PHASE_ITEM,
    ROUND_HEADING,
    ABSENT,
    NO_PHASE,
    NO_ROUND,
    NO_PLAN_PHASES,
    NO_GATE_TABLE,
    NO_NOT_VERIFIED,
    NO_NOT_DONE,
    NO_QUESTION_TABLE,
)


class Refused(ValueError):
    """What the generator will not copy or write, as `causes`: one
    `(where, line, why)` each, `where` a record's path under the work item,
    `""` for the work item's directory or None for the body file, and `line`
    1-based, or 0 where the cause is the whole file."""

    def __init__(self, causes):
        self.causes = list(causes)
        super().__init__("; ".join(why for _where, _line, why in self.causes))


def _phase_number(name):
    """The N in `phase-N.md`, or None when the name is not one."""
    found = PHASE_RE.fullmatch(os.path.basename(name))
    return int(found.group(1)) if found else None


def _numbered(texts, where, number):
    """`[(N, path)]` for the records of TEXTS directly in WHERE that NUMBER
    reads a number from, lowest first."""
    found = []
    for rel in texts:
        head, _, name = rel.rpartition("/")
        if head == where and number(name) is not None:
            found.append((number(name), rel))
    return sorted(found)


def _read_into(texts, item, rel):
    """TEXTS with the record at REL under ITEM, where it is a file."""
    path = os.path.join(item, *rel.split("/"))
    if not os.path.isfile(path):
        return
    try:
        with open(path, encoding="utf-8") as handle:
            texts[rel] = handle.read()
    except (OSError, UnicodeDecodeError) as exc:
        raise Refused([(rel, 0, f"cannot be read as UTF-8 text ({exc})")]) from None


def read_item(item):
    """`{path: text}` for the records `compose` copies from, by their path
    under the work item's directory ITEM, each read as UTF-8 with universal
    newlines. A record that is not there is not in the mapping. Refused
    where ITEM is not a directory or a record is not UTF-8 text."""
    if not os.path.isdir(item):
        raise Refused([("", 0, "is not a directory")])
    texts = {}
    for rel in (CHANGELOG, PLAN, GATE, GAPS, QUESTIONS):
        _read_into(texts, item, rel)
    for where, number in (
        (PHASE_DIR, _phase_number),
        (ROUND_DIR, ROUTING.round_number),
    ):
        directory = os.path.join(item, *where.split("/"))
        if os.path.isdir(directory):
            for name in sorted(os.listdir(directory)):
                if number(name) is not None:
                    _read_into(texts, item, f"{where}/{name}")
    return texts


def _copied(rel, raw, first, stop):
    """The lines RAW holds from FIRST to STOP, each with its source `(REL,
    line)`, with blank lines at either end dropped."""
    picked = [(raw[i], (rel, i + 1)) for i in range(first, stop)]
    while picked and not picked[0][0].strip():
        picked.pop(0)
    while picked and not picked[-1][0].strip():
        picked.pop()
    return picked


def _fixed(line):
    """One block of one fixed line, which no record is the source of."""
    return [(line, None)]


def _section(rel, text, heading):
    """`(the raw lines, first, stop)` for the one HEADING section of TEXT,
    its heading left out, or None where TEXT has none. Refused at the second
    where it has two, since copying one would leave the other out."""
    seen = READER.readable(text)
    starts = READER.sections(seen, heading)
    if not starts:
        return None
    if len(starts) > 1:
        raise Refused(
            [(rel, starts[1] + 1, f"a second `{heading}` section; the body copies one")]
        )
    return (
        READER.gfm_lines(text),
        starts[0] + 1,
        CHAIN.section_end(READER, seen, starts[0]),
    )


def _changed(texts):
    if CHANGELOG not in texts:
        return [_fixed(CHANGED), _fixed(ABSENT.format(path=CHANGELOG))]
    raw = READER.gfm_lines(texts[CHANGELOG])
    return [
        _fixed(CHANGED),
        _fixed(FROM.format(path=CHANGELOG)),
        _copied(CHANGELOG, raw, 0, len(raw)),
    ]


def _built(texts):
    blocks = [_fixed(BUILT)]
    found = _section(PLAN, texts[PLAN], PHASES) if PLAN in texts else None
    if PLAN not in texts:
        blocks.append(_fixed(ABSENT.format(path=PLAN)))
    elif found is None:
        blocks.append(_fixed(NO_PLAN_PHASES))
    else:
        blocks.append(_fixed(FROM_PHASES.format(path=PLAN)))
        blocks.append(_copied(PLAN, *found))
    phases = _numbered(texts, PHASE_DIR, _phase_number)
    if not phases:
        blocks.append(_fixed(NO_PHASE))
    else:
        blocks.append(_fixed(PHASE_LIST))
        blocks.append([(PHASE_ITEM.format(path=rel), None) for _n, rel in phases])
    return blocks


def _round(rel, number, text):
    """The blocks of one round record, read through `chain_check.py`."""
    _found, errors = CHAIN.round_of(READER, text, rel, number)
    if errors:
        raise Refused(errors)
    raw, seen = READER.gfm_lines(text), READER.readable(text)
    section, spans, _error = CHAIN.finding_spans(READER, seen)
    inside = {i for first, stop in spans for i in range(first, stop)}
    target = [
        i
        for i, line in enumerate(seen)
        if i not in inside and CHAIN.label_of(line) == CHAIN.TARGET_ROW
    ]
    blocks = [_fixed(ROUND_HEADING.format(path=rel))]
    blocks += [[(raw[i], (rel, i + 1))] for i in target]
    if section is not None:
        start, end = section
        blocks.append(_copied(rel, raw, start + 1, spans[0][0] if spans else end))
    for first, stop in spans:
        blocks.append([("#" + raw[first].lstrip(" "), (rel, first + 1))])
        for label in (
            SEVERITY,
            CHAIN.VERDICT_ROW,
            CHAIN.REGRESSION_ROW,
            CHAIN.REOPENS_ROW,
        ):
            blocks += [
                [(raw[i], (rel, i + 1))]
                for i in range(first + 1, stop)
                if CHAIN.label_of(seen[i]) == label
            ]
        for i in range(first + 1, stop):
            if CHAIN.label_of(seen[i]) == ANSWER:
                end = i
                while end < stop and raw[end].strip():
                    end += 1
                blocks.append(_copied(rel, raw, i, end))
                break
    return blocks


def _rounds(texts):
    blocks = [_fixed(REVIEWED)]
    rounds = _numbered(texts, ROUND_DIR, ROUTING.round_number)
    if not rounds:
        blocks.append(_fixed(NO_ROUND))
    for number, rel in rounds:
        blocks += _round(rel, number, texts[rel])
    return blocks


def _tables(text):
    """The indexes of TEXT's table lines, outside every fence."""
    return [i for i, line in enumerate(READER.readable(text)) if line[:1] == TABLE]


def _gate(texts):
    if GATE not in texts:
        return [_fixed(BROAD), _fixed(ABSENT.format(path=GATE))]
    tables = _tables(texts[GATE])
    if not tables:
        return [_fixed(BROAD), _fixed(NO_GATE_TABLE)]
    raw = READER.gfm_lines(texts[GATE])
    return [
        _fixed(BROAD),
        _fixed(FROM.format(path=GATE)),
        _copied(GATE, raw, tables[0], len(raw)),
    ]


def _gaps(texts, heading, missing):
    if GAPS not in texts:
        return [_fixed(heading), _fixed(ABSENT.format(path=GAPS))]
    found = _section(GAPS, texts[GAPS], heading)
    if found is None:
        return [_fixed(heading), _fixed(missing)]
    return [_fixed(heading), _fixed(FROM.format(path=GAPS)), _copied(GAPS, *found)]


def _questions(texts):
    if QUESTIONS not in texts:
        return [_fixed(ASKED), _fixed(ABSENT.format(path=QUESTIONS))]
    tables = _tables(texts[QUESTIONS])
    if not tables:
        return [_fixed(ASKED), _fixed(NO_QUESTION_TABLE)]
    raw = READER.gfm_lines(texts[QUESTIONS])
    return [
        _fixed(ASKED),
        _fixed(FROM.format(path=QUESTIONS)),
        [(raw[i], (QUESTIONS, i + 1)) for i in tables],
    ]


def _claims(rel, line, seen):
    """`(rel, line, why)` for each issue a closing keyword on the copied line
    LINE of REL claims, read by `CLOSER.keywords_in` over SEEN, the record's
    `readable` lines, so a fenced line and a code span claim nothing."""
    return [
        (
            rel,
            line,
            f"a closing keyword before #{number} would close that issue when "
            f"this pull request ships; the `Closes` line is the orchestrator's "
            f"alone, above `{HEADING}`, so write #{number} here in a code span",
        )
        for number in CLOSER.keywords_in(seen[line - 1])
    ]


def _composed(name, texts):
    """`[(line, source)]` for the generated part below `HEADING`, that line
    left out: a blank line, `FOLD`, the summary naming the copy, a blank
    line, each section followed by a blank line, and `FOLD_END`. `source`
    is `(path, line)` for a copied line and None for a fixed one. Refused at
    the record's line where a copied line is equal to `HEADING`, which would
    stand inside the fold as a second boundary line, or, outside a fence, to
    `FOLD` or `FOLD_END`, which would fold a part again or end the fold
    early, or where it holds a closing keyword outside a fence and a code
    span, since GitHub and the release's closer would close the issue it
    names."""
    blocks = _changed(texts)
    blocks += _built(texts)
    blocks += _rounds(texts)
    blocks += _gate(texts)
    blocks += _gaps(texts, NOT_VERIFIED, NO_NOT_VERIFIED)
    blocks += _gaps(texts, NOT_DONE, NO_NOT_DONE)
    blocks += _questions(texts)
    below = [("", None), (FOLD, None), (SUMMARY.format(name=name), None), ("", None)]
    for block in blocks:
        if block:
            below += [*block, ("", None)]
    below.append((FOLD_END, None))
    seen = {rel: READER.readable(text) for rel, text in texts.items()}
    causes = []
    for said, (rel, line) in (pair for pair in below if pair[1]):
        if said == HEADING:
            causes.append(
                (
                    rel,
                    line,
                    f"reads `{HEADING}`, the line the body's two parts split at",
                )
            )
        elif seen[rel][line - 1] in (FOLD, FOLD_END):
            causes.append(
                (
                    rel,
                    line,
                    f"reads `{said}`, which would fold the copy again or end "
                    f"its one `{FOLD}` early",
                )
            )
        causes += _claims(rel, line, seen[rel])
    if causes:
        raise Refused(causes)
    return below


def _joined(below):
    return "\n".join(line for line, _source in below) + "\n"


def compose(name, texts):
    """The generated part of the body for the work item called NAME, from
    `read_item`'s mapping TEXTS: `HEADING`, then `_composed`'s lines, the
    fold's end the last."""
    return HEADING + "\n" + _joined(_composed(name, texts))


def split(body):
    """`(own, generated)`: the text of BODY before its first line equal to
    `HEADING`, the orchestrator's part, and the text after that line, each
    as its bytes stood. Refused where no line equals it."""
    lines = READER.gfm_lines(body, keepends=True)
    for i, line in enumerate(lines):
        if line.rstrip("\r\n") == HEADING:
            return "".join(lines[:i]), "".join(lines[i + 1 :])
    raise Refused(
        [
            (
                None,
                0,
                f"no line reads `{HEADING}`, so the body has no part of its own to keep",
            )
        ]
    )


def _body(path):
    """The body file's text as its bytes stand, or None where it is absent."""
    try:
        with open(path, encoding="utf-8", newline="") as handle:
            return handle.read()
    except FileNotFoundError:
        return None
    except (OSError, UnicodeDecodeError) as exc:
        raise Refused([(None, 0, f"cannot be read as UTF-8 text ({exc})")]) from None


def _source(pair):
    line, source = pair
    if source is None:
        return f"`{line}`, a fixed line"
    return f"`{line}` at `{source[0]}:{source[1]}`"


def _check(below, body):
    """Refused, at each line where it differs, counted from BODY's first
    line, where the part of BODY below `HEADING` is not BELOW's lines. The
    part above it is the orchestrator's and is not read."""
    if body is None:
        raise Refused(
            [(None, 0, "is not there; `seal pr-body <item> --body <file>` writes it")]
        )
    own, generated = split(body)
    said = READER.gfm_lines(generated)
    given = [line for line, _source in below]
    # The lines above the part: the orchestrator's, and `HEADING`'s own.
    offset = len(READER.gfm_lines(own, keepends=True)) + 1
    causes = []
    matcher = difflib.SequenceMatcher(None, said, given, autojunk=False)
    for tag, i1, _i2, j1, _j2 in matcher.get_opcodes():
        if tag == "replace":
            why = f"reads `{said[i1]}`; the records give {_source(below[j1])}"
        elif tag == "delete":
            why = f"reads `{said[i1]}`, which the records do not give"
        elif tag == "insert":
            why = f"lacks {_source(below[j1])}"
        else:
            continue
        causes.append((None, offset + i1 + 1, why))
    if causes:
        raise Refused(causes)


def _place(where, line, item, body):
    """Where a cause stands, with no machine path in it: the body file BODY
    by its name, and a record by its path under the `seal/` root, whatever
    path the work item ITEM was given by. The sealer copies the first
    `refused:` line into a `guarantee.md` that is committed."""
    if where is None:
        path = os.path.basename(body)
    else:
        name = os.path.basename(os.path.normpath(os.path.abspath(item)))
        path = "/".join(p for p in (OPTIN.HOME, OPTIN.WORK_ITEMS, name, where) if p)
    return f"{path}:{line}" if line else path


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="seal pr-body",
        description="Write the part of a pull request body a work item's "
        f"records hold, below the line `{HEADING}`, or check it.",
    )
    parser.add_argument("item", help="the work item's directory")
    parser.add_argument("--body", required=True, metavar="FILE", help="the body file")
    parser.add_argument(
        "--check",
        action="store_true",
        help="write nothing; exit 1 where the part below the heading is not the records'",
    )
    args = parser.parse_args(argv)
    if not os.path.isdir(args.item):
        print(f"seal pr-body: {args.item} is not a directory", file=sys.stderr)
        return 2
    name = os.path.basename(os.path.normpath(os.path.abspath(args.item)))
    try:
        below = _composed(name, read_item(args.item))
        body = _body(args.body)
        if args.check:
            _check(below, body)
            print(f"matches: {args.body} below `{HEADING}` is the records' text")
            return 0
        own = "" if body is None else split(body)[0]
        try:
            with open(args.body, "w", encoding="utf-8", newline="") as handle:
                handle.write(own + HEADING + "\n" + _joined(below))
        except OSError as exc:
            raise Refused([(None, 0, f"cannot be written ({exc})")]) from None
    except Refused as refused:
        for where, line, why in refused.causes:
            print(f"refused: {_place(where, line, args.item, args.body)}: {why}")
        return 1
    print(f"wrote: {args.body} below `{HEADING}` from {args.item}'s records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
