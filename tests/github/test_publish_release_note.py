"""`.github/scripts/publish_release_note.py`, one class per function.

#386: the release note publishes itself, or the job goes red saying why.
Publishing a GitHub Release was a habit and nothing else, and three
consecutive releases skipped it. The repair is a workflow the tag push fires:

  A1  the changelog fragments the release's commits added become the release
      note at that tag, each under its work item's marker
  A2  a release already at the tag is left exactly as it is, exit 0
  A3  a tag whose range added no fragment goes RED, naming the range's tags
  A4  the title is read from the `release: X.Y.Z symptoms: <symptoms>` line,
      and where no such line is readable it is the tag name and the log says
      which was used, what it expected and what it found
  A5  the note is a summary read from the release's pull requests -- counts,
      one line per change under its type with the issues it closed, every
      outside contributor thanked by handle -- over the fragments, folded;
      with no pull request to read it is the fragments alone (#572)

#1053 removed the gathered release files, so the fragments are read from the
history at the tag (S1, S5, S6) and the note opens with the release's theme,
one sentence of its milestone's description (S2, S3, S4).

**Nothing here reaches GitHub.** `gh` is replaced at the module's own `run`
and `release_exists` by `Releases`, which records the calls as argument
tuples, in order, so a case can assert about a write that did NOT happen as
well as one that did. The milestone list is answered by `Milestones`, which
stands in for `subprocess.run`. The cases that read the history drive a real
`git` repository in `tmp_path`.

**Shown red before it was committed (contract rule 15).** Each case was run
against the script with the one behaviour it pins removed, in phase 1 of
work item `1790076050-the-release-tail-is-three-acts-no-document-names`, and
S1 to S6 against the script at `8a1173c8`, in phase 1 of work item
`1793188384-the-release-notes-are-kept-twice`.

#942's phase 6 placed these cases from
`tests/behaviour/test_a_release_publishes_its_note.py`, which keeps the cases that
read the workflow and the release checklist.
"""

import importlib.util
import json
import os

import pytest
from conftest import ROOT, census_case, commit_everything, git_out, git_repo, write

TARGET = ".github/scripts/publish_release_note.py"

SCRIPTS = os.path.join(ROOT, ".github", "scripts")
SCRIPT = os.path.join(SCRIPTS, "publish_release_note.py")

# `tests/behaviour/test_release_hygiene.py` refuses a loaded document naming the running
# version or anything above it. These are illustrative, which is the form that
# document's own message points at.
VERSION = "1.2.3"
TAG = "v1.2.3"
PREVIOUS = "v1.2.2"
REPO = "example/repo"
SYMPTOMS = "two acts nobody wrote down"
NOTES = "- **A thing that changed.** And what it changes for a reader."

# The fragments the release's commits added, as `fragments` returns them.
ENTRIES = [("1700000000-a-work-item", NOTES)]


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def publisher():
    return module(SCRIPT, "agentic_publish_release_note_for_tests")


class Done:
    """What `subprocess.run` returns, with the three fields the script reads."""

    def __init__(self, code, out="", err=""):
        self.returncode, self.stdout, self.stderr = code, out, err


class Milestones:
    """The repository's milestones, answered where the script lists them.

    `listed` is the list `gh api` prints, or None for a list that cannot be
    read. `calls` holds each argument list the script passed, in order.
    """

    def __init__(self, listed):
        self.listed = listed
        self.calls = []

    def __call__(self, args, **_):
        self.calls.append(list(args))
        assert list(args[:2]) == ["gh", "api"], f"unexpected command: {args}"
        if self.listed is None:
            return Done(1, err="HTTP 403: Resource not accessible by integration")
        return Done(0, json.dumps(self.listed))


def milestone(description, version=VERSION):
    return {"title": f"release: {version}", "description": description}


class Releases:
    """The releases a repository has, and every command the script ran.

    `calls` holds the argument tuples as the script passed them, in order, so
    a case can ask about absence — which is what A2 is entirely about.
    """

    def __init__(self, existing=()):
        self.existing = set(existing)
        self.calls = []

    def exists(self, repo, tag):
        return tag in self.existing

    def run(self, *args):
        self.calls.append(args)
        if args[:3] == ("gh", "release", "create"):
            self.existing.add(args[3])
            return ""
        if args[:2] == ("git", "log"):
            return self.message
        raise AssertionError(f"unexpected command: {args}")

    message = ""

    def creates(self):
        return [a for a in self.calls if a[:3] == ("gh", "release", "create")]


