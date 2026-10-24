"""`.github/scripts/label_merged_on_release_branch.py`, one class per function.

Issue #359, the signal half: a squash into `release/vX.Y.Z` puts
`merged: X.Y.Z` on the issues its pull requests answered. Until it did, an
issue's state was the only thing on the tracker that said whether a ticket
was done, and that state does not move until `main` moves, once per release.

  S1   a squash labels what its pull requests close, and nothing else
  S2   the label is created when it is absent, before it is added
  S3   re-running changes nothing

The cases replace `close_issues_on_release`'s `run`, `arrived` and
`_issue_api` through `wire`, never the real network. Several are about a
write NOT happening, which is why the fake tracker records every call rather
than only the interesting ones: a case that asserts a label was added cannot
see a second, redundant add beside it.

#942's phase 6 placed these cases from
`tests/test_a_merged_ticket_says_so_on_the_tracker.py`, which keeps the cases
that read the workflow, and the reader case from
`tests/test_a_declared_label_reaches_the_tracker.py`.
"""

import importlib.util
import json
import os

import pytest
from conftest import census_case, read
from test_close_issues_on_release import load

TARGET = ".github/scripts/label_merged_on_release_branch.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPTS = os.path.join(ROOT, ".github", "scripts")
SCRIPT = os.path.join(SCRIPTS, "label_merged_on_release_branch.py")

BRANCH = "release/v1.2.3"
VERSION = "1.2.3"
LABEL = "merged: 1.2.3"
REPO = "example/repo"


