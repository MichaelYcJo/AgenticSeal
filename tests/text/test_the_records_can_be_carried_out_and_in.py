"""`iadd export` and `iadd import`: the READMEs that name them.

The cases of `skills/implement/scripts/iadd.py` are in `tests/skills/test_iadd.py`,
and the three of `normalise_remote`, which `iadd.py` re-exports from
`lib/config.py`, are in `tests/lib/test_config.py`. The two cases here read
the READMEs.
"""

import os

import pytest
from conftest import ROOT

# No TARGET: its cases hold iadd export and iadd import across the READMEs and the `agentory/` README with its template.


@pytest.mark.parametrize("readme", ["README.md", "README.ko.md"])
def test_both_readmes_carry_the_pair_and_the_rule_that_makes_it_safe(readme):
    """`CONTRIBUTING.md`: both READMEs move together, and they must tell the
    same story about what exists.

    Where a collision lands is asserted beside the command names, because a
    reader has to know it before running `import` on a clone that already
    holds records.
    """
    with open(os.path.join(ROOT, readme), encoding="utf-8") as handle:
        text = handle.read()
    # The two commands a reader runs.
    assert "iadd export" in text and "iadd import" in text
    # The suffix of the path a colliding record lands at, which a reader
    # opens.
    assert ".incoming" in text, f"{readme} does not say where a collision lands"


def test_the_root_readme_and_its_template_say_it_too():
    """The template is what a first setup bootstraps a user's root from, and
    `tests/behaviour/test_first_setup_asks_once.py` asserts the two are byte-identical —
    so the rule lands in every repository that opts in, not only this one."""
    for parts in (
        ("agentory", "README.md"),
        ("templates", "setup", "agentory-README.md"),
    ):
        with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
            text = handle.read()
        # The two commands a reader runs.
        assert "iadd export" in text and "iadd import" in text, "/".join(parts)
        # The file name of the state that must not travel, which a reader
        # leaves out of a copy.
        assert "iadd-last-export.json" in text, (
            "/".join(parts) + " does not name the state that must not travel"
        )
