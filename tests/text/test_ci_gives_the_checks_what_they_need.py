"""Three workflow settings decide whether the checks below them mean anything,
and how often they are paid for.

None is visible from the checks themselves, and the first two failed silently.

**Checkout depth.** `actions/checkout@v4` fetches one commit unless told
otherwise. A case in this suite resolves a commit this repository's own
records name — `tests/behaviour/test_the_frozen_reading_never_grows.py` shows
`86256492:hooks/cmdline.py` — and at depth 1 that commit is not in the clone
at all, so the case skips where it should have answered.

**Which pull-request events run.** `on: pull_request:` with no `types:` runs
on `opened`, `synchronize` and `reopened` — and on nothing else. On a DRAFT
pull request `chain_check.py` prints its refusals and fails nothing. Pressing
*Ready for review* adds no commit, so `synchronize` never fires, and without
`ready_for_review` the workflow that runs the check never re-runs: the green
the draft earned stays on that SHA through the merge, and every refusal the
check holds for a ready pull request is voided by two clicks and no commit.
A workflow whose steps read no draft state gains nothing from those events
but a second run of the same commit. So the two events are required where a
workflow runs `chain_check.py`, the one script here that reads draft state,
and refused everywhere else. A later step that reads draft state through
another script is not seen by this, and naming the reader once is what keeps
that fix to one string.

**Which runs a newer one cancels.** A push to an open pull request starts
every workflow again, and the runs of the commit before it are spent. Each
workflow that runs on `pull_request` cancels its own runs still in progress
for the same pull request, and touches nothing else: a `push` to `main` is
the run `release-report` reads for a release tag's minutes, and GitHub keeps
one pending run per concurrency group and cancels any older pending one,
whatever `cancel-in-progress` says.

These are assertions about YAML, which is not this repository's usual shape
for a test. They are here because the alternative is a comment in the workflow
asking the next editor to remember.
"""

import os
import re

import pytest
from conftest import ROOT, _unquote, code_lines

WORKFLOWS = os.path.join(ROOT, ".github", "workflows")

# Events GitHub does NOT include by default, and that a workflow needs where
# it runs the one script that reads draft state: `chain_check.py` excuses a
# draft (`docs/the-review-record.md` *What the check reads at the pull
# request*), so leaving draft state has to re-run it.
DRAFT_EVENTS = ("ready_for_review", "converted_to_draft")
DRAFT_READER = "chain_check.py"

# What `cancel-in-progress` reads in a workflow that also runs on an event
# other than `pull_request`: a newer pull-request run cancels, nothing else.
CANCEL_ON_PULL_REQUEST = "${{ github.event_name == 'pull_request' }}"


def strip_comments(text):
    """The workflow with its comment lines removed.

    A setting that exists only in a comment is not a setting. The comment
    above each `types:` list names both draft events, so a substring test on
    the raw trigger passes with the `types:` line itself deleted -- measured:
    dropping the real line and keeping the comment left both checks green,
    which is exactly the edit that reopens the defect they were written for.

    What a comment is belongs to `tests/conftest.py#code_line`, the one rule
    every workflow reader in the suite uses, so a trailing comment is off
    the line here too (#482).
    """
    return "\n".join(code_lines(text))


def read(name):
    with open(os.path.join(WORKFLOWS, name), encoding="utf-8") as f:
        return strip_comments(f.read())


def workflows():
    return sorted(n for n in os.listdir(WORKFLOWS) if n.endswith((".yml", ".yaml")))


def top_level(text, key):
    """The lines under a workflow's top-level `key:`, or `None` where it has
    no such block. Comments are already off."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.rstrip() == f"{key}:":
            block = []
            for follow in lines[i + 1 :]:
                if follow.strip() and not follow.startswith(" "):
                    break
                block.append(follow)
            return block
    return None


def events(text):
    """{event: the lines under it} from a workflow's `on:` block."""
    out, name = {}, None
    for line in top_level(text, "on") or []:
        m = re.match(r"^  ([A-Za-z_]+):\s*$", line)
        if m:
            name = m.group(1)
            out[name] = []
        elif name and line.startswith("   "):
            out[name].append(line)
    return out


def concurrency(text):
    """{key: value} of a workflow's top-level `concurrency:` block, or
    `None` where it declares none."""
    block = top_level(text, "concurrency")
    if block is None:
        return None
    pairs = (re.match(r"^  ([a-z-]+):\s*(.*?)\s*$", line) for line in block)
    return dict(m.groups() for m in pairs if m)


