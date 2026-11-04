"""`skills/settle/scripts/settle.py`, one class per function.

`settle` reads before it removes: what counts as released and the root it
refuses (#458, closing #83). Its dry run groups the released specs whose
`## Rule changes` name one section, in merge order, lists the specs to read
whole and every open row, and refuses nothing; `--apply` removes each
released directory whose record holds no open row in the working tree and
writes no policy document (#1033), and where the root is shared keeps one
whose version's published note does not carry its entry, read from a `gh`
stub's release list (#1139). In local mode it reads the root under the
git directory and asks `gh` which pull request merged from each work item's
branch (#955). A file in a work item's directory named like a record it
reads, at another path, is named by both arms as not read and decides
nothing (#1126); `Test_misplaced` holds the walk that finds it. With
`--from`, the dry run lists every document of each directory a person
names and writes nothing there (#1054). With `--draft`, it writes every
released operation into the policy root in merge order and names each one
not placed (#1217).
`Test_report` and `Test_apply` drive the
two arms over the `tree` fixture's history; `Test_main` runs the command over
a repository whose merge order git holds, and over a local root with a `gh`
stub on PATH. `Test_module` holds the loader, the
launcher, the answer the command takes from `rule_changes.py#order`, asked
over the repositories this file builds, the copy run without its siblings,
and `SPECS` held under `seal/`.

#942's phase 6 placed these cases from
`tests/text/test_settle_reads_before_it_removes.py` and
`tests/behaviour/test_settle_applies_rule_changes_in_place.py`, which keep the cases
that read the skill, the documents, the READMEs, the checklist and the cheat
sheets. The copy's case came from `tests/test_a_script_copied_alone_exits_2.py`
and the `SPECS` case from `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`
in #942's round 9 fix pass, each a case of this module alone.
"""

import io
import json
import os
import subprocess
import sys

import pytest
from conftest import (
    DOC,
    ROOT,
    census_case,
    line_of,
    load_module,
    mark_root,
    names_path,
    op,
    spec,
    symlink_or_skip,
    write,
)
from conftest import flattened as flat

TARGET = "skills/settle/scripts/settle.py"

SCRIPT = os.path.join(ROOT, "skills", "settle", "scripts", "settle.py")

settle = load_module(SCRIPT, "settle")
rules = load_module(
    os.path.join(ROOT, "skills", "settle", "scripts", "rule_changes.py"),
    "agentic_rule_changes",
)


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
    ).stdout


def item(repo, name, changes):
    path = repo / "seal" / "threads" / name
    (path / "frame").mkdir(parents=True, exist_ok=True)
    (path / "frame" / "design.md").write_text(spec(changes), encoding="utf-8")


def commit(repo, message):
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", message)


def stamp(repo):
    """HEAD's short hash and date, as the named-directory listing prints a
    commit."""
    return git(repo, "log", "-1", "--format=%h %cs").strip()


@pytest.fixture
def repo(tmp_path):
    repo = tmp_path / "repo"
    (repo / "docs").mkdir(parents=True)
    (repo / "docs" / "a.md").write_text(DOC, encoding="utf-8")
    mark_root(repo / "seal")
    git(repo, "init", "-q", "-b", "main")
    git(repo, "config", "user.email", "x@example.com")
    git(repo, "config", "user.name", "x")
    commit(repo, "base")
    return repo


def files(repo):
    return {
        str(p.relative_to(repo)): p.read_bytes()
        for p in repo.rglob("*")
        if p.is_file() and ".git" not in p.parts
    }


def dry_run(repo, capfd, *args):
    code = settle.main(["--root", str(repo), "--released-at", "main", *args])
    out = capfd.readouterr()
    return code, out.out + out.err


def apply(repo, capfd):
    return dry_run(repo, capfd, "--apply")


def specs_dir(repo, name):
    return repo / "seal" / "threads" / name


def group_text(text, n=1):
    """The lines of the dry run's group N."""
    return text.split(f"\ngroup {n}\n")[1].split("\n\n")[0]


OPEN = (
    "# x — overview\n\n## Not verified\n\n| Item | Who must answer |\n"
    "|---|---|\n| a claim nobody ran | the repository owner |\n"
)


def configure(repo, *rows):
    table = "".join(f"| {item} | {value} |\n" for item, value in rows)
    (repo / "seal" / "config.md").write_text(
        f"| Item | Value |\n|---|---|\n{table}", encoding="utf-8"
    )


def no_rule(repo, work_item_id):
    """Give a released spec a `## Rule changes` that changes nothing, and
    commit it."""
    path = repo / "seal" / "threads" / work_item_id / "frame" / "design.md"
    path.write_text(
        path.read_text(encoding="utf-8")
        + "\n## Rule changes\n\n- nothing\n  why: a moment.\n",
        encoding="utf-8",
    )
    git(repo, "add", "--", f"seal/threads/{work_item_id}")
    git(repo, "commit", "-qm", f"{work_item_id} states no rule")


def run(repo, *args):
    """`(exit code, what a person reads)`."""
    out = io.StringIO()
    found = settle.survey(str(repo), "HEAD")
    assert found is not None, "the fixture's HEAD does not resolve"
    if "--apply" in args:
        code = settle.apply(found, str(repo), out=out)
    else:
        code = settle.report(found, "HEAD", out=out)
    return code, out.getvalue()


OVERVIEW_OPEN = """# x — overview

## Not verified

| Item | Who must answer |
|---|---|
| a claim nobody ran | the repository owner |
"""


OVERVIEW_CLOSED = """# x — overview

## Not verified

| Item | Who must answer |
|---|---|
| closed a claim | run on 2026-01-01 |
"""


MOMENT = "1700000006-release-0-1-0"


def moment(repo, name=MOMENT, overview=None):
    """A released work item below the SDD ladder: a routing declaration and
    perhaps a memo, and no `frame/design.md`. Committed on its own path, so the
    unreleased `delta` the fixture leaves on disk stays unreleased."""
    item = repo / "seal" / "threads" / name
    item.mkdir(parents=True)
    (item / "routing.md").write_text(f"# {name} — routing\n", encoding="utf-8")
    if overview is not None:
        (item / "gaps.md").write_text(overview, encoding="utf-8")
    git(repo, "add", "--", f"seal/threads/{name}")
    git(repo, "commit", "-qm", f"released {name}")
    return item


def released_item(repo, name, held):
    """A released work item holding HELD, `{path in its directory: text}`,
    committed on its own path like `moment`."""
    path = repo / "seal" / "threads" / name
    for rel, text in held.items():
        write(path, rel, text)
    git(repo, "add", "--", f"seal/threads/{name}")
    git(repo, "commit", "-qm", f"released {name}")
    return path


def judgments_plan(rows, heading="## Judgments of the run"):
    """A `frame/plan.md` whose HEADING, on line 3, holds ROWS under the
    exact *Judgments of the run* header."""
    table = "".join(f"| {' | '.join(row)} |\n" for row in rows)
    return (
        f"# Implementation Plan: x\n\n{heading}\n\n"
        "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n" + table
    )


def removed_plan(repo, name, plan, added, removed, tag=None):
    """A work item whose PLAN a commit with subject ADDED adds, TAG holds
    where given, and a commit with subject REMOVED deletes with its
    directory, as an earlier settle's `--apply` leaves it. `(adding commit,
    removing commit's short hash)`."""
    write(repo / "seal" / "threads" / name, "frame/plan.md", plan)
    commit(repo, added)
    adding = git(repo, "rev-parse", "HEAD").strip()
    if tag:
        git(repo, "tag", tag)
    git(repo, "rm", "-rq", f"seal/threads/{name}")
    commit(repo, removed)
    return adding, git(repo, "rev-parse", "--short", "HEAD").strip()


def not_read(name, rel, place):
    """The line naming a misplaced record file, as the dry run and `--apply`
    print it."""
    return f"seal/threads/{name}/{rel}, named like `{place}` and away from its place"


def docs_text(repo):
    return {p.name: p.read_text(encoding="utf-8") for p in (repo / "docs").glob("*")}


# The branch the release merges to, in the fixtures below. A name that
# appears nowhere else in the output, so the assertions on it read the base
# and nothing else.
BASE = "release-target"


def at(repo, ref, *args):
    """`(exit code, what a person reads)` for `survey` at `ref`, the way
    `main` reaches it with `--released-at ref`."""
    out = io.StringIO()
    found = settle.survey(str(repo), ref)
    assert found is not None, f"{ref} does not resolve in the fixture"
    if "--apply" in args:
        code = settle.apply(found, str(repo), out=out)
    else:
        code = settle.report(found, ref, out=out)
    return code, out.getvalue()


def closed_after_base(repo):
    """The moment released with its row open at `BASE`, and a later commit on
    the working branch closing it — the 0.15.3 shape, where the closure
    reached the release branch and not `main`."""
    moment(repo, overview=OVERVIEW_OPEN)
    git(repo, "branch", BASE)
    (repo / "seal" / "threads" / MOMENT / "gaps.md").write_text(
        OVERVIEW_CLOSED, encoding="utf-8"
    )
    git(repo, "add", "--", f"seal/threads/{MOMENT}")
    git(repo, "commit", "-qm", "close the row")


def settled_repo(tmp_path, keep_empty_dir):
    """A repository whose settle is complete: a `seal/` root with its README,
    and `seal/threads/` either empty on disk — the tree `--apply` leaves — or
    absent, which is what a fresh checkout of that commit has."""
    repo = tmp_path / "repo"
    (repo / "docs").mkdir(parents=True)
    (repo / "docs" / "one-root.md").write_text("# a policy\n", encoding="utf-8")
    mark_root(repo / "seal")
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "x@example.com")
    git(repo, "config", "user.name", "x")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "settled")
    if keep_empty_dir:
        (repo / "seal" / "threads").mkdir()
    return repo


# --- a root in local mode, and the `gh` it asks (#955) ----------------------
#
# The local cases run `main` in process, with a `gh` stub first on PATH that
# answers `gh pr list --head <branch>` from a file beside it and logs every
# call. The suite runs with `gh` logged out (`tests/conftest.py`), so no local
# case reaches the real one.

GH_STUB = """import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]
with open(os.path.join(HERE, "calls.jsonl"), "a", encoding="utf-8") as f:
    f.write(json.dumps(args) + "\\n")
try:
    with open(os.path.join(HERE, "answers.json"), encoding="utf-8") as f:
        answers = json.load(f)
except OSError:
    answers = {}
if "fail" in answers:
    sys.stderr.write(answers["fail"] + "\\n")
    sys.exit(4)
if "raw" in answers:
    sys.stdout.write(answers["raw"] + "\\n")
    sys.exit(0)
if args[:1] == ["api"]:
    sys.stdout.write(answers.get("api", "[]") + "\\n")
    sys.exit(0)
branch = args[args.index("--head") + 1] if "--head" in args else ""
sys.stdout.write(json.dumps(answers.get("branches", {}).get(branch, [])) + "\\n")
"""


class Gh:
    """A `gh` on PATH that answers each branch as `merged` says, or fails."""

    def __init__(self, home):
        self.home = home
        self.answers = {"branches": {}}
        self.write()

    def write(self):
        (self.home / "answers.json").write_text(
            json.dumps(self.answers), encoding="utf-8"
        )

    def merged(self, branch, *prs):
        """BRANCH's merged pull requests, `(number, merge commit)` each; a
        merge commit of None is a pull request listed with none."""
        self.answers["branches"][branch] = [
            {"number": n, "mergeCommit": None if oid is None else {"oid": oid}}
            for n, oid in prs
        ]
        self.write()

    def fail(self, message):
        """Exit non-zero with MESSAGE on stderr."""
        self.answers["fail"] = message
        self.write()

    def say(self, raw):
        """Exit 0 with RAW on stdout, whatever was asked."""
        self.answers["raw"] = raw
        self.write()

    def releases(self, *pages):
        """Answer `gh api` with PAGES, each a list of releases, one JSON
        array after another, the way `--paginate` prints them."""
        self.answers["api"] = "".join(json.dumps(page) for page in pages)
        self.write()

    def calls(self):
        log = self.home / "calls.jsonl"
        if not log.exists():
            return []
        return [json.loads(x) for x in log.read_text(encoding="utf-8").splitlines()]


@pytest.fixture
def gh(tmp_path, monkeypatch):
    home = tmp_path / "gh-stub"
    home.mkdir()
    script = home / "gh_stub.py"
    script.write_text(GH_STUB, encoding="utf-8")
    if os.name == "nt":
        (home / "gh.cmd").write_text(
            f'@"{sys.executable}" "{script}" %*\r\n', encoding="utf-8"
        )
    else:
        stub = home / "gh"
        stub.write_text(
            f'#!/bin/sh\nexec "{sys.executable}" "{script}" "$@"\n', encoding="utf-8"
        )
        stub.chmod(0o755)
    monkeypatch.setenv("PATH", str(home) + os.pathsep + os.environ["PATH"])
    return Gh(home)


# Why a local work item that names no branch is unreleased, as a person reads
# it: a file `hooks/lib/routing.py#parse` does not read names none, whatever rows
# it holds.
NO_BRANCH = (
    "no `routing.md` that `hooks/lib/routing.py` reads as a declaration names a "
    "branch, so `gh` was not asked"
)

ROUTED = """# {name} — routing

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Branch | {branch} |
"""


@pytest.fixture
def local(tmp_path):
    """A repository whose `seal/` root is under its git directory, with
    `docs/a.md` committed on `main` and no work item yet."""
    repo = tmp_path / "repo"
    (repo / "docs").mkdir(parents=True)
    (repo / "docs" / "a.md").write_text(DOC, encoding="utf-8")
    git(repo, "init", "-q", "-b", "main")
    git(repo, "config", "user.email", "x@example.com")
    git(repo, "config", "user.name", "x")
    commit(repo, "base")
    (mark_root(repo / ".git" / "seal") / "threads").mkdir()
    return repo


def local_dir(repo, name):
    return repo / ".git" / "seal" / "threads" / name


def local_item(repo, name, branch=None, changes=None, overview=None):
    """A local work item: a `routing.md` naming BRANCH where one is given,
    a `frame/design.md` holding CHANGES where they are given, and an overview."""
    path = local_dir(repo, name)
    path.mkdir(parents=True)
    if branch is not None:
        text = ROUTED.format(name=name, branch=branch)
        (path / "routing.md").write_text(text, encoding="utf-8")
    if changes is not None:
        (path / "frame").mkdir()
        (path / "frame" / "design.md").write_text(spec(changes), encoding="utf-8")
    if overview is not None:
        (path / "gaps.md").write_text(overview, encoding="utf-8")
    return path


def merge(repo, branch, into="main"):
    """Merge a commit of BRANCH into INTO with a merge commit, the way a pull
    request from BRANCH merges, and return the merge commit."""
    git(repo, "switch", "-q", into)
    git(repo, "switch", "-qc", branch)
    work = repo / "work"
    work.mkdir(exist_ok=True)
    (work / f"{branch.replace('/', '-')}.txt").write_text(branch, encoding="utf-8")
    commit(repo, f"work of {branch}")
    git(repo, "switch", "-q", into)
    git(repo, "merge", "-q", "--no-ff", "-m", f"merge {branch}", branch)
    return git(repo, "rev-parse", "HEAD").strip()


# --- the published note `--apply` reads where the root is shared (#1139) ----


def fragment(repo, name, subject, tag=None, text=None):
    """A released work item whose `changelog.md`, holding TEXT or a line of
    its own, the commit SUBJECT adds on the current branch, tagged TAG where
    one is given; its directory."""
    if text is None:
        text = f"- what {name} changed\n"
    write(specs_dir(repo, name), "changelog.md", text)
    commit(repo, subject)
    if tag is not None:
        git(repo, "tag", tag)
    return specs_dir(repo, name)


def release(tag, body="", draft=False):
    """One release as `gh api repos/{owner}/{repo}/releases` lists it."""
    return {"tag_name": tag, "draft": draft, "body": body}


# The one call `--apply` makes for the release list, as the stub logs it.
RELEASES_CALL = ["api", "--paginate", "repos/{owner}/{repo}/releases?per_page=100"]
RELEASES_ASKED = "`gh api --paginate repos/{owner}/{repo}/releases?per_page=100`"


class Test_tracked_text:
    def test_accepts_each_tracked_text_file_and_no_untracked_one(self, repo):
        """The citations are read from what git tracks, so a file nobody
        committed is no reader and cites nothing."""
        (repo / "notes.txt").write_text("untracked\n", encoding="utf-8")
        tracked = ("docs/a.md", "seal/README.md")
        assert dict(settle.tracked_text(str(repo))) == {
            rel: (repo / rel).read_bytes().decode("utf-8") for rel in tracked
        }

    def test_refuses_a_file_under_the_work_items_and_a_binary_file(self, repo):
        """Guards s4 of #1017: a work item's own files are what `--apply`
        removes, so none of them is read as a path citing into it, and a file
        holding a NUL byte is binary and skipped."""
        item(repo, "1700000001-alpha", "- nothing\n  why: a reason.")
        (repo / "b.bin").write_bytes(b"a\0b")
        commit(repo, "a work item and a binary file")
        assert [rel for rel, _ in settle.tracked_text(str(repo))] == [
            "docs/a.md",
            "seal/README.md",
        ]


