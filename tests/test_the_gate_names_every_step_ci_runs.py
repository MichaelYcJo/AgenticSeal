"""The gate's arm list was kept in step with the workflow's by whoever
remembered, and nothing held the two lists against each other (#468).

`skills/verify/scripts/broad_gate.py#gate` runs a handful of arms so the
sealer's one run says what CI will say. `.github/workflows/hygiene.yml`'s
`release` job runs ten named steps. #424 added one of them and the gate
was not extended, so from that merge onward a green run covered a
shorter list than the merge is judged by — and no case in the suite went red
for it.

The repair is a declared partition: every step of that job is either mirrored
by a named arm or excluded with a reason a person wrote. This module is what
keeps the partition total, and it is driven RED FROM BOTH SIDES. #423's
finding 4 was a narrow reader, one that saw three of four base spellings, and
it named both directions, which the two rows below hold:

  A1   a step added to the workflow and left unclassified fails here, so the
       seventh arm cannot arrive in silence
  A2   a partition entry naming a step the workflow no longer has fails here,
       so the list cannot rot into naming steps nobody runs

`spec.md` §*User scenarios & acceptance* numbers the rows A1 to A7 and each
case below names the one it holds.

**The step names are read out of `hygiene.yml` itself.** `plan.md` retypes
them for a human reader and says in the same breath that its copy will rot; a
case driven by a list in a document is a case that grades the document. No
YAML parser either — `broad_gate.py` runs with no third-party dependency, so
the reader is text, and it is driven over shapes this repository's workflow
does not happen to have. A reader nothing drives is a reader nobody can tell
is partial (#424's finding 4).
"""

import ast
import importlib.util
import os
import re
import subprocess
import sys

import pytest
from conftest import workflow_step

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GATE = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")
STAMP = os.path.join(ROOT, "skills", "verify", "scripts", "seal_stamp.py")
HYGIENE = os.path.join(ROOT, ".github", "workflows", "hygiene.yml")


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def gate_module():
    return _load("specseal_broad_gate_for_partition_tests", GATE)


def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


gate = gate_module()


# --- the reader, driven over shapes the workflow does not have -------------


WORKFLOW_WITH_TWO_JOBS = """\
name: example

on:
  pull_request:

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # - name: a step somebody commented out
      - name: the first step
        run: true
      - name: the second step
        run: true
  ledger:
    runs-on: ubuntu-latest
    steps:
      - name: a step of another job
        run: true
"""


def test_the_reader_takes_the_steps_of_the_job_it_was_asked_for():
    """A1's reader. In file order, this job only, and an unnamed step — the
    checkout every job opens with — is not one."""
    assert gate.job_steps(WORKFLOW_WITH_TWO_JOBS, "release") == [
        "the first step",
        "the second step",
    ]
    assert gate.job_steps(WORKFLOW_WITH_TWO_JOBS, "ledger") == ["a step of another job"]


def test_a_commented_out_step_is_not_a_step():
    """A step that exists only in a comment is not a step — the same reading
    `tests/test_ci_gives_the_checks_what_they_need.py#strip_comments` takes of
    the same file, for the same reason."""
    assert "a step somebody commented out" not in gate.job_steps(
        WORKFLOW_WITH_TWO_JOBS, "release"
    )


def test_a_job_the_workflow_does_not_have_reads_as_no_steps():
    assert gate.job_steps(WORKFLOW_WITH_TWO_JOBS, "nosuchjob") == []


def test_a_file_that_declares_no_jobs_reads_as_no_steps():
    """Not an exception. The gate calls this on whatever file sits at the
    workflow's path in the repository it was pointed at, and a file it cannot
    read as a workflow must leave the run exactly as it was (A7)."""
    assert gate.job_steps("name: not a workflow at all\n", "release") == []
    assert gate.job_steps("", "release") == []


def test_a_quoted_step_name_comes_back_unquoted():
    """YAML lets a name be quoted, and the partition holds the name a reader
    sees rather than the bytes the file spells it in."""
    text = 'jobs:\n  release:\n    steps:\n      - name: "the quoted step"\n'
    assert gate.job_steps(text, "release") == ["the quoted step"]
    text = "jobs:\n  release:\n    steps:\n      - name: 'the other quoting'\n"
    assert gate.job_steps(text, "release") == ["the other quoting"]


def test_a_step_name_carrying_a_colon_survives_the_reader():
    """`- name: a: b` is one name, not a mapping. A reader that split on the
    first colon would take `a` and the partition would name a step nobody
    runs — which is exactly A2's failure, arriving through the reader."""
    text = "jobs:\n  release:\n    steps:\n      - name: the step: and its tail\n"
    assert gate.job_steps(text, "release") == ["the step: and its tail"]


# --- A1 and A2: the partition is total, in both directions ------------------


