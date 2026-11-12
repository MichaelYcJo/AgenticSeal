"""The repository ships a command for its own suite, and the second call is cheap.

Issue #156. The cases here read the `bin/` wrappers, the workflows,
`CONTRIBUTING.md` *Running the checks* and the agent definitions that send
a reader to the runner.

The cases of `.github/scripts/run_tests.py`'s functions stand in
`tests/github/test_run_tests.py`, and this file reads the runner through that
file's `rt`.
"""

import os
import subprocess

import pytest
from conftest import ROOT, read
from test_run_tests import rt
from workflows import load, pytest_jobs

# No TARGET: its cases list every command under bin/, and hold the runner's floor and parser across .github/workflows/test.yml, CONTRIBUTING.md and the agent definitions.


BIN = os.path.join(ROOT, "bin")


def suite_jobs():
    """{job name: job} for each job of `test.yml` that runs the suite, as
    `tests/workflows.py#pytest_jobs` reads it: the legs stand in two jobs
    (#1516)."""
    jobs = pytest_jobs(load(".github/workflows/test.yml"))
    assert jobs, "no job of test.yml runs pytest"
    return jobs


def posix_entries():
    """Every `bin/` wrapper that is not the Windows twin."""
    return sorted(n for n in os.listdir(BIN) if not n.endswith(".cmd"))


def test_both_wrappers_ship_and_point_at_the_runner():
    """`bin/` is on the Bash tool's PATH while the plugin is enabled, and
    cmd.exe resolves the `.cmd` twin through PATHEXT. A new command means both
    files or it means one platform."""
    posix = os.path.join(BIN, "test")
    windows = os.path.join(BIN, "test.cmd")
    assert os.path.isfile(posix), "bin/test missing"
    assert os.path.isfile(windows), "bin/test.cmd missing"
    # The runner's path in each wrapper, which the shell and cmd.exe run.
    assert ".github/scripts/run_tests.py" in read(posix)
    text = read(windows)
    assert ".github\\scripts\\run_tests.py" in text
    # The two interpreter commands the `.cmd` twin runs, in its order.
    assert "py -3" in text and "python " in text, (
        "the .cmd twin prefers `py -3` and falls back to `python`"
    )


def test_every_bin_entry_has_a_windows_twin():
    """The rule the five earlier pairs follow, asked of all of them at once:
    the sixth entry is where a lone POSIX wrapper would have arrived."""
    missing = [n for n in posix_entries() if not os.path.isfile(f"{BIN}/{n}.cmd")]
    assert not missing, f"{missing} ship without a .cmd twin — Windows loses them"


@pytest.mark.parametrize("entry", posix_entries())
def test_every_posix_wrapper_resolves_its_own_directory(entry):
    """A wrapper that resolves against the caller's cwd works from the
    repository root and nowhere else, which is the failure a session hits
    from a subdirectory."""
    text = read(os.path.join(BIN, entry))
    # The line the shell runs to find the wrapper's own directory, and the
    # expansion that hands the caller's arguments on.
    assert 'here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)' in text, (
        f"bin/{entry} does not resolve its own directory the way its siblings do"
    )
    assert '"$@"' in text, f"bin/{entry} does not pass its arguments through"


def test_the_wrapper_points_at_the_contract_rather_than_inviting_a_full_run():
    """`bin/test` with no arguments runs the whole suite, which
    contract rule 2 forbids to every agent. The file a session reads before
    typing it names where the rule is; whose the run is, in its words, is
    the proofer's to read."""
    text = read(os.path.join(BIN, "test"))
    # The path of the contract, which a session reading the wrapper opens
    # for the rule that keeps the full run out of its hands.
    assert "skills/agent-contract/SKILL.md" in text, (
        "bin/test no longer names the rule that forbids the full suite to an "
        "agent, so a segment reading it has nothing telling it not to"
    )


@pytest.mark.skipif(os.name == "nt", reason="the POSIX wrapper needs a POSIX shell")
def test_a_copy_without_the_runner_beside_it_says_so(tmp_path):
    """A copy of `bin/` taken on its own — vendored wrappers, a partial
    copy — has no runner beside it. That has to be a sentence: `python3
    <missing path>` is a traceback about a file the reader never named."""
    copy = tmp_path / "bin"
    copy.mkdir()
    (copy / "test").write_text(read(os.path.join(BIN, "test")), encoding="utf-8")
    (copy / "test").chmod(0o755)
    result = subprocess.run(
        [str(copy / "test")], capture_output=True, encoding="utf-8", errors="replace"
    )
    assert result.returncode == 2, result
    assert "no runner beside it" in result.stderr, result.stderr
    assert "Traceback" not in result.stderr


