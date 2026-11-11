#!/usr/bin/env python3
"""seal pr-body: a pull request body, the work item's first part, its
`pr.<lang>.md` where the two language keys differ and its `pr.md`, and then
the part its other records hold, copied from them.

  seal pr-body <item> --body <file>           write the body
  seal pr-body <item> --body <file> --check   say whether it is still theirs

#1044. A body written by hand restated the records, and most of the sealer's
withheld verdicts were a sentence of it that restated one wrongly. This
writes the part of the body below the line `HEADING` holds from the records
themselves: the changelog fragment, the plan's `## Phases` section and the
phase records' paths, each round record's `seal` blocks and its findings'
headings, the broad run's `seal` blocks, `gaps.md`'s `## Not verified` and
`## Not done` sections, and every table line of `frame/questions.md`. It
copies lines and composes none: no count, no summary, no rewording. Each
section opens with a line of `FIXED` naming its source, and a record that is
not there is named by its own line of `FIXED`.

One fixed line depends on a record's verdict (#1204): the seal mark, `MARK`,
the plugin's icon at the default branch of the plugin's repository, stands
between `HEADING` and the changelog's section where `seal/config.json`'s
`Pull request seal mark` key reads `yes` and the work item's `guarantee.md`
reads `sealed` at HEAD, as `seal_mark` reads them. Its address is built
from the plugin's manifest, which is read and never written, and names no
version, so two releases of the plugin compose one line (#1452). It carries
no record text, and `--check` composes it the same way, so the sealer's
check, run before its own verdict exists, reads a part with no mark from
that run. The key and HEAD are read in the work item's own checkout, and in
the working directory's where the item sits under the common git directory.
A value other than `yes`, a seal that checkout cannot be read against, and
a manifest the address cannot be built from are named on one line opening
`seal pr-body:` and change no exit code.

The body opens with the orchestrator's part, its files written as their
bytes stand, and `HEADING` follows it on its own line (#1453). The part is
composed from `seal/config.json`'s `Commit and pull request language` and
`Record language` keys, read as the mark key is and compared with case
folded. Where they name different languages, the part is the work item's
one file matching `pr.*.md` beside `pr.md`, its renderings in the commit
language, then `pr.md`; where they name one language, it is `pr.md`, then
any such file in name order. The file's middle part names its
language for a person and is read by nothing here. The orchestrator commits
the files before the first round, so every round reads them, and a body
file's earlier text is replaced whole. Both forms refuse at `config.json`
where either key is absent, empty or refused, at the work item's directory
where the keys differ and it holds no such file or more than one, at a
file's line where it equals `HEADING`, and at `pr.md` where it is not
there. Below the line `HEADING` holds, the changelog fragment stands
first, whole and outside any fold, so the pull request's reader meets it
before the fold (#1478), and the rest of the copy stands in one `<details>`
fold, whose `<summary>` names the copy and is followed by a blank line so
the Markdown inside renders, and nothing inside it is folded again. The
squash commit keeps the fold's tags as text. `frame/design.md` *Data &
interfaces* of the work item that last reshaped this lays out the body line
for line. A copied line equal to `HEADING` is refused at the record's
line, and so is a copied line holding a `details` tag, `<details` or
`</details` in any case followed by whitespace, `/`, `>` or the line's end,
outside a fence, an HTML comment and a code span (#1218, #1181), and a
copied line where `close_issues_on_release.py#keywords_in` reads a closing
keyword: the `Closes` line is the orchestrator's, written in `pr.md`.
The comment is read on the copied line alone, as
`close_issues_on_release.py#HIDDEN` reads it: one that closes on the line
hides what it holds, and a `<!--` with no `-->` after it on the line is
text where other text stands before it. A copied line that begins with
such a `<!--`, after nothing but spaces, tabs and block markers, is refused
at its line whatever follows it, since GitHub hides the lines after it, the
fold's end among them (#1405).

Round records are read through `chain_check.py#round_read`, which places the
blocks `lib/fields.py` reads by the record's headings, and
`trail/gate.md` through `lib/fields.py`, the one reader of a record's
`seal` blocks; a record either refuses is refused here with its sentence. The other records' headings are read through `unverified_check.py`'s
`readable` and `sections`, so a heading inside a fence is no heading. No
record is parsed any other way.

Limits, stated here and not guarded:

- GitHub refuses a pull request body over its length limit, and
  `gh pr create` prints the refusal; nothing here repeats it.
- In local mode the records sit under the git directory, so a reader of the
  pull request cannot open the paths the generated part names. The copied
  text still stands in the body.
- A body edited on GitHub after the pull request opens is read by the pull
  request's check, `chain_check.py#body`, through `compared`, where the
  workflow runs on `edited`. In local mode nothing is committed for that
  check to read, so nothing reads such a body.
- The `details` tag reading reads characters, not GitHub's rendering. A tag
  GitHub renders as text is refused too where it is spelt as a tag outside a
  code span and a comment: in a table cell, after a backslash, in an indented
  code block. A tag between two backticks that GitHub does not read as a
  code span, such as an escaped backtick, is read as inside a span and
  passes.
- The opener reading reads one line, not GitHub's blocks. Where CommonMark's
  block rules make GitHub show the lines after an opener the reading treats
  as a line start, such as one in an indented code block (#1410), the line
  is refused too. Behind a list marker or a quote marker GitHub hides them,
  as the refusal assumes (#1408, #1409).
- Exit 2's line names `<item>` as it was given, or the module that would not
  load by its installed path. The normal flow gives neither: the sealer is
  handed a work item's directory that exists, from an installed plugin.

Exit: 0 written, or under `--check` the part above the heading is the lines
of the files the keys ask for, in their order, and the part below it what
the records give; 1 refused and nothing written, each cause on a line that
opens with `refused:` naming the body file by its name, or a record or
`config.json` by its path under the `seal/` root, and the line; 2 the
arguments are unusable,
`<item>` is not a directory, or a module this loads will not load.
"""

