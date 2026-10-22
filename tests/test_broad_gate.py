"""`skills/verify/scripts/broad_gate.py`, one class per function.

Rebuilt from the code by #942's phase 5. The pure units are driven with text,
hand-built records and an `is_directory` answer, so no git and no shell runs
under them. Git runs where the unit asks git a question: the base's
resolution over one repository built once for the module, and the base
comparison and the gate's own run over a fixture repository built once and
copied for each case. Those cases run the fixture's one-test suite through
the gate's recorder, one row per kind of answer, and each copy is the reset.
"""

import argparse
import ast
import json
import os
import pathlib
import shutil
import subprocess
import sys

import pytest
from conftest import census_case, git, git_out, load_module, symlink_or_skip, write
from conftest import commit_everything_as_e as commit

TARGET = "skills/verify/scripts/broad_gate.py"

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAIN = ROOT / "skills" / "code-review" / "scripts" / "chain_check.py"
READER = ROOT / "skills" / "verify" / "scripts" / "unverified_check.py"
ITEM = "seal/specs/1799000001-a-gated-work-item"
ROW = "Broad gate"

gate = load_module(ROOT / TARGET, "broad_gate_under_test")
chain = load_module(CHAIN, "chain_check_beside_broad_gate")
stamp = gate.stamp_module()

PASSING_TEST = "def test_one():\n    assert True\n"
FAILING_TEST = "def test_two():\n    assert False, 'planted'\n"
SUITE_ROW = f"{sys.executable} -m pytest -q -p no:cacheprovider tests"
OVERVIEW = (
    "# overview\n\n## Not verified\n\n- nothing\n  why: the fixture verifies nothing\n"
)
# The variables a runner sets that would make the chain check judge the
# fixture as the runner's own pull request, and the live session's id.
AMBIENT = ("GITHUB_EVENT_PATH", "GITHUB_HEAD_REF", "CLAUDE_CODE_SESSION_ID")


def config_of(row=SUITE_ROW, before="", after=""):
    """A `seal/config.md` with the `Broad gate` row ROW, or none where ROW is
    None, with BEFORE and AFTER around its table."""
    text = before + "| Item | Value |\n|---|---|\n| Mode | shared |\n"
    if row is not None:
        text += f"| {ROW} | {row} |\n"
    return text + after


def home_with(tmp_path, text):
    """A `seal/` directory holding TEXT as its `config.md`; its path."""
    write(tmp_path, "seal/config.md", text)
    return str(tmp_path / "seal")


def a_record(**fields):
    """A `RunRecord` with FIELDS set and every other field empty."""
    record = gate.RunRecord()
    for name, value in fields.items():
        setattr(record, name, value)
    return record


def jsonl(directory, name, *lines, mtime=None):
    """One record file of NAME under DIRECTORY, a JSON object or raw text per
    line; MTIME, where given, is its modification time in nanoseconds."""
    path = pathlib.Path(directory) / name
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(
        (line if isinstance(line, str) else json.dumps(line)) + "\n" for line in lines
    )
    path.write_text(text, encoding="utf-8")
    if mtime is not None:
        os.utime(path, ns=(mtime, mtime))
    return path


def session(key):
    return {"kind": "session", "key": key}


def a_test(path, outcome="passed", category="passed", when="call"):
    return {
        "kind": "test",
        "nodeid": f"{path}::t",
        "when": when,
        "outcome": outcome,
        "path": path,
        "category": category,
    }


def end(exitstatus=0, stopped=(), unplaced=0):
    return {
        "kind": "end",
        "exitstatus": exitstatus,
        "stopped": None if stopped is None else list(stopped),
        "unplaced": unplaced,
    }


WORKFLOW = (
    "name: hygiene\non: pull_request\njobs:\n"
    "  lint:\n    steps:\n      - name: not a release step\n"
    "  release:\n    steps:\n"
    "      - name: the unverified record is readable, and rows leave it closed\n"
    "      - name: 'a change to what ships must move the version'\n"
    "      - name: both READMEs move together\n"
    "      - name: a step nobody classified\n"
)


@pytest.fixture(autouse=True)
def _no_ambient_pull_request(monkeypatch):
    """Each case reads the fixture it built, never the pull request a runner
    describes in its environment."""
    for name in AMBIENT:
        monkeypatch.delenv(name, raising=False)


def clean_env():
    return {k: v for k, v in os.environ.items() if k not in AMBIENT}


# --- the module as a whole ------------------------------------------------------


class Test_module:
    def test_the_gate_reads_the_given_base_exactly_once(self):
        """Every check asks the resolved commit; `args.base`, the spelling
        the caller typed, is read once, by the resolution, so a consumer
        written later cannot take the unresolved value unseen (#423)."""
        tree = ast.parse((ROOT / TARGET).read_text(encoding="utf-8"))
        reads = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Attribute)
            and node.attr == "base"
            and isinstance(node.value, ast.Name)
            and node.value.id == "args"
        ]
        assert len(reads) == 1, [node.lineno for node in reads]

    def test_the_gate_and_the_check_spell_the_file_and_separator_alike(self):
        assert gate.GATE_FILE == chain.BROAD_GATE_FILE
        assert gate.EARLIER_RUN == chain.EARLIER_RUN
        assert gate.ROW == chain.BROAD_GATE
        assert gate.CHAIN_SEALING == chain.SEALING

    def test_a_file_the_gate_wrote_is_read_by_the_check(self, tmp_path):
        path = gate.write_gate_file(str(tmp_path), "abc1234", "def5678")
        reader = load_module(READER, "unverified_reader_beside_broad_gate")
        text = pathlib.Path(path).read_text(encoding="utf-8")
        assert chain.newest_run(reader, text) == "abc1234"
        assert chain.newest_run(reader, text.replace("abc1234", "zz")) is None


# --- loading a sibling ------------------------------------------------------------


class Test_load:
    def test_accepts_a_sibling_that_imports(self):
        mod = gate.load(gate.STAMP, "stamp_loaded_by_the_case")
        assert mod.PANEL_VALUE_WIDTH == stamp.PANEL_VALUE_WIDTH

    def test_refuses_a_missing_file(self, tmp_path):
        with pytest.raises(gate.Refused, match="this copy of the plugin is missing it"):
            gate.load(str(tmp_path / "gone.py"), "gone")

    def test_refuses_a_sibling_that_raises_with_its_own_sentence(self, tmp_path):
        write(tmp_path, "bad.py", "raise ValueError('the chart is malformed')\n")
        write(tmp_path, "bare.py", "raise ValueError()\n")
        with pytest.raises(gate.Refused) as said:
            gate.load(str(tmp_path / "bad.py"), "bad")
        assert str(said.value).endswith("nothing ran: the chart is malformed")
        with pytest.raises(gate.Refused) as bare:
            gate.load(str(tmp_path / "bare.py"), "bare")
        assert str(bare.value).endswith("nothing ran: ValueError")

    def test_refuses_to_turn_a_siblings_exit_into_a_refusal(self, tmp_path):
        write(tmp_path, "floor.py", "raise SystemExit(3)\n")
        with pytest.raises(SystemExit):
            gate.load(str(tmp_path / "floor.py"), "floor")


# --- which copy runs ----------------------------------------------------------------


def a_plugin(directory, version):
    write(directory, ".claude-plugin/plugin.json", json.dumps({"version": version}))
    return str(directory)


class Test_shipped_gate:
    def test_accepts_a_tree_that_ships_its_own_copy(self, tmp_path):
        write(tmp_path, gate.GATE_REL, "print('a copy')\n")
        assert gate.shipped_gate(str(tmp_path)) == str(tmp_path / gate.GATE_REL)

    def test_refuses_a_tree_without_one_and_the_running_file_itself(self, tmp_path):
        assert gate.shipped_gate(str(tmp_path)) is None
        assert gate.shipped_gate(str(ROOT)) is None


class Test_plugin_version:
    def test_accepts_the_version_plugin_json_names(self, tmp_path):
        assert gate.plugin_version(a_plugin(tmp_path, "9.8.7")) == "9.8.7"

    def test_refuses_a_file_that_is_missing_or_names_no_version(self, tmp_path):
        assert gate.plugin_version(str(tmp_path)) == "?"
        write(tmp_path, ".claude-plugin/plugin.json", "[1, 2]")
        assert gate.plugin_version(str(tmp_path)) == "?"
        write(tmp_path, ".claude-plugin/plugin.json", "{}")
        assert gate.plugin_version(str(tmp_path)) == "?"


