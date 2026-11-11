"""First setup asks once — shared or local — and every document that a session
or a person reads says the same thing about where the root lives.

Each case states the clause it holds and names it by its number, and a
number another work item gave carries that item's issue, as `S2 of #952`
does. The commands resolve
the root in code (`lib/optin.py#home_at`) and are pinned by
`tests/lib/test_optin.py`. What is pinned HERE
is the text: the one question the `implement`
skill asks, the sentence a session needs, the workflow template
`seal pr-checks install` writes and the commands its header names, and the
switch the READMEs give.
"""

import re
import subprocess

import pytest
from conftest import local_home, read, shell_probe

COMMON_DIR = "$(git rev-parse --git-common-dir)/seal/"
# The sentence a session reads, which the Q1 cases below hold in each place:
# the same rule `lib/optin.py` states, moved to where a session looks.
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


# --- S4: one question, three options, records only first ------------------

RECORDS_ONLY = "**shared, records only**"
WITH_CHECKS = "**shared, with pull-request checks**"


def test_the_three_options_are_named_in_order():
    """#952: where the records live and whether CI checks pull requests are
    two answers, and the default installs nothing that can stop a teammate.
    Which option the bootstrap marks as the default is the proofer's to
    read."""
    boot = bootstrap()
    # The harness tool the orchestrator calls to put the question.
    assert "AskUserQuestion" in boot
    # The three option labels the orchestrator puts to the person, in that
    # order; label and position are the fact.
    first, second = boot.index(RECORDS_ONLY), boot.index(WITH_CHECKS)
    local = boot.index("**local**")
    assert first < second < local, "the options are not in their order"


def test_each_option_says_what_it_creates_and_what_it_installs():
    """S2 of #952: each shared option and the local one name the path of the
    root it creates, and the checks option names the command that writes
    the checks. What each option leaves alone is the proofer's to read."""
    boot = bootstrap()
    records = paragraph(boot, RECORDS_ONLY)
    checks = paragraph(boot, WITH_CHECKS)
    local = paragraph(boot, "**local**")
    # The path `<repo>/seal/`, where the orchestrator creates the shared
    # root and where `lib/optin.py` looks for it first.
    assert "creates `<repo>/seal/`" in records
    # The command `seal pr-checks install`, which the orchestrator runs
    # under this option.
    assert "`seal pr-checks install`" in checks, checks
    # The path of the local root, which the orchestrator creates and
    # `lib/optin.py` looks for second.
    assert f"creates `{COMMON_DIR}`" in local


def test_the_root_is_spelled_through_the_common_dir_never_the_literal():
    """`.git` is a FILE in a linked worktree, so the literal path lands
    nowhere, and the bootstrap asks git for the common directory."""
    # The command the orchestrator runs to find where the local root goes.
    assert "git rev-parse --git-common-dir" in bootstrap()
    # `skills/implement/bootstrap.md` *Orchestrator: Bootstrap*, its **local**
    # option: the path is spelled through the common git directory rather
    # than through `.git`, which is a file in a linked worktree. The path is
    # one the orchestrator would create.
    assert "`.git/seal/`" not in bootstrap()


def test_a_repository_with_the_root_at_either_place_is_never_asked():
    """S4 (d) and S12: the prompt budget is one question, once per repository.
    The paragraph names the two places the orchestrator looks before it
    asks."""
    never_again = paragraph(bootstrap(), "Ask only here")
    # The path of the shared root and the command that finds the local one,
    # which the orchestrator checks before it asks.
    assert "<repo>/seal/" in never_again
    assert "git rev-parse --git-common-dir" in never_again


def test_the_parity_question_follows_the_mode_question():
    boot = bootstrap()
    assert boot.index("port behavior from an existing codebase") > boot.index(
        "**local**"
    )


# --- A9 of #401 and #1453: the keys first setup asks for -------------------

LANGUAGE_ROWS = ("Commit and pull request language", "Record language")


