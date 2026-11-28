"""`.github/scripts/release_completeness_check.py`, one class per function.

The check runs at the release pull request and asks two questions of the
same commit subjects, the ones from the merge base of the base and the head
to the head.

#1671: the number. A `feat:` among the subjects makes the release the next
minor of the version `plugin.json` holds at the base, and their absence the
next patch. A head that moves `plugin.json` to another version fails, and a
head that moves the major, to a version whose minor and patch are 0, is the
owner's word and is not read against the subjects. `judge_number()` is pure,
and `Test_judge_number` holds its lines.

#359, the labels. Two sets of issue numbers:

    D   what the release carries, read out of its own commit subjects
    L   what carries the label `merged: next`

`L \\ D` fails and `D \\ L` is reported. `judge()` is pure too, and
`Test_judge` holds its directions. What needs the fake tracker is the wiring
above both, `Test_main`'s: which command each version and each set is read
with, and the range the subjects are read over.

#942's phase 6 placed these cases from the step's test file, now
`tests/text/test_the_release_check_runs_from_its_step.py`, which keeps the
cases that read the hygiene workflow's step.
"""

import importlib.util
import json
import os
import re

import pytest
from conftest import ROOT, census_case, read
from test_close_issues_on_release import argv_words

TARGET = ".github/scripts/release_completeness_check.py"

SCRIPT = os.path.join(ROOT, ".github", "scripts", "release_completeness_check.py")

BASE_VERSION = "0.8.1"
MINOR = "0.9.0"
PATCH = "0.8.2"
LABEL = "merged: next"
REPO = "example/repo"
FEAT = "feat: a thing (#10)"


