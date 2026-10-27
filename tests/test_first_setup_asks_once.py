"""First setup asks once — shared or local — and every document that a session
or a person reads says the same thing about where the root lives.

The work item is `seal/specs/1788354065-the-tree-that-must-stay-clean-has-no-
way-to-opt-in/`; the clauses named per case are its spec's. The hooks resolve
the root in code (`hooks/optin.py#home_at`) and are pinned by
`tests/test_optin.py`, `tests/test_commit_review_gate.py` and
`tests/test_implementer_notice.py`. What is pinned HERE
is the text: the one question the `implement`
skill asks, the sentence a session needs, the workflow template
`seal pr-checks install` writes and what local mode does to it, and the
switch the READMEs give.

Every case was executed against the documents as they stood at 7e44106,
before any of them was edited, and every case failed; the output is in the
body of the commit that added this file.
"""

import os
import re
import subprocess

import pytest
from conftest import local_home, read, shell_probe

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

COMMON_DIR = "$(git rev-parse --git-common-dir)/seal/"
# The sentence a session reads (Q1 of the work item's `questions.md`): the
# same rule `hooks/optin.py` states, moved to where a session looks.
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
# The bootstrap is the orchestrator's half since #292: it asks a person, which
# a smith spawn may not, so it lives in the file no `skills:` list injects.
ORCH = ("skills", "implement", "orchestration.md")


def bootstrap():
    return section(read(*ORCH), "## Orchestrator: Bootstrap", 2)


def both_halves():
    """An absence has to hold in both files, or the move re-admits it."""
    return read(*SKILL) + read(*ORCH)


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
    """S2 of #952: records only writes nothing under `.github/`, and the
    checks are the command's to write."""
    boot = bootstrap()
    records = paragraph(boot, RECORDS_ONLY)
    checks = paragraph(boot, WITH_CHECKS)
    local = paragraph(boot, "**local**")
    assert "creates `<repo>/seal/`" in records
    assert "routing commit" in records, (
        "the shared option does not say what carries the root"
    )
    assert "writes nothing under `.github/`" in records, records
    assert "`seal pr-checks install`" in checks, checks
    assert f"creates `{COMMON_DIR}`" in local
    assert "installs nothing" in local
    assert "touches nothing in the tree" in local


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
# `templates/config.md` *Broad gate* says the row is a thing a PERSON wrote
# and that the seal covers exactly that. Nothing ever asked for it: grepped
# before this work, the bootstrap carried two `Ask, once` steps and neither
# was this one, and no command in `bin/` or `seal.py` wrote the row. So the
# question reached a person only as `broad-gate`'s refusal -- after the review
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


