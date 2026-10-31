"""`skills/verify/scripts/broad_gate.py`, one class per function.

Rebuilt from the code by #942's phase 5. The pure units are driven with text,
hand-built records and an `is_directory` answer, so no git and no shell runs
under them. Git runs where the unit asks git a question: the base's
resolution over one repository built once for the module, and the base
comparison and the gate's own run over a fixture repository built once and
copied for each case. Those cases run the fixture's one-test suite through
the gate's recorder, one row per kind of answer, and each copy is the reset.

Phase 6 placed the light files' cases here as they stood. The cases of
`run` and `handed_to_shell` that came from the file on what `cmd.exe` is
handed (#448, #596) drive the Windows half with the platform passed in as an
argument; two of them run the machine's real shell, and only CI's
`windows-latest` leg runs its `cmd.exe` path. The cases of `main` that came
from the file on the steps CI runs (#468) each build a repository with a
`feature` branch and run the command over it.
"""

import argparse
import ast
import json
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys

import conftest
import pytest
from conftest import (
    census_case,
    git,
    git_out,
    load_module,
    mark_root,
    read,
    symlink_or_skip,
    write,
)
from conftest import commit_everything_as_e as commit

TARGET = "skills/verify/scripts/broad_gate.py"

ROOT = pathlib.Path(conftest.ROOT)
CHAIN = ROOT / "skills" / "code-review" / "scripts" / "chain_check.py"
READER = ROOT / "skills" / "verify" / "scripts" / "unverified_check.py"
ITEM = "seal/threads/1799000001-a-gated-work-item"
# The record's path as the gate prints it: `os.path.relpath`, so with the
# platform's separator.
RECORD_REL = os.path.join(ITEM, "trail", "gate.md").replace("/", os.sep)
ROW = "Broad gate"

gate = load_module(ROOT / TARGET, "broad_gate_under_test")
chain = load_module(CHAIN, "chain_check_beside_broad_gate")
stamp = gate.stamp_module()
GATE = str(ROOT / TARGET)
STAMP = str(ROOT / "skills" / "verify" / "scripts" / "seal_stamp.py")
HYGIENE = str(ROOT / ".github" / "workflows" / "hygiene.yml")


def gate_module():
    """A fresh load of the gate, for the cases that load their own."""
    return load_module(GATE, "agentic_broad_gate_for_cmd")


PASSING_TEST = "def test_one():\n    assert True\n"
FAILING_TEST = "def test_two():\n    assert False, 'planted'\n"
SUITE_ROW = f"{sys.executable} -m pytest -q -p no:cacheprovider tests"
OVERVIEW = (
    "# overview\n\n## Not verified\n\n- nothing\n  why: the fixture verifies nothing\n"
)
# The live session's id. The conftest clears it before each case, and a
# fixture scoped to the module, such as `a_recorded_run`, starts the gate
# before that, so `clean_env` leaves it out of the gate's environment. No
# `GITHUB_` variable is listed: the conftest removes them all at import.
AMBIENT = ("CLAUDE_CODE_SESSION_ID",)


def config_of(row=SUITE_ROW, before="", after=""):
    """A `seal/config.md` with the `Broad gate` row ROW, or none where ROW is
    None, with BEFORE and AFTER around its table."""
    text = before + "| Item | Value |\n|---|---|\n| Mode | shared |\n"
    if row is not None:
        text += f"| {ROW} | {row} |\n"
    return text + after


def home_with(tmp_path, text):
    """A `seal/` root holding TEXT as its `config.md`; its path."""
    write(tmp_path, "seal/config.md", text)
    return str(mark_root(tmp_path / "seal"))


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
    "      - name: a declared review chain has the round record it claimed\n"
    "      - name: 'a change to what ships must move the version'\n"
    "      - name: both READMEs move together\n"
    "      - name: a step nobody classified\n"
)


def clean_env():
    return {k: v for k, v in os.environ.items() if k not in AMBIENT}


def gate_function():
    """`gate()`, as a syntax tree.

    Read as a tree rather than as text: the claim is about which checks the
    gate RUNS, and a substring search cannot tell a call from a mention of
    one in a docstring or a comment.
    """
    parsed = ast.parse(read(GATE))
    found = [
        node
        for node in ast.walk(parsed)
        if isinstance(node, ast.FunctionDef) and node.name == "gate"
    ]
    assert len(found) == 1, f"broad_gate.py has {len(found)} functions named gate"
    return found[0]


def arms_the_gate_runs():
    """The check name each `checks[...] = run(...)` in `gate()` records.

    The key is read as source rather than resolved, so `checks[CHAIN_NAME]`
    comes back as the constant's NAME — which is what the partition holds too,
    because a row names the arm by the same constant.
    """
    names = []
    for node in ast.walk(gate_function()):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if not isinstance(target, ast.Subscript):
                continue
            if ast.unparse(target.value) != "checks":
                continue
            call = node.value
            ran = isinstance(call, ast.Call) and ast.unparse(call.func) == "run"
            if ran:
                names.append(ast.unparse(target.slice))
    return names


