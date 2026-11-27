"""`skills/settle/scripts/settle.py`, one class per function.

`settle` reads before it removes: what counts as released and the root it
refuses (#458, closing #83). Its dry run groups the released specs whose
`## Rule changes` name one section, in merge order, lists the specs to read
whole and every open row, and refuses nothing; `--apply` removes each
released directory whose record holds no open row in the working tree and
writes no policy document (#1033), and where the root is shared keeps one
whose version's published note does not carry its entry, read from `gh`'s
release list (#1139). In local mode it reads the root under the git
directory and asks `gh` which pull request merged from each work item's
branch (#955). A file in a work item's directory named like a record it
reads, at another path, is named by both arms as not read and decides
nothing (#1126); `Test_misplaced` holds the walk that finds it. With
`--from`, the dry run lists every document of each directory a person
names and writes nothing there (#1054). With `--draft`, it writes every
released operation into the policy root in merge order and names each one
not placed (#1217).

`Test_report` and `Test_apply` drive the two arms, `survey` with `report`
or `apply`, mostly over a world drawn on disk, or `tests/conftest.py`'s
`tree`, whose readers that ask git are answered from the disk
(`answered`), and over a real history where the fact is what such a reader
makes of git. `Test_main` runs the command: each of
its arms once over a real history with every reader real, and over a local
root whose `gh` is answered in process; where a case's fact is one reader,
the others are `answered`. `Test_module` holds the loader, the launcher, the answer the
command takes from `rule_changes.py#order`, asked over the repositories
this file builds, and the copy run without its siblings. `Test_threads`
holds the work items' place under the root's own name.

#942's phase 6 placed these cases from
`tests/text/test_settle_reads_before_it_removes.py` and
`tests/behaviour/test_settle_applies_rule_changes_in_place.py`, which keep the cases
that read the skill, the documents, the READMEs, the checklist and the cheat
sheets. The copy's case came from `tests/test_a_script_copied_alone_exits_2.py`
and the case `Test_threads` replaced from
`tests/behaviour/test_a_reference_root_is_read_and_never_taken.py` in #942's
round 9 fix pass, each a case of this module alone.
"""

import inspect
import io
import json
import os
import shutil
import subprocess
import sys
import time

import conftest
import pytest
import test_unverified_check
from conftest import (
    DOC,
    ROOT,
    as_called,
    census_case,
    commit_everything,
    commit_everything_as_e,
    config_json,
    git,
    git_out,
    line_of,
    load_module,
    mark_root,
    op,
    spec,
    symlink_or_skip,
    write,
)
from conftest import flattened as flat
from test_unverified_check import CANONICAL, WORK, _committed, memo

TARGET = "skills/settle/scripts/settle.py"

SCRIPT = os.path.join(ROOT, "skills", "settle", "scripts", "settle.py")

settle = load_module(SCRIPT, "settle")
# `show` came here from `unverified_check.py` (#1482), and its cases read
# the world that file builds once.
plain = test_unverified_check.plain
rules = load_module(
    os.path.join(ROOT, "skills", "settle", "scripts", "rule_changes.py"),
    "agentic_rule_changes",
)
# The runner every git and `gh` command of `settle` starts through, the one
# instance `lib/sibling.py#load` hands both scripts.
gitcmd = settle.sibling.load("lib/gitcmd.py")


def item(repo, name, changes):
    path = repo / "seal" / "threads" / name
    (path / "frame").mkdir(parents=True, exist_ok=True)
    (path / "frame" / "design.md").write_text(spec(changes), encoding="utf-8")


def stamp(repo):
    """HEAD's short hash and date, as the named-directory listing prints a
    commit."""
    return git_out(repo, "log", "-1", "--format=%h %cs")


# --- the worlds, each built once per module and copied per case -------------
#
# A case commits, merges and tags in the repository it is given, so each
# world is built once and every case takes a copy under its own `tmp_path`
# (`CONTRIBUTING.md` *The test layout*, a rewritten module builds its world
# once). The copy stands at `tmp_path / "repo"`, where the cases' paths expect
# it. A case that only reads a world reads it where it stands.


def a_copy(world, tmp_path):
    """WORLD copied to TMP_PATH/repo, links kept as links; the copy."""
    repo = tmp_path / "repo"
    shutil.copytree(world, repo, symlinks=True)
    return repo


def started(repo):
    """REPO given a git history on `main` whose one commit, `base`, holds
    what REPO holds now."""
    git_out(repo, "init", "-q", "-b", "main")
    git_out(repo, "config", "user.email", "x@example.com")
    git_out(repo, "config", "user.name", "x")
    commit_everything(repo, "base")
    return repo


def shared_files(repo):
    """REPO holding `docs/a.md` and the marked `seal/` root, the files of
    `shared_repo` and of `drawn`; REPO."""
    write(repo, "docs/a.md", DOC)
    mark_root(repo / "seal")
    return repo


@pytest.fixture(scope="module")
def _shared_world(tmp_path_factory):
    return started(shared_files(tmp_path_factory.mktemp("settle-shared") / "repo"))


@pytest.fixture
def shared_repo(tmp_path, _shared_world):
    """A repository on `main` whose one commit holds `docs/a.md` and the
    `seal/` root, marked, with no work item."""
    return a_copy(_shared_world, tmp_path)


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


def asks(monkeypatch, read):
    """`(answer, asked)`: what READ() returned, and each `git` command it
    started, in order, as its argv and what it was given on stdin. Every
    run stays real."""
    real, asked = subprocess.run, []

    def run(argv, *args, **kwargs):
        if argv[0] == "git":
            asked.append((tuple(argv), kwargs.get("input")))
        return real(argv, *args, **kwargs)

    with monkeypatch.context() as patched:
        patched.setattr(subprocess, "run", run)
        answer = read()
    return answer, asked


def repeated(asked):
    """Each of ASKED, as `asks` lists them, that an earlier one equals,
    named by its words after `-C <root>` and what it was given."""
    seen, again = set(), []
    for argv, given in asked:
        if (argv, given) in seen:
            again.append((" ".join(argv[argv.index("-C") + 2 :]), given))
        seen.add((argv, given))
    return again


def calls(monkeypatch, read):
    """The number of `git` commands READ() starts."""
    return len(asks(monkeypatch, read)[1])


def unanswered(monkeypatch, *words):
    """Each process run whose argv, `as_called` reads it, holds WORDS in a
    row raises `subprocess.TimeoutExpired`, as a command past
    `lib/gitcmd.py#TIMEOUT` does; every other run is real. Returns the
    argv of each run WORDS matched."""
    real, asked, n = subprocess.run, [], len(words)

    def run(argv, *args, **kwargs):
        held = as_called(argv)
        if not any(held[i : i + n] == list(words) for i in range(len(held))):
            return real(argv, *args, **kwargs)
        asked.append(list(argv))
        raise subprocess.TimeoutExpired(list(argv), gitcmd.TIMEOUT)

    monkeypatch.setattr(subprocess, "run", run)
    return asked


def past_the_bound(held):
    """The runner's line for the git or `gh` argv HELD that did not finish:
    the program and the arguments after `-C <root>`, as `as_called` reads
    them, or after the path `shutil.which` found for `gh`."""
    git = "-C" in held
    held = as_called(held)
    shown = ["git", *held[held.index("-C") + 2 :]] if git else ["gh", *held[1:]]
    return f"`{' '.join(shown)}` did not finish within {gitcmd.TIMEOUT} seconds"


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
    (repo / "seal" / "config.json").write_text(config_json(*rows), encoding="utf-8")


# --- the drawn worlds: a case of what `settle` makes of its input (#1581) ---
#
# A case whose fact is how `survey`, `report`, `apply` or `draft` read what
# they are given writes that on disk, in `drawn`, which has no history, or
# in a world that has one. `answered` answers each reader that asks git from
# the disk, and every other reader reads the disk as a run does. Each
# reader it answers is real, beside every other, in one run of each arm of
# `main` in `Test_main`:
#
#   the dry run's merge order  `test_two_specs_on_one_sentence_are_one_group_in_merge_order`
#   the release at a ref       `test_s5_settle_shows_a_work_item_released_under_agentic_seal`
#   the published note         `test_apply_keeps_a_directory_its_published_note_does_not_carry`
#   the earlier settles        `test_the_judgments_earlier_settles_removed_are_read_from_the_history`
#   `--from`                   `test_from_lists_every_document_of_a_named_directory_in_gits_order`
#   `--draft`                  `test_draft_writes_each_operation_in_merge_order_and_names_what_it_missed`
#   local mode                 `test_local_mode_lists_a_released_and_an_unreleased_item`
#
# and keeps cases of its own over a real history, which say that the
# reading and git agree where those runs do not reach:
#
#   released            `Test_report::test_a_released_work_item_whose_id_is_not_ascii_is_a_candidate`
#   show                `Test_show`
#   rule_changes.order  `Test_module`'s `merge_order` cases
#   rule_changes._ancestor
#                       `Test_report::test_two_specs_on_parallel_branches_at_one_place_are_one_group_unordered`,
#                       for two commits no ancestry orders
#   resolves, released_local, rule_changes.merge_order
#                       the local runs of `Test_main` that merge a pull
#                       request, and `Test_module`'s `merge_order` cases
#   earlier_judgments   the cases of `Test_report` that remove plans in a history
#   git_fields          `Test_tracked_text`, the merge cases of `Test_main`'s
#                       `--from`, and
#                       `Test_report::test_every_open_row_is_listed_with_the_paths_it_names`
#   notes               the cases of `Test_apply` and `Test_main` that tag a `changelog.md`


def has_history(repo):
    return (repo / ".git" / "HEAD").is_file()


def recorded(repo, rel, message):
    """REL in REPO committed under MESSAGE, where REPO has a history. A
    drawn world has none, and its readers read the disk."""
    if has_history(repo):
        git_out(repo, "add", "--", rel)
        git_out(repo, "commit", "-qm", message)


def drawn_files(root):
    """Every file under ROOT outside `.git/`, `/`-joined, in path order."""
    out = []
    for here, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d != ".git"]
        out += [os.path.relpath(os.path.join(here, n), root) for n in names]
    return sorted(p.replace(os.sep, "/") for p in out)


def answered(monkeypatch, repo, real=(), unreleased=(), merged=()):
    """`settle`'s readers that ask git answered from what REPO's disk holds,
    each but those REAL names. Where REPO has no history, any process
    `lib/gitcmd.py` starts raises, so a case that leans on one is told.

      released           each work item directory on disk but UNRELEASED
      show               the file on disk (`read_text`)
      order              the designs in MERGED's order, then the rest as
                         handed, on one line of history (`_ancestor`)
      resolves           every ref
      released_local     each local work item but UNRELEASED, merged by
                         pull request #1, #2 and on in id order
      merge_order        the merge commits in the order handed, on one line
                         of history
      earlier_judgments  no plan removed
      git_fields         every file on disk: what git lists where it all
                         is committed. `documents`, its other caller, reads
                         git under REAL
      notes              no `changelog.md` at the ref (`NO_FRAGMENT`)
    """
    rule_changes = settle.sibling.load(settle.RULES)
    placed = {}

    def order(root, ref, ids, specs):
        held = [i for i in merged if i in ids] + [i for i in ids if i not in merged]
        placed.update((f"adds {i}", n) for n, i in enumerate(held))
        return [(i, f"adds {i}") for i in held]

    def merge_order(root, ref, pairs):
        placed.update((commit, n) for n, (_, commit) in enumerate(pairs))
        return list(pairs)

    answers = {
        (settle, "released"): lambda root, ref, specs: (
            set(settle.work_items(root, specs)) - set(unreleased)
        ),
        (settle, "show"): lambda root, ref, rel: settle.read_text(root, rel),
        (rule_changes, "order"): order,
        (settle, "resolves"): lambda root, ref: True,
        (settle, "released_local"): lambda root, records, ref, ids, specs: (
            {
                i: (n, f"merges {i}")
                for n, i in enumerate(ids, 1)
                if i not in unreleased
            },
            {i: "unreleased, as the case answers it" for i in ids if i in unreleased},
        ),
        (rule_changes, "merge_order"): merge_order,
        (rule_changes, "_ancestor"): lambda root, a, b: placed[a] < placed[b],
        (settle, "earlier_judgments"): lambda *_args: ([], [], 0),
        (settle, "git_fields"): lambda root, *args: drawn_files(root),
        (settle, "notes"): lambda root, ref, ids, specs: {
            i: (False, settle.NO_FRAGMENT.format(ref=ref)) for i in ids
        },
    }
    for (module, name), answer in answers.items():
        if name not in real:
            monkeypatch.setattr(module, name, answer)
    if not has_history(repo):

        def refused(command, *_args, **_kwargs):
            raise AssertionError(f"a drawn world started {command}")

        monkeypatch.setattr(gitcmd, "_start", refused)


@pytest.fixture
def drawn(tmp_path, monkeypatch):
    """`shared_repo` drawn on disk with no history, its readers `answered`:
    `docs/a.md`, the marked `seal/` root, and an empty `.git/`, which
    `lib/optin.py#git_common_dir` reads as the git directory without a
    process."""
    repo = shared_files(tmp_path / "repo")
    (repo / ".git").mkdir()
    answered(monkeypatch, repo)
    return repo


@pytest.fixture(scope="module")
def _tree_world(tmp_path_factory):
    """`tests/conftest.py`'s `tree`, built once per module by that fixture's
    own function, so the world keeps its one definition there."""
    return conftest.tree.__wrapped__(tmp_path_factory.mktemp("settle-tree"))


@pytest.fixture
def tree_copy(tmp_path, _tree_world):
    """A copy of `tests/conftest.py`'s `tree` with its history, for a case
    whose reader asks git."""
    return a_copy(_tree_world, tmp_path)


@pytest.fixture
def answered_tree(tmp_path, monkeypatch, _tree_world):
    """`tests/conftest.py`'s `tree` drawn on disk with no history, its
    readers `answered`: `alpha`, `beta` and `gamma` are released and `delta`
    is not, as the fixture's history holds them. The `.git/` is empty, as
    `drawn`'s is."""
    repo = tmp_path / "repo"
    shutil.copytree(_tree_world, repo, ignore=shutil.ignore_patterns(".git"))
    (repo / ".git").mkdir()
    answered(monkeypatch, repo, unreleased={"1700000004-delta"})
    return repo


def no_rule(repo, work_item_id):
    """Give a released spec a `## Rule changes` that changes nothing, and
    commit it."""
    path = repo / "seal" / "threads" / work_item_id / "frame" / "design.md"
    path.write_text(
        path.read_text(encoding="utf-8")
        + "\n## Rule changes\n\n- nothing\n  why: a moment.\n",
        encoding="utf-8",
    )
    recorded(repo, f"seal/threads/{work_item_id}", f"{work_item_id} states no rule")


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
    recorded(repo, f"seal/threads/{name}", f"released {name}")
    return item


def released_item(repo, name, held):
    """A released work item holding HELD, `{path in its directory: text}`,
    committed on its own path like `moment`."""
    path = repo / "seal" / "threads" / name
    for rel, text in held.items():
        write(path, rel, text)
    recorded(repo, f"seal/threads/{name}", f"released {name}")
    return path


def standing(repo, name):
    """A work item NAME on REPO's disk, holding a `routing.md` and never
    committed: released where `answered` reads `released` from the disk."""
    write(specs_dir(repo, name), "routing.md", f"# {name} — routing\n")


def judgments_plan(rows, heading="## Judgments of the run"):
    """A `frame/plan.md` whose HEADING, on line 3, holds ROWS under the
    exact *Judgments of the run* header."""
    table = "".join(f"| {' | '.join(row)} |\n" for row in rows)
    return (
        f"# Implementation Plan: x\n\n{heading}\n\n"
        "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n" + table
    )


def imported(repo, commits):
    """COMMITS written in REPO by one `git fast-import`. Each is `(ref,
    parents, subject, changes, tag)`: REF the branch it lands on; PARENTS
    the commit it is made from, then each it merges, as a committish or as
    `:<n>`, the Nth of COMMITS from 1; CHANGES `{path: text}`, a text of
    None deleting the path, a directory with all it holds; TAG the tag
    pointed at it, or None. Neither the index nor the working tree moves."""
    who = f"x <x@example.com> {int(time.time())} +0000\n"

    def data(text):
        raw = text.encode("utf-8")
        return b"data %d\n%s\n" % (len(raw), raw)

    stream = b""
    for n, (ref, parents, subject, changes, tag) in enumerate(commits, 1):
        stream += f"commit {ref}\nmark :{n}\nauthor {who}committer {who}".encode()
        stream += data(subject) + f"from {parents[0]}\n".encode()
        stream += "".join(f"merge {p}\n" for p in parents[1:]).encode()
        for path, text in changes.items():
            if text is None:
                stream += f"D {path}\n".encode()
            else:
                stream += f"M 100644 inline {path}\n".encode() + data(text)
        stream += b"\n"
        if tag:
            stream += f"reset refs/tags/{tag}\nfrom :{n}\n\n".encode()
    subprocess.run(
        ["git", "-C", str(repo), "fast-import", "--quiet"],
        input=stream,
        check=True,
        capture_output=True,
    )


def branch_of(repo):
    """The branch REPO's HEAD names, as `refs/heads/<name>`."""
    return (repo / ".git" / "HEAD").read_text(encoding="utf-8").split()[-1]


def committed(repo, *commits):
    """`{subject: (commit, short hash)}` for COMMITS, each `(subject,
    {path: text}, tag)` as `imported` reads them, written in order on the
    branch REPO is on. The index and the working tree are then reset to the
    last, where committing through them leaves them, and a file nothing
    tracks stays. One `git fast-import`, a reset and one `git log`, where
    committing through the working tree takes three processes a commit."""
    branch = branch_of(repo)
    imported(
        repo,
        [
            (branch, [f"{branch}^0" if n == 0 else f":{n}"], subject, changes, tag)
            for n, (subject, changes, tag) in enumerate(commits)
        ],
    )
    git_out(repo, "reset", "-q", "--hard")
    printed = git_out(repo, "log", f"-{len(commits)}", "--format=%s%x00%H %h")
    return {
        subject: tuple(ids.split())
        for subject, ids in (line.split("\0") for line in printed.splitlines())
    }


def removed_plan(repo, name, plan, added, removed, tag=None):
    """A work item whose PLAN a commit with subject ADDED adds, TAG holds
    where given, and a commit with subject REMOVED deletes with its
    directory, as an earlier settle's `--apply` leaves it. `(adding commit,
    removing commit's short hash)`.

    One `git fast-import` writes both commits on the branch REPO is on, and
    one `git log` reads their ids: the second commit's tree is the first's
    parent's, so the working tree and the index stand as they did, where
    committing through them takes six processes, seven with a tag."""
    branch, path = branch_of(repo), f"seal/threads/{name}"
    imported(
        repo,
        [
            (branch, [f"{branch}^0"], added, {f"{path}/frame/plan.md": plan}, tag),
            (branch, [":1"], removed, {path: None}, None),
        ],
    )
    (_, short), (adding, _) = (
        line.split()
        for line in git_out(repo, "log", "-2", "--format=%H %h").splitlines()
    )
    return adding, short


