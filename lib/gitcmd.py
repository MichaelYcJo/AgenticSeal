"""The one place a script of the plugin starts git or `gh`, and the argv of
every git command it starts, read the same under any person's or
repository's git configuration.

**`git` and `gh` are the two runners.** The rule
`docs/running/what-a-script-gates.md` *Which gate a script holds* states is
that each git and `gh` command a script under `lib/`, `skills/`,
`.github/scripts/` or `evals/scripts/` starts is started by one of them,
under one bound, `TIMEOUT`. A command that did not start, or did not finish
within it, is no answer: both runners raise `Unrun`, whose one line names
the command and what went wrong. Neither reads an exit code unless the
caller passes `check=True`, because for some commands, such as `merge-base
--is-ancestor`, `diff --quiet`, `config --get` and `rev-parse --verify
--quiet`, exit 1 is an answer. `Failed`, the class of both `Unrun` and
`Exited`, is a `SystemExit`, as `lib/sibling.py#Absent` is, so a script
that does not catch it ends with that line on stderr at exit 1 and never
in a traceback.

**A run inside `one_run` asks git each question once.** Inside it, `git`
answers a command the run already asked from the first answer. A command
enters it for a run in which nothing the command writes changes what git
answers it, so an answer given again is the answer git would give.
`chain-check` writes nothing. `iadd settle` writes the working tree under
`--apply`, and the policy root under `--draft`. The only git read after
those writes asks where the common git directory is
(`lib/optin.py#git_common_dir`, from a linked worktree), and neither write
moves it. A git write inside a run, or any other read after a write the
run made, is answered as git answered before it. `gh` is asked every time.

**This module is the one place that names which keys reshape what a script
reads of git, and which subcommands they reshape.** A configuration can put
text into the fields a script parses, take a commit's paths out of a
listing, or follow a path into another path's history. `argv` sets each key
measured to do that with `-c`, which outranks every configuration file and
`GIT_CONFIG_COUNT`; a git that does not know a key ignores it. Each key, and
what it changes where a person or a repository sets it otherwise:

  log.showSignature          a signed commit's verification is printed before
                             its fields in `log`
  log.showRoot               the root commit's paths are left out of `log`
  log.follow                 a `log` of one path follows a rename into
                             another path's commits
  i18n.logOutputEncoding     `log` re-encodes subjects and bodies into another
                             encoding
  status.showUntrackedFiles  `status --porcelain` leaves untracked paths out

`KEYS` holds the value each is held at, git's own default. The
subcommands these keys change are `log` and `status`, and `git` builds
every command it starts with `argv`, so the pairs open each one. A key or
a subcommand found later to change a reading is added here and nowhere
else. `core.quotePath` is not set: a script that takes a path out of output
git quotes under it asks for the path with `-z`, which quotes none.

A setting that no `-c` key holds is named here with the flag that holds
it, and `FLAGS` holds the flag for each subcommand the setting reshapes.
`argv` puts a subcommand's flags directly after it, so each command `git`
starts carries them and no script passes them. `diff.ignoreSubmodules`
and the `ignore` of a submodule's entry in `.gitmodules` take a
submodule's path out of `diff`, out of a `log` that lists paths, and out
of `status` where the submodule's checkout moved off the commit the index
holds; the `.gitmodules` entry takes it out of `diff-tree` too. `-c
diff.ignoreSubmodules=none` does not reach the `.gitmodules` entry, so
`FLAGS` holds `--ignore-submodules=none` for each of those subcommands. The
subcommand is the first argument that opens with no `-`: `-C` and `-c`
before it each take the next argument as their value, as git(1)'s synopsis
spells them, and a caller writes any other option before it in one
argument, as `--literal-pathspecs` or `--git-dir=<path>`.

**`OLDEST` is the oldest git the scripts under `lib/`, `skills/` and
`hooks/` are written for.** A person's machine runs them on the git it
has. `OLDEST` is the version git's release notes give for the newest
option those scripts pass: `rev-parse` learned `--end-of-options` in 2.30
(`Documentation/RelNotes/2.30.0.txt`), and
`skills/implement/scripts/range_read.py#_commit` passes it. The script
whose command set that version asks `older` before its first command, so
a person on an older git reads the cause, and not git's own refusal of
the option mid-run. A change that adds a command only a newer git reads
raises `OLDEST` in the same commit, names the option here, and moves the
ask to its script. `older` reads the one line `git version` prints, and a
line in another shape refuses nothing. The floor is not stated of
`.github/scripts/` and `evals/scripts/`, which run on GitHub's runners or
at the owner's machine.

Three helpers read a path: `git_path` turns a path built by `os.path`
into git's `/`-joined form, `under_root` turns a `/`-joined
repository-relative path into the disk's, and `inside` answers whether a
path on the disk is a directory or under it. `http_answer` reads the HTTP
status and the body out of what `gh api -i` printed, so a caller decides
on the status and not on the words of gh's stderr. `decoded` reads bytes
git printed as `git` reads its text, and `batch_texts` reads what `git
cat-file --batch` printed by the size each header gives.

Standard library only, and Python 3.9 syntax: the `Stop` hook's
`stamp.py`, and every hook that reads `lib/optin.py`, reach it on
whatever `python3` starts them.
"""

