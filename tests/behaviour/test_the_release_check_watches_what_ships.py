"""The hygiene step that asks a release for a version bump watches every root
that ships.

Issue #10. Updates are keyed to the version in `plugin.json`, so a change to
what ships that leaves the version alone reaches nobody — that is the whole
reason the step exists. Its pattern named five roots and `bin/` was not one
of them, although the plugin loader puts `bin/` on the Bash tool's PATH
(Claude Code plugin reference, *File locations*: "Executables added to the
Bash tool's PATH and invokable as bare commands while the plugin is
enabled"). A pull request fixing only a wrapper would have shipped without
moving the version, and nothing would have said so.

Issue #1571. The pattern and a hand-kept classification here agreed with
each other and disagreed with `dist`: `docs/`, which every installed agent
opens at the plugin's root, was watched by neither. So what ships is read
from `git archive`, the one product of `.gitattributes` and the tree of
each `dist` commit. Every top-level directory the archive holds is matched
by the step's pattern or named in `UNREAD`, the entries the archive holds
that nothing installed reads, and every top-level file the archive holds is
named in `UNREAD`. The next `commands/` or `.mcp.json` is a decision made in
`.gitattributes`, the pattern or `UNREAD`, rather than a gap somebody
notices while writing a change up.

The pattern is matched with Python's `re`, not by spawning `grep -E`: the
suite runs on windows-latest too, and the pattern uses only anchors,
alternation and one escaped dot, which POSIX ERE and `re` read alike.
"""

import os
import re
import subprocess

from conftest import ROOT, archived, code_lines
from workflows import load

# No TARGET: its cases classify every top-level entry the archive holds and git lists, and hold the release check of .github/workflows/hygiene.yml to them.


WORKFLOW = os.path.join(ROOT, ".github", "workflows", "hygiene.yml")
STEP = "a change to what ships must move the version"

# The top-level entries the archive holds that nothing installed reads, so a
# change confined to one moves no version. `assets/` stays in `dist` for the
# images the READMEs show wherever `dist` is rendered. The files are read by
# people on GitHub. `TRADEMARKS.md` is the brand notice (#1174), held as
# `LICENSE` is. An entry here must not be matched by the pattern.
UNREAD = {
    "assets",
    ".gitignore",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.ko.md",
    "README.md",
    "SECURITY.md",
    "TRADEMARKS.md",
}


def ships_pattern():
    """The regex the step filters the diff's file list through, verbatim."""
    found = re.search(r"grep -E '(\^\([^']*\)/)'", release_step())
    assert found, "the step no longer filters the file list with grep -E '^(...)/'"
    return re.compile(found.group(1))


def watched(entry):
    """Whether a change under the top-level ENTRY moves the version."""
    return bool(ships_pattern().match(f"{entry}/anything"))


def archive_top_level():
    """`(directories, files)`: the top-level entries the archive of the
    tree holds, a directory being an entry some path stands under."""
    held = archived(ROOT)
    top = {path.split("/", 1)[0] for path in held}
    directories = {path.split("/", 1)[0] for path in held if "/" in path}
    return directories, top - directories


def tracked_top_level_entries():
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, encoding="utf-8", check=True
    ).stdout
    return {line.split("/", 1)[0] for line in out.splitlines() if line}


def test_every_directory_the_archive_holds_is_watched_or_unread():
    """A directory the archive holds reaches every installed copy. A change
    under it moves the version, or it is named in `UNREAD`, and never both,
    so whoever adds a directory decides which."""
    directories, _files = archive_top_level()
    assert ".claude-plugin" in directories, sorted(directories)
    # The pattern the step's `grep -E` filters the diff's file list through,
    # which the runner runs at a release pull request.
    undecided = sorted(d for d in directories if watched(d) == (d in UNREAD))
    assert not undecided, (
        f"{undecided} is a top-level directory the archive holds, and the "
        f"hygiene step's pattern {ships_pattern().pattern!r} and UNREAD in "
        f"{os.path.basename(__file__)} do not decide it: watch it in the "
        "pattern where an installed copy reads it, name it in UNREAD where "
        "nothing installed does, or mark it `export-ignore` in `.gitattributes`"
    )


def test_every_file_the_archive_holds_at_the_top_is_unread():
    """A top-level file the archive holds is one nothing installed reads, or
    the loader reads it and the step has to watch it. Neither is safe to
    leave to whoever notices, so each is named in `UNREAD`."""
    _directories, files = archive_top_level()
    undecided = sorted(files - UNREAD)
    assert not undecided, (
        f"{undecided} is a top-level file the archive holds and UNREAD in "
        f"{os.path.basename(__file__)} does not name it. Name it there where "
        "nothing installed reads it, or mark it `export-ignore` in "
        "`.gitattributes`; a file the loader reads needs the step to watch it"
    )


def test_nothing_the_archive_leaves_out_is_watched():
    """A wrong deny at the release is a stopped release: a change confined to
    what `dist` does not hold must not be asked for a version bump."""
    directories, files = archive_top_level()
    left_out = tracked_top_level_entries() - directories - files
    assert "tests" in left_out, sorted(left_out)
    # The same pattern, which a change confined to such an entry must not
    # match.
    asked = sorted(entry for entry in left_out if watched(entry))
    assert not asked, (
        f"{asked} leaves the archive, so no installed copy holds it, yet the "
        f"pattern {ships_pattern().pattern!r} would demand a version bump for it"
    )


