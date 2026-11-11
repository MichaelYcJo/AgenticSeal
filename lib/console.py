"""Where the streams get fixed, and why it is at every entry point.

A script that raises while reading or printing dies with **stdout empty**, and
empty stdout is exactly how the stamp's `seal stamp --stop` says "nothing to
draw". So the failure mode of every gate in this repository, under a console it
cannot encode to, is a silent pass — the exact condition the gates exist to
end. The same shape costs the `bin/`-wrapped checks their output, and
`chain_check.py` its verdict in CI.

Korean, Japanese and Chinese Windows default to cp949/cp932/cp936 and encode
none of the em dash, arrow or middle dot these files print; a bare `LC_ALL=C`
does the same on POSIX. The English `windows-latest` runner uses cp1252, which
encodes the em dash, so CI does not see the writing half; the reading half
still reaches it (cp1252 decodes every byte to *something*, so a round
record's 🔴 arrives as four other characters, and an open blocking finding
passes).

Three decisions live here, each with the failure it prevents:

**Unconditional, not `if os.name == "nt"`.** Where a stream is already UTF-8
this is a no-op, and branching on the platform would leave the Windows path
proven by nothing while Linux CI runs the other one.

**`stdin` is in the loop.** A payload is where the non-ASCII actually is — the
`Stop` payload `seal stamp --stop` reads carries the session's own paths, and
one Korean path is enough. That is the only stdin read production takes, and a
raise there draws no stamp.

**`errors` is named.** `TextIOWrapper.reconfigure` resets it to `strict`
whenever `encoding` is given without it, so naming the encoding alone turns a
degradable character into a crash, on `sys.stderr` too, which ships as
`backslashreplace`. A path holding a lone
surrogate must degrade, not take the gate down on its way to reporting
something.

The call sites are each entry point's `__main__`, not this module's import,
because a module that changes the process's streams as a side effect of being
imported would do it to `pytest` too. Every gate is also runnable on its own —
that is how the tests drive them and how anyone debugging one reaches them — so
each carries the call rather than relying on a caller having made it.

Every entry point owes the answer: each tracked `.py` with a module-level
`__main__` block opens its first such block with it, and one that cannot
carries its reason in an exemption above the line
`tests/censuses.py#entry_point` names, as `lib/launch.py` does. An entry
point gives it by importing this module and calling `to_utf8()`, or by
spelling the loop inline. A script that loads nothing from `lib/` at
import spells the loop, because a load of this module would be one more load
that can fail before the answer. Many of the scripts under `skills/*/scripts/`
and `.github/scripts/` already reach `lib/` at import: each imports
`lib/sibling.py` and loads the modules it reads through `sibling.load`,
directly or through a sibling script, `skills/implement/scripts/seal.py`
among them.
`skills/code-review/scripts/chain_check.py` runs its loop before it loads any
of them, so that the refusal it prints when one will not load does not meet a
console's code page. None of the others says why it copies the loop rather
than loading this module the same way.
`.github/scripts/release_report.py`, `.github/scripts/release_seal.py` and
`.github/scripts/rules.py` load the tree's modules only when first asked,
after the arguments are read, so an absent module ends the first and the last
in `lib/sibling.py`'s sentence at exit 2 and `release_seal.py` in its note at
exit 0, rather than in a traceback. This command lists every place
that spells the loop, with this file among them:

    git grep -l "[.]reconfigure(" -- '*.py' ':!tests' ':!evals/behaviour'

What must not diverge is the ANSWER, which is written down here.

`annotate` is the one spelling of a line a check prints about a file: a
GitHub annotation in CI, a plain line anywhere else. `seal unverified` and
`chain-check` print through it. It names the file as git spells it,
`lib/gitcmd.py#git_path`, imported beside it.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitcmd import git_path

# stderr keeps `backslashreplace`, which is what Python ships it with and what
# makes an undecodable path degrade rather than raise while it is being
# reported.
STREAMS = (("stdin", "replace"), ("stdout", "replace"), ("stderr", "backslashreplace"))


def to_utf8():
    """Put this process's three streams into UTF-8. Idempotent, and a no-op
    where they already are.

    `hasattr` rather than a `None` check, because a stream can be absent (a
    process invoked with stdin closed) or be something without `reconfigure`
    at all — pytest's capture objects are the case the suite meets.
    """
    for name, errors in STREAMS:
        stream = getattr(sys, name, None)
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors=errors)


def annotate(kind, path, line, message):
    """A GitHub annotation in CI, a plain line anywhere else."""
    if os.environ.get("GITHUB_ACTIONS"):
        # An annotation is matched against the diff by path, and GitHub spells
        # those the way git does. `seal unverified` passes
        # `unverified_check.py#display_path` output, which is `os.sep`-spelled
        # on purpose -- right for a line a person reads, wrong for this. Live
        # wherever that command runs on a Windows runner.
        where = f" file={git_path(path)},line={line}" if path else ""
        return f"::{kind}{where}::{message}"
    return f"{path}:{line}  {message}" if path else message