class Test_citations:
    def test_accepts_a_line_citing_a_work_item_twice_as_one_citation(self, repo):
        """A `tests/` file that reads `seal/threads` is a reader, and its line
        citing a work item twice is one citation."""
        (repo / "tests").mkdir()
        (repo / "tests" / "test_reads.py").write_text(
            'SPECS = "seal/threads"\n'
            'A = "seal/threads/1700000001-alpha/frame/design.md seal/threads/1700000001-alpha/plan.md"\n',
            encoding="utf-8",
        )
        commit(repo, "a reader")
        assert settle.citations(str(repo), ["1700000001-alpha"]) == (
            {"1700000001-alpha": ["tests/test_reads.py:2"]},
            ["tests/test_reads.py"],
        )

    def test_refuses_a_tests_file_naming_specs_alone_as_a_reader(self, repo):
        """Guards s5 of #1017: a `tests/` file naming a team's own `specs`
        reads nothing `--apply` removes, so it owes no answer before the
        directories go."""
        (repo / "tests").mkdir()
        (repo / "tests" / "test_team.py").write_text(
            'TEAM = "specs"\n', encoding="utf-8"
        )
        commit(repo, "a team's reader")
        assert settle.citations(str(repo), ["1700000001-alpha"]) == (
            {"1700000001-alpha": []},
            [],
        )


class Test_report:
    def test_accepts_a_spec_with_no_rule_changes_and_lists_it_to_read_whole(self, tree):
        """S4's dry run half: a spec with no section joins no group, so the
        settling session reads it whole; it is not left in place."""
        code, text = run(tree)
        assert code == 0, text
        listed = text.split(settle.WHOLE_HEADING)[1].split("\n\n")[0] + "\n"
        for name in ("1700000001-alpha", "1700000002-beta", "1700000003-gamma"):
            where = f"seal/threads/{name}/frame/design.md"
            assert f"    {name}  {where}  {settle.NO_SECTION}\n" in listed, text
        assert "released at HEAD: 3 work items; 1 unreleased and untouched\n" in (
            text
        ), text

    def test_refuses_nothing_and_writes_and_removes_nothing(self, tree):
        """The dry run holds nothing back: a section that does not parse and
        an open row are shown at exit 0, and the tree is left as it was."""
        (
            tree / "seal" / "threads" / "1700000001-alpha" / "frame" / "design.md"
        ).write_text(
            spec("- rename\n  file: docs/one-root.md\n  to: x"), encoding="utf-8"
        )
        git(tree, "add", "--", "seal/threads/1700000001-alpha")
        git(tree, "commit", "-qm", "alpha does not parse")
        moment(tree, overview=OVERVIEW_OPEN)
        before = sorted(
            str(p.relative_to(tree)) for p in tree.rglob("*") if p.is_file()
        )
        code, text = run(tree)
        after = sorted(str(p.relative_to(tree)) for p in tree.rglob("*") if p.is_file())
        assert before == after, "the report touched the tree"
        assert code == 0, text
        assert "refused" not in text and "kept" not in text, text
        assert "Nothing was written and nothing was removed" in text, text

    def test_lists_a_design_with_a_line_its_reader_did_not_read_to_read_whole(
        self, tree
    ):
        """Round 6 of #1167, finding 1: a design holding `## Rule changes` and
        a heading near it parses, with the near heading in `unread`, and an
        item under that heading no group would hold. The dry run lists the
        design to read whole, at the near heading's line with the reader's
        reason, and neither groups its other item nor calls it a design with
        nothing to write. Seen red against the design grouped with one of
        its two items, and the no-change one listed as having nothing to
        write."""
        change = (
            "- change\n  file: docs/one-root.md\n  section: S\n"
            "  from: old.\n  to: new.\n"
        )
        designs = {
            "1700000001-alpha": spec(change) + f"\n## Rule Changes\n\n{change}",
            "1700000002-beta": spec("- nothing\n  why: a reason.")
            + f"\n## Rule Changes\n\n{change}",
        }
        for name, text in designs.items():
            (tree / "seal" / "threads" / name / "frame" / "design.md").write_text(
                text, encoding="utf-8"
            )
            git(tree, "add", "--", f"seal/threads/{name}")
        git(tree, "commit", "-qm", "two designs with a heading near the section's")
        code, text = run(tree)
        assert code == 0, text
        listed = text.split(settle.WHOLE_HEADING)[1].split("\n\n")[0] + "\n"
        for name, design in designs.items():
            where = f"seal/threads/{name}/frame/design.md:"
            where += str(line_of(design, "## Rule Changes"))
            said = "`## Rule Changes` opens like `## Rule changes` and is not it"
            assert f"    {name}  {where}  {said}" in listed, text
        assert "1. change  1700000001-alpha" not in text, text
        nothing = text.split("no-change block (")[-1].split("\n\n")[0]
        assert "1700000002-beta" not in nothing, text

    def test_an_unreleased_work_item_is_not_a_candidate(self, tree):
        """Released means present on the branch the release merges to, so this
        branch's own work item is outside the corpus entirely."""
        _, text = run(tree)
        assert "1700000004-delta" not in text, text
        assert "1 unreleased and untouched" in text, text

    def test_a_released_work_item_whose_id_is_not_ascii_is_a_candidate(self, tree):
        """#1283. `released` reads the ref's tree with `-z`, so a work item
        id that holds a character git quotes under the default
        `core.quotePath` is released where its directory stands. Seen red
        against the listing without `-z`, where the item read as unreleased."""
        name = "1700000006-정렬"
        moment(tree, name=name, overview=OVERVIEW_CLOSED)
        code, text = run(tree)
        assert code == 0, text
        assert "released at HEAD: 4 work items; 1 unreleased and untouched\n" in (
            text
        ), text
        stated = text.split("no `frame/design.md`, so no rule stated:\n")[1]
        assert stated.split("\n\n")[0] == f"    {name}", text

    def test_a_spec_less_directory_is_listed_as_stating_no_rule(self, tree):
        """D3: a directory with no `frame/design.md` states no rule, so it is listed
        apart from the specs, and its record's rows with every other's."""
        moment(tree, overview=OVERVIEW_CLOSED)
        code, text = run(tree)
        assert code == 0, text
        stated = text.split("no `frame/design.md`, so no rule stated:\n")[1].split(
            "\n\n"
        )[0]
        assert stated == f"    {MOMENT}", text
        assert MOMENT not in text.split(settle.WHOLE_HEADING)[1].split("\n\n")[0]

    def test_every_open_row_is_listed_with_the_paths_it_names(self, tree):
        """The open rows are a report the settling session decides from, so
        each carries the backticked paths it names and whether each is in the
        working tree, a bare file name found as a tracked file's name or in
        the work item's own directory."""
        row = (
            "the run of `docs/one-root.md` and `gone/away.py` at "
            "`tests/x.py::Test_y`, per `questions.md`, `one-root.md` and `cmd.exe`"
        )
        moment(tree, overview=OVERVIEW_OPEN.replace("a claim nobody ran", row))
        (tree / "seal" / "threads" / MOMENT / "questions.md").write_text(
            "# q\n", encoding="utf-8"
        )
        code, text = run(tree)
        assert code == 0, text
        rows = text.split(f"{settle.ROWS_HEADING}\n")[1].split("\n\n")[0]
        assert rows == (
            f"    {MOMENT}\n"
            f"        open in gaps.md: {row}\n"
            "            `docs/one-root.md` in the tree\n"
            "            `gone/away.py` not in the tree\n"
            "            `tests/x.py` not in the tree\n"
            "            `questions.md` in the tree\n"
            "            `one-root.md` in the tree"
        ), text
        assert "1 open row in 1 record\n" in text, text

    def test_the_report_lists_what_an_apply_would_remove(self, tree):
        """D1's table: the command reports by itself the paths outside
        `seal/threads/` that cite into what `--apply` would remove, and the
        `tests/` files that read `seal/threads` — what #514's frame found by
        hand. A directory still holding a row is listed with when it goes."""
        no_rule(tree, "1700000001-alpha")
        moment(tree, overview=OVERVIEW_OPEN)
        (tree / "docs" / "cites.md").write_text(
            "See `seal/threads/1700000001-alpha/frame/design.md` for the decision.\n"
            f"And `seal/threads/{MOMENT[:11]}…/routing.md` for the moment.\n"
            "A marker <!-- specs/1700000002-beta --> and a bare 1700000002-beta.\n",
            encoding="utf-8",
        )
        (tree / "tests").mkdir()
        (tree / "tests" / "test_reads.py").write_text(
            'SPECS = "seal/threads"\n', encoding="utf-8"
        )
        git(tree, "add", "--", "docs", "tests")
        git(tree, "commit", "-qm", "citations")
        _, text = run(tree)
        takes = text.split(settle.REMOVES_HEADING)[1]
        assert "    seal/threads/1700000001-alpha/  now\n" in takes, text
        assert f"    seal/threads/{MOMENT}/  once its 1 open row close\n" in takes, text
        assert "docs/cites.md:1" in takes, text
        assert "docs/cites.md:2" in takes, "an abbreviated path is a citation too"
        beta = takes.split("seal/threads/1700000002-beta/")[1].split("seal/threads/")[0]
        assert "cited from" not in beta, "a marker or a bare id is not a path"
        assert "tests/test_reads.py" in text.split("checks that read")[1], text
        # Contract rule 14: the heading a person reads names the section that
        # says what each check owes, by its heading text. The citation the
        # settle's report prints, which the settling session resolves.
        assert (
            "(`skills/settle/SKILL.md` *Answer every check that reads the corpus*)"
        ) in " ".join(text.split()), text

    def test_names_a_gaps_md_away_from_its_place_as_not_read(self, tree):
        """S1 of #1126, #956's R31: a released work item whose only `gaps.md`
        is `trail/gaps.md`, holding an open row. The settle reads the record
        at its place alone, so the row is not counted; the dry run names the
        file in a section of its own, which says who opens it and what
        `--apply` does with it, and refuses nothing. Seen red with the fix
        reverted in `settle.py`: the dry run named no file."""
        name = "1700000007-trail"
        released_item(tree, name, {"trail/gaps.md": OVERVIEW_OPEN})
        code, text = run(tree)
        assert f"seal/threads/{name}/trail/gaps.md" in text, text
        assert code == 0, text
        section = text.split(f"\n{settle.MISPLACED_HEADING}\n")[1].split("\n\n")[0]
        assert section == f"    {not_read(name, 'trail/gaps.md', 'gaps.md')}", text
        assert "0 open rows in 0 records\n" in text, text
        # Contract rule 14: the heading a person acts on is pinned.
        heading = flat(settle.MISPLACED_HEADING)
        assert heading.startswith("not read: each file named like a record the "), (
            heading
        )
        assert "settle reads, away from that record's place" in heading
        assert (
            "The settling session opens each one and decides each item in it "
            "that reads as an open row" in heading
        )
        assert (
            "`--apply` decides nothing on it and removes it with its directory"
            in heading
        )

    def test_names_a_misplaced_design_and_plan_as_not_read(self, tree):
        """S3 of #1126: the class is every file named like a record the settle
        reads, `gaps.md`, `frame/design.md` and `frame/plan.md`, at any other
        path of its directory, each named with the record it is named like.
        A record at its own place is not named. Seen red with the fix
        reverted in `settle.py`."""
        top = "1700000007-top-design"
        trail = "1700000008-trail-plan"
        released_item(tree, top, {"design.md": "# a design\n"})
        released_item(
            tree,
            trail,
            {"frame/plan.md": "# a plan\n", "trail/plan.md": "# a plan\n"},
        )
        code, text = run(tree)
        assert f"seal/threads/{top}/design.md" in text, text
        assert code == 0, text
        section = text.split(f"\n{settle.MISPLACED_HEADING}\n")[1].split("\n\n")[0]
        assert section == (
            f"    {not_read(top, 'design.md', 'frame/design.md')}\n"
            f"    {not_read(trail, 'trail/plan.md', 'frame/plan.md')}"
        ), text

    def test_prints_no_section_where_nothing_is_misplaced(self, tree):
        """S4 of #1126: every record at its place, so the section is not
        printed."""
        moment(tree, overview=OVERVIEW_OPEN)
        code, text = run(tree)
        assert code == 0, text
        assert settle.MISPLACED_HEADING not in text, text
        assert "named like" not in text, text


def records_in_place(tmp_path, name):
    """A work item directory under TMP_PATH holding the three records the
    settle reads, each at its place, and the `misplaced` reader."""
    top = tmp_path / "seal" / "threads" / name
    for rel in ("gaps.md", "frame/design.md", "frame/plan.md"):
        write(top, rel, "# x\n")
    return top, settle.load(settle.READER, "agentic_unverified_reader")


class Test_misplaced:
    def test_accepts_a_file_or_a_link_to_one_at_another_path(self, tmp_path):
        """*Scope* item 1 of #1126: a file named like a record, at any path
        but the record's own, is named with the record, as a regular file or
        as a link to one, and the records at their places are not. Seen red
        with the place test removed."""
        top, reader = records_in_place(tmp_path, "1700000001-a")
        (top / "x").mkdir()
        (top / "x" / "design.md").write_text("# x\n", encoding="utf-8")
        (top / "trail").mkdir()
        symlink_or_skip(top / "gaps.md", top / "trail" / "gaps.md")
        assert settle.misplaced(str(tmp_path), "1700000001-a", reader) == [
            ("trail/gaps.md", "gaps.md"),
            ("x/design.md", "frame/design.md"),
        ]

    def test_refuses_a_directory_a_link_to_nothing_and_another_spelling(self, tmp_path):
        """*Scope* item 1 of #1126: only the exact name of a file is read. A
        directory of that name, a link to nothing, another spelling and a
        longer name are not named, and a linked directory is not followed.
        Seen red with the walk following links, and with the file test
        removed."""
        top, reader = records_in_place(tmp_path, "1700000001-a")
        (top / "notes").mkdir()
        (top / "notes" / "Gaps.md").write_text("# x\n", encoding="utf-8")
        (top / "notes" / "gaps.md.bak").write_text("# x\n", encoding="utf-8")
        (top / "trail" / "plan.md").mkdir(parents=True)
        elsewhere = tmp_path / "elsewhere"
        elsewhere.mkdir()
        (elsewhere / "gaps.md").write_text("# x\n", encoding="utf-8")
        symlink_or_skip(elsewhere, top / "linked", directory=True)
        symlink_or_skip(tmp_path / "nowhere", top / "notes" / "plan.md")
        assert settle.misplaced(str(tmp_path), "1700000001-a", reader) == []


