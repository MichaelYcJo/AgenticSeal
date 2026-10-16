#!/usr/bin/env python3
"""Does every signer still agree with the pact? Run at the pact's repository.

Issue #647. A work item that commits in more than one repository, where those
repositories keep a contract together, keeps the one copy of that contract in
`seal/pact.md` in one of them -- the pact's repository -- and every repository
of the work item is a signer (`docs/the-pact.md`). A signer cites the
clauses it was built against as pact anchors,

  pact:<name>/"<heading path>"@<hash>

in its specs' Grounding. This command reads every signer from the pact's
repository and grades each of those anchors against the clause as the pact
holds it now.

  pact-check            in the pact's repository
  pact-check ROOT       the pact's repository at ROOT

**Local only.** No CI runs it: a signer's pull request can read one
repository, and this needs all of them (#647's decision 2). What a signer's
CI does instead is print the relationship, `chain_check.py#pact_notices`.

## Where the signers are

The pact's `| Signer |` table lists them by origin remote URL, and a
checkout is found for each, in this order and with nothing guessed:

  1. `~/.claude/specseal/pact-paths.md`, a `| Remote | Path |` table kept per
     machine and never committed, keyed by remote URL compared normalised;
  2. every sibling directory of the pact's repository whose origin remote
     normalises to the signer's -- exactly one of them.

A signer neither finds is reported with the map line to add.

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
     `BROKEN` anchor, an anchor naming this pact that does not parse, a
     `Pact` row that will not parse, a relationship
     recorded on one side only, or a pact's repository with no origin
     remote

`BROKEN` is exit 2 and a mismatch is exit 1. Nothing is ever written.

## A header written through 0.18.x

A pact whose table is headed with the word 0.18.x used is read exactly as
one headed `Signer`, and one line before
that file's other lines names the file, both headers and the release that
renamed them (`hooks/config.py#renamed_header`). The line is in no exit
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
HOOKS = os.path.join(HERE, "..", "..", "..", "hooks")
CHECKER = os.path.join(HERE, "coordinates.py")
PACT_FILE = "pact.md"
CONFIG_FILE = "config.md"
MAP_PARTS = (".claude", "specseal", "pact-paths.md")
# Read through the native path; named in every sentence by the one spelling
# the documents use on every platform, so a Windows run does not print
# `~/.claude\specseal\pact-paths.md`.
MAP = os.path.join(*MAP_PARTS)
MAP_SHOWN = "~/" + "/".join(MAP_PARTS)


def shown(path, repo=None, home_dir=None, flavour=os.path):
    """PATH as every line of `pact-check` prints it, on every platform:
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
    (`agent-contract` §13).
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


MAP_HEADER = re.compile(r"^\|\s*Remote\s*\|\s*Path\s*\|\s*$")

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
# A token that begins a pact anchor and does not complete one, so a mistyped
# citation -- `#` for `/`, no quotes, no hash -- is named rather than passed
# over. It is otherwise read by nobody: not here, not by the signer's own
# check, which passes pact anchors over by design, and not by chain-check
# (round 1 of #647, yellow 4).
#
# **The grammar, in one rule** (round 2, yellow 13; round 3 of #735, yellow
# 19), stated for a reader in `docs/the-pact.md` §*The pact anchor*: a token
# begins an anchor where `pact:<name>` is followed at once by `/` or `#`, or
# where the rest of an anchor follows with its `/` missing -- a quoted heading
# path closed by `@`, or `@` and a hash, at once or after one mark or one
# space. A `.`, `-` or `_` the name class takes in as that mark is read by
# `near_miss`, here and before a `/`. It is refused where it does not go on
# to parse. Anything else naming
# the pact is a mention and is left alone: `pact:<name>` followed by
# punctuation, a space or the end of a code span, so the `.` ending a sentence
# leaves a mention. The one form that begins an anchor and is not an attempt
# is the one this plugin prints to show the shape, its locator opening with a
# placeholder, `/"<heading path>"`.
# Straight or curly quotes, spelled by code point so no line of this file holds
# a character a reader takes for another.
OPEN_QUOTE = "[\"'" + chr(0x201C) + chr(0x2018) + "]"
CLOSE_QUOTE = "[\"'" + chr(0x201D) + chr(0x2019) + "]"
PACT_MENTION_RE = re.compile(
    r"(?<![A-Za-z0-9_.@/-])pact:(?P<name>[A-Za-z0-9_.-]+)"
    r"(?:(?=[/#])(?!/\"<)"
    r"|(?=[^\s`|/#]?[ \t]?" + OPEN_QUOTE + r"[^\n]*?" + CLOSE_QUOTE + r"@)"
    r"|(?=[^\s`|/#]?@[0-9A-Fa-f]))"
    r"[^\s`|]*"
)
# Which exit each finding is.
EXIT_ONE = frozenset({SUPERSEDED, NOT_TAKEN, UNMATCHED, NOT_FOUND})
EXIT_TWO = frozenset({BROKEN, ONE_SIDED, REFUSED, UNREADABLE})


