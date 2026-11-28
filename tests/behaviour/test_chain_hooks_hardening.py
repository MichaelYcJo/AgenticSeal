"""Hardening cases over what the plugin ships and the records it keeps: its
packaging, the READMEs' account of it, the wording of its skills, of its
agent definitions, of `CONTRIBUTING.md` and of `docs/running/the-run.md`,
and the work item directories under `agentory/threads/`.

The module is named for the plugin's hooks, which #1376 removed and #1430
brought back; #1608 added the `PreToolUse` hook and #1612 the
`PostToolUse` one. What the stamp's `Stop` command draws is held in
`tests/skills/test_stamp.py`, what the `SessionStart` command prints in
`tests/hooks/test_core_start.py`, what the `PreToolUse` command refuses in
`tests/hooks/test_ask_under_automation.py`, and what the `PostToolUse`
command names in `tests/hooks/test_edit_leaves_copies.py`.
"""

import json
import os
import re
import shlex
import subprocess
import sys

import pytest
from conftest import ROOT, git_listing, shell_probe

# No TARGET: its cases hold what the plugin ships across its packaging, both READMEs, the skills and the agent definitions.

# --- packaging sanity ------------------------------------------------------

# The entries `hooks/hooks.json` registers, each event's matcher (None for
# an entry with none), and the files `hooks/` holds.
HOOK_ENTRIES = {
    "Stop": None,
    "SessionStart": "startup|clear|compact",
    "PreToolUse": "AskUserQuestion",
    "PostToolUse": "Edit",
}
HOOK_FILES = [
    "hooks/ask-under-automation.py",
    "hooks/core-start.py",
    "hooks/edit-leaves-copies.py",
    "hooks/hooks.json",
]
PLUGIN_ROOT = "${CLAUDE_PLUGIN_ROOT}/"


def test_the_plugin_registers_its_hooks_and_writes_none_into_git():
    """#1430 *Scope* items 1 and 4, #1608 S8 and #1612 A12. The plugin ships
    command hooks and no dispatcher: a `Stop` entry with no matcher that
    runs `stamp.py --stop`, a `SessionStart` entry matched to
    `startup|clear|compact` that runs `hooks/core-start.py`, a `PreToolUse`
    entry matched to `AskUserQuestion` that runs
    `hooks/ask-under-automation.py`, and a `PostToolUse` entry matched to
    `Edit` that runs `hooks/edit-leaves-copies.py`. Each holds one command
    hook, three parts joined by ` || `: `python3` then `py -3`, naming one
    tracked script under `${CLAUDE_PLUGIN_ROOT}` with the same arguments,
    then `exit 0`, so the command exits 0 whatever its halves did. The harness
    reads `hooks/hooks.json` at the plugin's root, and `hooks/` holds those
    files and nothing else. Nothing writes into a clone's git hooks
    (`docs/checks/the-routing-check.md`).

    The plugin directory refuses a plugin that registers a command hook
    (#1376), and the owner chose on 2026-11-08 to ship such hooks until a
    listing is possible (#1430), filed #1608 for the `PreToolUse` one, and
    filed #1612, whose frame chose the `PostToolUse` one. When the
    directory lists the plugin with its hooks, or lists it on condition
    they go, the removal undoes: `hooks/hooks.json`, `hooks/core-start.py`,
    `hooks/ask-under-automation.py`, `hooks/edit-leaves-copies.py`,
    `lib/core.py`,
    `lib/routing.py#open_declarations`, `tests/hooks/test_core_start.py`,
    `tests/hooks/test_ask_under_automation.py`,
    `tests/hooks/test_edit_leaves_copies.py`, `tests/lib/test_core.py`,
    `Test_open_declarations` in `tests/lib/test_routing.py`, this case,
    `hooks` in the hygiene step's pattern and the roots sentence of
    `docs/releasing/branch-and-release.md` *Cutting a release*, `ruff.toml`'s
    `hooks/*.py` line and the start of
    `tests/behaviour/test_every_entry_point_runs_at_the_floor.py`'s floor
    derivation, `skills/verify/scripts/payload_meter.py#HOOK_ROW`, and the
    sentences this command lists:

        git grep -n "SessionStart\\|hooks/hooks.json\\|core-start\\|lib/core\\|IADD core from\\|PreToolUse\\|ask-under-automation\\|PostToolUse\\|edit-leaves-copies"

    and it gives the core and the stamp new carriers, which that work's frame
    decides."""
    with open(os.path.join(ROOT, "hooks", "hooks.json"), encoding="utf-8") as f:
        registered = json.load(f)
    assert list(registered) == ["hooks"], list(registered)
    assert sorted(registered["hooks"]) == sorted(HOOK_ENTRIES), registered["hooks"]
    tracked = git_listing(ROOT, "ls-files")
    for event, matcher in HOOK_ENTRIES.items():
        (entry,) = registered["hooks"][event]
        assert entry.get("matcher") == matcher, (event, entry)
        assert sorted(entry) == sorted(["hooks"] + (["matcher"] if matcher else []))
        (hook,) = entry["hooks"]
        assert hook["type"] == "command", (event, hook)
        parts = [shlex.split(part) for part in hook["command"].split(" || ")]
        assert len(parts) == 3, (event, hook["command"])
        first, second, last = parts
        assert last == ["exit", "0"], (event, hook["command"])
        halves = [first, second]
        assert first[0] == "python3" and second[:2] == ["py", "-3"], halves
        assert first[1:] == second[2:], halves
        script = first[1]
        assert script.startswith(PLUGIN_ROOT), (event, script)
        assert script[len(PLUGIN_ROOT) :] in tracked, (event, script)
    assert sorted(p for p in tracked if p.startswith("hooks/")) == HOOK_FILES
    assert os.path.isfile(os.path.join(ROOT, "lib", "optin.py"))


