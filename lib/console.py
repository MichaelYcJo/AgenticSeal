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
point that reaches `lib/` at import, by importing `lib/sibling.py` and
loading the modules it reads through `sibling.load`, loads this module the
same way, binds it as `console`, and opens the block with
`console.to_utf8()`. `skills/implement/scripts/seal.py` and
`tests/run_tests.py`, the suite's runner, are two of them. Two kinds of
script spell the loop inline instead, and only these.

- A script that loads nothing from `lib/` at import, because a load of this
  module would be one more load that can fail before the answer.
  `.github/scripts/release_report.py`, `.github/scripts/release_seal.py` and
  `skills/settle/scripts/rules.py` are of this kind: they load the tree's
  modules only when first asked, after the arguments are read, so an absent
  module ends the first and the last in `lib/sibling.py`'s sentence at exit
  2 and `release_seal.py` in its note at exit 0, rather than in a traceback.
- `skills/code-review/scripts/chain_check.py` and
  `skills/code-review/scripts/pr_body.py`, which run their loops before they
  load any module, so that the refusal each prints when one will not load
  does not meet a console's code page.

This command lists every place outside the suite that spells the loop, with
this file among them:

    git grep -l "[.]reconfigure(" -- '*.py' ':!tests' ':!evals/behaviour'

What must not diverge is the ANSWER, which is written down here.

`annotate` is the one spelling of a line a check prints about a file: a
GitHub annotation in CI, a plain line anywhere else. `seal unverified` and
`chain-check` print through it. It names the file as git spells it,
`lib/gitcmd.py#git_path`, imported beside it.

`write_output` is the one writer of a step's output to `$GITHUB_OUTPUT`,
which `.github/scripts/tag_release.py` and
`.github/scripts/publish_release_note.py` pass on to the steps after them.
It stands here so that neither script loads the other for it.
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


def write_output(name, value):
    """`name=value` appended to `$GITHUB_OUTPUT` where it is set. A write
    that fails is printed and ignored: the act the output reports on has
    already happened, and a job that went red over its own output would be
    a failed job for nothing."""
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    try:
        with open(path, "a", encoding="utf-8") as handle:
            handle.write(f"{name}={value}\n")
    except OSError as problem:
        print(f"could not write {name}={value} to $GITHUB_OUTPUT: {problem}")