def gate():
    spec = importlib.util.spec_from_file_location(
        "agentic_release_completeness_for_tests", SCRIPT
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verdict(carried, labels):
    lines, failed = gate().judge(set(carried), set(labels))
    return "\n".join(lines), failed


def number_verdict(head, subjects, base=BASE_VERSION):
    lines, failed = gate().judge_number(base, head, list(subjects))
    return lines, failed


class Tracker:
    """Every `closer.run` the gate makes, and a canned answer for each.

    `versions` maps a ref to the version `plugin.json` holds there, as
    `git show <ref>:.claude-plugin/plugin.json` answers it."""

    def __init__(self, versions=None, label=(), subjects=()):
        self.versions = dict(versions or {"origin/main": BASE_VERSION, "HEAD": MINOR})
        self.label = list(label)
        self.subjects = list(subjects)
        self.calls = []

    def run(self, *args):
        self.calls.append(args)
        if args[:2] == ("git", "merge-base"):
            return "f" * 40 + "\n"
        if args[:2] == ("git", "show"):
            ref, path = args[2].split(":", 1)
            assert path == ".claude-plugin/plugin.json", args
            return json.dumps({"name": "agentic", "version": self.versions[ref]})
        if args[0] == "git" and "log" in args:
            return "\n".join(self.subjects) + "\n"
        if args[:3] == ("gh", "issue", "list"):
            return json.dumps([{"number": n} for n in self.label])
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
    monkeypatch.setenv("REPO", REPO)
    monkeypatch.delenv("BASE", raising=False)
    monkeypatch.delenv("HEAD_SHA", raising=False)


class Test_judge:
    def test_accepts_labels_the_release_carries_and_prints_both_sets(self):
        """Printing them is not decoration: the reader who has just been told
        nothing is wrong is the reader who has to be able to check that."""
        out, failed = verdict(carried={88, 92}, labels={88, 92})
        assert not failed
        assert "::error::" not in out
        assert re.search(r"^D \(carried by this release\): #88, #92$", out, re.M), out
        assert re.search(r"^L \(carrying 'merged: next'\): #88, #92$", out, re.M), out

    def test_nothing_anywhere_is_not_a_failure(self):
        """A release with no claimed issue at all. Empty sets agree with each
        other."""
        out, failed = verdict(carried=set(), labels=set())
        assert not failed
        assert "none" in out

    def test_refuses_a_label_on_an_issue_the_release_does_not_carry(self):
        """The failing direction, and `questions.md` Q1's answer (c) of #359.

        `L \\ D` is a hand-edit, a squash subject that lost its `(#N)`, or a
        label the last release's close did not take off, and one command
        repairs each, which is why this half fails where the other reports.
        """
        out, failed = verdict(carried={88}, labels={88, 77})
        assert failed, "a label on an issue this release does not carry passed"
        assert "L \\ D" in out, "the finding does not name which direction it is"
        assert "#77" in out
        assert f"--remove-label {LABEL!r}" in out, (
            "the finding does not name the one command that repairs it"
        )
        assert "the last release's close did not take off" in out, out
        assert "#88" not in out.split("L \\ D")[1].split("\n")[0], (
            "the correctly-labelled issue is named in the refusal"
        )

    def test_the_signal_having_missed_one_reports_and_passes(self):
        """The passing direction. A release held for the signal's outage is a
        release paying for something that does not change what ships, and the
        remedy would be a person adding a label by hand, which is the act the
        signal exists to remove."""
        out, failed = verdict(carried={88, 92}, labels={88})
        assert not failed, "the release was held because a label write had not landed"
        assert "D \\ L" in out and "#92" in out
        assert "::error::" not in out


class Test_number_read:
    @pytest.mark.rule("a-patch-carries-no-feat")
    @pytest.mark.parametrize(
        "version, subjects, number",
        [
            ("0.8.1", [FEAT, "fix: a repair (#9)"], "0.9.0"),
            ("0.8.1", ["fix: a repair (#9)", "docs: a page (#8)"], "0.8.2"),
            ("1.9.0", [FEAT], "1.10.0"),
            ("0.9.9", [], "0.9.10"),
        ],
    )
    def test_accepts_a_feat_as_the_next_minor_and_its_absence_as_the_next_patch(
        self, version, subjects, number
    ):
        """S1 and S3 of #1671. A minor takes the patch back to 0, and each
        number counts past 9."""
        assert gate().number_read(version, subjects) == number

    @pytest.mark.rule("a-patch-carries-no-feat")
    @pytest.mark.parametrize(
        "subject", ["Feat: a thing (#12)", "feat(agents): a thing (#12)", "a feat: x"]
    )
    def test_refuses_any_spelling_but_feat_as_a_minor(self, subject):
        """The reading counts the one spelling `feat:` at the start of a
        subject, so a near spelling, or the word further in, reads a patch."""
        assert gate().number_read(BASE_VERSION, [subject]) == PATCH


class Test_judge_number:
    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_accepts_a_head_moved_to_the_minor_a_feat_reads(self):
        """S1 of #1671. The number is read and printed, beside the two
        versions and each `feat:` subject it was read from."""
        lines, failed = number_verdict(MINOR, [FEAT, "fix: a repair (#9)"])
        assert not failed, lines
        assert not any(line.startswith("::error::") for line in lines), lines
        assert lines[0] == (
            f"number read: {MINOR}, the next minor of {BASE_VERSION}, from "
            "1 feat: subject(s)"
        ), lines
        assert f"plugin.json: {BASE_VERSION} at the base, {MINOR} at the head" in (
            lines
        ), lines
        assert f"feat: subject: {FEAT}" in lines, lines
        assert not any("fix: a repair" in line for line in lines), lines

    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_refuses_a_patch_where_a_feat_reads_a_minor_and_names_each_subject(self):
        """S2 of #1671. The refusal is read by whoever is stopped by it, so it
        names the number read, each `feat:` subject it was read from, and the
        one repair."""
        lines, failed = number_verdict(
            PATCH, ["fix: a repair (#9)", FEAT, "feat: another (#11)"]
        )
        assert failed, (
            "a patch moved where a feat: reads a minor let the release through"
        )
        errors = [line for line in lines if line.startswith("::error::")]
        assert len(errors) == 1, lines
        error = errors[0]
        assert lines[0] == error, "the refusal is not the first line a reader meets"
        assert f"moves plugin.json to {PATCH}" in error, error
        assert f"the subjects read {MINOR}" in error, error
        assert f"`{FEAT}`" in error and "`feat: another (#11)`" in error, error
        assert "fix: a repair" not in error, "a fix: subject is named as a feat:"
        # The repair the printed line names, and where it is made.
        assert f"move plugin.json to {MINOR}" in error, error
        assert "release/next" in error, error
        # The printed line's closing clause.
        assert "never lowered to fit the number" in error, error

    @pytest.mark.rule("a-patch-carries-no-feat")
    @pytest.mark.parametrize("head, number", [(MINOR, PATCH), (PATCH, None)])
    def test_a_release_with_no_feat_reads_the_next_patch(self, head, number):
        """S3 of #1671. Every prefix but `feat:` fits a patch, so a minor moved
        for a release that carries none fails naming the patch, and the patch
        passes."""
        lines, failed = number_verdict(
            head, ["fix: a repair (#9)", "docs: a page (#8)"]
        )
        if number is None:
            assert not failed, lines
            assert lines[0] == (
                f"number read: {PATCH}, the next patch of {BASE_VERSION}, from "
                "0 feat: subject(s)"
            ), lines
        else:
            assert failed, lines
            assert f"the subjects read {number}" in lines[0], lines

    @pytest.mark.rule("a-patch-carries-no-feat")
    @pytest.mark.parametrize("subjects", [[FEAT], ["fix: a repair (#9)"], []])
    def test_accepts_a_major_as_the_owners_word_and_says_it_is_not_read(self, subjects):
        """S4 of #1671. A major is the owner's word alone: it is not read
        against the subjects, whatever they hold, and the line says so."""
        lines, failed = number_verdict("1.0.0", subjects)
        assert not failed, lines
        assert (
            "1.0.0 moves the major, the owner's word, and is not read against "
            "the subjects"
        ) in lines, lines

    @pytest.mark.rule("a-patch-carries-no-feat")
    @pytest.mark.parametrize(
        "base, head, number",
        [
            (BASE_VERSION, "1.0.1", MINOR),
            (BASE_VERSION, "1.1.0", MINOR),
            (BASE_VERSION, "0.7.0", MINOR),
            ("1.2.3", "0.0.0", "1.3.0"),
        ],
    )
    def test_refuses_a_major_that_is_not_its_first_release(self, base, head, number):
        """A version that moves the major with a minor or a patch above 0, or
        one below the base, a lower major among them, is no major the owner
        named, so it is read as every other move is."""
        lines, failed = number_verdict(head, [FEAT], base=base)
        assert failed, lines
        assert f"the subjects read {number}" in lines[0], lines

    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_a_head_that_leaves_the_version_prints_the_number_and_refuses_nothing(
        self,
    ):
        """S5 of #1671. Whether a release that leaves `plugin.json` where the
        base has it may ship is the version step's question, and this check
        prints the number that step's repair moves to."""
        lines, failed = number_verdict(BASE_VERSION, [FEAT])
        assert not failed, lines
        assert lines[0].startswith(f"number read: {MINOR}"), lines
        assert (
            f"plugin.json is not moved from {BASE_VERSION}, and the version "
            "step judges a release that leaves it"
        ) in lines, lines

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
        """The reading counts the one spelling `feat:` and keeps no list of
        the others. A subject whose first word is `feat` in another spelling is
        named, so the person reading the log judges what it meant, and it
        changes neither the number nor the exit code."""
        lines, failed = number_verdict(PATCH, [near, "featured: a word (#13)"])
        assert not failed, f"{near!r} was counted as a feat:"
        assert f"not read: {near}" in lines, lines
        assert lines[0].startswith(f"number read: {PATCH}"), lines
        assert not any("featured" in line for line in lines), (
            f"a word that only begins with feat is named: {lines}"
        )


class Test_version_at:
    def test_accepts_the_version_plugin_json_holds_at_the_ref(self, monkeypatch):
        m = gate()
        tracker = Tracker(versions={"upstream/main": "2.3.4"})
        monkeypatch.setattr(m.closer, "run", tracker.run)
        assert m.version_at("upstream/main") == "2.3.4"
        assert tracker.calls == [
            ("git", "show", "upstream/main:.claude-plugin/plugin.json")
        ], tracker.calls

    def test_refuses_a_ref_git_cannot_show_by_ending_the_run(self, monkeypatch):
        """A version that cannot be read is no number to judge against, so
        the runner's exit stands: the check fails loudly rather than reading
        a version it did not see."""
        m = gate()

        def refused(*args):
            raise SystemExit(f"`{' '.join(args)}` failed: no such path")

        monkeypatch.setattr(m.closer, "run", refused)
        with pytest.raises(SystemExit, match=r"plugin\.json"):
            m.version_at("upstream/main")


class Test_main:
    def test_accepts_a_run_that_reads_no_milestone_and_no_head_name(
        self, monkeypatch, capsys
    ):
        """S6 of #1671. No milestone names a release before its cut, and the
        number is read from `plugin.json`, so the check asks the tracker for
        no milestone and judges a run that names no head branch by the one
        reading. Every call is recorded, and the fake tracker answers no
        `gh api` call."""
        m = gate()
        tracker = Tracker(label=[88], subjects=["fix: a thing (#100)"])
        tracker.versions["HEAD"] = PATCH
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        assert m.main() == 0
        out = capsys.readouterr().out
        assert "nothing to judge" not in out, out
        assert f"number read: {PATCH}" in out, out
        assert not [a for a in tracker.calls if "--milestone" in a], tracker.calls
        assert not [a for a in tracker.calls if a[:2] == ("gh", "api")], tracker.calls

    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_refuses_a_patch_moved_where_a_feat_reads_a_minor(
        self, monkeypatch, capsys
    ):
        """S2 of #1671, through the wiring: the versions are read at the base
        and at the head, and the subjects between them."""
        m = gate()
        tracker = Tracker(label=[88], subjects=[FEAT])
        tracker.versions["HEAD"] = PATCH
        wire(monkeypatch, m, tracker, {10: "Closes #88"})
        assert m.main() == 1
        out = capsys.readouterr().out
        assert f"::error::the head moves plugin.json to {PATCH}" in out, out
        assert f"`{FEAT}`" in out, out

    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_both_readings_run_on_one_read_of_the_subjects(self, monkeypatch, capsys):
        """A release whose labels agree with its range does not let a wrong
        number through, and the range is read once for both readings."""
        m = gate()
        tracker = Tracker(label=[88], subjects=[FEAT])
        tracker.versions["HEAD"] = PATCH
        wire(monkeypatch, m, tracker, {10: "Closes #88"})
        assert m.main() == 1
        out = capsys.readouterr().out
        assert "::error::" in out and f"`{FEAT}`" in out, out
        assert "D (carried by this release): #88" in out, (
            "the label reading did not run beside the number reading"
        )
        logs = [args for args in tracker.calls if args[0] == "git" and "log" in args]
        assert len(logs) == 1, f"the subjects were read {len(logs)} times"

    def test_a_label_refusal_fails_the_step_with_the_number_right(self, monkeypatch):
        """The exit code is either reading's failure, so a stray label still
        stops a release whose number is the one read."""
        m = gate()
        tracker = Tracker(label=[88, 92], subjects=["fix: a thing (#100)"])
        tracker.versions["HEAD"] = PATCH
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        assert m.main() == 1

    def test_both_refusals_are_reported_together(self, monkeypatch, capsys):
        """A run that stopped at the first refusal would send a release
        preparation round the loop twice."""
        m = gate()
        tracker = Tracker(label=[88, 77], subjects=[FEAT])
        tracker.versions["HEAD"] = PATCH
        wire(monkeypatch, m, tracker, {10: "Closes #88"})
        assert m.main() == 1
        out = capsys.readouterr().out
        assert "::error::the head moves plugin.json" in out, out
        assert "::error::L \\ D" in out and "#77" in out, out

    def test_accepts_a_release_and_measures_from_where_it_left_main(self, monkeypatch):
        """`questions.md` Q8 of #359. `origin/main..HEAD` is the obvious
        spelling and it is wrong the moment `main` moves during a release's
        life; what the release carries is what it accumulated since it was
        cut. The versions are read at the base and at the head."""
        m = gate()
        tracker = Tracker(label=[88], subjects=["fix: a thing (#100)"])
        tracker.versions["HEAD"] = PATCH
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
        shows = [a[2] for a in tracker.calls if a[:2] == ("git", "show")]
        assert shows == [
            "origin/main:.claude-plugin/plugin.json",
            "HEAD:.claude-plugin/plugin.json",
        ], shows

    def test_the_range_is_measured_to_the_head_the_pull_request_names(
        self, monkeypatch
    ):
        """Round 1, finding 2 of #359. The script did what its docstring said
        and the checkout undid it.

        `actions/checkout` takes the MERGE ref on a `pull_request` event, so
        `HEAD` in the job already contains the base and the fork point
        collapses to the base tip, and the head's `plugin.json` is the merge
        ref's. So the head is an input, and this is the case that has it.
        """
        m = gate()
        head = "c" * 40
        tracker = Tracker(
            versions={"origin/main": BASE_VERSION, head: PATCH},
            label=[88],
            subjects=["fix: a thing (#100)"],
        )
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        monkeypatch.setenv("HEAD_SHA", head)
        assert m.main() == 0
        assert tracker.call_with("merge-base") == (
            "git",
            "merge-base",
            "origin/main",
            head,
        ), "the fork point is still measured against the merge ref"
        log = tracker.call_with("git", "log")
        assert log[-1] == "f" * 40 + ".." + head, (
            f"D was read over {log[-1]!r}, which does not end at the head the "
            "pull request names"
        )
        assert ("git", "show", f"{head}:.claude-plugin/plugin.json") in (
            tracker.calls
        ), "the head's version is not read at the head the pull request names"

    def test_without_a_named_head_the_range_ends_at_HEAD(self, monkeypatch):
        """The control for the case above, and the by-hand path.

        A session running this outside CI has no pull request and no head commit
        to name; its own `HEAD` is the branch tip, which is the thing CI's `HEAD`
        is not. Without this, setting `HEAD_SHA` to a constant would pass every
        assertion above.
        """
        m = gate()
        tracker = Tracker(label=[88], subjects=["fix: a thing (#100)"])
        tracker.versions["HEAD"] = PATCH
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        assert m.main() == 0
        assert tracker.call_with("merge-base")[3] == "HEAD"
        assert tracker.call_with("git", "log")[-1].endswith("..HEAD")

    def test_the_base_the_range_starts_from_is_configurable(self, monkeypatch):
        """CI passes `origin/<base_ref>`, and a session checking a release by
        hand has a different remote name for it. The base's version is read
        there too."""
        m = gate()
        tracker = Tracker(
            versions={"upstream/main": BASE_VERSION, "HEAD": PATCH}, subjects=[]
        )
        wire(monkeypatch, m, tracker, {})
        monkeypatch.setenv("BASE", "upstream/main")
        assert m.main() == 0
        assert tracker.call_with("merge-base")[2] == "upstream/main"
        assert ("git", "show", "upstream/main:.claude-plugin/plugin.json") in (
            tracker.calls
        ), tracker.calls

    def test_L_is_read_in_every_state(self, monkeypatch):
        """An issue closed by hand mid-release still carries the label the signal
        put on it. Reading only the open ones would report it as `D \\ L`, the
        signal blamed for a person's edit."""
        m = gate()
        tracker = Tracker(label=[88], subjects=["fix: a thing (#100)"])
        tracker.versions["HEAD"] = PATCH
        wire(monkeypatch, m, tracker, {100: "Closes #88"})
        assert m.main() == 0
        call = tracker.call_with("--label")
        assert call[call.index("--label") + 1] == LABEL
        assert call[call.index("--state") + 1] == "all"

    def test_D_comes_from_the_same_readers_the_signal_writes_it_with(self, monkeypatch):
        """The gate recomputes D rather than trusting L, and it has to recompute
        it the same way: a second reader of a pull request body is how the label
        and the refusal come to disagree about a fenced example."""
        m = gate()
        tracker = Tracker(
            label=[88],
            subjects=["fix: a thing (#100)", "docs: quoted (#101)"],
        )
        tracker.versions["HEAD"] = PATCH
        wire(monkeypatch, m, tracker, {100: "Closes #88", 101: "```\nCloses #92\n```"})
        assert m.main() == 0
        source = read(SCRIPT)
        assert "signal.issues_in(" in source, "the gate derives D some other way"
        for own in ("CLOSING = re.compile", "MERGED_PR = re.compile"):
            assert own not in source, f"the gate wrote its own {own.split()[0]}"

    def test_a_keyword_inside_an_html_comment_puts_nothing_in_D(
        self, monkeypatch, capsys
    ):
        """#1181. GitHub creates no reference from a keyword inside a comment
        (#1402), so a release whose only body naming #92 holds it in one does
        not carry #92."""
        m = gate()
        tracker = Tracker(
            label=[88],
            subjects=["fix: a thing (#100)", "docs: a note (#101)"],
        )
        tracker.versions["HEAD"] = PATCH
        wire(monkeypatch, m, tracker, {100: "Closes #88", 101: "<!-- Closes #92 -->"})
        assert m.main() == 0
        out = capsys.readouterr().out
        assert re.search(r"^D \(carried by this release\): #88$", out, re.M), out


class Test_module:
    def test_the_gate_writes_nothing(self, monkeypatch):
        """Its whole job is to judge. A gate that can write is a gate whose red
        can be made green by the thing that went red.

        The argvs are parsed through `argv_words`, never searched: a fold of
        the source survived an argv wrapped one word per line and not a
        comment between two of its words. `argv_words` says what the parse
        closes and what it does not."""
        prefixes = [words[:3] for words in argv_words(read(SCRIPT))]
        for forbidden in ("edit", "close", "create", "delete", "comment", "reopen"):
            assert ["gh", "issue", forbidden] not in prefixes, f"issue {forbidden}"
            assert ["gh", "label", forbidden] not in prefixes, f"label {forbidden}"


test_census = census_case(TARGET)
