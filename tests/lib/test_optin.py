"""`lib/optin.py`: one opt-in signal, read one way, `seal/` at the first of
three places.

`<repo>/seal/` is what shared mode commits, `<repo>/agentic-seal/` where the
project's own `seal/` stands (#1059), and `<git-common-dir>/seal/` is where
local mode keeps it (#80). The root's presence is the whole declaration, and
there is no config key. `.specseal/` and `_ai/` are not addresses at all, and
the throwaway opt-out is a file under the git directory, where nothing can
commit it. A reader that decoded nothing answers "not opted in" and never
raises.

The cases come from `tests/test_optin_home.py` and
`tests/test_gates_do_not_fail_open.py` (#942's phase 6), and the case of
`tests/test_local_mode_resolves_under_the_git_dir.py` where the scratch marker
under the common directory keeps the stamp's drawer silent in local mode.
"""

import json
import os
import subprocess

import pytest
from conftest import (
    KOREAN,
    ROOT,
    census_case,
    git_repo,
    home,
    legacy,
    linked_worktree,
    load_lib_module,
    load_module,
    local_home,
    mark_root,
    scratch,
)

TARGET = "lib/optin.py"

STAMP = os.path.join(ROOT, "skills", "verify", "scripts", "seal_stamp.py")
STAMP_VALUES = {
    "tree": "aaa1111",
    "base": "bbb2222",
    "from": "origin/base",
    "item": "/x/seal/threads/1799000000-an-item",
    "scale": 0.9,
    "rows": [("SEALED", ""), None, ("tree", "aaa1111")],
}


@pytest.fixture
def optin():
    return load_lib_module("optin.py", "agentic_optin")


class Test_repo_root:
    def test_accepts_a_repository_whose_path_the_locale_cannot_carry(
        self, tmp_path, optin
    ):
        """The encoding half, asked of the answer rather than of the source.

        Under `text=True` this returns one of two wrong things depending on the
        ambient codepage: nothing at all where the decode fails outright (cp949,
        and the reader-thread death above), or a plausible-looking path that does
        not exist where the codepage decodes every byte to something (cp1252 turns
        the UTF-8 bytes of Korean into Latin-1 letters, and `opted_in` then answers
        False about a repository that is opted in).

        Asserting that the answer names a directory that EXISTS catches both, and
        on a UTF-8 locale it is a no-op — the same shape as every other
        substitution in this work item.
        """
        repo = git_repo(tmp_path / KOREAN / "repo")
        mark_root(repo / "seal")
        got = optin.repo_root(str(repo))
        assert got, "the root came back empty for a repository that is right there"
        assert os.path.isdir(got), (
            f"resolved to a directory that does not exist: {got!r}"
        )
        assert os.path.normpath(got) == os.path.normpath(str(repo))
        assert optin.opted_in(str(repo)) is True

    def test_refuses_a_reader_that_decoded_nothing_and_answers_empty(
        self, monkeypatch, optin
    ):
        """The `None` stdout, produced directly.

        This is what the dead reader thread leaves behind, and it is the state that
        made `optin.repo_root` raise `AttributeError` out of its caller, which
        then exited with no answer where it should have read the repository as
        not opted in.

        The module's own docstring states the direction: everything here fails
        toward "not opted in", and that is `""`, not an exception.
        """

        def decoded_nothing(*args, **kwargs):
            return subprocess.CompletedProcess(args, 0, stdout=None, stderr=None)

        monkeypatch.setattr(optin.subprocess, "run", decoded_nothing)
        assert optin.repo_root(str(ROOT)) == ""
        assert optin.opted_in(str(ROOT)) is False

    def test_accepts_gits_answer_in_this_platforms_spelling(
        self, tmp_path, monkeypatch, optin
    ):
        """The root comes back as this platform spells a path, whatever
        spelling git answered with. The real git answers with forward slashes
        on every platform, which `normpath` changes only on Windows, so the
        answer is faked with a segment `normpath` folds everywhere (#1017, the
        body's `normpath` row)."""
        answer = "/x/y/../z"

        def answering(cmd, **kwargs):
            return subprocess.CompletedProcess(cmd, 0, stdout=answer + "\n", stderr="")

        monkeypatch.setattr(optin.subprocess, "run", answering)
        assert optin.repo_root(str(tmp_path)) == os.path.normpath(answer)

    def test_refuses_a_path_that_is_no_directory_whatever_git_answers(
        self, tmp_path, monkeypatch, optin
    ):
        """A file contains no repository. The real git refuses `-C` on a
        file too, so git is faked to answer for any path, which removes that
        guarantee (contract rule 13; #1017, the body's directory-test row)."""
        afile = tmp_path / "f.txt"
        afile.write_text("x\n", encoding="utf-8")

        def answering(cmd, **kwargs):
            return subprocess.CompletedProcess(
                cmd, 0, stdout=str(tmp_path) + "\n", stderr=""
            )

        monkeypatch.setattr(optin.subprocess, "run", answering)
        assert optin.repo_root(str(afile)) == ""


