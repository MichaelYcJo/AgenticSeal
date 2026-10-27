"""`hooks/root-migrate.py`, one class per function.

Rebuilt by #942's phase 5. The hook moves what `moves` lists at session
start, on whichever branch is checked out, and every step asks git, so the
cases run git.
`moves` lists nothing in this tree, and the 0.3.x layout is not read at all:
a case of `Test_main` pins that. The move itself takes
any paths, so the cases that pin its boundaries hand it `UNITS`, through the
`moving` fixture where they run `main`. Two repositories are built once for
the module and copied for each case: a tree holding the 0.3.x layout,
committed (a map and a map directory under `.specseal/` beside its README and
follow-up list, one work item and one foreign directory under `specs/`), and
a fresh repository holding one commit. Each copy is the reset. The state
directories the hook renames are under each case's own directory.
"""

import io
import json
import os
import shutil
import subprocess
import sys

import pytest
from conftest import (
    ROOT,
    ROOT_MARKER,
    census_case,
    commit_everything_as_e,
    git,
    load_hook_module,
    mark_root,
    staged,
    symlink_or_skip,
    write,
)

TARGET = "hooks/root-migrate.py"

# The subcommand a case makes fail, named once: a call spelling it would
# read as a path listing to `tests/test_a_shrunken_corpus_declines_to_judge.py`.
LS_FILES = "ls-files"

ROUND = (
    "# round 1\n\n| Field | Value |\n|---|---|\n| Target SHA | abc |\n\n- [x] Pass\n"
)
ROUTING = "# routing\n\n| Axis | Answer |\n|---|---|\n| Review | straight to the PR |\n"
FOLLOW_UP = "# Follow-up\n\nnothing scheduled\n"
OLD_README = "# .specseal/ — the old text, describing a layout that is gone\n"
ITEM = "1788000000-a-work-item"
TEAM = "1788000001-team-thing"
# 0.3.x's ledger, a file and a directory beside it in the fixture's tree.
MAP = "# map\n\n| Clause | Coordinate |\n|---|---|\n| A | a row |\n"
# What the cases of the move's boundaries hand it over `proj`'s tree: the
# README first, then the rest of `.specseal/`, then the work item.
UNITS = [
    ("readme", ".specseal/README.md", "seal/README.md"),
    ("other", ".specseal/follow-up.md", "seal/follow-up.md"),
    ("other", ".specseal/map", "seal/map"),
    ("other", ".specseal/map.md", "seal/map.md"),
    ("other", f"specs/{ITEM}", f"seal/specs/{ITEM}"),
]
MOVED_ALL = "moved .specseal/ and specs/ into seal/"

MIGRATE = load_hook_module("root-migrate.py", "root_migrate_under_test")


commit = commit_everything_as_e


def commit_staged(repo):
    """What the hook staged, committed as the notice asks."""
    git(
        repo,
        "-c",
        "user.email=e@example.com",
        "-c",
        "user.name=e",
        "commit",
        "-qm",
        "m",
    )


def unstaged(repo):
    """The paths changed in REPO's worktree and not staged."""
    return git(repo, "diff", "--name-only").stdout


def tracked(repo, *paths):
    """What git tracks in REPO under PATHS."""
    return git(repo, "ls-files", "--", *paths).stdout


def init(d):
    d.mkdir(parents=True)
    git(d, "init", "-q", "-b", "main")


@pytest.fixture(scope="module")
def _templates(tmp_path_factory):
    """`proj`, the old layout committed, and `fresh`, one commit and nothing
    old, built once for the module."""
    base = tmp_path_factory.mktemp("root-world")
    d = base / "proj"
    init(d)
    write(d, ".specseal/README.md", OLD_README)
    write(d, ".specseal/follow-up.md", FOLLOW_UP)
    write(d, f"specs/{ITEM}/routing.md", ROUTING)
    write(d, f"specs/{ITEM}/rounds/round-1.md", ROUND)
    write(d, "specs/notes/todo.md", "# not SpecSeal's\n")
    write(d, ".specseal/map.md", MAP)
    write(d, f".specseal/map/{ITEM}.md", MAP.replace("# map", f"# {ITEM}"))
    commit(d, "the old layout, committed")
    f = base / "fresh"
    init(f)
    write(f, "f.txt", "one\n")
    commit(f, "base")
    return base


@pytest.fixture
def proj(_templates, tmp_path):
    shutil.copytree(_templates / "proj", tmp_path / "proj", symlinks=True)
    return tmp_path / "proj"


@pytest.fixture
def fresh(_templates, tmp_path):
    shutil.copytree(_templates / "fresh", tmp_path / "fresh", symlinks=True)
    return tmp_path / "fresh"


@pytest.fixture
def hook(tmp_path, monkeypatch):
    """The hook with both state directories under the case's own directory,
    so no case renames the machine's own `~/.claude/` state."""
    monkeypatch.setattr(MIGRATE, "OLD_STATE_DIR", str(tmp_path / "old-state"))
    monkeypatch.setattr(MIGRATE, "STATE_DIR", str(tmp_path / "state"))
    return MIGRATE


