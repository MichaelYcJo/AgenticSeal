"""The repository ships a command for its own suite, and the second call is cheap.

Issue #156. The cases here read the `bin/` wrappers, the workflows,
`CONTRIBUTING.md` *Running the checks*, the handoff protocol and the agent
definitions that send a reader to the runner, and wait for #923;
`agents/crafter.md` and `agents/proofer.md` name this file on their `check:`
lines.

#942's phase 6 placed the cases of `.github/scripts/run_tests.py`'s
functions in `tests/github/test_run_tests.py`, and this file reads the runner
through that file's `rt`.
"""

import os
import subprocess

import pytest
from conftest import read
from test_ci_gives_the_checks_what_they_need import jobs, matrix_include_entries
from test_ci_gives_the_checks_what_they_need import read as read_workflow
from test_run_tests import rt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BIN = os.path.join(ROOT, "bin")
SCRIPT = os.path.join(ROOT, ".github", "scripts", "run_tests.py")


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
    assert ".github/scripts/run_tests.py" in read(posix)
    text = read(windows)
    assert ".github\\scripts\\run_tests.py" in text
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
    assert 'here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)' in text, (
        f"bin/{entry} does not resolve its own directory the way its siblings do"
    )
    assert '"$@"' in text, f"bin/{entry} does not pass its arguments through"


def test_the_runner_behind_the_wrapper_says_the_same_thing():
    """Round 1's finding 7. `bin/test` is five lines and one `exec` into
    `.github/scripts/run_tests.py`.

    #30 re-pointed the wrapper's comment from `orchestrator` to `sealer` and
    left the module it runs saying the other thing — one command, two files,
    two owners, which is the contract rule 12 class this branch already knows
    `survivor-check` cannot reach. The changelog claimed *the runner's own
    comment … all of them now say the sealer's*, true of the wrapper and
    false of the runner.

    Nothing pinned this docstring: the case above reads `bin/test`, and the
    negative pin in `tests/test_the_seal_is_taken_once_by_the_sealer.py` is
    applied to the two agent definitions only."""
    runner = read(os.path.join(ROOT, ".github", "scripts", "run_tests.py"))
    assert "is the orchestrator's, run once after" in runner, (
        "the file `bin/test` execs no longer says whose the full suite is"
    )
    assert "is the sealer's" not in runner, (
        "the wrapper and the module it runs name two different owners for one "
        "command; since #969 no agent runs it"
    )