def workflow_steps():
    steps = gate.job_steps(read(HYGIENE), gate.RELEASE_JOB)
    assert steps, (
        f"{HYGIENE} names no step of the `{gate.RELEASE_JOB}` job. Either the "
        "job was renamed or the file's shape moved under the reader — and a "
        "reader that comes back empty grades nothing, so this is a refusal "
        "rather than a pass"
    )
    return steps


def test_every_step_the_workflow_runs_is_classified():
    """A1. Red when a step is added to the workflow and nobody classifies it.

    This is the direction the work item exists for: #424 added the thirteenth
    step, the gate was not extended, and the suite said nothing. A step with
    no row is the silence this ends — `classified` includes `excluded`, and an
    exclusion carries prose rather than a category (A4).
    """
    classified = {name for name, _, _ in gate.PARTITION}
    missing = [name for name in workflow_steps() if name not in classified]
    assert not missing, (
        f"these steps of `hygiene.yml`'s `{gate.RELEASE_JOB}` job are in no "
        f"row of `broad_gate.py#PARTITION`: {missing}. Add an arm that mirrors "
        "each, or a row excluding it with the reason no arm can — there is no "
        "third state, and a step with no row is a seal that covers less than "
        "the merge is judged by"
    )


def test_every_entry_of_the_partition_names_a_step_the_workflow_has():
    """A2. The other side. Red when a step is renamed in the workflow, or
    removed, and the partition still names it.

    Without this the partition rots into a list of steps nobody runs, and a
    reader counting what the seal did not answer is counting ghosts."""
    steps = set(workflow_steps())
    stale = [name for name, _, _ in gate.PARTITION if name not in steps]
    assert not stale, (
        f"`broad_gate.py#PARTITION` names steps `hygiene.yml`'s "
        f"`{gate.RELEASE_JOB}` job does not have: {stale}. A renamed step is "
        "a row to rename here; a deleted one is a row to delete"
    )


def test_the_partition_names_each_step_once():
    """Two rows for one step is two answers to one question, and the second
    is unreachable — whichever way a reader resolves it, the count of what the
    seal did not answer is wrong by one."""
    names = [name for name, _, _ in gate.PARTITION]
    twice = sorted({name for name in names if names.count(name) > 1})
    assert not twice, f"these steps carry more than one row: {twice}"


def test_a_row_is_an_arm_or_a_reason_and_never_both_or_neither():
    """The partition's shape, which A1 and A2 assume and neither asserts. A
    row with both says a step is mirrored AND excluded; a row with neither is
    the silence written down."""
    broken = [
        (name, arm, reason)
        for name, arm, reason in gate.PARTITION
        if bool(arm) == bool(reason)
    ]
    assert not broken, (
        f"these rows are neither mirrored nor excluded, or claim to be both: {broken}"
    )


# --- A3: an arm the partition names is an arm the gate runs -----------------


def gate_function():
    """`gate()`, as a syntax tree.

    Read as a tree rather than as text: the claim is about which checks the
    gate RUNS, and a substring search cannot tell a call from a mention of
    one in a docstring or a comment.
    """
    parsed = ast.parse(read(GATE))
    found = [
        node
        for node in ast.walk(parsed)
        if isinstance(node, ast.FunctionDef) and node.name == "gate"
    ]
    assert len(found) == 1, f"broad_gate.py has {len(found)} functions named gate"
    return found[0]


def arms_the_gate_runs():
    """The check name each `checks[...] = run(...)` in `gate()` records.

    The key is read as source rather than resolved, so `checks[CHAIN_NAME]`
    comes back as the constant's NAME — which is what the partition holds too,
    because a row names the arm by the same constant.
    """
    names = []
    for node in ast.walk(gate_function()):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if not isinstance(target, ast.Subscript):
                continue
            if ast.unparse(target.value) != "checks":
                continue
            call = node.value
            ran = isinstance(call, ast.Call) and ast.unparse(call.func) == "run"
            if ran:
                names.append(ast.unparse(target.slice))
    return names


def test_every_arm_the_partition_names_is_an_arm_the_gate_runs():
    """A3. Red when an arm is deleted from `gate()` while its partition row
    stands — the row would then say a step is mirrored by nothing.

    The partition holds the arm's VALUE (`"chain"`) and `gate()` subscripts
    `checks` by the constant's NAME (`CHAIN_NAME`), so the two are joined
    through the module: a constant renamed in one place and not the other is
    red here rather than quiet."""
    ran = arms_the_gate_runs()
    assert ran, "gate() records no check at all"
    values = {}
    for name in ran:
        assert hasattr(gate, name), (
            f"gate() records `checks[{name}]` and broad_gate.py has no such constant"
        )
        values[getattr(gate, name)] = name
    missing = sorted({arm for _, arm, _ in gate.PARTITION if arm and arm not in values})
    assert not missing, (
        f"`PARTITION` says these arms mirror a step of the workflow and "
        f"`gate()` runs no check by those names: {missing}. The arms it does "
        f"run are {sorted(values)}"
    )


