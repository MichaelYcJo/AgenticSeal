"""Shared reader: which way did this work item say it was going?

The routing answer -- review chain or straight to the PR -- is given before the
first edit. Nothing used to receive it, so the commit gate re-derived it from
the absence of a review mark, and a mark only exists after a review passes.
Every commit of every round was stopped on its way to the reviewer the answer
had already named.

A declaration lives at `seal/threads/<work-item-id>/routing.md` and is committed.
Committed is the load-bearing part: the check moves to the pull request, and CI
sees only what is in the tree; nothing under the git directory travels there.

Beside the work item rather than at the root's top level, because a work item
begins and ends in one directory and routing is its first fact. It also gives
the work below the SDD ladder somewhere to exist: those items write no
`frame/design.md`, so until now they left no trace anywhere, and they are most of what
the gate sees.

Imported by the gate and by the hygiene check rather than copied into each --
the same reason `optin.py` gives for being a module: divergent copies is how
half of them keep the old answer.

Everything here fails toward "no declaration". A file that cannot be read is
not an answer somebody gave, so the gate goes back to asking. Silence would
make a corrupt file into the standing waiver
`docs/the-review-and-parity-arms.md` refuses to build.

Four of the rows are exceptions and none of them is a loophole. Nothing decides
a commit on `Implementation`, `Planning`, `Automation` or `Answer pressed` --
see `parse()` for why an absent or unreadable answer in any of them reads as
unanswered instead of taking the whole declaration down with it.
"""

import os
import re
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import optin

try:
    import blocks