import argparse
import difflib
import fnmatch
import html
import json
import os
import posixpath
import re
import sys

if __name__ == "__main__":
    # A record in another language prints through a console's code page.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, "..", "..", "..", "lib")

# `lib/sibling.py` loads every other module this command reads. Where it is
# absent, the refusal is its own sentence about itself, spelt here because
# the file that holds the sentence is the one missing.
sys.path.insert(0, LIB)
try:
    import sibling
except ImportError:
    sys.stderr.write(
        "cannot read "
        + os.path.normpath(os.path.join(LIB, "sibling.py"))
        + ", which this command loads. It ships in the plugin beside this "
        "script; a copy of one script taken on its own is not a plugin. "
        "Nothing was read.\n"
    )
    raise SystemExit(2) from None

# Loaded once, here: `chain_check.py` with the block reader and the shared
# markdown reader it loads at its import,
# `lib/routing.py`, whose `round_number` is the one ordering rule of
# round records and whose `optin` names a work item's files,
# `lib/config.py`, the one reader of a `seal/config.json` key, and
# `.github/scripts/close_issues_on_release.py`, whose `keywords_in` is the one
# reader of a closing keyword. The plugin ships from the repository root, so
# `.github/scripts/` stands in an installed copy as in a clone. An absent
# file is `lib/sibling.py#load`'s sentence and exit 2. As a command, a
# module that raises while it loads ends the run at exit 2; imported, the
# error is raised to the importer.
try:
    CHAIN = sibling.load("skills/code-review/scripts/chain_check.py")
    ROUTING = sibling.load("lib/routing.py")
    CONFIG = sibling.load("lib/config.py")
    CLOSER = sibling.load(".github/scripts/close_issues_on_release.py")
except (OSError, SyntaxError, ImportError, ValueError) as _exc:
    if __name__ != "__main__":
        raise
    print(
        f"seal pr-body: a reader of the records would not load ({_exc})",
        file=sys.stderr,
    )
    raise SystemExit(2) from None
READER = CHAIN.SHARED_READER
OPTIN = ROUTING.optin

# The line that ends the orchestrator's part, `first_part`'s files, and
# opens the generated one.
HEADING = "## From the records"
# The fold the generated part's sections after the changelog's stand in,
# opened under the changelog's section and ended on the part's last line.
FOLD = "<details>"
FOLD_END = "</details>"
# A `details` tag on a copied line, as GitHub reads one (#1218): `<details`
# or `</details`, in any case and anywhere in the line, followed by
# whitespace, `/`, `>` or the line's end, read once fences and code spans
# are blanked. It opens a second fold, or, on a line inside the copy's one
# fold, ends that fold early, whether the line is a sentence, a list item
# or indented. The form a
# record gives such a tag is a code span, the one spelling that passes;
# what follows the lookahead, up to a `>`, only names the tag as read.
TAG = re.compile(r"</?details(?=[\s/>]|$)[^>]*>?", re.IGNORECASE)
# The record headings the generator reads, beside `gaps.md`'s
# `## Not verified`, which is `unverified_check.py#HEADING`.
PHASES = "## Phases"
NOT_VERIFIED = READER.HEADING
NOT_DONE = "## Not done"