def load(path, name):
    """A sibling module by path, or a sentence and exit 2."""
    if not os.path.isfile(path):
        sys.stderr.write(
            f"pact-check: cannot read {shown(path, home_dir=os.path.expanduser('~'))}, "
            "which this command reads the pact "
            "through. It ships in the plugin beside this script; a copy of one "
            "script taken on its own is not a plugin. Nothing was read.\n"
        )
        raise SystemExit(2)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def near_miss(said, name):
    """True where SAID is NAME and one more mark the name class holds -- a
    `.`, `-` or `_` -- standing where an anchor's `/` went missing or just
    before it, as in `pact:orders-api."## A"@1a2b3c4d`: the name pattern
    takes the mark in, so without this the token names another pact and
    nobody reads it (round 1 of PR #749, yellow 4)."""
    said = said.lower()
    return len(said) == len(name) + 1 and said.startswith(name) and said[-1] in "._-"


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


def path_map(config, home_dir):
    """({normalised remote: path}, refusal or None) from the machine-local
    map under HOME_DIR. No map is an empty one; a map that is there and will
    not read is a refusal, because reading it as empty would report every
    signer it names as not found."""
    where = os.path.join(home_dir, MAP)
    if not os.path.lexists(where):
        return {}, None
    text = read(where)
    if text is None:
        return {}, f"{shown(where, home_dir=home_dir)} is there and could not be read"
    found, seen_header = {}, False
    row = re.compile(
        rf"^\|\s*(?P<remote>{config.CELL}+?)\s*\|\s*(?P<path>{config.CELL}+?)\s*\|\s*$"
    )
    for _index, line in config.unfenced(text.splitlines(), text):
        if not seen_header:
            seen_header = bool(MAP_HEADER.match(line))
            continue
        if config.CONFIG_SEPARATOR.match(line.strip()) and not found:
            continue
        match = row.match(line)
        if not match:
            break
        remote = config.normalise_remote(config.unescaped(match.group("remote")))
        found[remote] = os.path.expanduser(config.unescaped(match.group("path")))
    return found, None


