"""No case: `.github/scripts/gather_changelog.py` is gone, held until work item 1793188384's settle.

Work item 1793188384-the-release-notes-are-kept-twice (#1053) removed the
gather script, `changelog/` and `CHANGELOG.md`: the release note is built at
the tag from the fragments the release's commits added
(`tests/github/test_publish_release_note.py`). Every case here ran the
script, so none is left to run.

`docs/the-record-layout.md` and `docs/release-checklist.md` still name this
file on their `check:` lines, and `docs/release-checklist.md` names the
marker `second-gather-appends`. The policy root changes only at the settle
that writes that work item's `## Rule changes`, and `seal rules --check`
refuses a target that does not resolve. So the file stays with no case
until then, and the marker is carried by a class with no case. Nothing
removes the file on its own, because `settle` touches no file under
`tests/`: the pull request that settles that work item deletes it.
"""

import pytest


@pytest.mark.rule("second-gather-appends")
class Test_second_gather_appends:
    """`docs/release-checklist.md` *2. Gather, bump*: a second gather for the
    same version appended into its section. No gather is left to run twice."""
