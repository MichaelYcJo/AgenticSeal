#!/usr/bin/env python3
"""SessionStart: a layout an earlier release wrote moves into the current one,
wherever the checked-out tree still holds it.

`moves` lists the units, each a `(kind, src, dst)` of repository-relative
paths: a root an earlier release wrote, its README opening with a heading in
`optin.EARLIER_HEADINGS`, has `seal/README.md` rewritten from the template so it opens
with `optin.MARKER`, and each 0.22.x work item under `seal/specs/<id>/` moves
into `seal/threads/<id>/`, each name at its thread path (`THREAD_PATHS`). In
local mode `local_moves` lists the same units under the git directory, and
they move by rename. At every session start, whether or not the tree has
anything left to move, each state file beside the root and each entry of
`~/.claude/specseal/` takes the plugin's name (`rename_state`): that state is
the clone's and the machine's, not the tree's, so a clone that pulls a tree
another person moved still holds its own. The 0.3.x layout is not a unit: no code of the
plugin opens its two directories, a top-level `specs/` may be another tool's,
and README.md *Coming up from 0.3.x* gives the commands that move it by hand
(`docs/one-root-by-lifetime.md`, "The plugin writes only to its own root").

Writing to a tree unasked is licensed on three grounds: the tree is the
plugin's own, every step is a staged `git mv` or a rewrite of a file git
already tracks, and `git diff --cached` shows the whole of it with the old
text safe in history. The notice ends "review the diff and commit" because
the write is the beginning of a review.

Boundaries, each pinned in `tests/test_root_migrate.py`:

  - **never over uncommitted work** — anything `git status --porcelain`
    reports under a directory a unit comes from, or a git that cannot answer,
    refuses the whole move with one line
  - **only what git tracks** — a unit's files come from `git ls-files`, so an
    ignored file under a source directory is not moved and stays where it is,
    and the directory may remain on disk holding nothing else
  - **on any branch** — no stamp stands between a branch and its move: every
    session start lists what the checked-out tree holds, so a branch cut
    before the move and checked out after it moves at its own session start.
    The move never puts a root into a tree, because every unit comes from a
    root `ours` accepts under the directory the branch itself carries. One
    limit, not guarded: in a repository that left shared mode for local mode,
    a branch cut before that switch has its own `seal/` moved and marked
    beside the local root, and the hooks read it first, as they read it
    before the rename. A second limit, not guarded: nothing reads where HEAD
    points, so a session start on a detached HEAD (a tag, an old commit, a
    bisect step, a rebase stopped on a conflict) or during a merge,
    cherry-pick or revert stages the move there as well, and the commit that
    operation makes carries it. A session in this plugin's flow starts on its
    work item's own branch, so the flow does not produce that shape
  - **a stopped move resumes** — a step that fails stops the run and prints
    what moved and what did not; the next session start moves what remains
  - **silent when there is nothing to do**
"""

# RIDER: this file is a reader of a layout an earlier release wrote, and of
# nothing the current layout holds. It can be deleted once no repository is
# left to migrate; `hooks/dispatch.py`'s session-start group is the one place
# that names it, and `optin.EARLIER_HEADINGS` with its readers goes with it.

import importlib.util
import json
import os
import posixpath
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import console
import optin

HOOKS = os.path.dirname(os.path.abspath(__file__))
# The directory under `~/.claude/` the plugin keeps its state in, under the
# name through 0.22.x and under the plugin's `name` since. Every session
# start merges the first into the second, entry by entry.
OLD_STATE_DIR = os.path.join(os.path.expanduser("~"), ".claude", "specseal")
STATE_DIR = os.path.join(os.path.expanduser("~"), ".claude", "agentic")
# The cache `hooks/version-check.py` rewrites once a day, which a session
# start of this release writes into `STATE_DIR` before this hook runs: where
# the new directory holds one, the old one is dropped rather than kept.
CACHE = "version-check"
TEMPLATE = os.path.join(HOOKS, "..", "templates", "seal-README.md")
# The `seal` command, whose `workflow_at` is the one reader that tells this
# plugin's pull-request workflow from anybody else's.
SEAL = os.path.join(HOOKS, "..", "skills", "implement", "scripts", "seal.py")