def wire(
    monkeypatch,
    tmp_path,
    entries=ENTRIES,
    message="",
    existing=(),
    pulls=(),
    milestones=(),
    **env,
):
    """The script, with fixture fragments and no route to GitHub. `entries`
    are the fragments the range added, read after `PREVIOUS`; `milestones` is
    the milestone list, None for one that cannot be read."""
    mod = publisher()
    monkeypatch.setattr(
        mod,
        "merged_pulls",
        lambda repo, version: None if pulls is None else list(pulls),
    )
    tracker = Releases(existing)
    tracker.message = message
    monkeypatch.setattr(mod, "ROOT", str(tmp_path))
    monkeypatch.setattr(mod, "run", tracker.run)
    monkeypatch.setattr(mod, "release_exists", tracker.exists)
    monkeypatch.setattr(mod, "previous_tag", lambda tag: PREVIOUS)
    monkeypatch.setattr(mod, "fragments", lambda revisions: list(entries))
    tracker.milestones = Milestones(None if milestones is None else list(milestones))
    monkeypatch.setattr(mod.subprocess, "run", tracker.milestones)
    monkeypatch.setenv("TAG", env.pop("TAG", TAG))
    monkeypatch.setenv("REPO", REPO)
    monkeypatch.delenv("DRY_RUN", raising=False)
    for key, value in env.items():
        monkeypatch.setenv(key, value)
    return mod, tracker


def title_line(version=VERSION, symptoms=SYMPTOMS):
    """A tagged commit's message, in the shape this repository's history has.

    The subject is GitHub's, written by the merge button; the prescribed line
    is below it. That split is the measurement #386's own sentence got wrong,
    so the fixture carries it rather than a bare title line.
    """
    return (
        f"Merge pull request #500 from owner/release/v{version}\n\n"
        f"release: {version} symptoms: {symptoms}\n"
    )


def pull(number, login, title="docs: a sentence", body="", is_bot=False):
    return {
        "number": number,
        "title": title,
        "body": body,
        "author": {"login": login, "is_bot": is_bot},
    }


OWNER = REPO.split("/")[0]

RELEASE = [
    pull(9, OWNER, f"chore: release {VERSION} — the gathering", "Closes #1"),
    pull(10, OWNER, "fix: the owner's own change", "Closes #100 and fixes #101"),
    pull(11, "someone", "docs: explain a thing", "Closes #102"),
    pull(12, "dependabot[bot]", "chore: bump", is_bot=True),
    pull(13, "app/renovate", "chore: bump again"),
    pull(14, "someone", "fix(gate): and a second thing (#103)", "Closes #103"),
    pull(15, "another", "feat: a third", "Quotes `Closes #999` and closes #100"),
    pull(16, OWNER, "an untyped title"),
]


def body_of(tracker):
    args = tracker.creates()[0]
    return args[args.index("--notes") + 1]


def published(monkeypatch, tmp_path, pulls, **kw):
    mod, tracker = wire(monkeypatch, tmp_path, message=title_line(), pulls=pulls, **kw)
    assert mod.main() == 0
    return mod, body_of(tracker)


def lines_under(body, heading):
    """The `- ` lines between `heading` and the next heading or fold."""
    rest = body[body.index(heading) + len(heading) :]
    out = []
    for line in rest.splitlines()[1:]:
        if line.startswith(("### ", "<details>")):
            break
        if line.startswith("- "):
            out.append(line)
    return out