class Test_apply:
    def test_accepts_every_released_directory_with_no_open_row(self, tree):
        """S4's apply half: a spec holding the no-change block and specs with
        no `## Rule changes` leave alike, and the unreleased one stays."""
        no_rule(tree, "1700000001-alpha")
        code, text = run(tree, "--apply")
        assert code == 0, text
        for name in ("1700000001-alpha", "1700000002-beta", "1700000003-gamma"):
            assert not (tree / "seal" / "threads" / name).exists(), text
            assert f"removed seal/threads/{name}/\n" in text, text
        assert (tree / "seal" / "threads" / "1700000004-delta").exists(), text
        assert text.endswith(
            "\nremoved 3 directories; kept 0 with a row to close and 0 whose note "
            "lacks its entry\n"
        )

    def test_apply_leaves_a_team_specs_of_the_same_name_on_disk(self, tree):
        """#688 D3. A project's own `specs/` is read as history and never taken,
        even where a team directory carries the removed work item's very id: the
        removal is `seal/threads/` whatever else the tree holds (`SPECS`)."""
        team = tree / "specs" / "1700000001-alpha"
        team.mkdir(parents=True)
        (team / "design.md").write_text("# the team's design\n", encoding="utf-8")
        # exempt from old_names: another tool's own file, under a name the plugin once used
        (team / "spec.md").write_text("# the team's spec\n", encoding="utf-8")
        git(tree, "add", "-A")
        git(tree, "commit", "-qm", "a team directory of the same name")
        no_rule(tree, "1700000001-alpha")
        code, text = run(tree, "--apply")
        assert code == 0, text
        assert not (tree / "seal" / "threads" / "1700000001-alpha").exists()
        assert (team / "design.md").read_text(
            encoding="utf-8"
        ) == "# the team's design\n"
        # exempt from old_names: another tool's own file, under a name the plugin once used
        assert (team / "spec.md").is_file()

    def test_a_removed_record_prints_each_row_it_closed_and_writes_no_document(
        self, tree
    ):
        """What closed each row is copied into the settle's pull request body,
        so `--apply` prints it; the policy root is the settling session's."""
        moment(tree, overview=OVERVIEW_CLOSED)
        before = docs_text(tree)
        code, text = run(tree, "--apply")
        assert code == 0, text
        assert not (tree / "seal" / "threads" / MOMENT).exists(), text
        assert docs_text(tree) == before, "the apply wrote into docs/"
        assert (
            f"removed seal/threads/{MOMENT}/\n"
            "    no note read: HEAD holds no `changelog.md` in its directory\n"
            "    closed in gaps.md: a claim\n"
            "        what closed it: run on 2026-01-01\n"
        ) in text, text

    def test_an_open_row_keeps_its_directory_and_a_closure_on_disk_lets_it_go(
        self, repo, capfd
    ):
        """S3: the open row keeps the directory, named, at exit 1; closed in
        the working tree and not committed, the next `--apply` removes it,
        prints the row with what closed it, and exits 0. Nothing waits for
        the closure to reach a base."""
        item(repo, "1700000001-a", op("add", "S", new="Rule."))
        overview = specs_dir(repo, "1700000001-a") / "gaps.md"
        overview.write_text(OPEN, encoding="utf-8")
        commit(repo, "a")
        code, text = apply(repo, capfd)
        assert code == 1, text
        assert specs_dir(repo, "1700000001-a").exists(), text
        assert (
            "kept seal/threads/1700000001-a/: its record holds 1 open row; close "
            "each (`closed` with what closed it) and run `seal settle --apply` again\n"
            "    open in gaps.md: a claim nobody ran\n"
        ) in text, text
        overview.write_text(OVERVIEW_CLOSED, encoding="utf-8")
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not specs_dir(repo, "1700000001-a").exists(), text
        assert "    closed in gaps.md: a claim\n" in text, text
        assert (repo / "docs" / "a.md").read_text(encoding="utf-8") == DOC

    def test_a_closure_the_released_ref_has_not_seen_lets_the_directory_go(self, tree):
        """S3 at a base: the row is closed on the working branch and open at
        `--released-at`. The working tree is the fact `--apply` reads, so the
        directory goes (#602's base condition is gone)."""
        closed_after_base(tree)
        code, text = at(tree, BASE, "--apply")
        assert code == 0, text
        assert not (tree / "seal" / "threads" / MOMENT).exists(), text
        assert f"removed seal/threads/{MOMENT}/\n" in text, text

    def test_refuses_an_unreadable_memo_and_keeps_its_directory(self, tree):
        """A section this cannot read is a count it does not know, never zero."""
        moment(tree, overview="# x — overview\n\n## Not checked\n")
        code, text = run(tree, "--apply")
        assert code == 1, text
        assert (tree / "seal" / "threads" / MOMENT).exists(), text
        assert "cannot be read" in text, text

    def test_an_unreleased_spec_less_directory_is_not_a_candidate(self, tree):
        item = tree / "seal" / "threads" / MOMENT
        item.mkdir()
        (item / "routing.md").write_text("# routing\n", encoding="utf-8")
        _, text = run(tree, "--apply")
        assert item.exists(), text

    def test_removes_a_directory_whose_gaps_md_is_away_and_names_it(self, tree):
        """S1 of #1126, `--apply`: the directory goes on its record at its
        place, which it does not have, and the `removed` line is followed by
        a `not read:` line naming `trail/gaps.md`; the exit code and the last
        line's counts are as before. Seen red with the fix reverted in
        `settle.py`: the directory went without a word."""
        name = "1700000007-trail"
        path = released_item(tree, name, {"trail/gaps.md": OVERVIEW_OPEN})
        code, text = run(tree, "--apply")
        assert f"not read: seal/threads/{name}/trail/gaps.md" in text, text
        assert code == 0, text
        assert not path.exists(), text
        assert (
            f"removed seal/threads/{name}/\n"
            "    no note read: HEAD holds no `changelog.md` in its directory\n"
            f"    not read: {not_read(name, 'trail/gaps.md', 'gaps.md')}\n"
        ) in text, text
        assert text.endswith(
            "\nremoved 4 directories; kept 0 with a row to close and 0 whose note "
            "lacks its entry\n"
        ), text

    def test_keeps_on_the_record_at_its_place_and_names_the_copy(self, tree):
        """S2 of #1126: a top-level `gaps.md` holding an open row and a
        `frame/gaps.md` holding none. The directory is kept on the top-level
        row, at exit 1, and the `kept` line's rows are followed by a `not
        read:` line naming the copy; the dry run's section follows its open
        rows. Seen red with the fix reverted in `settle.py`."""
        name = "1700000007-copy"
        path = released_item(
            tree, name, {"gaps.md": OVERVIEW_OPEN, "frame/gaps.md": OVERVIEW_CLOSED}
        )
        _, report = run(tree)
        assert f"seal/threads/{name}/frame/gaps.md" in report, report
        rows = report.index(f"\n{settle.ROWS_HEADING}\n")
        assert rows < report.index(f"\n{settle.MISPLACED_HEADING}\n"), report
        code, text = run(tree, "--apply")
        assert code == 1, text
        assert path.exists(), text
        assert (
            f"kept seal/threads/{name}/: its record holds 1 open row; close "
            "each (`closed` with what closed it) and run `seal settle --apply` again\n"
            "    open in gaps.md: a claim nobody ran\n"
            f"    not read: {not_read(name, 'frame/gaps.md', 'gaps.md')}\n"
        ) in text, text
        assert text.endswith(
            "\nremoved 3 directories; kept 1 with a row to close and 0 whose note "
            "lacks its entry\n"
        ), text


