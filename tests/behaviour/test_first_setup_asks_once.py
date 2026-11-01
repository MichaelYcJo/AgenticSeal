"""First setup asks once — shared or local — and every document that a session
or a person reads says the same thing about where the root lives.

The work item is
`aa687d35:seal/specs/1788354065-the-tree-that-must-stay-clean-has-no-way-to-opt-in/`;
the clauses named per case are its spec's. The hooks resolve
the root in code (`hooks/lib/optin.py#home_at`) and are pinned by
`tests/hooks/test_optin.py`, `tests/test_commit_review_gate.py` and
`tests/hooks/test_implementer_notice.py`. What is pinned HERE
is the text: the one question the `implement`
skill asks, the sentence a session needs, the workflow template
`seal pr-checks install` writes and the commands its header names, and the
switch the READMEs give.

Every case was executed against the documents as they stood at 7e44106,
before any of them was edited, and every case failed; the output is in the
body of the commit that added this file.
"""

import os
import re
import subprocess

import pytest
from conftest import ROOT, local_home, read, shell_probe

COMMON_DIR = "$(git rev-parse --git-common-dir)/seal/"
# The sentence a session reads (Q1 of the work item's `questions.md`): the
# same rule `hooks/lib/optin.py` states, moved to where a session looks.
SESSION_RULE = "`$(git rev-parse --git-common-dir)/seal/` otherwise"


def section(text, heading, level):
    """The text under HEADING up to the next heading of the same LEVEL."""
    assert heading in text, f"{heading!r} is not a heading any more"
    body = text.split(heading, 1)[1]
    return body.split("\n" + "#" * level + " ", 1)[0]


def paragraph(text, opening):
    """The paragraph whose first words are OPENING, its line breaks folded."""
    i = text.find(opening)
    assert i >= 0, f"no paragraph opens with {opening!r}"
    return flat(text[i:].split("\n\n", 1)[0])


def flat(text):
    """Runs of whitespace folded to one space, so a phrase that a hand-wrap
    splits across two lines still reads as the phrase."""
    return re.sub(r"\s+", " ", text)


SKILL = ("skills", "implement", "SKILL.md")
ORCH = ("skills", "implement", "orchestration.md")
# The bootstrap is the orchestrator's since #292: it asks a person, which a
# crafter spawn may not, so it lives in a file no `skills:` list injects. It
# has its own file since #1046, because only a repository with no root yet
# needs it.
BOOT = ("skills", "implement", "bootstrap.md")


def bootstrap():
    return section(read(*BOOT), "## Orchestrator: Bootstrap", 2)


def both_halves():
    """An absence has to hold in every file the text has lived in, or the
    move re-admits it."""
    return read(*SKILL) + read(*ORCH) + read(*BOOT)


# --- S4: one question, three options, records only first ------------------

RECORDS_ONLY = "**shared, records only**"
WITH_CHECKS = "**shared, with pull-request checks**"


def test_the_three_options_are_named_in_order_with_records_only_as_the_default():
    """#952: where the records live and whether CI checks pull requests are
    two answers, and the default installs nothing that can stop a teammate."""
    boot = bootstrap()
    assert "AskUserQuestion" in boot
    first, second = boot.index(RECORDS_ONLY), boot.index(WITH_CHECKS)
    local = boot.index("**local**")
    assert first < second < local, "the options are not in their order"
    assert "default" in boot[first:second], "records only is not the default"
    assert "**shared**" not in boot, "a two-option label is still offered"


def test_each_option_says_what_it_creates_and_what_it_installs():
    """S2 of #952: each shared option and the local one name the path of the
    root it creates, and the checks option names the command that writes
    the checks. What each option leaves alone is the proofer's to read."""
    boot = bootstrap()
    records = paragraph(boot, RECORDS_ONLY)
    checks = paragraph(boot, WITH_CHECKS)
    local = paragraph(boot, "**local**")
    # The path `<repo>/seal/`, where the orchestrator creates the shared
    # root and where `hooks/lib/optin.py` looks for it first.
    assert "creates `<repo>/seal/`" in records
    # The command `seal pr-checks install`, which the orchestrator runs
    # under this option.
    assert "`seal pr-checks install`" in checks, checks
    # The path of the local root, which the orchestrator creates and
    # `hooks/lib/optin.py` looks for second.
    assert f"creates `{COMMON_DIR}`" in local


