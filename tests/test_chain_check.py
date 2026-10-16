"""`skills/code-review/scripts/chain_check.py`, one group per function.

Each group holds a case on good input and a case on bad input. The `main`
group runs the check end to end over a real git repository: a branch with a
routing declaration, a round record and a `broad-gate.md`, judged as a ready
or a draft pull request through the event payload GitHub writes.
"""

import importlib.util
import json
import os
import pathlib
import re
import subprocess

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAIN = ROOT / "skills" / "code-review" / "scripts" / "chain_check.py"
READER = ROOT / "skills" / "verify" / "scripts" / "unverified_check.py"
ITEM = "seal/specs/1791999999-a-work-item"
# The pictographs and symbols a mark is drawn from: the colour circles and
# squares, the check and cross marks, the question mark ornament and the
# variation selector that follows them.
EMOJI = re.compile("[⌀-⏿☀-➿⬀-⯿️\U0001f000-\U0001faff]")


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


chain = load(CHAIN, "chain_check_under_test")
reader = load(READER, "unverified_reader_for_chain_tests")


def git(d, *args):
    return subprocess.run(
        ["git", "-C", str(d), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.strip()


def write(d, rel, text):
    p = pathlib.Path(d) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def commit(d, message):
    git(d, "add", "-A")
    git(d, "commit", "-qm", message)
    return git(d, "rev-parse", "HEAD")


ROUTING = """# a work item -- routing

| Axis | Answer |
|---|---|
| Review | {review} |
| Destination | open the pull request |
| Planning | {planning} |
| Branch | feature/x |
"""


def finding(
    n,
    verdict,
    severity="must",
    title="the parser drops a row",
    location="`f.txt:1`",
    refixes=None,
):
    """One `### ` section of `## Findings`, in `templates/sdd-round.md`'s
    shape, its `verdict:` line reading `verdict`."""
    return (
        f"### {n}. {title}\n\n"
        f"severity: {severity}\n"
        f"location: {location}\n"
        f"verdict: {verdict}\n"
        + (f"refixes: {refixes}\n" if refixes else "")
        + "\nWhy it matters. read: `f.txt:1`.\n\n"
        "```python\nx = 1\n```\n\n"
        "answer: \n"
    )


def confirm(reference, what="the fix holds"):
    """One row of `## Confirmations`, its `Confirms` cell `reference`."""
    return f"| {reference} | {what} | `f.txt:1` | read |\n"


def record(target, findings=(), confirmations="", n=1):
    """A round record in `templates/sdd-round.md`'s shape: `findings` are
    `finding()` sections, `confirmations` rows of `## Confirmations`."""
    return (
        f"# 1791999999-a-work-item — review round {n}\n\n"
        "| Field | Value |\n|---|---|\n"
        f"| Target SHA | {target} against main |\n\n"
        "## Findings\n\n" + "\n".join(findings) + "\n## Confirmations\n\n"
        "| Confirms | What holds | Location | Grounds |\n|---|---|---|---|\n"
        f"{confirmations}\n"
        "## Not judged\n\n"
        "| What | Location | Who answers |\n|---|---|---|\n\n"
        "## Probes\n\n"
        "| Command | Result |\n|---|---|\n"
    )


def rounds_of(*texts):
    """The records `texts`, numbered from 1, read as `channel` takes them."""
    out, errors = [], []
    for n, text in enumerate(texts, 1):
        read, said = chain.round_of(reader, text, f"round-{n}.md", n)
        out.append(read)
        errors.extend(said)
    return out, errors


# The table the old generator's records carried, which nothing reads again:
# a merged item keeps one in the fixture, and the check must never open it.
OLD_RECORD = (
    "# 1788999999-a-merged-item — review round 1\n\n"
    "| Field | Value |\n|---|---|\n"
    "| Target SHA | 0000000 against main |\n\n"
    "## Verdicts\n\n"
    "| # | Finding | Location | Verdict | Grounds |\n"
    "|---|---|---|---|---|\n"
    "| 🔴 1 | wrong | `f.txt:1` | open | g |\n"
)
MERGED_ITEM = "seal/specs/1788999999-a-merged-item"


def gate_file(sha):
    return (
        "# 1791999999-a-work-item — broad gate\n\n"
        "| Field | Value |\n|---|---|\n"
        f"| Broad gate | {sha} against main |\n"
    )


def guarantee_file(sha, verdict="sound"):
    return (
        "# 1791999999-a-work-item — guarantee\n\n"
        "| Field | Value |\n|---|---|\n"
        f"| Target SHA | {sha} against main |\n\n"
        f"Verdict: {verdict}\n"
    )


SPEC = "# spec\n\nbody\n\nFramed 2026-10-15 by framer, before the build.\n"


@pytest.fixture
def branch(tmp_path):
    """A repository whose `feature/x` declares a work item and reviewed it.

    `main` holds one file and a work item another pull request merged, its
    declaration naming another branch and its one record in the old table's
    shape with a finding open (S11). `feature/x` adds the declaration, a code
    commit, round 1 at that commit with its one finding `fixed` by it, round
    2 — the verifying round — confirming `round-1#1` with nothing of its own,
    and the sealer's two files. Returns `(root, code commit)`.
    """
    d = tmp_path / "r"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@t")
    git(d, "config", "user.name", "t")
    write(d, "f.txt", "one\n")
    write(
        d,
        f"{MERGED_ITEM}/routing.md",
        ROUTING.format(
            review="through the review chain", planning="the session"
        ).replace("feature/x", "feature/merged"),
    )
    write(d, f"{MERGED_ITEM}/rounds/round-1.md", OLD_RECORD)
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/x")
    write(
        d,
        f"{ITEM}/routing.md",
        ROUTING.format(review="through the review chain", planning="the session"),
    )
    commit(d, "routing")
    write(d, "f.txt", "two\n")
    code = commit(d, "code")
    write(
        d,
        f"{ITEM}/rounds/round-1.md",
        record(code, [finding(1, f"fixed {code[:8]}")]),
    )
    commit(d, "the round record")
    write(
        d,
        f"{ITEM}/rounds/round-2.md",
        record(code, confirmations=confirm("round-1#1"), n=2),
    )
    reviewed = commit(d, "the verifying round")
    # Two runs, newest first: the earlier one names a commit nobody can see,
    # so a reader that took any run but the first would refuse the file.
    write(
        d,
        f"{ITEM}/broad-gate.md",
        gate_file(f"{reviewed} against main; earlier run: {'1' * 40}"),
    )
    write(d, f"{ITEM}/guarantee.md", guarantee_file(reviewed))
    commit(d, "the sealer's two files")
    return d, code


def seal(d):
    """The sealer's two files naming HEAD, committed: what a branch carries
    once the sealer has audited what is on it."""
    head = git(d, "rev-parse", "HEAD")
    write(d, f"{ITEM}/broad-gate.md", gate_file(f"{head} against main"))
    write(d, f"{ITEM}/guarantee.md", guarantee_file(head))
    commit(d, "the sealer's two files, again")


@pytest.fixture
def ready(tmp_path, monkeypatch):
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)


@pytest.fixture
def draft(tmp_path, monkeypatch):
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": True}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)


def check(root, capsys, *extra):
    code = chain.main(["--baseline", "main", "--root", str(root), *extra])
    return code, capsys.readouterr().out


# --- changed ------------------------------------------------------------------


def two_declarations(tmp_path):
    """`main` holds one declaration; `feature/y` checked out, nothing yet."""
    d = tmp_path / "c"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@t")
    git(d, "config", "user.name", "t")
    old = ROUTING.format(review="straight to the PR", planning="the session")
    write(d, "seal/specs/1788000000-old/routing.md", old)
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/y")
    return d, old


class TestChanged:
    def test_a_declaration_moved_unchanged_is_neither_judged_nor_missed(self, tmp_path):
        """A move of the whole root renames every declaration at once, and a
        declaration the pull request only moved is not one it made (#90)."""
        d, _old = two_declarations(tmp_path)
        git(d, "mv", "seal/specs/1788000000-old", "seal/specs/1788000000-moved")
        commit(d, "moved")
        paths, renamed = chain.changed(str(d), "main")
        assert renamed == {
            "seal/specs/1788000000-old/routing.md",
            "seal/specs/1788000000-moved/routing.md",
        }
        assert chain.changed_routing(paths, renamed, "seal/specs") == []

    def test_a_move_not_yet_committed_is_read_from_the_files(
        self, tmp_path, monkeypatch
    ):
        """Under `--worktree` an untracked file has no blob git can name, so
        the moved file's bytes are hashed to pair it."""
        d, _old = two_declarations(tmp_path)
        os.rename(d / "seal/specs/1788000000-old", d / "seal/specs/1788000000-moved")
        monkeypatch.setattr(chain, "WORKTREE", True)
        _paths, renamed = chain.changed(str(d), "main")
        assert renamed == {
            "seal/specs/1788000000-old/routing.md",
            "seal/specs/1788000000-moved/routing.md",
        }

    def test_a_deletion_beside_a_similar_addition_is_not_read_as_a_rename(
        self, tmp_path
    ):
        """Two declarations from one template differ in a row or two, which
        git's rename detection pairs. The check reads declarations, not file
        identity, so the deletion is seen."""
        d, old = two_declarations(tmp_path)
        git(d, "rm", "-q", "seal/specs/1788000000-old/routing.md")
        write(
            d,
            "seal/specs/1791999999-new/routing.md",
            old.replace("feature/x", "feature/y"),
        )
        commit(d, "one leaves, one arrives")
        paths, renamed = chain.changed(str(d), "main")
        assert renamed == set()
        assert chain.changed_routing(paths, renamed, "seal/specs") == [
            "seal/specs/1788000000-old/routing.md",
            "seal/specs/1791999999-new/routing.md",
        ]


# --- carried_by ---------------------------------------------------------------

RELEASE = "release/v9.9.9"
GITHUB = {"GIT_COMMITTER_NAME": "GitHub", "GIT_COMMITTER_EMAIL": "noreply@github.com"}


def squash(d, source, subject, committer=None):
    """Squash `source` onto the checked-out branch as GitHub's merge button
    does: one commit, committed by GitHub, its subject ending with the pull
    request's number. `committer` replaces GitHub's identity."""
    git(d, "merge", "--squash", "-q", source)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", subject],
        check=True,
        capture_output=True,
        env={**os.environ, **(committer or GITHUB)},
    )
    return git(d, "rev-parse", "HEAD")