@pytest.fixture
def moving(hook, monkeypatch):
    """The hook with `moves` listing `UNITS` less what has already moved,
    which is how a list read off the tree resumes a stopped run."""

    def still_to_move(root):
        return [u for u in UNITS if os.path.lexists(hook.under(root, u[1]))]

    monkeypatch.setattr(hook, "moves", still_to_move)
    return hook


def start(hook, repo, payload=None):
    """One session start at REPO, or with the stdin PAYLOAD as written;
    returns what the hook printed."""
    out = io.StringIO()
    stdin, stdout = sys.stdin, sys.stdout
    sys.stdin = io.StringIO(
        json.dumps({"cwd": str(repo)}) if payload is None else payload
    )
    sys.stdout = out
    try:
        hook.main()
    finally:
        sys.stdin, sys.stdout = stdin, stdout
    return out.getvalue()


def message(out):
    return json.loads(out)["systemMessage"] if out.strip() else ""


def failing(real, word, how="raise"):
    """HOOK.git with the subcommand WORD raising, or answering exit 1."""

    def git_but(root, *args):
        if args[0] == word:
            if how == "raise":
                raise OSError(f"no {word} today")
            return subprocess.CompletedProcess(args, 1, "", "refused")
        return real(root, *args)

    return git_but


class Test_MoveError:
    def test_accepts_a_unit_and_its_error_as_resumable_by_default(self):
        error = MIGRATE.MoveError("a/b", "disk full")
        assert (error.path, error.error, error.resumable) == ("a/b", "disk full", True)
        assert str(error) == "a/b: disk full"

    def test_refuses_to_promise_a_continuation_where_it_was_told_not_to(self):
        assert not MIGRATE.MoveError("a", "b", resumable=False).resumable


class Test_sources:
    def test_accepts_each_directory_a_unit_comes_from_once_sorted(self):
        assert MIGRATE.sources(UNITS) == [".specseal", "specs"]

    def test_refuses_a_directory_no_unit_comes_from(self):
        assert MIGRATE.sources(UNITS[:4]) == [".specseal"]
        assert MIGRATE.sources([]) == []


class Test_dirty:
    def test_accepts_a_committed_tree_and_a_stopped_runs_staged_renames(
        self, hook, proj
    ):
        assert not hook.dirty(str(proj), UNITS)
        (proj / "seal").mkdir()
        git(proj, "mv", ".specseal/map.md", "seal/map.md")
        git(proj, "rm", "-q", ".specseal/follow-up.md")
        assert not hook.dirty(str(proj), UNITS)

    @pytest.mark.parametrize(
        "shape", ["a worktree edit", "a staged edit", "an untracked file"]
    )
    def test_refuses_work_in_progress_under_a_units_directory(self, hook, proj, shape):
        if shape == "an untracked file":
            write(proj, f"specs/{ITEM}/overview.md", "# not yet added\n")
        else:
            ledger = proj / ".specseal" / "map.md"
            ledger.write_text(MAP + "| E | half a row |\n", encoding="utf-8")
            if shape == "a staged edit":
                git(proj, "add", "-A")
        assert hook.dirty(str(proj), UNITS)

    @pytest.mark.parametrize(
        "word, how", [(LS_FILES, "raise"), ("status", "raise"), ("status", "exit")]
    )
    def test_refuses_a_git_that_cannot_answer(self, hook, proj, monkeypatch, word, how):
        monkeypatch.setattr(hook, "git", failing(hook.git, word, how))
        assert hook.dirty(str(proj), UNITS)


class Test_tracked_names:
    def test_accepts_the_top_level_names_git_tracks_sorted(self, hook, proj):
        write(proj, ".gitignore", ".DS_Store\n")
        write(proj, ".specseal/.DS_Store", "\0")
        assert hook.tracked_names(str(proj), ".specseal") == [
            "README.md",
            "follow-up.md",
            "map",
            "map.md",
        ]
        assert hook.tracked_names(str(proj), "specs") == [ITEM, "notes"]

    def test_refuses_to_answer_where_git_cannot(self, hook, proj, monkeypatch):
        monkeypatch.setattr(hook, "git", failing(hook.git, LS_FILES, "exit"))
        assert hook.tracked_names(str(proj), ".specseal") is None


class Test_entries:
    def test_accepts_gits_list_and_the_directory_where_git_cannot_answer(
        self, hook, proj, monkeypatch
    ):
        write(proj, "specs/untracked/x.md", "x\n")
        assert hook.entries(str(proj), "specs") == [ITEM, "notes"]
        monkeypatch.setattr(hook, "git", failing(hook.git, LS_FILES))
        assert hook.entries(str(proj), "specs") == [ITEM, "notes", "untracked"]
        assert hook.entries(str(proj), "nowhere") == []

    def test_refuses_an_untracked_file_where_git_tracks_nothing_left(self, hook, proj):
        git(proj, "rm", "-rq", ".specseal")
        write(proj, ".specseal/.DS_Store", "\0")
        assert hook.entries(str(proj), ".specseal") == []