def reasons():
    """`PARTITION`'s written reasons, by step; the file on the steps CI runs
    imports it for the count of the steps with a local answer."""
    return [(name, reason) for name, _, reason in gate.PARTITION if reason]


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

    def test_the_gate_and_the_check_spell_the_file_and_flag_alike(self):
        assert gate.GATE_FILE == chain.BROAD_GATE_FILE
        assert gate.CHAIN_SEALING == chain.SEALING

    def test_a_file_the_gate_wrote_is_read_by_the_check(self, tmp_path):
        """#1198, *Scope* item 2: the run block the gate appends is the one
        `chain_check.py#broad_gate` reads, through the same reader."""
        path = gate.write_gate_file(str(tmp_path), "abc1234", "def5678")
        text = pathlib.Path(path).read_text(encoding="utf-8")
        found = chain.FIELDS.read(text, chain.FIELDS.GATE)
        assert (found.refusals, found.notices) == ([], [])
        (run,) = found.blocks
        assert run.fields[chain.FIELDS.RUN].match["commit"] == "abc1234"

    def test_the_one_shell_site_is_run_and_it_applies_the_rewrite(self):
        """A2, the class by construction. `broad_gate.py` has exactly one call
        passing `shell=`, it is inside `run`, and the string it is handed is the
        one `handed_to_shell` produced. `gate`'s `SUITE` and `compare_at_base`'s
        `suite-at-base` both reach a shell through it, so a third shell site
        written anywhere else turns this red rather than going unrewritten."""
        with open(GATE, encoding="utf-8") as handle:
            tree = ast.parse(handle.read())
        sites, callers = [], []
        for fn in ast.walk(tree):
            if not isinstance(fn, ast.FunctionDef):
                continue
            for node in ast.walk(fn):
                if not isinstance(node, ast.Call) or not any(
                    kw.arg == "shell" for kw in node.keywords
                ):
                    continue
                func = node.func
                if (
                    isinstance(func, ast.Attribute)
                    and isinstance(func.value, ast.Name)
                    and func.value.id == "subprocess"
                ):
                    sites.append((fn.name, node))
                elif isinstance(func, ast.Name) and func.id == "run":
                    callers.append(fn.name)
        names = [name for name, _ in sites]
        assert names == ["run"], f"`subprocess` calls passing `shell=` are in: {names}"
        # The two callers the spec enumerates, and a third is a change to read.
        assert sorted(callers) == ["compare_at_base", "gate"], callers
        run_fn = next(
            fn
            for fn in tree.body
            if isinstance(fn, ast.FunctionDef) and fn.name == "run"
        )
        call = sites[0][1]
        assert call.args and isinstance(call.args[0], ast.Name), ast.dump(call)
        handed = call.args[0].id
        assigned_from_rewrite = [
            node
            for node in ast.walk(run_fn)
            if isinstance(node, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == handed for t in node.targets)
            and any(
                isinstance(inner, ast.Call)
                and isinstance(inner.func, ast.Name)
                and inner.func.id == "handed_to_shell"
                for inner in ast.walk(node.value)
            )
        ]
        assert assigned_from_rewrite, (
            f"`run` hands the shell `{handed}`, and nothing in `run` assigns it "
            "from `handed_to_shell`"
        )

    def test_the_partition_names_each_step_once(self):
        """Two rows for one step is two answers to one question, and the second
        is unreachable — whichever way a reader resolves it, the count of what the
        seal did not answer is wrong by one."""
        names = [name for name, _, _ in gate.PARTITION]
        twice = sorted({name for name in names if names.count(name) > 1})
        assert not twice, f"these steps carry more than one row: {twice}"

    def test_a_row_is_an_arm_or_a_reason_and_never_both_or_neither(self):
        """The partition's shape, which A1 and A2 assume and neither asserts. A
        row with both says a step is mirrored AND excluded; a row with neither is
        the silence written down."""
        broken = [
            (name, arm, reason)
            for name, arm, reason in gate.PARTITION
            if bool(arm) == bool(reason)
        ]
        assert not broken, (
            f"these rows are neither mirrored nor excluded, or claim to be both: {broken}"
        )

    def test_every_arm_the_partition_names_is_an_arm_the_gate_runs(self):
        """A3. Red when an arm is deleted from `gate()` while its partition row
        stands — the row would then say a step is mirrored by nothing.

        The partition holds the arm's VALUE (`"chain"`) and `gate()` subscripts
        `checks` by the constant's NAME (`CHAIN_NAME`), so the two are joined
        through the module: a constant renamed in one place and not the other is
        red here rather than quiet."""
        ran = arms_the_gate_runs()
        assert ran, "gate() records no check at all"
        values = {}
        for name in ran:
            assert hasattr(gate, name), (
                f"gate() records `checks[{name}]` and broad_gate.py has no such constant"
            )
            values[getattr(gate, name)] = name
        missing = sorted(
            {arm for _, arm, _ in gate.PARTITION if arm and arm not in values}
        )
        assert not missing, (
            f"`PARTITION` says these arms mirror a step of the workflow and "
            f"`gate()` runs no check by those names: {missing}. The arms it does "
            f"run are {sorted(values)}"
        )

    def test_the_gate_runs_no_arm_the_partition_does_not_account_for(self):
        """A3's other side. An arm the gate runs and the partition never names is
        an arm nobody can say which step it stands for — the `suite` arm aside,
        which answers no step of this job at all: it is the repository's own
        command from the `Broad gate` row of `seal/config.md`."""
        answering_no_release_step = {gate.SUITE}
        named = {arm for _, arm, _ in gate.PARTITION if arm}
        loose = sorted(
            getattr(gate, name)
            for name in arms_the_gate_runs()
            if getattr(gate, name) not in named | answering_no_release_step
        )
        assert not loose, (
            f"`gate()` runs these arms and no partition row names them: {loose}. "
            "An arm belongs to a step of the `release` job, or it answers "
            "something outside that job — the repository's own command, or a job "
            "of another workflow — and belongs in the set above"
        )

    def test_every_exclusion_carries_prose_rather_than_a_category(self):
        """A4. Red against a reason cell reduced to a category word.

        `EXCLUDED` tells the next reader nothing, and the reason is the whole
        value of the row — it is what a person checks when they wonder whether
        the seal covers them. Two structural rules stand in for that judgment: a
        reason is several words, and it is written in the prose case rather than
        as a marker.

        **What this cannot catch is a category in prose clothing.** *not
        applicable here* passes every rule below and says as little as
        `EXCLUDED`. Only a reader catches that one, and `plan.md` *The failure
        scenario at six months* is where it is written down as an open hole
        rather than a closed one.
        """
        thin = [
            (name, reason)
            for name, reason in reasons()
            if len(reason.split()) < 3 or reason == reason.upper()
        ]
        assert not thin, (
            f"these rows give a marker where a reason belongs: {thin}. A reason "
            "is prose somebody wrote — `needs the pull request's body` is one, "
            "`EXCLUDED` is not"
        )

    def test_every_exclusion_says_what_the_gate_cannot_reach(self):
        """A4's second half. A reason that never names the thing out of reach is
        a sentence rather than a reason — it reads as prose and answers nothing.

        Held loosely on purpose: the vocabulary below is what the four kinds of
        unreachable thing are called in this repository, and a fifth kind is a
        word to add here rather than a case to delete."""
        out_of_reach = (
            "pull request",
            "tracker",
            "fetch",
            "network",
            "never fails",
            "warning",
            ".github/scripts/",
            "inline",
            "second reading",
            "second implementation",
        )
        silent = [
            name
            for name, reason in reasons()
            if not any(word in reason for word in out_of_reach)
        ]
        assert not silent, (
            f"these rows give a reason that names nothing out of the gate's "
            f"reach: {silent}. Say what the gate cannot get at — the pull "
            "request, the tracker, a fetch, a step that only warns, or a check "
            "this repository owns rather than the plugin"
        )


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
            f"seal gate: --base solo is {base.given_commit} in this checkout; CI "
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
            "seal gate: --base gone names no commit in this checkout; CI reads"
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
        mark_root(tmp_path / "shared" / "seal")
        assert gate.seal_home(str(tmp_path / "shared")) == str(
            tmp_path / "shared" / "seal"
        )
        local = tmp_path / "local"
        local.mkdir()
        git(local, "init", "-q")
        (local / "seal").mkdir()
        mark_root(local / ".git" / "seal")
        assert gate.seal_home(str(local)) == os.path.normpath(
            str(local / ".git" / "seal")
        )

    def test_refuses_a_repository_with_neither(self, tmp_path):
        """No `seal/` at all, and a `seal/` the project keeps for itself,
        whose README does not open with the marker, are no root to read a
        command from."""
        git(tmp_path, "init", "-q")
        assert gate.seal_home(str(tmp_path)) is None
        write(tmp_path, "seal/config.md", config_of("bin/test -q"))
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
        mark_root(tmp_path / "seal")
        (tmp_path / "seal" / "config.md").write_bytes(b"| Item | Value |\n\xff\xfe\n")
        with pytest.raises(gate.Refused, match=r"^seal gate: .*Nothing ran$"):
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

    def test_refuses_a_row_the_walk_read_above_the_line_it_refused(self, tmp_path):
        """A row the walk read is `broad_command`'s to answer, an empty value
        included. A line the walker refused below it does not make that row
        one the walk never reached."""
        home = home_with(tmp_path, config_of("") + "| Odd | a | b |\n")
        assert gate.refused_broad_row(home) is None


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

    def test_refuses_to_blame_a_fence_left_open_below_the_fenced_row(self, tmp_path):
        """The fence that swallows a row is one opened above it. A fence opened
        further down and never closed leaves the row in a block that closes,
        and moving the row is still the act."""
        said = gate.missing_row(home_with(tmp_path, FENCED + "\n```\nopen\n"))
        assert "Move the row into the `| Item | Value |` table" in said
        assert "never closed" not in said

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

CMD = r"C:\Windows\System32\cmd.exe"
CMD_ROW = "bin/test -q && uvx ruff check . && uvx ruff format --check ."
HANDED = r"bin\test -q && uvx ruff check . && uvx ruff format --check ."

# Every directory a row in this module starts a command name in. A name is
# rewritten only where it starts in a directory that exists where the row
# runs (#596), so each case says where that is rather than leaning on
# whatever pytest's working directory happens to hold.
DIRECTORIES = ("bin", "tools", "x")


@pytest.fixture
def tree(tmp_path):
    root = tmp_path / "tree"
    for name in DIRECTORIES:
        (root / name).mkdir(parents=True)
    return str(root)


def only_slashes_turned(row, got):
    """A3. Every character but `/` → `\\` stays where it was."""
    assert len(got) == len(row)
    moved = [(a, b) for a, b in zip(row, got, strict=True) if a != b]
    assert all(pair == ("/", "\\") for pair in moved), moved


class _Ran:
    """A stand-in for `subprocess.run` that records what it was handed."""

    def __init__(self):
        self.handed = []

    def __call__(self, args, **kwargs):
        self.handed.append((args, kwargs.get("shell")))
        return subprocess.CompletedProcess(args, 0, "1 passed in 0.01s\n", "")