class Test_git_common_dir:
    def test_accepts_a_main_worktree_without_asking_git(self, optin, repo, monkeypatch):
        """A `.git` directory at the toplevel is the git directory, so the common
        case costs no process, which every gated command would pay."""
        monkeypatch.setattr(
            optin.subprocess,
            "run",
            lambda *a, **k: (_ for _ in ()).throw(AssertionError("git was asked")),
        )
        assert optin.git_common_dir(str(repo)) == os.path.join(str(repo), ".git")

    def test_accepts_a_linked_worktree_by_asking_git(self, optin, repo, tmp_path):
        other = tmp_path / "linked"
        subprocess.run(
            ["git", "-C", str(repo), "worktree", "add", "-q", str(other), "feature/x"],
            check=True,
            capture_output=True,
        )
        assert os.path.isfile(other / ".git"), "a linked worktree carries a .git FILE"
        assert os.path.samefile(optin.git_common_dir(str(other)), repo / ".git")

    @pytest.mark.parametrize("shape", ["relative", "absolute"])
    def test_accepts_gits_answer_whichever_shape_it_has(
        self, optin, repo, tmp_path, monkeypatch, shape
    ):
        """S2, S11. `git rev-parse --git-common-dir` answers relative to the
        directory it ran in unless the path is absolute, and with forward
        slashes on every platform. Both shapes are joined and normalised; no
        drive-letter logic is added for the second."""
        home = local_home(repo)
        other = linked_worktree(repo, tmp_path)
        real = subprocess.run
        answer = (
            os.path.relpath(repo / ".git", other)
            if shape == "relative"
            else str(repo / ".git")
        ).replace(os.sep, "/")

        def answering(args, **kwargs):
            if "--git-common-dir" in args:
                return subprocess.CompletedProcess(
                    args, 0, stdout=answer + "\n", stderr=""
                )
            return real(args, **kwargs)

        monkeypatch.setattr(optin.subprocess, "run", answering)
        got = optin.git_common_dir(str(other))
        assert got == os.path.normpath(got), "the answer was not normalised"
        assert os.path.samefile(got, repo / ".git")
        assert os.path.samefile(optin.home(str(other)), home)

    def test_refuses_a_reader_that_decoded_nothing_and_answers_empty(
        self, tmp_path, monkeypatch, optin
    ):
        """S10 (#80). `git_common_dir` has the same `subprocess.run` shape as
        `repo_root` and, for a tree whose `.git` is a FILE, the same dead reader
        thread: `stdout` comes back `None`. That reads as "" — no common
        directory, so no local root, so not opted in — and never raises."""
        linked = tmp_path / "linked"
        linked.mkdir()
        (linked / ".git").write_text(
            "gitdir: /nowhere/.git/worktrees/linked\n", encoding="utf-8"
        )

        def decoded_nothing(*args, **kwargs):
            return subprocess.CompletedProcess(args, 0, stdout=None, stderr=None)

        monkeypatch.setattr(optin.subprocess, "run", decoded_nothing)
        assert optin.git_common_dir(str(linked)) == ""
        assert optin.home_at(str(linked)) == ""
        assert optin.home(str(linked)) == ""
        assert optin.opted_in(str(linked)) is False