class Test_git_mv:
    def test_accepts_one_staged_rename_making_its_parent(self, hook, proj):
        hook.git_mv(str(proj), ".specseal/map.md", "seal/deep/map.md")
        assert "seal/deep/map.md" in staged(proj)
        assert not (proj / ".specseal" / "map.md").exists()

    def test_refuses_a_parent_that_cannot_be_made_and_a_rename_git_refuses(
        self, hook, proj
    ):
        write(proj, "seal", "not a directory\n")
        with pytest.raises(hook.MoveError) as stopped:
            hook.git_mv(str(proj), ".specseal/map.md", "seal/map.md")
        assert stopped.value.error.startswith("cannot create seal/: ")
        assert not stopped.value.resumable
        with pytest.raises(hook.MoveError) as stopped:
            hook.git_mv(str(proj), ".specseal/gone.md", "x/gone.md")
        assert stopped.value.resumable and stopped.value.error, stopped.value.error


class Test_taken:
    def test_accepts_both_ways_a_person_settles_it(self):
        error = MIGRATE.taken(".specseal/map.md", "seal/map.md")
        assert error.error == (
            "seal/map.md already exists — keep one by hand: git rm "
            ".specseal/map.md if seal/map.md is the newer, or git rm seal/map.md "
            "to let the move bring the old one over"
        )

    def test_refuses_to_call_it_resumable(self):
        assert not MIGRATE.taken("a", "b").resumable


class Test_move:
    def test_accepts_a_directory_whole_or_file_by_file_into_one_that_exists(
        self, hook, proj
    ):
        hook.move(str(proj), ".specseal/map", "seal/map")
        assert (proj / "seal" / "map" / f"{ITEM}.md").is_file()
        write(proj, f"specs/{ITEM}/phases/deep/p.md", "# two directories down\n")
        commit(proj, "a file two directories down the item")
        write(proj, f"seal/specs/{ITEM}/spec.md", "# already here\n")
        hook.move(str(proj), f"specs/{ITEM}", f"seal/specs/{ITEM}")
        for rel in ("rounds/round-1.md", "phases/deep/p.md", "routing.md"):
            assert (proj / "seal" / "specs" / ITEM / rel).is_file(), rel
        assert not (proj / "seal" / "specs" / ITEM / ITEM).exists()
        assert not (proj / "specs" / ITEM / "rounds").exists(), "an emptied one stayed"
        assert not (proj / "specs" / ITEM).exists(), "the item's directory stayed"

    def test_refuses_a_file_already_at_its_destination(self, hook, proj):
        """The file already there is named and the walk stops at it: the
        files git lists before it have moved, and it stays at its source."""
        write(proj, "seal/map.md", "# the newer map\n")
        with pytest.raises(hook.MoveError, match=r"seal/map\.md already exists"):
            hook.move(str(proj), ".specseal/map.md", "seal/map.md")
        write(proj, f"specs/{ITEM}/spec.md", "# the old spec\n")
        write(proj, f"seal/specs/{ITEM}/spec.md", "# the newer spec\n")
        commit(proj, "both spec.md")
        with pytest.raises(hook.MoveError, match="already exists"):
            hook.move(str(proj), f"specs/{ITEM}", f"seal/specs/{ITEM}")
        assert (proj / "specs" / ITEM / "spec.md").is_file()
        assert (proj / "seal" / "specs" / ITEM / "routing.md").is_file()

    def test_refuses_to_remove_a_directory_an_ignored_file_holds_under_any_rmdir(
        self, hook, proj, monkeypatch
    ):
        """An ignored file keeps its directory, and the item's above it, on
        disk. Contract rule 13: `rmdir` is given a semantics that removes a
        directory whatever it holds, so the case pins `move`'s own reading of
        emptiness and not the platform's refusal."""
        real = os.rmdir

        def rmdir_whatever_it_holds(path, *args, **kwargs):
            for here, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    os.unlink(os.path.join(here, name))
                for name in dirs:
                    real(os.path.join(here, name))
            real(path, *args, **kwargs)

        write(proj, ".gitignore", ".DS_Store\n")
        commit(proj, "ignore the finder's file")
        write(proj, f"specs/{ITEM}/rounds/.DS_Store", "\0")
        write(proj, f"seal/specs/{ITEM}/spec.md", "# already here\n")
        monkeypatch.setattr(hook.os, "rmdir", rmdir_whatever_it_holds)
        hook.move(str(proj), f"specs/{ITEM}", f"seal/specs/{ITEM}")
        assert (proj / "seal" / "specs" / ITEM / "rounds" / "round-1.md").is_file()
        assert (proj / "specs" / ITEM / "rounds" / ".DS_Store").is_file()


