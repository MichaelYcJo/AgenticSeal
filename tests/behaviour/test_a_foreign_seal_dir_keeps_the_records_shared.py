"""A repository whose own `seal/` is a package keeps its records shared,
under `agentic-seal/` (#1059).

Each case builds a repository whose `seal/` is a Python package with no
marker in its `README.md`, and runs a command of the plugin in it, in the
process. The cases are named by the scenario of the work item's
`frame/design.md` they hold: S1, first setup beside the package, S3, the
pull request's check, S4, the stamp, S5, every other check, and S6, moving
the root between its two places and carrying a copy to another clone. The
case of `seal pr-checks install`, which *Scope* item 6 names and no
scenario row holds, is named by its command. The resolver's order itself is
`tests/lib/test_optin.py`'s.
"""

import io
import json
import os
import shutil
import subprocess
import sys
import zipfile

import pytest
from conftest import (
    ROOT,
    V2,
    commit_everything_as_e,
    config_json,
    git,
    load_module,
    local_home,
    mark_root,
    pact,
    pact_config,
    parity_file,
    symlink_or_skip,
    write,
)
from test_pr_body import (
    EXPECTED,
    LANGUAGES,
    MANIFEST,
    MARK_LINE,
    OWN,
    manifest_of,
)
from test_pr_body import NAME as BODIED
from test_pr_body import PR as PR_BODY
from test_pr_body import RECORDS as BODY_RECORDS
from test_pr_body import ROW as MARK_ROW
from test_rules import HELD as RULES_HELD
from test_rules import TESTS as RULES_TESTS
from test_rules import doc as rules_doc
from test_rules import rule as rules_rule
from test_rules import rules as RULES
from test_seal import status, unanswered
from test_seal_stamp import ITEM_ID as STAMPED_ID
from test_seal_stamp import ITEM_NAME as STAMPED
from test_seal_stamp import closing_records, queued, routing_text
from test_seal_stamp import stamp as STAMP

SEAL = load_module(
    os.path.join(ROOT, "skills", "implement", "scripts", "seal.py"),
    "seal_beside_a_foreign_seal_dir",
)
CHAIN = load_module(
    os.path.join(ROOT, "skills", "code-review", "scripts", "chain_check.py"),
    "chain_check_beside_a_foreign_seal_dir",
)
UNVERIFIED = load_module(
    os.path.join(ROOT, "skills", "verify", "scripts", "unverified_check.py"),
    "unverified_check_beside_a_foreign_seal_dir",
)
PACT = load_module(
    os.path.join(ROOT, "skills", "verify", "scripts", "pact_check.py"),
    "pact_check_beside_a_foreign_seal_dir",
)

ITEM = "1794200000-a-work-item"
REMOTE = "git@example.com:org/thing.git"
# The project's own package, which no command of the plugin may write into.
PACKAGE = {
    "seal/__init__.py": "VERSION = 1\n",
    "seal/README.md": "# seal\n\nThis package's own notes.\n",
}
RECORDS = {
    "follow-up.md": "# follow-up\n",
    f"threads/{ITEM}/routing.md": "# routing\n",
}
# A committed config with no `Mode` key, which `seal mode` fills in.
MODELESS = config_json(("Record language", "English"))


def files_under(path):
    """{`/`-joined path: bytes} of every file under PATH, {} where there is
    none."""
    found = {}
    for directory, _dirs, names in os.walk(path):
        for name in names:
            full = os.path.join(directory, name)
            rel = os.path.relpath(full, path).replace(os.sep, "/")
            with open(full, "rb") as handle:
                found[rel] = handle.read()
    return found


def records_at(home):
    """HOME made a root holding RECORDS."""
    mark_root(home)
    for rel, text in RECORDS.items():
        write(home, rel, text)
    return home


@pytest.fixture
def package(tmp_path):
    """A repository on `main` whose committed `seal/` is the package, with
    REMOTE as `origin` and no root at either place."""
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    git(repo, "remote", "add", "origin", REMOTE)
    for rel, text in PACKAGE.items():
        write(repo, rel, text)
    commit_everything_as_e(repo, "the package")
    return repo