class Test_home_paths:
    def test_accepts_the_two_places_shared_first(self, optin, repo):
        """#81. `seal import --into shared|local` has to be able to CREATE the
        root the user named, which `home_at` cannot answer: it reports where the
        root is, and the other mode's root is exactly the one that is not there.

        The pair is produced here so that command spells neither path itself.
        """
        shared, local = optin.home_paths(str(repo))
        assert shared == os.path.join(str(repo), "seal")
        assert local == os.path.join(str(repo), ".git", "seal")
        assert not os.path.isdir(shared) and not os.path.isdir(local), (
            "home_paths answers where a root WOULD be; nothing here exists yet"
        )

    def test_accepts_the_answer_home_at_gives_first(self, optin, repo):
        """The order is the mode's precedence, and it belongs with the pair
        rather than at each caller. With both roots present `home_at` returns the
        shared one, which is `home_paths`' first entry."""
        home(repo)
        local_home(repo)
        assert optin.home_at(str(repo)) == optin.home_paths(str(repo))[0]

    def test_accepts_a_common_dir_passed_and_asks_git_no_second_time(self, optin, repo):
        """A second `git` call here would be paid on every gated command. A
        caller that already resolved the common directory passes it, and
        nothing here asks git again."""
        common = optin.git_common_dir(str(repo))

        def refuse(*a, **k):
            raise AssertionError("home_paths asked git a second time")

        optin.subprocess.run, saved = refuse, optin.subprocess.run
        try:
            assert optin.home_paths(str(repo), common)[1] == os.path.join(
                common, "seal"
            )
        finally:
            optin.subprocess.run = saved

    def test_accepts_a_passed_common_directory_in_this_platforms_spelling(
        self, optin, tmp_path
    ):
        """The local place is spelled as this platform spells a path, however
        the common directory arrived (#1017, the body's local-normalisation
        row)."""
        common = str(tmp_path) + "/x/../.git"
        assert optin.home_paths(str(tmp_path), common)[1] == os.path.join(
            str(tmp_path), ".git", "seal"
        )

    @pytest.mark.parametrize(
        "seal, second, shared",
        [
            ("marked", "marked", "seal"),
            ("marked", "absent", "seal"),
            ("foreign", "marked", "agentic-seal"),
            ("absent", "marked", "agentic-seal"),
            ("absent", "absent", "seal"),
            ("foreign", "absent", "agentic-seal"),
            ("a file", "absent", "agentic-seal"),
            ("foreign", "foreign", "agentic-seal"),
        ],
    )
    def test_accepts_the_shared_place_the_tree_leaves_free(
        self, optin, repo, seal, second, shared
    ):
        """S2 of #1059. The shared entry is a marked `seal/`, else a marked
        `agentic-seal/`, else `seal/` where nothing stands at that path, else
        `agentic-seal/`; the local entry stays `seal` under the common
        directory in every state."""
        for name, state in (("seal", seal), ("agentic-seal", second)):
            if state == "marked":
                mark_root(repo / name)
            elif state == "foreign":
                readme_at(repo / name, FOREIGN)
            elif state == "a file":
                (repo / name).write_text("", encoding="utf-8")
        assert optin.home_paths(str(repo)) == (
            os.path.join(str(repo), shared),
            os.path.join(str(repo), ".git", "seal"),
        )

    def test_refuses_an_empty_root(self, optin):
        assert optin.home_paths("") == ("", "")


# The README a project keeps in a `seal/` of its own, which carries no marker.
FOREIGN = "# seal\n\nThis package's own notes.\n"


def readme_at(root, data):
    """`<root>/README.md` holding DATA, text or bytes, ROOT made where it is
    missing."""
    root.mkdir(parents=True, exist_ok=True)
    raw = data if isinstance(data, bytes) else data.encode("utf-8")
    (root / "README.md").write_bytes(raw)


