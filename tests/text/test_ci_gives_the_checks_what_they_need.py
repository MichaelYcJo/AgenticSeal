"""Four workflow settings decide whether the checks below them mean anything,
and how often they are paid for.

None is visible from the checks themselves, and all but the third failed
silently.

**Checkout depth.** `actions/checkout@v4` fetches one commit and no tag
unless told otherwise. `tests/behaviour/test_release_hygiene.py` reads this
repository's `v*` tags to tell a shipped version from one being cut, and at
depth 1 it reads none, so
`test_this_checkout_has_tags_to_read_the_shipped_set_from` fails on a tree
with nothing wrong in it.

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
that fix to one string. The same script reads the pull request's body, and an
edited body makes no commit either, so `edited` is required wherever it runs.

**Which runs a newer one cancels.** A push to an open pull request starts
every workflow again, and the runs of the commit before it are spent. Each
workflow that runs on `pull_request` cancels its own runs still in progress
for the same pull request, and touches nothing else: a `push` to `main` is
the run `release-report` reads for a release tag's minutes, and GitHub keeps
one pending run per concurrency group and cancels any older pending one,
whatever `cancel-in-progress` says.

**Which cases a leg names.** A case that skips on one system passes nothing
there, and a leg run with `-q` alone names no skipped case: it prints a count,
and the cases one helper skips fold under that helper's line, so every case
`tests/conftest.py#symlink_or_skip` skips reads as the line of its
`pytest.skip` call.
Rows that deferred a Windows question to the Windows legs met a log that could
not answer them (#1221). Each `pytest` leg therefore passes `-rfEs
--no-fold-skipped`, which names every skipped case with its reason. `-r`
replaces pytest's default `fE` rather than adding to it, so a leg passing
`-rs` would also stop naming the cases that failed.

**The workflow the plugin ships.** `seal pr-checks install` writes
`templates/setup/hygiene.yml` into a user's repository, where it runs on
`pull_request` as this repository's own workflows do, so the draft events and
the cancelling are asked of it too. It also states its token's scope, and it
is the one source of the two steps it shares with this repository's
`hygiene.yml`, which runs them from the tree instead of from a clone.

These are assertions about YAML, which is not this repository's usual shape
for a test. They are here because the alternative is a comment in the workflow
asking the next editor to remember. Each case reads a workflow as
`tests/workflows.py#load` parses it, so a setting that stands only in a
comment is no setting. The one comment a case reads, the pointer above each
step the template shares, is read from the file's text, because a parser
drops comments.
"""

import os
import re

import pytest
from conftest import ROOT, code_lines, read
from workflows import load

WORKFLOWS = ".github/workflows"
TEST = f"{WORKFLOWS}/test.yml"
HYGIENE = f"{WORKFLOWS}/hygiene.yml"

# Events GitHub does NOT include by default, and that a workflow needs where
# it runs the one script that reads draft state: `chain_check.py` excuses a
# draft (`docs/checks/the-pull-request-check.md` *What the check reads at
# the pull request*), so leaving draft state has to re-run it.
DRAFT_EVENTS = ("ready_for_review", "converted_to_draft")
DRAFT_READER = "chain_check.py"
# The event that carries a body edited after the pull request opened, which
# no commit follows: `chain_check.py` reads the body from the payload against
# what `seal pr-body` composes at HEAD (#1452), so a workflow that runs it
# runs on this event too.
BODY_EVENT = "edited"

# What `cancel-in-progress` reads in a workflow that also runs on an event
# other than `pull_request`: a newer pull-request run cancels, nothing else.
CANCEL_ON_PULL_REQUEST = "${{ github.event_name == 'pull_request' }}"

# The workflow the plugin ships, by its repository path, and the prefix its
# steps put before a script of the plugin's clone.
TEMPLATE = "templates/setup/hygiene.yml"
CLONE = '"$RUNNER_TEMP/agentic/'


def loaded():
    """{repository path: the loaded workflow} for every workflow under
    `.github/workflows/`, and for the shipped template under TEMPLATE."""
    names = sorted(
        n
        for n in os.listdir(os.path.join(ROOT, WORKFLOWS))
        if n.endswith((".yml", ".yaml"))
    )
    paths = [f"{WORKFLOWS}/{n}" for n in names] + [TEMPLATE]
    return {path: load(path) for path in paths}