except ImportError as missing:
    # `hooks/lib/config.py` raises the same sentence for the same reason: this is
    # a module gates and scripts import, and a script that loads it by path
    # (`chain_check.py`) catches the error or names the file first.
    raise ImportError(
        "cannot read "
        + os.path.join(os.path.dirname(os.path.abspath(__file__)), "blocks.py")
        + ", and it is the walk this reader reads routing.md through, which "
        "tells a live row from one quoted in a fence or parked in a comment. "
        "This file ships beside it under `hooks/`; a copy of one taken on its "
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
# The answer a declaration written before the plugin was renamed AgenticSeal
# carries for `BY_CRAFTER`, which the session-start move copies byte for byte;
# `parse` reads it as `BY_CRAFTER`, and the next minor release removes that
# reading, as it removes `chain_check.py#OLD_TRAILER`.
# exempt from old_names: the answer a declaration written before the rename carries
OLD_BY_CRAFTER = "smith"
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
# work item, and until now the answer was nowhere.
#
# `no` is not "a person did it by hand". It is "this run may stop to ask", which
# is the half a label cannot say and the half the measured instance got wrong.
#
# One gate reads it, and no commit is decided on it: `hooks/question-gate.py`
# refuses a question on the declared branch while it reads `yes`
# (`docs/the-review-record.md` *The run*).
AUTOMATION = "Automation"
AUTOMATION_YES = "yes"
AUTOMATION_NO = "no"
AUTOMATION_ANSWERS = (AUTOMATION_YES, AUTOMATION_NO)

# The sixth row: WHICH answer the person pressed, not what it derived to.
# Without it a chosen preset and four boxes somebody ticked by hand produce
# byte-identical files, which is #151's shape -- a `seal/` root somebody chose
# and one that appeared because a session followed a preset were the same
# bytes, and that is why `seal mode` writes a row saying a person was asked.
#
# `PRESSED_AUTOMATION` is the lower-case option LABEL a person pressed, where
# `AUTOMATION` above is the row name. One word deliberately: the answer pressed
# and the property recorded are the same idea seen from two sides, and a second
# word for one of them is what makes a reader hunt for the difference.
#
# Only two of question 1's three options ever reach this row. The third,
# `no work item`, opens no directory and writes no declaration at all, which is
# the hole `frame/design.md` names as a ticket of its own rather than closing here.
ANSWER_PRESSED = "Answer pressed"
PRESSED_AUTOMATION = "automation"
PRESSED_PER_AXIS = "per axis"
ANSWER_PRESSED_ANSWERS = (PRESSED_AUTOMATION, PRESSED_PER_AXIS)

# Repository-relative, `/`-joined, for the readers that classify paths as git
# prints them — `chain_check.py` lists a tree under it. The hooks below never
# join it under the root: they join `optin.WORK_ITEMS` under `optin.home_at`,
# so a root under the git directory (#80) is read by the same code.
WORK_ITEMS = f"{optin.HOME}/{optin.WORK_ITEMS}"
FILENAME = "routing.md"


def shown(lines, text=None):
    """[(index, line)] for each of LINES `table_rows` reads, ending removed.

    The walk's hidden lines are left out, and only those: where it is not
    sure, this reader's own reading from before #667 stands, and that
    reading hid nothing. So on every line the answer is either the old one
    or a renderer's, which `tests/test_the_hooks_hide_what_a_renderer_hides.py`
    holds over a generated corpus.

    TEXT is the file LINES were split from, and `table_rows` passes it: the
    walk reads it where GFM breaks a line, so a `<!--` after a U+2028 or a
    form feed, which `str.splitlines` breaks at, hides nothing a renderer
    shows (#667 round 1, 🟡 1; `hooks/lib/config.py#hidden_lines` says more).
    """
    walked = blocks.walk(lines) if text is None else blocks.walk_text(text)
    hidden = walked.hidden()
    return [
        (index, raw.rstrip("\r\n"))
        for index, raw in enumerate(lines)
        if index not in hidden
    ]


def table_rows(text):
    """Every two-cell markdown table row, as (label, value).

    Unknown labels are left in rather than filtered: a reader that drops what
    it does not recognise cannot gain a third axis later without the older
    readers silently ignoring it. The caller decides what it needs.

    The FOURTH axis arrived on that promise and is what tested it. `Planning`
    was added when seventy-two declarations had already been written, none of
    them carrying the row and none of them needing an edit -- and the only
    change this function needed was none.

    **A row a renderer does not show is not a row** (#658, #667). `parse`
    kept the LAST row of a label then, so an example quoted in a fenced block
    below the table answered for it, and so did an answer somebody parked in
    an HTML comment; since #867 a label shown twice has no value at all.
    `shown` below is what this walks, and it hides exactly the lines
    `hooks/lib/blocks.py` is sure a renderer hides: inside a fenced
    block or a comment block that begins its line, where either closes.
    Every other line is read as it always was, so a fence or a `<!--` nobody
    closed hides nothing, and a declaration that read before still reads.
    A file whose only table is hidden is not a declaration, the direction
    this module fails in.
    """
    rows = []
    # exempt from splitlines: lines the GFM walk numbers
    for _index, line in shown(text.splitlines(), text):
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        if set(cells[0]) <= set(":- "):  # the separator row
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
    required row would turn each of them back into an unanswered gate -- the
    review question would be asked again on branches whose answer is committed
    in the tree. The strict spelling below is deliberate for the first two,
    because a wrong answer there decides whether a reviewer sees the work. The
    only reader of these two is `hooks/implementer-notice.py`, which prints one
    line after a commit where a declared agent left no mark, and decides
    nothing -- so a wrong answer here is recorded and at most reminded about,
    where a wrong answer above stops a commit. That is why the rows are
    optional rather than lenient, and it is also the asymmetry to know about: a
    backticked or capitalised answer is rejected loudly in the first two,
    because the gate goes back to asking, and silently here.
    `templates/records/sdd-routing.md` is the only spelling a
    session should copy, and a test parses that file so it cannot drift.

    The two optional rows are read independently of each other. One answered
    and one absent is a common state -- a session that framed the work itself
    and spawned `crafter` to build it -- so neither may stand in for the other.

    `Automation` and `Answer pressed` are the fifth and sixth rows and they are
    read on the same looser terms, for the same reason one step further along:
    nothing decides a commit on either, and the one reader of `Automation`,
    `hooks/question-gate.py`, only refuses a question, so an absent or
    unreadable row leaves the run attended. A required row would turn all 84
    declarations already committed here into "not a declaration", which
    turns the edit gate's refusal back on for every branch that already
    answered.

    **What it reads is `table_rows`', which skips a row a renderer does not
    show** (#667): a table wholly inside a fenced block, or inside a comment
    block that closes, is no declaration, and the gate asks as it does for
    any `routing.md` that does not parse. A fence or a `<!--` nobody closed
    above the table is not a block at all, so that declaration still reads.

    **A label written twice has no value** (#867), the rule
    `hooks/lib/config.py#value_of` gives every `seal/config.md` row. This used to
    keep the LAST row of a label, so a second `Review` row below the first
    answered for it, and nothing said there were two. Now a strict label
    doubled -- `Review`, `Destination`, `Branch` -- makes the file no
    declaration, and the gate asks as it does for any file that will not
    parse; an optional label doubled is unanswered, on the terms above.
    Measured when the rule landed: none of the 86 committed declarations
    writes a label twice.
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
    if implementation == OLD_BY_CRAFTER:
        implementation = BY_CRAFTER
    planning = found.get(PLANNING)
    automation = found.get(AUTOMATION)
    pressed = found.get(ANSWER_PRESSED)
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
        # unchecked half is a VALUE rather than an absence (#151).
        "automation": automation if automation in AUTOMATION_ANSWERS else None,
        "pressed": pressed if pressed in ANSWER_PRESSED_ANSWERS else None,
    }


def current_branch(cwd):
    """The checked-out branch, or "" when detached or unreadable.

    A detached HEAD matches no declaration, so the gate asks. That is the
    correct direction: nothing on a detached HEAD is the work item a branch
    was declared for.
    """
    try:
        out = subprocess.run(
            ["git", "-C", cwd or ".", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    name = out.stdout.strip() if out.returncode == 0 else ""
    return "" if name == "HEAD" else name


def rebase_branch(cwd):
    """The branch a paused rebase in CWD's worktree names, or "".

    `rebase-merge/head-name`, else `rebase-apply/head-name`, under the
    worktree's own git directory: HEAD is detached while the rebase waits on
    a conflict, and the branch it names is the one the work is on.
    """
    try:
        out = subprocess.run(
            ["git", "-C", cwd or ".", "rev-parse", "--absolute-git-dir"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    git_dir = out.stdout.strip() if out.returncode == 0 else ""
    if not git_dir:
        return ""
    for state in ("rebase-merge", "rebase-apply"):
        try:
            with open(os.path.join(git_dir, state, "head-name"), encoding="utf-8") as f:
                name = f.read().strip()
        except (OSError, UnicodeDecodeError):
            continue
        prefix = "refs/heads/"
        return name[len(prefix) :] if name.startswith(prefix) else ""
    return ""


def unborn_branch(cwd):
    """The branch HEAD names before its first commit, or "" where HEAD is
    detached or git cannot answer. `rev-parse --abbrev-ref HEAD` fails on a
    branch with no commit; `symbolic-ref` reads the name HEAD points at
    without resolving it to a commit, and exits 1 on a detached HEAD."""
    try:
        out = subprocess.run(
            ["git", "-C", cwd or ".", "symbolic-ref", "-q", "--short", "HEAD"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout.strip() if out.returncode == 0 else ""


def worktree_branch(cwd):
    """The branch CWD's worktree is on: the one checked out, the one HEAD
    names before its first commit, else the one a paused rebase there names,
    or "" where none names one. The edit gate and `seal no-work-item` both
    resolve the branch here, so the record names the branch the gate reads.
    `unborn_branch` runs only where `current_branch` found none, so a branch
    with a commit costs no second `git` call."""
    return current_branch(cwd) or unborn_branch(cwd) or rebase_branch(cwd)


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
        try:
            with open(path, encoding="utf-8") as f:
                parsed = parse(f.read())
        except (OSError, UnicodeDecodeError):
            # `UnicodeDecodeError` is a `ValueError`, not an `OSError`, and it
            # is named rather than its parent: `parse()` is pure string work
            # today, so a `ValueError` reaching here later would be a defect in
            # it, and swallowing that as "no declaration" is how a gate goes
            # quiet for a reason nobody wrote down. A
            # declaration that is not valid UTF-8 used to raise out of
            # `declarations()` -> the gate that read it -> `dispatch.py`'s
            # `except Exception: return ""`, which is no output, which the
            # harness reads as approval. The module docstring says everything
            # here fails toward "no declaration"; a file nobody can decode is
            # not an answer somebody gave, so it is skipped and the gate goes
            # back to asking. `chain_check.py` already catches both when it
            # reads the event payload -- the CI half was hardened and this one
            # was not.
            continue
        if parsed:
            out.append((path, parsed))
    return out


def for_branch(root, branch):
    """The one declaration that applies here, or None.

    Two declarations naming the same branch is not an answer, so it reads as
    none. Declarations accumulate over a repository's life and a branch-less
    match would let the first work item ever declared silence the gate for
    every commit after it.
    """
    if not root or not branch:
        return None
    matching = [d for _, d in declarations(root) if d["branch"] == branch]
    return matching[0] if len(matching) == 1 else None


def declared(cwd, root):
    """The routing answer in force for `cwd`, or None when there is not one.
    The branch is resolved as the edit gate resolves it (`worktree_branch`),
    so a branch with no commit yet and a paused rebase read the declaration
    that names them."""
    return for_branch(root, worktree_branch(cwd))


# The record that a session's change belongs to no work item: a file per
# session under the common git directory, holding one branch name per line,
# UTF-8, each line ending in a newline. `seal no-work-item` adds the branch it
# ran on, and `hooks/routing-edit-gate.py` lets the session's edits through on
# a branch a line names and on no other. The rule is
# `docs/the-routing-check.md` *The edit check*.
NO_WORK_ITEM = "agentic-no-work-item"
# A record older than this is pruned when one is written, as a lease is.
NO_WORK_ITEM_AGE = 86400


def session_name(session):
    """SESSION's id as a file name, or "" where it cannot be one. The id is
    reduced to its basename, so a separator in it cannot name a file
    elsewhere."""
    name = os.path.basename(str(session or "").strip())
    return "" if name in ("", ".", "..") else name


def no_work_item_path(common, session):
    """`<common>/agentic-no-work-item/<session>`, or "" where either is
    missing."""
    name = session_name(session)
    if not common or not name:
        return ""
    return os.path.join(common, NO_WORK_ITEM, name)


def no_work_item_branches(path):
    """The branches the record at PATH names, one per line. A record that
    cannot be read names none. The lines are split at `\\n` alone, so no
    other character a branch name may hold ends one."""
    try:
        with open(path, encoding="utf-8", newline="") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError):
        return []
    return [line for line in text.split("\n") if line]


def no_work_item(common, session, branch):
    """Whether SESSION recorded, in the clone whose common git directory is
    COMMON, that its change on BRANCH belongs to no work item: true only
    where a line of its record equals BRANCH. No branch is never recorded."""
    path = no_work_item_path(common, session)
    return bool(path and branch) and branch in no_work_item_branches(path)


def record_no_work_item(common, session, branch, now=None):
    """Add BRANCH to SESSION's record under COMMON, where it does not name it
    yet, and prune the stale records; the record's path, or "" where nothing
    could be written. No branch writes nothing. The record is rewritten on
    every run, so a run on a branch it already names keeps it from the
    prune."""
    path = no_work_item_path(common, session)
    if not path or not branch:
        return ""
    branches = no_work_item_branches(path)
    if branch not in branches:
        branches.append(branch)
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write("".join(f"{name}\n" for name in branches))
    except OSError:
        return ""
    cutoff = (now if now is not None else time.time()) - NO_WORK_ITEM_AGE
    where = os.path.dirname(path)
    for name in os.listdir(where):
        stale = os.path.join(where, name)
        try:
            if stale != path and os.stat(stale).st_mtime < cutoff:
                os.unlink(stale)
        except OSError:
            pass
    return path


def item_dir(root, branch):
    """The work-item directory the declaration for `branch` lives in, or "".

    This is what makes a review round writable before a pull request exists.
    The round records live two levels down, in `trail/rounds/`, so whatever resolves
    the declaration resolves them too, and the branch is the only key
    available at the moment a round closes.

    Two declarations naming one branch resolve to nothing here for the same
    reason they do in `for_branch`: not an answer.
    """
    if not root or not branch:
        return ""
    matching = [path for path, d in declarations(root) if d["branch"] == branch]
    return os.path.dirname(matching[0]) if len(matching) == 1 else ""


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
    except NotADirectoryError:
        # A `rounds` that is a FILE, not a directory. Round 1 reached it by
        # following an earlier release's own migration command: a `git mv` of
        # each round record into a `rounds` directory fails because `git mv`
        # does not create its destination, and dropping the trailing slash is what a
        # person tries next -- which succeeds for a single record and renames
        # it to a file called `rounds`. Both readers then said the work item
        # held no round record while git carried the review's whole text, and
        # a review reported as never having happened is the one direction this
        # module refuses. Raised so a caller says which of the two it is.
        raise
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
    is the one member of the SDD set that is plural and unbounded: six
    records beside six other files was the worst case here, and the structure
    should say which member grows.

    The old flat location is NOT read, and `stray_rounds` exists so a caller
    can say so out loud. A permanent dual read would put two places to look in
    the reader four gates depend on, and an expiry nothing enforces is a
    comment -- so what replaces the fallback is a message naming the file and
    the destination.

    What stays different between the two readers is deliberate, and it is not
    the order: this one reads the working tree, because a hook fires before
    the commit and an uncommitted round record is exactly what it should see.
    The pull-request check reads what git carries, because CI sees nothing
    else -- an untracked file there is evidence nobody can open.
    """
    if not item:
        return []
    try:
        return _ordered(os.path.join(item, ROUNDS_DIR))
    except NotADirectoryError:
        # Caught here rather than raised at the gates. A hook that raises is
        # rendered as an allow by `hooks/dispatch.py` for the call it raised
        # on, and said only at the end of the turn, as a gate that failed
        # (#28). Propagating this would turn a nameable state into that --
        # the opposite of what `_ordered` refuses it for.
        # `rounds_unreadable` is how a caller asks which of the two happened.
        return []


def rounds_unreadable(item):
    """True when `rounds` exists beside the work item and is not a directory.

    Told apart from "no records" because the two need opposite answers: one
    is 28 of this repository's 35 work items and must stay quiet, the other
    is a review whose whole text git is still carrying while every reader
    reports that none happened.

    Reached by following an earlier release's own migration command. A
    `git mv` of each round record into a `rounds` directory fails -- `git mv`
    does not create its destination -- and dropping the trailing slash succeeds for a single
    record, renaming it to a file named `rounds`.
    """
    if not item:
        return False
    where = os.path.join(item, ROUNDS_DIR)
    if os.path.islink(where):
        # ANY link, including one that resolves to a directory holding
        # records. `os.path.exists` follows links, so the first version
        # returned False for a broken one; the second still followed a live
        # one into the directory and stayed quiet while the pull-request
        # check — which sees git's `120000` and calls it not-a-tree — failed
        # and told the reader to `mkdir` a path that already exists. The two
        # readers answer for what GIT carries, and git carries a link.
        # Round 4's fourth shape, after three were enumerated.
        return True
    if os.path.exists(where) and not os.path.isdir(where):
        return True
    if os.path.isdir(where):
        try:
            os.listdir(where)
        except OSError:
            # A directory nothing can list. `_ordered` returns [] for it, so
            # without this it reads as a work item that never ran a review.
            return True
    return False


def stray_rounds(item):
    """`round-N.md` left at the work item's own directory, lowest round first.

    These are records nothing reads. `rounds()` looks one level down and a
    reader that merely found nothing would report the same silence as a work
    item that never ran a review -- the state 28 of this repository's 35 work
    items are in, and the state that must stay quiet. The difference between
    "no review happened" and "the review is in a place nobody reads" is the
    whole reason this function is separate from the one above.
    """
    if not item:
        return []
    return _ordered(item)