@pytest.fixture
def shared(package):
    """PACKAGE's repository with its root committed at `agentic-seal/`."""
    records_at(package / "agentic-seal")
    commit_everything_as_e(package, "the root")
    return package


def said(capsys, cwd, *argv):
    """(exit code, stdout) of `seal <argv>` run in CWD."""
    code = SEAL.main(list(argv), cwd=str(cwd))
    return code, capsys.readouterr().out


def test_s1_first_setup_beside_the_package_puts_the_shared_root_at_agentic_seal(
    package, capsys
):
    """`seal mode` with no root prints `agentic-seal` as the shared place,
    and a root made there from the template reads as shared mode, writes its
    key there, and passes `--check`, with the package as it was. Switched to
    local before anything is committed, it says nothing under it was
    tracked."""
    before = files_under(package / "seal")
    code, out = said(capsys, package, "mode")
    assert code == 1, out
    places = [line.split()[0] for line in out.splitlines() if "mode)" in line]
    assert places == [
        os.path.join(str(package), "agentic-seal"),
        os.path.join(str(package), ".git", "seal"),
    ], out

    os.makedirs(places[0])
    shutil.copyfile(
        os.path.join(ROOT, "templates", "setup", "seal-README.md"),
        os.path.join(places[0], "README.md"),
    )
    code, out = said(capsys, package, "mode")
    assert code == 0, out
    with open(os.path.join(places[0], "config.json"), encoding="utf-8") as handle:
        assert json.load(handle)["Mode"] == "shared"
    code, out = said(capsys, package, "mode", "--check")
    assert code == 0, out
    assert files_under(package / "seal") == before
    assert not any(line[3:].startswith("seal/") for line in status(package))
    code, out = said(capsys, package, "mode", "local")
    assert code == 0, out
    assert "  nothing under agentic-seal/ was tracked\n" in out, out


def test_s6_mode_moves_agentic_seal_under_the_git_directory_and_back(shared, capsys):
    """`seal mode local` moves `agentic-seal/` to the common directory's
    `seal/` and stages its removal, and `seal mode shared` moves it back to
    `agentic-seal/` and stages it, the package untouched both ways. The key
    `seal mode` wrote into the committed `agentic-seal/config.json` and an
    untracked file there do not stop the move, as they do not under `seal/`."""
    write(shared / "agentic-seal", "config.json", MODELESS)
    commit_everything_as_e(shared, "the config")
    assert said(capsys, shared, "mode")[0] == 0
    write(shared / "agentic-seal", "notes.md", "# notes\n")
    before = files_under(shared / "seal")
    # The bytes as `write` put them on disk, with this platform's line ends,
    # which the move must carry unchanged.
    written = files_under(shared / "agentic-seal")
    code, out = said(capsys, shared, "mode", "local")
    assert code == 0, out
    assert "note: agentic-seal/notes.md is untracked" in out
    assert not (shared / "agentic-seal").exists()
    local = files_under(shared / ".git" / "seal")
    for rel in RECORDS:
        assert local[rel] == written[rel], rel
    assert status(shared) and all(
        line.startswith("D  agentic-seal/") for line in status(shared)
    ), status(shared)
    assert "staged the removal of agentic-seal/ from the tree" in out

    commit_everything_as_e(shared, "the switch to local")
    code, out = said(capsys, shared, "mode", "shared")
    assert code == 0, out
    assert out.count("`git reset -- :/agentic-seal`") == 2, out
    assert not (shared / ".git" / "seal").exists()
    back = files_under(shared / "agentic-seal")
    # The config is the one file `seal mode shared` rewrites, so it is
    # compared by the key it wrote rather than by its bytes.
    assert json.loads(back.pop("config.json"))["Mode"] == "shared"
    local.pop("config.json")
    assert back == local
    assert status(shared) and all(
        line.startswith("A  agentic-seal/") for line in status(shared)
    ), status(shared)
    assert "staged agentic-seal/" in out
    assert files_under(shared / "seal") == before


