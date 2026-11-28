"""`.github/scripts/publish_release_note.py`, one class per function.

#386: the release note publishes itself, or the job goes red saying why.
Publishing a GitHub Release was a habit and nothing else, and three
consecutive releases skipped it. The repair is a workflow the push to `main`
that ships a release fires, and a tag pushed by hand (#1117):

  A1  the changelog fragments the release's commits added, less those the
      previous tag holds, become the release note at that tag, each under a
      link to the pull request that added it (#1139)
  A2  a release already at the tag is left exactly as it is, exit 0
  A3  a tag whose range added no fragment the previous tag does not hold, and
      carries more than settles, goes RED, naming the range's tags and each
      commit of the range that is no settle
  A4  the title is read from the `release: X.Y.Z symptoms: <symptoms>` line,
      and where no such line is readable it is the tag name and the log says
      which was used, what it expected and what it found
  A5  the note is a summary read from the release's pull requests -- a
      header of its counts, one fold per type under its name and count
      holding one line per change with the issues it closed (#1153), every
      outside contributor thanked by handle -- over the fragments, folded;
      with no pull request to read it is the fragments alone (#572)
  A6  a range of settles alone, each commit other than a merge removing
      whole a work item directory that stood at its parent, is noted from
      the body of the release pull request whose merge commit is the tag,
      in the place the fragments take, and goes RED where that body cannot
      be read (#1655)

#1053 removed the gathered release files, so the fragments are read from the
history at the tag (S1, S5, S6), and the note carries the release's theme
under its header (#1153). Since #1671 no milestone names a release, so the
theme is the first sentence of the body of the release pull request whose
merge commit the tag names, and a note of settles alone carries none (S10).
The summary's pull requests are the ones whose `(#N)` ends a subject of the
tag's range (S9).

**Nothing here reaches GitHub.** `Releases` stands in for `subprocess.run`
under `lib/gitcmd.py`, so every git and `gh` command the script starts
reaches it with the argv the runner built, and `release_exists` is replaced
by it too. It records the calls as argument tuples, in order, so a case can
assert about a write that did NOT happen as well as one that did. The cases
that read the history drive a real `git` repository in `tmp_path`.

#942's phase 6 placed these cases from
`tests/behaviour/test_a_release_publishes_its_note.py`, which keeps the cases that
read the workflow.
"""

import html.parser
import importlib.util
import json
import os
import re
import urllib.parse

import cmarkgfm
import pytest
from cmarkgfm.cmark import Options
from conftest import (
    ROOT,
    census_case,
    commit_everything,
    git_out,
    git_repo,
    write,
)
from test_settle import unanswered

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

# The fragments the release's commits added, as `fragments` returns them:
# the work item, the fragment, and the pull request its adding commit names.
ENTRIES = [("1700000000-a-work-item", NOTES, 42)]
# The line the note writes above that fragment.
LINK = f"[#42](https://github.com/{REPO}/pull/42)"
# A release pull request's body, which a range of settles alone is noted
# from, and what `release_pull_body` says of where it came from.
RELEASE_BODY = "## What changed\n\n- **A settle closed two work items.** Nothing else."
FROM_RELEASE_PULL = "the body of the release pull request #500"


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


class Releases:
    """The releases a repository has, and every command the script ran.

    It stands in for `subprocess.run` under `lib/gitcmd.py`. `calls` holds
    each command as the program and the arguments the script passed,
    without `lib/gitcmd.py#argv`'s `-c` pairs and `-C <root>` or the path
    `shutil.which` found for `gh`, in order, so a case can ask about
    absence — which is what A2 is entirely about. A command it was not
    built for, a milestone read among them, fails the case.
    """

    def __init__(self, existing=()):
        self.existing = set(existing)
        self.calls = []

    def exists(self, repo, tag):
        return tag in self.existing

    def __call__(self, argv, **_):
        held = list(argv)
        if "-C" in held:
            args = ("git", *held[held.index("-C") + 2 :])
        else:
            args = ("gh", *held[1:])
        self.calls.append(args)
        if args[:3] == ("gh", "release", "create"):
            self.existing.add(args[3])
            return Done(0)
        if args[0] == "git" and "log" in args and "--format=%B" in args:
            return Done(0, self.message)
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
    settles=(False, ()),
    release_pull=(None, "no release pull request was read"),
    **env,
):
    """The script, with fixture fragments and no route to GitHub. `entries`
    are the fragments the range added, read after `PREVIOUS`; `pulls` is
    what `merged_pulls` returns, and `tracker.listed` holds each range it
    was asked for. `settles` is what `settles` reads of the range, and
    `release_pull` what `release_pull_body` returns; `tracker.asked` holds
    each call of the two, in order."""
    mod = publisher()
    tracker = Releases(existing)
    tracker.message = message
    tracker.asked, tracker.listed = [], []

    def pulls_reading(repo, revisions):
        tracker.listed.append((repo, revisions))
        return None if pulls is None else list(pulls)

    def settle_reading(revisions):
        tracker.asked.append(("settles", revisions))
        return settles[0], list(settles[1])

    def release_reading(repo, tag):
        tracker.asked.append(("release_pull_body", repo, tag))
        return release_pull

    monkeypatch.setattr(mod, "merged_pulls", pulls_reading)
    monkeypatch.setattr(mod, "settles", settle_reading)
    monkeypatch.setattr(mod, "release_pull_body", release_reading)
    monkeypatch.setattr(mod, "ROOT", str(tmp_path))
    monkeypatch.setattr(mod, "release_exists", tracker.exists)
    monkeypatch.setattr(mod, "previous_tag", lambda tag: PREVIOUS)
    monkeypatch.setattr(mod, "fragments", lambda revisions: list(entries))
    monkeypatch.setattr(mod.gitcmd.subprocess, "run", tracker)
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


# `RELEASE`'s pull request lines, under the summary of the fold each lands
# in, in the order the note reads in.
FOLDED = [
    ("✨ Features (1)", ["- A third (#15) · closes #100 — thanks @another"]),
    (
        "\U0001f41b Fixes (2)",
        [
            "- The owner's own change (#10) · closes #100, #101",
            "- And a second thing (#14) · closes #103 — thanks @someone",
        ],
    ),
    (
        "\U0001f4da Docs (1)",
        ["- Explain a thing (#11) · closes #102 — thanks @someone"],
    ),
    ("\U0001f9f9 Chores (2)", ["- Bump (#12)", "- Bump again (#13)"]),
    ("\U0001f4e6 Other (1)", ["- An untyped title (#16)"]),
]


def header(*lines):
    """A note's header holding `lines` in one paragraph on one line, parted
    by `<br>`, exactly as the note carries it (#1496)."""
    return f"<p>{'<br>'.join(lines)}</p>"


# The header `publish` writes for `RELEASE`: seven pull requests, four
# distinct issues closed (#100 twice counts once), and two outside people
# however many pull requests they made.
HEADER = header("7 pull requests merged", "4 issues closed", "2 outside contributors")

# The address the marked header's badges are drawn from (#1299).
BADGES = "https://img.shields.io/badge/"
# A badge's two colours by its label, as `(value, label)` (#1496): the wax seal's
# reds for `CLEARED`, green for the suite's passed count, grey for the
# skipped, capped and deferred counts, and a blue value beside a grey label
# for every other.
MARK_RED = ("d42420", "8e0c12")
GREEN = ("2ea44f", "555555")
GREY = ("6e7781", "555555")
BLUE = ("0969da", "555555")


def badge(path, alt, colours=BLUE):
    """One badge exactly as the marked header carries it: `path` is the
    label and the value as the address spells them, `alt` the escaped text
    a reader whose client draws no image reads in its place, and `colours`
    the value's colour and the label's."""
    colour, edge = colours
    return f'<img src="{BADGES}{path}-{colour}?labelColor={edge}" alt="{alt}">'


