"""The eval suite's shape, as `claude plugin eval` reads it.

A case is any directory under `evals/` holding `case.yaml` or `prompt.md`,
at any depth, which is how the runner finds `<eval dir>/**/case.yaml`. These
assertions cost nothing and hold every case to the layout the runner reads,
so a malformed case fails here rather than at the run that costs money.

The behaviour suite under `evals/behaviour/<agent>/` is held to the layout
measured on the runner (2.1.296): `max_turns`, `timeout_seconds`, `model`
and `allowed_tools` under `execution:`, where a top-level copy is dropped;
`context.scaffold_script` a path to a file beside `case.yaml`; one grader
per file, its name prefixed by its kind for `evals/scripts/noninferiority.py`.
"""

import glob
import os
import re

EVALS = os.path.join(os.path.dirname(__file__), "..", "evals")
BEHAVIOUR = os.path.join(EVALS, "behaviour")

REQUIRED = ("schema_version", "name", "runs", "max_turns", "timeout_seconds", "model")
EXECUTION = ("max_turns", "timeout_seconds", "model", "allowed_tools")
KINDS = ("reach", "shape", "truth")


def case_dirs():
    """Every directory under `evals/` holding a case file, at any depth."""
    found = set()
    for name in ("case.yaml", "prompt.md"):
        for path in glob.glob(os.path.join(EVALS, "**", name), recursive=True):
            if f"{os.sep}results{os.sep}" not in path:
                found.add(os.path.dirname(path))
    return sorted(found)


def flat_cases():
    top = os.path.normpath(EVALS)
    return [d for d in case_dirs() if os.path.dirname(os.path.normpath(d)) == top]


def behaviour_cases():
    top = os.path.normpath(BEHAVIOUR)
    return [d for d in case_dirs() if os.path.normpath(d).startswith(top + os.sep)]


def rel(d):
    return os.path.relpath(d, EVALS)


def top_level_keys(path):
    """`key:` at column zero — enough to check presence without a YAML dep."""
    keys = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line[:1].isalpha() and ":" in line:
                keys.append(line.split(":", 1)[0].strip())
    return keys


def block_keys(path, block):
    """`key:` two spaces in under the top-level `block:` line."""
    keys, inside = [], False
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line[:1].isalpha():
                inside = line.startswith(f"{block}:")
                continue
            m = re.match(r"^  (\w+):", line)
            if inside and m:
                keys.append(m.group(1))
    return keys


def test_every_case_declares_a_case_yaml_and_a_prompt():
    missing = []
    for d in case_dirs():
        for name in ("case.yaml", "prompt.md"):
            if not os.path.isfile(os.path.join(d, name)):
                missing.append(f"{rel(d)}/{name}")
    assert not missing, missing


def test_every_flat_case_yaml_carries_the_required_fields():
    gaps = []
    for d in flat_cases():
        path = os.path.join(d, "case.yaml")
        if not os.path.isfile(path):
            continue
        keys = top_level_keys(path)
        for field in REQUIRED:
            if field not in keys:
                gaps.append(f"{rel(d)}: {field}")
    assert not gaps, gaps


def test_a_behaviour_case_sets_its_bounds_where_the_runner_reads_them():
    """A bound at the top level is dropped, and the run takes the default."""
    gaps = []
    for d in behaviour_cases():
        path = os.path.join(d, "case.yaml")
        top = top_level_keys(path)
        inner = block_keys(path, "execution")
        for field in ("schema_version", "name", "runs"):
            if field not in top:
                gaps.append(f"{rel(d)}: {field}")
        for field in EXECUTION:
            if field not in inner:
                gaps.append(f"{rel(d)}: execution.{field}")
            if field in top:
                gaps.append(
                    f"{rel(d)}: {field} at the top level, where the runner drops it"
                )
    assert behaviour_cases(), "the behaviour suite holds no case"
    assert not gaps, gaps


def test_a_behaviour_scaffold_is_a_file_beside_its_case():
    """The runner reads `scaffold_script` as a path, and refuses an inline
    script as a path that does not exist."""
    gaps = []
    for d in behaviour_cases():
        path = os.path.join(d, "case.yaml")
        if block_keys(path, "context") != ["scaffold_script"]:
            gaps.append(f"{rel(d)}: context holds more or less than scaffold_script")
        with open(path, encoding="utf-8") as f:
            m = re.search(r"^  scaffold_script: (\S+)$", f.read(), re.M)
        if not m or not os.path.isfile(os.path.join(d, m.group(1))):
            gaps.append(f"{rel(d)}: scaffold_script names no file beside the case")
    assert not gaps, gaps


def test_a_behaviour_grader_names_its_kind():
    gaps = []
    for d in behaviour_cases():
        for path in glob.glob(os.path.join(d, "graders", "*.md")):
            if os.path.basename(path).split("-", 1)[0] not in KINDS:
                gaps.append(f"{rel(d)}/graders/{os.path.basename(path)}")
    assert not gaps, gaps


def test_a_tool_used_grader_bounded_at_zero_can_pass():
    """The runner's `min` defaults to 1, so `max: 0` without `min: 0` reads
    `expected 1..0` and fails every run: every one of the framer baseline's
    eight runs failed its four such graders."""
    gaps = []
    for d in behaviour_cases():
        for path in glob.glob(os.path.join(d, "graders", "*.md")):
            with open(path, encoding="utf-8") as f:
                head = f.read().split("---")[1]
            if re.search(r"^max: 0$", head, re.M) and not re.search(
                r"^min: 0$", head, re.M
            ):
                gaps.append(f"{rel(d)}/graders/{os.path.basename(path)}")
    assert not gaps, gaps


def test_a_behaviour_prompt_says_where_the_repository_is():
    """The plugin under test sits in a directory the session can see, and it
    is itself a SpecSeal repository: two of six sealer runs ran the gate
    there and one handed back that failure. Each prompt names the working
    directory as the repository."""
    gaps = []
    for d in behaviour_cases():
        with open(os.path.join(d, "prompt.md"), encoding="utf-8") as f:
            text = f.read()
        if not re.search(
            r"(?:repository|clone) is the current (?:working )?directory", text
        ):
            gaps.append(rel(d))
    assert not gaps, gaps


def test_the_prompt_holds_the_prompt_and_nothing_else():
    """Config lives in case.yaml. One case kept its config in the prompt's
    frontmatter, where the runner does not look for it."""
    offenders = []
    for d in case_dirs():
        with open(os.path.join(d, "prompt.md"), encoding="utf-8") as f:
            if f.read().startswith("---"):
                offenders.append(rel(d))
    assert not offenders, offenders


def test_every_case_has_at_least_one_grader():
    empty = [
        rel(d) for d in case_dirs() if not glob.glob(os.path.join(d, "graders", "*.md"))
    ]
    assert not empty, empty


def test_the_readme_names_every_flat_case_and_the_behaviour_suite():
    with open(os.path.join(EVALS, "README.md"), encoding="utf-8") as f:
        readme = f.read()
    unlisted = [rel(d) for d in flat_cases() if rel(d) not in readme]
    assert not unlisted, unlisted
    assert "behaviour/" in readme