def three_removals(repo):
    """Three removing commits, each deleting one plan of one row as an
    earlier settle's `--apply` leaves it, and a released work item. The
    lines each work item prints in the earlier section, newest removal
    first."""
    printed = []
    for n in range(1, 4):
        name = f"170000000{n}-old"
        _, short = removed_plan(
            repo,
            name,
            judgments_plan([(f"2026-10-0{n}", f"judged {n}", "y", "z")]),
            f"the old work item {n} (#{n})",
            f"settle 0.{n}.0 (#{n + 10})",
            f"v0.{n}.0",
        )
        printed.insert(
            0,
            f"    {name}  released in v0.{n}.0; removed by {short} (#{n + 10})\n"
            f"        {short}^:seal/threads/{name}/frame/plan.md:7  "
            f"2026-10-0{n}  judged {n}\n"
            "            grounds: y\n",
        )
    released_item(repo, "1700000009-new", {"routing.md": "# new — routing\n"})
    return printed


@pytest.fixture(scope="module")
def _removals_world(tmp_path_factory, _shared_world):
    repo = a_copy(_shared_world, tmp_path_factory.mktemp("settle-removals"))
    return repo, three_removals(repo)


@pytest.fixture
def removals(_removals_world, monkeypatch):
    """`(repo, printed)`: `shared_repo` after `three_removals`, and the
    lines that returned, read where the world stands, so a case reads and
    writes nothing; the readers but `earlier_judgments` `answered`."""
    answered(monkeypatch, _removals_world[0], real={"earlier_judgments"})
    return _removals_world


@pytest.fixture(scope="module")
def _one_removal_world(tmp_path_factory, _shared_world):
    repo = a_copy(_shared_world, tmp_path_factory.mktemp("settle-one-removal"))
    removed_plan(
        repo,
        "1700000001-old",
        judgments_plan([("2026-10-01", "x", "y", "z")]),
        "the old work item (#3)",
        "settle 0.1.0 (#7)",
        "v0.1.0",
    )
    standing(repo, "1700000002-new")
    return repo


@pytest.fixture
def one_removal(_one_removal_world, monkeypatch):
    """`shared_repo` after one tagged plan's removal, and a work item
    `standing`, read where it stands, as `removals` is."""
    answered(monkeypatch, _one_removal_world, real={"earlier_judgments"})
    return _one_removal_world


@pytest.fixture(scope="module")
def two_designs(tmp_path_factory, _shared_world):
    """`shared_repo` after two commits, each adding a design that adds a
    rule to `S`. A case reads it where it stands and changes nothing."""
    repo = a_copy(_shared_world, tmp_path_factory.mktemp("settle-two-designs"))
    item(repo, "1700000001-a", op("add", "S", new="A."))
    commit_everything(repo, "a")
    item(repo, "1700000002-b", op("add", "S", new="B."))
    commit_everything(repo, "b")
    return repo


def earlier_block(text):
    """The dry run's section of the judgments earlier settles removed,
    without its heading."""
    return text.split(f"\n{settle.EARLIER_HEADING}\n")[1].split(
        f"\n\n{settle.REMOVES_HEADING}"
    )[0]


def not_read(name, rel, place):
    """The line naming a misplaced record file, as the dry run and `--apply`
    print it."""
    return f"seal/threads/{name}/{rel}, named like `{place}` and away from its place"


def docs_text(repo):
    return {p.name: p.read_text(encoding="utf-8") for p in (repo / "docs").glob("*")}


def merged_history(repo, base, side, main, merge):
    """`{subject: stamp}` for four commits `imported` writes on REPO's
    `main`, each stamped as `stamp` prints it: BASE on `main`, SIDE on a new
    branch `side` from it, MAIN on `main` from BASE, and MERGE, the merge of
    `side` into `main`, over `main`'s tree. Each is `(subject, {path:
    text})`, a text of None deleting the path. The working tree and the
    index are then reset to the merge, where a merge committed through them
    leaves them.

    Git reads a merge by its tree and its parents, so these are the commits
    a checkout, the edits and `git merge` leave, written in three processes
    where those take about twenty."""
    main_ref, side_ref = "refs/heads/main", "refs/heads/side"
    imported(
        repo,
        [
            (main_ref, ["main^0"], *base, None),
            (side_ref, [":1"], *side, None),
            (main_ref, [":1"], *main, None),
            (main_ref, [":3", ":2"], *merge, None),
        ],
    )
    git_out(repo, "reset", "-q", "--hard", "main")
    printed = git_out(repo, "log", "--format=%s%x00%h %cs", "main")
    return dict(line.split("\0") for line in printed.splitlines())


# The branch the release merges to, in the fixtures below. A name that
# appears nowhere else in the output, so the assertions on it read the base
# and nothing else.
BASE = "release-target"


def at(repo, ref, *args):
    """`(exit code, what a person reads)` for `survey` at `ref`, the way
    `main` reaches it with `--released-at ref` at the top of REPO, the
    `seal/` root resolved as `main` resolves it and `--all-earlier` among
    ARGS."""
    out = io.StringIO()
    optin = settle.sibling.load(settle.OPTIN)
    home = optin.home_at(str(repo), optin.git_common_dir(str(repo)))
    found = settle.survey(str(repo), ref, home, every="--all-earlier" in args)
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
    git_out(repo, "branch", BASE)
    (repo / "seal" / "threads" / MOMENT / "gaps.md").write_text(
        OVERVIEW_CLOSED, encoding="utf-8"
    )
    git_out(repo, "add", "--", f"seal/threads/{MOMENT}")
    git_out(repo, "commit", "-qm", "close the row")


# --- the `gh` a case asks (#955, #1139) -------------------------------------
#
# `answer_of` is what `gh` answers. A case's `gh` gives it in process, to
# the run `lib/gitcmd.py#gh` starts, so `which`, the bound and the exit code
# are the runner's own and no process is started (#1581). One case,
# `test_local_mode_lists_a_released_and_an_unreleased_item`, asks a script
# first on PATH that answers the same, written once per module: a script run
# for the first time costs a security scan on macOS. The suite runs with
# `gh` logged out (`tests/conftest.py`), so no case reaches the real one.


def answer_of(answers, args):
    """`(exit code, stdout, stderr)` of `gh ARGS` answering ANSWERS: each
    branch's merged pull requests to `pr list --head`, the release pages to
    `api`, or, for any question, `raw` on stdout or `fail` at exit 4."""
    if "fail" in answers:
        return 4, "", answers["fail"] + "\n"
    if "raw" in answers:
        return 0, answers["raw"] + "\n", ""
    if args[:1] == ["api"]:
        return 0, answers.get("api", "[]") + "\n", ""
    branch = args[args.index("--head") + 1] if "--head" in args else ""
    return 0, json.dumps(answers.get("branches", {}).get(branch, [])) + "\n", ""


GH_HOME = "AGENTIC_SETTLE_GH_STUB_HOME"

GH_STUB = (
    "import json, os, sys\n\n"
    + inspect.getsource(answer_of)
    + f"""
HERE = os.environ[{GH_HOME!r}]
args = sys.argv[1:]
with open(os.path.join(HERE, "calls.jsonl"), "a", encoding="utf-8") as f:
    f.write(json.dumps(args) + "\\n")
with open(os.path.join(HERE, "answers.json"), encoding="utf-8") as f:
    code, out, err = answer_of(json.load(f), args)
sys.stdout.write(out)
sys.stderr.write(err)
sys.exit(code)
"""
)


class Gh:
    """`gh`'s answers, set by the case: given in process, or written to
    HOME for the script on PATH."""

    def __init__(self, home=None):
        self.home = home
        self.answers = {"branches": {}}
        self.asked = []
        self.write()

    def write(self):
        if self.home is not None:
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
        if self.home is None:
            return self.asked
        log = self.home / "calls.jsonl"
        if not log.exists():
            return []
        return [json.loads(x) for x in log.read_text(encoding="utf-8").splitlines()]


@pytest.fixture
def gh(monkeypatch):
    """A `gh` that each process run of a program named `gh` reaches in
    process, answering `answer_of` and logging what it was asked; every
    other run is real. `lib/gitcmd.py#gh` finds the suite's own `gh` on
    PATH (`tests/conftest.py`) and starts it through `subprocess.run`."""
    asked, real = Gh(), subprocess.run

    def run(argv, *args, **kwargs):
        if os.path.basename(argv[0]).split(".")[0] != "gh":
            return real(argv, *args, **kwargs)
        asked.asked.append(list(argv[1:]))
        code, out, err = answer_of(asked.answers, list(argv[1:]))
        return subprocess.CompletedProcess(argv, code, out, err)

    monkeypatch.setattr(subprocess, "run", run)
    return asked


@pytest.fixture(scope="module")
def _gh_stub(tmp_path_factory):
    """The directory holding the `gh` script, written once per module."""
    where = tmp_path_factory.mktemp("settle-gh")
    script = where / "gh_stub.py"
    script.write_text(GH_STUB, encoding="utf-8")
    if os.name == "nt":
        (where / "gh.cmd").write_text(
            f'@"{sys.executable}" "{script}" %*\r\n', encoding="utf-8"
        )
    else:
        stub = where / "gh"
        stub.write_text(
            f'#!/bin/sh\nexec "{sys.executable}" "{script}" "$@"\n', encoding="utf-8"
        )
        stub.chmod(0o755)
    return where


@pytest.fixture
def gh_on_path(tmp_path, monkeypatch, _gh_stub):
    """The script first on PATH, answering from and logging to this case's
    own directory."""
    home = tmp_path / "gh-stub"
    home.mkdir()
    monkeypatch.setenv(GH_HOME, str(home))
    monkeypatch.setenv("PATH", str(_gh_stub) + os.pathsep + os.environ["PATH"])
    return Gh(home)


# Why a local work item that names no branch is unreleased, as a person reads
# it: a file `lib/routing.py#parse` does not read names none, whatever rows
# it holds.
NO_BRANCH = (
    "no `routing.md` that `lib/routing.py` reads as a declaration names a "
    "branch, so `gh` was not asked"
)

ROUTED = """# {name} — routing

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Branch | {branch} |
"""


@pytest.fixture(scope="module")
def _local_world(tmp_path_factory):
    repo = tmp_path_factory.mktemp("settle-local") / "repo"
    (repo / "docs").mkdir(parents=True)
    (repo / "docs" / "a.md").write_text(DOC, encoding="utf-8")
    started(repo)
    (mark_root(repo / ".git" / "seal") / "threads").mkdir()
    return repo


