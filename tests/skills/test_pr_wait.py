"""`skills/code-review/scripts/pr_wait.py`, one class per function.

No case reaches the real `gh` or a network. The cases of the wait replace
the module's `gh` with `Hub`, which serves JSON in the shapes `gh` 2.92.0
printed for this repository's pull request #1537 and records each call, and
replace its `clock` and `sleep` with `Clock`, which advances by what is
slept, so the two-minute limit runs at once. The cases of `gh` itself and
the one that runs the script as a process put a `gh` stub of their own
first on `PATH`, ahead of the suite's, and that stub answers from a file
and calls nothing else.
"""

import json
import os
import subprocess
import sys

import pytest
from conftest import ROOT, census_case, git, load_module, write

TARGET = "skills/code-review/scripts/pr_wait.py"

PR = load_module(os.path.join(ROOT, *TARGET.split("/")), "pr_wait_under_test")

HEAD = "a" * 40
BEFORE = "b" * 40

# One entry of `statusCheckRollup` as `gh pr view` printed it on #1537; the
# command reads only how many there are.
ROLLUP_ENTRY = {
    "__typename": "CheckRun",
    "name": "pytest (ubuntu-latest, 3.12)",
    "status": "IN_PROGRESS",
    "conclusion": "",
    "workflowName": "tests",
}


def view(state="OPEN", mergeable="MERGEABLE", head=HEAD, rollup=1):
    """`gh pr view --json state,mergeable,headRefOid,statusCheckRollup`."""
    return {
        "state": state,
        "mergeable": mergeable,
        "headRefOid": head,
        "statusCheckRollup": [ROLLUP_ENTRY] * rollup,
    }


def check(name, bucket, event="pull_request", workflow="tests"):
    """One entry of `gh pr checks --json name,workflow,event,bucket`."""
    return {"name": name, "workflow": workflow, "event": event, "bucket": bucket}


def run(status, workflow="tests"):
    """One entry of `gh run list --json status,workflowName`."""
    return {"status": status, "workflowName": workflow}


# The three calls the command makes, by their first two arguments.
VERBS = {
    ("pr", "view"): "view",
    ("pr", "checks"): "checks",
    ("run", "list"): "runs",
}


class Hub:
    """`gh` as the command calls it: each call recorded in order, and each
    verb answered from its own list of answers, the last repeating."""

    def __init__(self, views, checks=(), runs=()):
        self.served = {"view": list(views), "checks": list(checks), "runs": list(runs)}
        self.calls = []

    def gh(self, *args):
        self.calls.append(args)
        queue = self.served[VERBS[args[:2]]]
        answer = queue.pop(0) if len(queue) > 1 else queue[0]
        return json.dumps(answer)

    def verbs(self):
        return [VERBS[args[:2]] for args in self.calls]


class Clock:
    """The module's clock and sleep: time moves only by what is slept. A
    wait still going after an hour is a case gone wrong, and stops."""

    def __init__(self):
        self.now = 0.0

    def monotonic(self):
        return self.now

    def sleep(self, seconds):
        assert self.now < 3600, "the wait never ended"
        self.now += seconds


@pytest.fixture
def clock(monkeypatch):
    held = Clock()
    monkeypatch.setattr(PR, "clock", held.monotonic)
    monkeypatch.setattr(PR, "sleep", held.sleep)
    return held


def serve(monkeypatch, views, checks=(), runs=()):
    """A `Hub` answering in place of the module's `gh`."""
    hub = Hub(views, checks, runs)
    monkeypatch.setattr(PR, "gh", hub.gh)
    return hub


def stub_gh(tmp_path, monkeypatch, out="", err="", code=0):
    """A `gh` first on PATH that writes OUT and ERR, exits CODE, and records
    its arguments in `tmp_path/asked.json`."""
    home = tmp_path / "stub"
    home.mkdir()
    write(
        tmp_path,
        "answer.json",
        json.dumps({"out": out, "err": err, "code": code}),
    )
    script = home / "gh_stub.py"
    write(
        home,
        "gh_stub.py",
        "import json, sys\n"
        f"ANSWER, ASKED = {str(tmp_path / 'answer.json')!r}, "
        f"{str(tmp_path / 'asked.json')!r}\n"
        "with open(ASKED, 'w', encoding='utf-8') as handle:\n"
        "    json.dump(sys.argv[1:], handle)\n"
        "with open(ANSWER, encoding='utf-8') as handle:\n"
        "    answer = json.load(handle)\n"
        "sys.stdout.write(answer['out'])\n"
        "sys.stderr.write(answer['err'])\n"
        "sys.exit(answer['code'])\n",
    )
    if os.name == "nt":
        write(home, "gh.cmd", f'@"{sys.executable}" "{script}" %*\r\n')
    else:
        stub = home / "gh"
        write(home, "gh", f'#!/bin/sh\nexec "{sys.executable}" "{script}" "$@"\n')
        stub.chmod(0o755)
    monkeypatch.setenv("PATH", str(home) + os.pathsep + os.environ["PATH"])
    return tmp_path / "asked.json"


