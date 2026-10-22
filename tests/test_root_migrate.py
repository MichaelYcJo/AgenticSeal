"""`hooks/root-migrate.py`, one class per function.

Rebuilt by #942's phase 5. The hook moves `.specseal/` and `specs/<id>/`
into `seal/` at session start, once per repository, and every one of its
units asks git, so the cases run git. Two repositories are built once for
the module and copied for each case: the old layout, committed (a map and a
map directory under `.specseal/` beside its README and follow-up list, one
work item and one foreign directory under `specs/`), and a fresh repository
holding one commit. Each copy is the reset. The marker the hook stamps is
under each case's own directory.
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
    census_case,
    commit_everything_as_e,
    git,
    load_hook_module,
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
ONE_MARK = "1788000002-one-mark"
# 0.3.x's ledger, which moves as any other entry of the old root does.
MAP = "# map\n\n| Clause | Coordinate |\n|---|---|\n| A | a row |\n"
MOVED_ALL = "moved .specseal/ and 1 work item into seal/"
LEFT_UNMARKED = (
    f"left specs/{TEAM} where it is (no routing.md or rounds/ that git tracks — "
    "not a SpecSeal work item)"
)

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


def staged(repo):
    """The paths staged in REPO, one per line."""
    return git(repo, "diff", "--cached", "--name-only").stdout


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
    """The hook, its marker under the case's own directory."""
    monkeypatch.setattr(MIGRATE, "STATE_DIR", str(tmp_path / "state"))
    monkeypatch.setattr(MIGRATE, "MARKER", str(tmp_path / "state" / "root-migrated"))
    return MIGRATE


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


def stamped(hook, repo):
    try:
        with open(hook.MARKER, encoding="utf-8") as f:
            # exempt from splitlines: a marker file of root paths
            return str(repo) in f.read().splitlines()
    except OSError:
        return False


def plant_team_directory(repo):
    """A team's own specification under a name `date +%s` could have made:
    the shape `ITEM_RE` accepts, and none of the plugin's marks."""
    write(repo, f"specs/{TEAM}/spec.md", "# the team's own specification\n")
    write(repo, f"specs/{TEAM}/plan.md", "# the team's own plan\n")
    commit(repo, "a team directory shaped like a work item")


def move_the_home_by_hand(repo):
    (repo / "seal").mkdir()
    for src, dst in (
        (".specseal/map.md", "seal/map.md"),
        (".specseal/map", "seal/map"),
        (".specseal/README.md", "seal/README.md"),
        (".specseal/follow-up.md", "seal/follow-up.md"),
    ):
        git(repo, "mv", src, dst)
    commit(repo, "the home moved, the item not yet")


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


class Test_attempted:
    def test_accepts_a_root_the_marker_lists(self, hook, tmp_path):
        write(tmp_path, "state/root-migrated", "/x/one\n/x/two\n")
        assert hook.attempted("/x/two")

    def test_refuses_a_root_only_a_longer_one_begins_with_and_no_marker(
        self, hook, tmp_path
    ):
        assert not hook.attempted("/x/one")
        write(tmp_path, "state/root-migrated", "/x/one-more\n")
        assert not hook.attempted("/x/one")


class Test_stamp:
    def test_accepts_a_root_appended_beside_the_ones_stamped_before(
        self, hook, tmp_path
    ):
        hook.stamp("/x/one")
        hook.stamp("/x/two")
        assert (tmp_path / "state" / "root-migrated").read_text(
            encoding="utf-8"
        ) == "/x/one\n/x/two\n"

    def test_refuses_to_raise_where_the_state_directory_cannot_be_made(
        self, hook, tmp_path
    ):
        write(tmp_path, "state", "a file where the directory goes\n")
        hook.stamp("/x/three")
        assert not hook.attempted("/x/three")