@pytest.mark.parametrize(
    "held", ["a staged edit", "a submodule", "an index git cannot list"]
)
def test_s6_mode_refuses_to_move_agentic_seal_over_what_its_index_holds(
    shared, capsys, monkeypatch, held
):
    """The guards read the index under `agentic-seal/`, not under the
    package: a staged edit there, a submodule there, and an index git cannot
    list there each refuse the move and name the root by its own name."""
    if held == "a staged edit":
        write(shared / "agentic-seal", "follow-up.md", "# edited\n")
        git(shared, "add", "agentic-seal/follow-up.md")
    elif held == "a submodule":
        sha = git(shared, "rev-parse", "HEAD").stdout.strip()
        gitlink = f"160000,{sha},agentic-seal/vendor"
        git(shared, "update-index", "--add", "--cacheinfo", gitlink)
    else:
        tail = ["--stage", "--", "agentic-seal"]
        unanswered(monkeypatch, tail, OSError("git is not here"))
    code, out = said(capsys, shared, "mode", "local")
    assert code == 1, out
    assert out.rstrip().endswith("Nothing was moved."), out
    if held == "a staged edit":
        assert "\n  M  agentic-seal/follow-up.md\n" in out, out
    elif held == "a submodule":
        assert "there is a submodule under agentic-seal/:\n" in out, out
        assert "`git rm -r --cached agentic-seal`" in out, out
    else:
        assert "whether there is a submodule under agentic-seal/ could not" in out
    assert (shared / "agentic-seal").is_dir()


@pytest.mark.parametrize("wanted", ["local", "shared"])
def test_s6_a_switch_that_could_not_stage_names_agentic_seal_in_the_command(
    shared, capsys, wanted
):
    """Where git refuses the staging step, the command the line hands the
    person stages `agentic-seal`: a held `index.lock` going local, and an
    ignore rule over the root going shared."""
    lock = shared / ".git" / "index.lock"
    if wanted == "shared":
        assert said(capsys, shared, "mode", "local")[0] == 0
        write(shared, ".gitignore", "agentic-seal/\n")
        commit_everything_as_e(shared, "the switch to local")
    else:
        lock.write_text("", encoding="utf-8")
    try:
        code, out = said(capsys, shared, "mode", wanted)
    finally:
        if lock.exists():
            lock.unlink()
    assert code == 0, out
    if wanted == "local":
        assert "Run `git rm -r --cached :/agentic-seal` yourself" in out, out
    else:
        assert "  agentic-seal/ could NOT be staged: " in out, out
        assert "`git add -f :/agentic-seal` yourself" in out, out


def test_pr_checks_install_writes_the_workflow_beside_a_shared_agentic_seal(
    shared, capsys
):
    """`seal pr-checks install` reads a marked `agentic-seal/` as the root in
    the tree, so it writes the workflow and stages it, where a project's own
    `seal/` alone would refuse it."""
    code, out = said(capsys, shared, "pr-checks", "install")
    assert code == 0, out
    assert (shared / ".github" / "workflows" / "hygiene.yml").is_file()
    assert "A  .github/workflows/hygiene.yml" in status(shared)


def test_pr_checks_install_names_agentic_seal_where_no_root_stands_beside_the_package(
    package, capsys
):
    """With no root beside the package, `seal pr-checks install` writes
    nothing and names the place it looked by its own name, `agentic-seal/`,
    not the package's `seal/`, which stands in the tree."""
    code, out = said(capsys, package, "pr-checks", "install")
    assert code == 1, out
    assert "no root stands at agentic-seal/ in this tree" in out, out
    assert not (package / ".github").exists()