@pytest.fixture
def local_repo(tmp_path, _local_world):
    """A repository whose `seal/` root is under its git directory, with
    `docs/a.md` committed on `main` and no work item yet."""
    return a_copy(_local_world, tmp_path)


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
    request from BRANCH merges, and return the merge commit. Both commits
    hold INTO's tree and are written by git's plumbing, so neither HEAD nor
    the working tree moves; BRANCH and INTO name them after."""
    tree = f"{into}^{{tree}}"
    work = git_out(repo, "commit-tree", tree, "-p", into, "-m", f"work of {branch}")
    merged = git_out(
        repo, "commit-tree", tree, "-p", into, "-p", work, "-m", f"merge {branch}"
    )
    git_out(repo, "update-ref", f"refs/heads/{branch}", work)
    git_out(repo, "update-ref", f"refs/heads/{into}", merged)
    return merged


# --- the published note `--apply` reads where the root is shared (#1139) ----


def fragment(repo, name, subject, tag=None, text=None):
    """A released work item whose `changelog.md`, holding TEXT or a line of
    its own, the commit SUBJECT adds on the current branch, tagged TAG where
    one is given; its directory."""
    if text is None:
        text = f"- what {name} changed\n"
    write(specs_dir(repo, name), "changelog.md", text)
    commit_everything(repo, subject)
    if tag is not None:
        git_out(repo, "tag", tag)
    return specs_dir(repo, name)


def release(tag, body="", draft=False):
    """One release as `gh api repos/{owner}/{repo}/releases` lists it."""
    return {"tag_name": tag, "draft": draft, "body": body}


# The one call `--apply` makes for the release list, as `gh` logs it.
RELEASES_CALL = ["api", "--paginate", "repos/{owner}/{repo}/releases?per_page=100"]
RELEASES_ASKED = "`gh api --paginate repos/{owner}/{repo}/releases?per_page=100`"


@pytest.fixture(scope="module")
def _noted_world(tmp_path_factory, _shared_world):
    repo = a_copy(_shared_world, tmp_path_factory.mktemp("settle-noted"))
    fragment(repo, "1700000001-a", "feat: a (#42)", tag="v1.2.3")
    return repo


@pytest.fixture
def noted(tmp_path, _noted_world):
    """`shared_repo` after `fragment` adds `1700000001-a`'s `changelog.md`
    in `feat: a (#42)`, tagged `v1.2.3`, copied, since `--apply` removes
    from it."""
    return a_copy(_noted_world, tmp_path)


class Test_tracked_text:
    def test_accepts_each_tracked_text_file_and_no_untracked_one(self, shared_repo):
        """The citations are read from what git tracks, so a file nobody
        committed is no reader and cites nothing."""
        (shared_repo / "notes.txt").write_text("untracked\n", encoding="utf-8")
        tracked = ("docs/a.md", "seal/README.md")
        assert dict(settle.tracked_text(str(shared_repo), "seal/threads")) == {
            rel: (shared_repo / rel).read_bytes().decode("utf-8") for rel in tracked
        }

    def test_refuses_a_file_under_the_work_items_and_a_binary_file(self, shared_repo):
        """Guards s4 of #1017: a work item's own files are what `--apply`
        removes, so none of them is read as a path citing into it, and a file
        holding a NUL byte is binary and skipped."""
        item(shared_repo, "1700000001-alpha", "- nothing\n  why: a reason.")
        (shared_repo / "b.bin").write_bytes(b"a\0b")
        commit_everything(shared_repo, "a work item and a binary file")
        assert [
            rel for rel, _ in settle.tracked_text(str(shared_repo), "seal/threads")
        ] == [
            "docs/a.md",
            "seal/README.md",
        ]


class Test_citations:
    def test_accepts_a_line_citing_a_work_item_twice_as_one_citation(self, drawn):
        """A `tests/` file that reads `seal/threads` is a reader, and its line
        citing a work item twice is one citation."""
        (drawn / "tests").mkdir()
        (drawn / "tests" / "test_reads.py").write_text(
            'SPECS = "seal/threads"\n'
            'A = "seal/threads/1700000001-alpha/frame/design.md seal/threads/1700000001-alpha/plan.md"\n',
            encoding="utf-8",
        )
        assert settle.citations(str(drawn), ["1700000001-alpha"], "seal/threads") == (
            {"1700000001-alpha": ["tests/test_reads.py:2"]},
            ["tests/test_reads.py"],
        )

    def test_refuses_a_tests_file_naming_specs_alone_as_a_reader(self, drawn):
        """Guards s5 of #1017: a `tests/` file naming a team's own `specs`
        reads nothing `--apply` removes, so it owes no answer before the
        directories go."""
        (drawn / "tests").mkdir()
        (drawn / "tests" / "test_team.py").write_text(
            'TEAM = "specs"\n', encoding="utf-8"
        )
        assert settle.citations(str(drawn), ["1700000001-alpha"], "seal/threads") == (
            {"1700000001-alpha": []},
            [],
        )


class Test_report:
    def test_accepts_a_spec_with_no_rule_changes_and_lists_it_to_read_whole(
        self, answered_tree
    ):
        """S4's dry run half: a spec with no section joins no group, so the
        settling session reads it whole; it is not left in place."""
        code, text = run(answered_tree)
        assert code == 0, text
        listed = text.split(settle.WHOLE_HEADING)[1].split("\n\n")[0] + "\n"
        for name in ("1700000001-alpha", "1700000002-beta", "1700000003-gamma"):
            where = f"seal/threads/{name}/frame/design.md"
            assert f"    {name}  {where}  {settle.NO_SECTION}\n" in listed, text
        assert "released at HEAD: 3 work items; 1 unreleased and untouched\n" in (
            text
        ), text

    def test_refuses_nothing_and_writes_and_removes_nothing(self, answered_tree):
        """The dry run holds nothing back: a section that does not parse and
        an open row are shown at exit 0, and the tree is left as it was."""
        (
            answered_tree
            / "seal"
            / "threads"
            / "1700000001-alpha"
            / "frame"
            / "design.md"
        ).write_text(
            spec("- rename\n  file: docs/one-root.md\n  to: x"), encoding="utf-8"
        )
        moment(answered_tree, overview=OVERVIEW_OPEN)
        before = sorted(
            str(p.relative_to(answered_tree))
            for p in answered_tree.rglob("*")
            if p.is_file()
        )
        code, text = run(answered_tree)
        after = sorted(
            str(p.relative_to(answered_tree))
            for p in answered_tree.rglob("*")
            if p.is_file()
        )
        assert before == after, "the report touched the tree"
        assert code == 0, text
        assert "refused" not in text and "kept" not in text, text
        assert "Nothing was written and nothing was removed" in text, text

    def test_lists_a_design_with_a_line_its_reader_did_not_read_to_read_whole(
        self, answered_tree
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
            (
                answered_tree / "seal" / "threads" / name / "frame" / "design.md"
            ).write_text(text, encoding="utf-8")
        code, text = run(answered_tree)
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

    def test_an_unreleased_work_item_is_not_a_candidate(self, answered_tree):
        """Released means present on the branch the release merges to, so this
        branch's own work item is outside the corpus entirely."""
        _, text = run(answered_tree)
        assert "1700000004-delta" not in text, text
        assert "1 unreleased and untouched" in text, text

    def test_a_released_work_item_whose_id_is_not_ascii_is_a_candidate(self, tree_copy):
        """#1283. `released` reads the ref's tree with `-z`, so a work item
        id that holds a character git quotes under the default
        `core.quotePath` is released where its directory stands. Seen red
        against the listing without `-z`, where the item read as unreleased."""
        name = "1700000006-정렬"
        moment(tree_copy, name=name, overview=OVERVIEW_CLOSED)
        code, text = run(tree_copy)
        assert code == 0, text
        assert "released at HEAD: 4 work items; 1 unreleased and untouched\n" in (
            text
        ), text
        stated = text.split("no `frame/design.md`, so no rule stated:\n")[1]
        assert stated.split("\n\n")[0] == f"    {name}", text

    def test_a_spec_less_directory_is_listed_as_stating_no_rule(self, answered_tree):
        """D3: a directory with no `frame/design.md` states no rule, so it is listed
        apart from the specs, and its record's rows with every other's."""
        moment(answered_tree, overview=OVERVIEW_CLOSED)
        code, text = run(answered_tree)
        assert code == 0, text
        stated = text.split("no `frame/design.md`, so no rule stated:\n")[1].split(
            "\n\n"
        )[0]
        assert stated == f"    {MOMENT}", text
        assert MOMENT not in text.split(settle.WHOLE_HEADING)[1].split("\n\n")[0]

    def test_every_open_row_is_listed_with_the_paths_it_names(self, tree_copy):
        """The open rows are a report the settling session decides from, so
        each carries the backticked paths it names and whether each is in the
        working tree, a bare file name found as a tracked file's name or in
        the work item's own directory."""
        row = (
            "the run of `docs/one-root.md` and `gone/away.py` at "
            "`tests/x.py::Test_y`, per `questions.md`, `one-root.md` and `cmd.exe`"
        )
        moment(tree_copy, overview=OVERVIEW_OPEN.replace("a claim nobody ran", row))
        (tree_copy / "seal" / "threads" / MOMENT / "questions.md").write_text(
            "# q\n", encoding="utf-8"
        )
        code, text = run(tree_copy)
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

    def test_the_report_lists_what_an_apply_would_remove(self, answered_tree):
        """D1's table: the command reports by itself the paths outside
        `seal/threads/` that cite into what `--apply` would remove, and the
        `tests/` files that read `seal/threads` — what #514's frame found by
        hand. A directory still holding a row is listed with when it goes."""
        no_rule(answered_tree, "1700000001-alpha")
        moment(answered_tree, overview=OVERVIEW_OPEN)
        (answered_tree / "docs" / "cites.md").write_text(
            "See `seal/threads/1700000001-alpha/frame/design.md` for the decision.\n"
            f"And `seal/threads/{MOMENT[:11]}…/routing.md` for the moment.\n"
            "A marker <!-- specs/1700000002-beta --> and a bare 1700000002-beta.\n",
            encoding="utf-8",
        )
        (answered_tree / "tests").mkdir()
        (answered_tree / "tests" / "test_reads.py").write_text(
            'SPECS = "seal/threads"\n', encoding="utf-8"
        )
        _, text = run(answered_tree)
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

    def test_names_a_gaps_md_away_from_its_place_as_not_read(self, answered_tree):
        """S1 of #1126, #956's R31: a released work item whose only `gaps.md`
        is `trail/gaps.md`, holding an open row. The settle reads the record
        at its place alone, so the row is not counted; the dry run names the
        file in a section of its own, which says who opens it and what
        `--apply` does with it, and refuses nothing. Seen red with the fix
        reverted in `settle.py`: the dry run named no file."""
        name = "1700000007-trail"
        released_item(answered_tree, name, {"trail/gaps.md": OVERVIEW_OPEN})
        code, text = run(answered_tree)
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

    def test_names_a_misplaced_design_and_plan_as_not_read(self, answered_tree):
        """S3 of #1126: the class is every file named like a record the settle
        reads, `gaps.md`, `frame/design.md` and `frame/plan.md`, at any other
        path of its directory, each named with the record it is named like.
        A record at its own place is not named. Seen red with the fix
        reverted in `settle.py`."""
        top = "1700000007-top-design"
        trail = "1700000008-trail-plan"
        released_item(answered_tree, top, {"design.md": "# a design\n"})
        released_item(
            answered_tree,
            trail,
            {"frame/plan.md": "# a plan\n", "trail/plan.md": "# a plan\n"},
        )
        code, text = run(answered_tree)
        assert f"seal/threads/{top}/design.md" in text, text
        assert code == 0, text
        section = text.split(f"\n{settle.MISPLACED_HEADING}\n")[1].split("\n\n")[0]
        assert section == (
            f"    {not_read(top, 'design.md', 'frame/design.md')}\n"
            f"    {not_read(trail, 'trail/plan.md', 'frame/plan.md')}"
        ), text

    def test_prints_no_section_where_nothing_is_misplaced(self, answered_tree):
        """S4 of #1126: every record at its place, so the section is not
        printed."""
        moment(answered_tree, overview=OVERVIEW_OPEN)
        code, text = run(answered_tree)
        assert code == 0, text
        assert settle.MISPLACED_HEADING not in text, text
        assert "named like" not in text, text

    def test_the_no_change_block_is_listed_with_no_section_to_write(self, drawn):
        """A spec whose section is the no-change block states that no rule
        changes, so it joins no group and is listed under the block."""
        item(drawn, "1700000001-a", "- nothing\n  why: a release entry.")
        code, text = at(drawn, "main")
        assert code == 0, text
        assert (
            "the no-change block (`- nothing`), so no section to write:\n"
            "    1700000001-a\n"
        ) in text, text
        assert "\ngroup 1\n" not in text, text

    def test_the_judgments_are_printed_by_the_document_each_stands_on(self, drawn):
        """#1167, *Scope* item 12: each released plan's *Judgments of the
        run*, read through `lib/tables.py#gfm_table`, grouped by the
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
            item(drawn, name, "- nothing\n  why: x.")
            table = "".join(f"| {' | '.join(row)} |\n" for row in rows)
            plan = (
                "# Implementation Plan: x\n\n## Phases\n\n"
                "| Phase | Delivers | Verified by | Status |\n|---|---|---|---|\n"
                "| 1 | a | b | c |\n\n## Judgments of the run\n\n"
                "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
                + table
            )
            (specs_dir(drawn, name) / "frame" / "plan.md").write_text(
                plan, encoding="utf-8"
            )
            lines[name] = [
                line_of(plan, f"| {' | '.join(row)} |") for row in rows if row[0]
            ]
            held = specs_dir(drawn, name) / "trail" / "rounds"
            held.mkdir(parents=True)
            for n in range(1, rounds + 1):
                (held / f"round-{n}.md").write_text("# round\n", encoding="utf-8")
        item(drawn, "1700000003-c", "- nothing\n  why: x.")
        (specs_dir(drawn, "1700000003-c") / "frame" / "plan.md").write_text(
            "# Implementation Plan: c\n\n## Phases\n", encoding="utf-8"
        )
        code, text = at(drawn, "main")
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
        self, drawn
    ):
        """The core's rule for a script: a section that holds no table under
        the exact header is named as not read, and the dry run still exits 0
        and prints the rest."""
        item(drawn, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(drawn, "1700000001-a") / "frame" / "plan.md").write_text(
            "# Implementation Plan: a\n\n## Judgments of the run\n\n"
            "| Date | Judgment | Grounds |\n|---|---|---|\n| 2026-10-01 | x | y |\n",
            encoding="utf-8",
        )
        code, text = at(drawn, "main")
        assert code == 0, text
        block = text.split(f"\n{settle.JUDGMENTS_HEADING}\n")[1]
        assert block.startswith(
            "    1700000001-a  seal/threads/1700000001-a/frame/plan.md  not read: "
            "holds no `| Date | Judgment | Grounds | Judged against |` table\n"
        ), block
        assert "judged against:" not in block, block
        assert settle.REMOVES_HEADING in text, text

    @pytest.mark.parametrize("shape", ["link", "unlistable"])
    def test_a_work_item_whose_rounds_cannot_be_listed_is_not_counted_as_none(
        self, drawn, monkeypatch, shape
    ):
        """Round 9, finding 1. A `trail/rounds` that is a link, or a
        directory nothing can list, holds a review git carries
        (`lib/routing.py#rounds_unreadable`), so the dry run says it
        counted none rather than that none happened. The unlistable
        directory is made by refusing `os.listdir` on that one path, since
        `chmod 000` does not bar a runner that is root."""
        item(drawn, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(drawn, "1700000001-a") / "frame" / "plan.md").write_text(
            "# Implementation Plan: a\n\n## Judgments of the run\n\n"
            "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
            "| 2026-10-01 | x | y | z |\n",
            encoding="utf-8",
        )
        trail = specs_dir(drawn, "1700000001-a") / "trail"
        trail.mkdir()
        if shape == "link":
            held = drawn / "elsewhere"
            held.mkdir()
            (held / "round-1.md").write_text("# Review round 1\n", encoding="utf-8")
            symlink_or_skip(held, trail / "rounds", directory=True)
        else:
            (trail / "rounds").mkdir()
            (trail / "rounds" / "round-1.md").write_text(
                "# Review round 1\n", encoding="utf-8"
            )
        if shape == "unlistable":
            barred = os.path.normcase(os.path.realpath(trail / "rounds"))
            listdir = os.listdir

            def refusing(path="."):
                if os.path.normcase(os.path.realpath(path)) == barred:
                    raise PermissionError(13, "Permission denied", str(path))
                return listdir(path)

            monkeypatch.setattr(os, "listdir", refusing)
        code, text = at(drawn, "main")
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
        self, drawn, heading
    ):
        """Round 9, finding 2. A heading whose letters, case folded, are the
        section's and that is not it is named at its line, and none of its
        rows is read: `--apply` removes the plan, so silence here loses the
        rows unread. Every live heading is the scope this reader scans."""
        item(drawn, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(drawn, "1700000001-a") / "frame" / "plan.md").write_text(
            f"# Implementation Plan: a\n\n{heading}\n\n"
            "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
            "| 2026-10-01 | x | y | z |\n",
            encoding="utf-8",
        )
        code, text = at(drawn, "main")
        assert code == 0, text
        block = text.split(f"\n{settle.JUDGMENTS_HEADING}\n")[1]
        assert block.startswith(
            "    1700000001-a  seal/threads/1700000001-a/frame/plan.md  not read: "
            f"line 3: `{heading}` opens like `## Judgments of the run` and is "
            "not it, so none of its rows were read\n"
        ), block
        assert "judged against:" not in block, block

    def test_accepts_a_near_heading_inside_a_fence_without_a_word(self, drawn):
        """The edge of finding 2's scope: a heading inside a fence is no
        heading, so the reader names nothing for it."""
        fence = "`" * 3
        item(drawn, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(drawn, "1700000001-a") / "frame" / "plan.md").write_text(
            f"# Implementation Plan: a\n\n{fence}\n## Judgments of the Run\n{fence}\n",
            encoding="utf-8",
        )
        code, text = at(drawn, "main")
        assert code == 0, text
        assert settle.JUDGMENTS_HEADING not in text, text

    def test_accepts_a_near_heading_inside_a_comment_without_a_word(self, drawn):
        """Round 10's edge of round 9's finding 2: a heading inside an HTML
        comment is no live heading (`lib/lines.py#live_lines`), so
        the reader names nothing for it."""
        item(drawn, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(drawn, "1700000001-a") / "frame" / "plan.md").write_text(
            "# Implementation Plan: a\n\n<!--\n## Judgments of the Run\n-->\n",
            encoding="utf-8",
        )
        code, text = at(drawn, "main")
        assert code == 0, text
        assert settle.JUDGMENTS_HEADING not in text, text

    def test_a_near_heading_is_named_beside_the_section_it_is_not(self, drawn):
        """A plan holding a near heading and the exact section gets the line
        for the first and the rows of the second: the naming runs before the
        reader looks for the exact section, and the near rows are not read."""
        item(drawn, "1700000001-a", "- nothing\n  why: x.")
        header = "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
        (specs_dir(drawn, "1700000001-a") / "frame" / "plan.md").write_text(
            "# Implementation Plan: a\n\n## Judgments Of The Run\n\n"
            + header
            + "| 2026-10-01 | near | y | z |\n\n## Judgments of the run\n\n"
            + header
            + "| 2026-10-02 | exact | y | z |\n",
            encoding="utf-8",
        )
        code, text = at(drawn, "main")
        assert code == 0, text
        block = text.split(f"\n{settle.JUDGMENTS_HEADING}\n")[1]
        assert block.startswith(
            "    1700000001-a  seal/threads/1700000001-a/frame/plan.md  not read: "
            "line 3: `## Judgments Of The Run` opens like `## Judgments of the "
            "run` and is not it, so none of its rows were read\n"
        ), block
        assert "2026-10-02  exact\n" in block, block
        assert "2026-10-01  near" not in block, block

    def test_a_deleted_plan_whose_directory_stands_is_not_an_earlier_one(
        self, shared_repo, monkeypatch
    ):
        """#1281, design S3. A plan deleted from a work item whose directory
        stands in the working tree is no earlier settle's removal, so it is
        not read and the section is not printed. Seen red with the exclusion
        of `work_items(records)` alone removed."""
        name = "1700000001-a"
        held = f"seal/threads/{name}"
        plan = judgments_plan([("2026-10-01", "x", "y", "z")])
        committed(
            shared_repo,
            (
                f"released {name}",
                {
                    f"{held}/routing.md": "# a — routing\n",
                    f"{held}/frame/plan.md": plan,
                },
                None,
            ),
            ("a drops its plan (#7)", {f"{held}/frame/plan.md": None}, None),
        )
        answered(monkeypatch, shared_repo, real={"earlier_judgments"})
        code, text = at(shared_repo, "main")
        assert code == 0, text
        assert settle.EARLIER_HEADING not in text, text

    def test_a_plan_is_read_once_at_its_newest_deletion(self, shared_repo, monkeypatch):
        """#1281, design *Scope* item 1. A plan deleted, added again and
        deleted again is read once, at the newest deletion's parent, and
        the work items of one cell come in the order of their removing
        commits, newest first, whatever their ids' order. Seen red with the
        once-only check removed, and with the deletions taken oldest first."""
        old, older = "1700000001-old", "seal/threads/1700000000-older"
        held = f"seal/threads/{old}"
        ids = committed(
            shared_repo,
            (
                "the older work item (#1)",
                {
                    f"{older}/frame/plan.md": judgments_plan(
                        [("2026-09-01", "older", "y", "z")]
                    )
                },
                None,
            ),
            ("settle 0.0.1 (#2)", {older: None}, None),
            (
                "the old work item (#3)",
                {
                    f"{held}/frame/plan.md": judgments_plan(
                        [("2026-10-01", "first", "y", "z")]
                    )
                },
                None,
            ),
            ("drop it (#5)", {held: None}, None),
            (
                "the old work item again (#6)",
                {
                    f"{held}/frame/plan.md": judgments_plan(
                        [("2026-10-02", "second", "y", "z")]
                    )
                },
                None,
            ),
            ("settle 0.1.0 (#7)", {held: None}, None),
        )
        short = ids["settle 0.1.0 (#7)"][1]
        standing(shared_repo, "1700000002-new")
        answered(monkeypatch, shared_repo, real={"earlier_judgments"})
        code, text = at(shared_repo, "main")
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

    def test_a_removed_plan_of_a_non_ascii_id_is_read(self, shared_repo, monkeypatch):
        """#1281, round 1, finding 1. A work item id may hold any character
        the slug takes, and git quotes such a path under the default
        `core.quotePath` unless `-z` is given, so the history is read with
        `-z`. Seen red against the reading without it."""
        old = "1700000001-정렬"
        plan = judgments_plan([("2026-10-01", "ended the rounds", "y", "z")])
        committed(
            shared_repo,
            (
                "the old work item (#3)",
                {f"seal/threads/{old}/frame/plan.md": plan},
                None,
            ),
            ("settle 0.1.0 (#7)", {f"seal/threads/{old}": None}, None),
        )
        standing(shared_repo, "1700000002-new")
        answered(monkeypatch, shared_repo, real={"earlier_judgments"})
        code, text = at(shared_repo, "main")
        assert code == 0, text
        assert f"\n    {old}  " in text, text

    def test_a_plan_deleted_where_another_is_added_is_still_read(
        self, shared_repo, monkeypatch
    ):
        """#1281, round 1, finding 2, design *Scope* item 1. One commit
        deletes a work item's plan and adds another's from the same text, so
        git's rename detection would pair the two and list no deletion. Seen
        red with `--no-renames` alone removed from `earlier_judgments`."""
        git_out(shared_repo, "config", "diff.renames", "true")
        old, new = "1700000001-old", "1700000002-new"
        plan = judgments_plan([("2026-10-01", "ended the rounds", "y", "z")])
        committed(
            shared_repo,
            (
                "the old work item (#3)",
                {f"seal/threads/{old}/frame/plan.md": plan},
                None,
            ),
            (
                "settle 0.1.0 and frame the new one (#7)",
                {
                    f"seal/threads/{old}": None,
                    f"seal/threads/{new}/frame/plan.md": plan,
                },
                None,
            ),
        )
        answered(monkeypatch, shared_repo, real={"earlier_judgments"})
        code, text = at(shared_repo, "main")
        assert code == 0, text
        assert f"\n    {old}  " in text, text

    def test_a_plan_added_where_another_is_deleted_names_its_release(
        self, shared_repo, monkeypatch
    ):
        """#1481, design *Scope* item 4. The adding commits are read in one
        `git log` over `seal/threads`, so a commit that deletes one plan and
        adds another from the same text is read as the add it is, and the
        second plan's line names the release that holds it. Seen red with
        `--no-renames` alone removed from `adding_commits`."""
        git_out(shared_repo, "config", "diff.renames", "true")
        old, new = "1700000001-old", "1700000002-new"
        plan = judgments_plan([("2026-10-01", "ended the rounds", "y", "z")])
        committed(
            shared_repo,
            (
                "the old work item (#3)",
                {f"seal/threads/{old}/frame/plan.md": plan},
                None,
            ),
            (
                "settle 0.1.0 and frame the new one (#7)",
                {
                    f"seal/threads/{old}": None,
                    f"seal/threads/{new}/frame/plan.md": plan,
                },
                "v0.2.0",
            ),
            ("settle 0.2.0 (#9)", {f"seal/threads/{new}": None}, None),
        )
        standing(shared_repo, "1700000003-next")
        answered(monkeypatch, shared_repo, real={"earlier_judgments"})
        code, text = at(shared_repo, "main")
        assert code == 0, text
        assert f"\n    {new}  released in v0.2.0; removed by " in text, text

    @pytest.mark.parametrize("added_by", ["an untagged commit", "no commit"])
    def test_names_a_plan_no_tag_holds_and_a_removal_no_number_names(
        self, shared_repo, monkeypatch, added_by
    ):
        """#1281, design S4. Where no `vX.Y.Z` tag holds the commit that
        added the plan, the work item's line names that commit, and a
        removing commit whose subject ends in no `(#N)` is named alone.
        Where no commit on the ref adds the plan, as for one only a merge's
        own resolution added, the line says so."""
        old = "1700000001-old"
        adding, short = removed_plan(
            shared_repo,
            old,
            judgments_plan([("2026-10-01", "x", "y", "z")]),
            "the old work item",
            "drop the old work item",
        )
        released = (
            "no `vX.Y.Z` tag holds "
            + git_out(shared_repo, "rev-parse", "--short", adding)
            + ", the commit that added its plan"
        )
        if added_by == "no commit":
            monkeypatch.setattr(settle, "adding_commits", lambda *_: {})
            released = "no commit on main adds its plan"
        standing(shared_repo, "1700000002-new")
        answered(monkeypatch, shared_repo, real={"earlier_judgments"})
        code, text = at(shared_repo, "main")
        assert code == 0, text
        assert f"\n    {old}  {released}; removed by {short}\n" in text, text

    def test_names_a_near_heading_in_a_removed_plan_and_reads_none_of_its_rows(
        self, shared_repo, monkeypatch
    ):
        """#1281, design S5. A removed plan is read by the reader the
        released plans are read by, so a near heading is named at its
        coordinate in the history, none of its rows is printed, and the dry
        run exits 0. Seen red with the reader's near-heading branch alone
        removed."""
        old = "1700000001-old"
        _, short = removed_plan(
            shared_repo,
            old,
            judgments_plan(
                [("2026-10-01", "x", "y", "z")], heading="## Judgments Of The Run"
            ),
            "the old work item (#3)",
            "settle 0.1.0 (#7)",
            "v0.1.0",
        )
        standing(shared_repo, "1700000002-new")
        answered(monkeypatch, shared_repo, real={"earlier_judgments"})
        code, text = at(shared_repo, "main")
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

    @pytest.mark.parametrize(
        "failing",
        [
            pytest.param(("log", "--diff-filter=D"), id="the deletions"),
            pytest.param(("cat-file", "--batch"), id="the texts"),
            pytest.param(("log", "--diff-filter=A"), id="the adding commits"),
            pytest.param(("for-each-ref", "refs/tags/v*"), id="the tags"),
            pytest.param(
                ("cat-file", "--batch-check=%(objecttype) %(objectname)"),
                id="the tags' peel",
            ),
            pytest.param(("rev-list", "--stdin"), id="the tag history"),
        ],
    )
    def test_a_git_that_cannot_read_an_earlier_plan_is_named_and_refuses_nothing(
        self, one_removal, monkeypatch, failing
    ):
        """#1281, design *Scope* item 4, and #1481, design *Scope* item 6.
        Each of the six calls the section reads through, the deletions'
        `git log`, the plans' `git cat-file --batch`, the adding commits'
        `git log`, and the tags' `for-each-ref`, `cat-file --batch-check`
        and `rev-list`, that fails
        is named once with what git said, no row is printed, and the dry run
        exits 0."""
        real = settle.git_run
        subcommand, marker = failing

        def git_run(root, *args, given=None):
            if args[0] == subcommand and marker in args:
                raise RuntimeError("git said no")
            return real(root, *args, given=given)

        monkeypatch.setattr(settle, "git_run", git_run)
        code, text = at(one_removal, "main")
        assert code == 0, text
        assert settle.EARLIER_HEADING in text, text
        block = text.split(f"\n{settle.EARLIER_HEADING}\n")[1].split(
            f"\n\n{settle.REMOVES_HEADING}"
        )[0]
        assert block == "    not read: git said no", block

    def test_the_git_calls_do_not_grow_with_the_plans_read(self, removals, monkeypatch):
        """#1481, design S4. The dry run over a history that removed one
        plan makes as many git calls as over one that removed three, each
        in its own commit, because the plans' texts, their adding commits
        and their tags are each read in one batched call. The ref after the
        first removal is the history that removed one. Seen red against
        the per-plan `git show`, `git log` and `git tag --contains`."""
        repo, _ = removals
        one = calls(monkeypatch, lambda: at(repo, "v0.2.0~1"))
        assert calls(monkeypatch, lambda: at(repo, "main")) == one

    def test_a_plan_git_holds_no_text_for_is_named_and_none_of_its_rows_printed(
        self, shared_repo, monkeypatch
    ):
        """#1481, design S6. Where `git cat-file --batch` answers `missing`
        for a removed plan, as it does where the plan's blob is gone from
        the object store, the plan is named as not read at its coordinate
        with what git answered, none of its rows is printed, the other
        plans' rows are, and the dry run exits 0. Seen red with the branch
        that names a plan the batch gave no text for alone removed."""
        old, kept = "1700000001-old", "1700000002-kept"
        adding, short = removed_plan(
            shared_repo,
            old,
            judgments_plan([("2026-10-01", "gone", "y", "z")]),
            "the old work item (#3)",
            "settle 0.1.0 (#7)",
            "v0.1.0",
        )
        removed_plan(
            shared_repo,
            kept,
            judgments_plan([("2026-10-02", "kept", "y", "z")]),
            "the kept work item (#8)",
            "settle 0.2.0 (#9)",
            "v0.2.0",
        )
        blob = git_out(
            shared_repo, "rev-parse", f"{adding}:seal/threads/{old}/frame/plan.md"
        )
        loose = shared_repo / ".git" / "objects" / blob[:2] / blob[2:]
        # Git writes a loose object read-only, and Windows refuses to unlink
        # a read-only file.
        os.chmod(loose, 0o644)
        loose.unlink()
        standing(shared_repo, "1700000003-new")
        answered(monkeypatch, shared_repo, real={"earlier_judgments"})
        code, text = at(shared_repo, "main")
        assert code == 0, text
        block = text.split(f"\n{settle.EARLIER_HEADING}\n")[1].split(
            f"\n\n{settle.REMOVES_HEADING}"
        )[0]
        assert (
            f"    {old}  {short}^:seal/threads/{old}/frame/plan.md  not read: "
            "`git cat-file --batch` answered `missing`, so none of its rows "
            "were read"
        ) in block, block
        assert "  2026-10-01  gone\n" not in block, block
        assert "  2026-10-02  kept\n" in block, block

    @pytest.mark.parametrize("beside", [True, False], ids=["beside", "alone"])
    def test_a_removed_plan_whose_path_holds_a_newline_is_named_and_the_rest_read(
        self, shared_repo, monkeypatch, beside
    ):
        """#1481, round 1, finding 2. `git cat-file --batch` reads one name
        per line, so a removed plan whose work item id holds a newline is
        named as not read at its coordinate and never asked for, and the
        plan removed beside it is read with its own text and its rows
        printed. Seen red against the batch asked for both, where the plain
        plan was named with the other path's answer; alone, seen red with
        the line naming it dropped where no other plan is left to ask for."""
        odd, plain = "1700000001-odd\nname", "1700000002-plain"
        plans = ((odd, "odd"), (plain, "plain")) if beside else ((odd, "odd"),)
        for name, judged in plans:
            plan = judgments_plan([("2026-10-01", judged, "y", "z")])
            blob = subprocess.run(
                ["git", "-C", str(shared_repo), "hash-object", "-w", "--stdin"],
                input=plan,
                check=True,
                capture_output=True,
                encoding="utf-8",
            ).stdout.strip()
            path = f"seal/threads/{name}/frame/plan.md"
            added = subprocess.run(
                [
                    "git",
                    "-C",
                    str(shared_repo),
                    "update-index",
                    "--add",
                    "--cacheinfo",
                    f"100644,{blob},{path}",
                ],
                capture_output=True,
                encoding="utf-8",
            )
            # Asked by attempting the add: Git for Windows refuses a path
            # holding a newline in the index, so no commit made with it can
            # hold the defect this case is about. The plain path is held to
            # the add like any fixture.
            if added.returncode != 0 and name == odd:
                pytest.skip(
                    "this git refuses a path holding a newline in the index, so "
                    f"no commit here can hold one: {added.stderr.strip()}"
                )
            assert added.returncode == 0, added.stderr
        git_out(shared_repo, "commit", "-qm", "the two work items (#3)")
        git_out(shared_repo, "rm", "-r", "-q", "--cached", "--", "seal/threads")
        git_out(shared_repo, "commit", "-qm", "settle 0.1.0 (#7)")
        short = git_out(shared_repo, "rev-parse", "--short", "HEAD")
        standing(shared_repo, "1700000009-new")
        answered(monkeypatch, shared_repo, real={"earlier_judgments"})
        code, text = at(shared_repo, "main")
        assert code == 0, text
        block = earlier_block(text)
        assert (
            f"    {odd}  {short}^:seal/threads/{odd}/frame/plan.md  not read: "
            "its path holds a newline, which `git cat-file --batch` reads as "
            "two names, so none of its rows were read"
        ) in block, block
        assert ("  2026-10-01  plain\n" in block) is beside, block
        assert "  2026-10-01  odd\n" not in block, block

    def test_reads_the_plans_of_the_two_newest_removing_commits_and_names_the_rest(
        self, removals
    ):
        """#1481, design S1. Of three commits that each removed one plan,
        the dry run prints the rows of the two newest commits' plans, none
        of the oldest's, and ends the section with the line counting the
        one older removing commit it did not read and naming
        `seal settle --all-earlier`. Seen red with the bound alone
        removed."""
        shared_repo, (newest, middle, _oldest) = removals
        code, text = at(shared_repo, "main")
        assert code == 0, text
        assert earlier_block(text) == (
            "\njudged against: z\n"
            + newest
            + middle
            + "\n1 older commit removed plans this section did not read; "
            "`seal settle --all-earlier` reads them"
        ), earlier_block(text)

    def test_a_removing_commit_that_deleted_two_plans_is_one_commit_of_the_window(
        self, shared_repo, monkeypatch
    ):
        """#1481, design *Scope* items 1 and 2. The window and the line
        count commits, never plans: a commit that deleted two plans is one
        removing commit, so both its plans are read beside the newest
        commit's, and the one oldest commit is counted once. Seen red with
        the removing commits listed once per plan."""
        plans = {
            name: {
                f"seal/threads/{name}/frame/plan.md": judgments_plan(
                    [("2026-10-0" + name[9], judged, "y", "z")]
                )
            }
            for name, judged in (
                ("1700000001-oldest", "oldest"),
                ("1700000002-a", "1700000002-a"),
                ("1700000003-b", "1700000003-b"),
                ("1700000004-newest", "newest"),
            )
        }
        committed(
            shared_repo,
            ("the oldest work item (#1)", plans["1700000001-oldest"], None),
            ("settle 0.1.0 (#11)", {"seal/threads/1700000001-oldest": None}, None),
            (
                "the two work items (#2)",
                {**plans["1700000002-a"], **plans["1700000003-b"]},
                None,
            ),
            ("settle 0.2.0 (#12)", {"seal/threads": None}, None),
            ("the newest work item (#4)", plans["1700000004-newest"], None),
            ("settle 0.3.0 (#14)", {"seal/threads/1700000004-newest": None}, None),
        )
        standing(shared_repo, "1700000009-new")
        answered(monkeypatch, shared_repo, real={"earlier_judgments"})
        code, text = at(shared_repo, "main")
        assert code == 0, text
        block = earlier_block(text)
        for judged in ("newest", "1700000002-a", "1700000003-b"):
            assert f"  {judged}\n" in block, block
        assert "  oldest\n" not in block, block
        assert block.endswith(
            "\n\n1 older commit removed plans this section did not read; "
            "`seal settle --all-earlier` reads them"
        ), block

    def test_prints_the_section_where_it_holds_only_the_line_of_older_commits(
        self, shared_repo, monkeypatch
    ):
        """#1481, design *Scope* item 2. Where the plans the window reads
        hold no row, the section is still printed, holding only the line
        that counts the older removing commits, so the settling session
        learns that rows stand past the window. Seen red with that line
        alone left out of what prints the section."""
        old, bare = "seal/threads/1700000001-old", "seal/threads/170000000{}-bare"
        committed(
            shared_repo,
            (
                "the old work item (#1)",
                {
                    f"{old}/frame/plan.md": judgments_plan(
                        [("2026-10-01", "old", "y", "z")]
                    )
                },
                None,
            ),
            ("settle 0.1.0 (#11)", {old: None}, None),
            *(
                commit
                for n in (2, 3)
                for commit in (
                    (
                        f"the bare work item {n} (#{n})",
                        {
                            f"{bare.format(n)}/frame/plan.md": "# Implementation Plan: x\n"
                        },
                        None,
                    ),
                    (f"settle 0.{n}.0 (#{n + 10})", {bare.format(n): None}, None),
                )
            ),
        )
        standing(shared_repo, "1700000009-new")
        answered(monkeypatch, shared_repo, real={"earlier_judgments"})
        code, text = at(shared_repo, "main")
        assert code == 0, text
        assert earlier_block(text) == (
            "\n1 older commit removed plans this section did not read; "
            "`seal settle --all-earlier` reads them"
        ), text

    def test_a_batched_read_that_fails_keeps_the_line_of_older_commits(
        self, removals, monkeypatch
    ):
        """#1481, design *Scope* items 2 and 6. The deletions' `git log`
        counted the removing commits before the plans' texts were asked, so
        where `git cat-file --batch` fails, the section names the failure,
        prints no row, and still counts the older removing commit. Seen red
        with the failure branch returning no count."""
        shared_repo, _ = removals
        real = settle.git_run

        def git_run(root, *args, given=None):
            if args[0] == "cat-file":
                raise RuntimeError("git said no")
            return real(root, *args, given=given)

        monkeypatch.setattr(settle, "git_run", git_run)
        code, text = at(shared_repo, "main")
        assert code == 0, text
        assert earlier_block(text) == (
            "    not read: git said no\n\n1 older commit removed plans this "
            "section did not read; `seal settle --all-earlier` reads them"
        ), earlier_block(text)

    def test_a_spec_no_commit_adds_is_marked_unordered(self, drawn, monkeypatch):
        """Where the history cannot place a spec, it has no place in the order,
        and the group says so rather than listing it as ordered."""
        item(drawn, "1700000001-a", op("add", "U", new="Rule."))
        item(drawn, "1700000002-b", op("add", "U", new="B."))
        monkeypatch.setattr(
            settle.sibling.load(settle.RULES),
            "order",
            lambda r, f, ids, s: [(i, None) for i in ids],
        )
        code, text = at(drawn, "main")
        assert code == 0, text
        said = settle.UNORDERED.format(a="1700000001-a", b="1700000002-b")
        assert said in group_text(text), text

    def test_a_run_without_from_prints_no_named_directory_listing(self, drawn):
        """#1054 A1: the listing is printed only where a person named a
        directory, so a run without `--from` prints what it printed before;
        the cases above hold that output line for line."""
        write(drawn, "adr/0001.md", "a decision\n")
        item(drawn, "1700000001-a", op("add", "U", new="Rule."))
        code, text = at(drawn, "main")
        assert code == 0, text
        assert settle.DOCUMENTS_HEADING not in text, text
        assert "adr/0001.md" not in text, text

    @pytest.mark.parametrize("section", ["S", "S child"])
    def test_two_specs_on_parallel_branches_at_one_place_are_one_group_unordered(
        self, shared_repo, monkeypatch, section
    ):
        """S5: ancestry cannot order them, so they are one group with the
        pair marked for the settling session to order by content, and nothing
        is refused. A sub-section is inside its section's range, so it is the
        same place. The two designs are added on branches `main` merged
        apart, which `merged_history` writes, and `rule_changes.py#order`
        and `#_ancestor` read them from git: the case that holds
        `_ancestor`'s answer of neither way. The other readers are
        `answered`."""
        a, b = (
            f"seal/threads/{name}/frame/design.md"
            for name in ("1700000001-a", "1700000002-b")
        )
        merged_history(
            shared_repo,
            ("base", {}),
            ("b", {b: spec(op("add", section, new="Rule."))}),
            ("a", {a: spec(op("change", "S", "old sentence.", "y."))}),
            ("merge b", {b: spec(op("add", section, new="Rule."))}),
        )
        answered(monkeypatch, shared_repo, real={"order", "_ancestor"})
        code, text = at(shared_repo, "main")
        assert code == 0, text
        assert "refused" not in text, text
        group = group_text(text)
        assert "1700000001-a" in group and "1700000002-b" in group, text
        said = settle.UNORDERED.format(a="1700000001-a", b="1700000002-b")
        assert f"    {said}" in group, text
        assert "\ngroup 2\n" not in text, text

    def test_two_local_merges_no_ancestry_orders_are_marked_unordered(
        self, local_repo, monkeypatch
    ):
        """S2 of #955, two lines of history: each pull request merged into a
        branch of its own, and `main` merged both, so no ancestry orders the
        two merge commits and the pair is marked. The readers are
        `answered`, and `rule_changes.py#_ancestor` answers neither way, as
        git answers for two commits on branches merged apart
        (`test_two_specs_on_parallel_branches_at_one_place_are_one_group_unordered`)."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        local_item(local_repo, "1700000002-b", "feat/2-b", op("add", "S", new="B."))
        answered(monkeypatch, local_repo)
        rule_changes = settle.sibling.load(settle.RULES)
        monkeypatch.setattr(rule_changes, "_ancestor", lambda root, a, b: False)
        code, text = at(local_repo, "main")
        assert code == 0, text
        said = settle.UNORDERED_LOCAL.format(a="1700000001-a", b="1700000002-b")
        assert f"    {said}" in group_text(text), text