def test_ci_installs_the_parser_the_runner_pins():
    """#667, phase 1. The pin is chosen once, in `MARKDOWN_IT`, and each CI
    job that runs the suite installs its own list. A version bumped in one
    place and not the other runs the oracle's cases against two parsers.
    Seen red with `pytest-wide`'s steps a copy whose install line names
    another PyYAML (#1516)."""
    for name, job in suite_jobs().items():
        installs = [
            step["run"].split()
            for step in job["steps"]
            if step.get("run", "").startswith("pip install")
        ]
        assert installs, f"`{name}` installs nothing to compare"
        # The pinned parser `run_tests.py#MARKDOWN_IT` names, which the runner
        # installs before the suite runs, and no other version of it.
        assert any(rt.MARKDOWN_IT in words for words in installs), (name, installs)
        assert not any(
            word.startswith("markdown-it-py") and word != rt.MARKDOWN_IT
            for words in installs
            for word in words
        ), (name, installs)
        # #647: cmarkgfm joins the same line, at the version the runner pins.
        assert any(rt.CMARKGFM in words for words in installs), (name, installs)
        assert not any(
            word.lower().startswith("cmarkgfm") and word != rt.CMARKGFM
            for words in installs
            for word in words
        ), (name, installs)
        # #1486: PyYAML joins the same line, at the version the runner pins.
        assert any(rt.PYYAML in words for words in installs), (name, installs)
        assert not any(
            word.lower().startswith("pyyaml") and word != rt.PYYAML
            for words in installs
            for word in words
        ), (name, installs)
        # #841: pytest-split joins the same line, at the version the runner pins.
        # It is CI's alone, so it is not in `PACKAGES` and `bin/test` never
        # installs it.
        assert any(rt.PYTEST_SPLIT in words for words in installs), (name, installs)
        assert not any(
            word.lower().startswith("pytest-split") and word != rt.PYTEST_SPLIT
            for words in installs
            for word in words
        ), (name, installs)
    assert rt.PYTEST_SPLIT not in rt.PACKAGES, rt.PACKAGES


def test_the_section_names_the_parser_and_where_it_is_pinned():
    """#667, phase 1. The section names the parser and the constant that
    pins it, and the fallback commands carry the pin as the runner spells
    it, so the fallback cannot run the oracle against another version
    either."""
    section = running_the_checks()
    # The parser's package and the constant that pins it, which a reader
    # installs and resolves in the runner.
    assert "`markdown-it-py`" in section and "MARKDOWN_IT" in section, section
    # The two fallback commands with the parser's pin, which a reader copies.
    assert f"uvx --with pytest --with {rt.MARKDOWN_IT} " in section, section
    assert f"pip install pytest {rt.MARKDOWN_IT} " in section, section
    # #647: the renderer's package and the constant that pins it, which a
    # reader installs and resolves in the runner.
    assert "`cmarkgfm`" in section and "`CMARKGFM`" in section, section
    # #1486: the YAML parser's package and the constant that pins it, which
    # a reader installs and resolves in the runner.
    assert "`PyYAML`" in section and "`PYYAML`" in section, section
    # The two fallback commands carrying the three pins in the runner's
    # order, which a reader copies.
    assert (
        f"--with {rt.MARKDOWN_IT} --with {rt.CMARKGFM} --with {rt.PYYAML} " in section
    ), section
    assert (
        f"pip install pytest {rt.MARKDOWN_IT} {rt.CMARKGFM} {rt.PYYAML} " in section
    ), section


# A command nobody is pointed at costs what the old one cost. Three documents
# carry the pointing, and each is a sentence somebody reads and acts on:
# `CONTRIBUTING.md` for a person in a clone, the handoff protocol for the
# orchestrator writing a spawn prompt, and `agents/crafter.md` for the segment
# that was not told.
def flat(*parts):
    """The file as one line, so a pinned phrase survives re-wrapping."""
    return " ".join(read(os.path.join(ROOT, *parts)).split())


def running_the_checks():
    """`CONTRIBUTING.md` *Running the checks*, to the next heading."""
    text = read(os.path.join(ROOT, "CONTRIBUTING.md"))
    start = text.index("## Running the checks")
    return text[start : text.index("\n## ", start + 1)]