def runs_under_cmd_exe(gate, repo):
    """Whether this machine's shell is `cmd.exe`, read from what the gate
    would hand it. `repo` holds `bin/`, so the probe's answer does not rest
    on what pytest's working directory happens to hold (#596)."""
    return gate.handed_to_shell("bin/probe", root=str(repo)) != "bin/probe"


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
        assert "seal gate: suite — cmd.exe reads a `/`" in capsys.readouterr().err

    def test_a_rewritten_row_is_kept_and_said_beside_the_row_as_written(
        self, tree, tmp_path, monkeypatch, capsys
    ):
        """A3. The shell is handed `bin\\test`; the kept file's first line is the
        row as written and its second is what `cmd.exe` was handed; and one
        stderr line, pinned verbatim here (contract rule 14), says the same before the run.
        `run` asks about the directory where the row runs, its own `root`."""
        gate = gate_module()
        ran = _Ran()
        monkeypatch.setattr(gate.subprocess, "run", ran)
        check = gate.run(
            "suite",
            CMD_ROW,
            tree,
            str(tmp_path),
            shell=True,
            windows=True,
            comspec=CMD,
        )
        assert ran.handed == [(HANDED, True)], ran.handed
        kept = (tmp_path / "suite.txt").read_text(encoding="utf-8").splitlines()
        assert kept[:3] == [
            f"$ {CMD_ROW}",
            f"cmd.exe was handed: {HANDED}",
            "exit 0",
        ], kept
        assert capsys.readouterr().err == (
            "seal gate: suite — cmd.exe reads a `/` in a command name as the start "
            "of a switch, so a command name that starts in a directory has its `/` "
            f"handed to it as `\\`: {HANDED}\n"
        )
        assert check.code == 0

    def test_run_judges_the_directory_where_the_row_runs(self, tmp_path, monkeypatch):
        """A5. The same row, run from a root with no `bin/`, is handed over as
        written: `run` passes its own `root` on, and the directory is asked
        there and not in the caller's working directory."""
        gate = gate_module()
        ran = _Ran()
        monkeypatch.setattr(gate.subprocess, "run", ran)
        bare = tmp_path / "bare"
        bare.mkdir()
        gate.run(
            "suite",
            CMD_ROW,
            str(bare),
            str(tmp_path),
            shell=True,
            windows=True,
            comspec=CMD,
        )
        assert ran.handed == [(CMD_ROW, True)], ran.handed

    @pytest.mark.parametrize(
        "windows, comspec, row",
        [
            (False, None, CMD_ROW),
            (True, r"C:\Program Files\Git\bin\bash.exe", CMD_ROW),
            # Nothing to rewrite, so nothing changed, so nothing extra is said.
            (True, CMD, "uvx ruff check ."),
        ],
    )
    def test_a_row_handed_as_written_adds_nothing_to_the_record(
        self, tmp_path, monkeypatch, capsys, windows, comspec, row
    ):
        """A3, the other half. Where nothing was rewritten, the kept file is the
        shape it always was and nothing is printed."""
        gate = gate_module()
        ran = _Ran()
        monkeypatch.setattr(gate.subprocess, "run", ran)
        gate.run(
            "suite",
            row,
            str(tmp_path),
            str(tmp_path),
            shell=True,
            windows=windows,
            comspec=comspec,
        )
        assert ran.handed == [(row, True)], ran.handed
        kept = (tmp_path / "suite.txt").read_text(encoding="utf-8").splitlines()
        assert kept[:2] == [f"$ {row}", "exit 0"], kept
        assert capsys.readouterr().err == ""

    def test_an_argv_check_is_never_rewritten(self, tmp_path, monkeypatch, capsys):
        """A3. The plugin's own checks are argv lists with `shell=False`, which
        reach `CreateProcess` directly and take no shell's reading; the rewrite is
        for shell strings only, whatever the platform."""
        gate = gate_module()
        ran = _Ran()
        monkeypatch.setattr(gate.subprocess, "run", ran)
        argv = [sys.executable, "tools/check.py"]
        gate.run(
            "ledger", argv, str(tmp_path), str(tmp_path), windows=True, comspec=CMD
        )
        assert ran.handed == [(argv, False)], ran.handed
        assert capsys.readouterr().err == ""

    def test_the_row_runs_on_the_real_platform(self, tmp_path):
        """A4. A fixture with the pair `bin/probe` (sh) and `bin/probe.cmd`, and
        the row `bin/probe`, run through the real shell of whatever machine this
        is. On macOS and ubuntu `sh` runs the POSIX half; only on
        `windows-latest` does `cmd.exe` run `bin\\probe` and resolve it to
        `bin\\probe.cmd`. Its red on Windows without the fix is #448's own
        measurement, not a run of this case."""
        gate = gate_module()
        repo = tmp_path / "repo"
        (repo / "bin").mkdir(parents=True)
        probe = repo / "bin" / "probe"
        probe.write_text("#!/bin/sh\necho probe ran under sh\n", encoding="utf-8")
        probe.chmod(probe.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        (repo / "bin" / "probe.cmd").write_text(
            "@echo probe ran under cmd\r\n", encoding="utf-8"
        )
        keep = tmp_path / "keep"
        keep.mkdir()
        check = gate.run("suite", "bin/probe", str(repo), str(keep), shell=True)
        kept = (keep / "suite.txt").read_text(encoding="utf-8")
        assert check.code == 0, kept
        under = "cmd" if runs_under_cmd_exe(gate, repo) else "sh"
        assert f"probe ran under {under}" in check.text, kept
        assert f"probe ran under {under}" in kept, kept

    def test_a_switch_against_a_program_runs_on_the_real_platform(self, tmp_path):
        """A6, #596. `where/q cmd` — a program that ships with Windows and is not
        one of `CMD_BUILTINS`, with a switch written straight against it —
        run through `run(..., shell=True)` from a root with no `where`
        directory, exits 0: `/q` prints nothing and `where` finds `cmd`. Only
        CI's `windows-latest` leg executes it; elsewhere the shell is not
        `cmd.exe` and the row means nothing there (`questions.md` M1)."""
        gate = gate_module()
        repo = tmp_path / "repo"
        (repo / "bin").mkdir(parents=True)
        if not runs_under_cmd_exe(gate, repo):
            # On Windows this case exists to run, and a skip there would let the
            # leg's green say nothing about M1: so it fails instead, and a pass on
            # `windows-latest` means it ran (round 2, M1).
            assert os.name != "nt", (
                "this is Windows and the shell the gate hands the row to is not "
                "cmd.exe, so the case cannot answer M1"
            )
            pytest.skip("the shell here is not cmd.exe")
        keep = tmp_path / "keep"
        keep.mkdir()
        row = "where/q cmd"
        assert gate.handed_to_shell(row, root=str(repo)) == row
        check = gate.run("suite", row, str(repo), str(keep), shell=True)
        kept = (keep / "suite.txt").read_text(encoding="utf-8")
        assert check.code == 0, kept


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

    @pytest.mark.parametrize(
        "windows, comspec, expected",
        [
            (True, CMD, HANDED),
            (True, "CMD.EXE", HANDED),
            (True, f'"{CMD}"', HANDED),
            # Unset and empty are what Python itself answers with `cmd.exe`.
            (True, "", HANDED),
            (True, r"C:\Program Files\Git\bin\bash.exe", CMD_ROW),
            (
                True,
                r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
                CMD_ROW,
            ),
            (False, CMD, CMD_ROW),
            (False, None, CMD_ROW),
        ],
    )
    def test_only_cmd_exe_on_windows_is_handed_the_backslashed_row(
        self, tree, windows, comspec, expected
    ):
        """A1. Windows and a `COMSPEC` naming `cmd.exe` get `bin\\test`; POSIX,
        and a Windows `COMSPEC` naming any other shell, get the row as written.
        Keyed on the shell rather than `os.name`, because a POSIX shell in
        `COMSPEC` runs `bin/test` as written."""
        gate = gate_module()
        got = gate.handed_to_shell(CMD_ROW, windows=windows, comspec=comspec, root=tree)
        assert got == expected, f"windows={windows} comspec={comspec!r}: {got!r}"

    def test_an_unset_comspec_on_windows_is_cmd_exe(self, tree, monkeypatch):
        """A1, the default. `subprocess` falls back to `cmd.exe` where `COMSPEC`
        is unset, so the rewrite must too — read from the environment when the
        argument is not given."""
        monkeypatch.delenv("COMSPEC", raising=False)
        gate = gate_module()
        assert gate.handed_to_shell(CMD_ROW, windows=True, root=tree) == HANDED

    @pytest.mark.parametrize(
        "row, expected",
        [
            (CMD_ROW, HANDED),
            # A runner handed quoted paths.
            ('bin/test "tests/x.py"', r'bin\test "tests/x.py"'),
            ("bin/test tests/a/b.py --out=dir/x", r"bin\test tests/a/b.py --out=dir/x"),
            ('"tools/run tests" -q "a/b"', r'"tools\run tests" -q "a/b"'),
            ("bin/test %OUT%/x & tools/lint", r"bin\test %OUT%/x & tools\lint"),
            ("bin/test ^& not/a/command", r"bin\test ^& not/a/command"),
            # An escaped character opens the command name it stands in, so the
            # word after the next blank is an argument and keeps its `/`: a
            # one-character name that is escaped is still the name.
            ("^a b/c", "^a b/c"),
            ('bin/test "a & b/c" && x/y', r'bin\test "a & b/c" && x\y'),
            ("(bin/a && bin/b) || bin/c", r"(bin\a && bin\b) || bin\c"),
            (
                "bin/test 2>&1 | tools/tee out/log.txt",
                r"bin\test 2>&1 | tools\tee out/log.txt",
            ),
            ("bin/test>out/log.txt", r"bin\test>out/log.txt"),
            ("bin/test<in/x.txt", r"bin\test<in/x.txt"),
            ("bin/test\tx/y", "bin\\test\tx/y"),
            ("@bin/test -q", r"@bin\test -q"),
            ("  bin/test", r"  bin\test"),
            ("echo a/b", "echo a/b"),
            ("echo (a/b)", "echo (a/b)"),
            ("echo(a/b)", "echo(a/b)"),
            ("cmd /c bin/x", "cmd /c bin/x"),
            # A `/` written against one of `cmd.exe`'s own commands is that
            # command's switch, which runs as written today.
            ("rd/s/q build && bin/test", r"rd/s/q build && bin\test"),
            ("@dir/b tests & bin/test", r"@dir/b tests & bin\test"),
            ("CD/D x && bin/test", r"CD/D x && bin\test"),
            ("echo/ && bin/test", r"echo/ && bin\test"),
            # The same after a separator: the built-in is the name that began there.
            ("bin/test && rd/s/q out", r"bin\test && rd/s/q out"),
            # A block that opens after `if`, `else` or `for … in` is not in
            # command position, which the template names as left as written.
            ("if exist x (bin/a) else (bin/b)", "if exist x (bin/a) else (bin/b)"),
            ("for %i in (x/y) do tools/x %i", "for %i in (x/y) do tools/x %i"),
            # Positions `templates/setup/config.md` names as not rewritten, pinned so
            # the gap stays the one it states.
            ("call bin/test", "call bin/test"),
            (">out.txt bin/test", ">out.txt bin/test"),
            # The redirection's target is not a command name, blank or not.
            ("> out/log.txt bin/test", "> out/log.txt bin/test"),
            # #596, the other side of the rows above: a name whose part before
            # its first `/` names no directory where the row runs.
            # A program with a switch written against it: no directory carries
            # the program's name, so the name and its switch reach `cmd.exe`.
            ("nothere/x -q", "nothere/x -q"),
            ('"nothere/run tests" -q', '"nothere/run tests" -q'),
            ("^nothere/x", "^nothere/x"),
            ("@nothere/x", "@nothere/x"),
            # Every leading `@` is dropped, as the built-in check drops them
            # (round 1, ⬜ 9).
            ("@@bin/test", r"@@bin\test"),
            # The same shapes, starting in a directory that exists.
            ("^bin/x", r"^bin\x"),
            ('@"tools/run tests"', r'@"tools\run tests"'),
            ('"bin"/x', r'"bin"\x'),
            # `.` and `..` are directories wherever the row runs.
            ("./bin/test", r".\bin\test"),
            ("../x/y", r"..\x\y"),
            # An empty part is the drive's root, which always exists.
            ("/abs/x -q", r"\abs\x -q"),
            # One decision per name: every later `/` goes the way the first did.
            ("bin/nothere/x", r"bin\nothere\x"),
            ("nothere/bin/x", "nothere/bin/x"),
            # Each name after a separator is judged on its own.
            ("bin/test && nothere/x a/b", r"bin\test && nothere/x a/b"),
            ("nothere/x & bin/test", r"nothere/x & bin\test"),
            ("(nothere/a && bin/b)", r"(nothere/a && bin\b)"),
            # A quoted or escaped name after a separator starts where it stands,
            # not where the name before it did.
            ('nothere/x && "bin/run tests"', r'nothere/x && "bin\run tests"'),
            ("bin/test && ^nothere/x", r"bin\test && ^nothere/x"),
        ],
    )
    def test_only_the_command_names_have_their_slash_turned(self, tree, row, expected):
        """A2. Arguments, quoted arguments, `%VAR%`, `^&`, `2>&1`, blocks and
        every operator reach `cmd.exe` as written; only `/` inside a command
        name changes. And the rewrite moves no character: the only difference
        anywhere is `/` → `\\`, position for position. Driven from a root in
        which the rows before #596's start in a directory (`DIRECTORIES`), so
        each is handed over exactly as it was before #596. #596's rows: a
        command name whose part before its first `/` names no directory where
        the row runs is handed over as written, and one that does is
        rewritten, whatever opened it."""
        gate = gate_module()
        got = gate.handed_to_shell(row, windows=True, comspec=CMD, root=tree)
        assert got == expected, f"{row!r} was handed as {got!r}"
        only_slashes_turned(row, got)

    def test_a_name_rooted_in_a_variable_is_judged_where_the_variable_points(
        self, tree, monkeypatch
    ):
        """#596, round 1's 🟡 3 and round 2's 🟡 1. `cmd.exe` expands `%VAR%`
        before it reads a command name, so the part is expanded before it is
        asked whether it is a directory, as far as `as_cmd_expands` models it: a
        name from the environment takes its value, and `%CD%` and `%__CD__%`,
        which `cmd.exe` computes where the environment defines neither, name the
        directory the row runs in. A defined `CD` wins, as it does in `cmd.exe`
        (#616). 0.15.3 rewrote `%CD%/bin/test`, and a literal `%CD%` directory
        never exists, so without the expansion that row stopped running. `$HOME`
        means nothing to `cmd.exe` and is not expanded."""
        gate = gate_module()
        monkeypatch.setenv("AGENTIC_PROBE_TREE", tree)
        monkeypatch.delenv("AGENTIC_PROBE_NOWHERE", raising=False)
        monkeypatch.delenv("CD", raising=False)
        monkeypatch.delenv("__CD__", raising=False)
        # A `$HOME` that names the tree, so only the expansion's rule can leave
        # it as written.
        monkeypatch.setenv("HOME", tree)
        for row, expected in (
            ("%AGENTIC_PROBE_TREE%/bin/test -q", r"%AGENTIC_PROBE_TREE%\bin\test -q"),
            ("%AGENTIC_PROBE_NOWHERE%/bin/x", "%AGENTIC_PROBE_NOWHERE%/bin/x"),
            ("xcopy/e/i a b", "xcopy/e/i a b"),
            # `CD` is computed by cmd.exe where the environment defines none, and
            # the case deletes it above (round 2, 🟡 1).
            ("%CD%/bin/test -q", r"%CD%\bin\test -q"),
            ("%cd%/bin/test -q", r"%cd%\bin\test -q"),
            ("%__CD__%bin/test", r"%__CD__%bin\test"),
            # A substring is not modelled, as `templates/setup/config.md` says (#616):
            # the name it starts is handed as written, although the variable it
            # cuts from names the tree.
            ("%AGENTIC_PROBE_TREE:~0,500%/bin/test -q",) * 2,
            ("$HOME/x", "$HOME/x"),
        ):
            got = gate.handed_to_shell(row, windows=True, comspec=CMD, root=tree)
            assert got == expected, got
            only_slashes_turned(row, got)
        # cmd.exe lets a defined `CD` override the one it computes (`set /?`),
        # so the environment is asked first (#616, round 3 of 1790297086, note 1).
        monkeypatch.setenv("CD", os.path.join(tree, "nowhere"))
        got = gate.handed_to_shell(
            "%CD%/bin/test -q", windows=True, comspec=CMD, root=tree
        )
        assert got == "%CD%/bin/test -q", got

    @pytest.mark.parametrize(
        "row, handed",
        [
            ("xcopy/e/i a b && bin/test", r"xcopy/e/i a b && bin\test"),
            ("findstr/s x *.py", "findstr/s x *.py"),
            ("timeout/t 5 && bin/test", r"timeout/t 5 && bin\test"),
            ("ipconfig/all", "ipconfig/all"),
            # The blank the template also names, which was never rewritten.
            ("xcopy /e /i a b && bin/test", r"xcopy /e /i a b && bin\test"),
        ],
    )
    def test_a_switch_against_another_program_reaches_cmd_exe_as_written(
        self, tree, row, handed
    ):
        """A1, #596. A `/` written straight after a program that is not one of
        `CMD_BUILTINS` is that program's switch: no directory carries the
        program's name where the row runs, so `xcopy/e/i` reaches `cmd.exe` as
        written, and the `bin/test` after it is still rewritten. Before #596
        this case pinned the opposite, `xcopy\\e\\i`, as a documented bound."""
        gate = gate_module()
        got = gate.handed_to_shell(row, windows=True, comspec=CMD, root=tree)
        assert got == handed, got
        only_slashes_turned(row, got)


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

    def test_refuses_to_turn_a_redirections_target_at_the_start_of_a_command(self):
        """A `<` or `>` ends command position until the next separator, so the
        target written after one is a file, even where it starts in a
        directory, and so is the word after it."""
        assert self.turned(">tests/out.txt bin/test", "tests", "bin") == (
            ">tests/out.txt bin/test"
        )

    @pytest.mark.parametrize(
        "row, asked",
        [
            ("bin/test -q", ["bin"]),
            ('"tools/run tests" -q', ["tools"]),
            ("^bin/x", ["bin"]),
            ("@bin/test", ["bin"]),
            ('@"a b"/c', ["a b"]),
            ("./bin/x", ["."]),
            # One question per name, at its first `/`.
            ("a/b/c && d/e", ["a", "d"]),
            # An empty part is answered without asking.
            ("/abs/x", []),
            # A built-in is asked about first, and is never a directory.
            ("rd/s/q x && y/z", ["y"]),
            # Only command names are asked about.
            ("echo a/b", []),
        ],
    )
    @pytest.mark.parametrize("answer", [True, False])
    def test_the_scan_asks_about_a_name_and_reads_nothing_itself(
        self, row, asked, answer
    ):
        """A4. The scan takes the directory question as an argument and does no
        I/O: a predicate here answers from no filesystem at all, and records
        what it was asked — the part before a name's first `/`, with `"`, `^`
        and a leading `@` removed. Both answers are driven, and the answer is
        what decides."""
        gate = gate_module()
        heard = []

        def is_directory(part):
            heard.append(part)
            return answer

        got = gate.command_names_backslashed(row, is_directory)
        assert heard == asked, heard
        only_slashes_turned(row, got)
        if asked:
            # Every asked name's `/` follows the answer.
            assert ("\\" in got) is answer, got


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

WORKFLOW_WITH_TWO_JOBS = """\
name: example

on:
  pull_request:

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # - name: a step somebody commented out
      - name: the first step
        run: true
      - name: the second step
        run: true
  ledger:
    runs-on: ubuntu-latest
    steps:
      - name: a step of another job
        run: true
"""

UNCLASSIFIED_WORKFLOW = """\
name: hygiene

on:
  pull_request:

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: a declared review chain has the round record it claimed
        run: true
      - name: deploy to staging
        run: true
"""

MIXED_WORKFLOW = """\
name: hygiene

on:
  pull_request:

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: a declared review chain has the round record it claimed
        run: true
      - name: both READMEs move together
        run: true
      - name: deploy to staging
        run: true
"""


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
            "a declared review chain has the round record it claimed",
            "a change to what ships must move the version",
            "both READMEs move together",
            "a step nobody classified",
        ]

    def test_refuses_a_text_with_no_jobs_and_another_jobs_steps(self):
        assert gate.job_steps("name: x\n", "release") == []
        assert gate.job_steps(WORKFLOW, "lint") == ["not a release step"]

    def test_the_reader_takes_the_steps_of_the_job_it_was_asked_for(self):
        """A1's reader. In file order, this job only, and an unnamed step — the
        checkout every job opens with — is not one. Nor is a step that exists
        only in a comment, the same reading
        `tests/text/test_ci_gives_the_checks_what_they_need.py#strip_comments` takes
        of the same file, for the same reason."""
        assert gate.job_steps(WORKFLOW_WITH_TWO_JOBS, "release") == [
            "the first step",
            "the second step",
        ]
        assert gate.job_steps(WORKFLOW_WITH_TWO_JOBS, "ledger") == [
            "a step of another job"
        ]

    def test_a_job_the_workflow_does_not_have_reads_as_no_steps(self):
        assert gate.job_steps(WORKFLOW_WITH_TWO_JOBS, "nosuchjob") == []

    def test_a_file_that_declares_no_jobs_reads_as_no_steps(self):
        """Not an exception. The gate calls this on whatever file sits at the
        workflow's path in the repository it was pointed at, and a file it cannot
        read as a workflow must leave the run exactly as it was (A7)."""
        assert gate.job_steps("name: not a workflow at all\n", "release") == []
        assert gate.job_steps("", "release") == []

    def test_a_quoted_step_name_comes_back_unquoted(self):
        """YAML lets a name be quoted, and the partition holds the name a reader
        sees rather than the bytes the file spells it in."""
        text = 'jobs:\n  release:\n    steps:\n      - name: "the quoted step"\n'
        assert gate.job_steps(text, "release") == ["the quoted step"]
        text = "jobs:\n  release:\n    steps:\n      - name: 'the other quoting'\n"
        assert gate.job_steps(text, "release") == ["the other quoting"]

    def test_a_step_name_carrying_a_colon_survives_the_reader(self):
        """`- name: a: b` is one name, not a mapping. A reader that split on the
        first colon would take `a` and the partition would name a step nobody
        runs — which is exactly A2's failure, arriving through the reader."""
        text = "jobs:\n  release:\n    steps:\n      - name: the step: and its tail\n"
        assert gate.job_steps(text, "release") == ["the step: and its tail"]


