"""The eval suite's shape, as `claude plugin eval` reads it.

A case is any directory under `evals/` holding `case.yaml` or `prompt.md`,
at any depth, which is how the runner finds `<eval dir>/**/case.yaml`. These
assertions cost nothing and hold every case to the layout the runner reads,
so a malformed case fails here rather than at the run that costs money.

Every case is held to the schema measured on the runner (2.1.296):
`max_turns`, `timeout_seconds`, `model` and `allowed_tools` under
`execution:`, where a top-level copy is dropped; `context.scaffold_script` a
path to a file beside `case.yaml`, where an inline script is refused. The
behaviour suite under `evals/behaviour/<agent>/` adds what
`evals/scripts/noninferiority.py` reads: a scaffold in every case, one grader
per file with its name prefixed by its kind, and a prompt naming the
repository.
"""

import glob
import importlib.util
import os
import re

EVALS = os.path.join(os.path.dirname(__file__), "..", "evals")

TOP = ("schema_version", "name", "runs")
EXECUTION = ("max_turns", "timeout_seconds", "model", "allowed_tools")
KINDS = ("reach", "shape", "truth")


def case_dirs(root=EVALS):
    """Every directory under ROOT holding a case file, at any depth."""
    found = set()
    for name in ("case.yaml", "prompt.md"):
        for path in glob.glob(os.path.join(root, "**", name), recursive=True):
            if f"{os.sep}results{os.sep}" not in path:
                found.add(os.path.dirname(path))
    return sorted(found)


def behaviour_cases(root=EVALS):
    top = os.path.normpath(os.path.join(root, "behaviour"))
    return [d for d in case_dirs(root) if os.path.normpath(d).startswith(top + os.sep)]


def rel(d, root=EVALS):
    return os.path.relpath(d, root)


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


def bound_gaps(root=EVALS):
    """Each case's fields where the runner reads them. A bound at the top
    level is dropped, and the run takes 10 turns and 300 s."""
    gaps = []
    for d in case_dirs(root):
        path = os.path.join(d, "case.yaml")
        if not os.path.isfile(path):
            continue
        top = top_level_keys(path)
        inner = block_keys(path, "execution")
        for field in TOP:
            if field not in top:
                gaps.append(f"{rel(d, root)}: {field}")
        for field in EXECUTION:
            if field not in inner:
                gaps.append(f"{rel(d, root)}: execution.{field}")
            if field in top:
                gaps.append(
                    f"{rel(d, root)}: {field} at the top level, where the runner drops it"
                )
    return gaps


def scaffold_gaps(root=EVALS):
    """The runner reads `scaffold_script` as a path, and refuses an inline
    script as a path that does not exist. A behaviour case carries one,
    because every agent works in a fixture repository."""
    gaps = []
    behaviour = set(behaviour_cases(root))
    for d in case_dirs(root):
        path = os.path.join(d, "case.yaml")
        if not os.path.isfile(path):
            continue
        context = block_keys(path, "context")
        if d in behaviour and context != ["scaffold_script"]:
            gaps.append(
                f"{rel(d, root)}: context holds more or less than scaffold_script"
            )
        if d in behaviour or "scaffold_script" in context:
            with open(path, encoding="utf-8") as f:
                m = re.search(r"^  scaffold_script: (\S+)$", f.read(), re.M)
            if not m or not os.path.isfile(os.path.join(d, m.group(1))):
                gaps.append(
                    f"{rel(d, root)}: scaffold_script names no file beside the case"
                )
    return gaps


def sealer_grade_gaps(root=EVALS):
    """Each sealer case that does not grade the guarantor's file, or that
    still grades the old sealer's `Broad gate` cell. The sealer's outcome is
    its verdict in `guarantee.md`; `broad-gate.md` is the script's (#923)."""
    gaps = []
    top = os.path.normpath(os.path.join(root, "behaviour", "sealer"))
    cases = [d for d in case_dirs(root) if os.path.normpath(d).startswith(top + os.sep)]
    if not cases:
        return ["behaviour/sealer: no case"]
    for d in cases:
        graders = []
        for path in glob.glob(os.path.join(d, "graders", "*.md")):
            with open(path, encoding="utf-8") as f:
                graders.append(f.read().split("---")[1])
        if not any(
            re.search(r"path: '[^']*/guarantee\.md'", g) and "^Verdict:" in g
            for g in graders
        ):
            gaps.append(f"{rel(d, root)}: no grader reads the verdict in guarantee.md")
        if any("Broad gate" in g for g in graders):
            gaps.append(f"{rel(d, root)}: a grader reads the `Broad gate` cell")
        if not any(
            re.search(r"^tool: 'Bash'$", g, re.M)
            and re.search(r"^input_match: 'broad-gate\\s\+--base'$", g, re.M)
            and re.search(r"^max: 0$", g, re.M)
            for g in graders
        ):
            gaps.append(f"{rel(d, root)}: no grader bounds `broad-gate --base` at zero")
    return gaps