class Test_under:
    def test_accepts_a_path_under_the_root(self, tmp_path):
        assert gate.under(str(tmp_path / "a" / "b"), str(tmp_path))

    def test_refuses_a_sibling_and_no_root(self, tmp_path):
        assert not gate.under(str(tmp_path / "b"), str(tmp_path / "a"))
        assert not gate.under(str(tmp_path), None)


class Test_copy_origin:
    def test_accepts_a_copy_under_the_root_as_the_trees(self, tmp_path):
        plugin = a_plugin(tmp_path / "plugin", "1.2.3")
        running = str(tmp_path / "repo" / "broad_gate.py")
        assert gate.copy_origin(str(tmp_path / "repo"), plugin, running) == "tree 1.2.3"

    def test_refuses_to_call_a_copy_elsewhere_the_trees(self, tmp_path):
        plugin = a_plugin(tmp_path / "plugin", "1.2.3")
        running = str(tmp_path / "plugin" / "broad_gate.py")
        assert gate.copy_origin(str(tmp_path / "repo"), plugin, running) == (
            "plugin 1.2.3"
        )
        assert gate.copy_origin(None, plugin, running).startswith("plugin ")


class Test_gate_copy:
    def test_accepts_a_tree_copy_whose_bytes_differ_from_the_invoked(self, tmp_path):
        plugin = a_plugin(tmp_path / "plugin", "1.2.3")
        write(tmp_path, "repo/gate.py", "mine\n")
        write(tmp_path, "installed/gate.py", "theirs\n")
        running, installed = tmp_path / "repo/gate.py", tmp_path / "installed/gate.py"
        root = str(tmp_path / "repo")
        assert gate.gate_copy(root, plugin, str(running), str(installed)) == (
            "tree 1.2.3"
        )
        assert gate.gate_copy(root, plugin, str(running), None) == "tree 1.2.3"

    def test_refuses_a_copy_outside_the_root_or_one_equal_to_the_invoked(
        self, tmp_path
    ):
        plugin = a_plugin(tmp_path / "plugin", "1.2.3")
        write(tmp_path, "repo/gate.py", "same\n")
        write(tmp_path, "installed/gate.py", "same\n")
        running, installed = tmp_path / "repo/gate.py", tmp_path / "installed/gate.py"
        root = str(tmp_path / "repo")
        assert gate.gate_copy(root, plugin, str(running), str(installed)) is None
        outside = str(tmp_path / "elsewhere")
        assert gate.gate_copy(outside, plugin, str(running), None) is None


# --- which base -------------------------------------------------------------------


@pytest.fixture(scope="module")
def refs(tmp_path_factory):
    """One repository, read and never written by the cases that take it:
    `base` tracks `other/base`, a remote's copy one commit ahead; `solo` has
    no upstream and `origin/solo` stands one commit ahead of it; `gone`
    exists only as `origin/gone`; and `origin/HEAD` points at `solo`."""
    d = tmp_path_factory.mktemp("refs") / "repo"
    d.mkdir()
    git(d, "init", "-q", "-b", "base")
    write(d, "a.txt", "1\n")
    first = commit(d, "first")
    write(d, "a.txt", "2\n")
    second = commit(d, "second")
    git(d, "reset", "-q", "--hard", first)
    git(d, "branch", "-q", "solo")
    git(d, "update-ref", "refs/remotes/other/base", second)
    git(d, "update-ref", "refs/remotes/origin/base", second)
    git(d, "update-ref", "refs/remotes/origin/solo", second)
    git(d, "update-ref", "refs/remotes/origin/gone", second)
    git(d, "symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/solo")
    git(d, "config", "branch.base.remote", "other")
    git(d, "config", "branch.base.merge", "refs/heads/base")
    git(d, "config", "remote.other.url", ".")
    git(d, "config", "remote.other.fetch", "+refs/heads/*:refs/remotes/other/*")
    return str(d), first[:7], second[:7]


def short(repo, rev):
    return git_out(repo, "rev-parse", "--short", rev)


class Test_Base:
    def test_accepts_two_commits_apart_as_moved(self):
        assert gate.Base("base", "aaa1111", "origin/base", "bbb2222").moved
        assert gate.Base("gone", None, "origin/gone", "bbb2222").moved

    def test_refuses_one_commit_as_moved(self):
        assert not gate.Base("base", "aaa1111", "base", "aaa1111").moved


class Test_moved_line:
    def test_accepts_a_base_the_runner_reads_ahead_of_the_local_one(self, refs):
        root = refs[0]
        base = gate.Base(
            "solo", short(root, "solo"), "origin/solo", short(root, "origin/solo")
        )
        line = gate.moved_line(root, base)
        assert line == (
            f"broad-gate: --base solo is {base.given_commit} in this checkout; CI "
            f"reads origin/solo, which is {base.commit} — origin/solo is 1 ahead "
            "and 0 behind solo. Every check below was asked about origin/solo."
        )

    def test_accepts_an_upstream_that_is_not_the_runners_and_names_both(self, refs):
        root = refs[0]
        base = gate.Base(
            "base", short(root, "base"), "other/base", short(root, "other/base")
        )
        line = gate.moved_line(root, base)
        assert "this checkout says base tracks other/base" in line
        assert "not the origin/base a runner reads" in line

    def test_accepts_a_spelling_that_names_no_commit_here(self, refs):
        root, _first, _second = refs
        base = gate.Base("gone", None, "origin/gone", short(root, "origin/gone"))
        assert gate.moved_line(root, base).startswith(
            "broad-gate: --base gone names no commit in this checkout; CI reads"
        )

    def test_accepts_a_spelling_no_runner_could_hold_without_naming_one(self, refs):
        root, _first, _second = refs
        base = gate.Base("@{-1}", None, "other/base", "abc1234")
        line = gate.moved_line(root, base)
        assert "a runner's checkout has no counterpart for @{-1}" in line
        assert "origin/@{-1}" not in line

    def test_refuses_to_print_where_nothing_moved(self, refs):
        root, _first, _second = refs
        commit_of = short(root, "base")
        assert (
            gate.moved_line(root, gate.Base("base", commit_of, "base", commit_of))
            is None
        )


class Test_short_commit:
    def test_accepts_a_revision_naming_a_commit(self, refs):
        root, first, _second = refs
        assert gate.short_commit(root, "base") == short(root, first)

    def test_refuses_a_revision_naming_nothing(self, refs):
        root, _first, _second = refs
        assert gate.short_commit(root, "no-such-ref") is None


class Test_names_a_branch:
    @pytest.mark.parametrize("given", ["base", "release/v1.2.3", "abc1234"])
    def test_accepts_a_spelling_a_branch_could_have(self, refs, given):
        assert gate.names_a_branch(refs[0], given)

    @pytest.mark.parametrize("given", ["HEAD", "HEAD~1", "base@{u}"])
    def test_refuses_a_revision_expression(self, refs, given):
        assert not gate.names_a_branch(refs[0], given)


class Test_a_runner_could_hold:
    def test_accepts_a_remote_ref_name(self, refs):
        assert gate.a_runner_could_hold(refs[0], "origin/base")

    def test_refuses_a_name_no_ref_can_have(self, refs):
        assert not gate.a_runner_could_hold(refs[0], "origin/@{-1}")


class Test_resolve_base:
    def test_accepts_the_upstream_this_checkout_declares(self, refs):
        root, first, second = refs
        base = gate.resolve_base(root, "base")
        assert (base.given, base.ref) == ("base", "other/base")
        assert (base.given_commit, base.commit) == (
            short(root, first),
            short(root, second),
        )

    def test_accepts_origins_ref_where_no_upstream_is_declared(self, refs):
        root, _first, second = refs
        base = gate.resolve_base(root, "solo")
        assert (base.ref, base.commit) == ("origin/solo", short(root, second))

    def test_refuses_to_read_a_revision_expression_through_a_remote(self, refs):
        root, first, _second = refs
        base = gate.resolve_base(root, "HEAD")
        assert (base.ref, base.commit) == ("HEAD", short(root, first))
        assert not base.moved

    def test_refuses_a_base_that_resolves_nowhere(self, refs):
        base = gate.resolve_base(refs[0], "nowhere")
        assert (base.ref, base.commit) == ("nowhere", None)


# --- the row ------------------------------------------------------------------------


