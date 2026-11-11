"""`skills/verify/scripts/unverified_check.py`, one class per function.

Rebuilt by #942's phase 5 from `tests/behaviour/test_unverified_rows_close.py`. The
script reads every `## Not verified` section, reports what is still open,
and fails on a section it cannot read. Its readers of markdown, of a section
and of a row are `lib/lines.py`'s, `lib/items.py`'s and `lib/gaps.py`'s, and
their cases stand in `tests/lib/`; the predicates `chain_check.py` and
`settle.py` read stand in their files' cases. Those cases build the worlds
below by importing them from here.

The walk, the root states and `main` read repositories built once for the
module: a clone of two work items and a
tracked overview under `build/`, a clone whose second overview is a tracked
link to the first, built once with the link sorting after its target and
once before it, a clone with a moved base branch beside its work
branch, a clone of work items a settle can remove, a clone with a `seal/`
root beside a team's own `specs/`, a `seal/` root with no `specs/`, and a
`seal/` root whose one work item holds no overview. A case that writes into
a world takes a copy,
and the copy is the reset. No world holds a file a case runs, so the copies
are plain copies.

The cases that run `main` beside a project's own `seal/` package
(#1059) build `tests/conftest.py`'s `package` or `shared` repository for
each case, whose root stands at `agentic-seal/`.
"""

import os
import shutil
import subprocess

import pytest
from conftest import (
    ITEM,
    ROOT,
    census_case,
    commit_everything_as_e,
    config_json,
    git,
    load_module,
    mark_root,
    symlink_or_skip,
    write,
)

TARGET = "skills/verify/scripts/unverified_check.py"

UC = load_module(os.path.join(ROOT, *TARGET.split("/")), "unverified_check_under_test")

WORK = "1780000000-work"
OTHER = "1780000001-other"
TUI = "| how the gate renders in a TUI | user, on the next session |"
WINDOWS = "| whether Windows hooks fire | a maintainer with a Windows machine |"
CANONICAL = f"""## Not verified

| Item | Who must answer |
|---|---|
{TUI}
{WINDOWS}
"""
CLOSED_SECTION = """## Not verified

| Item | Who must answer |
|---|---|
| closed how the gate renders in a TUI | seen on screen, 2026-01-01 |
"""


def memo(section, name=WORK):
    """An overview's text holding SECTION, under a heading and a section
    before it."""
    return f"# {name} overview\n\n## Not done\n\nsomething.\n\n{section}"


def memo_at(root, section, name=WORK):
    """The path of `specs/<name>/gaps.md` under ROOT, written as
    `memo(section)`."""
    write(root, f"specs/{name}/gaps.md", memo(section, name))
    return os.path.join(str(root), "specs", name, "gaps.md")


def same_path(a, b):
    """Whether A and B name one place, as git and the disk each spell it."""
    return os.path.normcase(os.path.realpath(a)) == os.path.normcase(
        os.path.realpath(b)
    )


def copy_of(world, tmp_path):
    """A copy of WORLD under TMP_PATH, links kept as links."""
    dst = tmp_path / world.name
    shutil.copytree(world, dst, symlinks=True)
    return dst


def _committed(base, files):
    """A repository at BASE/repo holding FILES, `{rel: text}`, in one
    commit; a `seal/` among them is made a root."""
    d = base / "repo"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    for rel, text in files.items():
        write(d, rel, text)
    if (d / "seal").is_dir():
        mark_root(d / "seal")
    commit_everything_as_e(d, "the base")
    return d


@pytest.fixture(scope="module")
def plain(tmp_path_factory):
    """Two work items in the 0.3.x spelling, `specs/<id>/`, and an overview
    tracked under `build/`, which every walk skips."""
    return _committed(
        tmp_path_factory.mktemp("plain"),
        {
            f"specs/{WORK}/gaps.md": memo(CANONICAL),
            f"specs/{OTHER}/gaps.md": memo(CANONICAL, OTHER),
            "build/x/gaps.md": memo(CANONICAL, "x"),
        },
    )