class Test_rewrite_readme:
    def test_accepts_the_moved_readme_as_the_templates_text_staged(self, hook, proj):
        hook.move(str(proj), ".specseal/README.md", "seal/README.md")
        hook.rewrite_readme(str(proj), "seal/README.md")
        with open(
            os.path.join(ROOT, "templates", "seal-README.md"), encoding="utf-8"
        ) as handle:
            assert (proj / "seal" / "README.md").read_text(
                encoding="utf-8"
            ) == handle.read()
        assert "seal/README.md" not in unstaged(proj)

    def test_refuses_to_stop_over_a_template_that_will_not_read(
        self, hook, proj, monkeypatch
    ):
        monkeypatch.setattr(hook, "TEMPLATE", str(proj / "gone.md"))
        hook.move(str(proj), ".specseal/README.md", "seal/README.md")
        hook.rewrite_readme(str(proj), "seal/README.md")
        assert (proj / "seal" / "README.md").read_text(encoding="utf-8") == OLD_README


class Test_run_moves:
    def test_accepts_every_unit_and_takes_away_the_emptied_roots(self, hook, proj):
        git(proj, "rm", "-rq", "specs/notes")
        commit(proj, "only the work item under specs/")
        assert hook.run_moves(str(proj), UNITS) == (5, None)
        assert not (proj / ".specseal").exists() and not (proj / "specs").exists()

    def test_refuses_to_go_past_a_unit_that_stopped_and_counts_what_moved(
        self, hook, proj, monkeypatch
    ):
        real, calls = hook.git_mv, []

        def flaky(root, src, dst):
            calls.append(src)
            if len(calls) == 3:
                raise hook.MoveError(src, "disk full")
            real(root, src, dst)

        monkeypatch.setattr(hook, "git_mv", flaky)
        done, error = hook.run_moves(str(proj), UNITS)
        assert (done, error.error) == (2, "disk full")

    def test_refuses_to_remove_a_linked_specs_under_windows_rmdir(
        self, hook, proj, monkeypatch
    ):
        """PR #700's `windows-latest` leg: Windows' `RemoveDirectoryW`
        removes a directory link itself, whatever is behind it. Contract
        rule 13: the POSIX guarantee is removed here, by giving `rmdir`
        Windows' semantics for a link. A team's linked `specs/` beside a run
        whose units come from `.specseal/` alone stays a link."""
        real = os.rmdir

        def windows_rmdir(path, *args, **kwargs):
            if os.path.islink(path):
                os.unlink(path)
                return
            real(path, *args, **kwargs)

        git(proj, "rm", "-rq", "specs")
        write(proj, f"team/{TEAM}/spec.md", "# the team's own specification\n")
        symlink_or_skip("team", proj / "specs")
        commit(proj, "the team's specs/ is a link")
        monkeypatch.setattr(hook.os, "rmdir", windows_rmdir)
        assert hook.run_moves(str(proj), UNITS[:4]) == (4, None)
        assert os.path.islink(proj / "specs"), "the cleanup removed the team's link"


class Test_listed:
    def test_accepts_one_directory_or_two_joined(self):
        assert MIGRATE.listed(["specs"]) == "specs/"
        assert MIGRATE.listed([".specseal", "specs"]) == ".specseal/ and specs/"

    def test_refuses_to_name_anything_for_no_directory(self):
        assert MIGRATE.listed([]) == ""