def released(root, subject="feat: a work item (#7)", committer=None, keep=False):
    """`release/v9.9.9` cut from `main` with `feature/x` squashed into it and
    the feature branch deleted, so the item's records name commits HEAD does
    not descend from — what a release pull request into `main` carries."""
    git(root, "switch", "-q", "-c", RELEASE, "main")
    squash(root, "feature/x", subject, committer)
    if not keep:
        git(root, "branch", "-q", "-D", "feature/x")


class TestCarriedBy:
    def test_a_declaration_only_a_squash_merge_touched_is_that_pull_requests(
        self, branch, monkeypatch
    ):
        root, _code = branch
        monkeypatch.setattr(chain, "WORKTREE", False)
        released(root)
        rel = f"{ITEM}/routing.md"
        sha, subject = chain.carried_by(str(root), "main", rel)
        assert sha == git(root, "rev-parse", "HEAD")
        assert subject == "feat: a work item (#7)"
        # Under `--worktree` an edit not yet committed is this branch's own.
        monkeypatch.setattr(chain, "WORKTREE", True)
        assert chain.carried_by(str(root), "main", rel) is not None
        write(root, rel, (root / rel).read_text(encoding="utf-8") + "\nA note.\n")
        assert chain.carried_by(str(root), "main", rel) is None

    def test_the_items_own_commits_a_persons_squash_and_an_unnumbered_one_are_not(
        self, branch, monkeypatch
    ):
        """The item's own branch, a squash a person committed with a subject
        naming an issue the way this repository's commits do, GitHub's commit
        whose subject does not end with a pull request number, and a path no
        commit touched each leave the declaration this pull request's."""
        root, _code = branch
        monkeypatch.setattr(chain, "WORKTREE", False)
        rel = f"{ITEM}/routing.md"
        assert chain.carried_by(str(root), "main", rel) is None
        released(root, committer={"GIT_COMMITTER_EMAIL": "t@t"}, keep=True)
        assert chain.carried_by(str(root), "main", rel) is None
        git(root, "reset", "-q", "--hard", "main")
        squash(root, "feature/x", "feat: a work item (#7), edited")
        assert chain.carried_by(str(root), "main", rel) is None
        assert chain.carried_by(str(root), "main", "seal/specs/none/routing.md") is None


# --- verdict_of ---------------------------------------------------------------


