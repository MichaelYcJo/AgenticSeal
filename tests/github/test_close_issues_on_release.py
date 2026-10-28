"""`.github/scripts/close_issues_on_release.py`, one class per function.

The closer runs when a release reaches `main`. It closes each issue a
shipped pull request claimed with a closing keyword, and takes `size: now`
off each issue it closes (#450). One issue the tracker refuses to close does
not leave the rest open (#536): a refusal on `gh issue close` takes the REST
route, a PATCH and then the same comment through `gh api ../comments`, and a
refusal on both routes is named with both errors at the end, after every
other issue was attempted.

The labels the cases' docstrings carry:

  A11  an issue carrying `size: now` that a shipped pull request claimed
       loses the label in the same act that closes it, and the issue closes
       even when that write fails
  S1   a refusal on `gh issue close` takes the REST route, and the run exits
       0 with every issue closed
  S2   a refusal on both routes is named with both errors, every other issue
       is still attempted and closed, the spent label still comes off each
       closed issue, and the exit is non-zero at the end

**Nothing here reaches GitHub.** `Tracker` and `RefusingTracker` record
every call as an argument tuple, in order, so a case can assert about a
write that did not happen and about the order of two writes. `Tracker`
closes everything it is asked to; `RefusingTracker` refuses the issues a
case names, on one route or both. `_offline` shuts every door the module has
to the tracker, for the cases that stub its readers by name.

**A11's second half is the one a green run hides.** An issue that closed
and kept a stale label is a wrong answer on a tracker; an issue left open
because a label write failed is a release that did not finish. So the
failing-write case asserts the close happened anyway, and the ordering case
asserts the close was made first.

**Shown red before it was committed (contract rule 15).** The A11 cases
were run against the script with the one behaviour each pins removed, in
phase 4 of work item `1790076050-the-release-tail-is-three-acts-no-document-names`,
whose directory #514's fold retired, so that record is read from history.
S1 and S2 fail at the commit before #536's fix, where `run` exits on the
refused close; phase 1's record of work item
`1790173209-the-release-tail-stops-at-the-first-issue-it-cannot-close`
quotes both outputs.

#942's phase 6 placed these cases from
`tests/test_a_declared_label_reaches_the_tracker.py`,
`tests/test_the_closer_carries_on_past_a_refusal.py` and
`tests/test_release_hygiene.py`, which keep the cases that read the
workflow, the documents and the records.
"""

import ast
import importlib.util
import json
import os
import re
import sys

import pytest
from conftest import ROOT, census_case, commit_everything, git_out, git_repo, read

TARGET = ".github/scripts/close_issues_on_release.py"

SCRIPTS = os.path.join(ROOT, ".github", "scripts")

REPO = "example/repo"
LABEL = "size: now"
GRAPHQL_REFUSAL = "GraphQL: Something went wrong while executing your query"
REST_REFUSAL = "HTTP 502: Bad Gateway"


def read_text(*parts):
    return read(os.path.join(ROOT, *parts))


