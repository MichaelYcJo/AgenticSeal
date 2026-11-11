"""`/agentic:update` reads the plugins of the config directory in use (#1184).

Claude Code keeps its plugins under the directory `CLAUDE_CONFIG_DIR`
names, and under `~/.claude` where the variable is unset. A command of
`skills/update/SKILL.md` that names `~/.claude` reads, under a set
variable, an install record, a marketplace clone and a version cache that
are not the ones the session loaded.

Each case runs a command as the skill's bash fence spells it, under
`bash -c`, with `HOME` and `CLAUDE_CONFIG_DIR` naming two scratch
directories that hold different answers, so a command that reads the
fixed path prints the other directory's. Each skips where `bash` is no
usable shell (`shell_probe`, for the reason its docstring gives). Step
4b's command reads the data directory the skill body receives, which the
case writes into the command as the harness substitutes it (#1430).
"""

import json
import os
import re
import shlex
import subprocess
import sys

import pytest
from conftest import ROOT, git, read, shell_probe

UPDATE = os.path.join(ROOT, "skills", "update", "SKILL.md")
# The config directory in use, as every command of the skill spells it.
SPELLING = "${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
FENCE = re.compile(r"```bash\n(.*?)\n```", re.S)


def step(number, following):
    """The text of update step NUMBER, from its number to FOLLOWING's."""
    text = read(UPDATE)
    return text[text.index(f"**{number}.") : text.index(f"**{following}.")]