class Test_seal_home:
    def test_accepts_the_shared_root_and_then_the_local_one(self, tmp_path):
        (tmp_path / "shared" / "seal").mkdir(parents=True)
        assert gate.seal_home(str(tmp_path / "shared")) == str(
            tmp_path / "shared" / "seal"
        )
        local = tmp_path / "local"
        local.mkdir()
        git(local, "init", "-q")
        (local / ".git" / "seal").mkdir()
        assert gate.seal_home(str(local)) == os.path.normpath(
            str(local / ".git" / "seal")
        )

    def test_refuses_a_repository_with_neither(self, tmp_path):
        git(tmp_path, "init", "-q")
        assert gate.seal_home(str(tmp_path)) is None


class Test_broad_command:
    def test_accepts_the_rows_value(self, tmp_path):
        home = home_with(tmp_path, config_of("bin/test -q"))
        assert gate.broad_command(home) == "bin/test -q"

    def test_refuses_no_file_no_row_and_an_empty_value_as_no_command(self, tmp_path):
        assert gate.broad_command(str(tmp_path / "nothing")) is None
        assert gate.broad_command(home_with(tmp_path / "a", config_of(None))) is None
        assert gate.broad_command(home_with(tmp_path / "b", config_of(""))) is None

    def test_refuses_a_row_written_twice(self, tmp_path):
        home = home_with(tmp_path, config_of("a") + f"| {ROW} | b |\n")
        with pytest.raises(gate.Refused, match="Nothing ran"):
            gate.broad_command(home)

    def test_refuses_a_file_that_will_not_read(self, tmp_path):
        (tmp_path / "seal").mkdir()
        (tmp_path / "seal" / "config.md").write_bytes(b"| Item | Value |\n\xff\xfe\n")
        with pytest.raises(gate.Refused, match=r"^broad-gate: .*Nothing ran$"):
            gate.broad_command(str(tmp_path / "seal"))


class Test_names_this_row:
    def test_accepts_a_line_whose_first_cell_is_the_row(self):
        assert gate.names_this_row(f"| {ROW} | a |")
        assert gate.names_this_row(f"  | {ROW} | a | b |")

    def test_refuses_another_row_and_a_line_with_no_cell(self):
        assert not gate.names_this_row("| Mode | shared |")
        assert not gate.names_this_row(ROW)


# A table the walker stops at, with the row below the line it refused.
STOPPED_ABOVE = config_of(None) + "| Odd | a | b |\n" + f"| {ROW} | bin/test |\n"
# A table whose `Broad gate` line holds a bare pipe, written last.
BARE_PIPE_LAST = config_of("bin/test -q | tee out.txt")
# The table read whole, and a `Broad gate` line in another table below it.
ANOTHER_TABLE = (
    config_of(None) + f"\n## Other\n\n| Name | What |\n|---|---|\n| {ROW} | x |\n"
)
FENCED = config_of(None) + f"\n```\n| Item | Value |\n|---|---|\n| {ROW} | x |\n```\n"
COMMENTED = config_of(None) + f"\n<!--\n| {ROW} | x |\n-->\n"


class Test_refused_broad_row:
    def test_accepts_a_row_below_the_line_the_walker_refused(self, tmp_path):
        home = home_with(tmp_path, STOPPED_ABOVE)
        assert gate.refused_broad_row(home) == f"| {ROW} | bin/test |"

    def test_refuses_a_table_the_walker_read_whole(self, tmp_path):
        assert gate.refused_broad_row(home_with(tmp_path, ANOTHER_TABLE)) is None
        assert gate.refused_broad_row(str(tmp_path / "nothing")) is None


class Test_stopping_line:
    def test_accepts_the_line_the_walkers_sentence_quotes(self):
        refused = gate.load(gate.CONFIG_READER, "c").config_table(STOPPED_ABOVE)[1][0]
        index, line = gate.stopping_line(STOPPED_ABOVE, refused)
        assert line == "| Odd | a | b |"
        assert STOPPED_ABOVE.splitlines()[index] == line

    def test_refuses_a_sentence_that_quotes_no_line(self):
        assert gate.stopping_line(STOPPED_ABOVE, "has no header") == (None, None)
        quoted = "has a `x` table that stops at `| a |`, which is not a row"
        assert gate.stopping_line("no table here\n", quoted) == (None, None)


class Test_rows_written_below:
    def test_accepts_a_row_below_the_line(self):
        assert gate.rows_written_below(STOPPED_ABOVE, 3)

    def test_refuses_nothing_below_or_a_heading_first(self):
        text = config_of(None) + "| Odd | a | b |\n"
        assert not gate.rows_written_below(text, 3)
        assert not gate.rows_written_below(text + "\n## Later\n\n| a | b |\n", 3)


class Test_hidden_row_at:
    def test_accepts_the_row_in_a_fence_as_fenced(self, tmp_path):
        home = home_with(tmp_path, FENCED)
        assert gate.fenced_row(home) == f"| {ROW} | x |"
        index, line = gate.fenced_row_at(home)
        assert FENCED.splitlines()[index] == line
        assert gate.commented_row_at(home) == (None, None)

    def test_refuses_to_call_a_commented_row_fenced(self, tmp_path):
        home = home_with(tmp_path, COMMENTED)
        assert gate.fenced_row(home) is None
        assert gate.commented_row_at(home)[1] == f"| {ROW} | x |"
        assert gate.hidden_row_at(str(tmp_path / "nothing"), "fence") == (None, None)


class Test_fence_left_open:
    def test_accepts_a_fence_above_that_never_closes(self, tmp_path):
        home = home_with(tmp_path, "```\n" + config_of())
        assert gate.fence_left_open(home, 5)
        assert gate.fence_left_open(home)

    def test_refuses_a_fence_opened_below_or_none_at_all(self, tmp_path):
        home = home_with(tmp_path, FENCED + "\n```\nopen\n")
        at = gate.fenced_row_at(home)[0]
        assert not gate.fence_left_open(home, at)
        assert not gate.fence_left_open(home_with(tmp_path / "b", config_of()), 3)
        assert not gate.fence_left_open(str(tmp_path / "nothing"))


class Test_missing_row:
    def test_accepts_a_file_with_no_row_as_a_question_for_a_person(self, tmp_path):
        said = gate.missing_row(home_with(tmp_path, config_of(None)))
        assert f"has no `{ROW}` row, so there is no command to run" in said
        assert "Take it to whoever owns the repository" in said
        assert said.endswith("Nothing ran.")

    def test_refuses_to_call_a_fenced_row_absent(self, tmp_path):
        said = gate.missing_row(home_with(tmp_path, FENCED))
        assert "written inside a code fence:\n    | Broad gate | x |" in said
        assert "Move the row into the `| Item | Value |` table" in said
        assert "Close that fence" not in said

    def test_refuses_to_send_a_person_to_move_a_row_a_fence_above_swallowed(
        self, tmp_path
    ):
        said = gate.missing_row(home_with(tmp_path, "```\n" + config_of("x")))
        assert "A fenced code block above it is never closed" in said
        assert "Move the row" not in said

    def test_refuses_to_call_a_commented_row_absent(self, tmp_path):
        said = gate.missing_row(home_with(tmp_path, COMMENTED))
        assert "written inside an HTML comment:\n    | Broad gate | x |" in said
        assert "has no `Broad gate` row" not in said

    def test_refuses_to_call_a_row_the_walker_did_not_read_absent(self, tmp_path):
        said = gate.missing_row(home_with(tmp_path, STOPPED_ABOVE))
        assert "stops at `| Odd | a | b |`" in said
        assert said.endswith("Nothing ran.")
        assert "inside" not in said and "has no `Broad gate` row" not in said


class Test_walker_refusal:
    def test_accepts_the_rows_own_line_with_the_escape(self, tmp_path):
        home = home_with(tmp_path, BARE_PIPE_LAST)
        said = gate.walker_refusal(home, f"| {ROW} | bin/test -q | tee out.txt |")
        assert "That line is the `Broad gate` row, so the walk never read it" in said
        assert "write it `\\|`" in said
        assert "would go unread" not in said

    def test_accepts_a_stray_row_last_as_losing_itself_alone(self, tmp_path):
        home = home_with(tmp_path, config_of(None) + f"\n| {ROW} | x |\n")
        said = gate.walker_refusal(home, f"| {ROW} | x |")
        assert f"ends above `| {ROW} | x |`" in said
        assert "a row the walk never reaches — it would go unread." in said

    def test_refuses_to_call_a_row_below_the_stopping_line_that_line(self, tmp_path):
        home = home_with(tmp_path, STOPPED_ABOVE)
        said = gate.walker_refusal(home, f"| {ROW} | bin/test |")
        assert "The `Broad gate` row is written below it" in said
        assert f"never reached it:\n    | {ROW} | bin/test |\n" in said
        assert "every row below it would go unread" in said
        assert "\\|" not in said