@pytest.mark.parametrize("event", sorted(HOOK_ENTRIES))
def test_each_hook_command_exits_0_where_its_script_cannot_be_opened(event, tmp_path):
    """Round 2 of #1430, finding 1. A `python3` handed a file it cannot open
    exits 2, the `py -3` half then hands the same file to a `py` where one
    stands, and a `Stop` command's exit 2 keeps the turn going. Each command
    ends with ` || exit 0`, so it exits 0 whatever its halves did. The
    command runs here as `hooks/hooks.json` spells it, under `sh`, with
    `${CLAUDE_PLUGIN_ROOT}` at a root that holds no script, `python3` read as
    this interpreter and `py` as a scratch one that exits 2."""
    why = shell_probe("sh")
    if why:
        pytest.skip(f"sh: {why}")
    with open(os.path.join(ROOT, "hooks", "hooks.json"), encoding="utf-8") as f:
        ((hook,),) = [e["hooks"] for e in json.load(f)["hooks"][event]]
    py = tmp_path / "py"
    py.write_text("#!/bin/sh\nexit 2\n", encoding="utf-8")
    py.chmod(0o755)
    command = hook["command"]
    # The two interpreter names, each the first word of its half, which the
    # harness runs and this case swaps for its own two.
    assert command.startswith("python3 ") and " || py -3 " in command, command
    command = command.replace("python3 ", f"{shlex.quote(sys.executable)} ", 1)
    command = command.replace(" || py -3 ", f" || {shlex.quote(str(py))} -3 ", 1)
    empty = tmp_path / "root"
    empty.mkdir()
    done = subprocess.run(
        ["sh", "-c", command],
        input=json.dumps({"hook_event_name": event, "cwd": str(tmp_path)}).encode(),
        capture_output=True,
        timeout=60,
        env={**os.environ, "CLAUDE_PLUGIN_ROOT": str(empty)},
    )
    assert done.returncode == 0, (event, done.returncode, done.stderr)