def test_the_gate_runs_no_arm_the_partition_does_not_account_for():
    """A3's other side. An arm the gate runs and the partition never names is
    an arm nobody can say which step it stands for — the `suite` arm aside,
    which answers no step of this job at all: it is the repository's own
    command from the `Broad gate` row of `seal/config.md`."""
    answering_no_release_step = {gate.SUITE}
    named = {arm for _, arm, _ in gate.PARTITION if arm}
    loose = sorted(
        getattr(gate, name)
        for name in arms_the_gate_runs()
        if getattr(gate, name) not in named | answering_no_release_step
    )
    assert not loose, (
        f"`gate()` runs these arms and no partition row names them: {loose}. "
        "An arm belongs to a step of the `release` job, or it answers "
        "something outside that job — the repository's own command, or a job "
        "of another workflow — and belongs in the set above"
    )


# --- a repository the gate can seal ------------------------------------------


def git(repo, *args, check=True):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=check,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def write(repo, rel, text):
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def commit(repo, message):
    git(repo, "add", "-A")
    git(
        repo,
        "-c",
        "user.email=e@example.com",
        "-c",
        "user.name=e",
        "commit",
        "-qm",
        message,
        "--allow-empty",
    )
    return git(repo, "rev-parse", "HEAD").stdout.strip()


CONFIG = (
    "# Repository config\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n"
    f"| Broad gate | {sys.executable} -c pass |\n"
)
OVERVIEW = "# overview\n\n## Not verified\n\nnone — the fixture verifies nothing\n"
ITEM = "seal/specs/1799000000-a-fixture-work-item"


def sealable_repo(tmp_path):
    """A repository on `base` with a `feature` branch one commit ahead.

    Driven from Python, per `agent-contract` §8: a probe that commits reaches
    the commit gate exactly as real work does, and the prompt lands on nobody
    while a round is running.
    """
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "base")
    write(repo, "src/service.py", "def handler(x):\n    return x + 1\n")
    write(repo, "seal/config.md", CONFIG)
    write(repo, f"{ITEM}/overview.md", OVERVIEW)
    commit(repo, "base")
    git(repo, "switch", "-qc", "feature")
    write(repo, "src/service.py", "def handler(x):\n    return x + 2\n")
    commit(repo, "feature changes the handler")
    return repo


def run_gate(repo, keep, base="base"):
    return subprocess.run(
        [
            sys.executable,
            GATE,
            "--base",
            base,
            "--root",
            str(repo),
            "--shape",
            "--keep-output",
            str(keep),
        ],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=300,
        env={
            key: value
            for key, value in os.environ.items()
            if key not in ("GITHUB_EVENT_PATH", "GITHUB_HEAD_REF")
        },
    )


def test_the_fixture_branch_passes(tmp_path):
    """The other cases' starting point: every arm passes on the fixture, so a
    refusal below is the one thing each case changed."""
    repo = sealable_repo(tmp_path)
    result = run_gate(repo, tmp_path / "out")
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.startswith("BROAD GATE PASSED   "), result.stdout


def test_a_mode_row_that_disagrees_with_the_folder_fails_the_gate(tmp_path):
    """A3's behavioural half for the other arm #468 added. `seal/config.md`
    says the root lives under the git directory and the root is committed in
    the tree, which is the one direction of that disagreement CI can ever
    reach — and the gate said nothing about it until this arm existed.

    Red against the gate as it stood: this fixture sealed green."""
    repo = sealable_repo(tmp_path)
    write(
        repo, "seal/config.md", CONFIG.replace("| Mode | shared |", "| Mode | local |")
    )
    commit(repo, "the row now says local while the folder is committed")
    result = run_gate(repo, tmp_path / "out")
    assert result.returncode == 1, result.stdout + result.stderr
    assert result.stdout.startswith("BROAD GATE FAILED   "), result.stdout
    assert gate.MODE_NAME in result.stdout, (
        f"the failure form does not name the `{gate.MODE_NAME}` arm:\n{result.stdout}"
    )


# --- A6: the run says which of the workflow's steps it did not answer -------


FIXTURE_WORKFLOW = """\
name: hygiene

on:
  pull_request:

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: a declared review chain has the round record it claimed
        run: true
      - name: the milestone this release claims is the work it carries
        run: |
          if [ "${{ github.base_ref }}" != "main" ]; then
            echo "not a release"; exit 0
          fi
      - name: both READMEs move together
        run: true
"""