def test_the_pattern_names_only_roots_the_archive_holds():
    """A root the pattern names and the archive does not hold is a watch on
    nothing, or on a directory `.gitattributes` took out."""
    directories, _files = archive_top_level()
    # The roots the step's pattern alternates, which the runner matches.
    named = set(ships_pattern().pattern[2:-2].replace("\\", "").split("|"))
    assert named <= directories, (
        f"the pattern names {sorted(named - directories)}, which the archive "
        "does not hold"
    )


# What a refused author reads (#443).
#
# The first person the step ever refused was a contributor whose pull request
# was aimed at the wrong branch, and the message named only `plugin.json`, the
# one file a contribution must not touch. At the moment it refuses, a release
# that forgot the bump and a contribution filed against `main` both arrive
# with `base_ref = main`, so the message names both causes. The cases below
# pin the facts of the `::error::` line a reader acts on: the file a release
# moves, the branch a contribution goes to and the document that holds the
# procedure. Its sentences are the proofer's to read.


def release_step():
    """The script of the one step called STEP, with its shell comments off."""
    steps = [
        step
        for job in load(WORKFLOW)["jobs"].values()
        for step in job["steps"]
        if step.get("name") == STEP
    ]
    assert len(steps) == 1, f"hygiene.yml has {len(steps)} steps named {STEP!r}"
    return "\n".join(code_lines(steps[0]["run"]))


def refusal():
    """The one `::error::` line the step emits when the version did not move."""
    found = re.search(r"::error::(.*)", release_step())
    assert found, "the step no longer emits an ::error:: annotation at all"
    return found.group(1)


def test_the_refusal_names_the_branch_a_contribution_goes_to():
    """#443. The real cause of the first refusal this step ever issued was the
    base branch, so the refusal names the branch a contribution's base
    belongs to."""
    text = refusal()
    # The integration branch `release/next`, which a contributor bases the
    # pull request on.
    assert "release/next" in text, (
        "the refusal does not say where a contribution's base belongs. A "
        "message that diagnoses without naming the fix leaves the reader "
        f"exactly where they were:\n{text}"
    )


def test_the_refusal_names_the_file_a_release_moves():
    """A2's readable half. Somebody genuinely cutting a release meets this
    line too, and for them the file to move is the fix."""
    text = refusal()
    # The file whose version a release moves, which a reader opens.
    assert "plugin.json" in text, (
        "the refusal no longer names the file a release has to move"
    )


def test_the_refusal_names_the_document_that_holds_the_procedure():
    """A CI log is read by somebody already stuck. The message states the
    cause and the fix inline and cites the file after, rather than making a
    second hop the only way to the answer."""
    text = refusal()
    # The document a refused author opens for the procedure.
    assert "CONTRIBUTING.md" in text, (
        f"the refusal cites no document for the procedure behind it:\n{text}"
    )


def test_the_base_guard_is_a_closed_if_with_the_early_exit_inside_it():
    """A2. The condition, the exit codes and the set of refused pull requests
    are identical before and after the message change — this is what says so.

    The whole guard, in order, not only its condition:
    `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py` records a
    mutation that deleted the `exit 0` and the `fi` and passed a check that
    asserted the condition alone, leaving a step that runs on every pull
    request and is malformed shell.

    **Closed before the next `if`, and that word is load-bearing.** The first
    form of this case was a regex spanning `then` to `exit 0 … fi` with
    `re.S`, and the same mutation walked straight past it: this step holds a
    second `if … exit 0 … fi` (the `-z "$ships"` early return) for the dotted
    part to reach. Caught by running the mutation rather than by reading.
    """
    lines = release_step().splitlines()
    opens = [
        number
        for number, line in enumerate(lines)
        if 'github.base_ref }}" != "main" ]; then' in line
    ]
    assert opens, (
        "the step no longer opens with the base guard the other release-only "
        f"steps use:\n{release_step()}"
    )
    start = opens[0]
    after = lines[start + 1 :]

    def first(predicate):
        for offset, line in enumerate(after):
            if predicate(line.strip()):
                return offset
        return len(after)

    closes = first(lambda line: line == "fi")
    reopens = first(lambda line: line.startswith("if "))
    assert closes < reopens, (
        "the base guard is not closed before the next `if` — an `if … then` "
        "left open runs its body on every pull request and is malformed "
        f"shell:\n{release_step()}"
    )
    # The shell command `exit 0` inside the guard, which the runner runs to
    # end the step early on any base but `main`.
    assert any("exit 0" in line for line in after[:closes]), (
        "the base guard is closed but nothing inside it returns early, so "
        "every contribution now reaches the version check and the exemption "
        f"list every contributor reads in CONTRIBUTING.md is false:\n"
        f"{release_step()}"
    )


def test_the_refusal_still_fails_the_run():
    """The message is the only thing that moved. A refusal that stopped
    exiting 1 would ship an unversioned release in silence."""
    step = release_step()
    # The shell command `exit 1` after the `::error::` line, which the runner
    # runs to fail the step.
    assert re.search(r"::error::.*\n\s*exit 1\n", step), (
        f"the ::error:: line is no longer followed by `exit 1`:\n{step}"
    )