class TestVerdictOf:
    def test_the_four_values_read_and_nothing_else_does(self):
        """S3 (T25): a `verdict:` value is one of four shapes, read as it is
        written. Anything else is None, which the arm refuses by name."""
        sha = "1a2b3c4d" * 5
        for value, read in (
            ("open", (chain.OPEN, None)),
            ("fixed abc1234", (chain.FIXED, "abc1234")),
            (f"fixed {sha}", (chain.FIXED, sha)),
            ("answered", (chain.ANSWERED, None)),
            ("deferred #12", (chain.DEFERRED, "#12")),
            ("deferred the frame", (chain.DEFERRED, "the frame")),
        ):
            assert chain.verdict_of(value) == read, value
        for value in (
            "Fixed abc1234",
            "fixed",
            "fixed abc1234.",
            "fixed abc123",
            f"fixed {sha}0",
            "fixed ABC1234",
            "fixed abc1234 · fix pass: done",
            "deferred",
            "deferred ",
            "confirmed",
            "**fixed** abc1234",
            "open — see below",
            "Open",
            " answered",
            "",
        ):
            assert chain.verdict_of(value) is None, value


# --- deferred_home and issue_of -----------------------------------------------


class TestDeferredHome:
    def test_the_home_after_the_word_is_read(self):
        assert chain.deferred_home("deferred #12") == "#12"
        assert chain.issue_of(chain.deferred_home("deferred #12")) == 12
        assert chain.deferred_home("deferred the frame") == "the frame"

    def test_no_home_and_prose_name_no_issue(self):
        assert chain.deferred_home("deferred") is None
        assert chain.deferred_home("deferredness #12") is None
        assert chain.deferred_home("fixed abc1234") is None
        assert chain.issue_of(chain.deferred_home("deferred to #664")) is None
        assert chain.issue_of(chain.deferred_home("deferred #12.")) is None


# --- location_of --------------------------------------------------------------


class TestLocationOf:
    def test_one_or_more_backticked_coordinates_read_and_nothing_else_does(self):
        """S22 (T33): a `location:` value is one or more backticked `path`,
        `path:line` or `path:first-last` items joined by `, `, read as the
        paths they name. Anything else is None, which the arm refuses."""
        for value, paths in (
            ("`a.py`", ["a.py"]),
            ("`a.py:12`", ["a.py"]),
            ("`a.py:12-14`", ["a.py"]),
            ("`docs/x/`", ["docs/x/"]),
            ("`a.py:1`, `docs/b.md:3-4`", ["a.py", "docs/b.md"]),
            ("`a.py:1`, `b.py`, `c/d.md:9`", ["a.py", "b.py", "c/d.md"]),
        ):
            assert chain.location_of(value) == paths, value
        for value in (
            "`:617`",
            "`a.py:1`, `:617`",
            "a.py:12",
            "https://example.com/a",
            "`https://example.com/a`",
            "**`a.py:1`**",
            "_`a.py:1`_",
            "`a.py:1`,`b.py`",
            "`a.py:1` and `b.py`",
            "`a.py:1`, ",
            "`a.py:x`",
            "`a.py:1-`",
            "`/abs/a.py`",
            "`a.py`.",
            "`a b.py`",
            "",
        ):
            assert chain.location_of(value) is None, value


# --- reference_of -------------------------------------------------------------


class TestReferenceOf:
    def test_a_round_and_a_finding_read_and_nothing_else_does(self):
        """S23 (T35): a reference is `round-<N>#<n>`, or `round-<N>` for a
        round's fix pass, in that spelling and no other."""
        for value, read in (
            ("round-2#3", (2, 3)),
            ("round-2", (2, None)),
            ("round-12#10", (12, 10)),
        ):
            assert chain.reference_of(value) == read, value
        for value in (
            "round 2's 3",
            "Round-2#3",
            "ROUND-2#3",
            "#3",
            "round-2#3.",
            "**round-2#3**",
            "`round-2#3`",
            "round-02#3",
            "round-2#03",
            "round-0#1",
            "round-2#",
            "round-2 #3",
            " round-2#3",
            "round-2#3, round-2#4",
            "none",
            "",
        ):
            assert chain.reference_of(value) is None, value


# --- findings -----------------------------------------------------------------


