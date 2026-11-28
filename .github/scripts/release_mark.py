#!/usr/bin/env python3
"""Put the release's mark in the note: the stamp's results, and the mark's
PNG beside them where the repository turns the image on.

**The image is one key's to turn on.** `MARK_KEY` in the
`config.json` of the tree's `agentory/` root turns it on where
`lib/config.py#switch` reads the key as on (`mark_on`). Then the PNG is
attached as `ASSET` and the note's header becomes a paragraph holding the
image floated beside the results. Under any other answer nothing is drawn
or attached, and the header becomes a paragraph of the results alone. An
absent or empty key says nothing; any other value, and a key the reader
refuses, are named on a `::warning::` line, and the results still go in.
The plugin ships no release workflow, so the key is read in this repository
alone.

**The mark is the page form of the stamp's mark.** The mark has two
forms: a sprite the terminal stamp draws
(`skills/verify/scripts/stamp.py`), and a vector drawn once to the PNG
that `.claude-plugin/plugin.json` names as its `icon`. `draw` copies that PNG
byte for byte to the release asset and answers its width divided by
`DENSITY`, the width the note shows it at, so a high-density screen draws it
sharp. Nothing here reads the terminal stamp, so a change to the sprite
leaves the release image as it is, and a new page image is a new icon.

**Standard library only.** This file imports no package beyond Python's
own, so attaching the mark needs no imaging library. Nothing under `lib/`
or `skills/` imports this file, and the gates stay stdlib-only
(`CONTRIBUTING.md`, *Running the checks*).

**The rows are a fixed set, read from what the tag carries.** The suite's
counts come from the record the broad gate's recorder wrote for the run at
the tag, read by the broad gate's own reader and counter (`suite_counts`),
the pull requests and their `chain: capped` labels from the one read the
note already makes, of the pull requests whose `(#N)` ends a subject of the
tag's range (`publish_release_note.py#merged_pulls`), and the work items,
rounds and deferred issues from the round records at the tag, through the
readers the review chain's own gates use (`chain_counts`). A source that
cannot be read says `not read` in its row.

**Any failure leaves the note as it was published.** `.github/workflows/
publish-release.yml` runs this in its `mark` job, after `publish` created
the release in the same run. The note is already out by then, so a mark that
cannot be drawn costs the image and never the counts -- the rule
`publish_release_note.py`'s docstring states for its summary. Every failure
here is one log line and one `::warning::` with an exit of 0, and nothing is
edited unless the note's header is still in it exactly once as
`publish_release_note.py#header` wrote it. A note somebody edited
after publication is left alone, and so is its asset list; so is a note a
run of this job already marked, whose header is the marked one by then, with
the image or without it, so a re-run uploads and edits nothing. The upload
comes before the edit, so an edit that fails leaves an attached image the
note does not show, which the warning names.

`DRY_RUN=1` draws the PNG at `MARK_PNG` (by default `mark.png` in a
temporary directory) where the row turns the image on, prints the rows and
the note it would write, and uploads and edits nothing, so the mark of a
release whose job did not run can be drawn by hand from a checkout at the
tag, attached with `gh release upload` and shown with
`gh release edit --notes-file`.

Environment: `TAG`, `REPO`, `GH_TOKEN`, `SUITE_RECORDS` (the directory the
recorder wrote in) and `SUITE_KEY` (the key the run at the tag was handed),
`SUITE_OUTCOME` (the suite step's outcome), `DRY_RUN`, `MARK_PNG`.

Exit code: 0, always.
"""

import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
# Where this file's own repository is, which the modules below are loaded
# from; and the tree the mark reads its data from: the round records the
# chain rows count and the manifest that names the page image. They are the
# same checkout at the tag, and two names so a case can point the second at
# a fixture without moving the first.
CODE = os.path.abspath(os.path.join(HERE, "..", ".."))
ROOT = CODE
# `lib/` first on `sys.path`, where `lib/sibling.py` is imported from at the
# first module `module` is asked for.
sys.path.insert(0, os.path.join(CODE, "lib"))