class Test_main:
    def test_accepts_the_first_start_as_the_move_said_in_one_line(self, moving, proj):
        """S5: every move staged, nothing left unstaged, and after the commit
        the notice asks for, `--follow` reaches the file's old name."""
        hook = moving
        out = message(start(hook, proj))
        assert out == f"agentic:{MOVED_ALL} — review the diff and commit", out
        for rel in (
            "seal/README.md",
            "seal/map.md",
            f"seal/map/{ITEM}.md",
            "seal/follow-up.md",
            f"seal/specs/{ITEM}/routing.md",
            f"seal/specs/{ITEM}/rounds/round-1.md",
        ):
            assert (proj / rel).is_file(), rel
        assert (proj / "specs" / "notes" / "todo.md").is_file()
        assert not (proj / ".specseal").exists(), "the old root was left behind"
        assert (proj / "seal" / "map.md").read_text(encoding="utf-8") == MAP
        assert unstaged(proj) == ""
        assert (
            f"R100\tspecs/{ITEM}/rounds/round-1.md\tseal/specs/{ITEM}/rounds/round-1.md"
            in git(proj, "diff", "--cached", "--name-status", "-M").stdout
        )
        commit_staged(proj)
        log = git(
            proj,
            "log",
            "--follow",
            "--oneline",
            "--",
            f"seal/specs/{ITEM}/rounds/round-1.md",
        ).stdout
        assert "the old layout, committed" in log, log
        assert start(hook, proj) == "", "the second session start spoke"

    def test_accepts_a_move_by_hand_that_stopped_halfway_and_a_fragment_there(
        self, moving, proj
    ):
        """S7: what remains moves, a directory already at its destination is
        merged file by file."""
        hook = moving
        (proj / "seal").mkdir()
        git(proj, "mv", ".specseal/map.md", "seal/map.md")
        write(proj, "seal/map/another.md", "# another fragment\n")
        commit(proj, "half a move, by hand")
        assert MOVED_ALL in message(start(hook, proj))
        assert (proj / "seal" / "map" / f"{ITEM}.md").is_file()
        assert (proj / "seal" / "map" / "another.md").is_file()
        assert not (proj / "seal" / "map" / "map").exists(), (
            "moved INTO the destination"
        )
        assert not (proj / ".specseal").exists()

    def test_accepts_an_ignored_file_under_a_source_left_where_it_is(
        self, moving, proj
    ):
        """Round 1's red 1: what moves is what git tracks, so an ignored file
        is left, and `.specseal/` may stay holding nothing else."""
        hook = moving
        write(proj, ".gitignore", ".DS_Store\n")
        commit(proj, "ignore the finder's file")
        write(proj, ".specseal/.DS_Store", "\0")
        assert MOVED_ALL in message(start(hook, proj))
        assert tracked(proj, ".specseal", f"specs/{ITEM}") == ""
        assert os.listdir(proj / ".specseal") == [".DS_Store"]
        assert start(hook, proj) == "", "nothing tracked is left, so nothing to say"

    @pytest.mark.parametrize(
        "shape", ["a worktree edit", "an untracked file", "ls-files raises"]
    )
    def test_refuses_to_move_over_work_in_progress(
        self, moving, proj, monkeypatch, shape
    ):
        """S6: the refusal says why and touches nothing, and the next clean
        start moves."""
        hook = moving
        if shape == "a worktree edit":
            (proj / ".specseal" / "map.md").write_text(
                MAP + "| E |\n", encoding="utf-8"
            )
        elif shape == "an untracked file":
            write(proj, f"specs/{ITEM}/overview.md", "# not yet added\n")
        else:
            monkeypatch.setattr(hook, "git", failing(hook.git, LS_FILES))
        out = message(start(hook, proj))
        assert out == (
            "agentic:the old layout under .specseal/ and specs/ holds "
            "uncommitted changes — not touching work in progress. Commit, then "
            "the next session start moves it into seal/."
        ), out
        assert (proj / ".specseal" / "map.md").is_file()
        assert not (proj / "seal").exists()

    def test_refuses_to_finish_a_stopped_move_and_the_next_start_continues(
        self, moving, proj, monkeypatch
    ):
        hook = moving
        real, calls = hook.git_mv, []

        def flaky(root, src, dst):
            calls.append(src)
            if len(calls) == 3:
                raise hook.MoveError(src, "disk full")
            real(root, src, dst)

        monkeypatch.setattr(hook, "git_mv", flaky)
        out = message(start(hook, proj))
        assert out == (
            "agentic:moved 2 of 5 into seal/ and stopped at .specseal/map: disk "
            "full. The next session start continues."
        ), out
        monkeypatch.setattr(hook, "git_mv", real)
        assert MOVED_ALL in message(start(hook, proj))
        assert not (proj / ".specseal").exists()

    @pytest.mark.parametrize("shape", ["a file named seal", "a file at seal/map.md"])
    def test_refuses_a_stop_a_person_has_to_settle(self, moving, proj, shape):
        hook = moving
        if shape == "a file named seal":
            write(proj, "seal", "not a directory\n")
            said = "stopped at .specseal/README.md: cannot create seal/: "
        else:
            write(proj, "seal/map.md", "# the newer map\n")
            said = (
                "stopped at .specseal/map.md: seal/map.md already exists — keep one "
                "by hand: git rm .specseal/map.md"
            )
        commit(proj, shape)
        out = message(start(hook, proj))
        assert said in out, out
        assert out.endswith(
            "Settle that by hand, then the next session start continues."
        )
        assert (proj / ".specseal" / "map.md").is_file()

    def test_refuses_to_speak_where_nothing_is_old(self, moving, fresh):
        """Silent with nothing old and no root, and nothing written."""
        hook = moving
        assert start(hook, fresh) == ""
        assert git(fresh, "status", "--porcelain").stdout == ""
        assert not os.path.exists(hook.STATE_DIR)

    def test_refuses_to_read_another_tools_specs_or_the_0_3_x_root(self, hook, proj):
        """A repository holding another tool's `specs/<unix-seconds>-<slug>/`
        with a tracked `routing.md`, and a `.specseal/` beside it, hears
        nothing at session start, and nothing in it moves or is staged."""
        before = tracked(proj)
        assert start(hook, proj) == ""
        assert tracked(proj) == before
        assert git(proj, "status", "--porcelain").stdout == ""
        assert not (proj / "seal").exists()

    @pytest.mark.parametrize(
        "payload",
        ["[]", '["x"]', '{"cwd": ""}', "{"],
        ids=["an empty list", "a list", "no cwd", "not json"],
    )
    def test_refuses_a_payload_that_names_no_directory(self, hook, payload):
        assert start(hook, None, payload) == ""

    def test_accepts_a_branch_cut_before_the_move_moved_at_its_own_start(
        self, hook, layout
    ):
        """A branch cut before the move, checked out after the move was
        committed on `main`, still holds its own work item under
        `seal/specs/`, and its own session start moves it: no stamp stands
        between a branch and its move."""
        other = "1788000002-another-item"
        git(layout, "switch", "-qc", "feat/b")
        write(layout, f"seal/specs/{other}/routing.md", ROUTING)
        commit(layout, "a second work item on its own branch")
        git(layout, "switch", "-q", "main")
        start(hook, layout)
        commit_staged(layout)
        git(layout, "switch", "-q", "feat/b")
        said = message(start(hook, layout))
        assert said.startswith("agentic:moved seal/specs/ into seal/"), said
        assert (layout / "seal" / "threads" / other / "routing.md").is_file()
        assert not (layout / "seal" / "specs").exists()
        assert first_line(layout / "seal" / "README.md") == ROOT_MARKER

    def test_refuses_to_write_the_tree_beside_a_local_root(self, hook, fresh, tmp_path):
        """S9 of #80: with only a marked `.git/seal/` the hook says nothing,
        and a branch carrying the 0.3.x layout checked out later puts nothing
        into the tree the person chose to keep clean. A linked worktree,
        which reads the main tree's root, is as silent."""
        git(fresh, "checkout", "-q", "-b", "old-layout")
        write(fresh, ".specseal/README.md", OLD_README)
        write(fresh, f"specs/{ITEM}/routing.md", ROUTING)
        commit(fresh, "the 0.3.x layout")
        git(fresh, "checkout", "-q", "main")
        mark_root(fresh / ".git" / "seal")
        assert start(hook, fresh) == ""
        git(fresh, "checkout", "-q", "old-layout")
        assert start(hook, fresh) == ""
        assert not (fresh / "seal").exists(), "the old layout was moved into the tree"
        assert git(fresh, "status", "--porcelain").stdout == ""
        linked = tmp_path / "linked"
        git(fresh, "worktree", "add", "-q", str(linked), "-b", "feature/x", "main")
        assert start(hook, linked) == ""

    def test_accepts_a_0_22_x_repository_moved_end_to_end_in_shared_mode(
        self, hook, layout
    ):
        """Every file of the work item stands at its thread path as a staged
        rename, `seal/specs/` is gone, the README opens with the marker, one
        line says what moved, and the routing reader finds the declaration at
        its new place."""
        said = message(start(hook, layout))
        assert said.startswith("agentic:moved seal/specs/ into seal/"), said
        assert said.endswith("review the diff and commit"), said
        assert thread_files(layout) == moved_to_threads()
        assert not (layout / "seal" / "specs").exists()
        assert first_line(layout / "seal" / "README.md") == ROOT_MARKER
        listed = tracked(layout, "seal").split()
        assert f"seal/threads/{ITEM}/frame/design.md" in listed
        assert not any(p.startswith("seal/specs/") for p in listed), listed
        assert unstaged(layout) == ""
        routing = load_hook_module("routing.py", "routing_after_the_move")
        found = [p for p, _ in routing.declarations(str(layout))]
        assert found == [str(layout / "seal" / "threads" / ITEM / "routing.md")]

    def test_refuses_a_linked_specs_and_moves_nothing(self, hook, fresh, tmp_path):
        """`seal/specs/` as a symbolic link is one blob to git: the README
        would open with the marker over work items that never moved, so the
        move is refused, every session start, until it goes."""
        write(fresh, "seal/README.md", OLD_HEADING)
        outside = tmp_path / "elsewhere"
        write(outside, f"{ITEM}/routing.md", ROUTING)
        symlink_or_skip(str(outside), str(fresh / "seal" / "specs"))
        commit(fresh, "a linked specs/")
        said = message(start(hook, fresh))
        assert "seal/specs/ is a symbolic link" in said, said
        assert first_line(fresh / "seal" / "README.md") == OLD_HEADING.split("\n")[0]


