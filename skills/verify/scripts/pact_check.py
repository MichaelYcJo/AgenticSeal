#!/usr/bin/env python3
"""Does every signer still agree with the pact? Run at the pact's repository.

Issue #647. A work item that commits in more than one repository, where those
repositories keep a contract together, keeps the one copy of that contract in
`seal/pact.md` in one of them -- the pact's repository -- and every repository
of the work item is a signer (`docs/the-pact.md`). A signer cites each
clause it was built against as a pact anchor, one row of the anchor table
in a work item's `frame/design.md`:

  | Pact | Clause | Hash |
  |---|---|---|
  | <origin URL of the pact's repository> | ## Clause / ### Narrower | <hash> |

This command reads every signer from the pact's repository and grades each
row naming this pact against the clause as the pact holds it now.

  seal pact             in the pact's repository
  seal pact ROOT        the pact's repository at ROOT

**Local only.** No CI runs it: a signer's pull request can read one
repository, and this needs all of them (#647's decision 2). A signer's CI
reads nothing of the pact.

## What each frame is read for

The anchor table is read by `hooks/lib/config.py#gfm_table`, and the cells
are written bare. A row is graded where its `Pact` cell, compared
normalised, is the origin URL of this repository; a row naming another pact
the signer's `Pact` row declares is passed over, for that pact's
`seal pact` to grade. Refused at the row's line: a `Pact` cell that is not
one remote URL, or that names a pact the signer's `Pact` row does not
declare, which no `seal pact` grades, because another pact's reports the
signer `ONE-SIDED` and reads none of its frames; and, in a row naming this
pact, a `Clause` cell that opens with no heading or a `Hash` cell that is
not eight lowercase hex digits. Refused at the frame: every refusal of the
walk, and a second anchor table. Another table below the anchor table,
such as a section's policy table, ends it and is no refusal, whatever
stands above its header; the walk steps over it and still refuses a row
written after it, before the next heading (`gfm_table`'s BESIDE).

Where the walk refused nothing, every other line that `config.unfenced`
shows and that reads as a row, its outer pipes given where it leaves them
out, is read once more (`stray_rows`). It is refused at its line where one
cell names a pact the signer declares and another opens with a heading:
the walk reads the `| Pact | Clause | Hash |` header alone, so such a row
is graded by nothing, whatever header it stands under, or with none. A row
that misses twice is passed over: one whose `Pact` cell is also a near
miss, in backticks or one letter off a declared remote, or that holds no
cell opening with a heading, has no anchor's shape a fact can tell. A
line four columns in, a tab counting to the next multiple of four, is read
as no row: below a blank line it is an indented code block, and right
under a paragraph line, where GitHub renders it as text, it is a row with
no header that is also indented, a row that misses twice.

Every `pact:` token outside a closed fence, in any case, is refused at its
line, with the row to write in its place: it is the inline anchor this
command read through 0.23.x. A token with a space beside its colon is not
read: prose writes the word before a colon and a space, and no release read
that spelling as an anchor.

## Where the signers are

The pact's `| Signer |` table lists them by origin remote URL, and a
checkout is found for each, in this order and with nothing guessed:

  1. `~/.claude/agentic/pact-paths.md`, a `| Remote | Path |` table kept per
     machine and never committed, keyed by remote URL compared normalised;
  2. every sibling directory of the pact's repository whose origin remote
     normalises to the signer's -- exactly one of them.

A signer neither finds is reported with the map line to add.

The map is read by `hooks/lib/config.py#gfm_table`, as every other table
here is, and a line it does not read is refused at exit 2, printed as
`REFUSED ~/.claude/agentic/pact-paths.md — the map <sentence>`: a map that
is there and will not read, one holding no `| Remote | Path |` table, every
refusal of the walk, a row with an empty cell, a remote on two rows, of
which neither is read, and a second header. A row nobody reads would report
its signer as not found. The rows the walk did read are used.

## What each anchor reads

  OK          the hash matches the clause in the pact's current checkout
  SUPERSEDED  it does not, and a commit in HEAD's own history of the pact
              gave the clause this hash: the signer was built against a
              superseded clause. Re-read it there and re-anchor
  NOT TAKEN   it does not, and a commit reachable from another ref but not
              from HEAD gave it this hash, named: the pact has not taken the
              signer's recorded change. Land that ref's change, or
              reconcile
  UNMATCHED   no commit here gave the clause this hash: squashed away, or
              never a version. Read both sides
  BROKEN      the heading path resolves to no clause, or to more than one:
              renamed or removed. Re-coordinate the signer

Git is asked one thing: which way a mismatch points. It never decides `OK`.
A pact under local mode has no history, so every mismatch there reads
`UNMATCHED`, and the summary says so.

## Exit codes

  0  every listed signer was read, and every anchor is `OK`
  1  a `SUPERSEDED`, `NOT TAKEN` or `UNMATCHED` anchor, or a signer not
     found on this machine
  2  unusable input: no pact here, a pact or file that cannot be read, a
     line of the machine-local map it does not read, a `BROKEN` anchor,
     an anchor row it cannot grade or does not read, a row naming a pact
     the signer does not declare, a row no anchor table holds, a `pact:`
     token, a `Pact` row that will not parse, a relationship recorded on
     one side only, or a pact's repository with no origin remote

`BROKEN` is exit 2 and a mismatch is exit 1. Nothing is ever written.

## A header written through 0.18.x

A pact whose table is headed with the word 0.18.x used is read exactly as
one headed `Signer`, and one line before
that file's other lines names the file, both headers and the release that
renamed them (`hooks/lib/config.py#renamed_header`). The line is in no exit
class: the exit is what it would be under the new header (#822).
"""

