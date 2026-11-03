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
and `git status` a script under `hooks/`, `skills/` or `.github/scripts/`
starts is built by `argv` (`docs/running/what-a-script-gates.md` *Which gate a
script holds*). A key or a subcommand found later to change a reading is
added here and nowhere else. `core.quotePath` is not set: a script that
takes a path out of output git quotes under it asks for the path with `-z`,
which quotes none.
"""

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
