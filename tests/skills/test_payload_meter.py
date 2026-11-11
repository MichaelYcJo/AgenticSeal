"""`skills/verify/scripts/payload_meter.py`, one class per function.

What a session's and each agent's startup payload is made of, and what it
costs in tokens -- with every token figure carrying its basis.

#292. The meter reads the tree (an agent's definition, each `SKILL.md` its
`skills:` list injects, the two `CLAUDE.md` files the harness adds and, since
#1177, each file their `@` lines import, and for a session the core the
plugin's `SessionStart` hook prints) and
reports bytes, characters and tokens. Bytes and characters are counted;
tokens are never — each is ESTIMATED from the row's bytes at one assumed
bytes-per-token ratio, and the label on each figure says so. A bare token
number is the defect this module exists to refuse, because the six
calibration spawns in `frame/design.md` showed bytes tracking tokens at 2.7
to 3.4 per token across three agents.

The fixtures are a hand-built tree with known sizes, so a change that
starts printing a number with no basis fails here.

#942's phase 6 placed these cases from
`tests/test_the_payload_meter_says_what_it_measured.py`. Its round 9 fix pass
placed in `Test_module` the two rows that run a copy of this script without
its siblings, from `tests/test_a_script_copied_alone_exits_2.py`, a case of
this module alone.
"""

import importlib.util
import json
import os
import re
import subprocess
import sys

import pytest
from conftest import LS, ROOT, census_case, symlink_or_skip

TARGET = "skills/verify/scripts/payload_meter.py"

SCRIPT = os.path.join(ROOT, "skills", "verify", "scripts", "payload_meter.py")
BIN = os.path.join(ROOT, "bin")

# One multibyte character per file so bytes and characters differ, and the
# case that checks them cannot pass by reading one column twice.
ACCENT = "é"