def signal():
    """The labelling script, imported so its readers can be monkeypatched.

    Importing it also loads `close_issues_on_release.py`, which is the point:
    a copy of those readers is exactly what this script exists not to have,
    and a test that stubbed them out could not see one arrive.
    """
    spec = importlib.util.spec_from_file_location(
        "specseal_label_merged_for_tests", SCRIPT
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Tracker:
    """A repository's issues, pull requests and labels, and every call made.

    `calls` holds the argument tuples exactly as the script passed them, in
    order, so an assertion can ask about ordering and about absence -- both of
    which a "was it labelled" check cannot see.
    """

    def __init__(self, issues=None, pulls=None, labels=()):
        self.issues = dict(issues or {})
        self.pulls = dict(pulls or {})
        self.labels = set(labels)
        self.calls = []

    def api(self, repo, number):
        if number in self.pulls:
            return {"pull_request": {}, "body": self.pulls[number]}, True
        if number in self.issues:
            return {
                "labels": [{"name": name} for name in self.issues[number]],
                "state": "open",
            }, True
        return None, False

    def run(self, *args):
        self.calls.append(args)
        if args[:3] == ("gh", "label", "list"):
            return json.dumps([{"name": name} for name in sorted(self.labels)])
        if args[:3] == ("gh", "label", "create"):
            self.labels.add(args[3])
            return ""
        if args[:3] == ("gh", "issue", "edit"):
            self.issues[int(args[3])].append(args[-1])
            return ""
        raise AssertionError(f"unexpected command: {args}")

    def writes(self):
        """The calls that change the tracker — everything but the read."""
        return [a for a in self.calls if a[:3] != ("gh", "label", "list")]


def wire(monkeypatch, module, tracker, subjects, branch=BRANCH, **env):
    monkeypatch.setattr(module.closer, "arrived", lambda before, after: subjects)
    monkeypatch.setattr(module.closer, "_issue_api", tracker.api)
    monkeypatch.setattr(module.closer, "run", tracker.run)
    monkeypatch.setenv("BRANCH", branch)
    monkeypatch.setenv("BEFORE", "a" * 40)
    monkeypatch.setenv("AFTER", "b" * 40)
    monkeypatch.setenv("REPO", REPO)
    monkeypatch.delenv("DRY_RUN", raising=False)
    for name, value in env.items():
        monkeypatch.setenv(name, value)


class Test_version_of:
    def test_accepts_a_release_branch_and_names_its_milestone_and_label(self):
        """One fact spelled four ways, and nothing checked the chain before.

        `docs/issues-and-milestones.md` and `docs/release-checklist.md` both write
        parts of it out in prose; the gate and the signal both have to agree with
        it and with each other, and a mismatch between `release: X.Y.Z` and
        `merged: X.Y.Z` is a release blocked on a milestone nothing can satisfy.
        """
        m = signal()
        assert m.version_of("release/v1.2.3") == "1.2.3"
        assert m.milestone_title("1.2.3") == "release: 1.2.3"
        assert m.label_name("1.2.3") == "merged: 1.2.3"
        assert "release/v1.2.3" in m.label_description("1.2.3"), (
            "the label's description does not name the branch it records, so a "
            "person reading it on the tracker cannot tell which release it means"
        )

    @pytest.mark.parametrize(
        "branch",
        [
            "main",
            "feat/a-thing",
            "release/next",
            "release/v1.2",
            "",
            "release/v1.2.3.4",
        ],
    )
    def test_refuses_a_branch_that_is_not_a_release(self, branch):
        """A shape it cannot name a version for is skipped, never guessed.

        The workflow triggers on `release/*`, so `release/next` reaches this and a
        version read out of it would be invented. `docs/branch-and-release.md`
        names only `release/vX.Y.Z`.
        """
        assert signal().version_of(branch) is None


class Test_main:
    def test_refuses_a_non_release_branch_and_writes_nothing(self, monkeypatch):
        """The skip is at entry: no range read, no API call, no write."""
        m = signal()
        tracker = Tracker(issues={88: []}, pulls={100: "Closes #88"})
        wire(monkeypatch, m, tracker, ["feat: a thing (#100)"], branch="release/next")
        m.main()
        assert tracker.calls == [], (
            "a branch with no version in its name still reached the tracker"
        )

    def test_accepts_the_issue_the_keyword_named_and_labels_nothing_else(
        self, monkeypatch
    ):
        """S1. Swapping the key and the value in `wanted` would label the pull
        requests instead of the issues, and no string check can see that."""
        m = signal()
        tracker = Tracker(
            issues={88: [], 92: []},
            pulls={100: "Closes #88", 101: "Part of #92"},
            labels={LABEL},
        )
        wire(
            monkeypatch,
            m,
            tracker,
            ["feat: a thing (#100)", "docs: another (#101)"],
        )
        m.main()
        assert tracker.issues[88] == [LABEL]
        assert tracker.issues[92] == [], (
            "`Part of #92` is not a closing keyword, and #92 was labelled anyway"
        )
        assert tracker.writes() == [
            ("gh", "issue", "edit", "88", "--repo", REPO, "--add-label", LABEL)
        ]

    def test_a_keyword_inside_a_fence_labels_nothing(self, monkeypatch):
        """The readers are the closer's, so a quoted example is not a claim here
        either. A body quoting `docs/branch-and-release.md`'s fenced example would
        otherwise label the issue that document names, and bodies here quote the
        documents routinely."""
        m = signal()
        tracker = Tracker(issues={88: []}, pulls={100: "```\nCloses #88\n```"})
        wire(monkeypatch, m, tracker, ["feat: a thing (#100)"])
        m.main()
        assert tracker.writes() == [], "a fenced keyword was read as a claim"

    def test_a_number_that_names_no_pull_request_is_skipped(self, monkeypatch):
        """`fix: the thing (#61)` is a number a person typed to name an issue.
        Failing on it would fail a push for a commit message."""
        m = signal()
        tracker = Tracker(issues={61: [], 88: []}, pulls={100: "Closes #88"})
        wire(monkeypatch, m, tracker, ["fix: a thing (#61)", "feat: b (#100)"])
        m.main()
        assert tracker.issues[61] == [], "an issue number in a subject was labelled"
        assert tracker.issues[88] == [LABEL]

    def test_a_claimed_number_that_names_nothing_is_skipped(self, monkeypatch):
        """A typo in a merged body is input, not a failure — and the run has to
        reach the issues sorted after it."""
        m = signal()
        tracker = Tracker(issues={88: []}, pulls={100: "closes #9999, closes #88"})
        wire(monkeypatch, m, tracker, ["feat: a thing (#100)"])
        m.main()
        assert tracker.issues[88] == [LABEL], (
            "a number naming nothing stopped the run before the real issue"
        )

    def test_the_label_is_created_before_it_is_added(self, monkeypatch):
        """S2. Ordering, because an add against a label that does not exist fails
        — and a case that only asserts both calls happened cannot see the order
        they happened in."""
        m = signal()
        tracker = Tracker(issues={88: []}, pulls={100: "Closes #88"}, labels=set())
        wire(monkeypatch, m, tracker, ["feat: a thing (#100)"])
        m.main()
        writes = tracker.writes()
        assert [a[:3] for a in writes] == [
            ("gh", "label", "create"),
            ("gh", "issue", "edit"),
        ], f"the label was not created before it was added: {writes}"
        assert writes[0][3] == LABEL
        assert "--description" in writes[0], (
            "the label is created with no description, so the tracker shows a "
            "bare name where a person has to work out what it means"
        )

    def test_an_existing_label_is_not_created_again(self, monkeypatch):
        """S2's other half. `gh label create` on a name that exists is an error,
        so this is the difference between a green run and a red one on every
        release after the first push."""
        m = signal()
        tracker = Tracker(issues={88: []}, pulls={100: "Closes #88"}, labels={LABEL})
        wire(monkeypatch, m, tracker, ["feat: a thing (#100)"])
        m.main()
        assert [a[:3] for a in tracker.writes()] == [("gh", "issue", "edit")]

    def test_the_label_is_read_before_it_is_created(self, monkeypatch):
        """The read is what makes the case above true of the real tracker rather
        than of this fixture: without it the script would be assuming the label's
        absence instead of checking it."""
        m = signal()
        tracker = Tracker(issues={88: []}, pulls={100: "Closes #88"}, labels=set())
        wire(monkeypatch, m, tracker, ["feat: a thing (#100)"])
        m.main()
        assert tracker.calls[0][:3] == ("gh", "label", "list"), (
            f"the first tracker call was {tracker.calls[0]}, not the label read"
        )

    def test_an_issue_that_already_carries_the_label_is_left_alone(self, monkeypatch):
        """S3, and the reason it is a case rather than an assumption.

        Whether adding a label an issue already has errors or is a no-op was never
        measured here (`questions.md` Q6). Reading first means the answer is not
        load-bearing: the path is never reached. A future edit that drops the read
        and adds unconditionally turns this red.
        """
        m = signal()
        tracker = Tracker(
            issues={88: [LABEL, "documentation"]},
            pulls={100: "Closes #88"},
            labels={LABEL},
        )
        wire(monkeypatch, m, tracker, ["feat: a thing (#100)"])
        m.main()
        assert tracker.writes() == [], "the same push labelled #88 a second time"
        assert tracker.issues[88] == [LABEL, "documentation"]

    def test_a_push_with_no_claimed_issue_writes_nothing(self, monkeypatch):
        """Including no label creation. A release branch that moves for a commit
        claiming nothing must not leave a label behind for a version it has not
        yet shipped anything of."""
        m = signal()
        tracker = Tracker(pulls={100: "Part of #92"}, labels=set())
        wire(monkeypatch, m, tracker, ["feat: a thing (#100)"])
        m.main()
        assert tracker.calls == []

    def test_dry_run_reads_and_writes_nothing(self, monkeypatch):
        """The neighbouring script grew this flag because it was run by hand for
        its output and closed a real issue. The same hand reaches this one."""
        m = signal()
        tracker = Tracker(issues={88: []}, pulls={100: "Closes #88"}, labels=set())
        wire(monkeypatch, m, tracker, ["feat: a thing (#100)"], DRY_RUN="1")
        m.main()
        assert tracker.writes() == [], "DRY_RUN wrote to the tracker"
        assert tracker.issues[88] == []


class Test_module:
    def test_the_label_reader_has_one_source(self):
        """Two scripts read an issue's labels and there is one reader. A second
        copy is what `label_merged_on_release_branch.py`'s own docstring says it
        exists not to have, and it had one until this work item gave the second
        caller a reason to share."""
        signal = load("label_merged", "label_merged_on_release_branch.py")
        assert hasattr(signal.closer, "issue_labels"), (
            "the reader is no longer on the module that owns the 404-tolerant "
            "read it is built on"
        )
        # The CALL, not the word. The sibling's docstring says in prose that it
        # used to unpack `closer._issue_api` here and now delegates, and a check
        # on the bare name counts that sentence as the defect — which would make
        # explaining the history the thing that fails.
        source = read(os.path.join(SCRIPTS, "label_merged_on_release_branch.py"))
        assert "_issue_api(" not in source, (
            "the sibling unpacks the private read again instead of delegating, "
            "which is the copied reader coming back"
        )

    def test_the_label_description_fits_the_trackers_cap_for_a_long_version(self):
        """#515's class. This description goes to `gh label create` too, and the
        tracker refuses one past its cap with a 422 — in the workflow that runs
        when a release branch moves, after the merge. The version is the only part
        that grows, so the case takes one far longer than any this repository will
        cut: fitting at that length is fitting at every realistic one."""
        m = signal()
        description = m.label_description("9999.9999.9999")
        assert len(description) <= m.LABEL_DESCRIPTION_LIMIT, (
            f"the tracker refuses a label description past "
            f"{m.LABEL_DESCRIPTION_LIMIT} characters, and this one is "
            f"{len(description)}: {description!r}"
        )

    def test_the_script_only_ever_creates_a_label_and_adds_one(self):
        """Fold the source before matching: the arguments go one per line, so a
        forbidden-substring list over the raw text forbids nothing.

        `close_issues_on_release.py` has the same case for the same reason — what
        makes a re-run and a force-push safe to reason about is that the set of
        writes is small enough to enumerate.
        """
        folded = " ".join(read(SCRIPT).split())
        assert '"gh", "label", "create",' in folded, "the script stopped creating"
        assert '"--add-label",' in folded, "the script stopped adding"
        for forbidden in ("close", "reopen", "delete", "comment", "transfer"):
            assert f'"gh", "issue", "{forbidden}"' not in folded, (
                f"the script gained `issue {forbidden}`. Closing an issue at the "
                "release-branch merge closes it for something nobody has received"
            )
        assert '"gh", "label", "delete"' not in folded, (
            "the script gained `label delete`, which removes the label from every "
            "issue that carried it and falsifies the record it was created to "
            "leave"
        )

    def test_the_readers_come_from_the_closer_rather_than_a_second_copy(self):
        """Two readers of the same pull request body drifted apart here before.

        `FENCE` and `SPAN` were widened once, for #266, and the comment above
        them says which shapes stay unmasked and why; a second copy of that
        treatment would answer that decision again by accident, in a file whose
        author never read the comment.
        """
        source = read(SCRIPT)
        assert "close_issues_on_release.py" in source, "the closer is not imported"
        for own in ("CLOSING = re.compile", "FENCE = re.compile", "SPAN = re.compile"):
            assert own not in source, f"the script wrote its own {own.split()[0]}"
        m = signal()
        assert m.closer.keywords_in("see `Closes #54` in the doc") == [], (
            "the imported reader is not the one that ignores a code span"
        )


test_census = census_case(TARGET)
