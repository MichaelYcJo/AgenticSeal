"""An installed preset block leaves through `/agentic:update`, and nothing writes one (#1177, S6 and S9).

Releases before 0.25.0 wrote a block into the user's `CLAUDE.md` between
`<!-- agentic:start -->` and `<!-- agentic:end -->`, or, before the rename,
between `<!-- specseal:start -->` and `<!-- specseal:end -->`. The core now
reaches a session from the plugin's `SessionStart` hook, so the block, its
installer, its uninstaller and `/agentic:preset-setup` retire.

The update to 0.25.0 runs the 0.24.x procedure, whose step 4 diffs the marker
region of the marketplace clone's `templates/setup/claude-md-block.md`
against the user's file and replaces a region that differs. So for one
release the template holds the two markers and nothing between them, and
that update leaves an empty marker pair. The next update runs 0.25.0's step
4, which takes any marker region out after a backup; its command is run here
over scratch files, the way the cases this module replaced ran `install.sh`.

This repository's own `CLAUDE.md` carries no block and imports nothing: a
session here reads the tree's core from the plugin's hook.
"""

import os
import re
import subprocess
import sys

from conftest import ROOT, flattened, git, read

TEMPLATE = os.path.join(ROOT, "templates", "setup", "claude-md-block.md")
UPDATE = os.path.join(ROOT, "skills", "update", "SKILL.md")
START, END = "<!-- agentic:start -->", "<!-- agentic:end -->"
# The markers every release before 0.23.0 wrote into a user's CLAUDE.md.
OLD_START, OLD_END = "<!-- specseal:start -->", "<!-- specseal:end -->"
# The file the step works on, as the shell expands it.
USER_FILE = '"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md"'
# Step 4's one command: a `python3 -c` program in step 3's shape, then the
# file it is given.
COMMAND = re.compile(
    r"```bash\npython3 -c '\n(?P<code>.*?)\n' (?P<args>[^\n]*)\n```", re.S
)


def step_4():
    """The text of update step 4, from its number to step 5's."""
    text = read(UPDATE)
    return text[text.index("**4.") : text.index("**5.")]


def command():
    """Step 4's program and the arguments the shell line passes it."""
    found = COMMAND.search(step_4())
    assert found, "update step 4 holds no `python3 -c` command in a bash fence"
    return found.group("code"), found.group("args")