def test_the_root_is_spelled_through_the_common_dir_never_the_literal():
    """`.git` is a FILE in a linked worktree, so the literal path lands nowhere."""
    assert "git rev-parse --git-common-dir" in bootstrap()
    assert "`.git/seal/`" not in both_halves()


def test_a_repository_with_the_root_at_either_place_is_never_asked():
    """S4 (d) and S12: the prompt budget is one question, once per repository."""
    never_again = paragraph(bootstrap(), "Ask only here")
    assert "either place" in never_again
    assert "<repo>/seal/" in never_again
    assert "git rev-parse --git-common-dir" in never_again


def test_the_parity_question_follows_the_mode_question():
    boot = bootstrap()
    assert boot.index("port behavior from an existing codebase") > boot.index(
        "**local**"
    )


# --- A9 of #401: the broad command is the second question, not a later one --
#
# `templates/setup/config.md` *Broad gate* says the row is a thing a PERSON wrote
# and that the seal covers exactly that. Nothing ever asked for it: grepped
# before this work, the bootstrap carried two `Ask, once` steps and neither
# was this one, and no command in `bin/` or `seal.py` wrote the row. So the
# question reached a person only as `seal gate`'s refusal -- after the review
# rounds had settled, which is the last moment available and the one where
# whoever is there has every reason to answer it themselves. That is what
# happened, and it is what #401 reported.
#
# Each case below was executed against `orchestration.md` as it stood at
# 81888e2, before the Bootstrap was edited, and each failed; the output is in
# the body of the commit that added them.

BROAD_ROW = "**The second question is the `Broad gate` row"


def test_the_broad_command_rides_the_question_that_already_stops_the_session():
    """#88's rule, one file over: questions that belong together are asked
    together. A second `AskUserQuestion` after the first is a second wait for
    one decision, and the prompt budget `CONTRIBUTING.md` guards is what a new
    one would owe an argument to. This adds none: the call already exists."""
    boot = bootstrap()
    assert boot.count("AskUserQuestion") == 1, (
        "the bootstrap opens more than one AskUserQuestion, which is the "
        "second wait this rides the first to avoid"
    )
    assert "two questions" in flat(boot), (
        "the one call is not said to carry both questions"
    )
    assert BROAD_ROW in boot, "the bootstrap does not ask for the row at all"
    assert boot.index(BROAD_ROW) > boot.index("**local**"), (
        "the row is asked before the mode's options are even laid out"
    )


# The paths the orchestrator opens to read a `Broad gate` candidate off the
# repository, the table's *Where to look* cells that name a path.
DERIVED = [
    ".github/workflows/*.yml",
    "a runner under `bin/`",
    "a `Makefile`",
]


def candidates():
    """The candidate table and the paragraph under it, bounded at the
    paragraph that follows — not the rest of the section.

    Round 1's 🟡 7. The slice ran from `BROAD_ROW` to the end of the whole
    Bootstrap section, so the four-row table could be moved anywhere below —
    past the decline paragraph, out of the question entirely — and every
    needle still matched a case named *the question proposes*.
    """
    boot = bootstrap()
    opening = "Read candidates off the repository"
    assert opening in boot, "the candidate table has no lead-in any more"
    body = boot[boot.index(opening) :]
    end = body.find("\n\n   **A candidate carrying")
    assert end > 0, "the candidate table is no longer followed by the pipe warning"
    return body[:end]


def test_the_question_proposes_candidates_read_off_the_repository():
    """Q4. A question with nothing in it is answered badly to get past it, and
    a repository being opted in may not yet know its broad command. The parity
    setup's shape is the answer — what the machine can derive is proposed and
    the person picks. The candidate table names the places the orchestrator
    reads candidates off."""
    row = candidates()
    for where in DERIVED:
        assert where in row, f"no candidate is read off {where}"


def test_a_candidate_carrying_a_pipe_is_escaped_where_candidates_are_derived():
    """Round 1's 🟡 2, second half, as #415 leaves it. The first source this
    table names is a CI `run:` step, and a `run:` step piping into `tee` is
    ordinary — so the bootstrap could derive a candidate, the person accept
    it, the session write it, and the row parse as no row.

    Such a candidate is written with the pipe escaped, and the warning gives
    the escape. What a bare one costs is the proofer's to read.
    """
    boot = flat(bootstrap())
    warning = boot[boot.index("**A candidate carrying a `|` is written") :]
    warning = warning[: warning.index("**Name the criterion")]
    # The escape `\|` the orchestrator writes into the `Broad gate` cell,
    # which the config reader turns back into a pipe; the code span is the
    # fact.
    assert "with the pipe escaped, `\\|`" in warning, (
        "the warning does not say how the pipe is written, which is the whole "
        "of what changed"
    )