# The tree's own modules are loaded when first asked for, not at import: a
# module that will not load is one more way for the mark to fail, and every
# way it fails has to end in today's note and an exit of 0 (`main`), which an
# import at the top of this file would end before `main` ran.
def module(rel):
    """The repository's module at REL, a `/`-joined path under `CODE`, as
    `lib/sibling.py#load` returns it."""
    import sibling

    return sibling.load(rel)


def publisher():
    """`.github/scripts/publish_release_note.py`, which owns the note's
    header, the pull request list and how a release is counted."""
    return module(".github/scripts/publish_release_note.py")


# How many PNG pixels the note shows per CSS pixel. The note's `<img>`
# carries the PNG's width divided by `DENSITY`, so a screen at twice the
# density draws it from pixels it has rather than by stretching them.
DENSITY = 2


# --- the rows ------------------------------------------------------------
#
# A release's panel is a fixed set of rows, held here as one constant: the
# owner's 0.17.0 wax seal is the drawing, and a label the code composed from free
# text could grow past the eight-wide label column the panel was drawn in, and
# a dry run still prints the rows in. That column is `{label:<8}`, not the
# longest label: `deferred` is exactly eight, which is the only reason the
# column looks set by it. The image carries no rows: they reach the note as
# the badges in its header (`results`).
LABELS = ("CLEARED", "tag", "PRs", "issues", "suite", "items", "capped", "deferred")
# The widest value a release's panel carries before the frame would cut it.
# The gate's panel value is 41 wide, for the open layout's 80 columns, and a
# release's rows are outside that layout, so this one is 23, and a case holds
# this one apart from the gate's.
PANEL_VALUE_WIDTH = 23
# What a row says when the source it is read from could not be read: the row
# stays, because a dropped row reads as none and a 0 reads as a count.
NOT_READ = "not read"
# The label the review chain puts on a pull request whose run ended at the
# round cap (`docs/running/the-run.md`).
CAPPED_LABEL = "chain: capped"


def release_rows(version, sha, pulls_n, issues_n, suite, chain):
    """The panel's rows for a release, `(label, value)` with `""` for a
    continuation, in `LABELS`' order.

    `suite` is `(passed, skipped)`; `chain` is `chain_counts`' four, each a
    number or None for not read. A suite value wider than
    `PANEL_VALUE_WIDTH` moves `S skipped` to a continuation row under
    `P passed`: only the suite can overflow, a five-digit
    count and a three-digit skip being 25. The items row needs both its
    numbers and the capped row both of its own, so either missing says
    `not read`."""
    items, rounds, capped, deferred = chain
    passed, skipped = suite
    rows = [
        ("CLEARED", f"v{version}"),
        ("tag", sha[:8]),
        ("", "main"),
        ("PRs", f"{pulls_n} merged"),
        ("issues", f"{issues_n} closed"),
    ]
    whole = f"{passed} passed, {skipped} skipped"
    if len(whole) <= PANEL_VALUE_WIDTH:
        rows.append(("suite", whole))
    else:
        rows += [("suite", f"{passed} passed"), ("", f"{skipped} skipped")]
    rows += [
        (
            "items",
            NOT_READ
            if items is None or rounds is None
            else f"{items} . {module('lib/console.py').plural(rounds, 'round')}",
        ),
        (
            "capped",
            NOT_READ if capped is None or items is None else f"{capped} of {items}",
        ),
        (
            "deferred",
            NOT_READ
            if deferred is None
            else module("lib/console.py").plural(deferred, "issue"),
        ),
    ]
    return rows


def results(rows):
    """`(cleared, lines)`: the stamp's results as badge lines, each a list of
    `(label, value)` pairs, which the note's header shows as badges.
    `cleared` is the cleared version, then the tagged commit with each branch
    it is on. `lines` are the suite and its skips, the review rounds and the
    work items, and how many were capped and the issues deferred, two to a
    line; a row not read gives `not read` on each badge it feeds. The pull
    requests and issues are left out: `publish_release_note.py#count_badges`
    states them. Each badge's colours are `publish_release_note.py#badge`'s,
    read by its label."""
    by = {}
    for label, value in rows:
        if label:
            by[label] = [value]
            last = label
        else:
            by[last].append(value)
    tag = by["tag"]
    cleared = [
        [("CLEARED", by["CLEARED"][0])],
        [("commit", tag[0]), *(("on", branch) for branch in tag[1:])],
    ]
    passed, skipped = [
        part.strip() for value in by["suite"] for part in value.split(",")
    ]
    lines = [[("suite", passed), ("skipped", skipped.split()[0])]]
    items, capped, deferred = by["items"][0], by["capped"][0], by["deferred"][0]
    if items == NOT_READ:
        lines.append([("review", NOT_READ), ("work items", NOT_READ)])
    else:
        count, rounds = items.split(" . ")
        lines.append([("review", rounds), ("work items", count)])
    lines.append(
        [
            ("capped", capped if capped == NOT_READ else capped.split()[0]),
            ("deferred", deferred if deferred == NOT_READ else deferred.split()[0]),
        ]
    )
    return cleared, lines