def records_in_place(tmp_path, name):
    """A work item directory under TMP_PATH holding the three records the
    settle reads, each at its place."""
    top = tmp_path / "seal" / "threads" / name
    for rel in ("gaps.md", "frame/design.md", "frame/plan.md"):
        write(top, rel, "# x\n")
    return top


class Test_misplaced:
    def test_accepts_a_file_or_a_link_to_one_at_another_path(self, tmp_path):
        """*Scope* item 1 of #1126: a file named like a record, at any path
        but the record's own, is named with the record, as a regular file or
        as a link to one, and the records at their places are not. Seen red
        with the place test removed."""
        top = records_in_place(tmp_path, "1700000001-a")
        (top / "x").mkdir()
        (top / "x" / "design.md").write_text("# x\n", encoding="utf-8")
        (top / "trail").mkdir()
        symlink_or_skip(top / "gaps.md", top / "trail" / "gaps.md")
        assert settle.misplaced(str(tmp_path), "1700000001-a", "seal/threads") == [
            ("trail/gaps.md", "gaps.md"),
            ("x/design.md", "frame/design.md"),
        ]

    def test_refuses_a_directory_a_link_to_nothing_and_another_spelling(self, tmp_path):
        """*Scope* item 1 of #1126: only the exact name of a file is read. A
        directory of that name, a link to nothing, another spelling and a
        longer name are not named, and a linked directory is not followed.
        Seen red with the walk following links, and with the file test
        removed."""
        top = records_in_place(tmp_path, "1700000001-a")
        (top / "notes").mkdir()
        (top / "notes" / "Gaps.md").write_text("# x\n", encoding="utf-8")
        (top / "notes" / "gaps.md.bak").write_text("# x\n", encoding="utf-8")
        (top / "trail" / "plan.md").mkdir(parents=True)
        elsewhere = tmp_path / "elsewhere"
        elsewhere.mkdir()
        (elsewhere / "gaps.md").write_text("# x\n", encoding="utf-8")
        symlink_or_skip(elsewhere, top / "linked", directory=True)
        symlink_or_skip(tmp_path / "nowhere", top / "notes" / "plan.md")
        assert settle.misplaced(str(tmp_path), "1700000001-a", "seal/threads") == []