class Test_dirty:
    def test_accepts_a_committed_tree_and_a_stopped_runs_staged_renames(
        self, hook, proj
    ):
        assert not hook.dirty(str(proj))
        (proj / "seal").mkdir()
        git(proj, "mv", ".specseal/map.md", "seal/map.md")
        git(proj, "rm", "-q", ".specseal/follow-up.md")
        assert not hook.dirty(str(proj))

    @pytest.mark.parametrize(
        "shape", ["a worktree edit", "a staged edit", "an untracked file"]
    )
    def test_refuses_work_in_progress_under_the_old_roots(self, hook, proj, shape):
        if shape == "an untracked file":
            write(proj, f"specs/{ITEM}/overview.md", "# not yet added\n")
        else:
            ledger = proj / ".specseal" / "map.md"
            ledger.write_text(MAP + "| E | half a row |\n", encoding="utf-8")
            if shape == "a staged edit":
                git(proj, "add", "-A")
        assert hook.dirty(str(proj))

    @pytest.mark.parametrize(
        "word, how", [(LS_FILES, "raise"), ("status", "raise"), ("status", "exit")]
    )
    def test_refuses_a_git_that_cannot_answer(self, hook, proj, monkeypatch, word, how):
        monkeypatch.setattr(hook, "git", failing(hook.git, word, how))
        assert hook.dirty(str(proj))


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


class Test_marked:
    def test_accepts_an_id_shaped_directory_with_either_mark_on_disk(self, hook, proj):
        assert hook.marked(str(proj), ITEM)
        write(proj, f"specs/{ONE_MARK}/rounds/round-1.md", ROUND)
        assert hook.marked(str(proj), ONE_MARK)

    def test_refuses_a_mark_under_another_name_and_an_id_without_one(self, hook, proj):
        write(proj, "specs/handbook/routing.md", "# how requests are routed\n")
        assert not hook.marked(str(proj), "handbook")
        plant_team_directory(proj)
        assert not hook.marked(str(proj), TEAM)


class Test_tracked_marks:
    def test_accepts_an_id_carrying_either_mark_git_tracks(self, hook, proj):
        write(proj, f"specs/{ONE_MARK}/rounds/round-1.md", ROUND)
        commit(proj, "a work item with rounds alone")
        assert hook.tracked_marks(str(proj)) == {ITEM, ONE_MARK}

    @pytest.mark.parametrize(
        "rel",
        [
            f"specs/{TEAM}/docs/routing.md",
            "specs/handbook/routing.md",
            f"specs/{TEAM}/rounds",
        ],
        ids=[
            "routing.md one level down",
            "a name without the shape",
            "a file named rounds",
        ],
    )
    def test_refuses_a_file_that_is_no_mark(self, hook, proj, rel):
        write(proj, rel, "# a team's file\n")
        commit(proj, "a team's file")
        assert hook.tracked_marks(str(proj)) == {ITEM}

    def test_refuses_to_answer_over_a_corrupt_index(self, hook, proj):
        (proj / ".git" / "index").write_bytes(b"DIRC garbage")
        assert hook.tracked_marks(str(proj)) is None


class Test_unmarked:
    def test_accepts_an_id_shaped_directory_git_tracks_no_mark_of(self, hook, proj):
        plant_team_directory(proj)
        assert hook.unmarked(str(proj), TEAM, {ITEM})

    def test_refuses_a_name_without_the_shape_a_marked_one_and_a_file(self, hook, proj):
        write(proj, "specs/1788000001-a-file.md", "x\n")
        for name in ("notes", ITEM, "1788000001-a-file.md"):
            assert not hook.unmarked(str(proj), name, {ITEM}), name


class Test_old_items:
    def test_accepts_the_marked_items_and_everything_else_on_disk(self, hook, proj):
        write(proj, "specs/untracked/x.md", "x\n")
        assert hook.old_items(str(proj)) == ([ITEM], ["notes", "untracked"])

    def test_refuses_to_lose_the_items_where_git_cannot_list_the_marks(
        self, hook, proj, monkeypatch
    ):
        """The marks are read from the disk then, so the run still has units
        and `dirty()` refuses it."""
        monkeypatch.setattr(hook, "git", failing(hook.git, LS_FILES))
        assert hook.old_items(str(proj)) == ([ITEM], ["notes"])