import argparse
import glob
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HOOKS = os.path.join(HERE, "..", "..", "..", "hooks", "lib")
CHECKER = os.path.join(HERE, "coordinates.py")
PACT_FILE = "pact.md"
CONFIG_FILE = "config.md"
MAP_PARTS = (".claude", "agentic", "pact-paths.md")
# Read through the native path; named in every sentence by the one spelling
# the documents use on every platform, so a Windows run does not print
# `~/.claude\agentic\pact-paths.md`.
MAP = os.path.join(*MAP_PARTS)
MAP_SHOWN = "~/" + "/".join(MAP_PARTS)


def shown(path, repo=None, home_dir=None, flavour=os.path):
    """PATH as every line of `seal pact` prints it, on every platform:
    relative to REPO where it lies inside that repository, `~/`-relative
    where it lies under HOME_DIR, and otherwise whole, with `/` for every
    separator.

    **Every path this command prints goes through here** (#647, the separator
    note). The `UNREADABLE` sentence used to join a native absolute path with
    `/`, so a Windows run printed `C:\\Users\\x\\orders-web\\seal/config.md`,
    and every other path line printed whatever separators the platform gave
    it. One function, so the class is closed by construction rather than one
    sentence at a time.

    The comparison is by whole segment and literal: nothing is case-folded,
    resolved or normalised, so a path reached by another spelling of the
    repository prints long and still names the file that was read.

    FLAVOUR is the path module whose separators and drive rule apply;
    `ntpath` is what a case passes, so the Windows spelling is exercised on
    every platform rather than resting on a POSIX guarantee
    (contract rule 13).
    """
    seps = "".join(s for s in (flavour.sep, flavour.altsep) if s)

    def parts(text):
        drive, rest = flavour.splitdrive(text)
        segments = [s for s in re.split(f"[{re.escape(seps)}]", rest) if s]
        return drive, rest[:1] in seps, segments

    drive, rooted, segments = parts(path)
    for base, lead in ((repo, ""), (home_dir, "~/")):
        if not base:
            continue
        base_drive, base_rooted, base_segments = parts(base)
        n = len(base_segments)
        if (
            (base_drive, base_rooted) == (drive, rooted)
            and len(segments) > n
            and segments[:n] == base_segments
        ):
            return lead + "/".join(segments[n:])
    rest = flavour.splitdrive(path)[1]
    for sep in seps:
        rest = rest.replace(sep, "/")
    return drive + rest