class Test_apply:
    def test_accepts_every_released_directory_with_no_open_row(self, answered_tree):
        """S4's apply half: a spec holding the no-change block and specs with
        no `## Rule changes` leave alike, and the unreleased one stays."""
        no_rule(answered_tree, "1700000001-alpha")
        code, text = run(answered_tree, "--apply")
        assert code == 0, text
        for name in ("1700000001-alpha", "1700000002-beta", "1700000003-gamma"):
            assert not (answered_tree / "seal" / "threads" / name).exists(), text
            assert f"removed seal/threads/{name}/\n" in text, text
        assert (answered_tree / "seal" / "threads" / "1700000004-delta").exists(), text
        assert text.endswith(
            "\nremoved 3 directories; kept 0 with a row to close and 0 whose note "
            "lacks its entry\n"
        )

    def test_apply_leaves_a_team_specs_of_the_same_name_on_disk(self, answered_tree):
        """#688 D3. A project's own `specs/` is read as history and never taken,
        even where a team directory carries the removed work item's very id: the
        removal is `seal/threads/` whatever else the tree holds (`threads`)."""
        team = answered_tree / "specs" / "1700000001-alpha"
        team.mkdir(parents=True)
        (team / "design.md").write_text("# the team's design\n", encoding="utf-8")
        (team / "spec.md").write_text("# the team's spec\n", encoding="utf-8")
        no_rule(answered_tree, "1700000001-alpha")
        code, text = run(answered_tree, "--apply")
        assert code == 0, text
        assert not (answered_tree / "seal" / "threads" / "1700000001-alpha").exists()
        assert (team / "design.md").read_text(
            encoding="utf-8"
        ) == "# the team's design\n"
        assert (team / "spec.md").is_file()

    def test_a_removed_record_prints_each_row_it_closed_and_writes_no_document(
        self, answered_tree
    ):
        """What closed each row is copied into the settle's pull request body,
        so `--apply` prints it; the policy root is the settling session's."""
        moment(answered_tree, overview=OVERVIEW_CLOSED)
        before = docs_text(answered_tree)
        code, text = run(answered_tree, "--apply")
        assert code == 0, text
        assert not (answered_tree / "seal" / "threads" / MOMENT).exists(), text
        assert docs_text(answered_tree) == before, "the apply wrote into docs/"
        assert (
            f"removed seal/threads/{MOMENT}/\n"
            "    no note read: HEAD holds no `changelog.md` in its directory\n"
            "    closed in gaps.md: a claim\n"
            "        what closed it: run on 2026-01-01\n"
        ) in text, text

    def test_an_open_row_keeps_its_directory_and_a_closure_on_disk_lets_it_go(
        self, drawn
    ):
        """S3: the open row keeps the directory, named, at exit 1; closed in
        the working tree and not committed, the next `--apply` removes it,
        prints the row with what closed it, and exits 0. Nothing waits for
        the closure to reach a base."""
        item(drawn, "1700000001-a", op("add", "S", new="Rule."))
        overview = specs_dir(drawn, "1700000001-a") / "gaps.md"
        overview.write_text(OPEN, encoding="utf-8")
        code, text = at(drawn, "main", "--apply")
        assert code == 1, text
        assert specs_dir(drawn, "1700000001-a").exists(), text
        assert (
            "kept seal/threads/1700000001-a/: its record holds 1 open row; close "
            "each (`closed` with what closed it) and run `seal settle --apply` again\n"
            "    open in gaps.md: a claim nobody ran\n"
        ) in text, text
        overview.write_text(OVERVIEW_CLOSED, encoding="utf-8")
        code, text = at(drawn, "main", "--apply")
        assert code == 0, text
        assert not specs_dir(drawn, "1700000001-a").exists(), text
        assert "    closed in gaps.md: a claim\n" in text, text
        assert (drawn / "docs" / "a.md").read_text(encoding="utf-8") == DOC

    def test_a_closure_the_released_ref_has_not_seen_lets_the_directory_go(
        self, tree_copy
    ):
        """S3 at a base: the row is closed on the working branch and open at
        `--released-at`. The working tree is the fact `--apply` reads, so the
        directory goes (#602's base condition is gone)."""
        closed_after_base(tree_copy)
        code, text = at(tree_copy, BASE, "--apply")
        assert code == 0, text
        assert not (tree_copy / "seal" / "threads" / MOMENT).exists(), text
        assert f"removed seal/threads/{MOMENT}/\n" in text, text

    def test_refuses_an_unreadable_memo_and_keeps_its_directory(self, answered_tree):
        """A section this cannot read is a count it does not know, never zero."""
        moment(answered_tree, overview="# x — overview\n\n## Not checked\n")
        code, text = run(answered_tree, "--apply")
        assert code == 1, text
        assert (answered_tree / "seal" / "threads" / MOMENT).exists(), text
        assert "cannot be read" in text, text

    def test_an_unreleased_spec_less_directory_is_not_a_candidate(
        self, answered_tree, monkeypatch
    ):
        item = answered_tree / "seal" / "threads" / MOMENT
        item.mkdir()
        (item / "routing.md").write_text("# routing\n", encoding="utf-8")
        answered(monkeypatch, answered_tree, unreleased={"1700000004-delta", MOMENT})
        _, text = run(answered_tree, "--apply")
        assert item.exists(), text

    def test_removes_a_directory_whose_gaps_md_is_away_and_names_it(
        self, answered_tree
    ):
        """S1 of #1126, `--apply`: the directory goes on its record at its
        place, which it does not have, and the `removed` line is followed by
        a `not read:` line naming `trail/gaps.md`; the exit code and the last
        line's counts are as before. Seen red with the fix reverted in
        `settle.py`: the directory went without a word."""
        name = "1700000007-trail"
        path = released_item(answered_tree, name, {"trail/gaps.md": OVERVIEW_OPEN})
        code, text = run(answered_tree, "--apply")
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

    def test_keeps_on_the_record_at_its_place_and_names_the_copy(self, answered_tree):
        """S2 of #1126: a top-level `gaps.md` holding an open row and a
        `frame/gaps.md` holding none. The directory is kept on the top-level
        row, at exit 1, and the `kept` line's rows are followed by a `not
        read:` line naming the copy; the dry run's section follows its open
        rows. Seen red with the fix reverted in `settle.py`."""
        name = "1700000007-copy"
        path = released_item(
            answered_tree,
            name,
            {"gaps.md": OVERVIEW_OPEN, "frame/gaps.md": OVERVIEW_CLOSED},
        )
        _, report = run(answered_tree)
        assert f"seal/threads/{name}/frame/gaps.md" in report, report
        rows = report.index(f"\n{settle.ROWS_HEADING}\n")
        assert rows < report.index(f"\n{settle.MISPLACED_HEADING}\n"), report
        code, text = run(answered_tree, "--apply")
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

    def test_a_stale_from_is_listed_and_neither_refused_nor_waited_on(self, drawn):
        """S2: an operation whose `from` matches nothing, and one whose
        heading is not there, are history in their groups; a later spec at
        the same place is listed after them, and the directories go."""
        item(drawn, "1700000001-a", op("change", "S", "not there.", "y."))
        item(drawn, "1700000002-c", op("remove", "Nowhere"))
        item(drawn, "1700000003-b", op("add", "S", new="Rule."))
        code, text = at(drawn, "main")
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
        code, text = at(drawn, "main", "--apply")
        assert code == 0, text
        for name in ("1700000001-a", "1700000002-c", "1700000003-b"):
            assert not specs_dir(drawn, name).exists(), text

    def test_a_spec_that_joins_no_group_is_read_whole_and_goes(self, drawn):
        """S4: a section that does not parse is listed to read whole with the
        reader's reason at its line, beside a spec with no section, and with
        no open row both leave."""
        bad = "- rename\n  file: docs/a.md\n  to: x"
        item(drawn, "1700000001-a", bad)
        old = specs_dir(drawn, "1700000002-old")
        (old / "frame").mkdir(parents=True)
        (old / "frame" / "design.md").write_text(
            "# old\n\n## Scope\n\nIn.\n", encoding="utf-8"
        )
        code, text = at(drawn, "main")
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
        code, text = at(drawn, "main", "--apply")
        assert code == 0, text
        assert not specs_dir(drawn, "1700000001-a").exists(), text
        assert not old.exists(), text

    def test_apply_names_a_document_past_the_ceiling(self, drawn):
        """Scope 5: after the removals, each document past `Document token
        ceiling` is named as one to split, and that refuses nothing."""
        configure(drawn, ("Document token ceiling", "10"))
        item(drawn, "1700000001-a", op("add", "U", new="Released."))
        code, text = at(drawn, "main", "--apply")
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

    @pytest.mark.parametrize("carried", ["link", "marker"])
    def test_apply_removes_a_directory_its_published_note_carries(
        self, noted, monkeypatch, gh, carried
    ):
        """S5 of #1139. A note carries the entry where it links the pull
        request under any owner and name, since a renamed repository's old
        links redirect, or where it holds the work item's marker, which the
        notes published before #1139 carry. The list comes in two pages, as
        `--paginate` prints a long one."""
        path = specs_dir(noted, "1700000001-a")
        body = (
            "[#42](https://github.com/old/name/pull/42)\n"
            if carried == "link"
            else "<!-- specs/1700000001-a -->\n"
        )
        gh.releases([release("v1.0.0")], [release("v1.2.3", body)])
        answered(monkeypatch, noted, real={"notes"})
        code, text = at(noted, "main", "--apply")
        assert code == 0, text
        assert not path.exists(), text
        assert "removed seal/threads/1700000001-a/\n" in text, text
        # The note was read and carried the entry: no reason for not reading it.
        assert "no note read" not in text, text
        assert text.endswith(
            "\nremoved 1 directory; kept 0 with a row to close and 0 whose note "
            "lacks its entry\n"
        ), text

    @pytest.mark.parametrize("listed", ["another", "a draft"])
    def test_apply_keeps_a_directory_whose_tag_has_no_published_release(
        self, noted, monkeypatch, gh, listed
    ):
        """S7b of #1139, its first half. `v1.2.3` holds the fragment, and the
        list holds another published release, so the repository publishes
        Releases and `v1.2.3` lacks one. A draft at `v1.2.3` is not
        published, and another tag's note is not this one's, though both
        link #42."""
        path = specs_dir(noted, "1700000001-a")
        tip = git_out(noted, "rev-parse", "main")
        link = "[#42](https://github.com/o/r/pull/42)"
        listing = [release("v1.0.0", link)]
        if listed == "a draft":
            listing.append(release("v1.2.3", link, draft=True))
        gh.releases(listing)
        answered(monkeypatch, noted, real={"notes"})
        code, text = at(noted, "main", "--apply")
        assert code == 1, text
        assert path.exists(), text
        assert (
            "kept seal/threads/1700000001-a/: v1.2.3 has no published GitHub "
            "Release, so no note carries its entry, a link to pull request #42; "
            f"publish one from `git show {tip}:seal/threads/1700000001-a/"
            "changelog.md` and run `seal settle --apply` again\n"
        ) in text, text

    @pytest.mark.parametrize("listed", ["none", "a draft"])
    def test_apply_removes_where_the_repository_publishes_no_release(
        self, noted, monkeypatch, gh, listed
    ):
        """S7b of #1139, its second half. The list holds no published
        release, so the repository publishes no Releases: the directory goes,
        and the line under its `removed` line says so."""
        path = specs_dir(noted, "1700000001-a")
        gh.releases([release("v1.2.3", draft=True)] if listed == "a draft" else [])
        answered(monkeypatch, noted, real={"notes"})
        code, text = at(noted, "main", "--apply")
        assert code == 0, text
        assert not path.exists(), text
        assert (
            "removed seal/threads/1700000001-a/\n"
            "    no note read: this repository has published no GitHub Release, "
            "so v1.2.3 has no note\n"
        ) in text, text

    def test_apply_removes_where_no_published_note_is_built_from_the_fragments(
        self, noted, monkeypatch, gh
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
        path = specs_dir(noted, "1700000001-a")
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
        answered(monkeypatch, noted, real={"notes"})
        code, text = at(noted, "main", "--apply")
        assert code == 0, text
        assert not path.exists(), text
        assert (
            "removed seal/threads/1700000001-a/\n"
            "    no note read: no published release of this repository opens an "
            "entry with a `[#N](https://github.com/<owner>/<name>/pull/N)` line "
            "or the old marker, so its notes are not built from the fragments\n"
        ) in text, text
        assert gh.calls() == [RELEASES_CALL], gh.calls()

    def test_apply_removes_a_directory_whose_fragment_is_empty(
        self, shared_repo, monkeypatch, gh
    ):
        """Round 1 finding 2 of #1139. The release note gives an empty
        fragment no entry (`publish_release_note.py#fragments`), so no note
        can carry it: the directory goes, the line under its `removed` line
        says the fragment holds no text, and no `gh` is asked for it. The
        other notes are built from the fragments and lack its link."""
        path = fragment(
            shared_repo, "1700000001-a", "feat: a (#42)", tag="v1.2.3", text="\n  \n"
        )
        gh.releases([release("v1.2.3", "[#41](https://github.com/o/r/pull/41)\n")])
        answered(monkeypatch, shared_repo, real={"notes"})
        code, text = at(shared_repo, "main", "--apply")
        assert code == 0, text
        assert not path.exists(), text
        assert (
            "removed seal/threads/1700000001-a/\n"
            "    no note read: its `changelog.md` at main holds no text, and the "
            "release note gives an empty fragment no entry\n"
        ) in text, text
        assert gh.calls() == [], gh.calls()

    def test_an_open_row_keeps_its_directory_before_its_note_is_read(
        self, noted, monkeypatch, gh
    ):
        """S8 of #1139. The record holds an open row and the note lacks the
        entry. The row keeps the directory as before, and no note is read
        for it, so `gh` is not asked."""
        path = specs_dir(noted, "1700000001-a")
        write(path, "gaps.md", OPEN)
        gh.releases([release("v1.2.3", "no entry")])
        answered(monkeypatch, noted, real={"notes"})
        code, text = at(noted, "main", "--apply")
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

    def test_shared_mode_asks_gh_for_no_note_it_cannot_read(
        self, shared_repo, gh, monkeypatch
    ):
        """S6 of #955 and S7 of #1139: a shared root's work items are
        released by presence at `--released-at`, so the dry run asks no
        `gh`, even for an item whose `routing.md` names a branch. `--apply`
        asks it only for a note it can read. One released work item holds no
        `changelog.md`, the commit adding another's names no pull request
        though `v1.0.0` holds it, and no version tag holds the third's. Each
        goes, and the line under its `removed` line says which case held.
        `released_local` stays real beside `notes`, so a shared root read as
        a local one would ask `gh`."""
        standing(shared_repo, MOMENT)
        bare = specs_dir(shared_repo, MOMENT)
        write(
            specs_dir(shared_repo, "1700000001-a"),
            "routing.md",
            ROUTED.format(name="1700000001-a", branch="feat/1-a"),
        )
        fragment(shared_repo, "1700000001-a", "feat: a", tag="v1.0.0")
        unnumbered = git_out(shared_repo, "rev-parse", "v1.0.0")
        fragment(shared_repo, "1700000002-b", "feat: b (#42)")
        untagged = git_out(shared_repo, "rev-parse", "main")
        answered(monkeypatch, shared_repo, real={"notes", "released_local"})
        code, text = at(shared_repo, "main")
        assert code == 0, text
        code, text = at(shared_repo, "main", "--apply")
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


class Test_main:
    def test_two_specs_on_one_sentence_are_one_group_in_merge_order(
        self, shared_repo, capfd
    ):
        """S1: B was added after A on one line of history, so B is listed
        after A whatever their ids say. A's `from` no longer matches, since
        the section holds the sentence as A left it, and nothing is refused;
        with both records holding no row, `--apply` removes both and writes
        no document."""
        (shared_repo / "docs" / "a.md").write_text(
            DOC.replace("old sentence.", "y."), encoding="utf-8"
        )
        commit_everything(shared_repo, "the section as A left it")
        item(shared_repo, "1700000009-a", op("change", "S", "old sentence.", "y."))
        commit_everything(shared_repo, "a")
        item(shared_repo, "1700000001-b", op("change", "S", "y.", "z."))
        commit_everything(shared_repo, "b")
        before = files(shared_repo)
        code, text = dry_run(shared_repo, capfd)
        assert code == 0, text
        assert files(shared_repo) == before, "the dry run wrote to the tree"
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
        docs = {k: v for k, v in files(shared_repo).items() if k.startswith("docs")}
        code, text = apply(shared_repo, capfd)
        assert code == 0, text
        assert not specs_dir(shared_repo, "1700000009-a").exists(), text
        assert not specs_dir(shared_repo, "1700000001-b").exists(), text
        assert {
            k: v for k, v in files(shared_repo).items() if k.startswith("docs")
        } == docs

    def test_the_judgments_earlier_settles_removed_are_read_from_the_history(
        self, shared_repo, capfd
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
            shared_repo,
            old,
            plan,
            "the old work item (#3)",
            "settle 0.1.0 (#7)",
            "v0.1.0",
        )
        released_item(
            shared_repo,
            "1700000002-new",
            {"frame/plan.md": judgments_plan([("2026-10-03", "x", "y", run_doc)])},
        )
        code, text = dry_run(shared_repo, capfd)
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

    def test_all_earlier_reads_the_plans_of_every_removing_commit(
        self, removals, capfd
    ):
        """#1481, design S2. Under `--all-earlier` the section prints the
        rows of every removing commit's plans, newest first, and no line of
        older commits not read."""
        shared_repo, printed = removals
        code, text = dry_run(shared_repo, capfd, "--all-earlier")
        assert code == 0, text
        assert earlier_block(text) == (
            "\njudged against: z\n" + "".join(printed).rstrip("\n")
        ), earlier_block(text)

    @pytest.mark.parametrize(
        "other, sentence",
        [
            pytest.param(
                "--apply",
                "settle: --all-earlier and --apply cannot be given together: "
                "--apply prints none of the judgments earlier settles removed, "
                "so nothing was read and nothing was removed.\n",
                id="apply",
            ),
            pytest.param(
                "--draft",
                "settle: --all-earlier and --draft cannot be given together: "
                "the draft prints none of the judgments earlier settles "
                "removed, so nothing was read and nothing was written.\n",
                id="draft",
            ),
        ],
    )
    def test_refuses_all_earlier_beside_apply_or_draft_and_reads_nothing(
        self, removals, capfd, monkeypatch, other, sentence
    ):
        """#1481, design S3. `--all-earlier` widens only what the dry run
        prints, so beside `--apply` or `--draft`, which print none of it,
        it is refused with exit 2 and one sentence before anything is read,
        and the tree is left as it was."""
        shared_repo, _ = removals
        before = files(shared_repo)

        def survey(*_args, **_kwargs):
            raise AssertionError("the refused run read the records")

        monkeypatch.setattr(settle, "survey", survey)
        code, text = dry_run(shared_repo, capfd, "--all-earlier", other)
        assert code == 2, text
        assert text == sentence, text
        assert files(shared_repo) == before

    def test_local_mode_lists_a_released_and_an_unreleased_item(
        self, local_repo, gh_on_path, capfd
    ):
        """S1 of #955. The root is under the git directory, so `settle` reads
        it there: the item whose branch's pull request merged into `main` is
        released, with its pull request and merge commit, and its rule joins
        a group; the other is unreleased because nothing merged from its
        branch. `gh` is asked once per branch, and the run writes and removes
        nothing. A repository holding work items is never told it has none,
        the half of the old local-mode refusal's case that stays. Its `gh` is
        a script first on PATH, the one run here that starts a `gh`."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="Rule."))
        local_item(local_repo, "1700000002-b", "feat/2-b", op("add", "U", new="B."))
        oid = merge(local_repo, "feat/1-a")
        gh_on_path.merged("feat/1-a", (11, oid))
        before = files(local_repo)
        records = sorted(p for p in (local_repo / ".git" / "seal").rglob("*"))
        code, text = dry_run(local_repo, capfd)
        assert code == 0, text
        home = os.path.join(str(local_repo), ".git", "seal")
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
        assert files(local_repo) == before, "the dry run wrote to the tree"
        assert sorted(p for p in (local_repo / ".git" / "seal").rglob("*")) == records
        query = ["pr", "list", "--head", "{}", "--state", "merged"]
        query += ["--json", "number,mergeCommit"]
        assert gh_on_path.calls() == [
            [a.format(b) for a in query] for b in ("feat/1-a", "feat/2-b")
        ], gh_on_path.calls()

    def test_a_local_run_from_a_subdirectory_reads_the_repositorys_top(
        self, local_repo, capfd, monkeypatch
    ):
        """Round 1 finding 2 of #955: from a subdirectory the local root is
        still found under the git directory, so the policy root has to be read
        from the repository's top too, or a document that is there reads as
        absent and the settling session is sent to write it."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="Rule."))
        answered(monkeypatch, local_repo)
        below = str(local_repo / "docs")
        code = settle.main(["--root", below, "--released-at", "main"])
        out = capfd.readouterr()
        text = out.out + out.err
        assert code == 0, text
        assert group_text(text).startswith(
            "    place: docs/a.md section `S`, at docs/a.md:3-9\n"
        ), text
        assert "not in the tree" not in text, text

    def test_a_shared_run_from_a_subdirectory_reads_the_repositorys_top(
        self, shared_repo, gh, capfd, monkeypatch
    ):
        """Round 2 finding 1 of #955: `main` resolves the root to the
        repository's top in both modes, so a shared run from a subdirectory
        prints what a run from the top prints. It used to refuse, saying the
        repository had no seal/threads/ at either place, which was false there."""
        item(shared_repo, "1700000001-a", op("add", "S", new="Rule."))
        answered(monkeypatch, shared_repo)
        top = dry_run(shared_repo, capfd)
        assert top[0] == 0, top[1]
        assert group_text(top[1]).startswith(
            "    place: docs/a.md section `S`, at docs/a.md:3-9\n"
        ), top[1]
        below = str(shared_repo / "docs")
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
        self, local_repo, gh, capfd, monkeypatch
    ):
        """S2 of #955, one line of history: B was created after A and merged
        before it, so B is listed first, and ancestry orders the pair. The
        readers but the three that read the merges are `answered`."""
        answered(
            monkeypatch,
            local_repo,
            real={"released_local", "merge_order", "_ancestor"},
        )
        local_item(
            local_repo, "1700000001-a", "feat/1-a", op("change", "S", "y.", "z.")
        )
        local_item(
            local_repo,
            "1700000002-b",
            "feat/2-b",
            op("change", "S", "old sentence.", "y."),
        )
        gh.merged("feat/2-b", (12, merge(local_repo, "feat/2-b")))
        gh.merged("feat/1-a", (11, merge(local_repo, "feat/1-a")))
        code, text = dry_run(local_repo, capfd)
        assert code == 0, text
        group = group_text(text)
        assert "    1. change  1700000002-b  " in group, text
        assert "    2. change  1700000001-a  " in group, text
        assert "unordered" not in group, text

    def test_a_merge_commit_the_ref_does_not_reach_leaves_the_item(
        self, local_repo, gh, capfd, monkeypatch
    ):
        """S3 of #955: the pull request merged into a branch `--released-at`
        does not reach, so the item is unreleased with that reason, and
        `--apply` keeps it. The readers but `released_local` are
        `answered`."""
        answered(monkeypatch, local_repo, real={"released_local"})
        git_out(local_repo, "branch", "other")
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="Rule."))
        oid = merge(local_repo, "feat/1-a", into="other")
        git_out(local_repo, "switch", "-q", "main")
        gh.merged("feat/1-a", (11, oid))
        code, text = dry_run(local_repo, capfd)
        assert code == 0, text
        assert (
            f"    1700000001-a  main reaches no merge commit of the pull requests "
            f"from `feat/1-a` that merged: #11 at {oid}\n"
        ) in text, text
        assert "released at main: 0 work items; 1 unreleased and untouched\n" in text
        code, text = apply(local_repo, capfd)
        assert code == 0, text
        assert local_dir(local_repo, "1700000001-a").exists(), text

    def test_apply_in_local_mode_removes_under_the_git_directory_alone(
        self, local_repo, capfd, monkeypatch
    ):
        """S4 of #955: the released item whose record holds no open row goes
        from under the git directory, the one holding a row is kept and its
        row named, the unreleased one stays, and nothing under the
        repository's top is written or removed; with the row closed on disk,
        a second run removes the kept one."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        local_item(local_repo, "1700000002-b", "feat/2-b", op("add", "U", new="B."))
        row = OPEN.replace("a claim nobody ran", "a claim about `questions.md`")
        held = local_item(
            local_repo,
            "1700000003-c",
            "feat/3-c",
            op("add", "T", new="C."),
            overview=row,
        )
        (held / "questions.md").write_text("# q\n", encoding="utf-8")
        answered(monkeypatch, local_repo, unreleased={"1700000002-b"})
        before = files(local_repo)
        code, text = dry_run(local_repo, capfd)
        rows = text.split(f"{settle.ROWS_HEADING}\n")[1].split("\n\n")[0]
        assert rows == (
            "    1700000003-c\n"
            "        open in gaps.md: a claim about `questions.md`\n"
            "            `questions.md` in the tree"
        ), text
        code, text = apply(local_repo, capfd)
        assert code == 1, text
        assert not local_dir(local_repo, "1700000001-a").exists(), text
        assert local_dir(local_repo, "1700000002-b").exists(), text
        assert local_dir(local_repo, "1700000003-c").exists(), text
        assert "removed seal/threads/1700000001-a/\n" in text, text
        assert (
            "kept seal/threads/1700000003-c/: its record holds 1 open row; close "
            "each (`closed` with what closed it) and run `seal settle --apply` again\n"
            "    open in gaps.md: a claim about `questions.md`\n"
        ) in text, text
        assert files(local_repo) == before, "the apply wrote or removed in the tree"
        (local_dir(local_repo, "1700000003-c") / "gaps.md").write_text(
            OVERVIEW_CLOSED, encoding="utf-8"
        )
        code, text = apply(local_repo, capfd)
        assert code == 0, text
        assert not local_dir(local_repo, "1700000003-c").exists(), text
        assert local_dir(local_repo, "1700000002-b").exists(), text
        assert "    closed in gaps.md: a claim\n" in text, text

    def test_apply_in_local_mode_names_a_gaps_md_away_from_its_place(
        self, local_repo, capfd, monkeypatch
    ):
        """S5 of #1126: under the git directory the misplaced file is found
        where `--apply` removes it. The dry run names `trail/gaps.md`, and
        `--apply` removes the directory and names the file under its
        `removed` line. Seen red with the fix reverted in `settle.py`."""
        name = "1700000001-a"
        path = local_item(local_repo, name, "feat/1-a")
        (path / "trail").mkdir()
        (path / "trail" / "gaps.md").write_text(OPEN, encoding="utf-8")
        answered(monkeypatch, local_repo)
        code, text = dry_run(local_repo, capfd)
        line = not_read(name, "trail/gaps.md", "gaps.md")
        assert line in text, text
        assert code == 0, text
        code, text = apply(local_repo, capfd)
        assert code == 0, text
        assert not path.exists(), text
        assert f"removed seal/threads/{name}/\n    not read: {line}\n" in text, text

    @pytest.mark.parametrize("arm", [False, True], ids=["report", "apply"])
    @pytest.mark.parametrize("state", ["absent", "fails", "garbled", "entry"])
    def test_refuses_a_gh_that_cannot_be_asked_in_local_mode(
        self, local_repo, gh, capfd, monkeypatch, state, arm
    ):
        """S5 of #955: with no `gh` to ask, every local item would read as
        unreleased and the run would report nothing to settle, the quiet zero
        the `--released-at` refusal is written against. So it exits 2, names
        `gh` and what it said, and removes nothing."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        if state == "absent":
            # `lib/gitcmd.py#gh` finds no `gh`, and git is still found.
            which = gitcmd.shutil.which
            monkeypatch.setattr(
                gitcmd.shutil,
                "which",
                lambda name, *a, **k: None if name == "gh" else which(name, *a, **k),
            )
            said = (
                "`gh pr list --head feat/1-a --state merged --json "
                "number,mergeCommit` could not be run: `gh` is not on PATH"
            )
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
        code, text = dry_run(local_repo, capfd, *(["--apply"] if arm else []))
        assert code == 2, text
        assert local_dir(local_repo, "1700000001-a").exists(), text
        assert text.startswith(
            f"settle: `gh` cannot be asked which pull requests merged: {said}. "
            "Nothing was read and nothing was removed."
        ), text
        assert (
            "a repository on a host `gh` cannot ask cannot settle in local mode"
        ) in flat(text), text

    @pytest.mark.parametrize(
        "flags, words",
        [
            ([], ("ls-tree", "-r")),
            ([], ("show",)),
            ([], ("--diff-filter=A", "--name-only", "--format=%x01%H")),
            ([], ("merge-base", "--is-ancestor")),
            ([], ("ls-files", "-z")),
            (["--from", "docs"], ("--cached", "--others")),
            (["--apply"], ("ls-tree", "-r")),
            (["--draft"], ("--diff-filter=A", "--name-only", "--format=%x01%H")),
        ],
        ids=[
            "released",
            "show",
            "order",
            "unordered",
            "tracked_text",
            "from",
            "apply",
            "draft",
        ],
    )
    def test_refuses_a_git_that_did_not_answer_in_one_line(
        self, two_designs, capfd, monkeypatch, flags, words
    ):
        """S7 of #1573: a git read past `lib/gitcmd.py#TIMEOUT`, in the dry
        run, `--from`, `--apply` or `--draft`, ends `settle` with one line
        on stderr, `settle: ` and the runner's line naming the command and
        the bound, at exit 2, with nothing printed or removed and no
        traceback. Seen red against `settle.py` before #1573, where no read
        had a bound and the timeout was raised out of `main`."""
        shared_repo = two_designs
        before = files(shared_repo)
        asked = unanswered(monkeypatch, *words)
        flags = [str(shared_repo / f) if f == "docs" else f for f in flags]
        code = settle.main(
            ["--root", str(shared_repo), "--released-at", "main", *flags]
        )
        out = capfd.readouterr()
        assert len(asked) == 1, asked
        assert out.err == f"settle: {past_the_bound(asked[0])}\n", out.err
        assert code == 2, out.err
        assert out.out == "", out.out
        assert files(shared_repo) == before, (
            "a settle that did not finish changed the tree"
        )

    @pytest.mark.parametrize(
        "words",
        [
            ("rev-parse", "--verify"),
            ("pr", "list"),
            ("merge-base", "--is-ancestor"),
            ("rev-list", "--topo-order"),
        ],
        ids=["resolves", "gh", "reaches", "merge_order"],
    )
    def test_refuses_a_git_or_gh_that_did_not_answer_in_local_mode(
        self, local_repo, gh, capfd, monkeypatch, words
    ):
        """S7 of #1573 in local mode. A git read past the bound ends the run
        as in a shared root. A `gh` past it is the `gh` that cannot be
        asked, and its refusal names the runner's line. Seen red against
        `settle.py` before #1573, where git raised the timeout out of `main`
        and `gh`'s line spelt the timeout's exception inside its own."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        gh.merged("feat/1-a", (11, merge(local_repo, "feat/1-a")))
        asked = unanswered(monkeypatch, *words)
        code = settle.main(["--root", str(local_repo), "--released-at", "main"])
        out = capfd.readouterr()
        assert len(asked) == 1, asked
        said = past_the_bound(asked[0])
        if words[0] == "pr":
            assert out.err == settle.UNASKED.format(why=said), out.err
        else:
            assert out.err == f"settle: {said}\n", out.err
        assert code == 2, out.err
        assert out.out == "", out.out
        assert local_dir(local_repo, "1700000001-a").exists(), out.err

    def test_a_released_at_ref_that_does_not_resolve_is_refused_in_local_mode(
        self, local_repo, gh, capfd
    ):
        """The `--released-at` refusal holds in local mode too, before `gh`
        is asked: a ref nothing can read would make every merge commit
        unreachable, the quiet zero by another door."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        code = settle.main(["--root", str(local_repo), "--released-at", "no/such/ref"])
        text = capfd.readouterr().err
        assert code == 2, text
        assert "--released-at no/such/ref does not resolve" in text, text
        assert gh.calls() == [], gh.calls()

    def test_gh_is_asked_once_for_a_branch_two_items_name(
        self, local_repo, gh, capfd, monkeypatch
    ):
        """`gh` is asked once per branch, so two work items naming one branch,
        the reused-branch limit, cost one query and both read as released.
        The merge commit `gh` names is the world's own commit on `main`, and
        the readers but `released_local` are `answered`."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        local_item(local_repo, "1700000002-b", "feat/1-a", op("add", "U", new="B."))
        gh.merged("feat/1-a", (11, git_out(local_repo, "rev-parse", "main")))
        answered(monkeypatch, local_repo, real={"released_local"})
        code, text = dry_run(local_repo, capfd)
        assert code == 0, text
        assert "released at main: 2 work items; 0 unreleased" in text, text
        assert len(gh.calls()) == 1, gh.calls()

    def test_asks_git_each_read_once_in_a_run(
        self, shared_repo, gh, capfd, monkeypatch
    ):
        """#1603, design S5. Two released designs each change `S` and `T`,
        so the merge order asks the ancestry of their one pair of commits
        once for each group, and the first one's record holds an open row,
        whose paths the dry run looks up in the tracked tree that its scan
        for citations lists too. An earlier settle removed a plan its tag
        holds, and the second design's fragment is in a published release,
        so `--apply` reads the tags for the judgments and for the note. The
        dry run and `--apply` each start no git command twice with the
        same input, every reader real. Seen red against `settle.py` before
        #1603, where the dry run repeats the pair's `merge-base
        --is-ancestor` and `ls-files -z`, and `--apply` repeats the pair and
        the three reads of `versions`."""
        removed_plan(
            shared_repo,
            "1700000001-old",
            judgments_plan([("2026-10-01", "x", "y", "z")]),
            "the old work item (#3)",
            "settle 0.1.0 (#7)",
            "v0.1.0",
        )
        for name, rule in (("1700000002-a", "A."), ("1700000003-b", "B.")):
            item(
                shared_repo,
                name,
                op("add", "S", new=rule) + "\n" + op("add", "T", new=rule),
            )
            commit_everything(shared_repo, name)
        write(specs_dir(shared_repo, "1700000002-a"), "gaps.md", OPEN)
        commit_everything(shared_repo, "an open row")
        fragment(shared_repo, "1700000003-b", "feat: b (#43)", tag="v0.2.0")
        gh.releases([release("v0.2.0", "[#43](https://github.com/o/r/pull/43)")])
        (code, text), asked = asks(monkeypatch, lambda: dry_run(shared_repo, capfd))
        assert code == 0, text
        assert "\ngroup 2\n" in text, text
        assert repeated(asked) == [], repeated(asked)
        (code, text), asked = asks(monkeypatch, lambda: apply(shared_repo, capfd))
        assert code == 1, text
        assert "kept seal/threads/1700000002-a/" in text, text
        assert "removed seal/threads/1700000003-b/\n" in text, text
        assert repeated(asked) == [], repeated(asked)

    def test_a_released_at_given_as_the_merge_commit_reaches_it(
        self, local_repo, gh, capfd, monkeypatch
    ):
        """The reach is asked of `lib/gitcmd.py#is_ancestor`, which counts a
        commit as reaching itself, and not of `rule_changes.py#_ancestor`,
        which answers False for two equal commits, so a `--released-at` naming the
        merge commit still reads the item as released (round 1 finding 6).
        The readers but `released_local` are `answered`."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        oid = merge(local_repo, "feat/1-a")
        gh.merged("feat/1-a", (11, oid))
        answered(monkeypatch, local_repo, real={"released_local"})
        code = settle.main(["--root", str(local_repo), "--released-at", oid])
        out = capfd.readouterr()
        assert code == 0, out.err
        assert f"released at {oid}: 1 work item;" in out.out, out.out

    def test_the_first_listed_pull_request_the_ref_reaches_is_taken(
        self, local_repo, gh, capfd, monkeypatch
    ):
        """Several merged pull requests from one branch: one the ref does not
        reach does not hide a later-listed one it does (round 1 finding 6).
        The readers but `released_local` are `answered`."""
        answered(monkeypatch, local_repo, real={"released_local"})
        git_out(local_repo, "branch", "other")
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        stray = merge(local_repo, "feat/1-a", into="other")
        git_out(local_repo, "switch", "-q", "main")
        git_out(local_repo, "merge", "-q", "--no-ff", "-m", "m", "feat/1-a")
        reached = git_out(local_repo, "rev-parse", "HEAD")
        gh.merged("feat/1-a", (12, stray), (11, reached))
        code, text = dry_run(local_repo, capfd)
        assert code == 0, text
        assert f"1700000001-a  pull request #11  merge commit {reached}" in text, text

    def test_a_pull_request_listed_with_no_merge_commit_is_named_as_such(
        self, local_repo, gh, capfd
    ):
        """A listed pull request whose `mergeCommit` is null names nothing git
        can reach, so the item is unreleased. `gh` was asked for merged pull
        requests and listed it, so the reason names it as one with no merge
        commit rather than saying none merged (round 1 finding 3)."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        gh.merged("feat/1-a", (11, None))
        code, text = dry_run(local_repo, capfd)
        assert code == 0, text
        assert (
            "    1700000001-a  main reaches no merge commit of the pull requests "
            "from `feat/1-a` that merged: #11 with no merge commit\n"
        ) in text, text

    def test_apply_keeps_a_directory_its_published_note_does_not_carry(
        self, shared_repo, gh, capfd
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
        kept = fragment(shared_repo, "1700000001-a", "feat: a (#42)")
        fragment(shared_repo, "1700000002-b", "feat: b (#43)", tag="v1.2.3")
        git_out(shared_repo, "tag", "v1.10.0")
        at = git_out(shared_repo, "rev-parse", "main")
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
        code, text = dry_run(shared_repo, capfd)
        assert code == 0, text
        assert gh.calls() == [], gh.calls()
        code, text = apply(shared_repo, capfd)
        assert code == 1, text
        assert kept.exists(), text
        assert not specs_dir(shared_repo, "1700000002-b").exists(), text
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

    @pytest.mark.parametrize("state", ["fails", "garbled", "entry"])
    def test_apply_stops_where_the_release_list_cannot_be_read(
        self, noted, gh, capfd, monkeypatch, state
    ):
        """S6 of #1139. A `gh` that fails, or answers anything but pages that
        are each a list of objects, stops `--apply` with exit 2 and one
        sentence naming `gh` and what it said. No directory goes, the one
        that needs no note among them, which sorts first so that a note read
        only when its directory's turn comes would have let it go."""
        standing(noted, "1700000000-bare")
        bare = specs_dir(noted, "1700000000-bare")
        tagged = specs_dir(noted, "1700000001-a")
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
        answered(monkeypatch, noted, real={"notes"})
        code, text = apply(noted, capfd)
        assert code == 2, text
        assert bare.exists(), text
        assert tagged.exists(), text
        assert text.startswith(
            f"settle: `gh` cannot be asked for this repository's releases: {said}. "
            "Nothing was removed."
        ), text

    def test_a_git_that_cannot_read_the_adding_commit_stops_apply(
        self, noted, gh, capfd, monkeypatch
    ):
        """#1139's phase 2. Where `git` cannot read the commit that added a
        released `changelog.md`, the pull request it names is unknown, and
        removing on an unknown is the quiet path an unreadable release list
        is refused for. So `--apply` exits 2 with what `git` said, asks no
        `gh`, and removes nothing."""
        standing(noted, MOMENT)
        bare = specs_dir(noted, MOMENT)
        path = specs_dir(noted, "1700000001-a")

        def refuse(root, revisions, rel):
            raise RuntimeError(f"`git log {revisions} -- {rel}` exited 128: fatal")

        monkeypatch.setattr(settle, "adding_commit", refuse)
        answered(monkeypatch, noted, real={"notes"})
        code, text = apply(noted, capfd)
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
        self, local_repo, gh, capfd
    ):
        """S7 of #955: one item has no `routing.md`, the other's has no
        `Branch` row, so there is no branch to ask about."""
        local_item(local_repo, "1700000001-a", changes=op("add", "S", new="A."))
        routing = ROUTED.format(name="1700000002-b", branch="x")
        local_item(local_repo, "1700000002-b", changes=op("add", "S", new="B."))
        (local_dir(local_repo, "1700000002-b") / "routing.md").write_text(
            routing.replace("| Branch | x |\n", ""), encoding="utf-8"
        )
        code, text = dry_run(local_repo, capfd)
        assert code == 0, text
        unreleased = text.split(settle.UNMERGED_HEADING + "\n")[1].split("\n\n")[0]
        assert unreleased == (
            f"    1700000001-a  {NO_BRANCH}\n    1700000002-b  {NO_BRANCH}"
        ), text
        assert gh.calls() == [], gh.calls()

    def test_a_local_routing_md_routing_py_does_not_read_names_no_branch(
        self, local_repo, gh, capfd
    ):
        """A `routing.md` with a `Branch` row whose `Review` answer is outside
        the vocabulary is no declaration to `lib/routing.py#parse`, so the
        item is unreleased and `gh` is not asked. The reason says the file is
        not read as a declaration, since a person who opens it finds the
        `Branch` row there (round 1 finding 3)."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "S", new="A."))
        path = local_dir(local_repo, "1700000001-a") / "routing.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(
            text.replace("| Review | through", "| Review | Through"), encoding="utf-8"
        )
        code, text = dry_run(local_repo, capfd)
        assert code == 0, text
        unreleased = text.split(settle.UNMERGED_HEADING + "\n")[1].split("\n\n")[0]
        assert unreleased == f"    1700000001-a  {NO_BRANCH}", text
        assert gh.calls() == [], gh.calls()

    def test_a_local_repository_with_no_policy_root_settles(
        self, local_repo, capfd, monkeypatch
    ):
        """S9 of #955: a local-mode repository has no `docs/` until the
        settling session creates it. The dry run says the new document is not
        there, and `--apply` removes the item and reads no policy root."""
        git_out(local_repo, "rm", "-rq", "docs")
        commit_everything(local_repo, "no policy root")
        local_item(
            local_repo,
            "1700000001-a",
            "feat/1-a",
            op("add", new="# New", file="docs/new.md"),
        )
        answered(monkeypatch, local_repo)
        code, text = dry_run(local_repo, capfd)
        assert code == 0, text
        assert group_text(text).startswith(
            "    place: docs/new.md, the whole document: the document is not in "
            "the tree"
        ), text
        code, text = apply(local_repo, capfd)
        assert code == 0, text
        assert not local_dir(local_repo, "1700000001-a").exists(), text
        assert settle.AFTER_HEADING not in text, text
        assert not (local_repo / "docs").exists()

    def test_a_repository_with_no_root_at_either_place_says_so(self, tmp_path):
        """The other arm of the same resolution, kept apart from local mode
        because the two are different states and used to share one sentence."""
        repo = tmp_path / "repo"
        repo.mkdir()
        git_out(repo, "init", "-q")
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
        git_out(repo, "init", "-q")
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
        """Round 3, finding 1. `lib/optin.py#home_at` reads the scratch marker
        with `os.path.isfile` and says why: `os.path.exists` also accepted a
        DIRECTORY of that name, and one created once turned every gate off in
        every clone. The refusal here asked `exists`, so a repository holding a
        directory of that name and no root was told it had opted out and to delete
        "that file" — and no gate reads a directory as the opt-out, so every clause
        of that sentence was false. The three readers of one marker answer alike."""
        repo = tmp_path / "repo"
        repo.mkdir()
        git_out(repo, "init", "-q")
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
            "reading `lib/optin.py` rejected by name"
        )

    def test_the_refusal_path_asks_for_the_common_directory_once(
        self, tmp_path, monkeypatch
    ):
        """Round 3, finding 5. `home_at(root)` resolves the common git directory
        for itself, and the opt-out arm then resolved it a second time, although
        `home_at(root, common)` exists for a caller that needs the value too and
        `lib/optin.py` documents the parameter with the measurement that created
        it. Counted through the one module `lib/sibling.py#load` hands `main`,
        and counted as calls rather than processes: on a main worktree the
        resolver's fast path costs no process, so a process count would have
        said nothing."""
        repo = tmp_path / "repo"
        repo.mkdir()
        git_out(repo, "init", "-q")
        optin = settle.sibling.load(settle.OPTIN)
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
        monkeypatch.setattr(optin, "git_common_dir", counted)
        monkeypatch.setattr(optin, "home_at", recorded)
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
        git_out(repo, "init", "-q")
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
    def test_accepts_a_settled_root_and_says_so(
        self, shared_repo, capfd, keep_empty_dir, flags
    ):
        """G7. After the last settle a fresh checkout has no `seal/threads/` at
        all and the tree that ran `--apply` has an empty one. Both are the state
        a complete settle reaches, and `settle` used to refuse the first at exit
        2 — so the command could not run on its own finished work. `--draft`
        there has no operation to write, and writes nothing (#1217)."""
        if keep_empty_dir:
            (shared_repo / "seal" / "threads").mkdir()
        before = files(shared_repo)
        code = settle.main(
            ["--root", str(shared_repo), "--released-at", "HEAD", *flags]
        )
        out = capfd.readouterr()
        assert code == 0, out.out + out.err
        assert "holds no work item" in out.out, out.out + out.err
        assert "A complete settle ends here" in out.out, out.out
        assert files(shared_repo) == before

    @pytest.mark.rule("an-empty-root-is-settled")
    @pytest.mark.parametrize("arm", [False, True], ids=["report", "apply"])
    def test_accepts_a_settled_local_root_and_names_it(self, local_repo, arm, capfd):
        """S8 of #955: a local root with no work item is settled too. The
        sentence names the root under the git directory, and says nothing
        about a fresh checkout, which carries no local root."""
        code, text = dry_run(local_repo, capfd, *(["--apply"] if arm else []))
        assert code == 0, text
        home = os.path.join(str(local_repo), ".git", "seal")
        assert text == (
            f"settle: {home} is the seal/ root, in local mode, and its threads/ "
            "holds no work item — nothing to show and nothing to remove. A "
            "complete settle ends here.\n"
        ), text

    def test_from_lists_every_document_of_a_named_directory_in_gits_order(
        self, shared_repo, capfd, monkeypatch
    ):
        """#1054 A2: every file git lists under the directory is a document,
        nested or of any extension, and an ignored file is none. Each is
        listed once in the order of the commits that add it, a moved file
        counting as added where it lands, with its last change beside it; a
        file changed in the working tree says so, and one no commit adds
        comes last. The path is read from the directory the command runs in,
        and the listing stands after the judgments and before what `--apply`
        removes."""
        item(shared_repo, "1700000001-a", op("add", "U", new="Rule."))
        write(shared_repo, "adr/0001.md", "one\n")
        write(shared_repo, "adr/old/moved.md", "moved\n")
        commit_everything(shared_repo, "first records")
        first = stamp(shared_repo)
        write(shared_repo, "adr/sub/0002.md", "nested\n")
        write(shared_repo, "adr/notes.txt", "no md extension\n")
        commit_everything(shared_repo, "second records")
        second = stamp(shared_repo)
        write(shared_repo, "adr/0001.md", "one, revised\n")
        commit_everything(shared_repo, "revise the first")
        third = stamp(shared_repo)
        git_out(shared_repo, "mv", "adr/old/moved.md", "adr/moved.md")
        commit_everything(shared_repo, "move one")
        fourth = stamp(shared_repo)
        write(shared_repo, "adr/.gitignore", "*.log\n")
        git_out(shared_repo, "add", "adr/.gitignore")
        git_out(shared_repo, "commit", "-qm", "ignore logs")
        fifth = stamp(shared_repo)
        write(shared_repo, "adr/build.log", "ignored\n")
        write(shared_repo, "adr/0003.md", "untracked\n")
        # Staged and never committed: `ls-files` prints it after the
        # untracked file, and the listing puts it first by its path.
        write(shared_repo, "adr/0000-staged.md", "staged\n")
        git_out(shared_repo, "add", "adr/0000-staged.md")
        write(shared_repo, "adr/0001.md", "one, revised again\n")
        monkeypatch.chdir(shared_repo)
        code, text = dry_run(shared_repo, capfd, "--from", "adr")
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
        self, shared_repo, capfd, monkeypatch
    ):
        """#1054, round 1's finding 1: a merge whose conflict resolution
        rewrote a document is the commit that last changed it, since `git log`
        prints a merge's own change only under `--cc`."""
        item(shared_repo, "1700000001-a", op("add", "U", new="Rule."))
        stamps = merged_history(
            shared_repo,
            ("a decision", {"adr/0001.md": "one\n"}),
            ("side", {"adr/0001.md": "side\n"}),
            ("main", {"adr/0001.md": "main\n"}),
            ("merge side, resolved", {"adr/0001.md": "resolved\n"}),
        )
        first, merged = stamps["a decision"], stamps["merge side, resolved"]
        answered(monkeypatch, shared_repo, real={"git_fields"})
        monkeypatch.chdir(shared_repo)
        code, text = dry_run(shared_repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/0001.md  added {first}  last changed {merged}\n" in text, text

    def test_a_clean_merge_of_two_edits_is_a_documents_last_change(
        self, shared_repo, capfd, monkeypatch
    ):
        """#1054, round 4's finding 1: a merge with no conflict that combines
        two branches' edits to one document holds content neither parent
        holds. Its hunks are all ones `--cc` calls uninteresting, and
        `--name-status` still names it `MM`, so it is the last change."""
        item(shared_repo, "1700000001-a", op("add", "U", new="Rule."))
        body = "".join(f"line {i}\n" for i in range(30))
        side = body.replace("line 25\n", "line 25, side\n")
        main = body.replace("line 2\n", "line 2, main\n")
        both = side.replace("line 2\n", "line 2, main\n")
        stamps = merged_history(
            shared_repo,
            ("a decision", {"adr/0001.md": body}),
            ("side edits the end", {"adr/0001.md": side}),
            ("main edits the start", {"adr/0001.md": main}),
            ("merge side", {"adr/0001.md": both}),
        )
        first, merged = stamps["a decision"], stamps["merge side"]
        answered(monkeypatch, shared_repo, real={"git_fields"})
        monkeypatch.chdir(shared_repo)
        code, text = dry_run(shared_repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/0001.md  added {first}  last changed {merged}\n" in text, text

    def test_a_merge_that_wrote_a_document_no_parent_holds_adds_it(
        self, shared_repo, capfd, monkeypatch
    ):
        """#1054, round 2's finding 1: a merge whose result holds a document
        neither parent holds is the commit that added it, since `--cc` gives
        that path one `A` per parent and an add is every letter `A`."""
        item(shared_repo, "1700000001-a", op("add", "U", new="Rule."))
        stamps = merged_history(
            shared_repo,
            ("a decision", {"adr/0001.md": "one\n"}),
            ("side", {"adr/side.md": "side\n"}),
            ("main", {"adr/main.md": "main\n"}),
            (
                "merge side, adding adr/0002.md",
                {"adr/side.md": "side\n", "adr/0002.md": "written in the merge\n"},
            ),
        )
        merged = stamps["merge side, adding adr/0002.md"]
        answered(monkeypatch, shared_repo, real={"git_fields"})
        monkeypatch.chdir(shared_repo)
        code, text = dry_run(shared_repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/0002.md  added {merged}  last changed {merged}\n" in text, text

    def test_a_merge_that_rewrote_a_document_one_parent_lacks_changes_it(
        self, shared_repo, capfd, monkeypatch
    ):
        """#1054, round 2's finding 1: a merge that rewrites a document only
        `side` holds prints `AM` under `--cc`, an `A` against `main` beside an
        `M` against `side`. Not every letter is `A`, so the merge changed the
        document and `side`'s commit still added it."""
        item(shared_repo, "1700000001-a", op("add", "U", new="Rule."))
        stamps = merged_history(
            shared_repo,
            ("a decision", {"adr/0001.md": "one\n"}),
            ("side adds a document", {"adr/side.md": "side\n"}),
            ("main", {"adr/main.md": "main\n"}),
            (
                "merge side, rewriting adr/side.md",
                {"adr/side.md": "side, rewritten in the merge\n"},
            ),
        )
        added = stamps["side adds a document"]
        merged = stamps["merge side, rewriting adr/side.md"]
        answered(monkeypatch, shared_repo, real={"git_fields"})
        monkeypatch.chdir(shared_repo)
        code, text = dry_run(shared_repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/side.md  added {added}  last changed {merged}\n" in text, text

    def test_a_deletion_is_no_change_to_a_document_head_holds(
        self, shared_repo, capfd, monkeypatch
    ):
        """#1054, round 2's finding 1: a status whose letters are `D` says the
        commit took the path out of its tree, so it is neither an add nor a
        change. Here `main` changes a document, `side` deletes it, and the
        merge keeps `main`'s content, so `--cc` names nothing at the merge and
        `side`'s deletion, which the walk reads after `main`'s change, is not
        the document's last change."""
        item(shared_repo, "1700000001-a", op("add", "U", new="Rule."))
        stamps = merged_history(
            shared_repo,
            ("a decision", {"adr/0001.md": "one\n"}),
            ("side deletes it", {"adr/0001.md": None}),
            ("main revises it", {"adr/0001.md": "one, revised\n"}),
            ("merge side, keeping main's revision", {}),
        )
        first, revised = stamps["a decision"], stamps["main revises it"]
        answered(monkeypatch, shared_repo, real={"git_fields"})
        monkeypatch.chdir(shared_repo)
        code, text = dry_run(shared_repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/0001.md  added {first}  last changed {revised}\n" in text, text

    def test_a_file_under_two_named_directories_is_listed_once(
        self, shared_repo, capfd, monkeypatch
    ):
        """#1054 A3: `--from a` and `--from a/b` both hold `a/b/inner.md`, and
        it is listed once, under the first directory named that holds it;
        each path is read from the directory the command runs in."""
        item(shared_repo, "1700000001-a", op("add", "U", new="Rule."))
        write(shared_repo, "a/top.md", "top\n")
        write(shared_repo, "a/b/inner.md", "inner\n")
        commit_everything(shared_repo, "a")
        answered(monkeypatch, shared_repo, real={"git_fields"})
        monkeypatch.chdir(shared_repo / "a")
        code, text = dry_run(shared_repo, capfd, "--from", ".", "--from", "b")
        assert code == 0, text
        assert text.count("a/b/inner.md  ") == 1, text
        assert "\nfrom a/: 2 documents\n" in text, text
        assert "\nfrom a/b/: 0 documents\n" in text, text

    @pytest.mark.skipif(os.name == "nt", reason="`*` is no character of a name there")
    def test_a_named_directory_is_read_as_its_name_and_never_as_a_pattern(
        self, shared_repo, capfd, monkeypatch
    ):
        """#1573: `settle.py#git_fields` starts git through
        `lib/gitcmd.py#git` with `--literal-pathspecs`, so `--from 'a*'`
        lists the documents of the directory named `a*` and none of `ab`,
        which the name read as a pattern also matches. Seen red with the
        flag taken out of `git_fields`."""
        item(shared_repo, "1700000001-a", op("add", "U", new="Rule."))
        write(shared_repo, "a*/named.md", "named\n")
        write(shared_repo, "ab/matched.md", "matched\n")
        commit_everything(shared_repo, "a")
        answered(monkeypatch, shared_repo, real={"git_fields"})
        monkeypatch.chdir(shared_repo)
        code, text = dry_run(shared_repo, capfd, "--from", "a*")
        assert code == 0, text
        assert "\nfrom a*/: 1 document\n" in text, text
        assert "a*/named.md  " in text, text
        assert "ab/matched.md" not in text, text

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
        self, shared_repo, capfd, monkeypatch, tmp_path, where, given, said
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
        write(shared_repo, "adr/0001.md", "a decision\n")
        item(shared_repo, "1700000001-a", op("add", "U", new="Rule."))
        before = files(shared_repo)
        monkeypatch.chdir(shared_repo / where)
        code, text = dry_run(shared_repo, capfd, "--from", given)
        assert code == 2, text
        assert text.startswith(f"settle: --from {given} {said}"), text
        # The path the command read, which the person opens next.
        assert f" it reads as {os.path.abspath(given)} from " in text, text
        assert text.count("\n") == 1 and text.endswith(".\n"), text
        assert files(shared_repo) == before

    def test_refuses_from_beside_apply_and_removes_nothing(self, drawn, capfd):
        """#1054 A4: `--apply` removes only under `seal/threads/`, so a
        `--from` it accepted would read as one it acted on. The pair exits 2
        with one sentence naming both, and the released directory stays."""
        write(drawn, "adr/0001.md", "a decision\n")
        item(drawn, "1700000001-a", op("add", "U", new="Rule."))
        before = files(drawn)
        code, text = dry_run(drawn, capfd, "--apply", "--from", str(drawn / "adr"))
        assert code == 2, text
        assert text.startswith("settle: --from and --apply"), text
        assert text.count("\n") == 1 and text.endswith(".\n"), text
        assert files(drawn) == before
        assert specs_dir(drawn, "1700000001-a").is_dir()

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
        git_out(repo, "init", "-q")
        git_out(repo, "config", "user.email", "x@example.com")
        git_out(repo, "config", "user.name", "x")
        if committed:
            commit_everything(repo, "a decision")
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

    def test_a_named_directory_is_never_written(self, shared_repo, capfd, monkeypatch):
        """#1054 A6: the dry run with `--from`, then `--apply` removing a
        released work item, leave every file under the named directory with
        the path and the bytes it had, and its `git status` as it was. The
        readers but `git_fields`, which the listing reads, are `answered`."""
        answered(monkeypatch, shared_repo, real={"git_fields"})
        item(shared_repo, "1700000001-a", op("add", "U", new="Rule."))
        write(shared_repo, "adr/0001.md", "a decision\n")
        write(shared_repo, "adr/sub/0002.txt", "another\n")
        commit_everything(shared_repo, "a and its records")
        write(shared_repo, "adr/0001.md", "a decision, revised\n")
        write(shared_repo, "adr/0003.md", "untracked\n")

        def named():
            return {k: v for k, v in files(shared_repo).items() if k.startswith("adr")}

        def status():
            return git_out(
                shared_repo, "status", "--porcelain", "--untracked-files=all", "adr"
            )

        before, said = named(), status()
        code, text = dry_run(shared_repo, capfd, "--from", str(shared_repo / "adr"))
        assert code == 0, text
        code, text = apply(shared_repo, capfd)
        assert code == 0, text
        assert not specs_dir(shared_repo, "1700000001-a").exists(), text
        assert named() == before
        assert status() == said

    # --- `--draft`: the released operations written literally (#1217) --------

    def test_draft_writes_each_operation_in_merge_order_and_names_what_it_missed(
        self, shared_repo, capfd
    ):
        """S4 and S5. A was added before B and B's `change` quotes A's `to`,
        so only merge order leaves B's `to`, whatever their ids say. C's
        first `from` is not there: that operation is printed with its
        coordinate and reason, and C's next operation and D, after it, are
        placed. The run exits 0, writes only under the policy root, and
        leaves every released directory as it was."""
        item(shared_repo, "1700000009-a", op("change", "S", "old sentence.", "y."))
        commit_everything(shared_repo, "a")
        item(shared_repo, "1700000001-b", op("change", "S", "y.", "z."))
        commit_everything(shared_repo, "b")
        missed = op("change", "T", "gone words.", "w.")
        item(shared_repo, "1700000005-c", missed + "\n" + op("add", "T", new="Kept."))
        commit_everything(shared_repo, "c")
        item(shared_repo, "1700000002-d", op("add", "U", new="Rule."))
        commit_everything(shared_repo, "d")
        records = {k: v for k, v in files(shared_repo).items() if k.startswith("seal")}
        code, text = dry_run(shared_repo, capfd, "--draft")
        assert code == 0, text
        line = line_of(spec(missed), "- change")
        assert text == (
            "not placed  change  1700000005-c  "
            f"seal/threads/1700000005-c/frame/design.md:{line}  "
            "the `from` text is not in section `T` of docs/a.md\n"
            "placed 4 of 5 operations in docs/\n"
            f"{settle.DRAFTED}"
        ), text
        assert (shared_repo / "docs" / "a.md").read_text(encoding="utf-8") == (
            DOC.replace("old sentence.", "z.")
            .replace("T's text.\n", "T's text.\n\nKept.\n")
            .replace("Last.\n", "Last.\n\nRule.\n")
        )
        assert git(shared_repo, "status", "--porcelain").stdout == " M docs/a.md\n"
        assert {
            k: v for k, v in files(shared_repo).items() if k.startswith("seal")
        } == (records)

    def test_draft_creates_and_deletes_whole_documents(
        self, shared_repo, capfd, monkeypatch
    ):
        """An `add` with no section creates its document, and a `remove`
        that empties one deletes it. A document written with CRLF is read
        and written with its line ends as they are."""
        (shared_repo / "docs" / "b.md").write_bytes(
            b"## Only\r\n\r\nText.\r\n\r\n## Two\r\n"
        )
        write(shared_repo, "docs/c.md", "## Gone\n\nText.\n")
        item(
            shared_repo,
            "1700000001-a",
            "\n".join(
                [
                    op("add", new="# New", file="docs/new.md"),
                    op("remove", "Only", file="docs/b.md"),
                    op("remove", "Gone", file="docs/c.md"),
                ]
            ),
        )
        answered(monkeypatch, shared_repo)
        code, text = dry_run(shared_repo, capfd, "--draft")
        assert code == 0, text
        assert text.startswith("placed 3 of 3 operations in docs/\n"), text
        assert (shared_repo / "docs" / "new.md").read_bytes() == b"# New\n"
        assert (shared_repo / "docs" / "b.md").read_bytes() == b"## Two\r\n"
        assert not (shared_repo / "docs" / "c.md").exists()

    def test_draft_creates_the_policy_root_its_first_document_needs(
        self, shared_repo, capfd, monkeypatch
    ):
        """A repository whose policy root is absent gets it from the `add`
        that creates its first document."""
        shutil.rmtree(shared_repo / "docs")
        item(shared_repo, "1700000001-a", op("add", new="# New", file="docs/new.md"))
        answered(monkeypatch, shared_repo)
        code, text = dry_run(shared_repo, capfd, "--draft")
        assert code == 0, text
        assert (shared_repo / "docs" / "new.md").read_bytes() == b"# New\n"

    @pytest.mark.parametrize(
        "other", [["--apply"], ["--from", "adr"]], ids=["apply", "from"]
    )
    def test_refuses_draft_beside_apply_or_from_and_writes_nothing(
        self, drawn, capfd, other
    ):
        """S6: `--draft` writes the released operations and nothing else, so
        a flag beside it that it would ignore is refused with exit 2 and one
        sentence, and the tree is left as it was."""
        write(drawn, "adr/0001.md", "a decision\n")
        other = [str(drawn / "adr") if o == "adr" else o for o in other]
        before = files(drawn)
        code, text = dry_run(drawn, capfd, "--draft", *other)
        assert code == 2, text
        assert text.startswith("settle: --draft and " + other[0]), text
        assert text.count("\n") == 1 and text.endswith(".\n"), text
        assert files(drawn) == before

    def test_draft_in_local_mode_reads_the_design_under_the_git_directory(
        self, local_repo, capfd, monkeypatch
    ):
        """S7: the released design is read from its directory under the git
        directory, and the draft writes the repository's policy root."""
        local_item(local_repo, "1700000001-a", "feat/1-a", op("add", "U", new="Rule."))
        answered(monkeypatch, local_repo)
        records = sorted(p for p in (local_repo / ".git" / "seal").rglob("*"))
        code, text = dry_run(local_repo, capfd, "--draft")
        assert code == 0, text
        assert text.startswith("placed 1 of 1 operation in docs/\n"), text
        assert (local_repo / "docs" / "a.md").read_text(encoding="utf-8") == (
            DOC.replace("Last.\n", "Last.\n\nRule.\n")
        )
        assert sorted(p for p in (local_repo / ".git" / "seal").rglob("*")) == records


class Test_adding_commit:
    def test_accepts_the_oldest_add_of_each_path(self, tmp_path):
        """#1139. The root commit adds one fragment, and a settle's commit
        removes it and adds another with the same text, so each path names
        the pull request of its own add. What a person's `log.follow` and
        `log.showRoot` would change of this reading is held by
        `lib/gitcmd.py`, whose cases are `tests/lib/test_gitcmd.py`."""
        repo = tmp_path / "repo"
        first = "seal/threads/1700000001-first/changelog.md"
        second = "seal/threads/1700000002-second/changelog.md"
        write(repo, first, "- the same text\n")
        git_out(repo, "init", "-q", "-b", "main")
        git_out(repo, "config", "user.email", "x@example.com")
        git_out(repo, "config", "user.name", "x")
        commit_everything(repo, "the first work item (#1)")
        git_out(repo, "rm", "-q", first)
        write(repo, second, "- the same text\n")
        commit_everything(repo, "the settle (#2)")
        assert settle.adding_commit(str(repo), "HEAD", first)[1] == 1
        assert settle.adding_commit(str(repo), "HEAD", second)[1] == 2

    def test_refuses_a_number_the_subject_does_not_end_with_and_a_failed_git(
        self, shared_repo
    ):
        """#1139. A `(#N)` inside the subject is not the pull request's, so
        the adding commit names none. A path no commit adds has no adding
        commit. A ref `git` cannot read raises with what `git` said, so the
        release note's job stops rather than writing an entry with no link.
        Seen red with the subject's end anchor taken out, and with the check
        of `git`'s exit taken out."""
        path = "seal/threads/1700000001-a/changelog.md"
        write(shared_repo, path, "- a\n")
        added = commit_everything(shared_repo, "fix: (#7) is not where the title ends")
        assert settle.adding_commit(str(shared_repo), "HEAD", path) == (added, None)
        missing = "seal/threads/1700000002-none/changelog.md"
        assert settle.adding_commit(str(shared_repo), "HEAD", missing) == (None, None)
        with pytest.raises(RuntimeError, match="nosuch"):
            settle.adding_commit(str(shared_repo), "nosuch", path)


def tagged(repo):
    """`(first, second, third)`, three commits over REPO's base: an
    annotated `v1.2.3` and a `v1.0` of another shape on the first, a
    `v1.10.0` on the second and a `v0.0.1` on its tree, and nothing on the
    third."""
    held = []
    for name, tags in (
        ("a", [("-a", "-m", "annotated", "v1.2.3"), ("v1.0",)]),
        ("b", [("v1.10.0",), ("v0.0.1", "HEAD^{tree}")]),
        ("c", []),
    ):
        write(repo, f"{name}.txt", f"{name}\n")
        held.append(commit_everything(repo, name))
        for tag in tags:
            git_out(repo, "tag", *tag)
    return tuple(held)


class Test_versions:
    def test_accepts_the_lowest_version_tag_by_number_an_annotated_one_peeled(
        self, shared_repo
    ):
        """#1481, design *Scope* item 5. Each commit is labelled by the
        lowest `vX.Y.Z` tag that holds it, by number and not by text, an
        annotated tag read at the commit it peels to. Seen red with the peel
        of an annotated tag alone removed, with the tags walked highest
        first, and with the numbers compared as text."""
        first, second, _third = tagged(shared_repo)
        labels = settle.versions(str(shared_repo))
        assert labels[first] == "v1.2.3", labels
        assert labels[second] == "v1.10.0", labels

    def test_accepts_a_version_tag_of_a_tag_at_the_commit_it_peels_to(
        self, shared_repo
    ):
        """#1481, round 1, finding 1. A `vX.Y.Z` tag whose object is
        another tag labels the commit the chain peels to, as
        `git tag --contains` counts it, so that commit is not labelled by
        the next tag up. A git before 2.44 peels `%(*objectname)` of
        `for-each-ref` one level only, so this is seen red only with such a
        git first on PATH: with git 2.39.3 against the reading of
        `%(*objecttype)`."""
        write(shared_repo, "a.txt", "a\n")
        first = commit_everything(shared_repo, "a")
        git_out(shared_repo, "tag", "-a", "-m", "inner", "inner")
        git_out(shared_repo, "tag", "-a", "-m", "outer", "v0.1.0", "inner")
        write(shared_repo, "b.txt", "b\n")
        commit_everything(shared_repo, "b")
        git_out(shared_repo, "tag", "v0.2.0")
        assert settle.versions(str(shared_repo))[first] == "v0.1.0"

    def test_refuses_a_tag_of_another_shape_one_on_a_tree_and_an_untagged_commit(
        self, shared_repo
    ):
        """#1481, design *Scope* item 5. A tag of another shape, or one on
        a tree, labels nothing, and a commit no tag holds is not labelled.
        Seen red with a tag on a tree taken as a tip."""
        _first, _second, third = tagged(shared_repo)
        labels = settle.versions(str(shared_repo))
        assert third not in labels, labels
        assert set(labels.values()) == {"v1.2.3", "v1.10.0"}, labels


class Test_blobs:
    def test_accepts_each_names_text_in_order(self, shared_repo):
        """#1481, design *Scope* item 4. One `git cat-file --batch` gives
        each name's text in the order asked, as `git_out` decodes it, a line
        ending `\\r\\n` read as a newline. Seen red with the read past each
        object's text taken one byte short, and with the line endings left
        as git gave them."""
        (shared_repo / "crlf.md").write_bytes(b"one\r\ntwo\r\n")
        git_out(shared_repo, "config", "core.autocrlf", "false")
        commit_everything(shared_repo, "crlf")
        assert settle.blobs(str(shared_repo), ["HEAD:crlf.md", "HEAD:docs/a.md"]) == [
            ("one\ntwo\n", None),
            (DOC, None),
        ]

    def test_refuses_a_name_git_holds_no_text_for(self, shared_repo):
        """#1481, design *Scope* item 6. Where git holds no file's text at
        a name, the batch gives what it answered, `missing` or the kind of
        object it holds, and the names after it are still read. Seen red
        with the kind of object left unread."""
        assert settle.blobs(
            str(shared_repo), ["HEAD:docs", "HEAD:nope.md", "HEAD:docs/a.md"]
        ) == [(None, "tree"), (None, "missing"), (DOC, None)]


class Test_module:
    def test_merge_order_is_the_commit_that_adds_the_spec(self, shared_repo):
        """A work item's directory is born with its `routing.md`, often well
        before its `frame/design.md`; the order is the spec's, not the directory's."""
        early = specs_dir(shared_repo, "1700000001-a")
        early.mkdir(parents=True)
        (early / "routing.md").write_text("# a — routing\n", encoding="utf-8")
        commit_everything(shared_repo, "a is declared")
        item(shared_repo, "1700000002-b", op("add", "U", new="B."))
        commit_everything(shared_repo, "b")
        item(shared_repo, "1700000001-a", op("add", "U", new="A."))
        commit_everything(shared_repo, "a is framed")
        ids = ["1700000001-a", "1700000002-b"]
        found = [
            i for i, _ in rules.order(str(shared_repo), "HEAD", ids, "seal/threads")
        ]
        assert found == ["1700000002-b", "1700000001-a"], found

    def test_merge_order_of_an_id_that_is_not_ascii_is_its_designs_add(
        self, shared_repo
    ):
        """#1283. `rule_changes.py#order` reads the history with `-z`, so a
        design whose id git quotes under the default `core.quotePath` is
        placed by the commit that adds it, not last with no commit. Seen red
        against the reading without `-z`."""
        item(shared_repo, "1700000001-정렬", op("add", "U", new="A."))
        added = commit_everything(shared_repo, "a is framed")
        item(shared_repo, "1700000002-b", op("add", "U", new="B."))
        commit_everything(shared_repo, "b is framed")
        ids = ["1700000001-정렬", "1700000002-b"]
        found = rules.order(str(shared_repo), "HEAD", ids, "seal/threads")
        assert found[0] == ("1700000001-정렬", added), found
        assert [i for i, _ in found] == ids, found

    def test_merge_order_of_local_specs_is_their_merge_commits_place(self, shared_repo):
        """#955: no commit adds a local spec, so `rule_changes.py#merge_order`
        sorts `(id, merge commit)` pairs by each commit's place on the ref,
        whatever order they are handed in. A commit the ref does not reach
        comes last."""
        a = merge(shared_repo, "feat/1-a")
        b = merge(shared_repo, "feat/2-b")
        stray = "0" * 40
        pairs = [("1700000002-b", b), ("1700000003-c", stray), ("1700000001-a", a)]
        assert rules.merge_order(str(shared_repo), "HEAD", pairs) == [
            ("1700000001-a", a),
            ("1700000002-b", b),
            ("1700000003-c", stray),
        ]

    def test_merge_order_refuses_a_history_git_did_not_print(self, shared_repo):
        """#1573. `rule_changes.py#order` reads the merge order from the
        history git prints, and a git that exits non-zero printed none, so
        the read raises `lib/gitcmd.py#Exited` with git's line rather than
        placing every design last as added by no commit. Seen red against
        `rule_changes.py` before #1573, which read the empty output as the
        history."""
        item(shared_repo, "1700000001-a", op("add", "U", new="A."))
        commit_everything(shared_repo, "a is framed")
        with pytest.raises(gitcmd.Exited, match="no/such/ref"):
            rules.order(
                str(shared_repo), "no/such/ref", ["1700000001-a"], "seal/threads"
            )

    def test_merge_order_of_local_specs_refuses_a_history_git_did_not_print(
        self, shared_repo
    ):
        """#1573. `rule_changes.py#merge_order` raises `lib/gitcmd.py#Exited`
        where `git rev-list` exits non-zero, rather than sorting every pair
        as a commit the ref does not reach. Seen red against
        `rule_changes.py` before #1573."""
        a = merge(shared_repo, "feat/1-a")
        with pytest.raises(gitcmd.Exited, match="no/such/ref"):
            rules.merge_order(str(shared_repo), "no/such/ref", [("1700000001-a", a)])

    def test_a_ref_that_does_not_resolve_is_refused_rather_than_empty(self, tree_copy):
        """The quiet zero this is written against: a ref nothing can read makes
        every work item look unreleased, and the report would then say there is
        nothing to do."""
        assert settle.survey(str(tree_copy), "no/such/ref") is None

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
        # Which plans it reads by default, and the flag that reads the rest
        # (#1481).
        assert (
            "deleted by one of the two newest commits on `--released-at` that "
            "deleted a plan, or by any such commit under `--all-earlier`"
            in flat(settle.EARLIER_HEADING)
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
        "args", [["--root", "{root}"], ["--help"]], ids=["a-run", "help"]
    )
    def test_a_script_copied_alone_exits_2_and_names_what_it_misses(
        self, tmp_path, args
    ):
        """#590, and S4 of #1482. A copy of this script taken without its
        siblings exits 2, with the loader's one sentence naming the absent
        `lib/sibling.py` by its path: 2 means the input or the tree was
        unusable and nothing was read, and a sibling that is not beside the
        command is that kind. The sentence names no purpose (#1482). `--help` reaches the sentence too, because the guard stands at
        import and reads no argument (#1482, A13)."""
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
        lib = os.path.join(str(alone), "..", "..", "..", "lib", "sibling.py")
        said = settle.sibling.MISSING.format(path=os.path.normpath(lib))
        assert done.stderr == said + "\n", done.stderr

    def test_a_spec_moved_into_place_is_ordered_by_the_commit_that_moved_it(
        self, shared_repo
    ):
        """git reads a moved directory as a rename, never as an add, unless it is
        told not to; the spec would then have no place in the order, and be
        listed last with no commit, which the dry run marks unordered."""
        item(shared_repo, "1700000001-old", op("add", "U", new="Rule."))
        commit_everything(shared_repo, "old")
        git_out(
            shared_repo,
            "mv",
            "seal/threads/1700000001-old",
            "seal/threads/1700000002-new",
        )
        moved = commit_everything(shared_repo, "renamed")
        item(shared_repo, "1700000003-b", op("add", "U", new="B."))
        b = commit_everything(shared_repo, "b")
        ids = ["1700000003-b", "1700000002-new"]
        found = rules.order(str(shared_repo), "HEAD", ids, "seal/threads")
        assert found == [("1700000002-new", moved), ("1700000003-b", b)], found


class Test_threads:
    def test_accepts_the_threads_under_the_roots_own_name(self, tmp_path):
        """#688's D3: the walk of work items reads under the root's own
        directory, `threads/` in it.
        `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`
        classifies every shipped command by what keeps it off a reference
        root."""
        assert settle.threads(str(tmp_path / "seal")) == "seal/threads"

    def test_refuses_the_directory_holding_the_root_as_its_name(self, tmp_path):
        """A local root is named by its own directory, `seal`, and not by
        the common git directory holding it, under which its threads are
        read (`records_of`)."""
        local = tmp_path / ".git" / "seal"
        assert settle.threads(str(local)) == "seal/threads"


class Test_policy_root:
    def test_accepts_the_row_a_config_writes(self, tmp_path):
        d = _committed(
            tmp_path, {"seal/config.json": config_json(("Policy root", "rules"))}
        )
        assert settle.policy_root(str(d)) == "rules"

    def test_refuses_to_read_anything_but_docs_with_no_row(self, tmp_path):
        d = _committed(tmp_path, {"seal/config.json": config_json()})
        assert settle.policy_root(str(d)) == "docs"


class Test_show:
    def test_accepts_a_path_at_a_ref(self, plain):
        assert settle.show(str(plain), "HEAD", f"seal/threads/{WORK}/gaps.md") == memo(
            CANONICAL
        )

    def test_refuses_a_path_the_ref_does_not_hold(self, plain):
        assert settle.show(str(plain), "HEAD", "seal/threads/none/gaps.md") is None

    def test_refuses_to_raise_on_a_byte_that_is_not_utf8(self, tmp_path):
        """#19: a revision read at a ref decodes as `check_file` decodes the
        disk, U+FFFD for a byte UTF-8 cannot read, or one such byte aborts
        the whole read."""
        d = _committed(tmp_path, {"gaps.md": memo(CANONICAL)})
        path = d / "gaps.md"
        path.write_bytes(memo(CANONICAL).encode("utf-8") + b"| a \xff b | c |\n")
        commit_everything_as_e(d, "a byte that is not UTF-8")
        with open(path, encoding="utf-8", errors="replace") as handle:
            on_disk = handle.read()
        assert "�" in on_disk
        assert settle.show(str(d), "HEAD", "gaps.md") == on_disk


test_census = census_case(TARGET)
