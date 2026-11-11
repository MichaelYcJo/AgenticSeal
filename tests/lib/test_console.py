"""`lib/console.py`: a console a script cannot encode to must not turn
it into a silent pass.

The failure this holds is not "a message came out wrong". It is that a
script which raises while reading or printing dies with **stdout empty**, and
empty stdout is how a script run for its output says "nothing to see here".
The case of the stamp's drawer on such a console, the script the plugin's
`Stop` hook runs, is
`tests/skills/test_seal_stamp.py#Test_main.test_the_plugins_stop_command_draws_on_a_console_it_cannot_encode_to`.
"""

import io
import sys

import pytest
from conftest import census_case, load_lib_module

TARGET = "lib/console.py"

# `annotate` came here from `unverified_check.py` (#1482), and its cases
# with it.
console = load_lib_module("console.py", "console_for_its_own_file")


def cp949_stream():
    """A text stream a Korean Windows console would hand the process."""
    return io.TextIOWrapper(io.BytesIO(), encoding="cp949", errors="strict")


class Test_to_utf8:
    def test_accepts_each_of_the_three_streams_and_makes_it_utf8(self, monkeypatch):
        """The streams are stand-ins, so the verdict is the same whatever
        console the case runs under."""
        console = load_lib_module("console.py", "console_for_to_utf8")
        streams = {name: cp949_stream() for name in ("stdin", "stdout", "stderr")}
        for name, stream in streams.items():
            monkeypatch.setattr(sys, name, stream)
        console.to_utf8()
        said = {name: (s.encoding, s.errors) for name, s in streams.items()}
        assert said == {
            "stdin": ("utf-8", "replace"),
            "stdout": ("utf-8", "replace"),
            "stderr": ("utf-8", "backslashreplace"),
        }

    def test_refuses_to_raise_on_a_stream_that_is_absent_or_cannot_reconfigure(
        self, monkeypatch
    ):
        console = load_lib_module("console.py", "console_for_absent_streams")
        stderr = cp949_stream()
        monkeypatch.setattr(sys, "stdin", None)
        monkeypatch.setattr(sys, "stdout", io.StringIO())
        monkeypatch.setattr(sys, "stderr", stderr)
        console.to_utf8()
        assert (stderr.encoding, stderr.errors) == ("utf-8", "backslashreplace")


class Test_annotate:
    def test_accepts_a_path_as_git_spells_it_in_ci_and_plain_elsewhere(
        self, monkeypatch
    ):
        monkeypatch.setenv("GITHUB_ACTIONS", "true")
        assert (
            console.annotate("error", "a/b.md", 3, "m")
            == "::error file=a/b.md,line=3::m"
        )
        monkeypatch.delenv("GITHUB_ACTIONS")
        assert console.annotate("error", "a/b.md", 3, "m") == "a/b.md:3  m"

    @pytest.mark.parametrize("in_ci, line", [(True, "::notice::m"), (False, "m")])
    def test_refuses_to_name_a_path_it_was_not_given(self, monkeypatch, in_ci, line):
        if in_ci:
            monkeypatch.setenv("GITHUB_ACTIONS", "true")
        assert console.annotate("notice", None, 1, "m") == line


test_census = census_case(TARGET)
