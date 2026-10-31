"""`.github/scripts/release_completeness_check.py`, one class per function.

Issue #359, the gate half: a release pull request is refused while its
milestone claims an open issue the release branch does not carry. Three
sets, and `Test_judge`'s cases are about which of the four directions
between them stops a release and which only gets reported:

    M   open issues whose milestone is `release: X.Y.Z`
    D   what the release branch carries, read out of its own commit subjects
    L   what carries the label `merged: X.Y.Z`

`judge()` is pure, so the four directions are cases rather than runs. What
needs the fake tracker is the wiring above it, `Test_main`'s: which command
each set is read with, and the range D is read over.

Issue #1199 adds the second question the step asks: a release named as a
patch whose own commit subjects carry a `feat:` is refused, because a
`feat:` makes a minor. `judge_feat()` is pure too, and `Test_judge_feat`
holds its lines; `Test_main` holds that both readings run on one read of
the subjects and that either one fails the step.

#942's phase 6 placed these cases from
`tests/text/test_a_release_cannot_ship_an_untrue_milestone.py`, which keeps the
cases that read the hygiene workflow's step and the two docstrings that
draw the input boundary.
"""

import importlib.util
import json
import os
import re

import pytest
from conftest import ROOT, census_case, read

TARGET = ".github/scripts/release_completeness_check.py"

SCRIPT = os.path.join(ROOT, ".github", "scripts", "release_completeness_check.py")

VERSION = "1.2.3"
MINOR = "1.3.0"
BRANCH = "release/v1.2.3"
MILESTONE = "release: 1.2.3"
LABEL = "merged: 1.2.3"
REPO = "example/repo"