class Test_wholly_substituted:
    @pytest.mark.parametrize(("value", "opener"), [("`x`", "`"), ("$(a (b))", "$(")])
    def test_accepts_a_wrapper_around_the_whole_value(self, value, opener):
        assert gate.wholly_substituted(value) == opener

    @pytest.mark.parametrize(
        "value",
        ["$(a) && b", "$(a) && $(b)", "`a` && `b`", "pytest -n $(nproc)", "plain"],
    )
    def test_refuses_a_pair_that_wraps_a_part(self, value):
        assert gate.wholly_substituted(value) is None


class Test_not_as_written:
    @pytest.mark.parametrize(
        "value", ["a && b", "a | tee f", "a & b", "x $(y)", "a &&"]
    )
    def test_accepts_a_value_that_runs_as_it_reads(self, value):
        assert gate.not_as_written("/h", value) is None

    @pytest.mark.parametrize(
        ("value", "form", "meant"),
        [
            ("`bin/test -q`", "wrapped in backticks", "bin/test -q"),
            ("$(bin/test -q)", "wrapped in `$(…)`", "bin/test -q"),
            ("bin/test -q &", "ends in a single `&`", "bin/test -q"),
        ],
    )
    def test_refuses_a_wrapped_or_backgrounded_value(self, value, form, meant):
        said = gate.not_as_written("/h", f"  {value} ")
        assert form in said
        assert f"    as written: | {ROW} | {value} |" in said
        assert f"    as meant:   | {ROW} | {meant} |" in said


# --- running one check ----------------------------------------------------------------


class Test_Check:
    def test_accepts_a_zero_exit_as_passed_and_quotes_its_lines(self):
        check = gate.Check("x", 0, "a\n\n  \nb  \n", "/k/x.txt")
        assert not check.failed
        assert check.first_lines() == ["a", "b"]

    def test_refuses_a_nonzero_exit_as_passed(self):
        assert gate.Check("x", 3, "", "/k").failed


class Test_run:
    def test_accepts_a_command_and_keeps_both_streams_and_the_exit(self, tmp_path):
        code = "import sys; print('out'); print('err', file=sys.stderr); sys.exit(3)"
        check = gate.run(
            "x", [sys.executable, "-c", code], str(tmp_path), str(tmp_path)
        )
        assert (check.code, check.text.split()) == (3, ["out", "err"])
        kept = pathlib.Path(check.path).read_text(encoding="utf-8").splitlines()
        assert kept[1:3] == ["exit 3", ""]

    def test_refuses_to_hide_what_cmd_exe_was_handed(self, tmp_path, capsys):
        (tmp_path / "bin").mkdir()
        check = gate.run(
            "suite",
            "bin/echo hi",
            str(tmp_path),
            str(tmp_path),
            shell=True,
            windows=True,
            comspec="cmd.exe",
        )
        kept = pathlib.Path(check.path).read_text(encoding="utf-8").splitlines()
        assert kept[:2] == ["$ bin/echo hi", "cmd.exe was handed: bin\\echo hi"]
        assert "broad-gate: suite — cmd.exe reads a `/`" in capsys.readouterr().err


class Test_as_cmd_expands:
    def test_accepts_cd_and_its_twin_as_the_rows_directory(self, tmp_path, monkeypatch):
        monkeypatch.delenv("CD", raising=False)
        monkeypatch.delenv("__CD__", raising=False)
        here = str(tmp_path)
        assert gate.as_cmd_expands("%CD%\\x", here) == os.path.abspath(here) + "\\x"
        assert gate.as_cmd_expands("%__CD__%x", here) == os.path.join(here, "x")

    def test_refuses_to_compute_a_name_the_environment_defines(
        self, tmp_path, monkeypatch
    ):
        monkeypatch.setenv("CD", "/set")
        monkeypatch.delenv("NOT_DEFINED_HERE", raising=False)
        assert gate.as_cmd_expands("%CD%", str(tmp_path)) == "/set"
        assert gate.as_cmd_expands("%NOT_DEFINED_HERE%%%", "/x") == (
            "%NOT_DEFINED_HERE%%%"
        )


class Test_cmd_exe_reads:
    @pytest.mark.parametrize("comspec", [None, "", r'"C:\Windows\System32\CMD.EXE"'])
    def test_accepts_windows_with_cmd_exe_or_no_comspec(self, comspec, monkeypatch):
        monkeypatch.delenv("COMSPEC", raising=False)
        assert gate.cmd_exe_reads(True, comspec)

    def test_refuses_another_shell_and_another_platform(self):
        assert not gate.cmd_exe_reads(True, r"C:\msys64\usr\bin\bash.exe")
        assert not gate.cmd_exe_reads(False, "cmd.exe")


class Test_handed_to_shell:
    def test_accepts_a_name_starting_in_a_directory_of_the_root(self, tmp_path):
        (tmp_path / "bin").mkdir()
        handed = gate.handed_to_shell("bin/test -q", True, "cmd.exe", str(tmp_path))
        assert handed == "bin\\test -q"

    def test_refuses_to_turn_a_name_whose_directory_the_root_lacks(self, tmp_path):
        assert gate.handed_to_shell("bin/test", True, "cmd.exe", str(tmp_path)) == (
            "bin/test"
        )
        assert gate.handed_to_shell("bin/test", False, None, str(ROOT)) == "bin/test"


class Test_command_names_backslashed:
    @staticmethod
    def turned(command, *dirs):
        return gate.command_names_backslashed(command, lambda part: part in dirs)

    def test_accepts_each_name_in_command_position(self):
        assert self.turned("bin/test -q a/b && tools/x", "bin", "tools") == (
            "bin\\test -q a/b && tools\\x"
        )
        assert self.turned("a | bin/test", "bin") == "a | bin\\test"
        assert self.turned("/abs/x") == "\\abs\\x"
        assert self.turned('"bin/a b/c" d/e', "bin") == '"bin\\a b\\c" d/e'

    def test_refuses_a_builtins_switch_a_program_and_an_escaped_separator(self):
        assert self.turned("rd/s/q x", "rd") == "rd/s/q x"
        assert self.turned("xcopy/e a") == "xcopy/e a"
        assert self.turned("echo a^&bin/test", "bin") == "echo a^&bin/test"
        assert self.turned("echo >out bin/test", "bin") == "echo >out bin/test"


# --- the base comparison ----------------------------------------------------------------


class Test_record_key:
    def test_accepts_the_kind_before_sixteen_hex_digits(self):
        kind, digits = gate.record_key("head").split("-")
        assert kind == "head" and len(digits) == 16 and int(digits, 16) >= 0

    def test_refuses_to_give_two_runs_one_key(self):
        assert len({gate.record_key("base") for _ in range(8)}) == 8


class Test_recording_env:
    def test_accepts_what_the_caller_set_and_adds_the_recorder(
        self, tmp_path, monkeypatch
    ):
        monkeypatch.chdir(tmp_path)
        monkeypatch.setenv("PYTHONPATH", "/theirs")
        monkeypatch.setenv("PYTEST_ADDOPTS", "-q")
        env = gate.recording_env("kept", "head-1")
        assert env["PYTHONPATH"] == os.pathsep.join([gate.RECORDER_DIR, "/theirs"])
        assert env["PYTEST_ADDOPTS"] == f"-q -p {gate.RECORDER}"
        assert env[gate.RECORD_KEY_VARIABLE] == "head-1"
        assert env[gate.RECORD_DIR_VARIABLE] == str(tmp_path / "kept" / "records")
        assert os.path.isdir(env[gate.RECORD_DIR_VARIABLE])

    def test_refuses_to_leave_an_empty_part_where_nothing_was_set(
        self, tmp_path, monkeypatch
    ):
        monkeypatch.delenv("PYTHONPATH", raising=False)
        monkeypatch.delenv("PYTEST_ADDOPTS", raising=False)
        env = gate.recording_env(str(tmp_path), "k")
        assert env["PYTHONPATH"] == gate.RECORDER_DIR
        assert env["PYTEST_ADDOPTS"] == f"-p {gate.RECORDER}"