@pytest.fixture(
    scope="module",
    params=[OTHER, "1779999999-link"],
    ids=["the link sorts after its target", "the link sorts before its target"],
)
def linked(tmp_path_factory, request):
    """One work item and a second whose overview is a tracked link to the
    first's, the second's directory sorting after the first's or before it.
    #19 stood only where the link sorted first."""
    d = _committed(
        tmp_path_factory.mktemp("linked"),
        {f"specs/{WORK}/gaps.md": memo(CANONICAL)},
    )
    (d / "specs" / request.param).mkdir()
    symlink_or_skip(
        os.path.join("..", WORK, "gaps.md"),
        str(d / "specs" / request.param / "gaps.md"),
    )
    commit_everything_as_e(d, "a link")
    return d


SIBLING = "1780000001-squashed-sibling"


@pytest.fixture(scope="module")
def forked(tmp_path_factory):
    """A work branch at the fork point, checked out, beside three refs:
    `fork` at the fork point itself; `base`, which moved past it when a
    sibling work item was squashed into it; and `unrelated`, a history of
    its own."""
    d = _committed(
        tmp_path_factory.mktemp("forked"),
        {f"specs/{WORK}/gaps.md": memo(CANONICAL)},
    )
    git(d, "branch", "fork")
    git(d, "switch", "-qc", "base")
    write(d, f"specs/{SIBLING}/gaps.md", memo(CANONICAL, SIBLING))
    commit_everything_as_e(d, "another work item, squashed into the base")
    git(d, "switch", "-q", "--orphan", "unrelated")
    write(d, "readme.md", "no commit in common\n")
    commit_everything_as_e(d, "an unrelated root")
    git(d, "switch", "-qc", "work", "fork")
    return d


DOC = "# a\n\n## S\n\nAn old rule.\n"


def rule(text):
    return f"- add\n  file: docs/a.md\n  section: S\n  to: {text}\n"


SETTLE_A = "1780000001-a"
SETTLE_B = "1780000002-b"
SETTLE_C = "1780000003-c"
SETTLE_BAD = "1780000004-bad"
CLOSED_ITEM = "1780000009-closed"
OPEN_ITEM = "1780000010-open"
DROPPED = "1780000011-dropped"


@pytest.fixture(scope="module")
def settle(tmp_path_factory):
    """`docs/a.md` and work items a settle may remove: two whose rule
    changes add a sentence each, one whose spec has no `## Rule changes`,
    one whose section will not parse, and three with no spec, closed, open,
    and one whose spec an earlier commit dropped."""
    files = {"docs/a.md": DOC}
    specs = {
        SETTLE_A: f"# a\n\n## Rule changes\n\n{rule('A new rule.')}",
        SETTLE_B: f"# b\n\n## Rule changes\n\n{rule('Another rule.')}",
        SETTLE_C: "# c\n",
        SETTLE_BAD: "# bad\n\n## Rule changes\n\nnot an item\n",
    }
    for name, spec in specs.items():
        files[f"specs/{name}/gaps.md"] = memo(CLOSED_SECTION, name)
        files[f"specs/{name}/design.md"] = spec
    for name, section in (
        (CLOSED_ITEM, CLOSED_SECTION),
        (OPEN_ITEM, CANONICAL),
        (DROPPED, CLOSED_SECTION),
    ):
        files[f"specs/{name}/routing.md"] = f"# {name} routing\n"
        files[f"specs/{name}/gaps.md"] = memo(section, name)
    files[f"specs/{DROPPED}/design.md"] = "# a spec\n\nA rule.\n"
    d = _committed(tmp_path_factory.mktemp("settle"), files)
    git(d, "rm", "-q", f"specs/{DROPPED}/design.md")
    commit_everything_as_e(d, "an earlier pull request drops it")
    return d


TEAM = "specs/1788000001-team-thing"
OURS = "seal/threads/1790000000-ours"
MALFORMED = "## Not verified\n\nnot a table, and not a none line either\n"


