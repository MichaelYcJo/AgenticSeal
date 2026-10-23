"""A unit of a file is bounded where a real parser decides its extent, and
named by content (#870, #519, #867).

`skills/verify/scripts/coordinates.py`'s cases moved to
`tests/test_coordinates.py` in #942's phase 6. The one left here reads this
repository's workflow, which is #923's to place. `docs/the-pact.md` names this
file on a `check:` line until the settle after the release applies
`spec.md`'s item for it.
"""

import os

from test_coordinates import RUBY, ec, places

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def test_a_quoted_line_resolves_in_any_file():
    """The quoted line needs no rule, so it resolves in a refused suffix and
    in this repository's own workflow, whose `pytest` job holds no blank line
    from its key to its last step."""
    assert places("svc.rb", '"def render"', RUBY) == [(1, 3)]
    assert ec.resolve_unit("svc.rb", '"def render"', RUBY).refused is None
    rel = ".github/workflows/test.yml"
    text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
    lines = ec.gfm_lines(text)
    (place,) = places(rel, '"pytest:"', text)
    start, end = place
    assert lines[start - 1].strip() == "pytest:", place
    assert all(line.strip() for line in lines[start - 1 : end]), place
    assert end == len(lines) or not lines[end].strip(), place
    assert end - start > 10, place