class Test_main:
    def test_accepts_the_releases_fragments_as_the_release_note(
        self, monkeypatch, tmp_path, capsys
    ):
        """A1. The body is the fragments the release's commits added, each under
        the marker naming its work item, and it links to no file in the tree."""
        mod, tracker = wire(monkeypatch, tmp_path, message=title_line())
        assert mod.main() == 0
        created = tracker.creates()
        assert len(created) == 1, tracker.calls
        args = created[0]
        assert args[3] == TAG
        body = args[args.index("--notes") + 1]
        assert f"<!-- specs/1700000000-a-work-item -->\n{NOTES}" in body, body
        assert "changelog/" not in body, "the note still names a gathered file"
        assert "published the release" in capsys.readouterr().out

    def test_the_note_is_built_from_the_fragments_the_range_added(
        self, monkeypatch, tmp_path, capsys
    ):
        """S1 of #1053. Two fragments added after `v1.2.2`, one of them edited
        and then removed by a settle before `v1.2.3`, both reach the note in id
        order, the removed one as it stood last. The fragment added before
        `v1.2.2` stays out though a commit in the range edited it, a fragment
        the settle's commit added beside a removed one of the same text is not
        read as its rename, an empty fragment gives no entry, and no
        `changelog/` path is named. Driven through a real `git` history."""
        repo = git_repo(tmp_path / "repo")
        thread = "seal/threads/{}/changelog.md"
        write(repo, thread.format("1700000000-older"), "- older entry\n")
        commit_everything(repo, "the release before")
        git_out(repo, "tag", PREVIOUS)
        write(repo, thread.format("1700000002-second"), "- second entry\n")
        commit_everything(repo, "the later work item")
        write(repo, thread.format("1700000001-first"), "- first entry\n")
        commit_everything(repo, "the earlier work item")
        write(repo, thread.format("1700000001-first"), "- first entry, revised\n")
        write(repo, thread.format("1700000000-older"), "- older entry, edited\n")
        commit_everything(repo, "a fix brings its fragment along")
        git_out(repo, "rm", "-q", "-r", "seal/threads/1700000001-first")
        git_out(repo, "rm", "-q", "-r", "seal/threads/1700000000-older")
        # Added in the settle's own commit with the removed fragment's text,
        # so only `--no-renames` keeps it from reading as a rename.
        write(repo, thread.format("1700000003-third"), "- first entry, revised\n")
        write(repo, thread.format("1700000004-empty"), "\n  \n")
        commit_everything(repo, "the settle")
        git_out(repo, "tag", TAG)

        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        monkeypatch.chdir(repo)
        monkeypatch.setattr(mod, "release_exists", lambda repo, tag: False)
        monkeypatch.setattr(mod, "merged_pulls", lambda repo, version: None)
        monkeypatch.setattr(
            mod, "milestone_description", lambda repo, version: ("", "none")
        )
        monkeypatch.setenv("TAG", TAG)
        monkeypatch.setenv("REPO", REPO)
        monkeypatch.setenv("DRY_RUN", "1")
        assert mod.main() == 0
        out = capsys.readouterr().out
        first = "<!-- specs/1700000001-first -->\n- first entry, revised"
        second = "<!-- specs/1700000002-second -->\n- second entry"
        third = "<!-- specs/1700000003-third -->\n- first entry, revised"
        assert first in out and second in out and third in out, out
        assert out.index(first) < out.index(second) < out.index(third), (
            "the fragments are not in id order"
        )
        assert "1700000004-empty" not in out, "an empty fragment became an entry"
        assert "older entry" not in out, "a fragment of the release before reached it"
        assert "changelog/" not in out, out

    def test_the_note_opens_with_the_releases_theme(
        self, monkeypatch, tmp_path, capsys
    ):
        """S2 of #1053. The first line of the note is the first sentence of the
        description of the milestone `release: X.Y.Z`, its `Purpose:` label
        left out, read from every milestone in every state."""
        described = "Purpose: the notes come from the fragments. Order: S1, then S2."
        mod, tracker = wire(
            monkeypatch,
            tmp_path,
            message=title_line(),
            pulls=RELEASE,
            milestones=[
                milestone("Purpose: an older one.", "1.2.2"),
                milestone(described),
            ],
            DRY_RUN="1",
        )
        assert mod.main() == 0
        out = capsys.readouterr().out
        note = out.split("characters of notes\n", 1)[1]
        assert note.splitlines()[0] == "The notes come from the fragments.", note[:300]
        assert note.splitlines()[2] == mod.GLANCE_HEADING, note[:300]
        (args,) = tracker.milestones.calls
        assert "--paginate" in args, args
        assert args[-1].startswith(f"repos/{REPO}/milestones?state=all"), args

    @pytest.mark.parametrize(
        "milestones, said",
        [
            pytest.param(None, "the milestones could not be listed", id="unread"),
            pytest.param(
                [milestone("Purpose: another.", "1.2.2")],
                f"no milestone is titled `release: {VERSION}`",
                id="not found",
            ),
            pytest.param(
                [milestone(" \n ")],
                f"the milestone `release: {VERSION}` has no description",
                id="empty",
            ),
        ],
    )
    def test_without_a_theme_the_note_has_no_theme_line_and_the_job_goes_on(
        self, monkeypatch, tmp_path, capsys, milestones, said
    ):
        """S4 of #1053. A milestone that cannot be listed, is not found or has
        an empty description leaves the note without a theme line, the job log
        says which of the three it was, and the release is published as it would
        have been with one."""
        mod, tracker = wire(
            monkeypatch,
            tmp_path,
            message=title_line(),
            pulls=RELEASE,
            milestones=milestones,
        )
        assert mod.main() == 0
        assert len(tracker.creates()) == 1, tracker.calls
        assert body_of(tracker).startswith(mod.GLANCE_HEADING), body_of(tracker)[:200]
        out = capsys.readouterr().out
        assert said in out and "no theme line" in out, out

    def test_an_existing_release_is_left_exactly_as_it_is(
        self, monkeypatch, tmp_path, capsys
    ):
        """A2. A re-pushed tag and a re-run job both land here. The note may have
        been edited by hand after publication, so the only safe act is none."""
        mod, tracker = wire(
            monkeypatch, tmp_path, message=title_line(), existing=(TAG,)
        )
        assert mod.main() == 0
        assert tracker.calls == [], (
            "something ran against GitHub for a release that already exists"
        )
        assert "already exists" in capsys.readouterr().out

    def test_refuses_a_tag_whose_range_added_no_fragment(
        self, monkeypatch, tmp_path, capsys
    ):
        """A3, and S5 of #1053. This is the release shipping unexplained, and the
        body is the whole of what the job publishes — so it is the one direction
        that fails. The message names both tags of the range it read."""
        mod, tracker = wire(monkeypatch, tmp_path, entries=[], message=title_line())
        assert mod.main() == 1
        assert tracker.creates() == [], "it published a release with no notes"
        out = capsys.readouterr().out
        assert PREVIOUS in out and TAG in out, (
            "the message does not name the range it read, so the job log does "
            "not say what to fix"
        )
        assert "changelog.md" in out, "the message does not name what it looked for"

    def test_a_tag_that_is_not_a_version_goes_red(self, monkeypatch, tmp_path, capsys):
        """A3's neighbour. `v*` matches `vnext` too, and a tag this cannot name a
        version for has no section to look for — so it says so instead of
        guessing one, the way `label_merged_on_release_branch.py` refuses a branch
        name it cannot read a version out of."""
        mod, tracker = wire(monkeypatch, tmp_path, TAG="vnext")
        assert mod.main() == 1
        assert tracker.calls == []
        assert "not a vX.Y.Z tag" in capsys.readouterr().out

    def test_the_title_is_the_line_the_checklist_prescribes(
        self, monkeypatch, tmp_path, capsys
    ):
        """A4, first branch, and S15 of #1000. `docs/release-checklist.md`
        *5. The release pull request*
        prescribes `release: X.Y.Z symptoms: <symptoms>` for the release pull
        request, and the merge commit's BODY carries it — the subject is GitHub's
        own line. The published title keeps its `X.Y.Z — <symptoms>` form."""
        mod, tracker = wire(monkeypatch, tmp_path, message=title_line())
        assert mod.main() == 0
        args = tracker.creates()[0]
        assert args[args.index("--title") + 1] == f"{VERSION} — {SYMPTOMS}"
        assert "the tagged commit's `release:` line" in capsys.readouterr().out, (
            "the log does not say which source the title came from, so a wrong "
            "title cannot be traced to the end that produced it"
        )

    @pytest.mark.parametrize(
        "line",
        [
            pytest.param(None, id="absent"),
            # The shape every release before #1000 carried, and the hyphen typed
            # for its dash, which dropped the symptoms there.
            pytest.param(f"release: {VERSION} — x", id="the old dash line"),
            pytest.param(f"release: {VERSION} - x", id="a hyphen"),
            # Measured in this repository's own history: v0.12.3's line carries no
            # symptoms. Reading a title out of it gives the version alone, which is
            # the tag name minus one character — so it is not the prescribed line
            # and takes the fallback rather than producing a near-duplicate.
            pytest.param(f"release: {VERSION}", id="no symptoms"),
            pytest.param(f"release: {VERSION} symptoms:", id="an empty value"),
            pytest.param(f"release: {VERSION} symptoms:x", id="no space"),
            pytest.param(f"Release: {VERSION} symptoms: x", id="capitalised"),
            # A line for a different release, which a cherry-pick or a retag can
            # leave on the commit a tag names.
            pytest.param("release: 9.9.9 symptoms: x", id="wrong version"),
        ],
    )
    def test_without_that_line_the_title_is_the_tag_and_the_log_says_so(
        self, monkeypatch, tmp_path, capsys, line
    ):
        """A4, second branch, and S16 of #1000. Nothing holds the
        commit-message convention, so a missing line falls back rather than
        failing: a wrong title is visible and fixable in one edit, where a failed
        job at the tag is a release that stops after `main` has already moved.
        The log names the shape it expected and quotes the first `release:`
        line it found, in any case, or says there was none. Seen red against the
        reader of the dash line, which read `the old dash line` as the title and
        whose log named no shape."""
        message = "Merge pull request #500 from owner/release/v1.2.3\n"
        message += f"\n{line}\n" if line else ""
        mod, tracker = wire(monkeypatch, tmp_path, message=message)
        assert mod.main() == 0
        args = tracker.creates()[0]
        assert args[args.index("--title") + 1] == TAG
        out = capsys.readouterr().out
        assert "the tag name" in out, (
            "the fallback is silent, so a title nobody chose reads as one somebody did"
        )
        assert f"`release: {VERSION} symptoms: <" in out, out
        found = f"`{line}`" if line else "no `release:` line"
        assert found in out, out

    def test_every_change_is_one_line_under_its_type(self, monkeypatch, tmp_path):
        """A5. The list is a partition of the release: every pull request but the
        preparation lands under exactly one heading, an unknown or missing type
        under Other, and each line names the issues its body closes -- read the
        way the closer reads them, so a quoted keyword closes nothing."""
        _, body = published(monkeypatch, tmp_path, RELEASE)
        assert lines_under(body, "### \U0001f41b Fixes") == [
            "- The owner's own change (#10) · closes #100, #101",
            "- And a second thing (#14) · closes #103 — thanks @someone",
        ]
        assert lines_under(body, "### ✨ Features") == [
            "- A third (#15) · closes #100 — thanks @another"
        ]
        assert lines_under(body, "### \U0001f4da Docs") == [
            "- Explain a thing (#11) · closes #102 — thanks @someone"
        ]
        assert lines_under(body, "### \U0001f9f9 Chores") == [
            "- Bump (#12)",
            "- Bump again (#13)",
        ]
        assert lines_under(body, "### \U0001f4e6 Other") == ["- An untyped title (#16)"]
        assert "#9)" not in body, "the preparation pull request is listed as a change"
        assert "#999" not in body, "a keyword inside a code span was read as a claim"
        assert (
            body.index("### ✨ Features")
            < body.index("### \U0001f41b Fixes")
            < body.index("### \U0001f4da Docs")
        ), "the headings are not in the order the note is meant to read in"

    def test_the_glance_counts_the_release(self, monkeypatch, tmp_path):
        """A5. Seven changes, four distinct issues closed (#100 twice counts
        once), two outside people however many pull requests they made."""
        mod, body = published(monkeypatch, tmp_path, RELEASE)
        glance = body[: body.index("### ✨ Features")]
        assert glance.startswith(mod.GLANCE_HEADING)
        assert "| \U0001f500 Pull requests | **7** |" in glance
        assert "| ✅ Issues closed | **4** |" in glance
        assert "| \U0001f64c Outside contributors | **2** |" in glance

    def test_an_outside_contributor_is_thanked_by_handle(self, monkeypatch, tmp_path):
        """A5. The owner's pull requests and a bot's are the release's own work;
        anybody else's is a contribution, and the note names who made it."""
        mod, body = published(monkeypatch, tmp_path, RELEASE)
        assert lines_under(body, mod.THANKS_HEADING) == [
            "- **@someone** — Explain a thing (#11); And a second thing (#14)",
            "- **@another** — A third (#15)",
        ]
        for excluded in (OWNER, "dependabot", "renovate"):
            assert f"@{excluded}" not in body, f"{excluded} is thanked for its own work"

    def test_the_fragments_are_kept_folded_under_the_summary(
        self, monkeypatch, tmp_path
    ):
        """A5. The fragments are the reasoning, and none of it is lost: they
        follow the summary whole, inside a fold that ends the note, each under
        its marker with a blank line before the next (#1053: no link to a file
        follows)."""
        entries = [*ENTRIES, ("1700000001-b", "- b")]
        mod, body = published(monkeypatch, tmp_path, RELEASE, entries=entries)
        fold = body[body.index("<details>") :]
        assert fold == (
            f"<details>\n<summary>{mod.FULL_SUMMARY}</summary>\n\n"
            f"<!-- specs/1700000000-a-work-item -->\n{NOTES}\n\n"
            "<!-- specs/1700000001-b -->\n- b\n\n</details>"
        ), fold
        assert body.index(mod.UPDATE_HEADING) < body.index("<details>")
        assert "/agentic:update" in body

    def test_a_release_with_no_outside_contribution_thanks_nobody(
        self, monkeypatch, tmp_path
    ):
        """A5, the other direction. Most releases carry only the owner's work:
        the summary is there, and no credit line or count is invented."""
        mod, body = published(monkeypatch, tmp_path, [pull(10, OWNER, "fix: a thing")])
        assert mod.THANKS_HEADING not in body
        assert "Outside contributors" not in body
        assert "thanks @" not in body

    @pytest.mark.parametrize(
        "pulls",
        [
            pytest.param(None, id="the list could not be read"),
            pytest.param([], id="no pull request"),
            pytest.param([RELEASE[0]], id="only the preparation"),
        ],
    )
    def test_with_nothing_to_summarise_the_note_is_the_theme_and_the_fragments(
        self, monkeypatch, tmp_path, capsys, pulls
    ):
        """A5 adds no way to fail the tag's job: a summary that cannot be built
        leaves the note the theme line and the fragments, unfolded, as the
        section alone was before #572."""
        theme = [milestone("Purpose: a theme. And more.")]
        _, body = published(monkeypatch, tmp_path, pulls, milestones=theme)
        assert body == f"A theme.\n\n<!-- specs/1700000000-a-work-item -->\n{NOTES}"
        if pulls is None:
            assert "no outside contribution" not in capsys.readouterr().out, (
                "a list that could not be read is reported as a release nobody helped"
            )

    @pytest.mark.parametrize(
        "existing, created",
        [((), "true"), ((TAG,), "false")],
        ids=["created", "already there"],
    )
    def test_the_job_says_whether_it_created_the_release(
        self, monkeypatch, tmp_path, existing, created
    ):
        """S4 (#718). `created` goes to `$GITHUB_OUTPUT`: `true` after the
        release is created, `false` where one was already at the tag, so the seal
        job, which edits the note, runs only on a note this run wrote. Seen red
        against the `main` that wrote nothing."""
        out = tmp_path / "github_output"
        mod, _ = wire(
            monkeypatch,
            tmp_path,
            message=title_line(),
            existing=existing,
            GITHUB_OUTPUT=str(out),
        )
        assert mod.main() == 0
        assert out.read_text(encoding="utf-8") == f"created={created}\n"

    def test_without_an_output_file_nothing_is_written_and_nothing_raises(
        self, monkeypatch, tmp_path, capsys
    ):
        """S4. On a laptop there is no `$GITHUB_OUTPUT`: nothing is written. Where
        the file cannot be written, that is printed and ignored, and the release
        is still published with exit 0."""
        mod, tracker = wire(monkeypatch, tmp_path, message=title_line())
        assert mod.main() == 0
        assert len(tracker.creates()) == 1
        assert not (tmp_path / "github_output").exists()
        blocked = tmp_path / "a-directory"
        blocked.mkdir()
        mod, tracker = wire(
            monkeypatch, tmp_path, message=title_line(), GITHUB_OUTPUT=str(blocked)
        )
        assert mod.main() == 0
        assert len(tracker.creates()) == 1
        assert "could not write created=true" in capsys.readouterr().out