def test_s6_export_in_shared_mode_names_agentic_seal_in_the_way_out(shared, capsys):
    """`seal export` writes no zip in shared mode, and the commands it gives
    for going local take `agentic-seal/` out of the tree, not the package."""
    code, out = said(capsys, shared, "export")
    assert code == 1, out
    assert (
        '  git rm -r --cached "$(git rev-parse --show-toplevel)/agentic-seal"\n'
        '  mv "$(git rev-parse --show-toplevel)/agentic-seal" '
        '"$(git rev-parse --git-common-dir)/seal"\n'
    ) in out


def test_s6_a_copy_travels_as_seal_and_lands_under_agentic_seal(
    package, capsys, tmp_path
):
    """`seal export` from the local root writes members named `seal/…`, the
    archive's own name, and `seal import --into shared` in a fresh clone
    writes them under `agentic-seal/`, leaving the package as it was."""
    # The bytes as `write` put them on disk, with this platform's line ends,
    # which the export and the import must carry unchanged.
    written = files_under(records_at(local_home(package)))
    zips = tmp_path / "zips"
    zips.mkdir()
    code, out = said(capsys, package, "export", "--output", str(zips))
    assert code == 0, out
    (archive,) = zips.iterdir()
    with zipfile.ZipFile(archive) as opened:
        names = sorted(opened.namelist())
    assert names == sorted(
        ["manifest.json", "seal/README.md", *(f"seal/{rel}" for rel in RECORDS)]
    )

    clone = tmp_path / "clone"
    git(tmp_path, "clone", "-q", str(package), str(clone))
    git(clone, "remote", "set-url", "origin", REMOTE)
    before = files_under(clone / "seal")
    code, out = said(capsys, clone, "import", str(archive), "--into", "shared")
    assert code == 0, out
    landed = files_under(clone / "agentic-seal")
    for rel in RECORDS:
        assert landed[rel] == written[rel], rel
    assert files_under(clone / "seal") == before


@pytest.mark.parametrize(
    "held, said_of_it",
    [("a link", "is a symbolic link"), ("a file", "is not a directory")],
)
def test_s6_an_import_names_what_blocks_it_in_the_root_by_the_roots_own_name(
    package, capsys, tmp_path, held, said_of_it
):
    """A symbolic link, or a file, where the zip needs `threads/` as a
    directory is refused, and the line names the place in this clone,
    `agentic-seal/threads`, not the archive's `seal/` prefix."""
    records_at(local_home(package))
    zips = tmp_path / "zips"
    zips.mkdir()
    assert said(capsys, package, "export", "--output", str(zips))[0] == 0
    (archive,) = zips.iterdir()
    root = package / "agentic-seal"
    mark_root(root)
    shutil.rmtree(package / ".git" / "seal")
    outside = tmp_path / "outside"
    outside.mkdir()
    if held == "a link":
        symlink_or_skip(str(outside), str(root / "threads"))
    else:
        write(root, "threads", "a file\n")
    code, out = said(capsys, package, "import", str(archive))
    assert code == 1, out
    assert out.startswith(f"agentic-seal/threads in this clone {said_of_it}"), out
    assert list(outside.iterdir()) == []


# --- S3: the pull request's check -------------------------------------------

DECLARED = "agentic-seal/threads/1794200001-a-declared-item"
# A declaration naming `feature`, straight to the pull request, so the
# check's guarantee arm names its missing `guarantee.md` once it is judged.
DECLARATION = (
    "| Axis | Answer |\n|---|---|\n| Review | straight to the PR |\n"
    "| Destination | open the pull request |\n| Planning | the session |\n"
    "| Branch | feature |\n"
)
NO_GUARANTEE = f"{DECLARED}/guarantee.md:0  git carries no guarantee file"


@pytest.fixture
def declared(shared, tmp_path, monkeypatch):
    """SHARED with DECLARATION committed on `main` under `agentic-seal/`,
    and `feature` checked out from it, which the check reads as a ready pull
    request."""
    write(shared, f"{DECLARED}/routing.md", DECLARATION)
    commit_everything_as_e(shared, "the declaration")
    git(shared, "switch", "-qc", "feature")
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    return shared