def test_the_wrapper_points_at_the_contract_rather_than_inviting_a_full_run():
    """`bin/test` with no arguments runs the whole suite, which
    contract rule 2 forbids to crafter and proofer. The file
    a session reads before typing it says so, and names where the rule is.

    Re-pointed by #30 from `orchestrator` to `sealer`, and back by #969, which
    moved the run out of every agent: the orchestrator takes it before it
    spawns the sealer, so the comment names that participant and says every
    agent is forbidden it."""
    text = read(os.path.join(BIN, "test"))
    flat = " ".join(text.split())
    assert "agent-contract" in text and "is the orchestrator's" in flat, (
        "bin/test no longer says the full suite is the orchestrator's, so a "
        "segment reading it has nothing telling it not to"
    )
    assert "forbids it to every agent" in flat, (
        "bin/test no longer says no agent runs the full suite"
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


def test_both_wrappers_say_the_same_thing_when_the_runner_is_missing():
    """The case above EXECUTES the POSIX wrapper and is skipped on `nt`, so on
    the one platform the `.cmd` twin runs, nothing reads its sentence. It
    shipped with half of one: the reader was told the copy has no runner and
    never told where to get it. This case reads both files, so it runs
    everywhere."""
    posix = read(os.path.join(BIN, "test"))
    windows = read(os.path.join(BIN, "test.cmd"))
    for fragment in (
        "has no runner beside it",
        "Run it from a clone of the AgenticSeal repository",
    ):
        assert fragment in posix, f"bin/test no longer says: {fragment}"
        assert fragment in windows, (
            f"bin/test.cmd drops what its POSIX twin tells the reader: {fragment}"
        )


def test_ci_installs_the_parser_the_runner_pins():
    """#667, phase 1. The pin is chosen once, in `MARKDOWN_IT`, and CI's
    pytest job installs its own list. A version bumped in one place and not
    the other runs the oracle's cases against two parsers."""
    job = jobs(read_workflow("test.yml"))["pytest"]
    installs = [
        line.split("run:", 1)[1].split()
        for line in job.splitlines()
        if "run: pip install" in line
    ]
    assert installs, "the pytest job installs nothing to compare"
    assert any(rt.MARKDOWN_IT in words for words in installs), installs
    assert not any(
        word.startswith("markdown-it-py") and word != rt.MARKDOWN_IT
        for words in installs
        for word in words
    ), installs
    # #718: Pillow joins the same line, so the pixel pin runs on all three
    # operating systems, at the version the runner pins.
    assert any(rt.PILLOW in words for words in installs), installs
    assert not any(
        word.lower().startswith("pillow") and word != rt.PILLOW
        for words in installs
        for word in words
    ), installs
    # #647: cmarkgfm joins the same line, at the version the runner pins.
    assert any(rt.CMARKGFM in words for words in installs), installs
    assert not any(
        word.lower().startswith("cmarkgfm") and word != rt.CMARKGFM
        for words in installs
        for word in words
    ), installs
    # #841: pytest-split joins the same line, at the version the runner pins.
    # It is CI's alone, so it is not in `PACKAGES` and `bin/test` never
    # installs it.
    assert any(rt.PYTEST_SPLIT in words for words in installs), installs
    assert not any(
        word.lower().startswith("pytest-split") and word != rt.PYTEST_SPLIT
        for words in installs
        for word in words
    ), installs
    assert rt.PYTEST_SPLIT not in rt.PACKAGES, rt.PACKAGES


def test_the_section_names_the_parser_and_where_it_is_pinned():
    """#667, phase 1. `CONTRIBUTING.md` said the suite needs only pytest.
    The sentence now names the parser and the constant that pins it, and the
    fallback commands carry the pin as the runner spells it, so the fallback
    cannot run the oracle against another version either."""
    section = running_the_checks()
    assert "needs only `pytest`" not in section, section
    assert "`markdown-it-py`" in section and "MARKDOWN_IT" in section, section
    assert f"uvx --with pytest --with {rt.MARKDOWN_IT} " in section, section
    assert f"pip install pytest {rt.MARKDOWN_IT} " in section, section
    # #718: Pillow is named beside the parser, with the constant that pins it,
    # and the fallbacks carry its pin too.
    assert "Pillow" in section and "`PILLOW`" in section, section
    # #647: the renderer is named with its constant, and the fallbacks carry
    # its pin after Pillow's.
    assert "`cmarkgfm`" in section and "`CMARKGFM`" in section, section
    assert (
        f"--with {rt.MARKDOWN_IT} --with {rt.PILLOW} --with {rt.CMARKGFM} " in section
    ), section
    assert (
        f"pip install pytest {rt.MARKDOWN_IT} {rt.PILLOW} {rt.CMARKGFM} " in section
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
    assert "bin/test" in section, (
        "`CONTRIBUTING.md` *Running the checks* does not name the runner at all"
    )
    assert section.index("bin/test") < section.index("uvx --with pytest"), (
        "the slow form is still the first command in the section, so it is "
        "still what a reader copies"
    )


def test_the_slow_form_says_what_it_is_for_and_what_it_costs():
    """Kept rather than deleted, because `bin/test` writes a `.venv` into the
    tree and a reader who does not want that needs the other form named. Kept
    without its cost, it reads as an equal alternative."""
    section = running_the_checks()
    assert "fallback" in section, (
        "the uvx form sits in the section as an unlabelled second option"
    )
    assert "seconds each" in section and "every call" in section, (
        "the fallback is named without the cost that demoted it, so the next "
        "reader promotes it back"
    )


def test_the_section_and_the_runner_state_the_same_floor():
    """The document names a version and the code enforces one. Two places
    saying a number is two places to disagree, and the disagreement is
    invisible until somebody's 3.11 builds an environment the suite needs
    3.12 for."""
    section = running_the_checks()
    assert f"Python {rt.FLOOR_TEXT} is the supported floor" in section, (
        "the floor sentence no longer states the floor the runner enforces "
        f"({rt.FLOOR_TEXT} in .github/scripts/run_tests.py's FLOOR)"
    )
    assert "FLOOR" in section, (
        "the sentence names a number the reader cannot trace to the code that holds it"
    )


def test_the_section_states_the_floor_once():
    """The sentence above is worth nothing while a second copy of the number
    sits in the same section untraced. Whichever one a reader finds first is
    the one they edit when the floor moves, and the other stays behind saying
    the old number with nothing pointing at it."""
    section = running_the_checks()
    found = section.count(rt.FLOOR_TEXT)
    assert found == 1, (
        f"the section states {rt.FLOOR_TEXT} {found} times; only the sentence "
        "naming FLOOR carries the number, and the rest refer back to it"
    )


def test_ci_runs_the_suite_at_the_floor_the_runner_holds():
    """`FLOOR`'s comment says the number is also the version CI runs the suite
    at. Nothing read the workflow, so that half was a claim about another file
    which could go stale in silence -- and a floor CI does not run at is a
    floor nothing measures."""
    versions = [
        e.get("python") for e in matrix_include_entries(read_workflow("test.yml"))
    ]
    assert versions, "the pytest job names no python version to compare"
    assert set(versions) == {rt.FLOOR_TEXT}, (
        f"CI runs the suite at {sorted(set(versions))} and the runner's FLOOR "
        f"comment claims {rt.FLOOR_TEXT}"
    )


def test_the_section_keeps_the_broad_once_rule():
    """It predates this work item and a cheap runner is exactly what would
    tempt a session to drop it."""
    section = running_the_checks()
    assert "The broad runs come once" in section


def test_the_section_says_the_full_run_is_the_orchestrators():
    """`bin/test` with no arguments runs the whole suite, which
    contract rule 2 forbids to every agent. The section that makes it cheap is the
    section that has to say who it is for, and name the form a segment
    types.

    Re-pointed by #30 to the `sealer`, and by #969 to the orchestrator,
    which takes the run before it spawns the sealer. The owner is read from
    its own sentence: the word `sealer` alone also matches the section's
    *before the sealer is spawned*, so it held nothing."""
    section = " ".join(running_the_checks().split())
    assert "agent-contract" in section, (
        "the section makes the full suite cheap and says nothing about the "
        "rule that forbids it to a segment"
    )
    assert "The full suite is the orchestrator's" in section, (
        "the section no longer says whose the full suite is"
    )
    assert "bin/test tests/" in section, (
        "no narrow form is shown, so the only command a segment can copy is "
        "the one it must not run"
    )


HANDOFF_LINK = "`docs/the-review-record.md` *The handoff*"


def test_the_protocol_says_a_shipped_runner_is_found_not_typed():
    """#156's cause: the orchestrator typed the runner into every spawn
    prompt, and the segments it forgot rediscovered one."""
    record = flat("docs", "the-review-record.md")
    assert "a runner the repository ships is named, not typed into every prompt" in (
        record
    ), "the handoff still requires the incantation in the prompt, always"


def test_the_protocol_hands_over_the_narrow_form():
    """The requirement points a segment at a command that runs the whole
    suite. Naming it without naming which form is how contract rule 2 gets widened by a
    document that never mentions it."""
    record = flat("docs", "the-review-record.md")
    assert "the form handed over is the narrow one" in record


def test_crafter_finds_the_runner_before_inventing_a_command():
    """The prompt is what went missing, so the fix cannot live in the prompt.
    `agents/crafter.md` reaches every segment at startup with nobody typing
    anything."""
    crafter = flat("agents", "crafter.md")
    assert "Find the runner, and type the narrow form." in crafter, (
        "a segment whose prompt omits the runner has nothing telling it one "
        "exists, which is what the repeats measured"
    )
    assert "run one module at a time" in crafter, (
        "crafter is pointed at a command that runs the full suite and not at "
        "the form contract rule 2 leaves it"
    )
    assert HANDOFF_LINK in crafter, (
        "the rule is restated rather than linked, so the two carriers can drift apart"
    )


def test_proofer_finds_the_runner_before_building_its_own():
    """The class is every segment that runs a test, and the fix reached one of
    them. `agents/proofer.md` told a reviewer to build a `uv` venv in its clone
    and named no runner, so a review round paid for an environment the
    repository already had built -- the same cost, on the segment that runs
    more cases than the crafter does. Both definitions ship to user
    repositories, so neither may name a command that exists only here."""
    proofer = flat("agents", "proofer.md")
    assert "Find the runner before you build your own" in proofer, (
        "the reviewing segment is still told to assemble its own environment "
        "with nothing telling it a shipped runner may exist"
    )
    assert "Type the narrow form, one module" in proofer, (
        "proofer is pointed at a command that runs the full suite and not at "
        "the form contract rule 2 leaves it"
    )
    assert HANDOFF_LINK in proofer, (
        "the rule is restated rather than linked, so the two carriers can drift apart"
    )
    assert "make a `uv` venv inside the clone" in proofer, (
        "the fallback went with the addition — a repository that ships no "
        "runner leaves the reviewer with nothing at all"
    )


@pytest.mark.parametrize("definition", ["crafter.md", "proofer.md"])
def test_no_agent_definition_names_this_repositorys_own_command(definition):
    """`agents/` is copied into every install, so a definition naming
    `bin/test` sends a user's segment after a file their repository does not
    have. The shape both carry instead is the generic one: a wrapper in
    `bin/`, or whatever the contribution guide names first."""
    text = flat("agents", definition)
    assert "bin/test" not in text, (
        f"agents/{definition} names this repository's own runner, and it "
        "ships to repositories that have no such file"
    )


def test_the_cheat_sheet_does_not_offer_the_runner():
    """`bin/` is on a plugin user's PATH, but `test` is a shell builtin, so
    PATH never gets a say. A row in the table that names commands a reader
    types would name the one command there that cannot be typed."""
    readme = read(os.path.join(ROOT, "README.md"))
    sheet = readme[readme.index("## Cheat sheet") :]
    rows = [line for line in sheet.splitlines() if line.startswith("| `")]
    assert not [row for row in rows if "bin/test" in row or "`test" in row], (
        "the cheat sheet offers a command a plugin user cannot type, and "
        "whose runner is this repository's own suite"
    )


def test_the_placement_stands_on_what_it_actually_buys():
    """Phase 1 recorded `.github/` as absent from a plugin cache. It is not:
    the plugin ships from the repository root, and 0.5.0, 0.7.0, 0.8.0 and
    0.8.1 each hold `.github/scripts/`. The location is still right and the
    reason is not, so the file has to carry the true one — otherwise the next
    reader moves the runner to fix a problem that was never there."""
    doc = " ".join(read(SCRIPT).split())
    assert "`.github/` does not" not in doc, (
        "the runner still claims a location hides it from a plugin cache"
    )
    assert "shell builtin" in doc, (
        "the runner does not say what actually keeps a plugin user from "
        "running this suite, so its placement reads as the guard"
    )


def test_no_loaded_document_states_the_serial_figure():
    """A6 (#337). Four carriers stated the suite's cost as *about five
    minutes* with no moment -- the serial figure, and the class
    `seal/follow-up.md` names as *a figure about a corpus, stated with no
    moment*. The measured before-and-after lives in the work item's changelog
    fragment with its date and machine; no loaded document states a figure.
    And the runner's comment no longer WITHHOLDS the flag: it says why it
    used to, which is the record a reader needs when the next flag arrives."""
    runner = " ".join(read(SCRIPT).split())
    assert "No `-n auto`" not in runner, (
        "the runner's comment still withholds the parallel default"
    )
    for name, text in (
        ("bin/test", flat("bin", "test")),
        (".github/scripts/run_tests.py", runner),
        (
            "`CONTRIBUTING.md` *Running the checks*",
            " ".join(running_the_checks().split()),
        ),
    ):
        assert "five minutes" not in text, f"{name} states the serial figure"
