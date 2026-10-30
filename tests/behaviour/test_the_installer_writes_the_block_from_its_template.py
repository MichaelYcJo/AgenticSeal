"""`install.sh` writes the CLAUDE.md block from its one source, and nothing else carries it.

The block between `<!-- agentic:start -->` and `<!-- agentic:end -->` lives
in `templates/setup/claude-md-block.md`, markers included. `install.sh` cuts it out
with `awk` and writes it into a `CLAUDE.md`; `uninstall.sh` takes it out;
`/agentic:update` step 4 diffs it against the installed copy, and
`/agentic:preset-setup` merges it. A block a release before 0.23.0 wrote sits
between `<!-- specseal:start -->` and `<!-- specseal:end -->`, and both
scripts read it as the block through 0.23.x. This repository's own `CLAUDE.md` carries
no copy: a session here loads the installed block from `~/.claude/CLAUDE.md`,
so a copy in the tree was read twice and was the one a consuming repository
never sees
(`0ed5dd3b:seal/specs/1792540458-on-demand-files-state-the-current-rule/plan.md`
A2).

The cases that ran an installer are kept from the module that held the copy
to its template, which left with the copy (#940).
"""

import os
import re
import subprocess

import pytest
from conftest import ROOT, read, shell_probe

TEMPLATE = os.path.join(ROOT, "templates", "setup", "claude-md-block.md")
INSTALL = os.path.join(ROOT, "install.sh")
UNINSTALL = os.path.join(ROOT, "uninstall.sh")
START, END = "<!-- agentic:start -->", "<!-- agentic:end -->"
# The markers every release before 0.23.0 wrote into a user's CLAUDE.md.
OLD_START, OLD_END = "<!-- specseal:start -->", "<!-- specseal:end -->"


def block_of(text):
    """The marker region, the way `install.sh`'s `awk` cuts it: from the line
    holding the start marker through the line holding the end marker."""
    lines = text.splitlines(keepends=True)
    first = next(i for i, line in enumerate(lines) if START in line)
    last = next(i for i, line in enumerate(lines) if END in line)
    return "".join(lines[first : last + 1])


def bash(script, *args, env=None, cwd=ROOT):
    """Run SCRIPT with ARGS (a target, or nothing) under bash, or skip where
    no working bash answers.

    `install.sh` is a POSIX installer a person runs from a clone, and a
    `windows-latest` runner has no shell to run it: `bash` on its PATH is the
    WSL launcher with no distribution installed (PR #329, run 34426711135).
    Asked of the shell rather than of the platform name, so the case still
    runs wherever somebody has a real bash, Windows included."""
    why = shell_probe("bash")
    if why:
        pytest.skip(f"bash: {why} -- the installer is a shell script")
    return subprocess.run(
        ["bash", script, *map(str, args)],
        cwd=cwd,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )


# The one line between the markers, and the tree path it names inside the
# marketplace clone (#1177).
IMPORT_LINE = "@plugins/marketplaces/agenticseal/skills/core/SKILL.md"
CLONE = os.path.join("plugins", "marketplaces", "agenticseal")


def test_the_template_is_the_block_and_nothing_else():
    """The template is what `install.sh` cuts with `awk`, so a line outside
    its markers is a line that reaches nobody and a line inside is one that
    reaches every user."""
    text = read(TEMPLATE)
    assert text.startswith(START + "\n"), (
        "the template does not open with the start marker"
    )
    assert text.endswith(END + "\n"), "the template does not close with the end marker"
    assert text.count(START) == 1 and text.count(END) == 1


def test_the_block_is_one_import_of_the_core_and_no_rule():
    """S2 and S4 of #1177. Between the markers stands the one `@` line and
    nothing else: each rule the block held stands in the file that applies
    it, and the line, read relative to the `CLAUDE.md` that holds it, names
    the core inside the marketplace clone, so the path past the clone is a
    file of this tree."""
    assert read(TEMPLATE) == f"{START}\n{IMPORT_LINE}\n{END}\n", (
        "the block holds more than the markers and the core's `@` line"
    )
    tail = IMPORT_LINE[1:].split(CLONE.replace(os.sep, "/") + "/", 1)
    assert len(tail) == 2 and tail[0] == "", IMPORT_LINE
    assert os.path.isfile(os.path.join(ROOT, tail[1])), (
        f"the block imports `{tail[1]}`, which this tree does not hold"
    )


def test_this_repository_carries_no_copy_of_the_block():
    """S2 of #940. A copy in `CLAUDE.md` is read by every session here beside
    the installed block, and nothing holds it to the template any more."""
    text = read(os.path.join(ROOT, "CLAUDE.md"))
    assert START not in text and END not in text, (
        "CLAUDE.md carries the block's markers again, which is a second copy "
        "of `templates/setup/claude-md-block.md` loaded beside the installed one"
    )


# An `@` import as Claude Code reads one: `@` at the start of a line or after
# whitespace, then a path. A backticked `@` is a code span, not an import.
IMPORT = re.compile(r"(?:^|\s)@[^\s`]")