class Test_marked:
    @pytest.mark.parametrize(
        "tail",
        [b"\n\nWhat it holds.\n", b"\r\n\r\nWhat it holds.\r\n", b"", b"\n\xff\xfe\n"],
        ids=["lf", "crlf", "no line end", "a stray byte below"],
    )
    def test_accepts_a_readme_whose_first_line_is_the_marker(
        self, optin, tmp_path, tail
    ):
        """The marker is the first line with its line end stripped, so either
        line end and a file of that one line all carry it, and a byte below
        the line that does not decode does not take it away."""
        readme_at(tmp_path / "seal", optin.MARKER.encode("utf-8") + tail)
        assert optin.marked(str(tmp_path / "seal"))

    @pytest.mark.parametrize(
        "text",
        [
            "# seal\n\nThis package's own notes.\n",
            "\n{marker}\n",
            "{marker} of a fork\n",
            "{marker} \n",
            "\N{BYTE ORDER MARK}{marker}\n",
            "",
        ],
        ids=[
            "another heading",
            "the marker on line two",
            "a longer line",
            "a space after it",
            "a byte order mark before it",
            "empty",
        ],
    )
    def test_refuses_a_readme_whose_first_line_is_another(self, optin, tmp_path, text):
        """A `seal/` a project or a package keeps for itself is not the
        plugin's root, whatever it holds below its first line. The line is
        compared whole with its line end alone taken off, so a space after the
        marker, a byte order mark before it and a blank line above it each
        make it another line, as `templates/setup/seal-README.md` says."""
        readme_at(tmp_path / "seal", text.format(marker=optin.MARKER))
        assert not optin.marked(str(tmp_path / "seal"))

    @pytest.mark.parametrize("shape", ["no README.md", "a directory", "not UTF-8"])
    def test_refuses_a_readme_there_is_no_first_line_to_read_in(
        self, optin, tmp_path, shape
    ):
        """No file, a directory of that name, and a first line that does not
        decode are no marker, and nothing raises: the module fails toward
        "not opted in"."""
        (tmp_path / "seal").mkdir()
        if shape == "a directory":
            (tmp_path / "seal" / "README.md").mkdir()
        elif shape == "not UTF-8":
            (tmp_path / "seal" / "README.md").write_bytes(b"\xff\xfe# What\n")
        assert not optin.marked(str(tmp_path / "seal"))

    def test_refuses_an_empty_path_wherever_the_process_stands(
        self, optin, tmp_path, monkeypatch
    ):
        """ "" is the answer `home_paths` gives for no root, and it names no
        README, even in a directory whose own README opens with the marker."""
        readme_at(tmp_path, optin.MARKER + "\n")
        monkeypatch.chdir(tmp_path)
        assert not optin.marked("")


class Test_home_at:
    def test_refuses_a_shared_root_without_the_marker(self, optin, repo):
        """`<repo>/seal/` holding a README of the project's own is not the
        root, and with no other place holding one the repository is out."""
        readme_at(repo / "seal", "# seal\n\nThis package's own notes.\n")
        assert optin.home_at(str(repo)) == ""
        assert not optin.opted_in(str(repo))

    def test_accepts_the_local_root_beside_a_projects_own_seal(self, optin, repo):
        """A project's own `<repo>/seal/` is passed over, and the local root
        under the common git directory is the answer where no
        `<repo>/agentic-seal/` carries the marker."""
        readme_at(repo / "seal", "# seal\n")
        readme_at(repo / ".git" / "seal", optin.MARKER + "\n")
        assert optin.home_at(str(repo)) == os.path.join(str(repo), ".git", "seal")

    @pytest.mark.parametrize(
        "seal, second, local, found",
        [
            ("marked", "marked", False, "seal"),
            ("foreign", "marked", True, "agentic-seal"),
            ("foreign", "foreign", True, ".git/seal"),
        ],
        ids=[
            "a marked seal over a marked agentic-seal",
            "a marked agentic-seal over the local root",
            "the local root where both are the project's own",
        ],
    )
    def test_accepts_the_three_places_in_their_order(
        self, optin, repo, seal, second, local, found
    ):
        """S2 of #1059: a marked `seal/`, then a marked `agentic-seal/`, then
        the local root."""
        for name, state in (("seal", seal), ("agentic-seal", second)):
            if state == "marked":
                mark_root(repo / name)
            else:
                readme_at(repo / name, FOREIGN)
        if local:
            local_home(repo)
        assert optin.home_at(str(repo)) == os.path.join(str(repo), *found.split("/"))