def test_the_house_rule_gives_the_shape_of_each_hook_command():
    """Contract rule 14, for rounds 1 and 2 of #1430, finding 1 of each. A
    script can fail before it runs, and `python3` exits 2 on a file it cannot
    open, so the exit is the command's to decide: each ends with
    ` || exit 0`. `CONTRIBUTING.md` *House rules* gives that shape; the rule
    it states for the exit is the proofer's to read."""
    from conftest import flat

    text = flat("CONTRIBUTING.md")
    # The shape of a hook's command, which a contributor copies for a hook.
    assert "`python3 <script> || py -3 <script> || exit 0`" in text


def test_the_plugin_icon_is_a_png_the_directory_accepts():
    """#857 S9. `.claude-plugin/plugin.json` names
    `./.claude-plugin/icon.png` as its `icon`, and that file is what
    `claude plugin validate` accepts for the directory: a PNG, square, 512
    to 2048 pixels on a side and under 2,000,000 bytes. The header is read
    with the standard library: the eight-byte signature, then the `IHDR`
    chunk's width and height. Seen red before the icon was drawn."""
    with open(
        os.path.join(ROOT, ".claude-plugin", "plugin.json"), encoding="utf-8"
    ) as f:
        icon = json.load(f).get("icon")
    assert icon == "./.claude-plugin/icon.png", icon
    # The manifest spells the path with `/`, so it is split before it is joined.
    path = os.path.join(ROOT, *icon.split("/"))
    with open(path, "rb") as f:
        head = f.read(24)
    assert head[:8] == b"\x89PNG\r\n\x1a\n" and head[12:16] == b"IHDR", head
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    assert width == height and 512 <= width <= 2048, (width, height)
    assert os.path.getsize(path) < 2_000_000, os.path.getsize(path)


def test_the_marketplace_describes_the_plugin_in_the_manifests_words():
    """#1055 S13. `.claude-plugin/plugin.json`'s `description` is the one
    source of the sentence that describes the plugin. JSON cannot link, so
    `.claude-plugin/marketplace.json` carries it twice, at its top level and
    in its plugin entry, and each copy must equal the source.

    #1102 S2: `README.md` carries it a third time, as the paragraph directly
    under `# IADD`, because the page's first reader meets the plugin
    there and a link cannot stand in for the sentence. The paragraph is
    wrapped at the page's line limit, so it is read with its line breaks
    folded."""
    with open(
        os.path.join(ROOT, ".claude-plugin", "plugin.json"), encoding="utf-8"
    ) as f:
        manifest = json.load(f)
    with open(
        os.path.join(ROOT, ".claude-plugin", "marketplace.json"), encoding="utf-8"
    ) as f:
        marketplace = json.load(f)
    source = manifest["description"]
    assert source, "plugin.json has no description"
    assert marketplace.get("description") == source, "marketplace.json, top level"
    entries = [p for p in marketplace["plugins"] if p.get("name") == manifest["name"]]
    assert len(entries) == 1, entries
    assert entries[0].get("description") == source, "marketplace.json, plugin entry"
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as f:
        lines = f.read().splitlines()
    under = lines[lines.index("# IADD") + 1 :]
    assert under[:1] == [""], "README.md: a line other than a blank follows the title"
    paragraph = under[1 : under.index("", 1)]
    assert " ".join(paragraph) == source, "README.md, the paragraph under the title"