def test_the_section_names_the_cheap_command_before_the_slow_one():
    """A reader copies the first command in the block. That is the whole of
    #156: the first one paid 55-58 seconds for its environment on every
    call, and a section that names the cheap one second still costs that."""
    section = running_the_checks()
    # The runner's command, which a reader copies from the section.
    assert "bin/test" in section, (
        "`CONTRIBUTING.md` *Running the checks* does not name the runner at all"
    )
    assert section.index("bin/test") < section.index("uvx --with pytest"), (
        "the slow form is still the first command in the section, so it is "
        "still what a reader copies"
    )


def test_the_section_and_the_runner_state_the_same_floor():
    """The document names a version and the code enforces one. Two places
    saying a number is two places to disagree, and the disagreement is
    invisible until somebody's 3.11 builds an environment the suite needs
    3.12 for."""
    section = running_the_checks()
    # The floor's version, read from the runner's `FLOOR`, which a reader
    # installs at least; and the constant's name, which the reader resolves
    # in the runner.
    assert rt.FLOOR_TEXT in section, (
        "the section no longer states the floor the runner enforces "
        f"({rt.FLOOR_TEXT} in .github/scripts/run_tests.py's FLOOR)"
    )
    assert "FLOOR" in section, (
        "the sentence names a number the reader cannot trace to the code that holds it"
    )


def test_ci_runs_the_suite_at_the_floor_the_runner_holds():
    """`CONTRIBUTING.md` *Running the checks* says CI runs the suite on
    ubuntu, Windows and macOS at the floor stated above, macOS in
    `pytest-wide`. So every operating system the matrices name holds at
    least one entry at `FLOOR`, whatever other Python it also runs (#1065)
    -- a floor CI does not run at is a floor nothing measures. The entries of every job that runs the suite are
    read together (#1516): ubuntu's floor leg and its 3.14 leg stand in two
    jobs. It reads a system and not its shards: one Windows shard moved off
    the floor leaves three at it, and this case passes that. Seen red with
    `pytest-wide`'s macOS entry moved to 3.13."""
    entries = [
        entry
        for job in suite_jobs().values()
        for entry in job["strategy"]["matrix"]["include"]
    ]
    systems = {e.get("os") for e in entries}
    assert systems, "no job that runs the suite names an operating system"
    at_floor = {e.get("os") for e in entries if e.get("python") == rt.FLOOR_TEXT}
    missing = sorted(systems - at_floor)
    assert not missing, (
        f"CI runs the suite on {missing} with no entry at the floor "
        f"{rt.FLOOR_TEXT} that `CONTRIBUTING.md` says every platform runs at"
    )


def test_the_section_names_the_contract_and_the_narrow_form():
    """`bin/test` with no arguments runs the whole suite, which
    contract rule 2 forbids to every agent. The section that makes it cheap
    names where that rule is and the form a segment types; whose the full
    run is, in its words, is the proofer's to read."""
    section = " ".join(running_the_checks().split())
    # The path of the contract, which a reader opens for the rule that keeps
    # the full run out of an agent's hands.
    assert "`skills/agent-contract/SKILL.md`" in section, (
        "the section makes the full suite cheap and says nothing about the "
        "rule that forbids it to a segment"
    )
    # The narrow form, which a segment copies to run one module.
    assert "bin/test tests/" in section, (
        "no narrow form is shown, so the only command a segment can copy is "
        "the one it must not run"
    )


# The citation of *The handoff*, which both definitions' runner rules carry and
# the agent resolves for the narrow form it is handed.
HANDOFF_LINK = "`docs/running/the-run.md` *The handoff*"


def test_crafter_cites_the_handoff_for_the_narrow_form():
    """The prompt is what went missing (#156: the orchestrator typed the
    runner into every spawn prompt, and the segments it forgot rediscovered
    one), so the fix cannot live in the prompt. `agents/crafter.md` reaches
    every segment at startup with nobody typing anything. Its rule's
    sentences are the proofer's to read; what is pinned is the link to the
    one statement of the form."""
    crafter = flat("agents", "crafter.md")
    assert HANDOFF_LINK in crafter, (
        "the rule is restated rather than linked, so the two carriers can drift apart"
    )


def test_proofer_cites_the_handoff_for_the_narrow_form():
    """The class is every segment that runs a test, and the fix reached one of
    them. `agents/proofer.md` told a reviewer to build a `uv` venv in its clone
    and named no runner, so a review round paid for an environment the
    repository already had built -- the same cost, on the segment that runs
    more cases than the crafter does. Both definitions ship to user
    repositories, so neither may name a command that exists only here. The
    rule's sentences, its fallback among them, are the proofer's to read."""
    proofer = flat("agents", "proofer.md")
    assert HANDOFF_LINK in proofer, (
        "the rule is restated rather than linked, so the two carriers can drift apart"
    )