class Test_home_name_in:
    def test_accepts_the_first_name_whose_readme_opens_with_the_marker(self, optin):
        """The tree is read through a callable, as `chain_check.py` reads one
        at a commit: `seal` where its README carries the marker, else
        `agentic-seal`, and either line end."""
        both = {
            "seal/README.md": optin.MARKER + "\n",
            "agentic-seal/README.md": optin.MARKER + "\n",
        }
        assert optin.home_name_in(both.get) == "seal"
        second = {
            "seal/README.md": FOREIGN,
            "agentic-seal/README.md": optin.MARKER + "\r\n\r\nWhat it holds.\r\n",
        }
        assert optin.home_name_in(second.get) == "agentic-seal"

    def test_refuses_a_tree_where_neither_readme_opens_with_the_marker(self, optin):
        """No README, a project's own and the marker on line two are no root,
        and the answer is "" rather than a guess."""
        tree = {
            "seal/README.md": FOREIGN,
            "agentic-seal/README.md": "\n" + optin.MARKER + "\n",
        }
        assert optin.home_name_in(tree.get) == ""
        assert optin.home_name_in({}.get) == ""


class Test_home_name:
    @pytest.mark.parametrize("name", ["seal", "agentic-seal"])
    def test_accepts_the_shared_root_in_force_by_its_name(self, optin, repo, name):
        """The name a reader classifying paths as git prints them takes:
        `agentic-seal` beside a project's own `seal/`, and `seal` where that
        one carries the marker."""
        if name == "agentic-seal":
            readme_at(repo / "seal", FOREIGN)
        mark_root(repo / name)
        local_home(repo)
        assert optin.home_name(str(repo)) == name

    @pytest.mark.parametrize("shape", ["local", "absent", "scratch"])
    def test_refuses_a_root_that_is_not_the_shared_one(self, optin, repo, shape):
        """A local root, no root and a repository marked throwaway have no
        repository-relative name, so the answer is ""."""
        readme_at(repo / "seal", FOREIGN)
        if shape == "local":
            local_home(repo)
        elif shape == "scratch":
            mark_root(repo / "agentic-seal")
            scratch(repo)
        assert optin.home_name(str(repo)) == ""


class Test_home:
    def test_accepts_the_shared_root_where_both_exist(self, optin, repo):
        home(repo)
        local_home(repo)
        assert optin.home(str(repo)) == os.path.join(str(repo), "seal")

    def test_accepts_the_worktrees_own_shared_root_over_the_common_local_one(
        self, optin, repo, tmp_path
    ):
        """S1's order, from a linked worktree: `<repo>/seal/` is read first, and
        the worktree's own tree is the repository here."""
        local_home(repo)
        other = linked_worktree(repo, tmp_path)
        mark_root(other / "seal")
        assert os.path.samefile(optin.home(str(other)), other / "seal")

    def test_refuses_a_file_named_seal_under_the_git_directory(self, optin, repo):
        """The signal is a DIRECTORY at either place. A file of that name under
        the common directory is not a home, and nothing raises over it."""
        (repo / ".git" / "seal").write_text("", encoding="utf-8")
        assert not optin.opted_in(str(repo))
        assert optin.home(str(repo)) == ""


