"""`.github/scripts/tracker_labels.py`, one class per function.

#450: a label this repository's documents specify exists on the tracker.
`size: now` was specified in 0.11.1 and never created, because the work item
that wrote the section assigned creating it to a person, and a person has no
queue anything here can read. The repair moves the act to the workflow that
already runs when `main` moves.

  A9   the reconcile step creates a missing label with the description the
       specifying document's own sentence gives, and says so
  A10  reconciling is idempotent: every label present, nothing written, exit 0
  A13  every declared description fits the tracker's cap, read from
       `LABEL_DESCRIPTION_LIMIT` rather than written here (#515)

**Nothing here reaches GitHub.** The fake tracker is
`tests/github/test_close_issues_on_release.py`'s `Tracker`, for its stated reason:
it records every call as an argument tuple, in order, so a case can assert
about a write that did NOT happen.

#942's phase 6 placed these cases from
`tests/behaviour/test_a_declared_label_reaches_the_tracker.py`, which keeps the cases
that read the workflow and `docs/issues-and-milestones.md`.
"""

from conftest import census_case
from test_close_issues_on_release import LABEL, REPO, Tracker, load

TARGET = ".github/scripts/tracker_labels.py"


def labels_module():
    return load("tracker_labels", "tracker_labels.py")


class Test_create:
    def test_accepts_the_declared_label_in_its_declared_colour(self, monkeypatch):
        """The colour is the declaration's, which says why it is
        `chain: capped`'s, so two labels of one shape read as one shape."""
        mod = labels_module()
        tracker = Tracker()
        monkeypatch.setattr(mod.closer, "run", tracker.run)
        (label,) = mod.declared()
        mod.create(REPO, label)
        (created,) = tracker.calls
        assert created[created.index("--color") + 1] == label["color"], created

    def test_refuses_to_send_any_name_sentence_or_colour_but_the_labels_own(
        self, monkeypatch
    ):
        mod = labels_module()
        tracker = Tracker()
        monkeypatch.setattr(mod.closer, "run", tracker.run)
        other = {"name": "chain: capped", "description": "a cap", "color": "abcdef"}
        mod.create(REPO, other)
        (created,) = tracker.calls
        assert created[3] == "chain: capped", created
        assert created[created.index("--description") + 1] == "a cap", created
        assert created[created.index("--color") + 1] == "abcdef", created


class Test_main:
    def test_accepts_a_missing_label_and_creates_it_with_the_documents_sentence(
        self, monkeypatch, capsys
    ):
        """A9. The description is what a person reads on the tracker, so it is the
        specifying document's sentence rather than a summary of it — and it says
        when the label stops being the current answer, which is the half nothing
        else on the tracker can tell them."""
        mod = labels_module()
        tracker = Tracker(labels={"documentation", "release"})
        monkeypatch.setattr(mod.closer, "run", tracker.run)
        monkeypatch.setenv("REPO", REPO)
        monkeypatch.delenv("DRY_RUN", raising=False)

        assert mod.main(["--apply"]) == 0
        created = [a for a in tracker.calls if a[:3] == ("gh", "label", "create")]
        assert len(created) == 1, tracker.calls
        assert created[0][3] == LABEL
        description = created[0][created[0].index("--description") + 1]
        assert "before the next work item starts" in description, (
            "the description is not the document's own sentence about what the label means"
        )
        assert "removed when its release closes the issue" in description, (
            "the description does not say when the label stops being the current "
            "answer, which is the one thing a reader cannot get from the name"
        )
        assert LABEL in capsys.readouterr().out

    def test_reconciling_an_already_complete_tracker_writes_nothing(
        self, monkeypatch, capsys
    ):
        """A10. A re-run of a push, a re-pushed release, a workflow re-run — all
        land here, and the no-op is by construction: the write happens only after
        a read says the name is absent."""
        mod = labels_module()
        tracker = Tracker(labels={label["name"] for label in mod.declared()})
        monkeypatch.setattr(mod.closer, "run", tracker.run)
        monkeypatch.setenv("REPO", REPO)
        monkeypatch.delenv("DRY_RUN", raising=False)

        assert mod.main(["--apply"]) == 0
        assert tracker.writes() == [], "it wrote to a tracker that needed nothing"
        assert "nothing to create" in capsys.readouterr().out

    def test_refuses_to_write_under_check_and_reports_what_is_missing(
        self, monkeypatch, capsys
    ):
        """`--check` is the arm a person types. It must not be the arm that acts,
        because then reading the state and changing it are one keystroke apart."""
        mod = labels_module()
        tracker = Tracker(labels=set())
        monkeypatch.setattr(mod.closer, "run", tracker.run)
        monkeypatch.setenv("REPO", REPO)
        monkeypatch.delenv("DRY_RUN", raising=False)

        assert mod.main(["--check"]) == 0
        assert tracker.writes() == []
        out = capsys.readouterr().out
        assert LABEL in out and "is missing" in out
        assert "--apply" in out, "the report does not name the arm that fixes it"

    def test_refuses_to_write_under_a_dry_run_of_apply(self, monkeypatch, capsys):
        """`DRY_RUN=1` makes `--apply` say what it would create and write
        nothing, so the arm that acts can be read before it acts."""
        mod = labels_module()
        tracker = Tracker(labels=set())
        monkeypatch.setattr(mod.closer, "run", tracker.run)
        monkeypatch.setenv("REPO", REPO)
        monkeypatch.setenv("DRY_RUN", "1")

        assert mod.main(["--apply"]) == 0
        assert tracker.writes() == [], "a dry run created a label"
        assert f"{LABEL!r} is missing" in capsys.readouterr().out


class Test_module:
    def test_every_declared_description_fits_the_trackers_cap(self):
        """A13, #515. GitHub refuses a label description past its cap with a 422,
        and the refusal arrives in the workflow that runs after a release reaches
        `main` — where it skips the step behind it and nobody is looking. Held
        here, an over-long description is refused before the merge instead.

        The cap is read from the module that names it rather than written here,
        so the number has one source and a pointer to where it comes from."""
        mod = labels_module()
        limit = mod.signal.LABEL_DESCRIPTION_LIMIT
        too_long = [
            (label["name"], len(label["description"]))
            for label in mod.declared()
            if len(label["description"]) > limit
        ]
        assert not too_long, (
            f"the tracker refuses a label description past {limit} characters, "
            f"and these are longer: {too_long}"
        )


test_census = census_case(TARGET)