def checked(capsys, repo):
    """(exit code, stdout) of `chain_check.py` run on REPO against `main`."""
    code = CHAIN.main(["--baseline", "main", "--root", str(repo)])
    return code, capsys.readouterr().out


@pytest.mark.parametrize("removed", [None, "agentic-seal/README.md"])
def test_s3_the_check_judges_the_declaration_under_agentic_seal(
    declared, capsys, removed
):
    """The declaration naming the branch under `agentic-seal/threads/` is
    judged, and so it stays where the pull request deletes only the
    marker: the merge base's root is still an entry at HEAD."""
    write(declared, "docs/a.md", "# a\n")
    if removed:
        git(declared, "rm", "-q", removed)
    commit_everything_as_e(declared, "the change")
    code, out = checked(capsys, declared)
    assert code == 1, out
    assert NO_GUARANTEE in out, out
    assert "so nothing is declared" not in out, out


@pytest.mark.parametrize("outside", [True, False], ids=["the package", "records"])
def test_s3_a_change_to_the_package_reaches_outside_the_document_roots(
    declared, capsys, outside
):
    """With the migration config at `agentic-seal/parity.json`, a change to
    the package's `seal/__init__.py` owes the comparison, so the config's
    placeholder baseline is refused; a change confined to `agentic-seal/`
    owes none."""
    write(declared, "agentic-seal/parity.json", parity_file(None))
    write(declared, "agentic-seal/follow-up.md", "# follow-up, again\n")
    if outside:
        write(declared, "seal/__init__.py", "VERSION = 2\n")
    commit_everything_as_e(declared, "the change")
    _code, out = checked(capsys, declared)
    refused = [ln for ln in out.splitlines() if ln.startswith("agentic-seal/parity")]
    if outside:
        (line,) = refused
        assert line.startswith("agentic-seal/parity.json:0  "), line
        assert "`Baseline commit`" in line, line
    else:
        assert refused == [], out


def test_s3_an_earlier_releases_parity_md_under_agentic_seal_is_refused_there(
    declared, capsys
):
    """#1454 beside #1059: an `agentic-seal/parity.md` git carries with no
    `agentic-seal/parity.json` beside it is refused once, at its path under
    the root's own name, naming the file to write, where a change reaches
    the package. Red with `chain_check.py#originals_of` reading the old
    file at `optin.HOME`."""
    write(declared, "agentic-seal/parity.md", "# Migration config\n")
    write(declared, "seal/__init__.py", "VERSION = 2\n")
    commit_everything_as_e(declared, "the change")
    _code, out = checked(capsys, declared)
    refused = [ln for ln in out.splitlines() if ln.startswith("agentic-seal/parity")]
    (line,) = refused
    assert line.startswith("agentic-seal/parity.md:0  "), line
    assert "agentic-seal/parity.json" in line, line


def test_s3_a_design_the_pull_request_edits_under_agentic_seal_is_read(
    declared, capsys
):
    """Another work item's `frame/design.md` the pull request adds under
    `agentic-seal/threads/` is read by the rule-changes arm, which refuses
    its section: a line continued past the field's one line."""
    other = "agentic-seal/threads/1794200002-another-item"
    write(
        declared,
        f"{other}/frame/design.md",
        "# spec\n\n## Rule changes\n\n"
        "- nothing\n  why: a reason\n  that continues two spaces in\n\n"
        "Framed 2026-11-09 by framer, before the build.\n",
    )
    commit_everything_as_e(declared, "another work item's design")
    _code, out = checked(capsys, declared)
    assert any(ln.startswith(f"{other}/frame/design.md:") for ln in out.splitlines())


@pytest.mark.parametrize("package_left", [False, True], ids=["kept", "removed"])
def test_s3_the_pull_request_that_adds_agentic_seal_is_judged_under_it(
    package, tmp_path, monkeypatch, capsys, package_left
):
    """A merge base with no root reads under the name HEAD gives, so the
    pull request that adds `agentic-seal/` has its declaration judged,
    and so it does where the same pull request takes the package's `seal/`
    out of the tree."""
    git(package, "switch", "-qc", "feature")
    mark_root(package / "agentic-seal")
    write(package, f"{DECLARED}/routing.md", DECLARATION)
    if package_left:
        git(package, "rm", "-rq", "seal")
    commit_everything_as_e(package, "the root")
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    code, out = checked(capsys, package)
    assert code == 1, out
    assert NO_GUARANTEE in out, out