class Test_opted_in:
    def test_accepts_the_new_home(self, optin, repo):
        home(repo)
        assert optin.opted_in(str(repo))
        assert optin.home(str(repo)) == os.path.join(str(repo), "seal")

    def test_accepts_the_git_directory_as_the_second_place(self, optin, repo):
        """S2, Q3 (a). Nothing in 0.4.0 creates `.git/seal/`; the scripts read it
        so that #80 changes where the folder is created and nothing that reads
        it."""
        local_home(repo)
        assert optin.opted_in(str(repo))
        assert optin.home(str(repo)) == os.path.join(str(repo), ".git", "seal")

    def test_accepts_the_same_answer_from_a_subdirectory(self, optin, repo):
        home(repo)
        sub = repo / "a" / "b"
        sub.mkdir(parents=True)
        assert optin.opted_in(str(sub))

    def test_accepts_a_linked_worktree_through_the_main_trees_common_root(
        self, optin, repo, tmp_path
    ):
        """S2. `.git/seal/` is under the COMMON git directory, so a linked
        worktree, whose `.git` is a file, reads the main tree's root."""
        home = local_home(repo)
        other = linked_worktree(repo, tmp_path)
        assert optin.opted_in(str(other))
        assert os.path.samefile(optin.home(str(other)), home)
        assert os.path.samefile(home, repo / ".git" / "seal")

    def test_accepts_the_answer_it_always_gave_without_the_scratch_file(
        self, optin, repo
    ):
        """The scratch file is the whole difference, so removing the condition
        turns the scratch case red and nothing else moves."""
        home(repo)
        assert optin.opted_in(str(repo))

    def test_accepts_a_directory_of_the_scratch_files_name_as_no_opt_out(
        self, optin, repo
    ):
        """The signal is an empty FILE, and `os.path.exists` did not say so.

        A directory created where the marker used to live turned every gate off
        in every clone of the repository — a kill switch nobody typed. Both the
        module's own docstring and `seal/README.md` say "file"; this is the read
        catching up with them.
        """
        home(repo)
        (repo / ".git" / "agentic-scratch").mkdir()
        assert optin.opted_in(str(repo))

    def test_accepts_the_old_scratch_file_as_an_ordinary_file(self, optin, repo):
        """Q4. `.specseal/scratch` used to be the opt-out and sat in a committed
        directory. A file of that name under the root is an ordinary file now,
        and nothing reads the old one."""
        home(repo)
        (repo / "seal" / "scratch").write_text("", encoding="utf-8")
        (repo / ".specseal").mkdir()
        (repo / ".specseal" / "scratch").write_text("", encoding="utf-8")
        assert optin.opted_in(str(repo))

    def test_refuses_the_legacy_directory(self, optin, repo):
        """S3. Without this case the constant can come back and everything stays
        green.

        `.specseal/` reads as an ordinary directory now. A repository still
        holding one is a repository that never opted in, which is the same
        standing as any other repository on the machine, and nothing reads
        the name.
        """
        legacy(repo)
        assert not optin.opted_in(str(repo))
        assert not hasattr(optin, "LEGACY"), "the second address is gone, not renamed"

    def test_refuses_a_repository_with_neither_place(self, optin, repo):
        assert not optin.opted_in(str(repo))

    def test_refuses_a_path_outside_any_repo(self, optin, tmp_path):
        assert not optin.opted_in(str(tmp_path / "nowhere"))

    def test_refuses_a_config_key_or_an_environment_variable(
        self, optin, repo, monkeypatch
    ):
        """S1. The place the root is at says both "on" and which mode; nothing
        else is read. Asked two ways: the module's source names no config key
        and no environment variable, and a repository carrying both a git config
        answer and an environment variable, with `seal/` at neither place, is
        still out."""
        src = open(optin.__file__, encoding="utf-8").read()
        for word in ('"config"', "'config'", "environ", "getenv"):
            assert word not in src, f"optin.py reads a key: {word}"
        subprocess.run(
            ["git", "-C", str(repo), "config", "agentic.mode", "local"],
            check=True,
            capture_output=True,
        )
        monkeypatch.setenv("AGENTIC_MODE", "local")
        assert not optin.opted_in(str(repo))
        assert optin.home(str(repo)) == ""

    def test_refuses_a_repository_carrying_the_scratch_marker(self, optin, repo):
        """S4. A `seal/` directory is the whole opt-in signal, so a git
        repository that exists for thirty seconds as a fixture is indistinguishable
        from a repository under review — and reproducing a gate decision by hand,
        which is what developing these gates consists of, cost a waiver on every
        command (issue #68).

        The marker is written once, by a person, in the repository being thrown
        away. The fixture builders in this suite are untouched: they assert that
        the gates FIRE, and a marker silencing them would invert what they test.
        """
        home(repo)
        scratch(repo)
        assert not optin.opted_in(str(repo))

    def test_refuses_the_scratch_marker_from_a_subdirectory(self, optin, repo):
        home(repo)
        scratch(repo)
        sub = repo / "a" / "b"
        sub.mkdir(parents=True)
        assert not optin.opted_in(str(sub))

    def test_refuses_the_scratch_marker_in_a_linked_worktree(
        self, optin, repo, tmp_path
    ):
        """The common directory is shared, so the opt-out is too: a fixture with
        two worktrees is one throwaway repository, not one and a half."""
        home(repo)
        scratch(repo)
        other = tmp_path / "linked"
        subprocess.run(
            ["git", "-C", str(repo), "worktree", "add", "-q", str(other), "feature/x"],
            check=True,
            capture_output=True,
        )
        mark_root(other / "seal")
        assert not optin.opted_in(str(other))