# --- the sources ---------------------------------------------------------


def gate():
    """`skills/verify/scripts/broad_gate.py`, whose reader and counter the
    broad gate's panel reads the same record with: one counter for the
    panel and the release, and no second reader of what pytest printed."""
    return module("skills/verify/scripts/broad_gate.py")


def suite_counts(directory, key):
    """`(passed, skipped)` from the record the broad gate's recorder wrote
    under `directory` for the sessions carrying `key`.

    The run at the tag loads the recorder as the broad gate loads it
    (`.github/workflows/publish-release.yml`), and `broad_gate.read_record`
    counts each report under the category pytest's own summary line counts
    it under. Raises `ValueError` where no directory or no key is named,
    where no session carries the key, where a line of a keyed record did not
    parse, where a session stopped part-way, where a test or a collection
    had no file of its own and so counts under no category (`unplaced`),
    or where the counts hold a failure or an error -- a `CLEARED` above a red
    or a short suite would be false, and a record nobody can read is never a
    zero."""
    if not directory:
        raise ValueError("SUITE_RECORDS names no directory")
    if not key:
        raise ValueError("SUITE_KEY names no key")
    record = gate().read_record(directory, key, CODE)
    if not record.sessions:
        raise ValueError(f"no record under {directory} carries the key {key}")
    if record.unread:
        raise ValueError(
            f"{record.unread} of the lines under {directory} did not parse as "
            "the recorder's"
        )
    if record.unended:
        raise ValueError(
            f"{record.unended} of the suite's pytest sessions stopped part-way"
        )
    if record.unplaced:
        raise ValueError(
            f"{record.unplaced} of the suite's tests and collections had no "
            "file of their own and were counted under no category"
        )
    failed = record.counts.get("failed", 0)
    errors = record.counts.get("error", 0)
    if failed or errors:
        raise ValueError(
            f"the suite at the tag did not pass: {failed} failed and {errors} errors"
        )
    return record.counts.get("passed", 0), record.counts.get("skipped", 0)


def readers():
    """`(routing, chain_check)`: the modules the review chain's own gates
    read round records with, so the counts here are the ones a gate would
    read and a change to where records live has to move these readers
    first."""
    chain = module("skills/code-review/scripts/chain_check.py")
    routing = module("lib/routing.py")
    return routing, chain


def labels_of(pull):
    return {
        (label.get("name") if isinstance(label, dict) else str(label)) or ""
        for label in pull.get("labels") or ()
    }