def test_this_repository_imports_no_core_and_names_the_tree_copy():
    """S3 of #1177. A session here reads the tree's core from the plugin's
    `SessionStart` hook, so an `@` line in `CLAUDE.md` would load it a second
    time; and `CLAUDE.md` names the tree's copy, which governs here."""
    text = read(os.path.join(ROOT, "CLAUDE.md"))
    assert not IMPORT.search(text), (
        "CLAUDE.md imports a file, so a session here reads the core twice"
    )
    assert "`skills/core/SKILL.md`" in text, (
        "CLAUDE.md does not name the core, so a session here cannot tell "
        "which copy governs"
    )


def test_an_import_line_is_told_from_a_code_span():
    """The check can fail: a planted import is found, a code span is not."""
    assert IMPORT.search("intro\n@skills/core/SKILL.md\n")
    assert IMPORT.search("see @docs/x.md here")
    assert not IMPORT.search("the block's `@` line imports it")


def test_install_sh_reads_the_template():
    """The installer reads the block's one source."""
    text = read(INSTALL)
    assert 'SOURCE="$REPO_DIR/templates/setup/claude-md-block.md"' in text, (
        "install.sh does not read the block from the template"
    )
    assert 'SOURCE="$REPO_DIR/CLAUDE.md"' not in text


def test_install_sh_puts_the_template_block_into_a_fresh_target(tmp_path):
    """S3, executed: `bash install.sh <scratch target>` and the file read
    afterwards. The block in the target is the template's block."""
    target = tmp_path / "probe-CLAUDE.md"
    out = bash(INSTALL, target)
    assert out.returncode == 0, out.stdout + out.stderr
    assert block_of(target.read_text(encoding="utf-8")) == read(TEMPLATE)


def test_a_second_install_changes_nothing(tmp_path):
    """S3: the installer is run again to update, so a run over its own output
    leaves the file as it was, the user's text on either side included."""
    target = tmp_path / "CLAUDE.md"
    target.write_text("# mine, above\n", encoding="utf-8")
    first = bash(INSTALL, target)
    assert first.returncode == 0, first.stdout + first.stderr
    once = target.read_text(encoding="utf-8")
    second = bash(INSTALL, target)
    assert second.returncode == 0, second.stdout + second.stderr
    assert target.read_text(encoding="utf-8") == once, (
        "a second install changed the file, so every update grows it"
    )
    assert once.count(START) == 1 and once.startswith("# mine, above\n")


def test_install_sh_replaces_an_older_block_from_the_template(tmp_path):
    """The update path: a target already holding a block gets the template's
    block in its place, and its own text on either side stays."""
    target = tmp_path / "CLAUDE.md"
    stale = read(TEMPLATE).replace(IMPORT_LINE, "## Tooling\n- an old rule")
    assert stale != read(TEMPLATE)
    target.write_text(
        "# mine, above\n\n" + stale + "\n# mine, below\n", encoding="utf-8"
    )
    out = bash(INSTALL, target)
    assert out.returncode == 0, out.stdout + out.stderr
    after = target.read_text(encoding="utf-8")
    assert block_of(after) == read(TEMPLATE)
    assert after.startswith("# mine, above\n") and after.endswith("# mine, below\n")


def test_install_sh_replaces_the_block_under_the_old_markers_once(tmp_path):
    """#1051: a CLAUDE.md a release before 0.23.0 wrote holds the block
    between the old markers. The installer puts the template's block in its
    place, under the new markers, so one block stands and the user's text on
    either side stays; a second run changes nothing."""
    target = tmp_path / "CLAUDE.md"
    old = read(TEMPLATE).replace(START, OLD_START).replace(END, OLD_END)
    target.write_text("# mine, above\n\n" + old + "\n# mine, below\n", encoding="utf-8")
    out = bash(INSTALL, target)
    assert out.returncode == 0, out.stdout + out.stderr
    after = target.read_text(encoding="utf-8")
    assert OLD_START not in after and OLD_END not in after, after
    assert after.count(START) == 1 and after.count(END) == 1, after
    assert block_of(after) == read(TEMPLATE)
    assert after.startswith("# mine, above\n") and after.endswith("# mine, below\n")
    again = bash(INSTALL, target)
    assert again.returncode == 0, again.stdout + again.stderr
    assert target.read_text(encoding="utf-8") == after


def warnings_of(out):
    """The lines `install.sh`'s `warn` printed."""
    return [line for line in out.stdout.splitlines() if "[warn]" in line]


def test_install_sh_warns_when_the_core_it_imports_is_not_there(tmp_path):
    """S7 of #1177. A dangling `@` import loads nothing and says nothing, so
    the installer says it once, at install time: it writes the block, exits
    0, and names the file the block imports beside the target it wrote."""
    target = tmp_path / "CLAUDE.md"
    out = bash(INSTALL, target)
    assert out.returncode == 0, out.stdout + out.stderr
    assert block_of(target.read_text(encoding="utf-8")) == read(TEMPLATE)
    missing = str(tmp_path / CLONE / "skills" / "core" / "SKILL.md")
    assert [line for line in warnings_of(out) if missing in line], (
        f"the installer did not name `{missing}`, which the block imports "
        f"and which is not there:\n{out.stdout}"
    )