import contextlib
import os
import re
import shutil
import subprocess

KEYS = (
    ("log.showSignature", "false"),
    ("log.showRoot", "true"),
    ("log.follow", "false"),
    ("i18n.logOutputEncoding", "UTF-8"),
    ("status.showUntrackedFiles", "normal"),
)

# The seconds one git or `gh` command may take before it is no answer. It
# guards against a git that hangs and is no budget of a read: measured over
# this repository's 675 commits, the heaviest read the scripts make took
# 0.02 s and `iadd settle`'s whole dry run 1.42 s. 60 was the largest of the
# bounds the scripts held one per call before this one (#1573).
TIMEOUT = 60


# The options `argv` puts directly after each subcommand it names.
FLAGS = {
    "diff": ("--ignore-submodules=none",),
    "diff-tree": ("--ignore-submodules=none",),
    "log": ("--ignore-submodules=none",),
    "status": ("--ignore-submodules=none",),
}

# The options before a subcommand that take the next argument as their
# value, as git(1)'s synopsis spells them.
VALUED = ("-C", "-c")


def argv(*args):
    """`["git", "-c", "<key>=<value>", ..., *args]`, one `-c` for each of
    `KEYS`, with the options `FLAGS` holds for the subcommand put directly
    after it."""
    held = []
    for key, value in KEYS:
        held += ["-c", f"{key}={value}"]
    at = 0
    while at < len(args) and args[at].startswith("-"):
        at += 2 if args[at] in VALUED else 1
    if at < len(args):
        args = (*args[: at + 1], *FLAGS.get(args[at], ()), *args[at + 1 :])
    return ["git", *held, *args]


def git_path(path):
    r"""`path` as git spells it: forward slashes, whatever `os.sep` is here.

    Each caller builds a repo-relative path by `os.path.relpath` and then
    reads it beside what git prints or hands it to a reader of git's paths:
    `unverified_check.py#repo_relative`'s answer is matched against the
    `Reference specs` key, `chain_check.py#tree_at` lists a directory on
    disk in the form `ls-tree` lists it at a ref, and
    `lib/console.py#annotate` names a file to GitHub. git answers and accepts `/`
    on every platform, so on Windows a path built by `os.sep` would match
    none of them: `threads\x\gaps.md` against `threads/x/gaps.md`.

    A no-op where `os.sep` already is `/`, rather than branching on `os.name`:
    the substitution has to be on the path Linux CI runs, or the Windows half
    is proven by nothing. It also must not run there — a backslash is a legal
    character in a POSIX filename, and rewriting it would corrupt a real name.
    """
    return path if os.sep == "/" else path.replace(os.sep, "/")


def under_root(root, rel):
    """The disk path of a `/`-joined repository-relative path."""
    return os.path.join(root, *rel.split("/"))


def inside(path, top):
    """Whether PATH is TOP or under it, each taken absolute from the
    directory this runs in. A caller that compares real paths resolves both
    first.

    `commonpath` rather than `startswith`, which reads `/repo-2/x` as under
    `/repo`. Paths on two drives share no prefix, and `commonpath` raises for
    them."""
    path, top = os.path.abspath(path), os.path.abspath(top)
    try:
        return os.path.commonpath([path, top]) == top
    except ValueError:
        return False