def test_bin_wrapper_resolves_the_checker_from_any_cwd():
    # bin/ lands on the Bash tool's PATH while the plugin is enabled, so the
    # wrapper must resolve the script relative to itself, never the caller's
    # working directory. Windows can't run a POSIX shebang script directly,
    # so a .cmd sibling ships alongside it -- PATHEXT resolves a bare
    # `agentic` to whichever one the platform can execute, and `agentic fold`
    # hands its arguments to the checker.
    posix_wrapper = os.path.join(ROOT, "bin", "agentic")
    windows_wrapper = os.path.join(ROOT, "bin", "agentic.cmd")
    assert os.path.isfile(posix_wrapper), "bin/agentic missing"
    assert os.path.isfile(windows_wrapper), "bin/agentic.cmd missing"
    assert os.access(posix_wrapper, os.X_OK), "bin/agentic not executable"
    target = os.path.join(ROOT, "skills", "settle", "scripts", "fold_check.py")
    assert os.path.isfile(target), "the subcommand points at a missing script"
    wrapper = windows_wrapper if sys.platform == "win32" else posix_wrapper
    r = subprocess.run(
        [wrapper, "fold", "--help"],
        cwd="/",
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    assert r.returncode == 0, r.stderr
    assert "usage: agentic fold" in r.stdout


def test_parity_declaration_is_bootstrappable_not_hand_written():
    # The migration config is the one declaration a user cannot derive, so the
    # blank-page problem is real: without a template and a place that asks,
    # migration mode is a feature nobody can reach.
    tpl = os.path.join(ROOT, "templates", "setup", "parity.json")
    assert os.path.isfile(tpl), "templates/setup/parity.json missing"
    with open(tpl, encoding="utf-8") as handle:
        members = json.load(handle, object_pairs_hook=list)
    # The keys of the declaration, which the person declaring parity fills
    # in, `chain_check.py` reads `Baseline commit` of, and agents read the
    # rest of, in `agentory/parity.json`. Where the original's local path goes
    # is `skills/legacy-parity/SKILL.md` *The migration config*'s, held by
    # `tests/text/test_review_axes.py`.
    assert [key for key, _value in members] == [
        "Original repo",
        "Module",
        "Baseline commit",
        "Policy root",
        "Coordinate-trust exceptions",
        "Scope notes",
    ], members

    # The bootstrap is the orchestrator's since #292, in a file of its own
    # since #1046. Its yes to the parity question follows the parity-setup
    # procedure, which is the one statement of the four fields, so the
    # bootstrap points at the procedure and the procedure points at the
    # template. Read from the Bootstrap section alone, so a sentence the
    # file's opening paragraph gains cannot stand in for step 3.
    implement = open(
        os.path.join(ROOT, "skills", "implement", "bootstrap.md"),
        encoding="utf-8",
    ).read()
    bootstrap = implement.split("## Orchestrator: Bootstrap", 1)[1]
    bootstrap = bootstrap.split("\n## ", 1)[0]
    # The procedure's path, which the orchestrator opens on the bootstrap's yes.
    assert "skills/parity-setup/SKILL.md" in bootstrap, (
        "the bootstrap's yes never reaches the parity-setup procedure"
    )
    # The path of the root's README, which the orchestrator writes there.
    assert "agentory/README.md" in bootstrap

    setup = os.path.join(ROOT, "skills", "parity-setup", "SKILL.md")
    assert os.path.isfile(setup), "no command for declaring parity later"
    # The template's path, which the procedure copies the declaration from.
    assert "templates/setup/parity.json" in open(setup, encoding="utf-8").read(), (
        "the parity-setup procedure never points at the template"
    )
    head = open(setup, encoding="utf-8").read().split("\n---\n", 1)[0]
    # The frontmatter key the harness reads to keep the skill from firing on
    # its own.
    assert "disable-model-invocation: true" in head, (
        "parity-setup writes a declaration; it must not fire on its own"
    )
    # Which mode commits the declaration, and what refuses a round record
    # without an `original:` line in each, is the proofer's to read in the
    # procedure (#1046).


def test_the_review_skill_names_the_built_in_command_a_person_types():
    """Contract rule 14, for #1376 phase 3. The review-skill gate asked the
    person which review a plain request meant, and it went with the hooks the
    plugin directory will not register. The owner's rule replaces it: a plain
    request runs this plugin's review, and Claude Code's built-in
    `/code-review` runs when the person types that command by name. The
    skill's description names the command; how it states the rule is the
    proofer's to read."""
    with open(
        os.path.join(ROOT, "skills", "code-review", "SKILL.md"), encoding="utf-8"
    ) as f:
        head = " ".join(f.read().split("\n---\n", 1)[0].split())
    # The command a person types for Claude Code's built-in review, which the
    # model reads in the description to leave that request alone.
    assert "`/code-review`" in head


def test_the_review_skill_opens_the_core_once_where_it_orchestrates():
    """#1430 *Scope* item 3. A plain review request reaches `code-review`,
    so where it orchestrates a review it holds the core from the plugin's
    `SessionStart` hook, and opens the file itself where the hook printed
    nothing into the session. Since #1579 the sentence stands in the
    opening of the skill's orchestrator half, which the proofer never
    opens, so the case reads that opening, up to its first section. The
    opening names the hook's output and the file; its sentence is the
    proofer's to read."""
    from conftest import flat

    text = flat("skills", "code-review", "orchestration.md")
    text = text.split("## Orchestrator:", 1)[0]
    # The opening of the hook's output, which the session looks for in its
    # context, and the path of the core it opens where none stands.
    assert "`IADD core from`" in text
    assert "`skills/core/SKILL.md`" in text


def test_the_orchestrator_holds_the_core_once_before_the_first_edit():
    """#1430 *Scope* item 3. The entry's first step opened the core; with the
    entry gone, step 1 of the order inside a ticket says where the core comes
    from and the one open that stands in for a hook that printed nothing,
    such as a plugin installed after the session began. Step 1 names the
    hook's output and the file; its sentences are the proofer's to read."""
    from conftest import flat

    text = flat("skills", "implement", "orchestration.md")
    step = text.split("## Orchestrator: the order inside a ticket", 1)[1]
    step = step.split(" 2. ", 1)[0]
    # The opening of the hook's output, which the orchestrator looks for in
    # its context, and the path of the core it opens where none stands.
    assert "`IADD core from`" in step, step
    assert "`skills/core/SKILL.md`" in step, step


# The row each edition lists the skills in. Scoping to the row is not
# tidiness: the membership cases below read the names where their absence
# means something.
SKILL_ROW = {"README.md": "| Skills |", "README.ko.md": "| 스킬 |"}

# Where each edition's skills row lists the skills a session loads on its
# own: the sentence of the row that holds this phrase.
ON_DEMAND = {"README.md": "a session loads on its own", "README.ko.md": "알아서 로드"}


def skill_groups():
    """The shipped skills' names split three ways from frontmatter: those an
    agent preloads, those a person has to type, and the rest, which a
    session loads on its own."""
    import glob

    paths = glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))
    preloaded = {
        name
        for path in glob.glob(os.path.join(ROOT, "agents", "*.md"))
        for name in re.findall(
            r"^  - (\S+)", open(path, encoding="utf-8").read().split("\n---\n")[0], re.M
        )
    }
    user_invoked = {
        os.path.basename(os.path.dirname(p))
        for p in paths
        if "disable-model-invocation: true"
        in open(p, encoding="utf-8").read().split("\n---\n", 1)[0]
    }
    on_demand = {os.path.basename(os.path.dirname(p)) for p in paths}
    on_demand -= preloaded | user_invoked
    return preloaded, user_invoked, on_demand