def test_install_sh_says_nothing_when_the_core_is_there(tmp_path):
    """S7's sibling: with the core where the block imports it, the installer
    warns about nothing, and the user's own text naming the old block's
    words draws no overlap warning, since the block holds no rule to
    overlap with."""
    core = tmp_path / CLONE / "skills" / "core" / "SKILL.md"
    core.parent.mkdir(parents=True)
    core.write_text("# The core\n", encoding="utf-8")
    target = tmp_path / "CLAUDE.md"
    target.write_text(
        "# mine\n- prefer uv and pnpm; a worktree per session\n"
        "- Verification first; the 3+ Fix Rule\n",
        encoding="utf-8",
    )
    out = bash(INSTALL, target)
    assert out.returncode == 0, out.stdout + out.stderr
    assert not warnings_of(out), out.stdout


def test_both_scripts_default_to_the_config_directorys_file(tmp_path):
    """With no argument both scripts work on the `CLAUDE.md` the harness
    reads as the user's, `$CLAUDE_CONFIG_DIR/CLAUDE.md` where that is set,
    which is the directory the block's relative import resolves against.
    HOME is a scratch directory too, so a script that ignored the variable
    writes there and not into the machine's own file."""
    config = tmp_path / "config"
    env = {
        **os.environ,
        "HOME": str(tmp_path / "home"),
        "CLAUDE_CONFIG_DIR": str(config),
    }
    out = bash(INSTALL, env=env)
    assert out.returncode == 0, out.stdout + out.stderr
    assert block_of((config / "CLAUDE.md").read_text(encoding="utf-8")) == read(
        TEMPLATE
    )
    out = bash(UNINSTALL, env=env)
    assert out.returncode == 0, out.stdout + out.stderr
    assert START not in (config / "CLAUDE.md").read_text(encoding="utf-8")
    assert not (tmp_path / "home" / ".claude").exists(), (
        "a script with no argument wrote under HOME while CLAUDE_CONFIG_DIR was set"
    )


def test_install_sh_has_no_project_scope(tmp_path):
    """In a project's `CLAUDE.md` the block's relative line names a
    `plugins/` directory inside the project, which is not there, and a line
    written to reach the clone from there is external: an approval dialog
    gates it and a headless session never loads it (#1177, probe d), so the
    scope is gone. An option, `--project` among them, is refused rather than
    taken for a file named after it."""
    env = {**os.environ, "HOME": str(tmp_path), "CLAUDE_CONFIG_DIR": str(tmp_path)}
    out = bash(INSTALL, "--project", env=env, cwd=tmp_path)
    assert out.returncode != 0, out.stdout + out.stderr
    assert "Unknown option --project" in out.stdout, (
        f"the installer did not refuse the option by name:\n{out.stdout}{out.stderr}"
    )
    assert not list(tmp_path.iterdir()), "the installer wrote a file for an option"


def test_uninstall_sh_removes_the_block_under_the_old_markers(tmp_path):
    """#1051: the uninstaller is the installer's inverse through 0.23.x, so
    the block the old markers hold goes and the user's own lines stay."""
    target = tmp_path / "CLAUDE.md"
    old = read(TEMPLATE).replace(START, OLD_START).replace(END, OLD_END)
    target.write_text("# mine, above\n\n" + old, encoding="utf-8")
    out = bash(UNINSTALL, target)
    assert out.returncode == 0, out.stdout + out.stderr
    after = target.read_text(encoding="utf-8")
    assert after.strip() == "# mine, above", after


def test_uninstall_sh_removes_the_block_and_nothing_else(tmp_path):
    """S3: `uninstall.sh` is the installer's inverse, so the block it wrote
    goes and the user's own lines stay."""
    target = tmp_path / "CLAUDE.md"
    target.write_text("# mine, above\n", encoding="utf-8")
    assert bash(INSTALL, target).returncode == 0
    out = bash(UNINSTALL, target)
    assert out.returncode == 0, out.stdout + out.stderr
    after = target.read_text(encoding="utf-8")
    assert after.strip() == "# mine, above", (
        f"uninstall left a line of the block, or took one of the user's: {after!r}"
    )


def test_the_runtime_readers_name_the_template_path():
    """`preset-setup` reads the block at runtime from the plugin's cache and
    `update` diffs it from the marketplace clone. Both name the template, and
    neither names a copy that no longer exists."""
    for name in ("preset-setup", "update"):
        text = read(os.path.join(ROOT, "skills", name, "SKILL.md"))
        assert "templates/setup/claude-md-block.md" in text, (
            f"{name} does not name the template"
        )
        for gone in (
            "plugin's CLAUDE.md",
            "marketplaces/agenticseal/CLAUDE.md",
            "generated copy",
        ):
            assert gone not in text, f"{name} still names `{gone}`"