def test_the_one_call_asks_for_the_two_language_rows_with_the_titles_beside_them():
    """#1453. `seal pr-body` refuses a repository without either language
    key, so first setup asks for both in the call that already stops the
    session, with the recent pull request titles shown beside the question,
    and writes the answers into the file `seal mode` wrote. What each option
    says its key governs is the proofer's to read."""
    boot = flat(bootstrap())
    # The two keys of `config.json` first setup asks for, which
    # `lib/config.py#declared_value` reads.
    for key in LANGUAGE_ROWS:
        assert f"`{key}`" in boot, f"first setup does not ask for `{key}`"
    # The command whose titles the orchestrator shows beside the question,
    # the one `skills/commit-pr-convention/SKILL.md` opens with.
    assert "gh pr list --state all --limit 10" in boot, (
        "the language questions show no history to answer them from"
    )
    # The paragraph that writes the answered keys into the file.
    assert "**Then the two language keys.**" in boot, (
        "nothing writes the answered keys into the file `seal mode` wrote"
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

    Round 1's 🟡 7. The slice ran from the `Broad gate` question's lead to
    the end of the whole Bootstrap section, so the four-row table could be
    moved anywhere below — past the decline paragraph, out of the question
    entirely — and every needle still matched a case named *the question
    proposes*.
    """
    boot = bootstrap()
    opening = "Read candidates off the repository"
    assert opening in boot, "the candidate table has no lead-in any more"
    body = boot[boot.index(opening) :]
    end = body.find("\n\n   **A candidate carrying")
    assert end > 0, "the candidate table is no longer followed by the escape warning"
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


def test_a_candidate_carrying_a_quote_or_a_backslash_is_escaped_where_derived():
    """Round 1's 🟡 2, second half, as #1454 leaves it. The first source this
    table names is a CI `run:` step, and a `run:` step quoting an argument is
    ordinary — so the bootstrap could derive a candidate, the person accept
    it, the session write it, and the file parse as no JSON.

    Such a candidate is written with the `"` or the `\\` escaped, and the
    warning gives the escape. What a bare one costs, and what the warning
    says of a pipe, are the proofer's to read.
    """
    boot = flat(bootstrap())
    warning = boot[boot.index('**A candidate carrying a `"` or a `\\` is written') :]
    warning = warning[: warning.index("**Name the criterion")]
    # The JSON escapes the orchestrator writes into the `Broad gate` value,
    # which the parser turns back into the characters; the code spans are
    # the fact.
    assert 'with it escaped, `\\"` or `\\\\`' in warning, (
        "the warning does not say how the character is written, which is the "
        "whole of what changed"
    )


def test_the_decline_names_the_command_back_to_the_row():
    """A question whose every answer must be a command is a gate wearing the
    shape of a question, so *Not yet* is offered. The decline paragraph names
    the command that fills the key in later; what the decline costs is the
    proofer's to read."""
    decline = paragraph(bootstrap(), "**Offer a decline, and say what it costs.**")
    # The command `/agentic:config`, which a person who declined types to
    # fill the `Broad gate` key in.
    assert "/agentic:config" in decline, "the decline names no way back to the key"


def test_the_criterion_is_named_by_pointer():
    """The criterion has one owner, `templates/setup/config.md`, and the
    bootstrap cites its section rather than spelling the three rules out."""
    pointer = paragraph(bootstrap(), "**Name the criterion; do not restate it.**")
    # The heading *The criterion for choosing a value*, which the person
    # answering resolves in `templates/setup/config.md`; the citation is the
    # fact.
    assert "*The criterion for choosing a value* owns the criterion" in pointer


def test_the_key_is_added_alone_and_its_documentation_is_pointed_at():
    """#1454. The `Broad gate` key lands the way `/agentic:config` step 3
    lands one: the key alone, since a JSON file carries no prose. The lists
    and the criterion stay in the plugin's template, which the paragraph
    names. When it lands and why no command writes it are the proofer's to
    read."""
    landing = paragraph(
        bootstrap(), "**Then the `Broad gate` key, where a command was chosen.**"
    )
    # The key and value as the orchestrator writes them into `config.json`.
    assert '`"Broad gate": "<command>"`' in landing
    # The path the orchestrator reads the lists and the criterion at.
    assert "$CLAUDE_PLUGIN_ROOT/templates/setup/config.md" in landing


OWN_SEAL = "**A `<repo>/seal/` whose `README.md` does not open with the marker"


def test_a_projects_own_seal_names_the_marker_template_and_the_git_dir_root():
    """First setup meeting a `seal/` the project keeps for itself names the
    template whose first line is the marker, the command whose output gives
    the shared place in its stead (#1059), and the path under the git
    directory where the root goes where that place is the project's own too.
    That it writes nothing into either is the proofer's to read."""
    own = paragraph(bootstrap(), OWN_SEAL)
    # The path of the template whose first line is the marker, which the
    # orchestrator opens to tell a project's own `seal/` from a root.
    assert "`templates/setup/seal-README.md`" in own, own
    # The command that prints the shared place, which no core printed into
    # the session can give at first setup.
    assert "`seal mode`" in own, own
    # The path of the local root, which the orchestrator creates instead.
    assert f"`{COMMON_DIR}`" in own, own


# --- Q1: the sentence a session reads, once in each place -----------------


@pytest.mark.parametrize(
    "parts",
    [
        ("skills", "implement", "SKILL.md"),
        # Phases 3 and 4 of #107 re-pointed both definitions' rows here. The
        # sentence was in two of them verbatim and in the third not at all,
        # and the agent without it is the one that reads `seal/parity.json`. It
        # is contract rule 11 now, which every agent receives at startup.
        ("skills", "agent-contract", "SKILL.md"),
    ],
)
def test_the_session_rule_names_both_places(parts):
    text = read(*parts)
    # The two places a session resolves the root at: the path of the shared
    # root, and the local one through the command that finds it.
    assert "`<repo>/seal/`" in text, "/".join(parts)
    assert SESSION_RULE in text, "/".join(parts)


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
    # The two scripts the workflow's steps run, from the plugin's clone.
    assert "skills/code-review/scripts/chain_check.py" in t
    assert "skills/implement/scripts/seal.py" in t
    # The flag a step passes the script it runs.
    assert "--baseline" in t
    # The tag placeholder `seal pr-checks install` fills, and the repository
    # the step clones at that tag.
    assert "v<version>" in t, "the plugin is not pinned to its tag"
    assert "MichaelYcJo/AgenticSeal" in t
    # The runner's temporary directory the step clones the plugin into.
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
    assert "`seal pr-checks install`" in boot, boot


# --- S8 and S1: the READMEs -----------------------------------------------

READMES = {
    "README.md": ("## Your first work item", "### Shared or local"),
    "README.ko.md": ("## 첫 작업 항목", "### shared 인가 local 인가"),
}
# A workflow left after a move to local stays, and which pin passes is the
# rule's home to say, linked rather than restated (round 2 of #952, finding 1):
# the citation of that home in each edition, which a reader resolves.
LEFT_BEHIND = {
    "README.md": "`docs/layout/one-root-by-lifetime.md` *Shared or local*",
    "README.ko.md": "`docs/layout/one-root-by-lifetime.ko.md` *shared 인가 local 인가*",
}


@pytest.mark.parametrize("readme", sorted(READMES))
def test_the_readme_gives_the_switch_under_the_first_work_item(readme):
    """The subsection stands under the section that walks a first reader
    through a work item, and names the checks' command, the way back before
    the commit to shared, the workflow a move to local leaves, and the pair
    that works between two machines. The two by-hand moves left both
    editions in #1102 for the template every root's `seal/README.md` is, and
    `switch_block` reads them there."""
    text = read(readme)
    first_run, subsection = READMES[readme]
    assert text.index(subsection) > text.index(first_run)
    body = section(text, subsection, 3)
    # The two commands a person runs to install and remove the checks.
    assert "seal pr-checks install" in body and "seal pr-checks remove" in body, (
        "the checks are their own command, and the section does not name it"
    )
    # #1055 S6: the citation of the skill section that holds the way back
    # before the commit to shared, which a reader resolves.
    assert SHARED_WAY_BACK in flat(body), readme
    # The citation of the section that says which pin a workflow left behind
    # by a move to local passes, which a reader resolves.
    assert LEFT_BEHIND[readme] in flat(body), LEFT_BEHIND[readme]
    # The pair of commands a person runs to carry the records between two
    # machines.
    assert "seal export" in body and "seal import" in body, (
        "the move is only available where both folders are on one machine, so "
        "this section has to point at the pair that works between two (#81). "
        "It named the issue number while the pair was later work"
    )


# What local mode leaves unchecked, said once under each edition's table of
# the three answers: no pull-request check reads records that are not
# committed, and no mechanism stands in for it (#1376).
LOCAL_LIMIT = {
    "README.md": (
        "In local mode no pull-request check reads the records, so "
        "`agents/sealer.md` step 1 and the orchestrator's guidance alone hold "
        "the four rows of `skills/core/SKILL.md` *Judgment is not licence "
        "to skip a party*, and that is a limit."
    ),
    "README.ko.md": (
        "local 모드에서는 기록을 커밋하지 않으므로 pull request 검사가 읽을 "
        "기록이 없습니다. 그래서 `skills/core/SKILL.md` *Judgment is not "
        "licence to skip a party* 표의 네 행은 sealer 의 1단계"
        "(`agents/sealer.md`)와 작업을 이끄는 세션이 따르는 지침만이 지키며, "
        "이것이 local 모드의 한계입니다."
    ),
}


@pytest.mark.parametrize("readme", sorted(READMES))
def test_the_readme_states_what_local_mode_leaves_unchecked_under_the_table(readme):
    """The paragraph right under the table of the three answers says that in
    local mode nothing checks the pull request's rows of the core's table,
    and names what holds them, as a limit."""
    body = section(read(readme), READMES[readme][1], 3)
    chunks = body.split("\n\n")
    table = next(i for i, chunk in enumerate(chunks) if chunk.startswith("|"))
    assert flat(chunks[table + 1]) == LOCAL_LIMIT[readme], chunks[table + 1]


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
        "`docs/layout/one-root-by-lifetime.md` *Shared or local*",
    ):
        assert said in body, said