@pytest.fixture(scope="module")
def joined(tmp_path_factory):
    """A `seal/` root holding one readable work item, and a team's own
    `specs/` whose overview the reader cannot read."""
    return _committed(
        tmp_path_factory.mktemp("joined"),
        {
            f"{OURS}/gaps.md": memo(CANONICAL, "ours"),
            f"{TEAM}/gaps.md": memo(MALFORMED, "team"),
            # exempt from old_names: another tool's own file, under a name the plugin once used
            f"{TEAM}/spec.md": "# the team's spec\n",
        },
    )


@pytest.fixture(scope="module")
def sealed(tmp_path_factory):
    """A `seal/` root with no `specs/`, the tree a complete settle leaves."""
    return _committed(tmp_path_factory.mktemp("sealed"), {"seal/ledger.md": "# l\n"})


@pytest.fixture(scope="module")
def unwritten(tmp_path_factory):
    """A `seal/` root whose one work item has a routing and a spec and never
    opened a closing memo."""
    return _committed(
        tmp_path_factory.mktemp("unwritten"),
        {
            f"seal/threads/{WORK}/routing.md": f"# {WORK} routing\n",
            f"seal/threads/{WORK}/frame/design.md": "# a spec\n",
        },
    )


def run(argv):
    """`main`'s exit code, so a case asserts what CI would see."""
    return UC.main(argv)


# --- the walk and the paths it reads ------------------------------------------


class Test_overviews:
    def test_accepts_every_overview_under_a_path_once_skipping_build_output(
        self, tmp_path
    ):
        for rel in ("specs/b", "specs/a", "build/c", "node_modules/d", ".venv/e"):
            write(tmp_path, f"{rel}/gaps.md", memo(CANONICAL))
        named = str(tmp_path / "specs" / "a" / "gaps.md")
        found = UC.overviews([str(tmp_path), named])
        here = os.path.realpath(str(tmp_path))
        assert found == [
            os.path.join(here, "specs", "a", "gaps.md"),
            os.path.join(here, "specs", "b", "gaps.md"),
        ]

    def test_refuses_a_reference_root_on_a_walk_and_reads_it_named(self, joined):
        """D2 of #688: a team's own `specs/` is read as history, never as
        this plugin's record, unless the person names it."""
        walked = UC.overviews([str(joined)])
        assert [os.path.basename(os.path.dirname(p)) for p in walked] == [
            "1790000000-ours"
        ]
        named = UC.overviews([str(joined / "specs")])
        assert [os.path.basename(os.path.dirname(p)) for p in named] == [
            "1788000001-team-thing"
        ]

    def test_refuses_a_reference_root_on_a_walk_reached_through_a_link(
        self, joined, tmp_path
    ):
        """`reference_rule` measures the walk against the top git names with
        its links resolved, so an argument reached through a link is read at
        its real path, and a team's `specs/` that a `Reference specs` key
        names by its prefix stays out of that walk too. The default value
        matches a `specs` part wherever it stands, so only a prefix reads
        where the path begins."""
        d = copy_of(joined, tmp_path)
        write(
            d,
            "seal/config.json",
            config_json(("Reference specs", "specs")),
        )
        symlink_or_skip(str(d), str(tmp_path / "link"), directory=True)
        walked = UC.overviews([str(tmp_path / "link")])
        assert [os.path.basename(os.path.dirname(p)) for p in walked] == [
            "1790000000-ours"
        ]


class Test_config_at:
    def test_accepts_the_config_reader_and_the_root(self, joined):
        config, home, name = UC.config_at(str(joined))
        assert callable(config.reference_roots)
        assert same_path(home, joined / "seal")
        assert name == "seal"

    def test_refuses_to_invent_a_root(self, plain):
        _config, home, name = UC.config_at(str(plain))
        assert not home and not name


class Test_references_at:
    def test_accepts_the_default_under_a_root_and_none_without_one(self, joined, plain):
        assert UC.references_at(str(joined))[1] is None
        assert UC.references_at(str(plain))[1] == ()

    def test_refuses_to_fail_where_lib_will_not_load(self, joined, monkeypatch):
        real = UC.sibling.load

        def load(rel):
            if rel == "lib/config.py":
                raise ImportError("planted")
            return real(rel)

        monkeypatch.setattr(UC.sibling, "load", load)
        assert UC.references_at(str(joined)) is None