# --- the 0.22.x layout, moved into threads -----------------------------------

# The heading `templates/seal-README.md` opened with through 0.22.x, which is
# what tells an earlier release's root from a project's own `seal/`.
OLD_HEADING = "# What this plugin maintains in seal/\n\nthe 0.22.x text\n"
# A 0.22.x work item's files, and where each one stands in its thread.
LAYOUT = {
    "routing.md": "routing.md",
    "spec.md": "frame/design.md",
    "plan.md": "frame/plan.md",
    "questions.md": "frame/questions.md",
    "overview.md": "gaps.md",
    "broad-gate.md": "trail/gate.md",
    "guarantee.md": "guarantee.md",
    "changelog.md": "changelog.md",
    "pr.ko.md": "pr.ko.md",
    "rounds/round-1.md": "trail/rounds/round-1.md",
    "phases/phase-1.md": "trail/phases/phase-1.md",
}


def lay_out(base, readme=OLD_HEADING):
    """The 0.22.x layout under BASE/seal/: the README an earlier release
    wrote, a config row, and one work item holding every file `LAYOUT` maps."""
    write(base, "seal/README.md", readme)
    write(base, "seal/config.md", "| Item | Value |\n|---|---|\n")
    for old in LAYOUT:
        write(base, f"seal/specs/{ITEM}/{old}", f"# {old}\n")
    write(
        base,
        f"seal/specs/{ITEM}/routing.md",
        "| Axis | Answer |\n|---|---|\n| Review | through the review chain |\n"
        "| Destination | open the pull request |\n| Branch | feat/x |\n",
    )