class TestFindings:
    def test_each_finding_is_read_by_its_labelled_lines(self):
        """A finding's `### ` heading names it and its number; its one
        `verdict:` line decides it, its one `location:` line names its paths
        and its `refixes:` line, where it stands, the earlier finding; a
        severity, an answer and a confirmation are read for nothing."""
        text = record(
            "abc1234",
            [
                finding(1, "open"),
                finding(2, "fixed abc1234", severity="should", refixes="round-1#4"),
                finding(
                    3,
                    "deferred #12",
                    severity="anything at all",
                    location="`a.py:3`, `docs/b.md`",
                    refixes="round-1",
                ),
            ],
            confirmations=confirm("round-1#2"),
        )
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert errors == []
        assert [
            (f.line, f.heading, f.number, f.verdict, f.paths, f.refixes) for f in found
        ] == [
            (
                lines.index("verdict: open") + 1,
                "### 1. the parser drops a row",
                1,
                (chain.OPEN, None),
                ["f.txt"],
                None,
            ),
            (
                lines.index("verdict: fixed abc1234") + 1,
                "### 2. the parser drops a row",
                2,
                (chain.FIXED, "abc1234"),
                ["f.txt"],
                (1, 4),
            ),
            (
                lines.index("verdict: deferred #12") + 1,
                "### 3. the parser drops a row",
                3,
                (chain.DEFERRED, "#12"),
                ["a.py", "docs/b.md"],
                (1, None),
            ),
        ]
        assert found[1].refixes_line == lines.index("refixes: round-1#4") + 1
        empty = reader.readable(record("abc1234"))
        assert chain.findings(reader, empty, "r.md") == ([], [])

    def test_what_the_check_cannot_read_is_refused_by_name(self):
        """S3, S11, S22 (T26, T33): what the reader cannot read is an error
        naming the path, the line and the finding's heading, never a pass — a
        finding with no `verdict:` line, with two, with its only one inside
        the fix block; a value outside the four; a labelled line above the
        first finding or under another section; a finding with no
        `location:` line, two, or one the check cannot read, whatever its
        verdict; two `refixes:` lines, or one it cannot read; no
        `## Findings`, or two."""
        sections = [
            finding(1, "answered").replace("verdict: answered\n", ""),
            finding(2, "answered").replace(
                "verdict: answered\n", "verdict: answered\nverdict: open\n"
            ),
            finding(3, "answered")
            .replace("verdict: answered\n", "")
            .replace("x = 1\n", "verdict: answered\n"),
            finding(4, "deferred #9").replace("location: `f.txt:1`\n", ""),
            finding(5, "confirmed"),
            finding(6, "deferred #9", location="f.txt:1"),
            finding(7, "answered").replace(
                "location: `f.txt:1`\n", "location: `f.txt:1`\nlocation: `g.txt`\n"
            ),
            finding(8, "answered", refixes="round 1's 3"),
            finding(9, "answered", refixes="round-1#3").replace(
                "refixes: round-1#3\n", "refixes: round-1#3\nrefixes: round-1#4\n"
            ),
            finding(10, "answered"),
        ]
        text = record(
            "abc1234",
            sections,
            confirmations=confirm("none") + "\nlocation: `f.txt:1`\n",
        ).replace("## Findings\n\n", "## Findings\n\nverdict: answered\n\n")
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.heading for f in found] == ["### 10. the parser drops a row"]
        heads = [i + 1 for i, ln in enumerate(lines) if ln.startswith("### ")]

        def at(prefix, k=0):
            return [i + 1 for i, ln in enumerate(lines) if ln.startswith(prefix)][k]

        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", at("verdict: ")),
            ("r.md", heads[0]),
            ("r.md", at("verdict: open")),
            ("r.md", heads[2]),
            ("r.md", heads[3]),
            ("r.md", at("verdict: confirmed")),
            ("r.md", at("location: f.txt:1")),
            ("r.md", at("location: `g.txt`")),
            ("r.md", at("refixes: round 1's 3")),
            ("r.md", at("refixes: round-1#4")),
            ("r.md", at("location: ", -1)),
        ], errors
        said = [why for _rel, _line, why in errors]
        assert "outside a finding" in said[0] and "outside a finding" in said[-1]
        assert "`verdict:`" in said[0] and "`location:`" in said[-1]
        for why, n in zip(said[1:10], (1, 2, 3, 4, 5, 6, 7, 8, 9), strict=True):
            assert f"### {n}. the parser drops a row" in why, why
        assert "2 `verdict:` lines" in said[2]
        assert "no `verdict:` line" in said[1] and "no `verdict:` line" in said[3]
        assert "no `location:` line" in said[4]
        assert "`verdict: confirmed`" in said[5]
        assert "`fixed <commit>`" in said[5] and "`deferred <home>`" in said[5]
        assert "`location: f.txt:1`" in said[6] and "`path:line`" in said[6]
        assert "2 `location:` lines" in said[7]
        assert "`refixes: round 1's 3`" in said[8] and "`round-<N>#<n>`" in said[8]
        assert "2 `refixes:` lines" in said[9]
        assert chain.findings(
            reader, reader.readable("# r\n\n## Probes\n"), "r.md"
        ) == (
            [],
            [("r.md", 0, chain.NO_FINDINGS)],
        )
        two = reader.readable(record("abc1234") + "\n## Findings\n")
        second = [i + 1 for i, ln in enumerate(two) if ln == "## Findings"][1]
        _found, errors = chain.findings(reader, two, "r.md")
        assert [(line, why) for _rel, line, why in errors] == [
            (second, chain.TWO_FINDINGS)
        ]

    def test_a_label_in_another_spelling_is_refused_by_line(self):
        """S24 (T32): a line whose first word, case-folded and stripped of
        emphasis, is one of the five labels or the old `fix of a fix`, and
        which is not the exact lowercase form, is refused at its line naming
        the label the check reads — never skipped as prose. A finding
        carrying one is not read past it, so a finding with both spellings
        does not pass on the lowercase one."""
        for spelling, label in (
            ("Verdict: open", "`verdict:`"),
            ("**verdict:** open", "`verdict:`"),
            ("VERDICT: open", "`verdict:`"),
            ("verdict : open", "`verdict:`"),
            ("_verdict_: open", "`verdict:`"),
            ("Fix of a fix: `open_findings`", "`refixes:`"),
            ("`fix of a fix`: the unit", "`refixes:`"),
            ("fix of a fix: the unit", "`refixes:`"),
            ("Severity: must", "`severity:`"),
            ("Location: `f.txt:1`", "`location:`"),
            ("Refixes: round-1#1", "`refixes:`"),
            ("Answer: done", "`answer:`"),
            ("  answer : done", "`answer:`"),
        ):
            text = record(
                "abc1234",
                [
                    finding(1, "answered").replace("answer: \n", f"{spelling}\n"),
                    finding(2, "answered"),
                ],
            )
            lines = reader.readable(text)
            found, errors = chain.findings(reader, lines, "r.md")
            assert [f.number for f in found] == [2], spelling
            assert [(rel, line) for rel, line, _why in errors] == [
                ("r.md", lines.index(spelling) + 1)
            ], spelling
            why = errors[0][2]
            assert "### 1. the parser drops a row" in why, why
            assert label in why and "another spelling" in why, why
        outside = record("abc1234", [finding(1, "answered")]).replace(
            "## Not judged", "Verdict: answered\n\n## Not judged"
        )
        lines = reader.readable(outside)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [1]
        assert [(line, "`verdict:`" in why) for _rel, line, why in errors] == [
            (lines.index("Verdict: answered") + 1, True)
        ]
        exact = record("abc1234", [finding(1, "answered").replace("answer: \n", "")])
        assert chain.findings(reader, reader.readable(exact), "r.md")[1] == []
        for prose in ("Answers: none", "Verdicts read below.", "Severity matters."):
            text = record("abc1234", [finding(1, "answered")]).replace(
                "Why it matters.", prose
            )
            assert chain.findings(reader, reader.readable(text), "r.md")[1] == []

    def test_the_template_is_the_record_the_check_reads(self):
        """S1 (T29, T38): `templates/sdd-round.md` is a record the check reads
        — `Target SHA` its one field row; one finding at `open`, located at
        one coordinate, refixing `round-1#1`; a `verdict:` written inside its
        fix block not read as a line; a `## Confirmations` table headed
        `Confirms`, its two example cells `round-1#2` and `none` read; and no
        emoji anywhere in it."""
        text = (ROOT / "templates" / "sdd-round.md").read_text(encoding="utf-8")
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "t")
        assert errors == []
        assert [(f.verdict, f.paths, f.refixes) for f in found] == [
            ((chain.OPEN, None), ["path"], (1, 1))
        ]
        assert found[0].heading.startswith("### 1. ") and found[0].number == 1
        confirmed, errors = chain.confirmations(reader, lines, "t")
        assert errors == []
        assert [ref for _line, ref in confirmed] == [(1, 2)]
        cells = [
            cells[0]
            for cells in chain.table_rows(reader, lines)
            if cells and cells[0] in ("round-1#2", "none")
        ]
        assert cells == ["round-1#2", "none"]
        head = text.split(chain.FINDINGS_HEADING)[0]
        rows = chain.table_rows(reader, reader.readable(head))
        labels = [c[0].strip() for c in rows if "-" not in c[0]]
        assert labels == ["Field", "Target SHA"]
        assert chain.target_of(reader, text.replace("<sha>", "abc1234", 1))
        fence = text.index("```", text.index("### 1. "))
        line_end = text.index("\n", fence) + 1
        fenced = text[:line_end] + "verdict: answered\n" + text[line_end:]
        found, errors = chain.findings(reader, reader.readable(fenced), "t")
        assert errors == [] and [f.verdict for f in found] == [(chain.OPEN, None)]
        marks = [c for c in text if EMOJI.match(c)]
        assert marks == [], marks