class Failed(SystemExit):
    """A git or `gh` command that gave no answer the caller can read. A
    `SystemExit` whose code is its one line, so an uncaught one ends the
    process with that line on stderr at exit 1. `command` is the program
    and the arguments the caller passed, without `argv`'s `-c` pairs, the
    options of `FLAGS` or `-C <root>`."""

    def __init__(self, command, line):
        super().__init__(line)
        self.command = command
        self.line = line


class Unrun(Failed):
    """The command did not start, its program is not on PATH, or it did
    not finish within `TIMEOUT`."""


class Exited(Failed):
    """A non-zero exit where the caller passed `check=True`, with its
    `returncode` and `stderr`. The line holds the code and the first line
    of `stderr`."""

    def __init__(self, command, returncode, stderr):
        said = (
            stderr.decode("utf-8", "replace") if isinstance(stderr, bytes) else stderr
        )
        first = (said or "").strip().split("\n", 1)[0].strip()
        line = f"{_shown(command)} exited {returncode}"
        super().__init__(command, f"{line}: {first}" if first else line)
        self.returncode = returncode
        self.stderr = stderr


def _shown(command):
    """COMMAND as the runner's lines name it, in backticks."""
    return "`" + " ".join(command) + "`"


def _start(command, found, check, encoding, **kwargs):
    """Start FOUND, the argv of COMMAND, under `TIMEOUT` with its output
    captured, as text in ENCODING with undecodable bytes replaced or as
    bytes where ENCODING is None; `Unrun` for no answer, `Exited` for a
    non-zero exit where CHECK is true.

    The encoding is named rather than left to `text=True`, which decodes
    with whatever locale the parent had. git answers UTF-8, and on a cp949
    console against a repository under a Korean path that decode killed
    subprocess's reader thread, leaving `stdout` None (measured)."""
    try:
        done = subprocess.run(
            found,
            capture_output=True,
            timeout=TIMEOUT,
            encoding=encoding,
            errors="replace" if encoding else None,
            **kwargs,
        )
    except subprocess.TimeoutExpired:
        raise Unrun(
            command, f"{_shown(command)} did not finish within {TIMEOUT} seconds"
        ) from None
    except (OSError, subprocess.SubprocessError) as exc:
        # `FileNotFoundError` is raised for a program not on PATH, and for a
        # `cwd` that is not there.
        why = (
            f"`{command[0]}` is not on PATH"
            if isinstance(exc, FileNotFoundError) and shutil.which(found[0]) is None
            else str(exc)
        )
        raise Unrun(command, f"{_shown(command)} could not be run: {why}") from None
    if check and done.returncode:
        raise Exited(command, done.returncode, done.stderr)
    return done


# The answers of the run `one_run` holds open, each `git` asked in it keyed
# by what it was asked, or None outside a run.
_answers = None


@contextlib.contextmanager
def one_run():
    """A run inside which `git` answers a command it already answered from
    that first answer and starts no process. The answers are dropped when
    the run ends, by return or by exception. Entered while a run stands,
    it joins that run, whose answers outlive the inner one. Which runs may
    enter it is the module docstring's."""
    global _answers
    if _answers is not None:
        yield
        return
    _answers = {}
    try:
        yield
    finally:
        _answers = None


def git(root, *args, given=None, binary=False, env=None, check=False):
    """The `subprocess.CompletedProcess` of `argv("-C", root, *args)`, with
    GIVEN on stdin, text as UTF-8 with undecodable bytes replaced or bytes
    where BINARY is true, and the variables of ENV added to this process's
    environment. `Unrun` where it gave no answer; the exit code is the
    caller's to read unless CHECK is true, where a non-zero one raises
    `Exited`.

    Inside `one_run`, a command asked with the same ROOT, ARGS, GIVEN,
    BINARY and ENV as one the run already answered is answered from that
    process, and CHECK is read on every ask. An `Unrun` is never kept, so
    the next ask starts the command again."""
    command = ["git", *args]
    key = (root, args, given, binary, tuple(sorted(env.items())) if env else None)
    done = _answers.get(key) if _answers is not None else None
    if done is None:
        done = _start(
            command,
            argv("-C", root, *args),
            False,
            None if binary else "utf-8",
            input=given,
            env={**os.environ, **env} if env else None,
        )
        if _answers is not None:
            _answers[key] = done
    if check and done.returncode:
        raise Exited(command, done.returncode, done.stderr)
    return done


