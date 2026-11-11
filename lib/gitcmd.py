"""The argv of a git command whose output a script parses, read the same
under any person's or repository's git configuration.

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

`KEYS` holds the value each is held at, git's own default. So the
subcommands these keys change are `log` and `status`, and every `git log`
and `git status` a script under `lib/`, `skills/` or `.github/scripts/`
starts is built by `argv` (`docs/running/what-a-script-gates.md` *Which gate a
script holds*). A key or a subcommand found later to change a reading is
added here and nowhere else. `core.quotePath` is not set: a script that
takes a path out of output git quotes under it asks for the path with `-z`,
which quotes none.

Two helpers spell a path the way git does and back: `git_path` turns a
path built by `os.path` into git's `/`-joined form, and `under_root` turns
a `/`-joined repository-relative path into the disk's.
"""

import os

KEYS = (
    ("log.showSignature", "false"),
    ("log.showRoot", "true"),
    ("log.follow", "false"),
    ("i18n.logOutputEncoding", "UTF-8"),
    ("status.showUntrackedFiles", "normal"),
)


def argv(*args):
    """`["git", "-c", "<key>=<value>", ..., *args]`, one `-c` for each of
    `KEYS`."""
    held = []
    for key, value in KEYS:
        held += ["-c", f"{key}={value}"]
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
