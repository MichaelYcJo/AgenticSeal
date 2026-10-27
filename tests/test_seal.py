"""`skills/implement/scripts/seal.py`, one class per function.

Rebuilt by #942's phase 5 from `tests/test_the_records_can_be_carried_out_and_in.py`
and `tests/test_the_mode_is_a_row_and_a_command.py`. `seal` carries a clone's
`seal/` root to another clone (`export`, `import`), moves it between the
two places it can live (`mode`), and writes or removes the pull-request
checks (`pr-checks`).

The units that read a name, a zip, a file or a config text run in the
process on a case's own directory, with no git. The commands run through
`main` in the process over worlds built once for the module: a local-mode
clone holding one work item and an `origin`, a shared-mode clone whose root
is committed, a second local-mode clone to import into, a clone with no
root, a clone with no commit, and two shared-mode clones each holding a
submodule, one under the root and one beside it. One zip, exported once
from the first world, is what every import reads. A case that writes into a
world takes a copy of it, and the copy is the reset. No world holds a file a
case runs, so a copy is a plain copy.

#942's phase 6 placed here the writer's cases of
`tests/test_the_mode_question_is_asked_once.py`, which hold `write_row` and
`with_row` to the reader they share a table with, and the two cases of
`seal.py`'s re-exports of that reader, from that file and from
`tests/test_a_signer_declares_its_pact.py`. Each loads the module under a
name of its own, as its old file did. Its round 9 fix pass placed in
`Test_refuse_without_hooks` the three rows that run a copy of this script
without `hooks/`, from `tests/test_a_script_copied_alone_exits_2.py`, a case
of this module alone.
"""

import datetime
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import types
import zipfile

import config_shapes
import pytest
from conftest import (
    FENCED_ABOVE,
    FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN,
    FENCED_REFUSAL,
    PIPED_TABLE,
    ROOT,
    ROOT_MARKER,
    UNDER_THE_COMMENT,
    census_case,
    commit_everything_as_e,
    crlf,
    fifo_or_skip,
    git,
    git_out,
    load_hook_module,
    load_module,
    local_home,
    mark_root,
    names_path,
    shape_text,
    staged,
    symlink_or_skip,
    write,
    write_config,
)

TARGET = "skills/implement/scripts/seal.py"

SEAL = load_module(os.path.join(ROOT, *TARGET.split("/")), "seal_under_test")
OPTIN = load_hook_module("optin.py", "optin_for_seal_cases")

ITEM = "1788000000-a-work-item"
SSH = "git@example.com:org/thing.git"
HTTPS = "https://example.com/org/thing"
ELSEWHERE = "git@example.com:org/somewhere-else.git"
RECORDS = {
    "README.md": ROOT_MARKER + "\n",
    "follow-up.md": "# follow-up\n",
    f"threads/{ITEM}/plan.md": "# rows\n",
    f"threads/{ITEM}/routing.md": "# routing\n",
    f"threads/{ITEM}/design.md": "# spec\n",
}
MEMBERS = ["manifest.json", *(f"seal/{rel}" for rel in sorted(RECORDS))]
# The import's last line: a collided pair is a reading for a person.
CLOSING = (
    "Which of a collided pair is right is a reading, not a merge — this "
    "command overwrites nothing."
)
# Session state that sits beside the root under the common git directory.
# None may be in a zip, and a new file beside the root joins the list.
BESIDE_THE_ROOT = (
    "agentic-implementer",
    "agentic-planner",
    "agentic-no-work-item",
    "agentic-stamp-refused",
    "agentic-last-export.json",
    "agentic-session-lease",
)
WORKFLOW_PATH = os.path.join(".github", "workflows", "hygiene.yml")
HEAD = "| Item | Value |\n|---|---|\n"
TWO_MODE_ROWS = (
    "# Repository config\n\n" + HEAD + "| Mode | local |\n"
    "| Record language | Korean |\n| Mode | shared |\n"
)
NAMES_BOTH_ROWS = "line 5 `| Mode | local |`, line 7 `| Mode | shared |`"
WALKED_PAST = config_shapes.SHAPES[7]
STOPS_AT = "stops at `| Broad gate | bin/test -q | tee out |`"
UNCLOSED_FENCE = "# Repository config\n\n```\nnotes\n"
CONFIG_GET_REMOTE = ["config", "--get", "remote.origin.url"]
REV_PARSE_HEAD = ["rev-parse", "HEAD"]
# The subcommand a case makes fail, named once: a call spelling it would
# read as a path listing to `tests/test_a_shrunken_corpus_declines_to_judge.py`.
LS_FILES = "ls-files"
TIMED_OUT = subprocess.TimeoutExpired(["git"], 15)
SHA = "0123456789abcdef" + "0" * 24
BARE_TABLE = PIPED_TABLE.replace("\\|", "|")


def clone_at(d, remote=None):
    """A repository at D with one commit on `main`, a branch `feature/x`
    beside it, and REMOTE as `origin` where one is given."""
    d.mkdir(parents=True)
    git(d, "init", "-q", "-b", "main")
    write(d, "f.txt", "one\n")
    commit_everything_as_e(d, "base")
    git(d, "branch", "feature/x")
    if remote:
        git(d, "remote", "add", "origin", remote)
    return d


def holding(home, records=RECORDS):
    """HOME, a root, with each of RECORDS written under it."""
    mark_root(home)
    for rel, text in records.items():
        write(home, rel, text)
    return home


@pytest.fixture(scope="module")
def _worlds(tmp_path_factory):
    """Every world of the module, built once; see the module docstring."""
    base = tmp_path_factory.mktemp("seal-worlds")
    holding(local_home(clone_at(base / "local", SSH)))
    shared = clone_at(base / "shared")
    holding(shared / "seal")
    commit_everything_as_e(shared, "the root")
    local_home(clone_at(base / "other", HTTPS))
    clone_at(base / "plain")
    unborn = base / "unborn"
    unborn.mkdir()
    git(unborn, "init", "-q")
    holding(local_home(unborn), {"follow-up.md": "# follow-up\n"})
    inner = clone_at(base / "inner")
    for name, where in (("under", "seal/vendor"), ("beside", "vendor")):
        d = base / name
        shutil.copytree(shared, d, symlinks=True)
        added = git(
            d,
            "-c",
            "protocol.file.allow=always",
            "submodule",
            "add",
            "--quiet",
            str(inner),
            where,
            check=False,
        )
        if added.returncode == 0:
            commit_everything_as_e(d, f"a submodule at {where}")
        else:
            shutil.rmtree(d)
    exporter = base / "exporter"
    shutil.copytree(base / "local", exporter, symlinks=True)
    (base / "zips").mkdir()
    assert SEAL.main(["export", "--output", str(base / "zips")], str(exporter)) == 0
    return base


@pytest.fixture
def take(_worlds, tmp_path):
    """A copy of the world NAME under the case's own directory."""

    def taking(name):
        if not (_worlds / name).is_dir():
            pytest.skip("this git refuses a file-protocol submodule")
        dest = tmp_path / name
        shutil.copytree(_worlds / name, dest, symlinks=True)
        return dest

    return taking


@pytest.fixture
def exported(_worlds):
    """The zip exported once from the local-mode world."""
    (found,) = (_worlds / "zips").iterdir()
    return found


def said(capsys, cwd, *argv):
    """(exit code, stdout) of `seal <argv>` run in CWD, in the process."""
    code = SEAL.main(list(argv), cwd=str(cwd))
    return code, capsys.readouterr().out


def roots(repo):
    """(the shared root, the local root) of REPO, as `seal` asks for them."""
    _repo, _home, shared, local, _mode = SEAL.resolve(str(repo))
    return shared, local


def listed(path):
    """Every file under PATH, `/`-joined and sorted; None where PATH is not
    a directory."""
    if not os.path.isdir(path):
        return None
    return sorted(
        os.path.relpath(os.path.join(d, n), path).replace(os.sep, "/")
        for d, _dirs, names in os.walk(path)
        for n in names
    )


def status(repo):
    """`git status --porcelain` in REPO, one line per entry, sorted."""
    return sorted(git(repo, "status", "--porcelain").stdout.splitlines())


def snapshot(repo):
    """What a refusal must leave as it was: both roots' files, git's status
    and whether the workflow is there."""
    shared, local = roots(repo)
    return (
        listed(shared),
        listed(local),
        status(repo),
        os.path.lexists(os.path.join(str(repo), WORKFLOW_PATH)),
    )


def declared_in(repo):
    """The `Mode` row of REPO's root in force, as `seal` reads it."""
    _repo, home, _shared, _local, _mode = SEAL.resolve(str(repo))
    return SEAL.declared(home)


def config_at(repo, text):
    """TEXT written as the config of REPO's root in force; its path."""
    _repo, home, _shared, _local, _mode = SEAL.resolve(str(repo))
    path = os.path.join(home, "config.md")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def mode_row(value):
    return HEAD + f"| Mode | {value} |\n"


def zipped(path, manifest, members=()):
    """A zip at PATH: MANIFEST as its `manifest.json` (a dict as JSON, a
    string as written, None for none), then each (name, data) of MEMBERS."""
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        if manifest is not None:
            text = manifest if isinstance(manifest, str) else json.dumps(manifest)
            archive.writestr("manifest.json", text)
        for name, data in members:
            archive.writestr(name, data)
    return path


def declare(path, member, size):
    """Rewrite the size the central directory of the zip at PATH declares
    for MEMBER, leaving its data as it is."""
    raw = bytearray(path.read_bytes())
    start = 0
    while (at := raw.find(b"PK\x01\x02", start)) != -1:
        length = int.from_bytes(raw[at + 28 : at + 30], "little")
        if raw[at + 46 : at + 46 + length] == member.encode():
            raw[at + 24 : at + 28] = size.to_bytes(4, "little")
        start = at + 4
    path.write_bytes(bytes(raw))


def unanswered(monkeypatch, tail, outcome, after=0):
    """Each git run whose arguments end with TAIL, past the first AFTER,
    answers OUTCOME: an exception raised, or a (code, stdout, stderr)
    triple. Every other run is real. Returns the runs TAIL matched."""
    real = subprocess.run
    asks = []

    def run(argv, *args, **kwargs):
        if list(argv)[-len(tail) :] != list(tail):
            return real(argv, *args, **kwargs)
        asks.append(list(argv))
        if len(asks) <= after:
            return real(argv, *args, **kwargs)
        if isinstance(outcome, BaseException):
            raise outcome
        return subprocess.CompletedProcess(argv, *outcome)

    monkeypatch.setattr(SEAL.subprocess, "run", run)
    return asks


def without_o_excl(monkeypatch):
    """`os.open` with `O_EXCL` taken off, which is what Windows gives for a
    link at the name opened (run 33715420379)."""
    real = os.open
    monkeypatch.setattr(
        SEAL.os, "open", lambda path, flags, *a: real(path, flags & ~os.O_EXCL, *a)
    )


def plugin_at(root, version='{"version": "1.2.3"}', template="--branch v<version>\n"):
    """A plugin root at ROOT: its `plugin.json` holding VERSION and its
    workflow template holding TEMPLATE, each left out where None."""
    if version is not None:
        write(root, ".claude-plugin/plugin.json", version)
    if template is not None:
        write(root, "templates/hygiene.yml", template)
    return str(root)


def workflow_in(repo, text, commit=True):
    """TEXT written as REPO's workflow, committed where COMMIT; its path."""
    path = os.path.join(str(repo), WORKFLOW_PATH)
    write(repo, WORKFLOW_PATH.replace(os.sep, "/"), text)
    if commit:
        commit_everything_as_e(repo, "the workflow")
    return path


def template_text():
    with open(os.path.join(ROOT, "templates", "hygiene.yml"), encoding="utf-8") as f:
        return f.read()