def test_s3_a_branch_nothing_declares_is_told_to_add_it_under_agentic_seal(
    shared, capsys
):
    """With no declaration naming the branch, the check names the place it
    searched and the file to add by the root's own name."""
    git(shared, "switch", "-qc", "feature")
    write(shared, "docs/a.md", "# a\n")
    commit_everything_as_e(shared, "the change")
    code, out = checked(capsys, shared)
    assert code == 0, out
    assert (
        "Nothing git carries under `agentic-seal/threads/` declares `feature`. "
        "Add agentic-seal/threads/<work-item>/routing.md to declare."
    ) in out, out


@pytest.mark.parametrize("worktree", [False, True], ids=["HEAD", "--worktree"])
def test_s3_a_pull_request_deleting_agentic_seal_declares_nothing(
    declared, capsys, worktree
):
    """The pull request that takes `agentic-seal/` out of the tree deletes
    the declaration with it, and the package's `seal/` standing at HEAD is
    not the root that stayed. Under `--worktree` the deletion, staged and
    not committed, reads the same."""
    git(declared, "rm", "-rq", "agentic-seal")
    if worktree:
        code = CHAIN.main(["--baseline", "main", "--root", str(declared), "--worktree"])
        out = capsys.readouterr().out
    else:
        commit_everything_as_e(declared, "the root leaves the tree")
        code, out = checked(capsys, declared)
    assert code == 0, out
    assert (
        "the tree the check reads has no top-level `agentic-seal` entry, so "
        "nothing is declared"
    ) in out, out
    assert NO_GUARANTEE not in out, out


# --- S4: the stamp -----------------------------------------------------------


def test_s4_the_stamp_queues_a_sealed_guarantee_under_agentic_seal(package, capsys):
    """`seal stamp --guarantee` given `agentic-seal/threads/<id>/guarantee.md`,
    written and not yet committed, queues the work item's stamp in the
    clone, as it does under `seal/`."""
    mark_root(package / "agentic-seal")
    commit_everything_as_e(package, "the root")
    git(package, "switch", "-qc", "feat/x")
    write(package, "work.txt", "the work\n")
    commit_everything_as_e(package, "the work")
    target = git(package, "rev-parse", "--short", "HEAD").stdout.strip()
    base = git(package, "rev-parse", "--short", "main").stdout.strip()
    item = package / "agentic-seal" / "threads" / STAMPED
    closing_records(item, target, base)
    write(item, "routing.md", routing_text())
    code = STAMP.main(["--guarantee", str(item / "guarantee.md")])
    out = capsys.readouterr().out
    assert code == 0, out
    assert out.startswith(f"agentic: the stamp for {STAMPED_ID} is queued in "), out
    assert len(queued(package / ".git")) == 1


# --- S5: every other check ---------------------------------------------------