class Test_reference_rule:
    def test_accepts_a_predicate_true_for_a_reference_root(self, joined):
        skip = UC.reference_rule(str(joined))
        assert skip(str(joined / "specs")) is True
        assert skip(str(joined / "seal" / "threads")) is False

    @pytest.mark.parametrize("where", ["inside", "outside"])
    def test_refuses_to_prune_a_named_root_or_outside_a_repository(
        self, joined, tmp_path, where
    ):
        start = joined / "specs" if where == "inside" else tmp_path
        assert UC.reference_rule(str(start)) is None


def refuses(path, start=None):
    raise ValueError("path is on mount 'D:', start on mount 'C:'")


class Test_repo_relative:
    def test_accepts_a_path_inside_the_root(self, tmp_path):
        inside = os.path.join(str(tmp_path), "specs", "a", "gaps.md")
        assert UC.repo_relative(inside, str(tmp_path)) == "specs/a/gaps.md"

    def test_refuses_a_path_with_no_relative_form(self, monkeypatch):
        monkeypatch.setattr(os.path, "relpath", refuses)
        assert UC.repo_relative(os.path.abspath("x"), os.path.abspath("y")) is None


class Test_display_path:
    def test_accepts_a_path_relative_to_where_the_run_started(self, tmp_path):
        inside = os.path.join(str(tmp_path), "specs", "gaps.md")
        assert UC.display_path(inside, str(tmp_path)) == os.path.join(
            "specs", "gaps.md"
        )

    def test_refuses_to_die_on_a_path_with_no_relative_form(self, monkeypatch):
        """`relpath` raises on Windows across drives, and this is the footing
        for every line the tool prints; driven by making it raise, so every
        leg runs it."""
        monkeypatch.setattr(os.path, "relpath", refuses)
        where = os.path.join("x", "gaps.md")
        assert UC.display_path(where, os.path.abspath("y")) == os.path.abspath(where)


class Test_unique_by_target:
    def test_accepts_every_path_to_a_file_of_its_own(self, tmp_path):
        paths = [str(tmp_path / "a"), str(tmp_path / "b")]
        assert UC.unique_by_target(paths) == paths

    def test_refuses_a_second_path_to_one_file(self, tmp_path):
        p = str(tmp_path / "a")
        assert UC.unique_by_target([p, os.path.join(str(tmp_path), ".", "a")]) == [p]

    @pytest.mark.parametrize(
        "paths",
        [["a", "b"], ["a"]],
        ids=["the link sorting first", "the link alone"],
    )
    def test_accepts_the_real_files_own_path_wherever_the_link_sorts(
        self, tmp_path, paths
    ):
        """#19: the path kept is the real file's own wherever the link sorts,
        so the report names the file the rows stand in."""
        (tmp_path / "b").write_text("x", encoding="utf-8")
        symlink_or_skip("b", str(tmp_path / "a"))
        given = [str(tmp_path / p) for p in paths]
        assert UC.unique_by_target(given) == [os.path.realpath(tmp_path / "b")]


# --- what git answers ---------------------------------------------------------


class Test_repo_root:
    def test_accepts_a_directory_and_a_file_inside_the_repository(self, plain):
        assert same_path(UC.repo_root(str(plain / "specs")), plain)
        assert same_path(UC.repo_root(str(plain / "specs" / WORK / "gaps.md")), plain)

    def test_refuses_a_directory_outside_every_repository(self, tmp_path):
        assert UC.repo_root(str(tmp_path)) is None


# --- what a settle removed ----------------------------------------------------