def panel_rows(repo):
    """The stamp's rows for a run over `repo`'s workflow, computed rather
    than scraped off the drawing — the rendered line is asserted separately,
    and a value's WIDTH cannot be measured once the frame has cut it."""
    checks = {
        name: gate.Check(name, 0, "", "") for name in (gate.SUITE, gate.CHAIN_NAME)
    }
    base = gate.Base("base", "cccccccc", "base", "cccccccc")
    return gate.panel(
        "ccccccc", base, checks, None, read(repo / ".github/workflows/hygiene.yml")
    )


def with_workflow(repo):
    """The fixture, given a hygiene workflow whose `release` job runs three
    real steps: one this gate mirrors and two it does not."""
    write(repo, ".github/workflows/hygiene.yml", FIXTURE_WORKFLOW)
    commit(repo, "the repository gains a hygiene workflow")
    return repo


def test_the_report_says_how_many_steps_the_run_did_not_answer(tmp_path):
    """A6, on the printed output rather than on the data behind it.

    W1's choice, recorded: **the panel carries the count and the names go to
    the stream beside it.** The panel gives a value 41 columns since #832
    (23 before it) — `seal_stamp.PANEL_VALUE_WIDTH` — and three
    step names do not fit in it, let alone fourteen. A reader given only a
    number would have to reconstruct WHICH from two files, which is the
    reconstruction this work item exists to remove, so both are printed and
    neither alone.

    The printed half is read off the run's own stdout since #975, where the
    panel's rows are text under the `BROAD GATE PASSED` line."""
    repo = with_workflow(sealable_repo(tmp_path))
    result = run_gate(repo, tmp_path / "out")
    assert result.returncode == 0, result.stdout + result.stderr

    printed = result.stdout.splitlines()
    rendered = [line for line in printed if "more steps" in line]
    assert len(rendered) == 1, (
        "the report says nothing about the steps this run did not answer:\n"
        + result.stdout
    )
    # Whole, not cut: a value one column too wide would read as a shorter
    # true statement — which is the failure mode the elision beside the
    # `from` row was added for. The substring is the assertion: a cut value
    # would not carry its tail.
    #
    # #666: over the steps CI runs for THIS base. The milestone step runs only
    # on a pull request into `main` and the base here is `base`, so it is
    # neither answered nor unanswered — `2 of 3` became `1 of 2`.
    #
    # #717: the owner's wording, `CI also  <n> more steps`. The denominator
    # left the panel for the stderr line beside the names, asserted below.
    # #832's S5a: the value leads with a dim `·`, which `--shape` writes `.`.
    assert re.search(r"^CI also [·.] 1 more steps$", rendered[0]), rendered[0]
    width = _load("specseal_seal_stamp", STAMP).PANEL_VALUE_WIDTH
    value = next(v for _, v in [r for r in panel_rows(repo) if r] if "more steps" in v)
    assert len(value) <= width, (
        f"the value is {len(value)} columns and the panel gives "
        f"{width}: {value!r}. This is W1's whole reason for a "
        "count rather than the names"
    )

    assert "both READMEs move together" in result.stderr
    # A11 at the fixture: the step CI will not run here is not named among
    # the unanswered, and one clause says how many were left out and why.
    assert "the milestone this release claims is the work it carries" not in (
        result.stderr
    ), result.stderr
    assert (
        "runs 2 steps for this base and this run answers 1. 1 more runs only on "
        "a pull request into `main`, so this count leaves it out."
    ) in result.stderr, result.stderr
    assert (
        "a declared review chain has the round record it claimed"
        not in (result.stderr.split("Not answered", 1)[-1])
    ), "a step the gate DOES mirror is listed among the ones it did not answer"


def test_a_seal_that_answers_every_step_says_so(tmp_path):
    """The other value of the same line. A run that leaves nothing unanswered
    must not go quiet: silence there is indistinguishable from a gate that
    stopped looking, which is the state this work item found the gate in.

    #666 keys it on the base: the milestone step stays in the workflow and
    runs only into `main`, so against `base` the one step CI runs is the
    mirrored one, and the line says every one is answered AND that one more
    was left out, rather than calling the milestone unanswered."""
    repo = sealable_repo(tmp_path)
    readmes = "      - name: both READMEs move together\n        run: true\n"
    assert readmes in FIXTURE_WORKFLOW, "the fixture no longer has the step"
    write(repo, ".github/workflows/hygiene.yml", FIXTURE_WORKFLOW.replace(readmes, ""))
    commit(repo, "a workflow whose every step CI runs here this gate mirrors")
    result = run_gate(repo, tmp_path / "out")
    assert result.returncode == 0, result.stdout + result.stderr
    assert (
        "this run answers every one of the 1 `release` steps "
        f"{gate.WORKFLOW} runs for this base. 1 more runs only on a pull request "
        "into `main`, so this count leaves it out."
    ) in result.stderr, result.stderr
    # #717: the panel's row does not go quiet either. At 0 it still prints,
    # and it says a count.
    assert ("CI also", "· 0 more steps") in panel_rows(repo), panel_rows(repo)