class Test_base_is_main:
    @pytest.mark.parametrize("given", ["main", "origin/main"])
    def test_accepts_main_as_typed_or_as_origins(self, given):
        assert gate.base_is_main(given)

    @pytest.mark.parametrize("given", [None, "release/v1", "upstream/main"])
    def test_refuses_any_other_base(self, given):
        assert not gate.base_is_main(given)

    @pytest.mark.parametrize(
        "given, main",
        [
            ("main", True),
            ("origin/main", True),
            ("origin/origin/main", False),
            ("refs/heads/main", False),
            ("mains", False),
            ("release/x", False),
            (None, False),
        ],
    )
    def test_one_reading_says_whether_the_base_is_main(self, given, main):
        """S5's `base_is_main`: the one reading the count takes, keyed on the spelling with one leading `origin/` removed."""
        assert gate.base_is_main(given) is main


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
        assert gate.mirrored()[gate.job_steps(WORKFLOW, "release")[0]] == "chain"
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
            "seal gate: this run answers every one of the 1 `release` steps "
            f"{gate.WORKFLOW} runs for this base."
        )

    def test_refuses_to_send_a_reader_to_a_row_for_an_unclassified_step(self):
        said = gate.coverage_line(WORKFLOW, "main")
        excluded, unknown = said.split(" In no row of ")
        assert "both READMEs move together" in excluded
        assert "a step nobody classified" not in excluded
        assert unknown.endswith(": a step nobody classified.")
        assert gate.coverage_line("name: x\n", "main") is None

    def test_a_step_no_row_classifies_is_not_said_to_carry_a_reason(self):
        """A6's other repository, and round 1's finding 3. `PARTITION` describes
        THIS repository's `release` job, and `broad_gate.py` ships to every
        installation — so a repository with a `release` job of its own has steps
        no row has ever heard of.

        Counting them as unanswered is honest; telling their reader the reason is
        in `PARTITION` is not, because `PARTITION` holds a row per step of a
        workflow that repository does not run. A reader who follows the pointer
        finds somebody else's list and no answer, which is the reconstruction
        from two files this work item exists to remove, one level further out."""
        said = gate.coverage_line(UNCLASSIFIED_WORKFLOW, "base")
        assert "deploy to staging" in said, said
        with_reasons = said.split("no arm mirrors it in", 1)
        assert len(with_reasons) == 1 or "deploy to staging" not in with_reasons[1], (
            f"a step in no row of PARTITION is named among the ones PARTITION "
            f"gives a reason for:\n{said}"
        )
        assert "no row of `broad_gate.py#PARTITION` at all" in said, said

    def test_the_two_clauses_render_together_and_hold_the_right_names(self):
        """Round 2's coverage note. The case above and
        `tests/behaviour/test_the_gate_names_every_step_ci_runs.py`'s
        `test_a_step_a_row_excludes_is_still_pointed_at_its_reason` each
        exercise one clause — `UNCLASSIFIED_WORKFLOW` leaves `excluded` empty
        and this repository's own workflow leaves `unknown` empty — so the
        JOINED sentence, which is
        the one a mixed repository's reader actually has to parse, was rendered
        by nothing.

        The two comprehensions are disjoint by construction, which is why the
        reviewer called this a coverage note rather than a defect. It is still
        the sentence that goes wrong if either clause ever learns to claim the
        other's steps."""
        said = gate.coverage_line(MIXED_WORKFLOW, "base")
        assert "runs 3 steps for this base and this run answers 1" in said, said

        reasoned, _, unknown = said.partition(
            "In no row of `broad_gate.py#PARTITION` at all"
        )
        assert unknown, f"the second clause did not render at all:\n{said}"
        assert "no arm mirrors it in `broad_gate.py#PARTITION`" in reasoned, said

        assert "both READMEs move together" in reasoned, said
        assert "both READMEs move together" not in unknown, (
            f"a step `PARTITION` excludes with a reason is named among the ones "
            f"it has never heard of:\n{said}"
        )
        assert "deploy to staging" in unknown, said
        assert "deploy to staging" not in reasoned, (
            f"a step in no row of `PARTITION` is named among the ones it gives a "
            f"reason for:\n{said}"
        )
        assert "a declared review chain has the round record it claimed" not in said, (
            f"a step the gate DOES mirror is named as unanswered:\n{said}"
        )

    def test_the_count_cannot_be_asked_without_a_base(self):
        """Round 1's 🟡 3: a caller that drops the base gets a `TypeError` rather
        than the feature-base answer in silence, so the merge that rewrote the
        gate's coverage call could not lose its argument unnoticed."""
        text = read(HYGIENE)
        for unit in (gate.unanswered, gate.coverage_line):
            with pytest.raises(TypeError):
                unit(text)


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
    """A round record in `templates/records/sdd-round.md`'s shape, one finding per
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
            write(tmp_path, f"trail/rounds/round-{n}.md", "x")
        write(tmp_path, "trail/rounds/round-2-report.md", "x")
        names = [os.path.basename(p) for p in gate.round_records(str(tmp_path))]
        assert names == ["round-1.md", "round-2.md", "round-10.md"]

    def test_refuses_an_item_with_no_rounds_directory(self, tmp_path):
        assert gate.round_records(str(tmp_path)) == []


class Test_write_gate_file:
    def test_accepts_a_second_run_appended_below_the_first(self, tmp_path):
        """#1198, *Scope* item 2: each green run appends one run block below
        the blocks already there, so the last is the newest, and a file the
        record had no block in keeps its text above the first one."""
        record = tmp_path / "trail" / "gate.md"
        record.parent.mkdir()
        old = "| Field | Value |\n|---|---|\n| Broad gate | aaa1111 against base1 |\n"
        record.write_text(old, encoding="utf-8")
        gate.write_gate_file(str(tmp_path), "aaa1111", "bbb2222")
        path = gate.write_gate_file(str(tmp_path), "ccc3333", "bbb2222")
        text = pathlib.Path(path).read_text(encoding="utf-8")
        assert path == os.path.join(str(tmp_path), "trail", "gate.md")
        assert text.startswith(old), text
        found = chain.FIELDS.read(text, chain.FIELDS.GATE)
        assert [b.fields[chain.FIELDS.RUN].value for b in found.blocks] == [
            "aaa1111 against bbb2222",
            "ccc3333 against bbb2222",
        ]

    def test_accepts_a_first_run_under_the_work_items_heading(self, tmp_path):
        item = tmp_path / "1799000000-an-item"
        item.mkdir()
        path = gate.write_gate_file(str(item), "aaa1111", "bbb2222")
        assert pathlib.Path(path).read_text(encoding="utf-8") == (
            "# 1799000000-an-item \u2014 broad gate\n\n"
            "```seal\nrun: aaa1111 against bbb2222\n```\n"
        )

    def test_refuses_to_record_one_run_twice(self, tmp_path):
        """A re-run over an unchanged checkout appends nothing where the last
        block names the same run; the same commit against another base is
        another run."""
        gate.write_gate_file(str(tmp_path), "aaa1111", "bbb2222")
        path = gate.write_gate_file(str(tmp_path), "aaa1111", "bbb2222")
        once = pathlib.Path(path).read_text(encoding="utf-8")
        assert once.count("run: ") == 1, once
        gate.write_gate_file(str(tmp_path), "aaa1111", "ccc3333")
        text = pathlib.Path(path).read_text(encoding="utf-8")
        assert text.count("run: aaa1111") == 2, text
        # The last block is the one asked: a re-run of the newest run appends
        # nothing, and a run an earlier block names is appended again.
        gate.write_gate_file(str(tmp_path), "aaa1111", "ccc3333")
        gate.write_gate_file(str(tmp_path), "aaa1111", "bbb2222")
        text = pathlib.Path(path).read_text(encoding="utf-8")
        assert text.count("run: aaa1111 against ccc3333") == 1, text
        assert text.count("run: aaa1111 against bbb2222") == 2, text

    @pytest.mark.parametrize(
        "held",
        ["# x\n\na note\n\n" + "`" * 3 + "\n", "<!-- a note -->\n\n# x\n"],
        ids=["a fence nobody closed", "a comment line"],
    )
    def test_refuses_a_file_whose_new_run_the_reader_would_not_read(
        self, tmp_path, held
    ):
        """Round 1 of #1198, finding 2: the run is appended to whatever the
        file holds, so the file as it would be written is read back. Below a
        fence nobody closed the new block's closer closes that fence and no
        run block reads; a comment line is refused at the pull request. Each
        is refused here, where a person can fix the file, and the file is
        left as it was."""
        record = tmp_path / "trail" / "gate.md"
        record.parent.mkdir()
        record.write_text(held, encoding="utf-8")
        with pytest.raises(gate.Refused, match="was not written"):
            gate.write_gate_file(str(tmp_path), "aaa1111", "bbb2222")
        assert record.read_text(encoding="utf-8") == held

    def test_refuses_a_run_the_reader_would_refuse(self, tmp_path):
        with pytest.raises(gate.Refused, match="does not read whole as `run: <value>`"):
            gate.write_gate_file(str(tmp_path), "HEAD", "main")
        assert not (tmp_path / "trail" / "gate.md").exists()

    def test_refuses_a_file_that_cannot_be_written_or_read(self, tmp_path):
        with pytest.raises(gate.Refused, match="could not be written"):
            gate.write_gate_file(str(tmp_path / "no-such-item"), "aaa1111", "bbb2222")
        (tmp_path / "trail").mkdir()
        (tmp_path / "trail" / "gate.md").write_bytes(b"\xff\xfe")
        with pytest.raises(gate.Refused, match="could not be read"):
            gate.write_gate_file(str(tmp_path), "aaa1111", "bbb2222")


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
        write(item, "trail/rounds/round-1.md", a_round("deferred #7", "fixed abc1234"))
        write(item, "trail/rounds/round-2.md", a_round("deferred #8"))
        write(item, "trail/rounds/round-3.md", a_round("deferred #9", "deferred"))
        write(item, "trail/rounds/round-4.md", a_round("**deferred** #9"))
        write(item, "trail/rounds/round-5.md", OLD_RECORD)
        write(
            item,
            "trail/rounds/round-6.md",
            a_round("deferred #9").replace("verdict:", "V:"),
        )
        rows = gate.rounds_rows(str(item))
        assert rows == [("rounds", "6"), ("", "2 deferred → #7, #8")], rows

    def test_refuses_a_deferral_row_where_nothing_was_deferred(self, tmp_path):
        item = tmp_path / "1799000003-y"
        assert gate.rounds_rows(str(item)) == [("rounds", "0")]
        write(item, "trail/rounds/round-1.md", a_round("fixed abc1234"))
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


# Pinned verbatim, because a person reads it on the failure form and decides
# from it whether to open the kept file (contract rule 14). It names every
# cause of a missing record, never one as the only one (#825, #869).
NO_RECORD_HERE = (
    "no pytest the row ran here left a record of the gate's recorder (the row "
    "started no pytest, because a part before its runner failed or it has none; "
    "none it started loaded the recorder; or the one that did could not write "
    "its record and warned 'agentic_pytest_record: no record written' in "
    "suite.txt), so this exit code is not a count of failing tests"
)


def a_counted_record(sessions=1, **counts):
    """A `RunRecord` of SESSIONS sessions whose counts are COUNTS."""
    record = gate.RunRecord()
    record.sessions, record.counts = sessions, dict(counts)
    return record


class Test_failure_lines:
    @pytest.mark.parametrize(
        "name, text, record, said",
        [
            # #448's case: the shell never reached the suite. The wording is
            # the machine's own language, which is why the line does not read it.
            (
                "suite",
                "'bin' is not recognized as an internal or external command,\n",
                None,
                True,
            ),
            ("suite", "", a_counted_record(sessions=0), True),
            # A printed summary is no record (#869): the form says no record.
            ("suite", "F\n1 failed in 0.01s\n", None, True),
            # A record's counts are what the form shows instead.
            ("suite", "", a_counted_record(failed=1), False),
            ("suite", "", a_counted_record(error=1), False),
            # Any other check's output was never a pytest run.
            ("ledger", "BROKEN a#b@c\n", None, False),
        ],
    )
    def test_a_failing_suite_with_no_record_says_it_is_not_a_count(
        self, name, text, record, said
    ):
        """A5. The line is keyed on what is missing, a record of the row's own
        pytest, and not on an exit code: `cmd.exe` exits 1 for a command it
        cannot find, which is pytest's own 1; nor on a summary the row printed,
        which anything the row runs can print (#869)."""
        gate = gate_module()
        lines = gate.failure_lines(
            gate.Check(name, 1, text, "/x/out.txt"), None, record
        )
        assert (NO_RECORD_HERE in lines) is said, lines
        assert lines[0] == "exit 1", lines
        assert lines[-1] == "full output: /x/out.txt", lines
        if name == "suite" and not said:
            assert gate.suite_counts(record) in lines, lines
        assert not hasattr(gate, "NO_SUMMARY")

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
        form = gate.failed_form("c", "a", [("longer-arm", ["u"]), ("suite", [])])
        assert form[2:] == ["  longer-arm u", "  suite      (no output)"]


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
    mark_root(d / "seal")
    write(d, f"{ITEM}/gaps.md", OVERVIEW)
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

    def test_refuses_new_for_a_file_a_red_base_never_collected(self, repo, tmp_path):
        """The base's run exited non-zero and never collected the file, so it
        may have stopped before reaching it, and the word carries the exit."""
        git(repo, "switch", "-q", "base")
        write(repo, "tests/test_red.py", FAILING_TEST)
        commit(repo, "a failure only the base has")
        git(repo, "switch", "-q", "feature")
        failing_on_feature(repo)
        words = gate.compare_at_base(
            str(repo), "base", SUITE_ROW, ["tests/test_two.py"], str(tmp_path)
        )
        assert words == {"tests/test_two.py": gate.NOT_REACHED.format(code=1)}

    def test_refuses_to_compare_at_a_base_that_cannot_be_checked_out(
        self, repo, tmp_path
    ):
        words = gate.compare_at_base(
            str(repo), "0" * 40, SUITE_ROW, ["a.py", "b.py"], str(tmp_path)
        )
        assert words == {"a.py": gate.NOT_CHECKED_OUT, "b.py": gate.NOT_CHECKED_OUT}


class Test_uncommitted_line:
    def test_accepts_a_written_file_git_sees_uncommitted(self, repo):
        path = gate.write_gate_file(str(repo / ITEM), "ccc3333", "bbb2222")
        assert gate.uncommitted_line(str(repo), path) == gate.CELL_UNCOMMITTED.format(
            path=RECORD_REL
        )

    def test_refuses_a_committed_file_and_no_file(self, repo):
        path = gate.write_gate_file(str(repo / ITEM), "ccc3333", "bbb2222")
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
        assert lines[-1] == gate.CELL_UNCOMMITTED.format(path=RECORD_REL)
        for name in ("suite", "chain", "mode"):
            assert (keep / f"{name}.txt").is_file(), name
        # The unverified record's arm left with #945, and no run asks it.
        assert not (keep / "unverified.txt").exists()
        assert "unverified" not in out.stdout
        chain_kept = (keep / "chain.txt").read_text(encoding="utf-8")
        assert f"--baseline {base} --root" in chain_kept.splitlines()[0]
        # The gate draws nothing and queues no stamp (#975).
        assert not (repo / ".git" / "agentic-stamp").exists()
        record = (repo / ITEM / "trail" / "gate.md").read_text(encoding="utf-8")
        assert f"```seal\nrun: {tree} against {base}\n```\n" in record
        assert f"seal gate: `{ROW}` says: {SUITE_ROW}" in out.stderr

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
        assert not (repo / ITEM / "trail" / "gate.md").exists()

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
        said = (
            r"has no seal/ root at either place a root lives \(`<repo>/seal/`, "
            r"`<git-common-dir>/seal/`, its README.md opening with the marker\)"
        )
        with pytest.raises(gate.Refused, match=said):
            gate.gate(namespace(tmp_path, tmp_path / "out"))
        write(tmp_path, "seal/config.md", config_of("bin/test -q"))
        with pytest.raises(gate.Refused, match=said):
            gate.gate(namespace(tmp_path, tmp_path / "out"))


CONFIG = (
    "# Repository config\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n"
    f"| Broad gate | {sys.executable} -c pass |\n"
)


def sealable_repo(tmp_path):
    """A repository on `base` with a `feature` branch one commit ahead.

    Driven from Python, per contract rule 8: a probe that commits reaches
    the commit gate exactly as real work does, and the prompt lands on nobody
    while a round is running.
    """
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "base")
    write(repo, "src/service.py", "def handler(x):\n    return x + 1\n")
    write(repo, "seal/config.md", CONFIG)
    mark_root(repo / "seal")
    write(repo, f"{ITEM}/gaps.md", OVERVIEW)
    commit(repo, "base")
    git(repo, "switch", "-qc", "feature")
    write(repo, "src/service.py", "def handler(x):\n    return x + 2\n")
    commit(repo, "feature changes the handler")
    return repo