def test_every_sealer_case_grades_the_guarantee():
    """T18. A sealer case grades the verdict line of `guarantee.md`, and none
    grades the `Broad gate` cell the sealer no longer writes.

    #969 T6: every sealer case also bounds a Bash `broad-gate --base` at zero
    calls. The gate is the orchestrator's run before the spawn, and a sealer
    that runs it again passes every other grader the cases have: #957's
    phase 3 measured the sealer's first act as `broad-gate --record` in six
    runs of six."""
    gaps = sealer_grade_gaps()
    assert not gaps, gaps


def test_a_bound_on_the_sealers_run_that_is_not_zero_is_a_gap(tmp_path):
    """#969 T6's reader, on a case the tree does not hold. Every committed
    sealer case bounds the gate at zero, so a reader that stopped checking
    the tool, the command or the bound would still pass on the tree; each of
    the three is changed here alone and each must be named."""
    case = tmp_path / "behaviour" / "sealer" / "c"
    (case / "graders").mkdir(parents=True)
    (case / "prompt.md").write_text("x\n", encoding="utf-8")
    (case / "graders" / "shape-verdict.md").write_text(
        "---\npath: 'seal/specs/i/guarantee.md'\npattern: '^Verdict:'\n---\nv\n",
        encoding="utf-8",
    )
    bound = (
        "---\ntype: 'tool_used'\ntool: 'Bash'\n"
        "input_match: 'broad-gate\\s+--base'\nmax: 0\nmin: 0\n---\ng\n"
    )
    grader = case / "graders" / "shape-runs-no-broad-gate.md"
    grader.write_text(bound, encoding="utf-8")
    assert sealer_grade_gaps(str(tmp_path)) == []
    gap = f"{os.path.join('behaviour', 'sealer', 'c')}: no grader bounds `broad-gate --base` at zero"
    for old, new in (
        ("max: 0\n", "max: 1\n"),
        ("tool: 'Bash'", "tool: 'Write'"),
        ("\\s+--base", "\\s+--preflight"),
    ):
        grader.write_text(bound.replace(old, new), encoding="utf-8")
        assert sealer_grade_gaps(str(tmp_path)) == [gap], old


def test_each_way_a_committed_case_leaves_the_generator_is_named(tmp_path):
    """#969 S11's reader, on a pair the tree does not hold. The tree's cases
    equal the generator's, so a reader that missed a file on one side or a
    file with other bytes would still pass on the tree; here each of the
    three is present once."""
    made, held = tmp_path / "made", tmp_path / "held"
    for top in (made, held):
        (top / "c" / "graders").mkdir(parents=True)
        (top / "c" / "case.yaml").write_text("same\n", encoding="utf-8")
    (made / "c" / "graders" / "shape-a.md").write_text("a\n", encoding="utf-8")
    (held / "c" / "graders" / "shape-a.md").write_text("a, by hand\n", encoding="utf-8")
    (made / "c" / "scaffold.sh").write_text("set -eu\n", encoding="utf-8")
    (held / "c" / "prompt.md").write_text("p\n", encoding="utf-8")
    assert case_differences(made, held) == [
        f"only in the generator's output: {os.path.join('c', 'scaffold.sh')}",
        f"only in the tree: {os.path.join('c', 'prompt.md')}",
        f"differs: {os.path.join('c', 'graders', 'shape-a.md')}",
    ]


