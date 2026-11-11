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

Nothing pinned the pattern, which is how a root fell out of it unnoticed.
This file is the pin. It reads the pattern out of the workflow rather than
restating it, classifies every tracked top-level entry of the repository as
shipping or staying home, and fails on an entry nobody has classified — so
the next `commands/` or `output-styles/` is a decision somebody makes in this
file rather than a gap somebody notices while writing a change up.

The pattern is matched with Python's `re`, not by spawning `grep -E`: the
suite runs on windows-latest too, and the pattern uses only anchors,
alternation and one escaped dot, which POSIX ERE and `re` read alike.
"""

import os
import re
import subprocess

import pytest
from conftest import ROOT, code_lines, read
from workflows import load

WORKFLOW = os.path.join(ROOT, ".github", "workflows", "hygiene.yml")
RELEASE_DOC = os.path.join(ROOT, "docs", "releasing", "branch-and-release.md")
STEP = "a change to what ships must move the version"

# What the plugin loader reads or puts in front of a user while the plugin is
# enabled. A root here must be matched by the workflow's pattern.
SHIPS = {
    "skills",  # skills/<name>/SKILL.md
    "agents",  # agents/<name>.md
    "hooks",  # hooks/hooks.json and the scripts it names
    "lib",  # the modules the shipped scripts import
    "templates",  # what the implement skill bootstraps a repository from
    ".claude-plugin",  # the manifest; the version itself
    "bin",  # executables the loader puts on the Bash tool's PATH
}

# This repository's own work: read by people on GitHub, by tooling in a clone,
# or by the suite. None of it reaches a user through the plugin, so a change
# confined to it needs no version bump. An entry here must NOT be matched.
STAYS_HOME = {
    "docs",
    "tests",
    "seal",
    "evals",
    "assets",
    ".github",
    ".gitattributes",
    ".gitignore",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.ko.md",
    "README.md",
    "SECURITY.md",
    # The brand notice (#1174). A user's installed plugin holds it, as it
    # holds `LICENSE`, because the install copies the repository's root;
    # the loader reads neither, so a change to it alone moves no version.
    "TRADEMARKS.md",
    "ruff.toml",
}


def ships_pattern():
    """The regex the step filters the diff's file list through, verbatim."""
    found = re.search(r"grep -E '(\^\([^']*\)/)'", release_step())
    assert found, "the step no longer filters the file list with grep -E '^(...)/'"
    return re.compile(found.group(1))


def tracked_top_level_entries():
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, encoding="utf-8", check=True
    ).stdout
    return {line.split("/", 1)[0] for line in out.splitlines() if line}


def test_the_two_lists_do_not_overlap():
    assert not SHIPS & STAYS_HOME


@pytest.mark.parametrize("root", sorted(SHIPS))
def test_every_shipping_root_is_watched(root):
    """A change under a root the loader reads has to move the version."""
    pattern = ships_pattern()
    # The pattern the step's `grep -E` filters the diff's file list through,
    # which the runner runs at a release pull request.
    assert pattern.match(f"{root}/anything"), (
        f"`{root}/` ships but the hygiene step's pattern {pattern.pattern!r} "
        f"does not match it — a release fixing only `{root}/` would reach "
        "nobody, because updates are keyed to the version it leaves alone"
    )


@pytest.mark.parametrize("entry", sorted(STAYS_HOME))
def test_nothing_that_stays_home_is_watched(entry):
    """A wrong deny at the release is a stopped release: a change confined to
    this repository's own work must not be asked for a version bump."""
    pattern = ships_pattern()
    # The same pattern, which a change confined to this root must not match.
    assert not pattern.match(f"{entry}/anything"), (
        f"`{entry}` does not reach a user through the plugin, yet the pattern "
        f"{pattern.pattern!r} would demand a version bump for it"
    )


def test_the_pattern_names_nothing_this_file_has_not_classified():
    """The pattern can only name roots this file says ship. A root added to the
    workflow alone is a decision with no record of why."""
    named = set(ships_pattern().pattern[2:-2].replace("\\", "").split("|"))
    # The roots the step's pattern alternates, which the runner matches.
    assert named == SHIPS, (
        f"the pattern names {sorted(named)} and this file says {sorted(SHIPS)} "
        "ship — classify the difference here, with the reason"
    )


def test_every_top_level_entry_is_classified():
    """A directory nobody has classified is the state `bin/` was in: it ships
    or it does not, and neither answer is safe to leave to whoever notices.
    Whoever classifies it also decides whether `dist` holds it, since the
    list of what leaves `dist` is a different list, in `.gitattributes`."""
    unclassified = tracked_top_level_entries() - SHIPS - STAYS_HOME
    assert not unclassified, (
        f"{sorted(unclassified)} is tracked at the top level and classified "
        "neither as shipping nor as staying home. Decide — does the plugin "
        "loader read it, or does a user run it while the plugin is enabled? — "
        f"and add it to SHIPS or STAYS_HOME in {os.path.basename(__file__)}. "
        "Then decide whether `dist`, the branch the plugin directory reads, "
        "holds it: an entry only this repository's development reads gets an "
        "`export-ignore` line in `.gitattributes`."
    )


def test_the_release_document_names_the_same_roots():
    """`docs/releasing/branch-and-release.md` tells the release sequence which roots
    trigger the bump. It said five when the pattern said five; both must name
    the SAME roots, so a root written into the paragraph alone, or taken out
    of it alone, reads as a disagreement with the workflow rather than as
    prose."""
    doc = read(RELEASE_DOC)
    # The paragraph, not the sentence: `.claude-plugin/` carries a full stop.
    paragraph = doc.split("the `hygiene` workflow", 1)[1].split("\n\n", 1)[0]
    named = set(re.findall(r"`([^`]+)/`", paragraph))
    # The roots the paragraph names as code spans, which a person cutting a
    # release reads to know which change moves the version.
    assert named == SHIPS, (
        f"docs/releasing/branch-and-release.md's paragraph about the hygiene workflow "
        f"names {sorted(named)} and the pattern's roots are {sorted(SHIPS)} — "
        "the two have to agree, and this file is where the list is decided"
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
    # The branch a contributor bases the pull request on, with the version
    # they fill in.
    assert "release/vX.Y.Z" in text, (
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