def jobs(text):
    """{job name: its block} — a two-space indent under `jobs:`.

    Hand-parsed rather than with PyYAML, which CI does not install: the
    workflow being read is the one that decides what CI installs, and it
    installs a test runner and a way to run it in parallel -- no parser.
    """
    body = text.split("\njobs:\n", 1)
    assert len(body) == 2, "no `jobs:` block"
    out, name, lines = {}, None, []
    for line in body[1].splitlines():
        m = re.match(r"^  ([A-Za-z0-9_-]+):\s*$", line)
        if m:
            if name:
                out[name] = "\n".join(lines)
            name, lines = m.group(1), []
            continue
        if name is not None:
            lines.append(line)
    if name:
        out[name] = "\n".join(lines)
    return out


_FLOW_ITEM = re.compile(r"^\s*-\s*\{(.*)\}\s*$")
_FLOW_PAIR = re.compile(r"\s*([A-Za-z0-9_-]+):\s+(\S.*?)\s*")


def _flow_mapping(body, line):
    """One `{ … }` item's keys and values, quotes off; refuses what it cannot
    read whole."""
    parts, quote, start = [], None, 0
    for i, c in enumerate(body):
        if quote:
            if c == quote:
                quote = None
        elif c in "\"'":
            quote = c
        elif c in "{}[]":
            raise ValueError(f"a nested collection in a matrix entry: {line!r}")
        elif c == ",":
            parts.append(body[start:i])
            start = i + 1
    if quote:
        raise ValueError(f"an unclosed quote in a matrix entry: {line!r}")
    parts.append(body[start:])
    entry = {}
    for part in parts:
        m = _FLOW_PAIR.fullmatch(part)
        if not m or m.group(1) in entry:
            raise ValueError(f"a matrix entry that is not `key: value, …`: {line!r}")
        entry[m.group(1)] = _unquote(m.group(2))
    return entry


def matrix_include_entries(text):
    """The `pytest` job's `include:` entries, one dict per entry (#864).

    The suite's one reading of the `pytest` job's entries in
    `.github/workflows/test.yml`, beside `jobs`, which finds the job. Four
    cases used to slice the job out of the raw text by its neighbour's name,
    and the one that read entries took every line starting `- { os:`: an
    entry written another way was not an entry, and nothing said so. Two
    other readings of the file remain, each asking something else:
    `tests/behaviour/test_release_hygiene.py` takes the floor from every `python:` in
    it, and `tests/skills/test_arm_check.py` reads the Pythons of the jobs that run
    its own module.

    The name carries no `pytest_` prefix: in a `conftest.py`, pytest reads a
    function so named as a hook and stops the run at an unknown one.

    The file is this repository's own, and every entry
    in it is a one-line flow mapping, `- { os: …, python: "…", … }`. That is
    the one shape read here, and values come back as strings with their
    quotes off, as `conftest.py#_unquote` reads a step's name. Comments are
    taken off first, through `conftest.py#code_lines`, so a commented-out
    entry is not an entry. Anything else under `include:` -- a block-style
    item, a nested value, a key written twice -- is refused with a
    `ValueError` naming its line rather than skipped, and so is a workflow
    with no `pytest` job, a job with no single `include:`, or one with no
    entry under it.

    **`include:` has to be the matrix's only key.** GitHub runs each entry
    as a job of its own only where the matrix has no other key: beside a base
    axis an entry is merged into the axis' combinations, and an `exclude:`
    takes combinations away, so the entries read here would no longer be the
    jobs. A sibling key under `matrix:` is refused naming its line, and so is
    an `include:` that is not a key of the job's `matrix:`.
    """
    job = jobs("\n".join(code_lines(text))).get("pytest")
    if job is None:
        raise ValueError("no `pytest` job under `jobs:`")
    lines = job.splitlines()
    heads = [i for i, ln in enumerate(lines) if ln.strip() == "include:"]
    if len(heads) != 1:
        raise ValueError(f"the `pytest` job has {len(heads)} `include:` keys, not one")

    def indent(line):
        return len(line) - len(line.lstrip(" "))

    head = indent(lines[heads[0]])
    parent = next(
        (
            i
            for i in range(heads[0] - 1, -1, -1)
            if lines[i].strip() and indent(lines[i]) < head
        ),
        None,
    )
    if parent is None or lines[parent].strip() != "matrix:":
        raise ValueError("the `pytest` job's `include:` is not a key of its `matrix:`")
    floor = indent(lines[parent])
    entries = []
    for line in lines[parent + 1 :]:
        if not line.strip():
            continue
        if indent(line) <= floor:
            break
        if indent(line) == head and not line.lstrip().startswith("-"):
            if line.strip() == "include:":
                continue
            raise ValueError(
                "a `matrix:` key beside `include:` changes which jobs the "
                f"entries are, and this reader does not read it: {line.strip()!r}"
            )
        m = _FLOW_ITEM.match(line)
        if not m:
            raise ValueError(
                "an `include:` item that is not a one-line `- { … }` flow "
                f"mapping, the one shape this reader owns: {line.strip()!r}"
            )
        entries.append(_flow_mapping(m.group(1), line.strip()))
    if not entries:
        raise ValueError("the `pytest` job's `include:` holds no entry")
    return entries