NEW = optin.HOME
# Where a work item stood through 0.22.x, under the root. A `seal/` whose
# README opens with neither `optin.MARKER` nor one of
# `optin.EARLIER_HEADINGS` is a project's own and is never read here.
EARLIER_ITEMS = f"{NEW}/specs"
README = f"{NEW}/{optin.README}"
# Where each name at the top of a 0.22.x work item stands in its thread; a
# name not listed (`routing.md`, `changelog.md`, `guarantee.md`, a `pr.*.md`)
# keeps its name at the thread's top.
THREAD_PATHS = {
    "spec.md": optin.DESIGN,
    "plan.md": optin.PLAN,
    "questions.md": optin.QUESTIONS,
    "overview.md": optin.GAPS,
    "broad-gate.md": optin.GATE,
    "phases": optin.PHASES,
    "rounds": optin.ROUNDS,
}
# The state files an earlier release wrote under the git directory, each
# renamed from `specseal-` to `agentic-` at session start.
OLD_PREFIX, NEW_PREFIX = "specseal-", "agentic-"
STATE_NAMES = (
    "scratch",
    "no-work-item",
    "leases",
    "planner",
    "implementer",
    "implementer-notice",
    "gate-failure",
    "mode-choice",
    "mode-retry",
    "review-choice",
    "worktree-choice",
    "worktree-consent",
    "stamp",
    "stamp-refused",
    "last-export.json",
)


class MoveError(Exception):
    """A unit that did not move. `resumable` says whether the next session
    start can pick it up unaided; a destination already holding the file, or
    a `seal` that is a file, needs a person first, and the line says so
    instead of promising a continuation that never comes."""

    def __init__(self, path, error, resumable=True):
        super().__init__(f"{path}: {error}")
        self.path = path
        self.error = error
        self.resumable = resumable


def under(root, rel):
    """The disk path of a `/`-joined repository-relative path."""
    return os.path.join(root, *rel.split("/"))