def gh(*args, root=None, check=False):
    """The `subprocess.CompletedProcess` of `gh <args>`, the `gh`
    `shutil.which` finds, started in ROOT, in `git`'s text mode and read
    as `git` reads."""
    command = ["gh", *args]
    found = shutil.which("gh")
    if found is None:
        raise Unrun(command, f"{_shown(command)} could not be run: `gh` is not on PATH")
    return _start(command, [found, *args], check, "utf-8", cwd=root)


# The status line `gh api -i` prints first: `HTTP/<version>`, a space, the
# three digits of the status, then a space and the reason phrase, or nothing.
STATUS_LINE = re.compile(r"HTTP/\S+ (\d{3})(?: .*)?")


def http_answer(stdout):
    """`(status, body)` of STDOUT, what `gh api -i` printed: the status
    line, the headers, an empty line and the body, read as `gh` returns it,
    with each line ending in LF.

    `status` is the integer the first line carries where that line is a
    status line, and None otherwise: a `gh` that reached no server prints
    nothing to stdout. `body` is the text after the first empty line, and
    `""` where there is none. It starts nothing."""
    head, _, body = stdout.partition("\n\n")
    found = STATUS_LINE.fullmatch(head.split("\n", 1)[0])
    return (int(found.group(1)) if found else None), body


def decoded(data):
    """DATA as `git` reads text: UTF-8 with each undecodable byte replaced,
    and every line ending a newline."""
    return data.decode("utf-8", "replace").replace("\r\n", "\n").replace("\r", "\n")


def batch_texts(out, names):
    """`[(text, None) or (None, answer)]`, one for each of NAMES, in their
    order, from OUT, the bytes `git cat-file --batch` printed when NAMES
    were given it one per line: the object's text as `decoded` reads it
    where it is a blob, or what the batch answered where it holds no file,
    such as `missing`, or the kind of object it holds instead. Each object
    is read by the size its header gives, never by a marker its bytes could
    hold. A name holds no newline, which git would read as two names."""
    read, at = [], 0
    for name in names:
        end = out.index(b"\n", at)
        header = decoded(out[at:end])
        at = end + 1
        fields = header.split(" ")
        if len(fields) != 3 or not fields[2].isdigit():
            # `<name> missing`, `<name> ambiguous`: the name is echoed.
            read.append((None, header.removeprefix(f"{name} ")))
            continue
        size = int(fields[2])
        content, at = out[at : at + size], at + size + 1
        read.append(
            (decoded(content), None) if fields[1] == "blob" else (None, fields[1])
        )
    return read


def is_ancestor(root, commit, ref):
    """Whether COMMIT is REF or reachable from it: `merge-base
    --is-ancestor`'s exit 0. `Unrun` as `git` raises it."""
    return git(root, "merge-base", "--is-ancestor", commit, ref).returncode == 0


# The oldest git the scripts under `lib/`, `skills/` and `hooks/` are
# written for, as its major and minor numbers. The module docstring gives
# the option it comes from.
OLDEST = (2, 30)

# The first line `git version` prints: the version, its major and minor
# numbers first, then anything after a space.
VERSION = re.compile(r"git version ((\d+)\.(\d+)\S*)(?: .*)?")


def older(root):
    """The line that says the git answering in ROOT is older than
    `OLDEST`, naming the version it printed, or None. None also where git
    exits non-zero or its first line is not one `VERSION` reads: that
    line is not read, and refuses nothing. `Unrun` as `git` raises it."""
    done = git(root, "version")
    found = VERSION.fullmatch(done.stdout.split("\n", 1)[0])
    if done.returncode or not found:
        return None
    if (int(found.group(2)), int(found.group(3))) >= OLDEST:
        return None
    return (
        f"git {found.group(1)} answers here, and the plugin's scripts need git "
        f"{OLDEST[0]}.{OLDEST[1]} or newer"
    )