def test_s5_pr_body_check_reads_the_seal_and_the_records_under_agentic_seal(
    package, tmp_path, monkeypatch, capsys
):
    """`seal pr-body` reads the keys of `agentic-seal/config.json` and a
    guarantee sealed at the commit before its own, so the body carries the
    mark and names the records where they stand; `--check` on that body
    exits 0. A refusal names the record by its path under `agentic-seal/`."""
    git(package, "switch", "-qc", "feature")
    home = mark_root(package / "agentic-seal")
    write(home, "config.json", config_json(*LANGUAGES, *MARK_ROW))
    item = home / "threads" / BODIED
    for rel, text in BODY_RECORDS.items():
        write(item, rel, text)
    (item / "pr.md").write_bytes(OWN.encode("utf-8"))
    sha = commit_everything_as_e(package, "the build")
    write(
        item,
        "guarantee.md",
        f"# Guarantee: {BODIED}\n\n```seal\ntarget: {sha} against main\n"
        "Verdict: sealed\n```\n",
    )
    commit_everything_as_e(package, "the seal")
    monkeypatch.setattr(PR_BODY, "MANIFEST", manifest_of(tmp_path, MANIFEST))
    monkeypatch.chdir(package)
    body = tmp_path / "pr-body.md"
    assert PR_BODY.main([str(item), "--body", str(body)]) == 0
    marked = EXPECTED.replace(
        "## From the records\n\n", f"## From the records\n\n{MARK_LINE}\n\n", 1
    ).replace(f" seal/threads/{BODIED}/ ", f" agentic-seal/threads/{BODIED}/ ", 1)
    assert body.read_bytes() == (OWN + marked).encode("utf-8")
    capsys.readouterr()
    assert PR_BODY.main([str(item), "--body", str(body), "--check"]) == 0
    assert "seal pr-body:" not in capsys.readouterr().out
    (item / "pr.md").unlink()
    for check in (["--check"], []):
        assert PR_BODY.main([str(item), "--body", str(body), *check]) == 1
        assert capsys.readouterr().out.startswith(
            f"refused: agentic-seal/threads/{BODIED}/pr.md: is not there"
        )


