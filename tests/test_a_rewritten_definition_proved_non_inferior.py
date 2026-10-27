"""The committed warden cases of the behaviour suite: no location one of a
case's truths accepts is accepted by another, so one finding is never
counted as two. The case reads the cases under `evals/behaviour/proofer/`.

#942's phase 6 placed the generators' cases in their files:
`evals/scripts/replay_targets.py`'s in `tests/test_replay_targets.py`,
`rule_cases.py`'s in `tests/test_rule_cases.py` and `seed_defects.py`'s in
`tests/test_seed_defects.py`. `evals/scripts/noninferiority.py`'s are in
`tests/test_noninferiority.py`.
"""

import os
import re

from test_rule_cases import truth_regex

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))

# An alternative of a generated truth's pattern: an escaped path and the
# line list it accepts, or a bare escaped path.
OPTION = re.compile(
    r"((?:[\w-]|\\[./-])+):\(\?:([\d|]+)\)\(\?!\\d\)|((?:[\w-]|\\[./-])+)\(\?!\["
)


def test_no_two_truths_of_a_warden_case_accept_one_location():
    """Guards #971 round 1 finding 1: a `location:` line one truth of a
    committed warden case accepts is accepted by no other truth of that
    case, so one finding is never counted as two. Every line each
    generated alternative lists is tried against every other truth."""
    root = os.path.join(ROOT, "evals", "behaviour", "proofer")
    shared = []
    for case in sorted(os.listdir(root)):
        graders = os.path.join(root, case, "graders")
        truths = {}
        for name in sorted(os.listdir(graders)):
            if name.startswith("truth-"):
                with open(os.path.join(graders, name), encoding="utf-8") as f:
                    truths[name] = truth_regex(name, f.read())
        for name, found in truths.items():
            for m in OPTION.finditer(found.pattern):
                path = (m[1] or m[3]).replace("\\", "")
                for n in m[2].split("|") if m[2] else [None]:
                    row = f"location: `{path}:{n}`" if n else f"location: `{path}`"
                    others = [
                        o for o, g in truths.items() if o != name and g.search(row)
                    ]
                    if others:
                        shared.append((case, name, row, others))
    assert not shared, shared[:3]