def test_the_decline_names_the_command_back_to_the_row():
    """A question whose every answer must be a command is a gate wearing the
    shape of a question, so *Not yet* is offered. The decline paragraph names
    the command that fills the row in later; what the decline costs is the
    proofer's to read."""
    decline = paragraph(bootstrap(), "**Offer a decline, and say what it costs.**")
    # The command `/agentic:config`, which a person who declined types to
    # fill the `Broad gate` row in.
    assert "/agentic:config" in decline, "the decline names no way back to the row"


def test_the_criterion_is_named_by_pointer():
    """The criterion has one owner, `templates/setup/config.md`, and the
    bootstrap cites its section rather than spelling the three rules out."""
    pointer = paragraph(bootstrap(), "**Name the criterion; do not restate it.**")
    # The heading *The criterion for choosing a value*, which the person
    # answering resolves in `templates/setup/config.md`; the citation is the
    # fact.
    assert "*The criterion for choosing a value* owns the criterion" in pointer


def test_the_row_is_copied_from_the_template_up_to_its_bounding_heading():
    """The `Broad gate` row lands the way `/agentic:config` step 3 lands one,
    with the prose under its heading, copied from the plugin's template and
    stopped at the heading that follows it. When it lands and why no command
    writes it are the proofer's to read."""
    boot = flat(bootstrap())
    # The path the orchestrator copies the row and its prose from.
    assert "$CLAUDE_PLUGIN_ROOT/templates/setup/config.md" in boot
    # The heading `### What is refused, and what stays allowed`, where the
    # orchestrator stops copying; the heading is the fact.
    assert "down to but not including `### What is refused" in boot


def test_the_sentence_that_said_nowhere_else_is_gone():
    """The 0.4.0 sentence said the root is created at `<repo>/seal/` and
    nowhere else. Both files are read with their whitespace folded, so a
    line break inside the sentence cannot hide it.

    What is refused is that claim, not the two words: `skills/implement/
    SKILL.md` says the closing memo holds what is *nowhere else*, which is
    about something else and stays."""
    assert "`<repo>/seal/` and nowhere else" not in flat(both_halves())


OWN_SEAL = "**A `<repo>/seal/` whose `README.md` does not open with the marker"


def test_a_projects_own_seal_names_the_marker_template_and_the_git_dir_root():
    """First setup meeting a `seal/` the project keeps for itself names the
    template whose first line is the marker, and the path under the git
    directory where the root goes instead. That it writes nothing into the
    project's `seal/` is the proofer's to read."""
    own = paragraph(bootstrap(), OWN_SEAL)
    # The path of the template whose first line is the marker, which the
    # orchestrator opens to tell a project's own `seal/` from a root.
    assert "`templates/setup/seal-README.md`" in own, own
    # The path of the local root, which the orchestrator creates instead.
    assert f"`{COMMON_DIR}`" in own, own


# --- Q1: the sentence a session reads, once in each place -----------------


@pytest.mark.parametrize(
    "parts",
    [
        ("skills", "implement", "SKILL.md"),
        # Phases 3 and 4 of #107 re-pointed both definitions' rows here. The
        # sentence was in two of them verbatim and in the third not at all,
        # and the agent without it is the one that reads `seal/parity.md`. It
        # is contract rule 11 now, which every agent receives at startup.
        ("skills", "agent-contract", "SKILL.md"),
    ],
)
def test_the_session_rule_appears_once(parts):
    text = read(*parts)
    assert text.count(SESSION_RULE) == 1, "/".join(parts)
    assert "means `<repo>/seal/` where" in text, "/".join(parts)


@pytest.mark.parametrize("agent", ["proofer.md", "crafter.md"])
def test_no_definition_carries_its_own_copy_of_the_root_rule(agent):
    """The move has to be a move. A definition that keeps the sentence beside
    the contract's is the duplication contract rule 11 was written to end, and it is
    invisible in a diff that only adds."""
    assert SESSION_RULE not in read("agents", agent), (
        f"agents/{agent} still spells the root rule out, so the tree holds "
        "two homes for it again"
    )