def git(root, *args):
    return subprocess.run(
        ["git", "-C", root, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    )


def sources(units):
    """The directories the units come from, each once and sorted: what
    `dirty` reads and what `run_moves` removes once the moves empty it."""
    return sorted({posixpath.dirname(src) for _, src, _ in units})


def dirty(root, units):
    """True when anything under a directory the units come from is
    uncommitted — or git cannot say. Work in progress outranks the move, and
    an unanswerable question is treated as work in progress: moving on a
    guess is the one direction this hook must never fail in.

    One shape is not work in progress: a staged rename or deletion with a
    clean worktree (`R ` and `D ` in porcelain's two columns). That is what
    a stopped run of this hook leaves behind, and a resume has to see past
    its own earlier steps or a stopped move can never finish. Anything with
    a worktree change, anything untracked, and anything staged as an
    addition or a modification still refuses.

    A `git ls-files` that cannot answer is the same case, because the units
    are what it lists, and it is refused here before a guess can move
    anything.
    """
    roots = sources(units)
    if any(tracked_names(root, rel) is None for rel in roots):
        return True
    try:
        r = git(root, "status", "--porcelain", "--", *roots)
    except (OSError, subprocess.SubprocessError):
        return True
    if r.returncode != 0:
        return True
    # exempt from splitlines: git output
    for line in r.stdout.splitlines():
        if len(line) < 2:
            continue
        x, y = line[0], line[1]
        if y != " " or x not in "RD":
            return True
    return False


def tracked_names(root, rel):
    """The top-level names git tracks under `rel`, sorted — or None when git
    cannot say.

    Every step of the move is a `git mv`, so a unit is what git tracks. An
    ignored file directly under a source directory (`.DS_Store` is macOS's
    default) passes `dirty()`, which reads porcelain, and then stops `git mv`
    for good: every session start met the same unit, and the tree stayed
    half-moved. Listing the directory was the defect; git's own list is the
    fix.
    """
    try:
        r = git(root, "ls-files", "-z", "--", rel)
    except (OSError, subprocess.SubprocessError):
        return None
    if r.returncode != 0:
        return None
    prefix = rel + "/"
    names = set()
    for path in r.stdout.split("\0"):
        if path.startswith(prefix):
            head = path[len(prefix) :].split("/", 1)[0]
            if head:
                names.add(head)
    return sorted(names)


def entries(root, rel):
    """What is under `rel` as units: git's list, or the directory listing when
    git cannot answer — `dirty()` reads as dirty then, so nothing moves."""
    names = tracked_names(root, rel)
    if names is not None:
        return names
    try:
        return sorted(os.listdir(under(root, rel)))
    except OSError:
        return []


def heading(base):
    """The first line of `base`'s `seal/README.md`, its end stripped, or None
    where it cannot be read."""
    try:
        with open(under(base, README), encoding="utf-8") as f:
            return f.readline().rstrip("\r\n")
    except (OSError, UnicodeDecodeError):
        return None


def ours(base):
    """True when `base`'s `seal/` is a root this plugin wrote: its README
    opens with the marker, or with the heading an earlier release wrote."""
    if os.path.islink(under(base, NEW)):
        return False
    return heading(base) in (optin.MARKER, *optin.EARLIER_HEADINGS)


def units_from(base, listing):
    """The units still to move under `base`, in the order they move, as
    (kind, src, dst): the README's rewrite first where it does not open
    with the marker, then every name at the top of each work item under
    `seal/specs/` into `seal/threads/<id>/` at its thread path. `listing`
    answers what is under a path: `entries` over what git tracks in shared
    mode, the directory in local mode."""
    if not ours(base):
        return []
    units = []
    if heading(base) != optin.MARKER:
        units.append(("readme", README, README))
    for item in listing(base, EARLIER_ITEMS):
        for name in listing(base, f"{EARLIER_ITEMS}/{item}"):
            new = THREAD_PATHS.get(name, name)
            units.append(
                (
                    "other",
                    f"{EARLIER_ITEMS}/{item}/{name}",
                    f"{NEW}/{optin.WORK_ITEMS}/{item}/{new}",
                )
            )
    return units


def moves(root):
    """The units still to move in shared mode, through `entries`.

    A `readme` unit is the template's text written over `seal/README.md`.
    The list is computed from what git tracks as it stands, which is what
    makes a stopped move resume: a unit that already moved is not there to
    be listed.
    """
    return units_from(root, entries)


def on_disk(base, rel):
    """What is under `rel` as names, sorted: a local root holds nothing git
    tracks, so its listing is the directory's."""
    path = under(base, rel)
    if not os.path.isdir(path) or os.path.islink(path):
        return []
    try:
        return sorted(os.listdir(path))
    except OSError:
        return []


def local_moves(common):
    """The units still to move under the local root, `<common>/seal/`."""
    return units_from(common, on_disk)


def local_move(common, src, dst):
    """`src` to `dst` under the git directory, a plain rename: nothing there
    is tracked, so there is nothing to stage."""
    if os.path.lexists(under(common, dst)):
        raise taken(src, dst)
    try:
        os.makedirs(os.path.dirname(under(common, dst)), exist_ok=True)
        os.rename(under(common, src), under(common, dst))
    except OSError as exc:
        raise MoveError(src, str(exc)) from exc


def git_mv(root, src, dst):
    """One staged rename. `git mv` does not create its destination's parent,
    and a `seal` that is a file makes creating it fail — inside the `try`,
    because an exception out of here ends the whole migration under the
    dispatcher, with nothing said until the turn ends (#28)."""
    parent = os.path.dirname(under(root, dst))
    try:
        os.makedirs(parent, exist_ok=True)
    except OSError as exc:
        raise MoveError(
            src, f"cannot create {os.path.dirname(dst)}/: {exc}", resumable=False
        ) from exc
    try:
        r = git(root, "mv", src, dst)
    except (OSError, subprocess.SubprocessError) as exc:
        raise MoveError(src, str(exc)) from exc
    if r.returncode != 0:
        raise MoveError(src, (r.stderr or r.stdout).strip() or f"exit {r.returncode}")


def taken(src, dst):
    """The error for a destination that already holds a file: `git mv` would
    say `destination exists` and the plain tail would promise a continuation
    that never comes, because the state does not change by itself."""
    return MoveError(
        src,
        f"{dst} already exists — keep one by hand: git rm {src} if {dst} is "
        f"the newer, or git rm {dst} to let the move bring the old one over",
        resumable=False,
    )


def move(root, src, dst):
    """`src` to `dst`, whole when nothing is at `dst` yet.

    When `dst` already exists — the state a stopped run leaves — a directory
    is moved file by file, in the order git lists them, because `git mv dir
    existing-dir` would put it INSIDE the destination. A file already at its
    destination is the person's to settle (a merge of a branch bootstrapped
    on the new layout leaves exactly that), and is named rather than tried.
    Then every directory under `src` that holds nothing when the walk reaches
    it is removed, the deepest first and `src` last, whichever run emptied
    it, unless its removal fails; one an ignored file holds stays, with every
    directory above it. Two limits, not guarded. A Windows junction placed
    under `src` by hand, which git does not track, is walked into, and the
    empty directories behind it are removed too. Where the removal of a
    directory fails, as on Windows when another process holds it open, that
    directory and every one above it stay, and nothing is removed by mistake.
    """
    if not os.path.isdir(under(root, src)):
        if os.path.exists(under(root, dst)):
            raise taken(src, dst)
        git_mv(root, src, dst)
        return
    if not os.path.exists(under(root, dst)):
        git_mv(root, src, dst)
        return
    r = git(root, "ls-files", "-z", "--", src)
    if r.returncode != 0:
        raise MoveError(src, (r.stderr or "").strip() or "git ls-files failed")
    for rel in sorted(p for p in r.stdout.split("\0") if p):
        target = dst + rel[len(src) :]
        if os.path.exists(under(root, target)):
            raise taken(rel, target)
        git_mv(root, rel, target)
    # Each directory is listed again when the walk reaches it. The lists
    # `os.walk` yields were read before the subdirectories below were
    # removed, so they still name them, and a directory that had held one
    # stayed on disk empty (#1016, #1018).
    for here, _, _ in os.walk(under(root, src), topdown=False):
        try:
            if not os.listdir(here):
                os.rmdir(here)
        except OSError:
            pass


def rewrite_readme(root, dst, stage=True):
    """A `readme` unit: the README becomes the template's text, staged in
    shared mode, so it opens with the marker.

    A template that cannot be read leaves the file as it was — a README
    describing the old layout is the state Q5 weighed, and it beats stopping
    the move for a file that is not the move.
    """
    try:
        with open(TEMPLATE, encoding="utf-8") as f:
            text = f.read()
        with open(under(root, dst), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        return
    if stage:
        git(root, "add", "--", dst)


def run_moves(root, units, local=False):
    """(units moved, the error that stopped the run or None). A `readme`
    unit whose source is its destination is a rewrite and nothing moves;
    any other `readme` unit moves first. `local` moves by rename under the
    git directory instead of by `git mv`."""
    done = 0
    for kind, src, dst in units:
        try:
            if src != dst:
                (local_move if local else move)(root, src, dst)
            if kind == "readme":
                rewrite_readme(root, dst, stage=not local)
        except MoveError as exc:
            return done, exc
        done += 1
    for old in sources(units):
        # The source directory, then each one above it that the moves left
        # empty, up to the root: `seal/specs/<id>/`, then `seal/specs/`.
        while old:
            path = under(root, old)
            # A link is never this cleanup's to remove. POSIX `rmdir` refuses
            # one with ENOTDIR; Windows' `RemoveDirectoryW` removes a
            # directory link itself, whatever is behind it, and deleted a
            # team's linked `specs/` from the working tree (PR #700's windows
            # leg, #688; contract rule 13).
            if os.path.islink(path) or old == NEW:
                break
            try:
                os.rmdir(path)
            except OSError:
                break  # something else is in it, or it is already gone
            old = posixpath.dirname(old)
    return done, None


def rename_state(root):
    """Each state file an earlier release wrote beside the root, under the
    git directory and the common one, and each entry of
    `~/.claude/specseal/`, renamed to the plugin's name where the new name
    is not taken. A `root` of "" (a session started outside a repository)
    merges only the directory under `~/.claude/`. Silent, safe to run at
    every session start, never over an entry already at its new name, and a
    rename that fails leaves the old file where it was."""
    places = set()
    if root:
        common = optin.git_common_dir(root)
        if common:
            places.add(common)
        try:
            r = git(root, "rev-parse", "--absolute-git-dir")
            if r.returncode == 0 and r.stdout.strip():
                places.add(r.stdout.strip())
        except (OSError, subprocess.SubprocessError):
            pass
    pairs = [
        (os.path.join(p, OLD_PREFIX + n), os.path.join(p, NEW_PREFIX + n))
        for p in sorted(places)
        for n in STATE_NAMES
    ]
    # `~/.claude/agentic/` may already stand: a session start of this release
    # writes `version-check` there before this hook runs. So the old
    # directory is merged, entry by entry, rather than renamed whole.
    pairs.extend(
        (os.path.join(OLD_STATE_DIR, n), os.path.join(STATE_DIR, n))
        for n in on_disk(OLD_STATE_DIR, ".")
    )
    if os.path.isdir(OLD_STATE_DIR):
        try:
            os.makedirs(STATE_DIR, exist_ok=True)
        except OSError:
            pass
    for old, new in pairs:
        if os.path.lexists(old) and not os.path.lexists(new):
            try:
                os.rename(old, new)
            except OSError:
                pass
    old_cache = os.path.join(OLD_STATE_DIR, CACHE)
    if os.path.isfile(old_cache) and os.path.lexists(os.path.join(STATE_DIR, CACHE)):
        try:
            os.remove(old_cache)
        except OSError:
            pass
    # Gone once every entry moved; any other entry the new directory already
    # held keeps the old directory, and that file, where they were.
    try:
        os.rmdir(OLD_STATE_DIR)
    except OSError:
        pass


def say(message):
    print(json.dumps({"systemMessage": message}))


def listed(dirs):
    """`a/` or `a/ and b/`, the way the notices name directories."""
    return " and ".join(f"{d}/" for d in dirs)


def origins(units):
    """What the notice names as moved: each unit's source directory cut to
    its first two names, once and sorted, so thirty work items under
    `seal/specs/` read as `seal/specs/`; a README rewritten in place moves
    nothing and is not named."""
    return sorted(
        {
            "/".join(posixpath.dirname(src).split("/")[:2])
            for _, src, dst in units
            if src != dst
        }
    )


def stale_workflow(root):
    """The path of the tree's pull-request workflow where a release before
    the rename wrote it, or "": `seal.py#workflow_at` reads it as this
    plugin's and its clone line names the repository's old name, so it runs
    a release that reads work items under `seal/specs/` and the old trailer,
    and after the move it examines nothing and passes. A `seal` command that
    will not load says "", and the line goes out without the tail."""
    try:
        spec = importlib.util.spec_from_file_location("agentic_seal_for_move", SEAL)
        seal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(seal)
        kind, text = seal.workflow_at(root)
    except (Exception, SystemExit):
        return ""
    return seal.WORKFLOW if kind == "plugin" and seal.PLUGIN_CLONE not in text else ""


def moved_line(units, tail):
    """The one line a finished move says, ending with TAIL."""
    if not origins(units):
        return f"agentic:wrote the marker into {README} {tail}"
    return f"agentic:moved {listed(origins(units))} into {NEW}/ {tail}"


def migrate_local(common):
    """The move under the local root: no git, so no dirty check and nothing
    staged; the line as in shared mode, and nothing said where nothing is
    left to move."""
    units = local_moves(common)
    if not units:
        return
    done, error = run_moves(common, units, local=True)
    if error is not None:
        say(
            f"agentic:moved {done} of {len(units)} into {NEW}/ under the git "
            f"directory and stopped at {error.path}: {error.error}. The next "
            "session start continues."
        )
        return
    say(moved_line(units, "under the git directory, where nothing is committed"))


def main():
    """Rename the state, move what the checked-out tree still holds, and say
    in one line what moved."""
    try:
        event = json.load(sys.stdin) or {}
        cwd = event.get("cwd")
    except (ValueError, AttributeError):
        return
    if not cwd or not os.path.isdir(cwd):
        return
    # NOT `optin.opted_in`: a layout still to move is one the gates may not
    # read as opted in, and a hook gated on the opt-in would never meet it.
    root = optin.repo_root(cwd)
    rename_state(root)
    if not root:
        return

    if ours(root) and os.path.islink(under(root, EARLIER_ITEMS)):
        # Git tracks the link as one blob, so it lists no work items behind
        # it: the README would be rewritten to open with the marker, so the
        # root would read as moved, and the files behind the link would never
        # move. Refused before anything else, every session start, until the
        # link is gone.
        say(
            f"agentic:{EARLIER_ITEMS}/ is a symbolic link, which git tracks as the "
            "link and not as its files — not moving it. Replace the link with "
            "the directory it points at, commit, and the next session start "
            f"moves it into {NEW}/{optin.WORK_ITEMS}/."
        )
        return

    units = moves(root)
    if not units:
        common = optin.git_common_dir(root)
        if common:
            migrate_local(common)
        return
    if dirty(root, units):
        say(
            f"agentic:the old layout under {listed(origins(units) or [NEW])} holds "
            "uncommitted changes — not touching work in progress. Commit, then "
            f"the next session start moves it into {NEW}/."
        )
        return

    done, error = run_moves(root, units)
    if error is not None:
        tail = (
            "The next session start continues."
            if error.resumable
            else "Settle that by hand, then the next session start continues."
        )
        say(
            f"agentic:moved {done} of {len(units)} into {NEW}/ and stopped at "
            f"{error.path}: {error.error}. {tail}"
        )
        return
    tail = "— review the diff and commit"
    workflow = stale_workflow(root)
    if workflow:
        tail += (
            ", and run `seal pr-checks install` with it: the workflow at "
            f"{workflow} clones a release before the rename, which reads work "
            f"items under {EARLIER_ITEMS}/, so after this move it examines "
            "nothing and passes every pull request"
        )
    say(moved_line(units, tail))


if __name__ == "__main__":
    console.to_utf8()
    main()