class Test_module:
    def test_the_template_opens_with_the_marker(self, optin):
        """The template is what first setup writes into a root, so its first
        line and the constant are one value, pinned here."""
        with open(
            os.path.join(ROOT, "templates", "setup", "seal-README.md"), encoding="utf-8"
        ) as f:
            assert f.readline().rstrip("\r\n") == optin.MARKER

    def test_the_move_notice_is_gone(self, optin):
        """Deleted, not muted. A notice with nobody left to warn is a branch that
        runs in no repository and still has to be kept true."""
        for name in ("legacy_only", "MOVE_NOTICE", "notice_due", "NOTICE_DIR"):
            assert not hasattr(optin, name), name

    def test_the_local_root_is_never_a_commit_candidate_and_needs_no_gitignore(
        self, repo
    ):
        """S3. A declaration, a round record and a ledger fragment under the
        local root are listed by nothing and staged by nothing: git never lists
        its own directory, so no `.gitignore` line exists for it."""
        home = local_home(repo)
        item = home / "threads" / "1788000000-a-work-item"
        (item / "trail" / "rounds").mkdir(parents=True)
        (item / "routing.md").write_text("# routing\n", encoding="utf-8")
        (item / "trail" / "rounds" / "round-1.md").write_text(
            "# round 1\n", encoding="utf-8"
        )
        (home / "ledger").mkdir()
        (home / "ledger" / "1788000000-a-work-item.md").write_text(
            "# rows\n", encoding="utf-8"
        )
        git = lambda *a: (
            subprocess.run(
                ["git", "-C", str(repo), *a],
                check=True,
                capture_output=True,
                encoding="utf-8",
                errors="replace",
            ).stdout
        )
        assert git("status", "--porcelain") == ""
        git("add", "-A")
        assert git("diff", "--cached", "--name-only") == ""
        assert not (repo / ".gitignore").exists()

    def test_a_scratch_marker_under_the_common_directory_keeps_the_stamp_silent(
        self, local
    ):
        """The stamp's drawer, `seal stamp --stop`, asks `opted_in` before it
        speaks. A stamp waits in the clone in local mode, and nothing is drawn
        while the scratch marker stands under the common directory; with the
        marker gone, the same `Stop` draws it."""
        repo, _home = local
        stamp = load_module(STAMP, "seal_stamp_for_the_scratch_marker")
        stamp.write_values(str(repo / ".git"), STAMP_VALUES)
        marker = repo / ".git" / "agentic-scratch"
        marker.write_text("", encoding="utf-8")
        stop = json.dumps({"hook_event_name": "Stop", "cwd": str(repo)})

        assert stamp.drawn_at_stop(stop) is None
        marker.unlink()
        assert stamp.drawn_at_stop(stop).startswith("SEALED aaa1111")


test_census = census_case(TARGET)
