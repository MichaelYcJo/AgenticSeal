"""Shared reader: which way did this work item say it was going?

The routing answer -- review chain or straight to the PR -- is given before the
first edit, and this module reads it back. Without a declaration, the route
could only be guessed from the absence of a review mark, and a mark only
exists after a review passes.

A declaration lives at `seal/threads/<work-item-id>/routing.md` and is committed.
Committed is the load-bearing part: the check moves to the pull request, and CI
sees only what is in the tree; nothing under the git directory travels there.

Beside the work item rather than at the root's top level, because a work item
begins and ends in one directory and routing is its first fact. It also gives
the work below the SDD ladder somewhere to exist: those items write no
`frame/design.md`, so without it they would leave no trace anywhere, and they
are most of what the pull request's check sees.

Loaded by the pull request's check and by every script that reads a
declaration, rather than copied into each -- the same reason `optin.py`
gives for being a module: divergent copies is how half of them keep the old
answer.

Everything here fails toward "no declaration". A file that cannot be read is
not an answer somebody gave, so the pull request's check reads its branch as
undeclared. Silence would make a corrupt file into the standing waiver
`docs/running/the-review-and-parity-arms.md` refuses to build.

Three of the rows are exceptions and none of them is a loophole. Nothing decides
a commit on `Implementation`, `Planning` or `Automation` -- see `parse()` for
why an absent or unreadable answer in any of them reads as unanswered instead
of taking the whole declaration down with it.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gitcmd
import optin

try:
    import blocks
except ImportError as missing:
    # `lib/config.py` raises the same sentence for the same reason: this is
    # a module gates and scripts import, and a script that loads it through
    # `lib/sibling.py` (`chain_check.py`) catches the error.
    raise ImportError(
        "cannot read "
        + os.path.join(os.path.dirname(os.path.abspath(__file__)), "blocks.py")
        + ", and it is the walk this reader reads routing.md through, which "
        "tells a live row from one quoted in a fence or parked in a comment. "
        "This file ships beside it under `lib/`; a copy of one taken on its "
        "own is not a plugin"
    ) from missing

try:
    import tables
except ImportError as missing:
    # The same sentence as the walk's above, for the file that splits a row
    # into its cells as cmark-gfm does.
    raise ImportError(
        "cannot read "
        + os.path.join(os.path.dirname(os.path.abspath(__file__)), "tables.py")
        + ", and it is the row splitter this reader reads routing.md's cells "
        "through, which reads an escaped pipe as one literal pipe. "
        "This file ships beside it under `lib/`; a copy of one taken on its "
        "own is not a plugin"
    ) from missing

REVIEW = "Review"
DESTINATION = "Destination"
BRANCH = "Branch"
IMPLEMENTATION = "Implementation"
PLANNING = "Planning"

CHAIN = "through the review chain"
DIRECT = "straight to the PR"
REVIEW_ANSWERS = (CHAIN, DIRECT)

OPEN_PR = "open the pull request"
STOP_BEFORE_PR = "stop before the pull request"
DESTINATION_ANSWERS = (OPEN_PR, STOP_BEFORE_PR)

BY_CRAFTER = "crafter"
BY_SESSION = "the session"
IMPLEMENTATION_ANSWERS = (BY_CRAFTER, BY_SESSION)

# The fourth axis. `BY_SESSION` is reused rather than aliased under a second
# name: one string, one vocabulary, and a second spelling of it is the shape
# that lets the two drift a release later.
BY_FRAMER = "framer"
PLANNING_ANSWERS = (BY_FRAMER, BY_SESSION)

# The fifth row, and the first that is not a party. The other four each name
# somebody who does or does not run; this one names a property of the RUN --
# whether it may come back and ask. A reader six months later asks that about a
# work item, and this row is where the answer stands.
#
# `no` is not "a person did it by hand". It is "this run may stop to ask", which
# is the half a label cannot say and the half a reader gets wrong.
#
# The pull request's check decides nothing on it: it is a record the
# orchestrator reads (`docs/running/the-run.md` *The run*). The plugin's
# `PreToolUse` hook, `hooks/ask-under-automation.py`, reads a `yes` alone,
# through `open_declarations`, and refuses an `AskUserQuestion` call while an
# open work item's row reads it.
AUTOMATION = "Automation"
AUTOMATION_YES = "yes"
AUTOMATION_NO = "no"
AUTOMATION_ANSWERS = (AUTOMATION_YES, AUTOMATION_NO)

FILENAME = "routing.md"


def shown(lines):
    """[(index, line)] for each of LINES `table_rows` reads, ending removed.

    The walk's hidden lines are left out, and only those: where it is not
    sure, this reader's base reading stands, and that reading hides
    nothing. So on every line the answer is either the base reading or a
    renderer's, which `tests/lib/test_routing.py`'s `Test_module`
    holds over a generated corpus.

    LINES are the file's lines as GFM ends them, which `table_rows` takes
    from `blocks.gfm_lines`: a `<!--` after a U+2028 or a form feed, which
    `str.splitlines` breaks at, stays mid-line and hides nothing a renderer
    shows (`lib/tables.py#hidden_lines` says more).
    """
    hidden = blocks.walk(lines).hidden()
    return [
        (index, raw.rstrip("\r\n"))
        for index, raw in enumerate(lines)
        if index not in hidden
    ]


def table_rows(text):
    """Every markdown table row of two cells or more, as (label, value), its
    first two cells.

    **A row is split as cmark-gfm splits it** (`lib/tables.py#table_cells`):
    an escaped pipe is one literal pipe in its cell, a row whose closing pipe
    is left off is a row, and a line four spaces in is code. The delimiter
    row (`tables.DELIMITER_ROW`) is no row.

    Unknown labels are left in rather than filtered: a reader that drops what
    it does not recognise cannot gain a third axis later without the older
    readers silently ignoring it. The caller decides what it needs.

    **A row a renderer does not show is not a row.** Otherwise an example
    quoted in a fenced block below the table, or an answer somebody parked
    in an HTML comment, would be a second row of its label, and a label
    written twice has no value at all.
    `shown` below is what this walks, and it hides exactly the lines
    `lib/blocks.py` is sure a renderer hides: inside a fenced
    block or a comment block that begins its line, where either closes.
    Every other line is read by the base reading, so a fence or a `<!--`
    nobody closed hides nothing, and a declaration below one reads.
    A file whose only table is hidden is not a declaration, the direction
    this module fails in.
    """
    rows = []
    for _index, line in shown(blocks.gfm_lines(text)):
        if tables.DELIMITER_ROW.match(line):
            continue
        cells = tables.table_cells(line)
        if cells is None or len(cells) < 2:
            continue
        rows.append((cells[0], cells[1]))
    return rows


def parse(text):
    """One declaration, or None when the text is not one.

    Strict on the two answer vocabularies and on the branch being named. A
    tolerant read here would turn prose that merely mentions the review chain
    into a waiver -- the same failure `has_marker` avoids by refusing to read a
    marker out of a commit message.

    `Implementation` and `Planning` are the third and fourth axes and they are
    read on DIFFERENT terms: both are optional, and an answer outside either
    vocabulary reads as unanswered rather than as "this file is not a
    declaration". Both halves of that are forced by what already exists. Every
    declaration written before an axis was added has no such row, and a
    required row would turn each of them into no declaration -- the pull
    request's check would read a branch whose answer is committed in the tree
    as undeclared. The strict spelling below is deliberate for the first two,
    because a wrong answer there decides whether a reviewer sees the work.
    `Planning`'s one reader is `chain_check.py`, which reads a `framer` answer
    against the frame's mark, and no script reads `Implementation`: the sealer
    reads it and withholds where a declared `crafter` left a closed phase with
    no record (`agents/sealer.md` step 4). So a wrong answer here is read
    against a record the run left, where a wrong answer above decides what the
    pull request owes. That is why
    the rows are optional rather than lenient, and it is also the asymmetry to
    know about: a backticked or capitalised answer is rejected loudly in the
    first two, because the file reads as no declaration, and silently here.
    `templates/records/sdd-routing.md` is the only spelling a
    session should copy, and a test parses that file so it cannot drift.

    The two optional rows are read independently of each other. One answered
    and one absent is a common state -- a session that framed the work itself
    and spawned `crafter` to build it -- so neither may stand in for the other.

    `Automation` is the fifth row and it is read on the same looser terms, for
    the same reason one step further along: the pull request's check decides
    nothing on it, and the plugin's `PreToolUse` hook reads a `yes` alone, so
    an absent or unreadable row reads as never asked and that hook lets the
    session's question through. A required row would
    turn every declaration committed without it into "not a declaration",
    and the pull request's check would read every branch that already
    answered as undeclared.

    **What it reads is `table_rows`', which skips a row a renderer does not
    show**: a table wholly inside a fenced block, or inside a comment
    block that closes, is no declaration, as any `routing.md` that does not
    parse is. A fence or a `<!--` nobody closed
    above the table is not a block at all, so that declaration still reads.

    **A label written twice has no value**, the rule
    `lib/config.py#config_value` gives every `seal/config.json` key: taking
    the last row would let a second `Review` row below the first answer for
    it, with nothing saying there were two. A strict label doubled --
    `Review`, `Destination`, `Branch` -- makes the file no declaration, as
    any file that will not parse is; an optional label doubled is
    unanswered, on the terms above.
    """
    rows = table_rows(text)
    counts = {}
    for label, _value in rows:
        counts[label] = counts.get(label, 0) + 1
    found = {label: value for label, value in rows if counts[label] == 1}
    review = found.get(REVIEW)
    destination = found.get(DESTINATION)
    branch = found.get(BRANCH)
    implementation = found.get(IMPLEMENTATION)
    planning = found.get(PLANNING)
    automation = found.get(AUTOMATION)
    if review not in REVIEW_ANSWERS:
        return None
    if destination not in DESTINATION_ANSWERS:
        return None
    if not branch:
        return None
    return {
        "review": review,
        "destination": destination,
        "branch": branch,
        # One value for "no row" and for "a row nobody can read". They must not
        # diverge: a reader that told them apart would have to decide what to
        # do about an unreadable one, and the only honest answer is the same
        # nothing it does for an absent one.
        "implementation": (
            implementation if implementation in IMPLEMENTATION_ANSWERS else None
        ),
        "planning": planning if planning in PLANNING_ANSWERS else None,
        # Absent and unreadable collapse here too, and for `Automation` the
        # collapse carries a meaning the other rows do not have: a question
        # that IS asked always writes one of the two values, so `None` means
        # the question was never put to anybody. A chosen `no` and a question
        # nobody read are not the same fact, which is the whole reason the
        # unchecked half is a VALUE rather than an absence.
        "automation": automation if automation in AUTOMATION_ANSWERS else None,
    }


def current_branch(cwd):
    """The checked-out branch, or "" when detached, unreadable or where git
    did not answer.

    A detached HEAD matches no declaration. That is the correct direction: nothing on a detached HEAD is the work item a branch
    was declared for.
    """
    try:
        out = gitcmd.git(cwd or ".", "rev-parse", "--abbrev-ref", "HEAD")
    except gitcmd.Failed:
        return ""
    name = out.stdout.strip() if out.returncode == 0 else ""
    return "" if name == "HEAD" else name


def read_declaration(path):
    """`parse` of the `routing.md` at PATH, or None where the file cannot be
    read or decoded. `declarations` reads each work item's file through it,
    and `settle.py` reads one in a records directory `--from` names."""
    try:
        with open(path, encoding="utf-8") as f:
            return parse(f.read())
    except (OSError, UnicodeDecodeError):
        # `UnicodeDecodeError` is a `ValueError`, not an `OSError`, and it
        # is named rather than its parent: `parse()` is pure string work
        # today, so a `ValueError` reaching here later would be a defect in
        # it, and swallowing that as "no declaration" is how a gate goes
        # quiet for a reason nobody wrote down. A
        # declaration that is not valid UTF-8 would raise out of
        # `declarations()` into the check that read it, which then decides
        # nothing on the branch. The module docstring says everything
        # here fails toward "no declaration"; a file nobody can decode is
        # not an answer somebody gave, so it reads as none and its branch
        # reads as undeclared. `chain_check.py` catches both when it reads
        # the event payload, for the same reason.
        return None


def declarations(root):
    """Every readable declaration under `root`, as (path, parsed) pairs.

    One per work-item directory. Nothing here reads the directory name: the id
    orders the directories and names the work, but which declaration APPLIES is
    settled by the branch it names, not by its position in a sort.

    `root` is the repository root; the work items are under whichever `seal/`
    `optin.home_at` finds for it, and a repository with none has no
    declarations — the same silence as a `seal/threads/` that is not there.
    """
    home = optin.home_at(root)
    if not home:
        return []
    where = os.path.join(home, optin.WORK_ITEMS)
    try:
        names = sorted(os.listdir(where))
    except OSError:
        return []
    out = []
    for name in names:
        path = os.path.join(where, name, FILENAME)
        parsed = read_declaration(path)
        if parsed:
            out.append((path, parsed))
    return out


def item_dir(root, branch):
    """The work-item directory the declaration for `branch` lives in, or "".

    This is what makes a review round writable before a pull request exists.
    The round records live two levels down, in `trail/rounds/`, so whatever resolves
    the declaration resolves them too, and the branch is the only key
    available at the moment a round closes.

    Two declarations naming one branch resolve to nothing here: that is not
    an answer. Declarations accumulate over a repository's life, and a
    branch-less match would let the first work item ever declared answer for
    every branch after it.
    """
    if not root or not branch:
        return ""
    matching = [path for path, d in declarations(root) if d["branch"] == branch]
    return os.path.dirname(matching[0]) if len(matching) == 1 else ""


# The two lines of `git worktree list --porcelain` `open_declarations`
# reads: the one that opens each worktree's entry with its path, and the
# one that names the branch it has checked out. A bare or detached entry has
# no `branch` line.
WORKTREE_LINE = "worktree "
BRANCH_LINE = "branch refs/heads/"


def open_declarations(cwd):
    """The declarations of the work items open in the repository CWD stands
    in, as `declarations` gives them: (path, parsed) pairs.

    **Open means that the branch a declaration names is checked out in a
    worktree of that repository**, any of the worktrees `git worktree list
    --porcelain` lists, and not only CWD's. A work item's directory outlives
    its run until the settle after its release, so the directory's presence
    says nothing about whether its run goes on: a released item's
    `Automation` row still reads what its run answered, and a reader that
    took the item as open would answer for a run nobody is making. A
    worktree left on a merged
    branch keeps its item open, which is the cost of reading git rather than
    a guess.

    The declarations are read under the root `optin.home_at` finds for each
    listed worktree, and each `routing.md` counts once, by its real path: in
    local mode every worktree answers the one root under the common git
    directory. `[]` where CWD is empty, where git does not start or does not
    finish (`gitcmd.Failed`, a `SystemExit` a bare `except Exception` does
    not catch), exits non-zero, or lists no worktree.
    `hooks/ask-under-automation.py` reads it.
    """
    if not cwd:
        return []
    try:
        done = gitcmd.git(cwd, "worktree", "list", "--porcelain")
    except gitcmd.Failed:
        return []
    if done.returncode:
        return []
    lines = done.stdout.split("\n")
    # `normpath` on git's answer, as `optin.home_paths` does: git prints a
    # worktree's path with `/` on Windows, and `declarations` joins the
    # records' path onto it with `\`, which would spell one path two ways.
    trees = [
        os.path.normpath(line[len(WORKTREE_LINE) :])
        for line in lines
        if line.startswith(WORKTREE_LINE)
    ]
    checked_out = {
        line[len(BRANCH_LINE) :] for line in lines if line.startswith(BRANCH_LINE)
    }
    out, seen = [], set()
    for tree in trees:
        for path, parsed in declarations(tree):
            real = os.path.realpath(path)
            if parsed["branch"] in checked_out and real not in seen:
                seen.add(real)
                out.append((path, parsed))
    return out


ROUND_RE = re.compile(r"round-(\d+)\.md")

# The subdirectory the records live in, under the work item, `/`-joined.
ROUNDS_DIR = optin.ROUNDS


def round_number(name):
    """The N in `round-N.md`, or None when the name is not one.

    The one place the ordering rule lives: `skills/code-review/scripts/chain_check.py`
    calls this rather than writing the pattern again, so records sort by
    number and `round-10.md` comes after `round-9.md`.
    """
    m = ROUND_RE.fullmatch(os.path.basename(name))
    return int(m.group(1)) if m else None


def _ordered(where):
    """`round-N.md` under `where`, lowest round first, or [] when unreadable.

    Filtered BEFORE the sort, not after. Both callers below hand this a
    directory that holds other things -- the work item's own directory holds
    `routing.md` and the rest of the SDD set, and `trail/rounds/` holds whatever a
    repository chooses to put beside its records -- and `sorted` comparing
    None against an int raises rather than ordering. Nothing here may assume
    a directory of records only.
    """
    try:
        names = os.listdir(where)
    except OSError:
        return []
    found = [(round_number(n), n) for n in names]
    return [
        os.path.join(where, n) for _, n in sorted(p for p in found if p[0] is not None)
    ]


def rounds(item):
    """Every round record in a work item's `trail/rounds/`, lowest round first.

    Numerically, not by name, for the reason `round_number` gives.

    `trail/rounds/` rather than the work-item directory itself, because `round-N`
    is the one member of the SDD set that is plural and unbounded, and the
    structure should say which member grows. A `trail/rounds` that is not
    there, or is a file, holds no record; `rounds_unreadable` names the
    states that hold records nothing can list.

    What stays different between the two readers is deliberate, and it is not
    the order: this one reads the working tree, because its callers, `seal
    settle` and the release scripts, read the checkout they run in. The
    pull-request check reads what git carries, because CI sees nothing
    else -- an untracked file there is evidence nobody can open.
    """
    if not item:
        return []
    return _ordered(os.path.join(item, *ROUNDS_DIR.split("/")))


def rounds_unreadable(item):
    """True when `rounds` beside the work item is a link of any kind, or a
    directory nothing can list.

    Told apart from "no records" because the two need opposite answers: one
    is every work item that ran no review and must stay quiet, the other
    is a review whose whole text git is still carrying while every reader
    reports that none happened.
    """
    if not item:
        return False
    where = os.path.join(item, *ROUNDS_DIR.split("/"))
    if os.path.islink(where):
        # ANY link, including one that resolves to a directory holding
        # records. `os.path.exists` follows links, so it is False for a broken
        # one, and `os.path.isdir` follows a live one into the directory and
        # stays quiet while the pull-request check — which sees git's `120000`
        # and calls it not-a-tree — fails and tells the reader to `mkdir` a
        # path that already exists. The two readers answer for what GIT
        # carries, and git carries a link.
        return True
    if os.path.isdir(where):
        try:
            os.listdir(where)
        except OSError:
            # A directory nothing can list. `_ordered` returns [] for it, so
            # without this it reads as a work item that never ran a review.
            return True
    return False
