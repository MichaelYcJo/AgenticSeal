"""No behaviour case tells the agent under test that the run is an evaluation.

The agent is shown a case's `prompt.md` and works in the repository its
`scaffold.sh` builds, so neither file holds a word that names the run as a
measurement (#1042). The words are refused at the start of a word, in any
case, as the stems `STEMS` lists: `evaluated`, `graders`, `judged` and
`scenarios` are refused with their stems. `evals/README.md` *The behaviour
suite* states the rule.

One kind of text is exempt, for its reason below, and nothing else is: the
record shapes this plugin's own templates write. A replay or seeded case is
not read at all. It is the record of a run at a recorded commit, which
`tests/censuses.py#RECORDED_CASE` passes over whole too, and its bytes stay
as that run read them.
"""

import os
import re

from censuses import RECORDED_CASE
from conftest import ROOT

SUITE = os.path.join(ROOT, "evals", "behaviour")
FILES = ("prompt.md", "scaffold.sh")

STEMS = ("eval", "grader", "judg", "fixture", "scenario")
REFUSED = re.compile(r"(?<![a-z])(?:" + "|".join(STEMS) + r")[a-z]*", re.I)

# The record shapes a scaffold copies from this plugin's templates, as whole
# lines. The first two are `templates/records/sdd-design.md`'s scenario
# heading and its table header; the third is `templates/records/sdd-round.md`'s
# heading. A record written in the plugin's shape is what the agent meets in
# production too.
RECORD_LINES = (
    "## User scenarios & acceptance *(mandatory)*",
    "| Scenario | Given / When / Then | Verifiable how |",
    "## Not judged",
)


def hits(suite):
    """`[(path relative to SUITE, line, word)]` for every refused word in a
    case file under SUITE outside a record shape. A replay or seeded case is
    passed over whole, as `RECORDED_CASE` reads its path under
    `evals/behaviour/`."""
    found = []
    for path in case_files(suite):
        rel = os.path.relpath(path, suite)
        if RECORDED_CASE.match("evals/behaviour/" + rel.replace(os.sep, "/")):
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        for n, line in enumerate(text.split("\n"), 1):
            if line in RECORD_LINES:
                continue
            for m in REFUSED.finditer(line):
                found.append((rel, n, m.group()))
    return found


def case_files(suite):
    """Every `prompt.md` and `scaffold.sh` of a case under SUITE, sorted."""
    return sorted(
        os.path.join(directory, name)
        for directory, _dirs, names in os.walk(suite)
        for name in names
        if name in FILES
    )


def test_no_case_file_holds_a_refused_word():
    """Guards S4: no `prompt.md` and no `scaffold.sh` under
    `evals/behaviour/` holds a refused word outside a record shape and a
    recorded case; each hit is named by its file, line and word."""
    assert case_files(SUITE), "no case file was read under evals/behaviour/"
    found = hits(SUITE)
    assert found == [], "\n".join(f"{p}:{n}: {word}" for p, n, word in found)


def test_a_rule_cases_word_is_named_and_a_recorded_case_is_not_read(tmp_path):
    """Guards #1487 S8: a refused word in a rule case's `prompt.md` is named
    by its file, line and word, and the same word in a replay or a seeded
    case is not read, since each is the record of a run at a recorded
    commit."""
    text = "Review the build.\nThe round is judged.\n"
    for case in ("rule-proofer-x", "replay-1-r2", "seeded-1a2b3c4d"):
        folder = tmp_path / "proofer" / case
        folder.mkdir(parents=True)
        (folder / "prompt.md").write_text(text, encoding="utf-8")
    assert hits(str(tmp_path)) == [
        (os.path.join("proofer", "rule-proofer-x", "prompt.md"), 2, "judged")
    ]