def skill_row(edition):
    with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
        rows = [ln for ln in f if ln.startswith(SKILL_ROW[edition])]
    assert len(rows) == 1, (
        f"{edition} has {len(rows)} rows starting `{SKILL_ROW[edition]}`; "
        "the check reads exactly one"
    )
    return rows[0]


def test_the_skills_row_lists_the_on_demand_skills():
    """#1055 S5. The row lists names. Its on-demand sentence names exactly
    the skills no agent preloads and nobody has to type, derived from the
    skills' and the agents' frontmatter, so a name in the wrong sentence is
    red as well as a missing one."""
    _, _, on_demand = skill_groups()
    for edition, phrase in ON_DEMAND.items():
        row = skill_row(edition)
        sentences = [s for s in row.split(". ") if phrase in s]
        assert len(sentences) == 1, (edition, phrase, sentences)
        named = set(re.findall(r"`([^`]+)`", sentences[0]))
        assert named == on_demand, (edition, sorted(named ^ on_demand))


def test_the_core_row_names_the_core_file():
    """#1055 S3. Since #1177 the always-on text is the core, and each
    edition's `Core` row names its file as its one source. Whether a row
    counts lines or rules again is the proofer's to read."""
    for edition, row_head in (("README.md", "| Core |"), ("README.ko.md", "| 코어 |")):
        with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
            rows = [ln for ln in f if ln.startswith(row_head)]
        assert len(rows) == 1, (edition, row_head)
        # The path of the core, which a reader of the row opens.
        assert "`skills/core/SKILL.md`" in rows[0], edition