class Test_settled_root:
    @pytest.mark.parametrize("state", ["absent", "empty", "a file only"])
    def test_accepts_a_roots_own_specs_with_no_work_item(self, tmp_path, state):
        (tmp_path / "seal").mkdir()
        if state != "absent":
            (tmp_path / "seal" / "threads").mkdir()
        if state == "a file only":
            write(tmp_path, "seal/threads/README.md", "r\n")
        assert UC.settled_root(str(tmp_path / "seal" / "threads")) is True

    @pytest.mark.parametrize("state", ["a work item", "another parent", "no root"])
    def test_refuses_a_work_item_another_parent_and_no_root(self, tmp_path, state):
        if state == "a work item":
            (tmp_path / "seal" / "threads" / WORK).mkdir(parents=True)
        if state == "another parent":
            (tmp_path / "other").mkdir()
        path = tmp_path / ("other" if state == "another parent" else "seal") / "threads"
        assert UC.settled_root(str(path)) is False


class Test_absent_root:
    def test_accepts_the_specs_path_of_a_top_level_holding_no_root(self, tmp_path):
        git(tmp_path, "init", "-q")
        assert UC.absent_root(str(tmp_path / "seal" / "threads")) is True

    @pytest.mark.parametrize(
        "state",
        ["a root", "a subdirectory", "no repository", "another parent", "a typo"],
    )
    def test_refuses_a_root_a_subdirectory_no_repository_and_another_name(
        self, sealed, tmp_path, state
    ):
        """Absence is read only at a working tree's top level and under the
        one spelling: anything else is a mistyped path, as it always was."""
        if state == "a typo":
            git(tmp_path, "init", "-q")
        path = {
            "a root": sealed / "seal" / "threads",
            "a subdirectory": sealed / "seal" / "seal" / "threads",
            "no repository": tmp_path / "seal" / "threads",
            "another parent": sealed / "other" / "threads",
            "a typo": tmp_path / "seal" / "spces",
        }[state]
        assert UC.absent_root(str(path)) is False


class Test_unwritten_root:
    def test_accepts_a_roots_specs_holding_work_items_and_no_overview(self, unwritten):
        assert UC.unwritten_root(str(unwritten / "seal" / "threads")) is True

    @pytest.mark.parametrize("state", ["an overview", "no work item", "another parent"])
    def test_refuses_an_overview_no_work_item_and_another_parent(self, tmp_path, state):
        (tmp_path / "seal" / "threads").mkdir(parents=True)
        path = tmp_path / ("other" if state == "another parent" else "seal") / "threads"
        if state == "another parent":
            write(tmp_path, f"other/threads/{WORK}/frame/design.md", "# a spec\n")
        if state == "an overview":
            write(tmp_path, f"seal/threads/{WORK}/gaps.md", memo(CANONICAL))
        assert UC.unwritten_root(str(path)) is False


# --- the command ---------------------------------------------------------------