class Test_record_path:
    def test_accepts_a_path_under_the_worktree_as_relative(self, tmp_path):
        assert gate.record_path(str(tmp_path / "t" / "a.py"), str(tmp_path)) == "t/a.py"

    def test_accepts_a_worktree_spelled_through_a_link(self, tmp_path):
        (tmp_path / "real").mkdir()
        symlink_or_skip(tmp_path / "real", tmp_path / "link")
        path = str(tmp_path / "real" / "t.py")
        assert gate.record_path(path, str(tmp_path / "link")) == "t.py"

    def test_refuses_to_name_a_path_outside_relatively(self, tmp_path):
        outside = tmp_path / "other" / "t.py"
        assert gate.record_path(str(outside), str(tmp_path / "w")) == os.path.realpath(
            outside
        )


class Test_read_record:
    def test_accepts_its_keys_files_in_the_order_they_were_written(self, tmp_path):
        # Written b, c, a, last modified c, a, b, and named a, b, c: the order
        # read is the third, whatever the directory lists first.
        for name, at in (("b", 3), ("c", 1), ("a", 2)):
            jsonl(
                tmp_path,
                f"{name}.jsonl",
                session("k"),
                a_test(f"/w/{name}.py", "failed", "failed"),
                end(1),
                mtime=at * 1_000_000_000,
            )
        record = gate.read_record(str(tmp_path), "k", "/w")
        assert record.sessions == 3
        assert list(record.failing) == ["c.py", "a.py", "b.py"]
        assert record.counts == {"failed": 3}
        assert record.unended == 0

    def test_accepts_one_collection_per_session_however_often_written(self, tmp_path):
        collect = {
            "kind": "collect",
            "nodeid": "t/c.py",
            "outcome": "failed",
            "path": "/w/t/c.py",
        }
        skipped = dict(collect, nodeid="t/s.py", outcome="skipped", path="/w/t/s.py")
        jsonl(tmp_path, "a.jsonl", session("k"), collect, collect, skipped, end(2))
        record = gate.read_record(str(tmp_path), "k", "/w")
        assert record.counts == {"error": 1, "skipped": 1}
        assert list(record.failing) == ["t/c.py"]
        assert record.collected == {"t/c.py", "t/s.py"}

    def test_refuses_another_runs_file_and_counts_none_of_it(self, tmp_path):
        jsonl(tmp_path, "a.jsonl", session("other"), a_test("/w/a.py", "failed"), "x")
        jsonl(tmp_path, "b.txt", session("k"))
        record = gate.read_record(str(tmp_path), "k", "/w")
        assert (record.sessions, record.unread, record.failing) == (0, 0, {})
        assert gate.read_record(str(tmp_path / "missing"), "k", "/w").sessions == 0

    def test_refuses_to_trust_a_line_that_is_no_object(self, tmp_path):
        jsonl(tmp_path, "a.jsonl", session("k"), "not json", "[1]", "", end(0))
        assert gate.read_record(str(tmp_path), "k", "/w").unread == 2

    @pytest.mark.parametrize(
        "ending",
        [[], [end(0, stopped=["exit"])], [end(2)], [end(0, stopped=None)]],
        ids=["no-end", "stopped", "interrupted", "stopped-unknown"],
    )
    def test_refuses_to_call_a_session_that_stopped_part_way_ended(
        self, tmp_path, ending
    ):
        jsonl(tmp_path, "a.jsonl", session("k"), a_test("/w/a.py"), *ending)
        assert gate.read_record(str(tmp_path), "k", "/w").unended == 1

    def test_refuses_to_count_unplaced_reports_of_a_session_that_passed_as_red(
        self, tmp_path
    ):
        jsonl(tmp_path, "a.jsonl", session("k"), end(0, unplaced=2))
        jsonl(tmp_path, "b.jsonl", session("k"), end(1, unplaced=3))
        jsonl(tmp_path, "c.jsonl", session("k"), end(1, unplaced="3"))
        record = gate.read_record(str(tmp_path), "k", "/w")
        assert (record.unplaced, record.unplaced_red) == (5, 3)


class Test_failing_files:
    def test_accepts_each_file_once_in_first_seen_order(self):
        text = (
            "FAILED tests/b c.py::t - x\nFAILED tests/a.py::t\n"
            "FAILED tests/b c.py::u - y\n  FAILED not/at/the/start.py::t\n"
        )
        assert gate.failing_files(text) == ["tests/b c.py", "tests/a.py"]

    def test_refuses_a_line_that_is_not_a_failure(self):
        assert gate.failing_files("PASSED tests/a.py::t\nERROR tests/b.py\n") == []


class Test_quote:
    def test_accepts_a_path_with_a_space_for_either_shell(self):
        assert gate.quote("a b.py", windows=False) == "'a b.py'"
        assert gate.quote("a b.py", windows=True) == '"a b.py"'

    def test_refuses_to_leave_a_metacharacter_to_cmd_exe(self):
        assert gate.quote("a&b.py", windows=True) == '"a&b.py"'


class Test_base_word:
    def test_accepts_a_file_the_base_fails_or_passes(self):
        record = a_record(
            sessions=1, failing={"a.py": None}, collected={"a.py", "b.py"}
        )
        assert gate.base_word(record, 1, "a.py") == gate.ON_BASE
        assert gate.base_word(record, 1, "b.py") == gate.NEW
        assert gate.base_word(a_record(sessions=1), 0, "c.py") == gate.NEW

    def test_refuses_new_where_the_base_did_not_measure_the_file(self):
        assert gate.base_word(a_record(), 0, "a.py") == gate.NO_RECORD
        assert gate.base_word(a_record(sessions=1), 4, "a.py") == (
            gate.NOT_REACHED.format(code=4)
        )

    @pytest.mark.parametrize(
        ("fields", "word"),
        [
            ({"unplaced_red": 2, "unended": 1, "unread": 1}, "UNPLACED_AT_BASE"),
            ({"unended": 3, "unread": 1}, "UNENDED_AT_BASE"),
            ({"unread": 4}, "UNREAD_AT_BASE"),
        ],
    )
    def test_refuses_new_from_a_record_that_left_something_out(self, fields, word):
        record = a_record(sessions=1, collected={"a.py"}, **fields)
        count = next(iter(fields.values()))
        assert gate.base_word(record, 1, "a.py") == getattr(gate, word).format(
            count=count
        )


# --- the workflow -----------------------------------------------------------------


class Test_unquote:
    def test_accepts_a_quoted_scalar_without_its_quotes(self):
        assert gate.unquote("'a b'") == "a b"
        assert gate.unquote('"a"') == "a"

    def test_refuses_quotes_that_do_not_match(self):
        for value in ("'a\"", "'", "a'"):
            assert gate.unquote(value) == value


class Test_job_steps:
    def test_accepts_the_named_steps_of_one_job(self):
        assert gate.job_steps(WORKFLOW, "release") == [
            "the unverified record is readable, and rows leave it closed",
            "a change to what ships must move the version",
            "both READMEs move together",
            "a step nobody classified",
        ]

    def test_refuses_a_text_with_no_jobs_and_another_jobs_steps(self):
        assert gate.job_steps("name: x\n", "release") == []
        assert gate.job_steps(WORKFLOW, "lint") == ["not a release step"]


class Test_base_is_main:
    @pytest.mark.parametrize("given", ["main", "origin/main"])
    def test_accepts_main_as_typed_or_as_origins(self, given):
        assert gate.base_is_main(given)

    @pytest.mark.parametrize("given", [None, "release/v1", "upstream/main"])
    def test_refuses_any_other_base(self, given):
        assert not gate.base_is_main(given)


class Test_steps_for:
    def test_accepts_every_step_into_main(self):
        assert len(gate.steps_for(WORKFLOW, "main")) == 4

    def test_refuses_the_main_only_steps_on_another_base(self):
        steps = gate.steps_for(WORKFLOW, "release/v1")
        assert "a change to what ships must move the version" not in steps
        assert len(steps) == 3
        assert gate.steps_for(None, "main") == []


class Test_left_out_clause:
    def test_accepts_the_count_and_why_on_another_base(self):
        assert gate.left_out_clause(WORKFLOW, "release/v1") == (
            " 1 more runs only on a pull request into `main`, so this count leaves "
            "it out."
        )

    def test_refuses_a_clause_where_nothing_was_left_out(self):
        assert gate.left_out_clause(WORKFLOW, "main") == ""
        assert gate.left_out_clause(None, "release/v1") == ""