def load(name, filename):
    spec = importlib.util.spec_from_file_location(
        f"agentic_{name}_for_label_tests", os.path.join(SCRIPTS, filename)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def closer_module():
    return load("close_issues_on_release", "close_issues_on_release.py")


def _closer():
    """The release-closing script, imported so its regexes can be read.

    Round 2: every string the first version of this case pinned also lives in
    the module docstring, so the whole script could be replaced by a seven-line
    stub carrying those words and all twelve tests passed. A string search
    cannot see what a regex matches."""
    import importlib.util

    path = os.path.join(ROOT, ".github", "scripts", "close_issues_on_release.py")
    spec = importlib.util.spec_from_file_location("close_issues_on_release", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Tracker:
    """A repository's issues, pull requests and labels, and every call made."""

    def __init__(self, issues=None, pulls=None, labels=(), refuse=()):
        self.issues = {n: list(v) for n, v in (issues or {}).items()}
        self.states = dict.fromkeys(self.issues, "open")
        self.pulls = dict(pulls or {})
        self.labels = set(labels)
        self.refuse = set(refuse)
        self.calls = []

    def api(self, repo, number):
        if number in self.pulls:
            return {"pull_request": {}, "body": self.pulls[number]}, True
        if number in self.issues:
            return {
                "labels": [{"name": name} for name in self.issues[number]],
                "state": self.states[number],
            }, True
        return None, False

    def run(self, *args):
        self.calls.append(args)
        if args[:3] == ("gh", "label", "list"):
            return json.dumps([{"name": name} for name in sorted(self.labels)])
        if args[:3] == ("gh", "label", "create"):
            self.labels.add(args[3])
            return ""
        raise AssertionError(f"unexpected command: {args}")

    def attempt(self, *args):
        """Stands in for the closer's `attempt`, which the close goes through
        since #536 so a refusal cannot end the run. Every close succeeds here;
        the refusing tracker is `RefusingTracker` below."""
        self.calls.append(args)
        if args[:3] == ("gh", "issue", "close"):
            self.states[int(args[3])] = "closed"
            return True, ""
        raise AssertionError(f"unexpected command: {args}")

    def edit(self, command, **kwargs):
        """Stands in for `subprocess.run` on the label removal alone."""
        self.calls.append(tuple(command))
        number = int(command[3])

        class Result:
            pass

        result = Result()
        if number in self.refuse:
            result.returncode, result.stderr = 1, "HTTP 502"
            return result
        if LABEL in self.issues.get(number, []):
            self.issues[number].remove(LABEL)
        result.returncode, result.stderr = 0, ""
        return result

    def writes(self):
        return [a for a in self.calls if a[:3] != ("gh", "label", "list")]


def wire_closer(monkeypatch, tracker, subjects):
    mod = closer_module()
    monkeypatch.setattr(mod, "arrived", lambda before, after: subjects)
    monkeypatch.setattr(mod, "_issue_api", tracker.api)
    monkeypatch.setattr(mod, "run", tracker.run)
    monkeypatch.setattr(mod, "attempt", tracker.attempt)
    monkeypatch.setattr(mod.subprocess, "run", tracker.edit)
    monkeypatch.setenv("AFTER", "aaa")
    monkeypatch.setenv("BEFORE", "bbb")
    monkeypatch.setenv("REPO", REPO)
    monkeypatch.delenv("DRY_RUN", raising=False)
    return mod


class RefusingTracker:
    """Issues with labels and states, pull request bodies, and every call.

    `refuse_close` is the set of issue numbers `gh issue close` refuses, the
    way the tracker refused #515 — AFTER the comment landed, because
    `gh issue close --comment` posts the comment and then sends the close,
    and the refused issue at the previous release carried the workflow's
    comment (round 1, finding 1). `refuse_before_comment` is the other order,
    a refusal that left nothing on the issue. `refuse_rest` is the set the
    REST PATCH refuses too. Both routes record the comment they post, so a
    case can count what the issue ends up carrying.
    """

    def __init__(
        self, issues, pulls, refuse_close=(), refuse_rest=(), refuse_before_comment=()
    ):
        self.issues = {n: list(labels) for n, labels in issues.items()}
        self.states = dict.fromkeys(self.issues, "open")
        self.pulls = dict(pulls)
        self.refuse_close = set(refuse_close)
        self.refuse_rest = set(refuse_rest)
        self.refuse_before_comment = set(refuse_before_comment)
        self.comments = {n: [] for n in self.issues}
        self.calls = []

    def api(self, repo, number):
        if number in self.pulls:
            return {"pull_request": {}, "body": self.pulls[number]}, True
        if number in self.issues:
            return {
                "labels": [{"name": name} for name in self.issues[number]],
                "state": self.states[number],
                "comments": len(self.comments[number]),
            }, True
        return None, False

    def run(self, *args):
        """The exiting runner. Before the fix the close went through it, and
        a refusal here is what `run` does with one: `sys.exit`."""
        self.calls.append(args)
        if args[:3] == ("gh", "issue", "close"):
            ok, error = self.attempt(*args)
            self.calls.pop()
            if not ok:
                raise SystemExit(f"{' '.join(args)} failed: {error}")
            return ""
        raise AssertionError(f"unexpected command: {args}")

    def attempt(self, *args):
        """`(ok, stderr)` for a write, the shape the fixed closer reads."""
        self.calls.append(args)
        if args[:3] == ("gh", "issue", "close"):
            number = int(args[3])
            if number in self.refuse_before_comment:
                return False, GRAPHQL_REFUSAL
            # The comment lands first and the close is what gets refused:
            # the order the tracker showed (round 1, finding 1).
            self.comments[number].append(args[args.index("--comment") + 1])
            if number in self.refuse_close:
                return False, GRAPHQL_REFUSAL
            self.states[number] = "closed"
            return True, ""
        if args[:2] == ("gh", "api"):
            path = next(a for a in args if a.startswith(f"repos/{REPO}/issues/"))
            number = int(path.split("/")[4])
            field = next(a for a in args if "=" in a and not a.startswith("-"))
            if path.endswith("/comments"):
                assert field.startswith("body="), args
                self.comments[number].append(field[len("body=") :])
                return True, ""
            assert "-X" in args and args[args.index("-X") + 1] == "PATCH", args
            assert field == "state=closed", args
            if number in self.refuse_rest:
                return False, REST_REFUSAL
            self.states[number] = "closed"
            return True, ""
        raise AssertionError(f"unexpected command: {args}")

    def edit(self, command, **kwargs):
        """Stands in for `subprocess.run` on the label removal alone."""
        self.calls.append(tuple(command))
        assert command[:3] == ["gh", "issue", "edit"], command
        number = int(command[3])

        class Result:
            returncode, stderr = 0, ""

        if LABEL in self.issues.get(number, []):
            self.issues[number].remove(LABEL)
        return Result()

    def closes(self):
        """`(number, route)` for every close attempted, in order."""
        out = []
        for args in self.calls:
            if args[:3] == ("gh", "issue", "close"):
                out.append((int(args[3]), "gh issue close"))
            elif args[:2] == ("gh", "api") and "-X" in args:
                path = next(a for a in args if a.startswith("repos/"))
                out.append((int(path.split("/")[4]), "gh api PATCH"))
        return out


def wire(monkeypatch, tracker):
    mod = closer_module()
    monkeypatch.setattr(mod, "arrived", lambda before, after: ["feat: a thing (#100)"])
    monkeypatch.setattr(mod, "_issue_api", tracker.api)
    monkeypatch.setattr(mod, "run", tracker.run)
    # `raising=False` so the case is red for its own reason on the tree
    # before the fix, where no `attempt` exists and every close goes through
    # `run` — rather than red on this line.
    monkeypatch.setattr(mod, "attempt", tracker.attempt, raising=False)
    monkeypatch.setattr(mod.subprocess, "run", tracker.edit)
    monkeypatch.setenv("AFTER", "aaa")
    monkeypatch.setenv("BEFORE", "bbb")
    monkeypatch.setenv("REPO", REPO)
    monkeypatch.delenv("DRY_RUN", raising=False)
    return mod


THREE = {1: [LABEL], 2: [LABEL], 3: [LABEL]}
CLAIMS = {100: "Closes #1\nCloses #2\nCloses #3"}


def _offline(monkeypatch, m, closed):
    """Shut every door this module has to the tracker, and make an escape loud.

    **Why this exists** — CI, 2026-09-22, on the pull request that merged
    #450. Three cases below stubbed `arrived`, `pull_request_body`,
    `issue_state` and `run`, and that was the whole set of readers `main`
    used. The label work added one more: `main` now asks `issue_labels`
    whether the issue carries a spent `size: now`, and that goes through
    `_issue_api`, which nothing here had stubbed. So all three walked into a
    live `gh api` call.

    **They passed anyway on every machine that ran them**, because `gh` is
    authenticated on a developer's laptop and under the broad gate. CI's
    pytest job has no `GH_TOKEN`, correctly, and it was the first party in
    the whole run that could see it: `SystemExit: gh api issues/88 failed`,
    on both the ubuntu and macOS legs, against `4164 passed`.

    That is the defect worth naming: **a case that reaches the network cannot
    fail for the reason it claims to test**, and whether it passes depends on
    who is logged in rather than on the code. Stubbing the one reader that
    leaked would have fixed the instance; this closes the class.

    Two doors, and both are shut here:

    - `_issue_api` is the only READ into the tracker, and `issue_state`,
      `pull_request_body` and `issue_labels` all go through it. Cases that
      stub those three by name keep their own stubs; this catches whatever
      they did not name, now or later.
    - `subprocess.run` is what `run` and `drop_label` reach for, and it
      RAISES rather than returning a stub, so a future path that escapes
      fails loudly and identically for everyone instead of passing for
      whoever holds a token.
    """

    def no_network(*args, **kwargs):
        raise AssertionError(
            f"this case reached the network: {args[0] if args else kwargs}. "
            "A case that calls `gh` passes or fails on whether the runner is "
            "authenticated, not on the code under test — CI caught exactly "
            "that on #500 and no local run could have"
        )

    monkeypatch.setattr(m.subprocess, "run", no_network)
    # An issue that exists and carries no labels: consistent with the
    # `issue_state` stubs above it, and it leaves `spent` False, so no case
    # here changes what it asserts.
    monkeypatch.setattr(m, "_issue_api", lambda repo, number: ({"labels": []}, True))
    monkeypatch.setattr(m, "run", lambda *a: closed.append(a) or "")
    # The close goes through `attempt` since #536, so a refusal cannot end
    # the run; it is the third door, and every close through it succeeds.
    monkeypatch.setattr(m, "attempt", lambda *a: closed.append(a) or (True, ""))


class Test_keywords_in:
    def test_accepts_only_a_keyword_before_a_number(self):
        """The regexes, read rather than searched for.

        The fenced `Closes #88` in `docs/branch-and-release.md` is the example a
        person copies, so a pull request body quoting the document must not close
        the issue the document names — and bodies here quote documents routinely.
        """
        m = _closer()
        assert m.keywords_in("Closes #88") == ["88"]
        assert m.keywords_in("Closes #88, closes #92") == ["88", "92"]
        assert m.keywords_in("Part of #90") == []
        assert m.keywords_in("see #90 and #92") == [], (
            "a bare number with no keyword closes an issue"
        )
        assert m.keywords_in("```\nCloses #88\n```") == [], (
            "a fenced example closes the issue it names"
        )
        assert m.keywords_in("see `Closes #54` in the doc") == [], (
            "an inline code span closes the issue it names"
        )
        assert m.keywords_in("```\nCloses #1\n```\nCloses #88") == ["88"], (
            "prose after a fence stopped being read"
        )
        assert m.MERGED_PR.search("feat: a thing (#100)").group(1) == "100"
        assert m.MERGED_PR.search("fix: the (#61) thing was wrong") is None, (
            "a number mid-subject is read as a merged pull request"
        )

    # #266: review round 1 of work item 1788844400 enumerated five well-formed
    # shapes `FENCE` and `SPAN` did not mask, by construction rather than by
    # reading. A closing keyword inside any of them was read as a claim, so a
    # RELEASE closed the issue. Three are masked now and two are deliberately
    # not; each of the five has a case, so a later widening or narrowing is a
    # red rather than a drift. The direction is stated at the patterns:
    # masking more closes fewer, and an unclosed issue is visible and
    # re-runnable where a wrong close is a false record on the tracker.

    def test_refuses_a_keyword_inside_a_tilde_fence(self):
        """`~~~` is a fence to CommonMark and to GitHub, and it was invisible here
        because the pattern spelled backticks."""
        m = _closer()
        assert m.keywords_in("~~~\nCloses #1\n~~~\nCloses #4") == ["4"], (
            "a keyword inside a tilde fence closes the issue it names"
        )
        # A fence closes on ITS delimiter. Read as any delimiter, this one ends
        # at the backticks and the keyword after them is prose.
        assert m.keywords_in("~~~\n```\nCloses #1\n~~~\nCloses #4") == ["4"], (
            "a tilde fence was closed by a backtick line inside it"
        )

    def test_a_fence_indented_under_a_list_item_masks_a_keyword(self):
        """A fence inside a list item is indented to the item's content, and the
        pattern anchored the delimiter at column 0."""
        m = _closer()
        body = "- the example:\n  ```\n  Closes #2\n  ```\nCloses #4"
        assert m.keywords_in(body) == ["4"], (
            "a keyword inside a fence indented under a list item closes the issue"
        )

    def test_a_double_backtick_span_masks_a_keyword(self):
        """A span opened with two backticks closes with two, and may hold a
        single backtick inside. The one-backtick pattern read `` ``#150`` `` as
        two EMPTY spans with the number in prose between them."""
        m = _closer()
        assert m.keywords_in("Closes ``#3``\nCloses #4") == ["4"], (
            "a double-backtick span around the number leaves the keyword read"
        )
        assert m.keywords_in("see ``Closes #3`` there\nCloses #4") == ["4"], (
            "a double-backtick span around the whole claim leaves it read"
        )
        # The inner backtick is UNPAIRED on purpose: with a pair, the one-backtick
        # arm masks the claim anyway and the double form's reach is unmeasured.
        assert m.keywords_in("see ``Closes #3 ` x`` and Closes #4") == ["4"], (
            "a double-backtick span holding a single backtick is cut at the inner backtick"
        )

    @pytest.mark.parametrize(
        ("body", "claimed"),
        [
            # Four spaces open an indented code block to CommonMark, and they
            # are ALSO how this repository's pull request bodies continue a
            # bullet's text onto the next line, so masking the shape would
            # drop real claims, which is the wrong direction for a closer.
            ("- a bullet whose text\n    Closes #5", ["5"]),
            # Whether GitHub acts on a keyword inside an HTML comment is
            # unmeasured (`docs/issues-and-milestones.md` *A keyword claims
            # the one number after it*), and a measurement needs a scratch
            # pull request on a tracker; until it is taken the shape stays.
            ("<!-- Closes #6 -->", ["6"]),
        ],
    )
    def test_accepts_a_shape_left_unmasked_as_a_claim(self, body, claimed):
        """Deliberately unmasked, each for the reason above its row. Stated at
        the pattern; this case turns a future widening into a decision."""
        m = _closer()
        assert m.keywords_in(body) == claimed


class Test_run:
    def test_accepts_a_call_that_succeeds_and_answers_what_it_printed(self):
        """The real call, through this interpreter, which every CI leg has.
        Every case of `Test_main` replaces `run`."""
        mod = closer_module()
        assert mod.run(sys.executable, "-c", "print('the labels')") == "the labels\n"

    def test_refuses_a_failed_call_by_exiting_and_naming_what_it_wrote(self):
        """A read the rest of the run depends on stops the run when it fails,
        and the exit carries the call's own error."""
        mod = closer_module()
        failing = "import sys; sys.stderr.write('HTTP 502'); sys.exit(3)"
        with pytest.raises(SystemExit) as stopped:
            mod.run(sys.executable, "-c", failing)
        assert "HTTP 502" in str(stopped.value.code)


def _gh_answers(monkeypatch, mod, returncode, stdout="", stderr=""):
    """`gh api` replaced by one answer, so `_issue_api` itself is what runs."""

    class Result:
        pass

    result = Result()
    result.returncode, result.stdout, result.stderr = returncode, stdout, stderr
    monkeypatch.setattr(mod.subprocess, "run", lambda *a, **k: result)


class Test__issue_api:
    def test_accepts_a_404_as_an_issue_that_does_not_exist(self, monkeypatch):
        """A number that names nothing is input, from a `(#N)` typed in a
        subject or a typo in a body, and a release does not stop on it."""
        mod = closer_module()
        _gh_answers(monkeypatch, mod, 1, stderr="gh: Not Found (HTTP 404)")
        assert mod._issue_api(REPO, 9999) == (None, False)

    def test_refuses_any_other_failure_by_exiting(self, monkeypatch):
        mod = closer_module()
        _gh_answers(monkeypatch, mod, 1, stderr=REST_REFUSAL)
        with pytest.raises(SystemExit) as stopped:
            mod._issue_api(REPO, 7)
        assert REST_REFUSAL in str(stopped.value.code)


class Test_issue_state:
    def test_accepts_a_closed_issue_as_closed(self, monkeypatch):
        """`main` leaves a closed issue alone only because this says closed."""
        mod = closer_module()
        monkeypatch.setattr(mod, "_issue_api", lambda r, n: ({"state": "closed"}, True))
        assert mod.issue_state(REPO, 7) == "closed"

    def test_refuses_an_issue_that_does_not_exist_as_no_state(self, monkeypatch):
        mod = closer_module()
        monkeypatch.setattr(mod, "_issue_api", lambda r, n: (None, False))
        assert mod.issue_state(REPO, 9999) is None


class Test_comments_on:
    def test_accepts_the_count_the_read_gave(self, monkeypatch):
        mod = closer_module()
        monkeypatch.setattr(mod, "_issue_api", lambda r, n: ({"comments": 2}, True))
        assert mod.comments_on(REPO, 7) == 2

    def test_refuses_a_read_that_gave_no_count_as_none(self, monkeypatch):
        """None, never 0: `close_issue` posts the comment where the count is
        unknown, and a 0 would read as a count it can compare."""
        mod = closer_module()
        monkeypatch.setattr(mod, "_issue_api", lambda r, n: ({"state": "open"}, True))
        assert mod.comments_on(REPO, 7) is None


def _refused_first_route(monkeypatch, counts):
    """The closer with `gh issue close` refused and the REST route taken,
    and `comments_on` answering COUNTS in turn; the closer and its calls."""
    mod = closer_module()
    calls = []
    reads = iter(counts)

    def attempt(*args):
        calls.append(args)
        if args[:3] == ("gh", "issue", "close"):
            return False, GRAPHQL_REFUSAL
        return True, ""

    monkeypatch.setattr(mod, "attempt", attempt)
    monkeypatch.setattr(mod, "comments_on", lambda repo, number: next(reads))
    return mod, calls


class Test_close_issue:
    def test_accepts_a_count_grown_by_one_as_the_comment_already_posted(
        self, monkeypatch
    ):
        mod, calls = _refused_first_route(monkeypatch, [0, 1])
        assert mod.close_issue(REPO, 7, "Closed by #100") == []
        assert not [a for a in calls if a[2].endswith("/comments")], calls

    def test_refuses_a_count_it_could_not_read_as_zero_and_posts_the_comment(
        self, monkeypatch
    ):
        """Unread before the first route and one after it says nothing about
        whether that route's comment landed, so the comment is posted."""
        mod, calls = _refused_first_route(monkeypatch, [None, 1])
        assert mod.close_issue(REPO, 7, "Closed by #100") == []
        posted = [a for a in calls if a[2] == f"repos/{REPO}/issues/7/comments"]
        assert posted, f"the closing comment was not posted: {calls}"


class Test_pull_request_body:
    def test_accepts_a_pull_request_with_no_body_as_an_empty_one(self, monkeypatch):
        mod = closer_module()
        answer = ({"pull_request": {}, "body": None}, True)
        monkeypatch.setattr(mod, "_issue_api", lambda r, n: answer)
        assert mod.pull_request_body(REPO, 100) == ""

    def test_refuses_an_issues_body_as_a_pull_requests(self, monkeypatch):
        """`/issues/N` answers for an issue too, and only a pull request
        carries `pull_request`. An issue's own `Closes #7` is no claim."""
        mod = closer_module()
        answer = ({"body": "Closes #7"}, True)
        monkeypatch.setattr(mod, "_issue_api", lambda r, n: answer)
        assert mod.pull_request_body(REPO, 61) is None


def _three_commits(tmp_path, monkeypatch):
    """A scratch repository of three commits, the working directory moved
    into it; their SHAs, oldest first."""
    repo = git_repo(tmp_path / "repo")
    shas = [git_out(repo, "rev-parse", "HEAD")]
    for number in (2, 3):
        (repo / f"{number}.txt").write_text(f"{number}\n", encoding="utf-8")
        shas.append(commit_everything(repo, f"feat: commit {number} (#{number})"))
    monkeypatch.chdir(repo)
    return shas


class Test_arrived:
    def test_accepts_every_subject_in_the_range(self, tmp_path, monkeypatch):
        """Real git in a scratch repository. A release push carries several
        pull requests, and reading the tip alone drops all but one."""
        mod = closer_module()
        base, _, tip = _three_commits(tmp_path, monkeypatch)
        assert mod.arrived(base, tip) == ["feat: commit 3 (#3)", "feat: commit 2 (#2)"]

    def test_refuses_an_all_zero_before_as_a_range_and_reads_the_tip(
        self, tmp_path, monkeypatch, capsys
    ):
        """A branch's first push names no commit before it, and a range from
        the zero SHA is no range git can read."""
        mod = closer_module()
        _, _, tip = _three_commits(tmp_path, monkeypatch)
        assert mod.arrived("0" * 40, tip) == ["feat: commit 3 (#3)"]
        assert "reading only the tip" in capsys.readouterr().out


class Test_main:
    def test_a_spent_label_comes_off_the_issue_the_release_closed(self, monkeypatch):
        """A11. The loop already knows exactly which issues shipped, which is the
        fact a person would otherwise reconstruct by hand."""
        tracker = Tracker(issues={7: [LABEL, "release"]}, pulls={100: "Closes #7"})
        mod = wire_closer(monkeypatch, tracker, ["feat: a thing (#100)"])
        mod.main()
        assert tracker.states[7] == "closed"
        assert LABEL not in tracker.issues[7], "the spent label survived the close"
        assert "release" in tracker.issues[7], "it removed a label it was not asked to"

    def test_the_close_comes_first_so_a_failed_label_write_cannot_cost_it(
        self, monkeypatch
    ):
        """A11's second half, asserted on the ORDER rather than on the outcome.

        Both acts succeeding tells you nothing about which would survive the
        other failing. The close is what this script exists for; the label is
        bookkeeping about it.
        """
        tracker = Tracker(issues={7: [LABEL]}, pulls={100: "Closes #7"})
        mod = wire_closer(monkeypatch, tracker, ["feat: a thing (#100)"])
        mod.main()
        closes = [
            i for i, a in enumerate(tracker.calls) if a[:3] == ("gh", "issue", "close")
        ]
        edits = [i for i, a in enumerate(tracker.calls) if "--remove-label" in a]
        assert closes and edits, tracker.calls
        assert closes[0] < edits[0], (
            "the label is removed before the issue is closed, so a failing label "
            "write takes the close with it"
        )

    def test_the_issue_closes_even_when_the_label_write_fails(
        self, monkeypatch, capsys
    ):
        """A11's stated direction: the issue closes either way."""
        tracker = Tracker(issues={7: [LABEL]}, pulls={100: "Closes #7"}, refuse={7})
        mod = wire_closer(monkeypatch, tracker, ["feat: a thing (#100)"])
        mod.main()
        assert tracker.states[7] == "closed"
        out = capsys.readouterr().out
        assert "could not remove" in out and "closed either way" in out, (
            "a failed label write is silent, so a stale label looks like one "
            "nobody was supposed to remove"
        )

    def test_an_issue_without_the_label_gets_no_label_call(self, monkeypatch):
        """Most issues do not carry it, and a write per issue to remove a label
        that is not there is a call per issue for nothing."""
        tracker = Tracker(issues={7: ["release"]}, pulls={100: "Closes #7"})
        mod = wire_closer(monkeypatch, tracker, ["feat: a thing (#100)"])
        mod.main()
        assert not [a for a in tracker.calls if "--remove-label" in a], tracker.calls

    def test_a_dry_run_writes_neither_the_close_nor_the_removal(
        self, monkeypatch, capsys
    ):
        tracker = Tracker(issues={7: [LABEL]}, pulls={100: "Closes #7"})
        mod = wire_closer(monkeypatch, tracker, ["feat: a thing (#100)"])
        monkeypatch.setenv("DRY_RUN", "1")
        mod.main()
        assert tracker.states[7] == "open"
        assert LABEL in tracker.issues[7]
        out = capsys.readouterr().out
        assert "would close #7" in out and f"would remove {LABEL!r} from #7" in out

    # The already-closed issue, which no case reached (round 1, finding 1).
    # Every A11 case above puts the issue in the `open` state, so all of them
    # walk the branch that closes it. The loop's OTHER branch — an issue a
    # previous run closed, or one closed by hand, still carrying a spent label
    # — was reachable in production and by no case, and both of its defects
    # lived there.

    def test_an_already_closed_issue_reports_no_removal_that_failed(
        self, monkeypatch, capsys
    ):
        """The job log is the only record of what a release did to the tracker.

        Unguarded, a refused write printed `could not remove …` and then
        `removed …` for the same issue in one log, with the tracker in the state
        the first line describes and the second denies — and the second is the
        line a reader takes away.
        """
        tracker = Tracker(issues={7: [LABEL]}, pulls={100: "Closes #7"}, refuse={7})
        tracker.states[7] = "closed"
        mod = wire_closer(monkeypatch, tracker, ["feat: a thing (#100)"])
        mod.main()
        out = capsys.readouterr().out
        assert "could not remove" in out, "the failed write is not reported at all"
        assert f"removed {LABEL!r} from #7" not in out, (
            "the log says the label came off an issue it is still on"
        )
        assert LABEL in tracker.issues[7]

    def test_an_already_closed_issue_reports_a_removal_that_worked(
        self, monkeypatch, capsys
    ):
        """The other direction of the same branch, so the case above cannot be
        satisfied by never reporting anything."""
        tracker = Tracker(issues={7: [LABEL]}, pulls={100: "Closes #7"})
        tracker.states[7] = "closed"
        mod = wire_closer(monkeypatch, tracker, ["feat: a thing (#100)"])
        mod.main()
        assert f"removed {LABEL!r} from #7" in capsys.readouterr().out
        assert LABEL not in tracker.issues[7], "the spent label survived"

    def test_a_dry_run_over_an_already_closed_issue_names_the_label_too(
        self, monkeypatch, capsys
    ):
        """A preview silent about half the act is the failure `DRY_RUN` exists to
        prevent — by this script's own stated reason for having the arm. The
        open-issue path said `would remove`; this one said nothing, so a person
        reading a dry run concluded the label was out of scope."""
        tracker = Tracker(issues={7: [LABEL]}, pulls={100: "Closes #7"})
        tracker.states[7] = "closed"
        mod = wire_closer(monkeypatch, tracker, ["feat: a thing (#100)"])
        monkeypatch.setenv("DRY_RUN", "1")
        mod.main()
        out = capsys.readouterr().out
        assert f"would remove {LABEL!r} from #7" in out
        assert LABEL in tracker.issues[7], "a dry run wrote to the tracker"
        assert not [a for a in tracker.calls if "--remove-label" in a], tracker.calls

    def test_a_refused_close_takes_the_rest_route_and_the_run_finishes(
        self, monkeypatch, capsys
    ):
        """S1. The tracker refuses `gh issue close 2` the way it refused #515;
        the PATCH closes it, the comment follows through the API, and #3 —
        sorted after it — is closed as well. Exit 0: nothing is left for a
        person to repair."""
        tracker = RefusingTracker(THREE, CLAIMS, refuse_close={2})
        mod = wire(monkeypatch, tracker)

        mod.main()

        assert tracker.states == {1: "closed", 2: "closed", 3: "closed"}, (
            f"a refusal on #2 left the tracker at {tracker.states}"
        )
        assert tracker.closes() == [
            (1, "gh issue close"),
            (2, "gh issue close"),
            (2, "gh api PATCH"),
            (3, "gh issue close"),
        ], tracker.calls
        out = capsys.readouterr().out
        assert "closed #2" in out and "REST" in out and GRAPHQL_REFUSAL in out, (
            f"the log does not say #2 took the fallback, or why: {out!r}"
        )

    def test_the_fallback_posts_the_same_comment_the_first_route_carries(
        self, monkeypatch
    ):
        """The comment is the last thing written on an issue people go on
        reading, and it says why a workflow closed it. An issue closed through
        the REST route ends up with the same sentence ONCE: `gh issue close
        --comment` posts the comment before the close it then fails, so the
        refused route usually left it already, and the fallback must not post it
        a second time. Measured on the tracker after the previous release: the
        issue that run could not close carried one identical comment per refused
        run (round 1, finding 1)."""
        tracker = RefusingTracker(THREE, CLAIMS, refuse_close={2})
        mod = wire(monkeypatch, tracker)

        mod.main()

        assert len(tracker.comments[2]) == 1, (
            f"#2 carries {len(tracker.comments[2])} closing comments; the refused "
            f"route had already posted one"
        )
        assert tracker.comments[2] == tracker.comments[1], (
            f"the REST route's comment differs from the first route's:\n"
            f"{tracker.comments[2][0]!r}\n{tracker.comments[1][0]!r}"
        )
        assert "Closed by #100" in tracker.comments[2][0]

    def test_a_refusal_before_the_comment_landed_still_gets_it_from_the_fallback(
        self,
        monkeypatch,
    ):
        """The other order: the comment mutation is what the tracker refused, so
        nothing is on the issue yet and the fallback has to say why it closed."""
        tracker = RefusingTracker(THREE, CLAIMS, refuse_before_comment={2})
        mod = wire(monkeypatch, tracker)

        mod.main()

        assert tracker.states[2] == "closed"
        assert tracker.comments[2] == tracker.comments[1], tracker.comments

    def test_a_tracker_that_does_not_count_comments_gets_the_comment_posted(
        self,
        monkeypatch,
    ):
        """Where the read cannot say whether the first route's comment landed,
        the fallback posts it: a duplicate is the smaller wrong answer than a
        close nobody explained."""

        class Uncounted(RefusingTracker):
            def api(self, repo, number):
                data, exists = super().api(repo, number)
                if exists:
                    data.pop("comments", None)
                return data, exists

        tracker = Uncounted(THREE, CLAIMS, refuse_close={2})
        mod = wire(monkeypatch, tracker)

        mod.main()

        assert tracker.states[2] == "closed"
        assert len(tracker.comments[2]) == 2, tracker.comments

    def test_an_issue_closed_through_the_fallback_still_loses_its_spent_label(
        self,
        monkeypatch,
    ):
        """The label comes off after the close, whichever route closed it. A
        fallback that skipped the bookkeeping would leave #2 the one issue on
        the tracker still carrying a spent `size: now`."""
        tracker = RefusingTracker(THREE, CLAIMS, refuse_close={2})
        mod = wire(monkeypatch, tracker)

        mod.main()

        assert all(LABEL not in tracker.issues[n] for n in (1, 2, 3)), tracker.issues

    def test_refuses_a_close_both_routes_refuse_and_names_it_at_the_end(
        self,
        monkeypatch,
    ):
        """S2. #2 stays open — nothing this script can do closes it — and the run
        says so with both errors, AFTER attempting #3. The exit is non-zero so
        the job is red, and it is red at the end rather than at #2."""
        tracker = RefusingTracker(THREE, CLAIMS, refuse_close={2}, refuse_rest={2})
        mod = wire(monkeypatch, tracker)

        with pytest.raises(SystemExit) as raised:
            mod.main()

        assert tracker.states == {1: "closed", 2: "open", 3: "closed"}, (
            f"#3 is sorted after the refused #2 and had to be closed anyway: "
            f"{tracker.states}"
        )
        assert tracker.closes() == [
            (1, "gh issue close"),
            (2, "gh issue close"),
            (2, "gh api PATCH"),
            (3, "gh issue close"),
        ], tracker.calls
        message = str(raised.value.code)
        assert raised.value.code, "the run exited 0 with an issue it could not close"
        assert (
            "#2" in message and GRAPHQL_REFUSAL in message and REST_REFUSAL in message
        ), f"the exit names neither the issue nor both refusals: {message!r}"
        # `\b`, because `#100` — the pull request every line names — holds `#1`.
        assert not re.search(r"#[13]\b", message), (
            f"the exit names an issue that closed: {message!r}"
        )

    def test_the_spent_label_comes_off_what_closed_and_stays_on_what_did_not(
        self,
        monkeypatch,
    ):
        """The label is bookkeeping about a close that happened. Taking it off
        an issue still open would say the release finished with it."""
        tracker = RefusingTracker(THREE, CLAIMS, refuse_close={2}, refuse_rest={2})
        mod = wire(monkeypatch, tracker)

        with pytest.raises(SystemExit):
            mod.main()

        assert LABEL not in tracker.issues[1] and LABEL not in tracker.issues[3]
        assert LABEL in tracker.issues[2], "the label came off an issue still open"

    def test_the_exit_message_says_how_a_partial_close_is_repaired(self, monkeypatch):
        """A red job nobody can act on is a red job somebody re-learns. The
        message names the re-run — the same script, the same three inputs —
        because a re-run skips what is already closed and reaches the rest."""
        tracker = RefusingTracker(THREE, CLAIMS, refuse_close={2}, refuse_rest={2})
        mod = wire(monkeypatch, tracker)

        with pytest.raises(SystemExit) as raised:
            mod.main()

        message = str(raised.value.code)
        for name in ("BEFORE", "AFTER", "REPO"):
            assert name in message, f"the exit does not name {name}: {message!r}"

    def test_accepts_the_issue_the_keyword_named_and_closes_nothing_else(
        self, monkeypatch
    ):
        """Swapping the key and value in `wanted` would close the pull requests
        instead of the issues, and no string check can see that."""
        m = _closer()
        closed = []
        monkeypatch.setattr(m, "arrived", lambda b, a: ["feat: a thing (#100)"])
        monkeypatch.setattr(
            m, "pull_request_body", lambda r, n: "Closes #88\ncloses #92"
        )
        monkeypatch.setattr(
            m, "issue_state", lambda r, n: "closed" if n == 92 else "open"
        )
        _offline(monkeypatch, m, closed)
        monkeypatch.setenv("AFTER", "x")
        monkeypatch.setenv("REPO", "example/repo")
        monkeypatch.delenv("DRY_RUN", raising=False)
        m.main()
        assert [a[3] for a in closed] == ["88"], (
            f"it closed {[a[3] for a in closed]}. #88 is the open issue the keyword "
            "named; #92 was already closed"
        )

    def test_a_number_that_names_nothing_does_not_kill_the_run(self, monkeypatch):
        """Round 2: the fix for `(#61)` reached one call site and not the other.

        A typo in a merged body — `Closes #9999` — sent a 404 through the shared
        `run`, which exits. Issues after it in sorted order stayed open, and a
        re-run died in the same place."""
        m = _closer()
        closed = []
        monkeypatch.setattr(m, "arrived", lambda b, a: ["feat: a thing (#100)"])
        monkeypatch.setattr(
            m, "pull_request_body", lambda r, n: "Closes #9999\ncloses #88"
        )
        monkeypatch.setattr(
            m, "issue_state", lambda r, n: None if n == 9999 else "open"
        )
        _offline(monkeypatch, m, closed)
        monkeypatch.setenv("AFTER", "x")
        monkeypatch.setenv("REPO", "example/repo")
        monkeypatch.delenv("DRY_RUN", raising=False)
        m.main()
        assert [a[3] for a in closed] == ["88"], (
            f"it closed {[a[3] for a in closed]}. A number naming nothing must be "
            "stepped over, not fatal, and the issues after it must still close"
        )

    def test_dry_run_writes_nothing(self, monkeypatch):
        m = _closer()
        closed = []
        monkeypatch.setattr(m, "arrived", lambda b, a: ["feat: a thing (#100)"])
        monkeypatch.setattr(m, "pull_request_body", lambda r, n: "Closes #88")
        monkeypatch.setattr(m, "issue_state", lambda r, n: "open")
        _offline(monkeypatch, m, closed)
        monkeypatch.setenv("AFTER", "x")
        monkeypatch.setenv("REPO", "example/repo")
        monkeypatch.setenv("DRY_RUN", "1")
        m.main()
        assert closed == [], (
            "DRY_RUN wrote. It exists because this script was run by hand for its "
            "output during development and closed a real issue"
        )

    def test_refuses_a_subject_number_naming_an_issue_and_closes_what_the_pull_request_claims(
        self, monkeypatch, capsys
    ):
        """`fix: … (#61)` names an issue a person typed, and the real
        `pull_request_body` says it is no pull request. The run steps over it
        and still closes what #100 claimed."""
        tracker = Tracker(issues={61: [], 88: []}, pulls={100: "Closes #88"})
        mod = wire_closer(
            monkeypatch, tracker, ["fix: a thing (#61)", "feat: b (#100)"]
        )
        mod.main()
        assert tracker.states == {61: "open", 88: "closed"}, tracker.states
        assert "#61 is not a pull request" in capsys.readouterr().out

    def test_accepts_the_first_pull_request_to_claim_an_issue_as_its_closer(
        self, monkeypatch
    ):
        """Two pull requests in one push claim #7. The closing comment names
        the one `arrived` lists first, and one close is made."""
        tracker = Tracker(issues={7: []}, pulls={100: "Closes #7", 101: "Closes #7"})
        mod = wire_closer(monkeypatch, tracker, ["feat: a (#100)", "feat: b (#101)"])
        mod.main()
        closes = [a for a in tracker.calls if a[:3] == ("gh", "issue", "close")]
        assert len(closes) == 1, tracker.calls
        comment = closes[0][closes[0].index("--comment") + 1]
        assert "Closed by #100" in comment, comment


class Test_module:
    def test_every_report_of_the_removal_goes_through_one_place(self):
        """Contract rule 12: the defect was one copy of three being unguarded, so what is owed
        is that a fourth copy cannot be written. Both branches of the loop call
        `spend_label`, and the two lines a reader sees are inside it."""
        source = read(os.path.join(SCRIPTS, "close_issues_on_release.py"))
        body = source.split('"""', 2)[2]
        assert body.count("would remove") == 1, (
            "the dry-run line is written in more than one place again"
        )
        assert body.count("removed {SPENT_ON_CLOSE!r}") == 1, (
            "the success line is written in more than one place again"
        )
        # Call sites, not occurrences: `def drop_label(repo, …)` is the third
        # match of a bare substring count and is not a caller. Measured — the
        # first spelling of this assertion counted the definition and went red
        # against the repaired file.
        calls = [
            line
            for line in body.splitlines()
            if "drop_label(" in line and not line.lstrip().startswith("def ")
        ]
        assert len(calls) == 1, (
            "a call site reaches `drop_label` without going through "
            f"`spend_label`, which is where the report is guarded on the "
            f"write: {calls}"
        )

    def test_attempt_answers_the_exit_code_and_the_error_rather_than_exiting(
        self,
        monkeypatch,
    ):
        """Every case above fakes `attempt`, so a mutation making it report every
        write as refused left all of them green. This one drives the real
        function against a fake `subprocess.run`, both ways round."""
        mod = closer_module()
        outcomes = iter([(0, ""), (1, "HTTP 502: Bad Gateway\n")])

        class Result:
            def __init__(self, returncode, stderr):
                self.returncode, self.stderr = returncode, stderr

        monkeypatch.setattr(
            mod.subprocess, "run", lambda *a, **k: Result(*next(outcomes))
        )
        assert mod.attempt("gh", "issue", "close", "1") == (True, "")
        assert mod.attempt("gh", "issue", "close", "2") == (
            False,
            "HTTP 502: Bad Gateway",
        )

    def test_the_fallback_comments_through_the_api_and_not_through_issue_comment(self):
        """`gh issue comment` is on the forbidden list of the argv case below,
        because a script that can comment on an issue can comment on an
        unrelated one. The fallback's comment is the REST
        `…/issues/<n>/comments` endpoint, reached through `gh api` — the same
        two writes, one route over."""
        with open(
            os.path.join(SCRIPTS, "close_issues_on_release.py"), encoding="utf-8"
        ) as f:
            source = f.read()
        body = source.split('"""', 2)[2]
        assert "/comments" in body, "the fallback posts no comment at all"
        assert '"comment"' not in body.replace('"--comment"', ""), (
            "the fallback reaches `gh issue comment`, which the argv case forbids"
        )

    def test_the_script_closes_and_takes_off_one_named_label_and_nothing_else(self):
        """Parse the source; never search it.

        The arguments go one per line, so `issue reopen` cannot occur as a literal
        and a forbidden-substring list over the raw text forbids nothing. Folding
        the source first was the answer to that for a long time, and it is not
        enough: a fold normalises whitespace and nothing else, so a comment
        between two words of the argv defeats it just as the line breaks did. Two
        review rounds of #450 each found that from a different side. The reader is
        `ast` now and the fold is gone.

        **What the parse closes, and what it does not.** It closes layout — the
        argv wrapped one word per line, a comment between two of its words, any
        whitespace at all — because the tree does not carry layout. It does NOT
        close a value that is not a string literal. `words` keeps only
        `ast.Constant` strings and `issue_argvs` compares the first three of them
        against `["gh", "issue", verb]`, so a name anywhere in those three
        positions is dropped, the prefix shifts by one, and the verb is never
        matched. Measured in round 3 of #450 and again in its fix pass, four
        spellings of a planted `gh issue reopen`: plain and comment-separated both
        red this case; `GH = "gh"` used as the first word, and the verb moved into
        a module constant, both leave it green.

        So this reader is strictly stronger than the fold and blind in a place the
        fold was blind too. Closing that means resolving module-level names before
        comparing, which is a different checker with its own argument to make;
        `seal/follow-up.md` carries it with the repository owner named.

        **This used to say `only ever closes`, and #450 changed what is true.**
        The script now also removes `size: now` from the issue it is closing —
        the moment `docs/issues-and-milestones.md` had already named as where a
        spent sizing label comes off, with nothing acting on it. So `issue edit`
        is no longer forbidden outright; what is forbidden is `issue edit` in any
        form but `--remove-label`, because the property being protected was never
        the verb. It is that a re-run and a force-push are safe to reason about,
        and both acts are idempotent: the close skips an issue already closed,
        and the removal is guarded by a read saying the label is there.

        Adding a label here would not be. That is the sibling's act
        (`label_merged_on_release_branch.py`, at the squash rather than at the
        close), and a second writer of labels is how two scripts come to disagree
        about which is the current answer.
        """
        # **Every claim in this case is parsed, and none is searched.**
        #
        # Round 1's finding 6 was that two flag assertions were not bound to the
        # call they judged, and bound them through `ast`. Round 2's finding 1 was
        # that the binding was then made conditional on the reader it replaced:
        # the block ran under `if edits:`, where `edits` was a folded-substring
        # count with `assert edits <= 1` above it — and that passes at ZERO. So
        # any re-spelling the substring missed took the count to zero, skipped the
        # parse, and left the case asserting nothing at all about what the script
        # edits. Measured by the round: the argv rewritten across lines with one
        # comment between its words and `"--add-assignee", "someone"` added exits
        # 0, while the script assigns a person on every label removal.
        #
        # **The same blindness was under the five forbidden verbs**, which is the
        # class rather than the coordinate (contract rule 12): they were
        # substring searches too, so a re-spelled `gh issue reopen` walked past
        # them for exactly the reason the `edit` one did. The folded reader is
        # gone from this case entirely; there is one reader and it does not care
        # how the argv is laid out.
        tree = ast.parse(read_text(".github", "scripts", "close_issues_on_release.py"))
        # BOTH argv shapes this file uses: `run("gh", …)` spreads the words as
        # call arguments, and `subprocess.run(["gh", …], …)` passes a list. The
        # one `issue edit` is written the second way, and a reader that knew only
        # the first parsed zero calls and asserted nothing — measured, on the
        # first spelling of round 1's fix.
        argvs = [node.elts for node in ast.walk(tree) if isinstance(node, ast.List)]
        argvs += [node.args for node in ast.walk(tree) if isinstance(node, ast.Call)]

        def words(argv):
            return [
                a.value
                for a in argv
                if isinstance(a, ast.Constant) and isinstance(a.value, str)
            ]

        def issue_argvs(verb):
            """Every `gh issue <verb>` argv in the script, however it is laid out."""
            return [argv for argv in argvs if words(argv)[:3] == ["gh", "issue", verb]]

        # **What this gave up, recorded rather than restored.** The folded form
        # asserted `'"gh", "issue", "close", str(issue),' in folded` — the verb
        # AND that the fourth word of that argv is the issue number. This checks
        # the count, which the folded form did not check at all, and reads no
        # operand: a close rewritten to act on something other than `issue`
        # passes. The trade is taken deliberately and is the same one the `edit`
        # argv below already makes, where the flags are read and the operand is
        # not — an operand is a variable name, and a name is exactly what this
        # reader cannot resolve (see the docstring). Pinning it would mean
        # asserting on an `ast.Name`'s spelling, which breaks on a rename that
        # changes nothing. Round 3 of #450 named the silence; this comment is it.
        closes = issue_argvs("close")
        assert len(closes) == 1, (
            f"{len(closes)} `gh issue close` argv lists; the script exists to "
            "close, exactly once, in one place"
        )
        for forbidden in ("reopen", "delete", "create", "comment", "transfer"):
            assert not issue_argvs(forbidden), (
                f"the script gained `issue {forbidden}`. Closing and taking off "
                "one named label is what makes a re-run and a force-push safe to "
                "reason about"
            )
        edit_calls = issue_argvs("edit")
        # EXACTLY one, never `<= 1`: the label removal is behaviour this case
        # pins, so a script that stopped editing is a script that stopped
        # spending the label, and the old `<= 1` was what let the whole block be
        # skipped at zero.
        assert len(edit_calls) == 1, (
            f"{len(edit_calls)} `gh issue edit` argv lists; there is one, and it "
            "is the removal of a spent sizing label"
        )
        flags = {word for word in words(edit_calls[0]) if word.startswith("--")}
        assert flags == {"--repo", "--remove-label"}, (
            f"the one `gh issue edit` carries {sorted(flags)}. It may carry "
            "`--remove-label` and nothing else that writes: adding a label is "
            "the sibling's act at the squash, and any other write is not the "
            "removal this case says the one edit is"
        )


test_census = census_case(TARGET)