# A matrix in this repository's shape, with a commented entry, a trailing
# comment, a single-quoted value, a value holding a `#`, a key of the job
# that ends the matrix and a second job's matrix. Neutral values
# only (`CONTRIBUTING.md` *House rules*, *No real identifiers*).
MATRIX = """\
name: tests

jobs:
  lint:
    runs-on: ubuntu-latest
  pytest:
    strategy:
      fail-fast: false
      matrix:
        include:
          - { os: ubuntu-latest, python: "3.12", timeout: 15 }
          # - { os: macos-latest, python: "3.12", timeout: 35 }
          - { os: macos-latest, python: "3.12", split: "--splits 2 --group 1", timeout: 5 }  # one
          - { os: example-os, python: '3.12', note: "a # b" }
    runs-on: ${{ matrix.os }}
    steps:
      - run: pytest tests/ ${{ matrix.split }}
  other:
    strategy:
      matrix:
        include:
          - { os: not-this-job }
"""

LAST_ENTRY = "- { os: example-os, python: '3.12', note: \"a # b\" }"


def test_the_matrix_entries_are_read_with_their_quotes_off():
    assert matrix_include_entries(MATRIX) == [
        {"os": "ubuntu-latest", "python": "3.12", "timeout": "15"},
        {
            "os": "macos-latest",
            "python": "3.12",
            "split": "--splits 2 --group 1",
            "timeout": "5",
        },
        {"os": "example-os", "python": "3.12", "note": "a # b"},
    ]


def test_a_commented_matrix_entry_is_not_an_entry():
    entries = matrix_include_entries(MATRIX)
    assert [e["os"] for e in entries] == [
        "ubuntu-latest",
        "macos-latest",
        "example-os",
    ], entries


@pytest.mark.parametrize(
    "item",
    [
        '- os: macos-latest\n            python: "3.12"',
        "- { os: macos-latest, python: [3.12] }",
        "- { os: macos-latest, os: example-os }",
        '- { os: macos-latest, split: "--splits 2 }',
        "- os-only",
    ],
    ids=["block-style", "nested", "key-twice", "unclosed-quote", "scalar"],
)
def test_an_include_item_this_reader_does_not_own_is_refused_by_its_line(item):
    text = MATRIX.replace(LAST_ENTRY, item)
    assert text != MATRIX
    with pytest.raises(ValueError) as caught:
        matrix_include_entries(text)
    assert item.splitlines()[0].strip() in str(caught.value), caught.value


@pytest.mark.parametrize(
    "sibling",
    ['python: ["3.12", "3.13"]', "exclude:\n          - { os: example-os }"],
    ids=["base-axis", "exclude"],
)
@pytest.mark.parametrize("where", ["before", "after"])
def test_a_matrix_key_beside_include_is_refused_by_its_line(sibling, where):
    """Round 1's 🟡 1. GitHub runs each `include:` entry as a job of its own
    only where the matrix has no other key; beside a base axis an entry is
    merged into the axis' combinations, so three shards can become fewer jobs
    while every entry still reads as a shard."""
    if where == "before":
        old, new = "      matrix:\n", f"      matrix:\n        {sibling}\n"
    else:
        old = "    runs-on: ${{ matrix.os }}\n"
        new = f"        {sibling}\n{old}"
    text = MATRIX.replace(old, new, 1)
    assert text != MATRIX
    with pytest.raises(ValueError, match="beside `include:`") as caught:
        matrix_include_entries(text)
    assert sibling.splitlines()[0] in str(caught.value), caught.value


