"""`hooks/lib/gate.py`, whether a change reaches outside the document roots, one
class per function.

`chain_check.py#originals_of` asks it of the paths a pull request changes;
its cases over a pull request are `tests/test_chain_check.py`'s
`Test_originals_of`. The commit gate's arms that lived here went with #1027.
"""

import pytest
from conftest import census_case, load_hook_module

TARGET = "hooks/lib/gate.py"

gate = load_hook_module("lib/gate.py", "gate_under_test")


class Test_touches_code:
    @pytest.mark.parametrize(
        "paths",
        [None, ["src/a.py"], ["docs/a.md", "f.txt"], ["documentation/a.md"]],
        ids=["git could not list", "code", "one path outside", "a near-miss root"],
    )
    def test_accepts_a_path_outside_the_document_roots_or_no_list_as_code(self, paths):
        """A change git could not list is not one confined to the roots
        (#868), and a root is matched with its slash."""
        assert gate.touches_code(paths) is True

    @pytest.mark.parametrize(
        "paths",
        [[], ["docs/a.md"], ["seal/threads/x/trail/rounds/round-1.md", "docs/b.md"]],
    )
    def test_refuses_a_change_confined_to_docs_and_seal_as_code(self, paths):
        assert gate.touches_code(paths) is False


test_census = census_case(TARGET)