def test_the_session_rule_sits_in_the_layout_section_of_the_skill():
    """The layout section runs from its heading to `## Procedure`; the
    bootstrap that used to close it left with #292 and is in
    `skills/implement/bootstrap.md` now (#1046)."""
    skill = read(*SKILL)
    assert (
        skill.index("## Document layout")
        < skill.index(SESSION_RULE)
        < skill.index("## Procedure")
    )


# --- S5 and S7: what `seal pr-checks install` writes, and local mode --------


def template():
    return read("templates", "setup", "hygiene.yml")


def test_the_template_runs_the_two_shipped_checks_from_the_plugin_at_its_tag():
    t = template()
    assert "skills/code-review/scripts/chain_check.py" in t
    assert "skills/implement/scripts/seal.py" in t
    # The unverified record's step left with #945: no step runs its reader.
    assert "unverified_check.py" not in t
    assert "--baseline" in t
    # The check reads a round record's `target:` line as an ancestor of HEAD only,
    # so the template fetches no pull-request heads (#923).
    assert "refs/pull/" not in t
    assert "v<version>" in t, "the plugin is not pinned to its tag"
    assert "MichaelYcJo/AgenticSeal" in t
    assert "RUNNER_TEMP" in t or "runner.temp" in t, "the plugin lands in the tree"


@pytest.mark.parametrize("stays_home", ["plugin.json", "fold_ledger", "README.ko.md"])
def test_the_rows_that_read_this_repository_do_not_travel(stays_home):
    assert stays_home not in template()


def test_the_template_header_names_the_commands_that_write_and_remove_it():
    """#952: the header of the workflow template names the command that
    writes the file and the one that takes it out. What local mode does to
    a copy is the proofer's to read."""
    header = flat(
        "\n".join(
            line
            for line in template().split("\nname:", 1)[0].splitlines()
            if line.startswith("#")
        )
    )
    # The command `seal pr-checks install`, which a person reading the
    # workflow file runs to write it; the code span is the fact.
    assert "`seal pr-checks install` writes" in header, header
    # The command a person runs to take the workflow out.
    assert "`seal pr-checks remove`" in header, header


def test_the_skill_names_the_workflow_paths_and_the_command_that_writes_it():
    """The orchestrator runs the command rather than writing the file, so
    the file has one writer (#952). The bootstrap names the template, the
    path it is written to, and the command. When the file is written is the
    proofer's to read."""
    boot = flat(bootstrap())
    # The template path and the workflow path, which the orchestrator
    # resolves to tell whether the command wrote the file or left one alone.
    assert "templates/setup/hygiene.yml" in boot
    assert ".github/workflows/hygiene.yml" in boot
    # The command `seal pr-checks install`, which the orchestrator runs
    # after `seal mode`; the code span is the fact.
    assert "then runs `seal pr-checks install`" in boot, boot


# --- S8 and S1: the READMEs -----------------------------------------------

READMES = {
    "README.md": ("## First run", "### Shared or local"),
    "README.ko.md": ("## 처음 실행", "### shared 인가 local 인가"),
}
# A workflow left after a move to local stays, and which pin passes is the
# rule's home to say, linked rather than restated (round 2 of #952, finding 1).
LEFT_BEHIND = {
    "README.md": (
        "A workflow left behind after a move to local stays in the tree, and "
        "`docs/one-root-by-lifetime.md` *Shared or local* says which pin passes "
        "there and how to move one that fails.",
    ),
    "README.ko.md": (
        "local 로 옮긴 뒤에도 워크플로는 트리에 남고, 어느 고정이 그곳에서 "
        "통과하는지와 실패하는 고정을 어떻게 옮기는지는 "
        "`docs/one-root-by-lifetime.ko.md` *shared 인가 local 인가* 가 "
        "말합니다.",
    ),
}


