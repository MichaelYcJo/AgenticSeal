"""Shared opt-in: does this repository run the AgenticSeal workflow?

Imported by the gates rather than copied into each, because the answer moved
once already and four divergent copies is how half of them keep the old answer.

The signal is `seal/` — the root the plugin maintains, whose existence is the
declaration — at the first of two places that has it with its `README.md`
opening with `MARKER`: `<repo>/seal/`, which shared mode commits, then
`<git-common-dir>/seal/`, where local mode keeps it (#80). One root, read one
way, and no config key (`docs/one-root-by-lifetime.md`, "The opt-in signal
is the root itself"). A `seal/` without the marker is a directory the project
keeps for itself, as a package named `seal` does, and declares nothing,
except one whose README opens with one of `EARLIER_HEADINGS`: an earlier
release's root, waiting for its move, which declares nothing either.

`<git-common-dir>/agentic-scratch` takes that declaration back. A repository
that exists for thirty seconds — a fixture built by hand to reproduce a gate
decision, which is what developing these gates consists of — carries the same
`seal/` as a repository under review, and the gates cannot tell them apart:
every probe stopped for a prompt about a repository that would be deleted
before the answer meant anything. The opt-out file is written once, by a
person, in the repository being thrown away. It lives under the git directory
rather than inside the root because the root is committed: a file committed
in the root would silence every gate in every clone with nothing in the diff
that read as the workflow being switched off. Nothing under `.git/` can be
committed, and a linked worktree shares the common directory, so it shares
the opt-out. `seal/README.md` says so too.

Everything here fails toward "not opted in": a gate that cannot tell should do
nothing rather than act on a guess.
"""

import os
import subprocess

HOME = "seal"
# The sub-directory of the root that holds the work items. Readers that
# classify repository-relative paths — `hooks/gate.py#DOC_ROOTS`, the CI
# scripts' globs, `chain_check.py`'s prefix — spell `seal/` as a string,
# because a path in a diff or a tree listing is only ever the shared root;
# every hook that opens a file joins this under `home()` instead, so #80
# changes where the folder is created and nothing that reads it.
WORK_ITEMS = "threads"
# Where each record sits in a thread, `/`-joined and relative to the thread's
# directory: `frame/` holds the design before the build, `trail/` what passed
# between the parties, and the four files at the top speak for the whole
# thread (`docs/the-record-layout.md`). Every reader of a thread's file joins
# one of these under the thread, and the migration moves a 0.22.x work item's
# files to them.
FRAME = "frame"
TRAIL = "trail"
DESIGN = f"{FRAME}/design.md"
PLAN = f"{FRAME}/plan.md"
QUESTIONS = f"{FRAME}/questions.md"
PHASES = f"{TRAIL}/phases"
ROUNDS = f"{TRAIL}/rounds"
GATE = f"{TRAIL}/gate.md"
GAPS = "gaps.md"
GUARANTEE = "guarantee.md"
CHANGELOG = "changelog.md"
# The migration config, directly under the root: `parity_config` below opens
# it, and `chain_check.py` reads it at HEAD under the shared root (#988).
PARITY_CONFIG = "parity.md"
# An empty FILE under the common git directory; its existence is the whole
# signal, read the way the root is read. It is not an entry inside an existing
# file because every gate would then parse one to answer what is a directory
# test. A directory of this name is not the opt-out — see `home_at()` below.
SCRATCH = "agentic-scratch"
# The first line of `templates/setup/seal-README.md`, which first setup and the
# migration write into every root: a `seal/` is the plugin's root only where
# its `README.md` opens with this line. `tests/test_optin.py` pins the
# template's first line to this value.
MARKER = "# What AgenticSeal maintains in seal/"
# The first line `templates/setup/seal-README.md` opened with in the releases before
# the rename. A `seal/` whose README opens with one is an earlier release's
# root, waiting for the move `hooks/root-migrate.py` makes at session start:
# not opted in until then, and not a project's own directory either, so no
# reader puts a second root beside it (`earlier`). It leaves with the
# migration, once no repository is left to move.
EARLIER_HEADINGS = (
    "# What this plugin maintains in seal/",
    "# seal/ — what this plugin maintains",
)
README = "README.md"