def job_scripts(job):
    """Each `run:` script of JOB's steps, with its shell comments off.

    The parser keeps a comment inside a script, where the shell does not run
    it, so each script's comments come off through `tests/conftest.py#code_line`.
    """
    return [
        "\n".join(code_lines(step["run"]))
        for step in job.get("steps", [])
        if "run" in step
    ]


def scripts(workflow):
    """Each `run:` script of every job of WORKFLOW, comments off."""
    return [script for job in workflow["jobs"].values() for script in job_scripts(job)]


def pull_request_types(workflow):
    """The `types:` WORKFLOW lists under `on.pull_request`, or `[]` where it
    lists none: an empty `pull_request:` loads as `''`."""
    pull_request = workflow["on"].get("pull_request") or {}
    return pull_request.get("types", [])


def checkouts(job):
    """JOB's steps that use `actions/checkout`."""
    return [
        step
        for step in job.get("steps", [])
        if step.get("uses", "").startswith("actions/checkout")
    ]


# A job runs pytest where a line of one of its `run:` scripts names it as a
# word: `run: pytest …`, `uvx --with pytest pytest`, `uv run pytest`,
# `PYTHONPATH=x pytest`, `cd sub && pytest`, `python -m pytest`, a line of a
# `run: |` block. This is the reach the old substring test had. Only the
# scripts are read, so `needs: pytest`, which names the job of that name and
# runs nothing (#931's `durations` job and the `release-report` job, neither
# of which runs the suite), is not; a script's comments are off before a
# line is read.
RUNS_PYTEST = re.compile(r"(?<![\w.-])pytest(?:\s|$)")


def runs_pytest(job):
    """Whether a line of one of JOB's scripts names pytest as a word."""
    return any(
        RUNS_PYTEST.search(line)
        for script in job_scripts(job)
        for line in script.splitlines()
    )


def shallow_pytest_jobs(workflow):
    """The jobs of a loaded WORKFLOW that run pytest on a checkout without
    the whole history."""
    found = []
    for name, job in workflow["jobs"].items():
        if not runs_pytest(job) or not checkouts(job):
            continue
        if not any(
            step.get("with", {}).get("fetch-depth") == "0" for step in checkouts(job)
        ):
            found.append(name)
    return found


# Every way a job here has been seen to call pytest, each on a shallow
# checkout, one that only names the job, and one whose script names it only
# in a shell comment: round 1's 🟡 3 of work item 1791876667 found the first
# four unselected. Neutral values only
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
def test_a_job_that_calls_pytest_any_way_is_held_to_the_whole_history(job, tmp_path):
    workflow = tmp_path / "workflow.yml"
    workflow.write_text(
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
        "  comments-on-it:\n"
        "    steps:\n"
        "      - uses: actions/checkout@v4\n"
        "      - run: |\n"
        "          # pytest tests/ -q\n"
        "          echo a-shell-comment-runs-nothing  # pytest -q\n",
        encoding="utf-8",
    )
    assert shallow_pytest_jobs(load(str(workflow))) == [job]