def checkout(config, signer, root, mapped, home_dir=None):
    """(path, None) for the signer's checkout, or (None, why not), every
    path in the reason as `shown` prints it."""
    written, normalised, _name = signer
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
    work item's `spec.md`.
    """
    return sorted(glob.glob(os.path.join(home, "specs", "*", "spec.md")))


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


def clause_hash(checker, text, locator):
    """(hash, None) for the clause LOCATOR names in a pact's TEXT, or
    (None, why it names none)."""
    body = checker.unescape(locator[1:-1])
    parts = [p for p in body.split(checker.HEADING_SEP) if p.strip()]
    if not parts or checker.heading_level(parts[0].strip()) is None:
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


def grade(checker, pact_text, history, locator, want):
    """(status, what to do) for one anchor."""
    current, why = clause_hash(checker, pact_text, locator)
    if current is None:
        return BROKEN, (
            f"the heading path {why}: the clause was renamed or removed. "
            "Re-coordinate the signer"
        )
    if current == want:
        return OK, ""
    for sha in history.head():
        text = history.text(sha)
        if text is not None and clause_hash(checker, text, locator)[0] == want:
            return SUPERSEDED, (
                f"the signer was built against a superseded clause, the one "
                f"at {sha[:8]}; it reads @{current} now. Re-read it in the "
                "signer and re-anchor"
            )
    for sha in history.other():
        text = history.text(sha)
        if text is not None and clause_hash(checker, text, locator)[0] == want:
            return NOT_TAKEN, (
                f"the pact has not taken the signer's recorded change: this "
                f"hash is the clause on {history.ref_holding(sha)} (at "
                f"{sha[:8]}), which HEAD does not hold. Land that ref's pact "
                "change, or reconcile"
            )
    return UNMATCHED, (
        f"no commit in this repository gave the clause this hash, and it reads "
        f"@{current} now: the version was squashed away or never existed. "
        "Read both sides"
    )


def check(root, out=sys.stdout, home_dir=None):
    """Read the pact at ROOT and every signer; print; return the exit."""
    config = load(os.path.join(HOOKS, "config.py"), "specseal_config_for_pact")
    optin = load(os.path.join(HOOKS, "optin.py"), "specseal_optin_for_pact")
    checker = load(CHECKER, "specseal_evidence_for_pact")
    home_dir = home_dir or os.path.expanduser("~")

    def say(line):
        out.write(line + "\n")

    repo = optin.repo_root(os.path.abspath(root))
    if not repo:
        say(
            f"pact-check: {shown(root, home_dir=home_dir)} is not in a git "
            "repository — nothing was read"
        )
        return 2
    home = optin.home_at(repo)
    pact_path = os.path.join(home, PACT_FILE) if home else ""
    if not home or not os.path.lexists(pact_path):
        say(
            f"pact-check: {shown(repo, home_dir=home_dir)} holds no "
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
    name = config.pact_name(mine)
    if not name:
        say(
            f"pact-check: {shown(repo, home_dir=home_dir)} has no origin remote, "
            "so the name every pact "
            "anchor carries cannot be derived — set `origin` and run it again"
        )
        return 2
    shared = optin.home_paths(repo)[0]
    local = os.path.realpath(home) != os.path.realpath(shared)
    rel = os.path.relpath(pact_path, repo).replace(os.sep, "/")
    history = History(repo, rel)

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
    mapped, map_refusal = path_map(config, home_dir)
    if map_refusal:
        found(REFUSED, MAP_SHOWN, "", map_refusal)

    counts = dict.fromkeys((OK, SUPERSEDED, NOT_TAKEN, UNMATCHED, BROKEN), 0)
    read_count = 0
    for signer in signers:
        written = signer[0]
        if signer[1] == config.normalise_remote(mine):
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
        if not any(n == config.normalise_remote(mine) for _w, n, _ in pacts):
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
        read_count += 1
        anchors = 0
        for file_path in anchor_files(their_home):
            body = read(file_path)
            where = shown(file_path, path, home_dir)
            if body is None:
                found(UNREADABLE, written, where, "could not be read")
                continue
            view = checker.unquoted(body)
            for match in checker.PACT_ANCHOR_RE.finditer(view):
                if match.group("name").lower() != name:
                    continue
                anchors += 1
                status, detail = grade(
                    checker,
                    pact_text,
                    history,
                    match.group("locator"),
                    match.group("hash"),
                )
                counts[status] += 1
                if status != OK:
                    line = view.count("\n", 0, match.start()) + 1
                    found(status, written, f"{where}:{line} {match.group(0)}", detail)
            # A whole anchor naming this pact plus one mark is an attempt at
            # this pact, not a span to step past (round 1 of PR #749,
            # yellow 4).
            graded = [
                m.span()
                for m in checker.PACT_ANCHOR_RE.finditer(view)
                if not near_miss(m.group("name"), name)
            ]
            for near in PACT_MENTION_RE.finditer(view):
                inside = any(s <= near.start() < e for s, e in graded)
                said = near.group("name")
                if not (said.lower() == name or near_miss(said, name)) or inside:
                    continue
                line = view.count("\n", 0, near.start()) + 1
                found(
                    REFUSED,
                    written,
                    f"{where}:{line}",
                    f"`{near.group(0)}` does not parse as "
                    f'`pact:{name}/"<heading path>"@<hash>`, so nothing grades '
                    "it. Quote the heading path and give it a hash, `@00000000` "
                    "until the first report names the real one; or, where it "
                    "shows the shape rather than citing a clause, put it in a "
                    "fenced code block, which nothing reads",
                )
        say(
            f"READ {written} {shown(path, home_dir=home_dir)} — {anchors} pact "
            f"anchor{'' if anchors == 1 else 's'} naming `{name}`"
        )

    summary = (
        f"pact-check: the pact `{name}` — {read_count} of {len(signers)} "
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
        say(f"pact-check: {where} {sentence}")


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="pact-check",
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
