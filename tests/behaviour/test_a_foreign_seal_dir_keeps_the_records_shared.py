"""A repository whose own `seal/` is a package keeps its records shared,
under `agentic-seal/` (#1059).

Each case builds a repository whose `seal/` is a Python package with no
marker in its `README.md`, and runs a command of the plugin in it, in the
process. The cases are named by the scenario of the work item's
`frame/design.md` they hold: S1, first setup beside the package, and S6,
moving the root between its two places and carrying a copy to another
clone. The resolver's order itself is `tests/lib/test_optin.py`'s.
"""

import os
import shutil
import zipfile

import pytest
from conftest import (
    ROOT,
    commit_everything_as_e,
    git,
    load_module,
    local_home,
    mark_root,
    symlink_or_skip,
    write,
)
from test_seal import status

SEAL = load_module(
    os.path.join(ROOT, "skills", "implement", "scripts", "seal.py"),
    "seal_beside_a_foreign_seal_dir",
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
# A committed config with no `Mode` row, which `seal mode` fills in.
ROWLESS = "# Repository config\n\n| Item | Value |\n|---|---|\n| Record language | English |\n"


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
    row there, and passes `--check`, with the package as it was."""
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
    with open(os.path.join(places[0], "config.md"), encoding="utf-8") as handle:
        assert "| Mode | shared |" in handle.read()
    code, out = said(capsys, package, "mode", "--check")
    assert code == 0, out
    assert files_under(package / "seal") == before
    assert not any(line[3:].startswith("seal/") for line in status(package))


def test_s6_mode_moves_agentic_seal_under_the_git_directory_and_back(shared, capsys):
    """`seal mode local` moves `agentic-seal/` to the common directory's
    `seal/` and stages its removal, and `seal mode shared` moves it back to
    `agentic-seal/` and stages it, the package untouched both ways. The row
    `seal mode` wrote into the committed `agentic-seal/config.md` and an
    untracked file there do not stop the move, as they do not under `seal/`."""
    write(shared / "agentic-seal", "config.md", ROWLESS)
    commit_everything_as_e(shared, "the config")
    assert said(capsys, shared, "mode")[0] == 0
    write(shared / "agentic-seal", "notes.md", "# notes\n")
    before = files_under(shared / "seal")
    code, out = said(capsys, shared, "mode", "local")
    assert code == 0, out
    assert "note: agentic-seal/notes.md is untracked" in out
    assert not (shared / "agentic-seal").exists()
    local = files_under(shared / ".git" / "seal")
    assert local[f"threads/{ITEM}/routing.md"] == b"# routing\n"
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
    assert back.pop("config.md").endswith(b"| Mode | shared |\n")
    local.pop("config.md")
    assert back == local
    assert status(shared) and all(
        line.startswith("A  agentic-seal/") for line in status(shared)
    ), status(shared)
    assert "staged agentic-seal/" in out
    assert files_under(shared / "seal") == before


@pytest.mark.parametrize("held", ["a staged edit", "a submodule"])
def test_s6_mode_refuses_to_move_agentic_seal_over_what_its_index_holds(
    shared, capsys, held
):
    """The guards read the index under `agentic-seal/`, not under the
    package: a staged edit there, and a submodule there, each refuse the
    move and name the root by its own name."""
    if held == "a staged edit":
        write(shared / "agentic-seal", "follow-up.md", "# edited\n")
        git(shared, "add", "agentic-seal/follow-up.md")
    else:
        sha = git(shared, "rev-parse", "HEAD").stdout.strip()
        gitlink = f"160000,{sha},agentic-seal/vendor"
        git(shared, "update-index", "--add", "--cacheinfo", gitlink)
    code, out = said(capsys, shared, "mode", "local")
    assert code == 1, out
    assert out.rstrip().endswith("Nothing was moved."), out
    if held == "a staged edit":
        assert "\n  M  agentic-seal/follow-up.md\n" in out, out
    else:
        assert "there is a submodule under agentic-seal/:\n" in out, out
        assert "`git rm -r --cached agentic-seal`" in out, out
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
    records_at(local_home(package))
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
    assert landed[f"threads/{ITEM}/routing.md"] == b"# routing\n"
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