class Test_moves:
    def test_accepts_the_readme_first_then_the_home_then_the_items(self, hook, proj):
        assert hook.moves(str(proj)) == [
            ("readme", ".specseal/README.md", "seal/README.md"),
            ("other", ".specseal/follow-up.md", "seal/follow-up.md"),
            ("other", ".specseal/map", "seal/map"),
            ("other", ".specseal/map.md", "seal/map.md"),
            ("item", f"specs/{ITEM}", f"seal/specs/{ITEM}"),
        ]

    def test_refuses_a_unit_where_nothing_old_is_tracked(self, hook, fresh):
        assert hook.moves(str(fresh)) == []


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
        write(proj, f"seal/specs/{ITEM}/spec.md", "# already here\n")
        hook.move(str(proj), f"specs/{ITEM}", f"seal/specs/{ITEM}")
        assert (proj / "seal" / "specs" / ITEM / "rounds" / "round-1.md").is_file()
        assert not (proj / "seal" / "specs" / ITEM / ITEM).exists()
        # The walk removes each emptied directory below the item; the item's
        # own directory, listed before its `rounds/` went, stays on disk
        # empty, and git sees nothing there.
        assert not (proj / "specs" / ITEM / "rounds").exists(), "an emptied one stayed"
        assert list((proj / "specs" / ITEM).iterdir()) == []

    def test_refuses_a_file_already_at_its_destination_and_moves_the_marks_last(
        self, hook, proj
    ):
        write(proj, "seal/map.md", "# the newer map\n")
        with pytest.raises(hook.MoveError, match=r"seal/map\.md already exists"):
            hook.move(str(proj), ".specseal/map.md", "seal/map.md")
        write(proj, f"specs/{ITEM}/spec.md", "# the old spec\n")
        write(proj, f"seal/specs/{ITEM}/spec.md", "# the newer spec\n")
        commit(proj, "both spec.md")
        with pytest.raises(hook.MoveError, match="already exists"):
            hook.move(str(proj), f"specs/{ITEM}", f"seal/specs/{ITEM}")
        assert (proj / "specs" / ITEM / "routing.md").is_file()
        assert (proj / "specs" / ITEM / "rounds" / "round-1.md").is_file()


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
        commit(proj, "only SpecSeal's work items under specs/")
        assert hook.run_moves(str(proj), hook.moves(str(proj))) == (5, None)
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
        done, error = hook.run_moves(str(proj), hook.moves(str(proj)))
        assert (done, error.error) == (2, "disk full")

    def test_refuses_to_remove_a_linked_specs_under_windows_rmdir(
        self, hook, proj, monkeypatch
    ):
        """PR #700's `windows-latest` leg: Windows' `RemoveDirectoryW`
        removes a directory link itself, whatever is behind it. Contract
        rule 13: the POSIX guarantee is removed here, by giving `rmdir`
        Windows' semantics for a link."""
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
        hook.run_moves(str(proj), hook.moves(str(proj)))
        assert os.path.islink(proj / "specs"), "the cleanup removed the team's link"


class Test_has_root:
    def test_accepts_a_root_in_the_tree_or_under_the_git_directory(
        self, hook, fresh, tmp_path
    ):
        (fresh / "seal").mkdir()
        assert hook.has_root(str(fresh))
        (fresh / "seal").rmdir()
        (fresh / ".git" / "seal").mkdir()
        assert hook.has_root(str(fresh))
        linked = tmp_path / "linked"
        git(fresh, "worktree", "add", "-q", str(linked), "-b", "feature/x")
        assert hook.has_root(str(linked))

    def test_refuses_a_file_named_seal_under_the_git_directory(self, hook, fresh):
        assert not hook.has_root(str(fresh))
        (fresh / ".git" / "seal").write_text("", encoding="utf-8")
        assert not hook.has_root(str(fresh))