# The machine-local map's header, as the cells `gfm_table` matches a header by.
MAP_TABLE = ("Remote", "Path")

OK, SUPERSEDED, NOT_TAKEN, UNMATCHED, BROKEN = (
    "OK",
    "SUPERSEDED",
    "NOT TAKEN",
    "UNMATCHED",
    "BROKEN",
)
NOT_FOUND, ONE_SIDED, REFUSED, UNREADABLE = (
    "NOT FOUND",
    "ONE-SIDED",
    "REFUSED",
    "UNREADABLE",
)
# The anchor table's header, as the cells `gfm_table` matches a header by.
ANCHOR_TABLE = ("Pact", "Clause", "Hash")
# The inline anchor read through 0.23.x, refused wherever it stands outside
# a closed fence: `pact:` in any case, so `PACT:` and `Pact:` too, with no
# letter, digit, `_`, `.`, `@`, `/` or `-` before it, so `compact:` is no
# token, and a character that is not a space after it. A space beside the
# colon, `pact: x` or `pact :x`, is not read: prose writes the word before a
# colon and a space, and no release read that spelling as an anchor. One
# pattern, and it names no typo.
INLINE_TOKEN = re.compile(r"(?<![A-Za-z0-9_.@/-])pact:(?=\S)", re.IGNORECASE)
# The sentences a row or a token is refused in, each reading after its line.
NOT_ONE_URL = (
    "the `Pact` cell is not one remote URL: it holds a space, a backtick or no "
    "host and path — write the origin URL of the pact's repository, bare, as "
    "the signer's `Pact` row writes it"
)
NO_HEADING = (
    "the `Clause` cell opens with no heading — write the clause's heading "
    "path, bare, such as `## Clause / ### Narrower`"
)
NOT_A_HASH = (
    "the `Hash` cell is not eight lowercase hex digits — write `00000000` "
    "until the first report names the real one"
)
# `{cell}` is the `Pact` cell as written, bare: `one_remote` refuses one
# holding a backtick before this sentence is reached.
UNDECLARED = (
    "the `Pact` cell names `{cell}`, a pact this signer's `seal/config.md` "
    "does not declare in its `Pact` row, so no `seal pact` grades the row — "
    "write the origin URL of a pact that row declares, or add `{cell}` to "
    "that row"
)
OUTSIDE_TABLE = (
    "the row names a pact this signer declares and a clause, and no anchor "
    "table holds it, so nothing grades it — write it as a row of a table "
    "headed exactly `| Pact | Clause | Hash |`"
)
INLINE = (
    "a `pact:` token is the inline pact anchor `seal pact` read through "
    "0.23.x, and nothing reads it now — write it as a row of a "
    "`| Pact | Clause | Hash |` table, `| <the origin URL of the pact's "
    "repository> | ## Clause / ### Narrower | <hash> |`; or, where the text "
    "shows the retired shape rather than citing a clause, put it in a fenced "
    "code block, which nothing reads"
)
# Which exit each finding is.
EXIT_ONE = frozenset({SUPERSEDED, NOT_TAKEN, UNMATCHED, NOT_FOUND})
EXIT_TWO = frozenset({BROKEN, ONE_SIDED, REFUSED, UNREADABLE})