class Test_workflow_text:
    def test_accepts_the_workflow_the_tree_holds(self, tmp_path):
        write(tmp_path, gate.WORKFLOW, WORKFLOW)
        assert gate.workflow_text(str(tmp_path)) == WORKFLOW

    def test_refuses_a_missing_file_and_one_that_is_not_utf8(self, tmp_path):
        assert gate.workflow_text(str(tmp_path)) is None
        path = tmp_path / gate.WORKFLOW
        path.parent.mkdir(parents=True)
        path.write_bytes(b"jobs:\n\xff\n")
        assert gate.workflow_text(str(tmp_path)) is None


class Test_unanswered:
    def test_accepts_the_steps_no_arm_mirrors(self):
        assert gate.unanswered(WORKFLOW, "main") == [
            "a change to what ships must move the version",
            "both READMEs move together",
            "a step nobody classified",
        ]

    def test_refuses_a_mirrored_step(self):
        assert gate.mirrored()[gate.job_steps(WORKFLOW, "release")[0]] == "unverified"
        assert gate.job_steps(WORKFLOW, "release")[0] not in gate.unanswered(
            WORKFLOW, "release/v1"
        )


class Test_coverage_line:
    def test_accepts_a_workflow_every_step_of_which_is_answered(self):
        text = (
            "jobs:\n  release:\n    steps:\n      - name: both READMEs move together\n"
        )
        text = text.replace(
            "both READMEs move together",
            "the mode the row declares is the mode the folder is in",
        )
        assert gate.coverage_line(text, "main") == (
            "broad-gate: this run answers every one of the 1 `release` steps "
            ".github/workflows/hygiene.yml runs for this base."
        )

    def test_refuses_to_send_a_reader_to_a_row_for_an_unclassified_step(self):
        said = gate.coverage_line(WORKFLOW, "main")
        excluded, unknown = said.split(" In no row of ")
        assert "both READMEs move together" in excluded
        assert "a step nobody classified" not in excluded
        assert unknown.endswith(": a step nobody classified.")
        assert gate.coverage_line("name: x\n", "main") is None


# --- what the report reads --------------------------------------------------------


class Test_suite_counts:
    def test_accepts_the_counts_in_pytests_order_and_words(self):
        record = a_record(
            sessions=1, counts={"weird": 1, "error": 2, "passed": 3, "failed": 1}
        )
        assert gate.suite_counts(record) == "1 failed, 3 passed, 2 errors, 1 weird"

    @pytest.mark.parametrize(
        "fields",
        [{}, {"unread": 1}, {"unplaced": 1}, {"counts": {}}],
        ids=["no-session", "unread", "unplaced", "nothing-counted"],
    )
    def test_refuses_a_count_nobody_can_vouch_for(self, fields):
        values = {"sessions": 1, "counts": {"passed": 1}}
        values.update(fields)
        if not fields:
            values["sessions"] = 0
        assert gate.suite_counts(a_record(**values)) is None


def a_round(*verdicts):
    """A round record in `templates/sdd-round.md`'s shape, one finding per
    `verdict:` value."""
    found = "".join(
        f"### {n}. x\n\nseverity: should\nlocation: `a:{n}`\n"
        f"evidence: read `a:{n}`\nverdict: {verdict}\n\nwhy\n\nanswer: \n\n"
        for n, verdict in enumerate(verdicts, 1)
    )
    return (
        "# r — review round 1\n\n"
        f"target: abc1234 against base\n\n## Findings\n\n{found}"
        "## Probes\n\n| Command | Result |\n|---|---|\n"
    )


class Test_round_records:
    def test_accepts_the_records_lowest_round_first(self, tmp_path):
        for n in (10, 2, 1):
            write(tmp_path, f"rounds/round-{n}.md", "x")
        write(tmp_path, "rounds/round-2-report.md", "x")
        names = [os.path.basename(p) for p in gate.round_records(str(tmp_path))]
        assert names == ["round-1.md", "round-2.md", "round-10.md"]

    def test_refuses_an_item_with_no_rounds_directory(self, tmp_path):
        assert gate.round_records(str(tmp_path)) == []


class Test_kept_runs:
    def test_accepts_a_new_run_first_and_keeps_the_earlier(self):
        held = "aaa1111 against base1; earlier run: bbb2222 against base1"
        assert gate.kept_runs(held, "ccc3333 against base1") == (
            "ccc3333 against base1; earlier run: aaa1111 against base1"
            "; earlier run: bbb2222 against base1"
        )
        assert gate.kept_runs("", "ccc3333 against base1") == "ccc3333 against base1"

    def test_refuses_to_record_one_comparison_twice(self):
        held = "aaa1111 against base1; earlier run: bbb2222 against base1"
        assert gate.kept_runs(held, "aaa1111 against base1") == held
        assert gate.kept_runs(held, "aaa1111 against base2").count("aaa1111") == 2


class Test_write_gate_file:
    def test_accepts_a_second_run_in_front_of_the_first(self, tmp_path):
        gate.write_gate_file(str(tmp_path), "aaa1111", "base1")
        path = gate.write_gate_file(str(tmp_path), "bbb2222", "base1")
        text = pathlib.Path(path).read_text(encoding="utf-8")
        assert os.path.basename(path) == "broad-gate.md"
        assert (
            "| Broad gate | bbb2222 against base1; earlier run: aaa1111 against base1 |"
        ) in text

    def test_refuses_a_file_that_cannot_be_written_or_read(self, tmp_path):
        with pytest.raises(gate.Refused, match="could not be written"):
            gate.write_gate_file(str(tmp_path / "no-such-item"), "aaa1111", "base1")
        (tmp_path / "broad-gate.md").write_bytes(b"\xff\xfe")
        with pytest.raises(gate.Refused, match="could not be read"):
            gate.write_gate_file(str(tmp_path), "aaa1111", "base1")


# The table the old generator's records carried, which the check's reader
# refuses.
OLD_RECORD = (
    "# r — review round 1\n\n## Verdicts\n\n"
    "| # | Finding | Location | Verdict | Grounds |\n|---|---|---|---|---|\n"
    "| 1 | x | `a:1` | deferred #9 | g |\n"
)


class Test_rounds_rows:
    def test_accepts_the_count_and_every_records_deferred_homes(self, tmp_path):
        """`deferred` is counted through the check's reader, so a record it
        refuses adds nothing beneath `rounds`, and the records it reads add
        every home they name."""
        item = tmp_path / "1799000002-x"
        write(item, "rounds/round-1.md", a_round("deferred #7", "fixed abc1234"))
        write(item, "rounds/round-2.md", a_round("deferred #8"))
        write(item, "rounds/round-3.md", a_round("deferred #9", "deferred"))
        write(item, "rounds/round-4.md", a_round("**deferred** #9"))
        write(item, "rounds/round-5.md", OLD_RECORD)
        write(
            item, "rounds/round-6.md", a_round("deferred #9").replace("verdict:", "V:")
        )
        rows = gate.rounds_rows(str(item))
        assert rows == [("rounds", "6"), ("", "2 deferred → #7, #8")], rows

    def test_refuses_a_deferral_row_where_nothing_was_deferred(self, tmp_path):
        item = tmp_path / "1799000003-y"
        assert gate.rounds_rows(str(item)) == [("rounds", "0")]
        write(item, "rounds/round-1.md", a_round("fixed abc1234"))
        assert gate.rounds_rows(str(item)) == [("rounds", "1")]


def checks(suite=0, chain_code=0):
    return {
        gate.SUITE: gate.Check(gate.SUITE, suite, "", "/k/suite.txt"),
        gate.CHAIN_NAME: gate.Check(gate.CHAIN_NAME, chain_code, "", "/k/chain.txt"),
    }