# A work item's records, by their path under its directory.
CHANGELOG = OPTIN.CHANGELOG
PLAN = OPTIN.PLAN
PHASE_DIR = OPTIN.PHASES
ROUND_DIR = OPTIN.ROUNDS
GATE = OPTIN.GATE
GAPS = OPTIN.GAPS
QUESTIONS = OPTIN.QUESTIONS
# The orchestrator's own file of the body's first part, which `read_own`
# reads and no section copies.
OWN_PART = OPTIN.PR
NO_OWN_PART = "is not there; the orchestrator writes it before the first round"

# #1453: the two keys `first_part` composes the first part from, read through
# `lib/config.py#declared_value` as `MARK_KEY` is, and the translated file
# beside `pr.md` the keys ask for where they name different languages: a
# file matching `TRANSLATED`, whose middle part nothing reads.
COMMIT_KEY = "Commit and pull request language"
RECORD_KEY = "Record language"
TRANSLATED = "pr.*.md"
# The root's `config.json` by its path from a work item's directory, which
# stands at `<root>/threads/<id>`: where a cause about a key stands.
ROOT_CONFIG = "../../" + CONFIG.CONFIG
NO_KEY = (
    "names no language in a `{key}` key; `templates/setup/config.md` *{key}* "
    "says what the key governs, and the orchestrator asks for it before the "
    "first edit"
)
NO_TRANSLATION = (
    f"`{COMMIT_KEY}` reads `{{commit}}` and `{RECORD_KEY}` reads `{{record}}`, "
    f"and no `pr.<lang>.md` stands beside `{OWN_PART}`; the orchestrator writes "
    "it before the first round"
)
TRANSLATIONS = (
    f"holds {{count}} files matching `{TRANSLATED}`, {{names}}, and one body has "
    "one translation"
)
# The phase records' names, in the shape of `routing.py#ROUND_RE`.
PHASE_RE = re.compile(r"phase-(\d+)\.md")
# What a table line opens with: a line outside a fence whose first
# character is this.
TABLE = "|"

# Every fixed line the generated part can hold, beside the seal mark,
# `MARK`. `{name}` is the work item's directory name, `{path}` a record's
# path under it, and `{home}` the root's name, `_in_tree`'s.
SUMMARY = (
    f"<summary>Copied from the records in {{home}}/{OPTIN.WORK_ITEMS}/{{name}}/ "
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
NO_GATE_BLOCK = f"`{GATE}` holds no run block."
NO_NOT_VERIFIED = f"`{GAPS}` has no `{NOT_VERIFIED}` section."
NO_NOT_DONE = f"`{GAPS}` has no `{NOT_DONE}` section."
NO_QUESTION_TABLE = f"`{QUESTIONS}` holds no table line."

# #1204: the seal mark, one fixed line between `HEADING`'s blank line and
# `FOLD`, written where `seal/config.json`'s `MARK_KEY` reads `MARK_ON`
# exactly and the work item is sealed at HEAD (`seal_mark`). Its address is
# built from the plugin's manifest, which stands three levels above HERE as
# `.github/scripts/` does, and which this reads and never writes.
MARK_KEY = "Pull request seal mark"
MARK_ON = "yes"
MANIFEST = os.path.join(HERE, "..", "..", "..", ".claude-plugin", "plugin.json")
MANIFEST_NAME = ".claude-plugin/plugin.json"
MARK_FIELDS = ("repository", "icon")
MARK = '<img src="{src}" alt="{alt}" width="{width}">'
MARK_ALT = "Sealed"
MARK_WIDTH = 128
# What `seal_mark` says where the mark is not written and nothing else
# names why; printed after `seal pr-body: `.
NO_MARK = "the body carries no seal mark"
KEY_NOT_YES = (
    f"`{MARK_KEY}` reads `{{value}}`, not `{MARK_ON}`, so the key is not read "
    f"and {NO_MARK}"
)
KEY_REFUSED = f"`{MARK_KEY}` is not read: {{why}}; {NO_MARK}"
BASE_UNSEEN = (
    "the guarantee names the base `{base}`, which this repository cannot "
    f"resolve, so whether its seal is at HEAD is not read and {NO_MARK}"
)
NOT_IN_HISTORY = (
    "the guarantee is sealed at `{commit}`, which HEAD in {root} does not "
    f"hold, so whether its seal is at HEAD is not read and {NO_MARK}"
)
NO_MANIFEST = (
    f"`{MANIFEST_NAME}` is not read ({{why}}), so the mark's address is not "
    f"built and {NO_MARK}"
)
NO_FIELD = (
    f"`{MANIFEST_NAME}` has no `{{field}}`, so the mark's address is not built "
    f"and {NO_MARK}"
)

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
    NO_GATE_BLOCK,
    NO_NOT_VERIFIED,
    NO_NOT_DONE,
    NO_QUESTION_TABLE,
)