# `marked_header`'s results as `release_mark.py#results` hands them (#1299):
# badge lines, each a list of `(label, value)` pairs.
CLEARED = [[("CLEARED", "v1.2.3")], [("commit", "aaa11111"), ("on", "main")]]
RESULTS = [[("suite", "5 passed"), ("skipped", "0")], [("capped", "not read")]]
# The badge lines `marked_header` builds from them for `RELEASE`, parted by
# `<br>`: the cleared part, the counts `header` states as badges, then the
# results.
BADGE_LINES = "<br>".join(
    [
        badge("CLEARED-v1.2.3", "CLEARED: v1.2.3", MARK_RED),
        badge("commit-aaa11111", "commit: aaa11111")
        + " "
        + badge("on-main", "on: main"),
        badge("pull%20requests-7%20merged", "pull requests: 7 merged"),
        badge("issues-4%20closed", "issues: 4 closed"),
        badge("outside%20contributors-2", "outside contributors: 2"),
        badge("suite-5%20passed", "suite: 5 passed", GREEN)
        + " "
        + badge("skipped-0", "skipped: 0", GREY),
        badge("capped-not%20read", "capped: not read", GREY),
    ]
)


def fold(summary, lines):
    """One category's fold, exactly as the note carries it."""
    return "\n".join(
        ["<details>", f"<summary>{summary}</summary>", "", *lines, "", "</details>"]
    )


# #1293, merged into release/v0.28.0, whose title holds three `details` tags
# bare, and the text its line reads as on the page.
PR_1293 = pull(
    1293,
    OWNER,
    "fix: agentic pr-body refused only an exact <details> or </details> line, "
    "and GitHub ends the fold at one inside a sentence, indented or in "
    "capitals, and nests a second at <details open>",
)
TEXT_1293 = (
    "Agentic pr-body refused only an exact <details> or </details> line, and "
    "GitHub ends the fold at one inside a sentence, indented or in capitals, "
    "and nests a second at <details open> (#1293)"
)