def load_rule_cases():
    """`evals/scripts/rule_cases.py` as a module, under a name of its own."""
    path = os.path.join(EVALS, "scripts", "rule_cases.py")
    spec = importlib.util.spec_from_file_location(
        "specseal_rule_cases_for_layout", path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tree_bytes(top):
    """{path relative to TOP: bytes} for every file under TOP."""
    found = {}
    for here, _, names in os.walk(top):
        for name in names:
            path = os.path.join(here, name)
            with open(path, "rb") as f:
                found[os.path.relpath(path, top)] = f.read()
    return found


def case_differences(generated, committed):
    """Where the directory COMMITTED is not the directory GENERATED, one line
    per file: only in one of them, or in both with other bytes."""
    made, held = tree_bytes(generated), tree_bytes(committed)
    out = [f"only in the generator's output: {p}" for p in sorted(made.keys() - held)]
    out += [f"only in the tree: {p}" for p in sorted(held.keys() - made)]
    out += [f"differs: {p}" for p in sorted(made.keys() & held) if made[p] != held[p]]
    return out


def test_the_sealer_cases_are_the_generators_output(tmp_path, capsys):
    """#969 S11. `evals/behaviour/sealer/` is byte for byte what
    `rule_cases.py` writes. A grader edited by hand is overwritten at the
    next regeneration, so the baseline and a later side run different suites
    while `--suite-rev` names one commit for both; nothing else compares the
    committed cases with the generator."""
    load_rule_cases().main(["--out", str(tmp_path)])
    capsys.readouterr()
    differences = case_differences(
        tmp_path / "sealer", os.path.join(EVALS, "behaviour", "sealer")
    )
    assert not differences, differences


def test_every_case_declares_a_case_yaml_and_a_prompt():
    missing = []
    for d in case_dirs():
        for name in ("case.yaml", "prompt.md"):
            if not os.path.isfile(os.path.join(d, name)):
                missing.append(f"{rel(d)}/{name}")
    assert not missing, missing


def test_every_case_sets_its_bounds_where_the_runner_reads_them():
    assert behaviour_cases(), "the behaviour suite holds no case"
    gaps = bound_gaps()
    assert not gaps, gaps


def test_every_scaffold_is_a_file_beside_its_case():
    gaps = scaffold_gaps()
    assert not gaps, gaps


def test_a_case_outside_the_behaviour_suite_is_held_to_the_same_schema(tmp_path):
    """The five cases that predated the behaviour suite set their bounds at
    the top level and four of them an inline scaffold, and nothing read them
    (#946). A case anywhere under `evals/` is read the same way."""
    legacy = tmp_path / "legacy"
    fixed = tmp_path / "fixed"
    for case in (legacy, fixed):
        (case / "graders").mkdir(parents=True)
        (case / "prompt.md").write_text("Do the thing.\n", encoding="utf-8")
    (legacy / "case.yaml").write_text(
        'schema_version: "1.1"\nname: "legacy"\nruns: 1\nmax_turns: 8\n'
        "context:\n  scaffold_script: |\n    git init -q .\n",
        encoding="utf-8",
    )
    (fixed / "case.yaml").write_text(
        'schema_version: "1.1"\nname: "fixed"\nruns: 1\n'
        "context:\n  scaffold_script: scaffold.sh\n"
        'execution:\n  max_turns: 8\n  timeout_seconds: 240\n  model: "m"\n'
        '  allowed_tools: ["Bash"]\n',
        encoding="utf-8",
    )
    (fixed / "scaffold.sh").write_text("git init -q .\n", encoding="utf-8")
    assert bound_gaps(str(tmp_path)) == [
        "legacy: execution.max_turns",
        "legacy: max_turns at the top level, where the runner drops it",
        "legacy: execution.timeout_seconds",
        "legacy: execution.model",
        "legacy: execution.allowed_tools",
    ]
    assert scaffold_gaps(str(tmp_path)) == [
        "legacy: scaffold_script names no file beside the case"
    ]


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
    for d in case_dirs():
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


def test_the_readme_names_the_behaviour_suite_and_every_case_outside_it():
    with open(os.path.join(EVALS, "README.md"), encoding="utf-8") as f:
        readme = f.read()
    behaviour = set(behaviour_cases())
    unlisted = [
        rel(d) for d in case_dirs() if d not in behaviour and rel(d) not in readme
    ]
    assert not unlisted, unlisted
    assert "behaviour/" in readme
