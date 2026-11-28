"""Shared opt-in: does this repository run the IADD process?

Imported by the gates rather than copied into each, because where the answer
moves, divergent copies are how half of them keep the old one.

The signal is `agentory/` — the root the plugin maintains, whose existence is the
declaration — at the first of two places that has it with its `README.md`
opening with `MARKER`: `<repo>/agentory/`, which shared mode commits, then
`<git-common-dir>/agentory/`, where local mode keeps it. One root, read one
way, and no config key (`docs/layout/one-root-by-lifetime.md`, "The opt-in signal
is the root itself"). An `agentory/` without the marker is a directory the project
keeps for itself, as a package named `agentory` does, and declares nothing; the
root of such a repository is the local one.

`<git-common-dir>/agentic-scratch` takes that declaration back. A repository
that exists for thirty seconds — a fixture built by hand to reproduce a gate
decision, which is what developing these gates consists of — carries the same
`agentory/` as a repository under review, and the gates cannot tell them apart:
every probe would stop for a prompt about a repository that is deleted
before the answer means anything. The opt-out file is written once, by a
person, in the repository being thrown away. It lives under the git directory
rather than inside the root because the root is committed: a file committed
in the root would silence every gate in every clone with nothing in the diff
that read as the IADD process being switched off. Nothing under
`.git/` can be committed, and a linked worktree shares the common directory,
so it shares the opt-out. `agentory/README.md` says so too.

Everything here fails toward "not opted in": a gate that cannot tell should do
nothing rather than act on a guess. `toplevel` alone raises where git did not
answer, for a caller that must tell that apart from no repository, and
`repo_root` is `toplevel` read toward "not opted in". Each git command here is
started by `lib/gitcmd.py#git`.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gitcmd

HOME = "agentory"
# The sub-directory of the root that holds the work items.
WORK_ITEMS = "threads"
# Where each record sits in a thread, `/`-joined and relative to the thread's
# directory: `frame/` holds the design before the build, `trail/` what passed
# between the parties, and the files at the top speak for the whole
# thread (`docs/layout/the-record-layout.md`). Every reader of a thread's file joins
# one of these under the thread.
FRAME = "frame"
TRAIL = "trail"
DESIGN = f"{FRAME}/design.md"
PLAN = f"{FRAME}/plan.md"
QUESTIONS = f"{FRAME}/questions.md"
# A keep file of phase N, `frame/keep-<N>.txt` or `frame/keep-<N>-paths.txt`,
# matched whole against a path relative to the thread's directory
# (`skills/verify/SKILL.md` *An absence claim is only as good as the search
# behind it*).
KEEP = re.compile(rf"{FRAME}/keep-[0-9]+(?:-paths)?\.txt")
PHASES = f"{TRAIL}/phases"
ROUNDS = f"{TRAIL}/rounds"
GATE = f"{TRAIL}/gate.md"
GAPS = "gaps.md"
INSPECTION = "inspection.md"
CHANGELOG = "changelog.md"
# The work item's own file of the pull request body's first part, which
# `agentic pr-body` writes above the copy of the records, after the work item's
# `pr.<lang>.md` where the two language keys differ.
PR = "pr.md"
# The migration config, directly under the root: `chain_check.py` reads it at
# HEAD under the shared root.
PARITY_CONFIG = "parity.json"
# An empty FILE under the common git directory; its existence is the whole
# signal, read the way the root is read. It is not an entry inside an existing
# file because every gate would then parse one to answer what is a directory
# test. A directory of this name is not the opt-out — see `opted_out()` below.
SCRATCH = "agentic-scratch"
# The first line of `templates/setup/agentory-README.md`, which first setup writes
# into every root: an `agentory/` is the plugin's root only where its `README.md`
# opens with this line. `tests/lib/test_optin.py` pins the template's first
# line to this value.
MARKER = "# What IADD keeps in agentory/"
README = "README.md"


def toplevel(cwd):
    """The repository root containing cwd, or "" when there is none.

    `lib/gitcmd.py#Failed` where git did not answer, for a caller that must
    tell a git that did not answer from a directory outside any
    repository."""
    if not cwd or not os.path.isdir(cwd):
        return ""
    # `or ""`: a process whose reader thread died while decoding returns
    # with `stdout` None, and `.strip()` would then raise `AttributeError`,
    # where this module fails toward "not opted in". `lib/gitcmd.py#_start`
    # names the encoding so that the decode does not fail; the None is still
    # read here.
    out = (gitcmd.git(cwd, "rev-parse", "--show-toplevel").stdout or "").strip()
    # Spelled the way this platform spells a path, because that is what every
    # caller does with it: `os.path.join` below, and the gates print it to
    # someone who has to recognise their own repository in it. git answers
    # with forward slashes on every platform, so on Windows the root would
    # arrive in one dialect and be joined in another -- `C:/proj` and then
    # `C:/proj\agentory\parity.json`. Both halves work; neither
    # equals a path the caller built, and the address is the whole point of a
    # module named for having ONE.
    #
    # A no-op where the two dialects already agree, so nothing about the POSIX
    # path changes and `normpath` is not asked to guess anything: git has
    # already resolved this to an absolute, existing directory.
    return os.path.normpath(out) if out else ""


def repo_root(cwd):
    """The repository root containing cwd, or "" when there is none or git
    did not answer: `toplevel` read toward "not opted in"."""
    try:
        return toplevel(cwd)
    except gitcmd.Failed:
        return ""


def git_common_dir(root):
    """The common git directory of the repository at `root`, or "".

    `.git` at the toplevel, when it is a directory, IS the repository's git
    directory, and for a main worktree the common directory is that same
    place — so that case is answered without a process. Every gated command
    in every opted-in repository reaches this through `home_at()`, so a
    `git` process started here is paid on every gated command. A `.git`
    that is a file (a linked worktree, a submodule) or absent is asked of git,
    which answers relative to the directory it ran in unless the path is
    absolute; `os.path.join` handles both spellings.
    """
    if not root:
        return ""
    dotgit = os.path.join(root, ".git")
    if os.path.isdir(dotgit):
        return dotgit
    try:
        out = gitcmd.git(root, "rev-parse", "--git-common-dir").stdout
    except gitcmd.Failed:
        return ""
    out = (out or "").strip()
    return os.path.normpath(os.path.join(root, out)) if out else ""


def home_paths(root, common=None):
    """The two places `agentory/` is read from at `root`, shared first then local.

    `("", "")` for no root, and the local entry is "" where the common git
    directory could not be resolved. The shared entry is `<root>/agentory` and
    the local entry `<common>/agentory`. Neither entry is tested for being the
    root: this answers *where would it be*, and `home_at` below answers
    *where is it*.

    It exists because the second question is not the only one asked. `agentic
    import` has to be able to create the root the user names — including the
    mode this repository is not in — and a caller that spelled
    `os.path.join(root, "agentory")` for itself would hold a second answer to the
    question this module is named for having ONE of. The order is part of
    that answer and lives here with it.

    `common` is passed by a caller that has already resolved the common git
    directory, so nothing here costs a second `git` call, which every gated
    command would pay.
    """
    if not root:
        return ("", "")
    if common is None:
        common = git_common_dir(root)
    # `normpath` on the git-derived half, and it is not tidying. `git
    # rev-parse --git-common-dir` answers with `/` on Windows as well, so
    # joining `agentory` onto it would produce `C:/Users/x/repo\.git\agentory` -- one
    # path spelled two ways, printed to a person in the gate's question and
    # in chain-check's local-mode sentence. Nothing here hands `home` to
    # git, so the native spelling is the right one, and normalising at the
    # source closes it for every caller rather than at each of the four
    # places that print it.
    return (
        os.path.join(root, HOME),
        os.path.normpath(os.path.join(common, HOME)) if common else "",
    )


def home_name(root, common=None):
    """`HOME`, the `/`-joined repository-relative name of the root in force
    at `root`, where that root is the shared one; "" where the root is local
    or there is none.

    For a reader that has to tell a root in the tree from a root under the
    git directory, which a path on this disk does not say by itself.
    """
    found = home_at(root, common)
    return HOME if found and found == os.path.join(root, HOME) else ""


def _first_line(path):
    """The first line of the file at `path`, bounded at the marker's length
    and the two characters a line end can take, or None where it cannot be
    read: absent, a directory, or no file at all."""
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.readline(len(MARKER) + 2)
    except OSError:
        return None


def _opens_with_marker(text):
    """True where TEXT's first line, its line end taken off, is `MARKER`;
    False for None."""
    if text is None:
        return False
    return text.split("\n", 1)[0].rstrip("\r") == MARKER


def marked(path):
    """True where `<path>/README.md` opens with `MARKER`.

    The first line is compared with its line end stripped, and nothing past
    it is read: the read is bounded at the marker's length and the two
    characters a line end can take, because every gated command pays for it,
    and a longer first line is not the marker anyway. A file that is absent
    or is a directory is not the marker, and neither is a first line that
    does not decode: `errors="replace"` turns its bytes into a character the
    marker does not hold, where a strict decode would also refuse a marked
    file for a stray byte further down the same buffered chunk. An empty
    path is no root: joined, it would name the README of whatever directory
    the process stands in.
    """
    if not path:
        return False
    return _opens_with_marker(_first_line(os.path.join(path, README)))


def home_at(root, common=None):
    """The `agentory/` of the repository at `root`, or "" — for a caller that has
    already resolved the root and should not pay for a second `git` call.

    The places are read in order, `<root>/agentory/`, then
    `<git-common-dir>/agentory/`, the two entries of `home_paths` above, and the
    first that is a directory whose `README.md` opens with `MARKER` is the
    answer; nothing else is read. A `<root>/agentory/` without the marker is
    passed over, so a project that keeps a directory of that name for itself
    keeps its root under the git directory, in local mode. The opt-out is
    read once, here, so it cannot be honoured by one arm of a gate and
    missed by the other — the
    migration config sits inside the root the opt-out takes back, and a
    repository nobody reviews has nothing to compare against an original
    either.

    `common` is passed by a caller that needs the common git directory for
    something else too, so one invocation asks git for it once rather than
    once per unit that wants it — the same parameter, for the same reason, as
    `home_paths` above. From a linked worktree, where `.git` is a file and
    the fast path below does not apply, a gate that resolves the root, the
    opt-in and its own marker separately runs the same `rev-parse
    --git-common-dir` three times on every Bash call.
    """
    if not root:
        return ""
    # One `git_common_dir` call: the opt-out below needs the common directory
    # even when the shared root is the answer, so no path skips it, and asking
    # once is what lets the two places be produced in one place.
    if common is None:
        common = git_common_dir(root)
    if opted_out(common):
        return ""
    return marked_home(root, common)


def opted_out(common):
    """True where COMMON, the common git directory, is not empty and the
    file `SCRATCH` stands under it: the one test of the opt-out, which
    `home_at` reads and a command asks to tell an opt-out from no root.

    A FILE, which is what this module and `agentory/README.md` both say the
    signal is. `os.path.exists` would also accept a DIRECTORY of that name,
    so a directory created where the opt-out goes would turn every gate off
    with nothing in the diff that reads as the IADD process being
    switched off. An empty COMMON names no opt-out: joined, it would name a
    file wherever the process stands."""
    return bool(common) and os.path.isfile(os.path.join(common, SCRATCH))


def marked_home(root, common=None):
    """The first of `home_paths(root, common)` that is a directory whose
    `README.md` opens with `MARKER`, or "": `home_at` without the opt-out,
    for the one reader that runs in a throwaway repository too,
    `broad_gate.py#agentory_home`."""
    for found in home_paths(root, common):
        if found and os.path.isdir(found) and marked(found):
            return found
    return ""


def home(cwd):
    """This repository's `agentory/`, or "" when it does not run the IADD
    process."""
    return home_at(repo_root(cwd))


def opted_in(cwd):
    """True when this repository runs the IADD process."""
    return bool(home(cwd))