class Test_main:
    def test_accepts_the_first_start_as_the_move_said_in_one_line(self, hook, proj):
        """S5: every move staged, nothing left unstaged, and after the commit
        the notice asks for, `--follow` reaches the file's old name."""
        out = message(start(hook, proj))
        assert out == (
            f"specseal: {MOVED_ALL} (left specs/notes where it is (not tracked as "
            "a SpecSeal work item)) — review the diff and commit"
        ), out
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
        assert stamped(hook, proj)
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

    def test_accepts_the_old_layout_that_does_not_opt_in(self, hook, proj):
        """The old layout is exactly what does not opt in any more, so a hook
        gated on `optin.opted_in` would never meet what it moves."""
        assert not hook.optin.opted_in(str(proj)), "the fixture already opted in"
        assert "moved" in message(start(hook, proj))
        assert hook.optin.opted_in(str(proj)), "the move did not produce the opt-in"

    def test_accepts_a_move_by_hand_that_stopped_halfway_and_a_fragment_there(
        self, hook, proj
    ):
        """S7: what remains moves, a directory already at its destination is
        merged file by file, and the marker is stamped only then."""
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
        assert stamped(hook, proj)

    def test_accepts_an_ignored_file_under_the_old_root_left_where_it_is(
        self, hook, proj
    ):
        """Round 1's red 1: the units are what git tracks, so an ignored file
        is left, and `.specseal/` may stay holding nothing else."""
        write(proj, ".gitignore", ".DS_Store\n")
        commit(proj, "ignore the finder's file")
        write(proj, ".specseal/.DS_Store", "\0")
        assert MOVED_ALL in message(start(hook, proj))
        assert stamped(hook, proj)
        assert tracked(proj, ".specseal", f"specs/{ITEM}") == ""
        assert os.listdir(proj / ".specseal") == [".DS_Store"]
        assert start(hook, proj) == "", "nothing tracked is left, so nothing to say"

    def test_accepts_only_work_items_under_specs_and_names_the_rest(self, hook, proj):
        """An item-shaped file, a mark under a name without the shape, and an
        id-shaped directory carrying no mark git tracks all stay, each named
        with its reason, and nothing is staged for them."""
        write(proj, "specs/1788000001-a-file.md", "# a file with an item's name\n")
        write(proj, "specs/handbook/routing.md", "# how requests are routed here\n")
        plant_team_directory(proj)
        write(proj, ".gitignore", "rounds/\n")
        write(proj, f"specs/{TEAM}/docs/routing.md", "# how our requests route\n")
        commit(proj, "a team's files")
        write(proj, f"specs/{TEAM}/rounds/scratch.md", "# local only\n")
        os.makedirs(proj / "specs" / TEAM / "rounds" / "empty")
        out = message(start(hook, proj))
        assert MOVED_ALL in out, out
        assert (
            "left specs/1788000001-a-file.md, specs/handbook, specs/notes where it "
            "is (not tracked as a SpecSeal work item); " + LEFT_UNMARKED
        ) in out, out
        assert (proj / "specs" / "handbook" / "routing.md").is_file()
        assert TEAM not in staged(proj)
        assert stamped(hook, proj)

    @pytest.mark.parametrize(
        "mark, text", [("routing.md", ROUTING), ("rounds/round-1.md", ROUND)]
    )
    def test_accepts_either_mark_alone_and_resumes_its_item_once_settled(
        self, hook, proj, mark, text
    ):
        """B3 and round 2 of #688: either mark is the proof on its own, and
        each moves last, so a stop at a taken `spec.md` strands nothing."""
        write(proj, f"specs/{ONE_MARK}/{mark}", text)
        write(proj, f"specs/{ONE_MARK}/spec.md", "# the old spec\n")
        write(proj, f"seal/specs/{ONE_MARK}/spec.md", "# the newer spec\n")
        commit(proj, "an item with one mark, its spec.md taken")
        out = message(start(hook, proj))
        assert f"stopped at specs/{ONE_MARK}/spec.md" in out, out
        git(proj, "rm", "-q", f"specs/{ONE_MARK}/spec.md")
        out = message(start(hook, proj))
        assert "moved 1 work item into seal/" in out, out
        assert (proj / "seal" / "specs" / ONE_MARK / mark).is_file()
        assert (proj / "seal" / "specs" / ONE_MARK / "spec.md").is_file()
        assert tracked(proj, f"specs/{ONE_MARK}") == ""
        assert not (proj / "specs" / ONE_MARK / "rounds").exists()

    def test_accepts_two_items_named_in_the_plural(self, hook, proj):
        write(proj, f"specs/{ONE_MARK}/routing.md", ROUTING)
        commit(proj, "a second work item")
        assert "moved .specseal/ and 2 work items into seal/" in message(
            start(hook, proj)
        )

    def test_accepts_a_linked_specs_holding_no_marked_directory(self, hook, proj):
        """A linked `specs/` whose entries carry no mark holds no work items,
        so the rest moves and the link is named as left."""
        git(proj, "rm", "-rq", "specs")
        write(proj, f"team/{TEAM}/spec.md", "# the team's own specification\n")
        write(proj, "team/handbook/routing.md", "# how requests are routed\n")
        symlink_or_skip("team", proj / "specs")
        commit(proj, "the team's specs/ is a link")
        out = message(start(hook, proj))
        assert "symbolic link" not in out, out
        assert "moved .specseal/ into seal/" in out, out
        assert LEFT_UNMARKED in out, out
        assert os.path.islink(proj / "specs")

    def test_accepts_a_local_root_beside_an_old_layout_as_moved_into_the_tree(
        self, hook, proj
    ):
        """A repository on the old layout committed `.specseal/`, so it is
        shared by definition, whatever sits under `.git/`."""
        (proj / ".git" / "seal").mkdir()
        assert MOVED_ALL in message(start(hook, proj))
        assert (proj / "seal" / "map.md").is_file()
        assert stamped(hook, proj)

    @pytest.mark.parametrize(
        "shape", ["a worktree edit", "an untracked file", "ls-files raises"]
    )
    def test_refuses_to_move_over_work_in_progress(
        self, hook, proj, monkeypatch, shape
    ):
        """S6: the refusal says why, stamps nothing and touches nothing, and
        the next clean start moves."""
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
            "specseal: .specseal/ and specs/ are the old layout, but they carry "
            "uncommitted changes — not touching work in progress. Commit, then "
            "the next session start moves them into seal/."
        ), out
        assert (proj / ".specseal" / "map.md").is_file()
        assert not (proj / "seal").exists()
        assert not stamped(hook, proj)

    @pytest.mark.parametrize("how", ["corrupt index", "ls-files raises"])
    def test_refuses_to_stamp_where_git_cannot_list_the_marks(
        self, hook, proj, monkeypatch, how
    ):
        """Round 2 of #688: with `.specseal/` moved, the items are the only
        units, and an empty answer would read as nothing old left."""
        move_the_home_by_hand(proj)
        index = proj / ".git" / "index"
        good, real = index.read_bytes(), hook.git
        if how == "corrupt index":
            index.write_bytes(b"DIRC garbage")
        else:
            monkeypatch.setattr(hook, "git", failing(real, LS_FILES))
        assert "uncommitted changes" in message(start(hook, proj))
        assert not stamped(hook, proj)
        index.write_bytes(good)
        monkeypatch.setattr(hook, "git", real)
        assert "moved 1 work item into seal/" in message(start(hook, proj))
        assert stamped(hook, proj)

    def test_refuses_to_stamp_a_stopped_move_and_the_next_start_continues(
        self, hook, proj, monkeypatch
    ):
        real, calls = hook.git_mv, []

        def flaky(root, src, dst):
            calls.append(src)
            if len(calls) == 3:
                raise hook.MoveError(src, "disk full")
            real(root, src, dst)

        monkeypatch.setattr(hook, "git_mv", flaky)
        out = message(start(hook, proj))
        assert out == (
            "specseal: moved 2 of 5 into seal/ and stopped at .specseal/map: disk "
            "full. The next session start continues."
        ), out
        assert not stamped(hook, proj)
        monkeypatch.setattr(hook, "git_mv", real)
        assert MOVED_ALL in message(start(hook, proj))
        assert stamped(hook, proj)

    @pytest.mark.parametrize("shape", ["a file named seal", "a file at seal/map.md"])
    def test_refuses_a_stop_a_person_has_to_settle(self, hook, proj, shape):
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
        assert not stamped(hook, proj)

    def test_refuses_a_repository_declaring_itself_throwaway(self, hook, proj):
        write(proj, ".specseal/scratch", "")
        commit(proj, "throwaway")
        assert message(start(hook, proj)) == (
            "specseal: .specseal/scratch says this repository is throwaway — not "
            "migrating it. Delete the file if it is not."
        )
        assert not (proj / "seal").exists()
        assert not stamped(hook, proj)

    @pytest.mark.parametrize("which", [".specseal", "specs"])
    def test_refuses_a_linked_old_root_every_start(self, hook, proj, which):
        """Git tracks a link as one blob, so the files behind it list no
        units: a half-move reported as success. Refused every start, nothing
        moved and nothing stamped."""
        git(proj, "mv", which, "vault")
        symlink_or_skip("vault", proj / which)
        commit(proj, "an old root is a link")
        said = (
            ".specseal/ is a symbolic link, which"
            if which == ".specseal"
            else "specs/ is a symbolic link holding work items, which"
        )
        for _ in range(2):
            out = message(start(hook, proj))
            assert f"specseal: {said} git tracks as the" in out, out
            assert out.endswith(
                'Move by hand (README, "Coming up from 0.3.x") and remove the link.'
            ), out
            assert not (proj / "seal").exists()
            assert not stamped(hook, proj)

    def test_refuses_to_speak_where_nothing_is_old_or_the_marker_answered(
        self, hook, proj, fresh
    ):
        """Silent with nothing old and no root, and silent where the marker
        already carries the root (Q8 (a)): the gates are the backstop."""
        assert start(hook, fresh) == ""
        assert not stamped(hook, fresh)
        hook.stamp(str(proj))
        assert start(hook, proj) == ""
        assert (proj / ".specseal").is_dir()

    @pytest.mark.parametrize(
        "payload", ["[]", '{"cwd": ""}', "{"], ids=["a list", "no cwd", "not json"]
    )
    def test_refuses_a_payload_that_names_no_directory(self, hook, payload):
        assert start(hook, None, payload) == ""

    def test_accepts_a_moved_repository_as_stamped_so_an_old_branch_stays(
        self, hook, proj
    ):
        """A branch cut before the move still carries the old layout, and
        checking it out later stages nothing."""
        start(hook, proj)
        commit_staged(proj)
        git(proj, "switch", "-qc", "old", "HEAD~1")
        assert (proj / ".specseal").is_dir()
        assert start(hook, proj) == ""
        assert (proj / ".specseal").is_dir()

    def test_accepts_a_local_root_as_stamped_and_leaves_an_old_branch_alone(
        self, hook, fresh, tmp_path
    ):
        """S9 of #80: with only `.git/seal/` the hook says nothing and stamps,
        and a branch still carrying the old layout checked out later is not
        moved INTO the tree the person chose to keep clean. A linked worktree
        reads the main tree's root and is stamped under its own path."""
        git(fresh, "checkout", "-q", "-b", "old-layout")
        write(fresh, ".specseal/README.md", OLD_README)
        write(fresh, f"specs/{ITEM}/routing.md", ROUTING)
        commit(fresh, "the 0.3.x layout")
        git(fresh, "checkout", "-q", "main")
        (fresh / ".git" / "seal").mkdir()
        assert start(hook, fresh) == ""
        assert stamped(hook, fresh)
        git(fresh, "checkout", "-q", "old-layout")
        assert start(hook, fresh) == ""
        assert not (fresh / "seal").exists(), "the old layout was moved into the tree"
        assert git(fresh, "status", "--porcelain").stdout == ""
        linked = tmp_path / "linked"
        git(fresh, "worktree", "add", "-q", str(linked), "-b", "feature/x", "main")
        assert start(hook, linked) == ""
        assert stamped(hook, linked)


test_census = census_case(TARGET)