@pytest.mark.parametrize("readme", sorted(READMES))
def test_the_readme_gives_both_moves_under_first_run(readme):
    text = read(readme)
    first_run, subsection = READMES[readme]
    assert text.index(subsection) > text.index(first_run)
    body = section(text, subsection, 3)
    assert f'mv "{COMMON}" "{TOP}"' in body
    assert f'git add "{TOP}"' in body
    assert f'git rm -r --cached "{TOP}"' in body
    assert f'mv "{TOP}" "{COMMON}"' in body
    assert "seal pr-checks install" in body and "seal pr-checks remove" in body, (
        "the checks are their own command, and the section does not name it"
    )
    # #1055 S6: the way back before the commit to shared has one home, the
    # skill section, which the README links to and does not restate.
    assert "git reset -- :/seal" not in body, readme
    assert SHARED_WAY_BACK in flat(body), readme
    for sentence in LEFT_BEHIND[readme]:
        assert sentence in flat(body), sentence
    assert "seal export" in body and "seal import" in body, (
        "the move is only available where both folders are on one machine, so "
        "this section has to point at the pair that works between two (#81). "
        "It named the issue number while the pair was later work"
    )


COMMON = "$(git rev-parse --git-common-dir)/seal"
TOP = "$(git rev-parse --show-toplevel)/seal"

# The one home of the way back before the commit to shared (#1055 S6), and
# the citation of it each README carries.
SHARED_HEADING = "Before switching to shared, say what cannot be undone"
SHARED_WAY_BACK = f"`skills/config/SKILL.md` *{SHARED_HEADING}*"


def test_the_way_back_before_the_commit_to_shared_is_told_in_its_home():
    """#1055 S6. The skill section is where the way back is said before the
    act, so it holds the command and both reasons the READMEs used to give,
    and it cites the policy for the rule rather than restating it."""
    skill = read("skills", "config", "SKILL.md")
    body = flat(section(skill, "## " + SHARED_HEADING, 2))
    for said in (
        "`git reset -- :/seal` and then `seal mode local` walk the whole thing back",
        "refuses a switch over a staged change",
        "a bare `git reset` unstages the whole index",
        "`docs/one-root-by-lifetime.md` *Shared or local*",
    ):
        assert said in body, said


def switch_block(readme):
    """The BY-HAND `bash` block under the README's switch section, comments
    off: two lines, local → shared and then shared → local.

    Bounded at the next `## ` heading and asserted to be there: the lines
    are run under `bash -c`, so a block that left its section must fail
    here rather than let a later block run in its place.

    The section holds more than one block since #104, which made switching a
    command (`seal mode`) and kept the by-hand pair below it. Taking "the
    first block" would hand `seal mode local` to `bash -c` and fail on a
    PATH this suite does not set up — so the block is chosen by what is IN
    it, and every candidate is read rather than the search stopping at the
    first that parses. A section that stopped carrying the by-hand pair
    fails here, which is the point: those two lines are what the command's
    move has to keep doing.
    """
    text = read(readme)
    _first_run, heading = READMES[readme]
    body = section(text, heading, 3).split("\n## ", 1)[0]
    assert "```bash\n" in body, f"{readme}: the switch block left its section"
    for chunk in body.split("```bash\n")[1:]:
        block = chunk.split("```", 1)[0]
        lines = [ln.split("#", 1)[0].strip() for ln in block.splitlines()]
        lines = [ln for ln in lines if ln]
        if len(lines) == 2 and all("mv " in ln for ln in lines):
            return lines
    raise AssertionError(
        f"{readme}: no bash block in the switch section holds the two by-hand "
        "moves. `seal mode` does that move, and this is where the move itself "
        "is checked against a subdirectory as the working directory"
    )