DERIVED = [
    ".github/workflows/*.yml",
    "a runner under `bin/`",
    "a package manifest",
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
    the person picks — so the floor is at least one derived candidate where
    one is findable, each named with the file it came from."""
    boot = bootstrap()
    assert boot.index("Read candidates off the repository") > boot.index(BROAD_ROW), (
        "the candidate table has left the question it belongs to"
    )
    row = candidates()
    for where in DERIVED:
        assert where in row, f"no candidate is read off {where}"
    assert "name the file it came from" in flat(row), (
        "a candidate with no source is one the person cannot correct"
    )


def test_a_candidate_carrying_a_pipe_is_escaped_where_candidates_are_derived():
    """Round 1's 🟡 2, second half, as #415 leaves it. The first source this
    table names is a CI `run:` step, and a `run:` step piping into `tee` is
    ordinary — so the bootstrap could derive a candidate, the person accept
    it, the session write it, and the row parse as no row.

    The warning used to say such a candidate *cannot be written into the row*
    and to offer the command without its pipe. It can be written now, with
    the pipe escaped, so the warning says how — and still says what a bare
    one costs, because that is the spelling somebody types.
    """
    boot = flat(bootstrap())
    warning = boot[boot.index("**A candidate carrying a `|` is written") :]
    warning = warning[: warning.index("**Name the criterion")]
    assert "`run:` step is where one is likeliest to come from" in warning
    assert "with the pipe escaped, `\\|`" in warning, (
        "the warning does not say how the pipe is written, which is the whole "
        "of what changed"
    )
    assert "cannot be written into the row" not in warning, (
        "the sentence #415 removed survived beside its replacement"
    )
    # #871: the table walker refuses a bare pipe, and reads nothing below a
    # line it refuses, whether or not a row parsed above it.
    assert "a bare one is refused" in warning and "cut off at the pipe" in warning
    assert "every row written below it goes unread with it" in warning, (
        "the warning states the row's own cost and not the file's"
    )
    assert "parses as no row" not in warning, (
        "the stop rule's sentence survived beside the walker's"
    )
    assert "where a row above it already parsed" not in warning, (
        "the stop rule's condition on the cost survived the stop rule"
    )


def test_the_question_never_guesses_and_says_so():
    """`Orchestrator: Parity setup` states the rule for the original — *never
    guess* — and the same holds here for the same reason: a row nobody chose
    is what `templates/config.md` argues against by name."""
    row = flat(bootstrap())
    row = row[row.index("The second question") :]
    assert "nothing is guessed" in row
    assert "say so rather than inventing one" in row, (
        "the bootstrap does not say what to do when no candidate is findable"
    )


def test_the_decline_is_offered_and_says_what_it_costs():
    """A question whose every answer must be a command is a gate wearing the
    shape of a question. *Not yet* continues, and what it costs is the thing
    the person is actually choosing between.

    Read from the decline paragraph alone (🟡 7): a slice running to the end
    of the section cannot fail by losing a sentence that has a twin anywhere
    below it.
    """
    decline = paragraph(bootstrap(), "**Offer a decline, and say what it costs.**")
    assert "refuses with nothing run" in decline
    assert "after the review rounds have settled" in decline, (
        "the decline does not say WHEN the refusal arrives, which is the cost"
    )
    assert "/specseal:config" in decline, "the decline names no way back to the row"


def test_the_criterion_is_named_by_pointer_and_not_restated():
    """The criterion has one owner (`tests/test_the_rules_have_one_owner.py`
    rule 12). A bootstrap that spelled the three rules out would be its third
    carrier and the next place for them to disagree."""
    pointer = paragraph(bootstrap(), "**Name the criterion; do not restate it.**")
    assert "*The criterion for choosing a value* owns the criterion" in pointer
    boot = flat(bootstrap())
    assert "red repository-wide" not in boot, (
        "the bootstrap restates a rule instead of pointing at its owner"
    )
    # Round 1's 🟡 3. Rule 3's normative half was restated here — *joined with
    # `&&`, the suite runner first* — which made the criterion's one home
    # three homes, and the ledger fragment's claim that this carrier restates
    # nothing false.
    assert "the suite runner first" not in boot, (
        "the bootstrap states rule 3 beside the pointer to the section that owns it"
    )
    assert "joined with `&&`" not in boot


def test_the_row_is_written_after_seal_mode_and_carries_its_section():
    """`seal mode` writes a config file holding only `Mode`, so the row lands
    afterwards — and it lands the way `/specseal:config` step 3 lands one, the
    row AND its section, because the documentation beside it is the half a
    person reads. No new writer: `skills/config/SKILL.md` *What this does not
    do* refuses a generic setter for a file people edit by hand."""
    boot = flat(bootstrap())
    assert "Then the `Broad gate` row" in boot
    assert boot.index("Then the `Broad gate` row") > boot.index(
        "Then record the answer: run `seal mode`"
    ), "the row is written before the file `seal mode` creates it in"
    assert "$CLAUDE_PLUGIN_ROOT/templates/config.md" in boot
    assert "none is being added" in boot, (
        "nothing says a writer is deliberately not being built for this"
    )
    # Round 1's 🟡 3. *The row and its section* now means 78 lines including
    # the two lists and the criterion table, so every repository bootstrapped
    # after this release would freeze a copy of them — and the next change to
    # either leaves that copy saying something false about the tool.
    assert "the row **and its section**" not in boot, (
        "the bootstrap still copies the whole section, lists and all"
    )
    assert "down to but not including `### What is refused" in boot
    assert "pointed at rather than copied down" in boot


def test_a_decline_leaves_no_trace_and_the_asymmetry_with_the_mode_is_stated():
    """The mode row records its answer because a never-asked repository got
    shared mode SILENTLY (#151). Nothing about this row is silent — a
    repository that declined and one that was never asked meet the same
    refusal and are told the same correct thing — so a trace would separate
    two states nothing treats differently.

    Read from the decline paragraph alone. The mode paragraph of the same
    section argues its own row, so a case reading the whole section cannot
    fail by losing the argument it is named for — which is what round 1's
    🟡 7 measured here. The issue number left the paragraph with #940; the
    argument it stood for is what is pinned.
    """
    decline = paragraph(bootstrap(), "**A decline writes nothing at all.**")
    assert "no sentinel" in decline
    assert "would separate two states nothing treats differently" in decline
    assert "The mode row is the opposite" in decline, (
        "the asymmetry with the mode row is asserted, not argued"
    )


def test_the_sentence_that_said_nowhere_else_is_gone():
    """The 0.4.0 sentence said the root is created at `<repo>/seal/` and
    nowhere else. Both files are read with their whitespace folded, so a
    line break inside the sentence cannot hide it.

    What is refused is that claim, not the two words: `skills/implement/
    SKILL.md` says the closing memo holds what is *nowhere else*, which is
    about something else and stays."""
    assert "`<repo>/seal/` and nowhere else" not in flat(both_halves())


OLD_LAYOUT = "A repository still on the 0.3.x layout"


def test_the_0_3_x_layout_is_sent_to_the_by_hand_path_and_the_bootstrap_goes_on():
    """No code of the plugin opens the 0.3.x layout, so nothing moves it at
    a session start: the bootstrap names README.md's by-hand section in one
    line and continues to the question, and a top-level `specs/` stays the
    project's own."""
    boot = bootstrap()
    told = paragraph(boot, OLD_LAYOUT)
    assert "README.md *Coming up from 0.3.x*" in told, told
    assert "continues" in told, told
    assert "top-level `specs/` is the project's own" in told, told
    assert "the plugin moves it" not in flat(boot), "the bootstrap promises a move"
    assert boot.index(OLD_LAYOUT) < boot.index(RECORDS_ONLY)


OWN_SEAL = "**A `<repo>/seal/` whose `README.md` does not open with the marker"


def test_a_projects_own_seal_gets_nothing_and_the_root_goes_under_the_git_dir():
    """First setup meeting a `seal/` the project keeps for itself writes
    nothing into it, and the orchestrator is told the root goes under the
    git directory in local mode, before the mode's options are offered."""
    boot = bootstrap()
    own = paragraph(boot, OWN_SEAL)
    assert "`templates/seal-README.md`" in own, own
    assert "writes nothing into it" in own, own
    assert f"`{COMMON_DIR}`" in own, own
    assert "local mode" in own, own
    assert boot.index(OWN_SEAL) < boot.index(RECORDS_ONLY)


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
    bootstrap that used to close it is in `orchestration.md` now (#292)."""
    skill = read(*SKILL)
    assert (
        skill.index("## Document layout")
        < skill.index(SESSION_RULE)
        < skill.index("## Procedure")
    )


# --- S5 and S7: what `seal pr-checks install` writes, and local mode --------


def template():
    return read("templates", "hygiene.yml")


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
    assert "MichaelYcJo/SpecSeal" in t
    assert "RUNNER_TEMP" in t or "runner.temp" in t, "the plugin lands in the tree"


@pytest.mark.parametrize(
    "stays_home", ["plugin.json", "gather_changelog", "fold_ledger", "README.ko.md"]
)
def test_the_rows_that_read_this_repository_do_not_travel(stays_home):
    assert stays_home not in template()


def test_the_template_header_says_who_writes_it_and_what_local_mode_does_to_it():
    """#952: `seal pr-checks install` writes the file and refuses in local
    mode, and a copy left after a switch to local examines nothing and
    passes, which phase 1 made true of every step."""
    header = flat(
        "\n".join(
            line
            for line in template().split("\nname:", 1)[0].splitlines()
            if line.startswith("#")
        )
    )
    assert "`seal pr-checks install` writes" in header, header
    assert "refuses in local mode" in header, header
    assert "examines nothing and passes" in header, header
    assert "`seal pr-checks remove`" in header, header
    assert "red forever" not in header, header


def test_the_skill_writes_the_workflow_only_when_absent_and_local_installs_nothing():
    """The orchestrator runs the command rather than writing the file, so
    the file has one writer (#952)."""
    boot = flat(bootstrap())
    assert "templates/hygiene.yml" in boot
    assert ".github/workflows/hygiene.yml" in boot
    assert "only when" in boot and "absent" in boot
    assert "never overwritten" in boot
    assert "installs nothing" in boot
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
    assert "`git reset -- :/seal`" in body and "reset -- :/seal :/" not in body
    for sentence in LEFT_BEHIND[readme]:
        assert sentence in flat(body), sentence
    assert "seal export" in body and "seal import" in body, (
        "the move is only available where both folders are on one machine, so "
        "this section has to point at the pair that works between two (#81). "
        "It named the issue number while the pair was later work"
    )


COMMON = "$(git rev-parse --git-common-dir)/seal"
TOP = "$(git rev-parse --show-toplevel)/seal"


def switch_block(readme):
    """The BY-HAND `bash` block under the README's switch section, comments
    off: two lines, local → shared and then shared → local.

    Bounded at the next `## ` heading and asserted to be there, the way
    `test_the_root_migrates_itself.by_hand_block` reads the coming-up block:
    the lines are run under `bash -c`, so a block that left its section must
    fail here rather than let a later block run in its place.

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
    executed, not assumed (`shell_probe`, for the reason the coming-up test
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
    rows = [
        line
        for line in read(readme).splitlines()
        if line.startswith("| ") and "`seal/`" in line.rsplit("|", 2)[-2]
    ]
    assert rows, f"{readme}: no gate row's Where cell names `seal/`"
    for row in rows:
        where = row.rsplit("|", 2)[-2]
        assert "local" in where, f"{readme}: {row[:40]}… still says the root only"


# --- S14: the root's own README, and the template it is rendered from ------


@pytest.mark.parametrize(
    "parts", [("seal", "README.md"), ("templates", "seal-README.md")]
)
def test_the_seal_readme_names_both_places(parts):
    text = read(*parts)
    assert "git rev-parse --git-common-dir" in text, "/".join(parts)
    assert "local" in text and "shared" in text, "/".join(parts)
    assert "either" in text, "/".join(parts)


def test_the_seal_readme_is_the_template_verbatim():
    assert read("seal", "README.md") == read("templates", "seal-README.md")


MARKER_SAID = "**The first line of this file is the marker.**"


def test_the_seal_readme_says_its_first_line_is_the_marker():
    """The root's own README tells a person not to edit the line the gates
    read, and what a `seal/` without it is; the 0.3.x paragraph it replaced
    is gone."""
    text = read("templates", "seal-README.md")
    said = paragraph(text, MARKER_SAID)
    assert "`hooks/optin.py#MARKER`" in said, said
    assert "never opted in" in said, said
    assert "writes nothing into it" in said, said
    assert "`.specseal/`" not in text


def test_the_seal_readme_points_at_the_drain_and_restates_none_of_it():
    """Round 2 of #940, finding 2. Who moves a work item's open rows, when
    and where each goes is `skills/implement/SKILL.md` section 6's alone; a
    second statement here drifted from it on all three. The README names the
    section and carries no destination of its own."""
    text = read("templates", "seal-README.md")
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
    "parts, opt_in, setup, stamp",
    [
        (
            ("docs", "one-root-by-lifetime.md"),
            "## The opt-in signal is the root itself",
            "## What first setup asks",
            "that hook stamps the repository as moved",
        ),
        (
            ("docs", "one-root-by-lifetime.ko.md"),
            "## 옵트인 신호는 루트 자체다",
            "## 처음 설정에서 무엇을 묻는가",
            "그 훅은 저장소에 옮겼다는 표시를 남기므로",
        ),
    ],
)
def test_the_design_record_states_the_setup_rules_where_they_rule(
    parts, opt_in, setup, stamp
):
    """The opt-out sits with the opt-in it takes back, and the question's
    shape, the workflow it installs and the migration hook's stamp sit with
    first setup, in both editions."""
    text = read(*parts)
    assert "agentic-scratch" in section(text, opt_in, 2), "/".join(parts)
    body = " ".join(section(text, setup, 2).split())
    for needle in ("templates/hygiene.yml", COMMON_DIR, "AskUserQuestion", stamp):
        assert needle in body, f"{'/'.join(parts)}: {setup} does not name {needle}"


# --- #151: the route that actually happens, and the state it leaves ---------
#
# The bootstrap above is where the mode question lives, and the cases in this
# file all reach it by reading the skill. That is not how a session gets
# there. `install.sh` copies the block between `<!-- specseal:start -->` and
# `<!-- specseal:end -->` — `templates/claude-md-block.md`, the block's one
# source — into `~/.claude/CLAUDE.md`, so the block loads in EVERY project on
# the machine —
# including one that has never seen SpecSeal —
# and it tells a session to write `seal/specs/<id>/routing.md` before the
# first edit. That write creates `seal/`. Creating `seal/` opts the repository
# in. Every case above passed while that route existed, because none of them
# read the preset block.
#
# Each case here was written against the block as it stood at 589cf25, before
# it was edited, and each failed; the output is in the body of the commit that
# added them.

START, END = "<!-- specseal:start -->", "<!-- specseal:end -->"


def preset():
    """Exactly the text `install.sh` copies, markers included.

    Read from `templates/claude-md-block.md`, the installer's source, and
    extracted the way the installer extracts it rather than by reading the
    whole file: a line outside the markers reaches no user, and a case that
    read the whole file could not tell the two apart.
    """
    text = read("templates", "claude-md-block.md")
    assert START in text and END in text, "the preset markers moved"
    return text[text.index(START) : text.index(END) + len(END)]


def routing_rule():
    """The preset's routing bullet, its line breaks folded."""
    return paragraph(preset(), "- **Routing, decided at the start.**")


def test_the_preset_sends_a_fresh_repository_to_the_bootstrap():
    """S11. The instruction that creates the root has to name the question
    first. #151's own reading of the cheap fix is that a conditional put into
    a block meant to be read straight through only helps a session that
    notices the condition applies — so the condition leads the rule rather
    than trailing it."""
    rule = routing_rule()
    lead = rule[: rule.index("write `seal/threads/")]
    assert "Bootstrap" in lead, (
        "the routing rule instructs the write before it names the bootstrap, "
        "which is the order that made #151 happen"
    )
    # The file the Bootstrap moved to, not the skill a `Skill implement` load
    # carries, which no longer holds it.
    assert "skills/implement/orchestration.md" in lead
    assert "neither" in lead, "the rule does not say WHICH repositories it means"
    # A project's own `seal/` is no root, so a repository holding only that
    # one is sent to the bootstrap too.
    assert "its `README.md` opening with the marker" in lead, lead


def test_the_preset_writes_no_declaration_under_no_work_item():
    """Round 1 of #940, finding 1. The write is conditioned on the answer,
    and the block names the file that states question 1 and the boxes, so a
    session in a rooted repository that reads only the block neither writes
    a declaration nobody gave nor asks a question it has no text for."""
    rule = routing_rule()
    lead = rule[: rule.index("write `seal/threads/")]
    assert "Except under `no work item`" in lead, (
        "the routing rule writes routing.md under every answer, `no work item` included"
    )
    assert "*Orchestrator: how the work is routed*" in lead, (
        "the routing rule names question 1 and the boxes without naming the "
        "section that states them"
    )


def test_the_preset_names_both_places_the_root_can_be():
    """A session cannot tell a fresh repository from an opted-in one without
    both. `<repo>/seal/` alone reads every local-mode repository as fresh, and
    sends it back through a question it already answered."""
    lead = routing_rule()
    assert "`<repo>/seal/`" in lead
    assert "git rev-parse --git-common-dir" in lead


def test_the_preset_says_whose_decision_the_place_is():
    """The block keeps the rule and leaves the reason (#940): where the root
    lands is the user's decision. That the write creates the root and opts
    the repository in is the Bootstrap's, which the same sentence sends a
    session to first."""
    rule = routing_rule()
    assert "Creating the root is what opts the repository in" in flat(bootstrap()), (
        "the Bootstrap no longer says creating the root opts the repository in"
    )
    assert "user's decision" in rule, (
        "the rule does not say whose decision the place is, which is the "
        "whole of what #151 lost"
    )


def test_what_the_installer_copies_carries_it():
    """S12. The block is copied by `install.sh` with `awk` between the two
    markers, so a sentence outside them ships to nobody. This reads the same
    span the installer reads."""
    assert "Bootstrap" in preset()


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