def thread_files(base):
    """Every file under BASE/seal/threads/, `/`-joined and relative to it."""
    top = os.path.join(str(base), "seal", "threads")
    return sorted(
        os.path.relpath(os.path.join(here, n), top).replace(os.sep, "/")
        for here, _, names in os.walk(top)
        for n in names
    )


def moved_to_threads():
    return sorted(f"{ITEM}/{new}" for new in LAYOUT.values())


def first_line(path):
    with open(path, encoding="utf-8") as f:
        return f.readline().rstrip("\n")


@pytest.fixture
def layout(fresh):
    """`fresh` with the 0.22.x layout committed in shared mode."""
    lay_out(fresh)
    commit(fresh, "the 0.22.x layout")
    return fresh


class Test_moves:
    def test_accepts_the_readme_then_each_file_of_a_work_item_into_its_thread(
        self, hook, layout
    ):
        units = hook.moves(str(layout))
        assert units[0] == ("readme", "seal/README.md", "seal/README.md")
        assert sorted((src, dst) for _, src, dst in units[1:]) == sorted(
            (f"seal/specs/{ITEM}/{old.split('/')[0]}", f"seal/threads/{ITEM}/{new}")
            for old, new in {
                **{k: v for k, v in LAYOUT.items() if "/" not in k},
                "rounds": "trail/rounds",
                "phases": "trail/phases",
            }.items()
        )

    @pytest.mark.parametrize(
        "readme", ["# seal, the project's own package\n", None], ids=["foreign", "none"]
    )
    def test_refuses_a_seal_whose_readme_no_release_of_the_plugin_wrote(
        self, hook, fresh, readme
    ):
        """A project's own `seal/`, with a README of its own or none, lists
        nothing, whatever it holds under `specs/`."""
        lay_out(fresh)
        if readme is None:
            os.remove(fresh / "seal" / "README.md")
        else:
            write(fresh, "seal/README.md", readme)
        commit(fresh, "a seal/ of the project's own")
        assert hook.moves(str(fresh)) == []

    def test_accepts_a_marked_root_with_no_readme_unit(self, hook, layout):
        """A root already opening with the marker, as a stopped move leaves
        it, lists the work items and no README rewrite."""
        write(layout, "seal/README.md", f"{ROOT_MARKER}\n")
        commit(layout, "the marker, by hand")
        kinds = {kind for kind, _, _ in hook.moves(str(layout))}
        assert kinds == {"other"}


class Test_migrate_local:
    def test_accepts_a_0_22_x_local_root_moved_end_to_end_by_rename(self, hook, fresh):
        """In local mode the root is under the git directory: the same units
        move as plain renames, nothing is staged, and the README there opens
        with the marker."""
        common = fresh / ".git"
        lay_out(common)
        said = message(start(hook, fresh))
        assert said.startswith("agentic:moved seal/specs/ into seal/"), said
        assert thread_files(common) == moved_to_threads()
        assert not (common / "seal" / "specs").exists()
        assert first_line(common / "seal" / "README.md") == ROOT_MARKER
        assert git(fresh, "status", "--porcelain").stdout == ""

    def test_refuses_a_local_seal_whose_readme_no_release_wrote(self, hook, fresh):
        """A `seal/` under the git directory with a README of its own is no
        root this plugin wrote: nothing there moves and nothing is said."""
        common = fresh / ".git"
        lay_out(common, readme="# a directory of the person's own\n")
        assert start(hook, fresh) == ""
        assert (common / "seal" / "specs" / ITEM / "spec.md").is_file()
        assert not (common / "seal" / "threads").exists()