def run_bash(script, home, config, cwd):
    """SCRIPT under `bash -c` from CWD, with HOME and CLAUDE_CONFIG_DIR set
    to the two scratch directories, and this interpreter for `python3`."""
    why = shell_probe("bash")
    if why:
        pytest.skip(f"bash: {why} -- the update skill's commands are bash")
    script = script.replace("python3 -c", f'"{sys.executable}" -c')
    env = dict(os.environ, HOME=str(home), CLAUDE_CONFIG_DIR=str(config))
    return subprocess.run(
        ["bash", "-c", script],
        cwd=cwd,
        env=env,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def install(claude_dir, copy, version):
    """An `installed_plugins.json` under CLAUDE_DIR whose one `installPath`
    is COPY, and a `plugin.json` in COPY at VERSION."""
    (copy / ".claude-plugin").mkdir(parents=True)
    (copy / ".claude-plugin" / "plugin.json").write_text(
        json.dumps({"name": "agentic", "version": version}), encoding="utf-8"
    )
    record = claude_dir / "plugins" / "installed_plugins.json"
    record.parent.mkdir(parents=True)
    record.write_text(
        json.dumps({"plugins": {"agentic@agenticseal": [{"installPath": str(copy)}]}}),
        encoding="utf-8",
    )


def test_step_2b_reads_the_copy_the_config_directory_installed(tmp_path):
    """S3. The install record and the copy it names are the config
    directory's, so step 2b's two commands print the version of that copy
    and not of the one `~/.claude` names."""
    home, config = tmp_path / "home", tmp_path / "config"
    install(home / ".claude", tmp_path / "copy-home", "9.9.0")
    install(config, tmp_path / "copy-in-use", "9.9.1")
    block = FENCE.findall(step("2b", "3"))[0]
    # The block's two `python3 -c` programs the session runs, which
    # `run_bash` points at this interpreter.
    assert block.count("python3 -c") == 2, block
    out = run_bash(block, home, config, tmp_path)
    assert out.returncode == 0, out.stdout + out.stderr
    assert out.stdout.strip() == "9.9.1", out.stdout + out.stderr


def test_step_2b_prints_the_repair_with_this_sessions_paths(tmp_path):
    """Round 1 of #1184, finding 1. The user types the repair in a terminal
    of their own, which holds neither `$p` nor, unless it is exported there,
    `CLAUDE_CONFIG_DIR`. So the block the session runs reads the copy and
    prints the repair, and runs nothing else. The repair names the copy the
    config directory's record names and that directory's clone, written out
    and quoted, so a path holding a space stays one word when it is typed."""
    home, config = tmp_path / "home", tmp_path / "con fig"
    copy = tmp_path / "copy in use"
    install(home / ".claude", tmp_path / "copy-home", "9.9.0")
    install(config, copy, "9.9.1")
    block = FENCE.findall(step("2b", "3"))[1]
    lines = block.splitlines()
    # The block's two shell lines the session runs, the assignment that reads
    # the copy and the `printf` that prints the repair.
    assert len(lines) == 2, block
    assert lines[0].startswith("p=$(") and lines[1].startswith("printf "), (
        "the repair block runs more than its read and its print"
    )
    out = run_bash(block, home, config, tmp_path)
    assert out.returncode == 0, out.stdout + out.stderr
    assert [shlex.split(line) for line in out.stdout.splitlines()] == [
        ["mv", str(copy), f"{copy}.stale.bak"],
        [
            "rsync",
            "-a",
            "--exclude",
            ".git",
            f"{config}/plugins/marketplaces/agenticseal/",
            f"{copy}/",
        ],
        ["mkdir", "-p", f"{copy}/.in_use"],
    ], out.stdout


def test_step_2b_prints_no_repair_where_the_record_cannot_be_read(tmp_path):
    """Round 2 of #1184, finding 1. Where the install record cannot be read,
    `p` is empty, and a repair printed from it would copy the clone into
    `/`. So the repair block prints nothing and fails."""
    home, config = tmp_path / "home", tmp_path / "config"
    home.mkdir()
    config.mkdir()
    block = FENCE.findall(step("2b", "3"))[1]
    out = run_bash(block, home, config, tmp_path)
    assert out.returncode != 0, out.stdout
    assert out.stdout == "", out.stdout


def test_step_3_takes_the_repository_from_the_config_directorys_clone(tmp_path):
    """S4. The marketplace clone is the config directory's, so step 3's
    `repo=` line yields that clone's `owner/repo`. Nothing reaches the
    network: the line reads a remote's URL and no more."""
    home, config = tmp_path / "home", tmp_path / "config"
    for claude_dir, url in (
        (home / ".claude", "git@github.com:owner-home/repo-home.git"),
        (config, "https://github.com/owner-in-use/repo-in-use.git"),
    ):
        clone = claude_dir / "plugins" / "marketplaces" / "agenticseal"
        clone.mkdir(parents=True)
        git(clone, "init", "-q")
        git(clone, "remote", "add", "origin", url)
    lines = FENCE.findall(step("3", "4"))[0].splitlines()
    repo = [line for line in lines if line.startswith("repo=$(")]
    # The one shell assignment of the repository, which the case runs alone.
    assert len(repo) == 1, lines
    out = run_bash(repo[0] + '\nprintf "%s" "$repo"', home, config, tmp_path)
    assert out.returncode == 0, out.stdout + out.stderr
    assert out.stdout == "owner-in-use/repo-in-use", out.stdout + out.stderr


def test_step_4b_reads_the_old_launcher_and_writes_nothing(tmp_path):
    """#1430. The plugin's `Stop` hook draws the stamp, so step 4b asks
    nothing and writes nothing. Its one command reads whether the launcher a
    release from 0.33.0 to 0.34.1 wrote stands under the data directory,
    which the skill body receives substituted and the case writes in the
    same way, and its row names the settings file and the command of the
    entry the person removes by hand. What the row says of the order is the
    proofer's to read."""
    text = step("4b", "5")
    (block,) = FENCE.findall(text)
    home, config = tmp_path / "home", tmp_path / "config"
    data = tmp_path / "data dir"
    data.mkdir()

    def said(directory):
        before = sorted(tmp_path.rglob("*"))
        out = run_bash(
            block.replace("${CLAUDE_PLUGIN_DATA}", directory), home, config, tmp_path
        )
        assert out.returncode == 0, out.stdout + out.stderr
        assert sorted(tmp_path.rglob("*")) == before, "step 4b wrote a file"
        return out.stdout

    assert said(str(data)) == "no launcher\n"
    (data / "stamp.py").write_text("", encoding="utf-8")
    assert said(str(data)) == f"launcher {data}/stamp.py\n"
    assert said("") == "no data directory\n"
    flat = " ".join(text.split())
    for needed in (
        # The row's first cell, the line the command prints, which the
        # session matches in what it read.
        "| `launcher <path>` |",
        # The settings file whose `Stop` entry the person removes.
        f"`{SPELLING}/settings.json`",
        # The entry's command, as the person finds it in that file.
        '`python3 "<path>" \\|\\| py -3 "<path>"`',
    ):
        assert needed in flat, needed
    # `skills/update/SKILL.md` *4b. The launcher an earlier release wrote*:
    # "This step asks nothing and writes nothing", so the step names no tool
    # that asks the person.
    assert "AskUserQuestion" not in flat, "step 4b names a tool that asks"


def test_the_skill_names_no_fixed_claude_directory():
    """S5. Every path into Claude Code's directory is spelled as the config
    directory in use, so step 5's sentinel method, which no case runs, names
    the directory the session loaded. The search is for the path segment
    `/.claude`, however the part before it is spelled; `.claude-plugin` is
    another name and does not count."""
    rest = read(UPDATE).replace(SPELLING, "")
    fixed = re.findall(r"\S*/\.claude(?![-\w])\S*", rest)
    # `skills/update/SKILL.md` *Procedure*: "Each command below carries that
    # spelling on its own", so no path into the directory is spelled fixed.
    assert not fixed, f"skills/update/SKILL.md names {fixed!r} outside {SPELLING!r}"