def load(path, name):
    """A sibling module by path, or a sentence and exit 2."""
    if not os.path.isfile(path):
        sys.stderr.write(
            f"seal pact: cannot read {shown(path, home_dir=os.path.expanduser('~'))}, "
            "which this command reads the pact "
            "through. It ships in the plugin beside this script; a copy of one "
            "script taken on its own is not a plugin. Nothing was read.\n"
        )
        raise SystemExit(2)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root, *args):
    """Git's stdout in ROOT, or None where git refused."""
    try:
        done = subprocess.run(
            ["git", "-C", root, *args],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return done.stdout if done.returncode == 0 else None


def read(path):
    """The file's text, or None for one that will not read."""
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except (OSError, ValueError):
        return None


def origin(root):
    """ROOT's origin remote URL as written, or ""."""
    return (git(root, "remote", "get-url", "origin") or "").strip()


def first_table(config, text, header, beside=False):
    """(rows, refusals) for the first table of TEXT headed HEADER, read by
    `hooks/lib/config.py#gfm_table`: its rows and its refusals, and, where
    the walk refused nothing, one refusal per further HEADER outside a
    fence, at its line, because the walk reads the first table only. A
    refusal of the walk already says every row below it goes unread, a
    second header among them. BESIDE is `gfm_table`'s: true where TEXT may
    hold other tables after this one, as a frame's section does."""
    rows, walked = config.gfm_table(text, header, beside=beside)
    if walked:
        return rows, list(walked)
    # exempt from splitlines: lines the GFM walk numbers
    lines = text.splitlines()
    headers = [
        index + 1
        for index, line in config.unfenced(lines, text)
        if config.table_cells(line) == header
    ]
    named = f"`| {' | '.join(header)} |`"
    return rows, [
        f"holds a second {named} header at line {at}, and the walk reads the "
        "first table only — move its rows into the first table and delete the "
        "second header"
        for at in headers[1:]
    ]


def path_map(config, home_dir):
    """({normalised remote: path}, refusals) from the machine-local map
    under HOME_DIR, each refusal a sentence that reads after the words `the
    map`.

    No map is an empty one. Every other line the map's reader does not read
    is a refusal, because a row nobody reads reports its signer as not
    found: a map that is there and will not read, one holding no
    `| Remote | Path |` table, every refusal of the walk
    (`hooks/lib/config.py#gfm_table`), a row with an empty cell, a remote on
    two rows, compared normalised, of which neither is read, and a second
    header, because the walk reads the first table only. The rows the walk
    did read are used, as `pact_signers`' are."""
    where = os.path.join(home_dir, MAP)
    if not os.path.lexists(where):
        return {}, []
    text = read(where)
    if text is None:
        return {}, ["is there and could not be read"]
    rows, refusals = first_table(config, text, MAP_TABLE)
    places = {}
    for line, cells in rows:
        remote, path = cells
        if not remote or not path:
            refusals.append(
                f"has a row at line {line} with an empty cell — write the remote "
                "and the path of its checkout, or delete the row"
            )
            continue
        places.setdefault(config.normalise_remote(remote), []).append((line, path))
    found = {}
    for remote, held in places.items():
        if len(held) == 1:
            found[remote] = os.path.expanduser(held[0][1])
            continue
        lines = [str(line) for line, _path in held]
        refusals.append(
            f"has rows at lines {', '.join(lines[:-1])} and {lines[-1]} naming one "
            f"repository, `{remote}`, so "
            f"{'neither' if len(held) == 2 else 'none of them'} is read — keep one"
        )
    return found, refusals


def checkout(config, signer, root, mapped, home_dir=None):
    """(path, None) for the signer's checkout, or (None, why not), every
    path in the reason as `shown` prints it."""
    written, normalised = signer
    if normalised in mapped:
        path = mapped[normalised]
        if not os.path.isdir(path):
            return None, (
                f"the map names {shown(path, home_dir=home_dir)}, which is not a "
                "directory here"
            )
        theirs = config.normalise_remote(origin(path))
        if theirs != normalised:
            return None, (
                f"the map names {shown(path, home_dir=home_dir)}, whose origin is "
                f"{theirs or 'not set'} rather than {normalised}"
            )
        return path, None
    parent = os.path.dirname(os.path.abspath(root))
    try:
        names = sorted(os.listdir(parent))
    except OSError:
        names = []
    hits = []
    for entry in names:
        path = os.path.join(parent, entry)
        if os.path.realpath(path) == os.path.realpath(root) or not os.path.isdir(path):
            continue
        if not os.path.lexists(os.path.join(path, ".git")):
            continue
        if config.normalise_remote(origin(path)) == normalised:
            hits.append(path)
    if len(hits) == 1:
        return hits[0], None
    line = f"`| {written} | <the path of its checkout> |`"
    if hits:
        return None, (
            f"{len(hits)} sibling directories have its origin "
            f"({', '.join(shown(h, home_dir=home_dir) for h in hits)}), "
            f"and nothing here guesses which: add {line} to {MAP_SHOWN}"
        )
    return (
        None,
        f"no checkout of it was found on this machine: add {line} to {MAP_SHOWN}",
    )


def anchor_files(home):
    """Every file of a signer's root its pact anchors are read from: every
    thread's `frame/design.md`.
    """
    return sorted(glob.glob(os.path.join(home, "threads", "*", "frame", "design.md")))


class History:
    """The pact file's versions, asked for lazily and once: HEAD's own
    history of it, newest first, and the commits that touched it on any
    other branch, remote-tracking branch or tag that HEAD does not hold.

    A pact under local mode sits under the git directory, a path git never
    tracked, so both lists come back empty with nothing special-cased: that is
    what makes every mismatch there `UNMATCHED`. `grade` reads HEAD's list
    before the other, so leaving HEAD's commits out of the second changes no
    verdict; it says what the list is and saves reading them twice."""

    def __init__(self, root, rel):
        self.root, self.rel = root, rel
        self._head = self._other = None
        self._texts = {}

    def commits(self, *revs):
        # `--full-history`: by default git follows only the TREESAME parent
        # of a merge, so a clause version on the side a merge did not keep
        # vanished from HEAD's list (and `--not HEAD` kept it out of the
        # other one), and its hash read UNMATCHED where SUPERSEDED is true.
        # A merge listed this way carries one parent's text, so it changes
        # no verdict.
        out = git(self.root, "rev-list", "--full-history", *revs, "--", self.rel)
        return out.split() if out else []

    def head(self):
        if self._head is None:
            self._head = self.commits("HEAD")
        return self._head

    def other(self):
        if self._other is None:
            self._other = self.commits(
                "--branches", "--remotes", "--tags", "--not", "HEAD"
            )
        return self._other

    def text(self, sha):
        if sha not in self._texts:
            self._texts[sha] = git(self.root, "show", f"{sha}:{self.rel}")
        return self._texts[sha]

    def ref_holding(self, sha):
        out = git(
            self.root,
            "for-each-ref",
            "--contains",
            sha,
            "--format=%(refname:short)",
            "refs/heads",
            "refs/remotes",
            "refs/tags",
        )
        refs = sorted(r for r in (out or "").split() if r)
        return refs[0] if refs else sha[:8]


def heading_parts(checker, clause):
    """The headings of CLAUSE, a heading path as an anchor row's `Clause`
    cell holds it, or None where it opens with no heading."""
    parts = [p for p in clause.split(checker.HEADING_SEP) if p.strip()]
    if not parts or checker.heading_level(parts[0].strip()) is None:
        return None
    return parts


def one_remote(config, cell):
    """CELL normalised, where an anchor row's `Pact` cell is one remote URL
    written bare; None where it holds a backtick, a space or no host and
    path, and so names no pact anybody can tell."""
    if "`" in cell:
        return None
    parsed, _refusals = config.remote_entries([cell], "")
    return parsed[0][1] if parsed else None


def row_cells(config, line):
    """The cells of LINE read as a table row by `config.table_cells`, with
    an outer pipe given where LINE leaves one out, so a row of a table
    written without them reads too; None where LINE holds no pipe, does
    not read as a row even so, or stands four columns in, a tab counting to
    the next multiple of four (`blocks.columns`, as `gfm_table` counts a
    heading's). Below a blank line such a line is an indented code block;
    right under a paragraph line it is paragraph text, which the module
    docstring states as a limit."""
    if "|" not in line:
        return None
    # Any tab in the leading run reaches four columns, so past this guard
    # the run is at most three spaces, which `table_cells` reads past.
    if config.blocks.columns(line) >= 4:
        return None
    cells = config.table_cells(line)
    if cells is not None:
        return cells
    content = line.lstrip(" ").rstrip()
    if not content.startswith("|"):
        content = "| " + content
    if not content.endswith("|") or content.endswith("\\|"):
        content += " |"
    return config.table_cells(content)


def stray_rows(config, checker, text, declared, walked):
    """The line numbers of the rows of TEXT no anchor table holds: each
    line `config.unfenced` shows, other than the anchor table's rows at the
    line numbers WALKED, that reads as a row (`row_cells`) holding one cell
    that is one remote URL among DECLARED, compared normalised, and another
    cell that opens with a heading (`heading_parts`). It reads the row and
    not the header above it, so every near miss of the header is one shape,
    and a row with no header is another of it."""
    # exempt from splitlines: lines `config.unfenced` numbers, as first_table's
    lines = text.splitlines()
    found = []
    for index, line in config.unfenced(lines, text):
        if index + 1 in walked:
            continue
        cells = row_cells(config, line) or ()
        remotes = [
            i for i, cell in enumerate(cells) if one_remote(config, cell) in declared
        ]
        headings = [
            i
            for i, cell in enumerate(cells)
            if heading_parts(checker, cell) is not None
        ]
        if any(r != h for r in remotes for h in headings):
            found.append(index + 1)
    return found


def clause_hash(checker, text, clause):
    """(hash, None) for the clause the heading path CLAUSE names in a
    pact's TEXT, or (None, why it names none)."""
    parts = heading_parts(checker, clause)
    if parts is None:
        return None, "names no heading path, and a pact clause is addressed by one"
    lines = checker.gfm_lines(text)
    # The clause's region as the checker reads a document's (#867): headings
    # on the lines a renderer shows, the hash over the lines as written.
    regions = checker.heading_path(checker.markdown_lines(text), parts)
    if len(regions) != 1:
        return None, (
            "resolves to no clause in the pact"
            if not regions
            else f"resolves to {len(regions)} clauses in the pact"
        )
    start, end = regions[0]
    return checker.content_hash(lines[start - 1 : end]), None


def grade(checker, pact_text, history, clause, want):
    """(status, what to do) for one anchor: the clause path CLAUSE and the
    hash WANT the signer recorded."""
    current, why = clause_hash(checker, pact_text, clause)
    if current is None:
        return BROKEN, (
            f"the heading path {why}: the clause was renamed or removed. "
            "Re-coordinate the signer"
        )
    if current == want:
        return OK, ""
    for sha in history.head():
        text = history.text(sha)
        if text is not None and clause_hash(checker, text, clause)[0] == want:
            return SUPERSEDED, (
                f"the signer was built against a superseded clause, the one "
                f"at {sha[:8]}; its hash is {current} now. Re-read it in the "
                "signer and re-anchor"
            )
    for sha in history.other():
        text = history.text(sha)
        if text is not None and clause_hash(checker, text, clause)[0] == want:
            return NOT_TAKEN, (
                f"the pact has not taken the signer's recorded change: this "
                f"hash is the clause on {history.ref_holding(sha)} (at "
                f"{sha[:8]}), which HEAD does not hold. Land that ref's pact "
                "change, or reconcile"
            )
    return UNMATCHED, (
        f"no commit in this repository gave the clause this hash, and its hash "
        f"is {current} now: the version was squashed away or never existed. "
        "Read both sides"
    )


def check(root, out=sys.stdout, home_dir=None):
    """Read the pact at ROOT and every signer; print; return the exit."""
    config = load(os.path.join(HOOKS, "config.py"), "agentic_config_for_pact")
    optin = load(os.path.join(HOOKS, "optin.py"), "agentic_optin_for_pact")
    checker = load(CHECKER, "agentic_evidence_for_pact")
    home_dir = home_dir or os.path.expanduser("~")

    def say(line):
        out.write(line + "\n")

    repo = optin.repo_root(os.path.abspath(root))
    if not repo:
        say(
            f"seal pact: {shown(root, home_dir=home_dir)} is not in a git "
            "repository — nothing was read"
        )
        return 2
    home = optin.home_at(repo)
    pact_path = os.path.join(home, PACT_FILE) if home else ""
    if not home or not os.path.lexists(pact_path):
        say(
            f"seal pact: {shown(repo, home_dir=home_dir)} holds no "
            f"seal/{PACT_FILE}, so there is no pact "
            "to reconcile here — run it in the repository that holds the pact"
        )
        return 2
    pact_text = read(pact_path)
    if pact_text is None:
        say(
            f"{UNREADABLE} {shown(pact_path, repo, home_dir)} — the pact could "
            "not be read"
        )
        return 2
    mine = origin(repo)
    if not mine:
        say(
            f"seal pact: {shown(repo, home_dir=home_dir)} has no origin remote, "
            "so no pact anchor can be matched to the pact — set `origin` and "
            "run it again"
        )
        return 2
    ours = config.normalise_remote(mine)
    shared = optin.home_paths(repo)[0]
    local = os.path.realpath(home) != os.path.realpath(shared)
    rel = os.path.relpath(pact_path, repo).replace(os.sep, "/")
    history = History(repo, rel)
    # A `Hash` cell is the clause's content hash, as long as the checker
    # writes one.
    hash_shape = re.compile(f"[0-9a-f]{{{checker.HASH_LEN}}}")

    findings = []

    def found(status, signer, where, detail):
        findings.append(status)
        say(
            f"{status} {signer} {where} — {detail}"
            if where
            else f"{status} {signer} — {detail}"
        )

    signers, refusals, header = config.pact_signers(pact_text)
    renamed(config, f"seal/{PACT_FILE}", header, config.SIGNER_HEADER, say)
    for refusal in refusals:
        found(REFUSED, f"seal/{PACT_FILE}", "", f"the pact {refusal}")
    # The table's own word in the lines below, so a refusal about a pact
    # headed the old way names the header the pact holds.
    table = f"`{(header or config.SIGNER_HEADER)[0]}` table"
    mapped, map_refusals = path_map(config, home_dir)
    for refusal in map_refusals:
        found(REFUSED, MAP_SHOWN, "", f"the map {refusal}")

    counts = dict.fromkeys((OK, SUPERSEDED, NOT_TAKEN, UNMATCHED, BROKEN), 0)
    read_count = 0
    for signer in signers:
        written = signer[0]
        if signer[1] == ours:
            # The owner's definition makes the pact's repository a signer
            # too, so listing it is a plausible slip; the sibling search
            # skips this repository and would call it not found here (round
            # 1 of #647, white 9).
            found(
                REFUSED,
                written,
                f"seal/{PACT_FILE}",
                f"the pact lists its own repository; the {table} lists every "
                "OTHER signer, so take this row out",
            )
            continue
        path, why = checkout(config, signer, repo, mapped, home_dir)
        if path is None:
            found(NOT_FOUND, written, "", why)
            continue
        their_repo = optin.repo_root(path) or path
        their_home = optin.home_at(their_repo)
        if not their_home:
            found(
                ONE_SIDED,
                written,
                shown(path, home_dir=home_dir),
                "the pact lists it, and it has no seal/ root to name this pact "
                "in: the relationship is recorded on one side only",
            )
            continue
        declared = config.declared_pacts(their_home)
        if declared is None:
            found(
                UNREADABLE,
                written,
                shown(config.config_path(their_home), their_repo, home_dir),
                "could not be read",
            )
            continue
        pacts, row_refusals = declared
        for refusal in row_refusals:
            found(REFUSED, written, f"seal/{CONFIG_FILE}", refusal)
        if not any(n == ours for _w, n in pacts):
            found(
                ONE_SIDED,
                written,
                f"seal/{CONFIG_FILE}",
                f"the pact lists it, and its config names no `{config.PACT_ROW}` "
                f"row for {mine}: the relationship is recorded on one side "
                f"only. Add `| {config.PACT_ROW} | {mine} |` there, or take it "
                f"out of the pact's {table}",
            )
            continue
        # Every pact the signer declares, this one among them: a row naming
        # one of the others is that pact's to grade, and a row naming none
        # of them is graded by no `seal pact`, since another pact's reports
        # this signer `ONE-SIDED` above and reads none of its frames.
        declared_remotes = frozenset(n for _w, n in pacts)
        read_count += 1
        anchors = 0
        for file_path in anchor_files(their_home):
            body = read(file_path)
            where = shown(file_path, path, home_dir)
            if body is None:
                found(UNREADABLE, written, where, "could not be read")
                continue
            rows, table_refusals = first_table(config, body, ANCHOR_TABLE, beside=True)
            if table_refusals and table_refusals[0].startswith("holds no "):
                # A frame that cites no pact holds no anchor table.
                table_refusals = []
            for refusal in table_refusals:
                found(REFUSED, written, where, f"the frame {refusal}")
            for line, (pact_cell, clause, want) in rows:
                at = f"{where}:{line}"
                named = one_remote(config, pact_cell)
                if named is None:
                    found(REFUSED, written, at, NOT_ONE_URL)
                    continue
                if named != ours:
                    if named not in declared_remotes:
                        found(REFUSED, written, at, UNDECLARED.format(cell=pact_cell))
                    continue
                if heading_parts(checker, clause) is None:
                    found(REFUSED, written, at, NO_HEADING)
                    continue
                if not hash_shape.fullmatch(want):
                    found(REFUSED, written, at, NOT_A_HASH)
                    continue
                anchors += 1
                status, detail = grade(checker, pact_text, history, clause, want)
                counts[status] += 1
                if status != OK:
                    found(status, written, f"{at} `{clause}`", detail)
            if not table_refusals:
                # Where the walk refused, its sentence already says the rows
                # below go unread, so a row it names is not refused twice;
                # once that refusal is answered, the next run reads the rest.
                walked = {line for line, _cells in rows}
                for line in stray_rows(config, checker, body, declared_remotes, walked):
                    found(REFUSED, written, f"{where}:{line}", OUTSIDE_TABLE)
            view = checker.unquoted(body)
            for token in INLINE_TOKEN.finditer(view):
                line = view.count("\n", 0, token.start()) + 1
                found(REFUSED, written, f"{where}:{line}", INLINE)
        say(
            f"READ {written} {shown(path, home_dir=home_dir)} — {anchors} pact "
            f"anchor{'' if anchors == 1 else 's'} naming this pact"
        )

    summary = (
        f"seal pact: the pact at {mine} — {read_count} of {len(signers)} "
        f"signer{'' if len(signers) == 1 else 's'} read · "
        + " · ".join(f"{counts[s]} {s.lower()}" for s in counts)
    )
    if local:
        summary += (
            ". The pact sits under the git directory (local mode), so it has no "
            "history and every mismatch reads unmatched"
        )
    say(summary)
    if any(status in EXIT_TWO for status in findings):
        return 2
    if any(status in EXIT_ONE for status in findings):
        return 1
    return 0


def renamed(config, where, header, current, say):
    """Print the line naming the rename where HEADER, the header a file at
    WHERE was read under, is the one CURRENT was written as through 0.18.x.
    In no exit class: the file reads exactly as under CURRENT (#822)."""
    old, sentence = config.renamed_header(current)
    if header is not None and header == old:
        say(f"seal pact: {where} {sentence}")


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="seal pact",
        description="At the pact's repository: does every signer still "
        "agree with the pact?",
    )
    ap.add_argument(
        "root",
        nargs="?",
        default=".",
        help="the pact's repository (default: the current directory)",
    )
    args = ap.parse_args(argv)
    return check(args.root)


if __name__ == "__main__":
    for _name, _errors in (("stdout", "replace"), ("stderr", "backslashreplace")):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