class Test_module:
    def test_the_template_carries_the_marker_and_the_placeholder(self):
        """The marker and the placeholder are literals in `seal.py`, and a
        template that stopped carrying either would silently change what the
        command does: a file nobody recognises as this plugin's is never
        removed, and a version that cannot be pinned is never written."""
        text = template_text()
        assert SEAL.PLUGIN_CLONE in text
        assert SEAL.PLACEHOLDER in text

    def test_both_wrappers_ship_and_point_at_this_script(self):
        """`bin/` is on the Bash tool's PATH while the plugin is enabled, and
        cmd.exe resolves a bare `seal` to the `.cmd` twin through PATHEXT."""
        with open(os.path.join(ROOT, "bin", "seal"), encoding="utf-8") as handle:
            assert "skills/implement/scripts/seal.py" in handle.read()
        with open(os.path.join(ROOT, "bin", "seal.cmd"), encoding="utf-8") as handle:
            text = handle.read()
        assert "skills\\implement\\scripts\\seal.py" in text
        assert "py -3" in text and "python " in text

    def test_accepts_the_command_a_person_types(self, take):
        """The script run as a process, from a directory below the clone's
        root, through the stream setup only `__main__` runs."""
        repo = take("local")
        (repo / "docs").mkdir()
        done = subprocess.run(
            [
                sys.executable,
                os.path.join(ROOT, *TARGET.split("/")),
                "export",
                "--check",
            ],
            cwd=str(repo / "docs"),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        assert done.returncode == 0, done.stdout + done.stderr
        assert done.stdout == (
            "1 work items here and no export yet — `seal export` writes the "
            "first copy.\n"
        )

    def test_extractall_would_have_written_through_that_link(self, tmp_path):
        """The hazard `linked_path` exists for, run against the standard
        library rather than asserted about it: `extractall` follows a linked
        directory in the destination."""
        destination = tmp_path / "root"
        destination.mkdir()
        outside = tmp_path / "outside"
        outside.mkdir()
        symlink_or_skip(str(outside), str(destination / "threads"))
        archive = zipped(
            tmp_path / "h.zip", None, [("threads/1788-x/design.md", "LANDED")]
        )
        zipfile.ZipFile(archive).extractall(destination)
        assert (outside / "1788-x" / "design.md").read_text(
            encoding="utf-8"
        ) == "LANDED"

    def test_the_command_and_the_gate_read_one_parser(self, config):
        """`seal mode` writes the row and the gate reads it. Two readers of one
        table is how a file passes one and fails the other; `seal.py` re-exports
        this one rather than keeping a copy."""
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
        spec = importlib.util.spec_from_file_location("agentic_seal_one_parser", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # By where the code was COMPILED, not by object identity: this test loads
        # `hooks/config.py` under a name of its own, so the two module objects
        # differ while the implementation behind them must not.
        owner = os.path.join("hooks", "config.py")
        for name in ("declared", "config_rows", "config_path"):
            where = getattr(module, name).__code__.co_filename
            assert where.endswith(owner), f"seal.{name} is compiled from {where}"
        assert config.declared_mode.__code__.co_filename.endswith(owner)

    def test_seal_keeps_one_normaliser(self):
        """`seal.py` re-exports the reader's normaliser rather than keeping a
        second copy that could drift from the one the `Pact` row goes through."""
        seal = load_hook_module(
            os.path.join("..", "skills", "implement", "scripts", "seal.py"),
            "seal_for_the_pact",
        )
        assert seal.normalise_remote is seal.repo_config.normalise_remote


class Test_refuse_without_hooks:
    def test_accepts_a_hooks_directory_holding_every_module_it_names(
        self, tmp_path, capsys
    ):
        for name in SEAL.HOOK_PURPOSES:
            write(tmp_path, name, "")
        assert SEAL.refuse_without_hooks(str(tmp_path)) is None
        assert capsys.readouterr().err == ""

    def test_refuses_with_exit_2_and_a_sentence_per_module_missing(
        self, tmp_path, capsys
    ):
        write(tmp_path, "config.py", "")
        with pytest.raises(SystemExit) as stopped:
            SEAL.refuse_without_hooks(str(tmp_path))
        err = capsys.readouterr().err
        assert stopped.value.code == 2
        for name in ("optin.py", "blocks.py"):
            assert f"seal: cannot read {os.path.join(str(tmp_path), name)}, and " in err
        assert os.path.join(str(tmp_path), "config.py") not in err
        assert err.endswith("Nothing was read.\n"), err

    @pytest.mark.parametrize(
        "args, purpose, absent",
        [
            (
                ["mode", "--check"],
                "it is what finds the repository's seal/ root",
                None,
            ),
            # Round 1's yellow 1 of #610: `hooks/config.py` reads `config.md`
            # and never writes it, so a purpose saying it writes is #590's
            # wrong-purpose defect again.
            (
                ["mode", "--check"],
                "it is what reads the root's config.md",
                "reads and writes",
            ),
            # #667: `hooks/config.py` imports `hooks/blocks.py`, so a `hooks/`
            # without it fails that import.
            (
                ["mode", "--check"],
                "it is the walk config.py reads config.md through",
                None,
            ),
            (
                ["mode", "--check"],
                "it is what writes the record `seal no-work-item` leaves",
                None,
            ),
            (
                ["mode", "--check"],
                "it names the variable a session's id is read from",
                None,
            ),
        ],
        ids=["optin.py", "config.py", "blocks.py", "routing.py", "hooksession.py"],
    )
    def test_a_script_copied_alone_exits_2_and_names_what_it_misses(
        self, tmp_path, args, purpose, absent
    ):
        """#590 and #610. A copy of this script taken without `hooks/` exits 2,
        with a sentence per missing module naming its path and what it is for.
        It puts `hooks/` on `sys.path` and then runs a plain `import`, which a
        search for by-path loaders does not find, and it asks before the
        import, at import, so any invocation argparse accepts reaches it:
        `mode --check`, and not an empty one, because argparse's own usage
        error is also exit 2 and would pass for the wrong reason."""
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


class Test_git_asked:
    def test_accepts_an_exit_the_caller_counts_as_an_answer(self, _worlds):
        assert SEAL.git_asked(str(_worlds / "local"), *CONFIG_GET_REMOTE) == (SSH, "")
        assert SEAL.git_asked(
            str(_worlds / "plain"), *CONFIG_GET_REMOTE, answered=(0, 1)
        ) == ("", "")

    @pytest.mark.parametrize(
        "outcome, why",
        [
            ((128, "HEAD\n", ""), "git rev-parse exited 128"),
            ((1, "", "fatal: bad object\n"), "fatal: bad object"),
            (OSError("no git here"), "git rev-parse could not be run (no git here)"),
            (TIMED_OUT, "git rev-parse could not be run ("),
        ],
        ids=["an exit and its output", "an exit and its stderr", "no git", "a timeout"],
    )
    def test_refuses_a_git_that_did_not_answer(
        self, monkeypatch, tmp_path, outcome, why
    ):
        unanswered(monkeypatch, REV_PARSE_HEAD, outcome)
        text, said_why = SEAL.git_asked(str(tmp_path), *REV_PARSE_HEAD)
        assert text is None
        assert said_why.startswith(why), said_why


class Test_git:
    def test_accepts_what_git_prints_stripped(self, _worlds):
        assert SEAL.git(
            str(_worlds / "local"), "rev-parse", "--abbrev-ref", "HEAD"
        ) == ("main")

    def test_refuses_a_failure_as_the_empty_string(self, tmp_path):
        assert SEAL.git(str(tmp_path), *REV_PARSE_HEAD) == ""


class Test_remote_url:
    def test_accepts_an_unset_origin_as_the_empty_answer(self, _worlds):
        assert SEAL.remote_url(str(_worlds / "local")) == (SSH, "")
        assert SEAL.remote_url(str(_worlds / "plain")) == ("", "")

    def test_refuses_a_config_git_cannot_parse(self, monkeypatch, _worlds):
        unanswered(
            monkeypatch, CONFIG_GET_REMOTE, (128, "", "fatal: bad config line 9\n")
        )
        assert SEAL.remote_url(str(_worlds / "local")) == (
            None,
            "fatal: bad config line 9",
        )


class Test_head_sha:
    def test_accepts_a_commit_as_its_sha(self, _worlds):
        repo = _worlds / "local"
        assert SEAL.head_sha(str(repo)) == (git_out(repo, *REV_PARSE_HEAD), "")

    def test_refuses_a_branch_with_no_commit(self, _worlds):
        sha, why = SEAL.head_sha(str(_worlds / "unborn"))
        assert sha is None and why


def same(a, b):
    return os.path.normcase(os.path.realpath(a)) == os.path.normcase(
        os.path.realpath(b)
    )


class Test_resolve:
    @pytest.mark.parametrize("mode", ["local", "shared"])
    def test_accepts_a_root_in_force_and_names_its_mode(self, _worlds, mode):
        repo, home, shared, local, found = SEAL.resolve(str(_worlds / mode))
        assert same(repo, _worlds / mode)
        assert same(shared, _worlds / mode / "seal")
        assert same(home, shared if mode == "shared" else local)
        assert found == mode

    def test_refuses_a_directory_with_no_root_or_no_repository(self, _worlds, tmp_path):
        assert SEAL.resolve(str(tmp_path)) == ("", "", "", "", "")
        repo, home, shared, local, found = SEAL.resolve(str(_worlds / "plain"))
        assert same(repo, _worlds / "plain") and shared and local
        assert (home, found) == ("", "")


class Test_root_files:
    def test_accepts_a_tree_as_sorted_slash_joined_paths(self, tmp_path):
        for rel in ("b.md", "a/c.md", "a/b/d.md"):
            write(tmp_path, rel, rel)
        files, links = SEAL.root_files(str(tmp_path))
        assert files == [
            (rel, os.path.join(str(tmp_path), *rel.split("/")))
            for rel in ("a/b/d.md", "a/c.md", "b.md")
        ]
        assert links == []

    def test_refuses_to_follow_a_link_and_names_it(self, tmp_path):
        root, outside = tmp_path / "root", tmp_path / "outside"
        write(root, "a.md", "a")
        write(outside, "secret.md", "secret")
        symlink_or_skip(str(outside / "secret.md"), str(root / "leak.md"))
        symlink_or_skip(str(outside), str(root / "linked"))
        files, links = SEAL.root_files(str(root))
        assert [rel for rel, _disk in files] == ["a.md"]
        assert links == ["leak.md", "linked/"]


class Test_read_bytes:
    def test_accepts_a_file_as_its_bytes(self, tmp_path):
        (tmp_path / "a").write_bytes(b"one\r\ntwo")
        assert SEAL.read_bytes(str(tmp_path / "a")) == b"one\r\ntwo"

    def test_refuses_a_path_that_is_not_there(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            SEAL.read_bytes(str(tmp_path / "absent"))


class Test_digest:
    def test_accepts_the_path_the_length_and_the_bytes(self, tmp_path):
        write(tmp_path, "a.md", "x")

        assert SEAL.digest([("a.md", str(tmp_path / "a.md"))]) == (
            hashlib.sha256(b"a.md\x001\x00x").hexdigest()
        )

    def test_refuses_to_call_a_rename_or_a_swap_the_same_tree(self, tmp_path):
        write(tmp_path, "x", "one")
        write(tmp_path, "y", "two")
        x, y = str(tmp_path / "x"), str(tmp_path / "y")
        first = SEAL.digest([("a.md", x), ("b.md", y)])
        assert SEAL.digest([("a.md", y), ("b.md", x)]) != first
        assert SEAL.digest([("c.md", x), ("b.md", y)]) != first


class Test_work_item_of:
    @pytest.mark.parametrize(
        "rel, item",
        [
            ("threads/1788-x/design.md", "1788-x"),
            ("threads/1788-y/trail/rounds/round-1.md", "1788-y"),
        ],
    )
    def test_accepts_a_path_under_a_work_items_directory(self, rel, item):
        assert SEAL.work_item_of(rel) == item

    @pytest.mark.parametrize(
        "rel", ["follow-up.md", "threads/1788-x", "notes/1788-x/a.md"]
    )
    def test_refuses_a_path_in_no_work_item(self, rel):
        assert SEAL.work_item_of(rel) == ""


class Test_work_item_digests:
    def test_accepts_each_item_as_the_digest_of_its_files(self, tmp_path):
        holding(tmp_path)
        write(tmp_path, "threads/1788000001-another/design.md", "# another\n")
        files = SEAL.root_files(str(tmp_path))[0]
        found = SEAL.work_item_digests(files)
        assert found == {
            item: SEAL.digest(
                sorted(e for e in files if e[0].startswith(f"threads/{item}/"))
            )
            for item in (ITEM, "1788000001-another")
        }

    def test_refuses_a_file_that_belongs_to_no_item(self, tmp_path):
        write(tmp_path, "follow-up.md", "x")
        write(tmp_path, "threads/loose.md", "x")
        assert SEAL.work_item_digests(SEAL.root_files(str(tmp_path))[0]) == {}


class Test_manifest_of:
    def test_accepts_what_git_answers_and_an_origin_that_is_not_set(self, _worlds):
        repo = _worlds / "local"
        manifest, unread = SEAL.manifest_of(str(repo), "local", [])
        assert unread == {}
        assert manifest["format"] == 1 and manifest["mode"] == "local"
        assert manifest["remote"] == SSH
        assert manifest["head"] == git_out(repo, *REV_PARSE_HEAD)
        assert manifest["exported_at"].endswith("Z")
        assert manifest["items"] == {}
        assert SEAL.manifest_of(str(_worlds / "plain"), "local", [])[0]["remote"] == ""

    @pytest.mark.parametrize(
        "field, tail", [("remote", CONFIG_GET_REMOTE), ("head", REV_PARSE_HEAD)]
    )
    def test_refuses_to_write_a_field_git_did_not_answer(
        self, monkeypatch, _worlds, field, tail
    ):
        unanswered(monkeypatch, tail, TIMED_OUT)
        manifest, unread = SEAL.manifest_of(str(_worlds / "local"), "local", [])
        assert field not in manifest
        assert list(unread) == [field]
        assert unread[field].startswith(
            "the remote was left out — "
            if field == "remote"
            else "the HEAD SHA was left out — "
        )


class Test_unused:
    def test_accepts_the_first_name_nothing_holds(self, tmp_path):
        assert SEAL.unused(str(tmp_path), "seal-x", ".zip") == str(
            tmp_path / "seal-x.zip"
        )
        write(tmp_path, "seal-x.zip", "")
        assert SEAL.unused(str(tmp_path), "seal-x", ".zip") == str(
            tmp_path / "seal-x-2.zip"
        )

    def test_refuses_a_broken_link_and_a_directory_with_every_name_taken(
        self, tmp_path, monkeypatch
    ):
        symlink_or_skip(str(tmp_path / "nowhere"), str(tmp_path / "seal-y.zip"))
        assert SEAL.unused(str(tmp_path), "seal-y", ".zip") == str(
            tmp_path / "seal-y-2.zip"
        )
        taken = types.SimpleNamespace(
            path=types.SimpleNamespace(join=os.path.join, lexists=lambda p: True)
        )
        monkeypatch.setattr(SEAL, "os", taken)
        assert SEAL.unused(str(tmp_path), "seal-z", ".zip") == ""


class Test_zip_stem:
    def test_accepts_the_clones_name_and_the_date(self, tmp_path):
        repo = os.path.join(str(tmp_path), "repo")
        assert SEAL.zip_stem(repo, "2026-09-03") == "seal-repo-2026-09-03"
        assert SEAL.zip_stem(repo + os.sep, "2026-09-03") == "seal-repo-2026-09-03"

    def test_refuses_a_character_a_name_should_not_carry(self, tmp_path):
        repo = os.path.join(str(tmp_path), "my repo!")
        assert SEAL.zip_stem(repo, "2026-09-03") == "seal-my-repo--2026-09-03"
        assert SEAL.zip_stem(os.sep, "2026-09-03") == "seal-repo-2026-09-03"


class Test_write_zip:
    def files(self, tmp_path):
        write(tmp_path, "home/a.md", "a\n")
        return str(tmp_path / "home"), [("a.md", str(tmp_path / "home" / "a.md"))]

    def test_accepts_the_manifest_and_the_records_under_the_root(self, tmp_path):
        home, files = self.files(tmp_path)
        target = str(tmp_path / "out.zip")
        SEAL.write_zip(target, home, files, {"format": 1})
        with zipfile.ZipFile(target) as archive:
            assert archive.namelist() == ["manifest.json", "seal/a.md"]
            assert json.loads(archive.read("manifest.json")) == {"format": 1}
        assert not os.path.lexists(target + ".partial")

    @pytest.mark.parametrize(
        "shape", ["a file", "a broken link", "a broken link, no O_EXCL"]
    )
    def test_refuses_a_partial_name_it_did_not_create_and_leaves_it(
        self, tmp_path, monkeypatch, shape
    ):
        home, files = self.files(tmp_path)
        target = str(tmp_path / "out.zip")
        partial = target + ".partial"
        outside = tmp_path / "outside"
        outside.mkdir()
        if shape == "a file":
            write(tmp_path, "out.zip.partial", "somebody's\n")
        else:
            symlink_or_skip(str(outside / "stolen.bin"), partial)
        if shape.endswith("no O_EXCL"):
            without_o_excl(monkeypatch)
        with pytest.raises(FileExistsError):
            SEAL.write_zip(target, home, files, {"format": 1})
        assert os.path.lexists(partial)
        assert list(outside.iterdir()) == []
        assert not os.path.lexists(target)

    def test_refuses_to_leave_a_half_archive_when_a_record_will_not_read(
        self, tmp_path
    ):
        home, files = self.files(tmp_path)
        target = str(tmp_path / "out.zip")
        with pytest.raises(OSError):
            SEAL.write_zip(target, home, [*files, ("b.md", str(tmp_path / "b"))], {})
        assert not os.path.lexists(target + ".partial")
        assert not os.path.lexists(target)


def only_zip(directory):
    found = sorted(p for p in os.listdir(directory) if p.endswith(".zip"))
    assert len(found) == 1, f"expected one zip in {directory}, found {found}"
    return os.path.join(directory, found[0])


def manifest_in(path):
    with zipfile.ZipFile(path) as archive:
        return json.loads(archive.read("manifest.json"))


class Test_export:
    def test_accepts_a_local_root_as_a_zip_beside_the_clone(
        self, take, capsys, tmp_path
    ):
        repo = take("local")
        code, out = said(capsys, repo, "export")
        assert code == 0, out
        written = only_zip(tmp_path)
        assert os.path.basename(written).startswith("seal-local-")
        with zipfile.ZipFile(written) as archive:
            assert archive.namelist() == MEMBERS
        manifest = manifest_in(written)
        assert manifest["mode"] == "local" and manifest["remote"] == SSH
        assert list(manifest["items"]) == [ITEM]
        assert status(repo) == [], "the export dirtied the working tree"
        assert out.startswith("wrote "), out
        assert (
            f"{os.path.basename(written)}\n  5 files from .git/seal, 1 work item\n"
        ) in out
        assert out.endswith(f"  seal import {os.path.basename(written)}\n"), out
        assert "was left out" not in out
        assert SEAL.read_state(str(repo)) == manifest

    def test_accepts_session_state_beside_the_root_and_leaves_it_out(
        self, take, capsys, tmp_path
    ):
        repo = take("local")
        for name in BESIDE_THE_ROOT:
            write(repo / ".git", name, "session state\n")
        write(repo / ".git", "agentic-worktree-choice/a-branch", "x")
        assert said(capsys, repo, "export")[0] == 0
        with zipfile.ZipFile(only_zip(tmp_path)) as archive:
            assert archive.namelist() == MEMBERS

    def test_accepts_a_link_in_the_root_as_skipped_and_named(
        self, take, capsys, tmp_path
    ):
        repo = take("local")
        write(repo / ".git", "agentic-implementer", "secret-branch\n")
        _shared, local = roots(repo)
        symlink_or_skip(
            os.path.join("..", "agentic-implementer"), os.path.join(local, "leak.md")
        )
        code, out = said(capsys, repo, "export")
        assert code == 0, out
        assert (
            "  skipped the symbolic link seal/leak.md — links are not followed\n" in out
        )
        with zipfile.ZipFile(only_zip(tmp_path)) as archive:
            assert archive.namelist() == MEMBERS
            assert not any(b"secret-branch" in archive.read(m) for m in MEMBERS)

    def test_accepts_a_taken_name_as_the_next_one(self, take, capsys, tmp_path):
        """A second export the same day, and a broken link at the zip's own
        name, each take the next name and replace nothing."""
        repo = take("local")
        assert said(capsys, repo, "export")[0] == 0
        first = only_zip(tmp_path)
        os.rename(first, first + ".kept")
        symlink_or_skip(str(tmp_path / "nowhere.bin"), first)
        assert said(capsys, repo, "export")[0] == 0
        assert os.path.islink(first), "the link was replaced by the zip"
        assert os.path.isfile(first[: -len(".zip")] + "-2.zip")

    def test_accepts_an_output_and_notes_one_inside_the_tree(
        self, take, capsys, tmp_path
    ):
        repo = take("local")
        (repo / "out").mkdir()
        code, out = said(capsys, repo, "export", "--output", str(repo / "out"))
        assert code == 0, out
        assert "is inside the working tree" in out
        assert only_zip(repo / "out")
        code, out = said(capsys, repo, "export", "--output", str(tmp_path / "x.zip"))
        assert code == 0, out
        assert os.path.isfile(tmp_path / "x.zip")
        assert "inside the working tree" not in out

    def test_accepts_a_clone_with_no_commit_and_leaves_its_head_out(
        self, take, capsys, tmp_path
    ):
        """Only a missing `remote` is refused on arrival, so the advice for
        it is not printed for a missing `head`."""
        repo = take("unborn")
        code, out = said(capsys, repo, "export")
        assert code == 0, out
        assert "head" not in manifest_in(only_zip(tmp_path))
        assert "the HEAD SHA was left out" in out
        assert "without a flag" not in out

    def test_refuses_a_shared_root_and_names_the_way_to_local(
        self, take, capsys, tmp_path
    ):
        code, out = said(capsys, take("shared"), "export")
        assert code == 1
        assert out.startswith("shared mode: the records are committed at seal/")
        assert '"$(git rev-parse --git-common-dir)/seal"' in out
        assert not [p for p in os.listdir(tmp_path) if p.endswith(".zip")]

    def test_refuses_without_a_root_or_in_a_throwaway_clone(self, take, capsys):
        plain = take("plain")
        code, out = said(capsys, plain, "export")
        assert code == 1
        assert "(shared mode)" in out and "(local mode)" in out
        assert not (plain / "seal").exists() and not (plain / ".git" / "seal").exists()
        local = take("local")
        write(local / ".git", "agentic-scratch", "")
        code, out = said(capsys, local, "export")
        assert code == 1
        assert "marked throwaway (agentic-scratch" in out

    @pytest.mark.parametrize("shape", ["a file", "a broken link"])
    def test_refuses_a_partial_name_somebody_holds(self, take, capsys, tmp_path, shape):
        repo = take("local")
        today = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d")
        stem = SEAL.zip_stem(str(repo), today)
        partial = tmp_path / f"{stem}.zip.partial"
        outside = tmp_path / "outside"
        outside.mkdir()
        if shape == "a file":
            partial.write_text("somebody else's bytes\n", encoding="utf-8")
        else:
            symlink_or_skip(str(outside / "stolen.bin"), str(partial))
        code, out = said(capsys, repo, "export")
        assert code == 1, out
        assert out.startswith("the zip could not be written to "), out
        assert f"{stem}.zip: " in out and f"{stem}.zip.partial" in out, out
        assert os.path.lexists(partial)
        assert list(outside.iterdir()) == []
        assert not [p for p in os.listdir(tmp_path) if p.endswith(".zip")]

    def test_refuses_to_keep_quiet_about_a_remote_it_could_not_read(
        self, take, capsys, monkeypatch, tmp_path
    ):
        repo = take("local")
        unanswered(monkeypatch, CONFIG_GET_REMOTE, TIMED_OUT)
        code, out = said(capsys, repo, "export")
        assert code == 0, out
        assert "remote" not in manifest_in(only_zip(tmp_path))
        assert "  the remote was left out — git config could not be run (" in out
        assert "  Running this again once git answers writes a zip the other " in out

    def test_refuses_an_output_with_no_directory_or_no_free_name(
        self, take, capsys, monkeypatch, tmp_path
    ):
        repo = take("local")
        missing = tmp_path / "missing"
        code, out = said(capsys, repo, "export", "--output", str(missing / "x.zip"))
        assert code == 1
        assert (
            out == f"{missing} is not a directory — pass --output somewhere that is\n"
        )
        monkeypatch.setattr(SEAL, "unused", lambda *a: "")
        code, out = said(capsys, repo, "export")
        assert code == 1
        assert out.startswith("no free name for seal-local-") and "pass --output" in out


class Test_plural:
    def test_accepts_one_as_the_noun_alone(self):
        assert SEAL.plural(1, "file") == "1 file"

    @pytest.mark.parametrize("count", [0, 2])
    def test_refuses_the_singular_for_any_other_count(self, count):
        assert SEAL.plural(count, "file") == f"{count} files"


class Test_display:
    def test_accepts_a_path_inside_as_slash_joined_and_relative(self, tmp_path):
        assert (
            SEAL.display(str(tmp_path), str(tmp_path / ".git" / "seal")) == ".git/seal"
        )

    def test_refuses_to_shorten_a_path_outside_or_nothing(self, tmp_path):
        outside = str(tmp_path.parent / "elsewhere")
        assert SEAL.display(str(tmp_path), outside) == outside
        assert SEAL.display(str(tmp_path), "") == ""


class Test_inside:
    def test_accepts_the_tree_and_a_path_below_it(self, tmp_path):
        assert SEAL.inside(str(tmp_path), str(tmp_path))
        assert SEAL.inside(str(tmp_path), str(tmp_path / "a" / "b"))

    def test_refuses_a_sibling_sharing_the_prefix_and_another_drive(
        self, tmp_path, monkeypatch
    ):
        assert not SEAL.inside(str(tmp_path / "repo"), str(tmp_path / "repo-2" / "x"))

        def other_drive(paths):
            raise ValueError("Paths don't have the same drive")

        monkeypatch.setattr(SEAL.os.path, "commonpath", other_drive)
        assert not SEAL.inside(str(tmp_path), str(tmp_path / "x"))


class Test_no_root:
    def test_accepts_a_repository_without_a_root_by_naming_both_places(
        self, _worlds, capsys
    ):
        repo, _home, shared, local, _mode = SEAL.resolve(str(_worlds / "plain"))
        assert SEAL.no_root(repo, shared, local) == 1
        out = capsys.readouterr().out
        assert f"  {shared}   (shared mode)\n  {local}   (local mode)\n" in out
        assert out.endswith(
            "The first time your session works in a repository it asks which one, "
            "and creates it.\n"
        )
        assert "crafter" not in out

    def test_refuses_a_directory_outside_git_and_a_throwaway_clone(self, take, capsys):
        assert SEAL.no_root("", "", "") == 1
        assert capsys.readouterr().out == (
            "not inside a git repository — seal works on a clone\n"
        )
        repo = take("plain")
        write(repo / ".git", "agentic-scratch", "")
        assert SEAL.no_root(str(repo), "", "") == 1
        assert "marked throwaway (agentic-scratch" in capsys.readouterr().out


class Test_state_path:
    def test_accepts_a_clone_as_a_file_beside_the_root(self, _worlds):
        repo = _worlds / "local"
        assert same(
            SEAL.state_path(str(repo)), repo / ".git" / "agentic-last-export.json"
        )

    def test_refuses_a_directory_outside_git(self, tmp_path):
        assert SEAL.state_path(str(tmp_path)) == ""


class Test_write_state:
    def test_accepts_the_manifest_as_json(self, take):
        repo = take("local")
        SEAL.write_state(str(repo), {"format": 1, "items": {}})
        with open(SEAL.state_path(str(repo)), encoding="utf-8") as handle:
            assert json.load(handle) == {"format": 1, "items": {}}

    def test_refuses_to_fail_an_export_it_cannot_record(self, take, tmp_path):
        repo = take("local")
        os.mkdir(SEAL.state_path(str(repo)))
        assert SEAL.write_state(str(repo), {"format": 1}) is None
        assert os.path.isdir(SEAL.state_path(str(repo)))
        assert SEAL.write_state(str(tmp_path), {"format": 1}) is None
        assert os.listdir(tmp_path) == ["local"]


class Test_read_state:
    def test_accepts_what_the_last_export_wrote(self, take):
        repo = take("local")
        write(repo / ".git", "agentic-last-export.json", '{"items": {"a": "b"}}')
        assert SEAL.read_state(str(repo)) == {"items": {"a": "b"}}

    @pytest.mark.parametrize(
        "text", [None, "{", "\udcff"], ids=["none", "not json", "not utf-8"]
    )
    def test_refuses_a_state_it_cannot_read_as_none(self, take, text):
        repo = take("local")
        if text == "\udcff":
            (repo / ".git" / "agentic-last-export.json").write_bytes(b"\xff{")
        elif text is not None:
            write(repo / ".git", "agentic-last-export.json", text)
        assert SEAL.read_state(str(repo)) is None


def member(name, size=1, link=False):
    info = zipfile.ZipInfo("x")
    info.filename = name
    info.file_size = size
    if link:
        info.external_attr = (0o120777 << 16) | 0o200000
    return info


class Test_unsafe:
    @pytest.mark.parametrize(
        "info",
        [
            member("seal/threads/x/design.md"),
            member("manifest.json"),
            member("manifest.json/"),
            member("seal/a.md", SEAL.MEMBER_LIMIT),
        ],
        ids=["a record", "the manifest", "the manifest with a slash", "at the limit"],
    )
    def test_accepts_a_record_under_the_root_and_the_manifest(self, info):
        assert SEAL.unsafe(info) == ""

    @pytest.mark.parametrize(
        "info, why",
        [
            (member(""), "a member with no name"),
            (member("seal/a\\..\\..\\b.md"), "holds a backslash"),
            (member("/etc/passwd"), "is an absolute path"),
            (member("C:x.md"), "is an absolute path"),
            (member("seal/a\0b.md"), "holds a NUL"),
            (member("seal/nested/../../out.md"), "climbs out of the root with `..`"),
            (member("seal/leak.md", link=True), "is a symbolic link"),
            (member("elsewhere/x.md"), "is not under seal/ and is not the manifest"),
            (member("seal/a.md", SEAL.MEMBER_LIMIT + 1), "one record may hold"),
        ],
        ids=[
            "no name",
            "a backslash",
            "absolute",
            "a drive",
            "a NUL",
            "a climb",
            "a link",
            "outside the root",
            "past the limit",
        ],
    )
    def test_refuses_a_member_it_has_no_place_for(self, info, why):
        assert why in SEAL.unsafe(info)


def opened(path):
    return zipfile.ZipFile(path)


class Test_linked_path:
    def archive(self, tmp_path):
        return zipped(
            tmp_path / "z.zip",
            {"format": 1},
            [("seal/threads/w/design.md", "w"), ("seal/follow-up.md", "f")],
        )

    def test_accepts_a_root_no_member_reaches_through_a_link(self, tmp_path):
        into = tmp_path / "root"
        into.mkdir()
        symlink_or_skip(str(tmp_path), str(into / "elsewhere"))
        with opened(self.archive(tmp_path)) as archive:
            assert SEAL.linked_path(str(into), archive) == ""

    @pytest.mark.parametrize("name", ["threads", "follow-up.md"])
    def test_refuses_a_link_on_a_members_way_or_at_its_name(self, tmp_path, name):
        into = tmp_path / "root"
        into.mkdir()
        symlink_or_skip(str(tmp_path / "nowhere"), str(into / name))
        with opened(self.archive(tmp_path)) as archive:
            assert SEAL.linked_path(str(into), archive) == name


class Test_blocked_path:
    def test_accepts_a_member_whose_directories_are_free(self, tmp_path):
        into = tmp_path / "root"
        (into / "a").mkdir(parents=True)
        z = zipped(tmp_path / "z.zip", {"format": 1}, [("seal/a/b.md", "b")])
        with opened(z) as archive:
            assert SEAL.blocked_path(str(into), archive) == ""

    @pytest.mark.parametrize("held", ["in the zip", "a file here", "a pipe here"])
    def test_refuses_a_directory_name_a_file_holds(self, tmp_path, held):
        into = tmp_path / "root"
        into.mkdir()
        members = [("seal/a/b.md", "b")]
        if held == "in the zip":
            members.insert(0, ("seal/a", "a file"))
        elif held == "a file here":
            write(into, "a", "already a file\n")
        else:
            fifo_or_skip(into / "a")
        z = zipped(tmp_path / "z.zip", {"format": 1}, members)
        with opened(z) as archive:
            assert SEAL.blocked_path(str(into), archive) == "a"


class Test_read_manifest:
    def test_accepts_an_object_of_this_format(self, tmp_path):
        z = zipped(tmp_path / "z.zip", {"format": 1, "remote": ""})
        with opened(z) as archive:
            assert SEAL.read_manifest(archive, "z") == ({"format": 1, "remote": ""}, "")

    @pytest.mark.parametrize(
        "manifest, why",
        [
            (None, "z holds no manifest.json — it was not written by `seal export`"),
            ("{", "z's manifest.json could not be read: "),
            ([1], "z's manifest.json is not an object"),
            ({"format": 2}, "z is format 2 and this build reads format 1."),
            ({}, "z is format None and this build reads format 1."),
        ],
        ids=["none", "not json", "not an object", "a later format", "no format"],
    )
    def test_refuses_a_manifest_this_build_cannot_place_records_by(
        self, tmp_path, manifest, why
    ):
        z = zipped(tmp_path / "z.zip", manifest, [("seal/a.md", "a")])
        with opened(z) as archive:
            found, said_why = SEAL.read_manifest(archive, "z")
        assert found is None
        assert said_why.startswith(why), said_why


class Test_place:
    def test_accepts_a_free_name_as_added(self, tmp_path):
        dest = str(tmp_path / "plan.md")
        assert SEAL.place(dest, b"x") == (dest, SEAL.ADDED)

    @pytest.mark.parametrize(
        "here, want",
        [
            ({"plan.md": "mine"}, ("plan.incoming.md", "collided")),
            ({"plan.md": "x"}, (None, "identical")),
            ({"plan.md": "mine", "plan.incoming.md": "x"}, (None, "identical")),
            (
                {"plan.md": "mine", "plan.incoming.md": "older"},
                ("plan.incoming-2.md", "collided"),
            ),
            (
                {"plan.md": "mine", "plan.incoming.md": None},
                ("plan.incoming-2.md", "collided"),
            ),
            ({"plan.md": None}, ("plan.incoming.md", "collided")),
        ],
        ids=[
            "a differing file",
            "the same bytes",
            "the same bytes beside it",
            "a differing copy beside it",
            "a broken link beside it",
            "a broken link at the name",
        ],
    )
    def test_refuses_to_overwrite_and_lands_beside(self, tmp_path, here, want):
        for name, text in here.items():
            if text is None:
                symlink_or_skip(str(tmp_path / "nowhere"), str(tmp_path / name))
            else:
                write(tmp_path, name, text)
        path, outcome = SEAL.place(str(tmp_path / "plan.md"), b"x")
        assert (path and os.path.basename(path), outcome) == want
        assert path is None or os.path.dirname(path) == str(tmp_path)


class Test_destination_root:
    def dirs(self, tmp_path, *names):
        for name in names:
            mark_root(tmp_path / name)
        return str(tmp_path / "shared"), str(tmp_path / "local")

    def test_accepts_a_projects_own_seal_beside_the_local_root_as_one_root(
        self, tmp_path
    ):
        """A `<repo>/seal/` whose README does not open with the marker is the
        project's own, so beside a local root it is no second root, and the
        copy lands in the local one."""
        shared, local = self.dirs(tmp_path, "local")
        write(tmp_path, "shared/README.md", "# seal\n\nThis package's notes.\n")
        assert SEAL.destination_root("", local, shared, local, None) == (local, "")

    @pytest.mark.parametrize(
        "home, into, want",
        [
            ("home", None, "home"),
            ("", None, "local"),
            ("", "shared", "shared"),
            ("", "local", "local"),
        ],
        ids=["the root in force", "neither, so local", "into shared", "into local"],
    )
    def test_accepts_the_root_in_force_then_local(self, tmp_path, home, into, want):
        shared, local = self.dirs(tmp_path)
        named = {"home": str(tmp_path / "home"), "shared": shared, "local": local}
        assert SEAL.destination_root("", named.get(home, ""), shared, local, into) == (
            named[want],
            "",
        )

    @pytest.mark.parametrize("into", [None, "shared", "local"])
    def test_refuses_two_roots_whatever_into_says(self, tmp_path, into):
        shared, local = self.dirs(tmp_path, "shared", "local")
        root, why = SEAL.destination_root("", shared, shared, local, into)
        assert root == ""
        assert why.startswith("both roots exist, and the gates read the first of them:")
        assert f"  {shared}   (shared mode — read first)\n" in why

    @pytest.mark.parametrize("into", [None, "local"])
    def test_refuses_a_local_root_it_cannot_place(self, tmp_path, into):
        shared, _local = self.dirs(tmp_path)
        assert SEAL.destination_root("", "", shared, "", into) == (
            "",
            "the common git directory could not be resolved",
        )


class Test_import_:
    def test_refuses_beside_a_root_an_earlier_release_wrote(
        self, take, exported, capsys
    ):
        """A `<repo>/seal/` whose README opens with a heading an earlier
        release wrote is that release's root, waiting for the session-start
        move, as `hooks/root-migrate.py#ours` reads it: `seal import` puts no
        second root under the git directory, and neither `seal mode` nor
        `seal pr-checks install` sends the person to first setup."""
        plain = take("plain")
        write(plain, "seal/README.md", f"{OPTIN.EARLIER_HEADINGS[0]}\n\nold\n")
        line = SEAL.earlier_root() + "\n"
        assert said(capsys, plain, "import", str(exported)) == (1, line)
        assert not os.path.exists(roots(plain)[1]), "a second root was made"
        assert said(capsys, plain, "mode") == (1, line)
        assert said(capsys, plain, "pr-checks", "install") == (1, line)

    def test_accepts_missing_records_as_added_and_asks_nothing(
        self, take, exported, capsys
    ):
        other = take("other")
        code, out = said(capsys, other, "import", str(exported))
        assert code == 0, out
        assert listed(roots(other)[1]) == sorted(RECORDS)
        # The README every root opens with is the one record already there.
        assert out.startswith(
            "imported into .git/seal\n  4 files added\n"
            "  1 file already here, byte for byte\n"
            "  0 files landed beside an existing one\n"
        ), out
        assert "another repository" not in out, "two spellings of one remote differ"
        assert "?" not in out and out.rstrip().endswith(CLOSING), out

    def test_accepts_the_same_zip_twice_as_the_same_bytes(self, take, exported, capsys):
        other = take("other")
        assert said(capsys, other, "import", str(exported))[0] == 0
        code, out = said(capsys, other, "import", str(exported))
        assert code == 0, out
        assert "  5 files already here, byte for byte\n" in out
        assert listed(roots(other)[1]) == sorted(RECORDS)

    def test_accepts_a_taken_name_by_landing_beside_it(self, take, exported, capsys):
        other = take("other")
        local = roots(other)[1]
        write(local, f"threads/{ITEM}/plan.md", "# mine\n")
        write(local, f"threads/{ITEM}/plan.incoming.md", "# earlier\n")
        code, out = said(capsys, other, "import", str(exported))
        assert code == 0, out
        work = os.path.join(local, "threads", ITEM)
        assert (
            open(os.path.join(work, "plan.md"), encoding="utf-8").read() == "# mine\n"
        )
        assert (
            open(os.path.join(work, "plan.incoming-2.md"), encoding="utf-8").read()
            == "# rows\n"
        )
        assert (
            f"  1 file landed beside an existing one:\n"
            f"    threads/{ITEM}/plan.md  ->  threads/{ITEM}/plan.incoming-2.md\n"
        ) in out

    @pytest.mark.parametrize(
        "into, where",
        [
            (["--into", "shared"], "shared"),
            (["--into", "local"], "local"),
            ([], "local"),
        ],
        ids=["into shared", "into local", "neither, so local"],
    )
    def test_accepts_into_either_root_and_defaults_to_local(
        self, take, exported, capsys, into, where
    ):
        other = take("other")
        shared, local = roots(other)
        shutil.rmtree(local)
        code, out = said(capsys, other, "import", str(exported), *into)
        assert code == 0, out
        assert listed(shared if where == "shared" else local) == sorted(RECORDS)
        assert listed(local if where == "shared" else shared) is None
        if where == "local":
            assert status(other) == []

    def test_accepts_a_remote_absent_by_answer_on_either_side(
        self, take, exported, capsys, tmp_path
    ):
        """`""` is an answer: a clone with no `origin`, or a zip from one."""
        other = take("other")
        git(other, "remote", "remove", "origin")
        assert said(capsys, other, "import", str(exported))[0] == 0
        other = take("plain")
        quiet = zipped(
            tmp_path / "empty-remote.zip",
            {"format": 1, "remote": ""},
            [("seal/a.md", "a")],
        )
        code, out = said(capsys, other, "import", str(quiet))
        assert code == 0, out
        assert listed(roots(other)[1]) == ["a.md"]

    def test_accepts_each_flag_past_the_check_it_names(
        self, take, exported, capsys, monkeypatch, tmp_path
    ):
        other = take("other")
        foreign = zipped(
            tmp_path / "foreign.zip",
            {"format": 1, "remote": ELSEWHERE},
            [("seal/follow-up.md", "# theirs\n")],
        )
        code, out = said(capsys, other, "import", str(foreign), "--allow-other-repo")
        assert code == 0, out
        assert listed(roots(other)[1]) == ["README.md", "follow-up.md"]
        unanswered(monkeypatch, CONFIG_GET_REMOTE, TIMED_OUT)
        code, out = said(
            capsys, other, "import", str(exported), "--allow-unreadable-remote"
        )
        assert code == 0, out
        assert listed(roots(other)[1]) == sorted([*RECORDS, "follow-up.incoming.md"])

    @pytest.mark.parametrize(
        "fields, flags, line",
        [
            (
                {"head": SHA, "exported_at": "2026-09-03T00:00:00Z"},
                [],
                "Exported at 2026-09-03T00:00:00Z from 0123456789ab.",
            ),
            (
                {"head": "a" * 40},
                [],
                "Exported at an unrecorded time from aaaaaaaaaaaa.",
            ),
            (
                {"head": "a" * 40, "exported_at": 12345},
                [],
                "Exported at an unrecorded time from aaaaaaaaaaaa.",
            ),
            ({"head": 12345, "exported_at": "x"}, [], None),
            ({"head": True, "exported_at": "x"}, [], None),
            ({"remote": ["a"]}, ["--allow-unreadable-remote"], None),
            ({"remote": {"a": 1}}, ["--allow-unreadable-remote"], None),
        ],
        ids=[
            "both",
            "no time",
            "a time that is no string",
            "a head that is a number",
            "a head that is true",
            "a remote that is a list",
            "a remote that is an object",
        ],
    )
    def test_accepts_a_manifest_another_machine_wrote_and_says_what_it_read(
        self, take, capsys, tmp_path, fields, flags, line
    ):
        other = take("other")
        z = zipped(
            tmp_path / "z.zip",
            {"format": 1, "remote": "", **fields},
            [("seal/threads/w/design.md", "# w\n")],
        )
        code, out = said(capsys, other, "import", str(z), *flags)
        assert code == 0, out
        assert out.rstrip().endswith(CLOSING), out
        if line is None:
            assert "Exported at" not in out
        else:
            assert f"\n{line}\n" in out, out

    def test_accepts_a_name_taken_during_the_write_by_naming_it(
        self, take, exported, capsys, monkeypatch
    ):
        other = take("other")
        local = roots(other)[1]
        write(local, "follow-up.md", "# taken a moment ago\n")
        real = SEAL.place

        def raced(destination, data):
            if destination.endswith("follow-up.md"):
                return destination, SEAL.ADDED
            return real(destination, data)

        monkeypatch.setattr(SEAL, "place", raced)
        code, out = said(capsys, other, "import", str(exported))
        assert code == 0, out
        assert "  3 files added\n" in out
        assert (
            "  follow-up.md was not written — its name was taken during the import\n"
            in out
        )

    @pytest.mark.parametrize(
        "shape", ["not a repository", "no file", "not a zip", "cut in half"]
    )
    def test_refuses_a_path_that_is_no_zip_or_a_place_that_is_no_clone(
        self, take, exported, capsys, tmp_path, shape
    ):
        other = take("other")
        before = snapshot(other)
        cwd, path = other, tmp_path / "x.zip"
        if shape == "not a repository":
            cwd, path = tmp_path, exported
        elif shape == "not a zip":
            path.write_text("hello", encoding="utf-8")
        elif shape == "cut in half":
            data = exported.read_bytes()
            path.write_bytes(data[: len(data) // 2])
        code, out = said(capsys, cwd, "import", str(path))
        assert code == 1, out
        assert out == {
            "not a repository": "not inside a git repository — seal works on a clone\n",
            "no file": f"{path} is not a file\n",
        }.get(shape, out)
        assert snapshot(other) == before

    @pytest.mark.parametrize(
        "bound",
        ["members", "bytes", "the manifest's bytes", "the manifest's other spelling"],
    )
    def test_refuses_a_zip_past_a_bound_before_reading_it(
        self, take, capsys, tmp_path, bound
    ):
        other = take("other")
        before = snapshot(other)
        z = tmp_path / "big.zip"
        if bound == "members":
            many = [(f"seal/m{n}.md", "") for n in range(SEAL.MEMBER_COUNT_LIMIT + 1)]
            zipped(z, {"format": 1, "remote": ""}, many)
            want = "more than the 20000 this command will write."
        elif bound == "bytes":
            zipped(z, {"format": 1, "remote": ""}, [("seal/m.md", "m")])
            declare(z, "seal/m.md", SEAL.ARCHIVE_LIMIT + 1)
            want = f"more than the {SEAL.ARCHIVE_LIMIT} this command will read."
        else:
            name = (
                "manifest.json" if bound == "the manifest's bytes" else "manifest.json/"
            )
            with zipfile.ZipFile(z, "w") as archive:
                if name != "manifest.json":
                    archive.writestr(name, "")
                archive.writestr(
                    "manifest.json", json.dumps({"format": 1, "remote": ""})
                )
                archive.writestr("seal/m.md", "m")
            declare(z, name, SEAL.MEMBER_LIMIT + 1)
            want = f"bytes for manifest.json, more than the {SEAL.MEMBER_LIMIT} a manifest may hold."
        code, out = said(capsys, other, "import", str(z))
        assert code == 1, out
        assert want in out, out
        assert out.endswith("A root this large is not a root of records.\n")
        assert snapshot(other) == before

    @pytest.mark.parametrize(
        "damage",
        ["a record's data", "the manifest's data", "a method with no decompressor"],
    )
    def test_refuses_a_member_that_does_not_read_before_the_manifest(
        self, take, capsys, tmp_path, damage
    ):
        other = take("other")
        before = snapshot(other)
        z = tmp_path / "broken.zip"
        with zipfile.ZipFile(z, "w") as archive:
            archive.writestr(
                "manifest.json", json.dumps({"format": 1, "remote": "MARKER"})
            )
            archive.writestr("seal/first.md", "first\n")
            archive.writestr("seal/second.md", "second\n")
        raw = bytearray(z.read_bytes())
        if damage == "a method with no decompressor":
            for signature, at in ((b"PK\x03\x04", 8), (b"PK\x01\x02", 10)):
                start = 0
                while (found := raw.find(signature, start)) != -1:
                    raw[found + at : found + at + 2] = (99).to_bytes(2, "little")
                    start = found + 4
        else:
            text = b"second\n" if damage == "a record's data" else b"MARKER"
            at = raw.find(text)
            raw[at : at + 6] = text[:6].swapcase()
        z.write_bytes(bytes(raw))
        code, out = said(capsys, other, "import", str(z))
        assert code == 1, out
        assert out.startswith(f"{z} holds a member this command cannot read: "), out
        assert snapshot(other) == before

    @pytest.mark.parametrize(
        "manifest, want",
        [
            (None, "holds no manifest.json"),
            ({"format": 99}, "is format 99 and this build reads format 1"),
            ({}, "is format None"),
            (["not", "an", "object"], "manifest.json is not an object"),
        ],
        ids=["none", "a later format", "no format", "not an object"],
    )
    def test_refuses_a_manifest_this_build_cannot_read(
        self, take, capsys, tmp_path, manifest, want
    ):
        other = take("other")
        before = snapshot(other)
        z = zipped(tmp_path / "odd.zip", manifest, [("seal/follow-up.md", "x")])
        code, out = said(capsys, other, "import", str(z))
        assert code == 1, out
        assert want in out, out
        assert snapshot(other) == before

    def test_refuses_a_later_format_by_its_format_before_its_names(
        self, take, capsys, tmp_path
    ):
        """A later format is what moves the names the name checks read."""
        other = take("other")
        later = zipped(
            tmp_path / "later.zip", {"format": 2, "remote": ""}, [("records/a.md", "a")]
        )
        code, out = said(capsys, other, "import", str(later))
        assert code == 1, out
        assert "reads format 1" in out and "will not write" not in out

    @pytest.mark.parametrize(
        "name",
        [
            "seal/../../escape.md",
            "/etc/passwd",
            "seal/a\\..\\..\\b.md",
            "seal/nested/../../../out.md",
            "elsewhere/x.md",
            "seal/leak.md",
        ],
    )
    def test_refuses_a_member_it_has_no_place_for_and_writes_none(
        self, take, capsys, tmp_path, name
    ):
        other = take("other")
        before = snapshot(other)
        hostile = tmp_path / "hostile.zip"
        with zipfile.ZipFile(hostile, "w") as archive:
            archive.writestr("manifest.json", json.dumps({"format": 1, "remote": ""}))
            archive.writestr("seal/first.md", "first\n")
            info = zipfile.ZipInfo(name)
            if name == "seal/leak.md":
                info.external_attr = (0o120777 << 16) | 0o200000
            archive.writestr(info, "../agentic-implementer")
        code, out = said(capsys, other, "import", str(hostile))
        assert code == 1, out
        assert out.startswith(f"{hostile} holds members this command will not write:\n")
        assert snapshot(other) == before
        assert (
            not (tmp_path / "escape.md").exists() and not (tmp_path / "out.md").exists()
        )

    @pytest.mark.parametrize(
        "side",
        [
            "this clone",
            "the zip",
            "both",
            "the zip, as null",
            "the zip, as a number",
            "this clone, under the other flag",
        ],
    )
    def test_refuses_a_remote_either_side_could_not_read(
        self, take, exported, capsys, monkeypatch, tmp_path, side
    ):
        """Which side is silent decides the advice: a re-run here can clear
        this clone's git and never the zip's bytes."""
        other = take("other")
        before = snapshot(other)
        path = exported
        if side.startswith("the zip") or side == "both":
            manifest = {"format": 1}
            if side == "the zip, as null":
                manifest["remote"] = None
            elif side == "the zip, as a number":
                manifest["remote"] = 42
            path = zipped(tmp_path / "silent.zip", manifest, [("seal/a.md", "a")])
        if side.startswith("this clone") or side == "both":
            unanswered(
                monkeypatch, CONFIG_GET_REMOTE, (128, "", "fatal: bad config line 9\n")
            )
        flags = ["--allow-other-repo"] if side.endswith("other flag") else []
        code, out = said(capsys, other, "import", str(path), *flags)
        assert code == 1, out
        assert out.startswith(
            "whether this zip came from this repository cannot be answered:\n"
        )
        if side.startswith("this clone"):
            assert (
                "  this clone's remote could not be read: fatal: bad config line 9\n"
                in out
            )
            assert "Run this again if the failure here was transient" in out
        else:
            assert "export again on the machine that wrote it" in out
            assert "Run this again" not in out
        assert "--allow-unreadable-remote" in out
        assert snapshot(other) == before

    def test_refuses_a_zip_from_another_repository_naming_what_it_compared(
        self, take, exported, capsys, monkeypatch
    ):
        """This clone's remote is read once, and the value compared is the
        value printed."""
        other = take("other")
        git(other, "remote", "set-url", "origin", "https://example.com/org/elsewhere")
        before = snapshot(other)
        asks = unanswered(monkeypatch, CONFIG_GET_REMOTE, TIMED_OUT, after=1)
        code, out = said(capsys, other, "import", str(exported))
        assert code == 1, out
        assert len(asks) == 1
        assert out.startswith(
            "this zip was exported from another repository:\n"
            f"  the zip says   {SSH}\n"
            "  this clone is  https://example.com/org/elsewhere\n"
        ), out
        assert "pass --allow-other-repo." in out
        assert snapshot(other) == before

    @pytest.mark.parametrize("into", [["--into", "local"], ["--into", "shared"], []])
    def test_refuses_two_roots_whatever_into_says(self, take, exported, capsys, into):
        other = take("other")
        mark_root(other / "seal")
        before = snapshot(other)
        code, out = said(capsys, other, "import", str(exported), *into)
        assert code == 1, out
        assert out.startswith("both roots exist") and "read first" in out
        assert snapshot(other) == before

    @pytest.mark.parametrize("name", ["threads", "follow-up.md"])
    def test_refuses_a_link_where_a_record_goes(
        self, take, exported, capsys, tmp_path, name
    ):
        other = take("other")
        outside = tmp_path / "outside"
        outside.mkdir()
        target = outside if name == "threads" else outside / "follow-up.md"
        symlink_or_skip(str(target), os.path.join(roots(other)[1], name))
        code, out = said(capsys, other, "import", str(exported))
        assert code == 1, out
        assert out.startswith(f"seal/{name} in this clone is a symbolic link, and ")
        assert list(outside.iterdir()) == []

    def test_accepts_a_broken_link_at_the_fallback_name_by_taking_the_next(
        self, take, exported, capsys, tmp_path
    ):
        """`linked_path` sees the member's own name and not its fallbacks;
        `place` turns a link there down and the copy still lands."""
        other = take("other")
        local = roots(other)[1]
        write(local, "follow-up.md", "bytes that differ from the zip's\n")
        stolen = tmp_path / "stolen.md"
        symlink_or_skip(str(stolen), os.path.join(local, "follow-up.incoming.md"))
        code, out = said(capsys, other, "import", str(exported))
        assert code == 0, out
        assert not stolen.exists()
        assert os.path.isfile(os.path.join(local, "follow-up.incoming-2.md"))

    @pytest.mark.parametrize("held", ["in the zip", "a file here", "a pipe here"])
    def test_refuses_a_name_one_side_holds_as_a_file(
        self, take, capsys, tmp_path, held
    ):
        other = take("other")
        local = roots(other)[1]
        members = [("seal/a/b.md", "under it\n"), ("seal/zzz.md", "after it\n")]
        if held == "in the zip":
            members.insert(0, ("seal/a", "a file\n"))
        elif held == "a file here":
            write(local, "a", "already a file\n")
        else:
            fifo_or_skip(os.path.join(local, "a"))
        before = snapshot(other)
        z = zipped(tmp_path / "clash.zip", {"format": 1, "remote": ""}, members)
        code, out = said(capsys, other, "import", str(z))
        assert code == 1, out
        if held == "in the zip":
            assert "names seal/a as a file" in out
            assert "Ask the machine that exported it for another zip." in out
        else:
            assert out.startswith("seal/a in this clone is not a directory")
        assert snapshot(other) == before

    def test_refuses_a_directory_it_cannot_write_into_with_a_line_of_its_own(
        self, take, capsys, tmp_path
    ):
        other = take("other")
        shut = os.path.join(roots(other)[1], "threads")
        os.mkdir(shut)
        z = zipped(
            tmp_path / "into.zip",
            {"format": 1, "remote": ""},
            [("seal/threads/x.md", "x")],
        )
        os.chmod(shut, 0o555)
        try:
            if os.access(shut, os.W_OK):
                pytest.skip("this filesystem ignores the directory's write bit")
            code, out = said(capsys, other, "import", str(z))
        finally:
            os.chmod(shut, 0o755)
        assert code == 1, out
        assert out.startswith("the copy stopped part-way: ")
        assert "run this again" in out


class Test_write_members:
    def test_accepts_each_record_and_counts_it(self, tmp_path):
        into = tmp_path / "root"
        write(into, "follow-up.md", "mine\n")
        z = tmp_path / "z.zip"
        with zipfile.ZipFile(z, "w") as archive:
            archive.writestr("manifest.json", "{}")
            archive.writestr(zipfile.ZipInfo("seal/threads/"), "")
            archive.writestr("seal/threads/w/design.md", "w\n")
            archive.writestr("seal/follow-up.md", "theirs\n")
        with opened(z) as archive:
            counts, collisions, refused = SEAL.write_members(archive, str(into))
        assert counts == {"added": 1, "identical": 0, "collided": 1}
        assert collisions == [("follow-up.md", "follow-up.incoming.md")]
        assert refused == []
        assert listed(into) == [
            "follow-up.incoming.md",
            "follow-up.md",
            "threads/w/design.md",
        ]

    def test_refuses_a_name_that_became_a_link_and_names_it(
        self, tmp_path, monkeypatch
    ):
        """`place` turning a link down is a check a race can pass, so the
        write asks again; here `place` hands back the name a raced check
        would have, with `O_EXCL` gone as on Windows."""
        into, outside = tmp_path / "root", tmp_path / "outside"
        into.mkdir()
        outside.mkdir()
        symlink_or_skip(str(outside / "stolen.md"), str(into / "follow-up.md"))
        monkeypatch.setattr(
            SEAL, "place", lambda destination, data: (destination, SEAL.ADDED)
        )
        without_o_excl(monkeypatch)
        z = zipped(tmp_path / "z.zip", None, [("seal/follow-up.md", "FROM THE ZIP")])
        with opened(z) as archive:
            counts, collisions, refused = SEAL.write_members(archive, str(into))
        assert list(outside.iterdir()) == []
        assert (counts["added"], collisions, refused) == (0, [], ["follow-up.md"])


class Test_ending_of:
    def test_accepts_the_lines_own_ending(self):
        assert SEAL.ending_of("a\r\n", "\n") == "\r\n"

    def test_refuses_a_line_with_none_by_the_fallback(self):
        assert [SEAL.ending_of(line, "\r\n") for line in ("a", "")] == ["\r\n"] * 2


class Test_line_ending:
    def test_accepts_the_first_ending_the_file_has(self):
        assert SEAL.line_ending(["a", "b\r\n", "c\n"]) == "\r\n"

    def test_refuses_a_file_with_no_ending_by_a_newline(self):
        assert SEAL.line_ending(["no ending"]) == "\n"


class Test_doubled_modes:
    @pytest.mark.parametrize("text", [HEAD, mode_row("local")], ids=["none", "one"])
    def test_accepts_one_mode_row_or_none(self, text):
        assert SEAL.doubled_modes(text.splitlines(keepends=True)) == ""

    def test_refuses_two_rows_naming_each_line(self):
        said_why = SEAL.doubled_modes(TWO_MODE_ROWS.splitlines(keepends=True))
        assert said_why.startswith(f"holds 2 `Mode` rows ({NAMES_BOTH_ROWS}), and "), (
            said_why
        )


class Test_with_row:
    @pytest.mark.parametrize(
        "text, want",
        [
            (
                "| Item | Value |\r\n|---|---|\r\n| Mode | local |\r\n",
                "| Item | Value |\r\n|---|---|\r\n| Mode | shared |\r\n",
            ),
            (
                HEAD + "| Record language | Korean |\n\nprose\n",
                HEAD + "| Record language | Korean |\n| Mode | shared |\n\nprose\n",
            ),
            (
                HEAD + "| Record language | Korean |",
                HEAD + "| Record language | Korean |\n| Mode | shared |\n",
            ),
            (HEAD + "\nprose\n", HEAD + "| Mode | shared |\n\nprose\n"),
            (
                "# notes\n\nnothing here.",
                "# notes\n\nnothing here.\n\n" + HEAD + "| Mode | shared |\n",
            ),
            ("", HEAD + "| Mode | shared |\n"),
        ],
        ids=[
            "a row replaced, its ending kept",
            "a row added at the table's end",
            "a row added under a last line with no ending",
            "a row added under the delimiter",
            "a table added to a file with none",
            "a table for an empty file",
        ],
    )
    def test_accepts_a_file_with_one_row_or_none_and_keeps_every_other_byte(
        self, text, want
    ):
        assert SEAL.with_row(text, "shared") == (want, "")

    @pytest.mark.parametrize(
        "text, why",
        [
            (TWO_MODE_ROWS, f"holds 2 `Mode` rows ({NAMES_BOTH_ROWS})"),
            (WALKED_PAST, STOPS_AT),
        ],
        ids=["two rows", "a table the walker refused"],
    )
    def test_refuses_a_file_with_no_row_to_replace(self, text, why):
        new, said_why = SEAL.with_row(text, "shared")
        assert new is None
        assert why in said_why, said_why

    def test_the_writer_inserts_where_the_walk_says_the_table_ends(self, tmp_path):
        """#871, S5. The writer's insertion point is read off the walk's own
        line numbers: after the last row the walk read, or under the delimiter
        row where the table holds no row yet; and it overwrites the one line the
        walk read as the `Mode` row. Shape 12, whose header the stop rule's
        pattern did not match, is one of each: seen red against the stop rule's
        writer, which appended a second table to the end of the file."""
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
        spec = importlib.util.spec_from_file_location("agentic_seal_for_871", path)
        seal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(seal)

        indented = config_shapes.SHAPES[12]
        assert seal.with_row(indented, "local") == (
            indented.replace("| Mode | shared |", "| Mode | local |"),
            "",
        )
        no_mode = indented.replace("| Mode | shared |", "| Record language | Korean |")
        assert seal.with_row(no_mode, "local") == (no_mode + "| Mode | local |\n", "")
        empty = "# c\n\n | Item | Value |\n|---|---|\n\nprose below.\n"
        assert seal.with_row(empty, "local") == (
            "# c\n\n | Item | Value |\n|---|---|\n| Mode | local |\n\nprose below.\n",
            "",
        )

    def test_the_fence_rule_answers_the_same_for_a_crlf_file(self, config, tmp_path):
        """A7. The reader walks `splitlines()` while the writer splits with
        `splitlines(keepends=True)`, so the shared rule is the one place the two
        spellings have to meet. Round 3 of #415 measured CRLF for the existing
        walks; this is the same measurement for the answers this work item adds,
        and since #871 for the walker's refusal as well."""
        assert config.config_rows(crlf(FENCED_ABOVE)) == config.config_rows(
            FENCED_ABOVE
        )
        assert config.config_rows(crlf(FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN)) == []
        assert config.config_table(crlf(FENCED_REFUSAL)) == config.config_table(
            FENCED_REFUSAL
        )

        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
        spec = importlib.util.spec_from_file_location("agentic_seal_for_429_crlf", path)
        seal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(seal)
        written, refused = seal.with_row(crlf(FENCED_ABOVE), "local")
        assert refused == "", refused
        assert "| Mode | local |\r\n| Broad gate | EXAMPLE |\r\n```" in written, (
            f"the writer rewrote the fenced row of a CRLF file:\n{written!r}"
        )
        assert written.count("\n") == written.count("\r\n"), (
            f"the write left a file in two endings:\n{written!r}"
        )


class Test_write_row:
    @pytest.mark.parametrize(
        "text, want",
        [
            (None, SEAL.NEW_CONFIG.format(item="Mode", value="shared")),
            (
                "# c\r\n\r\n| Item | Value |\r\n|---|---|\r\n| Mode | local |\r\n",
                "# c\r\n\r\n| Item | Value |\r\n|---|---|\r\n| Mode | shared |\r\n",
            ),
        ],
        ids=["no file", "a CRLF file"],
    )
    def test_accepts_a_row_it_can_read_back(self, tmp_path, text, want):
        if text is not None:
            (tmp_path / "config.md").write_bytes(text.encode())
        assert SEAL.write_row(str(tmp_path), "shared") == ""
        assert (tmp_path / "config.md").read_bytes() == want.encode()

    @pytest.mark.parametrize(
        "shape",
        [
            "a link",
            "a directory",
            "two rows",
            "an unclosed fence",
            "bytes that are not utf-8",
        ],
    )
    def test_refuses_a_file_it_cannot_write_the_row_into_and_leaves_it(
        self, tmp_path, shape
    ):
        path = tmp_path / "config.md"
        before = None
        if shape == "a link":
            symlink_or_skip(str(tmp_path / "nowhere.md"), str(path))
        elif shape == "a directory":
            path.mkdir()
        else:
            before = {
                "two rows": TWO_MODE_ROWS.encode(),
                "an unclosed fence": UNCLOSED_FENCE.encode(),
                "bytes that are not utf-8": b"\xff| Mode | local |\n",
            }[shape]
            path.write_bytes(before)
        said_why = SEAL.write_row(str(tmp_path), "shared")
        assert said_why.startswith(str(path)), said_why
        assert {
            "a link": " is a symbolic link",
            "a directory": " is a directory",
            "two rows": f" holds 2 `Mode` rows ({NAMES_BOTH_ROWS})",
            "an unclosed fence": " has a fenced code block that is never closed",
            "bytes that are not utf-8": " could not be read: ",
        }[shape] in said_why, said_why
        if before is not None:
            assert path.read_bytes() == before
        assert not (tmp_path / "nowhere.md").exists()

    def test_seal_mode_writes_one_row_where_the_mode_row_sits_below_a_piped_row(
        self, config, tmp_path
    ):
        """A3, and `questions.md` M1 — **executed 2026-09-17, and it duplicated.**

        The reader and the writer read one table, so when the reader stopped
        above the `Mode` row the writer stopped there too: `declared_mode`
        answered *none*, `table_span` returned no `Mode` row, and `with_row`
        inserted a second one ABOVE the piped line while the person's own row sat
        below it. Measured on the tree before this change — two `| Mode |` rows in
        a person's file, which `table_span`'s own comment says no command can
        bring back into agreement. It is the worst outcome in this work item and
        the strongest argument for teaching the reader the escape.

        This calls `write_row`, which is the unit `seal mode` calls when the row
        reads as undeclared (`seal.py#mode`), rather than a helper beside it.

        **Nothing is asserted before the write.** What the reader answered is
        read into the failure message instead, because a guard that fires first
        takes the case's own subject — the file two rows deep — off the screen.
        """
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
        spec = importlib.util.spec_from_file_location("agentic_seal_for_415", path)
        seal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(seal)

        home = tmp_path / "seal"
        home.mkdir()
        write_config(home, PIPED_TABLE)
        read_as = seal.declared(str(home))
        refused = seal.write_row(str(home), "shared")
        written = (home / "config.md").read_text(encoding="utf-8")
        assert written.count("| Mode |") == 1, (
            f"the person's file is {written.count('| Mode |')} `Mode` rows deep, "
            f"and no command brings it back into agreement. The reader answered "
            f"{read_as} for a file whose own row says `shared`:\n{written}"
        )
        assert refused == "", refused
        assert read_as == ("mode", "shared"), (
            "the writer stopped where the reader stopped, which is the agreement "
            "the two keep by reading one parser"
        )

    def test_seal_mode_writes_nothing_under_a_bare_pipe_and_names_the_line(
        self, config, tmp_path
    ):
        """The inverse of round 1's 🟡 4 of #415, which #871 closes.

        Written bare, the line was no row, so the reader stopped above the
        person's `Mode` row, the writer stopped where the reader stopped, and the
        file came back two rows deep -- pinned as a limitation until now. The
        walker refuses the line instead: the `Mode` row under it is a refusal,
        never an absent row, so the writer has no row to add, and it writes
        nothing and names the line. Seen red against the stop rule's writer: the
        write returned `""` and the file held two `Mode` rows.
        """
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
        spec = importlib.util.spec_from_file_location("agentic_seal_for_415_bare", path)
        seal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(seal)

        home = tmp_path / "seal"
        home.mkdir()
        write_config(home, BARE_TABLE)
        kind, _said = config.declared_mode(str(home))
        assert kind == "refused", kind
        said = seal.write_row(str(home), "shared")
        assert said.startswith(
            str(home / "config.md") + " has a `Item | Value` table"
        ), said
        assert "stops at `| Broad gate | bin/test -q | tee out.txt |`" in said, said
        assert said.endswith("Nothing was written"), said
        assert (home / "config.md").read_text(encoding="utf-8") == BARE_TABLE

    def test_the_writer_and_the_reader_agree_about_which_row_is_the_row(
        self, config, tmp_path
    ):
        """A4. The WRITER locates the line `with_row` overwrites, and since #871
        it locates it by the reader's own walk, `config_table`. A writer reading
        the table any other way rewrites the `Mode` row inside somebody's pasted
        example while every gate reads the live one: a file two rows deep that
        no command can bring into agreement.

        Asserted on the BYTES, not on the reader's answer: what makes this case
        the writer's is that the fenced line comes back byte-identical and
        exactly one line of the file changed.
        """
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
        spec = importlib.util.spec_from_file_location("agentic_seal_for_429", path)
        seal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(seal)

        before = FENCED_ABOVE.replace("| Mode | shared |", "| Mode | local |")
        home = tmp_path / "seal"
        home.mkdir()
        write_config(home, before)
        assert seal.write_row(str(home), "shared") == ""
        after = (home / "config.md").read_text(encoding="utf-8")

        assert "| Mode | local |\n| Broad gate | EXAMPLE |\n```" in after, (
            f"the writer rewrote the row inside the example block:\n{after}"
        )
        changed = [
            (i, was, now)
            # `strict=True`: a write that INSERTED a row leaves the two files
            # different lengths, and a silent truncation here would hide exactly
            # the outcome this case is about.
            for i, (was, now) in enumerate(
                zip(before.splitlines(), after.splitlines(), strict=True)
            )
            if was != now
        ]
        assert len(changed) == 1, f"the write touched {len(changed)} lines:\n{changed}"
        assert changed[0][2] == "| Mode | shared |", changed
        assert changed[0][0] > after.splitlines().index("```"), (
            "the line that changed is inside the fence, not in the live table"
        )

        # #871, S5: a table the walker refuses is one the writer refuses too,
        # in the shape a doubled `Mode` row takes -- `(None, the sentence)` --
        # and the file's bytes are left exactly as they were. Seen red against
        # the stop rule's writer, which inserted a second `Mode` row under the
        # last row above the bare pipe.
        refused_shape = config_shapes.SHAPES[7]
        assert seal.with_row(refused_shape, "local") == (
            None,
            config.config_table(refused_shape)[1][0],
        )
        shape_home = tmp_path / "shape-7" / "seal"
        shape_home.mkdir(parents=True)
        write_config(shape_home, refused_shape)
        said = seal.write_row(str(shape_home), "local")
        assert said.endswith("Nothing was written"), said
        assert (shape_home / "config.md").read_text(encoding="utf-8") == refused_shape

    def test_a_row_that_would_land_inside_an_unclosed_fence_is_refused(
        self, config, tmp_path
    ):
        """Round 1's 🔴. The writer's claim is that the row reads back.

        A fence nobody closed runs to the end of the file, so `table_span` sees no
        table at all and `with_row` falls to its third arm and appends one at the
        END — which is inside that fence. `write_row` returned `""`, `seal mode`
        printed *one was written from where the folder is*, and `declared_mode`
        still answered `('none', '')`: the mode gate asks again next session, and
        the file grows by a table a run. Measured before the fix over both
        fixtures below, three runs each — 9 → 13 → 17 → 21 lines and 4 → 8 → 12 →
        16, `('none', '')` throughout.

        **A regression this branch introduced.** At `release/v0.12.1` the fenced
        table was visible to the writer, so the row it rewrote was read back.

        The third fixture is the shape A4 pins — a fence that IS closed above a
        live table — and it is here so that a refusal wide enough to swallow it
        turns this case red rather than passing quietly.
        """
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
        spec = importlib.util.spec_from_file_location("agentic_seal_unclosed", path)
        seal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(seal)

        for name, before in (
            (
                "live_table_under_an_unclosed_fence",
                "# Repository config\n\nAn example of the format:\n\n```markdown\n"
                "| Item | Value |\n|---|---|\n| Mode | shared |\n",
            ),
            (
                "only_a_fenced_example_never_closed",
                "```markdown\n| Item | Value |\n|---|---|\n| Mode | shared |\n",
            ),
        ):
            home = tmp_path / name / "seal"
            home.mkdir(parents=True)
            write_config(home, before)
            failed = seal.write_row(str(home), "shared")
            assert "never closed" in failed, (
                f"{name}: the write reported success for a row no walk reads:\n{failed!r}"
            )
            assert (home / "config.md").read_text(encoding="utf-8") == before, (
                f"{name}: a refused write touched the person's file"
            )
            assert config.declared_mode(str(home)) == ("none", ""), (
                f"{name}: the reader's answer moved under a refused write"
            )

        closed = tmp_path / "closed" / "seal"
        closed.mkdir(parents=True)
        write_config(
            closed, FENCED_ABOVE.replace("| Mode | shared |", "| Mode | local |")
        )
        assert seal.write_row(str(closed), "shared") == "", (
            "the refusal reaches a file whose fence is closed and whose live "
            "table is right there"
        )
        assert config.declared_mode(str(closed)) == ("mode", "shared")

    def test_a_file_whose_last_line_has_no_ending_gets_its_row_on_a_line(
        self, config, tmp_path, monkeypatch
    ):
        """Round 2's 🔴, both acts of it.

        `with_row`'s insert arm put the new row at the end of the file without
        terminating the line already there, so
        `| Record language | Korean || Mode | shared |` came back as one line of
        four cells and `config_rows` of it was `[]` — both rows gone. At
        `release/v0.12.1` that was written silently and cost the row the person
        already had; round 1's guard stopped the write and then blamed a fence the
        file does not have, which is the wrong-cause shape this work item is about
        arriving from its own repair.

        **The second half is the message, and it is pinned separately** because
        fixing the first half is what makes the guard unreachable for this shape.
        A residual cause is driven through the same unit with `with_row` replaced
        by one that changes nothing: the refusal must not name a fence in a file
        that has none.
        """
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
        spec = importlib.util.spec_from_file_location("agentic_seal_no_ending", path)
        seal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(seal)

        no_ending = "| Item | Value |\n|---|---|\n| Record language | Korean |"
        home = tmp_path / "no_ending" / "seal"
        home.mkdir(parents=True)
        write_config(home, no_ending)
        assert seal.write_row(str(home), "shared") == "", (
            "the write is refused over a file with no fence in it at all"
        )
        written = (home / "config.md").read_text(encoding="utf-8")
        assert "Korean || Mode" not in written, (
            f"the new row was welded onto the line already there:\n{written!r}"
        )
        assert config.config_rows(written) == [
            ("Record language", "Korean"),
            ("Mode", "shared"),
        ], f"the person's own row did not survive the write:\n{written!r}"
        assert config.declared_mode(str(home)) == ("mode", "shared")

        stuck = tmp_path / "stuck" / "seal"
        stuck.mkdir(parents=True)
        write_config(stuck, no_ending)
        monkeypatch.setattr(seal, "with_row", lambda text, value: (text, ""))
        refused = seal.write_row(str(stuck), "shared")
        assert "would not read the `Mode` row back" in refused, refused
        assert "fence" not in refused, (
            f"the refusal names a fence in a file that has none:\n{refused}"
        )
        assert (stuck / "config.md").read_text(encoding="utf-8") == no_ending

    @pytest.mark.parametrize("name", ["LS", "FF"])
    def test_the_writer_reads_where_commonmark_breaks(self, config, tmp_path, name):
        """#667 round 1, 🟡 1, the writer's walk: the writer never appends a
        second table under a `<!--` a renderer reads mid-line.

        Re-pinned by #871: the writer reads the table the reader reads, and the
        walker refuses this one (`test_a_break_commonmark_does_not_honour_hides_
        no_config_row` says why), so the writer refuses it too and the file's
        bytes are left exactly as they were -- no second table, and no row
        rewritten in a table the walk could not read whole."""
        from block_shapes import BREAKS, OPEN

        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
        spec = importlib.util.spec_from_file_location("agentic_seal_for_667_r1", path)
        seal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(seal)

        before = (
            f"A note{BREAKS[name]}{OPEN}\n\n| Item | Value |\n|---|---|\n"
            "| Mode | local |\n-->\n"
        )
        home = tmp_path / "seal"
        home.mkdir()
        write_config(home, before)
        said = seal.write_row(str(home), "shared")
        assert said.endswith("Nothing was written"), said
        after = (home / "config.md").read_text(encoding="utf-8")
        assert after == before, after

    def test_the_writer_leaves_a_commented_row_alone(self, config, tmp_path):
        """S6, C10. The writer's walk located the FIRST `Mode` line -- the
        commented one -- so `seal mode` rewrote a row nobody reads while the live
        row kept its old value. Asserted on the bytes. Red at base.

        Re-pinned by #871: the comment sits directly under the delimiter row, so
        GFM ends the table there and the live `Mode` row below it is a row the
        walk never reaches. The reader refuses it, and the writer refuses with
        it: neither the commented row nor the live one is rewritten."""
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
        spec = importlib.util.spec_from_file_location("agentic_seal_for_667", path)
        seal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(seal)

        before = shape_text("C10")
        home = tmp_path / "seal"
        home.mkdir()
        write_config(home, before)
        said = seal.write_row(str(home), "shared")
        assert UNDER_THE_COMMENT.replace("shared", "local") in said, said
        after = (home / "config.md").read_text(encoding="utf-8")
        assert after == before, (
            f"the writer rewrote the commented row, or the live one:\n{after}"
        )
        assert config.declared_mode(str(home))[0] == "refused"

    def test_a_refused_append_names_the_walkers_cause_not_a_defect(
        self, config, tmp_path
    ):
        """#871 round 1, 🟡 2. A file with no table and an HTML comment that
        never closes: `with_row` appends a table, the walker refuses the
        appended header as inside that block, and `write_row` says so — the
        walker's sentence — rather than calling it a defect in the command. Seen
        red against the generic read-back sentence."""
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
        spec = importlib.util.spec_from_file_location("agentic_seal_for_871_r1", path)
        seal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(seal)
        from block_shapes import OPEN

        before = f"# Repository config\n\n{OPEN} a note nobody closed\n"
        home = tmp_path / "seal"
        home.mkdir()
        write_config(home, before)
        said = seal.write_row(str(home), "shared")
        assert "inside an HTML block opened above it and never closed" in said, said
        assert "defect in this command" not in said, said
        assert (home / "config.md").read_text(encoding="utf-8") == before


class Test_porcelain:
    def test_accepts_a_tree_as_the_lines_under_the_paths_asked(self, take):
        repo = take("shared")
        write(repo, "seal/follow-up.md", "# changed\n")
        write(repo, "f2.txt", "outside\n")
        assert SEAL.porcelain(str(repo), "seal") == [" M seal/follow-up.md"]
        assert SEAL.porcelain(str(repo), "f.txt") == []

    def test_refuses_a_git_that_cannot_answer_as_a_line_of_its_own(
        self, tmp_path, monkeypatch
    ):
        (line,) = SEAL.porcelain(str(tmp_path), "seal")
        assert line.startswith("fatal: ")
        unanswered(monkeypatch, ["--", "seal"], OSError("boom"))
        assert SEAL.porcelain(str(tmp_path), "seal") == [
            "git status could not be run (boom)"
        ]


class Test_indexed:
    @pytest.mark.parametrize(
        "line, moved",
        [
            ("?? seal/x.md", False),
            (" M seal/config.md", False),
            ("D  seal/x.md", True),
            (" D seal/x.md", True),
        ],
        ids=[
            "untracked",
            "the row this command wrote",
            "a staged deletion, moved",
            "a deletion, moved",
        ],
    )
    def test_accepts_what_the_index_cannot_lose(self, line, moved):
        assert not SEAL.indexed(line, moved=moved)

    @pytest.mark.parametrize(
        "line, moved",
        [
            (" M seal/ledger.md", False),
            ("M  seal/config.md", False),
            ("MM seal/config.md", False),
            ("D  seal/x.md", False),
            ("AD seal/x.md", True),
            ("fatal: not a git repository", False),
        ],
        ids=[
            "a modification",
            "the row staged",
            "the row staged and modified",
            "a deletion, not moved",
            "an addition then a deletion, moved",
            "a line git could not produce",
        ],
    )
    def test_refuses_what_git_rm_cached_would_drop(self, line, moved):
        assert SEAL.indexed(line, moved=moved)


class Test_tracked:
    def test_accepts_a_path_git_tracks_something_under(self, _worlds):
        assert SEAL.tracked(str(_worlds / "shared"), "seal")

    def test_refuses_a_path_git_tracks_nothing_under_or_cannot_read(
        self, _worlds, tmp_path
    ):
        assert not SEAL.tracked(str(_worlds / "shared"), "nothing-here")
        assert not SEAL.tracked(str(tmp_path), "seal")


class Test_other_worktrees:
    def test_accepts_a_linked_worktree_by_its_path(self, take, tmp_path):
        repo = take("shared")
        git(repo, "worktree", "add", "-q", str(tmp_path / "linked"), "feature/x")
        found = SEAL.other_worktrees(str(repo))
        assert [os.path.realpath(p) for p in found] == [
            os.path.realpath(tmp_path / "linked")
        ]

    def test_refuses_the_clone_itself_and_a_directory_outside_git(
        self, _worlds, tmp_path
    ):
        assert SEAL.other_worktrees(str(_worlds / "shared")) == []
        assert SEAL.other_worktrees(str(tmp_path)) == []


class Test_plugin_version:
    def test_accepts_the_version_the_plugin_names(self, tmp_path, monkeypatch):
        monkeypatch.setattr(SEAL, "PLUGIN_ROOT", plugin_at(tmp_path))
        assert SEAL.plugin_version() == "1.2.3"

    @pytest.mark.parametrize(
        "text",
        [None, "not json", "[1]", '{"version": 3}'],
        ids=["no file", "not json", "a list", "a number"],
    )
    def test_refuses_a_version_it_cannot_read_as_none(
        self, tmp_path, monkeypatch, text
    ):
        monkeypatch.setattr(SEAL, "PLUGIN_ROOT", plugin_at(tmp_path, text, None))
        assert SEAL.plugin_version() == ""


class Test_plugin_workflow:
    def test_accepts_the_template_pinned_to_the_version(self, tmp_path, monkeypatch):
        monkeypatch.setattr(SEAL, "PLUGIN_ROOT", plugin_at(tmp_path))
        assert SEAL.plugin_workflow() == "--branch v1.2.3\n"

    @pytest.mark.parametrize(
        "version, template",
        [
            (None, "--branch v<version>\n"),
            ('{"version": "1.2.3"}', None),
            ('{"version": "1.2.3"}', "--branch main\n"),
        ],
        ids=["no version", "no template", "no placeholder"],
    )
    def test_refuses_what_it_could_not_pin(
        self, tmp_path, monkeypatch, version, template
    ):
        monkeypatch.setattr(SEAL, "PLUGIN_ROOT", plugin_at(tmp_path, version, template))
        assert SEAL.plugin_workflow() == ""


# The clone line every workflow a release before 0.23.0 wrote carries: the
# repository under its name before #1051.
OLD_CLONE = "https://github.com/MichaelYcJo/SpecSeal.git"


def old_slug_workflow(pin="v0.22.4"):
    """The workflow a release before 0.23.0 wrote: this release's template,
    cloned at the old slug and pinned to an old release."""
    return (
        SEAL.plugin_workflow()
        .replace(SEAL.PLUGIN_CLONE, OLD_CLONE)
        .replace(f"v{SEAL.plugin_version()}", pin)
    )


class Test_workflow_at:
    def test_accepts_the_file_this_plugin_writes_as_its_own(self, take):
        repo = take("shared")
        workflow_in(repo, SEAL.plugin_workflow(), commit=False)
        assert SEAL.workflow_at(str(repo)) == ("plugin", SEAL.plugin_workflow())

    def test_accepts_a_file_cloning_the_old_slug_as_its_own(self, take):
        """#1051: through 0.23.x a workflow carrying the clone line of the
        repository's name before the rename is this plugin's, so the report,
        the install and the removal treat it as they treat their own."""
        repo = take("shared")
        old = old_slug_workflow()
        workflow_in(repo, old, commit=False)
        assert SEAL.workflow_at(str(repo)) == ("plugin", old)

    @pytest.mark.parametrize(
        "shape, kind",
        [
            ("absent", "absent"),
            ("a link", "link"),
            ("not utf-8", "unreadable"),
            ("no clone line", "other"),
        ],
    )
    def test_refuses_every_other_file_as_not_this_plugins(
        self, take, tmp_path, shape, kind
    ):
        """One rule tells this plugin's file from somebody else's: a regular
        file that reads and carries the plugin's clone line."""
        repo = take("shared")
        path = os.path.join(str(repo), WORKFLOW_PATH)
        if shape == "a link":
            os.makedirs(os.path.dirname(path))
            symlink_or_skip(str(tmp_path / "nowhere.yml"), path)
        elif shape == "not utf-8":
            workflow_in(repo, "x", commit=False)
            open(path, "wb").write(b"\xff" + SEAL.PLUGIN_CLONE.encode())
        elif shape == "no clone line":
            workflow_in(repo, "name: hygiene\njobs: {}\n", commit=False)
        assert SEAL.workflow_at(str(repo))[0] == kind


class Test_pinned:
    def test_accepts_the_release_the_clone_line_names(self):
        assert SEAL.pinned("git clone --depth 1 --branch v1.2.3 \\\n") == "v1.2.3"

    def test_refuses_a_file_naming_no_release(self):
        assert SEAL.pinned("name: hygiene\n") == ""


class Test_install_workflow:
    def test_accepts_a_shared_root_by_writing_it_pinned_and_staged(self, take):
        repo = take("shared")
        version = SEAL.plugin_version()
        assert SEAL.install_workflow(str(repo)) == (
            "written",
            f"wrote .github/workflows/hygiene.yml (pinned to v{version}) and staged it",
        )
        text = open(os.path.join(str(repo), WORKFLOW_PATH), encoding="utf-8").read()
        assert SEAL.PLACEHOLDER not in text and f"--branch v{version}" in text
        assert staged(repo) == ".github/workflows/hygiene.yml\n"

    def test_accepts_its_own_file_already_there_by_naming_the_pin(self, take):
        """S5: a repository set up by an older release keeps its file and its
        pin; installing again writes nothing."""
        repo = take("shared")
        old = SEAL.plugin_workflow().replace(f"v{SEAL.plugin_version()}", "v0.1.0")
        path = workflow_in(repo, old)
        assert SEAL.install_workflow(str(repo)) == (
            "installed",
            ".github/workflows/hygiene.yml is already this plugin's, pinned to "
            "v0.1.0, so nothing was written",
        )
        assert open(path, encoding="utf-8").read() == old and staged(repo) == ""

    def test_accepts_its_own_file_under_the_old_slug_by_rewriting_it(self, take):
        """#1051: a workflow a release before the rename wrote clones the
        plugin from the repository's old name. Install writes the template
        over it, at the new slug and pinned to this release, and stages it."""
        repo = take("shared")
        path = workflow_in(repo, old_slug_workflow())
        version = SEAL.plugin_version()
        assert SEAL.install_workflow(str(repo)) == (
            "written",
            f"rewrote .github/workflows/hygiene.yml, which cloned the plugin "
            f"from the repository's name before the rename, at the new name "
            f"(pinned to v{version}) and staged it",
        )
        assert open(path, encoding="utf-8").read() == SEAL.plugin_workflow()
        assert staged(repo) == ".github/workflows/hygiene.yml\n"

    @pytest.mark.parametrize(
        "shape, kind",
        [
            ("no shared root", "no-root"),
            ("a project's own seal", "no-root"),
            ("a file there", "kept"),
            ("no version", "no-version"),
            ("no template", "unreadable"),
            ("no placeholder", "no-placeholder"),
            ("an ignored directory", "unstaged"),
        ],
    )
    def test_refuses_to_overwrite_or_to_write_what_it_cannot_pin_or_stage(
        self, take, tmp_path, monkeypatch, shape, kind
    ):
        no_root = ("no shared root", "a project's own seal")
        repo = take("local" if shape in no_root else "shared")
        path = os.path.join(str(repo), WORKFLOW_PATH)
        if shape == "a file there":
            workflow_in(repo, "name: someone else's\n", commit=False)
        elif shape == "an ignored directory":
            write(repo, ".gitignore", ".github/\n")
            commit_everything_as_e(repo, "ignore the workflow's directory")
        elif shape == "a project's own seal":
            write(repo, "seal/README.md", "# seal\n\nThis package's notes.\n")
        elif shape not in no_root:
            version, template = '{"version": "1.2.3"}', "--branch v<version>\n"
            if shape == "no version":
                version = None
            elif shape == "no template":
                template = None
            else:
                template = "--branch main\n"
            monkeypatch.setattr(
                SEAL, "PLUGIN_ROOT", plugin_at(tmp_path / "p", version, template)
            )
        found, line = SEAL.install_workflow(str(repo))
        assert found == kind, line
        if shape == "a file there":
            assert open(path, encoding="utf-8").read() == "name: someone else's\n"
            assert "is not this plugin's file, so nothing was written" in line
        elif shape == "an ignored directory":
            assert os.path.isfile(path) and staged(repo) == ""
            assert "`git add -f :/.github/workflows/hygiene.yml`" in line
        else:
            assert not os.path.lexists(path)
            assert "was NOT written" in line
        if shape in no_root:
            assert (
                "the checks read committed records" in line
                and "`seal mode shared` puts it in the tree" in line
            )
        if shape == "no version":
            assert (
                "version could not be read" in line and "templates/hygiene.yml" in line
            )


class Test_remove_workflow:
    @pytest.mark.parametrize(
        "tracked", [True, False], ids=["tracked", "untracked, this plugin's bytes"]
    )
    def test_accepts_the_file_this_plugin_wrote(self, take, tracked):
        repo = take("shared")
        path = workflow_in(repo, SEAL.plugin_workflow(), commit=tracked)
        found, line = SEAL.remove_workflow(str(repo))
        assert found == "removed", line
        assert not os.path.lexists(path)
        if tracked:
            assert (
                line == "removed .github/workflows/hygiene.yml and staged the removal"
            )
            assert any(entry.startswith("D  .github/") for entry in status(repo))
        else:
            assert "untracked, and byte for byte this plugin's" in line
            assert "`seal pr-checks install` writes it back" in line

    @pytest.mark.parametrize(
        "shape, why",
        [
            ("absent", "there is no .github/workflows/hygiene.yml"),
            ("a link", "is a symbolic link, so it is not this plugin's file"),
            ("not utf-8", "could not be read ("),
            ("not this plugin's", "was not written by this plugin"),
            ("untracked, other bytes", "is not tracked and is not byte for byte"),
        ],
    )
    def test_refuses_a_file_this_plugin_cannot_put_back(
        self, take, tmp_path, shape, why
    ):
        repo = take("shared")
        path = os.path.join(str(repo), WORKFLOW_PATH)
        if shape == "a link":
            os.makedirs(os.path.dirname(path))
            symlink_or_skip(str(tmp_path / "nowhere.yml"), path)
        elif shape == "not utf-8":
            workflow_in(repo, "x", commit=False)
            open(path, "wb").write(b"\xff" + SEAL.PLUGIN_CLONE.encode())
        elif shape == "not this plugin's":
            workflow_in(repo, "name: hygiene\njobs: {}\n")
        elif shape == "untracked, other bytes":
            workflow_in(
                repo, "# somebody's own\n" + SEAL.PLUGIN_CLONE + "\n", commit=False
            )
        found, line = SEAL.remove_workflow(str(repo))
        assert found == ("absent" if shape == "absent" else "kept"), line
        assert why in line, line
        assert os.path.lexists(path) == (shape != "absent")
        assert "local mode" not in line, line


class Test_say_report:
    def where(self, tmp_path):
        return str(tmp_path), str(tmp_path / ".git" / "seal")

    def test_accepts_a_mode_row_with_the_folder_and_the_file(self, tmp_path, capsys):
        repo, home = self.where(tmp_path)
        SEAL.say_report(repo, home, "", "", "local", "mode", "local")
        assert capsys.readouterr().out == (
            "  folder: local  .git/seal/\n  row:    local  .git/seal/config.md\n"
        )

    @pytest.mark.parametrize(
        "kind, value, row",
        [
            (
                "unknown",
                "remote",
                "  row:    remote — which is not a mode. The two values are `local` and `shared`.\n",
            ),
            ("refused", "why", "  row:    refused  (.git/seal/config.md)\n"),
            ("none", "", "  row:    not declared  (.git/seal/config.md)\n"),
        ],
    )
    def test_refuses_a_row_that_names_no_mode_by_saying_which(
        self, tmp_path, capsys, kind, value, row
    ):
        repo, home = self.where(tmp_path)
        SEAL.say_report(repo, home, "", "", "local", kind, value)
        assert capsys.readouterr().out == "  folder: local  .git/seal/\n" + row


class Test_mode_refusal:
    @pytest.mark.parametrize(
        "text", [None, mode_row("local")], ids=["no file", "one row"]
    )
    def test_accepts_a_config_a_switch_can_write(self, tmp_path, text):
        if text is not None:
            write(tmp_path, "config.md", text)
        assert SEAL.mode_refusal(str(tmp_path)) == ""

    @pytest.mark.parametrize(
        "shape, why",
        [
            ("a directory", " is there and cannot be read"),
            (TWO_MODE_ROWS, f" holds 2 `Mode` rows ({NAMES_BOTH_ROWS})"),
            (WALKED_PAST, " " + STOPS_AT),
        ],
        ids=["unreadable", "two rows", "a table the walker refused"],
    )
    def test_refuses_what_the_writer_would_refuse_naming_the_file(
        self, tmp_path, shape, why
    ):
        path = tmp_path / "config.md"
        if shape == "a directory":
            path.mkdir()
        else:
            path.write_text(shape, encoding="utf-8")
        said_why = SEAL.mode_refusal(str(tmp_path))
        assert said_why.startswith(str(path) + " "), said_why
        assert why in said_why, said_why


class Test_mode_report:
    @pytest.mark.parametrize("mode", ["shared", "local"])
    def test_accepts_a_row_naming_the_folder_as_agreeing(self, take, capsys, mode):
        repo = take(mode)
        config_at(repo, mode_row(mode))
        before = snapshot(repo)
        code, out = said(capsys, repo, "mode")
        assert code == 0, out
        assert f"  folder: {mode:<7}" in out and f"  row:    {mode:<7}" in out
        assert out.endswith("\nThey agree.\n"), out
        assert snapshot(repo) == before

    @pytest.mark.parametrize(
        "mode, body",
        [
            ("shared", None),
            ("local", HEAD + "| Other | x |\n"),
            ("shared", HEAD + "| Mode |  |\n"),
            ("local", "# notes\n\nnothing here.\n"),
        ],
        ids=[
            "shared, no file",
            "local, no such row",
            "shared, an empty value",
            "local, not that table",
        ],
    )
    def test_accepts_an_absent_row_by_writing_the_folders_mode_once(
        self, take, capsys, mode, body
    ):
        """The value written is the folder's: a fixed default would write a
        lie into every undeclared repository of the other mode."""
        repo = take(mode)
        if body is not None:
            config_at(repo, body)
        code, out = said(capsys, repo, "mode")
        assert code == 0, out
        assert "was written from where the folder is" in out
        assert declared_in(repo) == ("mode", mode)
        assert out.endswith("\nThey agree.\n")
        _repo, home, _s, _l, _m = SEAL.resolve(str(repo))
        written = open(os.path.join(home, "config.md"), "rb").read()
        code, out = said(capsys, repo, "mode")
        assert code == 0 and "was written" not in out
        assert open(os.path.join(home, "config.md"), "rb").read() == written

    def test_accepts_check_writing_nothing_where_the_row_is_absent(self, take, capsys):
        repo = take("local")
        _repo, home, _s, _l, _m = SEAL.resolve(str(repo))
        code, out = said(capsys, repo, "mode", "--check")
        assert code == 0, out
        assert "not declared" in out
        assert not os.path.exists(os.path.join(home, "config.md"))

    @pytest.mark.parametrize("mode, other", [("shared", "local"), ("local", "shared")])
    def test_refuses_a_row_naming_the_other_mode_and_names_both_ways_out(
        self, take, capsys, mode, other
    ):
        repo = take(mode)
        config_at(repo, mode_row(other))
        code, out = said(capsys, repo, "mode", "--check")
        assert code == 1, out
        assert f"They disagree: the row says `{other}` and the folder is {mode}." in out
        assert (
            f"  seal mode --apply     move the folder to {other}, as the row says\n"
            in out
        )
        assert (
            f"  seal mode {mode:<11}correct the row to {mode}, as the folder is\n"
            in out
        )
        assert said(capsys, repo, "mode")[0] == 0

    def test_refuses_a_value_that_is_not_a_mode(self, take, capsys):
        repo = take("shared")
        config_at(repo, mode_row("remote"))
        assert said(capsys, repo, "mode", "--check")[0] == 1
        code, out = said(capsys, repo, "mode")
        assert code == 0 and "The row names no mode" in out
        assert declared_in(repo) == ("unknown", "remote")

    @pytest.mark.parametrize(
        "shape, check",
        [
            (TWO_MODE_ROWS, []),
            (TWO_MODE_ROWS, ["--check"]),
            (WALKED_PAST, ["--check"]),
            ("a directory", []),
            ("a broken link", []),
        ],
        ids=[
            "two rows",
            "two rows, checked",
            "a table the walker refused, checked",
            "a directory",
            "a broken link",
        ],
    )
    def test_refuses_a_config_that_will_not_read_at_exit_2(
        self, take, capsys, shape, check
    ):
        repo = take("shared")
        path = os.path.join(str(repo), "seal", "config.md")
        if shape == "a directory":
            os.mkdir(path)
        elif shape == "a broken link":
            symlink_or_skip(os.path.join(str(repo), "seal", "nowhere.md"), path)
        else:
            config_at(repo, shape)
        before = snapshot(repo)
        code, out = said(capsys, repo, "mode", *check)
        assert code == 2, out
        assert (
            "  folder: shared " in out
            and "  row:    refused  (seal/config.md)\n" in out
        )
        assert out.endswith(". Nothing was written.\n"), out
        assert snapshot(repo) == before

    def test_refuses_a_row_it_could_not_write_and_still_reports(self, take, capsys):
        repo = take("local")
        path = config_at(repo, UNCLOSED_FENCE)
        code, out = said(capsys, repo, "mode")
        assert code == 0, out
        assert out.startswith("the `Mode` row could not be written: ")
        assert "The folder is still the answer, and it is:\n  folder: local" in out
        assert open(path, encoding="utf-8").read() == UNCLOSED_FENCE


class Test_gitlinks_under_root:
    @pytest.mark.parametrize("world", ["shared", "beside"])
    def test_accepts_a_root_holding_no_submodule(self, _worlds, take, world):
        repo = _worlds / world if world == "shared" else take(world)
        assert SEAL.gitlinks_under_root(str(repo)) == ([], "")

    def test_refuses_a_submodule_under_the_root_and_a_git_that_cannot_answer(
        self, take, monkeypatch
    ):
        repo = take("under")
        (line,), why = SEAL.gitlinks_under_root(str(repo))
        assert (
            line.startswith("160000 ") and line.endswith("\tseal/vendor") and why == ""
        )
        unanswered(monkeypatch, ["--stage", "--", "seal"], OSError("git is not here"))
        assert SEAL.gitlinks_under_root(str(repo)) == (
            None,
            "git ls-files could not be run (git is not here)",
        )


def refusals_of(repo, wanted, local=None):
    _repo, home, shared, found_local, _mode = SEAL.resolve(str(repo))
    return SEAL.refusals(
        str(repo), home, shared, found_local if local is None else local, wanted
    )


class Test_refusals:
    @pytest.mark.parametrize(
        "shape",
        [
            "clean",
            "an untracked file and the row it wrote",
            "moved by hand",
            "a submodule beside the root",
            "an edited workflow",
        ],
    )
    def test_accepts_a_tree_the_switch_loses_nothing_of(self, take, shape):
        """The switch stages nothing under `.github/`, so an edit there is
        not its to lose."""
        repo = take("beside" if shape.startswith("a submodule") else "shared")
        if shape == "an edited workflow":
            workflow_in(repo, "name: hygiene\n")
            workflow_in(repo, "name: hygiene\n# edited\n", commit=False)
        if shape == "an untracked file and the row it wrote":
            config_at(repo, HEAD)
            commit_everything_as_e(repo, "a config with no Mode row")
            config_at(repo, mode_row("shared"))
            write(repo, "seal/untracked.md", "# a draft\n")
        elif shape == "moved by hand":
            shared, local = roots(repo)
            os.rename(shared, local)
        assert refusals_of(repo, "local") == []

    @pytest.mark.parametrize(
        "shape, why",
        [
            ("no local root", "the common git directory could not be resolved"),
            ("both roots", "both roots exist, and the gates read the first of them"),
            ("two rows", "holds 2 `Mode` rows"),
            (
                "a git that cannot answer",
                "whether there is a submodule under seal/ could not be read: git ls-files could not be run (git is not here).",
            ),
            (
                "a submodule under the root",
                "there is a submodule under seal/:\n  160000 ",
            ),
            (
                "a file at the destination",
                "already exists, and nothing here overwrites",
            ),
            (
                "a broken link at the destination",
                "already exists, and nothing here overwrites",
            ),
            (
                "a staged edit",
                "the tree is not clean under the path this would stage:\n  M  seal/follow-up.md\n",
            ),
            (
                "a staged deletion",
                "the tree is not clean under the path this would stage:\n  D  seal/follow-up.md\n",
            ),
            (
                "a config that is a link",
                "config.md is a symbolic link, and the row is written there",
            ),
        ],
    )
    def test_refuses_a_switch_that_would_lose_or_break_something(
        self, take, monkeypatch, shape, why
    ):
        repo = take("under" if shape == "a submodule under the root" else "shared")
        shared, local = roots(repo)
        if shape == "both roots":
            mark_root(local)
        elif shape == "two rows":
            config_at(repo, TWO_MODE_ROWS)
        elif shape == "a git that cannot answer":
            unanswered(
                monkeypatch, ["--stage", "--", "seal"], OSError("git is not here")
            )
        elif shape == "a file at the destination":
            write(os.path.dirname(local), "seal", "not a root\n")
        elif shape == "a broken link at the destination":
            symlink_or_skip(os.path.join(str(repo), "elsewhere"), local)
        elif shape == "a staged edit":
            write(repo, "seal/follow-up.md", "# changed\n")
            git(repo, "add", "--", "seal/follow-up.md")
        elif shape == "a staged deletion":
            git(repo, "rm", "--quiet", "--", "seal/follow-up.md")
        elif shape == "a config that is a link":
            symlink_or_skip(
                os.path.join(str(repo), "seal", "follow-up.md"),
                os.path.join(shared, "config.md"),
            )
        found = refusals_of(
            repo, "local", local="" if shape == "no local root" else None
        )
        assert any(why in line for line in found), found

    def test_refuses_a_source_that_is_a_link(self, take):
        repo = take("local")
        _shared, local = roots(repo)
        real = os.path.join(str(repo), "elsewhere")
        shutil.move(local, real)
        symlink_or_skip(real, local)
        found = refusals_of(repo, "shared")
        assert found == [
            f"{local} is a symbolic link, not the root itself. Moving it would "
            "move the link and leave the records where they are."
        ]

    def test_refuses_a_projects_own_seal_as_a_destination_not_as_two_roots(self, take):
        """A `<repo>/seal/` whose README does not open with the marker is no
        second root, so switching to shared is refused for the directory in
        the way, which nothing here overwrites."""
        repo = take("local")
        write(repo, "seal/README.md", "# seal\n\nThis package's notes.\n")
        found = refusals_of(repo, "shared")
        assert any("already exists, and nothing here overwrites" in f for f in found)
        assert not any("both roots exist" in f for f in found), found


class Test_switch:
    def test_accepts_shared_to_local_by_moving_staging_and_writing_the_row(
        self, take, capsys
    ):
        """S4: the plugin's workflow, committed, stays in the tree and out of
        the index, the output names the command that takes it out, and going
        back leaves `.github/` as it was."""
        repo = take("shared")
        workflow = workflow_in(repo, SEAL.plugin_workflow())
        shared, local = roots(repo)
        code, out = said(capsys, repo, "mode", "local")
        assert code == 0, out
        assert not os.path.exists(shared)
        assert listed(local) == sorted([*RECORDS, "config.md"])
        assert all(line.startswith("D  seal/") for line in status(repo)), status(repo)
        assert declared_in(repo) == ("mode", "local")
        assert open(workflow, encoding="utf-8").read() == SEAL.plugin_workflow()
        assert (
            "  .github/workflows/hygiene.yml stays: in local mode its checks "
            "examine nothing and pass, and `seal pr-checks remove` takes them out\n"
        ) in out
        assert "`seal export` here and `seal import` there" in out
        commit_everything_as_e(repo, "the switch to local")
        code, out = said(capsys, repo, "mode", "shared")
        assert code == 0, out
        assert open(workflow, encoding="utf-8").read() == SEAL.plugin_workflow()
        assert not any(".github" in line for line in status(repo)), status(repo)
        assert "seal pr-checks install" not in out, out

    @pytest.mark.parametrize(
        "pin, installed",
        [("v0.1.0", True), ("", True), (None, False)],
        ids=["an-older-release", "no-release-named", "a-version-it-cannot-read"],
    )
    def test_accepts_shared_to_local_and_names_a_pin_that_is_not_the_installed_release(
        self, take, capsys, monkeypatch, pin, installed
    ):
        """Round 1 of #952, finding 2: a workflow pinned to another release,
        or one beside a version that cannot be read, is not promised to pass.
        The line names the pin and the two ways out."""
        repo = take("shared")
        version = SEAL.plugin_version()
        text = SEAL.plugin_workflow()
        if pin is not None:
            old = f"--branch v{version} "
            assert old in text, text
            text = text.replace(old, f"--branch {pin} " if pin else "")
        workflow_in(repo, text)
        if not installed:
            monkeypatch.setattr(SEAL, "plugin_version", lambda: "")
        code, out = said(capsys, repo, "mode", "local")
        assert code == 0, out
        named = pin if pin is not None else f"v{version}"
        here = (
            f"pinned to {named or 'no release its clone line names'} and not to "
            f"the installed v{version}"
            if installed
            else f"pinned to {named}, and the installed release could not be read"
        )
        to = f"v{version}" if installed else "the installed release"
        assert (
            f"  .github/workflows/hygiene.yml stays, {here}: a release before "
            "this one fails every pull request with no seal/ in the tree. Move "
            f"its `--branch` line to {to}, or run `seal pr-checks remove`\n"
        ) in out
        assert "examine nothing" not in out, out

    def test_accepts_local_to_shared_and_says_the_commit_is_the_door(
        self, take, capsys
    ):
        repo = take("local")
        shared, local = roots(repo)
        code, out = said(capsys, repo, "mode", "shared")
        assert code == 0, out
        assert not os.path.exists(local)
        assert listed(shared) == sorted([*RECORDS, "config.md"])
        assert staged(repo).splitlines() == sorted(
            f"seal/{rel}" for rel in [*RECORDS, "config.md"]
        )
        assert not os.path.lexists(os.path.join(str(repo), WORKFLOW_PATH))
        assert declared_in(repo) == ("mode", "shared")
        assert out.index("history") < out.index("Now commit")
        assert out.count("`git reset -- :/seal`") == 2, out
        assert (
            "  no pull-request checks are installed: `seal pr-checks install` "
            "writes .github/workflows/hygiene.yml\n"
        ) in out

    def test_accepts_the_way_back_it_names_from_a_subdirectory(self, take, capsys):
        """The way back is spelled with `:/`, so it works from where a person
        stands."""
        repo = take("local")
        write(repo, "docs/x.md", "x\n")
        commit_everything_as_e(repo, "a subdirectory")
        code, out = said(capsys, repo / "docs", "mode", "shared")
        assert code == 0, out
        named = [
            line.split("`")[1] for line in out.splitlines() if "`git reset" in line
        ]
        assert len(named) == 2 and all(":/" in command for command in named), named
        subprocess.run(
            named[0].split(), cwd=str(repo / "docs"), check=True, capture_output=True
        )
        assert all(line.startswith("??") for line in status(repo)), status(repo)
        code, out = said(capsys, repo / "docs", "mode", "local")
        assert code == 0, out
        assert not (repo / "seal").exists()

    @pytest.mark.parametrize("wanted", ["local", "shared"])
    def test_accepts_a_run_stopped_after_the_move_as_one_to_finish(
        self, take, capsys, wanted
    ):
        repo = take("shared" if wanted == "local" else "local")
        shared, local = roots(repo)
        os.rename(*((shared, local) if wanted == "local" else (local, shared)))
        code, out = said(capsys, repo, "mode", wanted)
        assert code == 0, out
        assert "is already the root\n" in out
        assert declared_in(repo) == ("mode", wanted)
        if wanted == "local":
            assert all(line.startswith("D ") for line in status(repo))
        else:
            assert out.count("git reset -- ") == 1, out

    @pytest.mark.parametrize("mode", ["shared", "local"])
    def test_accepts_an_untracked_file_as_travelling_with_the_folder(
        self, take, capsys, mode
    ):
        repo = take(mode)
        _repo, home, shared, local, _m = SEAL.resolve(str(repo))
        write(home, "untracked.md", "# a draft\n")
        wanted = "local" if mode == "shared" else "shared"
        code, out = said(capsys, repo, "mode", wanted)
        assert code == 0, out
        assert os.path.isfile(
            os.path.join(local if mode == "shared" else shared, "untracked.md")
        )
        if mode == "shared":
            assert (
                "note: seal/untracked.md is untracked, so the index cannot lose it"
                in out
            )

    def test_accepts_a_root_git_never_tracked_and_another_worktree(
        self, take, capsys, tmp_path
    ):
        repo = take("plain")
        holding(repo / "seal")
        git(repo, "worktree", "add", "-q", str(tmp_path / "linked"), "feature/x")
        code, out = said(capsys, repo, "mode", "local")
        assert code == 0, out
        assert "  nothing under seal/ was tracked\n" in out
        assert "is another worktree of this clone" in out and "linked" in out

    def test_accepts_a_tracked_config_without_calling_it_untracked(self, take, capsys):
        repo = take("shared")
        config_at(repo, "# Repository config\n\n" + HEAD)
        commit_everything_as_e(repo, "a config with no Mode row")
        assert said(capsys, repo, "mode")[0] == 0
        assert " M seal/config.md" in status(repo)
        code, out = said(capsys, repo, "mode", "local")
        assert code == 0, out
        assert "config.md is untracked" not in out

    def test_refuses_what_its_refusals_name_and_moves_nothing(self, take, capsys):
        repo = take("shared")
        write(repo, "seal/follow-up.md", "# changed\n")
        git(repo, "add", "--", "seal/follow-up.md")
        before = snapshot(repo)
        code, out = said(capsys, repo, "mode", "local")
        assert code == 1, out
        assert out.endswith("\nNothing was moved.\n")
        assert snapshot(repo) == before

    def test_refuses_a_rename_the_filesystem_turns_down_and_names_the_mv(
        self, take, capsys
    ):
        repo = take("local")
        bits = os.stat(repo).st_mode
        os.chmod(repo, 0o500)
        try:
            if os.access(repo, os.W_OK):
                pytest.skip("the working tree is writable despite chmod")
            before = snapshot(repo)
            code, out = said(capsys, repo, "mode", "shared")
            after = snapshot(repo)
        finally:
            os.chmod(repo, bits)
        assert code == 1, out
        assert "the root could not be moved: " in out
        assert "Nothing else has run." in out and '  mv "' in out
        assert after == before

    def test_refuses_to_call_a_stage_git_turned_down_staged(self, take, capsys):
        repo = take("local")
        write(repo, ".gitignore", "seal/\n")
        write(repo, "docs/x.md", "x\n")
        commit_everything_as_e(repo, "an ignore rule")
        code, out = said(capsys, repo / "docs", "mode", "shared")
        assert code == 0, out
        assert "could NOT be staged" in out
        assert "A commit now would record nothing." in out
        assert "staged seal/\n" not in out


class Test_mode:
    @pytest.mark.parametrize("mode, other", [("shared", "local"), ("local", "shared")])
    def test_accepts_apply_moving_the_folder_to_the_row(
        self, take, capsys, mode, other
    ):
        repo = take(mode)
        config_at(repo, mode_row(other))
        shared, local = roots(repo)
        code, out = said(capsys, repo, "mode", "--apply")
        assert code == 0, out
        assert listed(local if other == "local" else shared) is not None
        assert listed(shared if other == "local" else local) is None

    def test_accepts_check_where_there_is_no_root(self, take, capsys):
        code, out = said(capsys, take("plain"), "mode", "--check")
        assert code == 0, out
        assert (
            out == "no seal/ here, so nothing is declared and nothing can disagree.\n"
        )

    @pytest.mark.parametrize("argv", [["mode"], ["mode", "local"]])
    def test_refuses_without_a_root_naming_both_places(self, take, capsys, argv):
        code, out = said(capsys, take("plain"), *argv)
        assert code == 1, out
        assert "(shared mode)" in out and "(local mode)" in out

    def test_refuses_check_where_no_repository_resolves(self, capsys, tmp_path):
        code, out = said(capsys, tmp_path, "mode", "--check")
        assert code == 1, out
        assert "the check could not run" in out

    @pytest.mark.parametrize(
        "row, code, want",
        [
            (None, 1, "the `Mode` row is not declared, so there is nothing to apply."),
            (
                mode_row("remote"),
                1,
                "the `Mode` row names `remote`, which is not a mode, so there is nothing to apply.",
            ),
            (TWO_MODE_ROWS, 2, ", so there is nothing to apply. Nothing was moved."),
        ],
        ids=["no row", "no mode", "two rows"],
    )
    def test_refuses_apply_with_no_row_to_act_on(self, take, capsys, row, code, want):
        repo = take("local")
        if row is not None:
            config_at(repo, row)
        before = snapshot(repo)
        found, out = said(capsys, repo, "mode", "--apply")
        assert found == code, out
        assert want in out, out
        if row is None:
            assert "  | Mode | local |\n" in out
        assert snapshot(repo) == before


class Test_pr_checks:
    """S3 and S5: the checks are a command of their own, and the workflow
    file is the one record of whether they are installed."""

    def test_accepts_install_report_and_remove_in_turn(self, take, capsys):
        repo = take("shared")
        version = SEAL.plugin_version()
        assert said(capsys, repo, "pr-checks") == (
            0,
            "not installed: there is no .github/workflows/hygiene.yml. "
            "`seal pr-checks install` writes it where seal/ is in the tree.\n",
        )
        code, out = said(capsys, repo, "pr-checks", "install")
        assert code == 0, out
        assert out == (
            f"wrote .github/workflows/hygiene.yml (pinned to v{version}) and staged it\n"
        )
        commit_everything_as_e(repo, "the checks")
        code, out = said(capsys, repo, "pr-checks", "install")
        assert code == 0 and "already this plugin's, pinned to v" in out, out
        assert said(capsys, repo, "pr-checks") == (
            0,
            "installed: .github/workflows/hygiene.yml is this plugin's "
            f"pull-request checks, pinned to v{version}. `seal pr-checks remove` "
            "takes them out.\n",
        )
        code, out = said(capsys, repo, "pr-checks", "remove")
        assert code == 0, out
        assert not os.path.lexists(os.path.join(str(repo), WORKFLOW_PATH))
        code, out = said(capsys, repo, "pr-checks", "remove")
        assert code == 0, out
        assert "there is no .github/workflows/hygiene.yml" in out

    def test_accepts_remove_straight_after_install_before_a_commit(self, take, capsys):
        """The sealer at `55aea15d`: `install` stages the file, and git
        refuses a plain `git rm` of a file staged and never committed."""
        repo = take("shared")
        before = status(repo)
        code, out = said(capsys, repo, "pr-checks", "install")
        assert code == 0, out
        code, out = said(capsys, repo, "pr-checks", "remove")
        assert code == 0, out
        assert out == (
            "removed .github/workflows/hygiene.yml and took it out of the "
            "index — staged, never committed, and byte for byte this plugin's, "
            "so `seal pr-checks install` writes it back\n"
        )
        assert not os.path.lexists(os.path.join(str(repo), ".github"))
        assert status(repo) == before

    @pytest.mark.parametrize("edited", ["index", "working copy"])
    def test_refuses_a_staged_file_that_differs_and_leaves_it(
        self, take, capsys, edited
    ):
        repo = take("shared")
        code, out = said(capsys, repo, "pr-checks", "install")
        assert code == 0, out
        path = os.path.join(str(repo), WORKFLOW_PATH)
        mine = SEAL.plugin_workflow() + "# mine\n"
        write(repo, WORKFLOW_PATH.replace(os.sep, "/"), mine)
        if edited == "index":
            git(repo, "add", "--", WORKFLOW_PATH.replace(os.sep, "/"))
            write(repo, WORKFLOW_PATH.replace(os.sep, "/"), SEAL.plugin_workflow())
        before = snapshot(repo)
        on_disk = open(path, encoding="utf-8").read()
        code, out = said(capsys, repo, "pr-checks", "remove")
        assert code == 1, out
        assert out == (
            ".github/workflows/hygiene.yml is staged and never committed, and "
            "its staged copy or its working copy is not byte for byte what this "
            "plugin writes NOW, so it is left alone: git holds no committed "
            "copy, and removing it would take that edit with it. Look at it "
            "and delete it yourself.\n"
        )
        assert snapshot(repo) == before
        assert open(path, encoding="utf-8").read() == on_disk

    @pytest.mark.parametrize("state", ["AD", " D", " D, another release"])
    def test_accepts_remove_of_a_file_deleted_by_hand_the_index_still_holds(
        self, take, capsys, state
    ):
        """Round 5, finding 1: a commit is made from the index, so a file
        gone from the working tree is not gone from the next commit. Round 6,
        finding 1: the index copy is taken where a copy survives it, in what
        `install` writes back or, for another release's pin, in HEAD."""
        repo = take("shared")
        before = status(repo)
        if state == " D, another release":
            old = SEAL.plugin_workflow().replace(f"v{SEAL.plugin_version()}", "v0.1.0")
            assert old != SEAL.plugin_workflow()
            workflow_in(repo, old)
        else:
            code, out = said(capsys, repo, "pr-checks", "install")
            assert code == 0, out
            if state == " D":
                commit_everything_as_e(repo, "the checks")
        os.remove(os.path.join(str(repo), WORKFLOW_PATH))
        code, out = said(capsys, repo, "pr-checks", "remove")
        assert code == 0, out
        assert out == (
            "there was no .github/workflows/hygiene.yml in the working tree, "
            "but the index still held it; took it out of the index, so the "
            "next commit does not carry it\n"
        )
        gone = [] if state == "AD" else ["D  .github/workflows/hygiene.yml"]
        assert status(repo) == sorted(before + gone)

    @pytest.mark.parametrize("committed", [False, True], ids=["AD", " D"])
    def test_refuses_a_staged_file_without_the_clone_line_deleted_by_hand(
        self, take, capsys, committed
    ):
        """The index may hold the only copy of somebody's file, and a file
        HEAD carries is still somebody's, so a copy without the clone line is
        left alone whether or not HEAD holds it too."""
        repo = take("shared")
        rel = WORKFLOW_PATH.replace(os.sep, "/")
        write(repo, rel, "name: mine\n")
        git(repo, "add", "--", rel)
        if committed:
            commit_everything_as_e(repo, "somebody's workflow")
        os.remove(os.path.join(str(repo), WORKFLOW_PATH))
        before = snapshot(repo)
        code, out = said(capsys, repo, "pr-checks", "remove")
        assert code == 1, out
        assert out == (
            "there is no .github/workflows/hygiene.yml in the working tree, "
            "and the index holds a copy that does not carry this plugin's "
            "clone line, so it was left alone: the index may hold the only "
            "copy of somebody's file. Look at it with `git diff --cached` and "
            "take it out yourself.\n"
        )
        assert snapshot(repo) == before
        assert git(repo, "cat-file", "blob", f":{rel}").stdout == "name: mine\n"

    @pytest.mark.parametrize(
        "state", ["AD, a staged edit", "AD, another release", "MD, a staged edit"]
    )
    def test_refuses_an_index_copy_no_other_copy_keeps_deleted_by_hand(
        self, take, capsys, state
    ):
        """Round 6, finding 1: with the working file gone, git's own `rm`
        does not refuse a staged change, so an index copy that is neither
        HEAD's nor what `install` writes now would go with nothing left of
        it."""
        repo = take("shared")
        rel = WORKFLOW_PATH.replace(os.sep, "/")
        mine = SEAL.plugin_workflow() + "# mine\n"
        if state == "AD, a staged edit":
            code, out = said(capsys, repo, "pr-checks", "install")
            assert code == 0, out
        elif state == "AD, another release":
            mine = SEAL.plugin_workflow().replace(f"v{SEAL.plugin_version()}", "v0.1.0")
            assert mine != SEAL.plugin_workflow()
        else:
            workflow_in(repo, SEAL.plugin_workflow())
        write(repo, rel, mine)
        git(repo, "add", "--", rel)
        os.remove(os.path.join(str(repo), WORKFLOW_PATH))
        before = snapshot(repo)
        code, out = said(capsys, repo, "pr-checks", "remove")
        assert code == 1, out
        assert out == (
            "there is no .github/workflows/hygiene.yml in the working tree, "
            "and the index holds a copy that is neither byte for byte the "
            "copy HEAD carries nor byte for byte what this plugin writes NOW, "
            "so it was left alone: removing it would take the only copy of "
            "that edit with it. Look at it with `git diff --cached` and take "
            "it out yourself.\n"
        )
        assert snapshot(repo) == before
        assert git(repo, "cat-file", "blob", f":{rel}").stdout == mine

    def test_refuses_an_index_entry_it_cannot_read_deleted_by_hand(self, take, capsys):
        """Round 6, finding 1: an unmerged path has no copy at stage 0 for
        git to give, and the refusal says so rather than naming a clone line
        it never read."""
        repo = take("shared")
        rel = WORKFLOW_PATH.replace(os.sep, "/")
        write(repo, rel, SEAL.plugin_workflow())
        blob = git_out(repo, "hash-object", "-w", "--", rel)
        os.remove(os.path.join(str(repo), WORKFLOW_PATH))
        done = subprocess.run(
            ["git", "-C", str(repo), "update-index", "-z", "--index-info"],
            # NUL-terminated: in text mode Python writes "\n" as os.linesep,
            # so on Windows each path would end in a carriage return.
            input="".join(f"100644 {blob} {n}\t{rel}\0" for n in (1, 2, 3)),
            capture_output=True,
            encoding="utf-8",
        )
        assert done.returncode == 0, done.stderr
        assert len(git_out(repo, "ls-files", "--unmerged", "--", rel).splitlines()) == 3
        before = snapshot(repo)
        code, out = said(capsys, repo, "pr-checks", "remove")
        assert code == 1, out
        assert out == (
            "there is no .github/workflows/hygiene.yml in the working tree, "
            "and the index's copy of it could not be read, as for a path left "
            "unmerged, so it was left alone. Look at it with `git status` and "
            "take it out yourself.\n"
        )
        assert snapshot(repo) == before
        assert len(git_out(repo, "ls-files", "--unmerged", "--", rel).splitlines()) == 3

    def test_accepts_remove_where_the_root_left_the_tree(self, take, capsys):
        """A workflow that outlived its root is the case `remove` is for."""
        repo = take("local")
        workflow_in(repo, SEAL.plugin_workflow())
        code, out = said(capsys, repo, "pr-checks", "remove")
        assert code == 0, out
        assert "D  .github/workflows/hygiene.yml" in status(repo)

    def test_refuses_install_in_local_mode_and_writes_nothing(self, take, capsys):
        repo = take("local")
        before = snapshot(repo)
        code, out = said(capsys, repo, "pr-checks", "install")
        assert code == 1, out
        assert "the checks read committed records" in out
        assert snapshot(repo) == before

    @pytest.mark.parametrize("action", ["", "install", "remove"])
    def test_refuses_somebody_elses_file_and_leaves_it(self, take, capsys, action):
        repo = take("shared")
        path = workflow_in(repo, "name: hygiene\njobs: {}\n")
        code, out = said(capsys, repo, "pr-checks", *([action] if action else []))
        assert code == (0 if not action else 1), out
        assert open(path, encoding="utf-8").read() == "name: hygiene\njobs: {}\n"
        if not action:
            assert out == (
                "not this plugin's: .github/workflows/hygiene.yml is there and "
                "does not carry this plugin's clone line, so this plugin's checks "
                "are not installed and that file is left alone.\n"
            )

    def test_refuses_to_call_an_install_git_turned_down_staged(self, take, capsys):
        """And the command it names instead works from a subdirectory."""
        repo = take("shared")
        write(repo, ".gitignore", ".github/\n")
        write(repo, "docs/x.md", "x\n")
        commit_everything_as_e(repo, "an ignore rule")
        code, out = said(capsys, repo / "docs", "pr-checks", "install")
        assert code == 1, out
        assert "the pull-request checks would never run." in out
        assert ".github" not in staged(repo)
        (prescribed,) = [
            span
            for line in out.splitlines()
            for span in line.split("`")[1::2]
            if span.startswith("git add -f")
        ]
        done = subprocess.run(
            prescribed.split(),
            cwd=str(repo / "docs"),
            capture_output=True,
            encoding="utf-8",
        )
        assert done.returncode == 0, done.stderr
        assert ".github/workflows/hygiene.yml" in staged(repo)

    def test_refuses_outside_a_repository(self, capsys, tmp_path):
        code, out = said(capsys, tmp_path, "pr-checks")
        assert code == 1, out
        assert "not inside a git repository" in out


class Test_check:
    def exported_once(self, take, capsys):
        repo = take("local")
        assert said(capsys, repo, "export")[0] == 0
        return repo, roots(repo)[1]

    def test_accepts_a_change_as_one_line_and_writes_nothing(self, take, capsys):
        repo, local = self.exported_once(take, capsys)
        write(local, f"threads/{ITEM}/design.md", "# edited\n")
        before = listed(local)
        code, out = said(capsys, repo, "export", "--check")
        assert (code, out) == (0, "1 work items changed since the last export\n")
        assert listed(local) == before

    def test_accepts_an_added_and_a_removed_item_and_no_root_level_file(
        self, take, capsys
    ):
        repo, local = self.exported_once(take, capsys)
        write(local, "follow-up.md", "# a new follow-up row\n")
        assert said(capsys, repo, "export", "--check")[1] == (
            "0 work items changed since the last export\n"
        )
        write(local, "threads/1788000001-another/design.md", "# another\n")
        shutil.rmtree(os.path.join(local, "threads", ITEM))
        assert said(capsys, repo, "export", "--check")[1] == (
            "2 work items changed since the last export\n"
        )

    @pytest.mark.parametrize(
        "state", [None, '{"items": []}'], ids=["none", "items that are no object"]
    )
    def test_refuses_to_count_against_no_export(self, take, capsys, state):
        repo = take("local")
        if state is not None:
            write(repo / ".git", "agentic-last-export.json", state)
        code, out = said(capsys, repo, "export", "--check")
        assert code == 0
        assert (
            out
            == "1 work items here and no export yet — `seal export` writes the first copy.\n"
        )

    @pytest.mark.parametrize("world, code", [("shared", 0), ("plain", 1)])
    def test_refuses_to_remind_a_shared_root_or_none(self, take, capsys, world, code):
        found, out = said(capsys, take(world), "export", "--check")
        assert found == code, out
        if world == "shared":
            assert (
                out
                == "shared mode: the records are committed, so there is nothing to export.\n"
            )


class Test_no_work_item:
    """`seal no-work-item` records, for this session on the branch checked out
    where it runs, that its change belongs to no work item, so
    `hooks/routing-edit-gate.py` lets its edits on that branch through
    (#1027, S4; `questions.md` Q7, answer (b))."""

    def record(self, repo, session="s1"):
        return os.path.join(
            os.path.realpath(repo), ".git", "agentic-no-work-item", session
        )

    def recorded(self, repo, session="s1"):
        with open(self.record(repo, session), encoding="utf-8", newline="") as f:
            return f.read()

    def test_accepts_the_session_variable_and_writes_its_branch(
        self, take, capsys, monkeypatch
    ):
        repo = take("plain")
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "s1")
        code, out = said(capsys, repo, "no-work-item")
        assert code == 0, out
        assert self.recorded(repo) == "main\n"
        assert out == (
            f"recorded: this session's change on `main` in "
            f"{os.path.realpath(repo)} belongs to no work item "
            f"({self.record(repo)}), so its edits on that branch go ahead.\n"
        )

    def test_a_second_branch_adds_a_line_and_the_same_branch_adds_none(
        self, take, capsys, monkeypatch
    ):
        repo = take("plain")
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "s1")
        assert said(capsys, repo, "no-work-item")[0] == 0
        git(repo, "switch", "-q", "feature/x")
        assert said(capsys, repo, "no-work-item")[0] == 0
        assert self.recorded(repo) == "main\nfeature/x\n"
        assert said(capsys, repo, "no-work-item")[0] == 0
        assert self.recorded(repo) == "main\nfeature/x\n"

    def test_accepts_a_branch_with_no_commit_yet_and_writes_it(
        self, tmp_path, capsys, monkeypatch
    ):
        """HEAD names `main` before the first commit, and that is the branch
        recorded, not a detached HEAD (round 4 of #1027, finding 1)."""
        repo = tmp_path / "fresh"
        git(tmp_path, "init", "-q", "-b", "main", str(repo))
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "s1")
        code, out = said(capsys, repo, "no-work-item")
        assert code == 0, out
        assert self.recorded(repo) == "main\n"

    def test_refuses_a_detached_head_and_writes_nothing(
        self, take, capsys, monkeypatch
    ):
        repo = take("plain")
        git(repo, "switch", "-q", "--detach")
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "s1")
        code, out = said(capsys, repo, "no-work-item")
        assert code == 1
        assert not os.path.exists(os.path.dirname(self.record(repo)))
        assert out == (
            f"seal: HEAD is detached in {os.path.realpath(repo)}, so no branch "
            "can be recorded and nothing was. Check out a branch there first, "
            "then run this again.\n"
        )

    def test_a_paused_rebase_records_the_branch_it_names(
        self, take, capsys, monkeypatch
    ):
        """HEAD is detached while the rebase waits on a conflict, and the
        branch the rebase names is the one recorded, as the edit gate
        resolves it."""
        repo = take("plain")
        identity = ["-c", "user.email=e@example.com", "-c", "user.name=e"]
        git(repo, "switch", "-q", "feature/x")
        write(repo, "f.txt", "feature\n")
        commit_everything_as_e(repo, "feature")
        git(repo, "switch", "-q", "main")
        write(repo, "f.txt", "base\n")
        commit_everything_as_e(repo, "base")
        git(repo, "switch", "-q", "feature/x")
        assert git(repo, *identity, "rebase", "main", check=False).returncode != 0
        assert git_out(repo, "rev-parse", "--abbrev-ref", "HEAD") == "HEAD"
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "s1")
        assert said(capsys, repo, "no-work-item")[0] == 0
        assert self.recorded(repo) == "feature/x\n"

    @pytest.mark.parametrize("value", [None, ".", ".."], ids=["unset", "dot", "dots"])
    def test_refuses_a_session_variable_naming_no_session_and_writes_nothing(
        self, take, capsys, monkeypatch, value
    ):
        """A value that is no file name would name the records' directory or
        its parent, so it names no session."""
        repo = take("plain")
        if value is not None:
            monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", value)
        code, out = said(capsys, repo, "no-work-item")
        assert code == 1
        assert not os.path.exists(os.path.dirname(self.record(repo)))
        assert out == (
            "seal: CLAUDE_CODE_SESSION_ID names no session in this environment, "
            "so nothing was recorded. Run this from the session's own Bash tool.\n"
        )

    def test_refuses_outside_a_repository_and_writes_nothing(
        self, tmp_path, capsys, monkeypatch
    ):
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "s1")
        code, out = said(capsys, tmp_path, "no-work-item")
        assert code == 1
        assert out == (
            f"seal: {tmp_path} is in no git repository, so nothing was recorded.\n"
        )

    def test_root_names_the_clone_from_anywhere(
        self, take, tmp_path, capsys, monkeypatch
    ):
        repo = take("plain")
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "s1")
        code, _ = said(capsys, tmp_path, "no-work-item", "--root", str(repo))
        assert code == 0
        assert os.path.isfile(self.record(repo))

    def test_a_record_older_than_a_day_is_pruned_when_one_is_written(
        self, take, capsys, monkeypatch
    ):
        repo = take("plain")
        old, fresh = self.record(repo, "old"), self.record(repo, "fresh")
        for path in (old, fresh):
            write(os.path.dirname(path), os.path.basename(path), "")
        day_and_a_minute = 86400 + 60
        stale = os.stat(old).st_mtime - day_and_a_minute
        os.utime(old, (stale, stale))
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "s1")
        assert said(capsys, repo, "no-work-item")[0] == 0
        assert not os.path.exists(old)
        assert os.path.isfile(fresh) and os.path.isfile(self.record(repo))