# The name each place that reaches the network carries in the READMEs' passage,
# spelt alike in both editions: `/iadd:update`, `agentic cost --post`,
# `chain_check.py` run without `--inspecting`, found by `--inspecting`, which the
# row held before #1620 did not carry, `agentic settle`, the IADD
# process's own steps (which open the pull request with `gh pr create`), and
# the checks `agentic pr-checks install` writes.
NETWORK_PLACES = (
    "/iadd:update",
    "--post",
    "--inspecting",
    "agentic settle",
    "gh pr create",
    "agentic pr-checks install",
)


def network_passage(path, said):
    """PATH's text from the sentence SAID to the next heading, as one line.
    The commands table elsewhere in each README names `/iadd:update` and
    `agentic settle` too, so a search over the whole file would pass with the
    passage's row gone."""
    from conftest import flattened, read

    text = read(path)
    at = re.search(r"\s+".join(re.escape(word) for word in said.split()), text)
    assert at, (path, said)
    end = text.find("\n#", at.start())
    return flattened(text[at.start() : end if end != -1 else len(text)])


def test_the_places_that_reach_the_network_are_named():
    """#1055 S4 and #1382. Since #1430 the plugin ships hooks, the stamp's
    `Stop` hook and the `SessionStart` hook that prints the core, since
    #1608 the `PreToolUse` hook that reads the open work items before a
    question, and since #1612 the `PostToolUse` hook that reads a work
    item's records after an edit of one, and none reaches a network. Each README edition's passage,
    from the sentence that says so to the next heading, names every place
    in `NETWORK_PLACES`, and `CONTRIBUTING.md` points at the passage."""
    from conftest import flat

    for path, said in (
        # The sentence each edition's passage opens at, which only locates
        # the passage the places are read in.
        ("README.md", "No hook reaches a network."),
        ("README.ko.md", "훅은 모두 네트워크를 타지 않습니다."),
    ):
        passage = network_passage(path, said)
        for place in NETWORK_PLACES:
            # The command or step a reader of the passage runs or looks for.
            assert place in passage, (path, place)
    # The citation a contributor resolves for the places that reach the
    # network: the path and the heading in italics.
    assert "`README.md` *What runs on your machine*" in flat("CONTRIBUTING.md")