def repo_root(cwd):
    """The repository root containing cwd, or "" when there is none."""
    # RIDER: every caller of this module resolves the root again. Counted with
    # a logging `git` on PATH: one gated command costs five `git` calls per
    # target and three of them are `rev-parse --show-toplevel` -- the commit
    # gate's own `root_of`, then `opted_in` and `parity_config` below. Fixing
    # it means passing the root in or memoising here, and three gates import
    # this module, so it is a change to all of them at once.
    if not cwd or not os.path.isdir(cwd):
        return ""
    try:
        out = subprocess.run(
            ["git", "-C", cwd, "rev-parse", "--show-toplevel"],
            capture_output=True,
            # Named, and the `.stdout or ""` below is the second half of the
            # same defect. `text=True` alone decodes with whatever locale the
            # parent had; git answers UTF-8, so a repository under a path this
            # locale cannot decode kills subprocess's reader thread -- and that
            # exception DOES NOT PROPAGATE. The call returns with `stdout` set
            # to None, and `.strip()` then raised `AttributeError`, which is
            # neither of the classes caught here.
            #
            # Measured on a cp949 console against a repository under a Korean
            # path: the gate exited 1 with no decision, and a PreToolUse hook
            # exiting non-zero is a non-blocking error -- so the commit went
            # through unjudged. Everything in this module is documented to fail
            # toward "not opted in", and that is silence, not a crash.
            encoding="utf-8",
            errors="replace",
            timeout=5,
        ).stdout
    except (OSError, subprocess.SubprocessError):
        return ""
    out = (out or "").strip()
    # Spelled the way this platform spells a path, because that is what every
    # caller does with it: `os.path.join` below, and the gates print it to
    # someone who has to recognise their own repository in it. git answers
    # with forward slashes on every platform, so on Windows the root arrived
    # in one dialect and was joined in another -- `C:/proj` and then
    # `C:/proj\seal\parity.md`. Both halves work; neither
    # equals a path the caller built, and the address is the whole point of a
    # module named for having ONE.
    #
    # A no-op where the two dialects already agree, so nothing about the POSIX
    # path changes and `normpath` is not asked to guess anything: git has
    # already resolved this to an absolute, existing directory.
    return os.path.normpath(out) if out else ""