# --- A4: a reason is prose a person wrote -----------------------------------


def reasons():
    return [(name, reason) for name, _, reason in gate.PARTITION if reason]


def test_every_exclusion_carries_prose_rather_than_a_category():
    """A4. Red against a reason cell reduced to a category word.

    `EXCLUDED` tells the next reader nothing, and the reason is the whole
    value of the row — it is what a person checks when they wonder whether
    the seal covers them. Two structural rules stand in for that judgment: a
    reason is several words, and it is written in the prose case rather than
    as a marker.

    **What this cannot catch is a category in prose clothing.** *not
    applicable here* passes every rule below and says as little as
    `EXCLUDED`. Only a reader catches that one, and `plan.md` §*The failure
    scenario at six months* is where it is written down as an open hole
    rather than a closed one.
    """
    thin = [
        (name, reason)
        for name, reason in reasons()
        if len(reason.split()) < 3 or reason == reason.upper()
    ]
    assert not thin, (
        f"these rows give a marker where a reason belongs: {thin}. A reason "
        "is prose somebody wrote — `needs the pull request's body` is one, "
        "`EXCLUDED` is not"
    )


def test_every_exclusion_says_what_the_gate_cannot_reach():
    """A4's second half. A reason that never names the thing out of reach is
    a sentence rather than a reason — it reads as prose and answers nothing.

    Held loosely on purpose: the vocabulary below is what the four kinds of
    unreachable thing are called in this repository, and a fifth kind is a
    word to add here rather than a case to delete."""
    out_of_reach = (
        "pull request",
        "tracker",
        "fetch",
        "network",
        "never fails",
        "warning",
        ".github/scripts/",
        "inline",
        "second reading",
        "second implementation",
    )
    silent = [
        name
        for name, reason in reasons()
        if not any(word in reason for word in out_of_reach)
    ]
    assert not silent, (
        f"these rows give a reason that names nothing out of the gate's "
        f"reach: {silent}. Say what the gate cannot get at — the pull "
        "request, the tracker, a fetch, a step that only warns, or a check "
        "this repository owns rather than the plugin"
    )


NUMBER_WORDS = ("no", "one", "two", "three", "four", "five", "six", "seven")


def test_the_skill_counts_the_steps_with_a_local_answer_and_no_arm():
    """The shipped verify skill counts the `release` steps that have a local
    answer and no arm — the ones that run this repository's own script, and
    the one written inline — and the count is `PARTITION`'s, so a step added
    to either kind moves the sentence or fails here."""
    scripts = sum(".github/scripts/" in reason for _, reason in reasons())
    inline = sum("inline" in reason for _, reason in reasons())
    with open(
        os.path.join(ROOT, "skills", "verify", "SKILL.md"), encoding="utf-8"
    ) as f:
        skill = " ".join(f.read().split())
    said = (
        f"{NUMBER_WORDS[scripts + inline].capitalize()} steps of SpecSeal's own "
        f"`release` job have a local answer and no arm: {NUMBER_WORDS[scripts]} "
        "run a script under `.github/scripts/`, which no plugin ships, and "
        f"{NUMBER_WORDS[inline]} is shell written inline in the workflow"
    )
    assert said in skill, said


# --- A7: a repository with no such workflow is untouched --------------------


# The panel of a run with no workflow, as it has stood release to release.
# `gate` joined it in 0.15.1 (#475), and since #666 it prints only where the
# copy that ran is not the one invoked, so a run handed no `copy` has none.
# #666 also moved the ref from `from` to the row under `base` (`""`), and the
# row's exit code from `row` to the row under `suite` — which this fixture's
# empty output, carrying no pytest counts, does not have. No row here is
# about the workflow: a run without one is still the run it was. #717 took
# `chain` off, because a drawn panel is green by construction and its title
# already said its exit was 0. #832's S5a, the owner's design of 2026-10-07,
# put it back with a `✓`, and the base's ref beside its commit on one row.
# #944 took the `ledger` row off with the ledger, and #975 the title row, when
# the rows became the gate's printed report and no stamp's.
HISTORICAL_ROWS = (
    "tree",
    "base",
    "suite",
    "chain",
)