def test_every_shipped_skill_is_named_in_both_readmes():
    """A count that matches while a name is missing is the quieter half.

    Round 1 found the first version of this useless in both directions. It
    searched the WHOLE file for a BARE name, so a name was satisfied by a
    longer command in the cheat sheet that contains it, and `verify` by two
    sentences of prose -- removing either from both editions' lists stayed
    green. The name is looked for in backticks, and in the row that lists
    the group, which is the only place its absence means anything."""
    import glob

    listed = {
        name
        for path in glob.glob(os.path.join(ROOT, "agents", "*.md"))
        for name in re.findall(
            r"^  - (\S+)", open(path, encoding="utf-8").read().split("\n---\n")[0], re.M
        )
    }
    for path in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))):
        name = os.path.basename(os.path.dirname(path))
        head = open(path, encoding="utf-8").read().split("\n---\n", 1)[0]
        user_invoked = "disable-model-invocation: true" in head
        for edition in ("README.md", "README.ko.md"):
            with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
                text = f.read()
            if name in listed:
                # The skill's name in backticks, in the agents table, which a
                # reader resolves for what an agent preloads. Round 2: `\`code-review\`
                # in text` was satisfied by the hook table thirty rows below,
                # so the name is read in the table's rows alone.
                agent_rows = [ln for ln in text.splitlines() if ln.startswith("| **")]
                assert any(f"`{name}`" in ln for ln in agent_rows), (
                    f"{edition}'s agents table never names `{name}` as "
                    "preloaded by any agent"
                )
                continue
            if user_invoked:
                # The command `/iadd:<name>` a person types: a skill nobody
                # can trigger is reachable only as a typed command.
                assert f"/iadd:{name}" in text, (
                    f"{edition} never shows `{name}` in the form a person types"
                )
                continue
            rows = [ln for ln in text.splitlines() if ln.startswith(SKILL_ROW[edition])]
            # The skill's name in backticks, in the skills row, which a
            # reader resolves for a skill a session loads on its own.
            assert f"`{name}`" in rows[0], (
                f"{edition}'s skills row does not list `{name}`, which no "
                "agent preloads and nobody can type"
            )


def test_the_writing_style_handoff_names_a_skill_that_ships():
    """Round 1, M6: reverting the handoff to its receiverless form was green.

    That line having no receiver IS the third strand of the work that added
    one, and every check on it compared the new text to itself. The pin is
    two facts: the frontmatter names a skill, and that skill is on disk --
    a name pointing at nothing is the same defect spelled differently."""
    head = (
        open(
            os.path.join(ROOT, "skills", "writing-style", "SKILL.md"), encoding="utf-8"
        )
        .read()
        .split("\n---\n", 1)[0]
    )
    # The label of the description's boundary and the skill name it hands
    # to, which the model reads to route a commit or branch request away.
    assert "NOT for:" in head, "the boundary went, so the handoff has no sender"
    assert "commit-pr-convention" in head, (
        "the handoff lost its receiver again -- `NOT for: … branch/commit "
        "format` pointing at nobody is what shipped a PR with no prefix"
    )
    assert os.path.exists(
        os.path.join(ROOT, "skills", "commit-pr-convention", "SKILL.md")
    ), "the frontmatter names a skill that does not ship"


def test_auto_firing_skills_declare_when_not_to_fire():
    # Model-invoked skills load into context when their description matches.
    # Keyword-shaped triggers ("auto-triggers on implement/create/build") fire
    # on nearly every request, which is the redundant-context cost the README
    # cites a paper about. Each one states where it does NOT belong.
    import glob

    offenders = []
    for path in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))):
        head = open(path, encoding="utf-8").read().split("\n---\n", 1)[0]
        if "disable-model-invocation: true" in head:
            continue  # user-invoked; never fires on its own
        name = os.path.basename(os.path.dirname(path))
        if "NOT for" not in head:
            offenders.append(name)
    assert not offenders, (
        "model-invoked skills with no NOT-for boundary — each will fire on "
        f"matches it should leave to another skill: {offenders}"
    )


def test_the_run_names_its_default_round_count_and_the_follow_up_file():
    """An unattended run needs a bound and a home for what it leaves. Where
    the chain ends, at a pull request and never a merge, is the orchestrator's
    to read in the crafter's hand-back."""
    with open(
        os.path.join(ROOT, "docs", "running", "the-run.md"), encoding="utf-8"
    ) as f:
        record = " ".join(f.read().split())
    # The value three, the finding rounds at which the orchestrator weighs
    # whether the run still pays.
    assert "three finding rounds by default" in record, "the review loop lost its bound"
    # The file name `follow-up.md`, where the orchestrator moves a finding
    # still open when it stops.
    assert "follow-up.md" in record, "no home recorded for what is left"