class Test_panel:
    def test_accepts_a_run_with_counts_a_branch_and_a_ref(self, tmp_path):
        base = gate.Base("base", "aaa1111", "origin/base", "bbb2222")
        run = a_record(sessions=1, counts={"passed": 3, "skipped": 1})
        rows = gate.panel("ccc3333", base, checks(), None, branch="feature", run=run)
        assert rows == [
            ("tree", "ccc3333"),
            ("", "feature"),
            ("base", "bbb2222  origin/base"),
            None,
            ("suite", "✓ 3 passed · 1 skipped"),
            ("chain", "✓ exit 0"),
        ]

    def test_accepts_the_item_the_gate_row_and_what_ci_also_asks(self, tmp_path):
        base = gate.Base("main", "aaa1111", "main", "aaa1111")
        item = tmp_path / "1799000005-z"
        item.mkdir()
        rows = gate.panel("c", base, checks(), str(item), WORKFLOW, "tree 1.0")
        assert ("item", "1799000005") in rows
        assert ("gate", "tree 1.0") in rows
        assert ("CI also", "· 3 more steps") in rows
        assert rows[-1] == ("rounds", "0")

    def test_refuses_to_print_a_ref_that_is_the_commit_or_counts_it_has_not(self):
        base = gate.Base("aaa1111", "aaa1111", "aaa1111", "aaa1111")
        rows = gate.panel("c", base, checks(suite=0), None, run=None)
        assert ("base", "aaa1111") in rows
        assert ("suite", "exit 0") in rows
        assert not any(
            row and row[0] in ("", "item", "gate", "CI also") for row in rows
        )

    def test_refuses_a_value_wider_than_the_frame_and_continues_a_list(self):
        width = stamp.PANEL_VALUE_WIDTH
        long_ref = "origin/" + "r" * 60
        base = gate.Base("x", "aaa1111", long_ref, "bbb2222")
        counts = {name: 1000 for name in ("failed", "passed", "skipped", "xfailed")}
        rows = gate.panel(
            "t" * 50,
            base,
            checks(),
            None,
            branch="b" * 60,
            run=a_record(sessions=1, counts=counts),
        )
        assert all(row is None or len(row[1]) <= width for row in rows), rows
        assert ("", "b" * (width - 3) + "...") in rows
        ((_, based),) = [row for row in rows if row and row[0] == "base"]
        assert based.startswith("bbb2222  ...") and based.endswith("rrr")
        suite = [row for row in rows if row and row[0] in ("suite", "")][1:]
        assert suite[0][1].startswith("✓ 1000 failed")
        assert suite[1][0] == "" and suite[1][1].endswith("1000 xfailed")
        assert long_ref.startswith("origin/") and len(based) == width


class Test_failure_lines:
    def test_accepts_a_failing_suite_compared_at_the_base_with_its_counts(self):
        check = gate.Check(gate.SUITE, 1, "first\nsecond\n", "/k/suite.txt")
        record = a_record(sessions=1, counts={"failed": 1}, unended=2)
        lines = gate.failure_lines(check, {"t/a.py": gate.NEW}, record)
        assert lines[:4] == ["exit 1", "first", "second", gate.COMPARED_AT_BASE]
        assert lines[4] == "  t/a.py  new"
        assert lines[5] == gate.UNENDED_HERE.format(count=2)
        assert lines[-2:] == ["1 failed", "full output: /k/suite.txt"]

    def test_refuses_to_call_files_compared_where_no_record_was_left(self):
        check = gate.Check(gate.SUITE, 1, "", "/k/suite.txt")
        lines = gate.failure_lines(check, {"t/a.py": gate.NO_RECORD_AT_HEAD}, None)
        assert gate.NAMED_BY_FAILED_LINES in lines
        assert gate.COMPARED_AT_BASE not in lines
        assert lines[-2] == gate.NO_RECORD_HERE
        lost = gate.failure_lines(check, {"t/a.py": gate.NOT_CHECKED_OUT}, a_record())
        assert gate.BASE_NOT_CHECKED_OUT in lost

    def test_refuses_counts_for_a_record_that_passed_lines_over(self):
        check = gate.Check(gate.SUITE, 1, "", "/k/suite.txt")
        record = a_record(sessions=1, counts={"failed": 1}, unread=1, unplaced=2)
        lines = gate.failure_lines(check, None, record)
        assert gate.UNPLACED.format(count=2) in lines
        assert gate.UNREAD_HERE.format(count=1) in lines
        assert "1 failed" not in lines


class Test_failed_form:
    def test_accepts_each_failure_under_one_head(self):
        form = gate.failed_form("ccc", "aaa", [("suite", ["x", "y"])], "feat", "base")
        assert form == [
            "BROAD GATE FAILED   feat @ ccc against base @ aaa",
            "",
            "  suite    x",
            "           y",
        ]

    def test_refuses_to_set_a_long_name_a_column_out(self):
        form = gate.failed_form("c", "a", [("unverified", ["u"]), ("suite", [])])
        assert form[2:] == ["  unverified u", "  suite      (no output)"]


class Test_report_lines:
    def test_accepts_the_rows_as_padded_text(self):
        lines = gate.report_lines([("tree", "c"), None, ("suite", "✓ 1 passed")])
        assert lines == ["tree    c", "", "suite   ✓ 1 passed"]

    def test_refuses_the_owners_marks_where_ascii_is_asked(self):
        lines = gate.report_lines([("suite", "✓ 1 · 2 → x")], ascii_marks=True)
        assert lines == ["suite   + 1 . 2 > x"]


# --- the run, over a fixture repository ---------------------------------------------


@pytest.fixture(scope="module")
def _repo_template(tmp_path_factory):
    """A repository on `base` with a one-test suite, the config row and an
    overview, then `feature` one commit ahead; built once, and copied for each
    case by `tests/conftest.py#repo`."""
    d = tmp_path_factory.mktemp("gate-template") / "repo"
    d.mkdir()
    git(d, "init", "-q", "-b", "base")
    write(d, "tests/test_one.py", PASSING_TEST)
    write(d, "seal/config.md", config_of())
    write(d, f"{ITEM}/overview.md", OVERVIEW)
    commit(d, "base")
    git(d, "switch", "-qc", "feature")
    write(d, "README.md", "# a fixture\n")
    commit(d, "feature")
    return d


def failing_on_feature(repo, on_base=False):
    """A failing `tests/test_two.py` on `feature`, and on `base` too where
    ON_BASE, committed in both."""
    if on_base:
        git(repo, "switch", "-q", "base")
        write(repo, "tests/test_two.py", FAILING_TEST)
        commit(repo, "a failure on the base")
        git(repo, "switch", "-q", "feature")
        git(
            repo,
            "-c",
            "user.email=e@example.com",
            "-c",
            "user.name=e",
            "merge",
            "-q",
            "--no-edit",
            "base",
        )
    else:
        write(repo, "tests/test_two.py", FAILING_TEST)
        commit(repo, "a failure")
    return repo


def args_for(repo, keep, *extra):
    return ["--base", "base", "--root", str(repo), "--keep-output", str(keep), *extra]


def namespace(repo, keep, base="base", record=None, preflight=False):
    return argparse.Namespace(
        root=str(repo),
        base=base,
        record=record,
        preflight=preflight,
        keep_output=str(keep),
        shape=True,
    )


class Test_compare_at_base:
    def test_accepts_a_file_the_base_never_had_as_new(self, repo, tmp_path):
        failing_on_feature(repo)
        words = gate.compare_at_base(
            str(repo), "base", SUITE_ROW, ["tests/test_two.py"], str(tmp_path)
        )
        assert words == {"tests/test_two.py": gate.NEW}
        assert (tmp_path / "suite-at-base.txt").is_file()
        assert len(git_out(repo, "worktree", "list").splitlines()) == 1

    def test_accepts_a_file_the_base_fails_too(self, repo, tmp_path):
        failing_on_feature(repo, on_base=True)
        words = gate.compare_at_base(
            str(repo), "base", SUITE_ROW, ["tests/test_two.py"], str(tmp_path)
        )
        assert words == {"tests/test_two.py": gate.ON_BASE}

    def test_refuses_to_compare_at_a_base_that_cannot_be_checked_out(
        self, repo, tmp_path
    ):
        words = gate.compare_at_base(
            str(repo), "0" * 40, SUITE_ROW, ["a.py", "b.py"], str(tmp_path)
        )
        assert words == {"a.py": gate.NOT_CHECKED_OUT, "b.py": gate.NOT_CHECKED_OUT}


class Test_uncommitted_line:
    def test_accepts_a_written_file_git_sees_uncommitted(self, repo):
        path = gate.write_gate_file(str(repo / ITEM), "c", "b")
        assert gate.uncommitted_line(str(repo), path) == gate.CELL_UNCOMMITTED.format(
            path=f"{ITEM}/broad-gate.md"
        )

    def test_refuses_a_committed_file_and_no_file(self, repo):
        path = gate.write_gate_file(str(repo / ITEM), "c", "b")
        commit(repo, "the record")
        assert gate.uncommitted_line(str(repo), path) is None
        assert gate.uncommitted_line(str(repo), None) is None