def test_a_repository_with_no_hygiene_workflow_is_sealed_exactly_as_before(tmp_path):
    """A7. The partition describes THIS repository's CI and `broad_gate.py`
    ships to every repository that installs the plugin. For one with no such
    workflow the run must be what it was: the same panel rows, and no line
    about steps nobody runs.

    Red against a gate that prints the row unconditionally — which is what a
    partition held as a constant and printed from would do, and why
    `questions.md` Q1's answer (a) survives only while this case is green.
    """
    repo = sealable_repo(tmp_path)
    assert not (repo / ".github").exists(), "the fixture has a workflow after all"
    result = run_gate(repo, tmp_path / "out")
    assert result.returncode == 0, result.stdout + result.stderr
    # The stamp's rows are what the run read: `panel` is handed
    # `workflow_text(root)`, and for this repository that is None, which is
    # the input the labels below are computed over. It used to be asked of a
    # drawing on stdout, and a piped run draws nothing since #400 — so that
    # absence held for every repository, workflow or not.
    assert gate.workflow_text(str(repo)) is None, (
        "the run read a workflow in a repository that has none, so the stamp "
        "would say something about that workflow's steps"
    )
    # What names the release job, and nothing a path can carry by accident:
    # the job as `coverage_line` spells it, the workflow's path, and every
    # step name the partition holds. A bare `release` used to be searched
    # for once the echoed paths were cut out of the stream, and a checkout
    # under a `release/` directory then went red for a path nobody had cut
    # yet (#499).
    for names_the_job in (
        f"`{gate.RELEASE_JOB}`",
        gate.WORKFLOW,
        *(name for name, _, _ in gate.PARTITION),
    ):
        assert names_the_job not in result.stderr, (
            f"the gate names {names_the_job!r} for a repository with no "
            f"hygiene workflow:\n{result.stderr}"
        )

    labels = tuple(
        row[0]
        for row in gate.panel(
            "ccccccc",
            gate.Base("base", "cccccccc", "base", "cccccccc"),
            {
                name: gate.Check(name, 0, "", "")
                for name in (gate.SUITE, gate.CHAIN_NAME)
            },
            None,
        )
        if row
    )
    assert labels == HISTORICAL_ROWS, (
        f"the panel of a run with no workflow is no longer the panel it was: {labels}"
    )


def test_a_workflow_that_is_not_utf8_leaves_the_run_as_it_was(tmp_path):
    """A7's other shape, and the one that ends the run rather than changing
    it. `UnicodeDecodeError` is a `ValueError`, not an `OSError`, and
    `broad_gate.main` catches only `Refused` — so before this the gate ended
    on a traceback for a repository whose workflow file happens to be
    latin-1. A repository this partition is not about must come out of the
    run exactly as it went in, and a traceback is the largest departure from
    that there is. Round 1, finding 5."""
    repo = sealable_repo(tmp_path)
    path = repo / ".github" / "workflows" / "hygiene.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(
        "jobs:\n  release:\n    steps:\n      - name: café step\n".encode("latin-1")
    )
    commit(repo, "a workflow file that is not utf-8")
    assert gate.workflow_text(str(repo)) is None
    result = run_gate(repo, tmp_path / "out")
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.startswith("BROAD GATE PASSED   "), result.stdout
    assert "Traceback" not in result.stderr, result.stderr
    # No `workflow` row on the stamp is `workflow_text(root)` being None,
    # asserted above: it is the one input `panel` takes the row from, and the
    # case before this one pins the rows of a run given None. It used to be
    # asked of a drawing on stdout as well, and a piped run draws nothing
    # since #400, so that absence held whatever the run read.


UNCLASSIFIED_WORKFLOW = """\
name: hygiene

on:
  pull_request:

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: a declared review chain has the round record it claimed
        run: true
      - name: deploy to staging
        run: true
"""


def test_a_step_no_row_classifies_is_not_said_to_carry_a_reason():
    """A6's other repository, and round 1's finding 3. `PARTITION` describes
    THIS repository's `release` job, and `broad_gate.py` ships to every
    installation — so a repository with a `release` job of its own has steps
    no row has ever heard of.

    Counting them as unanswered is honest; telling their reader the reason is
    in `PARTITION` is not, because `PARTITION` holds a row per step of a
    workflow that repository does not run. A reader who follows the pointer
    finds somebody else's list and no answer, which is the reconstruction
    from two files this work item exists to remove, one level further out."""
    said = gate.coverage_line(UNCLASSIFIED_WORKFLOW, "base")
    assert "deploy to staging" in said, said
    with_reasons = said.split("no arm mirrors it in", 1)
    assert len(with_reasons) == 1 or "deploy to staging" not in with_reasons[1], (
        f"a step in no row of PARTITION is named among the ones PARTITION "
        f"gives a reason for:\n{said}"
    )
    assert "no row of `broad_gate.py#PARTITION` at all" in said, said


def test_a_step_a_row_excludes_is_still_pointed_at_its_reason():
    """The other half, and what keeps the case above from being answered by
    deleting the pointer. A step the partition DOES exclude carries a written
    reason, and naming where it is written is the whole of `spec.md` §Scope
    5."""
    said = gate.coverage_line(read(HYGIENE), "base")
    assert "no arm mirrors it in `broad_gate.py#PARTITION`" in said, said
    assert "both READMEs move together" in said.split("no arm mirrors it in", 1)[1]
    assert "no row of `broad_gate.py#PARTITION` at all" not in said, said