def chain_counts(root, pulls):
    """`(items, rounds, capped, deferred)` for the release's pull requests,
    each a number or None for not read, with the log saying why.

    `capped` counts the pull requests labelled `CAPPED_LABEL`. A pull request
    is a work item where exactly one `routing.md` under `root` names its head
    branch (`lib/routing.py#item_dir`), and its rounds are
    `lib/routing.py#rounds`. `deferred` is the number of distinct issues
    that are the home of a finding whose close block's `verdict:` reads
    `deferred <home>`, read with `chain_check.record_findings` and `#issue_of`:
    a home names an issue only where it is exactly `#N`, so a file,
    the frame, or a home with words after the issue counts none. A finding
    with no close block is open and counts none. A round record the check's
    reader refuses anything of -- one in an older shape, a table or
    labelled lines, which holds no round block; a line of a
    `iadd` block that does not parse; a block out of its place; a finding
    with no finding block -- leaves
    `deferred` None -- an incomplete count is a wrong number -- a `rounds`
    that cannot be listed
    leaves `rounds` None as well, and a reader
    that will not load leaves all three tree counts None.

    A tree with no declaration at all, or a pull request labelled
    `CAPPED_LABEL` that resolves to no work item, is a count known to be
    incomplete -- records moved or retired before the tag -- so the
    three tree rows are not read rather than drawn as 0."""
    capped = sum(1 for pull in pulls if CAPPED_LABEL in labels_of(pull))
    try:
        import sibling

        # The mark goes on without these rows, so an absent reader raises
        # `lib/sibling.py#Absent` with no sentence of the loader's, and the
        # line below names it.
        with sibling.going_on():
            routing, chain = readers()
    except (Exception, SystemExit) as problem:
        # `Absent`'s path; an `ImportError` carries a `path` of its own.
        if isinstance(problem, SystemExit) and getattr(problem, "path", None):
            problem = f"{problem.path} is absent"
        print(
            f"the chain rows are not read: the round record's readers did not load ({problem})"
        )
        return None, None, capped, None
    if not routing.declarations(root):
        print(
            "the chain rows are not read: no routing.md under "
            f"{root} declares a branch, so the round records are not where "
            "the readers look"
        )
        return None, None, capped, None
    items, rounds, deferred, unread, lost = 0, 0, set(), [], []
    rounds_unread = False
    for pull in pulls:
        item = routing.item_dir(root, pull.get("headRefName") or "")
        if not item:
            if CAPPED_LABEL in labels_of(pull):
                lost.append(f"#{pull.get('number')}")
            continue
        items += 1
        if routing.rounds_unreadable(item):
            # Its records exist and cannot be listed, so its rounds are not
            # zero; the rounds row is not read, and neither is deferred.
            rounds_unread = True
            unread.append(os.path.join(item, *routing.ROUNDS_DIR.split("/")))
            continue
        records = routing.rounds(item)
        rounds += len(records)
        for path in records:
            try:
                with open(path, encoding="utf-8") as handle:
                    text = handle.read()
            except (OSError, UnicodeDecodeError):
                unread.append(path)
                continue
            found, errors = chain.record_findings(text, path)
            # A finding the reader refused is a verdict nobody counted.
            if errors:
                unread.append(path)
                continue
            for kind, home in (f.verdict for f in found):
                issue = chain.issue_of(home) if kind == chain.DEFERRED else None
                if issue is not None:
                    deferred.add(issue)
    if lost:
        print(
            f"the chain rows are not read: {', '.join(lost)} carry "
            f"{CAPPED_LABEL!r} and resolve to no work item under {root}"
        )
        return None, None, capped, None
    if unread:
        print(
            (
                "the rounds and deferred rows are"
                if rounds_unread
                else "the deferred row is"
            )
            + " not read: the round record's reader refused "
            + ", ".join(os.path.relpath(p, root) for p in unread)
        )
        return items, None if rounds_unread else rounds, capped, None
    return items, rounds, capped, len(deferred)


# --- publishing ----------------------------------------------------------

# The asset's name on the release, and so the last part of its URL.
ASSET = "mark.png"

# The key of the tree's `agentory/config.json` that turns the image on, read
# by `lib/config.py#switch`. What `mark_on` says where a key is written and
# does not turn it on is the switch's sentence, closed by `NO_IMAGE` and
# printed after `IMAGE_WARNING`.
MARK_KEY = "Release note inspection mark"
IMAGE_WARNING = "::warning::release mark image: "
NO_IMAGE = "the note's header holds the results without the mark's image"


def mark_on(root):
    """`(on, note)`: whether `MARK_KEY` in the `config.json` of the `agentory/`
    root of the tree at ROOT turns the image on, and the sentence naming a
    key that is written and does not, or None.

    The root is `lib/optin.py#home_at`'s, and the key is read through
    `lib/config.py#switch`, which reads a tree with no root as no file. A
    tree with no root, an absent key and an empty one are off and say
    nothing; any other value, and a refusal the reader returns, are off and
    named, closed by `NO_IMAGE`. Nothing here refuses: the image is a
    picture, and the results go in whatever the key says."""
    home = module("lib/optin.py").home_at(root)
    return module("lib/config.py").switch(home, MARK_KEY, NO_IMAGE)