@pytest.fixture(scope="module")
def a_recorded_run(tmp_path_factory, _repo_template):
    """One green run through `--record`, started as a person starts it, read
    by the cases that only read what it printed and kept. Under a directory
    whose name holds a space, so the paths it prints are read with one."""
    scratch = tmp_path_factory.mktemp("recorded")
    repo = scratch / "a checkout" / "repo"
    shutil.copytree(_repo_template, repo)
    keep = scratch / "out"
    out = subprocess.run(
        [
            sys.executable,
            str(ROOT / TARGET),
            *args_for(repo, keep, "--record", str(repo / ITEM)),
        ],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=300,
        env={**clean_env(), "PYTHONIOENCODING": "utf-8"},
    )
    return repo, keep, out


class Test_gate:
    def test_accepts_a_green_tree_and_runs_every_check_in_order(self, a_recorded_run):
        repo, keep, out = a_recorded_run
        assert out.returncode == 0, out.stdout + out.stderr
        tree, base = short(repo, "HEAD"), short(repo, "base")
        lines = out.stdout.splitlines()
        assert lines[0] == f"BROAD GATE PASSED   feature @ {tree} against base @ {base}"
        assert lines[1:4] == [
            f"tree    {tree}",
            "        feature",
            f"base    {base}  base",
        ]
        assert "suite   ✓ 1 passed" in lines
        assert lines[-1] == gate.CELL_UNCOMMITTED.format(path=f"{ITEM}/broad-gate.md")
        for name in ("suite", "unverified", "chain", "mode"):
            assert (keep / f"{name}.txt").is_file(), name
        chain_kept = (keep / "chain.txt").read_text(encoding="utf-8")
        assert f"--baseline {base} --root" in chain_kept.splitlines()[0]
        unverified_kept = (keep / "unverified.txt").read_text(encoding="utf-8")
        assert f"--baseline {base} " in unverified_kept.splitlines()[0]
        # The gate draws nothing and queues no stamp (#975).
        assert not (repo / ".git" / "specseal-stamp").exists()
        cell = (repo / ITEM / "broad-gate.md").read_text(encoding="utf-8")
        assert f"| {ROW} | {tree} against {base} |" in cell
        assert f"broad-gate: `{ROW}` says: {SUITE_ROW}" in out.stderr

    def test_accepts_a_failure_the_base_shares_as_failing_on_base_too(
        self, repo, tmp_path, capsys
    ):
        failing_on_feature(repo, on_base=True)
        assert gate.gate(namespace(repo, tmp_path / "out")) == 1
        out = capsys.readouterr().out
        assert out.startswith("BROAD GATE FAILED   feature @ ")
        assert "  tests/test_two.py  failing on base too" in out

    def test_refuses_a_failing_test_the_base_lacks_as_new(self, repo, tmp_path, capsys):
        failing_on_feature(repo)
        assert gate.gate(namespace(repo, tmp_path / "out")) == 1
        out = capsys.readouterr().out
        assert "  tests/test_two.py  new\n" in out
        assert "1 failed, 1 passed" in out
        assert not (repo / ITEM / "broad-gate.md").exists()

    def test_accepts_a_preflight_that_runs_no_row_and_writes_nothing(
        self, repo, tmp_path, capsys
    ):
        keep = tmp_path / "out"
        assert gate.gate(namespace(repo, keep, preflight=True)) == 0
        captured = capsys.readouterr()
        assert captured.out.startswith("PREFLIGHT PASSED   ")
        assert gate.PREFLIGHT_TAIL in captured.out
        assert gate.ROW_NOT_RUN in captured.err
        assert not (keep / "suite.txt").exists()
        assert (keep / "chain.txt").is_file()

    def test_refuses_a_preflight_with_a_record(self, repo, tmp_path):
        with pytest.raises(gate.Refused) as said:
            gate.gate(
                namespace(repo, tmp_path, record=str(repo / ITEM), preflight=True)
            )
        assert str(said.value) == gate.PREFLIGHT_RECORD

    @pytest.mark.parametrize(
        ("config", "said"),
        [
            (config_of(None), "has no `Broad gate` row"),
            (config_of(f"`{SUITE_ROW}`"), "is the whole command wrapped in backticks"),
        ],
        ids=["no-row", "wrapped-row"],
    )
    def test_refuses_a_row_it_cannot_run_and_runs_nothing(
        self, repo, tmp_path, config, said
    ):
        write(repo, "seal/config.md", config)
        keep = tmp_path / "out"
        with pytest.raises(gate.Refused, match=said):
            gate.gate(namespace(repo, keep))
        assert not keep.exists()

    def test_refuses_a_base_that_does_not_resolve(self, repo, tmp_path):
        with pytest.raises(gate.Refused, match="--base nowhere does not resolve"):
            gate.gate(namespace(repo, tmp_path / "out", base="nowhere"))

    def test_refuses_a_root_that_is_no_repository_or_not_opted_in(self, tmp_path):
        with pytest.raises(gate.Refused, match="is not in a git repository"):
            gate.gate(namespace(tmp_path, tmp_path / "out"))
        git(tmp_path, "init", "-q")
        with pytest.raises(gate.Refused, match="has no seal/ at either place"):
            gate.gate(namespace(tmp_path, tmp_path / "out"))


class Test_main:
    def test_accepts_the_trees_own_copy_with_the_same_arguments(self, repo, tmp_path):
        stub = "import sys\nprint('STUB GATE RAN', sys.argv[1:])\nsys.exit(3)\n"
        write(repo, gate.GATE_REL, stub)
        out = subprocess.run(
            [sys.executable, str(ROOT / TARGET), *args_for(repo, tmp_path, "--x")],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
            env=clean_env(),
        )
        assert out.returncode == 3
        assert "STUB GATE RAN" in out.stdout and "'--x'" in out.stdout
        assert f"broad-gate: {repo} ships its own gate; running" in out.stderr

    def test_refuses_to_leave_the_invoked_path_for_a_check_to_read(
        self, tmp_path, monkeypatch, capsys
    ):
        git(tmp_path, "init", "-q")
        monkeypatch.setenv(gate.INVOKED_AS_VAR, "/somewhere/broad_gate.py")
        assert gate.main(["--base", "base", "--root", str(tmp_path)]) == 2
        assert gate.INVOKED_AS_VAR not in os.environ
        err = capsys.readouterr().err
        assert f"broad-gate: gate {os.path.realpath(ROOT / TARGET)} (plugin " in err

    def test_refuses_a_copy_whose_sibling_will_not_load(self, tmp_path):
        scripts = tmp_path / "plugin" / "skills" / "verify" / "scripts"
        scripts.mkdir(parents=True)
        shutil.copy(ROOT / TARGET, scripts / "broad_gate.py")
        write(scripts, "seal_stamp.py", "raise ValueError('the mark chart is bad')\n")
        keep = tmp_path / "out"
        out = subprocess.run(
            [
                sys.executable,
                str(scripts / "broad_gate.py"),
                "--base",
                "x",
                "--keep-output",
                str(keep),
            ],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
            cwd=tmp_path,
        )
        assert out.returncode == 2
        assert "will not load, so nothing ran: the mark chart is bad" in out.stderr
        assert "Traceback" not in out.stderr and not keep.exists()

    def test_refuses_to_run_when_called_in_process_beside_a_broken_sibling(
        self, tmp_path, monkeypatch, capsys
    ):
        write(tmp_path, "seal_stamp.py", "raise ValueError('the chart is short')\n")
        monkeypatch.setattr(gate, "STAMP", str(tmp_path / "seal_stamp.py"))
        assert gate.main(["--base", "x", "--root", str(ROOT)]) == 2
        captured = capsys.readouterr()
        assert "will not load, so nothing ran: the chart is short" in captured.err
        assert "ships its own gate" not in captured.err

    def test_accepts_the_command_a_person_types(self):
        wrapper = ROOT / "bin" / "broad-gate"
        command = (
            [os.environ.get("COMSPEC", "cmd.exe"), "/c", f"{wrapper}.cmd", "--help"]
            if os.name == "nt"
            else [str(wrapper), "--help"]
        )
        out = subprocess.run(
            command,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
        assert out.returncode == 0, out.stderr
        assert out.stdout.startswith("usage: broad-gate")


test_census = census_case(TARGET)