MIXED_WORKFLOW = """\
name: hygiene

on:
  pull_request:

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: a declared review chain has the round record it claimed
        run: true
      - name: both READMEs move together
        run: true
      - name: deploy to staging
        run: true
"""


def test_the_two_clauses_render_together_and_hold_the_right_names():
    """Round 2's coverage note. The two cases above each exercise one clause
    — `UNCLASSIFIED_WORKFLOW` leaves `excluded` empty and this repository's
    own workflow leaves `unknown` empty — so the JOINED sentence, which is
    the one a mixed repository's reader actually has to parse, was rendered
    by nothing.

    The two comprehensions are disjoint by construction, which is why the
    reviewer called this a coverage note rather than a defect. It is still
    the sentence that goes wrong if either clause ever learns to claim the
    other's steps."""
    said = gate.coverage_line(MIXED_WORKFLOW, "base")
    assert "runs 3 steps for this base and this run answers 1" in said, said

    reasoned, _, unknown = said.partition(
        "In no row of `broad_gate.py#PARTITION` at all"
    )
    assert unknown, f"the second clause did not render at all:\n{said}"
    assert "no arm mirrors it in `broad_gate.py#PARTITION`" in reasoned, said

    assert "both READMEs move together" in reasoned, said
    assert "both READMEs move together" not in unknown, (
        f"a step `PARTITION` excludes with a reason is named among the ones "
        f"it has never heard of:\n{said}"
    )
    assert "deploy to staging" in unknown, said
    assert "deploy to staging" not in reasoned, (
        f"a step in no row of `PARTITION` is named among the ones it gives a "
        f"reason for:\n{said}"
    )
    assert "a declared review chain has the round record it claimed" not in said, (
        f"a step the gate DOES mirror is named as unanswered:\n{said}"
    )


# --- no mirrored step skips a pull request into `main` ---------------------

# A step's shell guard that ends it on a pull request into `main`, as
# `hygiene.yml` would write it: the test, then an `exit 0` before its `fi`.
SKIPS_AT_MAIN = re.compile(
    r'if \[ "\$\{\{ github\.base_ref \}\}" = "main" \]; then\n'
    r"(?:(?!\s*fi\b).*\n)*?.*\bexit 0\b"
)


def step_text(text, name):
    """The lines of the step called `name`, from its `- name:` line to the
    next step's, as one string."""
    lines = text.splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line.strip() == f"- name: {name}")
    end = next(
        (
            i
            for i in range(start + 1, len(lines))
            if lines[i].lstrip().startswith("- ")
            and len(lines[i]) - len(lines[i].lstrip())
            == len(lines[start]) - len(lines[start].lstrip())
        ),
        len(lines),
    )
    return "".join(lines[start:end])


def mirrored_steps_skipping_at_main(text):
    """The mirrored `release` steps whose `run:` exits on a pull request
    into `main`."""
    return {
        name
        for name, arm, _ in gate.PARTITION
        if arm and SKIPS_AT_MAIN.search(step_text(text, name))
    }


def test_every_mirrored_step_runs_at_every_base():
    """The gate runs every arm at every base, so a mirrored step CI skips at
    `main` would be a step the release seal answers and CI does not ask. None
    does; the reader is shown able to find one by planting a guard in a copy
    of the workflow."""
    text = read(HYGIENE)
    assert mirrored_steps_skipping_at_main(text) == set()
    name = "a declared review chain has the round record it claimed"
    step = step_text(text, name)
    guard = 'if [ "${{ github.base_ref }}" = "main" ]; then\n  exit 0\nfi\n'
    planted = text.replace(step, step.replace("run: |\n", "run: |\n" + guard, 1))
    assert planted != text, "the plant did not land"
    assert mirrored_steps_skipping_at_main(planted) == {name}


# --- #666: the count is over the steps CI runs for this base ---------------

# A step's shell guard that ends it on any pull request NOT into `main`, as
# `hygiene.yml` writes it — `SKIPS_AT_MAIN`'s twin, with `!=`.
RUNS_ONLY_AT_MAIN = re.compile(
    r'if \[ "\$\{\{ github\.base_ref \}\}" != "main" \]; then\n'
    r"(?:(?!\s*fi\b).*\n)*?.*\bexit 0\b"
)


def steps_guarded_off_main(text):
    """The `release` steps whose `run:` exits on a base that is not `main`."""
    return {
        name
        for name in gate.job_steps(text, gate.RELEASE_JOB)
        if RUNS_ONLY_AT_MAIN.search(workflow_step(text, name))
    }