class Test_rename_state:
    def test_accepts_the_old_home_state_merged_into_a_new_one_that_stands(
        self, hook, layout, tmp_path, monkeypatch
    ):
        """A `~/.claude/agentic/` that already stands, as a session start of
        the new release writes one before this hook runs, still receives each
        file of `~/.claude/specseal/` it does not hold; a file it holds keeps
        its own text, and the old one stays where it was, except the
        version cache, which the new directory's own copy replaces."""
        old_home = tmp_path / "home" / "specseal"
        new_home = tmp_path / "home" / "agentic"
        write(old_home, "pact-paths.md", "| a | b |\n")
        write(old_home, "parity-paths.md", "| old | row |\n")
        write(old_home, "version-check", "old\n")
        write(new_home, "parity-paths.md", "| new | row |\n")
        write(new_home, "version-check", "new\n")
        monkeypatch.setattr(hook, "OLD_STATE_DIR", str(old_home))
        monkeypatch.setattr(hook, "STATE_DIR", str(new_home))
        start(hook, layout)
        assert (new_home / "pact-paths.md").read_text(encoding="utf-8") == (
            "| a | b |\n"
        )
        assert (new_home / "parity-paths.md").read_text(encoding="utf-8") == (
            "| new | row |\n"
        )
        assert (old_home / "parity-paths.md").read_text(encoding="utf-8") == (
            "| old | row |\n"
        )
        assert (new_home / "version-check").read_text(encoding="utf-8") == "new\n"
        assert sorted(os.listdir(old_home)) == ["parity-paths.md"]

    def test_accepts_a_clone_whose_tree_another_person_moved(
        self, hook, fresh, tmp_path, monkeypatch
    ):
        """A clone that pulls a tree already moved has nothing to move and
        still holds its own state: its session start renames the state file
        under the git directory, so the scratch opt-out keeps the gates off,
        and merges `~/.claude/specseal/` into `~/.claude/agentic/`. A second
        start changes nothing."""
        write(fresh, "seal/README.md", f"{ROOT_MARKER}\n")
        write(fresh, f"seal/threads/{ITEM}/routing.md", ROUTING)
        commit(fresh, "the tree another person moved")
        old_home = tmp_path / "home" / "specseal"
        new_home = tmp_path / "home" / "agentic"
        write(old_home, "pact-paths.md", "| a | b |\n")
        write(old_home, "version-check", "old\n")
        write(new_home, "version-check", "new\n")
        monkeypatch.setattr(hook, "OLD_STATE_DIR", str(old_home))
        monkeypatch.setattr(hook, "STATE_DIR", str(new_home))
        write(fresh / ".git", "specseal-scratch", "")
        assert start(hook, fresh) == ""
        assert (fresh / ".git" / "agentic-scratch").is_file()
        assert not (fresh / ".git" / "specseal-scratch").exists()
        optin = load_hook_module("optin.py", "optin_after_the_state_rename")
        assert optin.home_at(str(fresh)) == "", "the scratch opt-out was lost"
        assert (new_home / "pact-paths.md").read_text(encoding="utf-8") == (
            "| a | b |\n"
        )
        assert (new_home / "version-check").read_text(encoding="utf-8") == "new\n"
        assert not old_home.exists()
        before = sorted(os.listdir(fresh / ".git")), sorted(os.listdir(new_home))
        assert start(hook, fresh) == ""
        assert (sorted(os.listdir(fresh / ".git")), sorted(os.listdir(new_home))) == (
            before
        )

    def test_refuses_to_make_a_state_file_where_no_old_one_stands(self, hook, fresh):
        """Nothing old, nothing new: the rename invents no file, and leaves
        a new-named file alone."""
        write(fresh / ".git", "agentic-scratch", "")
        before = sorted(os.listdir(fresh / ".git"))
        hook.rename_state(str(fresh))
        assert sorted(os.listdir(fresh / ".git")) == before
        assert not os.path.exists(hook.STATE_DIR)

    def test_accepts_each_old_state_file_renamed_where_no_new_one_stands(
        self, hook, layout, tmp_path, monkeypatch
    ):
        """With the move, a state file an earlier release wrote beside the
        root, and the directory under `~/.claude/`, take the plugin's new
        name; one whose new name is already taken is left as it is."""
        fresh = layout
        old_home = tmp_path / "home" / "specseal"
        new_home = tmp_path / "home" / "agentic"
        write(old_home, "pact-paths.md", "| a | b |\n")
        monkeypatch.setattr(hook, "OLD_STATE_DIR", str(old_home))
        monkeypatch.setattr(hook, "STATE_DIR", str(new_home))
        git_dir = fresh / ".git"
        write(git_dir, "specseal-scratch", "")
        write(git_dir, "specseal-leases/s1", "x\n")
        write(git_dir, "specseal-stamp/a", "old\n")
        write(git_dir, "agentic-stamp/a", "new\n")
        start(hook, fresh)
        assert (git_dir / "agentic-scratch").is_file()
        assert not (git_dir / "specseal-scratch").exists()
        assert (git_dir / "agentic-leases" / "s1").is_file()
        old_stamp = git_dir / "specseal-stamp" / "a"
        assert old_stamp.read_text(encoding="utf-8") == "old\n"
        assert (git_dir / "agentic-stamp" / "a").read_text(encoding="utf-8") == "new\n"
        assert (new_home / "pact-paths.md").is_file()
        assert not old_home.exists()


test_census = census_case(TARGET)