def test_every_job_that_runs_pytest_has_the_whole_history():
    """A case that reads the release tags is not excused from reading them."""
    offenders = [
        f"{path}:{job}"
        for path, workflow in loaded().items()
        for job in shallow_pytest_jobs(workflow)
    ]
    assert not offenders, (
        f"jobs that run pytest on a shallow checkout: {offenders}. "
        "At depth 1 no `v*` tag is fetched, so "
        "`tests/behaviour/test_release_hygiene.py#"
        "test_this_checkout_has_tags_to_read_the_shipped_set_from` fails and "
        "the timer sweep cannot tell a shipped version from one being cut"
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
    for path, workflow in loaded().items():
        types = pull_request_types(workflow)
        reads = any(DRAFT_READER in script for script in scripts(workflow))
        for event in DRAFT_EVENTS:
            if reads:
                assert event in types, (
                    f"{path}: runs `{DRAFT_READER}` and `on.pull_request` "
                    f"does not list `{event}`. The default set is "
                    "opened/synchronize/reopened, so leaving draft state "
                    "re-runs nothing and the draft's green is what merges"
                )
            else:
                assert event not in types, (
                    f"{path}: `on.pull_request` lists `{event}` and nothing "
                    f"in the workflow runs `{DRAFT_READER}`, the one script "
                    "that reads draft state, so a ready press re-runs every "
                    "job on a commit they already ran"
                )


def test_the_edited_event_runs_wherever_the_body_is_read():
    """Otherwise a body sent after the pull request opened is read only on
    the next push.

    `chain_check.py` refuses a ready pull request whose body is not what
    `seal pr-body` composes at HEAD, reading the body from the event payload.
    Rewriting the body makes no commit, so no `synchronize` fires, and the
    `edited` payload is the one that carries the new body. Another step may
    read the body too, as this repository's issue-claims step does, so the
    event is not refused where `chain_check.py` does not run. Seen red
    against `templates/setup/hygiene.yml` before #1452, which did not list
    the event.
    """
    for path, workflow in loaded().items():
        if not any(DRAFT_READER in script for script in scripts(workflow)):
            continue
        assert BODY_EVENT in pull_request_types(workflow), (
            f"{path}: runs `{DRAFT_READER}` and `on.pull_request` does not "
            f"list `{BODY_EVENT}`. A body edit makes no commit, so the body "
            "the check reads stays the one the pull request had at its last "
            "push"
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
    workflows = loaded()
    assert TEMPLATE in workflows, "the shipped workflow is not among those read"
    for path, workflow in workflows.items():
        on = workflow["on"]
        if "pull_request" not in on:
            continue
        block = workflow.get("concurrency")
        assert block is not None, (
            f"{path}: runs on `pull_request` and declares no `concurrency:`, "
            "so every push to an open pull request leaves the last commit's "
            "runs to finish"
        )
        group = block.get("group", "")
        for part in ("github.workflow", "github.event.pull_request.number"):
            assert part in group, (
                f"{path}: the concurrency group {group!r} does not name "
                f"`{part}`; it has to be one workflow's runs of one pull "
                "request"
            )
        cancel = block.get("cancel-in-progress")
        if set(on) == {"pull_request"}:
            assert cancel in ("true", CANCEL_ON_PULL_REQUEST), (
                f"{path}: `cancel-in-progress` reads {cancel!r}, so a newer "
                "push leaves the older run to finish"
            )
            continue
        assert "|| github.run_id }}" in group, (
            f"{path}: the concurrency group {group!r} does not fall back to "
            "`github.run_id`, so a run that is not a pull request's shares a "
            "group with the next one on its ref, waits behind it, and is "
            "cancelled while pending by the one after"
        )
        assert cancel == CANCEL_ON_PULL_REQUEST, (
            f"{path}: also runs on {sorted(set(on) - {'pull_request'})} and "
            f"`cancel-in-progress` reads {cancel!r}; only "
            f"`{CANCEL_ON_PULL_REQUEST}` cancels a pull request's run and "
            "no other"
        )


def test_every_pytest_leg_has_a_timeout_and_the_job_reads_it():
    """Each `pytest` leg of `test.yml` carries a `timeout-minutes` past which
    GitHub fails the job (#841). It moved here from the slow-case module when
    that module's ceiling became a report (#942)."""
    job = load(TEST)["jobs"]["pytest"]
    entries = job["strategy"]["matrix"]["include"]
    assert entries
    budgets = [e.get("timeout", "") for e in entries]
    assert all(b.isdigit() for b in budgets), f"a leg with no timeout: {entries}"
    assert all(int(b) > 0 for b in budgets), entries
    assert job.get("timeout-minutes") == "${{ matrix.timeout }}", (
        "the job does not read the matrix's timeout"
    )


# What every `pytest` leg hands pytest so that its short summary names each
# skipped case and still names each failed one (#1221).
REPORT_FLAGS = ("-rfEs", "--no-fold-skipped")


def test_every_pytest_leg_names_each_case_it_skipped_and_each_it_failed():
    """#1221. A row that defers a platform question to a leg is answered by
    that leg's log, and only where the log names the case. Seen red with
    `--no-fold-skipped` deleted from the line, and with `-rfEs` written
    `-rs`."""
    runs = [
        step["run"]
        for step in load(TEST)["jobs"]["pytest"]["steps"]
        if step.get("run", "").startswith("pytest ")
    ]
    assert len(runs) == 1, runs
    words = runs[0].split()
    missing = [flag for flag in REPORT_FLAGS if flag not in words]
    assert not missing, (
        f"the pytest line does not pass {missing}: {runs[0]}. `-r` replaces "
        "pytest's default `fE`, so a leg passing `-rs` drops its FAILED lines, "
        "and without `--no-fold-skipped` the cases one helper skips fold under "
        "the helper's line and no case is named"
    )


def test_the_shipped_workflow_states_its_token_scope_and_reads_the_whole_history():
    """#1055 S8. The template's token was whatever the user's account
    defaulted to, which nobody installing it reads, and its steps write
    nothing and call no `gh`, so `contents: read` is the whole of what it
    needs. The chain check diffs against the base branch, so the checkout
    carries the whole history."""
    template = load(TEMPLATE)
    assert template.get("permissions") == {"contents": "read"}, template.get(
        "permissions"
    )
    found = [step for job in template["jobs"].values() for step in checkouts(job)]
    assert found and all(
        step.get("with", {}).get("fetch-depth") == "0" for step in found
    ), f"{TEMPLATE} checks out one commit: {found}"


# The comment `.github/workflows/hygiene.yml` carries above each step it
# shares with the template: the template is the step's one source.
POINTER = f"One source: `{TEMPLATE}`, the workflow the plugin ships."

# Where the chain checker's refusals are listed, which the template's comment
# on the chain step names instead of listing them.
REFUSALS = (
    "`docs/checks/the-pull-request-check.md` *What the check reads at the pull request*"
)
CHAIN_STEP = "a declared review chain has the round record it claimed"


def named_steps(path):
    """{step name: step} for the named steps of the workflow at PATH."""
    return {
        step["name"]: step
        for job in load(path)["jobs"].values()
        for step in job.get("steps", [])
        if "name" in step
    }


def comment_above(path, name):
    """The comment lines directly above the step called NAME in the file at
    PATH, each with its `#` off.

    The comment is the subject here, and a parser drops comments, so this
    reads the file's text: the one line `- name: NAME`, and the lines above
    it whose first non-blank character is `#`."""
    lines = read(path).splitlines()
    at = [i for i, line in enumerate(lines) if line.strip() == f"- name: {name}"]
    assert len(at) == 1, f"{path} names the step {name!r} {len(at)} times"
    above = []
    for line in reversed(lines[: at[0]]):
        if not line.lstrip().startswith("#"):
            break
        above.insert(0, line.lstrip()[1:].strip())
    return above


def command(run):
    """A `run:` script as one command: continuations joined, each whitespace
    run one space, and the clone's prefix taken off with its closing quote."""
    text = " ".join(line.strip().rstrip("\\") for line in run.splitlines())
    text = re.sub(re.escape(CLONE) + r'([^"]*)"', r"\1", text)
    return " ".join(text.split())


def test_the_steps_the_template_shares_have_one_source():
    """#1055 S9 and S10. Each step the template names stands in this
    repository's `hygiene.yml` under the same name and runs the same command,
    once the template's prefix for the plugin's clone is off: the repository
    runs the checker from its own tree, so a change to it is checked by
    itself. The repository's copy carries the one-line pointer and no other
    comment, and the template's comment on the chain step names the review
    record's section rather than listing the refusals."""
    template = named_steps(TEMPLATE)
    ours = named_steps(HYGIENE)
    shared = [name for name, step in template.items() if CLONE in step.get("run", "")]
    assert CHAIN_STEP in shared, sorted(template)
    for name in shared:
        assert name in ours, f"the template's step {name!r} is not in hygiene.yml"
        assert command(ours[name].get("run", "")) == command(template[name]["run"]), (
            name
        )
        assert comment_above(HYGIENE, name) == [POINTER], (
            name,
            comment_above(HYGIENE, name),
        )
    comment = " ".join(comment_above(TEMPLATE, CHAIN_STEP))
    assert REFUSALS in comment, comment
