"""`lib/gate.py`, whether a change reaches outside the document roots, one
class per function.

`chain_check.py#originals_of` asks it of the paths a pull request changes;
its cases over a pull request are `tests/skills/test_chain_check.py`'s
`Test_originals_of`. The commit gate's arms that lived here went with #1027.
"""

import pytest
from conftest import census_case, load_lib_module

TARGET = "lib/gate.py"

gate = load_lib_module("gate.py", "gate_under_test")


class Test_touches_code:
    @pytest.mark.parametrize(
        "paths",
        [None, ["src/a.py"], ["docs/a.md", "f.txt"], ["documentation/a.md"]],
        ids=["git could not list", "code", "one path outside", "a near-miss root"],
    )
    def test_accepts_a_path_outside_the_document_roots_or_no_list_as_code(self, paths):
        """A change git could not list is not one confined to the roots
        (#868), and a root is matched with its slash."""
        assert gate.touches_code(paths, "seal") is True

    @pytest.mark.parametrize(
        "paths",
        [[], ["docs/a.md"], ["seal/threads/x/trail/rounds/round-1.md", "docs/b.md"]],
    )
    def test_refuses_a_change_confined_to_docs_and_seal_as_code(self, paths):
        assert gate.touches_code(paths, "seal") is False

    @pytest.mark.parametrize(
        "home, paths, code",
        [
            ("agentic-seal", ["agentic-seal/threads/x/routing.md", "docs/a.md"], False),
            ("agentic-seal", ["seal/__init__.py"], True),
            ("", ["seal/threads/x/routing.md"], True),
            ("", ["docs/a.md"], False),
        ],
        ids=["the second name", "a project's own seal", "no root", "no root, docs"],
    )
    def test_reads_the_root_by_the_name_it_is_given(self, home, paths, code):
        """#1059: the records root is the name the caller resolved, so a
        project's own `seal/` beside `agentic-seal/` is code, and with no
        root in the tree `docs/` is the one document root."""
        assert gate.touches_code(paths, home) is code


test_census = census_case(TARGET)