# --- record_findings ----------------------------------------------------------


class TestRecordFindings:
    def test_a_record_whose_regions_close_reads_as_findings_reads_it(self):
        text = record("abc1234", [finding(1, "open"), finding(2, "answered")])
        found, errors = chain.record_findings(reader, text, "r.md")
        assert errors == []
        assert found == chain.findings(reader, reader.readable(text), "r.md")[0]

    def test_a_fence_or_comment_that_never_closes_is_refused_by_its_opener(self):
        """A fence or a comment that never closes hides every line after it,
        so the findings below it would vanish and the record would pass. The
        record is refused at the opener's line instead, and what the reader
        could still see is read as well."""
        hidden = finding(2, "open")
        # A `~~~` fence, so the backtick fence of the finding below it is
        # content and cannot close it.
        for opener, why in (("~~~python\n", "fence"), ("<!-- a note\n", "comment")):
            text = record(
                "abc1234",
                [finding(1, "answered").replace("answer: \n", opener), hidden],
            )
            found, errors = chain.record_findings(reader, text, "r.md")
            lines = text.splitlines()
            second = lines.index("### 2. the parser drops a row")
            line = 1 + max(
                i for i, ln in enumerate(lines[:second]) if ln == opener.rstrip("\n")
            )
            assert [(rel, n) for rel, n, _why in errors] == [("r.md", line)], errors
            assert why in errors[0][2] and "never closes" in errors[0][2]
            assert [f.heading for f in found] == ["### 1. the parser drops a row"]


# --- confirmations ------------------------------------------------------------


class TestConfirmations:
    def test_each_confirms_cell_reads_as_a_reference_or_none(self):
        """S23: the first column of `## Confirmations` is `Confirms`, and each
        row's cell there is `round-<N>#<n>`, read with its line, or `none`."""
        text = record(
            "abc1234",
            confirmations=confirm("round-1#2") + confirm("none") + confirm("round-3#1"),
            n=4,
        )
        lines = reader.readable(text)
        found, errors = chain.confirmations(reader, lines, "r.md")
        assert errors == []
        assert found == [
            (lines.index(confirm("round-1#2").rstrip("\n")) + 1, (1, 2)),
            (lines.index(confirm("round-3#1").rstrip("\n")) + 1, (3, 1)),
        ]

    def test_a_cell_or_a_header_the_check_cannot_read_is_refused_by_line(self):
        """S23 (T36): a `Confirms` cell outside `round-<N>#<n>` and `none` —
        prose, another case, a bare `#3`, a round with no finding, emphasis —
        is refused by its line; so is a table whose first header cell is not
        `Confirms`, and a record with no `## Confirmations` section, or two."""
        bad = ("round 1's 3", "Round-1#3", "#3", "round-1", "**none**", "")
        text = record(
            "abc1234",
            confirmations="".join(confirm(cell) for cell in bad) + confirm("none"),
            n=2,
        )
        lines = reader.readable(text)
        found, errors = chain.confirmations(reader, lines, "r.md")
        assert found == []
        rows = [lines.index(confirm(cell).rstrip("\n")) + 1 for cell in bad]
        assert [(rel, line) for rel, line, _why in errors] == [
            ("r.md", line) for line in rows
        ], errors
        for (_rel, _line, why), cell in zip(errors, bad, strict=True):
            assert f"`{cell}`" in why and "`round-<N>#<n>` or `none`" in why, why
        old = text.replace("| Confirms | What holds |", "| What holds | Confirms |")
        lines = reader.readable(old)
        _found, errors = chain.confirmations(reader, lines, "r.md")
        header = next(i for i, ln in enumerate(lines) if ln.startswith("| What holds"))
        assert errors[0][1] == header + 1 and "`Confirms`" in errors[0][2], errors
        none = record("abc1234").replace("## Confirmations", "## Confirmed")
        assert chain.confirmations(reader, reader.readable(none), "r.md") == (
            [],
            [("r.md", 0, chain.NO_CONFIRMATIONS)],
        )
        two = reader.readable(record("abc1234") + "\n## Confirmations\n")
        second = [i + 1 for i, ln in enumerate(two) if ln == "## Confirmations"][1]
        assert chain.confirmations(reader, two, "r.md")[1] == [
            ("r.md", second, chain.TWO_CONFIRMATIONS)
        ]


# --- channel ------------------------------------------------------------------