def gate():
    spec = importlib.util.spec_from_file_location(
        "agentic_release_completeness_for_tests", SCRIPT
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verdict(milestone_open, carried, labels):
    lines, failed = gate().judge(
        set(milestone_open), set(carried), set(labels), VERSION
    )
    return "\n".join(lines), failed


def feat_verdict(version, subjects):
    lines, failed = gate().judge_feat(version, list(subjects))
    return lines, failed


class Tracker:
    """Every `closer.run` the gate makes, and a canned answer for each."""

    def __init__(self, milestones=(MILESTONE,), m=(), label=(), subjects=()):
        self.milestones = list(milestones)
        self.m = list(m)
        self.label = list(label)
        self.subjects = list(subjects)
        self.calls = []

    def run(self, *args):
        self.calls.append(args)
        if args[:2] == ("git", "merge-base"):
            return "f" * 40 + "\n"
        if args[:2] == ("git", "log"):
            return "\n".join(self.subjects) + "\n"
        if args[:2] == ("gh", "api"):
            return json.dumps([{"title": t} for t in self.milestones])
        if args[:3] == ("gh", "issue", "list"):
            which = self.label if "--label" in args else self.m
            return json.dumps([{"number": n} for n in which])
        raise AssertionError(f"unexpected command: {args}")

    def call_with(self, *needles):
        for args in self.calls:
            if all(n in args for n in needles):
                return args
        raise AssertionError(f"no call carrying {needles}: {self.calls}")


def wire(monkeypatch, m, tracker, pulls):
    monkeypatch.setattr(m.closer, "run", tracker.run)
    monkeypatch.setattr(
        m.closer,
        "_issue_api",
        lambda repo, n: (
            ({"pull_request": {}, "body": pulls[n]}, True)
            if n in pulls
            else (None, False)
        ),
    )
    monkeypatch.setenv("HEAD_BRANCH", BRANCH)
    monkeypatch.setenv("REPO", REPO)
    monkeypatch.delenv("BASE", raising=False)
    monkeypatch.delenv("HEAD_SHA", raising=False)


class Test_judge:
    def test_refuses_an_open_issue_the_release_does_not_carry(self):
        """S4. The whole reason the gate exists, and the direction that fails.

        The release this gate ships in met exactly this on the day it was
        written: its milestone held nine open issues and the branch carried two.
        """
        out, failed = verdict(milestone_open={88, 92, 99}, carried={88}, labels={88})
        assert failed, "a milestone claiming two absent issues let the release through"
        assert "M \\ D" in out, "the refusal does not name the direction it is about"
        assert "#92" in out and "#99" in out, f"the refusal names no issue: {out}"
        assert "::error::" in out, "the refusal is not annotated as an error"

    def test_a_pull_request_body_with_no_closing_keyword_refuses_the_release(self):
        """S8. `docs/issues-and-milestones.md` says a missing `Closes #N` "costs
        an issue that stays open forever"; this is the first thing that reports
        it, and it reports it as the milestone claiming an item that is not in.

        The issue is in M because a person scheduled it, and out of D because the
        body never said so — which is the same shape as work that has not been
        built, and correctly so: nothing in the tree can tell them apart.
        """
        out, failed = verdict(milestone_open={88}, carried=set(), labels=set())
        assert failed
        assert "#88" in out and "M \\ D" in out

    def test_the_refusal_says_what_to_do_about_it(self):
        """A refusal is read by whoever is stopped by it, and the half that says
        what to do is the half that has to survive a reword."""
        out, _ = verdict(milestone_open={88, 92}, carried={88}, labels={88})
        assert "another milestone" in out, (
            "the refusal does not offer moving the issue, so a reader meeting it "
            "mid-release has only 'build it now' on the table"
        )

    def test_accepts_a_milestone_the_release_satisfies_and_prints_both_sets(self):
        """S5. Printing them is not decoration: the reader who has just been told
        nothing is wrong is the reader who has to be able to check that."""
        out, failed = verdict(
            milestone_open={88, 92}, carried={88, 92}, labels={88, 92}
        )
        assert not failed
        assert "::error::" not in out
        assert re.search(r"^M \(open in .*\): #88, #92$", out, re.M), out
        assert re.search(r"^D \(carried by this release branch\): #88, #92$", out, re.M)
        assert re.search(r"^L \(carrying .*\): #88, #92$", out, re.M)

    def test_nothing_anywhere_is_not_a_failure(self):
        """A release branch with no claimed issue at all — the first push of a
        freshly cut branch. Empty sets agree with each other."""
        out, failed = verdict(milestone_open=set(), carried=set(), labels=set())
        assert not failed
        assert "none" in out

    def test_a_label_naming_a_release_the_issue_is_not_in_fails(self):
        """S6, the failing direction, and `questions.md` Q1's answer (c).

        `L \\ D` is always a hand-edit or a squash subject that lost its `(#N)`,
        and one command repairs it — which is why this half fails where the other
        reports.
        """
        out, failed = verdict(milestone_open={88}, carried={88}, labels={88, 77})
        assert failed, "a label on an issue this release does not carry passed"
        assert "L \\ D" in out, "the finding does not name which direction it is"
        assert "#77" in out
        assert "--remove-label" in out, (
            "the finding does not name the one command that repairs it"
        )
        assert "#88" not in out.split("L \\ D")[1].split("\n")[0], (
            "the correctly-labelled issue is named in the refusal"
        )

    def test_the_signal_having_missed_one_reports_and_passes(self):
        """S6, the passing direction. A release held for the signal's outage is a
        release paying for something that does not change what ships — and the
        remedy would be a person adding a label by hand, which is the act this
        work item exists to remove."""
        out, failed = verdict(milestone_open={88, 92}, carried={88, 92}, labels={88})
        assert not failed, "the release was held because a label write had not landed"
        assert "D \\ L" in out and "#92" in out
        assert "::error::" not in out

    def test_an_issue_closed_by_hand_mid_release_reports_and_passes(self):
        """`D \\ M`. It is in D because the release carries it and in no OPEN
        milestone because somebody closed it, and a gate that went red for that
        would go red for ordinary tracker hygiene."""
        out, failed = verdict(milestone_open=set(), carried={88}, labels={88})
        assert not failed
        assert "D \\ M" in out and "#88" in out

    def test_both_failing_directions_are_reported_together(self):
        """A run that stopped at the first refusal would send a release
        preparation round the loop twice."""
        out, failed = verdict(milestone_open={88, 99}, carried={88}, labels={88, 77})
        assert failed
        assert "M \\ D" in out and "#99" in out
        assert "L \\ D" in out and "#77" in out


class Test_judge_feat:
    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_refuses_a_feat_in_a_patch_and_names_each_subject_and_each_repair(self):
        """S1. A `feat:` makes a minor, and a release named as a patch that
        carries one ships a minor's content under a patch's number, which 14
        of the 37 patch releases from v0.8.1 to v0.25.1 did. The refusal is
        read by whoever is stopped by it, so it names each repair at the
        moment it can be made: before its squash, a `feat:` moves to the
        planned minor whose goal it shares; once squashed here, it stays in
        the range after a revert, and the repair is the rename."""
        lines, failed = feat_verdict(
            VERSION,
            ["fix: a repair (#9)", "feat: a thing (#10)", "feat: another (#11)"],
        )
        assert failed, "a patch carrying a feat: let the release through"
        errors = [line for line in lines if line.startswith("::error::")]
        assert len(errors) == 1, lines
        error = errors[0]
        assert "`feat: a thing (#10)`" in error and "`feat: another (#11)`" in error
        assert "fix: a repair" not in error, "a fix: subject is named as a feat:"
        assert f"{VERSION} is a patch" in error, error
        assert "A feat: makes a minor." in error, error
        assert "before its squash" in error, error
        assert "to the planned minor whose goal it shares" in error, error
        assert "stays in its range" in error and "after a revert" in error, error
        assert f"rename {MILESTONE!r} and every later planned" in error, error
        assert "cut this branch again under the new name" in error, error
        assert "plugin.json" in error, error
        assert "docs/branch-and-release.md" in error, error
        assert "never lowered to fit the number" in error, error
        assert lines[0] == error, "the refusal is not the first line a reader meets"

    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_accepts_a_feat_in_a_minor_and_counts_it(self):
        """S2. A minor is where a `feat:` belongs."""
        lines, failed = feat_verdict(MINOR, ["feat: a thing (#10)", "fix: x (#9)"])
        assert not failed
        assert lines == [
            f"1 feat: subject(s) on this release branch, and {MINOR} is a minor"
        ], lines

    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_a_patch_with_no_feat_passes_and_counts(self):
        """S3. Every prefix but `feat:` fits a patch."""
        lines, failed = feat_verdict(
            VERSION, ["fix: a (#1)", "refactor: b (#2)", "chore: c (#3)"]
        )
        assert not failed
        assert lines == [
            f"0 feat: subject(s) on this release branch, and {VERSION} is a patch"
        ], lines

    @pytest.mark.rule("a-patch-carries-no-feat")
    @pytest.mark.parametrize(
        "near",
        [
            "Feat: a thing (#12)",
            "feat(agents): a thing (#12)",
            "feat!: a thing (#12)",
            "FEAT a thing (#12)",
        ],
    )
    def test_a_spelling_the_reading_does_not_count_is_named_as_not_read(self, near):
        """S4. The reading counts the one spelling `feat:` and keeps no list of
        the others. A subject whose first word is `feat` in another spelling is
        named, so the person reading the log judges what it meant, and it
        changes no exit code."""
        lines, failed = feat_verdict(VERSION, [near, "featured: a word (#13)"])
        assert not failed, f"{near!r} was counted as a feat:"
        assert f"not read: {near}" in lines, lines
        assert lines[0] == (
            f"0 feat: subject(s) on this release branch, and {VERSION} is a patch"
        ), lines
        assert not any("featured" in line for line in lines), (
            f"a word that only begins with feat is named: {lines}"
        )

    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_a_minor_with_no_feat_ships_as_the_minor_it_was_named(self):
        """S7. Once a branch is cut, its name is never pulled back, so a minor
        that ends up with no `feat:` passes and says it ships as the minor it
        was named, because its branch is cut under that name. Before the cut a
        planned name follows its goal, which no reading here can see, so the
        line states the bound and not an unbounded never."""
        lines, failed = feat_verdict(MINOR, ["fix: x (#9)"])
        assert not failed
        assert lines == [
            f"0 feat: subject(s) on this release branch, and {MINOR} is a minor",
            f"{MINOR} carries no feat: and ships as the minor it was named, "
            "since its branch is cut under that name",
        ], lines


class Test_main:
    @pytest.mark.parametrize(
        "head",
        ["hotfix/v1.2.4", "fix/88-a-thing", "main", "release/next", "release/v1.2", ""],
    )
    def test_refuses_a_head_that_is_not_a_release_branch_with_a_reason(
        self, monkeypatch, capsys, head
    ):
        """S7. `docs/branch-and-release.md` lists a hotfix branch as the other
        thing that reaches `main`, and a hotfix carries no release milestone.
        Guessing a version out of the name is the one thing that must not
        happen."""
        m = gate()
        monkeypatch.setattr(
            m.closer, "run", lambda *a: pytest.fail(f"the gate ran {a}")
        )
        monkeypatch.setenv("HEAD_BRANCH", head)
        monkeypatch.setenv("REPO", REPO)
        assert m.main() == 0
        assert "nothing to judge" in capsys.readouterr().out

    def test_a_milestone_that_does_not_exist_says_it_verified_nothing(
        self, monkeypatch, capsys
    ):
        """Measured on the real tracker: `gh issue list --milestone` answers a
        title nothing has with `[]` and exit 0. So without a separate existence
        read, a mistyped or absent milestone makes this whole check pass while
        measuring an empty set — a check that cannot fail.

        It still passes, because a release nobody scheduled is a person's call
        rather than this gate's, and the `D \\ M` direction was rejected for the
        same reason. What it must not be is silent.
        """
        m = gate()
        tracker = Tracker(milestones=["release: 9.9.9"], subjects=["fix: x (#100)"])
        wire(monkeypatch, m, tracker, {})
        monkeypatch.setattr(
            m, "open_in_milestone", lambda *a: pytest.fail("the empty set was measured")
        )
        assert m.main() == 0
        out = capsys.readouterr().out
        assert "the milestone reading verified NOTHING" in out, out
        assert "That reading passes anyway" in out, out
        assert MILESTONE in out

    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_a_feat_in_a_patch_refuses_where_the_milestone_does_not_exist(
        self, monkeypatch, capsys
    ):
        """S5. The milestone reading passes a release nobody scheduled, and
        the version reading does not need a milestone: the number is in the
        head branch's name and the subjects are in its range."""
        m = gate()
        tracker = Tracker(
            milestones=["release: 9.9.9"], subjects=["feat: a thing (#100)"]
        )
        wire(monkeypatch, m, tracker, {})
        monkeypatch.setattr(
            m, "open_in_milestone", lambda *a: pytest.fail("the empty set was measured")
        )
        assert m.main() == 1
        out = capsys.readouterr().out
        assert "the milestone reading verified NOTHING" in out, out
        assert "Passing anyway" not in out, (
            "the warning tells a reader a run that exits 1 passed"
        )
        assert "::error::" in out and "`feat: a thing (#100)`" in out, out

    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_both_readings_run_on_one_read_of_the_subjects(self, monkeypatch, capsys):
        """The milestone the release satisfies does not let a feat: in a patch
        through, and the range is read once for both readings."""
        m = gate()
        tracker = Tracker(m=[88], label=[88], subjects=["feat: a thing (#100)"])
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        assert m.main() == 1
        out = capsys.readouterr().out
        assert "::error::" in out and "`feat: a thing (#100)`" in out, out
        assert "D (carried by this release branch): #88" in out, (
            "the milestone reading did not run beside the version reading"
        )
        logs = [args for args in tracker.calls if args[:2] == ("git", "log")]
        assert len(logs) == 1, f"the subjects were read {len(logs)} times"

    def test_a_milestone_refusal_fails_the_step_with_no_feat(self, monkeypatch):
        """The exit code is either reading's failure, so the milestone's own
        refusal still stops a patch that carries no feat:."""
        m = gate()
        tracker = Tracker(m=[88, 92], label=[88], subjects=["fix: a thing (#100)"])
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        assert m.main() == 1

    def test_accepts_a_release_branch_and_measures_from_where_it_left_main(
        self, monkeypatch
    ):
        """`questions.md` Q8. `origin/main..HEAD` is the obvious spelling and it
        is wrong the moment a hotfix moves `main` during a release's life; what
        the release carries is what it accumulated since it was cut."""
        m = gate()
        tracker = Tracker(m=[88], label=[88], subjects=["fix: a thing (#100)"])
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        assert m.main() == 0
        assert tracker.call_with("merge-base") == (
            "git",
            "merge-base",
            "origin/main",
            "HEAD",
        )
        log = tracker.call_with("git", "log")
        assert log[-1] == "f" * 40 + "..HEAD", (
            f"D was read over {log[-1]!r}, not over the fork point"
        )

    def test_the_range_is_measured_to_the_head_the_pull_request_names(
        self, monkeypatch
    ):
        """Round 1, finding 2. The script did what its docstring said and the
        checkout undid it.

        `actions/checkout` takes the MERGE ref on a `pull_request` event, so
        `HEAD` in the job already contains the base and the fork point collapses
        to the base tip — the `base..HEAD` spelling `questions.md` Q8 rejected,
        arriving through the workflow rather than through the code. Every case in
        this module passed while that was true, because none of them could see
        the shape of the commit the two commands were handed.

        So the head is an input now, and this is the case that has it.
        """
        m = gate()
        tracker = Tracker(m=[88], label=[88], subjects=["fix: a thing (#100)"])
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        monkeypatch.setenv("HEAD_SHA", "c" * 40)
        assert m.main() == 0
        assert tracker.call_with("merge-base") == (
            "git",
            "merge-base",
            "origin/main",
            "c" * 40,
        ), "the fork point is still measured against the merge ref"
        log = tracker.call_with("git", "log")
        assert log[-1] == "f" * 40 + ".." + "c" * 40, (
            f"D was read over {log[-1]!r}, which does not end at the head the "
            "pull request names"
        )

    def test_without_a_named_head_the_range_ends_at_HEAD(self, monkeypatch):
        """The control for the case above, and the by-hand path.

        A session running this outside CI has no pull request and no head commit
        to name; its own `HEAD` is the branch tip, which is the thing CI's `HEAD`
        is not. Without this, setting `HEAD_SHA` to a constant would pass every
        assertion above.
        """
        m = gate()
        tracker = Tracker(m=[88], label=[88], subjects=["fix: a thing (#100)"])
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        assert m.main() == 0
        assert tracker.call_with("merge-base")[3] == "HEAD"
        assert tracker.call_with("git", "log")[-1].endswith("..HEAD")

    def test_the_milestone_list_is_read_past_the_first_page(self, monkeypatch):
        """Round 1, finding 1. `per_page` caps at 100, and the read took one page.

        A repository with more milestones than that leaves the title off the page,
        and the gate then prints `verified NOTHING` and passes — through the very
        function written to stop it passing on an empty set. The round's probe
        gutted the whole query and all 25 cases here stayed green, which is why
        this exists: the guard's PRESENCE was pinned and the query behind it was
        not.

        Executed while writing this: 33 milestones here, so the hole is reachable
        by growth rather than now.
        """
        m = gate()
        tracker = Tracker(m=[88], label=[88], subjects=["fix: a thing (#100)"])
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        assert m.main() == 0
        call = tracker.call_with("gh", "api")
        assert "--paginate" in call, f"the milestone list is read one page deep: {call}"
        assert any("per_page=100" in arg for arg in call), (
            f"the read asks for fewer than the maximum page size: {call}"
        )

    def test_the_base_the_range_starts_from_is_configurable(self, monkeypatch):
        """CI passes `origin/<base_ref>`, and a session checking a release by
        hand has a different remote name for it."""
        m = gate()
        tracker = Tracker(subjects=[])
        wire(monkeypatch, m, tracker, {})
        monkeypatch.setenv("BASE", "upstream/main")
        assert m.main() == 0
        assert tracker.call_with("merge-base")[2] == "upstream/main"

    def test_M_is_read_with_gh_issue_list_and_not_the_rest_endpoint(self, monkeypatch):
        """Measured: REST `/issues` counts a pull request as an issue and
        `gh issue list` does not. A pull request carrying the milestone could
        never carry `merged: X.Y.Z`, so it would sit in `M \\ D` and block the
        release forever with nothing anybody could do about it."""
        m = gate()
        tracker = Tracker(m=[88], label=[88], subjects=["fix: a thing (#100)"])
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        assert m.main() == 0
        call = tracker.call_with("--milestone")
        assert call[:3] == ("gh", "issue", "list"), call
        assert "--state" in call and call[call.index("--state") + 1] == "open"

    def test_L_is_read_in_every_state(self, monkeypatch):
        """An issue closed by hand mid-release still carries the label the signal
        put on it. Reading only the open ones would report it as `D \\ L` — the
        signal blamed for a person's edit."""
        m = gate()
        tracker = Tracker(m=[], label=[88], subjects=["fix: a thing (#100)"])
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        assert m.main() == 0
        call = tracker.call_with("--label")
        assert call[call.index("--label") + 1] == LABEL
        assert call[call.index("--state") + 1] == "all"

    def test_D_comes_from_the_same_readers_the_signal_writes_it_with(self, monkeypatch):
        """The gate recomputes D rather than trusting L, and it has to recompute
        it the same way — a second reader of a pull request body is how the label
        and the refusal come to disagree about a fenced example."""
        m = gate()
        tracker = Tracker(
            m=[88],
            label=[88],
            subjects=["fix: a thing (#100)", "docs: quoted (#101)"],
        )
        wire(monkeypatch, m, tracker, {100: "Closes #88", 101: "```\nCloses #92\n```"})
        assert m.main() == 0
        source = read(SCRIPT)
        assert "signal.issues_in(" in source, "the gate derives D some other way"
        for own in ("CLOSING = re.compile", "MERGED_PR = re.compile"):
            assert own not in source, f"the gate wrote its own {own.split()[0]}"


class Test_module:
    def test_the_gate_writes_nothing(self, monkeypatch):
        """Its whole job is to judge. A gate that can write is a gate whose red
        can be made green by the thing that went red."""
        folded = " ".join(read(SCRIPT).split())
        for forbidden in ("edit", "close", "create", "delete", "comment", "reopen"):
            assert f'"gh", "issue", "{forbidden}"' not in folded, f"issue {forbidden}"
            assert f'"gh", "label", "{forbidden}"' not in folded, f"label {forbidden}"


test_census = census_case(TARGET)