class Refused(Exception):
    """A reason the mark is not attached; `main` says it and exits 0."""


def gh(*args):
    """`gh <args>`'s stdout, or `Refused` naming the call and what it said.

    `gh` starts through `lib/gitcmd.py#gh`, loaded here at first use, and a
    `gh` that gave no answer is `Refused` with the runner's line."""
    gitcmd = module("lib/gitcmd.py")
    try:
        out = gitcmd.gh(*args)
    except gitcmd.Failed as failed:
        raise Refused(failed.line) from None
    if out.returncode:
        raise Refused(f"gh {' '.join(args[:2])} failed: {out.stderr.strip()}")
    return out.stdout


def tagged(tag):
    """The commit `tag` names, which the panel's `tag` row shows, asked in
    the directory this runs in through `lib/gitcmd.py#git`; `Refused` as
    `gh` refuses."""
    gitcmd = module("lib/gitcmd.py")
    try:
        out = gitcmd.git(os.curdir, "rev-parse", f"{tag}^{{commit}}")
    except gitcmd.Failed as failed:
        raise Refused(failed.line) from None
    if out.returncode:
        raise Refused(f"git rev-parse {tag} failed: {out.stderr.strip()}")
    return out.stdout.strip()


# The eight bytes every PNG opens with. The chunk after them is `IHDR`, whose
# first four bytes of data are the image's width, big-endian (the PNG
# specification, *File structure*). So a PNG's first 24 bytes are the
# signature, the chunk's length and type, the width and the height.
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def draw(png):
    """Copy the page image to `png` and answer the note's width for it in
    CSS pixels, or raise `Refused` saying why.

    The page image is the file `.claude-plugin/plugin.json` under `ROOT`
    names as its `icon`, a path from the plugin's root spelt with `/`. It is
    copied byte for byte, and the answer is the width in its `IHDR` chunk
    divided by `DENSITY`. The refusals: the manifest cannot be read, it
    names no `icon`, the file it names cannot be read, the file does not
    open with the PNG signature and an `IHDR` chunk, or the copy cannot be
    written."""
    manifest = os.path.join(ROOT, ".claude-plugin", "plugin.json")
    try:
        with open(manifest, encoding="utf-8") as handle:
            fields = json.load(handle)
    except (OSError, ValueError) as problem:
        raise Refused(
            f"the plugin's manifest .claude-plugin/plugin.json cannot be read ({problem})"
        ) from problem
    icon = fields.get("icon") if isinstance(fields, dict) else None
    if not isinstance(icon, str) or not icon:
        raise Refused(
            "the plugin's manifest .claude-plugin/plugin.json names no icon, "
            "the page image the mark is"
        )
    # The manifest spells the path with `/`, so it is split before it is
    # joined, and its `.` segments are dropped.
    source = os.path.join(
        ROOT, *(part for part in icon.split("/") if part not in ("", "."))
    )
    try:
        with open(source, "rb") as handle:
            data = handle.read()
    except OSError as problem:
        raise Refused(
            f"the icon {icon} the manifest names cannot be read ({problem})"
        ) from problem
    if data[:8] != PNG_SIGNATURE or data[12:16] != b"IHDR" or len(data) < 24:
        raise Refused(
            f"the icon {icon} is not a PNG: it does not open with the PNG "
            "signature and an IHDR chunk"
        )
    try:
        with open(png, "wb") as handle:
            handle.write(data)
    except OSError as problem:
        raise Refused(f"the mark could not be written at {png}: {problem}") from problem
    return int.from_bytes(data[16:20], "big") // DENSITY