def take_out(target, cwd):
    """Step 4's program run over TARGET from CWD, as the step's shell line
    runs it, with this interpreter standing in for `python3`."""
    code, _ = command()
    return subprocess.run(
        [sys.executable, "-c", code, str(target)],
        cwd=cwd,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def test_the_template_is_the_two_markers_and_nothing_between_them():
    """S6. 0.24.x's step 4 replaces a differing region with the template's,
    so the template holds no `@` line, which would put a second read of the
    core into every session, and no rule, which a skill already states."""
    assert read(TEMPLATE) == f"{START}\n{END}\n", (
        "the template holds more than its two markers, so the update to 0.25.0 "
        "writes it into every user's CLAUDE.md"
    )


def test_step_4_takes_the_empty_pair_out_after_a_backup(tmp_path):
    """S6. The pair the update to 0.25.0 leaves is taken out with its
    markers, the user's lines on either side stay, and the file as it stood
    is kept beside it as `CLAUDE.md.bak`."""
    target = tmp_path / "CLAUDE.md"
    before = "# mine, above\n\n" + read(TEMPLATE) + "\n# mine, below\n"
    target.write_text(before, encoding="utf-8")
    out = take_out(target, tmp_path)
    assert out.returncode == 0, out.stdout + out.stderr
    assert target.read_text(encoding="utf-8") == "# mine, above\n\n\n# mine, below\n"
    assert (tmp_path / "CLAUDE.md.bak").read_text(encoding="utf-8") == before
    assert str(target) in out.stdout and "CLAUDE.md.bak" in out.stdout, out.stdout


def test_step_4_takes_out_a_block_under_either_markers_whatever_it_holds(tmp_path):
    """S6. A 0.24.x block that was never updated holds eight rules, and one
    from before the rename stands under the old markers; each region goes
    whole, so no rule line is left behind."""
    target = tmp_path / "CLAUDE.md"
    target.write_text(
        f"# mine\n{START}\n## Tooling\n- an old rule\n{END}\n"
        f"{OLD_START}\n@plugins/old.md\n{OLD_END}\n# mine, last\n",
        encoding="utf-8",
    )
    out = take_out(target, tmp_path)
    assert out.returncode == 0, out.stdout + out.stderr
    assert target.read_text(encoding="utf-8") == "# mine\n# mine, last\n"


def test_step_4_stops_at_a_start_marker_with_no_end_marker(tmp_path):
    """Without its end marker nothing says where the block ends, so the step
    changes nothing, writes no backup, says why, and exits 1."""
    target = tmp_path / "CLAUDE.md"
    before = f"# mine\n{START}\n- a line\n# mine, below\n"
    target.write_text(before, encoding="utf-8")
    out = take_out(target, tmp_path)
    assert out.returncode == 1, out.stdout + out.stderr
    assert target.read_text(encoding="utf-8") == before
    assert not (tmp_path / "CLAUDE.md.bak").exists()
    assert "no end marker" in out.stdout, out.stdout


def test_step_4_says_nothing_where_no_block_stands(tmp_path):
    """No block, or no file at all, is the state the step leaves: it prints
    nothing, writes nothing and exits 0."""
    mine = tmp_path / "CLAUDE.md"
    mine.write_text("# mine only\n", encoding="utf-8")
    for target in (mine, tmp_path / "absent" / "CLAUDE.md"):
        out = take_out(target, tmp_path)
        assert (out.returncode, out.stdout) == (0, ""), out.stdout + out.stderr
    assert mine.read_text(encoding="utf-8") == "# mine only\n"
    assert not (tmp_path / "CLAUDE.md.bak").exists()


def test_step_4_names_a_projects_block_and_does_not_edit_it(tmp_path):
    """S6. 0.24.x's installer could write the block into a project's
    `CLAUDE.md`, which is the project's committed text, so the step names it
    and leaves it as it stands."""
    repo = tmp_path / "repo"
    (repo / "src").mkdir(parents=True)
    git(repo, "init", "-q")
    project = repo / "CLAUDE.md"
    held = f"# the project\n{START}\n- a rule\n{END}\n"
    project.write_text(held, encoding="utf-8")
    out = take_out(tmp_path / "CLAUDE.md", repo / "src")
    assert out.returncode == 0, out.stdout + out.stderr
    assert project.read_text(encoding="utf-8") == held
    assert not (repo / "CLAUDE.md.bak").exists()
    named = [line for line in out.stdout.splitlines() if "needs action" in line]
    assert len(named) == 1 and "CLAUDE.md" in named[0], out.stdout
    assert os.path.realpath(named[0].split(": ", 1)[1].split(" ", 1)[0]) == (
        os.path.realpath(project)
    ), named[0]


def test_step_4_works_on_the_config_directorys_file_and_writes_no_block():
    """S6. The step reads the `CLAUDE.md` the harness reads as the user's,
    says where the core now comes from, names a project's file under *Needs
    action*, asks nothing, and reads no template, so no step writes an `@`
    line."""
    _, args = command()
    assert args == USER_FILE, args
    step = flattened(step_4())
    for said in (
        "**4. Take out the preset block.**",
        "`SessionStart` hook",
        "the skills and definitions the plugin installs",
        "*Needs action*",
        "No question is asked",
        "`CLAUDE.md.bak`",
    ):
        assert said in step, f"update step 4 does not say {said!r}"
    for gone in ("claude-md-block.md", "diff ", "@plugins"):
        assert gone not in step, f"update step 4 still carries {gone!r}"


def test_the_installer_the_uninstaller_and_preset_setup_are_gone():
    """S9. Nothing is left to write, and step 4 is the one remover, so the
    three are absent and no shipped document tells a reader to run one."""
    for rel in ("install.sh", "uninstall.sh", os.path.join("skills", "preset-setup")):
        assert not os.path.exists(os.path.join(ROOT, rel)), f"{rel} is back"
    shipped = ["README.md", "README.ko.md", "CONTRIBUTING.md"]
    for top in ("skills", "agents", "docs", "templates"):
        for here, _, names in os.walk(os.path.join(ROOT, top)):
            shipped += [
                os.path.relpath(os.path.join(here, n), ROOT)
                for n in names
                if n.endswith(".md")
            ]
    for rel in shipped:
        text = read(rel)
        for name in ("install.sh", "preset-setup"):
            assert name not in text, f"{rel} names `{name}`"


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