class TestChannel:
    def test_every_fixed_or_answered_finding_is_confirmed_or_refixed_by_the_next_round(
        self,
    ):
        """S23 (T36): every finding of round N at `fixed <commit>` or
        `answered` is named in round N+1, by a `Confirms` cell or by a
        `refixes:` line; a `deferred` one owes nothing, and a `refixes:` line
        naming the round alone covers no finding."""
        one = record(
            "abc1234",
            [
                finding(1, "fixed abc1234"),
                finding(2, "answered"),
                finding(3, "deferred #9"),
                finding(4, "fixed abc1234", title="the fourth"),
                finding(5, "answered", title="the fifth"),
            ],
        )
        two = record(
            "abc1234",
            [
                finding(1, "deferred the frame", refixes="round-1#2"),
                finding(2, "deferred the frame", refixes="round-1"),
            ],
            confirmations=confirm("round-1#1") + confirm("none"),
            n=2,
        )
        rounds, errors = rounds_of(one, two)
        assert errors == []
        problems = chain.channel(rounds)
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-2.md", 0),
            ("round-2.md", 0),
        ], problems
        said = [why for _rel, _line, why in problems]
        assert "`round-1#4`" in said[0] and "### 4. the fourth" in said[0]
        assert "`round-1#5`" in said[1] and "### 5. the fifth" in said[1]
        assert all("neither confirms nor refixes" in why for why in said), said
        covered = two.replace(
            confirm("none"), confirm("round-1#4") + confirm("round-1#5")
        )
        assert chain.channel(rounds_of(one, covered)[0]) == []
        deferred = record("abc1234", [finding(1, "deferred #9")])
        empty = record("abc1234", n=2)
        assert chain.channel(rounds_of(deferred, empty)[0]) == []

    def test_a_reference_the_check_cannot_read_or_naming_no_finding_is_refused(self):
        """S23 (T36): a reference naming a record the item has not got, or
        no earlier one, or a finding number that record does not hold, is
        refused by its line, naming the round and the number; any reference
        in the first record is refused, and `none` there passes."""
        one = record(
            "abc1234",
            [finding(1, "deferred #9", refixes="round-1#1")],
            confirmations=confirm("none") + confirm("round-1#1"),
        )
        two = record(
            "abc1234",
            [
                finding(1, "deferred #9", refixes="round-3#1"),
                finding(2, "deferred #9", refixes="round-2"),
            ],
            confirmations=confirm("round-1#7") + confirm("round-1#1"),
            n=2,
        )
        rounds, errors = rounds_of(one, two)
        assert errors == []
        problems = chain.channel(rounds)
        lines_one, lines_two = reader.readable(one), reader.readable(two)
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", lines_one.index("refixes: round-1#1") + 1),
            ("round-1.md", lines_one.index(confirm("round-1#1").rstrip("\n")) + 1),
            ("round-2.md", lines_two.index("refixes: round-3#1") + 1),
            ("round-2.md", lines_two.index("refixes: round-2") + 1),
            ("round-2.md", lines_two.index(confirm("round-1#7").rstrip("\n")) + 1),
        ], problems
        said = [why for _rel, _line, why in problems]
        assert all("the first record" in why for why in said[:2]), said
        assert "`round-3#1`" in said[2] and "not an earlier record" in said[2]
        assert "`round-2`" in said[3] and "not an earlier record" in said[3]
        assert "`round-1#7`" in said[4] and "holds no finding 7" in said[4]
        assert (
            chain.channel(
                rounds_of(record("abc1234", confirmations=confirm("none")))[0]
            )
            == []
        )

    def test_the_last_records_fixed_or_answered_finding_is_named(self):
        """S23 (T37): nothing after the last record has read its fixes or
        its answers, so each such finding is named with the words the
        `Target SHA` rule prints; its `deferred` findings, and none, pass."""
        last = record(
            "abc1234",
            [
                finding(1, "fixed abc1234"),
                finding(2, "answered"),
                finding(3, "deferred #9"),
                finding(4, "open"),
            ],
        )
        lines = reader.readable(last)
        problems = chain.channel(rounds_of(last)[0])
        assert [(rel, line) for rel, line, _why in problems] == [
            ("round-1.md", lines.index("verdict: fixed abc1234") + 1),
            ("round-1.md", lines.index("verdict: answered") + 1),
        ], problems
        assert all(chain.VERIFYING_ROUND in why for _r, _l, why in problems)
        assert "### 1." in problems[0][2] and "### 2." in problems[1][2]
        quiet = record("abc1234", [finding(1, "deferred #9")])
        assert chain.channel(rounds_of(quiet)[0]) == []
        assert chain.channel(rounds_of(record("abc1234"))[0]) == []


# --- follows ------------------------------------------------------------------


class TestFollows:
    def test_head_and_record_commits_after_it_pass(self, branch):
        root, code = branch
        assert chain.follows(str(root), code, "main", ITEM) is None

    def test_a_code_commit_after_it_and_an_unseen_commit_are_named(self, branch):
        root, code = branch
        write(root, "f.txt", "three\n")
        later = commit(root, "a fix nobody reviewed")
        found = chain.follows(str(root), code, "main", ITEM)
        assert found[0] == "after" and found[1] == later and found[2] == "f.txt"
        assert chain.follows(str(root), "0" * 40, "main", ITEM)[0] == "unseen"

    def test_another_items_records_and_a_commit_off_the_branch_are_named(self, branch):
        root, code = branch
        write(root, "seal/specs/1791999998-another-item/routing.md", "x\n")
        later = commit(root, "another work item's file")
        found = chain.follows(str(root), code, "main", ITEM)
        assert found[:2] == ("after", later)
        git(root, "switch", "-q", "main")
        write(root, "g.txt", "elsewhere\n")
        off = commit(root, "a commit the branch never had")
        git(root, "switch", "-q", "feature/x")
        assert chain.follows(str(root), off, "main", ITEM)[0] == "off"


# --- frame --------------------------------------------------------------------


class TestFrame:
    def declared(self):
        return {"planning": "framer", "review": "through the review chain"}

    def routing(self):
        return load(ROOT / "hooks" / "routing.py", "routing_for_chain_tests")

    def test_a_framed_item_with_a_reframe_by_the_framer_passes(self, branch):
        root, _code = branch
        write(
            root,
            f"{ITEM}/spec.md",
            SPEC + "Reframed 2026-10-16 by framer, after round 2.\n",
        )
        write(root, f"{ITEM}/plan.md", "# plan\n")
        commit(root, "frame")
        assert (
            chain.frame(reader, self.routing(), str(root), ITEM, self.declared()) == []
        )

    def test_a_missing_plan_and_a_reframe_by_another_party_are_named(self, branch):
        root, _code = branch
        write(
            root,
            f"{ITEM}/spec.md",
            SPEC + "Reframed 2026-10-16 by the session, after round 2.\n",
        )
        commit(root, "frame")
        problems = chain.frame(reader, self.routing(), str(root), ITEM, self.declared())
        assert any("plan.md" in p for p in problems)
        assert any("Reframed 2026-10-16 by the session" in p for p in problems)


# --- main: the arms over a pull request ---------------------------------------