def _load():
    spec = importlib.util.spec_from_file_location("payload_meter_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def meter():
    return _load()


# --- fixtures ----------------------------------------------------------------


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def a_tree(tmp_path, skills=("alpha", "beta"), extra_agent=False):
    """A plugin tree: one agent whose `skills:` names two skills, the two
    skill files, and the repository `CLAUDE.md`; plus a home with the user
    `CLAUDE.md`. Every file carries one accent so bytes ≠ chars."""
    root = tmp_path / "plugin"
    home = tmp_path / "home"
    listed = "".join(f"  - {name}\n" for name in skills)
    write(
        str(root / "agents" / "probe.md"),
        f"---\nname: probe\ndescription: a probe\nskills:\n{listed}---\n"
        f"# probe\n\nbody {ACCENT}\n",
    )
    if extra_agent:
        write(
            str(root / "agents" / "other.md"),
            f"---\nname: other\nskills:\n  - alpha\n---\n# other {ACCENT}\n",
        )
    write(
        str(root / "skills" / "alpha" / "SKILL.md"),
        f"---\nname: alpha\n---\n# alpha\n\nintro {ACCENT}\n\n## First\n\none\n\n"
        f"### Nested\n\ntwo\n\n## Second\n\nthree\n",
    )
    write(str(root / "skills" / "beta" / "SKILL.md"), f"# beta\n\nplain {ACCENT}\n")
    write(str(root / "CLAUDE.md"), f"## Repo rules {ACCENT}\n")
    write(str(home / ".claude" / "CLAUDE.md"), f"## User rules {ACCENT}\n")
    return root, home


def two_user_dirs(tmp_path):
    """#1367. `a_tree`, and a config directory beside its home. The home's
    `.claude` and the config directory each hold a `CLAUDE.md` and a shadow
    of `alpha`, every file a different size, so a row's bytes say which
    directory it read. Returns the root, the home and the config directory."""
    root, home = a_tree(tmp_path)
    config = tmp_path / "config"
    write(str(home / ".claude" / "CLAUDE.md"), "## Home rules\n" + "h" * 300 + "\n")
    write(str(config / "CLAUDE.md"), "## Config rules\n" + "c" * 400 + "\n")
    shadow = os.path.join("skills", "alpha", "SKILL.md")
    write(str(home / ".claude" / shadow), "# home alpha\n" + "h" * 500 + "\n")
    write(str(config / shadow), "# config alpha\n" + "c" * 600 + "\n")
    return root, home, config


def a_core(root):
    """The plugin's core and manifest under ROOT, so a session in that tree
    receives the core from the plugin's `SessionStart` hook. The core carries
    a frontmatter the hook leaves out and one accent so bytes ≠ chars."""
    write(
        str(root / ".claude-plugin" / "plugin.json"),
        '{"name": "agentic", "version": "9.9.9"}\n',
    )
    write(
        str(root / "skills" / "core" / "SKILL.md"),
        f"---\nname: core\ndescription: the core\n---\n\n# The core {ACCENT}\n\n"
        "One value.\n",
    )


def hook_output(root):
    """What `lib/core.py#rendered` prints for the core of the tree at ROOT:
    the one definition the hook and the meter share."""
    spec = importlib.util.spec_from_file_location(
        "payload_meter_test_core", os.path.join(ROOT, "lib", "core.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.rendered(module.origin(str(root), str(root)), str(root))


HOOK_ROW = "SessionStart hook: skills/core/SKILL.md"

# The basis every token figure carries, the session's and each agent's.
BASIS = "estimated (3.2 B/token, an assumed ratio)"


def size_of(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return len(raw), len(raw.decode("utf-8"))


def run(args, home, cwd=None, extra=None):
    """The script in a child under HOME and USERPROFILE set to HOME, with
    `extra`'s variables added. `tests/conftest.py` removes
    `CLAUDE_CONFIG_DIR`, so the child reads it only where `extra` sets it."""
    env = dict(os.environ, HOME=str(home), USERPROFILE=str(home), **(extra or {}))
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        capture_output=True,
        encoding="utf-8",
        env=env,
        cwd=cwd or ROOT,
    )


def rows_of(table_text):
    """The data rows of every markdown table in a report, split into cells."""
    out = []
    for line in table_text.splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append(cells)
    return out


class Test_measure:
    # --- S1: the meter reports composition -----------------------------------

    def test_accepts_a_tree_with_bytes_and_chars_per_file_and_in_total(
        self, meter, tmp_path
    ):
        root, home = a_tree(tmp_path)
        data = meter.measure(str(root), str(home))
        assert list(data["agents"]) == ["probe"]
        files = data["agents"]["probe"]["files"]
        paths = [f["path"] for f in files]
        assert paths == [
            "agents/probe.md",
            "skills/alpha/SKILL.md",
            "skills/beta/SKILL.md",
            "CLAUDE.md",
            "~/.claude/CLAUDE.md",
        ], paths
        on_disk = [
            root / "agents" / "probe.md",
            root / "skills" / "alpha" / "SKILL.md",
            root / "skills" / "beta" / "SKILL.md",
            root / "CLAUDE.md",
            home / ".claude" / "CLAUDE.md",
        ]
        for row, path in zip(files, on_disk, strict=True):
            raw, chars = size_of(path)
            assert (row["bytes"], row["chars"]) == (raw, chars), row["path"]
            assert row["bytes"] > row["chars"], (
                f"{row['path']} carries no multibyte char"
            )
        total = data["agents"]["probe"]["total"]
        assert total["bytes"] == sum(f["bytes"] for f in files)
        assert total["chars"] == sum(f["chars"] for f in files)

    def test_the_claude_md_pair_is_marked_as_the_harness_share(self, meter, tmp_path):
        """The two `CLAUDE.md` files sit in EVERY agent's prefix, so their
        rows carry the harness's share, and the text prints the pair as one
        line that says where it stands."""
        root, home = a_tree(tmp_path)
        data = meter.measure(str(root), str(home))
        files = data["agents"]["probe"]["files"]
        harness = [f["path"] for f in files if f.get("share") == "harness"]
        own = [f["path"] for f in files if f.get("share") == "agent"]
        assert harness == ["CLAUDE.md", "~/.claude/CLAUDE.md"]
        assert own == [
            "agents/probe.md",
            "skills/alpha/SKILL.md",
            "skills/beta/SKILL.md",
        ]
        text = meter.render(data)
        pair_line = next(c for c in rows_of(text) if c[0].startswith("CLAUDE.md pair"))
        assert pair_line[4] == f"{BASIS} — inside every agent's prefix", pair_line

    def test_an_import_in_either_file_of_the_pair_is_a_harness_row_under_it(
        self, meter, tmp_path
    ):
        """#1177, S5. Either file of the pair may import a file, and the
        harness puts what it imports into every spawn beside it; a meter that
        read the pair as two flat files counted the `@` line and missed the
        file it imports. Each imported file is a harness row, named by the importing
        file's name, an arrow and the path as written, with `via` naming the
        importer, and the pair's line sums and names it. A backticked `@`, an
        address and a quoted path are not imports."""
        root, home = a_tree(tmp_path)
        write(
            str(root / "CLAUDE.md"),
            f"## Repo rules {ACCENT}\n@docs/repo.md\n"
            'A backticked `@` line, mail me@example.com, @"quoted.md".\n',
        )
        write(str(root / "docs" / "repo.md"), f"repo import {ACCENT}\n")
        write(
            str(home / ".claude" / "CLAUDE.md"),
            "# my rules\n@rules/mine.md\n",
        )
        mine = home / ".claude" / "rules" / "mine.md"
        write(str(mine), f"# mine {ACCENT}\n\nmy rules\n")
        data = meter.measure(str(root), str(home))
        files = data["agents"]["probe"]["files"]
        harness = [f for f in files if f["share"] == "harness"]
        assert [f["path"] for f in harness] == [
            "CLAUDE.md",
            "CLAUDE.md → docs/repo.md",
            "~/.claude/CLAUDE.md",
            "~/.claude/CLAUDE.md → rules/mine.md",
        ], [f["path"] for f in harness]
        assert [f.get("via") for f in harness] == [
            None,
            "CLAUDE.md",
            None,
            "~/.claude/CLAUDE.md",
        ]
        assert (harness[1]["bytes"], harness[1]["chars"]) == size_of(
            root / "docs" / "repo.md"
        )
        assert (harness[3]["bytes"], harness[3]["chars"]) == size_of(mine)
        total = data["agents"]["probe"]["total"]
        assert total["bytes"] == sum(f["bytes"] for f in files)
        text = meter.render(data)
        pair_line = next(c for c in rows_of(text) if c[0].startswith("CLAUDE.md pair"))
        assert "`~/.claude/CLAUDE.md → rules/mine.md`" in pair_line[0], pair_line
        assert "`CLAUDE.md → docs/repo.md`" in pair_line[0], pair_line
        assert pair_line[1] == f"{sum(f['bytes'] for f in harness):,}", pair_line
        by_first = {c[0]: c for c in rows_of(text)}
        imported = by_first["&nbsp;&nbsp;`~/.claude/CLAUDE.md → rules/mine.md`"]
        assert imported[1] == f"{harness[3]['bytes']:,}", imported
        assert "imported by `~/.claude/CLAUDE.md`" in imported[4], imported

    def test_an_import_a_fence_of_an_imported_file_quotes_is_no_row(
        self, meter, tmp_path
    ):
        """#1185, S5. Every hop is read the same way: `x.md`, which the pair
        imports, quotes `@y.md` inside a fence, so the harness loads `x.md`
        and not `y.md`, and `y.md` is no row."""
        root, home = a_tree(tmp_path)
        write(str(root / "CLAUDE.md"), f"## Repo rules {ACCENT}\n@x.md\n")
        write(str(root / "x.md"), "An example:\n\n```\n@y.md\n```\n")
        write(str(root / "y.md"), "y\n")
        data = meter.measure(str(root), str(home))
        harness = [
            f["path"]
            for f in data["agents"]["probe"]["files"]
            if f["share"] == "harness"
        ]
        assert harness == [
            "CLAUDE.md",
            "CLAUDE.md → x.md",
            "~/.claude/CLAUDE.md",
        ], harness

    def test_an_import_that_is_not_a_file_is_a_missing_row(self, meter, tmp_path):
        """#1177, S5. A dangling import loads nothing and says nothing in a
        session, so the meter says it: a path that is no file, or a directory,
        is a row of 0 bytes marked `missing`."""
        root, home = a_tree(tmp_path)
        write(
            str(home / ".claude" / "CLAUDE.md"),
            "@rules/gone.md\n@rules\n",
        )
        os.makedirs(home / ".claude" / "rules")
        data = meter.measure(str(root), str(home))
        imported = [f for f in data["agents"]["probe"]["files"] if "via" in f]
        assert [f["path"] for f in imported] == [
            "~/.claude/CLAUDE.md → rules/gone.md",
            "~/.claude/CLAUDE.md → rules",
        ]
        for row in imported:
            assert (row["bytes"], row.get("missing")) == (0, True), row
        text = meter.render(data)
        assert (
            "| &nbsp;&nbsp;`~/.claude/CLAUDE.md → rules` | 0 | 0 | 0 | missing |"
            in text
        ), text

    def test_one_real_path_imported_twice_is_one_row(self, meter, tmp_path):
        """#1177, S5. Claude Code reads a file once when two memory files
        import it by one path, so one real path is one row across the pair,
        under the first importer, however each file spells it; an import back
        to a file of the pair is no row either."""
        root, home = a_tree(tmp_path)
        shared = home / "shared.md"
        write(str(shared), f"shared {ACCENT}\n@.claude/CLAUDE.md\n@shared.md\n")
        write(str(root / "CLAUDE.md"), "## Repo rules\n@~/shared.md\n")
        write(str(home / ".claude" / "CLAUDE.md"), "@../shared.md\n@../shared.md\n")
        data = meter.measure(str(root), str(home))
        harness = [
            f["path"]
            for f in data["agents"]["probe"]["files"]
            if f["share"] == "harness"
        ]
        assert harness == [
            "CLAUDE.md",
            "CLAUDE.md → ~/shared.md",
            "~/.claude/CLAUDE.md",
        ], harness

    # --- S8: a session's share, the core the hook prints included -------------

    def test_the_session_table_carries_the_hook_row_at_the_bytes_the_hook_prints(
        self, meter, tmp_path
    ):
        """#1177 and #1430, S8. A session receives the core from the plugin's
        `SessionStart` hook, not from a memory file, so a meter that reads only
        the `CLAUDE.md` pair counts none of it. The session's table holds one
        row for the hook, whose bytes and characters are those of
        `lib/core.py#rendered` for the measured tree's core: the header naming
        the file, the core below its frontmatter and the closing line. The
        table is printed before the agents', and lists each file of the pair
        on a line of its own, each import under its importer."""
        root, home = a_tree(tmp_path)
        a_core(root)
        write(str(home / ".claude" / "CLAUDE.md"), "# my rules\n@rules/mine.md\n")
        write(str(home / ".claude" / "rules" / "mine.md"), f"mine {ACCENT}\n")
        printed = hook_output(root)
        assert printed.startswith("AgenticSeal core from "), printed
        raw, chars = len(printed.encode("utf-8")), len(printed)
        data = meter.measure(str(root), str(home))
        hooks = [f for f in data["session"]["files"] if f["share"] == "hook"]
        assert [f["path"] for f in hooks] == [HOOK_ROW], hooks
        assert (hooks[0]["bytes"], hooks[0]["chars"]) == (raw, chars), hooks[0]
        assert hooks[0]["bytes"] > hooks[0]["chars"], "the accent reached no count"
        text = meter.render(data)
        assert text.index(f"`{HOOK_ROW}`") < text.index("## probe"), text
        session_part = text[: text.index("## probe")]
        by_first = {cells[0]: cells for cells in rows_of(session_part)}
        line = by_first[f"`{HOOK_ROW}`"]
        assert line[1:3] == [f"{raw:,}", f"{chars:,}"], line
        assert "what the `SessionStart` hook prints" in line[4], line
        for row in data["session"]["files"][:-1]:
            name = f"`{row['path']}`"
            if "via" in row:
                name = f"&nbsp;&nbsp;{name}"
            assert by_first[name][1] == f"{row['bytes']:,}", (name, session_part)
        imported = by_first["&nbsp;&nbsp;`~/.claude/CLAUDE.md → rules/mine.md`"]
        assert "imported by `~/.claude/CLAUDE.md`" in imported[4], imported
        total = by_first["**total**"]
        assert total[1] == f"{data['session']['total']['bytes']:,}", total

    def test_the_json_carries_the_session_as_an_object_of_its_own(
        self, meter, tmp_path
    ):
        """#1177, S8. `session` holds the pair with each file their `@` lines
        import, as the agents' tables do, then the hook's row, and a total that
        sums them. Every token figure is estimated at the assumed ratio and
        carries the one basis every agent's figure carries."""
        root, home = a_tree(tmp_path)
        a_core(root)
        write(str(home / ".claude" / "CLAUDE.md"), "# my rules\n@rules/mine.md\n")
        write(str(home / ".claude" / "rules" / "mine.md"), f"mine {ACCENT}\n")
        done = run(["--root", str(root), "--json"], home, cwd=str(tmp_path))
        assert done.returncode == 0, done.stderr
        session = json.loads(done.stdout)["session"]
        assert [(f["path"], f["share"]) for f in session["files"]] == [
            ("CLAUDE.md", "harness"),
            ("~/.claude/CLAUDE.md", "harness"),
            ("~/.claude/CLAUDE.md → rules/mine.md", "harness"),
            (HOOK_ROW, "hook"),
        ], session["files"]
        assert session["total"]["bytes"] == sum(f["bytes"] for f in session["files"])
        assert session["total"]["chars"] == sum(f["chars"] for f in session["files"])
        assert session["total"]["tokens"] == sum(f["tokens"] for f in session["files"])
        assert str(tmp_path) not in done.stdout, "an absolute path reached the JSON"
        for row in [*session["files"], session["total"]]:
            assert row["basis"] == BASIS, row
        for row in session["files"]:
            assert row["tokens"] == round(row["bytes"] / meter.ASSUMED_RATIO), row

    def test_no_agent_table_carries_the_hook_row(self, meter, tmp_path):
        """#1177 and #1430, S8. The hook's output reaches the session and no
        subagent, so the core an agent reads is the one its `skills:` list
        names, once, and the hook's row stands in the session's table
        alone."""
        root, home = a_tree(tmp_path, skills=("alpha", "core"), extra_agent=True)
        a_core(root)
        data = meter.measure(str(root), str(home))
        assert [f["path"] for f in data["session"]["files"]][-1] == HOOK_ROW
        for name, agent in data["agents"].items():
            assert not [
                f for f in agent["files"] if f["share"] == "hook" or "hook" in f["path"]
            ], name
            assert agent["total"]["bytes"] == sum(f["bytes"] for f in agent["files"])
        cores = [
            f["path"]
            for f in data["agents"]["probe"]["files"]
            if f["path"].startswith("skills/core/")
        ]
        assert cores == ["skills/core/SKILL.md"], cores
        assert meter.render(data).count(f"`{HOOK_ROW}`") == 1

    def test_a_tree_without_the_core_has_a_missing_hook_row(self, meter, tmp_path):
        """#1177, S8's before side. A tree that holds no `skills/core/SKILL.md`,
        such as a release before 0.25.0, prints no core into a session, so the
        hook's row is 0 bytes marked `missing` rather than the hook's one-line
        refusal, which no hook of that tree prints."""
        root, home = a_tree(tmp_path)
        data = meter.measure(str(root), str(home))
        hook = data["session"]["files"][-1]
        assert (hook["path"], hook["bytes"], hook.get("missing")) == (
            HOOK_ROW,
            0,
            True,
        ), hook
        text = meter.render(data)
        line = next(c for c in rows_of(text) if c[0] == f"`{HOOK_ROW}`")
        assert line[1:4] == ["0", "0", "0"], line
        assert line[4].startswith("missing"), line
        assert "so no hook prints one" in line[4], line

    def test_a_root_on_another_drive_than_the_cwd_is_named_as_given(
        self, meter, monkeypatch, tmp_path
    ):
        """PR #329's Windows leg, run 34424160836: `"root": os.path.relpath(root)`
        raised `ValueError: path is on mount 'C:', start on mount 'D:'` for every
        fixture root under pytest's temp dir -- sixteen cases -- because the
        checkout sits on `D:`. A relative root is a courtesy. `relpath` is
        monkeypatched to raise the way `ntpath` does, so the case is red on every
        platform against a `measure` that lets the error through; the run then
        finishes and names the root as given."""
        root, home = a_tree(tmp_path)

        def across_drives(path, start=os.curdir):
            raise ValueError("path is on mount 'C:', start on mount 'D:'")

        monkeypatch.setattr(os.path, "relpath", across_drives)
        data = meter.measure(str(root), str(home))
        assert data["root"] == str(root)
        assert data["agents"]["probe"]["total"]["bytes"] > 0

    def test_a_skill_the_list_names_and_the_tree_lacks_is_a_row_not_a_crash(
        self, meter, tmp_path
    ):
        root, home = a_tree(tmp_path, skills=("alpha", "ghost"))
        data = meter.measure(str(root), str(home))
        ghost = next(
            f for f in data["agents"]["probe"]["files"] if "ghost" in f["path"]
        )
        assert ghost["bytes"] == 0
        assert ghost.get("missing") is True
        assert "missing" in meter.render(data)

    # --- every token figure carries a basis -----------------------------------

    def test_every_token_figure_reads_estimated_at_the_assumed_ratio(
        self, meter, tmp_path
    ):
        """Every figure is an estimate at the assumed ratio; each FILE row is that
        row's bytes divided by it, and the total is the SUM of the rows.

        The two are not one number. Rounding each row and adding is not adding and
        rounding once, and PR #329's Windows leg found the gap: the fixture's lines
        are CRLF there, the sizes move, and the total read 81 tokens over 257 bytes
        where `round(257 / 3.2)` is 80. Nothing is measured twice -- every row's
        bytes are the file's bytes on disk, and 30 + 33 + 6 + 6 + 6 is 81. What the
        total may not be is a second division of the sum, or the column a reader
        adds up stops adding up to the total under it.

        The CRLF block below writes those endings explicitly, so the divergence is
        exercised on every platform rather than on the one whose fixture happens to
        round the other way."""
        root, home = a_tree(tmp_path)
        data = meter.measure(str(root), str(home))
        probe = data["agents"]["probe"]
        for row in [*probe["files"], probe["total"]]:
            assert row["basis"] == BASIS, row
        for row in probe["files"]:
            assert row["tokens"] == round(row["bytes"] / meter.ASSUMED_RATIO), row
        assert probe["total"]["tokens"] == sum(f["tokens"] for f in probe["files"])
        for base in (root, home):
            for folder, _subs, names in os.walk(base):
                for name in names:
                    path = os.path.join(folder, name)
                    with open(path, "rb") as handle:
                        raw = handle.read()
                    with open(path, "wb") as handle:
                        handle.write(
                            raw.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
                        )
        crlf = meter.measure(str(root), str(home))["agents"]["probe"]
        for row in crlf["files"]:
            on_disk = (
                os.path.join(str(home), ".claude", "CLAUDE.md")
                if row["path"].startswith("~/")
                else os.path.join(str(root), row["path"])
            )
            assert row["bytes"] == os.path.getsize(on_disk), row
            assert row["tokens"] == round(row["bytes"] / meter.ASSUMED_RATIO), row
        summed = sum(f["tokens"] for f in crlf["files"])
        assert crlf["total"]["tokens"] == summed, crlf["total"]
        assert summed != round(crlf["total"]["bytes"] / meter.ASSUMED_RATIO), (
            "the CRLF fixture no longer exercises the divergence: adding the "
            "rounded rows and dividing the total agree here, so this block would "
            "pass whichever number the total was built from"
        )
        text = meter.render(data)
        for cells in rows_of(text):
            if cells and cells[0] in ("File", "Section"):
                continue
            # A `missing` row's zeros count a file that is not there, not
            # tokens anything estimated: the fixture's tree holds no core, so
            # the session's hook row is one.
            if len(cells) >= 5 and cells[4].startswith("missing"):
                continue
            if len(cells) >= 5 and re.fullmatch(r"[\d,]+", cells[3]):
                assert cells[4].startswith(BASIS), cells

    def test_a_user_level_skill_shadows_the_trees_and_the_row_says_so(
        self, meter, tmp_path
    ):
        """Measured on the machine that wrote this: `agents/crafter.md` lists
        `writing-style`, and the harness resolved the bare name to
        `~/.claude/skills/writing-style/SKILL.md` (25,834 B) rather than the
        plugin's (19,762 B). The row reports the tree's file and notes the
        shadow."""
        root, home = a_tree(tmp_path)
        shadow = home / ".claude" / "skills" / "alpha" / "SKILL.md"
        write(str(shadow), "# alpha, the user's own\n" + "x" * 500 + "\n")
        data = meter.measure(str(root), str(home))
        alpha = data["agents"]["probe"]["files"][1]
        assert alpha["path"] == "skills/alpha/SKILL.md"
        assert alpha["bytes"] == size_of(root / "skills" / "alpha" / "SKILL.md")[0]
        assert alpha["shadow"] == {
            "path": "~/.claude/skills/alpha/SKILL.md",
            "bytes": size_of(shadow)[0],
        }
        assert "shadowed" in meter.render(data)

    def test_an_inline_skills_list_is_read(self, meter, tmp_path):
        """Round 1, finding 3. `skills: [a, b]` is the same field in YAML's
        flow form, and the meter read it as no skills — the definition then
        measured as its whole payload, and the check that shares the parser had
        nothing to check. Q6 ships the meter for users' own definitions, which is
        where the other spelling arrives."""
        assert meter.frontmatter("---\nname: p\nskills: [alpha, beta]\n---\n") == (
            "p",
            ["alpha", "beta"],
        )
        assert meter.frontmatter("---\nname: p\nskills: alpha, 'beta'\n---\n") == (
            "p",
            ["alpha", "beta"],
        )
        assert meter.frontmatter("---\nname: p\nskills:\n- alpha\n- beta\n---\n") == (
            "p",
            ["alpha", "beta"],
        ), "an unindented block list is a list too"
        root, home = a_tree(tmp_path)
        write(
            str(root / "agents" / "probe.md"),
            "---\nname: probe\nskills: [alpha, beta]\n---\n# probe\n",
        )
        data = meter.measure(str(root), str(home))
        paths = [f["path"] for f in data["agents"]["probe"]["files"]]
        assert "skills/alpha/SKILL.md" in paths and "skills/beta/SKILL.md" in paths

    @pytest.mark.parametrize(
        "text, expected",
        [
            (
                f"---\nname: p\nskills:\n- alpha{LS}beta\n---\n",
                ("p", [f"alpha{LS}beta"]),
            ),
            ("---\rname: p\rskills: [alpha]\r---\r", ("p", ["alpha"])),
        ],
        ids=["U+2028 inside an entry", "CR line ends"],
    )
    def test_a_frontmatter_line_ends_only_where_yaml_ends_it(
        self, meter, text, expected
    ):
        """#1198, Scope item 10. YAML 1.2 ends a line at LF, CR or CRLF and
        nowhere else, so a `skills:` entry holding U+2028 is one entry. Seen
        red against `str.splitlines`, which ends a line at U+2028 too and read
        `alpha` alone. `read` decodes the bytes as they are, so the CR shape
        pins the universal newlines the LF split comes after."""
        assert meter.frontmatter(text) == expected


class Test_imports_of:
    """#1177, `frame/design.md` *Scope* item 5: how an `@` line resolves, as
    code.claude.com/docs/en/memory.md states it -- relative to the file that
    holds it, `~` as the home, at most four hops. #1185: where an import is
    read, as the same page states it -- in the file's live text alone, with
    a backslash carrying a path past a space."""

    def test_accepts_a_tilde_path_as_the_home_it_was_given(
        self, meter, monkeypatch, tmp_path
    ):
        """The home the meter was given, not the process's: the cases run the
        meter against a scratch home, and `expanduser` would read the
        machine's."""
        home = tmp_path / "home"
        monkeypatch.setenv("HOME", str(tmp_path / "elsewhere"))
        monkeypatch.setenv("USERPROFILE", str(tmp_path / "elsewhere"))
        importer = tmp_path / "repo" / "CLAUDE.md"
        write(str(importer), "@~/notes/a.md\n")
        write(str(home / "notes" / "a.md"), "a\n")
        found = meter.imports_of(str(importer), str(home))
        assert found == [
            (("~/notes/a.md",), os.path.realpath(home / "notes" / "a.md"))
        ], found

    def test_accepts_a_relative_path_against_the_importing_file(
        self, meter, monkeypatch, tmp_path
    ):
        """Against the file that holds the line, at every hop: `inner/x.md`
        imports `y.md`, which is `inner/y.md`, not the top file's `y.md` and
        not the working directory's."""
        top = tmp_path / "a" / "CLAUDE.md"
        write(str(top), "@inner/x.md\n")
        write(str(tmp_path / "a" / "inner" / "x.md"), "@y.md\n")
        write(str(tmp_path / "a" / "inner" / "y.md"), "the right one\n")
        write(str(tmp_path / "a" / "y.md"), "a decoy beside the top file\n")
        write(str(tmp_path / "y.md"), "a decoy in the working directory\n")
        monkeypatch.chdir(tmp_path)
        found = meter.imports_of(str(top), str(tmp_path / "home"))
        assert found == [
            (("inner/x.md",), os.path.realpath(tmp_path / "a" / "inner" / "x.md")),
            (
                ("inner/x.md", "y.md"),
                os.path.realpath(tmp_path / "a" / "inner" / "y.md"),
            ),
        ], found

    def test_accepts_a_symlink_as_its_target(self, meter, tmp_path):
        """#1177. An import through a symlink loads the target, so the row is
        the target's, by its real path and its bytes."""
        target = tmp_path / "clone" / "core.md"
        write(str(target), f"# core {ACCENT}\n" + "x" * 300 + "\n")
        home = tmp_path / "home"
        os.makedirs(home / ".claude")
        symlink_or_skip(str(target), str(home / ".claude" / "core.md"))
        write(str(home / ".claude" / "CLAUDE.md"), "@core.md\n")
        found = meter.imports_of(str(home / ".claude" / "CLAUDE.md"), str(home))
        assert found == [(("core.md",), os.path.realpath(target))], found
        root, _home = a_tree(tmp_path / "tree")
        data = meter.measure(str(root), str(home))
        row = next(f for f in data["agents"]["probe"]["files"] if "via" in f)
        assert (row["bytes"], row["chars"]) == size_of(target), row

    def test_refuses_an_import_past_the_fourth_hop(self, meter, tmp_path):
        """The docs' "maximum depth of four hops": a chain of five imports
        loads four files, and the fifth is no row at all."""
        top = tmp_path / "CLAUDE.md"
        write(str(top), "@h1.md\n")
        for hop in range(1, 6):
            write(str(tmp_path / f"h{hop}.md"), f"@h{hop + 1}.md\n")
        found = meter.imports_of(str(top), str(tmp_path / "home"))
        assert [chain[-1] for chain, _real in found] == [
            "h1.md",
            "h2.md",
            "h3.md",
            "h4.md",
        ], found
        assert found[-1][0] == ("h1.md", "h2.md", "h3.md", "h4.md")

    @staticmethod
    def written(meter, tmp_path, text):
        """The chains `imports_of` returns for a `CLAUDE.md` holding TEXT,
        with `a.md` and `b.md` beside it, so a wrong reading names a file
        that exists."""
        importer = tmp_path / "CLAUDE.md"
        write(str(importer), text)
        for name in ("a.md", "b.md"):
            write(str(tmp_path / name), f"{name}\n")
        found = meter.imports_of(str(importer), str(tmp_path / "home"))
        return [chain for chain, _real in found]

    def test_refuses_an_import_a_fenced_code_block_quotes(self, meter, tmp_path):
        """#1185, S1. "Import parsing skips Markdown code spans and fenced
        code blocks" (code.claude.com/docs/en/memory.md): an `@` line a fence
        quotes is an example, and the harness loads nothing for it. The
        import after the fence closes is read."""
        text = "An example:\n\n```\n@a.md\n```\n@b.md\n"
        assert self.written(meter, tmp_path, text) == [("b.md",)]

    @pytest.mark.parametrize(
        "text",
        [
            "~~~\n@a.md\n~~~\n@b.md\n",
            "````\n```\n@a.md\n```\n````\n@b.md\n",
            "@b.md\n\n```\n@a.md\n\n## Later\n@a.md\n",
        ],
        ids=[
            "a tilde fence",
            "a three-backtick line inside a four-backtick fence",
            "a fence nobody closed",
        ],
    )
    def test_refuses_an_import_in_each_shape_of_a_fence(self, meter, tmp_path, text):
        """#1185, S2. A fence is the shared rule's, `fence_opener` and
        `fence_closes` (#584): a tilde fence is one, a shorter run does not
        close a longer fence, and a fence nobody closed runs to the end of
        the file, as CommonMark 4.5 says and Claude Code's lexer reads it
        (`frame/design.md` G3 of #1185)."""
        assert self.written(meter, tmp_path, text) == [("b.md",)]

    @pytest.mark.parametrize(
        "text",
        [
            "Run `cat @a.md` then @b.md\n",
            "Run `` @a.md `` then @b.md\n",
            "Run `cat @a.md\n@a.md` then @b.md\n",
        ],
        ids=[
            "a span on its own line",
            "a span of two backticks",
            "a span closed on the next line of its paragraph",
        ],
    )
    def test_refuses_an_import_a_code_span_holds(self, meter, tmp_path, text):
        """#1185, S3. The docs skip a code span in the same sentence as a
        fence. A span runs from a backtick run to the next run of the same
        length, on its line or, before its paragraph ends, on a later one
        (`lib/lines.py#_partner_ahead`), and the import after it is
        read."""
        assert self.written(meter, tmp_path, text) == [("b.md",)]

    def test_accepts_an_import_after_a_backtick_its_paragraph_never_closes(
        self, meter, tmp_path
    ):
        """#1185, S3. A backtick run whose partner does not arrive before
        the paragraph ends opens no span, so the import in the next
        paragraph is read."""
        text = "A lone ` here\n\n@b.md and a ` there\n"
        assert self.written(meter, tmp_path, text) == [("b.md",)]

    @pytest.mark.parametrize(
        "text",
        [
            "<!-- @a.md --> then @b.md\n",
            "<!--\n@a.md\n-->\n@b.md\n",
            "@b.md\n<!-- open\n\n@a.md\n",
        ],
        ids=[
            "a comment before an import on its line",
            "a comment over three lines",
            "a comment nobody closed",
        ],
    )
    def test_refuses_an_import_an_html_comment_holds(self, meter, tmp_path, text):
        """#1185, S4. A block-level HTML comment is stripped before the file
        reaches the context (code.claude.com/docs/en/memory.md *How CLAUDE.md
        files load*), and Claude Code scans what is left of the comment's
        token (`frame/design.md` G3 of #1185). A comment runs from `<!--` to
        the next `-->`, and one nobody closed hides the rest of the file."""
        assert self.written(meter, tmp_path, text) == [("b.md",)]

    def test_accepts_a_backslash_before_a_space_as_part_of_the_path(
        self, meter, tmp_path
    ):
        """#1185, S6. "To import a file whose path contains spaces, put a
        backslash before each space. Without the backslashes, the path ends
        at the first space" (code.claude.com/docs/en/memory.md). The target
        is the path with each `\\ ` read as a space, and the chain keeps the
        path as written."""
        importer = tmp_path / "CLAUDE.md"
        write(str(importer), "@Design\\ Docs/api.md\n")
        target = tmp_path / "Design Docs" / "api.md"
        write(str(target), "api\n")
        found = meter.imports_of(str(importer), str(tmp_path / "home"))
        assert found == [(("Design\\ Docs/api.md",), os.path.realpath(target))], found


class Test_module:
    @pytest.mark.parametrize(
        "args", [["--root", "{root}"], ["--help"]], ids=["a-run", "help"]
    )
    def test_a_script_copied_alone_exits_2_and_names_what_it_misses(
        self, tmp_path, meter, args
    ):
        """#590 and #610, and S4 of #1482. A copy of this script taken
        without its siblings exits 2, with the loader's one sentence naming
        the absent `lib/sibling.py` by its path; here 1 means an input that
        could not be measured, and 2 that nothing was read. The copy stands
        at its path in a plugin that holds nothing else, so the path is
        under the copy's plugin root. The sentence names no purpose (#1482). `--help` reaches the sentence too, because the guard stands at
        import and reads no argument (#1482, A13)."""
        script = TARGET
        alone = tmp_path / "alone"
        copy = alone.joinpath(*script.split("/"))
        copy.parent.mkdir(parents=True)
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
        said = meter.sibling.MISSING.format(path=str(alone / "lib" / "sibling.py"))
        assert done.stderr == said + "\n", done.stderr

    def test_a_copy_without_the_scan_exits_2_on_a_run_that_reads_a_claude_md(
        self, tmp_path, meter
    ):
        """#1185. Every read of a `CLAUDE.md` that exists asks
        `lib/blocks.py` for its lines and `lib/lines.py` where its live text
        is, so a copy that holds the loader and the core hook's module and
        neither of those exits 2 with no flag at all, in the loader's
        sentence naming the first it loads, `lib/blocks.py`.
        Every run loads `lib/core.py` first, so this copy carries it and
        `lib/optin.py`, the one module it loads."""
        alone = tmp_path / "alone"
        for rel in (TARGET, "lib/sibling.py", "lib/core.py", "lib/optin.py"):
            copy = alone.joinpath(*rel.split("/"))
            copy.parent.mkdir(parents=True, exist_ok=True)
            with open(os.path.join(ROOT, *rel.split("/")), encoding="utf-8") as f:
                copy.write_text(f.read(), encoding="utf-8")
        repo = tmp_path / "repo"
        repo.mkdir()
        (repo / "CLAUDE.md").write_text("# rules\n", encoding="utf-8")
        home = tmp_path / "home"
        home.mkdir()
        done = subprocess.run(
            [
                sys.executable,
                str(alone.joinpath(*TARGET.split("/"))),
                "--root",
                str(repo),
            ],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            env=dict(os.environ, HOME=str(home), USERPROFILE=str(home)),
            cwd=str(repo),
        )
        assert done.returncode == 2, (done.returncode, done.stderr)
        assert "Traceback" not in done.stderr, done.stderr
        reader = alone / "lib" / "blocks.py"
        assert meter.sibling.MISSING.format(path=str(reader)) in done.stderr, (
            done.stderr
        )

    def test_json_carries_the_same_numbers_as_the_text_and_no_machine_path(
        self, tmp_path
    ):
        """Each agent row's bytes and chars sit on its own table line, and the
        `CLAUDE.md` pair's on the pair line as a sum -- the text never prints a
        pair file alone. The first spelling of this case looked each row's byte
        count up as a substring of the whole report, and passed on POSIX because
        the 17-byte `CLAUDE.md` fixture matched the 17-byte `beta` row's cell;
        on Windows, where the fixture writes CRLF and the counts move, it failed
        on `CLAUDE.md` (PR #329's Windows leg, run 34424160836)."""
        root, home = a_tree(tmp_path)
        as_json = run(["--root", str(root), "--json"], home, cwd=str(tmp_path))
        assert as_json.returncode == 0, as_json.stderr
        data = json.loads(as_json.stdout)
        as_text = run(["--root", str(root)], home, cwd=str(tmp_path))
        assert as_text.returncode == 0, as_text.stderr
        rows = rows_of(as_text.stdout)
        by_first = {cells[0]: cells for cells in rows}
        files = data["agents"]["probe"]["files"]
        for row in files:
            if row["share"] == "harness":
                continue
            cells = by_first[f"`{row['path']}`"]
            assert cells[1:3] == [f"{row['bytes']:,}", f"{row['chars']:,}"], row["path"]
        pair = [r for r in files if r["share"] == "harness"]
        assert len(pair) == 2
        pair_line = next(c for c in rows if c[0].startswith("CLAUDE.md pair"))
        assert pair_line[1:3] == [
            f"{sum(r['bytes'] for r in pair):,}",
            f"{sum(r['chars'] for r in pair):,}",
        ], pair_line
        assert str(home) not in as_json.stdout
        assert str(tmp_path) not in as_json.stdout, "an absolute path reached the JSON"
        assert data["root"] == "plugin"
        assert "measured_at" in data

    # --- #1367: the config directory in use --------------------------------------

    def test_the_pair_reads_the_claude_md_of_the_config_directory_in_use(
        self, tmp_path
    ):
        """#1367, S3. Claude Code reads the user's `CLAUDE.md` in the
        directory `CLAUDE_CONFIG_DIR` names. Under a set variable the
        session's and each agent's pair row is that file, labelled
        `$CLAUDE_CONFIG_DIR/CLAUDE.md` so no absolute path reaches the
        output, and no row reads the file under HOME."""
        root, home, config = two_user_dirs(tmp_path)
        done = run(
            ["--root", str(root), "--json"],
            home,
            cwd=str(tmp_path),
            extra={"CLAUDE_CONFIG_DIR": str(config)},
        )
        assert done.returncode == 0, done.stderr
        data = json.loads(done.stdout)
        tables = {
            "session": data["session"]["files"],
            **{name: agent["files"] for name, agent in data["agents"].items()},
        }
        not_read = size_of(home / ".claude" / "CLAUDE.md")[0]
        for name, files in tables.items():
            pair = [f for f in files if f["share"] == "harness"]
            assert [f["path"] for f in pair] == [
                "CLAUDE.md",
                "$CLAUDE_CONFIG_DIR/CLAUDE.md",
            ], (name, pair)
            assert (pair[1]["bytes"], pair[1]["chars"]) == size_of(
                config / "CLAUDE.md"
            ), name
            assert not_read not in [f["bytes"] for f in files], name
        assert str(tmp_path) not in done.stdout, "an absolute path reached the JSON"

    def test_a_skill_shadow_is_read_in_the_config_directory_in_use(self, tmp_path):
        """#1367, S4. A user skill shadowing the plugin's stands in the
        directory `CLAUDE_CONFIG_DIR` names, so under a set variable the
        row's shadow is that file, labelled `$CLAUDE_CONFIG_DIR/skills/...`,
        with its bytes."""
        root, home, config = two_user_dirs(tmp_path)
        done = run(
            ["--root", str(root), "--json"],
            home,
            cwd=str(tmp_path),
            extra={"CLAUDE_CONFIG_DIR": str(config)},
        )
        assert done.returncode == 0, done.stderr
        alpha = json.loads(done.stdout)["agents"]["probe"]["files"][1]
        assert alpha["path"] == "skills/alpha/SKILL.md"
        assert alpha["shadow"] == {
            "path": "$CLAUDE_CONFIG_DIR/skills/alpha/SKILL.md",
            "bytes": size_of(config / "skills" / "alpha" / "SKILL.md")[0],
        }

    @pytest.mark.parametrize(
        "extra", [None, {"CLAUDE_CONFIG_DIR": ""}], ids=["unset", "empty"]
    )
    def test_an_unset_or_empty_variable_reads_the_home_directory(self, tmp_path, extra):
        """#1367, S5. `main` passes the variable as the process has it, and
        `user_dir` reads an empty value as unset, as the shell's `:-` does.
        Either way the pair row and the shadow are the files under
        `HOME/.claude`, under the labels a run read before #1367."""
        root, home, _config = two_user_dirs(tmp_path)
        done = run(
            ["--root", str(root), "--json"], home, cwd=str(tmp_path), extra=extra
        )
        assert done.returncode == 0, done.stderr
        files = json.loads(done.stdout)["agents"]["probe"]["files"]
        pair = [f for f in files if f["share"] == "harness"]
        assert [f["path"] for f in pair] == ["CLAUDE.md", "~/.claude/CLAUDE.md"]
        assert (pair[1]["bytes"], pair[1]["chars"]) == size_of(
            home / ".claude" / "CLAUDE.md"
        )
        assert files[1]["shadow"] == {
            "path": "~/.claude/skills/alpha/SKILL.md",
            "bytes": size_of(home / ".claude" / "skills" / "alpha" / "SKILL.md")[0],
        }

    def test_an_import_from_home_stays_under_the_home_directory(self, tmp_path):
        """#1367, S6. A `@~/` import is the home directory, which a set
        `CLAUDE_CONFIG_DIR` does not move (`imports_of`), so the config
        directory's `CLAUDE.md` importing `@~/shared.md` reads
        `HOME/shared.md` and not the file of that name in the config
        directory."""
        root, home, config = two_user_dirs(tmp_path)
        write(str(config / "CLAUDE.md"), "## Config rules\n@~/shared.md\n")
        write(str(home / "shared.md"), "the home's shared\n" + "h" * 50 + "\n")
        write(str(config / "shared.md"), "the config's shared\n" + "c" * 70 + "\n")
        done = run(
            ["--root", str(root), "--json"],
            home,
            cwd=str(tmp_path),
            extra={"CLAUDE_CONFIG_DIR": str(config)},
        )
        assert done.returncode == 0, done.stderr
        files = json.loads(done.stdout)["agents"]["probe"]["files"]
        pair = [f for f in files if f["share"] == "harness"]
        assert [(f["path"], f.get("via")) for f in pair] == [
            ("CLAUDE.md", None),
            ("$CLAUDE_CONFIG_DIR/CLAUDE.md", None),
            (
                "$CLAUDE_CONFIG_DIR/CLAUDE.md → ~/shared.md",
                "$CLAUDE_CONFIG_DIR/CLAUDE.md",
            ),
        ], pair
        assert (pair[2]["bytes"], pair[2]["chars"]) == size_of(home / "shared.md")

    # --- the command ------------------------------------------------------------

    def test_the_command_a_person_types_runs_the_meter(self):
        """`bin/` is on the Bash tool's PATH while the plugin is enabled, and
        cmd.exe resolves `bin/seal.cmd` through PATHEXT; `seal payload` hands
        its arguments to THIS script, whose help names what it measures."""
        wrapper = os.path.join(BIN, "seal")
        command = (
            [os.environ.get("COMSPEC", "cmd.exe"), "/c", f"{wrapper}.cmd"]
            if os.name == "nt"
            else [wrapper]
        )
        done = subprocess.run(
            [*command, "payload", "--help"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
        assert done.returncode == 0, done.stderr
        assert "what a session's and each agent's startup payload" in done.stdout, (
            done.stdout
        )


test_census = census_case(TARGET)