class Test_main:
    def test_two_specs_on_one_sentence_are_one_group_in_merge_order(self, repo, capfd):
        """S1: B was added after A on one line of history, so B is listed
        after A whatever their ids say. A's `from` no longer matches, since
        the section holds the sentence as A left it, and nothing is refused;
        with both records holding no row, `--apply` removes both and writes
        no document."""
        (repo / "docs" / "a.md").write_text(
            DOC.replace("old sentence.", "y."), encoding="utf-8"
        )
        commit(repo, "the section as A left it")
        item(repo, "1700000009-a", op("change", "S", "old sentence.", "y."))
        commit(repo, "a")
        item(repo, "1700000001-b", op("change", "S", "y.", "z."))
        commit(repo, "b")
        before = files(repo)
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert files(repo) == before, "the dry run wrote to the tree"
        assert "refused" not in text, text
        line = line_of(spec(op("change", "S", "y.", "z.")), "- change")
        assert group_text(text) == (
            "    place: docs/a.md section `S`, at docs/a.md:3-9\n"
            f"    1. change  1700000009-a  seal/threads/1700000009-a/frame/design.md:{line}"
            "  from not found, to found\n"
            f"    2. change  1700000001-b  seal/threads/1700000001-b/frame/design.md:{line}"
            "  from found, to not found"
        ), text
        assert "\ngroup 2\n" not in text, text
        docs = {k: v for k, v in files(repo).items() if k.startswith("docs")}
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not specs_dir(repo, "1700000009-a").exists(), text
        assert not specs_dir(repo, "1700000001-b").exists(), text
        assert {k: v for k, v in files(repo).items() if k.startswith("docs")} == docs

    def test_a_stale_from_is_listed_and_neither_refused_nor_waited_on(
        self, repo, capfd
    ):
        """S2: an operation whose `from` matches nothing, and one whose
        heading is not there, are history in their groups; a later spec at
        the same place is listed after them, and the directories go."""
        item(repo, "1700000001-a", op("change", "S", "not there.", "y."))
        item(repo, "1700000002-c", op("remove", "Nowhere"))
        commit(repo, "a and c")
        item(repo, "1700000003-b", op("add", "S", new="Rule."))
        commit(repo, "b")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert "refused" not in text and "waits" not in text, text
        first = group_text(text, 1)
        assert "1. change  1700000001-a" in first, text
        assert "from not found, to not found" in first, text
        assert "2. add  1700000003-b" in first and "to not found" in first, text
        assert group_text(text, 2).startswith(
            "    place: docs/a.md section `Nowhere`: no heading `Nowhere` in the "
            "working tree\n    1. remove  1700000002-c  "
        ), text
        assert group_text(text, 2).endswith("  the whole section"), text
        code, text = apply(repo, capfd)
        assert code == 0, text
        for name in ("1700000001-a", "1700000002-c", "1700000003-b"):
            assert not specs_dir(repo, name).exists(), text

    @pytest.mark.parametrize("section", ["S", "S child"])
    def test_two_specs_on_parallel_branches_at_one_place_are_one_group_unordered(
        self, repo, capfd, section
    ):
        """S5: ancestry cannot order them, so they are one group with the
        pair marked for the settling session to order by content, and nothing
        is refused. A sub-section is inside its section's range, so it is the
        same place."""
        git(repo, "switch", "-qc", "one")
        item(repo, "1700000001-a", op("change", "S", "old sentence.", "y."))
        commit(repo, "a")
        git(repo, "switch", "-q", "main")
        git(repo, "switch", "-qc", "two")
        item(repo, "1700000002-b", op("add", section, new="Rule."))
        commit(repo, "b")
        git(repo, "switch", "-q", "main")
        git(repo, "merge", "-q", "--no-ff", "-m", "one", "one")
        git(repo, "merge", "-q", "--no-ff", "-m", "two", "two")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert "refused" not in text, text
        group = group_text(text)
        assert "1700000001-a" in group and "1700000002-b" in group, text
        said = settle.UNORDERED.format(a="1700000001-a", b="1700000002-b")
        assert f"    {said}" in group, text
        assert "\ngroup 2\n" not in text, text

    def test_a_spec_that_joins_no_group_is_read_whole_and_goes(self, repo, capfd):
        """S4: a section that does not parse is listed to read whole with the
        reader's reason at its line, beside a spec with no section, and with
        no open row both leave."""
        bad = "- rename\n  file: docs/a.md\n  to: x"
        item(repo, "1700000001-a", bad)
        old = specs_dir(repo, "1700000002-old")
        (old / "frame").mkdir(parents=True)
        (old / "frame" / "design.md").write_text(
            "# old\n\n## Scope\n\nIn.\n", encoding="utf-8"
        )
        commit(repo, "a and old")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        whole = text.split(settle.WHOLE_HEADING)[1].split("\n\n")[0]
        line = line_of(spec(bad), "- rename")
        assert (
            f"    1700000001-a  seal/threads/1700000001-a/frame/design.md:{line}  `rename` "
            "is not one of"
        ) in whole, text
        assert (
            f"    1700000002-old  seal/threads/1700000002-old/frame/design.md  {settle.NO_SECTION}"
        ) in whole, text
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not specs_dir(repo, "1700000001-a").exists(), text
        assert not old.exists(), text

    def test_the_no_change_block_is_listed_with_no_section_to_write(self, repo, capfd):
        """A spec whose section is the no-change block states that no rule
        changes, so it joins no group and is listed under the block."""
        item(repo, "1700000001-a", "- nothing\n  why: a release entry.")
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert (
            "the no-change block (`- nothing`), so no section to write:\n"
            "    1700000001-a\n"
        ) in text, text
        assert "\ngroup 1\n" not in text, text

    def test_the_judgments_are_printed_by_the_document_each_stands_on(
        self, repo, capfd
    ):
        """#1167, *Scope* item 12: each released plan's *Judgments of the
        run*, read through `hooks/lib/config.py#gfm_table`, grouped by the
        `Judged against` cell in the order the work items are listed, with
        each work item's round count and each row's line. The template's
        empty row is no judgment, and a plan with no such section prints
        nothing for its work item."""
        run_doc = "`docs/running/the-run.md` *The run*"
        order = (
            "`skills/implement/orchestration.md` *Orchestrator: the order "
            "inside a ticket*"
        )
        plans = {
            "1700000001-a": (
                3,
                [
                    (
                        "2026-10-01",
                        "ended the rounds",
                        "round 3 found 2, round 2 found 2",
                        run_doc,
                    ),
                    ("", "", "", ""),
                ],
            ),
            "1700000002-b": (
                1,
                [
                    (
                        "2026-10-02",
                        "folded the owner's answer",
                        "the owner answered Q1",
                        order,
                    ),
                    (
                        "2026-10-03",
                        "sent a regression to the framer",
                        "the frame named the unit",
                        run_doc,
                    ),
                ],
            ),
        }
        lines = {}
        for name, (rounds, rows) in plans.items():
            item(repo, name, "- nothing\n  why: x.")
            table = "".join(f"| {' | '.join(row)} |\n" for row in rows)
            plan = (
                "# Implementation Plan: x\n\n## Phases\n\n"
                "| Phase | Delivers | Verified by | Status |\n|---|---|---|---|\n"
                "| 1 | a | b | c |\n\n## Judgments of the run\n\n"
                "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
                + table
            )
            (specs_dir(repo, name) / "frame" / "plan.md").write_text(
                plan, encoding="utf-8"
            )
            lines[name] = [
                line_of(plan, f"| {' | '.join(row)} |") for row in rows if row[0]
            ]
            held = specs_dir(repo, name) / "trail" / "rounds"
            held.mkdir(parents=True)
            for n in range(1, rounds + 1):
                (held / f"round-{n}.md").write_text("# round\n", encoding="utf-8")
        item(repo, "1700000003-c", "- nothing\n  why: x.")
        (specs_dir(repo, "1700000003-c") / "frame" / "plan.md").write_text(
            "# Implementation Plan: c\n\n## Phases\n", encoding="utf-8"
        )
        commit(repo, "a, b and c")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        block = text.split(f"\n{settle.JUDGMENTS_HEADING}\n")[1].split(
            f"\n\n{settle.REMOVES_HEADING}"
        )[0]
        a, b = lines["1700000001-a"], lines["1700000002-b"]
        assert block == (
            f"\njudged against: {run_doc}\n"
            "    1700000001-a  3 rounds\n"
            f"        frame/plan.md:{a[0]}  2026-10-01  ended the rounds\n"
            "            grounds: round 3 found 2, round 2 found 2\n"
            "    1700000002-b  1 round\n"
            f"        frame/plan.md:{b[1]}  2026-10-03  sent a regression to the framer\n"
            "            grounds: the frame named the unit\n"
            f"\njudged against: {order}\n"
            "    1700000002-b  1 round\n"
            f"        frame/plan.md:{b[0]}  2026-10-02  folded the owner's answer\n"
            "            grounds: the owner answered Q1"
        ), block
        assert "1700000003-c" not in block, block

    def test_a_judgments_section_it_cannot_read_is_named_and_refuses_nothing(
        self, repo, capfd
    ):
        """The core's rule for a script: a section that holds no table under
        the exact header is named as not read, and the dry run still exits 0
        and prints the rest."""
        item(repo, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(repo, "1700000001-a") / "frame" / "plan.md").write_text(
            "# Implementation Plan: a\n\n## Judgments of the run\n\n"
            "| Date | Judgment | Grounds |\n|---|---|---|\n| 2026-10-01 | x | y |\n",
            encoding="utf-8",
        )
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        block = text.split(f"\n{settle.JUDGMENTS_HEADING}\n")[1]
        assert block.startswith(
            "    1700000001-a  seal/threads/1700000001-a/frame/plan.md  not read: "
            "holds no `| Date | Judgment | Grounds | Judged against |` table\n"
        ), block
        assert "judged against:" not in block, block
        assert settle.REMOVES_HEADING in text, text

    @pytest.mark.parametrize("shape", ["file", "link", "unlistable"])
    def test_a_work_item_whose_rounds_cannot_be_listed_is_not_counted_as_none(
        self, repo, capfd, monkeypatch, shape
    ):
        """Round 9, finding 1. A `trail/rounds` that is a file, a link, or a
        directory nothing can list holds a review git carries
        (`hooks/lib/routing.py#rounds_unreadable`), so the dry run says it
        counted none rather than that none happened. The unlistable
        directory is made by refusing `os.listdir` on that one path, since
        `chmod 000` does not bar a runner that is root."""
        item(repo, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(repo, "1700000001-a") / "frame" / "plan.md").write_text(
            "# Implementation Plan: a\n\n## Judgments of the run\n\n"
            "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
            "| 2026-10-01 | x | y | z |\n",
            encoding="utf-8",
        )
        trail = specs_dir(repo, "1700000001-a") / "trail"
        trail.mkdir()
        if shape == "file":
            (trail / "rounds").write_text("# Review round 1\n", encoding="utf-8")
        elif shape == "link":
            held = repo / "elsewhere"
            held.mkdir()
            (held / "round-1.md").write_text("# Review round 1\n", encoding="utf-8")
            symlink_or_skip(held, trail / "rounds", directory=True)
        else:
            (trail / "rounds").mkdir()
            (trail / "rounds" / "round-1.md").write_text(
                "# Review round 1\n", encoding="utf-8"
            )
        commit(repo, "a")
        if shape == "unlistable":
            barred = os.path.normcase(os.path.realpath(trail / "rounds"))
            listdir = os.listdir

            def refusing(path="."):
                if os.path.normcase(os.path.realpath(path)) == barred:
                    raise PermissionError(13, "Permission denied", str(path))
                return listdir(path)

            monkeypatch.setattr(os, "listdir", refusing)
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert (
            "    1700000001-a  its trail/rounds is not a directory this can "
            "list, so no round was counted\n"
        ) in text, text
        assert " round\n" not in text and " rounds\n" not in text, text

    @pytest.mark.parametrize(
        "heading",
        [
            "## Judgments of the Run",
            "## judgments of the run",
            "### Judgments Of The Run",
        ],
    )
    def test_refuses_to_read_rows_under_a_heading_near_the_judgments_section(
        self, repo, capfd, heading
    ):
        """Round 9, finding 2. A heading whose letters, case folded, are the
        section's and that is not it is named at its line, and none of its
        rows is read: `--apply` removes the plan, so silence here loses the
        rows unread. Every live heading is the scope this reader scans."""
        item(repo, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(repo, "1700000001-a") / "frame" / "plan.md").write_text(
            f"# Implementation Plan: a\n\n{heading}\n\n"
            "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
            "| 2026-10-01 | x | y | z |\n",
            encoding="utf-8",
        )
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        block = text.split(f"\n{settle.JUDGMENTS_HEADING}\n")[1]
        assert block.startswith(
            "    1700000001-a  seal/threads/1700000001-a/frame/plan.md  not read: "
            f"line 3: `{heading}` opens like `## Judgments of the run` and is "
            "not it, so none of its rows were read\n"
        ), block
        assert "judged against:" not in block, block

    def test_accepts_a_near_heading_inside_a_fence_without_a_word(self, repo, capfd):
        """The edge of finding 2's scope: a heading inside a fence is no
        heading, so the reader names nothing for it."""
        fence = "`" * 3
        item(repo, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(repo, "1700000001-a") / "frame" / "plan.md").write_text(
            f"# Implementation Plan: a\n\n{fence}\n## Judgments of the Run\n{fence}\n",
            encoding="utf-8",
        )
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert settle.JUDGMENTS_HEADING not in text, text

    def test_accepts_a_near_heading_inside_a_comment_without_a_word(self, repo, capfd):
        """Round 10's edge of round 9's finding 2: a heading inside an HTML
        comment is no live heading (`unverified_check.py#live_lines`), so
        the reader names nothing for it."""
        item(repo, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(repo, "1700000001-a") / "frame" / "plan.md").write_text(
            "# Implementation Plan: a\n\n<!--\n## Judgments of the Run\n-->\n",
            encoding="utf-8",
        )
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert settle.JUDGMENTS_HEADING not in text, text

    def test_a_near_heading_is_named_beside_the_section_it_is_not(self, repo, capfd):
        """A plan holding a near heading and the exact section gets the line
        for the first and the rows of the second: the naming runs before the
        reader looks for the exact section, and the near rows are not read."""
        item(repo, "1700000001-a", "- nothing\n  why: x.")
        header = "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
        (specs_dir(repo, "1700000001-a") / "frame" / "plan.md").write_text(
            "# Implementation Plan: a\n\n## Judgments Of The Run\n\n"
            + header
            + "| 2026-10-01 | near | y | z |\n\n## Judgments of the run\n\n"
            + header
            + "| 2026-10-02 | exact | y | z |\n",
            encoding="utf-8",
        )
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        block = text.split(f"\n{settle.JUDGMENTS_HEADING}\n")[1]
        assert block.startswith(
            "    1700000001-a  seal/threads/1700000001-a/frame/plan.md  not read: "
            "line 3: `## Judgments Of The Run` opens like `## Judgments of the "
            "run` and is not it, so none of its rows were read\n"
        ), block
        assert "2026-10-02  exact\n" in block, block
        assert "2026-10-01  near" not in block, block

    def test_the_judgments_earlier_settles_removed_are_read_from_the_history(
        self, repo, capfd
    ):
        """#1281, design S1. A plan a commit on the ref deleted is read at
        that commit's parent, after *The judgments*: its rows grouped by the
        `Judged against` cell as written, each work item with the release
        that holds its adding commit and the removing commit's `(#N)`, and
        each row at its coordinate in the history."""
        run_doc = "`docs/running/the-run.md` *The run*"
        order = (
            "`skills/implement/orchestration.md` *Orchestrator: the order "
            "inside a ticket*"
        )
        rows = [
            ("2026-10-01", "ended the rounds", "round 3 found 2", run_doc),
            ("2026-10-02", "folded the owner's answer", "the owner answered Q1", order),
        ]
        plan = judgments_plan(rows)
        old = "1700000001-old"
        _, short = removed_plan(
            repo, old, plan, "the old work item (#3)", "settle 0.1.0 (#7)", "v0.1.0"
        )
        released_item(
            repo,
            "1700000002-new",
            {"frame/plan.md": judgments_plan([("2026-10-03", "x", "y", run_doc)])},
        )
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert text.index(settle.JUDGMENTS_HEADING) < text.index(
            settle.EARLIER_HEADING
        ), text
        block = text.split(f"\n{settle.EARLIER_HEADING}\n")[1].split(
            f"\n\n{settle.REMOVES_HEADING}"
        )[0]
        where = f"{short}^:seal/threads/{old}/frame/plan.md"
        a, b = (line_of(plan, f"| {' | '.join(row)} |") for row in rows)
        assert block == (
            f"\njudged against: {run_doc}\n"
            f"    {old}  released in v0.1.0; removed by {short} (#7)\n"
            f"        {where}:{a}  2026-10-01  ended the rounds\n"
            "            grounds: round 3 found 2\n"
            f"\njudged against: {order}\n"
            f"    {old}  released in v0.1.0; removed by {short} (#7)\n"
            f"        {where}:{b}  2026-10-02  folded the owner's answer\n"
            "            grounds: the owner answered Q1"
        ), block

    def test_a_deleted_plan_whose_directory_stands_is_not_an_earlier_one(
        self, repo, capfd
    ):
        """#1281, design S3. A plan deleted from a work item whose directory
        stands in the working tree is no earlier settle's removal, so it is
        not read and the section is not printed. Seen red with the exclusion
        of `work_items(records)` alone removed."""
        name = "1700000001-a"
        released_item(
            repo,
            name,
            {
                "routing.md": "# a — routing\n",
                "frame/plan.md": judgments_plan([("2026-10-01", "x", "y", "z")]),
            },
        )
        git(repo, "rm", "-q", f"seal/threads/{name}/frame/plan.md")
        commit(repo, "a drops its plan (#7)")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert settle.EARLIER_HEADING not in text, text

    def test_a_plan_is_read_once_at_its_newest_deletion(self, repo, capfd):
        """#1281, design *Scope* item 1. A plan deleted, added again and
        deleted again is read once, at the newest deletion's parent, and
        the work items of one cell come in the order of their removing
        commits, newest first, whatever their ids' order. Seen red with the
        once-only check removed, and with the deletions taken oldest first."""
        removed_plan(
            repo,
            "1700000000-older",
            judgments_plan([("2026-09-01", "older", "y", "z")]),
            "the older work item (#1)",
            "settle 0.0.1 (#2)",
        )
        old = "1700000001-old"
        removed_plan(
            repo,
            old,
            judgments_plan([("2026-10-01", "first", "y", "z")]),
            "the old work item (#3)",
            "drop it (#5)",
        )
        plan = judgments_plan([("2026-10-02", "second", "y", "z")])
        write(repo / "seal" / "threads" / old, "frame/plan.md", plan)
        commit(repo, "the old work item again (#6)")
        git(repo, "rm", "-rq", f"seal/threads/{old}")
        commit(repo, "settle 0.1.0 (#7)")
        short = git(repo, "rev-parse", "--short", "HEAD").strip()
        released_item(repo, "1700000002-new", {"routing.md": "# new — routing\n"})
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert settle.EARLIER_HEADING in text, text
        block = text.split(f"\n{settle.EARLIER_HEADING}\n")[1].split(
            f"\n\n{settle.REMOVES_HEADING}"
        )[0]
        assert "  2026-10-01  first\n" not in block, block
        assert block.index(f"    {old}  ") < block.index("    1700000000-older  "), (
            block
        )
        assert (
            f"; removed by {short} (#7)\n        {short}^:seal/threads/{old}/"
            f"frame/plan.md:7  2026-10-02  second\n"
        ) in block, block

    def test_a_removed_plan_of_a_non_ascii_id_is_read(self, repo, capfd):
        """#1281, round 1, finding 1. A work item id may hold any character
        the slug takes, and git quotes such a path under the default
        `core.quotePath` unless `-z` is given, so the history is read with
        `-z`. Seen red against the reading without it."""
        old = "1700000001-정렬"
        plan = judgments_plan([("2026-10-01", "ended the rounds", "y", "z")])
        write(repo / "seal" / "threads" / old, "frame/plan.md", plan)
        commit(repo, "the old work item (#3)")
        git(repo, "rm", "-rq", f"seal/threads/{old}")
        commit(repo, "settle 0.1.0 (#7)")
        released_item(repo, "1700000002-new", {"routing.md": "# new — routing\n"})
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert f"\n    {old}  " in text, text

    def test_a_plan_deleted_where_another_is_added_is_still_read(self, repo, capfd):
        """#1281, round 1, finding 2, design *Scope* item 1. One commit
        deletes a work item's plan and adds another's from the same text, so
        git's rename detection would pair the two and list no deletion. Seen
        red with `--no-renames` alone removed from `earlier_judgments`."""
        git(repo, "config", "diff.renames", "true")
        old, new = "1700000001-old", "1700000002-new"
        plan = judgments_plan([("2026-10-01", "ended the rounds", "y", "z")])
        write(repo / "seal" / "threads" / old, "frame/plan.md", plan)
        commit(repo, "the old work item (#3)")
        git(repo, "rm", "-rq", f"seal/threads/{old}")
        write(repo / "seal" / "threads" / new, "frame/plan.md", plan)
        commit(repo, "settle 0.1.0 and frame the new one (#7)")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert f"\n    {old}  " in text, text

    @pytest.mark.parametrize("added_by", ["an untagged commit", "no commit"])
    def test_names_a_plan_no_tag_holds_and_a_removal_no_number_names(
        self, repo, capfd, monkeypatch, added_by
    ):
        """#1281, design S4. Where no `vX.Y.Z` tag holds the commit that
        added the plan, the work item's line names that commit, and a
        removing commit whose subject ends in no `(#N)` is named alone.
        Where no commit on the ref adds the plan, as for one only a merge's
        own resolution added, the line says so."""
        old = "1700000001-old"
        adding, short = removed_plan(
            repo,
            old,
            judgments_plan([("2026-10-01", "x", "y", "z")]),
            "the old work item",
            "drop the old work item",
        )
        released_item(repo, "1700000002-new", {"routing.md": "# new — routing\n"})
        released = (
            "no `vX.Y.Z` tag holds "
            + git(repo, "rev-parse", "--short", adding).strip()
            + ", the commit that added its plan"
        )
        if added_by == "no commit":
            monkeypatch.setattr(settle, "adding_commit", lambda *_: (None, None))
            released = "no commit on main adds its plan"
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert f"\n    {old}  {released}; removed by {short}\n" in text, text

    def test_names_a_near_heading_in_a_removed_plan_and_reads_none_of_its_rows(
        self, repo, capfd
    ):
        """#1281, design S5. A removed plan is read by the reader the
        released plans are read by, so a near heading is named at its
        coordinate in the history, none of its rows is printed, and the dry
        run exits 0. Seen red with the reader's near-heading branch alone
        removed."""
        old = "1700000001-old"
        _, short = removed_plan(
            repo,
            old,
            judgments_plan(
                [("2026-10-01", "x", "y", "z")], heading="## Judgments Of The Run"
            ),
            "the old work item (#3)",
            "settle 0.1.0 (#7)",
            "v0.1.0",
        )
        released_item(repo, "1700000002-new", {"routing.md": "# new — routing\n"})
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert settle.EARLIER_HEADING in text, text
        block = text.split(f"\n{settle.EARLIER_HEADING}\n")[1].split(
            f"\n\n{settle.REMOVES_HEADING}"
        )[0]
        assert block == (
            f"    {old}  {short}^:seal/threads/{old}/frame/plan.md  not read: "
            "line 3: `## Judgments Of The Run` opens like `## Judgments of the "
            "run` and is not it, so none of its rows were read"
        ), block

    @pytest.mark.parametrize("failing", ["log", "show", "tag"])
    def test_a_git_that_cannot_read_an_earlier_plan_is_named_and_refuses_nothing(
        self, repo, capfd, monkeypatch, failing
    ):
        """#1281, design *Scope* item 4. The history's `git log`, a plan's
        `git show` or its tag read that fails is named with what git said,
        no row of that plan is printed, and the dry run exits 0."""
        old = "1700000001-old"
        _, short = removed_plan(
            repo,
            old,
            judgments_plan([("2026-10-01", "x", "y", "z")]),
            "the old work item (#3)",
            "settle 0.1.0 (#7)",
            "v0.1.0",
        )
        released_item(repo, "1700000002-new", {"routing.md": "# new — routing\n"})
        real = settle.git_out

        def git_out(root, *args):
            if args[0] == failing and (failing != "log" or "--diff-filter=D" in args):
                raise RuntimeError("git said no")
            return real(root, *args)

        monkeypatch.setattr(settle, "git_out", git_out)
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert settle.EARLIER_HEADING in text, text
        block = text.split(f"\n{settle.EARLIER_HEADING}\n")[1].split(
            f"\n\n{settle.REMOVES_HEADING}"
        )[0]
        where = (
            ""
            if failing == "log"
            else f"{old}  {short}^:seal/threads/{old}/frame/plan.md  "
        )
        assert block == f"    {where}not read: git said no", block

    @pytest.mark.parametrize("flag", ["--retire", "--retire-process"])
    def test_the_retired_flags_are_an_argument_error(self, repo, flag, capfd):
        """A script that still calls either gets exit 2, which the changelog
        fragment says."""
        with pytest.raises(SystemExit) as raised:
            settle.main(["--root", str(repo), "--released-at", "main", flag])
        assert raised.value.code == 2

    def test_a_spec_moved_into_place_is_ordered_by_the_commit_that_moved_it(
        self, repo, capfd
    ):
        """git reads a moved directory as a rename, never as an add, unless it is
        told not to; the spec would then have no place in the order, and be
        listed last and unordered."""
        item(repo, "1700000001-old", op("add", "U", new="Rule."))
        commit(repo, "old")
        git(repo, "mv", "seal/threads/1700000001-old", "seal/threads/1700000002-new")
        commit(repo, "renamed")
        item(repo, "1700000003-b", op("add", "U", new="B."))
        commit(repo, "b")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        group = group_text(text)
        assert group.index("1700000002-new") < group.index("1700000003-b"), text
        assert "unordered" not in group, text

    def test_a_spec_no_commit_adds_is_marked_unordered(self, repo, capfd, monkeypatch):
        """Where the history cannot place a spec, it has no place in the order,
        and the group says so rather than listing it as ordered."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        item(repo, "1700000002-b", op("add", "U", new="B."))
        commit(repo, "a and b")
        real = settle.load

        def load(path, name):
            module = real(path, name)
            if path == settle.RULES:
                monkeypatch.setattr(
                    module, "order", lambda r, f, ids, s: [(i, None) for i in ids]
                )
            return module

        monkeypatch.setattr(settle, "load", load)
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        said = settle.UNORDERED.format(a="1700000001-a", b="1700000002-b")
        assert said in group_text(text), text

    def test_apply_names_a_document_past_the_ceiling(self, repo, capfd):
        """Scope 5: after the removals, each document past `Document token
        ceiling` is named as one to split, and that refuses nothing."""
        configure(repo, ("Document token ceiling", "10"))
        item(repo, "1700000001-a", op("add", "U", new="Released."))
        commit(repo, "a")
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert (
            "docs/a.md is about "
            in text.split("past the ceiling")[0].rsplit("\n", 1)[-1]
        ), text
        assert (
            "past the ceiling of 10: split it by who opens each section and at "
            "which step" in text
        ), text
        assert settle.AFTER_HEADING in text, text

    def test_local_mode_lists_a_released_and_an_unreleased_item(self, local, gh, capfd):
        """S1 of #955. The root is under the git directory, so `settle` reads
        it there: the item whose branch's pull request merged into `main` is
        released, with its pull request and merge commit, and its rule joins
        a group; the other is unreleased because nothing merged from its
        branch. `gh` is asked once per branch, and the run writes and removes
        nothing. A repository holding work items is never told it has none,
        the half of the old local-mode refusal's case that stays."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="Rule."))
        local_item(local, "1700000002-b", "feat/2-b", op("add", "U", new="B."))
        oid = merge(local, "feat/1-a")
        gh.merged("feat/1-a", (11, oid))
        before = files(local)
        records = sorted(p for p in (local / ".git" / "seal").rglob("*"))
        code, text = dry_run(local, capfd)
        assert code == 0, text
        home = os.path.join(str(local), ".git", "seal")
        assert text.split("\n")[0] == (
            f"local mode: the seal/ root is {home}, under the git directory"
        ), text
        assert "released at main: 1 work item; 1 unreleased and untouched\n" in text
        released = text.split(settle.MERGED_HEADING + "\n")[1].split("\n\n")[0]
        assert released == f"    1700000001-a  pull request #11  merge commit {oid}"
        unreleased = text.split(settle.UNMERGED_HEADING + "\n")[1].split("\n\n")[0]
        assert unreleased == (
            "    1700000002-b  no pull request from `feat/2-b` has merged"
        ), text
        assert "1. add  1700000001-a  seal/threads/1700000001-a/frame/design.md:" in (
            group_text(text)
        ), text
        assert "1700000002-b" not in group_text(text), text
        assert "\ngroup 2\n" not in text, text
        assert settle.REMOVES_HEADING_LOCAL in text, text
        assert "    seal/threads/1700000001-a/  now\n" in text, text
        assert "has nothing to settle" not in text, text
        assert files(local) == before, "the dry run wrote to the tree"
        assert sorted(p for p in (local / ".git" / "seal").rglob("*")) == records
        query = ["pr", "list", "--head", "{}", "--state", "merged"]
        query += ["--json", "number,mergeCommit"]
        assert gh.calls() == [
            [a.format(b) for a in query] for b in ("feat/1-a", "feat/2-b")
        ], gh.calls()

    def test_a_local_run_from_a_subdirectory_reads_the_repositorys_top(
        self, local, gh, capfd
    ):
        """Round 1 finding 2 of #955: from a subdirectory the local root is
        still found under the git directory, so the policy root has to be read
        from the repository's top too, or a document that is there reads as
        absent and the settling session is sent to write it."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="Rule."))
        gh.merged("feat/1-a", (11, merge(local, "feat/1-a")))
        below = str(local / "docs")
        code = settle.main(["--root", below, "--released-at", "main"])
        out = capfd.readouterr()
        text = out.out + out.err
        assert code == 0, text
        assert group_text(text).startswith(
            "    place: docs/a.md section `S`, at docs/a.md:3-9\n"
        ), text
        assert "not in the tree" not in text, text

    def test_a_shared_run_from_a_subdirectory_reads_the_repositorys_top(
        self, repo, gh, capfd
    ):
        """Round 2 finding 1 of #955: `main` resolves the root to the
        repository's top in both modes, so a shared run from a subdirectory
        prints what a run from the top prints. It used to refuse, saying the
        repository had no seal/threads/ at either place, which was false there."""
        item(repo, "1700000001-a", op("add", "S", new="Rule."))
        commit(repo, "released a")
        top = dry_run(repo, capfd)
        assert top[0] == 0, top[1]
        assert group_text(top[1]).startswith(
            "    place: docs/a.md section `S`, at docs/a.md:3-9\n"
        ), top[1]
        below = str(repo / "docs")
        code = settle.main(["--root", below, "--released-at", "main"])
        out = capfd.readouterr()
        assert (code, out.out + out.err) == top, out.out + out.err
        assert "at either place" not in out.err, out.err
        assert gh.calls() == [], gh.calls()

    def test_the_local_dry_runs_texts_say_what_they_hold(self, capsys):
        """Contract rule 14 for #955's dry run: the sentences a person acts
        on are pinned, not only their presence. `--released-at`'s help names
        the ref as what reaches the merge commit (round 1 finding 5)."""
        with pytest.raises(SystemExit):
            settle.main(["--help"])
        assert (
            "or in local mode when this ref reaches the merge commit of the pull "
            "request from the work item's branch"
        ) in flat(capsys.readouterr().out)
        assert "each with the pull request that merged it" in flat(
            settle.MERGED_HEADING
        )
        assert "unreleased in local mode and untouched, each with why" in flat(
            settle.UNMERGED_HEADING
        )
        removes = flat(settle.REMOVES_HEADING_LOCAL)
        assert "In local mode no commit holds these directories" in removes
        # The heading the local dry run prints, with the command the settling
        # session runs to keep a copy.
        assert "`seal export` takes a copy for whoever wants one" in removes
        assert "no ancestry orders their pull requests' merge commits" in flat(
            settle.UNORDERED_LOCAL
        )

    def test_local_specs_are_listed_in_the_order_their_pull_requests_merged(
        self, local, gh, capfd
    ):
        """S2 of #955, one line of history: B was created after A and merged
        before it, so B is listed first, and ancestry orders the pair."""
        local_item(local, "1700000001-a", "feat/1-a", op("change", "S", "y.", "z."))
        local_item(
            local, "1700000002-b", "feat/2-b", op("change", "S", "old sentence.", "y.")
        )
        gh.merged("feat/2-b", (12, merge(local, "feat/2-b")))
        gh.merged("feat/1-a", (11, merge(local, "feat/1-a")))
        code, text = dry_run(local, capfd)
        assert code == 0, text
        group = group_text(text)
        assert "    1. change  1700000002-b  " in group, text
        assert "    2. change  1700000001-a  " in group, text
        assert "unordered" not in group, text

    def test_two_local_merges_no_ancestry_orders_are_marked_unordered(
        self, local, gh, capfd
    ):
        """S2 of #955, two lines of history: each pull request merged into a
        branch of its own, and `main` merged both, so no ancestry orders the
        two merge commits and the pair is marked."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        local_item(local, "1700000002-b", "feat/2-b", op("add", "S", new="B."))
        git(local, "branch", "one")
        git(local, "branch", "two")
        gh.merged("feat/1-a", (11, merge(local, "feat/1-a", into="one")))
        gh.merged("feat/2-b", (12, merge(local, "feat/2-b", into="two")))
        git(local, "switch", "-q", "main")
        git(local, "merge", "-q", "--no-ff", "-m", "one", "one")
        git(local, "merge", "-q", "--no-ff", "-m", "two", "two")
        code, text = dry_run(local, capfd)
        assert code == 0, text
        said = settle.UNORDERED_LOCAL.format(a="1700000001-a", b="1700000002-b")
        assert f"    {said}" in group_text(text), text

    def test_a_merge_commit_the_ref_does_not_reach_leaves_the_item(
        self, local, gh, capfd
    ):
        """S3 of #955: the pull request merged into a branch `--released-at`
        does not reach, so the item is unreleased with that reason, and
        `--apply` keeps it."""
        git(local, "branch", "other")
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="Rule."))
        oid = merge(local, "feat/1-a", into="other")
        git(local, "switch", "-q", "main")
        gh.merged("feat/1-a", (11, oid))
        code, text = dry_run(local, capfd)
        assert code == 0, text
        assert (
            f"    1700000001-a  main reaches no merge commit of the pull requests "
            f"from `feat/1-a` that merged: #11 at {oid}\n"
        ) in text, text
        assert "released at main: 0 work items; 1 unreleased and untouched\n" in text
        code, text = apply(local, capfd)
        assert code == 0, text
        assert local_dir(local, "1700000001-a").exists(), text

    def test_apply_in_local_mode_removes_under_the_git_directory_alone(
        self, local, gh, capfd
    ):
        """S4 of #955: the released item whose record holds no open row goes
        from under the git directory, the one holding a row is kept and its
        row named, the unreleased one stays, and nothing under the
        repository's top is written or removed; with the row closed on disk,
        a second run removes the kept one."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        local_item(local, "1700000002-b", "feat/2-b", op("add", "U", new="B."))
        row = OPEN.replace("a claim nobody ran", "a claim about `questions.md`")
        held = local_item(
            local, "1700000003-c", "feat/3-c", op("add", "T", new="C."), overview=row
        )
        (held / "questions.md").write_text("# q\n", encoding="utf-8")
        gh.merged("feat/1-a", (11, merge(local, "feat/1-a")))
        gh.merged("feat/3-c", (13, merge(local, "feat/3-c")))
        before = files(local)
        code, text = dry_run(local, capfd)
        rows = text.split(f"{settle.ROWS_HEADING}\n")[1].split("\n\n")[0]
        assert rows == (
            "    1700000003-c\n"
            "        open in gaps.md: a claim about `questions.md`\n"
            "            `questions.md` in the tree"
        ), text
        code, text = apply(local, capfd)
        assert code == 1, text
        assert not local_dir(local, "1700000001-a").exists(), text
        assert local_dir(local, "1700000002-b").exists(), text
        assert local_dir(local, "1700000003-c").exists(), text
        assert "removed seal/threads/1700000001-a/\n" in text, text
        assert (
            "kept seal/threads/1700000003-c/: its record holds 1 open row; close "
            "each (`closed` with what closed it) and run `seal settle --apply` again\n"
            "    open in gaps.md: a claim about `questions.md`\n"
        ) in text, text
        assert files(local) == before, "the apply wrote or removed in the tree"
        (local_dir(local, "1700000003-c") / "gaps.md").write_text(
            OVERVIEW_CLOSED, encoding="utf-8"
        )
        code, text = apply(local, capfd)
        assert code == 0, text
        assert not local_dir(local, "1700000003-c").exists(), text
        assert local_dir(local, "1700000002-b").exists(), text
        assert "    closed in gaps.md: a claim\n" in text, text

    def test_apply_in_local_mode_names_a_gaps_md_away_from_its_place(
        self, local, gh, capfd
    ):
        """S5 of #1126: under the git directory the misplaced file is found
        where `--apply` removes it. The dry run names `trail/gaps.md`, and
        `--apply` removes the directory and names the file under its
        `removed` line. Seen red with the fix reverted in `settle.py`."""
        name = "1700000001-a"
        path = local_item(local, name, "feat/1-a")
        (path / "trail").mkdir()
        (path / "trail" / "gaps.md").write_text(OPEN, encoding="utf-8")
        gh.merged("feat/1-a", (11, merge(local, "feat/1-a")))
        code, text = dry_run(local, capfd)
        line = not_read(name, "trail/gaps.md", "gaps.md")
        assert line in text, text
        assert code == 0, text
        code, text = apply(local, capfd)
        assert code == 0, text
        assert not path.exists(), text
        assert f"removed seal/threads/{name}/\n    not read: {line}\n" in text, text

    @pytest.mark.parametrize("arm", [False, True], ids=["report", "apply"])
    @pytest.mark.parametrize("state", ["absent", "fails", "garbled", "entry"])
    def test_refuses_a_gh_that_cannot_be_asked_in_local_mode(
        self, local, gh, capfd, monkeypatch, state, arm
    ):
        """S5 of #955: with no `gh` to ask, every local item would read as
        unreleased and the run would report nothing to settle, the quiet zero
        the `--released-at` refusal is written against. So it exits 2, names
        `gh` and what it said, and removes nothing."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        gh.merged("feat/1-a", (11, merge(local, "feat/1-a")))
        if state == "absent":
            monkeypatch.setattr(settle, "GH", "agentic-no-such-gh")
            said = "`agentic-no-such-gh` is not on PATH"
        elif state in ("garbled", "entry"):
            # A list whose entry is not an object is as garbled as an answer
            # that is no list (round 1 finding 3).
            gh.say('{"message": "Not Found"}' if state == "garbled" else "[11]")
            said = "`gh pr list --head feat/1-a` did not answer a list of pull requests"
        else:
            gh.fail("HTTP 401: Bad credentials (https://api.github.com/graphql)")
            said = (
                "`gh pr list --head feat/1-a` exited 4: HTTP 401: Bad "
                "credentials (https://api.github.com/graphql)"
            )
        code, text = dry_run(local, capfd, *(["--apply"] if arm else []))
        assert code == 2, text
        assert local_dir(local, "1700000001-a").exists(), text
        assert text.startswith(
            f"settle: `gh` cannot be asked which pull requests merged: {said}. "
            "Nothing was read and nothing was removed."
        ), text
        assert (
            "a repository on a host `gh` cannot ask cannot settle in local mode"
        ) in flat(text), text

    def test_a_released_at_ref_that_does_not_resolve_is_refused_in_local_mode(
        self, local, gh, capfd
    ):
        """The `--released-at` refusal holds in local mode too, before `gh`
        is asked: a ref nothing can read would make every merge commit
        unreachable, the quiet zero by another door."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        code = settle.main(["--root", str(local), "--released-at", "no/such/ref"])
        text = capfd.readouterr().err
        assert code == 2, text
        assert "--released-at no/such/ref does not resolve" in text, text
        assert gh.calls() == [], gh.calls()

    def test_gh_is_asked_once_for_a_branch_two_items_name(self, local, gh, capfd):
        """`gh` is asked once per branch, so two work items naming one branch,
        the reused-branch limit, cost one query and both read as released."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        local_item(local, "1700000002-b", "feat/1-a", op("add", "U", new="B."))
        gh.merged("feat/1-a", (11, merge(local, "feat/1-a")))
        code, text = dry_run(local, capfd)
        assert code == 0, text
        assert "released at main: 2 work items; 0 unreleased" in text, text
        assert len(gh.calls()) == 1, gh.calls()

    def test_a_released_at_given_as_the_merge_commit_reaches_it(self, local, gh, capfd):
        """`reaches` asks git itself because `rule_changes.py#_ancestor`
        answers False for two equal commits, so a `--released-at` naming the
        merge commit still reads the item as released (round 1 finding 6)."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        oid = merge(local, "feat/1-a")
        gh.merged("feat/1-a", (11, oid))
        code = settle.main(["--root", str(local), "--released-at", oid])
        out = capfd.readouterr()
        assert code == 0, out.err
        assert f"released at {oid}: 1 work item;" in out.out, out.out

    def test_the_first_listed_pull_request_the_ref_reaches_is_taken(
        self, local, gh, capfd
    ):
        """Several merged pull requests from one branch: one the ref does not
        reach does not hide a later-listed one it does (round 1 finding 6)."""
        git(local, "branch", "other")
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        stray = merge(local, "feat/1-a", into="other")
        git(local, "switch", "-q", "main")
        git(local, "merge", "-q", "--no-ff", "-m", "m", "feat/1-a")
        reached = git(local, "rev-parse", "HEAD").strip()
        gh.merged("feat/1-a", (12, stray), (11, reached))
        code, text = dry_run(local, capfd)
        assert code == 0, text
        assert f"1700000001-a  pull request #11  merge commit {reached}" in text, text

    def test_a_pull_request_listed_with_no_merge_commit_is_named_as_such(
        self, local, gh, capfd
    ):
        """A listed pull request whose `mergeCommit` is null names nothing git
        can reach, so the item is unreleased. `gh` was asked for merged pull
        requests and listed it, so the reason names it as one with no merge
        commit rather than saying none merged (round 1 finding 3)."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        gh.merged("feat/1-a", (11, None))
        code, text = dry_run(local, capfd)
        assert code == 0, text
        assert (
            "    1700000001-a  main reaches no merge commit of the pull requests "
            "from `feat/1-a` that merged: #11 with no merge commit\n"
        ) in text, text

    def test_shared_mode_asks_gh_for_no_note_it_cannot_read(self, repo, gh, capfd):
        """S6 of #955 and S7 of #1139: a shared root's work items are
        released by presence at `--released-at`, so the dry run asks no
        `gh`, even for an item whose `routing.md` names a branch. `--apply`
        asks it only for a note it can read. One released work item holds no
        `changelog.md`, the commit adding another's names no pull request
        though `v1.0.0` holds it, and no version tag holds the third's. Each
        goes, and the line under its `removed` line says which case held."""
        bare = moment(repo)
        write(
            specs_dir(repo, "1700000001-a"),
            "routing.md",
            ROUTED.format(name="1700000001-a", branch="feat/1-a"),
        )
        fragment(repo, "1700000001-a", "feat: a", tag="v1.0.0")
        unnumbered = git(repo, "rev-parse", "v1.0.0").strip()
        fragment(repo, "1700000002-b", "feat: b (#42)")
        untagged = git(repo, "rev-parse", "main").strip()
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not bare.exists(), text
        assert (
            f"removed seal/threads/{MOMENT}/\n"
            "    no note read: main holds no `changelog.md` in its directory\n"
        ) in text, text
        assert (
            "removed seal/threads/1700000001-a/\n"
            f"    no note read: {unnumbered}, the commit that added its "
            "`changelog.md`, names no pull request\n"
        ) in text, text
        assert (
            "removed seal/threads/1700000002-b/\n"
            f"    no note read: no `vX.Y.Z` tag holds {untagged}, the commit "
            "that added its `changelog.md`\n"
        ) in text, text
        assert text.endswith(
            "\nremoved 3 directories; kept 0 with a row to close and 0 whose "
            "note lacks its entry\n"
        ), text
        assert gh.calls() == [], gh.calls()

    def test_apply_keeps_a_directory_its_published_note_does_not_carry(
        self, repo, gh, capfd
    ):
        """S4 of #1139. `v1.2.3` holds the fragments of two released work
        items, added by `(#42)` and `(#43)`, and so does `v1.10.0`. The
        version is the lowest tag by number, `v1.2.3`, whose note links #43,
        #420 and another work item's marker, none of which carries #42. So
        `--apply` keeps the first directory and names the tag, the pull
        request and where its fragment can be read, removes the second,
        exits 1, and lists the releases once. `v1.10.0`'s note carries #42,
        and a version read by its text would have taken it. The dry run asks
        no `gh`."""
        kept = fragment(repo, "1700000001-a", "feat: a (#42)")
        fragment(repo, "1700000002-b", "feat: b (#43)", tag="v1.2.3")
        git(repo, "tag", "v1.10.0")
        at = git(repo, "rev-parse", "main").strip()
        gh.releases(
            [
                release("v1.10.0", "[#42](https://github.com/o/r/pull/42)"),
                release(
                    "v1.2.3",
                    "[#43](https://github.com/o/r/pull/43)\n"
                    "[#420](https://github.com/o/r/pull/420)\n"
                    "<!-- specs/1700000002-b -->\n",
                ),
            ]
        )
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert gh.calls() == [], gh.calls()
        code, text = apply(repo, capfd)
        assert code == 1, text
        assert kept.exists(), text
        assert not specs_dir(repo, "1700000002-b").exists(), text
        assert (
            "kept seal/threads/1700000001-a/: the published note of v1.2.3 does "
            "not carry its entry, a link to pull request #42; repair the note "
            f"from `git show {at}:seal/threads/1700000001-a/changelog.md` and "
            "run `seal settle --apply` again\n"
        ) in text, text
        assert "removed seal/threads/1700000002-b/\n" in text, text
        assert text.endswith(
            "\nremoved 1 directory; kept 0 with a row to close and 1 whose note "
            "lacks its entry\n"
        ), text
        assert gh.calls() == [RELEASES_CALL], gh.calls()

    @pytest.mark.parametrize("carried", ["link", "marker"])
    def test_apply_removes_a_directory_its_published_note_carries(
        self, repo, gh, capfd, carried
    ):
        """S5 of #1139. A note carries the entry where it links the pull
        request under any owner and name, since a renamed repository's old
        links redirect, or where it holds the work item's marker, which the
        notes published before #1139 carry. The list comes in two pages, as
        `--paginate` prints a long one."""
        path = fragment(repo, "1700000001-a", "feat: a (#42)", tag="v1.2.3")
        body = (
            "[#42](https://github.com/old/name/pull/42)\n"
            if carried == "link"
            else "<!-- specs/1700000001-a -->\n"
        )
        gh.releases([release("v1.0.0")], [release("v1.2.3", body)])
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not path.exists(), text
        assert "removed seal/threads/1700000001-a/\n" in text, text
        # The note was read and carried the entry: no reason for not reading it.
        assert "no note read" not in text, text
        assert text.endswith(
            "\nremoved 1 directory; kept 0 with a row to close and 0 whose note "
            "lacks its entry\n"
        ), text

    @pytest.mark.parametrize("state", ["fails", "garbled", "entry"])
    def test_apply_stops_where_the_release_list_cannot_be_read(
        self, repo, gh, capfd, state
    ):
        """S6 of #1139. A `gh` that fails, or answers anything but pages that
        are each a list of objects, stops `--apply` with exit 2 and one
        sentence naming `gh` and what it said. No directory goes, the one
        that needs no note among them, which sorts first so that a note read
        only when its directory's turn comes would have let it go."""
        bare = moment(repo, "1700000000-bare")
        tagged = fragment(repo, "1700000001-a", "feat: a (#42)", tag="v1.2.3")
        if state == "fails":
            gh.fail("HTTP 401: Bad credentials (https://api.github.com/releases)")
            said = (
                f"{RELEASES_ASKED} exited 4: HTTP 401: Bad credentials "
                "(https://api.github.com/releases)"
            )
        else:
            gh.say(
                '{"message": "Not Found"}'
                if state == "garbled"
                else '[{"tag_name": "v1.2.3", "draft": false}][1]'
            )
            said = f"{RELEASES_ASKED} did not answer a list of releases"
        code, text = apply(repo, capfd)
        assert code == 2, text
        assert bare.exists(), text
        assert tagged.exists(), text
        assert text.startswith(
            f"settle: `gh` cannot be asked for this repository's releases: {said}. "
            "Nothing was removed."
        ), text

    @pytest.mark.parametrize("listed", ["another", "a draft"])
    def test_apply_keeps_a_directory_whose_tag_has_no_published_release(
        self, repo, gh, capfd, listed
    ):
        """S7b of #1139, its first half. `v1.2.3` holds the fragment, and the
        list holds another published release, so the repository publishes
        Releases and `v1.2.3` lacks one. A draft at `v1.2.3` is not
        published, and another tag's note is not this one's, though both
        link #42."""
        path = fragment(repo, "1700000001-a", "feat: a (#42)", tag="v1.2.3")
        at = git(repo, "rev-parse", "main").strip()
        link = "[#42](https://github.com/o/r/pull/42)"
        listing = [release("v1.0.0", link)]
        if listed == "a draft":
            listing.append(release("v1.2.3", link, draft=True))
        gh.releases(listing)
        code, text = apply(repo, capfd)
        assert code == 1, text
        assert path.exists(), text
        assert (
            "kept seal/threads/1700000001-a/: v1.2.3 has no published GitHub "
            "Release, so no note carries its entry, a link to pull request #42; "
            f"publish one from `git show {at}:seal/threads/1700000001-a/"
            "changelog.md` and run `seal settle --apply` again\n"
        ) in text, text

    @pytest.mark.parametrize("listed", ["none", "a draft"])
    def test_apply_removes_where_the_repository_publishes_no_release(
        self, repo, gh, capfd, listed
    ):
        """S7b of #1139, its second half. The list holds no published
        release, so the repository publishes no Releases: the directory goes,
        and the line under its `removed` line says so."""
        path = fragment(repo, "1700000001-a", "feat: a (#42)", tag="v1.2.3")
        gh.releases([release("v1.2.3", draft=True)] if listed == "a draft" else [])
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not path.exists(), text
        assert (
            "removed seal/threads/1700000001-a/\n"
            "    no note read: this repository has published no GitHub Release, "
            "so v1.2.3 has no note\n"
        ) in text, text

    def test_apply_removes_where_no_published_note_is_built_from_the_fragments(
        self, repo, gh, capfd
    ):
        """Round 1 finding 1 of #1139. The release note is built from the
        fragments by this repository's CI script, which ships to nobody. A
        user's notes are written by hand or by another tool: one links the
        pull request as an issue, one links it on another host, GitHub's
        generated line links another pull request inside a sentence, and a
        conventional-changelog line holds the link's very shape inside a
        longer line. No published release holds a whole line the release
        note opens an entry with, so a missing entry says nothing of the
        fragment, and the directory goes, named."""
        path = fragment(repo, "1700000001-a", "feat: a (#42)", tag="v1.2.3")
        gh.releases(
            [
                release(
                    "v1.2.2",
                    "[#42](https://ghe.example.com/o/r/pull/42)\n"
                    "* b by @x in https://github.com/o/r/pull/41\n"
                    "* **settle:** c ([#40](https://github.com/o/r/pull/40))\n",
                ),
                release("v1.2.3", "- a ([#42](https://github.com/o/r/issues/42))\n"),
            ]
        )
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not path.exists(), text
        assert (
            "removed seal/threads/1700000001-a/\n"
            "    no note read: no published release of this repository opens an "
            "entry with a `[#N](https://github.com/<owner>/<name>/pull/N)` line "
            "or the old marker, so its notes are not built from the fragments\n"
        ) in text, text
        assert gh.calls() == [RELEASES_CALL], gh.calls()

    def test_apply_removes_a_directory_whose_fragment_is_empty(self, repo, gh, capfd):
        """Round 1 finding 2 of #1139. The release note gives an empty
        fragment no entry (`publish_release_note.py#fragments`), so no note
        can carry it: the directory goes, the line under its `removed` line
        says the fragment holds no text, and no `gh` is asked for it. The
        other notes are built from the fragments and lack its link."""
        path = fragment(
            repo, "1700000001-a", "feat: a (#42)", tag="v1.2.3", text="\n  \n"
        )
        gh.releases([release("v1.2.3", "[#41](https://github.com/o/r/pull/41)\n")])
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not path.exists(), text
        assert (
            "removed seal/threads/1700000001-a/\n"
            "    no note read: its `changelog.md` at main holds no text, and the "
            "release note gives an empty fragment no entry\n"
        ) in text, text
        assert gh.calls() == [], gh.calls()

    def test_an_open_row_keeps_its_directory_before_its_note_is_read(
        self, repo, gh, capfd
    ):
        """S8 of #1139. The record holds an open row and the note lacks the
        entry. The row keeps the directory as before, and no note is read
        for it, so `gh` is not asked."""
        path = specs_dir(repo, "1700000001-a")
        write(path, "gaps.md", OPEN)
        fragment(repo, "1700000001-a", "feat: a (#42)", tag="v1.2.3")
        gh.releases([release("v1.2.3", "no entry")])
        code, text = apply(repo, capfd)
        assert code == 1, text
        assert path.exists(), text
        assert (
            "kept seal/threads/1700000001-a/: its record holds 1 open row; close "
            "each (`closed` with what closed it) and run `seal settle --apply` again\n"
            "    open in gaps.md: a claim nobody ran\n"
        ) in text, text
        assert text.endswith(
            "\nremoved 0 directories; kept 1 with a row to close and 0 whose note "
            "lacks its entry\n"
        ), text
        assert gh.calls() == [], gh.calls()

    def test_a_git_that_cannot_read_the_adding_commit_stops_apply(
        self, repo, gh, capfd, monkeypatch
    ):
        """#1139's phase 2. Where `git` cannot read the commit that added a
        released `changelog.md`, the pull request it names is unknown, and
        removing on an unknown is the quiet path an unreadable release list
        is refused for. So `--apply` exits 2 with what `git` said, asks no
        `gh`, and removes nothing."""
        bare = moment(repo)
        path = fragment(repo, "1700000001-a", "feat: a (#42)", tag="v1.2.3")

        def refuse(root, revisions, rel):
            raise RuntimeError(f"`git log {revisions} -- {rel}` exited 128: fatal")

        monkeypatch.setattr(settle, "adding_commit", refuse)
        code, text = apply(repo, capfd)
        assert code == 2, text
        assert bare.exists(), text
        assert path.exists(), text
        assert text.startswith("settle: `git log "), text
        assert (
            "exited 128: fatal, so the pull request a released `changelog.md` "
            "names cannot be read. Nothing was removed.\n"
        ) in text, text
        assert gh.calls() == [], gh.calls()

    def test_a_local_item_with_no_branch_is_unreleased_and_gh_is_not_asked(
        self, local, gh, capfd
    ):
        """S7 of #955: one item has no `routing.md`, the other's has no
        `Branch` row, so there is no branch to ask about."""
        local_item(local, "1700000001-a", changes=op("add", "S", new="A."))
        routing = ROUTED.format(name="1700000002-b", branch="x")
        local_item(local, "1700000002-b", changes=op("add", "S", new="B."))
        (local_dir(local, "1700000002-b") / "routing.md").write_text(
            routing.replace("| Branch | x |\n", ""), encoding="utf-8"
        )
        code, text = dry_run(local, capfd)
        assert code == 0, text
        unreleased = text.split(settle.UNMERGED_HEADING + "\n")[1].split("\n\n")[0]
        assert unreleased == (
            f"    1700000001-a  {NO_BRANCH}\n    1700000002-b  {NO_BRANCH}"
        ), text
        assert gh.calls() == [], gh.calls()

    def test_a_local_routing_md_routing_py_does_not_read_names_no_branch(
        self, local, gh, capfd
    ):
        """A `routing.md` with a `Branch` row whose `Review` answer is outside
        the vocabulary is no declaration to `hooks/lib/routing.py#parse`, so the
        item is unreleased and `gh` is not asked. The reason says the file is
        not read as a declaration, since a person who opens it finds the
        `Branch` row there (round 1 finding 3)."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        path = local_dir(local, "1700000001-a") / "routing.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(
            text.replace("| Review | through", "| Review | Through"), encoding="utf-8"
        )
        code, text = dry_run(local, capfd)
        assert code == 0, text
        unreleased = text.split(settle.UNMERGED_HEADING + "\n")[1].split("\n\n")[0]
        assert unreleased == f"    1700000001-a  {NO_BRANCH}", text
        assert gh.calls() == [], gh.calls()

    def test_a_local_repository_with_no_policy_root_settles(self, local, gh, capfd):
        """S9 of #955: a local-mode repository has no `docs/` until the
        settling session creates it. The dry run says the new document is not
        there, and `--apply` removes the item and reads no policy root."""
        git(local, "rm", "-rq", "docs")
        commit(local, "no policy root")
        local_item(
            local,
            "1700000001-a",
            "feat/1-a",
            op("add", new="# New", file="docs/new.md"),
        )
        gh.merged("feat/1-a", (11, merge(local, "feat/1-a")))
        code, text = dry_run(local, capfd)
        assert code == 0, text
        assert group_text(text).startswith(
            "    place: docs/new.md, the whole document: the document is not in "
            "the tree"
        ), text
        code, text = apply(local, capfd)
        assert code == 0, text
        assert not local_dir(local, "1700000001-a").exists(), text
        assert settle.AFTER_HEADING not in text, text
        assert not (local / "docs").exists()

    def test_a_repository_with_no_root_at_either_place_says_so(self, tmp_path):
        """The other arm of the same resolution, kept apart from local mode
        because the two are different states and used to share one sentence."""
        repo = tmp_path / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        r = subprocess.run(
            [sys.executable, SCRIPT, "--root", str(repo), "--released-at", "HEAD"],
            capture_output=True,
            encoding="utf-8",
        )
        assert r.returncode == 2, r.stdout + r.stderr
        assert "at either place" in r.stderr, r.stderr

    def test_an_opted_out_repository_is_told_which_state_it_is_in(self, tmp_path):
        """Round 2, finding 7. `home_at` answers `""` for two states — no root at
        either place, and a repository that opted out with the scratch marker —
        and they were given one sentence, so a tree holding work items was told it
        had none. That is finding 3's defect through another door."""
        repo = tmp_path / "repo"
        (repo / "docs").mkdir(parents=True)
        git(repo, "init", "-q")
        item = repo / "seal" / "threads" / "1700000001-alpha"
        (item / "frame").mkdir(parents=True)
        (item / "frame" / "design.md").write_text("# a\n", encoding="utf-8")
        (repo / ".git" / "agentic-scratch").write_text("", encoding="utf-8")
        r = subprocess.run(
            [sys.executable, SCRIPT, "--root", str(repo), "--released-at", "HEAD"],
            capture_output=True,
            encoding="utf-8",
        )
        assert r.returncode == 2, r.stdout + r.stderr
        assert "has opted out" in r.stderr, r.stderr
        assert "agentic-scratch" in r.stderr, r.stderr
        assert "has nothing to settle" not in r.stderr, (
            "a repository holding a work item is still being told it has none"
        )

    def test_a_directory_of_the_markers_name_is_not_an_opt_out(self, tmp_path):
        """Round 3, finding 1. `hooks/lib/optin.py#home_at` reads the scratch marker
        with `os.path.isfile` and says why: `os.path.exists` also accepted a
        DIRECTORY of that name, and one created once turned every gate off in
        every clone. The refusal here asked `exists`, so a repository holding a
        directory of that name and no root was told it had opted out and to delete
        "that file" — and no gate reads a directory as the opt-out, so every clause
        of that sentence was false. The three readers of one marker answer alike."""
        repo = tmp_path / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        (repo / ".git" / "agentic-scratch").mkdir()
        r = subprocess.run(
            [sys.executable, SCRIPT, "--root", str(repo), "--released-at", "HEAD"],
            capture_output=True,
            encoding="utf-8",
        )
        assert r.returncode == 2, r.stdout + r.stderr
        assert "has no seal/threads/ at either place" in r.stderr, r.stderr
        assert "has opted out" not in r.stderr, (
            "a directory of the marker's name is read as the opt-out, which is the "
            "reading `hooks/lib/optin.py` rejected by name"
        )

    def test_the_refusal_path_asks_for_the_common_directory_once(
        self, tmp_path, monkeypatch
    ):
        """Round 3, finding 5. `home_at(root)` resolves the common git directory
        for itself, and the opt-out arm then resolved it a second time, although
        `home_at(root, common)` exists for a caller that needs the value too and
        `hooks/lib/optin.py` documents the parameter with the measurement that created
        it. Counted through the module `settle.load` hands `main`, and counted as
        calls rather than processes: on a main worktree the resolver's fast path
        costs no process, so a process count would have said nothing."""
        repo = tmp_path / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        optin = settle.load(settle.OPTIN, "agentic_optin_counted")
        calls, received = [], []
        common_dir, home_at = optin.git_common_dir, optin.home_at

        def counted(root):
            calls.append(root)
            return common_dir(root)

        def recorded(root, common=None):
            received.append(common)
            return home_at(root, common)

        # `home_at` reaches `git_common_dir` through the module global, so the
        # counter sees the resolver's own call as well as `main`'s.
        optin.git_common_dir, optin.home_at = counted, recorded
        real_load = settle.load
        monkeypatch.setattr(
            settle,
            "load",
            lambda path, name: optin if path == settle.OPTIN else real_load(path, name),
        )
        assert settle.main(["--root", str(repo), "--released-at", "HEAD"]) == 2
        assert len(calls) == 1, calls
        assert received == [common_dir(os.path.abspath(str(repo)))], received

    def test_the_released_at_refusal_is_about_the_ref_and_nothing_else(self, tmp_path):
        """Round 2, finding 4. The clause about local mode sat inside a message
        for a different failure and could not fire in the case it described:
        local mode returns before `survey` is ever called."""
        repo = tmp_path / "repo"
        (mark_root(repo / "seal") / "threads" / "1700000001-alpha" / "frame").mkdir(
            parents=True
        )
        (
            repo / "seal" / "threads" / "1700000001-alpha" / "frame" / "design.md"
        ).write_text("# a\n", encoding="utf-8")
        git(repo, "init", "-q")
        r = subprocess.run(
            [
                sys.executable,
                SCRIPT,
                "--root",
                str(repo),
                "--released-at",
                "no/such/ref",
            ],
            capture_output=True,
            encoding="utf-8",
        )
        assert r.returncode == 2, r.stdout + r.stderr
        assert "does not resolve" in r.stderr, r.stderr
        assert "local mode" not in r.stderr, (
            "the ref refusal still talks about a state it cannot be in"
        )

    @pytest.mark.rule("an-empty-root-is-settled")
    @pytest.mark.parametrize("keep_empty_dir", [True, False], ids=["empty", "absent"])
    @pytest.mark.parametrize(
        "flags", [[], ["--apply"], ["--draft"]], ids=["report", "apply", "draft"]
    )
    def test_accepts_a_settled_root_and_says_so(self, tmp_path, keep_empty_dir, flags):
        """G7. After the last settle a fresh checkout has no `seal/threads/` at
        all and the tree that ran `--apply` has an empty one. Both are the state
        a complete settle reaches, and `settle` used to refuse the first at exit
        2 — so the command could not run on its own finished work. `--draft`
        there has no operation to write, and writes nothing (#1217)."""
        repo = settled_repo(tmp_path, keep_empty_dir)
        before = git(repo, "status", "--porcelain", "--untracked-files=all")
        argv = [sys.executable, SCRIPT, "--root", str(repo), "--released-at", "HEAD"]
        r = subprocess.run(argv + flags, capture_output=True, encoding="utf-8")
        assert r.returncode == 0, r.stdout + r.stderr
        assert "holds no work item" in r.stdout, r.stdout + r.stderr
        assert "A complete settle ends here" in r.stdout, r.stdout
        assert git(repo, "status", "--porcelain", "--untracked-files=all") == before

    @pytest.mark.rule("an-empty-root-is-settled")
    @pytest.mark.parametrize("arm", [False, True], ids=["report", "apply"])
    def test_accepts_a_settled_local_root_and_names_it(self, local, arm, capfd):
        """S8 of #955: a local root with no work item is settled too. The
        sentence names the root under the git directory, and says nothing
        about a fresh checkout, which carries no local root."""
        code, text = dry_run(local, capfd, *(["--apply"] if arm else []))
        assert code == 0, text
        home = os.path.join(str(local), ".git", "seal")
        assert text == (
            f"settle: {home} is the seal/ root, in local mode, and its threads/ "
            "holds no work item — nothing to show and nothing to remove. A "
            "complete settle ends here.\n"
        ), text

    # --- `--from`: the directories a person names (#1054) --------------------

    def test_a_run_without_from_prints_no_named_directory_listing(self, repo, capfd):
        """#1054 A1: the listing is printed only where a person named a
        directory, so a run without `--from` prints what it printed before;
        the cases above hold that output line for line."""
        write(repo, "adr/0001.md", "a decision\n")
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert settle.DOCUMENTS_HEADING not in text, text
        assert "adr/0001.md" not in text, text

    def test_from_lists_every_document_of_a_named_directory_in_gits_order(
        self, repo, capfd, monkeypatch
    ):
        """#1054 A2: every file git lists under the directory is a document,
        nested or of any extension, and an ignored file is none. Each is
        listed once in the order of the commits that add it, a moved file
        counting as added where it lands, with its last change beside it; a
        file changed in the working tree says so, and one no commit adds
        comes last. The path is read from the directory the command runs in,
        and the listing stands after the judgments and before what `--apply`
        removes."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        write(repo, "adr/0001.md", "one\n")
        write(repo, "adr/old/moved.md", "moved\n")
        commit(repo, "first records")
        first = stamp(repo)
        write(repo, "adr/sub/0002.md", "nested\n")
        write(repo, "adr/notes.txt", "no md extension\n")
        commit(repo, "second records")
        second = stamp(repo)
        write(repo, "adr/0001.md", "one, revised\n")
        commit(repo, "revise the first")
        third = stamp(repo)
        git(repo, "mv", "adr/old/moved.md", "adr/moved.md")
        commit(repo, "move one")
        fourth = stamp(repo)
        write(repo, "adr/.gitignore", "*.log\n")
        git(repo, "add", "adr/.gitignore")
        git(repo, "commit", "-qm", "ignore logs")
        fifth = stamp(repo)
        write(repo, "adr/build.log", "ignored\n")
        write(repo, "adr/0003.md", "untracked\n")
        # Staged and never committed: `ls-files` prints it after the
        # untracked file, and the listing puts it first by its path.
        write(repo, "adr/0000-staged.md", "staged\n")
        git(repo, "add", "adr/0000-staged.md")
        write(repo, "adr/0001.md", "one, revised again\n")
        monkeypatch.chdir(repo)
        code, text = dry_run(repo, capfd, "--from", "adr")
        assert code == 0, text
        assert (
            "\nfrom adr/: 7 documents\n"
            f"    adr/0001.md  added {first}  last changed {third}  changed in the "
            "working tree\n"
            f"    adr/notes.txt  added {second}  last changed {second}\n"
            f"    adr/sub/0002.md  added {second}  last changed {second}\n"
            f"    adr/moved.md  added {fourth}  last changed {fourth}\n"
            f"    adr/.gitignore  added {fifth}  last changed {fifth}\n"
            "    adr/0000-staged.md  no commit adds it\n"
            "    adr/0003.md  no commit adds it\n\n"
        ) in text, text
        assert "build.log" not in text, text
        assert "adr/old/" not in text, text
        heading = text.index(f"\n{settle.DOCUMENTS_HEADING}\n")
        assert (
            heading < text.index("\nfrom adr/") < text.index(settle.REMOVES_HEADING)
        ), text

    def test_a_merge_that_resolved_a_document_is_its_last_change(
        self, repo, capfd, monkeypatch
    ):
        """#1054, round 1's finding 1: a merge whose conflict resolution
        rewrote a document is the commit that last changed it, since `git log`
        prints a merge's own change only under `--cc`."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        write(repo, "adr/0001.md", "one\n")
        commit(repo, "a decision")
        first = stamp(repo)
        git(repo, "checkout", "-qb", "side")
        write(repo, "adr/0001.md", "side\n")
        commit(repo, "side")
        git(repo, "checkout", "-q", "main")
        write(repo, "adr/0001.md", "main\n")
        commit(repo, "main")
        # The merge conflicts and exits 1, which `git` here would raise on.
        subprocess.run(
            ["git", "-C", str(repo), "merge", "--no-ff", "-q", "side"],
            capture_output=True,
        )
        write(repo, "adr/0001.md", "resolved\n")
        commit(repo, "merge side, resolved")
        merged = stamp(repo)
        monkeypatch.chdir(repo)
        code, text = dry_run(repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/0001.md  added {first}  last changed {merged}\n" in text, text

    def test_a_clean_merge_of_two_edits_is_a_documents_last_change(
        self, repo, capfd, monkeypatch
    ):
        """#1054, round 4's finding 1: a merge with no conflict that combines
        two branches' edits to one document holds content neither parent
        holds. Its hunks are all ones `--cc` calls uninteresting, and
        `--name-status` still names it `MM`, so it is the last change."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        body = "".join(f"line {i}\n" for i in range(30))
        write(repo, "adr/0001.md", body)
        commit(repo, "a decision")
        first = stamp(repo)
        git(repo, "checkout", "-qb", "side")
        write(repo, "adr/0001.md", body.replace("line 25\n", "line 25, side\n"))
        commit(repo, "side edits the end")
        git(repo, "checkout", "-q", "main")
        write(repo, "adr/0001.md", body.replace("line 2\n", "line 2, main\n"))
        commit(repo, "main edits the start")
        git(repo, "merge", "--no-ff", "-q", "-m", "merge side", "side")
        merged = stamp(repo)
        monkeypatch.chdir(repo)
        code, text = dry_run(repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/0001.md  added {first}  last changed {merged}\n" in text, text

    def test_a_merge_that_wrote_a_document_no_parent_holds_adds_it(
        self, repo, capfd, monkeypatch
    ):
        """#1054, round 2's finding 1: a merge whose result holds a document
        neither parent holds is the commit that added it, since `--cc` gives
        that path one `A` per parent and an add is every letter `A`."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        write(repo, "adr/0001.md", "one\n")
        commit(repo, "a decision")
        git(repo, "checkout", "-qb", "side")
        write(repo, "adr/side.md", "side\n")
        commit(repo, "side")
        git(repo, "checkout", "-q", "main")
        write(repo, "adr/main.md", "main\n")
        commit(repo, "main")
        git(repo, "merge", "--no-ff", "--no-commit", "-q", "side")
        write(repo, "adr/0002.md", "written in the merge\n")
        commit(repo, "merge side, adding adr/0002.md")
        merged = stamp(repo)
        monkeypatch.chdir(repo)
        code, text = dry_run(repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/0002.md  added {merged}  last changed {merged}\n" in text, text

    def test_a_merge_that_rewrote_a_document_one_parent_lacks_changes_it(
        self, repo, capfd, monkeypatch
    ):
        """#1054, round 2's finding 1: a merge that rewrites a document only
        `side` holds prints `AM` under `--cc`, an `A` against `main` beside an
        `M` against `side`. Not every letter is `A`, so the merge changed the
        document and `side`'s commit still added it."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        write(repo, "adr/0001.md", "one\n")
        commit(repo, "a decision")
        git(repo, "checkout", "-qb", "side")
        write(repo, "adr/side.md", "side\n")
        commit(repo, "side adds a document")
        added = stamp(repo)
        git(repo, "checkout", "-q", "main")
        write(repo, "adr/main.md", "main\n")
        commit(repo, "main")
        git(repo, "merge", "--no-ff", "--no-commit", "-q", "side")
        write(repo, "adr/side.md", "side, rewritten in the merge\n")
        commit(repo, "merge side, rewriting adr/side.md")
        merged = stamp(repo)
        monkeypatch.chdir(repo)
        code, text = dry_run(repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/side.md  added {added}  last changed {merged}\n" in text, text

    def test_a_deletion_is_no_change_to_a_document_head_holds(
        self, repo, capfd, monkeypatch
    ):
        """#1054, round 2's finding 1: a status whose letters are `D` says the
        commit took the path out of its tree, so it is neither an add nor a
        change. Here `main` changes a document, `side` deletes it, and the
        merge keeps `main`'s content, so `--cc` names nothing at the merge and
        `side`'s deletion, which the walk reads after `main`'s change, is not
        the document's last change."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        write(repo, "adr/0001.md", "one\n")
        commit(repo, "a decision")
        first = stamp(repo)
        git(repo, "checkout", "-qb", "side")
        git(repo, "rm", "-q", "adr/0001.md")
        commit(repo, "side deletes it")
        git(repo, "checkout", "-q", "main")
        write(repo, "adr/0001.md", "one, revised\n")
        commit(repo, "main revises it")
        revised = stamp(repo)
        # A modify/delete conflict, which `git` here would raise on.
        subprocess.run(
            ["git", "-C", str(repo), "merge", "--no-ff", "-q", "side"],
            capture_output=True,
        )
        write(repo, "adr/0001.md", "one, revised\n")
        commit(repo, "merge side, keeping main's revision")
        monkeypatch.chdir(repo)
        code, text = dry_run(repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/0001.md  added {first}  last changed {revised}\n" in text, text

    def test_a_file_under_two_named_directories_is_listed_once(
        self, repo, capfd, monkeypatch
    ):
        """#1054 A3: `--from a` and `--from a/b` both hold `a/b/inner.md`, and
        it is listed once, under the first directory named that holds it;
        each path is read from the directory the command runs in."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        write(repo, "a/top.md", "top\n")
        write(repo, "a/b/inner.md", "inner\n")
        commit(repo, "a")
        monkeypatch.chdir(repo / "a")
        code, text = dry_run(repo, capfd, "--from", ".", "--from", "b")
        assert code == 0, text
        assert text.count("a/b/inner.md  ") == 1, text
        assert "\nfrom a/: 2 documents\n" in text, text
        assert "\nfrom a/b/: 0 documents\n" in text, text

    @pytest.mark.parametrize(
        "where, given, said",
        [
            (".", "missing", "names no directory"),
            (".", "docs/a.md", "names no directory"),
            ("docs", "adr", "names no directory"),
            (".", "{outside}", "is outside the repository"),
            (".", "../elsewhere", "is outside the repository"),
            (".", "seal", "is the seal/ root or under it"),
            (".", "seal/threads", "is the seal/ root or under it"),
        ],
        ids=[
            "missing",
            "a-file",
            "a-directory-of-the-top-read-from-a-subdirectory",
            "outside",
            "outside-and-relative",
            "the-root",
            "under-the-root",
        ],
    )
    def test_refuses_a_from_that_names_no_directory_to_read(
        self, repo, capfd, monkeypatch, tmp_path, where, given, said
    ):
        """#1054 A4: a path that is no directory of the working tree, one
        outside the repository, and the `seal/` root or a path under it, whose
        records the settle already reads, each exit 2 with one sentence naming
        the path, and nothing is read or removed. The sentence names the path
        as it was read, from the directory the command runs in, so `--from
        adr` run in `docs/` names `docs/adr` where `adr/` stands at the top
        (round 1's finding 2)."""
        (tmp_path / "elsewhere").mkdir()
        given = given.format(outside=tmp_path / "elsewhere")
        write(repo, "adr/0001.md", "a decision\n")
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        commit(repo, "a")
        before = files(repo)
        monkeypatch.chdir(repo / where)
        code, text = dry_run(repo, capfd, "--from", given)
        assert code == 2, text
        assert text.startswith(f"settle: --from {given} {said}"), text
        # The path the command read, which the person opens next.
        assert f" it reads as {os.path.abspath(given)} from " in text, text
        assert text.count("\n") == 1 and text.endswith(".\n"), text
        assert files(repo) == before

    def test_refuses_from_beside_apply_and_removes_nothing(self, repo, capfd):
        """#1054 A4: `--apply` removes only under `seal/threads/`, so a
        `--from` it accepted would read as one it acted on. The pair exits 2
        with one sentence naming both, and the released directory stays."""
        write(repo, "adr/0001.md", "a decision\n")
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        commit(repo, "a")
        before = files(repo)
        code, text = dry_run(repo, capfd, "--apply", "--from", str(repo / "adr"))
        assert code == 2, text
        assert text.startswith("settle: --from and --apply"), text
        assert text.count("\n") == 1 and text.endswith(".\n"), text
        assert files(repo) == before
        assert specs_dir(repo, "1700000001-a").is_dir()

    @pytest.mark.parametrize("committed", [True, False], ids=["committed", "no-head"])
    def test_a_root_with_no_work_item_lists_the_named_documents_and_is_settled(
        self, tmp_path, capfd, committed
    ):
        """#1054 A5: a root holding no work item lists the named documents,
        then prints the settled line, exit 0, with no `--released-at`. In a
        repository whose HEAD has no commit, every document is one no commit
        adds."""
        repo = tmp_path / "repo"
        mark_root(repo / "seal")
        write(repo, "adr/0001.md", "a decision\n")
        git(repo, "init", "-q")
        git(repo, "config", "user.email", "x@example.com")
        git(repo, "config", "user.name", "x")
        if committed:
            commit(repo, "a decision")
        listed = (
            f"added {stamp(repo)}  last changed {stamp(repo)}"
            if committed
            else "no commit adds it"
        )
        code = settle.main(["--root", str(repo), "--from", str(repo / "adr")])
        out = capfd.readouterr()
        text = out.out + out.err
        assert code == 0, text
        # The settled line names the root as git spells it, which on Windows
        # is not `str(repo)`; its words are read instead.
        assert text.startswith(
            f"{settle.DOCUMENTS_HEADING}\n"
            "\nfrom adr/: 1 document\n"
            f"    adr/0001.md  {listed}\n\n"
            "settle: seal/threads/ in "
        ), text
        assert "holds no work item" in text and "A complete settle ends here" in text
        assert text.count("\n") == settle.DOCUMENTS_HEADING.count("\n") + 6, text

    def test_a_named_directory_is_never_written(self, repo, capfd):
        """#1054 A6: the dry run with `--from`, then `--apply` removing a
        released work item, leave every file under the named directory with
        the path and the bytes it had, and its `git status` as it was."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        write(repo, "adr/0001.md", "a decision\n")
        write(repo, "adr/sub/0002.txt", "another\n")
        commit(repo, "a and its records")
        write(repo, "adr/0001.md", "a decision, revised\n")
        write(repo, "adr/0003.md", "untracked\n")

        def named():
            return {k: v for k, v in files(repo).items() if k.startswith("adr")}

        def status():
            return git(repo, "status", "--porcelain", "--untracked-files=all", "adr")

        before, said = named(), status()
        code, text = dry_run(repo, capfd, "--from", str(repo / "adr"))
        assert code == 0, text
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not specs_dir(repo, "1700000001-a").exists(), text
        assert named() == before
        assert status() == said

    # --- `--draft`: the released operations written literally (#1217) --------

    def test_draft_writes_each_operation_in_merge_order_and_names_what_it_missed(
        self, repo, capfd
    ):
        """S4 and S5. A was added before B and B's `change` quotes A's `to`,
        so only merge order leaves B's `to`, whatever their ids say. C's
        first `from` is not there: that operation is printed with its
        coordinate and reason, and C's next operation and D, after it, are
        placed. The run exits 0, writes only under the policy root, and
        leaves every released directory as it was."""
        item(repo, "1700000009-a", op("change", "S", "old sentence.", "y."))
        commit(repo, "a")
        item(repo, "1700000001-b", op("change", "S", "y.", "z."))
        commit(repo, "b")
        missed = op("change", "T", "gone words.", "w.")
        item(repo, "1700000005-c", missed + "\n" + op("add", "T", new="Kept."))
        commit(repo, "c")
        item(repo, "1700000002-d", op("add", "U", new="Rule."))
        commit(repo, "d")
        records = {k: v for k, v in files(repo).items() if k.startswith("seal")}
        code, text = dry_run(repo, capfd, "--draft")
        assert code == 0, text
        line = line_of(spec(missed), "- change")
        assert text == (
            "not placed  change  1700000005-c  "
            f"seal/threads/1700000005-c/frame/design.md:{line}  "
            "the `from` text is not in section `T` of docs/a.md\n"
            "placed 4 of 5 operations in docs/\n"
            f"{settle.DRAFTED}"
        ), text
        assert (repo / "docs" / "a.md").read_text(encoding="utf-8") == (
            DOC.replace("old sentence.", "z.")
            .replace("T's text.\n", "T's text.\n\nKept.\n")
            .replace("Last.\n", "Last.\n\nRule.\n")
        )
        assert git(repo, "status", "--porcelain") == " M docs/a.md\n"
        assert {k: v for k, v in files(repo).items() if k.startswith("seal")} == (
            records
        )

    def test_draft_creates_and_deletes_whole_documents(self, repo, capfd):
        """An `add` with no section creates its document, and a `remove`
        that empties one deletes it. A document written with CRLF is read
        and written with its line ends as they are."""
        (repo / "docs" / "b.md").write_bytes(b"## Only\r\n\r\nText.\r\n\r\n## Two\r\n")
        write(repo, "docs/c.md", "## Gone\n\nText.\n")
        commit(repo, "b and c")
        item(
            repo,
            "1700000001-a",
            "\n".join(
                [
                    op("add", new="# New", file="docs/new.md"),
                    op("remove", "Only", file="docs/b.md"),
                    op("remove", "Gone", file="docs/c.md"),
                ]
            ),
        )
        commit(repo, "a")
        code, text = dry_run(repo, capfd, "--draft")
        assert code == 0, text
        assert text.startswith("placed 3 of 3 operations in docs/\n"), text
        assert (repo / "docs" / "new.md").read_bytes() == b"# New\n"
        assert (repo / "docs" / "b.md").read_bytes() == b"## Two\r\n"
        assert not (repo / "docs" / "c.md").exists()

    def test_draft_creates_the_policy_root_its_first_document_needs(self, repo, capfd):
        """A repository whose policy root is absent gets it from the `add`
        that creates its first document."""
        git(repo, "rm", "-rq", "docs")
        commit(repo, "no policy root")
        item(repo, "1700000001-a", op("add", new="# New", file="docs/new.md"))
        commit(repo, "a")
        code, text = dry_run(repo, capfd, "--draft")
        assert code == 0, text
        assert (repo / "docs" / "new.md").read_bytes() == b"# New\n"

    @pytest.mark.parametrize(
        "other", [["--apply"], ["--from", "adr"]], ids=["apply", "from"]
    )
    def test_refuses_draft_beside_apply_or_from_and_writes_nothing(
        self, repo, capfd, other
    ):
        """S6: `--draft` writes the released operations and nothing else, so
        a flag beside it that it would ignore is refused with exit 2 and one
        sentence, and the tree is left as it was."""
        write(repo, "adr/0001.md", "a decision\n")
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        commit(repo, "a")
        other = [str(repo / "adr") if o == "adr" else o for o in other]
        before = files(repo)
        code, text = dry_run(repo, capfd, "--draft", *other)
        assert code == 2, text
        assert text.startswith("settle: --draft and " + other[0]), text
        assert text.count("\n") == 1 and text.endswith(".\n"), text
        assert files(repo) == before

    def test_draft_in_local_mode_reads_the_design_under_the_git_directory(
        self, local, gh, capfd
    ):
        """S7: the released design is read from its directory under the git
        directory, and the draft writes the repository's policy root."""
        local_item(local, "1700000001-a", "feat/1-a", op("add", "U", new="Rule."))
        gh.merged("feat/1-a", (11, merge(local, "feat/1-a")))
        records = sorted(p for p in (local / ".git" / "seal").rglob("*"))
        code, text = dry_run(local, capfd, "--draft")
        assert code == 0, text
        assert text.startswith("placed 1 of 1 operation in docs/\n"), text
        assert (local / "docs" / "a.md").read_text(encoding="utf-8") == (
            DOC.replace("Last.\n", "Last.\n\nRule.\n")
        )
        assert sorted(p for p in (local / ".git" / "seal").rglob("*")) == records


class Test_adding_commit:
    def test_accepts_the_oldest_add_of_each_path(self, tmp_path):
        """#1139. The root commit adds one fragment, and a settle's commit
        removes it and adds another with the same text, so each path names
        the pull request of its own add. What a person's `log.follow` and
        `log.showRoot` would change of this reading is held by
        `hooks/lib/gitcmd.py`, whose cases are `tests/hooks/test_gitcmd.py`."""
        repo = tmp_path / "repo"
        first = "seal/threads/1700000001-first/changelog.md"
        second = "seal/threads/1700000002-second/changelog.md"
        write(repo, first, "- the same text\n")
        git(repo, "init", "-q", "-b", "main")
        git(repo, "config", "user.email", "x@example.com")
        git(repo, "config", "user.name", "x")
        commit(repo, "the first work item (#1)")
        git(repo, "rm", "-q", first)
        write(repo, second, "- the same text\n")
        commit(repo, "the settle (#2)")
        assert settle.adding_commit(str(repo), "HEAD", first)[1] == 1
        assert settle.adding_commit(str(repo), "HEAD", second)[1] == 2

    def test_refuses_a_number_the_subject_does_not_end_with_and_a_failed_git(
        self, repo
    ):
        """#1139. A `(#N)` inside the subject is not the pull request's, so
        the adding commit names none. A path no commit adds has no adding
        commit. A ref `git` cannot read raises with what `git` said, so the
        release note's job stops rather than writing an entry with no link.
        Seen red with the subject's end anchor taken out, and with the check
        of `git`'s exit taken out."""
        path = "seal/threads/1700000001-a/changelog.md"
        write(repo, path, "- a\n")
        commit(repo, "fix: (#7) is not where the title ends")
        added = git(repo, "rev-parse", "HEAD").strip()
        assert settle.adding_commit(str(repo), "HEAD", path) == (added, None)
        missing = "seal/threads/1700000002-none/changelog.md"
        assert settle.adding_commit(str(repo), "HEAD", missing) == (None, None)
        with pytest.raises(RuntimeError, match="nosuch"):
            settle.adding_commit(str(repo), "nosuch", path)


class Test_module:
    def test_merge_order_is_the_commit_that_adds_the_spec(self, repo):
        """A work item's directory is born with its `routing.md`, often well
        before its `frame/design.md`; the order is the spec's, not the directory's."""
        early = specs_dir(repo, "1700000001-a")
        early.mkdir(parents=True)
        (early / "routing.md").write_text("# a — routing\n", encoding="utf-8")
        commit(repo, "a is declared")
        item(repo, "1700000002-b", op("add", "U", new="B."))
        commit(repo, "b")
        item(repo, "1700000001-a", op("add", "U", new="A."))
        commit(repo, "a is framed")
        ids = ["1700000001-a", "1700000002-b"]
        found = [i for i, _ in rules.order(str(repo), "HEAD", ids)]
        assert found == ["1700000002-b", "1700000001-a"], found

    def test_merge_order_of_an_id_that_is_not_ascii_is_its_designs_add(self, repo):
        """#1283. `rule_changes.py#order` reads the history with `-z`, so a
        design whose id git quotes under the default `core.quotePath` is
        placed by the commit that adds it, not last with no commit. Seen red
        against the reading without `-z`."""
        item(repo, "1700000001-정렬", op("add", "U", new="A."))
        commit(repo, "a is framed")
        added = git(repo, "rev-parse", "HEAD").strip()
        item(repo, "1700000002-b", op("add", "U", new="B."))
        commit(repo, "b is framed")
        ids = ["1700000001-정렬", "1700000002-b"]
        found = rules.order(str(repo), "HEAD", ids)
        assert found[0] == ("1700000001-정렬", added), found
        assert [i for i, _ in found] == ids, found

    def test_merge_order_of_a_moved_thread_is_its_first_add_before_the_move(self, repo):
        """The session-start move adds every 0.22.x thread's design in one
        commit, so a moved thread is placed by the commit that first added
        its design under the earlier path, and two threads moved together
        keep the order they merged in, not the order of their ids."""
        old = repo / "seal" / "specs"
        for name in ("1700000002-b", "1700000001-a"):
            (old / name).mkdir(parents=True)
            (old / name / rules.EARLIER[1]).write_text(spec([]), encoding="utf-8")
            commit(repo, f"{name} is framed under the earlier path")
        (repo / "seal" / "threads").mkdir()
        for name in ("1700000001-a", "1700000002-b"):
            (repo / "seal" / "threads" / name / "frame").mkdir(parents=True)
            git(
                repo,
                "mv",
                f"{rules.EARLIER[0]}/{name}/{rules.EARLIER[1]}",
                f"seal/threads/{name}/{rules.DESIGN}",
            )
        commit(repo, "the session-start move")
        ids = ["1700000001-a", "1700000002-b"]
        found = [i for i, _ in rules.order(str(repo), "HEAD", ids)]
        assert found == ["1700000002-b", "1700000001-a"], found

    def test_merge_order_of_local_specs_is_their_merge_commits_place(self, repo):
        """#955: no commit adds a local spec, so `rule_changes.py#merge_order`
        sorts `(id, merge commit)` pairs by each commit's place on the ref,
        whatever order they are handed in. A commit the ref does not reach
        comes last."""
        a = merge(repo, "feat/1-a")
        b = merge(repo, "feat/2-b")
        stray = "0" * 40
        pairs = [("1700000002-b", b), ("1700000003-c", stray), ("1700000001-a", a)]
        assert rules.merge_order(str(repo), "HEAD", pairs) == [
            ("1700000001-a", a),
            ("1700000002-b", b),
            ("1700000003-c", stray),
        ]

    def test_a_ref_that_does_not_resolve_is_refused_rather_than_empty(self, tree):
        """The quiet zero this is written against: a ref nothing can read makes
        every work item look unreleased, and the report would then say there is
        nothing to do."""
        assert settle.survey(str(tree), "no/such/ref") is None

    def test_the_dry_runs_headings_say_who_decides(self):
        """Contract rule 14: the sentences a person acts on are pinned, not only
        their presence."""
        # The headings the dry run prints, which the settling session reads
        # for what it decides under each.
        assert "writes each section as its group's latest decision" in flat(
            settle.GROUPS_HEADING
        )
        assert "order them by content" in flat(settle.UNORDERED)
        # The four kinds of the skill's step 6, in its table's order (#1045).
        assert (
            "moot, answered, a measurement no record asks for, or a measurement "
            "to re-home" in flat(settle.ROWS_HEADING)
        )
        assert "close with `closed` and what closed it" in flat(settle.ROWS_HEADING)
        # The judgments heading the dry run prints, read the same way.
        assert "grouped by the document each stands on" in flat(
            settle.JUDGMENTS_HEADING
        )
        assert (
            "rewrites a section where one kind of judgment recurs or kept "
            "costing rounds" in flat(settle.JUDGMENTS_HEADING)
        )
        # The earlier settles' rows: the script matches none of them to a
        # row above, and the kind is the settling session's (#1281).
        assert "The script matches no row to another" in flat(settle.EARLIER_HEADING)
        assert (
            "whether a row here is one kind with a row above is the settling "
            "session's to judge" in flat(settle.EARLIER_HEADING)
        )
        # The named directories' heading: the session proposes, the person
        # marks (#1054).
        assert "The settling session proposes each one as promote or skip" in flat(
            settle.DOCUMENTS_HEADING
        )
        assert "the person marks it" in flat(settle.DOCUMENTS_HEADING)
        # What the dry run says `--apply` removes, which the note can keep
        # where the dry run cannot say so (#1139).
        assert (
            "each released directory whose record holds no open row, unless "
            "`--apply`, which alone reads the published notes, finds its entry "
            "missing from a note built from the fragments"
            in flat(settle.REMOVES_HEADING)
        )

    def test_the_command_is_reachable_by_the_name_a_document_gives_it(self):
        """A6. The pair rule is
        `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`'s;
        this is the instance, asked here so a missing twin
        names this work item rather than a parametrisation. Since #1051 the
        name is `seal settle`, run here the way a person types it."""
        wrapper = os.path.join(ROOT, "bin", "seal")
        command = (
            [os.environ.get("COMSPEC", "cmd.exe"), "/c", f"{wrapper}.cmd"]
            if os.name == "nt"
            else [wrapper]
        )
        done = subprocess.run(
            [*command, "settle", "--help"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
        assert done.returncode == 0, done.stderr
        assert done.stdout.startswith("usage: seal settle"), done.stdout

    @pytest.mark.parametrize(
        "which, phrase",
        [
            ("READER", "it is where a record's open rows are read from"),
            ("OPTIN", "it is what finds the repository's seal/ root"),
            (
                "ROUTING",
                "it is what reads the branch a local work item's `routing.md` "
                "names and counts a work item's round records",
            ),
            ("CONFIG", "it is what reads a plan's *Judgments of the run* table"),
            ("RULES", "it is what reads a design's `## Rule changes`"),
            (
                "FOLD_CHECK",
                "it is what reads the index and the one read after an apply",
            ),
            (
                "GITCMD",
                "it is what holds what this command reads of `git log` to one "
                "reading under any git configuration",
            ),
        ],
    )
    def test_each_sibling_is_refused_with_its_own_purpose(
        self, which, phrase, monkeypatch, capsys
    ):
        """Round 1, ⬜ 5 — #590's second half, per file: the table entry for each
        real sibling, not an entry the case put there itself. A copy taken alone
        stops at `OPTIN` first, so the class case never reaches the other one."""
        path = getattr(settle, which)
        real = os.path.isfile
        monkeypatch.setattr(
            os.path, "isfile", lambda p: False if p == path else real(p)
        )
        with pytest.raises(SystemExit) as raised:
            settle.load(path, "absent")
        assert raised.value.code == 2
        assert phrase in capsys.readouterr().err

    def test_a_missing_sibling_reader_is_a_sentence_and_not_a_traceback(
        self, tmp_path, monkeypatch, capsys
    ):
        """`spec_from_file_location` hands back a spec for any path ending in
        `.py`, present or not, so a missing sibling reaches `exec_module` and dies
        with `FileNotFoundError`. This case keeps `settle.load` from that shape:
        the refusal is exit 2 on stderr, and it names what the missing file is
        for, per file."""
        missing = str(tmp_path / "not-here.py")
        monkeypatch.setitem(
            settle.PURPOSES, missing, "it is where the fold record is read from"
        )
        with pytest.raises(SystemExit) as raised:
            settle.load(missing, "absent")
        err = capsys.readouterr().err
        assert raised.value.code == 2, raised.value
        assert "not-here.py" in err, err
        assert "fold record" in err, (
            "the refusal does not say what the missing file was for"
        )

    def test_surveys_docstring_does_not_invite_the_mutation_that_reopens_finding_4(
        self,
    ):
        """Round 2, finding 6. `apply` performs the second traversal `survey`'s
        docstring warned against, and the two contradicted each other — the stale
        half being the one a reader meets first. A pin catches the edit; a
        docstring is what a reader consults before making it."""
        import ast

        with open(SCRIPT, encoding="utf-8") as f:
            tree_ = ast.parse(f.read())
        doc = {
            node.name: ast.get_docstring(node) or ""
            for node in tree_.body
            if isinstance(node, ast.FunctionDef)
        }
        assert "the retirement are both derived from" not in doc["survey"], doc[
            "survey"
        ]
        assert "does not take its candidates from here" in doc["survey"], doc["survey"]
        assert "not taken from `survey`" in doc["apply"], doc["apply"]

    @pytest.mark.parametrize(
        "args, purpose, absent",
        [
            (
                ["--root", "{root}"],
                "it is what finds the repository's seal/ root",
                "fold record",
            )
        ],
        ids=["optin.py"],
    )
    def test_a_script_copied_alone_exits_2_and_names_what_it_misses(
        self, tmp_path, args, purpose, absent
    ):
        """#590. A copy of this script taken without its siblings exits 2, with
        a sentence naming the missing path and what it is for: 2 means the
        input or the tree was unusable and nothing was read, and a sibling that
        is not beside the command is that kind. It loads `hooks/lib/optin.py`
        before it reads the root, so `--root` reaches the loader. The loader
        used to give every file the fold record's purpose, which is false of
        `optin.py`, so that phrase must not appear."""
        script = TARGET
        name = script.rsplit("/", 1)[1]
        alone = tmp_path / "alone"
        alone.mkdir()
        copy = alone / name
        with open(os.path.join(ROOT, *script.split("/")), encoding="utf-8") as f:
            copy.write_text(f.read(), encoding="utf-8")
        repo = tmp_path / "repo"
        repo.mkdir()
        done = subprocess.run(
            [sys.executable, str(copy), *(a.format(root=repo) for a in args)],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(repo),
        )
        assert done.returncode == 2, (done.returncode, done.stderr)
        assert "Traceback" not in done.stderr, done.stderr
        assert names_path(str(alone), done.stderr), (
            f"the refusal does not name the missing path: {done.stderr}"
        )
        assert purpose in done.stderr, (
            f"the refusal does not say what the missing file is for: {done.stderr}"
        )
        if absent:
            assert absent not in done.stderr, done.stderr

    def test_the_pinned_checks_read_under_the_root_alone(self):
        """#688's D3: the constant this command's walk of work items rests on,
        held under `seal/`. Widening it to a top-level `specs/` turns this red,
        which is the probe that work item's plan names for `SPECS`.
        `tests/hooks/test_routing.py` holds `hooks/lib/routing.py#WORK_ITEMS` to the
        same, and `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`
        classifies every shipped command by what keeps it off a reference
        root."""
        assert settle.SPECS == "seal/threads"


test_census = census_case(TARGET)
