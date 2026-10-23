"""How `hooks/cmdline.py` reads two shapes the commit gate's corpus of leaks
turned up.

The corpus itself, the shapes measured to leak the last time the reading was
narrowed (work items `1790635415` and `1790660768`), is
`tests/test_commit_review_gate.py::Test_main::test_refuses_each_shape_the_base_stops`
and the classes beside it since #942's phase 5, one `main` call per row in a
world built once. The two cases left here read `cmdline` with no git, for the
phase of #942 that rebuilds that module. `docs/commit-review-gate-spec.md`
still names this file for the rule the corpus holds.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hooks"))
import cmdline

BODY = "git commit -m x"


@pytest.mark.parametrize("header", ["case a in a) ", "f() { ", "coproc "])
def test_past_the_header_bound_the_reading_stops(header):
    """Round 1 of 1790660768, red 2. Past `HEADERS_READ` headers, one inside
    the next, both header readings answer in the stopping direction; one
    header fewer, the same segment is read to its end and names nothing."""

    bound = cmdline.HEADERS_READ
    for depth, expected in ((bound - 1, False), (bound, True)):
        tokens = (header * depth + "true watch").split()
        assert cmdline._is_the_program(tokens, len(tokens) - 1) is expected, depth
        assert cmdline.names_an_unknown_command(header * depth + "true") is expected


@pytest.mark.parametrize("cd", ["cd u2 2>&1", "cd u2 >|f", "cd u2 >&2"])
def test_a_cd_the_splitter_cut_after_its_operand_lands_once(tmp_path, cd):
    """Round 2 of 1790660768's fix pass. In `cd W 2>&1` the splitter's first
    part is `cd W 2>`, which lands in W on its own words. The group's glued
    view landed it again from there, and the walk named W/W, a directory the
    command never reaches."""
    items = cmdline.split_segments_with_separators(f"{cd} && {BODY}")[0]
    here = str(tmp_path)
    wheres = [w for t, w in cmdline.walk_directories(items, here) if t[:1] == ["git"]]
    assert wheres, cd
    named = [str(w) for w in wheres[0]]
    landed = [str(w) for w in wheres[0] if not isinstance(w, cmdline.Unresolved)]
    assert os.path.join(here, "u2") in landed, (cd, named)
    assert os.path.join(here, "u2", "u2") not in named, (cd, named)