class TestMain:
    def test_a_reviewed_branch_passes_a_ready_pull_request(self, branch, ready, capsys):
        """S11: the merged item's old-shape record, a finding open in it, is
        never opened — the check judges only what this pull request carries."""
        root, _code = branch
        code, out = check(root, capsys)
        assert code == 0, out
        assert MERGED_ITEM not in out

    def test_an_open_finding_fails_a_ready_pull_request(self, branch, ready, capsys):
        """S3 (T27): the `verdict:` lines decide, the line and the finding's
        heading are named, and a draft prints the same line and passes. A
        finding's `severity:` decides nothing."""
        root, code_sha = branch
        rel = f"{ITEM}/rounds/round-1.md"
        write(root, rel, record(code_sha, [finding(1, "open")]))
        commit(root, "the record, still open")
        code, out = check(root, capsys)
        assert code == 1
        line = next(ln for ln in out.splitlines() if "### 1." in ln)
        number = reader.readable(record(code_sha, [finding(1, "open")])).index(
            "verdict: open"
        )
        assert line.startswith(f"{rel}:{number + 1}"), line
        assert "### 1. the parser drops a row" in line
        assert (
            "reads `verdict: open`: the fix pass answers it with `fixed <commit>`, "
            "`answered` or `deferred <home>`"
        ) in line
        event = pathlib.Path(os.environ["GITHUB_EVENT_PATH"])
        event.write_text(
            json.dumps({"pull_request": {"draft": True}}), encoding="utf-8"
        )
        code, out = check(root, capsys)
        assert code == 0
        assert any("### 1." in ln and "verdict: open" in ln for ln in out.splitlines())
        event.write_text(
            json.dumps({"pull_request": {"draft": False}}), encoding="utf-8"
        )
        write(root, rel, record(code_sha, [finding(1, "answered")]))
        commit(root, "the record, answered at the most severe severity")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out

    def test_a_fixed_commit_head_does_not_descend_from_is_refused(
        self, branch, ready, capsys
    ):
        """S3 (T28): `fixed <commit>` names a commit on this branch. One this
        repository cannot resolve, and one on another branch, are refused by
        the finding's line and heading; the fixture's own code commit is not."""
        root, code_sha = branch
        git(root, "switch", "-q", "main")
        write(root, "g.txt", "elsewhere\n")
        off = commit(root, "a commit the branch never had")
        git(root, "switch", "-q", "feature/x")
        rel = f"{ITEM}/rounds/round-1.md"
        sections = [
            finding(1, "fixed 0000000"),
            finding(2, f"fixed {off[:8]}"),
            finding(3, f"fixed {code_sha[:8]}"),
        ]
        write(root, rel, record(code_sha, sections))
        commit(root, "the record, three fixes")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        named = [ln for ln in out.splitlines() if ln.startswith(f"{rel}:")]
        assert len(named) == 2, out
        assert "### 1." in named[0] and "`0000000`" in named[0]
        assert "### 2." in named[1] and f"`{off[:8]}`" in named[1]
        assert all("HEAD does not descend from" in ln for ln in named), named

    def test_a_fixed_commit_that_touches_nothing_of_the_finding_is_refused(
        self, branch, ready, capsys
    ):
        """S22 (T34): a `fixed <commit>` on the branch must change a path the
        finding's `location:` names, or one under it. A commit touching
        another path is refused naming the finding, the commit and what it
        touched; one touching one of two named paths, a file under a named
        directory, or a path the fix pass appended to the line passes, and so
        does the root commit, whose paths are read too. A path sharing a
        named directory's prefix is not under it."""
        root, code_sha = branch
        base = git(root, "rev-list", "--max-parents=0", "HEAD")
        made = {}
        for name, path in (
            ("g", "g.txt"),
            ("dir", "docs/x/y.md"),
            ("h", "h.txt"),
            ("near", "docs/xy.md"),
        ):
            write(root, path, f"{name}\n")
            made[name] = commit(root, f"touch {path}")[:8]
        rel = f"{ITEM}/rounds/round-1.md"
        sections = [
            finding(1, f"fixed {made['g']}"),
            finding(2, f"fixed {made['g']}", location="`f.txt:1`, `g.txt:3`"),
            finding(3, f"fixed {made['dir']}", location="`docs/x/`"),
            finding(4, f"fixed {made['dir']}", location="`docs/x`"),
            finding(5, f"fixed {made['h']}", location="`f.txt:1`, `h.txt`"),
            finding(6, f"fixed {base[:8]}", location="`f.txt`"),
            finding(7, f"fixed {made['near']}", location="`docs/x`"),
        ]
        write(root, rel, record(code_sha, sections))
        commit(root, "the record, seven fixes")
        write(
            root,
            f"{ITEM}/rounds/round-2.md",
            record(
                made["near"],
                confirmations="".join(confirm(f"round-1#{n}") for n in range(1, 8)),
                n=2,
            ),
        )
        commit(root, "the verifying round")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        named = [ln for ln in out.splitlines() if ln.startswith(f"{rel}:")]
        assert len(named) == 2, out
        assert "### 1." in named[0] and f"`{made['g']}`" in named[0], named
        assert "`g.txt`" in named[0] and "`f.txt`" in named[0], named
        assert "### 7." in named[1] and "`docs/xy.md`" in named[1], named
        assert all("touches no path" in ln for ln in named), named

    def test_the_last_records_fixed_or_answered_finding_owes_a_verifying_round(
        self, branch, ready, capsys
    ):
        """S23 (T37): on a ready pull request a `fixed` or `answered` finding
        in the last record fails as *a verifying round is owed*, since no
        round after it read the fix or the answer; a draft prints it and
        passes, and a last record of `deferred` findings, or of none, passes."""
        root, code_sha = branch
        git(root, "rm", "-q", f"{ITEM}/rounds/round-2.md")
        commit(root, "no verifying round")
        seal(root)
        rel = f"{ITEM}/rounds/round-1.md"
        code, out = check(root, capsys)
        assert code == 1
        line = next(ln for ln in out.splitlines() if ln.startswith(f"{rel}:"))
        assert "### 1." in line and chain.VERIFYING_ROUND in line, line
        event = pathlib.Path(os.environ["GITHUB_EVENT_PATH"])
        event.write_text(
            json.dumps({"pull_request": {"draft": True}}), encoding="utf-8"
        )
        code, out = check(root, capsys)
        assert code == 0 and chain.VERIFYING_ROUND in out
        event.write_text(
            json.dumps({"pull_request": {"draft": False}}), encoding="utf-8"
        )
        for found, closes in (
            ([finding(1, "answered")], False),
            ([finding(1, "deferred #9")], True),
            ([], True),
        ):
            write(root, rel, record(code_sha, found))
            commit(root, "the last record, again")
            seal(root)
            code, out = check(root, capsys)
            assert (code == 0) is closes, out
            assert (chain.VERIFYING_ROUND in out) is not closes, out

    def test_the_last_record_is_at_head_or_only_record_commits_follow(
        self, branch, ready, capsys
    ):
        """S4 (T12): a record commit after the last record passes; a code
        commit after it fails naming the commit and the verifying round."""
        root, _code = branch
        write(root, f"{ITEM}/overview.md", "# overview\n")
        commit(root, "a record commit")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out
        write(root, "f.txt", "three\n")
        later = commit(root, "a fix after the last round")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        assert later[:8] in out and "a verifying round is owed" in out

    def test_a_chain_with_no_record_fails_ready_and_prints_on_a_draft(
        self, tmp_path, monkeypatch, capsys, branch
    ):
        root, _code = branch
        git(root, "rm", "-rq", f"{ITEM}/rounds")
        commit(root, "no record")
        event = tmp_path / "e.json"
        event.write_text(
            json.dumps({"pull_request": {"draft": False}}), encoding="utf-8"
        )
        monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
        code, out = check(root, capsys)
        assert code == 1 and "holds no `round-N.md`" in out
        event.write_text(
            json.dumps({"pull_request": {"draft": True}}), encoding="utf-8"
        )
        code, out = check(root, capsys)
        assert code == 0 and "holds no `round-N.md`" in out

    def test_an_old_shape_record_under_the_declared_item_is_refused(
        self, branch, ready, capsys
    ):
        """S11: nothing reads the old table. A record of that shape under the
        item this pull request declares has no `## Findings`, and is refused
        by name rather than read as a record with nothing open."""
        root, code_sha = branch
        rel = f"{ITEM}/rounds/round-1.md"
        write(root, rel, OLD_RECORD.replace("0000000", code_sha))
        commit(root, "an old-shape record")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1
        assert f"{rel}:0" in out and chain.NO_FINDINGS in out

    def test_an_unclosed_fence_hiding_an_open_finding_fails_a_ready_pull_request(
        self, branch, ready, capsys
    ):
        """A fence the warden never closed hides the open finding below it;
        the check names the fence's opener rather than passing the record."""
        root, code_sha = branch
        rel = f"{ITEM}/rounds/round-1.md"
        text = record(
            code_sha,
            [
                finding(1, "answered").replace("answer: \n", "~~~python\n"),
                finding(2, "open"),
            ],
        )
        write(root, rel, text)
        commit(root, "a record with a fence left open")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1, out
        opener = text.splitlines().index("~~~python")
        assert f"{rel}:{opener + 1}" in out, out

    def test_a_broad_gate_file_naming_another_commit_fails_a_ready_pull_request(
        self, branch, ready, capsys
    ):
        """S5 (T15): the newest run must be HEAD or have only records after
        it; a stale run fails naming the file, and `--sealing` prints it."""
        root, _code = branch
        rel = f"{ITEM}/broad-gate.md"
        write(root, rel, gate_file("1" * 40))
        commit(root, "a run this repository cannot see")
        code, out = check(root, capsys)
        assert code == 1
        assert any(ln.startswith(f"{rel}:") for ln in out.splitlines())
        code, out = check(root, capsys, "--sealing")
        assert code == 0 and rel in out

    def test_a_straight_to_the_pr_item_owes_the_sealers_two_files(
        self, branch, ready, capsys
    ):
        root, _code = branch
        write(
            root,
            f"{ITEM}/routing.md",
            ROUTING.format(review="straight to the PR", planning="the session"),
        )
        git(
            root,
            "rm",
            "-rq",
            f"{ITEM}/rounds",
            f"{ITEM}/broad-gate.md",
            f"{ITEM}/guarantee.md",
        )
        commit(root, "direct, and no run")
        code, out = check(root, capsys)
        assert code == 1 and "broad-gate.md" in out and "guarantee.md" in out
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out

    def test_an_unreadable_declaration_fails_and_none_passes(
        self, branch, ready, capsys
    ):
        root, _code = branch
        write(root, f"{ITEM}/routing.md", "# nothing to read\n")
        commit(root, "garbled")
        code, out = check(root, capsys)
        assert code == 1 and "not a readable declaration" in out
        git(root, "rm", "-rq", ITEM)
        commit(root, "no work item")
        code, out = check(root, capsys)
        assert code == 0 and "declared neither way" in out

    def test_a_release_pull_request_leaves_a_squashed_item_to_its_own_pull_request(
        self, branch, ready, capsys, monkeypatch
    ):
        """Q7: a pull request into `main` from the release branch carries every
        item squashed into it, whose records name commits the squash orphaned.
        Each was judged at the pull request that carried it, so the release
        pull request passes and names each item it left with its squash."""
        root, _code = branch
        released(root)
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        code, out = check(root, capsys)
        assert code == 0, out
        line = next(ln for ln in out.splitlines() if f"{ITEM}/routing.md" in ln)
        assert "judged at its own pull request" in line and "(#7)" in line
        assert "does not descend from" not in out
        # A declaration naming the head branch is judged however it arrived.
        monkeypatch.setenv("GITHUB_HEAD_REF", "feature/x")
        code, out = check(root, capsys)
        assert code == 1 and "does not descend from" in out
        assert "judged at its own pull request" not in out

    def test_an_item_the_release_pull_requests_own_commit_changes_is_judged(
        self, branch, ready, capsys, monkeypatch
    ):
        """Q7: a commit made on the release branch itself is the release pull
        request's own, so the declaration it changed is judged there."""
        root, _code = branch
        released(root)
        monkeypatch.setenv("GITHUB_HEAD_REF", RELEASE)
        rel = f"{ITEM}/routing.md"
        write(root, rel, (root / rel).read_text(encoding="utf-8") + "\nA note.\n")
        commit(root, "a change on the release branch itself (#8)")
        code, out = check(root, capsys)
        assert code == 1
        assert "does not descend from" in out
        assert "judged at its own pull request" not in out

    def test_a_baseline_that_does_not_resolve_is_exit_2(self, branch, capsys):
        root, _code = branch
        code = chain.main(["--baseline", "no-such-ref", "--root", str(root)])
        assert code == 2
        assert "does not resolve" in capsys.readouterr().err


