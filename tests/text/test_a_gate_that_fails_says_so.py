"""A gate that fails to load says so (#28).

Work item 1790635415. The cases of `hooks/dispatch.py`'s failure report moved
to `tests/hooks/test_dispatch.py` (#942's phase 6). What stays is the case that
reads the policy, which `docs/the-session-hooks.md` *Registration* names
on its `check:` line.
"""

import os

from conftest import ROOT

# --- S14: the policy says it, and names what enforces it -----------------------


def test_the_registration_section_says_a_failure_is_said_and_names_its_case():
    """S14. `docs/the-session-hooks.md` *Registration* says a raising gate is
    skipped and the skip is said, and its `check:` line names this module."""
    path = os.path.join(ROOT, "docs", "the-session-hooks.md")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    start = text.index("## Registration\n")
    section = text[start : text.index("\n## ", start + 1)]
    flat_text = " ".join(section.split())
    assert (
        "**A gate that fails is said once per session, at the end of the main "
        "session's turn, and the call it failed on still goes ahead.**"
    ) in flat_text, section
    enforced = [ln for ln in section.splitlines() if ln.startswith("check: ")]
    assert any(
        "tests/text/test_a_gate_that_fails_says_so.py" in ln.split() for ln in enforced
    ), enforced
