"""`install.sh` writes the CLAUDE.md block from its one source, and nothing else carries it.

The block between `<!-- specseal:start -->` and `<!-- specseal:end -->` lives
in `templates/claude-md-block.md`, markers included. `install.sh` cuts it out
with `awk` and writes it into a `CLAUDE.md`; `uninstall.sh` takes it out;
`/specseal:update` step 4 diffs it against the installed copy, and
`/specseal:preset-setup` merges it. This repository's own `CLAUDE.md` carries
no copy: a session here loads the installed block from `~/.claude/CLAUDE.md`,
so a copy in the tree was read twice and was the one a consuming repository
never sees (`seal/specs/1792540458-on-demand-files-state-the-current-rule/plan.md`
A2).

The cases that ran an installer are kept from the module that held the copy
to its template, which left with the copy (#940).
"""

import os
import subprocess

import pytest
from conftest import shell_probe

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATE = os.path.join(ROOT, "templates", "claude-md-block.md")
INSTALL = os.path.join(ROOT, "install.sh")
UNINSTALL = os.path.join(ROOT, "uninstall.sh")
START, END = "<!-- specseal:start -->", "<!-- specseal:end -->"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def block_of(text):
    """The marker region, the way `install.sh`'s `awk` cuts it: from the line
    holding the start marker through the line holding the end marker."""
    lines = text.splitlines(keepends=True)
    first = next(i for i, line in enumerate(lines) if START in line)
    last = next(i for i, line in enumerate(lines) if END in line)
    return "".join(lines[first : last + 1])


def bash(script, target):
    """Run SCRIPT on TARGET with bash, or skip where no working bash answers.

    `install.sh` is a POSIX installer a person runs from a clone, and a
    `windows-latest` runner has no shell to run it: `bash` on its PATH is the
    WSL launcher with no distribution installed (PR #329, run 34426711135).
    Asked of the shell rather than of the platform name, so the case still
    runs wherever somebody has a real bash, Windows included."""
    why = shell_probe("bash")
    if why:
        pytest.skip(f"bash: {why} -- the installer is a shell script")
    return subprocess.run(
        ["bash", script, str(target)],
        cwd=ROOT,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


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


def test_this_repository_carries_no_copy_of_the_block():
    """S2 of #940. A copy in `CLAUDE.md` is read by every session here beside
    the installed block, and nothing holds it to the template any more."""
    text = read(os.path.join(ROOT, "CLAUDE.md"))
    assert START not in text and END not in text, (
        "CLAUDE.md carries the block's markers again, which is a second copy "
        "of `templates/claude-md-block.md` loaded beside the installed one"
    )


def test_install_sh_reads_the_template():
    """The installer reads the block's one source."""
    text = read(INSTALL)
    assert 'SOURCE="$REPO_DIR/templates/claude-md-block.md"' in text, (
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
    stale = read(TEMPLATE).replace("## Tooling", "## Tooling (old)")
    assert stale != read(TEMPLATE)
    target.write_text(
        "# mine, above\n\n" + stale + "\n# mine, below\n", encoding="utf-8"
    )
    out = bash(INSTALL, target)
    assert out.returncode == 0, out.stdout + out.stderr
    after = target.read_text(encoding="utf-8")
    assert block_of(after) == read(TEMPLATE)
    assert after.startswith("# mine, above\n") and after.endswith("# mine, below\n")


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
        assert "templates/claude-md-block.md" in text, (
            f"{name} does not name the template"
        )
        for gone in (
            "plugin's CLAUDE.md",
            "marketplaces/specseal/CLAUDE.md",
            "generated copy",
        ):
            assert gone not in text, f"{name} still names `{gone}`"