def git_common_dir(root):
    """The common git directory of the repository at `root`, or "".

    `.git` at the toplevel, when it is a directory, IS the repository's git
    directory, and for a main worktree the common directory is that same
    place — so that case is answered without a process. Every gated command
    in every opted-in repository reaches this through `home_at()`, and the
    rider on `repo_root` counts what one more `git` per call costs. A `.git`
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
        out = subprocess.run(
            ["git", "-C", root, "rev-parse", "--git-common-dir"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        ).stdout
    except (OSError, subprocess.SubprocessError):
        return ""
    out = (out or "").strip()
    return os.path.normpath(os.path.join(root, out)) if out else ""


def home_paths(root, common=None):
    """The two places `seal/` is read from at `root`, shared first then local.

    `("", "")` for no root, and the local entry is "" where the common git
    directory could not be resolved. Neither is tested for existence: this
    answers *where would it be*, and `home_at` below answers *where is it*.

    It exists because the second question is not the only one asked. `seal
    import` has to be able to create the root the user names — including the
    mode this repository is not in — and a caller that spelled
    `os.path.join(root, "seal")` for itself would hold a second answer to the
    question this module is named for having ONE of. The order is part of
    that answer and lives here with it.

    `common` is passed by a caller that has already resolved the common git
    directory, so nothing here costs a second `git` call; the rider on
    `repo_root` counts what one more per gated command is worth.
    """
    if not root:
        return ("", "")
    if common is None:
        common = git_common_dir(root)
    # `normpath` on the git-derived half, and it is not tidying. `git
    # rev-parse --git-common-dir` answers with `/` on Windows as well, so
    # joining `seal` onto it produced `C:/Users/x/repo\.git\seal` -- one
    # path spelled two ways, printed to a person in the gate's question and
    # in chain-check's local-mode sentence. Nothing here hands `home` to
    # git, so the native spelling is the right one, and normalising at the
    # source closes it for every caller rather than at each of the four
    # places that print it. Found by CI's Windows leg on a branch whose two
    # authors both said Windows was CI's to answer.
    return (
        os.path.join(root, HOME),
        os.path.normpath(os.path.join(common, HOME)) if common else "",
    )


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
    try:
        with open(os.path.join(path, README), encoding="utf-8", errors="replace") as f:
            first = f.readline(len(MARKER) + 2)
    except OSError:
        return False
    return first.rstrip("\r\n") == MARKER


def earlier(path):
    """True where `<path>/README.md` opens with one of `EARLIER_HEADINGS`,
    read as `marked` reads the marker: the first line with its end stripped,
    and an empty path or a README that cannot be opened is no root."""
    if not path:
        return False
    longest = max(len(h) for h in EARLIER_HEADINGS)
    try:
        with open(os.path.join(path, README), encoding="utf-8", errors="replace") as f:
            first = f.readline(longest + 2)
    except OSError:
        return False
    return first.rstrip("\r\n") in EARLIER_HEADINGS


def home_at(root, common=None):
    """The `seal/` of the repository at `root`, or "" — for a caller that has
    already resolved the root and should not pay for a second `git` call.

    The two places are read in order, `<root>/seal/` then
    `<git-common-dir>/seal/`, and the first that is a directory whose
    `README.md` opens with `MARKER` is the answer; nothing else is read. A
    `<root>/seal/` without the marker is passed over, so a project that keeps
    a directory of that name for itself can still keep the root under the
    git directory. The opt-out is read once, here, so it cannot be
    honoured by one arm of a gate and missed by the other — the migration
    config sits inside the root the opt-out takes back, and a repository
    nobody reviews has nothing to compare against an original either.

    `common` is passed by a caller that needs the common git directory for
    something else too, so one invocation asks git for it once rather than
    once per unit that wants it — the same parameter, for the same reason, as
    `home_paths` above. `hooks/mode-gate.py#main` is that caller: it resolves
    the root, the opt-in and its own `marker_dir` in one pass, and measured
    2026-09-08 from a linked worktree, where `.git` is a file and the fast
    path below does not apply, the same `rev-parse --git-common-dir` was
    running three times on every Bash call.
    """
    if not root:
        return ""
    # One `git_common_dir` call, which is what this cost before `home_paths`
    # existed too: the opt-out below needs the common directory even when the
    # shared root is the answer, so the old fast path never actually skipped
    # it. Hoisting it is what lets the two places be produced in one place.
    if common is None:
        common = git_common_dir(root)
    # A FILE, which is what this module and `seal/README.md` both say the
    # signal is. `os.path.exists` also accepted a DIRECTORY of that name, so
    # a directory created where the opt-out goes would have turned every
    # gate off with nothing in the diff that reads as the workflow being
    # switched off.
    if common and os.path.isfile(os.path.join(common, SCRATCH)):
        return ""
    for found in home_paths(root, common):
        if found and os.path.isdir(found) and marked(found):
            return found
    return ""


def home(cwd):
    """This repository's `seal/`, or "" when it does not run the workflow."""
    return home_at(repo_root(cwd))


def opted_in(cwd):
    """True when this repository runs the workflow."""
    return bool(home(cwd))


def parity_config(cwd):
    """Path to the migration config, or "" when there is none."""
    root = home(cwd)
    if not root:
        return ""
    path = os.path.join(root, PARITY_CONFIG)
    return path if os.path.isfile(path) else ""