def test_the_frame_rule_names_the_phase_record_section_a_no_goes_to():
    """S5 of #84. A `frame/design.md` and a `frame/plan.md` are a drawing another party
    made, and a drawing can be wrong about the tree it describes. #107's
    phase 1 established that its own stated path could not work before a line
    was written; phase 1 of #84 did it again on a `skills:` list it was
    handed. Twice in two work items, unprompted, and written into no
    document -- which makes it a habit, and a habit is what the next spawn
    does not inherit.

    A `no` needs a destination or it becomes a second interruption, so the
    rule names the record and the section it goes to. Where the step stands
    in the order of work, and that a `no` never goes back to the framer, are
    the orchestrator's to read in the crafter's hand-back. #1628 and #1629
    moved the rule from `agents/crafter.md` to `skills/implement/SKILL.md`
    *1.*, said of the builder, so an orchestrator that builds reads it too."""
    skill = os.path.join(ROOT, "skills", "implement", "SKILL.md")
    builder = open(skill, encoding="utf-8").read()
    rule = builder[builder.index("**The frame is judged before it is built to.**") :]
    rule = " ".join(rule.split("\n\n", 1)[0].split())
    # The path `trail/phases/phase-N.md` and its heading
    # `## What this phase found`, where the builder writes a frame that does
    # not hold and the next phase reads it.
    for named in (
        "trail/phases/phase-N.md",
        "## What this phase found",
    ):
        assert named in rule, (
            f"the rule no longer names `{named}` as where a `no` goes. A "
            "`no` with no destination is a finding that reaches nobody"
        )


def test_spec_directories_carry_the_timestamp_prefix():
    # implement/SKILL.md: "A work item's directory is
    # agentory/threads/<unix-epoch-seconds>-<slug>/ ... keeps directories in
    # creation order and collision-free without a registry". Two were written
    # without
    # it and nothing noticed — the drift this plugin exists to catch, in its
    # own tree. The four that predate the convention were backfilled from the
    # commit that introduced each, so a plain listing now reads in order.
    import re

    specs = os.path.join(ROOT, "agentory", "threads")
    # Absent after a complete fold (#517); an absent directory holds no
    # offender, and the rule is the same at any size.
    offenders = [
        name
        for name in sorted(os.listdir(specs) if os.path.isdir(specs) else [])
        if os.path.isdir(os.path.join(specs, name))
        and not re.match(r"^\d{10}-[a-z0-9][a-z0-9-]*$", name)
    ]
    assert not offenders, (
        "spec directories missing the <unix-epoch-seconds>-<slug> prefix "
        f"the implement skill specifies: {offenders}"
    )


def test_every_spec_directory_that_reached_the_ladder_has_an_overview():
    """A work item that wrote a spec or a plan owes a closing memo.

    Not every directory does. Below the SDD ladder nothing is written but the
    routing declaration, and a routing-only directory is the whole record of a
    typo fix -- demanding a memo there would either fabricate one or push those
    changes back to leaving no trace at all, which is what giving them a
    directory was for.

    The exemption is narrow on purpose: the moment a directory holds a
    `frame/design.md` or a `frame/plan.md`, someone decided the work was worth describing,
    and the memo is the other half of that.

    The first phase writes it, from its template, when that phase closes
    (#1148). This case runs at every phase boundary, so a memo the last phase
    wrote would leave every earlier boundary red, as #1177's phase 1 met, and
    one a plan row asked for was written by no phase of five 0.24.0 work
    items whose rows did not ask.
    """
    specs = os.path.join(ROOT, "agentory", "threads")
    missing = []
    # Absent after a complete fold (#517), which is no directory missing a memo.
    for n in sorted(os.listdir(specs) if os.path.isdir(specs) else []):
        d = os.path.join(specs, n)
        if not os.path.isdir(d):
            continue
        on_the_ladder = any(
            os.path.isfile(os.path.join(d, "frame", f))
            for f in ("design.md", "plan.md")
        )
        if on_the_ladder and not os.path.isfile(os.path.join(d, "gaps.md")):
            missing.append(n)
    assert not missing, f"work items with no closing overview: {missing}"