class Refused(ValueError):
    """What the generator will not copy or write, as `causes`: one
    `(where, line, why)` each, `where` a record's path under the work item,
    `ROOT_CONFIG` for the root's `config.json`, `""` for the work item's
    directory or None for the body file, and `line`
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


def read_own(item, name=OWN_PART):
    """The text of NAME, `pr.md` where none is given, in the work item's
    directory ITEM, a file of the body's first part, as its bytes stand,
    with a line end after its last line where it has none, so what follows
    it stands on its own line. Refused at NAME where it is not there or not
    UTF-8 text, and at its line where a line equals `HEADING`, since the
    body would split there."""
    path = os.path.join(item, name)
    if not os.path.isfile(path):
        raise Refused([(name, 0, NO_OWN_PART)])
    try:
        with open(path, encoding="utf-8", newline="") as handle:
            text = handle.read()
    except (OSError, UnicodeDecodeError) as exc:
        raise Refused([(name, 0, f"cannot be read as UTF-8 text ({exc})")]) from None
    for i, line in enumerate(READER.gfm_lines(text)):
        if line == HEADING:
            raise Refused(
                [
                    (
                        name,
                        i + 1,
                        f"reads `{HEADING}`, the line the body's two parts split at",
                    )
                ]
            )
    if text and not text.endswith(("\n", "\r")):
        text += "\n"
    return text


def first_part(item, root):
    """`[(name, text)]`, the files of the body's part above `HEADING` for the
    work item's directory ITEM in the repository at ROOT, in their order,
    each as `read_own` reads it (#1453).

    The two language keys are read from the root's `config.json` through
    `lib/config.py#declared_value`, in the same checkout `seal_mark` reads,
    and compared with case folded. Where they name different languages,
    the work item's one file matching `TRANSLATED` comes first, then
    `pr.md`; where they name one language, `pr.md` comes first, then each
    such file in name order. Refused at the root's `config.json`, one cause
    per key, where a key is absent, empty or refused, a file no key can be
    read from among them; and on the work item's directory where the keys
    differ and it holds no such file, or more than one."""
    home = OPTIN.home_at(root)
    values, causes = [], []
    for key in (COMMIT_KEY, RECORD_KEY):
        value, refused = CONFIG.declared_value(home, key)
        if refused is not None:
            # A file that will not read is named once, by the path `_place`
            # gives, not by this machine's.
            path = CONFIG.config_path(home) + " "
            cause = (
                ROOT_CONFIG,
                0,
                refused[len(path) :] if refused.startswith(path) else refused,
            )
        elif not value:
            cause = (ROOT_CONFIG, 0, NO_KEY.format(key=key))
        else:
            values.append(value)
            continue
        if cause not in causes:
            causes.append(cause)
    if causes:
        raise Refused(causes)
    own = read_own(item)
    found = sorted(
        name
        for name in os.listdir(item)
        if fnmatch.fnmatchcase(name, TRANSLATED)
        and os.path.isfile(os.path.join(item, name))
    )
    commit, record = values
    if commit.casefold() == record.casefold():
        return [(OWN_PART, own)] + [(name, read_own(item, name)) for name in found]
    if not found:
        raise Refused([("", 0, NO_TRANSLATION.format(commit=commit, record=record))])
    if len(found) > 1:
        names = ", ".join(f"`{name}`" for name in found[:-1]) + f" and `{found[-1]}`"
        raise Refused([("", 0, TRANSLATIONS.format(count=len(found), names=names))])
    return [(found[0], read_own(item, found[0])), (OWN_PART, own)]


def _names(parts):
    """The files of PARTS, `first_part`'s, in order, for a line a person reads."""
    return " then ".join(f"`{name}`" for name, _text in parts)


def _in_tree(root):
    """The `/`-joined name the records stand under in the repository at
    ROOT: the shared root's name in the tree, `lib/optin.py#home_name`'s,
    which is `seal` or, beside a project's own `seal/`, the second name
    (#1059); and `lib/optin.py#HOME` where the root is local or absent,
    the name the text gives the root, since no path in the tree holds it."""
    return OPTIN.home_name(root) or OPTIN.HOME


def _seal_at_head(item, root, base=None):
    """`(sealed, note)`: whether `guarantee.md` in the work item's directory
    ITEM is sealed at HEAD of the repository at ROOT, the way
    `chain_check.py#guarantee` asks it. Its blocks are read through
    `lib/fields.py` with no refusal, the newest reads `sealed`, and
    `chain_check.py#follows` finds the commit its `target:` names to be
    HEAD or followed only by the closing records. The base `follows` reads
    against is BASE where it is given, the base the pull request's check
    runs against and its guarantee arm reads, so a commit the base gained
    after the seal, which the merge commit CI checks out reaches, is not
    read as following the seal (#1452); and otherwise the base the same
    `target:` line names, which is right at the branch head, where no later
    base commit is reachable. NOTE names what ROOT cannot read the seal
    against: a base it cannot resolve, where `follows` would list no later
    commit, and a sealed commit its HEAD does not hold, as in a checkout
    other than the work item's. Every other way of not being sealed is the
    sealer's and the pull request check's to name."""
    try:
        with open(os.path.join(item, OPTIN.GUARANTEE), encoding="utf-8") as handle:
            text = handle.read()
    except (OSError, UnicodeDecodeError):
        return False, None
    found = CHAIN.FIELDS.read(text, CHAIN.FIELDS.GUARANTEE)
    if found.refusals or not found.blocks:
        return False, None
    newest = found.blocks[-1]
    if CHAIN.FIELDS.verdict_word(newest) != CHAIN.FIELDS.SEALED:
        return False, None
    target = newest.fields[CHAIN.FIELDS.TARGET].match
    base = base or target["base"]
    if (
        CHAIN.git(root, "rev-parse", "--verify", "--quiet", f"{base}^{{commit}}")
        is None
    ):
        return False, BASE_UNSEEN.format(base=base)
    name = os.path.basename(os.path.normpath(os.path.abspath(item)))
    rel = f"{_in_tree(root)}/{OPTIN.WORK_ITEMS}/{name}"
    behind = CHAIN.follows(
        root, target["commit"], base, rel, only=CHAIN.CLOSING_RECORDS
    )
    if behind is not None and behind[0] in ("unseen", "off"):
        return False, NOT_IN_HISTORY.format(commit=target["commit"], root=root)
    return behind is None, None


def _mark_line(manifest):
    """`(line, note)`: the mark built from the plugin's manifest at MANIFEST,
    its `repository`, `/raw/HEAD/` and its `icon` with a leading `./`
    dropped, escaped; or None and the sentence naming what the manifest
    lacks. The address names no version: the installed plugin writes the
    body and the pull request check's copy composes it again, and the two
    can be different releases, so the line reads nothing they differ in
    (#1452). GitHub resolves `HEAD` to the repository's default branch."""
    try:
        with open(manifest, encoding="utf-8") as handle:
            fields = json.load(handle)
    except OSError as exc:
        return None, NO_MANIFEST.format(why=exc.strerror or exc)
    except ValueError as exc:
        return None, NO_MANIFEST.format(why=exc)
    if not isinstance(fields, dict):
        fields = {}
    for field in MARK_FIELDS:
        if not isinstance(fields.get(field), str) or not fields[field]:
            return None, NO_FIELD.format(field=field)
    icon = fields["icon"]
    if icon.startswith("./"):
        icon = icon[2:]
    src = f"{fields['repository']}/raw/HEAD/{icon}"
    return MARK.format(
        src=html.escape(src), alt=html.escape(MARK_ALT), width=MARK_WIDTH
    ), None


def seal_mark(item, root, manifest=None, base=None):
    """`(line, note)` for the work item's directory ITEM in the repository
    at ROOT: the mark `_composed` writes under `HEADING`, or None, and the
    one sentence `seal pr-body` prints about it, or None (#1204).

    The mark is written where `MARK_KEY` in the root's `config.json`, read
    through `lib/config.py#declared_value`, reads `MARK_ON` exactly
    and the work item is sealed at HEAD against BASE where it is given, and
    otherwise against the guarantee's own base (`_seal_at_head`). An absent
    or empty key, and a work item not sealed at HEAD, write no mark and say
    nothing. Any other value, a refused key, a base that does not resolve,
    a sealed commit HEAD does not hold, and a manifest the address cannot be
    built from, at MANIFEST or the
    plugin's own, write no mark and are named. Nothing here refuses: the
    mark is a picture, and no key of it stops the body."""
    value, refused = CONFIG.declared_value(OPTIN.home_at(root), MARK_KEY)
    if refused is not None:
        return None, KEY_REFUSED.format(why=refused)
    if not value:
        return None, None
    if value != MARK_ON:
        return None, KEY_NOT_YES.format(value=value)
    sealed, note = _seal_at_head(item, root, base)
    if not sealed:
        return None, note
    return _mark_line(manifest or MANIFEST)


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
    """The blocks of one round record, read through `chain_check.py`, in the
    record's order: each `seal` block outside every finding, the prose under
    `## Findings` before its first finding, and each finding's heading one
    level down followed by its finding block and its close block, each
    block copied whole (#1198)."""
    parsed = CHAIN.round_read(READER, text, rel)
    if parsed.errors:
        raise Refused(parsed.errors)
    raw = READER.gfm_lines(text)

    def whole(block):
        return _copied(rel, raw, block.line - 1, block.end)

    placed = [(block.line - 1, [whole(block)]) for block in parsed.outside]
    if parsed.section is not None:
        start, end = parsed.section
        stop = parsed.spans[0][0] if parsed.spans else end
        placed.append((start + 1, [_copied(rel, raw, start + 1, stop)]))
    for k, (first, _stop) in enumerate(parsed.spans):
        heading = [("#" + raw[first].lstrip(" "), (rel, first + 1))]
        placed.append((first, [heading, *(whole(b) for b in parsed.inside[k])]))
    blocks = [_fixed(ROUND_HEADING.format(path=rel))]
    for _at, copied in sorted(placed, key=lambda pair: pair[0]):
        blocks += copied
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
    """The broad run's blocks, each copied whole through
    `lib/fields.py`, the reader the pull request's check reads them
    through; a record it refuses is refused with its sentence (#1198)."""
    if GATE not in texts:
        return [_fixed(BROAD), _fixed(ABSENT.format(path=GATE))]
    found = CHAIN.FIELDS.read(texts[GATE], CHAIN.FIELDS.GATE)
    if found.refusals:
        raise Refused([(GATE, line, why) for line, why in found.refusals])
    if not found.blocks:
        return [_fixed(BROAD), _fixed(NO_GATE_BLOCK)]
    raw = READER.gfm_lines(texts[GATE])
    return [
        _fixed(BROAD),
        _fixed(FROM.format(path=GATE)),
        *(_copied(GATE, raw, run.line - 1, run.end) for run in found.blocks),
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
    `readable` lines, so a fenced line, a comment and a code span claim
    nothing."""
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


def _laid(blocks):
    """The lines of each of BLOCKS that holds one, each block followed by a
    blank line; a block a record left empty adds nothing."""
    return [pair for block in blocks if block for pair in (*block, ("", None))]


def _composed(name, texts, mark=None, home=OPTIN.HOME):
    """`[(line, source)]` for the generated part below `HEADING`, that line
    left out: a blank line, the line MARK and a blank line where it is
    given, the changelog's section followed by a blank line, outside any
    fold so the reader meets it before the fold (#1478), `FOLD`, the summary
    naming the copy under HOME, the root's name as `_in_tree` gives it, a
    blank line, each other section followed by a blank line, and
    `FOLD_END`. `source`
    is `(path, line)` for a copied line and None for a fixed one. Refused at
    the record's line where a copied line is equal to `HEADING`, which would
    stand in the copy as a second boundary line, or begins with a `<!--`
    that no `-->` closes on the line, as `CLOSER.COMMENT`'s second arm
    matches it at the line's start, since GitHub would hide the lines after
    it and the fold's end among them, or holds a `TAG` outside a fence, a
    comment and a code span, which would fold a part again or, inside the
    fold, end it early, or holds a closing keyword outside a fence, a comment and a code
    span, since GitHub and the release's closer would close the issue it
    names. The tag and the keyword are read on one line, blanked one way, by
    `CLOSER.HIDDEN`."""
    blocks = _built(texts)
    blocks += _rounds(texts)
    blocks += _gate(texts)
    blocks += _gaps(texts, NOT_VERIFIED, NO_NOT_VERIFIED)
    blocks += _gaps(texts, NOT_DONE, NO_NOT_DONE)
    blocks += _questions(texts)
    below = [("", None)]
    if mark:
        below += [(mark, None), ("", None)]
    below += _laid(_changed(texts))
    below += [(FOLD, None), (SUMMARY.format(home=home, name=name), None), ("", None)]
    below += _laid(blocks)
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
        elif (opened := CLOSER.COMMENT.match(seen[rel][line - 1])) and (
            "-->" not in opened.group()
        ):
            causes.append(
                (
                    rel,
                    line,
                    "begins with a `<!--` that no `-->` closes on the line, and "
                    "GitHub hides the lines that follow such a line, the "
                    f"copy's other lines and the fold's end `{FOLD_END}` among "
                    "them; write the `<!--` in a code span",
                )
            )
        elif tag := TAG.search(CLOSER.HIDDEN.sub(" ", seen[rel][line - 1])):
            causes.append(
                (
                    rel,
                    line,
                    f"holds `{tag.group()}`, a `details` tag GitHub would read "
                    f"as a second fold or as the end of the copy's one "
                    f"`{FOLD}`; write it in a code span",
                )
            )
        causes += _claims(rel, line, seen[rel])
    if causes:
        raise Refused(causes)
    return below


def _joined(below):
    return "\n".join(line for line, _source in below) + "\n"


def compose(name, texts, mark=None, home=OPTIN.HOME):
    """The generated part of the body for the work item called NAME, from
    `read_item`'s mapping TEXTS: `HEADING`, then `_composed`'s lines, the
    seal mark MARK first where `seal_mark` gave one, the summary naming the
    copy under HOME, the fold's end the last."""
    return HEADING + "\n" + _joined(_composed(name, texts, mark, home))


def split(body):
    """`(own, generated)`: the text of BODY before its first line equal to
    `HEADING`, the orchestrator's part, and the text after that line, each
    as its bytes stood. Refused where no line equals it, a body 0.25.0 wrote
    among them, and the refusal names the repair."""
    lines = READER.gfm_lines(body, keepends=True)
    for i, line in enumerate(lines):
        if line.rstrip("\r\n") == HEADING:
            return "".join(lines[:i]), "".join(lines[i + 1 :])
    raise Refused(
        [
            (
                None,
                0,
                f"no line reads `{HEADING}`, so the body is not one this command "
                "wrote: run `seal pr-body <item> --body <file>`, which writes it "
                "whole, and check it again",
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


def _run(named):
    """The lines NAMED, a run a differ added or took out, each as it is
    named, in one phrase: a refusal names every line of the run, so a body
    lacking the mark and the blank line under it names the mark (#1452)."""
    return ", then ".join(named)


def _givers(names):
    """`(files, one)`: NAMES, the files a run of lines comes from, each once
    in order and joined by `and`, and whether they are one file, which the
    verb after them agrees with."""
    named = list(dict.fromkeys(names))
    return " and ".join(named), len(named) == 1


def _first_part(head, parts):
    """`(None, line, why)` for each line where HEAD, the part of the body
    above `HEADING`, is not the lines of PARTS, `first_part`'s files in
    order, counted from the body's first line; each line PARTS give is
    named with the file that gives it."""
    said = READER.gfm_lines(head)
    given, owner = [], []
    for name, text in parts:
        lines = READER.gfm_lines(text)
        given += lines
        owner += [name] * len(lines)
    causes = []
    matcher = difflib.SequenceMatcher(None, said, given, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "replace":
            why = f"reads `{said[i1]}`; {owner[j1]} gives `{given[j1]}`"
        elif tag == "delete":
            run = _run(f"`{line}`" for line in said[i1:i2])
            files, one = _givers(name for name, _text in parts)
            why = f"reads {run}, which {files} {'does' if one else 'do'} not give"
        elif tag == "insert":
            run = _run(f"`{line}`" for line in given[j1:j2])
            files, one = _givers(owner[j1:j2])
            why = f"lacks {run}, which {files} {'gives' if one else 'give'}"
        else:
            continue
        causes.append((None, i1 + 1, why))
    return causes


def _check(below, body, parts):
    """Refused, at each line where it differs, counted from BODY's first
    line, where the part of BODY above `HEADING` is not the lines of PARTS,
    the files `first_part` gives, or the part below it is not BELOW's
    lines."""
    if body is None:
        raise Refused(
            [(None, 0, "is not there; `seal pr-body <item> --body <file>` writes it")]
        )
    head, generated = split(body)
    said = READER.gfm_lines(generated)
    given = [line for line, _source in below]
    # The lines above the part: the first part's, and `HEADING`'s own.
    offset = len(READER.gfm_lines(head, keepends=True)) + 1
    causes = _first_part(head, parts)
    matcher = difflib.SequenceMatcher(None, said, given, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "replace":
            why = f"reads `{said[i1]}`; the records give {_source(below[j1])}"
        elif tag == "delete":
            run = _run(f"`{line}`" for line in said[i1:i2])
            why = f"reads {run}, which the records do not give"
        elif tag == "insert":
            why = f"lacks {_run(_source(pair) for pair in below[j1:j2])}"
        else:
            continue
        causes.append((None, offset + i1 + 1, why))
    if causes:
        raise Refused(causes)


def compared(item, body, root, manifest=None, base=None):
    """`(note, causes)` for BODY, a pull request body's text or None where
    there is none, against what `seal pr-body` composes for the work item's
    directory ITEM in the repository at ROOT: the first part `first_part`
    gives from the two language keys, `HEADING`, the seal mark `seal_mark`
    gives from MANIFEST or the plugin's own, read against BASE where it is
    given, and the records' copy. NOTE is `seal_mark`'s sentence, or None;
    CAUSES are the `(where, line, why)` of `Refused`, a record's, the root's
    `config.json`'s or the body's, empty where BODY is that composition.
    `main --check` and the pull request's check, `chain_check.py#body`, both
    call this, so the body is read by one code path at the sealer and at
    the pull request (#1452)."""
    mark, note = seal_mark(item, root, manifest, base)
    name = os.path.basename(os.path.normpath(os.path.abspath(item)))
    try:
        below = _composed(name, read_item(item), mark, _in_tree(root))
        _check(below, body, first_part(item, root))
    except Refused as refused:
        return note, refused.causes
    return note, []


def _place(where, line, item, body, home):
    """Where a cause stands, with no machine path in it: the body file BODY
    by its name, and a record by its path under HOME, the root's name as
    `_in_tree` gives it, whatever path the work item ITEM was given by,
    `ROOT_CONFIG` as the root's `config.json`. The sealer copies the first
    `refused:` line into a `guarantee.md` that is committed."""
    if where is None:
        path = os.path.basename(body)
    else:
        name = os.path.basename(os.path.normpath(os.path.abspath(item)))
        path = posixpath.normpath(
            "/".join(p for p in (home, OPTIN.WORK_ITEMS, name, where) if p)
        )
    return f"{path}:{line}" if line else path


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="seal pr-body",
        description="Write a pull request body: the work item's `pr.<lang>.md` "
        f"where the two language keys differ, its `{OWN_PART}`, the line "
        f"`{HEADING}`, and the part its other records hold; or check it.",
    )
    parser.add_argument("item", help="the work item's directory")
    parser.add_argument("--body", required=True, metavar="FILE", help="the body file")
    parser.add_argument(
        "--check",
        action="store_true",
        help="write nothing; exit 1 where the part above the heading is not "
        "the files the language keys ask for or the part below it not the "
        "records'",
    )
    args = parser.parse_args(argv)
    if not os.path.isdir(args.item):
        print(f"seal pr-body: {args.item} is not a directory", file=sys.stderr)
        return 2
    name = os.path.basename(os.path.normpath(os.path.abspath(args.item)))
    # The mark is read in the work item's own checkout, so a run from
    # another checkout of the repository writes the body a run from the
    # item's would. A local-mode item sits under the common git directory,
    # where git finds no checkout and `repo_root` answers "", so its
    # checkout is the working directory's.
    root = OPTIN.repo_root(os.path.abspath(args.item)) or OPTIN.repo_root(os.getcwd())
    home = _in_tree(root)
    if args.check:
        try:
            note, causes = compared(args.item, _body(args.body), root)
            # The files the part above the heading was compared with, named
            # on the line that says it matches.
            parts = [] if causes else first_part(args.item, root)
        except Refused as refused:
            note, causes = None, refused.causes
        for where, line, why in causes:
            print(f"refused: {_place(where, line, args.item, args.body, home)}: {why}")
        if causes:
            return 1
        said = f"seal pr-body: {note}\n" if note else ""
        print(
            f"{said}matches: {args.body} is {_names(parts)} above `{HEADING}` "
            "and the records' text below it"
        )
        return 0
    mark, note = seal_mark(args.item, root)
    said = f"seal pr-body: {note}\n" if note else ""
    try:
        below = _composed(name, read_item(args.item), mark, home)
        parts = first_part(args.item, root)
        try:
            with open(args.body, "w", encoding="utf-8", newline="") as handle:
                handle.write(
                    "".join(text for _name, text in parts)
                    + HEADING
                    + "\n"
                    + _joined(below)
                )
        except OSError as exc:
            raise Refused([(None, 0, f"cannot be written ({exc})")]) from None
    except Refused as refused:
        for where, line, why in refused.causes:
            print(f"refused: {_place(where, line, args.item, args.body, home)}: {why}")
        return 1
    print(f"{said}wrote: {args.body} from {args.item}'s {_names(parts)} and records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