TO_SHARED, TO_LOCAL = "From local to shared:", "From shared to local:"


def switch_block():
    """The two by-hand moves `templates/setup/seal-README.md` gives, local →
    shared and then shared → local, each as one command line.

    Each move is the code spans after its lead, to the end of the paragraph,
    joined with `&&`. The template is every root's own `seal/README.md`, and
    the README links it for the moves rather than restating them (#1102). A
    paragraph that stopped carrying two spans after each lead fails here,
    which is the point: those lines are what `seal mode`'s move has to keep
    doing, and this is where they are run from a subdirectory.
    """
    text = read("templates", "setup", "seal-README.md")
    assert TO_SHARED in text, f"no paragraph gives the move {TO_SHARED!r}"
    paragraph = flat(text.split(TO_SHARED, 1)[1].split("\n\n", 1)[0])
    assert TO_LOCAL in paragraph, f"the paragraph gives no move {TO_LOCAL!r}"
    moves = [re.findall(r"`([^`]+)`", half) for half in paragraph.split(TO_LOCAL)]
    for spans in moves:
        assert len(spans) == 2, spans
    return [" && ".join(spans) for spans in moves]


def porcelain(repo):
    return subprocess.run(
        ["git", "-C", str(repo), "status", "--porcelain"],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.splitlines()


def test_the_switch_block_lands_the_root_at_the_tree_root_from_a_subdirectory(repo):
    """Round 1 of #80, 🟡 3. The two moves were spelled relative to the
    working directory: run from `src/`, `git rev-parse --git-common-dir`
    answers `../.git` and `mv … seal && git add seal` created and staged
    `src/seal/`, after which neither place held a root and the repository
    was opted OUT. Both paths are asked of git now, so the two moves read out
    of the template and run from a subdirectory land the root at
    `<repo>/seal/` one way and back under the common directory the other.

    Each move is run under `bash -c`; the precondition is executed, not
    assumed (`shell_probe`, for the reason its docstring gives).
    """
    why = shell_probe("bash")
    if why:
        pytest.skip(f"bash: {why} -- the switch block is a bash block")
    home = local_home(repo)
    (home / "ledger").mkdir()
    (home / "ledger" / "f.md").write_text("# rows\n", encoding="utf-8")
    sub = repo / "src"
    sub.mkdir()
    to_shared, to_local = switch_block()

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


# --- S14: the root's own README, and the template it is rendered from ------


@pytest.mark.parametrize(
    "parts", [("seal", "README.md"), ("templates", "setup", "seal-README.md")]
)
def test_the_seal_readme_names_the_command_that_finds_the_local_root(parts):
    text = read(*parts)
    # The command a person runs to find the root in local mode.
    assert "git rev-parse --git-common-dir" in text, "/".join(parts)


def test_the_seal_readme_is_the_template_verbatim():
    assert read("seal", "README.md") == read("templates", "setup", "seal-README.md")


MARKER_SAID = "**The first line of this file is the marker.**"


def test_the_seal_readme_cites_the_marker_constant():
    """The root's own README tells a person not to edit the line the gates
    read, and cites the constant that holds it. What a `seal/` without the
    line is, is the proofer's to read."""
    text = read("templates", "setup", "seal-README.md")
    said = paragraph(text, MARKER_SAID)
    # The citation `lib/optin.py#MARKER`, which a person resolves to
    # the one spelling of the line the gates read.
    assert "`lib/optin.py#MARKER`" in said, said


def test_the_seal_readme_points_at_the_drain_and_restates_none_of_it():
    """Round 2 of #940, finding 2. Who moves a work item's open rows, when
    and where each goes is `skills/implement/orchestration.md`'s drain
    section's alone; a second statement here drifted from it on all three.
    The README names the section and carries no destination of its own."""
    text = read("templates", "setup", "seal-README.md")
    rules = flat(text.split("\n## Export rules\n", 1)[1].split("\n## ", 1)[0])
    heading = (
        "## Orchestrator: drain the rows before the broad run, and keep the records"
    )
    assert heading in read("skills", "implement", "orchestration.md")
    cited = "`skills/implement/orchestration.md` " + f"*{heading[3:]}*"
    assert cited in rules, rules
    for copied in ("| Item still here |", "follow-up.md", "open-questions"):
        assert copied not in rules, (copied, rules)


# --- Q8: the design record agrees with the code -----------------------------


@pytest.mark.parametrize(
    "parts, wrong",
    [
        (
            ("docs", "layout", "one-root-by-lifetime.md"),
            "would refuse a pull request with no round records",
        ),
        (
            ("docs", "layout", "one-root-by-lifetime.ko.md"),
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
            ("docs", "layout", "one-root-by-lifetime.md"),
            "## The opt-in signal is the root itself",
            "## What first setup asks",
        ),
        (
            ("docs", "layout", "one-root-by-lifetime.ko.md"),
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
    # The name of the opt-out file, which `lib/optin.py` looks for.
    assert "agentic-scratch" in section(text, opt_in, 2), "/".join(parts)
    body = " ".join(section(text, setup, 2).split())
    # The template path, the local root's path and the harness tool, which
    # the orchestrator resolves at first setup.
    for needle in ("templates/setup/hygiene.yml", COMMON_DIR, "AskUserQuestion"):
        assert needle in body, f"{'/'.join(parts)}: {setup} does not name {needle}"


# --- #151: the route that actually happens, and the state it leaves ---------
#
# The bootstrap above is where the mode question lives, and the cases in this
# file all reach it by reading the skill. That is not how a session gets
# there. A session is told to write `seal/threads/<id>/routing.md` before the
# first edit, and that write creates `seal/`, which opts the repository in.
# Until #1177 the preset block in `~/.claude/CLAUDE.md` said so in every
# project on the machine. The block is retired; the core, which the plugin's
# `SessionStart` hook prints into a session, names the routing section
# (`tests/text/test_review_axes.py`), and the cases
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
    key, so a bootstrap that records nothing leaves no trace that anybody was
    asked."""
    boot = flat(bootstrap())
    # The command the orchestrator runs to record the answer.
    assert "seal mode" in boot
