"""`seal export` and `seal import`: what is left here after #942.

The cases of `skills/implement/scripts/seal.py` are in `tests/test_seal.py`,
and the three of `normalise_remote`, which `seal.py` re-exports from
`hooks/config.py`, are in `tests/test_config.py`. The two README cases left
here read prose, and they are #923's.
"""

import os

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


@pytest.mark.parametrize("readme", ["README.md", "README.ko.md"])
def test_both_readmes_carry_the_pair_and_the_rule_that_makes_it_safe(readme):
    """`CONTRIBUTING.md`: both READMEs move together, and they must tell the
    same story about what exists. Until this work item they both said the pair
    arrives with #81.

    The never-overwrite rule is asserted rather than just the command names,
    because that is the property a reader has to know before running `import`
    on a clone that already holds records — a command that quietly merged
    would be reported the same way by a README that only lists it.
    """
    with open(os.path.join(ROOT, readme), encoding="utf-8") as handle:
        text = handle.read()
    assert "seal export" in text and "seal import" in text
    assert ".incoming" in text, f"{readme} does not say where a collision lands"
    assert "#81" not in text, (
        f"{readme} still calls the pair later work, and it is here"
    )


def test_the_root_readme_and_its_template_say_it_too():
    """The template is what a first setup bootstraps a user's root from, and
    `tests/test_first_setup_asks_once.py` asserts the two are byte-identical —
    so the rule lands in every repository that opts in, not only this one."""
    for parts in (("seal", "README.md"), ("templates", "setup", "seal-README.md")):
        with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
            text = handle.read()
        assert "seal export" in text and "seal import" in text, "/".join(parts)
        assert "agentic-last-export.json" in text, (
            "/".join(parts) + " does not name the state that must not travel"
        )