def run_gate(repo, keep, base="base"):
    return subprocess.run(
        [
            sys.executable,
            GATE,
            "--base",
            base,
            "--root",
            str(repo),
            "--shape",
            "--keep-output",
            str(keep),
        ],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=300,
    )


FIXTURE_WORKFLOW = """\
name: hygiene

on:
  pull_request:

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: a declared review chain has the round record it claimed
        run: true
      - name: the milestone this release claims is the work it carries, and a patch carries no feat
        run: |
          if [ "${{ github.base_ref }}" != "main" ]; then
            echo "not a release"; exit 0
          fi
      - name: both READMEs move together
        run: true
"""


def panel_rows(repo):
    """The stamp's rows for a run over `repo`'s workflow, computed rather
    than scraped off the drawing — the rendered line is asserted separately,
    and a value's WIDTH cannot be measured once the frame has cut it."""
    checks = {
        name: gate.Check(name, 0, "", "") for name in (gate.SUITE, gate.CHAIN_NAME)
    }
    base = gate.Base("base", "cccccccc", "base", "cccccccc")
    return gate.panel(
        "ccccccc", base, checks, None, read(repo / ".github/workflows/hygiene.yml")
    )


def with_workflow(repo):
    """The fixture, given a hygiene workflow whose `release` job runs three
    real steps: one this gate mirrors and two it does not."""
    write(repo, ".github/workflows/hygiene.yml", FIXTURE_WORKFLOW)
    commit(repo, "the repository gains a hygiene workflow")
    return repo