# --- retired ------------------------------------------------------------------

OLD_ITEM = "seal/specs/1788000000-an-earlier-item"


def remove_an_earlier_item(root, marker):
    """Declare an earlier work item on `main`, bring it into the branch, and
    remove its directory there, with or without the `docs/` marker a fold
    writes."""
    git(root, "switch", "-q", "main")
    # Close enough to the branch's own declaration for git's rename detection
    # to pair the two, which `changed` reads without.
    write(
        root,
        f"{OLD_ITEM}/routing.md",
        ROUTING.format(review="straight to the PR", planning="the session"),
    )
    # A spec at the merge base keeps the rule arm (`retired_by_rule`) from
    # excusing the removal, so only the marker can.
    write(root, f"{OLD_ITEM}/spec.md", "# a spec\n\nA rule.\n")
    commit(root, "an earlier item, declared")
    git(root, "switch", "-q", "feature/x")
    git(root, "merge", "-q", "--no-edit", "main")
    git(root, "rm", "-rq", OLD_ITEM)
    if marker:
        write(
            root,
            "docs/policy.md",
            "<!-- specs/1788000000-an-earlier-item -->\nA rule.\n",
        )
    commit(root, "the earlier item leaves")


class TestRetired:
    def test_a_declaration_a_fold_retired_is_not_one_this_branch_made(
        self, branch, draft, capsys
    ):
        """A `routing.md` that `settle --retire` removed is a deletion in the
        diff, and the work item it declared was reviewed at its own pull
        request; the `docs/` marker is what tells it from a deletion."""
        root, _code = branch
        remove_an_earlier_item(root, marker=True)
        _code, out = check(root, capsys)
        assert "retired:" in out and "1788000000-an-earlier-item" in out
        assert "does not carry this file at HEAD" not in out

    def test_a_declaration_deleted_with_nothing_absorbing_it_is_refused(
        self, branch, draft, capsys
    ):
        root, _code = branch
        remove_an_earlier_item(root, marker=False)
        _code, out = check(root, capsys)
        assert "does not carry this file at HEAD" in out
        assert "retired:" not in out
