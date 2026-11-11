"""The one way a script of the plugin reaches another module of it.

A script puts `lib/` first on its `sys.path`, imports this module by its
plain name, and asks `load` for every other module it reads, a `lib/` one
included:

    sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "lib"))
    import sibling

    reader = sibling.load("lib/lines.py")

`load` names a module in `sys.modules` by its file's stem, the name a
`lib/` module already imports its neighbour by (`lib/tables.py` imports
`blocks`), so a module runs once in a process however many scripts and
`lib/` modules ask for it. No two tracked modules outside `tests/` share a
stem, and a file that came to share one is refused with both paths rather
than handed the other's module.

An absent file is said in one sentence, `MISSING`, whichever script asked:
a copy of one script taken on its own is not a plugin, and exit 2 says
nothing was read. A command that guards its own import of this
module spells the same sentence about this file, since it cannot read the
constant from a file that is not there. A caller whose run goes on without
the module loads inside `going_on`: there the absent file raises `Absent`
and no sentence is written, because "Nothing was read." is false of a run
that goes on, and the caller's own line names `Absent.path` and what goes
unread.

Standard library only, and Python 3.9 syntax: the `Stop` hook's
`seal_stamp.py` reaches it on whatever `python3` starts it.
"""

import contextlib
import importlib.util
import os
import sys

# The plugin root: the directory that holds `lib/`.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# What an absent module is called, the one spelling of it.
MISSING = (
    "cannot read {path}, which this command loads. It ships in the plugin "
    "beside this script; a copy of one script taken on its own is not a "
    "plugin. Nothing was read."
)
# What a stem held by another file is called.
TAKEN = "cannot load {path} as `{stem}`: {held} already runs under that name"


class Absent(SystemExit):
    """The exit `load` raises for an absent file: code 2, the file's path in
    `path`. A `SystemExit`, so a caller that does not catch it ends at exit
    2."""

    def __init__(self, path):
        super().__init__(2)
        self.path = path


# How many `going_on` blocks the process is inside.
_going_on = 0


@contextlib.contextmanager
def going_on():
    """A block whose caller goes on where a module is absent. A load inside
    it that meets an absent file raises `Absent` without writing `MISSING`,
    and the caller says in its own line what goes unread, naming
    `Absent.path`."""
    global _going_on
    _going_on += 1
    try:
        yield
    finally:
        _going_on -= 1


def _same(module, path):
    """Whether MODULE was executed from the file at PATH. The spelling
    `load` gave is compared first, since a reader asked for once per line
    asks again on every call."""
    held = getattr(module, "__file__", None)
    if not held:
        return False
    if held == path:
        return True
    return os.path.normcase(os.path.realpath(held)) == os.path.normcase(
        os.path.realpath(path)
    )


def load(rel):
    """The module at REL, a `/`-joined path under the plugin root such as
    `"lib/optin.py"`, executed once in this process.

    Where `sys.modules` holds the file's stem for this same file, that
    module is returned: a `lib/` module imported by its plain name and a
    module a script loaded are one instance. Otherwise the file is executed
    under its stem and registered. A module that raises while it executes
    is taken out of `sys.modules` again, and its exception reaches the
    caller unchanged; the caller decides what that means for its command.

    An absent file writes `MISSING` to stderr and raises `Absent`, a
    `SystemExit` whose code is the integer 2, because a string argument to
    `SystemExit` exits 1. Inside `going_on` nothing is written. A stem
    another file holds raises `ImportError` naming both files, and replaces
    nothing."""
    path = os.path.join(ROOT, *rel.split("/"))
    stem = os.path.splitext(os.path.basename(path))[0]
    held = sys.modules.get(stem)
    if held is not None and _same(held, path):
        return held
    if not os.path.isfile(path):
        if not _going_on:
            sys.stderr.write(MISSING.format(path=path) + "\n")
        raise Absent(path)
    if held is not None:
        where = getattr(held, "__file__", None) or repr(held)
        raise ImportError(TAKEN.format(path=path, stem=stem, held=where))
    spec = importlib.util.spec_from_file_location(stem, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[stem] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        if sys.modules.get(stem) is module:
            del sys.modules[stem]
        raise
    return module