# The panel of a run with no workflow, as it has stood release to release.
# `gate` joined it in 0.15.1 (#475), and since #666 it prints only where the
# copy that ran is not the one invoked, so a run handed no `copy` has none.
# #666 also moved the ref from `from` to the row under `base` (`""`), and the
# row's exit code from `row` to the row under `suite` — which this fixture's
# empty output, carrying no pytest counts, does not have. No row here is
# about the workflow: a run without one is still the run it was. #717 took
# `chain` off, because a drawn panel is green by construction and its title
# already said its exit was 0. #832's S5a, the owner's design of 2026-10-07,
# put it back with a `✓`, and the base's ref beside its commit on one row.
# #944 took the `ledger` row off with the ledger, and #975 the title row, when
# the rows became the gate's printed report and no stamp's.
HISTORICAL_ROWS = (
    "tree",
    "base",
    "suite",
    "chain",
)


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
        assert f"seal gate: {repo} ships its own gate; running" in out.stderr

    def test_refuses_to_leave_the_invoked_path_for_a_check_to_read(
        self, tmp_path, monkeypatch, capsys
    ):
        git(tmp_path, "init", "-q")
        monkeypatch.setenv(gate.INVOKED_AS_VAR, "/somewhere/broad_gate.py")
        assert gate.main(["--base", "base", "--root", str(tmp_path)]) == 2
        assert gate.INVOKED_AS_VAR not in os.environ
        err = capsys.readouterr().err
        assert f"seal gate: gate {os.path.realpath(ROOT / TARGET)} (plugin " in err

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
        wrapper = ROOT / "bin" / "seal"
        command = (
            [
                os.environ.get("COMSPEC", "cmd.exe"),
                "/c",
                f"{wrapper}.cmd",
                "gate",
                "--help",
            ]
            if os.name == "nt"
            else [str(wrapper), "gate", "--help"]
        )
        out = subprocess.run(
            command,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
        assert out.returncode == 0, out.stderr
        assert out.stdout.startswith("usage: seal gate")

    def test_the_fixture_branch_passes(self, tmp_path):
        """The other cases' starting point: every arm passes on the fixture, so a
        refusal below is the one thing each case changed."""
        repo = sealable_repo(tmp_path)
        result = run_gate(repo, tmp_path / "out")
        assert result.returncode == 0, result.stdout + result.stderr
        assert result.stdout.startswith("BROAD GATE PASSED   "), result.stdout

    def test_a_mode_row_that_disagrees_with_the_folder_fails_the_gate(self, tmp_path):
        """A3's behavioural half for the other arm #468 added. `seal/config.md`
        says the root lives under the git directory and the root is committed in
        the tree, which is the one direction of that disagreement CI can ever
        reach — and the gate said nothing about it until this arm existed.

        Red against the gate as it stood: this fixture sealed green."""
        repo = sealable_repo(tmp_path)
        write(
            repo,
            "seal/config.md",
            CONFIG.replace("| Mode | shared |", "| Mode | local |"),
        )
        commit(repo, "the row now says local while the folder is committed")
        result = run_gate(repo, tmp_path / "out")
        assert result.returncode == 1, result.stdout + result.stderr
        assert result.stdout.startswith("BROAD GATE FAILED   "), result.stdout
        assert gate.MODE_NAME in result.stdout, (
            f"the failure form does not name the `{gate.MODE_NAME}` arm:\n{result.stdout}"
        )

    def test_the_report_says_how_many_steps_the_run_did_not_answer(self, tmp_path):
        """A6, on the printed output rather than on the data behind it.

        W1's choice, recorded: **the panel carries the count and the names go to
        the stream beside it.** The panel gives a value 41 columns since #832
        (23 before it) — `seal_stamp.PANEL_VALUE_WIDTH` — and three
        step names do not fit in it, let alone fourteen. A reader given only a
        number would have to reconstruct WHICH from two files, which is the
        reconstruction this work item exists to remove, so both are printed and
        neither alone.

        The printed half is read off the run's own stdout since #975, where the
        panel's rows are text under the `BROAD GATE PASSED` line."""
        repo = with_workflow(sealable_repo(tmp_path))
        result = run_gate(repo, tmp_path / "out")
        assert result.returncode == 0, result.stdout + result.stderr

        printed = result.stdout.splitlines()
        rendered = [line for line in printed if "more steps" in line]
        assert len(rendered) == 1, (
            "the report says nothing about the steps this run did not answer:\n"
            + result.stdout
        )
        # Whole, not cut: a value one column too wide would read as a shorter
        # true statement — which is the failure mode the elision beside the
        # `from` row was added for. The substring is the assertion: a cut value
        # would not carry its tail.
        #
        # #666: over the steps CI runs for THIS base. The milestone step runs only
        # on a pull request into `main` and the base here is `base`, so it is
        # neither answered nor unanswered — `2 of 3` became `1 of 2`.
        #
        # #717: the owner's wording, `CI also  <n> more steps`. The denominator
        # left the panel for the stderr line beside the names, asserted below.
        # #832's S5a: the value leads with a dim `·`, which `--shape` writes `.`.
        assert re.search(r"^CI also [·.] 1 more steps$", rendered[0]), rendered[0]
        width = load_module(STAMP, "agentic_seal_stamp").PANEL_VALUE_WIDTH
        value = next(
            v for _, v in [r for r in panel_rows(repo) if r] if "more steps" in v
        )
        assert len(value) <= width, (
            f"the value is {len(value)} columns and the panel gives "
            f"{width}: {value!r}. This is W1's whole reason for a "
            "count rather than the names"
        )

        assert "both READMEs move together" in result.stderr
        # A11 at the fixture: the step CI will not run here is not named among
        # the unanswered, and one clause says how many were left out and why.
        assert (
            "the milestone this release claims is the work it carries, and a patch carries no feat"
            not in result.stderr
        ), result.stderr
        assert (
            "runs 2 steps for this base and this run answers 1. 1 more runs only on "
            "a pull request into `main`, so this count leaves it out."
        ) in result.stderr, result.stderr
        assert (
            "a declared review chain has the round record it claimed"
            not in (result.stderr.split("Not answered", 1)[-1])
        ), "a step the gate DOES mirror is listed among the ones it did not answer"

    def test_a_seal_that_answers_every_step_says_so(self, tmp_path):
        """The other value of the same line. A run that leaves nothing unanswered
        must not go quiet: silence there is indistinguishable from a gate that
        stopped looking, which is the state this work item found the gate in.

        #666 keys it on the base: the milestone step stays in the workflow and
        runs only into `main`, so against `base` the one step CI runs is the
        mirrored one, and the line says every one is answered AND that one more
        was left out, rather than calling the milestone unanswered."""
        repo = sealable_repo(tmp_path)
        readmes = "      - name: both READMEs move together\n        run: true\n"
        assert readmes in FIXTURE_WORKFLOW, "the fixture no longer has the step"
        write(
            repo, ".github/workflows/hygiene.yml", FIXTURE_WORKFLOW.replace(readmes, "")
        )
        commit(repo, "a workflow whose every step CI runs here this gate mirrors")
        result = run_gate(repo, tmp_path / "out")
        assert result.returncode == 0, result.stdout + result.stderr
        assert (
            "this run answers every one of the 1 `release` steps "
            f"{gate.WORKFLOW} runs for this base. 1 more runs only on a pull request "
            "into `main`, so this count leaves it out."
        ) in result.stderr, result.stderr
        # #717: the panel's row does not go quiet either. At 0 it still prints,
        # and it says a count.
        assert ("CI also", "· 0 more steps") in panel_rows(repo), panel_rows(repo)

    def test_a_repository_with_no_hygiene_workflow_is_sealed_exactly_as_before(
        self, tmp_path
    ):
        """A7. The partition describes THIS repository's CI and `broad_gate.py`
        ships to every repository that installs the plugin. For one with no such
        workflow the run must be what it was: the same panel rows, and no line
        about steps nobody runs.

        Red against a gate that prints the row unconditionally — which is what a
        partition held as a constant and printed from would do, and why
        `questions.md` Q1's answer (a) survives only while this case is green.
        """
        repo = sealable_repo(tmp_path)
        assert not (repo / ".github").exists(), "the fixture has a workflow after all"
        result = run_gate(repo, tmp_path / "out")
        assert result.returncode == 0, result.stdout + result.stderr
        # The stamp's rows are what the run read: `panel` is handed
        # `workflow_text(root)`, and for this repository that is None, which is
        # the input the labels below are computed over. It used to be asked of a
        # drawing on stdout, and a piped run draws nothing since #400 — so that
        # absence held for every repository, workflow or not.
        assert gate.workflow_text(str(repo)) is None, (
            "the run read a workflow in a repository that has none, so the stamp "
            "would say something about that workflow's steps"
        )
        # What names the release job, and nothing a path can carry by accident:
        # the job as `coverage_line` spells it, the workflow's path, and every
        # step name the partition holds. A bare `release` used to be searched
        # for once the echoed paths were cut out of the stream, and a checkout
        # under a `release/` directory then went red for a path nobody had cut
        # yet (#499).
        for names_the_job in (
            f"`{gate.RELEASE_JOB}`",
            gate.WORKFLOW,
            *(name for name, _, _ in gate.PARTITION),
        ):
            assert names_the_job not in result.stderr, (
                f"the gate names {names_the_job!r} for a repository with no "
                f"hygiene workflow:\n{result.stderr}"
            )

        labels = tuple(
            row[0]
            for row in gate.panel(
                "ccccccc",
                gate.Base("base", "cccccccc", "base", "cccccccc"),
                {
                    name: gate.Check(name, 0, "", "")
                    for name in (gate.SUITE, gate.CHAIN_NAME)
                },
                None,
            )
            if row
        )
        assert labels == HISTORICAL_ROWS, (
            f"the panel of a run with no workflow is no longer the panel it was: {labels}"
        )

    def test_a_workflow_that_is_not_utf8_leaves_the_run_as_it_was(self, tmp_path):
        """A7's other shape, and the one that ends the run rather than changing
        it. `UnicodeDecodeError` is a `ValueError`, not an `OSError`, and
        `broad_gate.main` catches only `Refused` — so before this the gate ended
        on a traceback for a repository whose workflow file happens to be
        latin-1. A repository this partition is not about must come out of the
        run exactly as it went in, and a traceback is the largest departure from
        that there is. Round 1, finding 5."""
        repo = sealable_repo(tmp_path)
        path = repo / ".github" / "workflows" / "hygiene.yml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(
            "jobs:\n  release:\n    steps:\n      - name: café step\n".encode("latin-1")
        )
        commit(repo, "a workflow file that is not utf-8")
        assert gate.workflow_text(str(repo)) is None
        result = run_gate(repo, tmp_path / "out")
        assert result.returncode == 0, result.stdout + result.stderr
        assert result.stdout.startswith("BROAD GATE PASSED   "), result.stdout
        assert "Traceback" not in result.stderr, result.stderr
        # No `workflow` row on the stamp is `workflow_text(root)` being None,
        # asserted above: it is the one input `panel` takes the row from, and the
        # case before this one pins the rows of a run given None. It used to be
        # asked of a drawing on stdout as well, and a piped run draws nothing
        # since #400, so that absence held whatever the run read.


test_census = census_case(TARGET)
