"""`seal export` and `seal import`: what is left here after #942's phase 5.

The cases of `skills/implement/scripts/seal.py` are in `tests/test_seal.py`.
Two kinds stay in this file. The three cases of `normalise_remote` pin how
`hooks/config.py` reduces a remote URL, which `seal.py` reaches through an
alias, and they wait for the phase that rebuilds `hooks/config.py`. The two
README cases read prose, and they are #923's.
"""

import importlib.util
import os

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "implement", "scripts", "seal.py")


@pytest.fixture
def seal():
    spec = importlib.util.spec_from_file_location("specseal_seal", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    "left,right",
    [
        ("git@example.com:org/repo.git", "https://example.com/org/repo"),
        ("ssh://git@example.com/org/repo.git", "https://example.com/org/repo/"),
        ("HTTPS://Example.com/Org/Repo.git", "https://example.com/org/repo"),
    ],
)
def test_remote_urls_reduce_to_host_and_path(seal, left, right):
    assert seal.normalise_remote(left) == seal.normalise_remote(right)


def test_a_port_is_not_read_as_an_scp_separator(seal):
    """The colon becomes `/` only where there was no scheme. Otherwise
    `https://example.com:8443/x` reduces to `example.com/8443/x`, and two
    ports of one host stop comparing equal to themselves."""
    assert seal.normalise_remote("https://example.com:8443/org/repo") == (
        "example.com:8443/org/repo"
    )


def test_two_different_repositories_do_not_reduce_to_one(seal):
    """The direction the normalisation must not be wrong in."""
    assert seal.normalise_remote("git@example.com:org/a.git") != seal.normalise_remote(
        "git@example.com:org/b.git"
    )
    assert seal.normalise_remote("git@example.com:org/a") != seal.normalise_remote(
        "git@other.example:org/a"
    )


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
    for parts in (("seal", "README.md"), ("templates", "seal-README.md")):
        with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
            text = handle.read()
        assert "seal export" in text and "seal import" in text, "/".join(parts)
        assert "specseal-last-export.json" in text, (
            "/".join(parts) + " does not name the state that must not travel"
        )