def test_the_steps_left_out_off_main_are_the_steps_guarded_off_main():
    """A13. `ONLY_AT_MAIN` is exactly the set of `release` steps whose guard
    ends them on any base but `main`, from both sides — and the comparison is
    shown able to fail on a copy of the workflow with one guard turned
    around, so a guard added to a fourth step, or dropped from one of the
    three, fails here."""
    text = read(HYGIENE)
    guarded = steps_guarded_off_main(text)
    assert guarded, "no step is guarded off main, so the reader found nothing"
    assert guarded == set(gate.ONLY_AT_MAIN), (
        f"the workflow guards these steps off `main`: {sorted(guarded)}, and "
        f"`ONLY_AT_MAIN` holds {sorted(gate.ONLY_AT_MAIN)}"
    )
    assert len(gate.ONLY_AT_MAIN) == len(set(gate.ONLY_AT_MAIN)) == 3
    flipped = text.replace('" != "main" ]', '" = "main" ]', 1)
    assert flipped != text and steps_guarded_off_main(flipped) != set(
        gate.ONLY_AT_MAIN
    ), "turning one guard around did not move the reader"


@pytest.mark.parametrize(
    "given, main",
    [
        ("main", True),
        ("origin/main", True),
        ("origin/origin/main", False),
        ("refs/heads/main", False),
        ("mains", False),
        ("release/x", False),
        (None, False),
    ],
)
def test_one_reading_says_whether_the_base_is_main(given, main):
    """S5's `base_is_main`: the one reading the count takes, keyed on the spelling with one leading `origin/` removed."""
    assert gate.base_is_main(given) is main


def test_the_count_cannot_be_asked_without_a_base():
    """Round 1's 🟡 3: a caller that drops the base gets a `TypeError` rather
    than the feature-base answer in silence, so the merge that rewrote the
    gate's coverage call could not lose its argument unnoticed."""
    text = read(HYGIENE)
    for unit in (gate.unanswered, gate.coverage_line):
        with pytest.raises(TypeError):
            unit(text)


FEATURE_UNANSWERED = (
    "every issue this pull request claims, and every one it only names",
    "the CLAUDE.md block is the template's, line for line",
    "both READMEs move together",
)


def real_panel_workflow_row(given):
    checks = {
        name: gate.Check(name, 0, "", "") for name in (gate.SUITE, gate.CHAIN_NAME)
    }
    base = gate.Base(given, "cccccccc", given, "cccccccc")
    rows = gate.panel("ccccccc", base, checks, None, read(HYGIENE))
    return next(value for label, value in [r for r in rows if r] if label == "CI also")


def test_a_feature_seal_counts_the_steps_ci_runs_for_it():
    """A11 over this repository's own workflow. Against a base that is not
    `main` CI runs 6 of the 9 steps and the gate mirrors 3, so the panel
    reads `CI also · 3 more steps`; the line names the three unanswered steps
    CI runs and none of the three only-at-`main` ones, and says three were
    left out and why. Pinned verbatim (`agent-contract` §14)."""
    assert gate.steps_for(read(HYGIENE), "release/x") == [
        step
        for step in gate.job_steps(read(HYGIENE), gate.RELEASE_JOB)
        if step not in gate.ONLY_AT_MAIN
    ]
    assert real_panel_workflow_row("release/x") == "· 3 more steps"
    said = gate.coverage_line(read(HYGIENE), "release/x")
    assert said.startswith(
        f"broad-gate: {gate.WORKFLOW}'s `release` job runs 6 steps for this base "
        "and this run answers 3. 3 more run only on a pull request into `main`, "
        "so this count leaves them out."
    ), said
    for step in FEATURE_UNANSWERED:
        assert step in said, step
    for step in gate.ONLY_AT_MAIN:
        assert step not in said, step


def test_a_release_seal_counts_every_step_ci_runs_for_it():
    """A12. Against `main` CI runs every one of the 9 steps and the gate
    mirrors 3, so the panel reads `CI also · 6 more steps` and the line
    leaves no step out."""
    for given in ("main", "origin/main"):
        assert real_panel_workflow_row(given) == "· 6 more steps", given
        said = gate.coverage_line(read(HYGIENE), given)
        assert said.startswith(
            f"broad-gate: {gate.WORKFLOW}'s `release` job runs 9 steps for this "
            "base and this run answers 3."
        ), said
        assert "leaves" not in said.split("Not answered", 1)[0], said
        for step in gate.ONLY_AT_MAIN:
            assert step in said, step


def test_the_documents_say_the_count_is_over_the_steps_ci_runs():
    """S5's documentation (`agent-contract` §14): the skill section that
    explains the count and the partition's policy paragraph each say a step
    CI does not run for the base is outside the count. Since #969 the sealer
    sees no output of the gate's and explains none of it, so its definition
    is not asked."""
    verify = " ".join(read(os.path.join(ROOT, "skills", "verify", "SKILL.md")).split())
    assert "counted over the steps CI runs for the base" in verify
    broad = " ".join(read(os.path.join(ROOT, "docs", "the-broad-gate.md")).split())
    assert "A step CI does not run for the base is neither answered nor unanswered" in (
        broad
    )
