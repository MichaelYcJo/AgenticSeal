"""A repository whose own `seal/` is a package keeps its records shared,
under `agentic-seal/` (#1059).

The one case here runs `seal rules --check` in a repository whose `seal/` is
a Python package with no marker in its `README.md`, beside a root at
`agentic-seal/`; it is named by the scenario of #1059's `frame/design.md` it
holds, S5, every other check. The world it is built in, the `package` and
`shared` fixtures, is `tests/conftest.py`'s. The cases of every other
command run in that world stand in each command's module file under
`tests/skills/`, and the resolver's order itself is `tests/lib/test_optin.py`'s.
"""

from conftest import ITEM, write
from test_rules import HELD, TESTS, doc, rule, rules
from test_seal import configured


def test_s5_rules_check_excuses_a_section_a_design_under_agentic_seal_removes(
    shared, capsys
):
    """`seal rules --check` reads the designs under `agentic-seal/threads/`
    and the `Policy root` key of `agentic-seal/config.json`: a refused `check:`
    line in a section a design there removes is excused and named by its
    path under the root."""
    configured(shared / "agentic-seal", ("Policy root", "policy"))
    write(shared, HELD, TESTS)
    write(shared, "policy/a.md", doc(rule("check: tests/test_gone.py")))
    write(
        shared / "agentic-seal" / "threads" / ITEM,
        "frame/design.md",
        "# Design\n\n## Rule changes\n\n- remove\n  file: policy/a.md\n"
        "  section: The heading\n",
    )
    code = rules.main(["--check", "--root", str(shared)])
    out = capsys.readouterr().out
    assert code == 0, out
    assert (
        "seal rules: excused: policy/a.md:6: The heading: tests/test_gone.py does "
        f"not exist; agentic-seal/threads/{ITEM}/ removes this section at the "
        "settle\n"
    ) in out, out