def porcelain(repo):
    return subprocess.run(
        ["git", "-C", str(repo), "status", "--porcelain"],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.splitlines()


@pytest.mark.parametrize("readme", sorted(READMES))
def test_the_switch_block_lands_the_root_at_the_tree_root_from_a_subdirectory(
    readme, repo
):
    """Round 1 of #80, 🟡 3. The two moves were spelled relative to the
    working directory: run from `src/`, `git rev-parse --git-common-dir`
    answers `../.git` and `mv … seal && git add seal` created and staged
    `src/seal/`, after which neither place held a root and the repository
    was opted OUT. Both paths are asked of git now, so the block read out of
    the document and run from a subdirectory lands the root at `<repo>/seal/`
    one way and back under the common directory the other.

    A bash block, run under `bash -c` line by line; the precondition is
    executed, not assumed (`shell_probe`, for the reason its docstring
    gives).
    """
    why = shell_probe("bash")
    if why:
        pytest.skip(f"bash: {why} -- the switch block is a bash block")
    home = local_home(repo)
    (home / "ledger").mkdir()
    (home / "ledger" / "f.md").write_text("# rows\n", encoding="utf-8")
    sub = repo / "src"
    sub.mkdir()
    to_shared, to_local = switch_block(readme)

    r = subprocess.run(["bash", "-c", to_shared], cwd=str(sub), capture_output=True)
    assert r.returncode == 0, r.stderr
    assert (repo / "seal" / "ledger" / "f.md").is_file(), porcelain(repo)
    assert not (sub / "seal").exists(), "the root landed under the subdirectory"
    assert not home.exists(), "the local root was copied, not moved"
    assert porcelain(repo) == ["A  seal/README.md", "A  seal/ledger/f.md"], porcelain(
        repo
    )

    r = subprocess.run(["bash", "-c", to_local], cwd=str(sub), capture_output=True)
    assert r.returncode == 0, r.stderr
    assert (home / "ledger" / "f.md").is_file(), porcelain(repo)
    assert not (repo / "seal").exists()
    assert not (sub / "seal").exists()
    assert porcelain(repo) == [], porcelain(repo)


@pytest.mark.parametrize("readme", sorted(READMES))
def test_the_gates_table_says_the_root_may_sit_under_the_git_dir(readme):
    # The gate table's rows alone: since #1055 the `seal/` row of the records
    # table names `seal/` in its last cell too, and that cell is no Where.
    lines = read(readme).splitlines()
    start = next(
        i for i, ln in enumerate(lines) if ln.startswith(("| Gate |", "| 게이트 |"))
    )
    table = []
    for line in lines[start + 2 :]:
        if not line.startswith("|"):
            break
        table.append(line)
    rows = [line for line in table if "`seal/`" in line.rsplit("|", 2)[-2]]
    assert rows, f"{readme}: no gate row's Where cell names `seal/`"
    # #1055 round 1, finding 1: *First run* and the records table's `seal/`
    # row select the opt-in hooks by `seal/` in this column, so a Where cell
    # that points at another row ("same opt-in") drops its hook from that
    # pointer. Each cell names its condition itself, and implementer-notice,
    # which returns before anything where `optin.opted_in` is false
    # (`hooks/implementer-notice.py#notify`), is among the `seal/` rows.
    for row in table:
        where = row.rsplit("|", 2)[-2].strip()
        assert not where.startswith(("same ", "같은 ")), f"{readme}: {row[:40]}…"
    assert any(row.startswith("| implementer-notice |") for row in rows), readme
    for row in rows:
        where = row.rsplit("|", 2)[-2]
        assert "local" in where, f"{readme}: {row[:40]}… still says the root only"


# --- S14: the root's own README, and the template it is rendered from ------


@pytest.mark.parametrize(
    "parts", [("seal", "README.md"), ("templates", "setup", "seal-README.md")]
)
def test_the_seal_readme_names_both_places(parts):
    text = read(*parts)
    assert "git rev-parse --git-common-dir" in text, "/".join(parts)
    assert "local" in text and "shared" in text, "/".join(parts)
    assert "either" in text, "/".join(parts)


def test_the_seal_readme_is_the_template_verbatim():
    assert read("seal", "README.md") == read("templates", "setup", "seal-README.md")


MARKER_SAID = "**The first line of this file is the marker.**"


def test_the_seal_readme_cites_the_marker_constant():
    """The root's own README tells a person not to edit the line the gates
    read, and cites the constant that holds it. What a `seal/` without the
    line is, is the proofer's to read."""
    text = read("templates", "setup", "seal-README.md")
    said = paragraph(text, MARKER_SAID)
    # The citation `hooks/lib/optin.py#MARKER`, which a person resolves to
    # the one spelling of the line the gates read.
    assert "`hooks/lib/optin.py#MARKER`" in said, said


def test_the_seal_readme_points_at_the_drain_and_restates_none_of_it():
    """Round 2 of #940, finding 2. Who moves a work item's open rows, when
    and where each goes is `skills/implement/SKILL.md` section 6's alone; a
    second statement here drifted from it on all three. The README names the
    section and carries no destination of its own."""
    text = read("templates", "setup", "seal-README.md")
    rules = flat(text.split("\n## Export rules\n", 1)[1].split("\n## ", 1)[0])
    heading = "### 6. Drain the rows before the broad run, and keep the records"
    assert heading in read("skills", "implement", "SKILL.md")
    cited = "`skills/implement/SKILL.md` " + f"*{heading[4:]}*"
    assert cited in rules, rules
    for copied in ("| Item still here |", "follow-up.md", "open-questions"):
        assert copied not in rules, (copied, rules)


# --- Q8: the design record agrees with the code -----------------------------


@pytest.mark.parametrize(
    "parts, wrong",
    [
        (
            ("docs", "one-root-by-lifetime.md"),
            "would refuse a pull request with no round records",
        ),
        (
            ("docs", "one-root-by-lifetime.ko.md"),
            "라운드 기록이 없는 PR 은 그 워크플로에서",
        ),
    ],
)
def test_the_record_no_longer_says_the_checks_would_refuse(parts, wrong):
    text = read(*parts)
    assert wrong not in text, "/".join(parts)


@pytest.mark.parametrize(
    "parts, opt_in, setup",
    [
        (
            ("docs", "one-root-by-lifetime.md"),
            "## The opt-in signal is the root itself",
            "## What first setup asks",
        ),
        (
            ("docs", "one-root-by-lifetime.ko.md"),
            "## 옵트인 신호는 루트 자체다",
            "## 처음 설정에서 무엇을 묻는가",
        ),
    ],
)
def test_the_design_record_states_the_setup_rules_where_they_rule(parts, opt_in, setup):
    """The opt-out sits with the opt-in it takes back, and the question's
    shape and the workflow it installs sit with first setup, in both
    editions."""
    text = read(*parts)
    assert "agentic-scratch" in section(text, opt_in, 2), "/".join(parts)
    body = " ".join(section(text, setup, 2).split())
    for needle in ("templates/setup/hygiene.yml", COMMON_DIR, "AskUserQuestion"):
        assert needle in body, f"{'/'.join(parts)}: {setup} does not name {needle}"


# --- #151: the route that actually happens, and the state it leaves ---------
#
# The bootstrap above is where the mode question lives, and the cases in this
# file all reach it by reading the skill. That is not how a session gets
# there. A session is told to write `seal/threads/<id>/routing.md` before the
# first edit, and that write creates `seal/`, which opts the repository in.
# Until #1177 the preset block in `~/.claude/CLAUDE.md` said so in every
# project on the machine, and the cases that read it were written against the
# block as it stood at 589cf25, each failing first. The block is retired; the
# core, which the plugin's `SessionStart` hook prints into every session,
# names the routing section (`tests/text/test_review_axes.py`), and the cases
# below read the orchestrator's half and the Bootstrap, the files that hold
# the rule.


def test_the_orchestrators_half_sends_a_fresh_repository_to_the_bootstrap():
    """S3 of #1046. A session that opens `orchestration.md` first, under an
    older release's preset block written before the bootstrap left that
    file, meets the bootstrap's file in the opening paragraph, before any
    section, with both places the root can be."""
    opening = paragraph(read(*ORCH), "This file is the orchestrator's")
    # The path of the bootstrap, which the orchestrator opens where no root
    # stands yet.
    assert "`skills/implement/bootstrap.md`" in opening, (
        "the orchestrator's half does not send a fresh repository to the bootstrap"
    )
    # The two paths the orchestrator looks at for a root before it opens
    # the bootstrap.
    assert "`<repo>/seal/`" in opening, opening
    assert COMMON_DIR in opening, opening


def test_the_bootstrap_records_the_answer_it_was_given():
    """#151's second Done-when: the answer has to be observable afterwards.
    An asked-and-answered root and a root that appeared because a session
    followed the routing rule are byte-identical until something writes the
    row — and `hooks/mode-gate.py` reads exactly that absence, so a bootstrap
    that records nothing gets the person it just asked asked again."""
    boot = flat(bootstrap())
    assert "seal mode" in boot
    assert "Do **not** write that config row here" not in both_halves(), (
        "the skill still forbids recording the answer it just collected"
    )


def test_the_gate_that_reads_the_absence_exists_and_is_wired():
    """The document half and the mechanism half are one change. A skill that
    says a gate reads this, beside no such gate, is the shape #151 opened
    about one layer up."""
    hooks = os.path.join(ROOT, "hooks")
    assert os.path.isfile(os.path.join(hooks, "mode-gate.py"))
    dispatch = read("hooks", "dispatch.py")
    assert '"mode-gate.py"' in dispatch