class Test_gh:
    def test_accepts_a_zero_exit_and_answers_its_stdout(self, tmp_path, monkeypatch):
        asked = stub_gh(tmp_path, monkeypatch, out='{"state":"OPEN"}\n')
        assert PR.gh("pr", "view", "12", "--json", "state") == '{"state":"OPEN"}\n'
        with open(asked, encoding="utf-8") as handle:
            assert json.load(handle) == ["pr", "view", "12", "--json", "state"]

    def test_refuses_a_non_zero_exit_naming_the_command_and_its_stderr(
        self, tmp_path, monkeypatch
    ):
        """S9, in the shape `gh pr view 999999 --json state` answered: a
        number GitHub does not resolve."""
        said = (
            "GraphQL: Could not resolve to a PullRequest with the number of 999999.\n"
        )
        stub_gh(tmp_path, monkeypatch, err=said, code=1)
        with pytest.raises(PR.Unanswered) as raised:
            PR.gh("pr", "view", "999999", "--json", "state")
        assert raised.value.lines() == [
            "could not ask: `gh pr view 999999 --json state` exited 1",
            "  GraphQL: Could not resolve to a PullRequest with the number of 999999.",
        ]

    def test_refuses_where_no_gh_is_on_path(self, tmp_path, monkeypatch):
        """S9: no `gh` to ask."""
        monkeypatch.setenv("PATH", str(tmp_path))
        with pytest.raises(PR.Unanswered) as raised:
            PR.gh("pr", "view", "12", "--json", "state")
        assert raised.value.lines() == ["could not ask: no `gh` on PATH"]


class Test_head:
    def test_accepts_a_checkout_and_answers_its_head(self, tmp_path, monkeypatch):
        git(tmp_path, "init", "-q")
        write(tmp_path, "a.txt", "a\n")
        git(tmp_path, "add", "a.txt")
        git(tmp_path, "-c", "user.name=e", "-c", "user.email=e@e", "commit", "-qm", "a")
        monkeypatch.chdir(tmp_path)
        assert PR.head() == git(tmp_path, "rev-parse", "HEAD").stdout.strip()

    def test_refuses_a_directory_git_cannot_read(self, tmp_path, monkeypatch):
        """S9: a working directory with no HEAD to wait on."""
        monkeypatch.chdir(tmp_path)
        monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path.parent))
        with pytest.raises(PR.Unanswered) as raised:
            PR.head()
        assert (
            raised.value.lines()[0] == "could not ask: `git rev-parse HEAD` exited 128"
        )


class Test_decide:
    def test_accepts_a_read_of_passed_and_skipped_checks(self):
        listed = [check("pytest", "pass"), check("lint", "skipping")]
        assert PR.decide(listed) == (0, ["every check passed or was skipped"])

    def test_refuses_a_failed_check_naming_its_workflow_and_name(self):
        """S2."""
        listed = [check("pytest", "pass"), check("pytest (windows)", "fail")]
        assert PR.decide(listed) == (
            1,
            ["a check failed or was cancelled", "  failed: tests / pytest (windows)"],
        )

    def test_refuses_a_cancelled_check_where_watch_passes_it(self):
        """S7: `gh pr checks --watch` exits 0 where the only bad check is in
        `cancel`; this command does not."""
        listed = [
            check("pytest", "pass"),
            check("hygiene", "cancel", workflow="hygiene"),
        ]
        assert PR.decide(listed) == (
            1,
            ["a check failed or was cancelled", "  cancelled: hygiene / hygiene"],
        )