def test_an_include_that_is_not_the_matrixs_own_is_refused():
    text = MATRIX.replace("      matrix:\n", "      other:\n", 1)
    with pytest.raises(ValueError, match="not a key of its `matrix:`"):
        matrix_include_entries(text)


def test_a_workflow_with_no_entry_to_read_is_refused():
    with pytest.raises(ValueError, match="no `pytest` job"):
        matrix_include_entries(MATRIX.replace("  pytest:", "  tests:"))
    with pytest.raises(ValueError, match="holds no entry"):
        matrix_include_entries(
            MATRIX.split("          - { os: ubuntu")[0] + "    runs-on: x\n"
        )
    with pytest.raises(ValueError, match="0 `include:` keys"):
        matrix_include_entries(
            MATRIX.replace(
                "        include:\n          - { os: ubuntu",
                "          - { os: ubuntu",
                1,
            )
        )


# A job runs pytest where a line of its code names it as a word: `run: pytest
# …`, `uvx --with pytest pytest`, `uv run pytest`, `PYTHONPATH=x pytest`,
# `cd sub && pytest`, `python -m pytest`, a line of a `run: |` block. This is
# the reach the old substring test had. `needs: pytest` names the job of that
# name and runs nothing (#931's `durations` job and the `release-report` job,
# neither of which runs the suite), so a `needs:` line is not read; comments
# are off before this reads a line.
RUNS_PYTEST = re.compile(r"(?<![\w.-])pytest(?:\s|$)")


def runs_pytest(block):
    """Whether a line of `block`'s code, other than its `needs:`, names
    pytest as a word."""
    return any(
        RUNS_PYTEST.search(line)
        for line in block.splitlines()
        if not re.match(r"^\s*needs:", line)
    )


def shallow_pytest_jobs(text):
    """The jobs of a workflow's code (comments already off) that run pytest
    on a checkout without the whole history."""
    found = []
    for job, block in jobs(text).items():
        if not runs_pytest(block):
            continue
        if "actions/checkout" not in block:
            continue
        if "fetch-depth: 0" not in block:
            found.append(job)
    return found


# Every way a job here has been seen to call pytest, each on a shallow
# checkout, and one that only names the job: round 1's 🟡 3 of work item
# 1791876667 found the first four unselected. Neutral values only
# (`CONTRIBUTING.md` *House rules*, *No real identifiers*).
SHALLOW_RUNNERS = {
    "uvx-pytest": "uvx --with pytest pytest tests/ -q",
    "uv-run-pytest": "uv run pytest tests/ -q",
    "env-prefixed": "PYTHONPATH=x pytest tests/ -q",
    "cd-and-pytest": "cd sub && pytest -q",
    "plain-pytest": "pytest tests/ -q",
    "python-m-pytest": "python -m pytest tests/ -q",
}


@pytest.mark.parametrize("job", sorted(SHALLOW_RUNNERS))
def test_a_job_that_calls_pytest_any_way_is_held_to_the_whole_history(job):
    workflow = (
        "on: push\n"
        "jobs:\n"
        f"  {job}:\n"
        "    runs-on: example-os\n"
        "    steps:\n"
        "      - uses: actions/checkout@v4\n"
        f"      - run: {SHALLOW_RUNNERS[job]}\n"
        "  reads-a-part:\n"
        "    needs: pytest\n"
        "    steps:\n"
        "      - uses: actions/checkout@v4\n"
        "      - run: echo needs-names-a-job\n"
    )
    assert shallow_pytest_jobs(strip_comments(workflow)) == [job]


def test_every_job_that_runs_pytest_has_the_whole_history():
    """A check that cannot resolve a SHA is not excused from resolving it."""
    offenders = [
        f"{name}:{job}"
        for name in workflows()
        for job in shallow_pytest_jobs(read(name))
    ]
    assert not offenders, (
        f"jobs that run pytest on a shallow checkout: {offenders}. "
        "At depth 1 a ref this repository's own records name is MISSING "
        "rather than wrong, so a case that resolves one skips instead of "
        "failing — which turns the one checkout setting that voids these "
        "checks into the setting that silences them. "
        "`tests/behaviour/test_the_frozen_reading_never_grows.py#"
        "test_the_bytes_below_the_rider_are_86256492s` is the live case: it "
        "shows `86256492:hooks/cmdline.py` and skips when it cannot"
    )