def mark_release(tag, repo, dry):
    """Put the mark for `tag` in its note, drawing and attaching its image
    where `mark_on` reads the row on, or raise `Refused` at the first thing
    that stops it -- before any write, apart from the edit."""
    note = publisher()
    version = note.version_of(tag)
    if version is None:
        raise Refused(f"{tag!r} is not a vX.Y.Z tag")
    outcome = os.environ.get("SUITE_OUTCOME", "").strip()
    if outcome and outcome != "success":
        raise Refused(f"the suite at {tag} ended {outcome}, and a mark says it passed")
    try:
        suite = suite_counts(
            os.environ.get("SUITE_RECORDS", "").strip(),
            os.environ.get("SUITE_KEY", "").strip(),
        )
    except (OSError, ValueError) as problem:
        raise Refused(f"the suite's counts cannot be read: {problem}") from problem
    pulls = note.merged_pulls(repo, note.commit_range(note.previous_tag(tag), tag))
    if pulls is None:
        raise Refused("the release's pull requests could not be read")
    work, closed, people = note.tally(pulls, repo.split("/")[0])
    chain = chain_counts(ROOT, work)
    rows = release_rows(version, tagged(tag), len(work), len(closed), suite, chain)
    for label, value in rows:
        print(f"{label:<8} {value}")
    # Read before the draw, so a tree that leaves the image off never meets
    # a refusal of the draw's over an image it does not show.
    on, unread = mark_on(ROOT)
    if unread:
        print(IMAGE_WARNING + unread)
    if on:
        # The upload names the asset after the file, so a run that uploads
        # writes `ASSET` in a directory of its own; `MARK_PNG` is a dry run's.
        path = os.environ.get("MARK_PNG") if dry else ""
        path = path or os.path.join(tempfile.mkdtemp(prefix="release-mark-"), ASSET)
        width = draw(path)
        print(f"copied the icon the plugin's manifest names to {path}")
    try:
        body = json.loads(gh("release", "view", tag, "--repo", repo, "--json", "body"))[
            "body"
        ]
    except (ValueError, KeyError, TypeError) as problem:
        raise Refused(f"gh release view printed no note: {problem}") from problem
    header = note.header(work, closed, people)
    if body.count(header) != 1:
        raise Refused(
            "the header is not in the note exactly once as `header` writes it "
            "for this release -- the note was edited after publication, a run "
            "of this job already replaced it, it went out without one, or the "
            "pull requests moved between the two lists; nothing was uploaded"
        )
    said, lines = results(rows)
    if on:
        image = f"https://github.com/{repo}/releases/download/{tag}/{ASSET}"
        alt = f"The {version} release mark"
        replacement = note.marked_header(
            image, alt, width, said, lines, work, closed, people
        )
    else:
        replacement = note.marked_header(
            None, None, None, said, lines, work, closed, people
        )
    marked = body.replace(header, replacement)
    if dry:
        print("DRY_RUN -- nothing uploaded and nothing edited; the note would read:")
        print(marked)
        return
    if not on:
        gh("release", "edit", tag, "--repo", repo, "--notes", marked)
        print(f"put the mark's results in {tag}'s note, with no image")
        return
    gh("release", "upload", tag, path, "--repo", repo)
    try:
        gh("release", "edit", tag, "--repo", repo, "--notes", marked)
    except Refused as problem:
        raise Refused(
            f"{problem}; {ASSET} was uploaded and the note does not show it"
        ) from problem
    print(f"attached {ASSET} to {tag} and put it in the note")


def main():
    tag = os.environ.get("TAG", "").strip()
    repo = os.environ.get("REPO", "").strip()
    dry = os.environ.get("DRY_RUN", "").strip() not in ("", "0", "false", "no")
    if dry:
        print("DRY_RUN -- nothing will be uploaded or edited")
    try:
        import sibling

        # The job exits 0 whatever fails, and the loader's "Nothing was
        # read." pairs with exit 2, so an absent module raises
        # `lib/sibling.py#Absent` with no sentence and the line below names
        # it.
        with sibling.going_on():
            mark_release(tag, repo, dry)
    except (Exception, SystemExit) as problem:
        if isinstance(problem, Refused):
            reason = str(problem)
        # `Absent`'s path; an `ImportError` carries a `path` of its own.
        elif isinstance(problem, SystemExit) and getattr(problem, "path", None):
            reason = f"{problem.path} is absent"
        else:
            reason = f"{type(problem).__name__}: {problem}"
        reason = " ".join(reason.split())
        print(f"no mark: {reason} -- the note stays as it was published")
        print(f"::warning::release mark skipped: {reason}")
    return 0


if __name__ == "__main__":
    # `lib/console.py#STREAMS` owns this answer. The loop is spelt here
    # rather than imported because this script loads the tree's modules only
    # when first asked (`module`), so a module that will not load ends in
    # today's note and an exit of 0 (`main`).
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