class Test_main:
    # The plain run: what is open is reported, and a record that cannot be
    # read fails.

    def test_accepts_open_items_without_failing_the_run(self, tmp_path, capsys):
        """Never a red build for an honest row: punishing them teaches
        sessions to write none."""
        memo_at(tmp_path, CANONICAL)
        assert run([str(tmp_path)]) == 0
        out = capsys.readouterr().out
        assert "2 open" in out and "open: 0" not in out

    def test_accepts_every_item_closed_as_open_0(self, tmp_path, capsys):
        memo_at(tmp_path, "## Not verified\n\n- nothing\n  why: all executed.\n")
        assert run([str(tmp_path)]) == 0
        assert "open: 0" in capsys.readouterr().out

    def test_refuses_a_record_it_cannot_read_by_another_exit_and_other_words(
        self, tmp_path, capsys
    ):
        """A reader must never confuse "everything is closed" with "this
        could not be read", and a section that could not be read lists none
        of the rows it did read as open."""
        memo_at(tmp_path, CANONICAL + "| an item | an answerer | a third cell |\n")
        assert run([str(tmp_path)]) == 1
        out = capsys.readouterr().out
        # The refusal the check prints for a record it cannot read, which a
        # reader must not take for zero open items.
        assert "could not be read" in out and "open: 0" not in out
        assert "This is not a report of zero open items." in out
        assert "open  how the gate renders in a TUI" not in out, out

    @pytest.mark.parametrize("state", ["empty", "missing", "and a root"])
    def test_refuses_a_path_that_holds_no_overview(self, tmp_path, capsys, state):
        """Zero files and zero open items are different answers, and a path
        beside the root's settled `specs/` is still read."""
        (tmp_path / "empty").mkdir()
        argv = [str(tmp_path / "empty")]
        if state == "missing":
            argv = [str(tmp_path / "spces")]
        if state == "and a root":
            (tmp_path / "seal").mkdir()
            argv.append(str(tmp_path / "seal" / "threads"))
        assert run(argv) == 2
        err = capsys.readouterr().err
        assert ("no such path" if state == "missing" else "nothing was checked") in err

    def test_accepts_a_walk_outside_a_repository_reading_no_reference_root(
        self, tmp_path, monkeypatch
    ):
        """Outside a git repository there is no root to be outside of, and
        every fixture of the 0.3.x spelling lives there."""

        def refuse(top):
            raise AssertionError(f"reference roots were read for {top!r}")

        monkeypatch.setattr(UC, "references_at", refuse)
        memo_at(tmp_path, CANONICAL)
        assert run([str(tmp_path)]) == 0

    def test_refuses_the_baseline_option_it_no_longer_has(self, plain, capsys):
        """A1 of #1240: the mode that compared the record with a base left,
        so `--baseline` is an argument argparse does not know, exit 2, and
        the help a person reads names no such option (contract rule 14)."""
        with pytest.raises(SystemExit) as refused:
            UC.main(["--baseline", "HEAD", str(plain)])
        assert refused.value.code == 2
        assert "unrecognized arguments: --baseline" in capsys.readouterr().err
        with pytest.raises(SystemExit):
            UC.main(["--help"])
        assert "--baseline" not in capsys.readouterr().out

    def test_accepts_a_tracked_link_counted_once(self, linked, capsys):
        """One record, two paths: counting both doubles its open items
        (#19)."""
        assert run([str(linked)]) == 0
        out = capsys.readouterr().out
        tally = [ln for ln in out.split("\n") if ln.startswith("1 closing memos")]
        assert len(tally) == 1 and " 2 open " in tally[0], out

    @pytest.mark.rule("an-empty-root-is-settled")
    @pytest.mark.parametrize("keep_empty_dir", [True, False], ids=["empty", "absent"])
    def test_the_roots_own_specs_path_is_settled_when_nothing_is_under_it(
        self, sealed, tmp_path, capsys, keep_empty_dir
    ):
        """G7: after a complete settle the root's own `seal/threads/` holds
        nothing, or is gone because git keeps no empty directory, and a run
        handed that path reads it as settled, not as a typo. The line says
        there is nothing to read and claims nothing about what left."""
        d = sealed
        if keep_empty_dir:
            d = copy_of(sealed, tmp_path)
            (d / "seal" / "threads").mkdir()
        assert run([str(d / "seal" / "threads")]) == 0
        out = capsys.readouterr()
        said = " ".join((out.out + out.err).split())
        assert (
            "holds no work item and its `seal/` root is there — the state a "
            "complete settle ends in, so there is nothing to read"
        ) in said, said
        assert "left the record" not in said, said

    def test_refuses_any_other_missing_path_as_a_typo(self, sealed, capsys):
        assert run([str(sealed / "seal" / "spces")]) == 2
        assert "no such path" in capsys.readouterr().err

    # A pull request that declares nothing owes nothing (#952).

    @pytest.mark.rule("nothing-declared-nothing-owed")
    def test_accepts_no_root_in_the_tree(self, joined, tmp_path, capsys):
        """S6: the pull request that moves a root to local mode with the
        workflow kept takes every overview out of the tree. With no root
        there nothing is declared, and the line says there is no record to
        read."""
        d = copy_of(joined, tmp_path)
        shutil.rmtree(d / "seal")
        assert run([str(d / "seal" / "threads")]) == 0
        out = capsys.readouterr()
        said = " ".join((out.out + out.err).split())
        assert (
            "has no `seal/` root in this tree, so nothing here is declared: "
            "there is no record to read. A root in local mode"
        ) in said, said
        assert "open: 0" not in said, said

    @pytest.mark.rule("nothing-declared-nothing-owed")
    def test_accepts_work_items_none_of_which_opened_a_closing_memo(
        self, unwritten, capsys
    ):
        """S6: every work item that never opened an `gaps.md` holds no
        row to read, and that was exit 2, `nothing was checked`."""
        assert run([str(unwritten / "seal" / "threads")]) == 0
        out = capsys.readouterr()
        said = " ".join((out.out + out.err).split())
        assert "none of them carries an `gaps.md`" in said, said
        assert "open: 0" not in said, said

    @pytest.mark.rule("nothing-declared-nothing-owed")
    def test_refuses_a_missing_root_below_the_top_level_as_a_typo(self, sealed, capsys):
        """Absence is read at the working tree's top level only, so a
        `seal/threads` typed from the wrong directory still names nothing."""
        assert run([str(sealed / "seal" / "seal" / "threads")]) == 2
        assert "no such path" in capsys.readouterr().err

    # A team's own `specs/` is read as history and never checked (#688).

    def test_accepts_a_walk_from_the_root_leaving_a_team_specs_out(
        self, joined, capsys
    ):
        """D2: the team's unreadable overview fails nothing."""
        assert run([str(joined)]) == 0
        out = capsys.readouterr().out
        assert "1790000000-ours" in out and "team-thing" not in out, out

    def test_refuses_a_team_overview_the_person_names(self, joined):
        """A person who names the file, or the directory it sits in, has
        asked for it."""
        assert run([str(joined / TEAM / "gaps.md")]) == 1
        assert run([str(joined / "specs")]) == 1

    def test_refuses_nothing_less_where_lib_will_not_load(self, joined, monkeypatch):
        """Where `lib/config.py` raises while it loads, the walk reads every
        overview, as it did before reference roots existed."""
        real = UC.sibling.load

        def load(rel):
            if rel == "lib/config.py":
                raise ImportError("planted")
            return real(rel)

        monkeypatch.setattr(UC.sibling, "load", load)
        assert run([str(joined)]) == 1

    @pytest.mark.parametrize("state", ["unwritten", "settled", "absent"])
    def test_s5_unverified_reads_agentic_seal_threads_as_the_roots_own(
        self, shared, capsys, monkeypatch, state
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
        code = UC.main(["agentic-seal/threads"])
        out = capsys.readouterr().out
        assert code == 0, out
        assert out.startswith(f"seal unverified: agentic-seal/threads {said_of_it}"), (
            out
        )

    def test_s5_unverified_walks_agentic_seal_and_passes_over_the_packages_specs(
        self, shared, capsys, monkeypatch
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
        code = UC.main(["."])
        out = capsys.readouterr().out
        assert code == 0, out
        assert "\n1 closing memos · 0 open · 0 closed · 0 unreadable\n" in out, out


class Test_module:
    def test_the_command_is_present_and_runs_the_script(self):
        """`bin/` lands on the Bash tool's PATH while the plugin is enabled,
        so `bin/seal` resolves its script relative to itself, a .cmd sibling
        ships for the platform that cannot run a POSIX shebang, and
        `seal unverified` hands its arguments to this script."""
        posix = os.path.join(ROOT, "bin", "seal")
        windows = os.path.join(ROOT, "bin", "seal.cmd")
        assert os.path.isfile(posix), "bin/seal missing"
        assert os.path.isfile(windows), "bin/seal.cmd missing"
        assert os.access(posix, os.X_OK), "bin/seal not executable"
        command = (
            [os.environ.get("COMSPEC", "cmd.exe"), "/c", windows]
            if os.name == "nt"
            else [posix]
        )
        done = subprocess.run(
            [*command, "unverified", "--help"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
        assert done.returncode == 0, done.stderr
        assert done.stdout.startswith("usage: seal unverified"), done.stdout


test_census = census_case(TARGET)