def test_the_draft_events_run_where_draft_state_is_read_and_nowhere_else():
    """Otherwise the draft excuse is permanent, or a ready press re-runs a
    suite on the commit it already ran.

    `chain_check.py` lets a draft pull request through with an open finding.
    That excuse is meant to end when the pull request stops being a draft,
    and without these two event types it never does — no commit is needed to
    leave draft state, and no commit means no `synchronize`. A workflow that
    does not run the check reads nothing a ready press changes, so the two
    events there buy one more run of the same commit and nothing else.
    """
    for name in workflows():
        text = read(name)
        trigger = "\n".join(events(text).get("pull_request", []))
        for event in DRAFT_EVENTS:
            if DRAFT_READER in text:
                assert event in trigger, (
                    f"{name}: runs `{DRAFT_READER}` and `on.pull_request` "
                    f"does not list `{event}`. The default set is "
                    "opened/synchronize/reopened, so leaving draft state "
                    "re-runs nothing and the draft's green is what merges"
                )
            else:
                assert event not in trigger, (
                    f"{name}: `on.pull_request` lists `{event}` and nothing "
                    f"in the workflow runs `{DRAFT_READER}`, the one script "
                    "that reads draft state, so a ready press re-runs every "
                    "job on a commit they already ran"
                )


def test_a_newer_pull_request_run_cancels_the_older_and_no_other_run_waits():
    """A push to an open pull request spends the runs of the commit before
    it, and nothing outside that pull request is held or cancelled.

    Concurrency groups are the repository's, not the workflow's, so a group
    without the workflow's name makes one pull request's `tests` and
    `hygiene` cancel each other. And GitHub keeps one pending run per group,
    cancelling any older pending one whatever `cancel-in-progress` says: a
    `push` run grouped by its ref waits behind the run before it, and a third
    push to `main` cancels it while it waits. That run is the one
    `release-report` reads for a release tag, so a run that is not a pull
    request's takes a group of its own, `github.run_id`.
    """
    for name in workflows():
        text = read(name)
        on = events(text)
        if "pull_request" not in on:
            continue
        block = concurrency(text)
        assert block is not None, (
            f"{name}: runs on `pull_request` and declares no `concurrency:`, "
            "so every push to an open pull request leaves the last commit's "
            "runs to finish"
        )
        group = block.get("group", "")
        for part in ("github.workflow", "github.event.pull_request.number"):
            assert part in group, (
                f"{name}: the concurrency group {group!r} does not name "
                f"`{part}`; it has to be one workflow's runs of one pull "
                "request"
            )
        cancel = block.get("cancel-in-progress")
        if set(on) == {"pull_request"}:
            assert cancel in ("true", CANCEL_ON_PULL_REQUEST), (
                f"{name}: `cancel-in-progress` reads {cancel!r}, so a newer "
                "push leaves the older run to finish"
            )
            continue
        assert "|| github.run_id }}" in group, (
            f"{name}: the concurrency group {group!r} does not fall back to "
            "`github.run_id`, so a run that is not a pull request's shares a "
            "group with the next one on its ref, waits behind it, and is "
            "cancelled while pending by the one after"
        )
        assert cancel == CANCEL_ON_PULL_REQUEST, (
            f"{name}: also runs on {sorted(set(on) - {'pull_request'})} and "
            f"`cancel-in-progress` reads {cancel!r}; only "
            f"`{CANCEL_ON_PULL_REQUEST}` cancels a pull request's run and "
            "no other"
        )


def test_every_pytest_leg_has_a_timeout_and_the_job_reads_it():
    """Each `pytest` leg of `test.yml` carries a `timeout-minutes` past which
    GitHub fails the job (#841). It moved here from the slow-case module when
    that module's ceiling became a report (#942)."""
    text = read("test.yml")
    entries = matrix_include_entries(text)
    assert entries
    budgets = [e.get("timeout", "") for e in entries]
    assert all(b.isdigit() for b in budgets), f"a leg with no timeout: {entries}"
    assert all(int(b) > 0 for b in budgets), entries
    job = jobs(text)["pytest"]
    assert "\n    timeout-minutes: ${{ matrix.timeout }}\n" in job, (
        "the job does not read the matrix's timeout"
    )