class Test_wait:
    def test_accepts_a_push_before_any_check_has_reported(self, monkeypatch, clock):
        """S1: the checks are asked for only once the rollup is not empty,
        and the pass is decided on a read taken after every run completed."""
        hub = serve(
            monkeypatch,
            views=[view(rollup=0), view(rollup=0), view()],
            checks=[
                [check("pytest", "pending"), check("label", "pass", event="push")],
                [check("pytest", "pass"), check("label", "pass", event="push")],
            ],
            runs=[[run("completed"), run("completed", workflow="hygiene")]],
        )
        assert PR.wait(12, HEAD) == (0, ["every check passed or was skipped"])
        assert hub.verbs() == [
            "view",
            "view",
            "view",
            "checks",
            "view",
            "checks",
            "runs",
            "checks",
        ]
        assert hub.calls[-2] == (
            "run",
            "list",
            "--commit",
            HEAD,
            "--event",
            "pull_request",
            "--json",
            "status,workflowName",
        )

    def test_refuses_to_start_past_two_minutes_with_no_check(self, monkeypatch, clock):
        """S3."""
        hub = serve(monkeypatch, views=[view(rollup=0)])
        assert PR.wait(12, HEAD) == (
            3,
            [f"no check of a pull_request run was listed on {HEAD} within 120 seconds"],
        )
        assert clock.now == 120
        assert set(hub.verbs()) == {"view"}

    def test_refuses_a_head_that_is_still_the_commit_before_the_push(
        self, monkeypatch, clock
    ):
        """S4: the commit before the push has every check passed, and the
        command reads none of them."""
        hub = serve(
            monkeypatch,
            views=[view(head=BEFORE)],
            checks=[[check("pytest", "pass")]],
            runs=[[run("completed")]],
        )
        assert PR.wait(12, HEAD) == (
            3,
            [
                f"no check of a pull_request run was listed on {HEAD} within 120 "
                f"seconds, and the pull request's head stayed {BEFORE}"
            ],
        )
        assert set(hub.verbs()) == {"view"}

    def test_accepts_a_head_that_moves_to_the_pushed_commit(self, monkeypatch, clock):
        """S4: the head reaches HEAD within the limit, and the wait goes on
        from there."""
        hub = serve(
            monkeypatch,
            views=[view(head=BEFORE), view(head=BEFORE), view()],
            checks=[[check("pytest", "pass")]],
            runs=[[run("completed")]],
        )
        assert PR.wait(12, HEAD)[0] == 0
        assert hub.verbs()[:3] == ["view", "view", "view"]

    def test_refuses_to_start_on_another_events_finished_check(
        self, monkeypatch, clock
    ):
        """S5, in the shape of #1537's `label` check, of event `push`."""
        hub = serve(
            monkeypatch,
            views=[view()],
            checks=[[check("label", "pass", event="push", workflow="label")]],
            runs=[[run("completed")]],
        )
        assert PR.wait(12, HEAD) == (
            3,
            [f"no check of a pull_request run was listed on {HEAD} within 120 seconds"],
        )
        assert "runs" not in hub.verbs()

    def test_refuses_to_decide_while_a_run_has_not_completed(self, monkeypatch, clock):
        """S6: `pytest` has passed and `release-report`, which needs it, has
        no check yet; the run says it is not over, and the read after it
        has completed holds the dependent's failure."""
        passed = [check("pytest", "pass")]
        hub = serve(
            monkeypatch,
            views=[view()],
            checks=[passed, passed, [*passed, check("release-report", "fail")]],
            runs=[[run("in_progress")], [run("completed")]],
        )
        assert PR.wait(12, HEAD) == (
            1,
            ["a check failed or was cancelled", "  failed: tests / release-report"],
        )
        assert hub.verbs() == [
            "view",
            "checks",
            "runs",
            "view",
            "checks",
            "runs",
            "checks",
        ]

    def test_refuses_to_decide_on_a_last_read_that_holds_a_pending_check(
        self, monkeypatch, clock
    ):
        """The read after every run completed lists `hygiene` pending: a
        new run, started by an edit of the body, cancelled the one before it
        and has not been listed among the runs yet. The command polls on and
        decides on the read where `hygiene` has failed."""
        passed = [check("pytest", "pass")]
        rerun = [*passed, check("hygiene", "pending", workflow="hygiene")]
        hub = serve(
            monkeypatch,
            views=[view()],
            checks=[
                passed,
                rerun,
                [*passed, check("hygiene", "fail", workflow="hygiene")],
            ],
            runs=[[run("completed")]],
        )
        assert PR.wait(12, HEAD) == (
            1,
            ["a check failed or was cancelled", "  failed: hygiene / hygiene"],
        )
        assert hub.verbs() == [
            "view",
            "checks",
            "runs",
            "checks",
            "view",
            "checks",
            "runs",
            "checks",
        ]

    @pytest.mark.parametrize(
        "answer, code, outcome",
        [
            (view(state="MERGED", mergeable="UNKNOWN"), 4, "merged"),
            (view(state="CLOSED"), 5, "closed"),
            (view(mergeable="CONFLICTING"), 6, "conflicts with its base"),
        ],
    )
    def test_refuses_a_pull_request_that_is_not_open_and_mergeable(
        self, monkeypatch, clock, answer, code, outcome
    ):
        """S8, at the first read and at a later one."""
        serve(monkeypatch, views=[answer])
        assert PR.wait(12, HEAD) == (code, [outcome])
        hub = serve(
            monkeypatch,
            views=[view(), answer],
            checks=[[check("pytest", "pending")]],
        )
        assert PR.wait(12, HEAD) == (code, [outcome])
        assert hub.verbs() == ["view", "checks", "view"]

    def test_refuses_to_start_while_mergeable_is_never_known(self, monkeypatch, clock):
        """S8: `UNKNOWN` is read again, and past the limit it is said. The
        checks on HEAD have all passed, and the command asks for none of
        them while GitHub has not said the pull request can be merged."""
        hub = serve(
            monkeypatch,
            views=[view(mergeable="UNKNOWN")],
            checks=[[check("pytest", "pass")]],
            runs=[[run("completed")]],
        )
        assert PR.wait(12, HEAD) == (
            3,
            [
                f"no check of a pull_request run was listed on {HEAD} within 120 "
                "seconds, and GitHub never said whether the pull request is mergeable"
            ],
        )
        assert len(hub.calls) == 13

    def test_refuses_a_bucket_gh_does_not_name(self, monkeypatch, clock):
        """S9: a bucket none of gh's five is never read as `pass`."""
        serve(
            monkeypatch,
            views=[view()],
            checks=[[check("pytest", "pass"), check("lint", "succeeded")]],
        )
        with pytest.raises(PR.Unanswered) as raised:
            PR.wait(12, HEAD)
        assert raised.value.lines() == [
            "could not read the answer: `gh pr checks` answered bucket 'succeeded' for "
            "tests / lint, which is none of pass, skipping, fail, cancel, pending"
        ]