class Test_main:
    @pytest.mark.parametrize(
        "argv, called",
        [
            (["export"], "export"),
            (["export", "--check"], "check"),
            (["import", "x.zip"], "import_"),
            (["mode", "local"], "mode"),
            (["no-work-item"], "no_work_item"),
            (["pr-checks"], "pr_checks"),
            (["pr-checks", "install"], "pr_checks"),
            (["pr-checks", "remove"], "pr_checks"),
        ],
    )
    def test_accepts_each_subcommand_and_hands_it_on(
        self, monkeypatch, tmp_path, argv, called
    ):
        seen = []
        for name in ("export", "check", "import_", "mode", "no_work_item", "pr_checks"):
            monkeypatch.setattr(
                SEAL, name, lambda *a, _name=name: seen.append(_name) or 0
            )
        assert SEAL.main(argv, cwd=str(tmp_path)) == 0
        assert seen == [called]

    @pytest.mark.parametrize(
        "name, script",
        [
            ("gate", "skills/verify/scripts/broad_gate.py"),
            ("settle", "skills/settle/scripts/settle.py"),
            ("cost", "skills/verify/scripts/session_cost.py"),
            ("mutate", "skills/verify/scripts/mutation_check.py"),
            ("unverified", "skills/verify/scripts/unverified_check.py"),
            ("arms", "skills/verify/scripts/arm_check.py"),
            ("deferrals", "skills/verify/scripts/deferral_check.py"),
            ("fold", "skills/settle/scripts/fold_check.py"),
            ("pact", "skills/verify/scripts/pact_check.py"),
            ("payload", "skills/verify/scripts/payload_meter.py"),
            ("stamp", "skills/verify/scripts/seal_stamp.py"),
            ("layout", "skills/verify/scripts/test_layout.py"),
            ("rules", ".github/scripts/rules.py"),
        ],
    )
    def test_accepts_each_tool_and_hands_its_script_every_argument(
        self, monkeypatch, tmp_path, name, script
    ):
        """#1051: one command, one subcommand per tool. Each subcommand runs
        the script its `bin/` wrapper ran, on this interpreter, with every
        argument after the name handed on untouched, `--help` among them, so
        the script's own parser answers it."""
        handed = []
        monkeypatch.setattr(
            SEAL, "hand_over", lambda command: handed.append(command) or 0
        )
        argv = ["--base", "origin/main", "x y", "--help"]
        assert SEAL.main([name, *argv], cwd=str(tmp_path)) == 0
        path = os.path.normpath(os.path.join(ROOT, *script.split("/")))
        assert os.path.isfile(path), path
        assert handed == [[sys.executable, path, *argv]]

    @pytest.mark.parametrize(
        "argv",
        [
            [],
            ["mode", "remote"],
            ["mode", "local", "--apply"],
            ["mode", "--check", "--apply"],
            ["mode", "local", "--check"],
            ["pr-checks", "add"],
        ],
        ids=[
            "no subcommand",
            "no mode",
            "a mode and apply",
            "check and apply",
            "a mode and check",
            "no action",
        ],
    )
    def test_refuses_arguments_with_two_answers_or_none(self, capsys, tmp_path, argv):
        with pytest.raises(SystemExit) as stopped:
            SEAL.main(argv, cwd=str(tmp_path))
        assert stopped.value.code == 2
        if len(argv) == 3:
            assert "cannot be given together" in capsys.readouterr().err


test_census = census_case(TARGET)