class Test_module:
    def test_the_title_line_pattern_is_linear_in_the_line(self):
        """#941's round 3 met a pattern that backtracked exponentially; the
        title line's pattern repeats, so a long line is read inside the bound,
        which is far above the linear time (under 0.1 s) and far below a
        backtracking one (no end), so a loaded runner does not fail it."""
        import time

        mod = module(SCRIPT, "publish_release_note_for_its_pattern")
        start = time.monotonic()
        for line in (
            f"release: {VERSION} symptoms: " + "x " * 50000,
            f"release: {VERSION} symptoms: " + "x" * 100000,
            " \t" * 50000 + "Release",
            f"release: {VERSION} symptoms:" + " " * 100000,
            "release: " * 20000,
        ):
            mod.title_from(line, VERSION, TAG)
        assert time.monotonic() - start < 5.0

    def test_the_list_is_read_from_the_release_branch(self, monkeypatch, capsys):
        """The set is the pull requests merged into `release/vX.Y.Z` — the base
        every feature branch squashes into — and a failed `gh` call is None,
        with the log saying what the note is instead (#1053: the theme line
        and the fragments)."""
        mod = publisher()
        seen = []

        def fake(args, **_):
            seen.append(args)
            return Done(0, '[{"number": 1, "title": "t", "author": {"login": "x"}}]')

        monkeypatch.setattr(mod.subprocess, "run", fake)
        assert mod.merged_pulls(REPO, VERSION)[0]["number"] == 1
        args = seen[0]
        assert args[args.index("--base") + 1] == f"release/v{VERSION}"
        assert "body" in args[args.index("--json") + 1].split(","), (
            "the body is not fetched, so no line can say which issues it closed"
        )
        # #718: the seal reads the capped label and the head branch from the same
        # call, so the list is fetched once for the note and the seal alike.
        fields = args[args.index("--json") + 1].split(",")
        assert "labels" in fields and "headRefName" in fields, fields
        assert args[args.index("--state") + 1] == "merged"
        assert args[args.index("--repo") + 1] == REPO

        monkeypatch.setattr(
            mod.subprocess, "run", lambda args, **_: Done(1, err="HTTP 502")
        )
        assert mod.merged_pulls(REPO, VERSION) is None
        out = capsys.readouterr().out
        assert "the note is the theme line and the fragments alone" in out, out

    def test_the_glance_block_is_built_by_one_function_and_its_sealed_twin_by_another(
        self, monkeypatch, tmp_path
    ):
        """S1's shape (#718). The note's glance block is exactly `glance`'s, so
        the seal can find it by the same function; `sealed_glance` is the heading,
        the image, a blank line and one line carrying every row the table had, in
        its order. Since #832 the image is an `<img>` carrying its display
        width, because the PNG is drawn at twice that size for a high-density
        screen and Markdown's image syntax has no width; and the alt text and
        the URL are escaped for the attribute they sit in, so a quote cannot end
        it early. Seen red against the Markdown image, and by the escape
        removed."""
        mod, body = published(monkeypatch, tmp_path, RELEASE)
        work, closed, people = mod.tally(RELEASE, OWNER)
        block = mod.glance(work, closed, people)
        assert body.startswith(block + "\n\n### ✨ Features"), body[:400]
        assert mod.sealed_glance(
            "https://example.com/seal.png", "a seal", 160, work, closed, people
        ) == (
            f"{mod.GLANCE_HEADING}\n\n"
            '<img src="https://example.com/seal.png" alt="a seal" width="160">\n\n'
            "\U0001f500 Pull requests **7** · ✅ Issues closed **4** · \U0001f64c Outside contributors **2**"
        )
        alone = [pull(10, OWNER, "fix: one", "Closes #100")]
        work, closed, people = mod.tally(alone, OWNER)
        assert mod.sealed_glance("u", "a", 160, work, closed, people).endswith(
            "\U0001f500 Pull requests **1** · ✅ Issues closed **1**"
        )
        odd = mod.sealed_glance('u?a=1&b="2"', 'a "seal" <b>', 80, work, closed, people)
        assert (
            '<img src="u?a=1&amp;b=&quot;2&quot;" alt="a &quot;seal&quot; &lt;b&gt;" '
            'width="80">'
        ) in odd, odd

    @pytest.mark.parametrize(
        "description, theme",
        [
            pytest.param(
                "Purpose: the notes come from the fragments. Order: x",
                "The notes come from the fragments.",
                id="the Purpose label left out",
            ),
            pytest.param(
                "the notes come once. Then twice.",
                "The notes come once.",
                id="no label",
            ),
            pytest.param(
                "Purpose: a first line\nthat goes on. Then.",
                "A first line",
                id="the line ends first",
            ),
            pytest.param(
                "Purpose: what 0.18.0 left. Then.",
                "What 0.18.0 left.",
                id="a version inside the sentence",
            ),
            pytest.param(
                "Purpose:   the  notes\tcome.",
                "The notes come.",
                id="whitespace collapsed",
            ),
            pytest.param("no full stop at all", "No full stop at all", id="no stop"),
        ],
    )
    def test_the_theme_is_the_descriptions_first_sentence(self, description, theme):
        """S3 of #1053. The sentence runs to the first `.` followed by
        whitespace or the end, or to the first line end where that comes first;
        a leading `Purpose:` is left out, the whitespace is collapsed and the
        first letter is upper-cased."""
        assert publisher().theme_of(description) == theme

    def test_the_previous_tag_is_the_highest_version_on_the_first_parent(
        self, tmp_path, monkeypatch
    ):
        """S6 of #1053. Tags that are not `vX.Y.Z` are passed over, a version
        tag the tagged merge brings in through its second parent is passed over, the
        highest is taken by number rather than by spelling, and with none the
        range is the whole history up to the tag."""
        repo = git_repo(tmp_path / "repo")
        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        git_out(repo, "tag", "v0.9.0")
        write(repo, "a.txt", "a\n")
        commit_everything(repo, "a")
        git_out(repo, "tag", "v0.10.0")
        git_out(repo, "tag", "vnext")
        git_out(repo, "tag", "v0.11")
        git_out(repo, "switch", "-q", "-c", "aside")
        write(repo, "b.txt", "b\n")
        commit_everything(repo, "b")
        git_out(repo, "tag", "v0.12.0")
        git_out(repo, "switch", "-q", "-")
        # The tagged commit merges `aside`, so `v0.12.0` is merged into the tag
        # and not into its first parent.
        git_out(repo, "merge", "-q", "--no-ff", "-m", "c", "aside")
        git_out(repo, "tag", "v0.11.0")
        assert mod.previous_tag("v0.11.0") == "v0.10.0"
        assert mod.commit_range("v0.10.0", "v0.11.0") == "v0.10.0..v0.11.0"

        bare = git_repo(tmp_path / "bare")
        write(bare, "a.txt", "a\n")
        commit_everything(bare, "a")
        git_out(bare, "tag", "v0.1.0")
        monkeypatch.setattr(mod, "ROOT", str(bare))
        assert mod.previous_tag("v0.1.0") is None
        assert mod.commit_range(None, "v0.1.0") == "v0.1.0"

    def test_a_fragment_the_settle_removed_reaches_a_note_tagged_on_a_merge(
        self, tmp_path, monkeypatch
    ):
        """The release's shape: the tag is the `--no-ff` merge of the release
        branch into `main`, whose first parent never held the fragment, and the
        settle removed it on the release branch (0.22.4). A fragment of the
        release before, restored by a commit in the range, is not read again
        (0.15.3). Round 1 of #1053, finding 1."""
        repo = git_repo(tmp_path / "repo")
        thread = "seal/threads/{}/changelog.md"
        write(repo, thread.format("1700000000-older"), "- older entry\n")
        commit_everything(repo, "the release before")
        git_out(repo, "tag", PREVIOUS)
        git_out(repo, "switch", "-q", "-c", "release")
        write(repo, thread.format("1700000001-first"), "- first entry\n")
        commit_everything(repo, "the work item")
        git_out(repo, "rm", "-q", "-r", "seal/threads/1700000001-first")
        git_out(repo, "rm", "-q", "-r", "seal/threads/1700000000-older")
        commit_everything(repo, "the settle")
        write(repo, thread.format("1700000000-older"), "- older entry\n")
        commit_everything(repo, "a directory restored")
        git_out(repo, "switch", "-q", "-")
        git_out(repo, "merge", "-q", "--no-ff", "-m", "the release", "release")
        git_out(repo, "tag", TAG)
        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        revisions = mod.commit_range(mod.previous_tag(TAG), TAG)
        assert mod.fragments(revisions) == [("1700000001-first", "- first entry")]


test_census = census_case(TARGET)