class Test_once:
    @pytest.mark.parametrize(
        "answer, code, outcome",
        [
            (view(mergeable="CONFLICTING", rollup=0), 0, "open"),
            (view(state="MERGED", mergeable="UNKNOWN"), 4, "merged"),
            (view(state="CLOSED"), 5, "closed"),
        ],
    )
    def test_accepts_one_read_of_the_state(self, monkeypatch, answer, code, outcome):
        """S8: one `gh pr view` and nothing else, whatever it answers."""
        hub = serve(monkeypatch, views=[answer])
        assert PR.once(12) == (code, HEAD, [outcome])
        assert hub.verbs() == ["view"]

    def test_refuses_a_state_gh_does_not_name(self, monkeypatch):
        """S9."""
        serve(monkeypatch, views=[view(state="DRAFT")])
        with pytest.raises(PR.Unanswered) as raised:
            PR.once(12)
        assert raised.value.lines() == [
            "could not read the answer: `gh pr view` answered state 'DRAFT', which is none of "
            "OPEN, MERGED, CLOSED"
        ]


class Test_main:
    def test_accepts_a_number_and_prints_the_outcome_on_one_line(
        self, monkeypatch, clock, capsys
    ):
        monkeypatch.setattr(PR, "head", lambda: HEAD)
        serve(monkeypatch, views=[view(state="CLOSED")])
        assert PR.main(["12"]) == 5
        assert (
            capsys.readouterr().out
            == f"seal pr-wait: pull request #12 at {HEAD}: closed\n"
        )

    def test_refuses_a_number_that_names_no_pull_request(self):
        with pytest.raises(SystemExit) as raised:
            PR.main(["0"])
        assert raised.value.code == 2

    def test_refuses_where_git_cannot_read_head(self, tmp_path, monkeypatch, capsys):
        """S9: nothing is asked of `gh` without a HEAD to wait on."""
        monkeypatch.chdir(tmp_path)
        monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path.parent))
        hub = serve(monkeypatch, views=[view()])
        assert PR.main(["12"]) == 2
        out = capsys.readouterr().out
        assert out.startswith(
            "seal pr-wait: pull request #12: could not ask: `git rev-parse HEAD` "
            "exited 128\n"
        )
        assert hub.calls == []

    def test_refuses_as_a_process_where_gh_answers_an_error(
        self, tmp_path, monkeypatch
    ):
        """S9 end to end: the script run as a process, through its own `gh`
        call, with `--once`, which reads no HEAD."""
        said = (
            "GraphQL: Could not resolve to a PullRequest with the number of 999999.\n"
        )
        stub_gh(tmp_path, monkeypatch, err=said, code=1)
        done = subprocess.run(
            [
                sys.executable,
                os.path.join(ROOT, *TARGET.split("/")),
                "999999",
                "--once",
            ],
            capture_output=True,
            encoding="utf-8",
            cwd=tmp_path,
        )
        assert done.returncode == 2
        assert done.stdout == (
            "seal pr-wait: pull request #999999: could not ask: `gh pr view 999999 "
            "--json state,mergeable,headRefOid,statusCheckRollup` exited 1\n"
            "  GraphQL: Could not resolve to a PullRequest with the number of 999999.\n"
        )


test_census = census_case(TARGET)