def tool(cwd, name, *args):
    """(exit code, stdout, stderr) of the script `seal <name>` hands over to,
    run in CWD on this interpreter, as a person types it there."""
    done = subprocess.run(
        [sys.executable, os.path.join(ROOT, SEAL.TOOLS[name][0]), *args],
        cwd=str(cwd),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    return done.returncode, done.stdout, done.stderr


def configured(home, *pairs):
    """HOME's `config.json` holding PAIRS, each `(key, value)`."""
    write(home, "config.json", config_json(*pairs))


def test_s5_gate_reads_its_key_from_agentic_seal_and_names_it_where_none_is(
    package, tmp_path
):
    """`seal gate --preflight` with no root names `<repo>/agentic-seal` as
    the shared place a root would stand, not the package's `seal/`; with
    the root there, it reads the `Broad gate` key of `agentic-seal/config.json`."""
    top = os.path.realpath(package)
    code, _out, err = tool(package, "gate", "--base", "main", "--preflight")
    assert code == 2, err
    shared = os.path.join(top, "agentic-seal")
    assert f"at either place a root lives (`{shared}`, `" in err, err
    command = f"{sys.executable} -c pass"
    configured(records_at(package / "agentic-seal"), ("Broad gate", command))
    commit_everything_as_e(package, "the root")
    _code, _out, err = tool(package, "gate", "--base", "main", "--preflight")
    assert f"seal gate: `Broad gate` says: {command} — read, and not run" in err, err


def test_s5_rules_check_excuses_a_section_a_design_under_agentic_seal_removes(
    shared, capsys
):
    """`seal rules --check` reads the designs under `agentic-seal/threads/`
    and the `Policy root` key of `agentic-seal/config.json`: a refused `check:`
    line in a section a design there removes is excused and named by its
    path under the root."""
    configured(shared / "agentic-seal", ("Policy root", "policy"))
    write(shared, RULES_HELD, RULES_TESTS)
    write(shared, "policy/a.md", rules_doc(rules_rule("check: tests/test_gone.py")))
    write(
        shared / "agentic-seal" / "threads" / ITEM,
        "frame/design.md",
        "# Design\n\n## Rule changes\n\n- remove\n  file: policy/a.md\n"
        "  section: The heading\n",
    )
    code = RULES.main(["--check", "--root", str(shared)])
    out = capsys.readouterr().out
    assert code == 0, out
    assert (
        "seal rules: excused: policy/a.md:6: The heading: tests/test_gone.py does "
        f"not exist; agentic-seal/threads/{ITEM}/ removes this section at the "
        "settle\n"
    ) in out, out


@pytest.mark.parametrize("state", ["unwritten", "settled", "absent"])
def test_s5_unverified_reads_agentic_seal_threads_as_the_roots_own(
    shared, capsys, monkeypatch, state
):
    """`seal unverified agentic-seal/threads` reads the root's own `threads/`:
    work items with no `gaps.md` are unwritten, none is a finished settle,
    and with the root out of the tree there is nothing declared. Each exits
    0, where a path read as a typo exits 2."""
    said_of_it = {
        "unwritten": "holds work items and none of them carries an `gaps.md`",
        "settled": "holds no work item and its `seal/` root is there",
        "absent": "has no `seal/` root in this tree, so nothing here is declared",
    }[state]
    if state == "settled":
        shutil.rmtree(shared / "agentic-seal" / "threads" / ITEM)
    elif state == "absent":
        shutil.rmtree(shared / "agentic-seal")
    monkeypatch.chdir(shared)
    code = UNVERIFIED.main(["agentic-seal/threads"])
    out = capsys.readouterr().out
    assert code == 0, out
    assert out.startswith(f"seal unverified: agentic-seal/threads {said_of_it}"), out


def test_s5_unverified_walks_agentic_seal_and_passes_over_the_packages_specs(
    shared, capsys, monkeypatch
):
    """`seal unverified .` reads the closing memo under `agentic-seal/` and
    takes the package's `seal/vendor/specs/` for what it is beside a root
    of the second name, a directory named `specs` outside the root, which
    no `Reference specs` key keeps and the walk passes over: its memo,
    which does not read, is never opened."""
    write(
        shared / "agentic-seal" / "threads" / ITEM,
        "gaps.md",
        "# overview\n\n## Not verified\n\n- nothing\n  why: nothing to verify\n",
    )
    write(
        shared,
        "seal/vendor/specs/1794200003-theirs/gaps.md",
        "# theirs\n\n## Not verified\n\nnot a table, and not a none line either\n",
    )
    monkeypatch.chdir(shared)
    code = UNVERIFIED.main(["."])
    out = capsys.readouterr().out
    assert code == 0, out
    assert "\n1 closing memos · 0 open · 0 closed · 0 unreadable\n" in out, out


def test_s5_settle_shows_a_work_item_released_under_agentic_seal(shared):
    """`seal settle`'s dry run reads the work items under
    `agentic-seal/threads/` as the shared root's, released where `main`
    holds them, and names each by its path there."""
    code, out, err = tool(shared, "settle", "--released-at", "main")
    assert code == 0, err
    assert f"agentic-seal/threads/{ITEM}/" in out, out
    assert "local mode" not in out, out


def test_s5_pact_names_the_signers_key_under_agentic_seal(shared, tmp_path):
    """`seal pact` reads `agentic-seal/pact.md` and the `Pact signers` key of
    `agentic-seal/config.json`, and names the config by that path: a key
    that lists the pact's own repository is refused at it."""
    write(shared / "agentic-seal", "pact.md", pact(V2))
    write(shared / "agentic-seal", "config.json", pact_config(REMOTE))
    commit_everything_as_e(shared, "the pact")
    out = io.StringIO()
    code = PACT.check(str(shared), out=out, home_dir=str(tmp_path))
    assert code == 2, out.getvalue()
    assert (
        f"REFUSED {REMOTE} agentic-seal/config.json — the `Pact signers` key "
        "lists the pact's own repository"
    ) in out.getvalue(), out.getvalue()


def test_s5_fold_reads_its_keys_from_agentic_seal(shared):
    """`seal fold` reads `Policy root` and `Document token ceiling` from
    `agentic-seal/config.json`, so the documents it holds to the ceiling are
    the ones under the root that key names."""
    configured(
        shared / "agentic-seal",
        ("Policy root", "policy"),
        ("Document token ceiling", "1"),
    )
    write(shared, "policy/a.md", "# A\n")
    code, out, err = tool(shared, "fold")
    assert code == 0, err
    assert "policy/a.md is about 2 tokens, past the ceiling of 1" in out, out