class Folds(html.parser.HTMLParser):
    """Each `details` element in rendered HTML, as `(summary, [list item
    texts])`, in the order each closes, the texts as a reader sees them."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.folds, self.open, self.text = [], [], None

    def handle_starttag(self, tag, attrs):
        if tag == "details":
            self.open.append(["", []])
        elif tag in ("summary", "li") and self.open:
            self.text = []

    def handle_endtag(self, tag):
        if tag in ("summary", "li") and self.open and self.text is not None:
            said = "".join(self.text).strip()
            if tag == "summary":
                self.open[-1][0] = said
            else:
                self.open[-1][1].append(said)
            self.text = None
        elif tag == "details" and self.open:
            self.folds.append(tuple(self.open.pop()))

    def handle_data(self, data):
        if self.text is not None:
            self.text.append(data)


def folds_read(body):
    """The `details` elements of `body` as GitHub renders a release note:
    cmark-gfm, the renderer the suite pins
    (`tests/requirements.txt`), with raw HTML kept."""
    reader = Folds()
    reader.feed(
        cmarkgfm.github_flavored_markdown_to_html(
            body, options=Options.CMARK_OPT_UNSAFE
        )
    )
    reader.close()
    return reader.folds


class Test_main:
    def test_accepts_the_releases_fragments_as_the_release_note(
        self, monkeypatch, tmp_path, capsys
    ):
        """A1. The body is the fragments the release's commits added, less those
        the previous tag holds, each under a link to the pull request that
        added it, and it links to no file in the tree."""
        mod, tracker = wire(monkeypatch, tmp_path, message=title_line())
        assert mod.main() == 0
        created = tracker.creates()
        assert len(created) == 1, tracker.calls
        args = created[0]
        assert args[3] == TAG
        body = args[args.index("--notes") + 1]
        assert f"{LINK}\n{NOTES}" in body, body
        assert "changelog/" not in body, "the note still names a gathered file"
        assert "published the release" in capsys.readouterr().out
        # S5 of #1655: a range that added a fragment is noted from it, and
        # the settle reading is not asked. The release pull request is asked
        # once, for the theme alone (S10 of #1671).
        assert tracker.asked == [("release_pull_body", REPO, TAG)], tracker.asked
        # S9 of #1671: the summary's pull requests are read from the range
        # the fragments are read from.
        assert tracker.listed == [(REPO, f"{PREVIOUS}..{TAG}")], tracker.listed

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
        thread = "agentory/threads/{}/changelog.md"
        write(repo, thread.format("1700000000-older"), "- older entry\n")
        commit_everything(repo, "the release before")
        git_out(repo, "tag", PREVIOUS)
        write(repo, thread.format("1700000002-second"), "- second entry\n")
        commit_everything(repo, "the later work item (#2)")
        write(repo, thread.format("1700000001-first"), "- first entry\n")
        commit_everything(repo, "the earlier work item (#1)")
        write(repo, thread.format("1700000001-first"), "- first entry, revised\n")
        write(repo, thread.format("1700000000-older"), "- older entry, edited\n")
        commit_everything(repo, "a fix brings its fragment along")
        git_out(repo, "rm", "-q", "-r", "agentory/threads/1700000001-first")
        git_out(repo, "rm", "-q", "-r", "agentory/threads/1700000000-older")
        # Added in the settle's own commit with the removed fragment's text,
        # so only `--no-renames` keeps it from reading as a rename.
        write(repo, thread.format("1700000003-third"), "- first entry, revised\n")
        write(repo, thread.format("1700000004-empty"), "\n  \n")
        commit_everything(repo, "the settle (#3)")
        git_out(repo, "tag", TAG)

        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        monkeypatch.chdir(repo)
        monkeypatch.setattr(mod, "release_exists", lambda repo, tag: False)
        monkeypatch.setattr(mod, "merged_pulls", lambda repo, revisions: None)
        monkeypatch.setattr(mod, "release_pull_body", lambda repo, tag: (None, "none"))
        monkeypatch.setenv("TAG", TAG)
        monkeypatch.setenv("REPO", REPO)
        monkeypatch.setenv("DRY_RUN", "1")
        assert mod.main() == 0
        out = capsys.readouterr().out
        pulls = f"https://github.com/{REPO}/pull"
        first = f"[#1]({pulls}/1)\n- first entry, revised"
        second = f"[#2]({pulls}/2)\n- second entry"
        third = f"[#3]({pulls}/3)\n- first entry, revised"
        assert first in out and second in out and third in out, out
        assert out.index(first) < out.index(second) < out.index(third), (
            "the fragments are not in id order"
        )
        assert "1700000004-empty" not in out, "an empty fragment became an entry"
        assert "older entry" not in out, "a fragment of the release before reached it"
        assert "changelog/" not in out, out

    def test_each_entry_links_the_pull_request_that_added_it(
        self, monkeypatch, tmp_path, capsys
    ):
        """S1, S2 and S3 of #1139. The entry's first line links the pull
        request whose number ends the subject of the range's commit that added
        the fragment, in the `REPO` the note is built for. A later commit that
        edits the fragment, or adds it again after a removal, names no number
        for it: the oldest adding commit does. Where the subject ends with
        several `(#N)`, as a title that ends with its issue does, the last is
        the pull request. An adding commit with no `(#N)` gives the fragment's
        text alone, and no entry carries the hidden work-item marker. Driven
        through a real `git` history."""
        repo = git_repo(tmp_path / "repo")
        thread = "agentory/threads/{}/changelog.md"
        git_out(repo, "tag", PREVIOUS)
        write(repo, thread.format("1700000001-linked"), "- linked entry\n")
        commit_everything(repo, "feat: a change (#42)")
        write(repo, thread.format("1700000001-linked"), "- linked entry, revised\n")
        commit_everything(repo, "fix: a later edit (#43)")
        git_out(repo, "rm", "-q", "-r", "agentory/threads/1700000001-linked")
        commit_everything(repo, "chore: removed by mistake (#45)")
        write(repo, thread.format("1700000001-linked"), "- linked entry, revised\n")
        commit_everything(repo, "chore: restored (#46)")
        write(repo, thread.format("1700000002-titled"), "- titled entry\n")
        commit_everything(repo, "fix: a title that ends with its issue (#7) (#44)")
        write(repo, thread.format("1700000003-bare"), "- bare entry\n")
        commit_everything(repo, "a commit pushed with no pull request")
        git_out(repo, "tag", TAG)

        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        monkeypatch.chdir(repo)
        monkeypatch.setattr(mod, "release_exists", lambda repo, tag: False)
        monkeypatch.setattr(mod, "merged_pulls", lambda repo, revisions: None)
        monkeypatch.setattr(mod, "release_pull_body", lambda repo, tag: (None, "none"))
        monkeypatch.setenv("TAG", TAG)
        monkeypatch.setenv("REPO", "o/r")
        monkeypatch.setenv("DRY_RUN", "1")
        assert mod.main() == 0
        note = capsys.readouterr().out.split("characters of notes\n", 1)[1]
        assert "[#42](https://github.com/o/r/pull/42)\n- linked entry, revised" in (
            note
        ), note
        for later in ("#43", "#45", "#46"):
            assert later not in note, f"a later commit than the oldest add, {later}"
        assert "[#44](https://github.com/o/r/pull/44)\n- titled entry" in note, note
        assert "pull/7)" not in note, "the issue the title ends with was linked"
        assert "- titled entry\n\n- bare entry" in note, (
            "an adding commit that names no pull request gave its entry a line "
            f"above the fragment: {note}"
        )
        assert "<!-- specs/" not in note, note

    def test_the_theme_follows_the_notes_header(self, monkeypatch, tmp_path, capsys):
        """S10 of #1671, S2 of #1053, and #1153 S2. The line under the note's
        header is the first sentence of the body of the release pull request
        whose merge commit the tag names, the log says where it came from,
        and the first fold follows it. No milestone is read: `Releases`
        fails the case on a command it was not built for."""
        opened = "Release 1.2.3 carries the notes from the fragments. Order: S1."
        mod, tracker = wire(
            monkeypatch,
            tmp_path,
            message=title_line(),
            pulls=RELEASE,
            release_pull=(f"{opened}\n\n## What changed\n", FROM_RELEASE_PULL),
            DRY_RUN="1",
        )
        assert mod.main() == 0
        out = capsys.readouterr().out
        note = out.split("characters of notes\n", 1)[1]
        theme = "Release 1.2.3 carries the notes from the fragments."
        assert note.startswith(f"{HEADER}\n\n{theme}\n\n<details>\n"), note[:300]
        assert f"theme {theme!r}, from {FROM_RELEASE_PULL}" in out, out
        assert tracker.asked == [("release_pull_body", REPO, TAG)], tracker.asked

    @pytest.mark.parametrize(
        "said",
        [
            pytest.param(
                "the release pull request could not be listed: HTTP 502",
                id="unread",
            ),
            pytest.param(
                f"no pull request merged into main has {TAG}'s commit as its "
                "merge commit",
                id="not found",
            ),
            pytest.param("the release pull request #500 has an empty body", id="empty"),
        ],
    )
    def test_without_a_theme_the_note_has_no_theme_line_and_the_job_goes_on(
        self, monkeypatch, tmp_path, capsys, said
    ):
        """S10 of #1671, and S4 of #1053. A release pull request that cannot
        be listed, is not found or has an empty body leaves a note of
        fragments without a theme line, the job log says which of the three
        it was, and the release is published as it would have been with
        one."""
        mod, tracker = wire(
            monkeypatch,
            tmp_path,
            message=title_line(),
            pulls=RELEASE,
            release_pull=(None, said),
        )
        assert mod.main() == 0
        assert len(tracker.creates()) == 1, tracker.calls
        body = body_of(tracker)
        assert body.startswith(f"{HEADER}\n\n<details>\n"), body[:200]
        assert f"no theme line: {said}" in capsys.readouterr().out

    @pytest.mark.parametrize(
        "kw",
        [
            pytest.param({}, id="fragments"),
            pytest.param(
                {
                    "entries": [],
                    "settles": (True, ()),
                    "release_pull": (RELEASE_BODY, ""),
                },
                id="settles alone",
            ),
        ],
    )
    def test_an_existing_release_is_left_exactly_as_it_is(
        self, monkeypatch, tmp_path, capsys, kw
    ):
        """A2. A re-pushed tag and a re-run job both land here. The note may have
        been edited by hand after publication, so the only safe act is none.
        A range of settles alone meets the same guard before its release pull
        request is read (#1655)."""
        mod, tracker = wire(
            monkeypatch, tmp_path, message=title_line(), existing=(TAG,), **kw
        )
        assert mod.main() == 0
        assert tracker.calls == [], (
            "something ran against GitHub for a release that already exists"
        )
        assert not [a for a in tracker.asked if a[0] == "release_pull_body"], (
            "the release pull request was read for a release that already exists"
        )
        assert "already exists" in capsys.readouterr().out

    @pytest.mark.parametrize(
        "unsettled",
        [
            pytest.param((), id="no commit but merges"),
            pytest.param(
                (("abc1234", "fix: a change"), ("def5678", "docs: a sentence")),
                id="commits that are no settle",
            ),
        ],
    )
    def test_refuses_a_tag_whose_range_added_no_fragment(
        self, monkeypatch, tmp_path, capsys, unsettled
    ):
        """A3, and S5 of #1053. This is the release shipping unexplained, and the
        body is the whole of what the job publishes — so it is the one direction
        that fails. The message names both tags of the range it read, and says
        a fragment the previous tag holds is not counted (round 2 of #1053).
        A range that holds no commit but merges, or a commit that is no settle,
        is not a range of settles alone, and the log names each such commit
        by its short hash and subject (S2 of #1655). Seen red against the
        script before #1655 on the naming, which it did not print."""
        mod, tracker = wire(
            monkeypatch,
            tmp_path,
            entries=[],
            message=title_line(),
            settles=(bool(unsettled), unsettled),
        )
        assert mod.main() == 1
        assert tracker.creates() == [], "it published a release with no notes"
        assert not [a for a in tracker.asked if a[0] == "release_pull_body"]
        out = capsys.readouterr().out
        for short, subject in unsettled:
            assert f"{short} {subject} is no settle" in out, out
        assert PREVIOUS in out and TAG in out, (
            "the message does not name the range it read, so the job log does "
            "not say what to fix"
        )
        assert "changelog.md" in out, "the message does not name what it looked for"
        # The refusal the publish job prints, which the person reading the
        # job log acts on: a fragment the previous tag holds is not counted.
        assert f"that {PREVIOUS} does not already hold" in out, out

    def test_a_tag_that_is_not_a_version_goes_red(self, monkeypatch, tmp_path, capsys):
        """A3's neighbour. `v*` matches `vnext` too, and a tag this cannot name a
        version for has no section to look for — so it says so instead of
        guessing one."""
        mod, tracker = wire(monkeypatch, tmp_path, TAG="vnext")
        assert mod.main() == 1
        assert tracker.calls == []
        assert "not a vX.Y.Z tag" in capsys.readouterr().out

    def test_the_title_is_the_line_the_checklist_prescribes(
        self, monkeypatch, tmp_path, capsys
    ):
        """A4, first branch, and S15 of #1000. `docs/releasing/release-checklist.md`
        *The release pull request*
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

    def test_each_type_is_a_fold_under_its_name_and_count(self, monkeypatch, tmp_path):
        """A5 and #1153 S1. The list is a partition of the release: every pull
        request lands in exactly one fold, an unknown or missing type in
        Other's, and each line names the issues its body closes -- read the
        way the closer reads them, so a quoted keyword closes nothing. A
        fold's summary is its type's name and the number of pull requests in
        it; its tags stand on lines of their own, with a blank line after the
        summary and before the closing tag; one blank line parts two folds;
        and the folds follow in the order the note is meant to read in. No
        `### ` line names a type. Seen red against the renderer that wrote a
        `### ` heading over each type's lines."""
        mod, body = published(monkeypatch, tmp_path, RELEASE)
        folds = "\n\n".join(fold(summary, lines) for summary, lines in FOLDED)
        assert f"\n\n{folds}\n\n" in body, body
        names = {heading for _, heading in mod.TYPES} | {mod.OTHER}
        headed = [s for s in body.splitlines() if s[:4] == "### " and s[4:] in names]
        assert headed == [], "a type is still a heading over its lines"
        assert "#999" not in body, "a keyword inside a code span was read as a claim"

    def test_github_reads_each_fold_as_one_element_holding_its_lines(
        self, monkeypatch, tmp_path
    ):
        """#1153 S1, read the way GitHub reads it. Rendered as a release note
        is rendered, each fold is one `details` element whose summary is its
        name and count and which holds its own pull request lines as list
        items, and the full changelog's fold follows them. A title quoting a
        closing `details` tag in a code span is text, and stays in its fold,
        and so is #1293's title, which holds three `details` tags bare. Seen
        red against the renderer that wrote a `### ` heading over each type's
        lines, with the blank line after a fold's summary taken out, which
        leaves the fold's lines raw HTML and no list, and with #1293's title
        written as it is, whose tags the reader then met as folds."""
        quoting = pull(17, OWNER, "fix: a title quoting `</details>`")
        mod, body = published(monkeypatch, tmp_path, [*RELEASE, quoting, PR_1293])
        read = [(summary, [line[2:] for line in lines]) for summary, lines in FOLDED]
        fixes = [*read[1][1], "A title quoting </details> (#17)", TEXT_1293]
        read[1] = ("\U0001f41b Fixes (4)", fixes)
        changelog = (mod.FULL_SUMMARY, [NOTES.replace("**", "")[2:]])
        assert folds_read(body) == [*read, changelog]

    @pytest.mark.parametrize("tag", ["<details>", "</details>"])
    def test_a_bare_tag_in_a_title_is_written_as_text(self, monkeypatch, tmp_path, tag):
        """#1153 S1, round 1's finding 1. A title holding a bare `details`
        tag alone, opening or closing, reaches its fold's line and the thanks
        line with its `<` written `&lt;`, so the page shows the tag and the
        fold holds the line whole, with the full changelog's fold after it.
        Seen red against the renderer that wrote the title as it is, and
        again with only the escape removed."""
        title = f"fix: a bare {tag} in a title"
        mod, body = published(monkeypatch, tmp_path, [pull(20, "outsider", title)])
        shown = f"A bare {tag.replace('<', '&lt;')} in a title"
        assert f"\n- {shown} (#20) — thanks @outsider\n" in body, body
        assert f"\n- **@outsider** — {shown} (#20)\n" in body, body
        assert folds_read(body) == [
            (
                "\U0001f41b Fixes (1)",
                [f"A bare {tag} in a title (#20) — thanks @outsider"],
            ),
            (mod.FULL_SUMMARY, [NOTES.replace("**", "")[2:]]),
        ]

    def test_the_note_opens_with_a_header_of_its_counts(self, monkeypatch, tmp_path):
        """A5, #1153 S2 and #1496 S1. The note opens with one paragraph on
        one line holding the release's counts in words, parted by `<br>` --
        seven changes, four distinct issues closed, two outside people --
        then the theme and the first fold. A release of one pull request
        closing one issue says each in the singular, and has no
        contributors' line. No glance heading or table is left, and the note
        holds no HTML table, because GitHub draws a border around every
        cell of one. Seen red against the note that opened with the theme
        and carried the glance table under it, and against the header that
        was a table of one cell."""
        theme = ("A theme. And more.", FROM_RELEASE_PULL)
        _, body = published(monkeypatch, tmp_path, RELEASE, release_pull=theme)
        assert body.startswith(f"{HEADER}\n\nA theme.\n\n{fold(*FOLDED[0])}\n\n"), body
        assert "At a glance" not in body, body
        assert "<table>" not in body, body[:400]
        alone = [pull(10, OWNER, "fix: one", "Closes #100")]
        _, body = published(monkeypatch, tmp_path, alone)
        one = header("1 pull request merged", "1 issue closed")
        assert body.startswith(f"{one}\n\n<details>\n"), body

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
        the link to its pull request, or alone where its adding commit names
        none, with a blank line before the next (#1053: no link to a file
        follows)."""
        entries = [*ENTRIES, ("1700000001-b", "- b", None)]
        mod, body = published(monkeypatch, tmp_path, RELEASE, entries=entries)
        opens = body.index(f"<details>\n<summary>{mod.FULL_SUMMARY}</summary>")
        fold = body[opens:]
        assert fold == (
            f"<details>\n<summary>{mod.FULL_SUMMARY}</summary>\n\n"
            f"{LINK}\n{NOTES}\n\n- b\n\n</details>"
        ), fold
        assert body.index(mod.UPDATE_HEADING) < opens
        assert "/agentic:update" in body

    def test_a_release_with_no_outside_contribution_thanks_nobody(
        self, monkeypatch, tmp_path
    ):
        """A5, the other direction. Most releases carry only the owner's work:
        the summary is there, and no credit line or count is invented."""
        mod, body = published(monkeypatch, tmp_path, [pull(10, OWNER, "fix: a thing")])
        assert mod.THANKS_HEADING not in body
        assert "outside contributor" not in body
        assert "thanks @" not in body

    @pytest.mark.parametrize(
        "pulls",
        [
            pytest.param(None, id="the list could not be read"),
            pytest.param([], id="no pull request"),
        ],
    )
    def test_with_nothing_to_summarise_the_note_is_the_theme_and_the_fragments(
        self, monkeypatch, tmp_path, capsys, pulls
    ):
        """A5 adds no way to fail the tag's job: a summary that cannot be built
        leaves the note the theme line and the fragments, unfolded, as the
        section alone was before #572."""
        theme = ("A theme. And more.", FROM_RELEASE_PULL)
        _, body = published(monkeypatch, tmp_path, pulls, release_pull=theme)
        assert body == f"A theme.\n\n{LINK}\n{NOTES}"
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
        release is created, `false` where one was already at the tag, so the mark
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

    def test_a_range_of_settles_alone_is_noted_from_the_release_pull_request(
        self, monkeypatch, tmp_path, capsys
    ):
        """A6, S1 of #1655. A settle writes no fragment, so a range of settles
        alone carries the release pull request's body in the place the
        fragments take: the note opens with the header the mark finds,
        exactly once, and the body stands inside the fold that ends it. The
        title, the release and `created=true` are any note's. No theme line
        stands above the folds, since the body below them is the note's
        whole text (S10 of #1671). Seen red against the script before #1655,
        where `main` returned 1."""
        out = tmp_path / "github_output"
        mod, tracker = wire(
            monkeypatch,
            tmp_path,
            entries=[],
            message=title_line(),
            pulls=RELEASE,
            settles=(True, ()),
            release_pull=(RELEASE_BODY, FROM_RELEASE_PULL),
            GITHUB_OUTPUT=str(out),
        )
        assert mod.main() == 0
        created = tracker.creates()
        assert len(created) == 1, tracker.calls
        args = created[0]
        assert args[args.index("--title") + 1] == f"{VERSION} — {SYMPTOMS}"
        body = args[args.index("--notes") + 1]
        assert body.startswith(f"{HEADER}\n\n<details>\n"), body[:200]
        assert body.count(HEADER) == 1, body
        assert body.endswith(
            f"<details>\n<summary>{mod.FULL_SUMMARY}</summary>\n\n"
            f"{RELEASE_BODY}\n\n</details>"
        ), body
        assert out.read_text(encoding="utf-8") == "created=true\n"
        assert tracker.asked == [
            ("settles", f"{PREVIOUS}..{TAG}"),
            ("release_pull_body", REPO, TAG),
        ], tracker.asked
        said = capsys.readouterr().out
        assert f"the note carries {FROM_RELEASE_PULL}" in said, said
        assert "no theme line: a note of settles alone" in said, said

    def test_a_range_of_settles_alone_with_no_release_pull_request_goes_red(
        self, monkeypatch, tmp_path, capsys
    ):
        """A6, S4 of #1655. Without the release pull request's body a range
        of settles alone has no text to publish, so the job goes red with
        the line `release_pull_body` gave, creates nothing and writes no
        `created`. Seen red against the script before #1655 on that line,
        which it did not print."""
        out = tmp_path / "github_output"
        said = "no pull request merged into main is the tag"
        mod, tracker = wire(
            monkeypatch,
            tmp_path,
            entries=[],
            message=title_line(),
            settles=(True, ()),
            release_pull=(None, said),
            GITHUB_OUTPUT=str(out),
        )
        assert mod.main() == 1
        assert tracker.creates() == [], tracker.calls
        assert said in capsys.readouterr().out
        assert not out.exists()


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

    def test_the_list_is_the_pull_requests_the_range_names(
        self, tmp_path, monkeypatch, capsys
    ):
        """S9 of #1671, on a real history. The set is the pull requests
        whose `(#N)` ends a subject of the range, the last where a title
        ends with its issue, each once, in number order. The range bounds
        it, so a pull request squashed before the range's lower tag is not
        in it, and no branch is named. Each is asked of `gh pr view` once,
        for the fields the note and the mark read (#718: the mark reads the
        capped label and the head branch from the same set). A failed call,
        and an answer that is not JSON, make the set None, with the log
        saying what the note is instead (#1053, #1655)."""
        repo = git_repo(tmp_path / "repo")
        write(repo, "a.txt", "a\n")
        commit_everything(repo, "fix: before the range (#10)")
        git_out(repo, "tag", PREVIOUS)
        for n, subject in enumerate(
            (
                "feat: a change (#12)",
                "fix: a title that ends with its issue (#7) (#11)",
                "a commit pushed with no pull request",
                "Merge pull request #500 from owner/release/next",
                "Revert a change, named twice (#12)",
            )
        ):
            write(repo, "a.txt", f"{n}\n")
            commit_everything(repo, subject)
        git_out(repo, "tag", TAG)
        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        real, viewed = mod.gitcmd.subprocess.run, []

        def answered(code=0, out=None):
            def run(argv, *args, **kwargs):
                if "-C" in list(argv):
                    return real(argv, *args, **kwargs)
                viewed.append(list(argv)[1:])
                number = int(argv[3])
                said = json.dumps({"number": number, "title": "t"})
                return Done(code, said if out is None else out, "HTTP 502")

            monkeypatch.setattr(mod.gitcmd.subprocess, "run", run)

        answered()
        pulls = mod.merged_pulls(REPO, f"{PREVIOUS}..{TAG}")
        assert [p["number"] for p in pulls] == [11, 12], pulls
        assert [args[:3] for args in viewed] == [
            ["pr", "view", "11"],
            ["pr", "view", "12"],
        ], viewed
        args = viewed[0]
        assert args[args.index("--repo") + 1] == REPO
        fields = args[args.index("--json") + 1].split(",")
        assert fields == ["number", "title", "author", "body", "labels", "headRefName"]
        assert "--base" not in args and "--head" not in args, args

        answered(code=1)
        assert mod.merged_pulls(REPO, f"{PREVIOUS}..{TAG}") is None
        assert capsys.readouterr().out == (
            "gh pr view 11 failed, so the note is the theme line and the "
            "fragments, or the release pull request's body, with no summary of "
            "the pull requests: HTTP 502\n"
        )

        answered(out="not json")
        assert mod.merged_pulls(REPO, f"{PREVIOUS}..{TAG}") is None
        assert capsys.readouterr().out == (
            "gh pr view 11 printed something that is not JSON, so the note is "
            "the theme line and the fragments, or the release pull request's "
            "body, with no summary of the pull requests\n"
        )

    def test_a_create_gh_refuses_stops_the_run_in_the_runners_line(self, monkeypatch):
        """A release GitHub did not create is a red job, said in
        `lib/gitcmd.py#Exited`'s line, which names the command and what `gh`
        said (#1573)."""
        mod = publisher()
        monkeypatch.setattr(
            mod.gitcmd.subprocess,
            "run",
            lambda args, **_: Done(1, err="HTTP 422: Validation Failed\n"),
        )
        with pytest.raises(SystemExit) as stopped:
            mod.create(REPO, TAG, "a title", "a body")
        said = str(stopped.value.code)
        assert said.startswith(f"`gh release create {TAG} --repo {REPO} "), said
        assert said.endswith("exited 1: HTTP 422: Validation Failed"), said

    def test_a_gh_that_gave_no_answer_is_read_as_each_read_reads_a_failure(
        self, tmp_path, monkeypatch, capsys
    ):
        """#1573. A `gh` past `lib/gitcmd.py#TIMEOUT` leaves the summary
        out, saying so in the runner's line, and stops the run where it was
        asked whether the release exists, since a release that cannot be
        looked up may be published twice. The theme's read is
        `Test_release_pull_body`'s."""
        repo = git_repo(tmp_path / "repo")
        git_out(repo, "tag", PREVIOUS)
        write(repo, "a.txt", "a\n")
        commit_everything(repo, "fix: a change (#5)")
        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        unanswered(monkeypatch, "pr", "view")
        assert mod.merged_pulls(REPO, f"{PREVIOUS}..HEAD") is None
        out = capsys.readouterr().out
        assert "gh pr view 5 failed, so the note is the theme line and the " in out
        assert "pull requests: `gh pr view 5 --repo example/repo --json " in out, out
        unanswered(monkeypatch, f"repos/{REPO}/releases/tags/{TAG}")
        with pytest.raises(SystemExit) as stopped:
            mod.release_exists(REPO, TAG)
        assert stopped.value.code == (
            f"`gh api -i repos/{REPO}/releases/tags/{TAG}` did not finish within "
            "60 seconds"
        )

    def test_a_git_read_that_fails_stops_the_run_in_the_runners_line(
        self, tmp_path, monkeypatch
    ):
        """#1573. The note's history reads stop the run where git refuses,
        with `lib/gitcmd.py#Exited`'s line naming the command and git's
        error."""
        repo = git_repo(tmp_path / "repo")
        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        with pytest.raises(SystemExit) as stopped:
            mod.commit_message("v9.9.9")
        assert str(stopped.value.code).startswith(
            "`git log -1 --format=%B v9.9.9` exited 128: fatal: "
        ), stopped.value.code
        # The settle reading's own reads stop the run the same way (#1655).
        with pytest.raises(SystemExit) as stopped:
            mod.settles("v9.9.9")
        assert str(stopped.value.code).startswith("`git log --no-merges "), (
            stopped.value.code
        )
        assert " exited 128: fatal: " in str(stopped.value.code), stopped.value.code

    def test_the_header_is_built_by_one_function_and_its_marked_twin_by_another(
        self, monkeypatch, tmp_path
    ):
        """#718's shape, #1153 S2, #1299 S1 and S3, and #1496 S2. The note's
        header is exactly `header`'s, so the mark can find it by the same
        function. `marked_header` is the same one-line paragraph: the image
        floated left, then the results as badges, one or two to a line, then
        a `<br clear="left">` that ends the float before the theme. The
        badges are the cleared version, the commit and its branch, the counts
        `header` states in its order, then the stamp's other results. Since
        #832 the image is an `<img>` carrying its display width, because the
        PNG is drawn at twice that size for a high-density screen. Each
        badge's alt text is its label and value, so a reader whose client
        draws no image reads every result in words; the whole-string
        assertion pins every alt attribute, which is #1299 S3. The image's
        URL and alt text, and each badge's alt text, are escaped, so a quote
        cannot end an attribute and a `<` opens no tag; a badge's address is
        percent-encoded and needs no escape. Seen red against the
        `marked_header` that wrote `CLEARED` in bold and the results as text,
        one per line, with the badge's alt attribute alone left out, and
        against the header that was a table of two cells."""
        mod, body = published(monkeypatch, tmp_path, RELEASE)
        work, closed, people = mod.tally(RELEASE, OWNER)
        assert mod.header(work, closed, people) == HEADER
        assert body.startswith(HEADER + "\n\n" + fold(*FOLDED[0])), body[:400]
        cleared = mod.marked_header(
            "https://example.com/mark.png",
            "a mark",
            160,
            CLEARED,
            RESULTS,
            work,
            closed,
            people,
        )
        assert cleared == (
            '<p><img src="https://example.com/mark.png" alt="a mark" width="160" '
            f'align="left">{BADGE_LINES}<br clear="left"></p>'
        ), cleared
        alone = [pull(10, OWNER, "fix: one", "Closes #100")]
        work, closed, people = mod.tally(alone, OWNER)
        odd = mod.marked_header(
            'u?a=1&b="2"',
            'a "mark" <b>',
            80,
            [[("CLEARED", "v<1>")]],
            [[("a & b", 'say "x"')]],
            work,
            closed,
            people,
        )
        assert odd == (
            '<p><img src="u?a=1&amp;b=&quot;2&quot;" alt="a &quot;mark&quot; &lt;b&gt;" '
            'width="80" align="left">'
            + "<br>".join(
                [
                    badge("CLEARED-v%3C1%3E", "CLEARED: v&lt;1&gt;", MARK_RED),
                    badge("pull%20requests-1%20merged", "pull requests: 1 merged"),
                    badge("issues-1%20closed", "issues: 1 closed"),
                    badge("a%20%26%20b-say%20%22x%22", "a &amp; b: say &quot;x&quot;"),
                ]
            )
            + '<br clear="left"></p>'
        ), odd

    def test_the_marked_header_given_no_image_is_its_badges_alone(
        self, monkeypatch, tmp_path
    ):
        """#1204 S7, #1299 S2 and #1496 S3. Where the repository leaves the
        release note's mark image off, `marked_header` is given no image and
        builds the paragraph of the badges alone: the same badges, in the
        same order and escaped the same way, as the header with the image
        holds, with no float to clear. Seen red against the `marked_header`
        that always drew the image's cell, against the one that wrote the
        results as text, and against the header that was a table of one
        cell."""
        mod, _body = published(monkeypatch, tmp_path, RELEASE)
        work, closed, people = mod.tally(RELEASE, OWNER)
        said = (CLEARED, RESULTS, work, closed, people)
        two = mod.marked_header("https://example.com/mark.png", "a mark", 160, *said)
        one = mod.marked_header(None, None, None, *said)
        assert one == f"<p>{BADGE_LINES}</p>", one
        image = (
            '<img src="https://example.com/mark.png" alt="a mark" '
            'width="160" align="left">'
        )
        assert two.replace(image, "").replace('<br clear="left">', "") == one, (
            two,
            one,
        )

    def test_a_badge_spells_its_label_and_value_as_the_service_reads_them(self):
        """#1299 S4. The badge service reads a static badge's address by its
        own grammar: the segment after `/badge/` splits at each single `-`
        into the label, the value and the colour, `--` reads as `-`, `__`
        as `_`, a single `_` as a space, and the rest is percent-decoded.
        So a label and a value holding a `-`, a `_`, a space and the
        characters a URL or an attribute gives a meaning to come back
        exactly as written, and the alt text is the same two words. The
        label has no colours of its own, so its value is blue and its label
        grey (#1496 S4).
        Seen red against an encoder that percent-encoded alone, without
        doubling, and against the `badge` that coloured every label with the
        wax seal's two reds."""
        mod = publisher()
        label, value = "a-b_c d", '50% & ? # / < " x-y__z'
        img = mod.badge(label, value)
        src = html.unescape(re.search(r'src="([^"]*)"', img).group(1))
        alt = html.unescape(re.search(r'alt="([^"]*)"', img).group(1))
        address = urllib.parse.urlsplit(src)
        assert address.path.startswith("/badge/"), src
        held = address.path[len("/badge/") :].replace("--", "\0").replace("__", "\1")
        read = [
            urllib.parse.unquote(
                field.replace("_", " ").replace("\0", "-").replace("\1", "_")
            )
            for field in held.split("-")
        ]
        assert read == [label, value, BLUE[0]], (src, read)
        assert urllib.parse.parse_qs(address.query) == {"labelColor": [BLUE[1]]}, src
        assert alt == f"{label}: {value}", img

    @pytest.mark.parametrize(
        "label, colours",
        [
            pytest.param("CLEARED", MARK_RED, id="CLEARED"),
            pytest.param("suite", GREEN, id="suite"),
            *(
                pytest.param(label, GREY, id=label)
                for label in ("skipped", "capped", "deferred")
            ),
            *(
                pytest.param(label, BLUE, id=label)
                for label in (
                    "commit",
                    "on",
                    "pull requests",
                    "issues",
                    "outside contributors",
                    "review",
                    "work items",
                )
            ),
        ],
    )
    def test_a_badge_takes_its_two_colours_from_its_label(self, label, colours):
        """#1496 S4, colours C3. A badge's value colour and label colour are
        read by its label, so a passing result does not read like a failure:
        `CLEARED` keeps the wax seal's dark red label beside its bright red value,
        and every other label is grey. The suite's passed count is green, the
        skipped, capped and deferred counts are grey, and every other value
        of the marked header is blue. The value is `not read`, the one a
        source that could not be read gives, and the label alone still
        decides the colours; a label with no colours of its own is the case
        above. Seen red against the `badge` that coloured every label with
        the wax seal's two reds, at every parameter but `CLEARED`, whose two reds
        that `badge` already gave; `CLEARED`'s was seen red with its entry
        removed."""
        mod = publisher()
        img = mod.badge(label, "not read")
        src = html.unescape(re.search(r'src="([^"]*)"', img).group(1))
        address = urllib.parse.urlsplit(src)
        colour = address.path.rsplit("-", 1)[1]
        edge = urllib.parse.parse_qs(address.query)["labelColor"]
        assert (colour, edge) == (colours[0], [colours[1]]), src

    @pytest.mark.parametrize(
        "body, theme",
        [
            pytest.param(
                "Release 1.2.3 carries two work items: a and b. Then x.",
                "Release 1.2.3 carries two work items: a and b.",
                id="a release pull request's opening",
            ),
            pytest.param(
                "the notes come once. Then twice.",
                "The notes come once.",
                id="upper-cased",
            ),
            pytest.param(
                "a first line\nthat goes on. Then.",
                "A first line",
                id="the line ends first",
            ),
            pytest.param(
                "what 0.18.0 left. Then.",
                "What 0.18.0 left.",
                id="a version inside the sentence",
            ),
            pytest.param(
                "  the  notes\tcome.",
                "The notes come.",
                id="whitespace collapsed",
            ),
            pytest.param(
                "Purpose: the notes come. Then.",
                "Purpose: the notes come.",
                id="a label is read as written",
            ),
            pytest.param("no full stop at all", "No full stop at all", id="no stop"),
        ],
    )
    def test_the_theme_is_the_bodys_first_sentence(self, body, theme):
        """S10 of #1671, and S3 of #1053. The sentence runs to the first `.`
        followed by whitespace or the end, or to the first line end where
        that comes first; the whitespace is collapsed and the first letter
        is upper-cased. A leading `Purpose:`, the label a milestone's
        description opened with, is read as written, since the body is no
        milestone's."""
        assert publisher().theme_of(body) == theme

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

    def test_a_git_that_cannot_read_the_adding_commit_stops_the_run(self, monkeypatch):
        """#1139. Where `git` cannot read the commit that adds a fragment,
        the job stops saying what `git` said, as `run` does, rather than
        publishing that entry without its link."""
        mod = publisher()

        def fails(root, revisions, path):
            raise RuntimeError("`git log nosuch -- p` exited 128: bad revision")

        monkeypatch.setattr(mod.settle, "adding_commit", fails)
        with pytest.raises(SystemExit, match="exited 128: bad revision"):
            mod.pull_request("nosuch", "p")

    def test_the_process_table_takes_its_shape_from_the_template(self):
        """#1117. The heading, the header row and the delimiter row `section`
        writes are `templates/records/process.md`'s, the section's one
        source."""
        with open(
            os.path.join(ROOT, "templates", "records", "process.md"), encoding="utf-8"
        ) as handle:
            template = handle.read().split("\n")
        assert publisher().process_shape() == (template[0], template[2], template[3])

    def test_a_fragment_the_settle_removed_reaches_a_note_tagged_on_a_merge(
        self, tmp_path, monkeypatch
    ):
        """The release's shape: the tag is the `--no-ff` merge of the release
        branch into `main`, whose first parent never held the fragment, and the
        settle removed it on the release branch (0.22.4). A fragment of the
        release before, restored by a commit in the range, is not read again
        (0.15.3). Round 1 of #1053, finding 1. The pull request its adding
        commit names is read through the same merge (#1139)."""
        repo = git_repo(tmp_path / "repo")
        thread = "agentory/threads/{}/changelog.md"
        write(repo, thread.format("1700000000-older"), "- older entry\n")
        commit_everything(repo, "the release before")
        git_out(repo, "tag", PREVIOUS)
        git_out(repo, "switch", "-q", "-c", "release")
        write(repo, thread.format("1700000001-first"), "- first entry\n")
        commit_everything(repo, "the work item (#5)")
        git_out(repo, "rm", "-q", "-r", "agentory/threads/1700000001-first")
        git_out(repo, "rm", "-q", "-r", "agentory/threads/1700000000-older")
        commit_everything(repo, "the settle")
        write(repo, thread.format("1700000000-older"), "- older entry\n")
        commit_everything(repo, "a directory restored")
        git_out(repo, "switch", "-q", "-")
        git_out(repo, "merge", "-q", "--no-ff", "-m", "the release", "release")
        git_out(repo, "tag", TAG)
        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        revisions = mod.commit_range(mod.previous_tag(TAG), TAG)
        assert mod.fragments(revisions) == [("1700000001-first", "- first entry", 5)]

    def test_a_fragment_whose_id_is_not_ascii_reaches_the_note(
        self, tmp_path, monkeypatch
    ):
        """#1283. The range's added paths are read with `-z`, so a fragment
        whose id git quotes under the default `core.quotePath`, which CI has
        too, is read as it is and not left out. Seen red against the reading
        without `-z`, which returned the ASCII fragment alone."""
        repo = git_repo(tmp_path / "repo")
        thread = "agentory/threads/{}/changelog.md"
        git_out(repo, "tag", PREVIOUS)
        write(repo, thread.format("1700000001-정렬"), "- sorted entry\n")
        commit_everything(repo, "the work item (#5)")
        write(repo, thread.format("1700000002-plain"), "- plain entry\n")
        commit_everything(repo, "the other work item (#6)")
        git_out(repo, "tag", TAG)
        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        assert mod.fragments(f"{PREVIOUS}..{TAG}") == [
            ("1700000001-정렬", "- sorted entry", 5),
            ("1700000002-plain", "- plain entry", 6),
        ]

    def test_a_settle_is_a_commit_that_removes_a_work_item_directory_whole(
        self, tmp_path, monkeypatch
    ):
        """A6, S3 of #1655, on a real history. A commit is a settle where it
        removes whole a directory under `agentory/threads/` that stood at its
        parent, as `chain_check.py#settled` reads one. A commit that removes
        one file of a directory that stays, and one that removes a whole
        directory outside the root, are no settle, and each is named by its
        short hash and subject, oldest first. A range that holds no commit
        but a merge holds none to judge, so it is no range of settles alone.
        Seen red against the script before #1655, where the reading did not
        exist."""
        repo = git_repo(tmp_path / "repo")
        thread = "agentory/threads/{}/{}"
        write(repo, thread.format("1700000000-gone", "changelog.md"), "- gone\n")
        write(repo, thread.format("1700000001-kept", "a.md"), "a\n")
        write(repo, thread.format("1700000001-kept", "b.md"), "b\n")
        write(repo, "docs/old/c.md", "c\n")
        commit_everything(repo, "the release before")
        git_out(repo, "tag", PREVIOUS)
        git_out(repo, "rm", "-q", "-r", "agentory/threads/1700000000-gone")
        settle = commit_everything(repo, "the settle")
        git_out(repo, "rm", "-q", "agentory/threads/1700000001-kept/a.md")
        part = commit_everything(repo, "a part of a work item")
        git_out(repo, "rm", "-q", "-r", "docs/old")
        outside = commit_everything(repo, "a directory outside the root")
        merge = git_out(
            repo, "commit-tree", "HEAD^{tree}", "-p", "HEAD", "-p", "HEAD~1", "-m", "m"
        )
        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        assert mod.settles(f"{PREVIOUS}..{settle}") == (True, [])
        assert mod.settles(f"{PREVIOUS}..{outside}") == (
            True,
            [
                (git_out(repo, "rev-parse", "--short", part), "a part of a work item"),
                (
                    git_out(repo, "rev-parse", "--short", outside),
                    "a directory outside the root",
                ),
            ],
        )
        assert mod.settles(f"{outside}..{merge}") == (False, [])

    def test_the_line_the_checklist_copies_is_the_line_the_reader_reads(self):
        """S17 of #1000. The command in `docs/releasing/release-checklist.md` *The
        release pull request*, filled with a version and a symptom, is the merge
        commit's body line, and `title_from` reads it as S15 does. Protects: the
        document a release session copies and the reader moving apart, which
        loses the next release's title."""
        doc = open(
            os.path.join(ROOT, "docs", "releasing", "release-checklist.md"),
            encoding="utf-8",
        )
        text = doc.read()
        doc.close()
        step = text[text.index("## The release pull request") :]
        title = step.split('--title "', 1)[1].split('"', 1)[0]
        filled = title.replace("X.Y.Z", VERSION).replace(
            "<the symptoms the release answers>", SYMPTOMS
        )
        assert filled != title and "<" not in filled, title
        mod = module(SCRIPT, "publish_release_note_for_the_checklist")
        message = f"Merge pull request #500 from owner/release/v{VERSION}\n\n{filled}\n"
        title, source = mod.title_from(message, VERSION, TAG)
        assert (title, source) == (
            f"{VERSION} — {SYMPTOMS}",
            "the tagged commit's `release:` line",
        )
        # Trailing whitespace after the symptoms is no part of the title.
        spaced = mod.title_from(message.replace("\n", "  \n"), VERSION, TAG)[0]
        assert spaced == title, spaced


def gh_api_answers(monkeypatch, mod, returncode, stdout, stderr):
    """`gh api -i` replaced by one answer, so `release_exists` itself is what
    runs. Returns the argv of each run."""
    asked = []

    def run(argv, **_):
        asked.append(list(argv))
        return Done(returncode, stdout, stderr)

    monkeypatch.setattr(mod.gitcmd.subprocess, "run", run)
    return asked


# What `gh api -i` prints to stdout for a release, in the shape
# `tests/lib/test_gitcmd.py#Test_http_answer` reads.
RELEASE_MISSING = 'HTTP/2.0 404 Not Found\nContent-Type: x\n\n{"message":"Not Found"}'
RELEASE_FORBIDDEN = 'HTTP/2.0 403 Forbidden\nContent-Type: x\n\n{"message":"x"}'
RELEASE_PRESENT = 'HTTP/2.0 200 OK\nContent-Type: x\n\n{"tag_name":"v1.2.3"}'


class Test_release_exists:
    """`release_exists` decides on the HTTP status `gh api -i` printed, read
    by `lib/gitcmd.py#http_answer`, and never on the words of gh's stderr.
    Where two cases call `release_exists` alike, the world differs: the
    answer `gh api -i` gives."""

    @pytest.mark.parametrize(
        "returncode, stdout, stderr, exists",
        [
            (1, RELEASE_MISSING, "gh: Not Found (HTTP 404)", False),
            (0, RELEASE_PRESENT, "", True),
        ],
        ids=["a-404-is-no-release", "a-200-is-a-release"],
    )
    def test_accepts_a_404_as_no_release_and_a_2xx_as_one(
        self, monkeypatch, returncode, stdout, stderr, exists
    ):
        mod = publisher()
        asked = gh_api_answers(monkeypatch, mod, returncode, stdout, stderr)
        assert mod.release_exists(REPO, TAG) is exists
        assert asked[0][1:] == ["api", "-i", f"repos/{REPO}/releases/tags/{TAG}"]

    @pytest.mark.parametrize(
        "stdout, stderr",
        [(RELEASE_FORBIDDEN, "gh: Not Found (HTTP 403)"), ("", "HTTP 502")],
        ids=["a-403-whose-stderr-says-not-found", "no-http-answer"],
    )
    def test_refuses_any_other_status_and_no_status_by_exiting(
        self, monkeypatch, stdout, stderr
    ):
        """A token without the scope to read releases, read as no release,
        would publish a second one at the tag."""
        mod = publisher()
        gh_api_answers(monkeypatch, mod, 1, stdout, stderr)
        with pytest.raises(SystemExit) as stopped:
            mod.release_exists(REPO, TAG)
        assert str(stopped.value.code) == (
            f"gh api releases/tags/{TAG} failed: {stderr}"
        )


def gh_pr_list_answers(monkeypatch, mod, returncode, stdout, stderr=""):
    """`gh` replaced by one answer and `git` run for real, so
    `release_pull_body` itself is what runs. Returns the argv of each `gh`
    run."""
    real, asked = mod.gitcmd.subprocess.run, []

    def run(argv, *args, **kwargs):
        if "-C" in list(argv):
            return real(argv, *args, **kwargs)
        asked.append(list(argv))
        return Done(returncode, stdout, stderr)

    monkeypatch.setattr(mod.gitcmd.subprocess, "run", run)
    return asked


class Test_release_pull_body:
    """`release_pull_body` reads the body of the pull request merged into
    `main` whose merge commit is the tagged commit, by no head name, or says
    why there is none (A6, S4 of #1655, S10 of #1671). Seen red against the
    script before #1655, where the reader did not exist, and against the
    one before #1671, which named the numbered release branch as the
    head."""

    def tagged(self, tmp_path, monkeypatch):
        """The script at a repository whose `TAG` names a commit; the
        commit's full hash."""
        repo = git_repo(tmp_path / "repo")
        git_out(repo, "tag", TAG)
        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        return mod, git_out(repo, "rev-parse", "HEAD")

    def test_accepts_the_body_of_the_pull_request_the_tag_merged(
        self, tmp_path, monkeypatch
    ):
        mod, commit = self.tagged(tmp_path, monkeypatch)
        listed = [
            {"number": 499, "body": "an older one", "mergeCommit": {"oid": "0" * 40}},
            {
                "number": 500,
                "body": f"\n{RELEASE_BODY}\n",
                "mergeCommit": {"oid": commit},
            },
        ]
        asked = gh_pr_list_answers(monkeypatch, mod, 0, json.dumps(listed))
        assert mod.release_pull_body(REPO, TAG) == (RELEASE_BODY, FROM_RELEASE_PULL)
        args = asked[0]
        assert args[1:3] == ["pr", "list"], args
        assert args[args.index("--repo") + 1] == REPO
        assert args[args.index("--base") + 1] == "main"
        assert "--head" not in args, args
        assert args[args.index("--state") + 1] == "merged"
        assert args[args.index("--limit") + 1] == str(mod.RELEASE_PULLS_LISTED)
        fields = args[args.index("--json") + 1].split(",")
        assert "body" in fields and "mergeCommit" in fields, fields

    @pytest.mark.parametrize(
        "returncode, stdout, stderr, said",
        [
            pytest.param(
                1,
                "",
                "HTTP 502",
                "the release pull request could not be listed: HTTP 502",
                id="gh fails",
            ),
            pytest.param(
                0,
                "not json",
                "",
                "gh pr list printed something that is not JSON, so the release "
                "pull request could not be read",
                id="no JSON",
            ),
            pytest.param(
                0,
                json.dumps([{"number": 499, "body": "x", "mergeCommit": {"oid": "0"}}]),
                "",
                f"no pull request merged into main has {TAG}'s commit as its "
                "merge commit",
                id="none merged at the tag",
            ),
            pytest.param(
                0,
                "MERGED_HERE",
                "",
                "the release pull request #500 has an empty body",
                id="an empty body",
            ),
        ],
    )
    def test_refuses_a_release_pull_request_that_cannot_be_read(
        self, tmp_path, monkeypatch, returncode, stdout, stderr, said
    ):
        mod, commit = self.tagged(tmp_path, monkeypatch)
        if stdout == "MERGED_HERE":
            stdout = json.dumps(
                [{"number": 500, "body": " \n", "mergeCommit": {"oid": commit}}]
            )
        gh_pr_list_answers(monkeypatch, mod, returncode, stdout, stderr)
        assert mod.release_pull_body(REPO, TAG) == (None, said)

    def test_a_gh_that_gave_no_answer_is_a_list_that_could_not_be_read(
        self, tmp_path, monkeypatch
    ):
        mod, _ = self.tagged(tmp_path, monkeypatch)
        unanswered(monkeypatch, "pr", "list")
        body, said = mod.release_pull_body(REPO, TAG)
        assert body is None
        assert said.startswith(
            "the release pull request could not be listed: `gh pr list --repo "
        ), said
        assert said.endswith("did not finish within 60 seconds"), said


class Test_section:
    def test_accepts_process_rows_into_one_table_above_the_fragments(self):
        """S9 of #1117. A work item that changed the way of working ends its
        fragment with a `### Process changes` table. The note carries one
        such table above the fragments, holding every fragment's rows in id
        order, and each fragment follows without its section, so a row is
        shown once. A fragment that is the section alone keeps its link line
        with nothing under it, and gives no entry where its adding commit
        names no pull request (#1139)."""
        header = "| Date | Change | Why | Source |\n|---|---|---|---|\n"
        first = (
            "- **A change.** What it does.\n\n### Process changes\n\n"
            + header
            + "| 2026-10-01 | one | why one | https://example.com/1 |\n"
            + "| 2026-10-02 | two | why two | https://example.com/2 |"
        )
        third = (
            "### Process changes\n\n"
            + header
            + "| 2026-10-03 | three | why three | https://example.com/3 |"
        )
        fourth = (
            "### Process changes\n\n"
            + header
            + "| 2026-10-04 | four | why four | https://example.com/4 |"
        )
        entries = [
            ("1-first", first, 1),
            ("2-second", "- b", 2),
            ("3-third", third, 3),
            ("4-fourth", fourth, None),
        ]
        pulls = f"https://github.com/{REPO}/pull"
        assert publisher().section(entries, REPO) == (
            "### Process changes\n\n"
            + header
            + "| 2026-10-01 | one | why one | https://example.com/1 |\n"
            + "| 2026-10-02 | two | why two | https://example.com/2 |\n"
            + "| 2026-10-03 | three | why three | https://example.com/3 |\n"
            + "| 2026-10-04 | four | why four | https://example.com/4 |\n\n"
            + f"[#1]({pulls}/1)\n- **A change.** What it does.\n\n"
            + f"[#2]({pulls}/2)\n- b\n\n"
            + f"[#3]({pulls}/3)"
        )

    def test_refuses_to_take_a_line_past_the_next_heading(self):
        """The process section ends at the next heading, so a table under a
        later heading stays in its fragment and none of its rows is lifted."""
        header = "| Date | Change | Why | Source |\n|---|---|---|---|\n"
        later = "### Removed\n\n| What | Where |\n|---|---|\n| a file | `x.md` |"
        body = f"### Process changes\n\n{header}| d | c | w | s |\n\n{later}"
        assert publisher().section([("1-first", body, None)], REPO) == (
            f"### Process changes\n\n{header}| d | c | w | s |\n\n{later}"
        )

    def test_refuses_a_table_where_no_fragment_carries_a_row(self):
        """S10 of #1117. With no process row in any fragment, the output is
        what `section` returned before #1117: each entry, its link line and
        its body, and no `### Process changes` heading."""
        entries = [
            ("1-first", "- a\n\n### Removed\n\n- gone", 1),
            ("2-second", "- b", None),
        ]
        assert publisher().section(entries, REPO) == (
            f"[#1](https://github.com/{REPO}/pull/1)\n- a\n\n### Removed\n\n- gone\n\n"
            "- b"
        )


test_census = census_case(TARGET)
